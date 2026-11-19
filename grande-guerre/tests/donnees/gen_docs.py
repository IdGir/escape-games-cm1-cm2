# -*- coding: utf-8 -*-
"""Génère README.md et GUIDE-PEDAGOGIQUE.md de grande-guerre/ depuis assets/data (solutions et compétences toujours à jour).
Lancer depuis grande-guerre/ : python tests/donnees/gen_docs.py"""
import json, re

E = json.load(open("assets/data/enigmes.json", encoding="utf-8"))
D = json.load(open("assets/data/dialogues.json", encoding="utf-8"))
COMP = {1: "Comprendre les causes de la Première Guerre mondiale (rivalités entre puissances, alliances) ; situer l'attentat de Sarajevo et la mobilisation générale (1914) ; distinguer légende et réalité",
        2: "Décrire le déroulement de la guerre : le front, les tranchées et la vie des poilus ; batailles emblématiques (Verdun, la Somme, 1916) ; armes nouvelles ; soldats venus des colonies",
        3: "Décrire une guerre totale : l'arrière, le rôle des femmes dans les usines et les champs, les enfants, l'économie de guerre, les travailleurs venus des colonies",
        4: "Connaître la fin de la guerre et ses conséquences : armistice du 11 novembre 1918, traité de Versailles (1919), bilan humain (chiffres officiels)",
        5: "Comprendre la mémoire de la guerre (monuments aux morts, 11 novembre) et ses conséquences : colère, crise et montée des extrêmes (Italie, 1922), qui ouvre la voie aux régimes autoritaires"}
txt = lambda h: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()
pers = D["personnages"]

r = ["# Les Lettres du poilu — escape game d'histoire (cycle 3, jeu n°19)", "",
     "Histoire, programme 2026 (arrêté du 22 avril 2026, BO n° 22 du 28 mai 2026 : la Première Guerre mondiale est au programme de CM2) ; progression de l'enseignant : thème 6, année A, période 5 :",
     "*La France des guerres mondiales à l'UE. Deux guerres mondiales au XXème siècle : la première GM causes, déroulement, conséquence, montée des extrêmes, collaboration et résistance, victoire des alliés.*",
     "Ce jeu couvre la Première Guerre mondiale et le début de la « montée des extrêmes » ; collaboration, résistance et victoire des Alliés sont traitées dans le jeu n°20 « Radio Londres ».", "",
     "**Jouer** : version immersive `../immersifs/grande-guerre/` (5 grades : Lecteur ≈ CE2, Apprenti historien ≈ CM1, Historien ≈ CM2, Archiviste ≈ 6ᵉ, Gardien de la mémoire ≈ 5ᵉ).",
     "Ce dossier contient les **données sources** (format des jeux classiques) d'où la variante immersive est générée ; la version classique (pages `index.html`, `prof.html`) n'est pas écrite.", "",
     "**SUJET SENSIBLE — RELECTURE OBLIGATOIRE avant la classe** : ton du souvenir ; aucun détail violent ni photo de blessé ; aucun « gagner la guerre » comme mécanisme de jeu ; chiffres officiels avec source ; village, famille Garnier et registre des noms inventés ; les personnes réelles ne parlent jamais. Pour certaines familles, la guerre est une histoire proche : prévenir les élèves, laisser la parole libre.", "",
     "## Fil narratif", "",
     "Dans le grenier de l'école du village (inventé) de Vaux-les-Tilleuls, en Côte-d'Or, la classe trouve une boîte : cinq lettres reçues par Jeanne Garnier, la petite sœur du soldat Louis, de 1914 à 1922. L'humidité a effacé des mots ; les élèves historiens remettent de l'ordre dans chaque lettre et rassemblent cinq mots qui ouvrent la dernière lettre, fermée par un cadenas à date :",
     "> " + D["metadata"]["phrase_bilan"], "",
     "| Lettre | Lieu | Personnage (inventé) | Mot |", "|---|---|---|---|"]
for s in D["salles"]:
    p = s["dialogue_intro"]["perso"]
    r.append(f"| {s['num']} | {s['lieu']} | {pers[p]['nom']}, {pers[p]['role'][0].lower() + pers[p]['role'][1:]} | {s['motCle']} |")
