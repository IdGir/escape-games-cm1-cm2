"""Base de données SQLite : classes, élèves, textes, séances de correction, séances de fluence."""
import sqlite3, json, datetime
from paths import chemin_base

VERSION_SCHEMA = 2


def _connexion():
    cx = sqlite3.connect(str(chemin_base()))
    cx.row_factory = sqlite3.Row
    cx.execute("PRAGMA foreign_keys = ON")
    return cx


def maintenant():
    return datetime.datetime.now().isoformat(timespec="seconds")


SCHEMA = """
CREATE TABLE IF NOT EXISTS meta (
    cle TEXT PRIMARY KEY, valeur TEXT
);

CREATE TABLE IF NOT EXISTS classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL UNIQUE,
    niveau TEXT DEFAULT 'CM1',
    annee TEXT DEFAULT ''
);

CREATE TABLE IF NOT EXISTS eleves (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prenom TEXT NOT NULL,
    nom TEXT DEFAULT '',
    classe_id INTEGER NOT NULL REFERENCES classes(id) ON DELETE CASCADE,
    archive INTEGER DEFAULT 0
);

-- Banque de textes du module 1 (textes à corriger imposés par l'enseignant)
CREATE TABLE IF NOT EXISTS textes_correction (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    contenu TEXT NOT NULL,
    niveau INTEGER DEFAULT 2,
    actif INTEGER DEFAULT 1,
    corrige TEXT DEFAULT '',          -- version corrigée facultative
    cree_le TEXT
);

-- Banque de textes du module 2 (fluence, 5 niveaux)
CREATE TABLE IF NOT EXISTS textes_fluence (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    contenu TEXT NOT NULL,
    niveau INTEGER NOT NULL DEFAULT 1,
    nb_mots INTEGER DEFAULT 0,
    actif INTEGER DEFAULT 1,
    cree_le TEXT
);

-- Une séance d'autocorrection (module 1)
CREATE TABLE IF NOT EXISTS seances_correction (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    eleve_id INTEGER NOT NULL REFERENCES eleves(id) ON DELETE CASCADE,
    origine TEXT NOT NULL,            -- 'saisie' | 'impose' | 'ia'
    texte_id INTEGER,                 -- si origine = 'impose'
    texte_initial TEXT NOT NULL,
    texte_reference TEXT DEFAULT '',   -- corrigé connu (texte généré ou imposé)
    texte_final TEXT DEFAULT '',
    nb_mots INTEGER DEFAULT 0,
    nb_phrases INTEGER DEFAULT 0,
    erreurs_avant INTEGER DEFAULT 0,
    erreurs_apres INTEGER DEFAULT 0,
    corrigees_seul INTEGER DEFAULT 0,     -- corrigées à l'étape 1 (repérage seul)
    corrigees_avec_aide INTEGER DEFAULT 0,-- corrigées après consultation des outils
    detail_avant TEXT DEFAULT '{}',       -- JSON {categorie: nb}
    detail_apres TEXT DEFAULT '{}',
    duree_secondes INTEGER DEFAULT 0,
    etape_atteinte INTEGER DEFAULT 1,
    terminee INTEGER DEFAULT 0,
    exportee INTEGER DEFAULT 0,
    date_seance TEXT
);

-- Une séance de fluence (module 2)
CREATE TABLE IF NOT EXISTS seances_fluence (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    eleve_id INTEGER NOT NULL REFERENCES eleves(id) ON DELETE CASCADE,
    texte_id INTEGER REFERENCES textes_fluence(id) ON DELETE SET NULL,
    titre_texte TEXT DEFAULT '',
    niveau INTEGER DEFAULT 1,
    nb_mots_texte INTEGER DEFAULT 0,
    mots_lus INTEGER DEFAULT 0,       -- si lecture non terminée, mots effectivement lus
    erreurs INTEGER DEFAULT 0,
    duree_secondes REAL DEFAULT 0,
    mclm REAL DEFAULT 0,
    saisi_par TEXT DEFAULT 'eleve',   -- 'eleve' | 'enseignant'
    exportee INTEGER DEFAULT 0,
    date_seance TEXT
);

-- Journal des envois vers Notes & Suivi (traçabilité RGPD)
CREATE TABLE IF NOT EXISTS journal_integration (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    action TEXT, details TEXT, date_action TEXT
);

-- Devoirs : un texte de correction assigné à une classe ou à un élève (Phase I)
CREATE TABLE IF NOT EXISTS assignations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    texte_id INTEGER NOT NULL REFERENCES textes_correction(id) ON DELETE CASCADE,
    classe_id INTEGER REFERENCES classes(id) ON DELETE CASCADE,
    eleve_id INTEGER REFERENCES eleves(id) ON DELETE CASCADE,
    consigne TEXT DEFAULT '',
    cree_le TEXT
);

-- Banque lexicale personnelle : les mots que CET élève rate, pas une liste
-- générique. Alimentée automatiquement à chaque bilan de correction (Phase J).
CREATE TABLE IF NOT EXISTS mots_a_travailler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    eleve_id INTEGER NOT NULL REFERENCES eleves(id) ON DELETE CASCADE,
    mot TEXT NOT NULL,
    categorie TEXT NOT NULL,
    nb_fois INTEGER DEFAULT 1,
    maitrise INTEGER DEFAULT 0,       -- 1 = l'élève l'a marqué comme su
    derniere_date TEXT,
    UNIQUE(eleve_id, mot, categorie)
);
"""


