# -*- coding: utf-8 -*-
"""Génère README.md et GUIDE-PEDAGOGIQUE.md de naissances-animaux/ depuis assets/data (solutions et compétences toujours à jour).
Lancer depuis naissances-animaux/ : python tests/donnees/gen_docs.py"""
import json, re

E = json.load(open("assets/data/enigmes.json", encoding="utf-8"))
D = json.load(open("assets/data/dialogues.json", encoding="utf-8"))
COMP = {1: "Décrire les étapes du développement des animaux de la fécondation à la naissance : rencontre d'un gamète mâle et d'un gamète femelle, cellule-œuf, embryon",
        2: "Distinguer fécondation externe (dans l'eau) et fécondation interne (dans le corps de la femelle) ; exemples",
        3: "Mettre en relation le type de fécondation (interne ou externe) avec le mode de reproduction ovipare ou vivipare ; exceptions",
        4: "Décrire le développement avant la naissance : couvaison et éclosion de l'œuf de poule, gestation de mammifères (durées sourcées)",
        5: "Pour des animaux variés, dire le type de fécondation et le mode de reproduction (tableau à deux entrées)"}
txt = lambda h: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()
pers = D["personnages"]

r = ["# La Nurserie du zoo — escape game de sciences (cycle 3, jeu n°15)", "",
     "Sciences et technologie, programme 2026 (BO n° 24 du 11 juin 2026), CM1, « Les êtres vivants dans leur environnement » : reproduction, croissance et développement ; progression de l'enseignant : année B, période 3 :",
     "*Décrire les étapes du développement des animaux de la fécondation à la naissance. Mettre en relation le type de fécondation (interne ou externe) avec le mode de reproduction ovipare et vivipare des animaux.*", "",
     "**Jouer** : version immersive `../immersifs/naissances-animaux/` (5 grades : Bénévole ≈ CE2, Apprenti soigneur ≈ CM1, Soigneur ≈ CM2, Biologiste ≈ 6ᵉ, Chef de la nurserie ≈ 5ᵉ).",
     "Ce dossier contient les **données sources** (format des jeux classiques) d'où la variante immersive est générée ; la version classique (pages `index.html`, `prof.html`) n'est pas encore écrite.", "",
     "**Vigilance** : pas de reproduction humaine (laissée à l'enseignant) ; aucune image ni vidéo de naissance ; les exceptions (ornithorynque, vipère aspic, requins) sont traitées comme des exceptions.", "",
     "## Fil narratif", "",
     "Une tempête a ouvert les fenêtres de la nurserie du zoo des Trois-Sources (inventé) : fiches et étiquettes des œufs et des berceaux sont mélangées. Les élèves, apprentis soigneurs, retrouvent comment naît chaque animal et cinq mots qui ouvrent le carnet de naissance :",
     "> " + D["metadata"]["phrase_bilan"], "",
     "| Salle | Lieu | Guide (personnage inventé) | Mot |", "|---|---|---|---|"]
for s in D["salles"]:
    p = s["dialogue_intro"]["perso"]
    r.append(f"| {s['num']} | {s['lieu']} | {pers[p]['nom']}, {pers[p]['role'][0].lower() + pers[p]['role'][1:]} | {s['motCle']} |")
r += ["", "## 🎯 Compétences du programme (vue d'ensemble)", "", "| Salle | Compétence du programme |", "|---|---|"]
r += [f"| {n} | {c} |" for n, c in COMP.items()]
r += ["", "CM1 : 3 énigmes par salle (15) ; CM2 : 4 énigmes par salle (20). Repères en CM1 (cellule du mâle, cellule de la femelle, durées arrondies) ; vocabulaire exact et calculs en CM2 (gamètes, spermatozoïde, ovule, embryon, durées en jours).", "",
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
      "- Variante immersive : `python vingt-mille-lieues/outils/immersif/migrer-jeu.py naissances-animaux --theme naissances-animaux/tests/donnees/theme-immersif.json --force`, puis `appliquer-grades.py naissances-animaux`, `appliquer-narration.py naissances-animaux`, `finir-jeu.py naissances-animaux`.",
      "- Grades : `vingt-mille-lieues/outils/immersif/grades/naissances_animaux_s1..s5.py` et `naissances_animaux_theme.py` ; narration : `vingt-mille-lieues/outils/immersif/narration/naissances-animaux.json`.", ""]
open("README.md", "w", encoding="utf-8").write("\n".join(r))

