"""Pont vers l'application « Notes & Suivi ».

POURQUOI CE SERVEUR ?
---------------------
Notes & Suivi est une application Electron dont les données sont chiffrées au
repos : elle n'est PAS interrogeable directement (ni base lisible, ni serveur).
En revanche, elle sait se comporter en CLIENT HTTP : son module `integration.ts`
appelle une application partenaire sur http://localhost:PORT, avec le même
contrat que celui utilisé pour le « Cahier Journal ».

C'est donc au Correcteur Pédagogique d'exposer ce contrat. Le seul réglage à
faire côté Notes & Suivi est de pointer son URL partenaire sur
http://localhost:4100 (clé localStorage `nes_cahier_url`, ou `setCahierUrl()`).

ENDPOINTS EXPOSÉS (contrat Notes & Suivi)
-----------------------------------------
  HEAD /                                          → test de joignabilité (ping)
  PUT  /api/integrations/apps                     → enregistrement de l'app partenaire
  POST /api/integrations/webhooks/notes-et-suivi  → réception d'événements
        · type "eleves.sync"          → met à jour la liste des élèves
        · type "evaluation.resultats" → archivé dans le journal
  GET  /api/integrations/export/eleves            → nos élèves
  GET  /api/integrations/export/evaluations       → nos résultats, convertis en
                                                    « évaluations » notées sur 100
  GET  /api/integrations/export/seances           → séances (correction + fluence)
                                                    filtrables par ?from=&to=

Tout tourne en local (127.0.0.1) : aucune donnée ne sort de l'ordinateur.
"""
import json
import threading
import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

import database as db
from config_manager import config
from theme import LIBELLES_CATEGORIES, REPERES_MCLM

_serveur = None
_thread = None


# ------------------------------------------------------------------ Conversions
def _prenom_nom(e):
    """Respecte le réglage RGPD : nom transmis seulement si autorisé."""
    if config.get("integration_anonymiser_nom", True):
        return {"id": f"cp-{e['id']}", "prenom": e["prenom"],
                "niveau": e.get("classe_niveau", ""), "classe": e.get("classe_nom", "")}
    return {"id": f"cp-{e['id']}", "prenom": e["prenom"], "nom": e.get("nom", ""),
            "niveau": e.get("classe_niveau", ""), "classe": e.get("classe_nom", "")}


def _eleves_payload():
    return [_prenom_nom(e) for e in db.liste_eleves()]


def score_correction(s) -> float:
    """Note /100 d'une séance d'autocorrection = % d'erreurs effectivement corrigées."""
    avant = s.get("erreurs_avant", 0) or 0
    apres = s.get("erreurs_apres", 0) or 0
    if avant == 0:
        return 100.0
    return round(max(0.0, (avant - apres) / avant) * 100, 1)


def taux_autonomie(s) -> float:
    """% des erreurs corrigées SANS consulter les outils d'aide."""
    total = (s.get("corrigees_seul", 0) or 0) + (s.get("corrigees_avec_aide", 0) or 0)
    if total == 0:
        return 0.0
    return round((s.get("corrigees_seul", 0) or 0) / total * 100, 1)


def score_fluence(s) -> float:
    """Note /100 d'une séance de fluence = MCLM rapporté au repère du niveau de classe."""
    repere = REPERES_MCLM.get(s.get("classe_niveau") or
                              config.get("fluence_niveau_classe", "CM1"), 90)
    return round(min(100.0, (s.get("mclm", 0) or 0) / max(1, repere) * 100), 1)


