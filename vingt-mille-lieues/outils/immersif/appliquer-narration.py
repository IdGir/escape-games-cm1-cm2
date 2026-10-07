#!/usr/bin/env python3
"""Applique un fichier de narration (narration/<jeu>.json) à immersifs/<jeu>/assets/data.

Format : {"tons": {perso: "ton"}, "enigmes": {"e1-2": {"objet": "...", "description": "...", "enjeu": "...",
          "situation": "...", "reaction": "...", "dialogue": "..."}}}
- objet/description : nom et description de la zone cliquable (decors-fx.json) ;
- enjeu, situation (probleme_narratif), reaction (reaction_du_decor.description) ;
- dialogue : remplace la phrase générique « Voici la suite… » (énigmes 2 à 4) aux deux grades.
Après : python immersifs/<jeu>/outils/embarquer-donnees.py
"""
import json, os, sys

RACINE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def main(jeu):
    nar = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "narration", jeu + ".json"), encoding="utf-8"))
    data = os.path.join(RACINE, "immersifs", jeu, "assets", "data")
    ch = lambda n: os.path.join(data, n)
    enig = json.load(open(ch("enigmes.json"), encoding="utf-8"))
    fx = json.load(open(ch("decors-fx.json"), encoding="utf-8"))
    pers = json.load(open(ch("personnages.json"), encoding="utf-8"))
    manque = set(nar["enigmes"])
    for s in enig["escales"]:
        for e in s["enigmes"]:
            n = nar["enigmes"].get(e["id"])
            if not n:
                continue
            manque.discard(e["id"])
            e["enjeu"], e["probleme_narratif"] = n["enjeu"], n["situation"]
            e["reaction_du_decor"]["description"] = n["reaction"]
            for g in ("mousse", "matelot", "timonier", "lieutenant", "second"):
                if g not in e: continue
                d = e[g].get("dialogue")
                if n.get("dialogue") and d is not None and d.startswith("Voici la suite"):
                    e[g]["dialogue"] = n["dialogue"]
            e.pop("_brouillon", None)
            for z in fx["decors"][e["decor"]]["zones"]:
                if z["id"] == e["objet_principal"]:
                    z["libelle"], z["description"] = n["objet"], n["description"]
    for d in fx["decors"].values():
        d.pop("_brouillon", None)
    for k, t in nar.get("tons", {}).items():
        pers["personnages"][k]["ton"] = t
    if manque:
        sys.exit("Énigmes inconnues : " + ", ".join(sorted(manque)))
    for nom, obj in (("enigmes.json", enig), ("decors-fx.json", fx), ("personnages.json", pers)):
        json.dump(obj, open(ch(nom), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(jeu, ": narration appliquée à", len(nar["enigmes"]), "énigmes")


if __name__ == "__main__":
    main(sys.argv[1])
