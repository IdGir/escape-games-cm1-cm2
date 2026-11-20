#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les évaluations imprimables de « L'Expédition biodiversité » (jeu n°17, vivant et écosystèmes).

    python vivant-ecosystemes/outils/generer-evaluations.py

Écrit vivant-ecosystemes/assets/data/evaluations.json (format commun des jeux) et
vivant-ecosystemes/assets/data/evaluations-embarquees.js (copie lue en double-clic, file://).
Page d'impression : vivant-ecosystemes/evaluations-imprimables.html.
Tous les faits viennent des leçons du jeu (assets/data/lecons.json). Les documents marqués
« inventé pour le jeu » sont des carnets d'observation de la réserve (inventée) du Val-des-Saules.
"""
import json, os
ICI = os.path.dirname(os.path.abspath(__file__))
JEU = os.path.dirname(ICI)

def q(texte, options, bonne): return {"q": texte, "options": options, "bonne": bonne, "pts": 1}
def vf(texte, rep): return {"q": texte, "type": "vf", "bonne": rep, "pts": 1}
def court(texte, rep): return {"q": texte, "type": "court", "rep": rep, "pts": 1}

EVAL = {
 "metadata": {
  "sujet": "Observer le vivant et définir l'espèce, classer en groupes emboîtés et identifier, la biodiversité passée et les fossiles, l'écosystème, le réseau alimentaire",
  "niveaux": ["CM1", "CM2"],
  "programme": "Sciences et technologie, cycle 3 — « Unité et diversité du vivant » et « Les écosystèmes » (programme 2026, BO n° 24 du 11 juin 2026). Progression de l'enseignant : année A, période 4. Repères en CM1, chiffres en millions d'années en CM2.",
  "sources": "Leçons du jeu (assets/data/lecons.json) ; voir README.md et A-VERIFIER.md du jeu."
 },
 "quizz_final": {
  "CM1": [
   q("Ce que possède un être vivant et que l'on peut observer s'appelle...", ["un attribut", "un milieu", "une proie"], 0),
   q("Pour classer les êtres vivants, on utilise...", ["leur lieu de vie", "les attributs qu'ils possèdent", "ce qu'ils mangent"], 1),
   q("Un fossile se trouve...", ["dans l'air", "dans une ruche", "dans une roche"], 2),
   q("L'abeille transporte le pollen d'une fleur à l'autre : c'est...", ["de la coopération", "de la prédation", "une extinction"], 0),
   q("Dans un réseau alimentaire, la flèche va...", ["du prédateur vers la proie", "de la proie vers celui qui la mange", "de l'eau vers le soleil"], 1)],
  "CM2": [
   q("L'âne et le cheval sont deux espèces différentes parce que...", ["ils n'ont pas la même couleur", "le mulet ne peut pas avoir de petits", "ils ne vivent pas au même endroit"], 1),
   q("Une clé de détermination sert à...", ["trouver le nom d'un être vivant", "dater un fossile", "mesurer la température d'une mare"], 0),
   q("Les dinosaures et les ammonites ont disparu il y a environ...", ["300 000 ans", "4,6 milliards d'années", "66 millions d'années"], 2),
   q("Laquelle est une caractéristique physique du milieu ?", ["la prédation", "l'humidité", "le pollen"], 1),
   q("L'écrevisse de Louisiane, introduite en France, est...", ["une espèce exotique envahissante", "un fossile", "un décomposeur"], 0)]
 },
 "fiches_preparatoires": [
  {"salle": 1, "titre": "La tente-laboratoire — Observer le vivant, l'espèce",
   "objectifs": ["Décrire un être vivant par ses attributs", "Savoir ce qu'est une espèce"],
   "vocabulaire": [{"mot": "attribut", "def": "ce que possède un être vivant et que l'on peut observer"}, {"mot": "espèce", "def": "êtres vivants qui se ressemblent et peuvent avoir ensemble des petits, eux-mêmes capables d'avoir des petits"}, {"mot": "inventaire", "def": "liste des espèces observées dans un lieu"}],
   "contexte": "On observe ce que l'être vivant possède (plumes, poils, coquille, pattes) et on compte avec précision. Un caniche et un berger allemand sont de la même espèce."},
  {"salle": 2, "titre": "La cabane du garde — Classer et identifier",
   "objectifs": ["Ranger des êtres vivants dans des groupes emboîtés", "Utiliser une clé de détermination"],
   "vocabulaire": [{"mot": "classer", "def": "ranger dans des groupes selon des attributs communs"}, {"mot": "groupes emboîtés", "def": "groupes rangés les uns dans les autres"}, {"mot": "clé de détermination", "def": "suite de questions qui permet de trouver le nom d'un être vivant"}],
   "contexte": "On classe avec ce que les êtres vivants possèdent, jamais avec ce qu'ils ne possèdent pas, ni avec leur lieu de vie."},
  {"salle": 3, "titre": "L'ancienne carrière — La biodiversité passée",
   "objectifs": ["Savoir ce qu'est un fossile", "Ranger dans l'ordre de grands repères du temps géologique"],
   "vocabulaire": [{"mot": "fossile", "def": "reste ou trace d'un être vivant ancien conservé dans une roche"}, {"mot": "temps géologique", "def": "temps de l'histoire de la Terre, compté en millions d'années"}, {"mot": "extinction massive", "def": "disparition d'un très grand nombre d'espèces en peu de temps"}],
   "contexte": "Les fossiles montrent que des espèces apparaissent et disparaissent. Les dinosaures ont disparu bien avant l'arrivée des humains."},
  {"salle": 4, "titre": "La mare et le pré fleuri — L'écosystème",
   "objectifs": ["Définir un écosystème", "Donner un exemple de prédation et de coopération"],
   "vocabulaire": [{"mot": "écosystème", "def": "un milieu de vie, les êtres vivants qui l'habitent et leurs relations"}, {"mot": "milieu de vie", "def": "lieu décrit par sa température, sa lumière, son humidité…"}, {"mot": "coopération", "def": "relation où chacun gagne"}],
   "contexte": "La grenouille pond dans la mare et chasse dans la prairie ; le héron la mange ; l'abeille et la fleur s'entraident."},
  {"salle": 5, "titre": "Le ponton de l'étang — Le réseau alimentaire",
   "objectifs": ["Dessiner un réseau alimentaire avec des flèches", "Expliquer ce qui arrive quand une espèce change beaucoup"],
   "vocabulaire": [{"mot": "réseau alimentaire", "def": "ensemble des chaînes « est mangé par » d'un écosystème"}, {"mot": "proie", "def": "être vivant mangé par un autre"}, {"mot": "espèce exotique envahissante", "def": "espèce venue d'ailleurs qui se multiplie et perturbe l'écosystème"}],
   "contexte": "Algues, têtards, larves de libellule, perches et héron : si l'on pêche trop de perches, tout le réseau est touché."}
 ],
 "qcm": {
  "CM1": [
   q("Lequel est un attribut de l'oiseau ?", ["il vit dans les arbres", "il a des plumes", "il mange des graines"], 1),
   q("Un caniche et un berger allemand sont...", ["de la même espèce", "de deux espèces différentes", "deux insectes"], 0),
   q("Noter toutes les espèces d'un lieu, c'est faire...", ["un réseau", "une clé", "un inventaire"], 2),
   q("Combien de pattes a un insecte ?", ["6", "8", "14"], 0),
   q("Combien de pattes a une araignée ?", ["6", "8", "4"], 1),
   q("Le dauphin est rangé avec la vache parce qu'il...", ["vit dans l'eau", "nage vite", "a des poumons et allaite ses petits"], 2),
   q("La plupart des fossiles se forment...", ["au fond de l'eau", "dans le ciel", "dans les nuages"], 0),
   q("Le héron cendré qui attrape une grenouille : c'est...", ["de la coopération", "de la prédation", "une décomposition"], 1),
   q("Les nénuphars ont besoin...", ["d'un endroit sec", "de la neige", "d'une eau calme et ensoleillée"], 2),
   q("Au départ de chaque chaîne alimentaire, on trouve...", ["une plante ou une algue", "un héron", "un prédateur"], 0)],
  "CM2": [
   q("Ce qu'un être vivant mange est-il un attribut ?", ["oui, toujours", "non : un attribut est ce qu'il possède", "seulement pour les oiseaux"], 1),
   q("Le nom scientifique du héron cendré s'écrit...", ["en un mot", "en deux mots, le même dans tous les pays", "en chiffres"], 1),
   q("« Les animaux sans pattes » est...", ["un groupe de classification", "une espèce", "un groupe qui n'existe pas en classification"], 2),
   q("Le renard est plus proche parent...", ["du loup", "du hérisson", "de la grenouille"], 0),
   q("Une application d'identification propose un nom. Que faire ?", ["la croire toujours", "vérifier avec une clé de détermination", "changer de nom"], 1),
   q("La Terre s'est formée il y a environ...", ["66 millions d'années", "300 000 ans", "4,6 milliards d'années"], 2),
   q("Les trilobites ont disparu il y a...", ["252 millions d'années", "66 millions d'années", "300 000 ans"], 0),
   q("Après l'extinction de la fin du Crétacé, se sont beaucoup diversifiés...", ["les trilobites", "les mammifères", "les ammonites"], 1),
   q("Les oiseaux descendent...", ["des poissons", "des ammonites", "de petits dinosaures à plumes"], 2),
   q("Après une perturbation, un écosystème peut se rétablir...", ["dans certaines limites", "toujours et tout de suite", "jamais"], 0),
   q("Si l'on pêche trop de perches dans l'étang...", ["les algues disparaissent", "les larves de libellule deviennent trop nombreuses", "le héron a plus de poissons"], 1),
   q("Le frelon asiatique, observé en France depuis 2004, chasse surtout...", ["les hérons", "les perches", "les abeilles"], 2)]
 },
 "questions_fermees": {
  "CM1": [
   vf("Ce qu'un être vivant possède et que l'on peut voir s'appelle un attribut.", "vrai"),
   vf("On peut faire un groupe « les animaux qui n'ont pas d'ailes ».", "faux"),
   vf("Des humains ont vu des dinosaures vivants.", "faux"),
   vf("Une mare est un écosystème.", "vrai"),
   vf("Dans un réseau alimentaire, la flèche va de la proie vers celui qui la mange.", "vrai"),
   court("Cite deux attributs que l'on peut observer sur un animal.", "par exemple : des plumes, des poils, une coquille, des pattes, des ailes"),
   court("Qu'est-ce qu'un fossile ?", "un reste ou une trace d'un être vivant ancien conservé dans une roche"),
   court("Donne un exemple de coopération.", "l'abeille boit le nectar de la fleur et transporte son pollen")],
  "CM2": [
   vf("L'âne et le cheval appartiennent à la même espèce.", "faux"),
   vf("Le lieu de vie sert à classer les êtres vivants.", "faux"),
   vf("Les dinosaures et les ammonites ont disparu il y a environ 66 millions d'années.", "vrai"),
   vf("Un écosystème peut toujours se rétablir, quelle que soit la perturbation.", "faux"),
   court("Pourquoi le mulet montre-t-il que l'âne et le cheval sont deux espèces ?", "parce que le mulet, leur petit, ne peut pas avoir de petits"),
   court("Quelle est la différence entre identifier et classer ?", "identifier, c'est trouver le nom d'une espèce ; classer, c'est montrer ses liens de parenté avec les autres"),
   court("Cite deux caractéristiques physiques d'un milieu de vie.", "par exemple : la température, la lumière, l'humidité, la pluie, l'altitude"),
   court("Donne deux actions humaines qui protègent un écosystème.", "par exemple : creuser une mare, garder les haies, éviter les pesticides, ne jamais relâcher un animal exotique")]
 },
 "etudes_documents": {
  "CM1": [
   {"titre": "Le carnet de Lina", "document": {"contenu": "Inventaire du bord du ruisseau, un matin de mai. Une coccinelle : 6 pattes, 2 élytres rouges à points noirs. Une araignée : 8 pattes. Un cloporte : 14 pattes. Une mésange : des plumes, un bec, 2 pattes. Un escargot : une coquille enroulée.", "source": "Carnet inventé pour le jeu, d'après les leçons 1 et 2."},
    "questions": [court("Combien d'espèces Lina a-t-elle notées ?", "5 espèces"),
                  court("Lequel de ces animaux est un insecte ? Pourquoi ?", "la coccinelle, parce qu'elle a 6 pattes"),
                  court("Cite un attribut de l'escargot.", "une coquille enroulée")]},
   {"titre": "La mare de Rose", "document": {"contenu": "Au printemps, la grenouille pond ses œufs dans l'eau de la mare. Elle chasse les insectes dans la prairie voisine. Le héron cendré vient pêcher les grenouilles. Autour de la mare, les abeilles butinent les fleurs du pré.", "source": "Texte inventé pour le jeu, d'après la leçon 4."},
    "questions": [court("Pourquoi la grenouille a-t-elle besoin de la mare ?", "pour pondre ses œufs dans l'eau"),
                  court("Trouve une relation de prédation dans le texte.", "le héron mange les grenouilles (ou la grenouille mange les insectes)"),
                  court("Que transportent les abeilles d'une fleur à l'autre ?", "le pollen")]}],
  "CM2": [
   {"titre": "Les repères de la carrière", "document": {"contenu": "Formation de la Terre : environ 4,6 milliards d'années. Premières traces de vie : environ 3,8 milliards d'années. Trilobites : il y a 540 millions d'années, disparus il y a 252 millions d'années. Disparition des dinosaures et des ammonites : il y a environ 66 millions d'années. Homo sapiens : environ 300 000 ans.", "source": "Document de la leçon 3 du jeu (académie de Martinique ; Espace des sciences)."},
    "questions": [court("Range du plus ancien au plus récent : dinosaures disparus, trilobites, Homo sapiens.", "trilobites, dinosaures disparus, Homo sapiens"),
                  court("Pendant combien de millions d'années les trilobites ont-ils vécu ?", "540 − 252 = 288 millions d'années"),
                  court("Un humain a-t-il pu voir une ammonite vivante ? Justifie.", "non : les ammonites ont disparu il y a 66 millions d'années, Homo sapiens n'existe que depuis 300 000 ans")]},
   {"titre": "Le carnet d'Élio", "document": {"contenu": "Dans l'étang, les algues sont mangées par les têtards, les têtards par les larves de libellule, les larves par les perches et les perches par le héron. Cette année, des pêcheurs ont pris beaucoup trop de perches.", "source": "Texte inventé pour le jeu, d'après la leçon 5."},
    "questions": [court("Écris la chaîne avec des flèches.", "algues → têtards → larves de libellule → perches → héron"),
                  court("Que va-t-il arriver aux larves de libellule ? Pourquoi ?", "elles vont devenir trop nombreuses, car moins de perches les mangent"),
                  court("Et au héron ?", "il va manquer de poissons")]}]
 }
}

with open(os.path.join(JEU, "assets", "data", "evaluations.json"), "w", encoding="utf-8", newline="\n") as f:
    json.dump(EVAL, f, ensure_ascii=False, indent=1); f.write("\n")
with open(os.path.join(JEU, "assets", "data", "evaluations-embarquees.js"), "w", encoding="utf-8", newline="\n") as f:
    f.write("/* FICHIER GÉNÉRÉ par vivant-ecosystemes/outils/generer-evaluations.py — ne pas modifier à la main. */\n")
    f.write("window.EVAL_EMBARQUEES = "); json.dump(EVAL, f, ensure_ascii=False, separators=(",", ":")); f.write(";\n")
n = {k: {niv: len(v[niv]) for niv in v} for k, v in EVAL.items() if k in ("qcm", "questions_fermees", "etudes_documents")}
print("évaluations écrites :", n)
