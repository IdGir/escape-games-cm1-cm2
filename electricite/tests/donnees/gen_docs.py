# -*- coding: utf-8 -*-
"""Génère README.md et GUIDE-PEDAGOGIQUE.md de electricite/ depuis assets/data (solutions et compétences toujours à jour).
Lancer depuis electricite/ : python tests/donnees/gen_docs.py"""
import json, re

E = json.load(open("assets/data/enigmes.json", encoding="utf-8"))
D = json.load(open("assets/data/dialogues.json", encoding="utf-8"))
COMP = {1: "Réaliser un circuit électrique à une boucle (pile, interrupteur, un ou deux récepteurs) ; circuit ouvert, circuit fermé",
        2: "Identifier des matériaux conducteurs et isolants ; un même objet peut être fabriqué dans l'un ou l'autre type de matériau",
        3: "Réaliser et schématiser un circuit, lire et utiliser des schémas normalisés ; justifier par une boucle ininterrompue de récepteurs et de conducteurs",
        4: "Chercher des informations sur les règles de sécurité électrique et les appliquer ; économiser l'électricité",
        5: "Produire et transporter l'électricité : centrales, sources renouvelables ou non, de la centrale à la prise (chiffres RTE 2025)"}
txt = lambda h: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()
pers = D["personnages"]

r = ["# La Centrale en panne — escape game de sciences (cycle 3, jeu n°14)", "",
     "Sciences et technologie, programme 2026 (BO n° 24 du 11 juin 2026), CM2, partie « Signaux » : électricité ; progression de l'enseignant : année A, période 3 :",
     "*Matière, mouvement, énergie et information. L'électricité.*", "",
     "**Jouer** : version immersive `../immersifs/electricite/` (5 grades : Stagiaire ≈ CE2, Électricien ≈ CM1, Technicien ≈ CM2, Ingénieur ≈ 6ᵉ, Chef de quart ≈ 5ᵉ).",
     "Ce dossier contient les **données sources** (format des jeux classiques) d'où la variante immersive est générée ; la version classique (pages `index.html`, `prof.html`) n'est pas encore écrite.", "",
     "**Sécurité** : aucune expérience ni manipulation avec le secteur ; seules les piles de la classe sont utilisées.", "",
     "## Fil narratif", "",
     "Un orage a plongé dans le noir la petite ville de Clairval (inventée). Les élèves, apprentis électriciens de la centrale, réparent salle après salle et retrouvent cinq mots qui ferment le dernier circuit :", "",
     "> " + D["metadata"]["phrase_bilan"], "",
     "| Salle | Lieu | Guide (personnage inventé) | Mot |", "|---|---|---|---|"]
for s in D["salles"]:
    p = s["dialogue_intro"]["perso"]
    r.append(f"| {s['num']} | {s['lieu']} | {pers[p]['nom']}, {pers[p]['role'].lower()} | {s['motCle']} |")
r += ["", "## 🎯 Compétences du programme (vue d'ensemble)", "", "| Salle | Compétence du programme |", "|---|---|"]
r += [f"| {n} | {c} |" for n, c in COMP.items()]
r += ["", "CM1 : 3 énigmes par salle (15) ; CM2 : 4 énigmes par salle (20). La notion est au programme de CM2 ; en CM1 (et au grade Stagiaire), le jeu reste sur le circuit à une boucle, les matériaux et la sécurité.", "",
      "## Solutions (générées depuis `assets/data/enigmes.json`)", ""]
for s, d in zip(E["salles"], D["salles"]):
    r.append(f"### Salle {s['num']} — {s['titre']} (mot : **{d['motCle']}**)")
    r.append("")
    for e in s["enigmes"]:
        r.append(f"- **{e['id']} {e['titre']}** ({e['type']}{', CM2' if e.get('niveaux') == ['CM2'] else ''}) : {txt(e['correction'])}")
    r.append("")
