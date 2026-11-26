# -*- coding: utf-8 -*-
"""Génère README.md et GUIDE-PEDAGOGIQUE.md de reproduction/ depuis assets/data (solutions et compétences toujours à jour).
Lancer depuis reproduction/ : python tests/donnees/gen_docs.py"""
import json, re

E = json.load(open("assets/data/enigmes.json", encoding="utf-8"))
D = json.load(open("assets/data/dialogues.json", encoding="utf-8"))
COMP = {1: "Identifier les organes reproducteurs de la fleur (étamines, pollen, pistil, ovaire, ovules) — première approche de la reproduction des plantes à fleurs (programme de 6e) ; vocabulaire mobilisé par le programme : pollen, pistil",
        2: "Mettre en évidence le rôle de la pollinisation dans la transformation de la fleur en fruit et des ovules en graines ; illustrer la coopération par la pollinisation ; relier insecticides et pollinisateurs (programme de 6e, première approche en CM1-CM2)",
        3: "Ordonner les étapes de la vie d'une plante à fleurs : germination, croissance, fleur, fruit, dispersion des graines (rappel du CE2) ; besoins de la germination (démarche expérimentale)",
        4: "Mettre en relation le type de fécondation (interne ou externe) avec le mode de reproduction des animaux (CM1)",
        5: "Décrire les étapes du développement des animaux de la fécondation à la naissance ; distinguer ovipares et vivipares (CM1) ; définir une espèce comme un ensemble d'individus interféconds (CM1) ; diversité des individus et variation héréditaire (6e)"}
txt = lambda h: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()
pers = D["personnages"]

r = ["# Le Jardin de la vie — escape game de sciences (cycle 3, jeu n°24)", "",
     "Sciences et technologie, programme 2026 (BO n° 24 du 11 juin 2026, annexe 2), « Les êtres vivants dans leur environnement » (CM1 « Reproduction, croissance et développement » et « Unité et diversité du vivant », 6e « Reproduction, croissance et développement ») ; progression de l'enseignant : année A, période 5 :",
     "*Le vivant, sa diversité et les fonctions qui le caractérisent. La reproduction sexuelle.*", "",
     "**Jouer** : version immersive `../immersifs/reproduction/` (5 grades : Visiteur du jardin ≈ CE2, Apprenti jardinier ≈ CM1, Naturaliste ≈ CM2, Botaniste ≈ 6ᵉ, Directeur du jardin ≈ 5ᵉ).",
     "Ce dossier contient les **données sources** (format des jeux classiques) d'où la variante immersive est générée ; la version classique (pages `index.html`, `prof.html`) n'est pas écrite.", "",
     "**Vigilance** : plantes et animaux seulement ; la reproduction humaine et la puberté ne sont pas abordées (partie « Puberté et reproduction humaine » du programme, menée à part par l'enseignant). Pas d'anthropomorphisme. Jardin, ferme et personnages inventés.", "",
     "## Fil narratif", "",
     "Cette nuit, un orage a ouvert la serre du jardin des Coteaux (inventé, Bourgogne) et les barrières de la ferme voisine : planches, cahiers, graines et registres sont mélangés, et le portail entre le jardin et la ferme s'est verrouillé. Les élèves, apprentis naturalistes, aident cinq personnes et rassemblent cinq mots qui ouvrent le portail :",
     "> " + D["metadata"]["phrase_bilan"], "",
     "| Salle | Lieu | Guide (personnage inventé) | Mot |", "|---|---|---|---|"]
for s in D["salles"]:
    p = s["dialogue_intro"]["perso"]
    r.append(f"| {s['num']} | {s['lieu']} | {pers[p]['nom']}, {pers[p]['role'][0].lower() + pers[p]['role'][1:]} | {s['motCle']} |")
