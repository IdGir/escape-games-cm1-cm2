# -*- coding: utf-8 -*-
"""Leçons imprimables — Radio Londres (Seconde Guerre mondiale, jeu n°20, version immersive seule).
JEU TRÈS SENSIBLE : relecture obligatoire avant la classe.
Compétences : histoire, cycle 3, Seconde Guerre mondiale (programme 2026, BO n° 22 du 28 mai 2026),
d'après le tableau « Compétences du programme » du README du jeu.
Visuels : schémas du jeu (lecons.json : frise 1919-1945, carte simplifiée de la France coupée en deux,
organisation de la Résistance, carte simplifiée de la Libération), tableaux et frises dessinés par script.
Aucun visuel généré par IA ; aucune image de guerre, de persécution ni de camp. La leçon 3 parle de la
Shoah sobrement, par le texte seul. Tous les faits viennent des leçons du jeu.
La page est écrite dans seconde-guerre/ (données sources du jeu)."""
from graphiques import tableau, etapes

JEU = {
    "titre": "Radio Londres",
    "matiere": "Histoire",
    "theme": "La Seconde Guerre mondiale : la montée des dictatures, la défaite de 1940 et Vichy, la vie sous l'Occupation, la Résistance, la Libération et la victoire",
    "couleur": "#2f3b45", "accent": "#8a2f2a",
    "couleur_pale": "#e6e9ec", "accent_pale": "#f3e3e1",
}
GRIS, ROUGE = "#2f3b45", "#8a2f2a"

DICTATURES = tableau(["Pays", "Chef", "Dictature"], [
    ["Italie", "Mussolini\n(au pouvoir en 1922)", "fasciste"],
    ["Allemagne", "Hitler\n(30 janvier 1933)", "nazie, raciste\net antisémite"],
    ["URSS", "Staline", "communiste"]],
    couleur=GRIS, largeurs=[0.9, 1.4, 1.4], label="Tableau : trois dictatures en Europe avant 1939")

JUIN_1940 = etapes([("1er-3 septembre 1939", "invasion de la Pologne ; début de la guerre"),
                    ("10 mai 1940", "attaque allemande à l'ouest ; l'exode"),
                    ("18 juin 1940", "appel du général de Gaulle depuis Londres"),
                    ("22 juin 1940", "armistice : la France coupée en deux"),
                    ("10 juillet 1940", "pleins pouvoirs à Pétain : Vichy")],
                   sens="v", couleur=ROUGE, label="Frise : de l'entrée en guerre au régime de Vichy, 1939-1940")

MANQUE = tableau(["Ce qui manque", "Comment on fait"], [
    ["pain, viande, sucre", "tickets, longues queues"],
    ["le café", "ersatz : orge grillée"],
    ["le cuir des chaussures", "semelles de bois"],
    ["ce qu'on ne trouve plus", "marché noir (caché, cher)"]],
    couleur=GRIS, largeurs=[1.1, 1.4], label="Tableau : vivre avec le manque sous l'Occupation")

FORMES = tableau(["Forme", "Ce que font les résistants"], [
    ["journaux clandestins", "dire la vérité en cachette"],
    ["réseaux", "informer les Alliés"],
    ["Radio Londres", "messages personnels codés"],
    ["agents de liaison", "porter messages et tracts"],
    ["maquis", "se cacher en forêt (Morvan)"]],
    couleur=GRIS, largeurs=[1.1, 1.5], label="Tableau : les formes de la Résistance")

LIBERATION = etapes([("6 juin 1944", "débarquement de Normandie, le Jour J"),
                     ("15 août 1944", "débarquement de Provence"),
                     ("25 août 1944", "libération de Paris"),
                     ("11 septembre 1944", "libération de Dijon"),
                     ("8 mai 1945", "capitulation de l'Allemagne nazie")],
                    sens="v", couleur=ROUGE, label="Frise : la Libération et la victoire, 1944-1945")

LECONS = {
    "montee": {
        "competence": "Comprendre la montée des extrêmes après la Première Guerre mondiale : la crise de 1929, les régimes totalitaires (fascisme en Italie, nazisme en Allemagne, communisme soviétique), la démocratie menacée.",
        "visuels": [
            {"type": "schema", "titre": "Frise de 1919 à 1945"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Trois dictatures en Europe", "svg": DICTATURES,
             "legende": "Dans une dictature : un parti unique, pas d'élections libres, aucune liberté."},
        ],
    },
    "defaite": {
        "competence": "Connaître le début de la Seconde Guerre mondiale et la défaite de 1940 : l'exode, l'armistice, l'appel du 18 juin 1940, le régime de Vichy et la collaboration.",
        "visuels": [
            {"type": "schema", "titre": "La France coupée en deux (1940)"},
            {"type": "svg", "etiquette": "Frise", "titre": "De la guerre à Vichy", "svg": JUIN_1940,
             "legende": "En octobre 1940, à Montoire, Pétain choisit la collaboration avec l'Allemagne nazie."},
        ],
    },
    "occupation": {
        "competence": "Décrire la vie quotidienne sous l'Occupation (rationnement, STO) ; connaître les persécutions et la Shoah, génocide des Juifs d'Europe, et l'action des Justes.",
        "visuels": [
            {"type": "svg", "etiquette": "Tableau", "titre": "Vivre avec le manque", "svg": MANQUE,
             "legende": "Chaque Français reçoit une carte et des tickets selon son âge."},
        ],
    },
    "resistance": {
        "competence": "Connaître la Résistance : refus de la défaite, France libre, Radio Londres, journaux, réseaux et maquis, Jean Moulin et le Conseil national de la Résistance.",
        "visuels": [
            {"type": "schema", "titre": "Comment la Résistance s'organise"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Les armes de l'ombre", "svg": FORMES,
             "legende": "Les résistants risquent l'arrestation, la déportation ou la mort."},
        ],
    },
    "liberation": {
        "competence": "Connaître la victoire des Alliés et la Libération : débarquements de 1944, libération de Paris, capitulation de l'Allemagne le 8 mai 1945, retour de la République et vote des femmes.",
        "visuels": [
            {"type": "schema", "titre": "La Libération de la France (1944)"},
            {"type": "svg", "etiquette": "Frise", "titre": "1944-1945", "svg": LIBERATION,
             "legende": "La guerre se termine dans le monde le 2 septembre 1945. L'ONU est créée en 1945."},
        ],
    },
}
