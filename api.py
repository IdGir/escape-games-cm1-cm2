"""API HTTP locale : le pont entre l'interface web et la logique métier Python.

Tout le code métier (base, correcteur, vérification, fluence, intégration) est
inchangé : cette couche ne fait que l'exposer. Le serveur n'écoute que sur
127.0.0.1 : rien ne sort de l'ordinateur.
"""
import csv
import io
import os
import statistics
import threading

from flask import Flask, jsonify, request, send_from_directory

import aide as aide_mod
import auth
import correction_engine as ce
import corrector
import database as db
import exercices
import integration_server as ig
import lecons_manuel as lm
import lexical_hints as lh
import pilotage
import reseau
import sauvegarde
import seed_data
import theme as T
from config_manager import config, DEFAUTS
from paths import (dossier_exports, dossier_ressources, dossier_donnees,
                   chemin_base)
from theme import (CATEGORIES, LIBELLES_CATEGORIES, COULEURS_CATEGORIES,
                   NIVEAUX_FLUENCE, REPERES_MCLM)

DOSSIER_WEB = str(dossier_ressources() / "web")

app = Flask(__name__, static_folder=None)
# Sans cela, Flask trie les clés par ordre alphabétique : les modes de dictée
# sortiraient « expressions, mots, phrases » au lieu de l'ordre pédagogique
# voulu (mots → expressions → phrases).
app.json.sort_keys = False

# --- Phase I : sécurité, sauvegardes, réseau ---
gestion_auth = auth.GestionnaireAuth(config)
gestion_sauv = sauvegarde.GestionnaireSauvegardes(
    chemin_base(), dossier_donnees() / "sauvegardes")


def _appliquer_reglages_sauvegarde():
    """Recharge la copie externe depuis la configuration (appelé au démarrage
    et à chaque modification du réglage)."""
    gestion_sauv.configurer_externe(
        dossier=config.get("sauvegarde_externe_dossier", ""),
        actif=config.get("sauvegarde_externe_active", False),
        nb_conservees=config.get("sauvegarde_externe_nb", 10),
    )


_appliquer_reglages_sauvegarde()
PORT_ACTUEL = 5173  # renseigné par demarrer()

# Routes réservées à l'enseignant (protégées dès qu'un PIN est défini).
# Tout le reste — connexion élève, correction, fluence, séances — reste ouvert.
PREFIXES_PROTEGES = ("/api/prof/", "/api/securite/", "/api/reglages",
                     "/api/pont", "/api/export/", "/api/donnees/purger")
# Ces routes de sécurité sont les « portes » du verrou : toujours accessibles.
SECURITE_OUVERTES = (
    "/api/securite/etat", "/api/securite/creer",
    "/api/securite/verifier", "/api/securite/recuperer",
)


def _route_protegee(chemin, methode):
    if chemin in SECURITE_OUVERTES:
        return False
    if any(chemin.startswith(p) for p in PREFIXES_PROTEGES):
        return True
    # écriture sur classes / élèves / textes = enseignant uniquement
    if methode in ("POST", "DELETE") and (
        chemin.startswith("/api/classes") or chemin.startswith("/api/eleves")
        or chemin.startswith("/api/textes") or chemin.startswith("/api/assignations")
    ):
        return True
    return False


@app.before_request
def _controle_acces():
    # Sans PIN défini, l'application se comporte exactement comme avant.
    if not gestion_auth.pin_defini():
        return None
    if _route_protegee(request.path, request.method):
        jeton = request.headers.get("X-Jeton", "")
        if not gestion_auth.session_valide(jeton):
            return jsonify({"erreur": "verrouille"}), 401
    return None


# ============================================================================
#  Fichiers de l'interface
# ============================================================================
@app.route("/")
def index():
    return send_from_directory(DOSSIER_WEB, "index.html")


@app.route("/<path:chemin>")
def statique(chemin):
    return send_from_directory(DOSSIER_WEB, chemin)


# ============================================================================
#  Référentiel (couleurs, catégories, repères) — le front s'y aligne
# ============================================================================
@app.get("/api/referentiel")
def referentiel():
    return jsonify({
        "categories": CATEGORIES,
        # Aux 8 catégories d'erreurs écrites s'ajoutent les besoins repérés
        # en lecture et en dictée : ils forment eux aussi des groupes.
        "libelles": {**LIBELLES_CATEGORIES,
                     "lecture_fluence": "Fluence de lecture",
                     "dictee_score": "Orthographe sous dictée",
                     "dictee_ecoute": "Discrimination auditive"},
        "couleurs": {**COULEURS_CATEGORIES,
                     "lecture_fluence": "#0EA5E9",
                     "dictee_score": "#E8890C",
                     "dictee_ecoute": "#DC2626"},
        "niveaux_fluence": {str(k): {"libelle": v[0], "couleur": v[1]}
                            for k, v in NIVEAUX_FLUENCE.items()},
        "reperes_mclm": REPERES_MCLM,
        "theme_sombre": T.mode_sombre(),
        "config": config.tout(),
        "moteur": _etat_moteur(),
    })


def _etat_moteur():
    if not config.get("ia_active"):
        return {"actif": False, "nom": "Génération hors ligne",
                "detail": "secours local toujours prêt"}
    import ia_client
    return {
        "actif": True,
        "nom": ia_client.nom_moteur(config.get("ia_moteur", "deepseek")),
        "detail": "correction par IA activée",
    }


# ============================================================================
#  Thème
# ============================================================================
@app.post("/api/theme")
def theme():
    T.basculer_mode(bool(request.json.get("sombre")))
    return jsonify({"sombre": T.mode_sombre()})


# ============================================================================
#  Classes et élèves
# ============================================================================
@app.get("/api/classes")
def classes():
    cs = db.liste_classes()
    for c in cs:
        c["eleves"] = db.liste_eleves(classe_id=c["id"])
    return jsonify(cs)


@app.post("/api/classes")
def creer_classe():
    d = request.json
    cid = db.ajouter_classe(d["nom"], d.get("niveau", "CM1"))
    return jsonify({"id": cid})


@app.delete("/api/classes/<int:cid>")
def suppr_classe(cid):
    db.supprimer_classe(cid)
    return jsonify({"ok": True})


@app.post("/api/eleves")
def creer_eleve():
    d = request.json
    eid = db.ajouter_eleve(d["prenom"], d.get("nom", ""), d["classe_id"])
    return jsonify({"id": eid})


@app.delete("/api/eleves/<int:eid>")
def suppr_eleve(eid):
    db.supprimer_eleve(eid)
    return jsonify({"ok": True})


@app.post("/api/eleves/import")
def importer_eleves():
    """Import CSV : prénom ; nom ; classe. Les classes absentes sont créées."""
    contenu = request.json.get("csv", "")
    delim = ";" if contenu.count(";") >= contenu.count(",") else ","
    lecteur = csv.reader(io.StringIO(contenu), delimiter=delim)
    cache = {c["nom"].lower(): c["id"] for c in db.liste_classes()}
    vus = {(e["prenom"].lower(), e["classe_nom"].lower())
           for e in db.liste_eleves()}
    ajoutes = ignores = 0
    for ligne in lecteur:
        if len(ligne) < 2:
            continue
        prenom = ligne[0].strip()
        if prenom.lower() in ("prénom", "prenom", "élève", "eleve"):
            continue
        nom = ligne[1].strip() if len(ligne) > 2 else ""
        classe = (ligne[2] if len(ligne) > 2 else ligne[1]).strip()
        if not prenom or not classe:
            continue
        cid = cache.get(classe.lower())
        if cid is None:
            cid = db.ajouter_classe(classe)
            cache[classe.lower()] = cid
        if (prenom.lower(), classe.lower()) in vus:
            ignores += 1
            continue
        db.ajouter_eleve(prenom, nom, cid)
        vus.add((prenom.lower(), classe.lower()))
        ajoutes += 1
    return jsonify({"ajoutes": ajoutes, "ignores": ignores})


@app.post("/api/donnees/purger")
def purger():
    db.purger_donnees_demo()
    return jsonify({"ok": True})


# ============================================================================
#  Banques de textes
# ============================================================================
@app.get("/api/textes/correction")
def textes_correction():
    tous = request.args.get("tous") == "1"
    return jsonify(db.liste_textes_correction(actifs_seulement=not tous))


@app.post("/api/textes/correction")
def creer_texte_correction():
    d = request.json
    tid = db.ajouter_texte_correction(d["titre"], d["contenu"],
                                      int(d.get("niveau", 2)),
                                      d.get("corrige", ""))
    return jsonify({"id": tid})


@app.delete("/api/textes/correction/<int:tid>")
def suppr_texte_correction(tid):
    db.supprimer_texte_correction(tid)
    return jsonify({"ok": True})


@app.post("/api/textes/correction/<int:tid>/corrige")
def definir_corrige(tid):
    """Ajoute/complète le corrigé d'un texte existant de la banque."""
    corrige = (request.json or {}).get("corrige", "")
    db.definir_corrige_texte(tid, corrige)
    return jsonify({"ok": True})


@app.get("/api/textes/fluence")
def textes_fluence():
    niveau = request.args.get("niveau")
    return jsonify(db.liste_textes_fluence(
        niveau=int(niveau) if niveau else None,
        actifs_seulement=request.args.get("tous") != "1"))


@app.post("/api/textes/fluence")
def creer_texte_fluence():
    d = request.json
    tid = db.ajouter_texte_fluence(d["titre"], d["contenu"], int(d["niveau"]))
    return jsonify({"id": tid})


@app.delete("/api/textes/fluence/<int:tid>")
def suppr_texte_fluence(tid):
    db.supprimer_texte_fluence(tid)
    return jsonify({"ok": True})


@app.post("/api/textes/reinstaller")
def reinstaller_textes():
    seed_data.reinstaller_textes()
    return jsonify({"ok": True})


@app.post("/api/textes/correction/installer-fournis")
def installer_textes_fournis():
    """Ajoute les textes de correction fournis manquants (avec leur corrigé)."""
    ajoutes = seed_data.completer_textes_correction()
    return jsonify({"ok": True, "ajoutes": ajoutes})


