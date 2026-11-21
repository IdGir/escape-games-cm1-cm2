# -*- coding: utf-8 -*-
"""Génère README.md et GUIDE-PEDAGOGIQUE.md de seconde-guerre/ depuis assets/data (solutions et compétences toujours à jour).
Lancer depuis seconde-guerre/ : python tests/donnees/gen_docs.py"""
import json, re

E = json.load(open("assets/data/enigmes.json", encoding="utf-8"))
D = json.load(open("assets/data/dialogues.json", encoding="utf-8"))
COMP = {1: "Comprendre la montée des extrêmes après la Première Guerre mondiale : la crise de 1929, les régimes totalitaires (fascisme en Italie, nazisme en Allemagne, communisme soviétique), la démocratie menacée",
        2: "Connaître le début de la Seconde Guerre mondiale et la défaite de 1940 : l'exode, l'armistice, l'appel du 18 juin 1940, le régime de Vichy et la collaboration",
        3: "Décrire la vie quotidienne sous l'Occupation (rationnement, STO) ; connaître les persécutions et la Shoah, génocide des Juifs d'Europe, et l'action des Justes (leçon et discussion, sans énigme notée)",
        4: "Connaître la Résistance : refus de la défaite, France libre, Radio Londres, journaux, réseaux et maquis, Jean Moulin et le Conseil national de la Résistance",
        5: "Connaître la victoire des Alliés et la Libération : débarquements de 1944, libération de Paris, capitulation de l'Allemagne le 8 mai 1945, retour de la République et vote des femmes"}
txt = lambda h: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()
pers = D["personnages"]
SENS = ("**SUJET TRÈS SENSIBLE — RELECTURE OBLIGATOIRE avant la classe.** Les élèves sont de jeunes messagers : ils ne sont jamais mis en position de victime ni de bourreau. "
        "Les persécutions et la Shoah sont enseignées dans la fiche de la fréquence 3, avec sobriété, **sans aucune énigme notée ni point gagné à leur sujet**, et sans aucune image de camp. "
        "Vocabulaire exact : Shoah, génocide des Juifs d'Europe. La France de 1940-1944 n'est pas réduite à la Résistance : Vichy, la collaboration et l'attente de la majorité sont présentés. "
        "Aucun symbole nazi, aucun uniforme allemand, aucun combat dans les décors. Village, familles et personnages inventés ; les personnes réelles ne parlent jamais. "
        "Prévoir un temps de parole après la fréquence 3 et à la fin du jeu (pistes ci-dessous dans le guide).")

r = ["# Radio Londres — escape game d'histoire (cycle 3, jeu n°20)", "",
     "Histoire, programme 2026 (arrêté du 22 avril 2026, BO n° 22 du 28 mai 2026 ; niveau exact de la Seconde Guerre mondiale à confirmer, cf. `A-VERIFIER.md`) ; progression de l'enseignant : thème 6, année A, période 5 :",
     "*La France des guerres mondiales à l'UE. Deux guerres mondiales au XXème siècle : la première GM causes, déroulement, conséquence, montée des extrêmes, collaboration et résistance, victoire des alliés.*",
     "Ce jeu fait suite aux « Lettres du poilu » (n°19, Première Guerre mondiale) : il couvre la montée des extrêmes, la collaboration et la résistance, la victoire des Alliés. Il ouvre sur la construction européenne (jeu n°22).", "",
     "**Jouer** : version immersive `../immersifs/seconde-guerre/` (5 grades : Jeune auditeur ≈ CE2, Messager ≈ CM1, Agent de liaison ≈ CM2, Archiviste ≈ 6ᵉ, Passeur de mémoire ≈ 5ᵉ).",
     "Ce dossier contient les **données sources** (format des jeux classiques) d'où la variante immersive est générée ; la version classique (pages `index.html`, `prof.html`) n'est pas écrite.", "",
     "## ⚠️ Avertissement pour l'enseignant", "", SENS, "",
     "## Fil narratif", "",
     "Dans la cave de l'école du village (inventé) de Chantelune-en-Morvan, dans la Nièvre, la classe trouve un vieux poste de radio clandestin. Lucie, agente de liaison en 1944, y a laissé un message : un message de Londres est arrivé en cinq morceaux, sur cinq fréquences. Chaque fréquence ramène les élèves, jeunes messagers, dans un souvenir de 1938 à 1945 ; ils rassemblent cinq mots qui allument le poste :",
     "> " + D["metadata"]["phrase_bilan"], "",
     "| Fréquence | Lieu | Personnage (inventé) | Mot |", "|---|---|---|---|"]
