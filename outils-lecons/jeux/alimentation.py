# -*- coding: utf-8 -*-
"""Leçons imprimables — Le Grand Repas du chef (alimentation).
Visuels : courbe de Caramel, toise de Lou, barres des besoins, mâchoire et tube digestif (schémas dessinés
de lecons.json, jamais générés par IA), schéma du sang, pouls de Lou."""
from graphiques import barres, courbes, ouvrir, texte, taille

JEU = {
    "titre": "Le Grand Repas du chef",
    "matiere": "Sciences et technologie",
    "theme": "L'alimentation humaine : besoins alimentaires et nutrition humaine",
    "couleur": "#2b5d6b", "accent": "#a8432a",
    "couleur_pale": "#e6f0f2", "accent_pale": "#f8ebe6",
}

CANARD, TOMATE, SAFRAN, VERT, BLEU = "#2b5d6b", "#a8432a", "#c0661c", "#4f7a3a", "#2f6690"

CARAMEL = courbes(["0", "1", "2", "3", "4"], [("Masse de Caramel (g)", [40, 95, 180, 300, 450], SAFRAN)],
                  titre_y="semaines →  masse", unite="g", vmin=0, vmax=500, graduation=100,
                  label="Courbe : la masse du poussin Caramel passe de 40 g à la naissance à 450 g à 4 semaines (relevé fictif)")


def toise():
    """La toise de Lou : une marque par anniversaire, de 6 à 10 ans (relevé fictif)."""
    W, H = 360, 230
    fs = taille(W, 66)
    tailles = [(6, 115), (7, 121), (8, 126), (9, 132), (10, 137)]
    Y = lambda t: 210 - (t - 105) * 5.2
    s = [ouvrir(W, H, "Toise : Lou mesure 115 cm à 6 ans et 137 cm à 10 ans, soit 22 cm de plus en 4 ans (relevé fictif)")]
    s.append(f'<rect x="120" y="{Y(141):.1f}" width="46" height="{Y(105) - Y(141):.1f}" fill="#e9d7b5" stroke="#8a6d3b"/>')
    for t in range(105, 142):
        lg = 14 if t % 10 == 0 else 9 if t % 5 == 0 else 5
        s.append(f'<line x1="120" y1="{Y(t):.1f}" x2="{120 + lg}" y2="{Y(t):.1f}" stroke="#8a6d3b" stroke-width="{1.2 if t % 5 == 0 else .6}"/>')
        if t % 10 == 0:
            s.append(texte(114, Y(t) + fs * .33, f"{t} cm", fs * .85, "end", "#5b6470"))
    for age, t in tailles:
        s.append(f'<line x1="150" y1="{Y(t):.1f}" x2="196" y2="{Y(t):.1f}" stroke="{BLEU}" stroke-width="2.4"/>')
        s.append(texte(202, Y(t) + fs * .33, f"{age} ans : {t} cm", fs * .9, "start", BLEU, 700))
    s.append(texte(W / 2, 226, "+ 22 cm en 4 ans : 5 à 6 cm par an", fs * .9, fill=TOMATE, poids=700))
    s.append("</svg>")
    return "".join(s)


BESOINS = barres([("Enfant\n10 ans", 2000, BLEU), ("Adulte", 2400, VERT), ("Basile\nau repos", 2800, CANARD),
                  ("Basile\nen course", 6000, TOMATE)], unite="kcal par jour", vmax=7000, graduation=1000,
                 label="Diagramme en barres : besoins en énergie par jour, en ordres de grandeur : enfant de 10 ans environ 2 000 kcal, adulte environ 2 400, Basile au repos environ 2 800, Basile un jour d'étape de montagne environ 6 000")

POULS = barres([("Lou au repos", 88, BLEU), ("Lou après\nl'escalier", 160, TOMATE)], unite="battements par minute",
               vmax=200, graduation=40,
               label="Diagramme en barres : pouls de Lou, 88 battements par minute au repos, 160 après avoir monté l'escalier en courant (relevés fictifs)")

LECONS = {
    "croissance": {
        "masquer": ["schema"],
        "competence": "Exploiter des données mettant en évidence le besoin de matière pour la croissance et le développement des êtres vivants.",
        "visuels": [
            {"type": "svg", "etiquette": "Graphique", "titre": "La courbe de Caramel", "svg": CARAMEL,
             "legende": "Relevé fictif. En 4 semaines, Caramel a mangé 700 g de nourriture et grossi de 410 g."},
            {"type": "svg", "etiquette": "Schéma", "titre": "La toise de Lou", "svg": toise(),
             "legende": "Relevé fictif, pour s'exercer : on ne mesure pas les élèves en classe."},
        ],
    },
    "besoins": {
        "masquer": ["schema"],
        "competence": "Exploiter des données pour expliquer la variation des besoins alimentaires au cours de la croissance et selon l'activité physique.",
        "visuels": [
            {"type": "svg", "etiquette": "Graphique", "titre": "Des besoins qui changent", "svg": BESOINS,
             "legende": "Ordres de grandeur (adulte : 2 000 à 2 700 kcal selon l'activité). Ils servent à comparer, pas à compter ses repas."},
        ],
    },
    "mastication": {
        "competence": "Identifier et localiser la transformation des aliments dans l'appareil digestif (mastication par les dents, changements de texture lors du trajet).",
        "visuels": [{"type": "schema", "titre": "La mâchoire du bas, vue de dessus"}],
    },
    "digestion": {
        "competence": "Nommer et localiser les différents organes du système digestif, en les associant à leur fonction ; nutriments utilisables par les organes.",
        "visuels": [{"type": "schema", "titre": "Le tube digestif"}],
    },
    "circulation": {
        "competence": "Identifier le rôle de la circulation sanguine dans l'approvisionnement des organes en nutriments ; associer l'augmentation de l'activité cardiaque lors d'un effort aux besoins accrus des muscles.",
        "visuels": [
            {"type": "schema", "titre": "Du repas aux muscles"},
            {"type": "svg", "etiquette": "Graphique", "titre": "Le pouls de Lou", "svg": POULS,
             "legende": "Relevés fictifs. Pouls = battements comptés en 15 secondes × 4."},
        ],
    },
}
