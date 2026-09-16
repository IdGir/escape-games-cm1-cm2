"""dictee.py — La dictée qui s'adapte à CET élève.

Une dictée de classe est la même pour tous : les uns s'ennuient, les autres
coulent. Ici, la liste est fabriquée à partir de ce que l'élève a réellement
raté, dans cette application :

  1. les mots de sa banque personnelle (ceux qu'il rate en se corrigeant)
  2. les mots qu'il est allé chercher au dictionnaire (ceux dont il DOUTE)
  3. à défaut, des mots de sa catégorie d'erreur la plus fréquente

Chaque mot est, si possible, replacé dans une phrase tirée des textes de
l'application : dicter un mot isolé est moins formateur que de l'entendre
dans un contexte qui en fixe le sens et l'accord.
"""
import random
import re

import database as db
import phonetique as ph

# --------------------------------------------------------------------------
#  Phrases porteuses : on cherche d'abord dans les textes de l'application
# --------------------------------------------------------------------------
_CORPUS = None


def _corpus():
    """Toutes les phrases correctes dont dispose l'application.

    Sources : les corrigés des textes à corriger, les textes de fluence, et
    la banque de phrases d'exercices. Ce sont des phrases écrites pour des
    élèves de cycle 3 : elles conviennent parfaitement à une dictée.
    """
    global _CORPUS
    if _CORPUS is not None:
        return _CORPUS
    phrases = []
    try:
        for t in db.liste_textes_correction(actifs_seulement=False):
            source = (t.get("corrige") or "").strip()
            if source:
                phrases += _decouper(source)
    except Exception:
        pass
    try:
        for t in db.liste_textes_fluence(actifs_seulement=False):
            phrases += _decouper(t.get("contenu") or "")
    except Exception:
        pass
    try:
        import exercices
        for liste in exercices.EXERCICES.values():
            phrases += [correct for (_faux, correct, _i) in liste]
    except Exception:
        pass
    # On ne garde que des phrases dictables : ni trop courtes, ni trop longues.
    _CORPUS = [p for p in dict.fromkeys(phrases) if 4 <= len(p.split()) <= 16]
    return _CORPUS


def _decouper(texte):
    morceaux = re.split(r"(?<=[.!?])\s+", (texte or "").strip())
    return [m.strip() for m in morceaux if m.strip()]


def phrase_contenant(mot):
    """Une phrase de l'application qui contient ce mot (ou None)."""
    motif = re.compile(r"\b" + re.escape(mot) + r"\b", re.IGNORECASE)
    candidates = [p for p in _corpus() if motif.search(p)]
    if not candidates:
        return None
    return min(candidates, key=len)      # la plus courte : la plus dictable


# ==========================================================================
#  Fabrication d'une banque de dictées par l'IA
#
#  Comme pour les textes à corriger : l'enseignant en produit autant qu'il
#  veut, d'un coup, et elles rejoignent une banque réutilisable.
# ==========================================================================
_CONSIGNES_IA = {
    "mots": (
        "Donne {n} MOTS ISOLÉS français, adaptés à des élèves de {age}. "
        "IMPÉRATIF : uniquement des formes de base — noms au SINGULIER, "
        "adjectifs au MASCULIN SINGULIER, adverbes, mots invariables. "
        "AUCUN pluriel, AUCUN verbe conjugué : dictés seuls, ils seraient "
        "impossibles à écrire correctement. "
        "Choisis des mots dont l'orthographe présente une vraie difficulté "
        "(lettre muette, double consonne, son qui s'écrit de plusieurs façons)."),
    "expressions": (
        "Donne {n} GROUPES NOMINAUX français, adaptés à des élèves de {age}. "
        "Chacun doit être un déterminant + un nom, avec un ou deux adjectifs : "
        "« des feuilles mortes », « un vieux château fort », « les grandes "
        "vacances ». "
        "IMPÉRATIF : chaque groupe doit former une UNITÉ DE SENS complète et "
        "autonome. Ce ne sont NI des phrases, NI des débuts de phrases, NI des "
        "suites de mots au hasard : pas de verbe, pas de préposition qui "
        "traîne à la fin. "
        "Varie le singulier et le pluriel : c'est l'accord qui se travaille."),
    "phrases": (
        "Donne {n} PHRASES françaises courtes et complètes, adaptées à des "
        "élèves de {age}. "
        "Chaque phrase commence par une majuscule, finit par un point, et "
        "contient un verbe conjugué. Entre {mini} et {maxi} mots. "
        "Choisis des phrases qui font travailler les accords et la "
        "conjugaison. Elles doivent avoir du sens et être imagées."),
}