r += ["", "## 🎯 Compétences du programme (vue d'ensemble)", "", "| Salle | Compétence du programme |", "|---|---|"]
r += [f"| {n} | {c} |" for n, c in COMP.items()]
r += ["", "CM1 : 3 énigmes par salle (15) ; CM2 : 4 énigmes par salle (20). Repères en CM1 (pétale, étamine, pistil, fécondation dans le corps ou dans l'eau, œuf ou ventre de la mère) ; vocabulaire précis en CM2 (sépale, ovaire, stigmate, gamète, interne, externe, ovipare, vivipare, larve, espèce) et durées (21 jours, 9 mois, 5 mois).", "",
      "## Solutions (générées depuis `assets/data/enigmes.json`)", ""]
for s, d in zip(E["salles"], D["salles"]):
    r.append(f"### Salle {s['num']} — {s['titre']} (mot : **{d['motCle']}**)")
    r.append("")
    for e in s["enigmes"]:
        r.append(f"<details><summary><b>{e['id']} {e['titre']}</b> ({e['type']}{', CM2' if e.get('niveaux') == ['CM2'] else ''})</summary>\n\n{txt(e['correction'])}\n\n</details>\n")
    r.append("")
r += ["## Sources", ""] + [f"- {x.strip()}" for x in E["metadata"]["sources"].split(" ; ")] + [
      "", "## Fichiers", "",
      "- `assets/data/` : `enigmes.json`, `lecons.json`, `dialogues.json`, générés par `tests/donnees/gen_enigmes.py`, `gen_lecons.py`, `gen_dialogues.py` ; phrases des fiches dans `tests/donnees/fiches.py` (reprises mot pour mot par les justifications des grades) ; schémas SVG dans `tests/donnees/schemas.py`.",
      "- Variante immersive : `python vingt-mille-lieues/outils/immersif/migrer-jeu.py reproduction --theme reproduction/tests/donnees/theme-immersif.json --force`, puis `appliquer-narration.py reproduction`, `finir-jeu.py reproduction` et `python reproduction/tests/donnees/gen_medias.py` (prompts des médias), enfin `prompts-flow.py reproduction`.",
      "- Grades : `vingt-mille-lieues/outils/immersif/grades/reproduction_s1..s5.py` et `reproduction_theme.py` ; narration : `vingt-mille-lieues/outils/immersif/narration/reproduction.json`.", ""]
open("README.md", "w", encoding="utf-8").write("\n".join(r))

g = ["# Guide pédagogique — Le Jardin de la vie (jeu n°24)", "", "## 1. Place dans les programmes", "",
     "Sciences et technologie, cycle 3 (BO n° 24 du 11 juin 2026, annexe 2), « Les êtres vivants dans leur environnement ». Le programme répartit la reproduction ainsi :",
     "- **CM1**, « Reproduction, croissance et développement » (cycle de vie) : décrire les étapes du développement des animaux de la fécondation à la naissance ; mettre en relation le type de fécondation (interne ou externe) avec le mode de reproduction ovipare et vivipare ;",
     "- **CM1**, « Unité et diversité du vivant » : définir une espèce comme un ensemble d'individus interféconds ;",
     "- **6e**, « Reproduction, croissance et développement » : mettre en évidence le rôle de la pollinisation dans la transformation de la fleur en fruit et des ovules en graines ; illustrer la coopération avec la pollinisation ; relier insecticides et pollinisateurs ; diversité des individus et variation héréditaire ;",
     "- **CE2** (rappel) : étapes de la vie d'une plante à fleurs, de la graine à la plante, de la fleur au fruit, dispersion des graines.",
     "Le CM2 n'a pas de partie « Reproduction » : en classe à double niveau, les CM2 revoient le CM1 avec un vocabulaire plus précis et une première approche du programme de 6e (salles 1 et 2). La reproduction non sexuée (bouturage, stolons), proposée par la progression, n'est pas au programme 2026 : elle n'est pas notée dans le jeu.", "",
     "## 🎯 Compétences du programme, énigme par énigme", "", "| Salle | Énigme | Type | Compétence du programme |", "|---|---|---|---|"]
