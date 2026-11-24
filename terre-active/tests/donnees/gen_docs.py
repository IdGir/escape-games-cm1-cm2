# -*- coding: utf-8 -*-
"""Génère README.md et GUIDE-PEDAGOGIQUE.md de terre-active/ depuis assets/data (solutions et compétences toujours à jour).
Lancer depuis terre-active/ : python tests/donnees/gen_docs.py"""
import json, re

E = json.load(open("assets/data/enigmes.json", encoding="utf-8"))
D = json.load(open("assets/data/dialogues.json", encoding="utf-8"))
COMP = {1: "Repérer des manifestations de l'activité interne ou externe de la Terre (CM2) ; modéliser l'intérieur du globe (croûte, manteau, noyau) — approfondissement, cycle 4",
        2: "Concevoir, mettre en œuvre et discuter une modélisation simple (maquette) d'un phénomène (CM2) ; plaques et frontières de plaques — approfondissement, cycle 4",
        3: "Repérer des manifestations de l'activité interne de la Terre : l'éruption volcanique, ses produits, des exemples français, une étude de cas historique (CM2)",
        4: "Repérer des manifestations de l'activité interne de la Terre : le séisme (foyer, épicentre, ondes, sismographe, magnitude) ; savoir qu'on ne prévoit pas le jour d'un séisme (CM2)",
        5: "Définir la notion de risque naturel et identifier les mesures de prévention et de protection associées, à partir d'un exemple (séisme, éruption volcanique) (CM2)"}
txt = lambda h: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()
pers = D["personnages"]

r = ["# L'Observatoire des volcans — escape game de sciences (cycle 3, jeu n°23)", "",
     "Sciences et technologie, programme 2026 (BO n° 24 du 11 juin 2026, annexe 2), thème « La Terre, une planète active », CM2 « L'activité terrestre » ; progression de l'enseignant : année A, période 5 :",
     "*La planète Terre. L'activité interne.*", "",
     "**Jouer** : version immersive `../immersifs/terre-active/` (5 grades : Visiteur de l'observatoire ≈ CE2, Apprenti géologue ≈ CM1, Observateur ≈ CM2, Volcanologue ≈ 6ᵉ, Directeur de l'observatoire ≈ 5ᵉ).",
     "Ce dossier contient les **données sources** (format des jeux classiques) d'où la variante immersive est générée ; la version classique (pages `index.html`, `prof.html`) n'est pas écrite.", "",
     "**Vigilance** : ton rassurant (les risques existent, on sait s'y préparer) ; personne ne sait prévoir le jour d'un séisme ; la catastrophe de Saint-Pierre (1902) est évoquée avec sobriété ; station, village et personnages inventés.", "",
     "## Fil narratif", "",
     "Une classe de Bourgogne est jumelée avec l'école de Bois-Clair, village (inventé) au pied du volcan, sur l'île de La Réunion. Cette nuit, la station d'observation des Hauts (inventée) a enregistré de petits séismes sous le volcan, et une secousse a tout renversé. Les élèves, jeunes volcanologues et sismologues, aident cinq personnes et rassemblent cinq mots qui composent le message d'information des habitants :",
     "> " + D["metadata"]["phrase_bilan"], "",
     "| Salle | Lieu | Guide (personnage inventé) | Mot |", "|---|---|---|---|"]
for s in D["salles"]:
    p = s["dialogue_intro"]["perso"]
    r.append(f"| {s['num']} | {s['lieu']} | {pers[p]['nom']}, {pers[p]['role'][0].lower() + pers[p]['role'][1:]} | {s['motCle']} |")
r += ["", "## 🎯 Compétences du programme (vue d'ensemble)", "", "| Salle | Compétence du programme |", "|---|---|"]
r += [f"| {n} | {c} |" for n, c in COMP.items()]
r += ["", "CM1 : 3 énigmes par salle (15) ; CM2 : 4 énigmes par salle (20). Repères en CM1 (mots, schémas, bons réflexes) ; dates et chiffres exacts en CM2 (2 900 km, 6 400 km, 8 mai 1902, 1976, 2018, magnitude 4,8 du Teil en 2019, cinq zones de sismicité).", "",
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
      "- Variante immersive : `python vingt-mille-lieues/outils/immersif/migrer-jeu.py terre-active --theme terre-active/tests/donnees/theme-immersif.json --force`, puis `appliquer-narration.py terre-active`, `finir-jeu.py terre-active` et `python terre-active/tests/donnees/gen_medias.py` (prompts des médias), enfin `prompts-flow.py terre-active`.",
      "- Grades : `vingt-mille-lieues/outils/immersif/grades/terre_active_s1..s5.py` et `terre_active_theme.py` ; narration : `vingt-mille-lieues/outils/immersif/narration/terre-active.json`.", ""]
open("README.md", "w", encoding="utf-8").write("\n".join(r))

