# -*- coding: utf-8 -*-
"""Leçons imprimables — Le Grand Prix de l'observatoire (mouvement).
Visuels : schémas dessinés de lecons.json (ruban gradué, deux instants, même distance, trois trajectoires, deux observateurs),
tableau des instruments, étapes du chronométrage, barres des vitesses (ordres de grandeur), tableau des trajectoires,
tableau « immobile ou en mouvement ». Aucun visuel généré par IA."""
from graphiques import barres, tableau, etapes

JEU = {
    "titre": "Le Grand Prix de l'observatoire",
    "matiere": "Sciences et technologie",
    "theme": "Mesurer une distance et une durée, comparer des déplacements, trajectoires, la Terre autour du Soleil, le rôle de l'observateur",
    "couleur": "#23406e", "accent": "#b3361f",
    "couleur_pale": "#e6ecf6", "accent_pale": "#f7e8e4",
}
NUIT, COURSE = "#23406e", "#b3361f"

INSTRUMENTS = tableau(["Longueur à mesurer", "Instrument"], [
    ["quelques centimètres", "règle graduée"], ["quelques mètres", "mètre ruban"],
    ["quelques dizaines de mètres", "décamètre"], ["plusieurs centaines de mètres", "roue de mesure"]],
    couleur=NUIT, largeurs=[1.8, 1.4], label="Tableau : choisir l'instrument selon la longueur à mesurer")

CHRONO = etapes([("Zéro", "remettre le chronomètre à zéro"), ("Départ", "le déclencher au signal"),
                 ("Arrivée", "l'arrêter quand l'objet franchit la ligne"), ("Noter", "écrire la durée avec son unité")],
                sens="v", couleur=NUIT, label="Étapes du chronométrage : zéro, départ, arrivée, noter la durée")

VITESSES = barres([("piéton", 4), ("cycliste en ville", 15), ("voiture en ville (maximum)", 50), ("guépard (pointe)", 110)],
                  unite="km/h", titre_y="km/h", couleur=COURSE,
                  label="Barres : ordres de grandeur des vitesses, environ 4 km/h pour un piéton, 15 km/h pour un cycliste en ville, 50 km/h au plus pour une voiture en ville, plus de 100 km/h pour un guépard en pointe")

TRAJ = tableau(["Trajectoire", "Exemples"], [
    ["rectiligne (droite)", "bille lâchée, ascenseur"], ["circulaire (cercle)", "grande roue, manège"],
    ["curviligne (courbe)", "ballon lancé, virage en S"]],
    couleur=NUIT, largeurs=[1.4, 2], label="Tableau des trajectoires avec des exemples")

OBS = tableau(["Le voyageur assis…", "pour son voisin", "pour la personne sur le quai"], [
    ["est-il en mouvement ?", "non : immobile", "oui"]],
    couleur=NUIT, largeurs=[1.6, 1.3, 1.6], label="Tableau : le même voyageur est immobile pour son voisin et en mouvement pour la personne sur le quai")

LECONS = {
    "distance": {
        "competence": "Mesurer une distance lors du déplacement d'un objet (CM1) ; effectuer des conversions d'unités de distance (CM2).",
        "visuels": [
            {"type": "schema", "titre": "Lire une distance sur un ruban gradué"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Le bon instrument", "svg": INSTRUMENTS,
             "legende": "1 km = 1 000 m ; 1 dam = 10 m ; 1 m = 100 cm ; 1 cm = 10 mm. Toujours écrire l'unité."},
        ],
    },
    "duree": {
        "competence": "Mesurer une durée, comme intervalle entre deux instants, lors du déplacement d'un objet (CM1) ; effectuer des conversions d'unités de temps (CM2).",
        "visuels": [
            {"type": "schema", "titre": "Une durée entre deux instants"},
            {"type": "svg", "etiquette": "Schéma", "titre": "Chronométrer une descente", "svg": CHRONO,
             "legende": "1 h = 60 min ; 1 min = 60 s. Refaire la mesure pour vérifier."},
        ],
    },
    "comparer": {
        "competence": "Comparer des déplacements : même distance, durées différentes ; même durée, distances différentes (prolongement de la sixième, sans formule).",
        "visuels": [
            {"type": "schema", "titre": "Même distance, durées différentes"},
            {"type": "svg", "etiquette": "Graphique", "titre": "Quelques vitesses de la vie réelle", "svg": VITESSES,
             "legende": "Ordres de grandeur : FFRandonnée (piéton), Club des villes et territoires cyclables (cycliste), Code de la route (50 km/h en ville), Vikidia (guépard)."},
        ],
    },
    "trajectoires": {
        "competence": "Observer et identifier le mouvement rectiligne ou circulaire d'un objet, en fonction de l'observateur ; décrire le mouvement de la Terre par rapport au Soleil (CM2).",
        "visuels": [
            {"type": "schema", "titre": "Trois formes de trajectoire"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Les notes de Léonie", "svg": TRAJ,
             "legende": "La Terre, troisième planète à partir du Soleil, en fait le tour en environ un an (Vikidia, « Terre »)."},
        ],
    },
    "observateur": {
        "competence": "Savoir que le mouvement d'un objet est toujours décrit par rapport à un observateur (CM2).",
        "visuels": [
            {"type": "schema", "titre": "Le même voyageur, vu par deux observateurs"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Immobile ou en mouvement ?", "svg": OBS,
             "legende": "Un objet lâché tombe en ligne droite verticale pour la personne qui le lâche."},
        ],
    },
}