_AGES = {1: "8 à 9 ans (facile)", 2: "9 à 11 ans (moyen)",
         3: "10 à 12 ans (difficile)"}


def generer_banque_ia(genre="mots", niveau=2, nombre=20, theme=""):
    """Fabrique des éléments de dictée avec l'IA. Renvoie (liste, message)."""
    genre = genre if genre in MODES else "mots"
    niveau = niveau if niveau in (1, 2, 3) else 2
    nombre = max(5, min(int(nombre or 20), 60))
    try:
        import ia_client
        from config_manager import config
        if not config.get("ia_active"):
            return [], ("Aucune IA active. Activez-en une dans "
                        "Paramètres → Réglages pour fabriquer des dictées.")
        cfg = MODES[genre]["niveaux"][niveau]
        consigne = _CONSIGNES_IA[genre].format(
            n=nombre, age=_AGES[niveau],
            mini=max(5, cfg.get("max_mots", 10) - 4),
            maxi=cfg.get("max_mots", 12))
        if theme:
            consigne += f" Thème : {theme}."
        brut = ia_client.appeler(
            "Tu prépares des dictées pour l'école primaire française. "
            + consigne +
            " Réponds UNIQUEMENT par un tableau JSON de chaînes, sans "
            'commentaire : ["…", "…"]',
            temperature=0.8, max_tokens=1400, tache="generation")
        import json as _json
        t = (brut or "").replace("```json", "").replace("```", "").strip()
        d, f = t.find("["), t.rfind("]")
        if d == -1 or f == -1:
            return [], "Réponse de l'IA illisible."
        liste = _json.loads(t[d:f + 1])
    except Exception as e:
        return [], f"Fabrication impossible ({type(e).__name__})."

    # On filtre : l'IA se trompe parfois de format malgré la consigne.
    propres = []
    for x in liste:
        s = str(x).strip().strip('"«»')
        if not s:
            continue
        nb = len(s.split())
        if genre == "mots":
            if nb != 1 or not mot_dictable_seul(s, _nature_de(s)):
                continue
        elif genre == "expressions":
            if not (2 <= nb <= cfg.get("max_mots", 4)):
                continue
            if s[-1] in ".!?":               # une phrase déguisée
                continue
            premier = s.split()[0].lower()
            if premier not in DETERMINANTS_EXPR:
                continue
        else:
            if nb < 4 or s[-1] not in ".!?":
                continue
        if s not in propres:
            propres.append(s)
    if not propres:
        return [], "L'IA n'a rien produit d'exploitable. Réessayez."
    return propres, ""


def phrase_ia(mots):
    """Demande à l'IA une phrase courte contenant les mots donnés."""
    try:
        import ia_client
        from config_manager import config
        if not config.get("ia_active"):
            return None
        liste = ", ".join(mots)
        brut = ia_client.appeler(
            "Tu prépares une dictée pour des élèves de 9 à 11 ans. Écris UNE "
            f"phrase courte (8 à 14 mots), simple et imagée, contenant le mot : "
            f"{liste}. La phrase doit être parfaitement correcte. "
            "Réponds UNIQUEMENT par la phrase, sans guillemets.",
            temperature=0.7, max_tokens=90, tache="generation")
        p = (brut or "").strip().strip('"«»').split("\n")[0].strip()
        return p if 15 < len(p) < 200 else None
    except Exception:
        return None


# --------------------------------------------------------------------------
#  Choix des mots
# --------------------------------------------------------------------------
def _mots_banque(eleve_id):
    """Les mots que l'élève rate en se corrigeant, les plus ratés d'abord."""
    out = []
    try:
        for m in db.banque_lexicale(eleve_id):
            if m.get("maitrise"):
                continue
            mot = (m.get("mot") or "").strip()
            if len(mot) >= 3:
                out.append({"mot": mot, "origine": "banque",
                            "categorie": m.get("categorie", "orthographe"),
                            "poids": 3 + int(m.get("nb_fois") or 1)})
    except Exception:
        pass
    return out


