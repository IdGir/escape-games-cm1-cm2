# -*- coding: utf-8 -*-
"""Leçons imprimables — La Fabrique des états (etats-matiere).
Visuels : schémas dessinés de lecons.json (trois états, ballon pesé, changements d'état, glaçons pesés, cycle de l'eau),
tableau des critères des états, tableau « ce qui change / ce qui reste », courbe du relevé de Paolo (fictif), étapes du
protocole de pesée de l'air, tableau des propriétés. Aucun visuel généré par IA."""
from graphiques import courbes, tableau, etapes

JEU = {
    "titre": "La Fabrique des états",
    "matiere": "Sciences et technologie",
    "theme": "Les états de la matière, l'air, les changements d'état de l'eau, la masse et le volume, le cycle de l'eau",
    "couleur": "#1f4e5f", "accent": "#a8432a",
    "couleur_pale": "#e6f0f3", "accent_pale": "#f7ebe6",
}
ACIER, BRIQUE = "#1f4e5f", "#a8432a"

CRITERES = tableau(["État", "Forme\npropre ?", "Volume\npropre ?", "Se comprime ?"], [
    ["solide", "oui", "oui", "non"], ["liquide", "non", "oui", "presque pas"], ["gaz", "non", "non", "oui"]],
    couleur=ACIER, largeurs=[1.2, 1, 1, 1.2], label="Tableau des critères : le solide a une forme et un volume propres ; le liquide a un volume propre ; le gaz n'a ni l'un ni l'autre et se comprime")

PROTOCOLE = etapes([("Peser", "le ballon peu gonflé"), ("Pomper", "de l'air, sans rien changer d'autre"),
                    ("Repeser", "le même ballon"), ("Conclure", "la masse a augmenté : l'air a une masse")],
                   sens="v", couleur=ACIER, label="Protocole en quatre étapes : peser le ballon, pomper de l'air, repeser, conclure que l'air a une masse")

PAOLO = courbes(["0", "2", "4", "6", "8", "10", "12", "14", "16", "18", "20"], [("Température (°C)", [-15, -6, 0, 0, 0, 25, 45, 70, 90, 100, 100], BRIQUE)],
                titre_y="minutes →  température", unite="°C", vmin=-20, vmax=110, graduation=20,
                label="Courbe : température de glaçons chauffés, relevée toutes les 2 minutes : moins 15, moins 6, puis 0 degré pendant la fusion, puis 25, 45, 70, 90 et 100 degrés pendant l'ébullition (relevé fictif)")

CHANGE = tableau(["Pendant que l'eau gèle…", "Change ?"], [
    ["l'état (liquide puis solide)", "oui"], ["la forme (elle devient fixe)", "oui"], ["le volume (environ 9 % de plus)", "oui"],
    ["la masse", "non : elle se conserve"], ["la matière (c'est toujours de l'eau)", "non"]],
    couleur=ACIER, largeurs=[2.2, 1.4], label="Tableau : quand l'eau gèle, l'état, la forme et le volume changent ; la masse et la matière restent les mêmes")

PROPRIETES = tableau(["Propriété", "Exemples"], [
    ["flotte sur l'eau", "bois, liège, glace"], ["coule", "fer, verre, caillou"],
    ["conduit bien la chaleur", "métaux"], ["conduit mal la chaleur", "bois, plastique, laine, air"],
    ["se dissout dans l'eau", "sucre, sel"], ["ne se dissout pas", "sable, huile"]],
    couleur=ACIER, largeurs=[1.6, 2], label="Tableau des propriétés de la matière avec des exemples")

LECONS = {
    "etats": {
        "competence": "Identifier les états physiques de la matière (solide, liquide, gaz) à partir de critères observables : forme, volume, écoulement, compressibilité.",
        "visuels": [
            {"type": "schema", "titre": "Les trois états de la matière"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Les critères de l'ingénieure", "svg": CRITERES,
             "legende": "Un solide en poudre (sable, farine, sucre) reste un solide : chaque grain garde sa forme."},
        ],
    },
    "air": {
        "competence": "Mettre en évidence que l'air est de la matière : il occupe un volume, il se comprime, il a une masse.",
        "visuels": [
            {"type": "schema", "titre": "L'air pompé dans un ballon a une masse"},
            {"type": "svg", "etiquette": "Schéma", "titre": "Le protocole de Bastien", "svg": PROTOCOLE,
             "legende": "Un litre d'air a une masse d'environ 1,2 g (académie de Grenoble, fiche « L'air »)."},
        ],
    },
    "changements": {
        "competence": "Observer des changements d'état physique et leur réversibilité : fusion, solidification, vaporisation, liquéfaction ; 0 °C et 100 °C pour l'eau.",
        "visuels": [
            {"type": "schema", "titre": "Les changements d'état"},
            {"type": "svg", "etiquette": "Graphique", "titre": "Le relevé de Paolo", "svg": PAOLO,
             "legende": "Relevé fictif. Pendant la fusion, la température reste à 0 °C ; pendant l'ébullition, à 100 °C. L'eau qui bout brûle : expérience avec un adulte."},
        ],
    },
    "conservation": {
        "competence": "Comparer avant et après un changement d'état : la masse se conserve, le volume peut changer.",
        "visuels": [
            {"type": "schema", "titre": "La masse se conserve pendant la fusion"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Ce qui change, ce qui reste", "svg": CHANGE,
             "legende": "1 000 mL d'eau donnent environ 1 090 mL de glace (Vikidia, « Glace ») : jamais de bouteille en verre pleine au congélateur."},
        ],
    },
    "proprietes": {
        "competence": "Utiliser les propriétés physiques des matériaux pour les classer ; identifier les états de l'eau dans la nature : le cycle de l'eau.",
        "visuels": [
            {"type": "schema", "titre": "Le cycle de l'eau"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Les fiches de Ninon", "svg": PROPRIETES,
             "legende": "Un nuage est fait de gouttelettes d'eau liquide ou de cristaux de glace : la vapeur d'eau est invisible (IRM)."},
        ],
    },
}