for s in E["salles"]:
    for e in s["enigmes"]:
        g.append(f"| {s['num']} | {e['id']} {e['titre']} ({'CM2' if e.get('niveaux') == ['CM2'] else 'CM1-CM2'}) | {e['type']} | {COMP[s['num']]} |")
g += ["", "## 2. Prérequis", "",
      "- Avoir observé des plantes en classe (semis, plantation) et connaître le vocabulaire racine, tige, feuille, fleur.", "- Savoir lire un schéma légendé et un tableau de résultats.", "",
      "## 3. Déroulés possibles", "",
      "- **Une séance de 60 à 75 min** : équipes de 3 ou 4, une tablette ou un ordinateur par équipe ; tableau de bord enseignant `immersifs/reproduction/prof.html`.",
      "- **Cinq séances de 25 min** : une salle par séance, la fiche de la salle lue en fin de séance (bouton « Leçons A4 » des réglages).",
      "- **Avec des manipulations** : avant la salle 1, disséquer une fleur (tulipe, lys) et coller ses pièces ; avant la salle 3, lancer l'expérience des quatre pots de Tom une semaine plus tôt ; après la salle 5, observer des têtards ou une couveuse si l'école en a une.", "",
      "## 4. Différenciation (grades)", "",
      "- **Visiteur du jardin (≈ CE2)** : 15 énigmes courtes, vocabulaire simple, premier indice offert.",
      "- **Apprenti jardinier (≈ CM1)** et **Naturaliste (≈ CM2)** : les énigmes des niveaux CM1 et CM2 ci-dessus.",
      "- **Botaniste (≈ 6ᵉ)** et **Directeur du jardin (≈ 5ᵉ)** : 20 énigmes avec justification par une phrase de la fiche ; dissection, chaîne insecticides → pollinisateurs → récolte, démarche expérimentale, lien fécondation et mode de reproduction, diversité des individus.", "",
      "## 5. Lexique", "",
      "fleur, sépale, pétale, étamine, pollen, pistil, stigmate, ovaire, ovule, pollinisation, pollinisateur, nectar, fécondation, fruit, graine, embryon, réserves, dispersion, germination, cycle de vie, mâle, femelle, gamète, cellule reproductrice, fécondation interne, fécondation externe, ovipare, vivipare, éclosion, couvaison, larve, têtard, espèce, individu.", "",
      "## 6. Évaluation", "",
      "- Fin de jeu : la phrase des cinq mots à expliquer à l'oral.", "- Trace écrite : légender une fleur ; classer cinq animaux (fécondation interne ou externe, ovipare ou vivipare) ; ordonner le cycle de vie d'une plante.", "",
      "## 7. Points de vigilance", "",
      "- Plantes et animaux seulement : la reproduction humaine et la puberté relèvent d'une séquence à part (partie « Puberté et reproduction humaine » du programme, dans le cadre de l'éducation à la sexualité). Si un élève pose une question, y répondre simplement et renvoyer à cette séquence.",
      "- Éviter l'anthropomorphisme : l'abeille ne « veut » pas aider la fleur, elle se nourrit ; la plante ne « choisit » pas de disperser ses graines.",
      "- Conceptions fréquentes : « pondre des œufs = fécondation externe » (faux : la poule) ; « la graine a besoin de lumière pour germer » (faux pour la plupart des graines) ; « le fruit, c'est ce qui est sucré » (la gousse de haricot et la noisette sont aussi des fruits).",
      "- Chiffres arrondis : « environ » 21 jours, 9 mois, 5 mois.", "",
      "## 8. Sources", ""] + [f"- {x.strip()}" for x in E["metadata"]["sources"].split(" ; ")] + [""]
open("GUIDE-PEDAGOGIQUE.md", "w", encoding="utf-8").write("\n".join(g))
print("README.md et GUIDE-PEDAGOGIQUE.md écrits")