def _mots_cherches(eleve_id):
    """Les mots cherchés au dictionnaire : ceux dont l'élève doute."""
    out, vus = [], set()
    try:
        for r in db.recherches_dico(eleve_id=eleve_id, limite=120):
            mot = (r.get("mot_retenu") or "").strip()
            if len(mot) < 3 or mot in vus:
                continue
            vus.add(mot)
            out.append({"mot": mot, "origine": "dictionnaire",
                        "categorie": "orthographe", "poids": 2})
    except Exception:
        pass
    return out


# Mots outils : les dicter n'apprend rien, ils sont sus depuis le CE1.
MOTS_OUTILS = {
    "elle", "elles", "ils", "nous", "vous", "avec", "sans", "dans", "pour",
    "mais", "donc", "alors", "cette", "cette", "leur", "leurs", "notre",
    "votre", "quand", "comme", "très", "plus", "moins", "aussi", "encore",
    "être", "avoir", "faire", "cela", "celui", "celle", "tout", "tous",
    "toute", "toutes", "chaque", "autre", "autres", "même", "quel", "quelle",
    "sont", "était", "avait", "sera", "peut", "veut", "doit", "fait",
}


def _mots_categorie(categorie, nombre):
    """Complément : des mots porteurs de la difficulté travaillée."""
    out = []
    try:
        import exercices
        for _faux, correct, _indice in exercices.EXERCICES.get(categorie, []):
            for mot in re.findall(r"[A-Za-zÀ-ÿ'-]{4,}", correct):
                bas = mot.lower()
                if bas in MOTS_OUTILS:
                    continue
                out.append({"mot": bas, "origine": "categorie",
                            "categorie": categorie, "poids": 1})
    except Exception:
        pass
    random.shuffle(out)
    return out[:nombre]


def _mots_dictionnaire(nombre):
    """Dernier recours : des mots courants du dictionnaire embarqué."""
    out = []
    try:
        import dictionnaire as dico
        dico._charger()
        courants = [m for m in dico._MOTS if m[3] == 0 and 4 <= len(m[0]) <= 11]
        for mot, nature, _codes, _rang in random.sample(
                courants, min(nombre, len(courants))):
            out.append({"mot": mot, "origine": "courant",
                        "categorie": "orthographe", "poids": 1})
    except Exception:
        pass
    return out


# ==========================================================================
#  Les trois modes de dictée
#
#  Ce découpage vient d'une contrainte réelle : certains mots ne peuvent PAS
#  être dictés isolément. « chantent » ou « pommes » seuls sont indevinables —
#  rien n'indique le pluriel ni la personne. Il faut donc :
#
#   · MOTS        formes de base uniquement (ni pluriel, ni verbe conjugué)
#   · EXPRESSIONS groupes nominaux : le déterminant porte l'information
#                 (« des pommes rouges » : le pluriel s'entend et se déduit)
#   · PHRASES     phrase entière : verbe conjugué, compléments, ponctuation
# ==========================================================================
MODES = {
    "mots": {
        "nom": "Des mots", "emoji": "🔤",
        "explication": "Un mot à la fois, dans sa forme de base. Ni pluriel, "
                       "ni verbe conjugué : ils seraient impossibles à deviner.",
        "niveaux": {
            1: {"nom": "Facile", "nb": 6, "max_lettres": 7},
            2: {"nom": "Moyen", "nb": 10, "max_lettres": 10},
            3: {"nom": "Difficile", "nb": 14, "max_lettres": 99},
        },
    },
    "expressions": {
        "nom": "Des expressions", "emoji": "🧩",
        "explication": "Des groupes de mots avec leur petit mot devant. Là, "
                       "le pluriel s'entend : à toi de bien l'écrire partout.",
        "niveaux": {
            1: {"nom": "Facile", "nb": 5, "max_mots": 3},
            2: {"nom": "Moyen", "nb": 8, "max_mots": 4},
            3: {"nom": "Difficile", "nb": 10, "max_mots": 6},
        },
    },
    "phrases": {
        "nom": "Des phrases", "emoji": "📜",
        "explication": "Des phrases entières, avec les verbes, les accords et "
                       "la ponctuation. Le plus complet.",
        "niveaux": {
            1: {"nom": "Facile", "nb": 3, "max_mots": 8},
            2: {"nom": "Moyen", "nb": 4, "max_mots": 12},
            3: {"nom": "Difficile", "nb": 5, "max_mots": 18},
        },
    },
}

