# -*- coding: utf-8 -*-
"""Leçons imprimables — L'Expédition biodiversité (vivant et écosystèmes, jeu n°17, version immersive seule).
Compétences : sciences et technologie, cycle 3 (programme 2026, BO n° 24 du 11 juin 2026, annexe 2),
d'après le tableau « Compétences du programme » du README du jeu.
Visuels : schémas du jeu (lecons.json : attributs, groupes emboîtés, temps géologique, mare, réseau de
l'étang), tableaux et frise dessinés par script. Aucun visuel généré par IA. La page est écrite dans
vivant-ecosystemes/ (données sources du jeu)."""
from graphiques import tableau, etapes

JEU = {
    "titre": "L'Expédition biodiversité",
    "matiere": "Sciences et technologie",
    "theme": "Observer le vivant et définir l'espèce, classer en groupes emboîtés et identifier, la biodiversité passée et les fossiles, l'écosystème, le réseau alimentaire",
    "couleur": "#2f5d3a", "accent": "#b5832a",
    "couleur_pale": "#e6efe6", "accent_pale": "#f6ecd9",
}
VERT, OCRE = "#2f5d3a", "#b5832a"

ESPECE = tableau(["Question", "Même espèce ?"], [
    ["un caniche et un berger allemand", "oui : ce sont deux chiens"],
    ["un âne et une jument", "non : leur petit, le mulet, ne peut pas avoir de petits"],
    ["deux hérons cendrés", "oui : leurs petits auront des petits"]],
    couleur=VERT, largeurs=[1.2, 1.5], label="Tableau : même espèce ou non ? chien, âne et cheval, héron cendré")

PATTES = tableau(["Animal", "Nombre de pattes"], [
    ["insecte (coccinelle, abeille)", "6"],
    ["araignée", "8"],
    ["cloporte", "14"],
    ["mille-pattes", "de très nombreuses paires"]],
    couleur=VERT, largeurs=[1.5, 1], label="Tableau : compter les pattes pour identifier une petite bête")

TEMPS = etapes([("4,6 milliards d'années", "formation de la Terre"),
                ("3,8 milliards d'années", "premières traces de vie"),
                ("540 millions d'années", "les trilobites dans la mer"),
                ("66 millions d'années", "extinction des dinosaures et des ammonites"),
                ("300 000 ans", "apparition d'Homo sapiens en Afrique")],
               sens="v", couleur=OCRE, label="Frise du temps géologique : de la formation de la Terre à Homo sapiens")

RELATIONS = tableau(["Relation", "Exemple dans la réserve"], [
    ["prédation", "le héron cendré attrape les grenouilles et les poissons"],
    ["coopération", "l'abeille boit le nectar et transporte le pollen"],
    ["besoin du milieu", "la grenouille pond dans l'eau de la mare"]],
    couleur=VERT, largeurs=[1, 2], label="Tableau des relations dans l'écosystème : prédation, coopération, besoin du milieu")

PROTEGER = tableau(["Ce qui perturbe", "Ce qui protège"], [
    ["la surpêche", "creuser une mare"],
    ["une espèce exotique envahissante", "laisser des haies"],
    ["les pesticides", "ne jamais relâcher un animal exotique"]],
    couleur=VERT, largeurs=[1, 1], label="Tableau : ce qui perturbe un réseau alimentaire et ce qui protège les écosystèmes")

LECONS = {
    "espece": {
        "competence": "Décrire un être vivant par ses attributs ; définir l'espèce comme un ensemble d'êtres vivants qui se ressemblent et peuvent se reproduire entre eux ; faire l'inventaire d'un lieu (prolongement 6e : la cellule, unité du vivant).",
        "visuels": [
            {"type": "schema", "titre": "Observer les attributs"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Même espèce ou non ?", "svg": ESPECE,
             "legende": "Chaque espèce a un nom scientifique en deux mots : le héron cendré s'appelle Ardea cinerea."},
        ],
    },
    "classer": {
        "competence": "Réaliser une classification en groupes emboîtés à partir des attributs ; en déduire des liens de parenté ; identifier des espèces proches avec une clé de détermination.",
        "visuels": [
            {"type": "schema", "titre": "Des groupes emboîtés"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Compter les pattes", "svg": PATTES,
             "legende": "On classe avec ce que l'être vivant possède, jamais avec ce qu'il ne possède pas, ni avec son lieu de vie."},
        ],
    },
    "fossiles": {
        "competence": "Distinguer les échelles du temps géologique et de l'histoire humaine ; caractériser l'évolution de la biodiversité grâce aux fossiles ; l'extinction massive de la fin du Crétacé (CM2).",
        "visuels": [
            {"type": "schema", "titre": "Quelques repères du temps géologique"},
            {"type": "svg", "etiquette": "Frise", "titre": "Une très longue histoire", "svg": TEMPS,
             "legende": "Aucun humain n'a jamais vu de dinosaure vivant. Sources : académie de Martinique ; Espace des sciences."},
        ],
    },
    "ecosysteme": {
        "competence": "Définir un écosystème : un milieu de vie, les êtres vivants qui l'habitent et leurs relations ; relier la présence d'êtres vivants aux caractéristiques du milieu ; prédation et coopération.",
        "visuels": [
            {"type": "schema", "titre": "La mare : un milieu de vie et des êtres vivants"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Des relations entre êtres vivants", "svg": RELATIONS,
             "legende": "Une mare, une forêt, une prairie ou une vigne sont des écosystèmes."},
        ],
    },
    "reseau": {
        "competence": "Représenter les liens alimentaires par un réseau (flèche de la proie vers celui qui la mange) ; expliquer l'effet d'une forte variation d'une espèce ; conséquences d'actions humaines.",
        "visuels": [
            {"type": "schema", "titre": "Le réseau alimentaire de l'étang"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Perturber ou protéger", "svg": PROTEGER,
             "legende": "Au départ de chaque chaîne, une plante ou une algue fabrique sa matière grâce à la lumière."},
        ],
    },
}