# ============================================================================
#  Le cœur : générer, corriger, analyser
# ============================================================================
@app.post("/api/generer")
def generer():
    """Fabrique un texte fautif, avec son corrigé et les catégories injectées."""
    import ai_generator as ai
    nb = int((request.json or {}).get("nb_phrases") or config.get("ia_nb_phrases", 5))
    texte, corrige, erreurs, moteur, message = ai.generer(nb_phrases=nb)
    return jsonify({
        "texte": texte, "reference": corrige, "moteur": moteur, "message": message,
        # Tout texte fabriqué arrive avec un titre : l'enseignant peut le changer.
        "titre": ai.titre_auto(corrige or texte),
        "categories": {f"{f.lower()}|{j.lower()}": c for f, j, c in erreurs},
    })


@app.post("/api/generer-lot")
def generer_lot():
    """Fabrique et enregistre plusieurs textes à corriger d'un seul coup.

    Sert à se constituer rapidement une banque suffisante. Chaque texte est
    enregistré avec son corrigé et un titre automatique modifiable ensuite.
    """
    import ai_generator as ai
    d = request.json or {}
    nombre = max(1, min(int(d.get("nombre") or 5), 30))
    nb = int(d.get("nb_phrases") or config.get("ia_nb_phrases", 5))
    niveau = int(d.get("niveau") or 2)
    crees, moteurs = [], set()
    themes = ai.themes_actifs()
    # On fait tourner les thèmes cochés : dix textes sur le même sujet
    # reviennent tous avec le même titre, ce qui les rend inutilisables.
    deja = {t["titre"].strip().lower()
            for t in db.liste_textes_correction(actifs_seulement=False)}
    for i in range(nombre):
        try:
            theme = themes[i % len(themes)]
            texte, corrige, _err, moteur, _msg = ai.generer(
                nb_phrases=nb, theme_=theme)
            if not texte or not corrige:
                continue
            titre = _titre_unique(ai.titre_auto(corrige), corrige, deja)
            deja.add(titre.strip().lower())
            tid = db.ajouter_texte_correction(titre, texte, niveau, corrige)
            crees.append({"id": tid, "titre": titre, "theme": theme,
                          "nb_mots": len(texte.split())})
            moteurs.add(moteur)
        except Exception:
            continue
    return jsonify({"ok": True, "ajoutes": len(crees), "textes": crees,
                    "themes": themes,
                    "moteur": ", ".join(sorted(moteurs)) or "—"})


def _titre_unique(titre, texte, deja):
    """Garantit qu'aucun titre ne se répète dans la banque.

    Si le titre existe déjà, on le complète avec un mot marquant du texte —
    et seulement en dernier recours avec un numéro.
    """
    import re
    titre = (titre or "").strip() or "Texte à corriger"
    if titre.lower() not in deja:
        return titre

    # Un mot du texte, assez long pour être distinctif et absent du titre.
    mots = re.findall(r"[A-Za-zÀ-ÿœŒ'’-]{5,}", texte or "")
    bas_titre = titre.lower()
    for m in mots:
        if m.lower() not in bas_titre:
            essai = f"{titre} — {m.lower()}"
            if essai.lower() not in deja:
                return essai
    n = 2
    while f"{titre} ({n})".lower() in deja:
        n += 1
    return f"{titre} ({n})"


@app.post("/api/textes/fluence/proposer")
def fluence_proposer():
    """Propose des textes de lecture — inventés ou extraits littéraires.

    Rien n'est enregistré : l'enseignant valide chaque texte proposé.
    """
    import ai_generator as ai
    d = request.json or {}
    props, moteur, message = ai.proposer_textes_fluence(
        nombre=d.get("nombre", 3), niveau=int(d.get("niveau") or 2),
        litteraire=bool(d.get("litteraire")))
    return jsonify({"propositions": props, "moteur": moteur, "message": message})


@app.post("/api/textes/fluence/lot")
def fluence_enregistrer_lot():
    """Enregistre les textes de fluence validés par l'enseignant."""
    d = request.json or {}
    ajoutes = 0
    for t in (d.get("textes") or []):
        titre = (t.get("titre") or "").strip()
        contenu = (t.get("contenu") or t.get("texte") or "").strip()
        if not titre or not contenu:
            continue
        db.ajouter_texte_fluence(titre, contenu, int(t.get("niveau") or 2))
        ajoutes += 1
    return jsonify({"ok": True, "ajoutes": ajoutes})


@app.post("/api/textes/titre-auto")
def texte_titre_auto():
    """Propose un titre pour un texte saisi ou collé par l'enseignant."""
    import ai_generator as ai
    contenu = (request.json or {}).get("contenu", "")
    return jsonify({"titre": ai.titre_auto(contenu)})


@app.post("/api/corriger")
def corriger():
    """Corrige un texte quelconque (celui que l'élève vient de taper).

    C'est ce qui permet ensuite de ne signaler QUE de vraies erreurs.
    """
    texte = (request.json or {}).get("texte", "")
    r = corrector.corriger(texte)
    return jsonify({
        "reference": r.corrige, "moteur": r.moteur, "message": r.message,
        "fiable": r.fiable,
        "categories": {f"{f.lower()}|{j.lower()}": c for f, j, c in r.erreurs},
    })


@app.post("/api/analyser")
def analyser():
    """Repère les erreurs dans l'état actuel du texte de l'élève."""
    d = request.json or {}
    texte = d.get("texte", "")
    reference = d.get("reference", "")
    cats = {tuple(k.split("|", 1)): v for k, v in (d.get("categories") or {}).items()}

    sigs = corrector.analyser(texte, reference, cats)
    return jsonify({
        "mots": ce.compter_mots(texte),
        "phrases": ce.compter_phrases(texte),
        "certaines": len(ce.certaines(sigs)),
        "vigilances": len(ce.vigilances(sigs)),
        "par_categorie": ce.compter_par_categorie(sigs),
        "signalements": [{
            "debut": s.debut, "fin": s.fin, "mot": s.mot,
            "categorie": s.categorie, "message": s.message,
            "suggestion": s.suggestion, "certain": bool(s.certain),
        } for s in sigs],
    })


@app.get("/api/lecon/<categorie>")
def lecon(categorie):
    return jsonify(lh.lecon(categorie))


# ============================================================================
#  Fiches du classeur (Phase J) — les 70 mini-leçons réelles de l'enseignant,
#  rattachées aux 8 catégories d'erreurs. Routes ouvertes (élève ET enseignant
#  doivent pouvoir les consulter librement).
# ============================================================================
@app.get("/api/classeur/disponible")
def classeur_disponible():
    return jsonify({"disponible": lm.disponible()})


@app.get("/api/classeur/liste")
def classeur_liste():
    return jsonify(lm.liste(request.args.get("domaine")))


@app.get("/api/classeur/fiche/<lecon_id>")
def classeur_fiche(lecon_id):
    f = lm.fiche(lecon_id)
    if not f:
        return jsonify({"erreur": "fiche introuvable"}), 404
    return jsonify({**f, "css": lm.CSS_MANUEL})


@app.get("/api/classeur/pour-categorie/<categorie>")
def classeur_pour_categorie(categorie):
    fiches = lm.fiches_pour_categorie(categorie)
    return jsonify({"fiches": fiches, "css": lm.CSS_MANUEL})



@app.post("/api/aide")
def aide_guidee():
    """Aide en deux niveaux (question + indice) sur une erreur précise.

    Route ouverte aux élèves : elle ne révèle jamais la réponse toute faite.
    """
    d = request.json or {}
    return jsonify(aide_mod.aide(
        d.get("categorie", ""), d.get("mot", ""), d.get("correct", ""),
        d.get("contexte", ""), d.get("message", "")))


@app.post("/api/textes/corrige-auto")
def corrige_auto():
    """Fabrique automatiquement le corrigé d'un texte (pour la banque enseignant).

    Utilise l'IA si elle est active. Sans IA, les règles hors ligne ne savent pas
    produire un corrigé complet fiable : on le signale honnêtement à l'enseignant.
    """
    texte = (request.json or {}).get("contenu", "")
    r = corrector.corriger(texte)
    return jsonify({"corrige": r.corrige, "moteur": r.moteur,
                    "message": r.message, "fiable": r.fiable})


@app.get("/api/conjugaison")
def conjugaison():
    return jsonify(lh.CONJUGAISON)


# ============================================================================
#  Séances
# ============================================================================
@app.post("/api/seance/correction")
def seance_correction():
    d = request.json or {}
    try:
        rid = db.enregistrer_seance_correction(d)
        # Banque lexicale personnelle : alimentée avec les mots encore en
        # erreur (lexique/orthographe/homophone) à la fin de la séance.
        mots = d.get("mots_restants") or []
        if mots and d.get("eleve_id"):
            db.enregistrer_mots_travailler(d["eleve_id"], mots)
        return jsonify({"id": rid, "enregistre": True})
    except Exception as e:
        # Le bilan de l'élève ne doit JAMAIS disparaître à cause d'une erreur
        # d'enregistrement : le front affiche le bilan quoi qu'il arrive.
        return jsonify({"enregistre": False, "erreur": str(e)}), 200


@app.get("/api/eleve/<int:eleve_id>/banque-lexicale")
def banque_lexicale(eleve_id):
    return jsonify(db.banque_lexicale(eleve_id, request.args.get("tout") == "1"))


@app.post("/api/eleve/<int:eleve_id>/banque-lexicale/maitrise")
def banque_lexicale_maitrise(eleve_id):
    d = request.json or {}
    db.marquer_mot_maitrise(eleve_id, d.get("mot", ""), d.get("categorie", ""),
                             bool(d.get("maitrise", True)))
    return jsonify({"ok": True})


@app.post("/api/seance/fluence")
def seance_fluence():
    d = request.json or {}
    try:
        rid = db.enregistrer_seance_fluence(d)
        return jsonify({"id": rid, "enregistre": True})
    except Exception as e:
        return jsonify({"enregistre": False, "erreur": str(e)}), 200


@app.get("/api/eleve/<int:eid>/resume")
def resume_eleve(eid):
    c = db.seances_correction(eleve_id=eid)
    f = db.seances_fluence(eleve_id=eid)
    return jsonify({
        "corrections": len(c), "lectures": len(f),
        "meilleur_mclm": max((s["mclm"] for s in f), default=0),
        "dernier_mclm": f[0]["mclm"] if f else 0,
    })