for s in D["salles"]:
    p = s["dialogue_intro"]["perso"]
    r.append(f"| {s['num']} | {s['lieu']} | {pers[p]['nom']}, {pers[p]['role'][0].lower() + pers[p]['role'][1:]} | {s['motCle']} |")
r += ["", "## 🎯 Compétences du programme (vue d'ensemble)", "", "| Fréquence | Compétence du programme |", "|---|---|"]
r += [f"| {n} | {c} |" for n, c in COMP.items()]
r += ["", "CM1 : 3 énigmes par fréquence (15) ; CM2 : 4 énigmes par fréquence (20). Repères en CM1 (ordre des événements, années) ; dates exactes en CM2 (30 janvier 1933, 1er et 3 septembre 1939, 10 mai, 14, 17, 18 et 22 juin 1940, 10 juillet 1940, 16 février 1943, 27 mai 1943, 6 juin, 15 et 25 août, 11 septembre 1944, 8 mai 1945).", "",
      "## Solutions (générées depuis `assets/data/enigmes.json`)", ""]
for s, d in zip(E["salles"], D["salles"]):
    r.append(f"### {s['titre']} (mot : **{d['motCle']}**)")
    r.append("")
    for e in s["enigmes"]:
        r.append(f"<details><summary><b>{e['id']} {e['titre']}</b> ({e['type']}{', CM2' if e.get('niveaux') == ['CM2'] else ''})</summary>\n\n{txt(e['correction'])}\n\n</details>\n")
    r.append("")
r += ["## Sources", ""] + [f"- {x.strip()}" for x in E["metadata"]["sources"].split(" ; ")] + [
      "", "## Fichiers", "",
      "- `assets/data/` : `enigmes.json`, `lecons.json`, `dialogues.json`, générés par `tests/donnees/gen_enigmes.py`, `gen_lecons.py`, `gen_dialogues.py` ; phrases des fiches dans `tests/donnees/fiches.py` (reprises mot pour mot par les justifications des grades) ; cartes et frise SVG dans `tests/donnees/schemas.py`.",
      "- Variante immersive : `python vingt-mille-lieues/outils/immersif/migrer-jeu.py seconde-guerre --theme seconde-guerre/tests/donnees/theme-immersif.json --force`, puis `appliquer-narration.py seconde-guerre` et `finir-jeu.py seconde-guerre`.",
      "- Prompts des médias : `python seconde-guerre/tests/donnees/gen_medias.py` après chaque migration (le migrateur réécrit `medias.csv`), puis `prompts-flow.py seconde-guerre`.",
      "- Grades : `vingt-mille-lieues/outils/immersif/grades/seconde_guerre_s1..s5.py` et `seconde_guerre_theme.py` ; narration : `vingt-mille-lieues/outils/immersif/narration/seconde-guerre.json`.", ""]
open("README.md", "w", encoding="utf-8").write("\n".join(r))

g = ["# Guide pédagogique — Radio Londres (jeu n°20)", "", "## ⚠️ Avertissement", "", SENS, "",
     "## 1. Place dans les programmes", "",
     "Histoire, cycle 3 (arrêté du 22 avril 2026, BO n° 22 du 28 mai 2026). La progression de l'enseignant place la Seconde Guerre mondiale en année A, période 5 (thème 6 « La France des guerres mondiales à l'UE »), juste après la Première Guerre mondiale. Le jeu couvre :",
     "- **la montée des extrêmes** : crise de 1929, régimes totalitaires (fascisme, nazisme, communisme soviétique), démocratie menacée ;",
     "- **la défaite et Vichy** : 1939-1940, exode, armistice, appel du 18 Juin, État français, collaboration ;",
     "- **l'Occupation** : rationnement, STO ; persécutions, Shoah et Justes (leçon et discussion) ;",
     "- **la Résistance** : France libre, Radio Londres, journaux, réseaux, maquis du Morvan, Jean Moulin et le CNR ;",
     "- **la victoire des Alliés** : débarquements, Libération, 8 mai 1945, retour de la République, vote des femmes, « plus jamais ça ».", "",
     "## 🎯 Compétences du programme, énigme par énigme", "", "| Fréquence | Énigme | Type | Compétence du programme |", "|---|---|---|---|"]
for s in E["salles"]:
    for e in s["enigmes"]:
        g.append(f"| {s['num']} | {e['id']} {e['titre']} ({'CM2' if e.get('niveaux') == ['CM2'] else 'CM1-CM2'}) | {e['type']} | {COMP[s['num']]} |")