r += ["", "## 🎯 Compétences du programme (vue d'ensemble)", "", "| Lettre | Compétence du programme |", "|---|---|"]
r += [f"| {n} | {c} |" for n, c in COMP.items()]
r += ["", "CM1 : 3 énigmes par lettre (15) ; CM2 : 4 énigmes par lettre (20). Repères en CM1 (début et fin de la guerre, ordre des événements) ; dates exactes et chiffres officiels en CM2 (28 juin 1914, 1er-3 août 1914, 1916, 11 novembre 1918 à 5 h 15, 28 juin 1919, 1,4 million, 8,7 millions, 600 000 veuves, 430 000 munitionnettes, 1922).", "",
      "## Solutions (générées depuis `assets/data/enigmes.json`)", ""]
for s, d in zip(E["salles"], D["salles"]):
    r.append(f"### {s['titre']} (mot : **{d['motCle']}**)")
    r.append("")
    for e in s["enigmes"]:
        r.append(f"<details><summary><b>{e['id']} {e['titre']}</b> ({e['type']}{', CM2' if e.get('niveaux') == ['CM2'] else ''})</summary>\n\n{txt(e['correction'])}\n\n</details>\n")
    r.append("")
r += ["## Sources", ""] + [f"- {x.strip()}" for x in E["metadata"]["sources"].split(" ; ")] + [
      "", "## Fichiers", "",
      "- `assets/data/` : `enigmes.json`, `lecons.json`, `dialogues.json`, générés par `tests/donnees/gen_enigmes.py`, `gen_lecons.py`, `gen_dialogues.py` ; phrases des fiches dans `tests/donnees/fiches.py` (reprises mot pour mot par les justifications des grades) ; schémas SVG dans `tests/donnees/schemas.py`.",
      "- Variante immersive : `python vingt-mille-lieues/outils/immersif/migrer-jeu.py grande-guerre --theme grande-guerre/tests/donnees/theme-immersif.json --force`, puis `appliquer-narration.py grande-guerre` et `finir-jeu.py grande-guerre`.",
      "- Prompts des médias : `python grande-guerre/tests/donnees/gen_medias.py` après chaque migration (le migrateur réécrit `medias.csv`), puis `prompts-flow.py grande-guerre`.",
      "- Grades : `vingt-mille-lieues/outils/immersif/grades/grande_guerre_s1..s5.py` et `grande_guerre_theme.py` ; narration : `vingt-mille-lieues/outils/immersif/narration/grande-guerre.json`.", ""]
open("README.md", "w", encoding="utf-8").write("\n".join(r))

g = ["# Guide pédagogique — Les Lettres du poilu (jeu n°19)", "", "## 1. Place dans les programmes", "",
     "Histoire, cycle 3 (arrêté du 22 avril 2026, BO n° 22 du 28 mai 2026) : la Première Guerre mondiale figure au programme de **CM2** (application en CM2 à la rentrée 2027). La progression de l'enseignant la place en année A, période 5 (thème 6 « La France des guerres mondiales à l'UE »). Le jeu couvre :",
     "- **les causes** : rivalités entre puissances, alliances, attentat de Sarajevo, mobilisation générale ;",
     "- **le déroulement** : le front et les tranchées, la vie des poilus, Verdun et la Somme, les armes nouvelles, les soldats des colonies ; l'arrière (femmes, enfants, économie de guerre) ;",
     "- **les conséquences** : armistice, traité de Versailles, bilan humain, mémoire (monuments aux morts, 11 novembre) ;",
     "- **le début de la montée des extrêmes** : colère des vaincus, crise, prise du pouvoir de Mussolini en Italie (1922). La crise de 1929, les régimes autoritaires, la collaboration, la résistance et la victoire des Alliés sont développés dans le jeu n°20 « Radio Londres ».", "",
     "## 🎯 Compétences du programme, énigme par énigme", "", "| Lettre | Énigme | Type | Compétence du programme |", "|---|---|---|---|"]