def _evaluations_payload():
    """Nos données converties en évaluations lisibles par Notes & Suivi.

    Deux évaluations synthétiques :
      · « Autocorrection — français »  : une note /100 par séance
      · « Fluence de lecture »         : une note /100 par séance
    Chaque évaluation porte aussi des « compétences » = les 8 catégories d'erreurs.
    """
    evals = []

    corr = db.seances_correction()
    if corr:
        resultats = []
        for s in corr:
            resultats.append({
                "eleveDistantId": f"cp-{s['eleve_id']}",
                "objectifId": "autocorrection-globale",
                "valeur": score_correction(s),
                "date": s["date_seance"],
                "detail": {
                    "erreurs_avant": s["erreurs_avant"],
                    "erreurs_apres": s["erreurs_apres"],
                    "autonomie_pct": taux_autonomie(s),
                    "origine_texte": s["origine"],
                    "erreurs_par_categorie": s["detail_avant"],
                },
            })
        evals.append({
            "id": "cp-eval-autocorrection",
            "nom": "Autocorrection — français écrit",
            "matiere": "Français",
            "systemeNotation": {"type": "numerique", "min": 0, "max": 100, "decimales": 1},
            "competences": [{"id": f"cat-{c}", "nom": LIBELLES_CATEGORIES[c]}
                            for c in LIBELLES_CATEGORIES],
            "resultats": resultats,
        })

    flu = db.seances_fluence()
    if flu:
        resultats = []
        for s in flu:
            resultats.append({
                "eleveDistantId": f"cp-{s['eleve_id']}",
                "objectifId": "fluence-mclm",
                "valeur": score_fluence(s),
                "date": s["date_seance"],
                "detail": {
                    "mclm": s["mclm"],
                    "niveau_texte": s["niveau"],
                    "duree_secondes": s["duree_secondes"],
                    "erreurs_lecture": s["erreurs"],
                    "titre_texte": s["titre_texte"],
                },
            })
        evals.append({
            "id": "cp-eval-fluence",
            "nom": "Fluence de lecture (MCLM)",
            "matiere": "Français",
            "systemeNotation": {"type": "numerique", "min": 0, "max": 100, "decimales": 1},
            "competences": [{"id": "fluence-mclm", "nom": "Mots corrects lus par minute"}],
            "resultats": resultats,
        })
    return evals


def _groupes_payload():
    """Les groupes de besoin, prêts à devenir des groupes de travail.

    Notes & Suivi peut ainsi récupérer directement « qui travaille quoi » :
    un groupe par catégorie d'erreur, avec ses élèves, la remédiation
    conseillée et la leçon du classeur qui s'y rattache.
    """
    import api  # analyser_eleve() y vit déjà : on ne duplique pas la logique

    groupes = {}
    for e in db.liste_eleves():
        bilan = api.analyser_eleve(e)
        for besoin in bilan["besoins"]:
            cat = besoin.get("categorie")
            if not cat:
                continue                       # besoin individuel, pas un groupe
            g = groupes.setdefault(cat, {
                "code": f"besoin-{cat}",
                "libelle": LIBELLES_CATEGORIES.get(cat, cat),
                "domaine": "Français — écrit",
                "remediation": besoin.get("remediation", ""),
                "leconId": besoin.get("lecon_id", ""),
                "procedure": besoin.get("procedure", []),
                "eleves": [],
            })
            g["eleves"].append({
                "eleveDistantId": f"cp-{e['id']}",
                **_prenom_nom(e),
                "classe": e.get("classe_nom", ""),
                "gravite": besoin.get("gravite", "moyenne"),
            })

    sortie = sorted(groupes.values(), key=lambda g: -len(g["eleves"]))
    for g in sortie:
        g["effectif"] = len(g["eleves"])
    return sortie


def _seances_payload(depuis=None, jusqua=None):
    def dans_periode(d):
        if depuis and d < depuis:
            return False
        if jusqua and d > jusqua + "T23:59:59":
            return False
        return True

    out = []
    for s in db.seances_correction():
        if dans_periode(s["date_seance"]):
            out.append({
                "id": f"corr-{s['id']}", "type": "autocorrection",
                "date": s["date_seance"], "eleveDistantId": f"cp-{s['eleve_id']}",
                "titre": "Séance d'autocorrection",
                "duree_minutes": round((s["duree_secondes"] or 0) / 60, 1),
                "note": score_correction(s),
            })
    for s in db.seances_fluence():
        if dans_periode(s["date_seance"]):
            out.append({
                "id": f"flu-{s['id']}", "type": "fluence",
                "date": s["date_seance"], "eleveDistantId": f"cp-{s['eleve_id']}",
                "titre": f"Fluence — {s['titre_texte']}",
                "duree_minutes": round((s["duree_secondes"] or 0) / 60, 1),
                "note": score_fluence(s), "mclm": s["mclm"],
            })
    out.sort(key=lambda x: x["date"], reverse=True)
    return out


