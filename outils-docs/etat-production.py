#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
État de production des jeux, pour le tableau de bord de l'enseignant (enseignant.html, rubrique « Production »).

    python outils-docs/etat-production.py          écrit commun/donnees/production.js (lu par le site en ligne)
    python outils-docs/etat-production.py --json   affiche l'état (JSON)

serveur.py appelle aussi etat() pour /api/production (état recalculé en direct sur ce PC).
Pour chaque jeu du catalogue : variante immersive et grades, médias manquants (medias.csv), voix mp3,
leçons A4, évaluations imprimables, affiche, bande-annonce, points ouverts de A-VERIFIER.md, médias
sans crédit (diffusion/AUDIT-MEDIAS.md), jeu sensible ; puis l'état « fini » (définition C1 de la
stratégie du 14/11/2026) et la file « À relire ». Aucune donnée d'élève. Python 3.6+, sans dépendance.
"""
import csv, datetime, json, os, re, sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Jeux sensibles : relecture de l'enseignant obligatoire avant la classe (règles du dépôt).
SENSIBLES = {
    "traite-colonies": "RELECTURE OBLIGATOIRE avant la classe (traite, esclavage)",
    "grande-guerre": "RELECTURE OBLIGATOIRE avant la classe (Première Guerre mondiale)",
    "seconde-guerre": "RELECTURE OBLIGATOIRE avant la classe (Seconde Guerre mondiale, persécutions)",
    "etats-matiere": "Formulations sensibles à relire",
}
IMAGES = (".webp", ".jpg", ".jpeg", ".png", ".gif", ".svg")
VIDEOS = (".mp4", ".webm")


def chemin(*p):
    return os.path.join(RACINE, *p)


def existe(*p):
    return os.path.exists(chemin(*p))


def catalogue():
    t = open(chemin("commun", "donnees", "catalogue.js"), encoding="utf-8").read()
    debut = t.index("var CATALOGUE =") + len("var CATALOGUE =")
    fin = t.index("/* Adresses", debut) if "/* Adresses" in t[debut:] else len(t)
    return json.loads(t[debut:fin].strip().rstrip(";"))


def nb_grades(imm):
    try:
        with open(chemin(imm, "assets", "data", "enigmes.json"), encoding="utf-8") as f:
            return len(json.load(f).get("niveaux") or [])
    except (OSError, ValueError, AttributeError):
        return 0


def medias(imm):
    """(attendus, images manquantes, vidéos manquantes, exemples manquants) d'après medias.csv."""
    att, img, vid, ex = 0, 0, 0, []
    try:
        with open(chemin(imm, "medias.csv"), encoding="utf-8-sig", newline="") as f:
            for l in csv.DictReader(f, delimiter=";"):
                fichier = (l.get("fichier") or "").strip()
                if not fichier:
                    continue
                att += 1
                if not os.path.exists(chemin(imm, *fichier.split("/"))):
                    ext = os.path.splitext(fichier)[1].lower()
                    if ext in VIDEOS:
                        vid += 1
                    else:
                        img += 1
                    if len(ex) < 5:
                        ex.append(fichier)
    except (OSError, csv.Error):
        return None
    return att, img, vid, ex


def nb_voix(imm):
    n = 0
    for _, _, fichiers in os.walk(chemin(imm, "assets", "audio", "voix")):
        n += sum(1 for f in fichiers if f.lower().endswith(".mp3"))
    return n


def points_a_verifier(dossier):
    """Points ouverts de A-VERIFIER.md : éléments de liste de premier niveau non barrés ni cochés."""
    try:
        lignes = open(chemin(dossier, "A-VERIFIER.md"), encoding="utf-8").read().splitlines()
    except OSError:
        return None
    pts = []
    for l in lignes:
        m = re.match(r"^ ?(?:\d+\.|[-*])\s+(.*)", l)
        if not m:
            continue
        texte = m.group(1).strip()
        if not texte or re.match(r"^\[[xX]\]", texte) or "✅" in texte or texte.startswith("~~"):
            continue
        texte = re.sub(r"^\[ \]\s*", "", texte)
        titre = re.match(r"\*\*(.+?)\*\*", texte)
        pts.append((titre.group(1) if titre else re.sub(r"[*`]", "", texte))[:90].rstrip(" :."))
    return pts


def sans_credit():
    """{jeu: nombre} lu dans le tableau « Par jeu » de diffusion/AUDIT-MEDIAS.md (python outils-docs/audit-licences.py)."""
    res = {}
    try:
        t = open(chemin("diffusion", "AUDIT-MEDIAS.md"), encoding="utf-8").read()
    except OSError:
        return res
    entete = None
    for l in t.splitlines():
        if not l.startswith("|"):
            entete = None if not l.strip() else entete
            continue
        cases = [c.strip() for c in l.strip().strip("|").split("|")]
        if "Sans crédit" in cases:
            entete = cases.index("Sans crédit")
        elif entete is not None and len(cases) > entete and cases[entete].isdigit():
            res[cases[0]] = int(cases[entete])
    return res