# ============================================================================
#  MIGRATIONS
#
#  Règle absolue : l'enseignant ne doit JAMAIS avoir à supprimer sa base.
#  Toute évolution du schéma passe par une migration idempotente, appliquée
#  au démarrage. On vérifie l'existence de chaque colonne avant de l'ajouter.
# ============================================================================
def _colonnes(cx, table):
    return {r["name"] for r in cx.execute(f"PRAGMA table_info({table})").fetchall()}


def _ajouter_colonne(cx, table, colonne, definition):
    """Ajoute une colonne si elle manque. Sans effet si elle est déjà là."""
    if colonne not in _colonnes(cx, table):
        cx.execute(f"ALTER TABLE {table} ADD COLUMN {colonne} {definition}")
        return True
    return False


# Chaque migration est (version_cible, description, fonction).
def _migration_2(cx):
    """v2 : mémorisation du corrigé de référence d'une séance."""
    _ajouter_colonne(cx, "seances_correction", "texte_reference", "TEXT DEFAULT ''")
    _ajouter_colonne(cx, "textes_correction", "corrige", "TEXT DEFAULT ''")


def _migration_3(cx):
    """v3 : nombre d'aides consultées (question/indice) pendant la séance.

    Sert à tenir compte de l'aide apportée dans l'évaluation de l'autonomie.
    """
    _ajouter_colonne(cx, "seances_correction", "nb_aides", "INTEGER DEFAULT 0")


def _migration_4(cx):
    """v4 : dictionnaire par consonance — définitions mémorisées et recherches.

    Les définitions obtenues une fois ne sont jamais redemandées : la classe
    se constitue ainsi son propre dictionnaire, qui marche ensuite hors ligne.
    Les recherches sont tracées : savoir quels mots les élèves cherchent est
    une information précieuse pour l'enseignant.
    """
    cx.executescript("""
        CREATE TABLE IF NOT EXISTS definitions (
            mot          TEXT PRIMARY KEY,
            nature       TEXT DEFAULT '',
            definition   TEXT NOT NULL,
            source       TEXT DEFAULT '',
            date_ajout   TEXT
        );
        CREATE TABLE IF NOT EXISTS recherches_dico (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            eleve_id     INTEGER,
            essai        TEXT NOT NULL,
            mot_retenu   TEXT DEFAULT '',
            trouve       INTEGER DEFAULT 0,
            depuis       TEXT DEFAULT 'dictionnaire',
            date_recherche TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_rech_eleve ON recherches_dico(eleve_id);
    """)


def _migration_5(cx):
    """v5 : dictée adaptée — séances et détail mot par mot."""
    cx.executescript("""
        CREATE TABLE IF NOT EXISTS seances_dictee (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            eleve_id       INTEGER NOT NULL,
            nb_mots        INTEGER DEFAULT 0,
            nb_justes      INTEGER DEFAULT 0,
            score          INTEGER DEFAULT 0,
            err_orthographe INTEGER DEFAULT 0,
            err_ecoute     INTEGER DEFAULT 0,
            err_accent     INTEGER DEFAULT 0,
            detail         TEXT DEFAULT '[]',
            duree_secondes INTEGER DEFAULT 0,
            date_seance    TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_dictee_eleve ON seances_dictee(eleve_id);
    """)