# Terminaisons qui trahissent une forme conjuguée : on ne dicte pas ces
# mots-là isolément, l'élève ne peut pas retrouver la personne ni le temps.
FINS_CONJUGUEES = ("ent", "ons", "ez", "ais", "ait", "aient", "erai", "eras",
                   "era", "erons", "erez", "eront", "âmes", "âtes", "èrent",
                   "issent", "issons", "issez")


def mot_dictable_seul(mot, nature=""):
    """Ce mot peut-il être dicté tout seul, sans contexte ?

    On refuse les pluriels (le « s » ne s'entend pas) et les formes
    conjuguées (rien n'indique la personne). Restent les formes de base :
    noms singuliers, adjectifs masculins singuliers, adverbes, invariables.
    """
    m = (mot or "").strip().lower()
    if len(m) < 3:
        return False
    nature = (nature or "").lower()

    # Un verbe n'est dictable qu'à l'infinitif.
    if "verbe" in nature and not m.endswith(("er", "ir", "re", "oir")):
        return False
    if m.endswith(FINS_CONJUGUEES) and "adverbe" not in nature:
        # « souvent », « comment » sont des adverbes : eux restent dictables.
        return False
    # Pluriel probable : le « s » ou « x » final ne s'entend pas.
    if m.endswith(("s", "x")) and not m.endswith(("ss", "ous", "as", "is", "us")):
        return False
    if m.endswith(("aux", "eaux", "eux")) and "adjectif" not in nature:
        return False
    return True


def _nature_de(mot):
    try:
        import dictionnaire as dico
        infos = dico.infos(mot)
        return infos["nature"] if infos else ""
    except Exception:
        return ""


def _forme_de_base(mot):
    """Ramène un mot à la forme qu'on peut dicter (singulier, infinitif…).

    Renvoie None si aucune forme de base n'est trouvée dans le dictionnaire.
    """
    try:
        import dictionnaire as dico
    except Exception:
        return mot if mot_dictable_seul(mot) else None
    m = (mot or "").strip().lower()
    essais = [m]
    if m.endswith(("s", "x")):
        essais.append(m[:-1])
    if m.endswith("es"):
        essais.append(m[:-2])
    if m.endswith("aux"):
        essais.append(m[:-3] + "al")
    for e in essais:
        infos = dico.infos(e)
        if infos and mot_dictable_seul(e, infos["nature"]):
            return e
    return None


DETERMINANTS_EXPR = ["le", "la", "les", "un", "une", "des", "mon", "ma", "mes",
                     "ce", "cette", "ces", "deux", "trois", "plusieurs"]


# Un groupe nominal s'arrête net devant ces mots : au-delà, on ramasserait un
# morceau de phrase (« des pommes rouges DANS le panier ») ou un verbe.
COUPURES = {"dans", "sur", "sous", "avec", "sans", "pour", "par", "chez",
            "vers", "depuis", "pendant", "après", "avant", "et", "ou", "mais",
            "que", "qui", "quand", "car", "donc", "à", "au", "aux", "en", "de",
            "du", "des", "d'", "l'", "y", "ne", "se", "s'", "est", "sont",
            "a", "ont", "était", "avait", "font", "fait",
            # Adverbes que le dictionnaire classe parfois aussi comme noms
            # ou adjectifs : ils n'ont rien à faire dans un groupe nominal.
            "bien", "très", "trop", "plus", "moins", "assez", "beaucoup",
            "peu", "aussi", "encore", "toujours", "jamais", "souvent", "si",
            "tout", "tous", "toute", "toutes", "même", "seul", "seulement"}