# ============================================================================
#  Analyse enseignant
# ============================================================================
def moyenne(v):
    return round(statistics.mean(v), 1) if v else 0.0


def analyser_eleve(e):
    corr = db.seances_correction(eleve_id=e["id"])
    flu = db.seances_fluence(eleve_id=e["id"])
    dic = db.seances_dictee(eleve_id=e["id"])
    b = {"eleve": e, "nb_corr": len(corr), "nb_flu": len(flu),
         "nb_dictees": len(dic), "besoins": []}
    b["dictee_score"] = moyenne([d["score"] for d in dic]) if dic else 0
    b["dictee_orthographe"] = sum(d["err_orthographe"] for d in dic)
    b["dictee_ecoute"] = sum(d["err_ecoute"] for d in dic)
    b["dictee_courbe"] = [{"date": d["date_seance"][5:10], "valeur": d["score"]}
                          for d in reversed(dic)]

    if corr:
        b["taux_correction"] = moyenne(
            [(s["erreurs_avant"] - s["erreurs_apres"]) / s["erreurs_avant"] * 100
             for s in corr if s["erreurs_avant"]])
        autos = [s["corrigees_seul"] / t * 100 for s in corr
                 if (t := s["corrigees_seul"] + s["corrigees_avec_aide"])]
        b["autonomie"] = moyenne(autos)
        n = config.get("seuil_nb_seances", 3)
        cats = {}
        for s in corr[:n]:
            for c, v in s["detail_avant"].items():
                cats[c] = cats.get(c, 0) + v
        b["categories"] = cats
        b["progression"] = [
            {"date": s["date_seance"][5:10],
             "valeur": round((s["erreurs_avant"] - s["erreurs_apres"])
                             / s["erreurs_avant"] * 100) if s["erreurs_avant"] else 100}
            for s in reversed(corr)]
    else:
        b.update({"taux_correction": 0, "autonomie": 0, "categories": {},
                  "progression": []})

    niveau = e.get("classe_niveau") or config.get("fluence_niveau_classe", "CM1")
    b["repere"] = REPERES_MCLM.get(niveau, 90)
    if flu:
        b["mclm_moyen"] = moyenne([s["mclm"] for s in flu])
        b["mclm_dernier"] = flu[0]["mclm"]
        b["mclm_meilleur"] = max(s["mclm"] for s in flu)
        b["fluence"] = [{"date": s["date_seance"][5:10], "valeur": s["mclm"]}
                        for s in reversed(flu)]
    else:
        b.update({"mclm_moyen": 0, "mclm_dernier": 0, "mclm_meilleur": 0,
                  "fluence": []})

    # --- Besoins de suivi ---
    seuil = config.get("seuil_categorie_alerte", 3)
    for c, v in sorted(b["categories"].items(), key=lambda x: -x[1]):
        if v >= seuil:
            L = lh.lecon(c)
            b["besoins"].append({
                "domaine": "Écrit", "categorie": c,
                "gravite": "forte" if v >= seuil * 2 else "moyenne",
                "titre": f"{LIBELLES_CATEGORIES[c]} — {v} erreurs sur les "
                         f"{config.get('seuil_nb_seances', 3)} dernières séances",
                "remediation": L.get("titre", ""), "lecon_id": L.get("lecon_id", ""),
                "procedure": L.get("procedure", []),
            })
    if corr and b["autonomie"] < config.get("seuil_autonomie_faible", 50):
        b["besoins"].append({
            "domaine": "Méthode", "categorie": None, "gravite": "moyenne",
            "titre": f"Autonomie faible : {b['autonomie']:.0f} % des erreurs "
                     f"corrigées sans aide",
            "remediation": "Relecture ciblée : une seule catégorie à la fois",
            "lecon_id": "",
            "procedure": ["Faire relire l'élève en cherchant UNE catégorie à la fois.",
                          "Lui faire verbaliser à voix haute la procédure."],
        })
    if flu:
        ecart = (b["repere"] - b["mclm_moyen"]) / max(1, b["repere"]) * 100
        if ecart >= config.get("seuil_mclm_ecart", 25):
            b["besoins"].append({
                # « categorie » est renseignée : ce besoin peut désormais
                # constituer un groupe, au même titre que les erreurs écrites.
                "domaine": "Lecture", "categorie": "lecture_fluence",
                "gravite": "forte" if ecart >= 40 else "moyenne",
                "titre": f"Fluence insuffisante : {b['mclm_moyen']:.0f} mots/min "
                         f"(repère {b['repere']})",
                "remediation": "Lecture répétée (3 passages) + 5 min par jour",
                "lecon_id": "FR-LECT-FLU-01",
                "procedure": ["Relire 3 fois le même texte de niveau adapté.",
                              "Séance courte mais quotidienne."],
            })

    # --- Besoins repérés en dictée ---------------------------------------
    if dic:
        recentes = dic[:3]
        score_moyen = moyenne([d["score"] for d in recentes])
        if score_moyen < 60:
            b["besoins"].append({
                "domaine": "Dictée", "categorie": "dictee_score",
                "gravite": "forte" if score_moyen < 40 else "moyenne",
                "titre": f"Dictée : {score_moyen:.0f} % de mots justes "
                         f"sur les {len(recentes)} dernières",
                "remediation": "Mémorisation éclair des mots, puis redictée",
                "lecon_id": "ORTH-12",
                "procedure": ["Travailler la liste en flash cards avant la dictée.",
                              "Redicter les mêmes mots deux jours plus tard."],
            })
        # Beaucoup d'erreurs d'écoute : ce n'est pas de l'orthographe.
        ecoute = sum(d["err_ecoute"] for d in recentes)
        ortho = sum(d["err_orthographe"] for d in recentes)
        if ecoute >= 4 and ecoute > ortho:
            b["besoins"].append({
                "domaine": "Dictée", "categorie": "dictee_ecoute",
                "gravite": "forte",
                "titre": f"{ecoute} mot(s) non reconnus à l'oreille",
                "remediation": "Discrimination auditive — et vérifier l'audition",
                "lecon_id": "",
                "procedure": ["Faire répéter le mot par l'élève avant qu'il écrive.",
                              "Signaler au médecin scolaire si cela persiste."],
            })
    return b


@app.get("/api/prof/bord")
def prof_bord():
    cid = request.args.get("classe_id")
    cid = int(cid) if cid and cid != "0" else None
    corr = db.seances_correction(classe_id=cid)
    flu = db.seances_fluence(classe_id=cid)
    eleves = db.liste_eleves(classe_id=cid)

    cats = {}
    for s in corr:
        for c, v in s["detail_avant"].items():
            cats[c] = cats.get(c, 0) + v
    par_niveau = {}
    for s in flu:
        par_niveau.setdefault(s["niveau"], []).append(s["mclm"])

    autos = [s["corrigees_seul"] / t * 100 for s in corr
             if (t := s["corrigees_seul"] + s["corrigees_avec_aide"])]

    lignes = []
    # Profil de lecture : combien d'élèves se situent où par rapport au repère
    # de leur niveau de classe ? Bien plus parlant qu'une moyenne par niveau
    # de texte, qui dépendait surtout du texte choisi et non des élèves.
    profil = {"au_dela": 0, "atteint": 0, "fragile": 0, "difficulte": 0}
    reperes_vus, progressions = [], []
    for e in eleves:
        b = analyser_eleve(e)
        if b["nb_flu"]:
            rep = b["repere"] or 1
            reperes_vus.append(rep)
            ecart = b["mclm_moyen"] / rep * 100
            if ecart >= 110:
                profil["au_dela"] += 1
            elif ecart >= 90:
                profil["atteint"] += 1
            elif ecart >= 75:
                profil["fragile"] += 1
            else:
                profil["difficulte"] += 1
            # Progression : première lecture → dernière lecture.
            pts = b["fluence"]
            if len(pts) >= 2:
                progressions.append(pts[-1]["valeur"] - pts[0]["valeur"])
        if b["nb_corr"] or b["nb_flu"]:
            lignes.append({
                "id": e["id"], "prenom": e["prenom"], "classe": e["classe_nom"],
                "seances": b["nb_corr"] + b["nb_flu"],
                "taux": b["taux_correction"], "autonomie": b["autonomie"],
                "mclm": b["mclm_moyen"], "besoins": len(b["besoins"]),
            })

    repere_moyen = round(statistics.mean(reperes_vus)) if reperes_vus else \
        REPERES_MCLM.get(config.get("fluence_niveau_classe", "CM1"), 90)

    return jsonify({
        "fluence_profil": profil,
        "fluence_repere": repere_moyen,
        "fluence_nb_suivis": len(reperes_vus),
        "fluence_en_progres": sum(1 for x in progressions if x > 0),
        "fluence_nb_progressions": len(progressions),
        "fluence_gain_moyen": round(statistics.mean(progressions)) if progressions else 0,
        "eleves": len(eleves), "corrections": len(corr), "lectures": len(flu),
        "taux": moyenne([(s["erreurs_avant"] - s["erreurs_apres"])
                         / s["erreurs_avant"] * 100
                         for s in corr if s["erreurs_avant"]]),
        "autonomie": moyenne(autos),
        "mclm": moyenne([s["mclm"] for s in flu]),
        "par_categorie": cats,
        "fluence_par_niveau": {str(k): moyenne(v) for k, v in par_niveau.items()},
        "lignes": lignes,
    })


@app.get("/api/prof/eleve/<int:eid>")
def prof_eleve(eid):
    e = next((x for x in db.liste_eleves() if x["id"] == eid), None)
    if not e:
        return jsonify({"erreur": "élève inconnu"}), 404
    return jsonify(analyser_eleve(e))


@app.get("/api/prof/remediation")
def prof_remediation():
    tous, groupes = [], {}
    for e in db.liste_eleves():
        b = analyser_eleve(e)
        for bz in b["besoins"]:
            tous.append({"eleve_id": e["id"], "prenom": e["prenom"],
                         "classe": e["classe_nom"], **bz})
            if bz["categorie"]:
                groupes.setdefault(bz["categorie"], []).append(e["prenom"])
    tous.sort(key=lambda x: (x["gravite"] != "forte", x["prenom"]))
    return jsonify({"besoins": tous,
                    "groupes": {k: sorted(v) for k, v in groupes.items()}})