def _migration_6(cx):
    """v6 : activités à faire, proposées par l'analyse et validées par le maître."""
    cx.executescript("""
        CREATE TABLE IF NOT EXISTS activites_assignees (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            eleve_id    INTEGER NOT NULL,
            genre       TEXT NOT NULL,
            categorie   TEXT DEFAULT '',
            lecon_id    TEXT DEFAULT '',
            texte_id    INTEGER,
            consigne    TEXT DEFAULT '',
            terminee    INTEGER DEFAULT 0,
            date_ajout  TEXT,
            date_fin    TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_act_eleve ON activites_assignees(eleve_id);
    """)


def _migration_7(cx):
    """v7 : modes de dictée, niveaux, objectif personnel de l'élève."""
    _ajouter_colonne(cx, "seances_dictee", "genre", "TEXT DEFAULT 'mots'")
    _ajouter_colonne(cx, "seances_dictee", "niveau", "INTEGER DEFAULT 2")
    cx.executescript("""
        CREATE TABLE IF NOT EXISTS objectifs_eleve (
            eleve_id     INTEGER PRIMARY KEY,
            mclm_vise    INTEGER DEFAULT 0,
            dictee_visee INTEGER DEFAULT 0,
            date_maj     TEXT
        );
    """)


def _migration_8(cx):
    """v8 : banque de dictées — mots, expressions et phrases prêts à dicter."""
    cx.executescript("""
        CREATE TABLE IF NOT EXISTS banque_dictee (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            genre      TEXT NOT NULL,          -- mots | expressions | phrases
            contenu    TEXT NOT NULL,
            niveau     INTEGER DEFAULT 2,
            categorie  TEXT DEFAULT '',
            source     TEXT DEFAULT '',
            actif      INTEGER DEFAULT 1,
            cree_le    TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_bd_genre ON banque_dictee(genre, niveau);
        CREATE UNIQUE INDEX IF NOT EXISTS idx_bd_unique
            ON banque_dictee(genre, contenu);
    """)


MIGRATIONS = [
    (2, "Corrigé de référence des séances et des textes", _migration_2),
    (3, "Comptage des aides consultées par l'élève", _migration_3),
    (4, "Dictionnaire par consonance : définitions et recherches", _migration_4),
    (5, "Dictée adaptée : séances et détail des mots", _migration_5),
    (6, "Activités à faire proposées par l'analyse", _migration_6),
    (7, "Modes de dictée, niveaux et objectifs personnels", _migration_7),
    (8, "Banque de dictées : mots, expressions et phrases", _migration_8),
]


def version_base(cx) -> int:
    try:
        r = cx.execute("SELECT valeur FROM meta WHERE cle='version'").fetchone()
        return int(r["valeur"]) if r else 0
    except Exception:
        return 0


def initialiser():
    """Crée la base si besoin, puis applique les migrations manquantes."""
    cx = _connexion()
    cx.executescript(SCHEMA)          # CREATE TABLE IF NOT EXISTS : sans danger
    cx.execute("INSERT OR IGNORE INTO meta(cle, valeur) VALUES ('version', '1')")
    cx.commit()

    actuelle = version_base(cx)
    appliquees = []
    for cible, description, fn in MIGRATIONS:
        if actuelle < cible:
            fn(cx)
            cx.execute("UPDATE meta SET valeur=? WHERE cle='version'", (str(cible),))
            cx.commit()
            appliquees.append(f"v{cible} — {description}")
            actuelle = cible

    if appliquees:
        for m in appliquees:
            try:
                cx.execute(
                    "INSERT INTO journal_integration(action, details, date_action) "
                    "VALUES (?,?,?)", ("migration", m, maintenant()))
            except Exception:
                pass
        cx.commit()
    cx.close()
    return appliquees


# ---------------------------------------------------------------- Classes / élèves
def liste_classes():
    cx = _connexion()
    r = cx.execute("SELECT * FROM classes ORDER BY nom").fetchall()
    cx.close()
    return [dict(x) for x in r]


def liste_eleves(classe_id=None, inclure_archives=False):
    cx = _connexion()
    q = ("SELECT e.*, c.nom AS classe_nom, c.niveau AS classe_niveau "
         "FROM eleves e JOIN classes c ON c.id = e.classe_id WHERE 1=1")
    p = []
    if classe_id:
        q += " AND e.classe_id = ?"
        p.append(classe_id)
    if not inclure_archives:
        q += " AND e.archive = 0"
    q += " ORDER BY e.prenom, e.nom"
    r = cx.execute(q, p).fetchall()
    cx.close()
    return [dict(x) for x in r]


