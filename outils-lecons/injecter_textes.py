#!/usr/bin/env python3
"""Injecte les textes courts A4 (outils-lecons/textes/<jeu>.json) dans <jeu>/assets/data/lecons-a4.json.

Usage (sans Node, depuis le dossier du projet) :
    python3 outils-lecons/injecter_textes.py            # tous les jeux
    python3 outils-lecons/injecter_textes.py lumiere    # un seul jeu

Ces textes ne servent qu'à la page A4 : les leçons du jeu (lecons.json) ne sont pas modifiées.
Si le jeu n'a pas encore de lecons-a4.json (ex. traite-colonies), le fichier est créé.
construire.py fait la même fusion : relancer l'un ou l'autre donne le même résultat."""
import glob, json, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)

cibles = sys.argv[1:] or sorted(os.path.basename(f)[:-5] for f in glob.glob(os.path.join(ICI, "textes", "*.json")))
for jeu in cibles:
    src = os.path.join(ICI, "textes", jeu + ".json")
    dest = os.path.join(RACINE, jeu, "assets", "data", "lecons-a4.json")
    if not os.path.exists(src):
        print("pas de textes pour", jeu); continue
    textes = json.load(open(src, encoding="utf-8"))
    a4 = json.load(open(dest, encoding="utf-8")) if os.path.exists(dest) else {"jeu": {}, "lecons": {}}
    a4.setdefault("lecons", {})
    for lid, txt in textes.items():
        a4["lecons"].setdefault(lid, {})["texte"] = txt
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8", newline="\n") as f:
        json.dump(a4, f, ensure_ascii=False, indent=1)
    print(f"{jeu} : {len(textes)} textes courts → {os.path.relpath(dest, RACINE)}")