# ============================================================================
#  Réglages
# ============================================================================
@app.get("/api/reglages")
def get_reglages():
    return jsonify({"valeurs": config.tout(), "defauts": DEFAUTS})


@app.post("/api/reglages")
def set_reglages():
    for cle, val in (request.json or {}).items():
        if cle not in DEFAUTS:
            continue
        d = DEFAUTS[cle]
        if isinstance(d, bool):
            config.set(cle, bool(val))
        elif isinstance(d, int):
            try:
                config.set(cle, int(val))
            except (TypeError, ValueError):
                pass
        else:
            config.set(cle, val)
    config.sauver()
    return jsonify({"ok": True, "moteur": _etat_moteur()})


@app.get("/api/reglages/moteurs")
def reglages_moteurs():
    """Ce qu'il faut pour régler les deux moteurs IA et leur répartition."""
    import ia_client
    return jsonify({
        "principal": config.get("ia_moteur", "deepseek"),
        "secondaire": config.get("ia_moteur_secondaire", "aucun"),
        "taches": config.get("ia_taches", {}),
        "libelles_taches": ia_client.TACHES,
        "presets": ia_client.PRESETS,
        "nom_principal": ia_client.nom_moteur(config.get("ia_moteur")),
        "nom_secondaire": (ia_client.nom_moteur(config.get("ia_moteur_secondaire"))
                           if config.get("ia_moteur_secondaire", "aucun") != "aucun"
                           else ""),
    })


@app.post("/api/reglages/tester")
def tester_ia():
    """Teste un moteur avec les valeurs SAISIES À L'ÉCRAN.

    Le test ne lit pas la configuration enregistrée : sinon il faudrait
    enregistrer avant de pouvoir tester, ce qui est déroutant et donne des
    « 401 » incompréhensibles alors que la clé vient d'être collée.
    """
    import ia_client
    d = request.json or {}
    quel = d.get("moteur")

    # Valeurs éventuellement transmises depuis le formulaire, non enregistrées.
    url, cle, modele = d.get("url"), d.get("cle"), d.get("modele")

    if quel in ("api", "api2") or (url and cle):
        if quel == "api2" and not url:
            url, cle, modele = (config.get("ia_url_api2"),
                                config.get("ia_cle_api2"),
                                config.get("ia_modele_api2"))
        elif quel == "api" and not url:
            url, cle, modele = (config.get("ia_url_api"),
                                config.get("ia_cle_api_perso"),
                                config.get("ia_modele_api"))
        ok, msg = ia_client.tester(url, cle, modele)
        return jsonify({"ok": ok, "message": msg})

    if quel and quel not in ("principal", "aucun"):
        try:
            ia_client.appeler("Réponds uniquement par : ok", temperature=0.0,
                              max_tokens=20, moteur=quel)
            return jsonify({"ok": True,
                            "message": f"Connexion réussie ({ia_client.nom_moteur(quel)})."})
        except Exception as e:
            return jsonify({"ok": False, "message": ia_client.expliquer_erreur(e)})

    ok, msg = corrector.tester_moteur()
    return jsonify({"ok": ok, "message": msg})


@app.post("/api/reglages/modeles")
def reglages_modeles():
    """Liste les modèles auxquels la clé donne accès.

    C'est le moyen le plus sûr de vérifier une clé ET d'obtenir le nom exact
    des modèles à recopier — les noms varient d'un service à l'autre.
    """
    import ia_client
    d = request.json or {}
    modeles, erreur = ia_client.lister_modeles(d.get("url"), d.get("cle"))
    return jsonify({"ok": not erreur, "message": erreur, "modeles": modeles})


# ============================================================================
#  Pont Notes & Suivi
# ============================================================================
@app.get("/api/pont")
def pont_etat():
    return jsonify({"actif": ig.est_actif(), "url": ig.url(),
                    "ecoute_lan": bool(config.get("integration_ecoute_lan", False)),
                    "ecoute_lan_suspendue": bool(config.get("mode_salle", False)
                                                 and config.get("integration_ecoute_lan", False)),
                    "ip": reseau.ip_locale(),
                    "journal": db.journal(40)})


@app.post("/api/pont/<action>")
def pont_action(action):
    if action == "demarrer":
        ok, msg = ig.demarrer()
    elif action == "redemarrer":
        ok, msg = ig.redemarrer()
    else:
        ok, msg = ig.arreter()
    return jsonify({"ok": ok, "message": msg, "actif": ig.est_actif(),
                    "url": ig.url()})


@app.post("/api/export/<genre>")
def exporter(genre):
    if genre == "json":
        chemin = os.path.join(dossier_exports(), "pour_notes_et_suivi.json")
        ig.exporter_json(chemin)
    elif genre == "csv":
        chemin = os.path.join(dossier_exports(), "resultats_complets.csv")
        with open(chemin, "w", newline="", encoding="utf-8-sig") as fo:
            w = csv.writer(fo, delimiter=";")
            w.writerow(["Élève", "Classe", "Date", "Activité", "Note /100",
                        "Erreurs avant", "Erreurs après", "% sans aide",
                        "Aides utilisées", "MCLM"])
            for s in db.seances_correction():
                w.writerow([s["prenom"], s["classe_nom"], s["date_seance"],
                            "Autocorrection", ig.score_correction(s),
                            s["erreurs_avant"], s["erreurs_apres"],
                            ig.taux_autonomie(s), s.get("nb_aides", 0), ""])
            for s in db.seances_fluence():
                w.writerow([s["prenom"], s["classe_nom"], s["date_seance"],
                            "Fluence", ig.score_fluence(s), "", "", "", "", s["mclm"]])
    elif genre == "besoins":
        chemin = os.path.join(dossier_exports(), "besoins_de_suivi.csv")
        with open(chemin, "w", newline="", encoding="utf-8-sig") as fo:
            w = csv.writer(fo, delimiter=";")
            w.writerow(["Élève", "Classe", "Domaine", "Gravité", "Besoin",
                        "Remédiation", "Leçon"])
            for e in db.liste_eleves():
                for b in analyser_eleve(e)["besoins"]:
                    w.writerow([e["prenom"], e["classe_nom"], b["domaine"],
                                b["gravite"], b["titre"], b["remediation"],
                                b["lecon_id"]])
    else:
        return jsonify({"erreur": "type inconnu"}), 400
    return jsonify({"ok": True, "chemin": chemin})


# ============================================================================
#  Phase I — Sécurité (code PIN enseignant)
# ============================================================================
@app.get("/api/securite/etat")
def securite_etat():
    return jsonify({"defini": gestion_auth.pin_defini(),
                    "delai": gestion_auth.delai_verrou_min()})


@app.post("/api/securite/creer")
def securite_creer():
    try:
        code = gestion_auth.creer_pin((request.json or {}).get("pin", ""))
        return jsonify({"code_recuperation": code,
                        "jeton": gestion_auth.deverrouiller((request.json or {}).get("pin", ""))})
    except ValueError as e:
        return jsonify({"erreur": str(e)}), 400


@app.post("/api/securite/verifier")
def securite_verifier():
    jeton = gestion_auth.deverrouiller((request.json or {}).get("pin", ""))
    if jeton:
        return jsonify({"jeton": jeton})
    return jsonify({"erreur": "Code incorrect."}), 401


@app.post("/api/securite/recuperer")
def securite_recuperer():
    d = request.json or {}
    try:
        nouveau = gestion_auth.reinitialiser_par_recuperation(
            d.get("code", ""), d.get("pin", ""))
        return jsonify({"code_recuperation": nouveau,
                        "jeton": gestion_auth.deverrouiller(d.get("pin", ""))})
    except ValueError as e:
        return jsonify({"erreur": str(e)}), 400


@app.post("/api/securite/verrouiller")
def securite_verrouiller():
    gestion_auth.verrouiller(request.headers.get("X-Jeton", ""))
    return jsonify({"ok": True})


@app.post("/api/securite/delai")
def securite_delai():
    gestion_auth.definir_delai_verrou((request.json or {}).get("minutes", 15))
    return jsonify({"delai": gestion_auth.delai_verrou_min()})


@app.post("/api/securite/changer")
def securite_changer():
    d = request.json or {}
    try:
        gestion_auth.changer_pin(request.headers.get("X-Jeton", ""),
                                 d.get("ancien", ""), d.get("nouveau", ""))
        return jsonify({"ok": True})
    except (ValueError, PermissionError) as e:
        return jsonify({"erreur": str(e)}), 400


@app.post("/api/securite/supprimer")
def securite_supprimer():
    try:
        gestion_auth.supprimer_pin(request.headers.get("X-Jeton", ""))
        return jsonify({"ok": True})
    except PermissionError as e:
        return jsonify({"erreur": str(e)}), 400


# ============================================================================
#  Phase I — Sauvegardes
# ============================================================================
@app.get("/api/prof/sauvegardes")
def sauvegardes_liste():
    return jsonify({
        "sauvegardes": gestion_sauv.lister(),
        "externes": gestion_sauv.lister(externe=True),
        "externe": gestion_sauv.etat_externe(),
    })


@app.post("/api/prof/sauvegardes/creer")
def sauvegardes_creer():
    if gestion_sauv.sauvegarder("manuelle"):
        return jsonify({"ok": True,
                        "sauvegardes": gestion_sauv.lister(),
                        "externes": gestion_sauv.lister(externe=True),
                        "externe": gestion_sauv.etat_externe()})
    return jsonify({"erreur": "Sauvegarde impossible (disque ou permissions)."}), 500


@app.post("/api/prof/sauvegardes/restaurer")
def sauvegardes_restaurer():
    d = request.json or {}
    nom = d.get("nom", "")
    externe = bool(d.get("externe", False))
    if gestion_sauv.restaurer(nom, externe=externe):
        return jsonify({"ok": True})
    return jsonify({"erreur": "Restauration impossible."}), 400


