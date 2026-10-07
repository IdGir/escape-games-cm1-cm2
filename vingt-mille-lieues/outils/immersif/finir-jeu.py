#!/usr/bin/env python3
"""Enchaîne les étapes d'une variante immersive : moteur, grades, données, test, voix, prompts Google Flow.

    python vingt-mille-lieues/outils/immersif/finir-jeu.py <jeu>
Variable d'environnement NODE_PATH : dossier contenant jsdom (par défaut ~/node_modules).
"""
import os, subprocess, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.abspath(os.path.join(ICI, "..", "..", ".."))
jeu = sys.argv[1]
dest = os.path.join(RACINE, "immersifs", jeu)
env = dict(os.environ, PYTHONIOENCODING="utf-8", NODE_PATH=os.environ.get("NODE_PATH", os.path.join(os.path.expanduser("~"), "node_modules")))


def go(titre, cmd, cwd=RACINE, fin=3):
    print("==", titre, flush=True)
    r = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace")
    sortie = (r.stdout + r.stderr).strip().splitlines()
    print("\n".join(sortie[-fin:]), flush=True)
    if r.returncode:
        print(f"✖ échec ({r.returncode}) : {titre}", flush=True)
        if "grades" in titre.lower() or "test" in titre.lower():
            sys.exit(r.returncode)
    return r.returncode


py = sys.executable
go("moteur", [py, "vingt-mille-lieues/outils/immersif/migrer-jeu.py", "--maj-moteur", f"immersifs/{jeu}"], fin=1)
go("grades", [py, "vingt-mille-lieues/outils/immersif/appliquer-grades.py", jeu], fin=30)
go("données embarquées", [py, f"immersifs/{jeu}/outils/embarquer-donnees.py"], fin=1)
go("test immersif", ["node", f"immersifs/{jeu}/tests/test-immersif.js"], fin=4)
go("voix (mp3 Edge)", [py, "outils/voix/generer-voix.py"], cwd=dest, fin=3)
go("test voix", ["node", "tests/test-voix.js"], cwd=dest, fin=2)
go("prompts Google Flow", [py, "vingt-mille-lieues/outils/immersif/prompts-flow.py", jeu], fin=1)