def ajouter_classe(nom, niveau="CM1", annee=""):
    cx = _connexion()
    try:
        cur = cx.execute("INSERT INTO classes(nom, niveau, annee) VALUES (?,?,?)",
                         (nom.strip(), niveau, annee))
        cx.commit()
        return cur.lastrowid
    except sqlite3.IntegrityError:
        r = cx.execute("SELECT id FROM classes WHERE nom = ?", (nom.strip(),)).fetchone()
        return r["id"] if r else None
    finally:
        cx.close()


def maj_classe(cid, nom, niveau):
    cx = _connexion()
    cx.execute("UPDATE classes SET nom=?, niveau=? WHERE id=?", (nom, niveau, cid))
    cx.commit(); cx.close()


def supprimer_classe(cid):
    cx = _connexion()
    cx.execute("DELETE FROM classes WHERE id=?", (cid,))
    cx.commit(); cx.close()


def ajouter_eleve(prenom, nom, classe_id):
    cx = _connexion()
    cur = cx.execute("INSERT INTO eleves(prenom, nom, classe_id) VALUES (?,?,?)",
                     (prenom.strip(), nom.strip(), classe_id))
    cx.commit(); rid = cur.lastrowid; cx.close()
    return rid


def maj_eleve(eid, prenom, nom, classe_id):
    cx = _connexion()
    cx.execute("UPDATE eleves SET prenom=?, nom=?, classe_id=? WHERE id=?",
               (prenom, nom, classe_id, eid))
    cx.commit(); cx.close()


def supprimer_eleve(eid):
    cx = _connexion()
    cx.execute("DELETE FROM eleves WHERE id=?", (eid,))
    cx.commit(); cx.close()


# ---------------------------------------------------------------- Textes
def liste_textes_correction(actifs_seulement=True):
    cx = _connexion()
    q = "SELECT * FROM textes_correction"
    if actifs_seulement:
        q += " WHERE actif = 1"
    q += " ORDER BY niveau, titre"
    r = cx.execute(q).fetchall(); cx.close()
    return [dict(x) for x in r]


def ajouter_texte_correction(titre, contenu, niveau=2, corrige=""):
    cx = _connexion()
    cur = cx.execute(
        "INSERT INTO textes_correction(titre, contenu, niveau, corrige, cree_le) VALUES (?,?,?,?,?)",
        (titre, contenu, niveau, corrige, maintenant()))
    cx.commit(); rid = cur.lastrowid; cx.close()
    return rid


def supprimer_texte_correction(tid):
    cx = _connexion()
    cx.execute("DELETE FROM textes_correction WHERE id=?", (tid,))
    cx.commit(); cx.close()


def definir_corrige_texte(tid, corrige):
    """Complète (ou remplace) le corrigé d'un texte existant."""
    cx = _connexion()
    cx.execute("UPDATE textes_correction SET corrige=? WHERE id=?", (corrige, tid))
    cx.commit(); cx.close()


def liste_textes_fluence(niveau=None, actifs_seulement=True):
    cx = _connexion()
    q = "SELECT * FROM textes_fluence WHERE 1=1"
    p = []
    if actifs_seulement:
        q += " AND actif = 1"
    if niveau:
        q += " AND niveau = ?"
        p.append(niveau)
    q += " ORDER BY niveau, titre"
    r = cx.execute(q, p).fetchall(); cx.close()
    return [dict(x) for x in r]


def ajouter_texte_fluence(titre, contenu, niveau):
    nb = len([m for m in contenu.split() if any(c.isalnum() for c in m)])
    cx = _connexion()
    cur = cx.execute(
        "INSERT INTO textes_fluence(titre, contenu, niveau, nb_mots, cree_le) VALUES (?,?,?,?,?)",
        (titre, contenu, niveau, nb, maintenant()))
    cx.commit(); rid = cur.lastrowid; cx.close()
    return rid


def supprimer_texte_fluence(tid):
    cx = _connexion()
    cx.execute("DELETE FROM textes_fluence WHERE id=?", (tid,))
    cx.commit(); cx.close()


