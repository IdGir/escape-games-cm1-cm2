# -*- coding: utf-8 -*-
"""Génère README.md et GUIDE-PEDAGOGIQUE.md de vivant-ecosystemes/ depuis assets/data (solutions et compétences toujours à jour).
Lancer depuis vivant-ecosystemes/ : python tests/donnees/gen_docs.py"""
import json, re

E = json.load(open("assets/data/enigmes.json", encoding="utf-8"))
D = json.load(open("assets/data/dialogues.json", encoding="utf-8"))
COMP = {1: "Définir l'espèce comme un ensemble d'individus interféconds ; décrire un être vivant par ses attributs (CM1) ; la cellule, unité du vivant (prolongement 6e)",
        2: "Réaliser une classification en groupes emboîtés à partir d'attributs ; en déduire des liens de parenté ; identifier des espèces proches avec une clé de détermination (CM1)",
        3: "Distinguer les échelles du temps géologique et de l'histoire humaine ; caractériser l'évolution de la biodiversité grâce aux fossiles ; extinction massive de la fin du Crétacé et remplacement rapide d'espèces (CM2)",
        4: "Définir un écosystème : êtres vivants, milieu de vie et relations ; caractéristiques physiques du milieu ; relier la présence d'êtres vivants au milieu ; prédation et coopération (CM1)",
        5: "Représenter les liens alimentaires par un réseau (flèche de la proie vers le prédateur) ; effet d'une forte variation d'une espèce (surpêche, espèce invasive) ; conséquences d'une action humaine (CM1 ; EDD en CM2)"}
txt = lambda h: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()
pers = D["personnages"]

r = ["# L'Expédition biodiversité — escape game de sciences (cycle 3, jeu n°17)", "",
     "Sciences et technologie, programme 2026 (BO n° 24 du 11 juin 2026, annexe 2), parties « Unité et diversité du vivant » et « Les écosystèmes » ; progression de l'enseignant : année A, période 4 :",
     "*Le vivant, sa diversité et les fonctions qui le caractérisent. Panorama du vivant : organisation des êtres vivants et biodiversité actuelle et passée. La planète Terre. Écosystème : structure, fonctionnement et dynamique.*", "",
     "**Jouer** : version immersive `../immersifs/vivant-ecosystemes/` (5 grades : Promeneur ≈ CE2, Jeune naturaliste ≈ CM1, Naturaliste ≈ CM2, Écologue ≈ 6ᵉ, Conservateur de la réserve ≈ 5ᵉ).",
     "Ce dossier contient les **données sources** (format des jeux classiques) d'où la variante immersive est générée ; la version classique (pages `index.html`, `prof.html`) n'est pas écrite.", "",
     "**Vigilance** : vocabulaire du programme (« milieu de vie », « êtres vivants » ; ni biotope ni biocénose) ; pas de groupe « invertébrés » (on ne classe pas sur une absence) ; ton non alarmiste ; réserve et personnages inventés.", "",
     "## Fil narratif", "",
     "Le ruisseau a débordé sur le campement de l'expédition, dans la réserve naturelle (inventée) du Val-des-Saules, en Bourgogne : toutes les fiches sont mélangées. Les élèves, jeunes naturalistes, aident cinq experts et rassemblent cinq mots qui ouvrent la boîte de la carte du vivant :",
     "> " + D["metadata"]["phrase_bilan"], "",
     "| Étape | Lieu | Guide (personnage inventé) | Mot |", "|---|---|---|---|"]
for s in D["salles"]:
    p = s["dialogue_intro"]["perso"]
    r.append(f"| {s['num']} | {s['lieu']} | {pers[p]['nom']}, {pers[p]['role'][0].lower() + pers[p]['role'][1:]} | {s['motCle']} |")
r += ["", "## 🎯 Compétences du programme (vue d'ensemble)", "", "| Étape | Compétence du programme |", "|---|---|"]
r += [f"| {n} | {c} |" for n, c in COMP.items()]
r += ["", "CM1 : 3 énigmes par étape (15) ; CM2 : 4 énigmes par étape (20). Repères en CM1 (ordre des grandes étapes, mots simples) ; dates et calculs en millions d'années en CM2 (4,6 milliards, 540, 252, 66 millions d'années, 300 000 ans).", "",
      "## Solutions (générées depuis `assets/data/enigmes.json`)", ""]
for s, d in zip(E["salles"], D["salles"]):
    r.append(f"### Étape {s['num']} — {s['titre']} (mot : **{d['motCle']}**)")
    r.append("")
    for e in s["enigmes"]:
        r.append(f"<details><summary><b>{e['id']} {e['titre']}</b> ({e['type']}{', CM2' if e.get('niveaux') == ['CM2'] else ''})</summary>\n\n{txt(e['correction'])}\n\n</details>\n")
    r.append("")
r += ["## Sources", ""] + [f"- {x.strip()}" for x in E["metadata"]["sources"].split(" ; ")] + [
      "", "## Fichiers", "",
      "- `assets/data/` : `enigmes.json`, `lecons.json`, `dialogues.json`, générés par `tests/donnees/gen_enigmes.py`, `gen_lecons.py`, `gen_dialogues.py` ; phrases des fiches dans `tests/donnees/fiches.py` (reprises mot pour mot par les justifications des grades) ; schémas SVG dans `tests/donnees/schemas.py`.",
      "- Variante immersive : `python vingt-mille-lieues/outils/immersif/migrer-jeu.py vivant-ecosystemes --theme vivant-ecosystemes/tests/donnees/theme-immersif.json --force`, puis `appliquer-narration.py vivant-ecosystemes` et `finir-jeu.py vivant-ecosystemes` ; enfin remplacer « la étape » par « l'étape » dans `immersifs/vivant-ecosystemes/assets/data/*.json` (le migrateur écrit « la » devant le mot du thème) et relancer `outils/embarquer-donnees.py`.",
      "- Grades : `vingt-mille-lieues/outils/immersif/grades/vivant_ecosystemes_s1..s5.py` et `vivant_ecosystemes_theme.py` ; narration : `vingt-mille-lieues/outils/immersif/narration/vivant-ecosystemes.json`.", ""]