@app.post("/api/prof/sauvegardes/externe")
def sauvegardes_externe_regler():
    """Règle le second dossier de sauvegarde (Nextcloud, clé USB…).

    On teste l'écriture AVANT d'enregistrer : inutile de laisser l'enseignant
    croire que ses copies partent quelque part si le dossier est inaccessible.
    """
    d = request.json or {}
    dossier = str(d.get("dossier", "") or "").strip()
    actif = bool(d.get("actif", False))
    nb = d.get("nb_conservees") or config.get("sauvegarde_externe_nb", 10)

    if actif:
        ok, message = sauvegarde.GestionnaireSauvegardes.tester_dossier(dossier)
        if not ok:
            return jsonify({"erreur": message}), 400

    config.set("sauvegarde_externe_dossier", dossier)
    config.set("sauvegarde_externe_active", actif)
    config.set("sauvegarde_externe_nb", nb)
    config.sauver()
    _appliquer_reglages_sauvegarde()

    # Dès l'activation, on met le dossier à jour sans attendre demain.
    copiees = gestion_sauv._copier_manquantes_externe() if actif else 0
    return jsonify({"ok": True, "copiees": copiees,
                    "externe": gestion_sauv.etat_externe(),
                    "externes": gestion_sauv.lister(externe=True)})


@app.post("/api/prof/sauvegardes/externe/tester")
def sauvegardes_externe_tester():
    """Teste un dossier SAISI À L'ÉCRAN, sans l'enregistrer."""
    dossier = (request.json or {}).get("dossier", "")
    ok, message = sauvegarde.GestionnaireSauvegardes.tester_dossier(dossier)
    return jsonify({"ok": ok, "message": message})


# ============================================================================
#  Phase I — Mode salle informatique (réseau + QR)
# ============================================================================
@app.get("/api/prof/reseau")
def reseau_etat():
    actif = bool(config.get("mode_salle", False))
    ip = reseau.ip_locale()
    url = reseau.url_acces(PORT_ACTUEL, ip)
    return jsonify({"actif": actif, "ip": ip, "url": url,
                    "qr": reseau.qr_svg(url) if actif else ""})


@app.post("/api/prof/reseau/basculer")
def reseau_basculer():
    config.set("mode_salle", bool((request.json or {}).get("actif", False)))
    config.sauver()
    # GARDE-FOU : le pont Portail (port 4100) ne doit jamais être ouvert au
    # réseau pendant le mode salle (réseau de l'école = élèves). On le
    # redémarre : hote_ecoute() le ramène d'office sur 127.0.0.1 tant que le
    # mode salle est actif, puis restaure l'écoute LAN éventuelle à la sortie.
    if ig.est_actif():
        ig.redemarrer()
        if config.get("mode_salle") and config.get("integration_ecoute_lan"):
            db.journaliser("pont-garde-fou",
                           "mode salle actif : écoute LAN du pont suspendue (127.0.0.1)")
    return reseau_etat()


# ============================================================================
#  Phase I — Devoirs (assignations)
# ============================================================================
@app.get("/api/prof/assignations")
def assignations_liste():
    return jsonify({"assignations": db.toutes_assignations()})


@app.post("/api/assignations")
def assignations_creer():
    d = request.json or {}
    db.assigner_texte(d.get("texte_id"), classe_id=d.get("classe_id"),
                      eleve_id=d.get("eleve_id"), consigne=d.get("consigne", ""))
    return jsonify({"ok": True, "assignations": db.toutes_assignations()})


@app.delete("/api/assignations/<int:aid>")
def assignations_supprimer(aid):
    db.supprimer_assignation(aid)
    return jsonify({"ok": True})


@app.get("/api/eleve/<int:eid>/devoirs")
def eleve_devoirs(eid):
    return jsonify({"devoirs": db.devoirs_eleve(eid)})


# ============================================================================
#  « Mon bilan » — le retour donné à l'ÉLÈVE sur ses réussites
#
#  Rien à voir avec le tableau de bord de l'enseignant : ici, tout est formulé
#  pour un enfant de 9 à 11 ans. On montre d'abord ce qui est réussi, ensuite
#  ce qui progresse, et jamais un classement avec les autres.
# ============================================================================
def _dictee_par_mode(dictees):
    """Combien de dictées et quel meilleur score, mode par mode."""
    import dictee as dct
    out = {}
    for cle, m in dct.MODES.items():
        liste = [d for d in dictees if (d.get("genre") or "mots") == cle]
        out[cle] = {
            "nom": m["nom"], "emoji": m["emoji"], "nb": len(liste),
            "meilleur": max((d["score"] for d in liste), default=0),
            "moyenne": round(statistics.mean([d["score"] for d in liste]))
                       if liste else 0,
            "niveau_max": max((d.get("niveau") or 1 for d in liste), default=0),
        }
    return out


def _badges_eleve(e):
    """Tous les badges d'un élève, calculés par le module dédié."""
    import badges as bg
    eid = e["id"]
    corr = db.seances_correction(eleve_id=eid)
    flu = db.seances_fluence(eleve_id=eid)
    dic = db.seances_dictee(eleve_id=eid)
    niveau = e.get("classe_niveau") or config.get("fluence_niveau_classe", "CM1")
    repere = REPERES_MCLM.get(niveau, 90)
    tous_mots = db.banque_lexicale(eid, inclure_maitrises=True)
    mots_appris = sum(1 for m in tous_mots if m.get("maitrise"))
    autos = [s["corrigees_seul"] / t * 100 for s in corr
             if (t := s["corrigees_seul"] + s["corrigees_avec_aide"])]
    trouves = len({r["mot_retenu"] for r in db.recherches_dico(eleve_id=eid)
                   if r.get("mot_retenu")})
    return bg.calculer(corr, flu, dic, repere, mots_appris,
                       moyenne(autos), trouves)


def _badges(corr, flu, repere, mots_appris, autonomie, dictees=()):
    """Ancienne version, conservée pour compatibilité — non utilisée."""
    nb_parfaits = sum(1 for s in corr if s["erreurs_avant"] and not s["erreurs_apres"])
    meilleur = max((s["mclm"] for s in flu), default=0)
    progres_lecture = (len(flu) >= 2 and flu[0]["mclm"] > flu[-1]["mclm"])
    dictee_parfaite = any(d["score"] == 100 for d in dictees)

    definitions = [
        ("premier", "🌱", "Je me lance", "Corriger un premier texte",
         len(corr) >= 1, len(corr), 1),
        ("cinq", "📚", "Bon lecteur de mes textes", "Corriger 5 textes",
         len(corr) >= 5, len(corr), 5),
        ("dix", "🏅", "Correcteur confirmé", "Corriger 10 textes",
         len(corr) >= 10, len(corr), 10),
        ("parfait", "✨", "Sans faute !", "Terminer un texte sans aucune erreur",
         nb_parfaits >= 1, nb_parfaits, 1),
        ("autonome", "🎯", "Je me débrouille seul", "Corriger 6 erreurs sur 10 sans aide",
         autonomie >= 60, round(autonomie), 60),
        ("lecteur", "📖", "Premier chrono", "Faire une lecture chronométrée",
         len(flu) >= 1, len(flu), 1),
        ("plus_vite", "🚀", "Je lis plus vite", "Battre son premier score de lecture",
         progres_lecture, 1 if progres_lecture else 0, 1),
        ("repere", "🏆", "Objectif atteint", f"Lire {repere} mots en une minute",
         meilleur >= repere, meilleur, repere),
        ("mots", "🎒", "Collectionneur de mots", "Apprendre 10 mots difficiles",
         mots_appris >= 10, mots_appris, 10),
        ("dictee", "✍️", "Première dictée", "Faire une dictée en entier",
         len(dictees) >= 1, len(dictees), 1),
        ("dictee_top", "🎖️", "Dictée sans faute", "Écrire tous les mots justes",
         dictee_parfaite, 1 if dictee_parfaite else 0, 1),
    ]
    return [{"cle": c, "emoji": e, "titre": t, "objectif": o,
             "obtenu": bool(ok), "valeur": v, "cible": cible}
            for (c, e, t, o, ok, v, cible) in definitions]