def premier_existant(*chemins):
    for p in chemins:
        if p and existe(*p.split("/")):
            return p
    return ""


def etat_jeu(j, credits):
    d = j.get("dossier") or ""
    imm = j.get("immersif") or ""
    ident = os.path.basename(imm) if imm else d
    a_imm = bool(imm) and existe(imm, "index.html")
    g = nb_grades(imm) if a_imm else 0
    m = medias(imm) if a_imm else None
    voix = nb_voix(imm) if a_imm else 0
    lecons = premier_existant(d + "/lecons-imprimables.html", imm and imm + "/lecons-imprimables.html")
    evals = premier_existant(d + "/evaluations-imprimables.html", imm and imm + "/evaluations-imprimables.html",
                             d + "/assets/data/evaluations.json")
    affiche = premier_existant(*[d + "/assets/images/affiche." + e for e in ("jpg", "webp", "png")])
    bande = premier_existant(d + "/assets/videos/bande-annonce.mp4")
    pts = points_a_verifier(d)
    manque = []
    if not a_imm:
        manque.append("variante immersive")
    elif g < 5:
        manque.append("5 grades ({} seulement)".format(g))
    if m and m[1]:
        manque.append("{} image{}".format(m[1], "s" if m[1] > 1 else ""))
    if m and m[2]:
        manque.append("{} vidéo{}".format(m[2], "s" if m[2] > 1 else ""))
    if a_imm and not voix:
        manque.append("voix")
    if not lecons:
        manque.append("leçons A4")
    if not evals:
        manque.append("évaluations")
    if not affiche:
        manque.append("affiche")
    if not bande:
        manque.append("bande-annonce")
    if j.get("medias_en_attente"):
        manque.append("carte de l'accueil « médias en attente »")
    sensible = SENSIBLES.get(ident) or SENSIBLES.get(d) or ""
    etat = "fini" if not manque else "en-cours"
    return {
        "id": ident, "num": j.get("num"), "titre": j.get("titre"), "icone": j.get("icone", ""), "matiere": j.get("matiere", ""),
        "annee": j.get("annee", ""), "dossier": d, "immersif": imm if a_imm else "", "grades": g,
        "medias": {"attendus": m[0], "images": m[1], "videos": m[2], "exemples": m[3]} if m else None,
        "voix": voix, "lecons": lecons, "evaluations": evals, "affiche": affiche, "bande_annonce": bande,
        "a_verifier": len(pts) if pts is not None else None, "points": (pts or [])[:4],
        "sans_credit": credits.get(ident, credits.get(d, 0)) + (credits.get(imm, 0) if imm else 0),
        "sensible": sensible, "etat": etat, "manque": manque,
    }


def etat():
    c = catalogue()
    credits = sans_credit()
    jeux = [etat_jeu(j, credits) for j in c.get("jeux", []) if j.get("dossier")]
    tot = {"jeux": len(jeux), "finis": sum(1 for j in jeux if j["etat"] == "fini"),
           "sensibles": sum(1 for j in jeux if j["sensible"]),
           "images": sum((j["medias"] or {}).get("images", 0) for j in jeux),
           "videos": sum((j["medias"] or {}).get("videos", 0) for j in jeux),
           "sans_voix": sum(1 for j in jeux if j["immersif"] and not j["voix"]),
           "a_verifier": sum(j["a_verifier"] or 0 for j in jeux),
           "sans_credit": sum(j["sans_credit"] for j in jeux)}
    tot["en_cours"] = tot["jeux"] - tot["finis"]
    a_relire = [{"jeu": j["id"], "titre": j["titre"], "point": j["sensible"], "priorite": 1} for j in jeux if j["sensible"]]
    for j in sorted(jeux, key=lambda x: -(x["a_verifier"] or 0)):
        for p in j["points"][:2]:
            a_relire.append({"jeu": j["id"], "titre": j["titre"], "point": p, "priorite": 2})
    return {"genere": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M"), "totaux": tot, "jeux": jeux, "a_relire": a_relire[:30]}


def main(argv):
    e = etat()
    if "--json" in argv:
        print(json.dumps(e, ensure_ascii=False, indent=1))
        return 0
    js = ("/* Fichier GÉNÉRÉ par outils-docs/etat-production.py — ne pas modifier à la main.\n"
          "   État de production des jeux, lu par le tableau de bord (enseignant.html) quand le serveur local\n"
          "   n'est pas là (site en ligne). Avec le serveur : /api/production, recalculé en direct. */\n"
          "var PRODUCTION = " + json.dumps(e, ensure_ascii=False, indent=0) + ";\n")
    with open(chemin("commun", "donnees", "production.js"), "w", encoding="utf-8", newline="\n") as f:
        f.write(js)
    t = e["totaux"]
    print("commun/donnees/production.js : {} jeux, {} fini(s), {} en cours, {} sensible(s), {} point(s) à vérifier."
          .format(t["jeux"], t["finis"], t["en_cours"], t["sensibles"], t["a_verifier"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
