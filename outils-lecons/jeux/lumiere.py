# -*- coding: utf-8 -*-
"""Leçons imprimables — Le Phare de l'île Lumière (lumiere).
Visuels : schémas dessinés de lecons.json (trajet de la lumière, matériaux, ombres, trajet du Soleil, phases de la Lune),
tableau du code Morse, tableau d'essais des matériaux, tableau des tailles d'ombres, courbe du relevé d'Achille (fictif),
cycle des phases. Aucun visuel généré par IA."""
from graphiques import courbes, tableau, etapes

JEU = {
    "titre": "Le Phare de l'île Lumière",
    "matiere": "Sciences et technologie",
    "theme": "La lumière : sources, matériaux, ombres, Soleil et Lune, signaux lumineux",
    "couleur": "#1d3557", "accent": "#b03a2e",
    "couleur_pale": "#e8eef6", "accent_pale": "#f8e9e6",
}
NUIT, PHARE, LAMPE = "#1d3557", "#b03a2e", "#c99a00"

MORSE = tableau(["Lettre", "Code", "Lettre", "Code"], [
    ["A", "• —", "N", "— •"], ["E", "•", "O", "— — —"], ["I", "• •", "P", "• — — •"],
    ["L", "• — • •", "S", "• • •"], ["M", "— —", "U", "• • —"]],
    couleur=NUIT, label="Tableau : quelques lettres du code Morse (éclat court •, éclat long —)")

ESSAIS = tableau(["Matériau", "La lumière\npasse ?", "On voit\nnettement ?", "Il est…"], [
    ["vitre", "oui", "oui", "transparent"], ["papier calque", "oui", "non", "translucide"],
    ["verre dépoli", "oui", "non", "translucide"], ["carton", "non", "non", "opaque"],
    ["aluminium", "non", "non", "opaque"]],
    couleur=NUIT, largeurs=[1.4, 1, 1, 1.4], label="Tableau d'essais : la lumière passe-t-elle, voit-on nettement à travers, et le classement de chaque matériau")

TAILLES = tableau(["Lampe-écran", "Lampe-figurine", "Ombre portée"], [
    ["1 m", "80 cm", "un peu plus grande"], ["1 m", "50 cm", "2 fois plus grande"],
    ["1 m", "25 cm", "4 fois plus grande"]],
    couleur=NUIT, largeurs=[1, 1.2, 1.6], label="Tableau : plus la figurine est proche de la lampe, plus son ombre portée est grande")

ACHILLE = courbes(["10 h", "12 h", "14 h", "16 h", "18 h"], [("Longueur de l'ombre (cm)", [118, 62, 47, 76, 151], PHARE)],
                  titre_y="heure →  longueur", unite="cm", vmin=0, vmax=160, graduation=40,
                  label="Courbe : longueur de l'ombre d'un bâton de 1 m, fin juin : 118 cm à 10 h, 62 cm à 12 h, 47 cm à 14 h, 76 cm à 16 h, 151 cm à 18 h (relevé fictif)")

CYCLE = etapes([("Nouvelle lune", "presque invisible"), ("Premier quartier", "moitié droite éclairée"),
                ("Pleine lune", "tout le disque, environ 15 jours après"), ("Dernier quartier", "moitié gauche éclairée")],
               sens="cycle", couleur=NUIT, label="Cycle des phases de la Lune : nouvelle lune, premier quartier, pleine lune, dernier quartier, puis de nouveau la nouvelle lune")

LECONS = {
    "sources": {
        "competence": "Signaux — la lumière : identifier une source lumineuse et des objets éclairés ; la lumière se propage en ligne droite jusqu'à l'œil ; la lumière porte un signal.",
        "visuels": [
            {"type": "schema", "titre": "Le trajet de la lumière"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Quelques lettres du code Morse", "svg": MORSE,
             "legende": "SOS : • • •  — — —  • • • (Vikidia, « Alphabet morse »). Sécurité : ne jamais regarder le Soleil ; pas de laser vers les yeux."},
        ],
    },
    "matieres": {
        "competence": "Observer et classer des matériaux selon qu'ils sont transparents, opaques à la lumière ou translucides ; justifier un tri.",
        "visuels": [
            {"type": "schema", "titre": "Trois matériaux devant une lampe"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Le carnet d'essais de Salomé", "svg": ESSAIS,
             "legende": "Deux questions suffisent pour classer : la lumière passe-t-elle ? Voit-on nettement à travers ?"},
        ],
    },
    "ombres": {
        "competence": "Produire expérimentalement une ombre à l'aide d'un objet opaque et distinguer ombre propre et ombre portée ; associer les positions et les tailles des ombres à celles de la source et de l'objet.",
        "visuels": [
            {"type": "schema", "titre": "Ombre propre et ombre portée"},
            {"type": "svg", "etiquette": "Tableau", "titre": "La taille de l'ombre (écran fixe)", "svg": TAILLES,
             "legende": "On ne change qu'une distance à la fois. À mi-distance entre la lampe et l'écran, l'ombre est deux fois plus grande (La main à la pâte)."},
        ],
    },
    "soleil": {
        "competence": "Observer la position de l'ombre d'un bâton sur le sol au cours d'une journée ensoleillée et l'associer au déplacement du Soleil dans le ciel du point de vue de la cour de récréation.",
        "visuels": [
            {"type": "schema", "titre": "Le trajet apparent du Soleil"},
            {"type": "svg", "etiquette": "Graphique", "titre": "Le carnet d'Achille", "svg": ACHILLE,
             "legende": "Relevé fictif (bâton de 1 m, fin juin). L'ombre la plus courte, à 14 h, marque le midi solaire. Ne jamais regarder le Soleil."},
        ],
    },
    "lune": {
        "competence": "Observer, schématiser et nommer les phases de la Lune ; constater l'existence d'un cycle.",
        "visuels": [
            {"type": "schema", "titre": "Les phases de la Lune vues depuis la France"},
            {"type": "svg", "etiquette": "Schéma", "titre": "Un cycle : la lunaison", "svg": CYCLE,
             "legende": "Une lunaison dure environ 29 jours et demi (Vikidia, « Phases de la Lune »)."},
        ],
    },
}