@app.get("/api/eleve/<int:eid>/bilan")
def eleve_bilan(eid):
    e = next((x for x in db.liste_eleves() if x["id"] == eid), None)
    if not e:
        return jsonify({"erreur": "élève inconnu"}), 404

    corr = db.seances_correction(eleve_id=eid)     # du plus récent au plus ancien
    flu = db.seances_fluence(eleve_id=eid)
    dictees = db.seances_dictee(eleve_id=eid)
    niveau = e.get("classe_niveau") or config.get("fluence_niveau_classe", "CM1")
    repere = REPERES_MCLM.get(niveau, 90)

    # --- Écriture ---
    taux = moyenne([(s["erreurs_avant"] - s["erreurs_apres"]) / s["erreurs_avant"] * 100
                    for s in corr if s["erreurs_avant"]])
    autos = [s["corrigees_seul"] / t * 100 for s in corr
             if (t := s["corrigees_seul"] + s["corrigees_avec_aide"])]
    autonomie = moyenne(autos)
    progression = [{"date": s["date_seance"][5:10],
                    "valeur": round((s["erreurs_avant"] - s["erreurs_apres"])
                                    / s["erreurs_avant"] * 100)
                    if s["erreurs_avant"] else 100}
                   for s in reversed(corr)]

    # --- Ce qui progresse : 3 dernières séances contre les 3 précédentes ---
    def cumul(seances):
        d = {}
        for s in seances:
            for c, v in s["detail_avant"].items():
                d[c] = d.get(c, 0) + v
        return d

    recentes, avant = cumul(corr[:3]), cumul(corr[3:6])
    n_rec, n_av = max(1, len(corr[:3])), max(1, len(corr[3:6]))
    evolution = []
    for c in set(list(recentes) + list(avant)):
        moy_rec = recentes.get(c, 0) / n_rec
        moy_av = avant.get(c, 0) / n_av
        if moy_rec or moy_av:
            evolution.append({
                "categorie": c, "libelle": LIBELLES_CATEGORIES.get(c, c),
                "avant": round(moy_av, 1), "maintenant": round(moy_rec, 1),
                "mieux": moy_rec < moy_av, "comparable": bool(corr[3:6]),
            })
    evolution.sort(key=lambda x: -x["maintenant"])

    # --- Lecture ---
    fluence = [{"date": s["date_seance"][5:10], "valeur": s["mclm"]}
               for s in reversed(flu)]
    meilleur = max((s["mclm"] for s in flu), default=0)
    dernier = flu[0]["mclm"] if flu else 0
    premier = flu[-1]["mclm"] if flu else 0

    # --- Banque de mots ---
    tous_mots = db.banque_lexicale(eid, inclure_maitrises=True)
    mots_appris = sum(1 for m in tous_mots if m.get("maitrise"))
    mots_restants = len(tous_mots) - mots_appris

    return jsonify({
        "prenom": e["prenom"],
        "classe": e.get("classe_nom", ""),
        "nb_corrections": len(corr),
        "nb_lectures": len(flu),
        "taux": round(taux),
        "autonomie": round(autonomie),
        "erreurs_corrigees_total": sum(
            max(0, s["erreurs_avant"] - s["erreurs_apres"]) for s in corr),
        "progression": progression,
        "evolution": evolution[:6],
        "fluence": fluence,
        "repere": repere,
        "mclm_dernier": dernier,
        "mclm_meilleur": meilleur,
        "mclm_gain": dernier - premier if len(flu) >= 2 else 0,
        "mots_appris": mots_appris,
        "mots_restants": mots_restants,
        # --- Dictée ---
        "nb_dictees": len(dictees),
        "dictee_score": round(statistics.mean([d["score"] for d in dictees]))
                        if dictees else 0,
        "dictee_meilleur": max((d["score"] for d in dictees), default=0),
        "dictee_courbe": [{"date": d["date_seance"][5:10], "valeur": d["score"]}
                          for d in reversed(dictees)],
        "dictee_orthographe": sum(d["err_orthographe"] for d in dictees),
        "dictee_ecoute": sum(d["err_ecoute"] for d in dictees),
        "dictee_par_mode": _dictee_par_mode(dictees),
        "badges": _badges_eleve(e),
        "badges_resume": __import__("badges").resume(_badges_eleve(e)),
        "objectif": db.objectif_eleve(eid),
        # Les catégories à retravailler, pour proposer LA bonne leçon.
        "a_travailler": [x["categorie"] for x in evolution[:3]
                         if x["maintenant"] >= 1],
    })


# ============================================================================
#  Dictionnaire par consonance
#
#  L'élève écrit le mot comme il l'entend ; on lui propose ce qui sonne
#  pareil, et il choisit lui-même en lisant les définitions. Routes ouvertes :
#  l'élève doit y accéder sans code.
# ============================================================================
@app.get("/api/dico/etat")
def dico_etat():
    import dictionnaire as dico
    return jsonify({
        "disponible": dico.disponible(),
        "nb_mots": dico.nombre_de_mots(),
        "definitions_memorisees": db.nb_definitions_memorisees(),
        "ia_active": bool(config.get("ia_active")),
    })


@app.post("/api/dico/chercher")
def dico_chercher():
    import dictionnaire as dico
    d = request.json or {}
    essai = (d.get("essai") or "").strip()
    resultats = dico.chercher(essai, int(d.get("limite") or 10))
    # On trace la recherche : savoir ce que les élèves cherchent est une
    # information pédagogique, pas une surveillance (aucun texte n'est stocké).
    try:
        db.journaliser_recherche(d.get("eleve_id"), essai,
                                 trouve=1 if resultats else 0,
                                 depuis=d.get("depuis") or "dictionnaire")
    except Exception:
        pass
    return jsonify({
        "essai": essai,
        "sons": __import__("phonetique").sons(essai),
        "resultats": resultats,
        "bien_ecrit": dico.existe(essai),
    })


@app.post("/api/dico/definition")
def dico_definition():
    """La définition d'un mot, avec sa nature et sa famille.

    Ordre de recherche : mémoire de l'application → banque intégrée → IA.
    Toute définition obtenue est mémorisée pour la classe entière.
    """
    import dictionnaire as dico
    d = request.json or {}
    mot = (d.get("mot") or "").strip().lower()
    if not mot:
        return jsonify({"erreur": "aucun mot"}), 400

    infos = dico.infos(mot) or {}
    nature = infos.get("nature", "")

    memo = db.definition_memorisee(mot)
    if memo:
        definition, source = memo["definition"], memo["source"] or "memoire"
    else:
        definition = dico.definition_hors_ligne(mot)
        source = "banque" if definition else ""
        if not definition:
            definition = dico.definition_ia(mot, nature)
            source = "ia" if definition else ""
            # Seules les définitions obtenues par l'IA méritent d'être
            # mémorisées : celles de la banque sont déjà là, hors ligne.
            if definition:
                db.memoriser_definition(mot, definition, nature, source)

    # On garde la trace du mot finalement retenu par l'élève.
    if d.get("eleve_id") and d.get("essai"):
        try:
            db.journaliser_recherche(d["eleve_id"], d["essai"], mot_retenu=mot,
                                     trouve=1, depuis=d.get("depuis") or "dictionnaire")
        except Exception:
            pass

    return jsonify({
        "mot": mot,
        "nature": nature,
        "definition": definition or "",
        "source": source,
        "famille": dico.famille(mot),
        "sons": __import__("phonetique").sons(mot),
        # Sans définition disponible, on le dit franchement plutôt que
        # d'afficher un vide inexpliqué.
        "message": "" if definition else (
            "Ce mot n'a pas encore de définition ici. Regarde sa nature et les "
            "mots de sa famille : ils aident souvent à reconnaître le bon mot."),
    })


# ============================================================================
#  Lecture en autonomie : la voix de l'élève est transcrite, puis comparée
#  au texte. Route ouverte (l'élève doit pouvoir s'en servir seul), mais elle
#  ne fait rien tant que l'enseignant n'a pas activé la fonction.
# ============================================================================
@app.get("/api/fluence/auto/etat")
def fluence_auto_etat():
    import transcription
    return jsonify(transcription.etat())


@app.post("/api/fluence/auto/analyser")
def fluence_auto_analyser():
    """Reçoit l'enregistrement, le transcrit, et compare au texte attendu."""
    import transcription
    if not transcription.disponible():
        return jsonify({"ok": False,
                        "message": "La lecture en autonomie n'est pas activée."})

    fichier = request.files.get("audio")
    if not fichier:
        return jsonify({"ok": False, "message": "Aucun enregistrement reçu."}), 400

    texte_id = request.form.get("texte_id")
    reference = request.form.get("reference") or ""
    if texte_id and not reference:
        t = next((x for x in db.liste_textes_fluence(actifs_seulement=False)
                  if str(x["id"]) == str(texte_id)), None)
        reference = (t or {}).get("contenu", "")
    if not reference.strip():
        return jsonify({"ok": False, "message": "Texte de référence introuvable."}), 400

    try:
        secondes = float(request.form.get("secondes") or 0)
    except ValueError:
        secondes = 0.0

    octets = fichier.read()
    # Garde-fou : un enregistrement démesuré est refusé avant tout envoi.
    if len(octets) > 12 * 1024 * 1024:
        return jsonify({"ok": False,
                        "message": "Enregistrement trop long (12 Mo maximum)."})

    resultat = transcription.analyser(reference, octets, secondes,
                                      fichier.filename or "lecture.webm")
    # L'audio n'est jamais conservé : il a servi, il disparaît.
    del octets
    return jsonify(resultat)


@app.post("/api/prof/stt/tester")
def prof_stt_tester():
    """Teste le service de transcription avec les valeurs SAISIES À L'ÉCRAN."""
    import struct
    import transcription
    d = request.json or {}
    url = d.get("url") or config.get("stt_url")
    cle = d.get("cle") or config.get("stt_cle")
    modele = d.get("modele") or config.get("stt_modele")

    if not (url or "").strip():
        return jsonify({"ok": False, "message": "Renseignez l'adresse de l'API."})
    if not (cle or "").strip():
        return jsonify({"ok": False, "message": "Renseignez la clé d'accès."})

    # Un WAV d'une demi-seconde de silence : de quoi vérifier la connexion.
    donnees = b"\x00\x00" * 8000
    entete = (b"RIFF" + struct.pack("<I", 36 + len(donnees)) + b"WAVEfmt "
              + struct.pack("<IHHIIHH", 16, 1, 1, 16000, 32000, 2, 16)
              + b"data" + struct.pack("<I", len(donnees)))
    _texte, message = transcription.transcrire(
        entete + donnees, "test.wav", url=url, cle=cle, modele=modele)
    # Une transcription vide sur du silence est le résultat NORMAL : cela
    # prouve justement que le service a répondu.
    if message and "vide" not in message:
        return jsonify({"ok": False, "message": message})
    return jsonify({"ok": True, "message": "Le service répond correctement."})