# ------------------------------------------------------------------ Portail Enseignant
# Endpoints de LECTURE consommés par le Portail (tableau de bord agrégé).
# Mêmes règles RGPD que le reste du pont : identité via _prenom_nom()
# (prénom seul si « integration_anonymiser_nom » est actif).

_COULEURS_GRAVITE = {"haute": "#dc2626", "moyenne": "#f59e0b", "faible": "#22c55e"}


def _nom_affiche(e):
    """Prénom (+ initiale du nom si le réglage RGPD l'autorise)."""
    p = _prenom_nom(e)
    nom = (p.get("nom") or "").strip()
    return f"{p['prenom']} {nom[0].upper()}." if nom else p["prenom"]


def _stats_seances(seances):
    """Agrégats simples sur des séances de correction."""
    mots = sum(s.get("nb_mots") or 0 for s in seances)
    avant = sum(s.get("erreurs_avant") or 0 for s in seances)
    apres = sum(s.get("erreurs_apres") or 0 for s in seances)
    return {
        "nb_seances": len(seances),
        "mots_ecrits": mots,
        "erreurs_detectees": avant,
        "erreurs_corrigees": max(0, avant - apres),
        "taux_erreurs_100_mots": round(avant / mots * 100, 1) if mots else 0.0,
        "taux_correction": round(max(0.0, (avant - apres) / avant) * 100, 1) if avant else 100.0,
    }


def _classes_payload():
    return [{"id": c["id"], "nom": c["nom"], "niveau": c.get("niveau", "")}
            for c in db.liste_classes()]


def _overview_payload(classe_id=None):
    seances = db.seances_correction(classe_id=classe_id)
    flu = db.seances_fluence(classe_id=classe_id)
    stats = _stats_seances(seances)
    autos = [taux_autonomie(s) for s in seances
             if (s.get("corrigees_seul") or 0) + (s.get("corrigees_avec_aide") or 0) > 0]
    stats["autonomie_moyenne"] = round(sum(autos) / len(autos), 1) if autos else None
    stats["nb_seances_fluence"] = len(flu)
    stats["mclm_moyen"] = (round(sum((s.get("mclm") or 0) for s in flu) / len(flu), 1)
                           if flu else None)
    return stats


def _erreurs_par_categorie(seances):
    """Cumul {catégorie: nb} sur les detail_avant des séances données."""
    cats = {}
    for s in seances:
        detail = s.get("detail_avant") or {}
        if isinstance(detail, str):
            try:
                detail = json.loads(detail)
            except Exception:
                detail = {}
        for c, v in detail.items():
            cats[c] = cats.get(c, 0) + (v or 0)
    return cats


def _by_type_payload(classe_id=None):
    seances = db.seances_correction(classe_id=classe_id)
    cats = _erreurs_par_categorie(seances)
    return [{"error_type": LIBELLES_CATEGORIES.get(c, c), "categorie": c, "count": n}
            for c, n in sorted(cats.items(), key=lambda x: -x[1])]


def _comparison_payload(classe_id=None):
    lignes = []
    for e in db.liste_eleves(classe_id=classe_id):
        seances = db.seances_correction(eleve_id=e["id"])
        if not seances:
            continue
        stats = _stats_seances(seances)
        autos = [taux_autonomie(s) for s in seances
                 if (s.get("corrigees_seul") or 0) + (s.get("corrigees_avec_aide") or 0) > 0]
        lignes.append({
            "student_id": f"cp-{e['id']}",
            "name": _nom_affiche(e),
            "classe": e.get("classe_nom", ""),
            "nb_seances": stats["nb_seances"],
            "erreurs": stats["erreurs_detectees"],
            "rate_per_100": stats["taux_erreurs_100_mots"],
            "taux_correction": stats["taux_correction"],
            "autonomie": round(sum(autos) / len(autos), 1) if autos else None,
        })
    lignes.sort(key=lambda x: -(x["rate_per_100"] or 0))
    return lignes