g = ["# Guide pédagogique — La Nurserie du zoo (jeu n°15)", "", "## 1. Place dans les programmes", "",
     "Sciences et technologie, cycle 3 (BO n° 24 du 11 juin 2026) : la partie « Reproduction, croissance et développement » (« Les êtres vivants dans leur environnement ») figure en **CM1** et en 6ᵉ. Le jeu couvre l'extrait de la progression de l'enseignant (année B, période 3) : étapes du développement de la fécondation à la naissance ; type de fécondation et mode de reproduction ovipare ou vivipare.",
     "À jouer avant ou avec « Le Jardin de la vie » (n°24, reproduction sexuée, année A) : ce jeu-ci ne traite pas des plantes et ne répète pas la reproduction sexuée en général.", "",
     "## 🎯 Compétences du programme, énigme par énigme", "", "| Salle | Énigme | Type | Compétence du programme |", "|---|---|---|---|"]
for s in E["salles"]:
    for e in s["enigmes"]:
        g.append(f"| {s['num']} | {e['id']} {e['titre']} ({'CM2' if e.get('niveaux') == ['CM2'] else 'CM1-CM2'}) | {e['type']} | {COMP[s['num']]} |")
g += ["", "## 2. Prérequis", "",
      "- Savoir qu'un être vivant naît, grandit, se reproduit et meurt (cycle 2).", "- Connaître quelques grands groupes d'animaux : oiseaux, mammifères, poissons, amphibiens, reptiles, insectes.", "",
      "## 3. Déroulés possibles", "",
      "- **Une séance de 60 à 75 min** : équipes de 3 ou 4, une tablette ou un ordinateur par équipe ; tableau de bord enseignant `immersifs/naissances-animaux/prof.html`.",
      "- **Cinq séances de 25 min** : une salle par séance, la leçon de la salle lue en fin de séance (bouton « Leçons A4 » des réglages).",
      "- **En atelier** : un groupe joue pendant que l'enseignant mène l'observation d'une ponte de grenouille en classe ou d'œufs d'escargots (élevage, La main à la pâte).", "",
      "## 4. Différenciation (grades)", "",
      "- **Bénévole (≈ CE2)** : 15 énigmes courtes, vocabulaire simple, premier indice offert.",
      "- **Apprenti soigneur (≈ CM1)** et **Soigneur (≈ CM2)** : les énigmes des niveaux CM1 et CM2 ci-dessus.",
      "- **Biologiste (≈ 6ᵉ)** et **Chef de la nurserie (≈ 5ᵉ)** : 20 énigmes avec justification par une phrase de la fiche ; contre-exemples (dauphin, tortue marine), ovovivipares (vipère aspic, grand requin blanc), calculs de durées.", "",
      "## 5. Lexique", "",
      "gamète, spermatozoïde, ovule, fécondation, cellule-œuf, embryon, fécondation externe, fécondation interne, accouplement, ponte, ovipare, vivipare, ovovivipare, placenta, cordon ombilical, couvaison, éclosion, gestation.", "",
      "## 6. Évaluation", "",
      "- Fin de jeu : la phrase des cinq mots à expliquer à l'oral.", "- Trace écrite : le tableau à deux entrées de la salle 5, complété avec trois animaux nouveaux choisis par les élèves.", "",
      "## 7. Points de vigilance", "",
      "- Pas de reproduction humaine dans ce jeu ; si une question arrive, la renvoyer au cadre de l'éducation à la sexualité défini par l'enseignant.",
      "- Le mot « œuf » a deux sens : la cellule-œuf (première cellule) et l'œuf pondu (avec réserves et coquille). Le jeu dit « cellule-œuf » en CM2, « œuf (première cellule) » en CM1.",
      "- Conception fréquente : « les animaux qui vivent dans l'eau ont une fécondation externe » (contre-exemples : dauphin, tortue marine, requin).",
      "- Exceptions présentées comme telles : ornithorynque (mammifère ovipare), vipère aspic (ovovivipare), requins (roussette ovipare, requin-marteau vivipare).",
      "- Les durées de gestation sont des moyennes : elles varient selon les individus et les races.",
      "- Pas d'image ni de vidéo de naissance (consigne de l'enseignant).", "",
      "## 8. Sources", ""] + [f"- {x.strip()}" for x in E["metadata"]["sources"].split(" ; ")] + [""]
open("GUIDE-PEDAGOGIQUE.md", "w", encoding="utf-8").write("\n".join(g))
print("README.md et GUIDE-PEDAGOGIQUE.md écrits")
