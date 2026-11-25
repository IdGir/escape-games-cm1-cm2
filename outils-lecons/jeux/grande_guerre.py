# -*- coding: utf-8 -*-
"""Leçons imprimables — Les Lettres du poilu (Première Guerre mondiale, jeu n°19, version immersive seule).
JEU SENSIBLE : relecture obligatoire avant la classe.
Compétences : histoire, cycle 3, Première Guerre mondiale (programme 2026, BO n° 22 du 28 mai 2026),
d'après le tableau « Compétences du programme » du README du jeu.
Visuels : schémas du jeu (lecons.json : alliances, coupe d'une tranchée, front et arrière, frise 1914-1922,
monument aux morts), tableaux et frise dessinés par script. Aucun visuel généré par IA, aucune image de
combat ni de blessé. La page est écrite dans grande-guerre/ (données sources du jeu)."""
from graphiques import tableau, etapes

JEU = {
    "titre": "Les Lettres du poilu",
    "matiere": "Histoire",
    "theme": "La Première Guerre mondiale : l'entrée en guerre, le front et les tranchées, l'arrière, l'armistice et la paix, la mémoire et une paix fragile",
    "couleur": "#3d4f6b", "accent": "#9e3a32",
    "couleur_pale": "#e7ebf1", "accent_pale": "#f4e4e2",
}
BLEU, ROUGE = "#3d4f6b", "#9e3a32"

ETE_1914 = etapes([("28 juin 1914", "attentat de Sarajevo"),
                   ("28 juillet 1914", "l'Autriche-Hongrie déclare la guerre à la Serbie"),
                   ("1er août 1914", "affiche de la mobilisation générale"),
                   ("3 août 1914", "l'Allemagne déclare la guerre à la France")],
                  sens="v", couleur=ROUGE, label="Frise de l'été 1914 : de Sarajevo à la déclaration de guerre")

BATAILLES = tableau(["Bataille", "Dates (1916)", "Qui attaque ?"], [
    ["Verdun", "21 février – 18 décembre", "l'armée allemande ; l'armée française résiste"],
    ["la Somme", "1er juillet – 18 novembre", "les Britanniques et les Français ensemble"]],
    couleur=BLEU, largeurs=[0.8, 1.2, 1.6], label="Tableau : les batailles de Verdun et de la Somme en 1916")

FEMMES = tableau(["Où ?", "Ce que font les femmes"], [
    ["à la campagne", "les moissons et les vendanges"],
    ["à l'usine", "fabriquer des obus : les « munitionnettes »"],
    ["en ville", "conduire les tramways, distribuer le courrier"],
    ["à l'hôpital", "soigner les blessés (infirmières)"]],
    couleur=BLEU, largeurs=[0.8, 1.6], label="Tableau : le travail des femmes à l'arrière pendant la guerre")

CHIFFRES = tableau(["Repère", "Chiffre officiel"], [
    ["Français mobilisés (1914-1918)", "8,7 millions"],
    ["soldats français morts", "près de 1,4 million"],
    ["veuves de guerre en France", "près de 600 000"]],
    couleur=BLEU, largeurs=[1.5, 1], label="Tableau des repères chiffrés de la guerre pour la France (chiffres officiels)")

APRES = etapes([("1920", "le Soldat inconnu à l'Arc de Triomphe"),
                ("1922", "le 11 novembre devient jour férié ; Mussolini au pouvoir en Italie"),
                ("1929", "début d'une grave crise économique"),
                ("1939", "une nouvelle guerre mondiale commence")],
               sens="v", couleur=ROUGE, label="Frise : de la mémoire de la guerre à une paix fragile, 1920-1939")

LECONS = {
    "causes": {
        "competence": "Comprendre les causes de la Première Guerre mondiale (rivalités entre puissances, alliances) ; situer l'attentat de Sarajevo et la mobilisation générale (1914) ; distinguer légende et réalité.",
        "visuels": [
            {"type": "schema", "titre": "Deux alliances face à face en 1914"},
            {"type": "svg", "etiquette": "Frise", "titre": "L'été 1914", "svg": ETE_1914,
             "legende": "En quelques semaines, une crise locale devient une guerre européenne, puis mondiale."},
        ],
    },
    "front": {
        "competence": "Décrire le déroulement de la guerre : le front, les tranchées et la vie des poilus ; batailles emblématiques (Verdun, la Somme, 1916) ; armes nouvelles ; soldats venus des colonies.",
        "visuels": [
            {"type": "schema", "titre": "Coupe d'une tranchée"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Deux grandes batailles de 1916", "svg": BATAILLES,
             "legende": "Source : ministère des Armées, Chemins de mémoire."},
        ],
    },
    "arriere": {
        "competence": "Décrire une guerre totale : l'arrière, le rôle des femmes dans les usines et les champs, les enfants, l'économie de guerre, les travailleurs venus des colonies.",
        "visuels": [
            {"type": "schema", "titre": "Le front et l'arrière"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Les femmes remplacent les hommes partis", "svg": FEMMES,
             "legende": "Les Françaises obtiendront le droit de vote en 1944."},
        ],
    },
    "armistice": {
        "competence": "Connaître la fin de la guerre et ses conséquences : armistice du 11 novembre 1918, traité de Versailles (1919), bilan humain (chiffres officiels).",
        "visuels": [
            {"type": "schema", "titre": "Frise de 1914 à 1922"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Un bilan très lourd", "svg": CHIFFRES,
             "legende": "Sources : ministère des Armées, Chemins de mémoire ; musée de l'Armée."},
        ],
    },
    "memoire": {
        "competence": "Comprendre la mémoire de la guerre (monuments aux morts, 11 novembre) et ses conséquences : colère, crise et montée des extrêmes (Italie, 1922), qui ouvre la voie aux régimes autoritaires.",
        "visuels": [
            {"type": "schema", "titre": "Le monument aux morts"},
            {"type": "svg", "etiquette": "Frise", "titre": "Se souvenir, et une paix fragile", "svg": APRES,
             "legende": "Depuis 2012, le 11 novembre rend hommage à tous les morts pour la France."},
        ],
    },
}
