#!/usr/bin/env python3
"""Assemble les sources d'escales (sources/escale-NN.json) dans les données du jeu.

Chaque source contient : « escale » (objet complet, avec ses énigmes), et facultativement « rayons », « lecons »,
« decors » (décors-fx), « dialogues » (cinematiques, fin_escale). L'assemblage remplace, dans assets/data/,
l'escale de même numéro, les leçons et décors de même identifiant ; il ne touche pas au reste.
Puis il régénère js/donnees-embarquees.js.

Usage : python vingt-mille-lieues/outils/assembler-escales.py
"""
import glob, json, os, subprocess, sys

ICI = os.path.dirname(os.path.abspath(__file__))
JEU = os.path.dirname(ICI)
DATA = os.path.join(JEU, "assets", "data")


def lire(nom):
    with open(os.path.join(DATA, nom), encoding="utf-8") as f:
        return json.load(f)


def ecrire(nom, d):
    with open(os.path.join(DATA, nom), "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")


E, L, F, Dg = lire("enigmes.json"), lire("lecons.json"), lire("decors-fx.json"), lire("dialogues.json")
sources = sorted(glob.glob(os.path.join(JEU, "sources", "escale-*.json")))
for s in sources:
    with open(s, encoding="utf-8") as f:
        src = json.load(f)
    es = src["escale"]
    E["escales"] = [x for x in E["escales"] if x["numero"] != es["numero"]] + [es]
    for r in src.get("rayons", []):
        L["rayons"] = [x for x in L["rayons"] if x["id"] != r["id"]] + [r]
    for l in src.get("lecons", []):
        L["lecons"] = [x for x in L["lecons"] if x["id"] != l["id"]] + [l]
    for k, v in src.get("decors", {}).items():
        F["decors"][k] = v
    dl = src.get("dialogues", {})
    for k, v in dl.get("cinematiques", {}).items():
        Dg["cinematiques"][k] = v
    for k, v in dl.get("fin_escale", {}).items():
        Dg["fin_escale"][k] = v
    print("assemblé :", os.path.relpath(s, JEU), f"(escale {es['numero']}, {len(es['enigmes'])} énigmes)")
E["escales"].sort(key=lambda x: x["numero"])
ordre_rayons = ["histoire", "geographie", "electricite", "technologie", "navigation", "vivant", "terre"]
L["rayons"].sort(key=lambda r: ordre_rayons.index(r["id"]) if r["id"] in ordre_rayons else 99)
L["lecons"].sort(key=lambda l: (l.get("escale", 0), l["rayon"], l["fiche"]))
ecrire("enigmes.json", E); ecrire("lecons.json", L); ecrire("decors-fx.json", F); ecrire("dialogues.json", Dg)
subprocess.run([sys.executable, os.path.join(ICI, "embarquer-donnees.py")], check=True)