def _analyse_payload(classe_id=None, student_id=None):
    """Analyse consommée par la page Synthèse du Portail.

    Champs attendus côté Portail : error_types, competences, need_groups,
    et — pour un élève — recurrences + autonomy.success_rate.
    """
    import api  # analyser_eleve() y vit déjà : on ne duplique pas la logique

    eleve = None
    if student_id:
        brut = str(student_id).replace("cp-", "")
        for e in db.liste_eleves():
            if str(e["id"]) == brut:
                eleve = e
                break

    seances = (db.seances_correction(eleve_id=eleve["id"]) if eleve
               else db.seances_correction(classe_id=classe_id))
    cats = _erreurs_par_categorie(seances)
    mots = sum(s.get("nb_mots") or 0 for s in seances)

    error_types = [{"error_type": LIBELLES_CATEGORIES.get(c, c), "categorie": c, "count": n}
                   for c, n in sorted(cats.items(), key=lambda x: -x[1])]

    competences = [{
        "label": LIBELLES_CATEGORIES.get(c, c),
        "competence": LIBELLES_CATEGORIES.get(c, c),
        "count": n,
        "rate_per_100": round(n / mots * 100, 1) if mots else 0.0,
        "level_color": "#dc2626" if mots and n / mots * 100 >= 5
                       else "#f59e0b" if mots and n / mots * 100 >= 2 else "#22c55e",
    } for c, n in sorted(cats.items(), key=lambda x: -x[1])]

    # Groupes de besoin (classe) — réutilise _groupes_payload, formes Portail.
    need_groups = []
    if not eleve:
        for g in _groupes_payload():
            need_groups.append({
                "competence": g["libelle"],
                "label": g["libelle"],
                "remediation": g.get("remediation", ""),
                "level_color": _COULEURS_GRAVITE.get(
                    max((m.get("gravite", "moyenne") for m in g["eleves"]),
                        default="moyenne"), "#f59e0b"),
                "students": [{
                    "name": f"{m['prenom']} {(m.get('nom') or '')[:1]}.".strip().rstrip("."),
                    "rate_per_100": None,
                    "gravite": m.get("gravite", "moyenne"),
                } for m in g["eleves"]
                   if classe_id is None or str(m.get("classe", "")) ==
                   next((c["nom"] for c in db.liste_classes() if c["id"] == classe_id), "")],
            })
        need_groups = [g for g in need_groups if g["students"]]

    payload = {
        "error_types": error_types,
        "competences": competences,
        "need_groups": need_groups,
    }

    if eleve:
        bilan = api.analyser_eleve(eleve)
        n_recentes = bilan.get("categories", {})
        payload["recurrences"] = [
            {"error_type": LIBELLES_CATEGORIES.get(c, c), "count": n}
            for c, n in sorted(n_recentes.items(), key=lambda x: -x[1]) if n >= 2
        ]
        payload["autonomy"] = {"success_rate": round(bilan.get("autonomie") or 0)}
        payload["taux_correction"] = bilan.get("taux_correction")
        payload["mclm"] = {
            "moyen": bilan.get("mclm_moyen"),
            "dernier": bilan.get("mclm_dernier"),
            "repere": bilan.get("repere"),
        }
    return payload