# ---------------------------------------------------------------- Séances
def enregistrer_mots_travailler(eleve_id: int, mots: list) -> None:
    """Alimente la banque lexicale personnelle de l'élève.

    `mots` : liste de {"mot": str, "categorie": str} restés en erreur à la fin
    d'une séance. Incrémente le compteur si le mot est déjà connu pour cet
    élève ; le fait réapparaître comme "à retravailler" s'il avait été marqué
    maîtrisé puis re-raté.
    """
    if not mots:
        return
    cx = _connexion()
    for m in mots:
        mot = (m.get("mot") or "").strip().lower()
        cat = (m.get("categorie") or "").strip()
        if not mot or not cat:
            continue
        cx.execute("""
            INSERT INTO mots_a_travailler (eleve_id, mot, categorie, nb_fois, maitrise, derniere_date)
            VALUES (?,?,?,1,0,?)
            ON CONFLICT(eleve_id, mot, categorie) DO UPDATE SET
                nb_fois = nb_fois + 1, maitrise = 0, derniere_date = excluded.derniere_date
        """, (eleve_id, mot, cat, maintenant()))
    cx.commit(); cx.close()


def banque_lexicale(eleve_id: int, inclure_maitrises=False) -> list:
    cx = _connexion()
    clause = "" if inclure_maitrises else "AND maitrise = 0"
    rows = cx.execute(f"""
        SELECT mot, categorie, nb_fois, maitrise, derniere_date
        FROM mots_a_travailler
        WHERE eleve_id = ? {clause}
        ORDER BY maitrise ASC, nb_fois DESC, derniere_date DESC
    """, (eleve_id,)).fetchall()
    cx.close()
    return [dict(r) for r in rows]


def marquer_mot_maitrise(eleve_id: int, mot: str, categorie: str, maitrise: bool) -> None:
    cx = _connexion()
    cx.execute("""
        UPDATE mots_a_travailler SET maitrise = ?
        WHERE eleve_id = ? AND mot = ? AND categorie = ?
    """, (1 if maitrise else 0, eleve_id, mot.strip().lower(), categorie))
    cx.commit(); cx.close()