def _nature_courte(mot):
    """« nom », « adjectif », « autre » — d'après le dictionnaire embarqué."""
    try:
        import dictionnaire as dico
    except Exception:
        return ""
    m = (mot or "").lower().strip("'’-")
    for essai in (m, m[:-1] if m.endswith(("s", "x")) else m,
                  m[:-2] if m.endswith("es") else m,
                  (m[:-3] + "al") if m.endswith("aux") else m):
        infos = dico.infos(essai)
        if infos:
            n = infos["nature"]
            if n.startswith("nom"):
                return "nom"
            if n.startswith("adjectif"):
                return "adjectif"
            return "autre"
    return ""


def expressions_pour(mots, niveau_cfg):
    """Extrait de VRAIS groupes nominaux des textes de l'application.

    Un groupe nominal, c'est : un déterminant, puis un nom, éventuellement
    accompagné d'adjectifs. Rien d'autre. On vérifie la nature de chaque mot
    dans le dictionnaire embarqué, et on s'arrête dès qu'apparaît un verbe,
    une préposition ou une conjonction.

    Sans cette vérification, on ramassait des suites de mots sans unité de
    sens, voire des débuts de phrase — ce qui n'apprend rien.
    """
    import re as _re
    maxi = niveau_cfg.get("max_mots", 4)
    trouvees, vues = [], set()

    for phrase in _corpus():
        jetons = _re.findall(r"[A-Za-zÀ-ÿ'’-]+", phrase)
        i = 0
        while i < len(jetons):
            if jetons[i].lower() not in DETERMINANTS_EXPR:
                i += 1
                continue
            groupe = [jetons[i]]
            a_un_nom = False
            j = i + 1
            while j < len(jetons) and len(groupe) < maxi:
                suivant = jetons[j]
                bas = suivant.lower()
                if bas in COUPURES or bas in DETERMINANTS_EXPR:
                    break
                nat = _nature_courte(suivant)
                if nat == "nom":
                    # Deux noms de suite : le second ouvre autre chose.
                    if a_un_nom:
                        break
                    a_un_nom = True
                elif nat != "adjectif":
                    break            # verbe, adverbe, mot inconnu : on arrête
                groupe.append(suivant)
                j += 1
            # Un groupe n'est valable qu'avec un nom et au moins deux mots.
            if a_un_nom and 2 <= len(groupe) <= maxi:
                expr = " ".join(groupe)
                bas = expr.lower()
                if bas not in vues:
                    vues.add(bas)
                    trouvees.append(expr)
            i = j if j > i else i + 1

    # On met devant les groupes contenant un mot que l'élève rate, puis les
    # plus riches (avec un adjectif : c'est là que l'accord se travaille).
    cibles = {m["mot"].lower() for m in mots}
    trouvees.sort(key=lambda e: (
        0 if cibles & set(e.lower().split()) else 1,
        0 if len(e.split()) >= 3 else 1,
        len(e)))
    return trouvees


def preparer(eleve_id, nombre=10, avec_phrases=True, categorie_faible=None):
    """Fabrique la dictée d'un élève. Renvoie la liste des mots à dicter."""
    nombre = max(3, min(int(nombre or 10), 20))
    candidats = _mots_banque(eleve_id) + _mots_cherches(eleve_id)

    # Pas assez de matière ? On complète avec sa difficulté principale, puis
    # avec du vocabulaire courant : la dictée est toujours réalisable.
    if len(candidats) < nombre and categorie_faible:
        candidats += _mots_categorie(categorie_faible, nombre - len(candidats))
    if len(candidats) < nombre:
        candidats += _mots_dictionnaire(nombre - len(candidats))

    # Dédoublonnage en gardant le poids le plus fort.
    par_mot = {}
    for c in candidats:
        cle = c["mot"].lower()
        if cle not in par_mot or c["poids"] > par_mot[cle]["poids"]:
            par_mot[cle] = c
    liste = list(par_mot.values())

    # Tirage pondéré : les mots les plus ratés ont plus de chances de sortir,
    # sans que la dictée soit deux fois la même.
    choisis = []
    while liste and len(choisis) < nombre:
        total = sum(c["poids"] for c in liste)
        seuil = random.uniform(0, total)
        cumul = 0
        for i, c in enumerate(liste):
            cumul += c["poids"]
            if cumul >= seuil:
                choisis.append(liste.pop(i))
                break
        else:
            choisis.append(liste.pop())

    items = []
    for c in choisis:
        phrase = phrase_contenant(c["mot"]) if avec_phrases else None
        items.append({
            "mot": c["mot"],
            "phrase": phrase,
            "origine": c["origine"],
            "categorie": c["categorie"],
            "sons": ph.sons(c["mot"]),
            "nature": _nature(c["mot"]),
        })
    return items