g += ["", "## 2. Prérequis", "",
      "- Avoir étudié la Première Guerre mondiale (jeu n°19 « Les Lettres du poilu »).", "- Lire une frise et une carte simple ; savoir qu'un discours radio, une affiche, un ticket sont des documents d'histoire.", "",
      "## 3. Déroulés possibles", "",
      "- **Une séance de 60 à 75 min** : équipes de 3 ou 4 ; tableau de bord enseignant `immersifs/seconde-guerre/prof.html`. Faire une pause collective après la fréquence 3.",
      "- **Cinq séances de 25 min** : une fréquence par séance, la fiche lue en fin de séance (bouton « Leçons A4 » des réglages). La séance 3 se termine par la lecture de la fiche « Vivre sous l'Occupation » en classe entière.",
      "- **Avec une sortie ou un témoignage** : Musée de la Résistance en Morvan (Saint-Brisson), stèles et plaques de la commune, cérémonie du 8 mai.", "",
      "## 4. Différenciation (grades)", "",
      "- **Jeune auditeur (≈ CE2)** : 15 énigmes courtes, vocabulaire simple, premier indice offert.",
      "- **Messager (≈ CM1)** et **Agent de liaison (≈ CM2)** : les énigmes des niveaux CM1 et CM2 ci-dessus.",
      "- **Archiviste (≈ 6ᵉ)** et **Passeur de mémoire (≈ 5ᵉ)** : 20 énigmes avec justification par une phrase de la fiche ; nuances (résister, collaborer, attendre), calculs de durées, chaînes de causes.", "",
      "## 5. Gestion de classe et pistes de discussion", "",
      "- Présenter le jeu comme une enquête sur un message, pas comme un jeu de guerre ; aucun point n'est gagné sur les persécutions.",
      "- Après la fréquence 3 : lire ensemble la partie « Les persécutions » de la fiche ; répondre simplement aux questions ; ne montrer aucune image de camp. Ressource : Mémorial de la Shoah, pages pédagogiques pour l'école.",
      "- Questions pour discuter : « Qu'est-ce qui fait qu'une démocratie peut disparaître ? » ; « Pourquoi Madeleine prend-elle un risque ? » (les Justes) ; « Pourquoi la plupart des Français n'étaient-ils ni résistants ni collaborateurs ? » ; « Que veut dire “plus jamais ça” aujourd'hui ? » (lien avec le jeu n°22 sur l'Europe).",
      "- Certains élèves peuvent avoir une histoire familiale liée à la guerre, à la déportation ou à l'exil : laisser la parole libre, sans obligation.", "",
      "## 6. Lexique", "",
      "crise économique, dictature, régime totalitaire, fascisme, nazisme, antisémitisme, démocratie, propagande, exode, armistice, ligne de démarcation, Occupation, collaboration, appel du 18 Juin, rationnement, ticket, ersatz, marché noir, STO, réfractaire, persécution, Shoah, génocide, Juste parmi les Nations, résistant, clandestin, maquis, réseau, agent de liaison, CNR, débarquement, Alliés, Libération, capitulation, droit de vote, ONU.", "",
      "## 7. Évaluation", "",
      "- Fin de jeu : la phrase des cinq mots à expliquer à l'oral.", "- Trace écrite : une frise 1929-1945 avec six repères ; ou un « message personnel » de Radio Londres expliqué en deux phrases.",
      "- Évaluations imprimables (QCM, vrai/faux, études de documents) : à produire avec les leçons A4.", "",
      "## 8. Points de vigilance notionnels", "",
      "- Armistice (22 juin 1940) n'est pas paix ; l'État français de Vichy n'est pas la République (10 juillet 1940).",
      "- « Zone libre » : dire de préférence « zone non occupée » ; elle est envahie à son tour en novembre 1942 (à mentionner en CM2 si une question vient).",
      "- La Résistance est d'abord une minorité ; la collaboration est un choix du régime de Vichy ; la plupart des Français essaient de survivre.",
      "- Chiffres : uniquement ceux du jeu, avec leur source (75 721 déportés, 2 566 survivants, environ 13 000 arrêtés au Vél d'Hiv) ; ne pas en ajouter.",
      "- Les catégories des cartes d'alimentation de la fréquence 3 sont un barème simplifié ; la famille de Madeleine est inventée.", "",
      "## 9. Sources", ""] + [f"- {x.strip()}" for x in E["metadata"]["sources"].split(" ; ")] + [""]
open("GUIDE-PEDAGOGIQUE.md", "w", encoding="utf-8").write("\n".join(g))
print("README.md et GUIDE-PEDAGOGIQUE.md écrits")
