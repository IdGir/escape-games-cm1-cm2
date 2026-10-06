#!/usr/bin/env python3
"""Régénère js/donnees-embarquees.js à partir de assets/data/*.json.

Pourquoi : en double-clic (file://), le navigateur bloque fetch() ; le jeu lit alors cette copie.
À relancer après toute modification d'un JSON :  python vingt-mille-lieues/outils/embarquer-donnees.py
(tests/test-jeu.js vérifie que la copie est à jour).
"""
import json, os
ICI = os.path.dirname(os.path.abspath(__file__))
JEU = os.path.dirname(ICI)
NOMS = ["enigmes", "lecons", "decors-fx", "dialogues", "personnages"]
donnees = {}
for nom in NOMS:
    with open(os.path.join(JEU, "assets", "data", nom + ".json"), encoding="utf-8") as f:
        donnees[nom] = json.load(f)
sortie = os.path.join(JEU, "js", "donnees-embarquees.js")
with open(sortie, "w", encoding="utf-8", newline="\n") as f:
    f.write("/* FICHIER GÉNÉRÉ par outils/embarquer-donnees.py — ne pas modifier à la main.\n"
            "   Copie de assets/data/*.json pour le jeu en double-clic (file://). */\n")
    f.write("window.VML_DONNEES_EMBARQUEES = ")
    json.dump(donnees, f, ensure_ascii=False, separators=(",", ":"))
    f.write(";\n")
print("écrit :", os.path.relpath(sortie, JEU))