@app.get("/api/prof/devoirs-suggeres")
def prof_devoirs_suggeres():
    """Ce que l'analyse conseille de donner à faire, élève par élève.

    L'idée : au lieu que l'enseignant lise les tableaux et décide, l'analyse
    propose directement l'activité de reprise adaptée. Il valide d'un clic, et
    l'élève la trouve « à faire » à sa prochaine connexion.
    """
    cid = request.args.get("classe_id")
    cid = int(cid) if cid and cid != "0" else None
    suggestions = []

    for e in db.liste_eleves(classe_id=cid):
        b = analyser_eleve(e)
        if not (b["nb_corr"] or b["nb_flu"] or b["nb_dictees"]):
            continue
        pistes = []

        # 1. Trop de mots en attente dans sa banque → mémorisation éclair.
        mots = db.banque_lexicale(e["id"])
        if len(mots) >= 5:
            pistes.append({
                "genre": "flash", "titre": "Mémoriser ses mots (flash cards)",
                "motif": f"{len(mots)} mots en attente dans sa banque",
                "urgence": 2 if len(mots) >= 10 else 1,
            })

        # 2. Beaucoup d'erreurs non déductibles → dictée ciblée.
        dic = db.seances_dictee(eleve_id=e["id"])
        if mots and (not dic or dic[0]["score"] < 70):
            pistes.append({
                "genre": "dictee", "titre": "Une dictée sur ses mots",
                "motif": (f"dernière dictée à {dic[0]['score']} %"
                          if dic else "aucune dictée faite"),
                "urgence": 2 if (dic and dic[0]["score"] < 50) else 1,
            })

        # 3. Une catégorie d'erreur domine → texte à corriger + leçon.
        cats = b.get("categories") or {}
        if cats:
            pire = max(cats, key=cats.get)
            if cats[pire] >= config.get("seuil_categorie_alerte", 3):
                lecon = lm.fiche_principale(pire) if lm.disponible() else None
                pistes.append({
                    "genre": "lecon", "titre": f"Revoir : {LIBELLES_CATEGORIES[pire]}",
                    "motif": f"{cats[pire]} erreurs sur les séances récentes",
                    "categorie": pire,
                    "lecon_id": lecon["lecon_id"] if lecon else "",
                    "lecon_titre": lecon.get("titre", "") if lecon else "",
                    "urgence": 2,
                })

        # 4. Fluence en retrait → lecture répétée.
        if b["nb_flu"] and b["repere"]:
            ecart = (b["repere"] - b["mclm_moyen"]) / max(1, b["repere"]) * 100
            if ecart >= config.get("seuil_mclm_ecart", 25):
                pistes.append({
                    "genre": "fluence", "titre": "Lecture répétée",
                    "motif": f"{b['mclm_moyen']:.0f} mots/min pour un repère "
                             f"de {b['repere']}",
                    "urgence": 2 if ecart >= 40 else 1,
                })

        if pistes:
            pistes.sort(key=lambda p: -p["urgence"])
            suggestions.append({
                "eleve_id": e["id"], "prenom": e["prenom"],
                "classe": e.get("classe_nom", ""), "pistes": pistes,
            })

    suggestions.sort(key=lambda s: -max(p["urgence"] for p in s["pistes"]))
    return jsonify({"suggestions": suggestions,
                    "libelles": {"flash": "Mémorisation éclair",
                                 "dictee": "Dictée",
                                 "lecon": "Leçon + texte à corriger",
                                 "fluence": "Lecture répétée"}})


@app.post("/api/prof/devoirs-suggeres/assigner")
def prof_devoirs_assigner():
    """Transforme une suggestion en devoir réellement assigné à l'élève."""
    d = request.json or {}
    eid = d.get("eleve_id")
    genre = d.get("genre")
    if not eid or not genre:
        return jsonify({"erreur": "données manquantes"}), 400

    # Pour une leçon, on assigne aussi un texte portant sur la difficulté.
    texte_id = None
    if genre == "lecon":
        textes = db.liste_textes_correction()
        if textes:
            texte_id = textes[0]["id"]

    db.assigner_activite(eid, genre, categorie=d.get("categorie", ""),
                         lecon_id=d.get("lecon_id", ""), texte_id=texte_id,
                         consigne=d.get("titre", ""))
    return jsonify({"ok": True})


@app.get("/api/eleve/<int:eid>/a-faire")
def eleve_a_faire(eid):
    """Ce que l'élève doit faire en priorité, décidé par son enseignant."""
    return jsonify({"activites": db.activites_assignees(eid)})


@app.post("/api/eleve/<int:eid>/a-faire/<int:aid>/termine")
def eleve_a_faire_termine(eid, aid):
    db.terminer_activite(aid)
    return jsonify({"ok": True})


@app.get("/api/prof/dico/recherches")
def prof_dico_recherches():
    """Ce que les élèves cherchent : matière première pour la remédiation."""
    import collections
    cid = request.args.get("classe_id")
    cid = int(cid) if cid and cid != "0" else None
    lignes = db.recherches_dico(classe_id=cid, limite=1500)

    par_mot = collections.Counter()
    par_essai = collections.Counter()
    echecs = collections.Counter()
    for r in lignes:
        if r["mot_retenu"]:
            par_mot[r["mot_retenu"]] += 1
        elif r["essai"]:
            par_essai[r["essai"]] += 1
        if not r["trouve"] and r["essai"]:
            echecs[r["essai"]] += 1

    return jsonify({
        "total": len(lignes),
        "mots_cherches": [{"mot": m, "n": n} for m, n in par_mot.most_common(30)],
        "essais_sans_choix": [{"mot": m, "n": n} for m, n in par_essai.most_common(20)],
        "sans_resultat": [{"mot": m, "n": n} for m, n in echecs.most_common(20)],
        "recentes": lignes[:40],
    })


# ============================================================================
#  Dictée adaptée — fabriquée à partir des erreurs de CET élève
# ============================================================================
@app.get("/api/dictee/modes")
def dictee_modes():
    import dictee
    return jsonify({"modes": dictee.MODES})


@app.get("/api/eleve/<int:eid>/dictee")
def eleve_dictee(eid):
    import dictee
    e = next((x for x in db.liste_eleves() if x["id"] == eid), None)
    if not e:
        return jsonify({"erreur": "élève inconnu"}), 404

    # Sa difficulté principale sert de complément si sa banque est trop maigre.
    bilan_eleve = analyser_eleve(e)
    cats = bilan_eleve.get("categories") or {}
    faible = max(cats, key=cats.get) if cats else "orthographe"

    mode = request.args.get("mode") or "mots"
    niveau = int(request.args.get("niveau") or 2)
    items, explication_mode = dictee.preparer_mode(
        eid, mode=mode, niveau=niveau, categorie_faible=faible)

    origines = {}
    for i in items:
        origines[i["origine"]] = origines.get(i["origine"], 0) + 1
    return jsonify({
        "prenom": e["prenom"],
        "mode": mode, "niveau": niveau,
        "mots": items,
        "origines": origines,
        "categorie_faible": faible,
        "explication_mode": explication_mode,
        # Ce que l'élève doit comprendre : cette dictée est LA SIENNE.
        "explication": _explication_dictee(origines),
    })


# ============================================================================
#  Banque de dictées (module enseignant)
# ============================================================================
@app.get("/api/prof/banque-dictee")
def prof_banque_dictee():
    genre = request.args.get("genre")
    return jsonify({
        "elements": db.banque_dictee(genre=genre),
        "comptes": db.compter_banque_dictee(),
    })


@app.post("/api/prof/banque-dictee/generer")
def prof_banque_dictee_generer():
    """Propose des éléments fabriqués par l'IA — rien n'est encore enregistré."""
    import dictee
    d = request.json or {}
    liste, message = dictee.generer_banque_ia(
        genre=d.get("genre", "mots"), niveau=int(d.get("niveau") or 2),
        nombre=int(d.get("nombre") or 20), theme=(d.get("theme") or "").strip())
    return jsonify({"ok": bool(liste), "propositions": liste, "message": message})


@app.post("/api/prof/banque-dictee")
def prof_banque_dictee_ajouter():
    """Enregistre les éléments validés par l'enseignant."""
    d = request.json or {}
    genre = d.get("genre", "mots")
    niveau = int(d.get("niveau") or 2)
    ajoutes = 0
    for contenu in (d.get("elements") or []):
        ajoutes += db.ajouter_banque_dictee(
            genre, contenu, niveau, d.get("categorie", ""),
            d.get("source", "ia"))
    return jsonify({"ok": True, "ajoutes": ajoutes,
                    "comptes": db.compter_banque_dictee()})


@app.delete("/api/prof/banque-dictee/<int:bid>")
def prof_banque_dictee_supprimer(bid):
    db.supprimer_banque_dictee(bid)
    return jsonify({"ok": True})


@app.post("/api/dictee/verifier-groupe")
def dictee_verifier_groupe():
    """Corrige une expression ou une phrase, mot par mot."""
    import dictee
    d = request.json or {}
    return jsonify(dictee.verifier_groupe(d.get("attendu", ""), d.get("saisi", "")))


# ============================================================================
#  Objectifs personnels — l'élève choisit de viser plus haut
# ============================================================================
@app.get("/api/eleve/<int:eid>/objectif")
def eleve_objectif(eid):
    return jsonify(db.objectif_eleve(eid))


@app.post("/api/eleve/<int:eid>/objectif")
def eleve_objectif_maj(eid):
    d = request.json or {}
    db.definir_objectif(eid, mclm=d.get("mclm_vise"), dictee=d.get("dictee_visee"))
    return jsonify(db.objectif_eleve(eid))


# ============================================================================
#  Impression : badges sur étiquettes, leçons en cartes
# ============================================================================
@app.get("/api/prof/impression/planches")
def impression_planches():
    import etiquettes
    return jsonify({
        "badges": etiquettes.planches("badges"),
        "lecons": etiquettes.planches("lecons"),
    })


@app.get("/api/prof/badges/classe")
def prof_badges_classe():
    """Tous les badges obtenus, élève par élève : matière à imprimer."""
    cid = request.args.get("classe_id")
    cid = int(cid) if cid and cid != "0" else None
    sortie = []
    for e in db.liste_eleves(classe_id=cid):
        b = _badges_eleve(e)
        obtenus = [x for x in b if x["obtenu"]]
        if obtenus:
            sortie.append({
                "eleve_id": e["id"], "prenom": e["prenom"],
                "classe": e.get("classe_nom", ""),
                "badges": [{"cle": x["cle"], "emoji": x["emoji"],
                            "titre": x["titre"], "objectif": x["objectif"],
                            "couleur": x["couleur"], "famille": x["famille_nom"]}
                           for x in obtenus],
            })
    return jsonify({"eleves": sortie})


@app.post("/api/prof/impression/badges")
def impression_badges():
    """Écrit la planche de badges et l'ouvre dans le navigateur."""
    import re
    import webbrowser
    from pathlib import Path
    import etiquettes
    d = request.json or {}
    items = d.get("badges") or []
    if not items:
        return jsonify({"erreur": "aucun badge sélectionné"}), 400
    html = etiquettes.html_badges(
        items, planche=d.get("planche", "L7159"),
        decalage=(float(d.get("dx") or 0), float(d.get("dy") or 0)),
        depart=int(d.get("depart") or 0))
    chemin = Path(dossier_exports()) / "badges_a_imprimer.html"
    chemin.write_text(html, encoding="utf-8")
    threading.Thread(target=lambda: webbrowser.open(chemin.as_uri()),
                     daemon=True).start()
    return jsonify({"ok": True, "chemin": str(chemin), "nombre": len(items)})