def enregistrer_seance_correction(d: dict) -> int:
    cx = _connexion()
    cur = cx.execute("""
        INSERT INTO seances_correction
        (eleve_id, origine, texte_id, texte_initial, texte_reference, texte_final,
         nb_mots, nb_phrases,
         erreurs_avant, erreurs_apres, corrigees_seul, corrigees_avec_aide,
         detail_avant, detail_apres, duree_secondes, etape_atteinte, terminee,
         nb_aides, date_seance)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (
        d["eleve_id"], d["origine"], d.get("texte_id"), d["texte_initial"],
        d.get("texte_reference", ""),
        d.get("texte_final", ""), d.get("nb_mots", 0), d.get("nb_phrases", 0),
        d.get("erreurs_avant", 0), d.get("erreurs_apres", 0),
        d.get("corrigees_seul", 0), d.get("corrigees_avec_aide", 0),
        json.dumps(d.get("detail_avant", {}), ensure_ascii=False),
        json.dumps(d.get("detail_apres", {}), ensure_ascii=False),
        d.get("duree_secondes", 0), d.get("etape_atteinte", 1),
        d.get("terminee", 0), d.get("nb_aides", 0), maintenant()))
    cx.commit(); rid = cur.lastrowid; cx.close()
    return rid


def enregistrer_seance_fluence(d: dict) -> int:
    cx = _connexion()
    cur = cx.execute("""
        INSERT INTO seances_fluence
        (eleve_id, texte_id, titre_texte, niveau, nb_mots_texte, mots_lus, erreurs,
         duree_secondes, mclm, saisi_par, date_seance)
        VALUES (?,?,?,?,?,?,?,?,?,?,?)
    """, (d["eleve_id"], d.get("texte_id"), d.get("titre_texte", ""), d.get("niveau", 1),
          d.get("nb_mots_texte", 0), d.get("mots_lus", 0), d.get("erreurs", 0),
          d.get("duree_secondes", 0), d.get("mclm", 0),
          d.get("saisi_par", "eleve"), maintenant()))
    cx.commit(); rid = cur.lastrowid; cx.close()
    return rid


def seances_correction(eleve_id=None, classe_id=None, limite=None):
    cx = _connexion()
    q = ("SELECT s.*, e.prenom, e.nom, e.classe_id, c.nom AS classe_nom "
         "FROM seances_correction s JOIN eleves e ON e.id = s.eleve_id "
         "JOIN classes c ON c.id = e.classe_id WHERE 1=1")
    p = []
    if eleve_id:
        q += " AND s.eleve_id = ?"; p.append(eleve_id)
    if classe_id:
        q += " AND e.classe_id = ?"; p.append(classe_id)
    q += " ORDER BY s.date_seance DESC"
    if limite:
        q += f" LIMIT {int(limite)}"
    r = cx.execute(q, p).fetchall(); cx.close()
    out = []
    for x in r:
        d = dict(x)
        d["detail_avant"] = json.loads(d.get("detail_avant") or "{}")
        d["detail_apres"] = json.loads(d.get("detail_apres") or "{}")
        out.append(d)
    return out


def seances_fluence(eleve_id=None, classe_id=None, limite=None):
    cx = _connexion()
    q = ("SELECT s.*, e.prenom, e.nom, e.classe_id, c.nom AS classe_nom, c.niveau AS classe_niveau "
         "FROM seances_fluence s JOIN eleves e ON e.id = s.eleve_id "
         "JOIN classes c ON c.id = e.classe_id WHERE 1=1")
    p = []
    if eleve_id:
        q += " AND s.eleve_id = ?"; p.append(eleve_id)
    if classe_id:
        q += " AND e.classe_id = ?"; p.append(classe_id)
    q += " ORDER BY s.date_seance DESC"
    if limite:
        q += f" LIMIT {int(limite)}"
    r = cx.execute(q, p).fetchall(); cx.close()
    return [dict(x) for x in r]


# ---------------------------------------------------- Dictionnaire (phase J5)
def definition_memorisee(mot):
    cx = _connexion()
    r = cx.execute("SELECT * FROM definitions WHERE mot = ?",
                   ((mot or "").strip().lower(),)).fetchone()
    cx.close()
    return dict(r) if r else None


def memoriser_definition(mot, definition, nature="", source="ia"):
    """Une définition obtenue une fois ne sera jamais redemandée."""
    cx = _connexion()
    cx.execute("""INSERT INTO definitions(mot, nature, definition, source, date_ajout)
                  VALUES (?,?,?,?,?)
                  ON CONFLICT(mot) DO UPDATE SET
                    definition = excluded.definition,
                    nature     = excluded.nature,
                    source     = excluded.source""",
               ((mot or "").strip().lower(), nature, definition, source, maintenant()))
    cx.commit(); cx.close()


def nb_definitions_memorisees():
    cx = _connexion()
    n = cx.execute("SELECT COUNT(*) AS n FROM definitions").fetchone()["n"]
    cx.close()
    return n


def journaliser_recherche(eleve_id, essai, mot_retenu="", trouve=0,
                          depuis="dictionnaire"):
    cx = _connexion()
    cx.execute("""INSERT INTO recherches_dico
                  (eleve_id, essai, mot_retenu, trouve, depuis, date_recherche)
                  VALUES (?,?,?,?,?,?)""",
               (eleve_id, (essai or "").strip().lower(),
                (mot_retenu or "").strip().lower(), int(bool(trouve)),
                depuis, maintenant()))
    cx.commit(); cx.close()


def recherches_dico(eleve_id=None, classe_id=None, limite=400):
    cx = _connexion()
    q = ("SELECT r.*, e.prenom, e.classe_id, c.nom AS classe_nom "
         "FROM recherches_dico r LEFT JOIN eleves e ON e.id = r.eleve_id "
         "LEFT JOIN classes c ON c.id = e.classe_id WHERE 1=1")
    p = []
    if eleve_id:
        q += " AND r.eleve_id = ?"; p.append(eleve_id)
    if classe_id:
        q += " AND e.classe_id = ?"; p.append(classe_id)
    q += f" ORDER BY r.date_recherche DESC LIMIT {int(limite)}"
    r = cx.execute(q, p).fetchall(); cx.close()
    return [dict(x) for x in r]


# ---------------------------------------------------------- Dictée (phase J6)
def enregistrer_seance_dictee(d: dict) -> int:
    cx = _connexion()
    cur = cx.execute("""
        INSERT INTO seances_dictee
        (eleve_id, nb_mots, nb_justes, score, err_orthographe, err_ecoute,
         err_accent, detail, duree_secondes, genre, niveau, date_seance)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
    """, (d["eleve_id"], d.get("nb_mots", 0), d.get("nb_justes", 0),
          d.get("score", 0), d.get("err_orthographe", 0), d.get("err_ecoute", 0),
          d.get("err_accent", 0),
          json.dumps(d.get("detail", []), ensure_ascii=False),
          d.get("duree_secondes", 0), d.get("genre", "mots"),
          d.get("niveau", 2), maintenant()))
    cx.commit(); rid = cur.lastrowid; cx.close()
    return rid


# ------------------------------------------------- Banque de dictées (v8)
def ajouter_banque_dictee(genre, contenu, niveau=2, categorie="", source="ia"):
    """Ajoute un élément. Les doublons sont ignorés sans faire d'histoire."""
    contenu = (contenu or "").strip()
    if not contenu:
        return 0
    cx = _connexion()
    try:
        cur = cx.execute("""INSERT OR IGNORE INTO banque_dictee
            (genre, contenu, niveau, categorie, source, cree_le)
            VALUES (?,?,?,?,?,?)""",
            (genre, contenu, int(niveau), categorie, source, maintenant()))
        cx.commit()
        return cur.rowcount
    finally:
        cx.close()


def banque_dictee(genre=None, niveau=None, actifs_seulement=True):
    cx = _connexion()
    q, p = "SELECT * FROM banque_dictee WHERE 1=1", []
    if genre:
        q += " AND genre = ?"; p.append(genre)
    if niveau:
        q += " AND niveau = ?"; p.append(int(niveau))
    if actifs_seulement:
        q += " AND actif = 1"
    q += " ORDER BY niveau, id"
    r = cx.execute(q, p).fetchall(); cx.close()
    return [dict(x) for x in r]


def compter_banque_dictee():
    cx = _connexion()
    r = cx.execute("""SELECT genre, niveau, COUNT(*) AS n FROM banque_dictee
                      WHERE actif = 1 GROUP BY genre, niveau""").fetchall()
    cx.close()
    out = {}
    for x in r:
        out.setdefault(x["genre"], {})[str(x["niveau"])] = x["n"]
    return out


def supprimer_banque_dictee(bid):
    cx = _connexion()
    cx.execute("DELETE FROM banque_dictee WHERE id=?", (bid,))
    cx.commit(); cx.close()


def objectif_eleve(eleve_id):
    cx = _connexion()
    r = cx.execute("SELECT * FROM objectifs_eleve WHERE eleve_id=?",
                   (eleve_id,)).fetchone()
    cx.close()
    return dict(r) if r else {"eleve_id": eleve_id, "mclm_vise": 0,
                              "dictee_visee": 0}


def definir_objectif(eleve_id, mclm=None, dictee=None):
    """L'élève choisit lui-même de viser plus haut : c'est son objectif."""
    actuel = objectif_eleve(eleve_id)
    m = int(mclm) if mclm is not None else actuel.get("mclm_vise", 0)
    d = int(dictee) if dictee is not None else actuel.get("dictee_visee", 0)
    cx = _connexion()
    cx.execute("""INSERT INTO objectifs_eleve(eleve_id, mclm_vise, dictee_visee, date_maj)
                  VALUES (?,?,?,?)
                  ON CONFLICT(eleve_id) DO UPDATE SET
                    mclm_vise=excluded.mclm_vise,
                    dictee_visee=excluded.dictee_visee,
                    date_maj=excluded.date_maj""",
               (eleve_id, m, d, maintenant()))
    cx.commit(); cx.close()


def seances_dictee(eleve_id=None, classe_id=None, limite=None):
    cx = _connexion()
    q = ("SELECT s.*, e.prenom, e.classe_id, c.nom AS classe_nom "
         "FROM seances_dictee s JOIN eleves e ON e.id = s.eleve_id "
         "JOIN classes c ON c.id = e.classe_id WHERE 1=1")
    p = []
    if eleve_id:
        q += " AND s.eleve_id = ?"; p.append(eleve_id)
    if classe_id:
        q += " AND e.classe_id = ?"; p.append(classe_id)
    q += " ORDER BY s.date_seance DESC"
    if limite:
        q += f" LIMIT {int(limite)}"
    r = cx.execute(q, p).fetchall(); cx.close()
    sortie = []
    for x in r:
        d = dict(x)
        try:
            d["detail"] = json.loads(d.get("detail") or "[]")
        except Exception:
            d["detail"] = []
        sortie.append(d)
    return sortie


# ------------------------------------------- Activités à faire (phase J7)
def assigner_activite(eleve_id, genre, categorie="", lecon_id="", texte_id=None,
                      consigne=""):
    """Une même activité n'est pas assignée deux fois tant qu'elle est à faire."""
    cx = _connexion()
    deja = cx.execute("""SELECT id FROM activites_assignees
                         WHERE eleve_id=? AND genre=? AND categorie=? AND terminee=0""",
                      (eleve_id, genre, categorie)).fetchone()
    if deja:
        cx.close()
        return deja["id"]
    cur = cx.execute("""INSERT INTO activites_assignees
        (eleve_id, genre, categorie, lecon_id, texte_id, consigne, date_ajout)
        VALUES (?,?,?,?,?,?,?)""",
        (eleve_id, genre, categorie, lecon_id, texte_id, consigne, maintenant()))
    cx.commit(); rid = cur.lastrowid; cx.close()
    return rid


def activites_assignees(eleve_id, inclure_terminees=False):
    cx = _connexion()
    q = "SELECT * FROM activites_assignees WHERE eleve_id=?"
    if not inclure_terminees:
        q += " AND terminee=0"
    q += " ORDER BY date_ajout DESC"
    r = cx.execute(q, (eleve_id,)).fetchall(); cx.close()
    return [dict(x) for x in r]


def terminer_activite(aid):
    cx = _connexion()
    cx.execute("UPDATE activites_assignees SET terminee=1, date_fin=? WHERE id=?",
               (maintenant(), aid))
    cx.commit(); cx.close()


def assigner_texte(texte_id, classe_id=None, eleve_id=None, consigne=""):
    cx = _connexion()
    cur = cx.execute(
        "INSERT INTO assignations (texte_id, classe_id, eleve_id, consigne, cree_le) "
        "VALUES (?,?,?,?,?)",
        (texte_id, classe_id, eleve_id, consigne, maintenant()))
    cx.commit(); rid = cur.lastrowid; cx.close()
    return rid


def supprimer_assignation(aid):
    cx = _connexion()
    cx.execute("DELETE FROM assignations WHERE id = ?", (aid,))
    cx.commit(); cx.close()


def toutes_assignations():
    cx = _connexion()
    r = cx.execute("""
        SELECT a.id, a.cree_le, a.consigne, t.titre,
               COALESCE(c.nom, e.prenom) AS cible,
               CASE WHEN a.eleve_id IS NOT NULL THEN 'Élève' ELSE 'Classe' END AS type
        FROM assignations a
        JOIN textes_correction t ON t.id = a.texte_id
        LEFT JOIN classes c ON c.id = a.classe_id
        LEFT JOIN eleves e ON e.id = a.eleve_id
        ORDER BY a.cree_le DESC""").fetchall()
    cx.close()
    return [dict(x) for x in r]


def devoirs_eleve(eleve_id):
    """Textes assignés à un élève (directement ou via sa classe)."""
    cx = _connexion()
    r = cx.execute("""
        SELECT a.id, a.consigne, a.texte_id, t.titre, t.contenu, a.cree_le
        FROM assignations a
        JOIN textes_correction t ON t.id = a.texte_id
        WHERE a.eleve_id = ?
           OR a.classe_id = (SELECT classe_id FROM eleves WHERE id = ?)
        ORDER BY a.cree_le DESC""", (eleve_id, eleve_id)).fetchall()
    cx.close()
    return [dict(x) for x in r]


def marquer_exportees(table, ids):
    if not ids:
        return
    cx = _connexion()
    cx.executemany(f"UPDATE {table} SET exportee = 1 WHERE id = ?", [(i,) for i in ids])
    cx.commit(); cx.close()


def journaliser(action, details=""):
    cx = _connexion()
    cx.execute("INSERT INTO journal_integration(action, details, date_action) VALUES (?,?,?)",
               (action, details, maintenant()))
    cx.commit(); cx.close()


def journal(limite=100):
    cx = _connexion()
    r = cx.execute("SELECT * FROM journal_integration ORDER BY id DESC LIMIT ?",
                   (limite,)).fetchall()
    cx.close()
    return [dict(x) for x in r]


def purger_donnees_demo():
    """Supprime toutes les classes/élèves ET leurs séances (cascade)."""
    cx = _connexion()
    cx.execute("DELETE FROM classes")
    cx.commit(); cx.close()
