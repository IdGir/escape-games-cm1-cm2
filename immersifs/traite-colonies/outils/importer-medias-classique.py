#!/usr/bin/env python3
"""Reprend dans la variante immersive les médias produits pour le jeu classique (outils-medias\\produire-medias.bat traite-colonies).

    python immersifs/traite-colonies/outils/importer-medias-classique.py

traite-colonies/assets/images/decors/salleN.jpg       → décor immersif (cartes, registres, colonies, musee, lecture) + image de départ transition-eN
traite-colonies/assets/images/personnages/<id>.png    → portrait immersif <id>
traite-colonies/assets/videos/salleN.mp4              → vidéo transition-eN
traite-colonies/assets/videos/final.mp4               → vidéo fin
Les fichiers absents sont simplement sautés : on peut relancer quand la production a avancé.
Crédits : « Agnes AI (image générée par IA) ». Ensuite : python immersifs/traite-colonies/outils/embarquer-donnees.py
"""
import os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, "medias"))
import importlib.util
spec = importlib.util.spec_from_file_location("importer", os.path.join(ICI, "medias", "importer-image.py"))
imp = importlib.util.module_from_spec(spec); spec.loader.exec_module(imp)

CLASSIQUE = os.path.abspath(os.path.join(ICI, "..", "..", "..", "traite-colonies", "assets"))
DECORS = {1: "cartes", 2: "registres", 3: "colonies", 4: "musee", 5: "lecture"}
PERSOS = ["ines", "malik", "celia", "margot", "theo"]
SRC, LIC = "Agnes AI (image générée par IA)", "usage selon les conditions du compte Agnes de l'enseignant"


def f(*p):
    c = os.path.join(CLASSIQUE, *p)
    return c if os.path.isfile(c) else None


def main():
    n = 0
    for k, decor in DECORS.items():
        if f("images", "decors", f"salle{k}.jpg"):
            imp.deposer(f("images", "decors", f"salle{k}.jpg"), decor=decor, depart=f"transition-e{k}", source=SRC, licence=LIC); n += 1
        if f("videos", f"salle{k}.mp4"):
            imp.deposer(f("videos", f"salle{k}.mp4"), video=f"transition-e{k}", source="Agnes AI (vidéo générée par IA)", licence=LIC); n += 1
    for p in PERSOS:
        if f("images", "personnages", f"{p}.png"):
            imp.deposer(f("images", "personnages", f"{p}.png"), portrait=p, source=SRC, licence=LIC); n += 1
    if f("videos", "final.mp4"):
        imp.deposer(f("videos", "final.mp4"), video="fin", source="Agnes AI (vidéo générée par IA)", licence=LIC); n += 1
    print(f"{n} média(s) repris du jeu classique. Lancer ensuite : python immersifs/traite-colonies/outils/embarquer-donnees.py")


if __name__ == "__main__":
    main()