open("README.md", "w", encoding="utf-8").write("\n".join(r))

g = ["# Guide pédagogique — L'Expédition biodiversité (jeu n°17)", "", "## 1. Place dans les programmes", "",
     "Sciences et technologie, cycle 3 (BO n° 24 du 11 juin 2026, annexe 2). Le jeu couvre l'extrait de la progression de l'enseignant (année A, période 4) en suivant la répartition du programme :",
     "- **CM1** : classification du vivant (espèce, groupes emboîtés, parenté) ; identification avec une clé de détermination ; écosystème (milieu de vie, êtres vivants, relations de prédation et de coopération) ; réseaux alimentaires et effet d'une forte variation d'une espèce.",
     "- **CM2** : biodiversité passée (fossiles, échelle des temps géologiques, extinction massive de la fin du Crétacé) ; projets d'éducation au développement durable sur la biodiversité.",
     "- **6ᵉ** (grades Écologue et Conservateur, sections « Pour aller plus loin » des fiches) : la cellule, unité du vivant ; arbres de parenté ; place des végétaux à la base des réseaux ; décomposition.",
     "« Organisation des êtres vivants » : au CM1-CM2, le jeu l'aborde par les attributs observables ; la cellule et les organismes unicellulaires sont au programme de 6ᵉ. « La planète Terre » est traitée par le temps géologique ; l'activité interne de la Terre fait l'objet du jeu n°23.", "",
     "## 🎯 Compétences du programme, énigme par énigme", "", "| Étape | Énigme | Type | Compétence du programme |", "|---|---|---|---|"]
for s in E["salles"]:
    for e in s["enigmes"]:
        g.append(f"| {s['num']} | {e['id']} {e['titre']} ({'CM2' if e.get('niveaux') == ['CM2'] else 'CM1-CM2'}) | {e['type']} | {COMP[s['num']]} |")
g += ["", "## 2. Prérequis", "",
      "- Savoir qu'un être vivant naît, grandit, se nourrit, se reproduit et meurt (cycle 2).", "- Avoir observé des êtres vivants de l'environnement proche (cour, jardin, mare).", "",
      "## 3. Déroulés possibles", "",
      "- **Une séance de 60 à 75 min** : équipes de 3 ou 4, une tablette ou un ordinateur par équipe ; tableau de bord enseignant `immersifs/vivant-ecosystemes/prof.html`.",
      "- **Cinq séances de 25 min** : une étape par séance, la fiche de l'étape lue en fin de séance (bouton « Leçons A4 » des réglages).",
      "- **Avec une sortie** : jouer les étapes 1 et 2 avant une sortie à la mare ou au bois (inventaire, clé de détermination des petites bêtes de la litière), puis les étapes 4 et 5 au retour.", "",
      "## 4. Différenciation (grades)", "",
      "- **Promeneur (≈ CE2)** : 15 énigmes courtes, vocabulaire simple, premier indice offert.",
      "- **Jeune naturaliste (≈ CM1)** et **Naturaliste (≈ CM2)** : les énigmes des niveaux CM1 et CM2 ci-dessus.",
      "- **Écologue (≈ 6ᵉ)** et **Conservateur de la réserve (≈ 5ᵉ)** : 20 énigmes avec justification par une phrase de la fiche ; cellule, arbre de parenté, décomposition, prévisions sur un réseau, calculs en millions d'années.", "",
      "## 5. Lexique", "",
      "attribut, espèce, biodiversité, inventaire, classer, groupes emboîtés, parenté, clé de détermination, fossile, temps géologique, extinction massive, écosystème, milieu de vie, prédation, coopération, réseau alimentaire, proie, prédateur, espèce exotique envahissante ; 6ᵉ : cellule, membrane, noyau, paroi, unicellulaire, ancêtre commun, décomposition.", "",
      "## 6. Évaluation", "",
      "- Fin de jeu : la phrase des cinq mots à expliquer à l'oral.", "- Trace écrite : dessiner le réseau alimentaire d'un lieu proche (mare, haie, potager), flèches dans le bon sens.", "",
      "## 7. Points de vigilance", "",
      "- Classer n'est pas identifier : la clé de détermination donne un nom ; la classification montre la parenté.",
      "- On ne classe jamais sur une absence (« invertébrés », « sans pattes ») ni sur le lieu de vie (le dauphin n'est pas rangé avec les poissons).",
      "- La flèche d'un réseau alimentaire va de celui qui est mangé vers celui qui mange (« est mangé par ») : conception erronée fréquente.",
      "- Les termes biotope, biocénose, producteurs, consommateurs ne figurent pas au programme de CM1-CM2 : le jeu dit « milieu de vie » et « êtres vivants ».",
      "- Dates : « environ » pour les âges très anciens ; l'extinction de la fin du Crétacé a des causes encore discutées (météorite, volcanisme).",
      "- Ton non alarmiste : les espèces exotiques envahissantes sont présentées avec des gestes simples de protection.", "",
      "## 8. Sources", ""] + [f"- {x.strip()}" for x in E["metadata"]["sources"].split(" ; ")] + [""]
open("GUIDE-PEDAGOGIQUE.md", "w", encoding="utf-8").write("\n".join(g))
print("README.md et GUIDE-PEDAGOGIQUE.md écrits")