r += ["## Sources", ""] + [f"- {x.strip()}" for x in E["metadata"]["sources"].split(" ; ")] + [
      "", "## Fichiers", "",
      "- `assets/data/` : `enigmes.json`, `lecons.json`, `dialogues.json`, générés par `tests/donnees/gen_enigmes.py`, `gen_lecons.py`, `gen_dialogues.py` ; phrases des fiches dans `tests/donnees/fiches.py` (reprises mot pour mot par les justifications des grades) ; montages et schémas SVG par `tests/donnees/schemas.py`.",
      "- Variante immersive : `python vingt-mille-lieues/outils/immersif/migrer-jeu.py electricite --theme electricite/tests/donnees/theme-immersif.json --force`, puis `appliquer-grades.py electricite`, `appliquer-narration.py electricite`, `immersifs/electricite/outils/embarquer-donnees.py`.",
      "- Grades : `vingt-mille-lieues/outils/immersif/grades/electricite_s1..s5.py` et `electricite_theme.py` ; narration : `vingt-mille-lieues/outils/immersif/narration/electricite.json`.", ""]
open("README.md", "w", encoding="utf-8").write("\n".join(r))

g = ["# Guide pédagogique — La Centrale en panne (jeu n°14)", "", "## 1. Place dans les programmes", "",
     "Sciences et technologie, cycle 3 (arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026). L'électricité est au programme de **CM2** (partie « Signaux ») : circuit à une boucle avec une pile, un interrupteur et un ou deux récepteurs ; conducteurs et isolants ; schémas normalisés ; règles de sécurité électrique. La 6ᵉ reprend la conductivité et les risques domestiques.",
     "Progression de l'enseignant : année A, période 3. Suite de « L'Atelier de l'inventeur » (objets techniques) et de « La lumière » ; prépare les jeux sur le climat et les énergies et sur la programmation.", "",
     "## 🎯 Compétences du programme, énigme par énigme", "", "| Salle | Énigme | Type | Compétence du programme |", "|---|---|---|---|"]
for s in E["salles"]:
    for e in s["enigmes"]:
        g.append(f"| {s['num']} | {e['id']} {e['titre']} ({'CM2' if e.get('niveaux') == ['CM2'] else 'CM1-CM2'}) | {e['type']} | {COMP[s['num']]} |")
g += ["", "## 2. Déroulement conseillé", "",
      "- **Avant** : une séance de manipulation avec piles plates, lampes et fils (La main à la pâte) ; rappeler la règle : jamais d'expérience avec une prise.",
      "- **Pendant** (45 à 60 min) : équipes de 3 ou 4, une tablette ou un ordinateur par équipe ; tableau de bord enseignant `immersifs/electricite/prof.html`.",
      "- **Après** : faire réaliser pour de vrai le montage de la salle 1, puis le schéma de la salle 3 ; reprendre la phrase des cinq mots.", "",
      "## 3. Différenciation (grades)", "",
      "- **Stagiaire (≈ CE2)** : 15 énigmes courtes ; la salle 1 commence par un vrai montage interactif (poser le fil qui manque).",
      "- **Électricien (≈ CM1)** et **Technicien (≈ CM2)** : les énigmes des niveaux CM1 et CM2 ci-dessus.",
      "- **Ingénieur (≈ 6ᵉ)** et **Chef de quart (≈ 5ᵉ)** : 20 énigmes avec justification par une phrase de la fiche ; deux montages interactifs (deux lampes en série, puis lampes en dérivation et suppression d'un court-circuit) ; calculs sur les chiffres RTE 2025.", "",
      "## 4. Points de vigilance", "",
      "- Sécurité prioritaire : aucune manipulation avec le secteur ; la salle 4 rappelle pile 4,5 V sans danger, secteur 230 V dangereux, conduite à tenir (couper le courant, 18 ou 112).",
      "- Vocabulaire : pas d'électrons ; « tension » seulement pour les volts de la pile, de la prise et des lignes.",
      "- Conception fréquente à faire tomber : « le courant s'use dans la lampe » (salle 1).",
      "- Les chiffres de la production (RTE, Bilan électrique 2025) changent chaque année : les mettre à jour à chaque rentrée (`tests/donnees/fiches.py`, `gen_enigmes.py`, `electricite_s5.py`).", ""]
open("GUIDE-PEDAGOGIQUE.md", "w", encoding="utf-8").write("\n".join(g))
print("README.md et GUIDE-PEDAGOGIQUE.md écrits")