g = ["# Guide pédagogique — L'Observatoire des volcans (jeu n°23)", "", "## 1. Place dans les programmes", "",
     "Sciences et technologie, cycle 3 (BO n° 24 du 11 juin 2026, annexe 2), thème « La Terre, une planète active ». Le programme place l'activité interne au **CM2**, partie « L'activité terrestre » :",
     "- repérer des manifestations de l'activité interne ou externe de la Terre ;",
     "- définir la notion de risque naturel et identifier les mesures de prévention et de protection associées, à partir d'un exemple au choix (ici : séisme et éruption volcanique) ;",
     "- concevoir, mettre en œuvre et discuter une modélisation simple (maquette) ; étude de cas historique ou actuel.",
     "Le CM1 du programme ne traite que la météorologie dans ce thème : en classe à double niveau, les CM1 jouent ici une première approche (repères, mots, bons réflexes).",
     "La **structure interne du globe** (croûte, manteau, noyau) et les **plaques** ne sont pas nommées par le programme de cycle 3 : le jeu les utilise comme modèle simple pour expliquer l'origine interne des volcans et des séismes (prolongement au cycle 4, grades Volcanologue et Directeur de l'observatoire).", "",
     "## 🎯 Compétences du programme, énigme par énigme", "", "| Salle | Énigme | Type | Compétence du programme |", "|---|---|---|---|"]
for s in E["salles"]:
    for e in s["enigmes"]:
        g.append(f"| {s['num']} | {e['id']} {e['titre']} ({'CM2' if e.get('niveaux') == ['CM2'] else 'CM1-CM2'}) | {e['type']} | {COMP[s['num']]} |")
g += ["", "## 2. Prérequis", "",
      "- Avoir mené la séquence de météorologie (activité externe : vent, pluie, tempête).", "- Savoir lire un schéma en coupe avec des repères numérotés.", "",
      "## 3. Déroulés possibles", "",
      "- **Une séance de 60 à 75 min** : équipes de 3 ou 4, une tablette ou un ordinateur par équipe ; tableau de bord enseignant `immersifs/terre-active/prof.html`.",
      "- **Cinq séances de 25 min** : une salle par séance, la fiche de la salle lue en fin de séance (bouton « Leçons A4 » des réglages).",
      "- **Avec une maquette** : avant la salle 2, construire en classe la maquette de Noé (deux plaques de polystyrène sur de la pâte à modeler) et discuter de ses limites (vitesse, taille) ; après la salle 5, faire l'exercice « séisme » de l'école (PPMS) et le comparer à la fiche d'Adèle.", "",
      "## 4. Différenciation (grades)", "",
      "- **Visiteur de l'observatoire (≈ CE2)** : 15 énigmes courtes, vocabulaire simple, premier indice offert.",
      "- **Apprenti géologue (≈ CM1)** et **Observateur (≈ CM2)** : les énigmes des niveaux CM1 et CM2 ci-dessus.",
      "- **Volcanologue (≈ 6ᵉ)** et **Directeur de l'observatoire (≈ 5ᵉ)** : 20 énigmes avec justification par une phrase de la fiche ; frontières de plaques, éruptions effusives et explosives, comparaison de magnitudes, limites d'un modèle, chaîne d'alerte.", "",
      "## 5. Lexique", "",
      "activité interne, activité externe, croûte, manteau, noyau, plaque, frontière de plaques, maquette, modéliser, magma, chambre magmatique, cheminée, cratère, lave, cendres, gaz, nuée ardente, éruption effusive, éruption explosive, séisme, faille, foyer, épicentre, ondes sismiques, sismographe, sismogramme, magnitude, réplique, tsunami, risque naturel, prévention, protection, observatoire, évacuer.", "",
      "## 6. Évaluation", "",
      "- Fin de jeu : la phrase des cinq mots à expliquer à l'oral.", "- Trace écrite : légender un volcan et un séisme en coupe ; écrire les trois bons réflexes pendant un séisme.", "",
      "## 7. Points de vigilance", "",
      "- Ton rassurant : les risques existent, on sait s'y préparer. Ne pas laisser croire qu'on prévoit le jour d'un séisme ; on sait seulement où il est probable.",
      "- Consignes de sécurité : celles des préfectures (DDRM) et du ministère de l'Europe et des Affaires étrangères, relues en novembre 2026. Elles diffèrent légèrement selon les documents (sortir ou non quand on est au rez-de-chaussée) : le jeu retient « rester où l'on est » pendant les secousses, comme à l'école. Se référer au PPMS de l'école.",
      "- La catastrophe de Saint-Pierre (8 mai 1902) n'est chiffrée qu'en CM2 et à partir du grade Observateur, sans image ; prévoir un temps d'échange si des élèves ont de la famille aux Antilles.",
      "- Les tailles de la maquette sont fausses (la croûte est dessinée bien plus épaisse) : le dire aux élèves, c'est l'occasion de parler des limites d'un modèle.",
      "- Chiffres arrondis : « environ » 30 km, 2 900 km, 6 400 km ; vitesse des plaques « quelques centimètres par an ».", "",
      "## 8. Sources", ""] + [f"- {x.strip()}" for x in E["metadata"]["sources"].split(" ; ")] + [""]
open("GUIDE-PEDAGOGIQUE.md", "w", encoding="utf-8").write("\n".join(g))
print("README.md et GUIDE-PEDAGOGIQUE.md écrits")
