# -*- coding: utf-8 -*-
"""Tient à jour le journal des versions (CHANGELOG.md) de chaque jeu, à partir de l'historique git.

    python outils-docs/maj-journaux.py            (les 9 jeux)
    python outils-docs/maj-journaux.py melanges   (un seul)

Premier passage : tout l'historique du jeu. Ensuite : seuls les nouveaux commits (ceux qui
touchent le dossier du jeu ou le tronc commun commun/) sont ajoutés en tête, à la date du
jour, sous forme de liste. Le texte déjà présent n'est jamais modifié : on peut le compléter
à la main (une phrase d'explication, une remarque pour les collègues…).
Repère technique en fin de fichier : <!-- dernier-commit: … -->.
À lancer avant de publier, puis : git add */CHANGELOG.md
"""
import os, re, subprocess, sys, datetime
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JEUX = ["declaration", "tour-du-monde", "mission-geo", "constitution", "moyen-age-abbaye",
        "chateau-fort", "station-meteo", "melanges", "objets-techniques", "versailles", "renaissance", "alimentation", "lumiere"]
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
REPERE = re.compile(r"<!-- dernier-commit: ([0-9a-f]+) -->")

def git(*a):
    return subprocess.run(["git", *a], cwd=RACINE, capture_output=True, text=True, encoding="utf-8", check=True).stdout

def titre_jeu(jeu):
    with open(os.path.join(RACINE, jeu, "README.md"), encoding="utf-8") as f:
        l = f.readline().lstrip("# ").strip()
    return re.sub(r"^[^\wÀ-ÿ«]+", "", l)

def lisible(sujet):
    if sujet.startswith("Merge"): return None
    if sujet in ("Add files via upload",) or sujet.startswith("Add files via upload"): return "Médias déposés directement sur GitHub"
    m = re.match(r"Delete (.+)", sujet)
    if m: return "Fichier retiré : " + m.group(1)
    m = re.match(r"(Update|Create) (.+)", sujet)
    if m: return ("Mise à jour : " if m.group(1) == "Update" else "Ajout : ") + m.group(2)
    return sujet

# Fichiers du tronc commun qui changent ce que voient les élèves ou l'enseignant dans un jeu
# (pas les tests ni la documentation). Mission géographique ne charge qu'une partie du tronc commun.
COMMUN_JEU = ("commun/js/", "commun/css/", "commun/polices/", "commun/donnees/", "commun/icones/")
COMMUN_MISSION = ("commun/js/lecons-a4", "commun/css/lecons-a4", "commun/js/transitions", "commun/js/accessibilite",
                  "commun/js/pwa", "commun/polices/", "commun/icones/")

def commits(jeu, depuis=None):
    plage = [f"{depuis}..HEAD"] if depuis else []
    sortie = git("log", "--format=%h%x09%ad%x09%s", "--date=short", *plage, "--", jeu, "commun")
    l = []
    for ligne in sortie.splitlines():
        h, d, s = ligne.split("\t", 2)
        fichiers = git("show", "--name-only", "--format=", h).split()
        utiles = COMMUN_MISSION if jeu == "mission-geo" else COMMUN_JEU
        if not any(f.startswith(jeu + "/") or f.startswith(utiles) for f in fichiers):
            continue
        t = lisible(s)
        if t: l.append((h, d, t))
    return l

def date_fr(iso):
    a, m, j = map(int, iso.split("-"))
    return f"{j} {MOIS[m - 1]} {a}"

def sections(liste):
    """Regroupe par date (plus récent d'abord) et fusionne les dépôts de médias répétés."""
    par = {}
    for h, d, t in liste:
        par.setdefault(d, []).append(t)
    out = []
    for d in sorted(par, reverse=True):
        lignes, vus = [], {}
        for t in par[d]:
            if t == "Médias déposés directement sur GitHub":
                vus[t] = vus.get(t, 0) + 1
                if vus[t] > 1: continue
            lignes.append(t)
        lignes = [f"{t} ({vus[t]} envois)" if vus.get(t, 0) > 1 and t in vus else t for t in lignes]
        out.append(f"## {date_fr(d)}\n\n" + "\n".join(f"- {t}" for t in lignes) + "\n")
    return out

def maj(jeu):
    chemin = os.path.join(RACINE, jeu, "CHANGELOG.md")
    tete = git("rev-parse", "--short", "HEAD").strip()
    if os.path.exists(chemin):
        texte = open(chemin, encoding="utf-8").read()
        m = REPERE.search(texte)
        depuis = m.group(1) if m else None
        nouveaux = commits(jeu, depuis)
        if not nouveaux:
            print(f"{jeu} : à jour"); return
        corps = REPERE.sub("", texte).rstrip() + "\n"
        i = corps.find("\n## ")
        corps = (corps[:i + 1] + "\n".join(sections(nouveaux)) + "\n" + corps[i + 1:]) if i >= 0 else corps + "\n" + "\n".join(sections(nouveaux))
    else:
        nouveaux = commits(jeu)
        corps = (f"# Journal des versions — {titre_jeu(jeu)}\n\n"
                 "Les évolutions du jeu, de la plus récente à la plus ancienne. Ce journal est durable et publié\n"
                 "(contrairement aux fichiers RECAP-… de reprise de session). Les entrées viennent de l'historique\n"
                 "git (`python outils-docs/maj-journaux.py`) ; on peut les compléter à la main.\n\n"
                 + "\n".join(sections(nouveaux)))
    # même jour déjà présent juste en dessous : une seule rubrique datée
    corps = re.sub(r"(\n## (.+)\n\n(?:- .*\n)+)\n## \2\n\n", r"\1", corps)
    with open(chemin, "w", encoding="utf-8", newline="\n") as f:
        f.write(corps.rstrip() + f"\n\n<!-- dernier-commit: {tete} -->\n")
    print(f"{jeu} : {len(nouveaux)} entrée(s)")

if __name__ == "__main__":
    for j in (sys.argv[1:] or JEUX):
        maj(j)