# ==========================================================================
#  Préparation selon le mode et le niveau
# ==========================================================================
def preparer_mode(eleve_id, mode="mots", niveau=2, categorie_faible=None):
    """Fabrique la dictée demandée. Renvoie (items, explication)."""
    mode = mode if mode in MODES else "mots"
    niveau = niveau if niveau in MODES[mode]["niveaux"] else 2
    cfg = MODES[mode]["niveaux"][niveau]

    # Les mots de l'élève servent de base dans les trois modes.
    candidats = _mots_banque(eleve_id) + _mots_cherches(eleve_id)
    if categorie_faible:
        candidats += _mots_categorie(categorie_faible, 12)

    if mode == "mots":
        return _preparer_mots(candidats, cfg, niveau)
    if mode == "expressions":
        return _preparer_expressions(candidats, cfg, niveau)
    return _preparer_phrases(candidats, cfg, niveau)


def _preparer_mots(candidats, cfg, niveau=2):
    """Formes de base uniquement : ni pluriel, ni verbe conjugué."""
    items, vus = [], set()
    # La banque de l'enseignant passe devant : c'est son choix pédagogique.
    for x in _depuis_banque("mots", niveau, max(2, cfg["nb"] // 2)):
        mot = x["contenu"].strip().lower()
        if mot in vus or len(mot) > cfg["max_lettres"]:
            continue
        vus.add(mot)
        items.append({"contenu": mot, "mot": mot, "genre": "mots",
                      "origine": "banque_prof",
                      "categorie": x["categorie"] or "orthographe",
                      "nature": _nature_de(mot), "phrase": phrase_contenant(mot)})
    for c in candidats:
        base = _forme_de_base(c["mot"])
        if not base or base in vus:
            continue
        if len(base) > cfg["max_lettres"]:
            continue
        vus.add(base)
        items.append({
            "contenu": base, "mot": base, "genre": "mots",
            "origine": c["origine"], "categorie": c["categorie"],
            "nature": _nature_de(base),
            "phrase": phrase_contenant(base),
        })
        if len(items) >= cfg["nb"]:
            break

    # Complément avec des mots courants dictables tels quels.
    if len(items) < cfg["nb"]:
        for c in _mots_dictionnaire(cfg["nb"] * 4):
            base = c["mot"]
            if base in vus or len(base) > cfg["max_lettres"]:
                continue
            if not mot_dictable_seul(base, _nature_de(base)):
                continue
            vus.add(base)
            items.append({"contenu": base, "mot": base, "genre": "mots",
                          "origine": "courant", "categorie": "orthographe",
                          "nature": _nature_de(base),
                          "phrase": phrase_contenant(base)})
            if len(items) >= cfg["nb"]:
                break
    return items, ("Des mots seuls, dans leur forme de base : ni pluriel, "
                   "ni verbe conjugué — ceux-là seraient indevinables.")


def _depuis_banque(genre, niveau, nombre):
    """Ce que l'enseignant a mis dans la banque, tiré au sort."""
    try:
        import database as _db
        liste = _db.banque_dictee(genre=genre, niveau=niveau)
        if len(liste) < nombre:            # on élargit aux niveaux voisins
            liste += [x for x in _db.banque_dictee(genre=genre)
                      if x["id"] not in {y["id"] for y in liste}]
        random.shuffle(liste)
        return liste[:nombre]
    except Exception:
        return []


def _preparer_expressions(candidats, cfg, niveau=2):
    """Groupes nominaux : le déterminant porte l'information du pluriel."""
    items = []
    # 1. D'abord la banque de l'enseignant : c'est son choix pédagogique.
    for x in _depuis_banque("expressions", niveau, cfg["nb"]):
        items.append({"contenu": x["contenu"], "mot": x["contenu"],
                      "genre": "expressions", "origine": "banque_prof",
                      "categorie": x["categorie"] or "accord",
                      "nature": "groupe de mots", "phrase": None})
    # 2. Puis les groupes extraits des textes, si besoin de compléter.
    if len(items) < cfg["nb"]:
        deja = {i["contenu"].lower() for i in items}
        for expr in expressions_pour(candidats, cfg):
            if expr.lower() in deja:
                continue
            items.append({"contenu": expr, "mot": expr, "genre": "expressions",
                          "origine": "corpus", "categorie": "accord",
                          "nature": "groupe de mots", "phrase": None})
            if len(items) >= cfg["nb"]:
                break
    if not items:                       # rien nulle part : repli sur les mots
        return _preparer_mots(candidats, {"nb": cfg["nb"], "max_lettres": 12})[0], \
            ("Pas encore assez de textes pour fabriquer des expressions : "
             "voici des mots seuls. L'enseignant peut en créer dans "
             "« Banques de textes ».")
    return items[:cfg["nb"]], (
        "Des groupes de mots. Attention aux accords : si le petit mot du début "
        "est au pluriel, tout le groupe suit.")


def _preparer_phrases(candidats, cfg, niveau=2):
    """Phrases entières : verbes conjugués, accords, ponctuation."""
    items = []
    for x in _depuis_banque("phrases", niveau, cfg["nb"]):
        items.append({"contenu": x["contenu"], "mot": x["contenu"],
                      "genre": "phrases", "origine": "banque_prof",
                      "categorie": x["categorie"] or "accord",
                      "nature": "phrase", "phrase": None})
    if len(items) < cfg["nb"]:
        cibles = {c["mot"].lower() for c in candidats}
        deja = {i["contenu"].lower() for i in items}
        phrases = [p for p in _corpus() if len(p.split()) <= cfg["max_mots"]]
        phrases.sort(key=lambda p: (0 if cibles & set(
            re.findall(r"[a-zà-ÿ'’-]+", p.lower())) else 1, len(p)))
        for p in phrases:
            if p.lower() in deja:
                continue
            items.append({"contenu": p, "mot": p, "genre": "phrases",
                          "origine": "corpus", "categorie": "accord",
                          "nature": "phrase", "phrase": None})
            if len(items) >= cfg["nb"]:
                break
    return items[:cfg["nb"]], (
        "Des phrases entières. Pense aux verbes, aux accords, à la majuscule "
        "et au point.")


def _nature(mot):
    try:
        import dictionnaire as dico
        infos = dico.infos(mot)
        return infos["nature"] if infos else ""
    except Exception:
        return ""


# --------------------------------------------------------------------------
#  Correction : ce que l'élève a écrit, et POURQUOI c'est faux
# --------------------------------------------------------------------------
def verifier(attendu, saisi):
    """Compare la réponse au mot attendu et explique l'écart.

    La distinction essentielle : l'élève a-t-il bien ENTENDU le mot mais mal
    su l'ÉCRIRE (c'est de l'orthographe), ou a-t-il écrit un autre mot
    (c'est de l'écoute, ou du vocabulaire) ? Ce ne sont pas les mêmes
    remédiations, il ne faut donc pas les confondre.
    """
    a = (attendu or "").strip()
    s = (saisi or "").strip()
    if not s:
        return {"juste": False, "genre": "vide", "meme_son": False,
                "conseil": "Tu n'as rien écrit. Réécoute et essaie : "
                           "même une réponse fausse fait progresser."}

    if s.lower() == a.lower():
        return {"juste": True, "genre": "juste", "meme_son": True,
                "conseil": ""}

    sa, ss = ph.sons(a), ph.sons(s)
    meme_son = (sa == ss)

    # Accents seulement : on le teste EN PREMIER, sinon ces mots seraient
    # rangés en « orthographe » alors que l'écart est bien plus mince.
    if ph._sans_accent(a.lower()) == ph._sans_accent(s.lower()):
        return {"juste": False, "genre": "accent", "meme_son": meme_son,
                "conseil": "Il ne manque que les accents. Regarde bien les "
                           "é, è, ê — le reste du mot est juste."}

    # Même son, écriture différente : c'est une erreur d'orthographe pure.
    if meme_son:
        return {"juste": False, "genre": "orthographe", "meme_son": True,
                "conseil": "Tu as bien entendu le mot : ça se prononce "
                           "exactement comme ce que tu as écrit. C'est "
                           "l'orthographe qui change."}

    ecart = ph.distance_sons(sa, ss) / max(len(sa), len(ss), 1)
    if ecart <= 0.34:
        return {"juste": False, "genre": "proche", "meme_son": False,
                "conseil": "Tu es tout près : un seul son ne va pas. "
                           "Réécoute lentement, syllabe par syllabe."}

    return {"juste": False, "genre": "ecoute", "meme_son": False,
            "conseil": "Ce n'est pas le mot qui a été dicté. Réécoute-le "
                       "attentivement avant d'écrire."}


def verifier_groupe(attendu, saisi):
    """Corrige une expression ou une phrase, mot par mot.

    On ne se contente pas de « juste / faux » : sur une phrase, l'élève a
    souvent 9 mots sur 10 corrects, et il doit voir lesquels.
    """
    import difflib
    a_mots = re.findall(r"[A-Za-zÀ-ÿ0-9'’-]+", attendu or "")
    s_mots = re.findall(r"[A-Za-zÀ-ÿ0-9'’-]+", saisi or "")
    a = [m.lower() for m in a_mots]
    s = [m.lower() for m in s_mots]

    etats = ["oublie"] * len(a_mots)
    sm = difflib.SequenceMatcher(None, a, s, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            for k in range(i1, i2):
                etats[k] = "juste"
        elif op == "replace":
            for k in range(i1, i2):
                etats[k] = "faux"

    justes = sum(1 for e in etats if e == "juste")
    total = len(a_mots) or 1
    # La casse et la ponctuation comptent, mais on les signale à part.
    exact = (attendu or "").strip() == (saisi or "").strip()
    ponctuation = (not exact and justes == total)

    return {
        "juste": exact,
        "genre": "juste" if exact else ("ponctuation" if ponctuation
                                        else ("orthographe" if justes else "ecoute")),
        "meme_son": ph.sons(attendu) == ph.sons(saisi),
        "detail": [{"mot": a_mots[k], "etat": etats[k]} for k in range(len(a_mots))],
        "justes": justes, "total": total,
        "conseil": "" if exact else (
            "Tous les mots y sont : regarde la majuscule, les accents ou la "
            "ponctuation." if ponctuation else
            (f"{justes} mot(s) sur {total} sont justes. Regarde ceux qui sont "
             f"soulignés." if justes else
             "Réécoute attentivement : ce n'est pas ce qui a été dicté.")),
    }


def bilan(reponses):
    """Synthèse d'une dictée : compte et répartition des types d'erreurs."""
    total = len(reponses)
    justes = sum(1 for r in reponses if r.get("juste"))
    genres = {}
    for r in reponses:
        if not r.get("juste"):
            g = r.get("genre", "autre")
            genres[g] = genres.get(g, 0) + 1
    return {
        "total": total,
        "justes": justes,
        "score": round(justes / total * 100) if total else 0,
        "par_genre": genres,
        # Message d'ensemble, formulé pour l'élève.
        "message": _message(justes, total, genres),
    }


def _message(justes, total, genres):
    if not total:
        return ""
    pct = justes / total * 100
    if pct == 100:
        return "🏆 Sans faute ! Tous les mots sont justes."
    if pct >= 80:
        base = "🌟 Très bon résultat !"
    elif pct >= 60:
        base = "👏 Bon travail, continue !"
    else:
        base = "💪 C'est en s'entraînant qu'on progresse."
    ortho = genres.get("orthographe", 0) + genres.get("accent", 0)
    ecoute = genres.get("ecoute", 0)
    if ortho and ortho >= ecoute:
        return (base + " Tes erreurs sont surtout des erreurs d'orthographe : "
                "tu entends bien les mots, il faut maintenant retenir "
                "comment ils s'écrivent.")
    if ecoute:
        return (base + " Plusieurs mots n'ont pas été bien entendus : "
                "prends le temps de réécouter avant d'écrire.")
    return base