# ------------------------------------------------------------------ Serveur HTTP
class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *a):
        pass  # pas de bruit dans la console

    # -- utilitaires
    def _jeton_ok(self):
        attendu = (config.get("integration_jeton") or "").strip()
        if not attendu:
            return True
        recu = (self.headers.get("Authorization") or "").replace("Bearer", "").strip()
        return recu == attendu

    def _repondre(self, code, data=None):
        corps = json.dumps(data if data is not None else {"ok": True},
                           ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(corps)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, HEAD, OPTIONS")
        self.end_headers()
        self.wfile.write(corps)

    def do_OPTIONS(self):
        self._repondre(204, {})

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-Length", "0")
        self.send_header("X-App", "correcteur-pedagogique")
        self.end_headers()

    def do_GET(self):
        u = urlparse(self.path)
        q = parse_qs(u.query)

        def param(nom):
            return (q.get(nom) or [None])[0]

        def param_classe():
            v = param("class_id") or param("classe_id")
            try:
                return int(v) if v not in (None, "", "0") else None
            except (TypeError, ValueError):
                return None

        if not self._jeton_ok():
            return self._repondre(401, {"erreur": "jeton invalide"})
        try:
            if u.path in ("/", "/api/status", "/api/health"):
                return self._repondre(200, {"app": "correcteur-pedagogique",
                                            "version": "G", "statut": "actif"})
            # ── Contrat Notes & Suivi (inchangé) ──
            if u.path == "/api/integrations/export/eleves":
                return self._repondre(200, {"eleves": _eleves_payload()})
            if u.path == "/api/integrations/export/evaluations":
                return self._repondre(200, {"evaluations": _evaluations_payload()})
            if u.path == "/api/integrations/export/seances":
                return self._repondre(200, {"seances": _seances_payload(
                    param("from"), param("to"))})
            if u.path == "/api/integrations/export/groupes":
                return self._repondre(200, {"groupes": _groupes_payload()})
            # ── Lecture Portail Enseignant (agrégats désidentifiés) ──
            if u.path == "/api/classes":
                return self._repondre(200, _classes_payload())
            if u.path == "/api/stats/overview":
                return self._repondre(200, _overview_payload(param_classe()))
            if u.path == "/api/stats/by-type":
                return self._repondre(200, _by_type_payload(param_classe()))
            if u.path == "/api/stats/comparison":
                return self._repondre(200, _comparison_payload(param_classe()))
            if u.path == "/api/analyse":
                return self._repondre(200, _analyse_payload(
                    param_classe(), param("student_id")))
            return self._repondre(404, {"erreur": "endpoint inconnu"})
        except Exception as e:
            return self._repondre(500, {"erreur": str(e)})

    def do_PUT(self):
        u = urlparse(self.path)
        n = int(self.headers.get("Content-Length") or 0)
        brut = self.rfile.read(n) if n else b"{}"
        if u.path == "/api/integrations/apps":
            try:
                d = json.loads(brut.decode("utf-8") or "{}")
            except Exception:
                d = {}
            db.journaliser("app-enregistree", json.dumps(d, ensure_ascii=False)[:400])
            return self._repondre(200, {"ok": True, "app": d.get("code", "?")})
        return self._repondre(404, {"erreur": "endpoint inconnu"})

    def do_POST(self):
        u = urlparse(self.path)
        n = int(self.headers.get("Content-Length") or 0)
        brut = self.rfile.read(n) if n else b"{}"
        if not self._jeton_ok():
            return self._repondre(401, {"erreur": "jeton invalide"})
        if u.path.startswith("/api/integrations/webhooks/"):
            try:
                ev = json.loads(brut.decode("utf-8") or "{}")
            except Exception:
                return self._repondre(400, {"erreur": "JSON invalide"})
            typ = ev.get("type", "")
            payload = ev.get("payload", ev.get("data", {}))
            if typ == "eleves.sync":
                nb = _fusionner_eleves(payload)
                db.journaliser("webhook-eleves.sync", f"{nb} élève(s) reçu(s)")
                return self._repondre(200, {"ok": True, "recus": nb})
            db.journaliser(f"webhook-{typ}",
                           json.dumps(payload, ensure_ascii=False)[:400])
            return self._repondre(200, {"ok": True})
        return self._repondre(404, {"erreur": "endpoint inconnu"})


def _fusionner_eleves(payload):
    """Reçoit les élèves envoyés par Notes & Suivi et complète notre base.

    On n'écrase JAMAIS un élève existant : on ajoute uniquement les manquants,
    en rapprochant sur (prénom, classe).
    """
    liste = payload if isinstance(payload, list) else payload.get("eleves", [])
    if not isinstance(liste, list):
        return 0
    existants = {(e["prenom"].lower(), (e.get("classe_nom") or "").lower())
                 for e in db.liste_eleves()}
    classes = {c["nom"].lower(): c["id"] for c in db.liste_classes()}
    nb = 0
    for e in liste:
        if not isinstance(e, dict):
            continue
        prenom = (e.get("prenom") or "").strip()
        if not prenom:
            continue
        classe_nom = (e.get("classe") or e.get("niveau") or "Import").strip()
        cle = (prenom.lower(), classe_nom.lower())
        if cle in existants:
            continue
        cid = classes.get(classe_nom.lower())
        if cid is None:
            cid = db.ajouter_classe(classe_nom, e.get("niveau", "CM1"))
            classes[classe_nom.lower()] = cid
        db.ajouter_eleve(prenom, e.get("nom", "") or "", cid)
        existants.add(cle)
        nb += 1
    return nb


# ------------------------------------------------------------------ Démarrage
def hote_ecoute():
    """Interface d'écoute du pont.

    127.0.0.1 par défaut. L'option « integration_ecoute_lan » (réglages,
    désactivée par défaut) ouvre le pont au réseau local — usage prévu :
    consulter le Portail Enseignant depuis la tablette/le téléphone à la
    MAISON, sur le PC fixe uniquement.

    GARDE-FOU : si le « mode salle » est actif (espace élève ouvert au réseau
    de l'école), le pont reste sur 127.0.0.1 quoi qu'il arrive. Les élèves ne
    doivent jamais pouvoir atteindre les données agrégées destinées au
    Portail. Les deux ouvertures réseau sont indépendantes : mode salle =
    interface élève (port de l'application), écoute LAN = pont Portail
    (port 4100), et jamais les deux en même temps.
    """
    if config.get("mode_salle", False):
        return "127.0.0.1"
    return "0.0.0.0" if config.get("integration_ecoute_lan", False) else "127.0.0.1"


def demarrer():
    """Lance le serveur en arrière-plan. Ne bloque jamais l'application."""
    global _serveur, _thread
    if _serveur is not None:
        return True, "Le pont est déjà actif."
    port = int(config.get("integration_port", 4100))
    hote = hote_ecoute()
    try:
        _serveur = ThreadingHTTPServer((hote, port), Handler)
    except OSError as e:
        _serveur = None
        return False, f"Impossible d'ouvrir le port {port} : {e}"
    _thread = threading.Thread(target=_serveur.serve_forever, daemon=True)
    _thread.start()
    if hote == "0.0.0.0":
        db.journaliser("pont-demarre", f"port {port} — ÉCOUTE RÉSEAU LOCAL (Portail maison)")
        return True, f"Pont actif sur le réseau local, port {port} (Portail maison)."
    db.journaliser("pont-demarre", f"port {port} (127.0.0.1)")
    return True, f"Pont actif sur http://localhost:{port}"


def redemarrer():
    """Applique un changement d'écoute (LAN/local) ou de port sans fermer l'appli."""
    etait_actif = est_actif()
    if etait_actif:
        arreter()
    if etait_actif or config.get("integration_active", True):
        return demarrer()
    return False, "Le pont n'était pas actif."


def arreter():
    global _serveur, _thread
    if _serveur:
        _serveur.shutdown()
        _serveur.server_close()
        _serveur = None
        _thread = None
        db.journaliser("pont-arrete", "")
        return True, "Pont arrêté."
    return False, "Le pont n'était pas actif."


def est_actif():
    return _serveur is not None


def url():
    return f"http://localhost:{config.get('integration_port', 4100)}"


# ------------------------------------------------------------------ Export fichier
def exporter_json(chemin):
    """Export de secours au format fichier (si le pont n'est pas utilisé)."""
    data = {
        "app": "correcteur-pedagogique",
        "exportLe": datetime.datetime.now().isoformat(timespec="seconds"),
        "eleves": _eleves_payload(),
        "evaluations": _evaluations_payload(),
        "seances": _seances_payload(),
        "groupes": _groupes_payload(),
    }
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    db.journaliser("export-json", str(chemin))
    return chemin