for s in E["salles"]:
    for e in s["enigmes"]:
        g.append(f"| {s['num']} | {e['id']} {e['titre']} ({'CM2' if e.get('niveaux') == ['CM2'] else 'CM1-CM2'}) | {e['type']} | {COMP[s['num']]} |")
g += ["", "## 2. Prérequis", "",
      "- Lire une frise chronologique (siècles, années).", "- Savoir qu'une lettre, une affiche, un registre sont des documents d'histoire (source, date, auteur).", "",
      "## 3. Déroulés possibles", "",
      "- **Une séance de 60 à 75 min** : équipes de 3 ou 4, une tablette ou un ordinateur par équipe ; tableau de bord enseignant `immersifs/grande-guerre/prof.html`.",
      "- **Cinq séances de 25 min** : une lettre par séance, la fiche de la lettre lue en fin de séance (bouton « Leçons A4 » des réglages).",
      "- **Avec une sortie** : avant la lettre 5, aller lire et photographier le monument aux morts de la commune ; chercher un nom dans la base Mémoire des hommes (avec l'enseignant) ; participer à la cérémonie du 11 novembre.", "",
      "## 4. Différenciation (grades)", "",
      "- **Lecteur (≈ CE2)** : 15 énigmes courtes, vocabulaire simple, premier indice offert.",
      "- **Apprenti historien (≈ CM1)** et **Historien (≈ CM2)** : les énigmes des niveaux CM1 et CM2 ci-dessus.",
      "- **Archiviste (≈ 6ᵉ)** et **Gardien de la mémoire (≈ 5ᵉ)** : 20 énigmes avec justification par une phrase de la fiche ; dates exactes, chiffres officiels, raisonnement sur les causes et les conséquences.", "",
      "## 5. Gestion de classe et sensibilité du sujet", "",
      "- Présenter le jeu comme une enquête de mémoire, pas comme un jeu de guerre : on ne « gagne » pas la guerre, on ouvre une lettre.",
      "- Prévenir que des élèves peuvent avoir un aïeul sur un monument ; laisser la parole libre, sans obligation.",
      "- Aucune image de blessé ou de combat : décors de lieux (village, abri, usine, hôpital, monument).", "",
      "## 6. Lexique", "",
      "alliance, attentat, mobilisation, déclaration de guerre, propagande, front, tranchée, poilu, censure, tirailleur, arrière, munitionnette, économie de guerre, armistice, traité, réparations, veuve, orphelin, monument aux morts, commémorer, « mort pour la France », régime autoritaire, extrémiste.", "",
      "## 7. Évaluation", "",
      "- Fin de jeu : la phrase des cinq mots à expliquer à l'oral.", "- Trace écrite : une frise 1914-1922 avec cinq repères ; ou une courte lettre de Jeanne à Louis décrivant l'arrière.",
      "- Évaluations imprimables (QCM, vrai/faux, études de documents) : à produire avec les leçons A4.", "",
      "## 8. Points de vigilance notionnels", "",
      "- Armistice n'est pas paix : la paix est signée à Versailles le 28 juin 1919.",
      "- 1er août 1914 : l'affiche est collée ; 2 août : premier jour de la mobilisation ; 3 août : l'Allemagne déclare la guerre à la France.",
      "- « La fleur au fusil » : image de propagande ; la plupart partent avec résignation et sens du devoir.",
      "- Chiffres : uniquement les chiffres officiels du jeu (1,4 million de soldats français morts, 8,7 millions de mobilisés, près de 600 000 veuves) ; dire « près de », « environ ».",
      "- Soldats des colonies : environ 600 000 combattants ; ne pas les oublier dans le récit national.",
      "- Le registre de la lettre 5 et les noms sont inventés : pour une vraie enquête, la base Mémoire des hommes.", "",
      "## 9. Sources", ""] + [f"- {x.strip()}" for x in E["metadata"]["sources"].split(" ; ")] + [""]
open("GUIDE-PEDAGOGIQUE.md", "w", encoding="utf-8").write("\n".join(g))
print("README.md et GUIDE-PEDAGOGIQUE.md écrits")