@app.post("/api/prof/impression/lecons")
def impression_lecons():
    """Écrit la planche de leçons en cartes et l'ouvre dans le navigateur."""
    import webbrowser
    from pathlib import Path
    import etiquettes
    d = request.json or {}
    ids = d.get("lecons") or []
    fiches = []
    for lid in ids:
        f = lm.fiche(lid)
        if f:
            fiches.append({"titre": f.get("titre", ""), "html": f.get("html", "")})
    if not fiches:
        return jsonify({"erreur": "aucune leçon sélectionnée"}), 400
    html = etiquettes.html_lecons(
        fiches, lm.CSS_MANUEL, planche=d.get("planche", "A7"),
        decalage=(float(d.get("dx") or 0), float(d.get("dy") or 0)))
    chemin = Path(dossier_exports()) / "lecons_a_plastifier.html"
    chemin.write_text(html, encoding="utf-8")
    threading.Thread(target=lambda: webbrowser.open(chemin.as_uri()),
                     daemon=True).start()
    return jsonify({"ok": True, "chemin": str(chemin), "nombre": len(fiches)})


def _explication_dictee(origines):
    morceaux = []
    if origines.get("banque"):
        morceaux.append(f"{origines['banque']} mot(s) que tu rates souvent")
    if origines.get("dictionnaire"):
        morceaux.append(f"{origines['dictionnaire']} mot(s) que tu as cherché(s) "
                        f"au dictionnaire")
    if origines.get("categorie"):
        morceaux.append(f"{origines['categorie']} mot(s) sur ta difficulté "
                        f"du moment")
    if origines.get("courant"):
        morceaux.append(f"{origines['courant']} mot(s) courant(s)")
    if not morceaux:
        return "Une dictée pour t'entraîner."
    return "Cette dictée contient " + ", ".join(morceaux) + "."


@app.post("/api/dictee/verifier")
def dictee_verifier():
    """Corrige un mot et explique l'écart (orthographe / écoute / accent)."""
    import dictee
    d = request.json or {}
    return jsonify(dictee.verifier(d.get("attendu", ""), d.get("saisi", "")))


@app.post("/api/dictee/phrase")
def dictee_phrase():
    """Une phrase contenant le mot, pour le dicter en contexte."""
    import dictee
    d = request.json or {}
    mot = (d.get("mot") or "").strip()
    phrase = dictee.phrase_contenant(mot)
    if not phrase and d.get("ia"):
        phrase = dictee.phrase_ia([mot])
    return jsonify({"mot": mot, "phrase": phrase or ""})


@app.post("/api/seance/dictee")
def seance_dictee():
    """Enregistre la dictée et met à jour la banque de mots de l'élève."""
    import dictee
    d = request.json or {}
    eid = d.get("eleve_id")
    reponses = d.get("reponses") or []
    if not eid or not reponses:
        return jsonify({"enregistre": False, "erreur": "données manquantes"}), 400

    b = dictee.bilan(reponses)
    genres = b["par_genre"]
    try:
        db.enregistrer_seance_dictee({
            "eleve_id": eid, "nb_mots": b["total"], "nb_justes": b["justes"],
            "score": b["score"],
            "err_orthographe": genres.get("orthographe", 0) + genres.get("proche", 0),
            "err_ecoute": genres.get("ecoute", 0),
            "err_accent": genres.get("accent", 0) + genres.get("ponctuation", 0),
            "detail": reponses, "duree_secondes": int(d.get("duree_secondes") or 0),
            "genre": d.get("mode") or "mots", "niveau": int(d.get("niveau") or 2),
        })
    except Exception as e:
        return jsonify({"enregistre": False, "erreur": str(e)}), 500

    # Un mot écrit juste sort de la banque ; un mot raté y entre ou y reste.
    try:
        rates = [{"mot": r["attendu"], "categorie": r.get("categorie", "orthographe")}
                 for r in reponses if not r.get("juste") and r.get("attendu")]
        if rates:
            db.enregistrer_mots_travailler(eid, rates)
        for r in reponses:
            if r.get("juste") and r.get("attendu"):
                db.marquer_mot_maitrise(eid, r["attendu"],
                                        r.get("categorie", "orthographe"), True)
    except Exception:
        pass

    return jsonify({"enregistre": True, "bilan": b})


# ============================================================================
#  Cloisonnement de l'espace élève
# ============================================================================
TOUTES_ACTIVITES = ["correction", "fluence", "banque", "dico", "dictee"]


def activites_de_la_classe(classe_id):
    """Activités autorisées pour une classe (repli : le réglage général)."""
    par_classe = config.get("activites_par_classe", {}) or {}
    generales = config.get("activites_autorisees", TOUTES_ACTIVITES)
    valeurs = par_classe.get(str(classe_id), generales)
    return [a for a in valeurs if a in TOUTES_ACTIVITES] or TOUTES_ACTIVITES


@app.get("/api/eleve/<int:eid>/acces")
def eleve_acces(eid):
    """Ce à quoi CET élève a droit : activités ouvertes, mode verrouillé.

    C'est le serveur qui décide, pas l'interface : même en bricolant la page,
    un élève ne peut pas s'ouvrir une activité fermée.
    """
    e = next((x for x in db.liste_eleves() if x["id"] == eid), None)
    if not e:
        return jsonify({"erreur": "élève inconnu"}), 404
    return jsonify({
        "eleve_id": eid,
        "prenom": e["prenom"],
        "classe_id": e.get("classe_id"),
        "verrouille": bool(config.get("eleve_verrouille", False)),
        "activites": activites_de_la_classe(e.get("classe_id")),
        "sources": {
            "saisie_libre": bool(config.get("source_saisie_libre", True)),
            "texte_impose": bool(config.get("source_texte_impose", True)),
            "generation_ia": bool(config.get("source_generation_ia", True)),
        },
    })


@app.get("/api/prof/activites")
def prof_activites():
    """État des activités autorisées, classe par classe (écran Réglages)."""
    classes = db.liste_classes()
    return jsonify({
        "verrouille": bool(config.get("eleve_verrouille", False)),
        "generales": config.get("activites_autorisees", TOUTES_ACTIVITES),
        "par_classe": config.get("activites_par_classe", {}) or {},
        "classes": [{"id": c["id"], "nom": c["nom"],
                     "activites": activites_de_la_classe(c["id"])}
                    for c in classes],
        "libelles": {"correction": "Je me corrige",
                     "fluence": "Je lis à voix haute",
                     "banque": "Ma banque de mots",
                     "dico": "Mon dictionnaire",
                     "dictee": "Ma dictée"},
    })


@app.post("/api/prof/activites")
def prof_activites_maj():
    d = request.json or {}
    if "verrouille" in d:
        config.set("eleve_verrouille", bool(d["verrouille"]))
    if "generales" in d:
        config.set("activites_autorisees",
                   [a for a in (d["generales"] or []) if a in TOUTES_ACTIVITES])
    if "par_classe" in d:
        propre = {}
        for cid, liste in (d["par_classe"] or {}).items():
            propre[str(cid)] = [a for a in (liste or []) if a in TOUTES_ACTIVITES]
        config.set("activites_par_classe", propre)
    config.sauver()
    return prof_activites()


# ============================================================================
#  Phase I — Fiches d'exercices ciblées
# ============================================================================
@app.post("/api/prof/fiche")
def prof_fiche():
    d = request.json or {}
    prenom = d.get("prenom", "")
    genre = d.get("genre") or "exercices"
    nombre = int(d.get("nombre") or 6)

    if genre == "fluence":
        # Fiche de lecture répétée : un texte court + trois passages chronométrés.
        f = exercices.fiche_fluence(prenom, db, config)
        cat = "lecture"
    elif genre == "dictee":
        f = exercices.fiche_dictee(prenom, d.get("eleve_id"))
        cat = "memorisation"
    elif genre == "methode":
        f = exercices.fiche_methode(prenom)
        cat = "methode"
    else:
        cat = d.get("categorie") or exercices.categorie_faible(d.get("eleve_id"))
        f = exercices.fiche(prenom, cat, nombre, groupe=bool(d.get("groupe")))

    # pywebview ne sait pas ouvrir window.open : on écrit la fiche sur disque et
    # on l'ouvre dans le navigateur du système, où l'impression fonctionne.
    import re
    import webbrowser
    from pathlib import Path
    nom = re.sub(r"[^A-Za-z0-9]+", "_", f"{prenom}_{cat}").strip("_") or "fiche"
    chemin = Path(dossier_exports()) / f"fiche_{nom}.html"
    chemin.write_text(exercices.html_fiche(f), encoding="utf-8")
    # Ouverture non bloquante dans le navigateur du système (où l'impression marche).
    threading.Thread(
        target=lambda: webbrowser.open(chemin.as_uri()), daemon=True).start()
    return jsonify({"fiche": f, "chemin": str(chemin)})


# ============================================================================
#  Phase I — Pilotage avancé (régression, heatmap, badge)
# ============================================================================
@app.get("/api/prof/heatmap")
def prof_heatmap():
    cid = request.args.get("classe_id")
    cid = int(cid) if cid and cid != "0" else None
    return jsonify({"heatmap": pilotage.heatmap(cid),
                    "libelles": LIBELLES_CATEGORIES})


@app.get("/api/prof/regressions")
def prof_regressions():
    return jsonify({"regressions": pilotage.regressions(),
                    "libelles": LIBELLES_CATEGORIES})


@app.get("/api/prof/badge")
def prof_badge():
    return jsonify(pilotage.besoins_nouveaux(config))


# ============================================================================
#  Démarrage
# ============================================================================
def demarrer(port=5173):
    global PORT_ACTUEL
    PORT_ACTUEL = port
    # Mode salle informatique : on écoute toutes les interfaces (réseau local).
    hote = "0.0.0.0" if config.get("mode_salle", False) else "127.0.0.1"
    t = threading.Thread(
        target=lambda: app.run(host=hote, port=port, debug=False,
                               use_reloader=False, threaded=True),
        daemon=True)
    t.start()
    return f"http://127.0.0.1:{port}"
