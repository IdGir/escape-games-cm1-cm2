# -*- coding: utf-8 -*-
"""Leçons imprimables — La Station météo disparue (station-meteo)."""
from graphiques import barres, courbes, tableau, climatogramme, picto

JEU = {
    "titre": "La Station météo disparue",
    "matiere": "Sciences",
    "theme": "La planète Terre : réaliser et exploiter des mesures météorologiques",
    "couleur": "#13286b", "accent": "#d68910",
    "couleur_pale": "#ebeff8", "accent_pale": "#fdf3e1",
}
BLEU, ROUGE, ORANGE = "#2f6690", "#b22222", "#d68910"
JOURS = ["Lun.", "Mar.", "Mer.", "Jeu.", "Ven."]
# Relevés de la semaine du jeu (station fictive, données cohérentes du jeu)
TMIN, TMAX = [9, 11, 12, 8, 7], [17, 19, 21, 14, 16]
VENT, PLUIE = [12, 18, 24, 30, 8], [0, 3, 7, 12, 0]

BEAUFORT = tableau(["Force", "Nom", "Vitesse", "Ce que l'on voit"], [
    ["0", "calme", "moins de 1 km/h", "la fumée monte droit"],
    ["2", "légère brise", "6 à 11 km/h", "le vent sur le visage"],
    ["4", "jolie brise", "20 à 28 km/h", "la poussière se soulève"],
    ["6", "vent frais", "39 à 49 km/h", "les grosses branches\ns'agitent"],
    ["8", "coup de vent", "62 à 74 km/h", "des branches cassent"],
    ["12", "ouragan", "118 km/h et plus", "dégâts très importants"],
], couleur=BLEU, largeurs=[0.55, 1.05, 1.15, 1.6])

RELEVES = tableau(["", *JOURS], [
    ["T. min (°C)", *map(str, TMIN)],
    ["T. max (°C)", *map(str, TMAX)],
    ["Vent (km/h)", *map(str, VENT)],
    ["Pluie (mm)", *map(str, PLUIE)],
], couleur=BLEU, largeurs=[1.5, 1, 1, 1, 1, 1])

VILLES = [("Lille", [3.06, 50.63], "nuages", "13°"), ("Brest", [-4.49, 48.39], "pluie", "14°"),
          ("Paris", [2.35, 48.86], "eclaircies", "17°"), ("Strasbourg", [7.75, 48.58], "eclaircies", "18°"),
          ("Dijon", [5.04, 47.32], "soleil", "19°"), ("Bordeaux", [-0.58, 44.84], "pluie", "18°"),
          ("Lyon", [4.84, 45.76], "soleil", "21°"), ("Marseille", [5.37, 43.30], "soleil", "24°"),
          ("Toulouse", [1.44, 43.60], "eclaircies", "22°")]

LECONS = {
    "thermometre": {
        "competence": "Réaliser des mesures météorologiques en utilisant des capteurs : le thermomètre.",
        "visuels": [
            {"type": "schema", "titre": "Lire un thermomètre"},
            {"type": "photo", "src": "assets/images/cartes/e1-2.jpg", "titre": "Un abri météorologique",
             "legende": "Blanc et percé de persiennes : l'air circule, le soleil ne chauffe pas le capteur.", "facultatif": False},
        ],
    },
    "vent": {
        "competence": "Réaliser des mesures météorologiques en utilisant des capteurs : l'anémomètre (et la girouette).",
        "visuels": [
            {"type": "schema", "titre": "La rose des vents"},
            {"type": "photo", "src": "assets/images/cartes/e2-2.jpg", "titre": "Girouette et anémomètre",
             "legende": "La girouette donne la direction, l'anémomètre à coupelles la vitesse.", "facultatif": False},
            {"type": "svg", "etiquette": "Tableau", "titre": "L'échelle de Beaufort (extrait)", "svg": BEAUFORT},
        ],
    },
    "pluie": {
        "competence": "Réaliser des mesures météorologiques en utilisant des capteurs : le pluviomètre.",
        "visuels": [
            {"type": "schema", "titre": "1 mm de pluie = 1 litre par m²"},
            {"type": "photo", "src": "assets/images/cartes/e3-2.jpg", "titre": "Un pluviomètre", "facultatif": False},
            {"type": "svg", "etiquette": "Graphique", "titre": "La pluie de la semaine (station du jeu)",
             "svg": barres([(j, v) for j, v in zip(JOURS, PLUIE)], unite="mm", titre_y="Pluie", couleur="#5b9bd5", vmax=14, graduation=2),
             "legende": "Cumul de la semaine : 0 + 3 + 7 + 12 + 0 = 22 mm."},
        ],
    },
    "releves": {
        "competence": "Exploiter des mesures météorologiques (organiser et lire un tableau de relevés).",
        "visuels": [
            {"type": "svg", "etiquette": "Tableau", "titre": "Le tableau des relevés de la semaine", "svg": RELEVES,
             "legende": "Une ligne par grandeur, une colonne par jour, l'unité toujours écrite."},
            {"type": "schema", "etiquette": "Graphique", "titre": "Les températures de la semaine"},
            {"type": "svg", "etiquette": "Graphique", "titre": "Le vent de la semaine",
             "svg": barres([(j, v) for j, v in zip(JOURS, VENT)], unite="km/h", titre_y="Vitesse", couleur="#7f8c8d", vmax=35, graduation=5)},
        ],
    },
    "bulletin": {
        "competence": "Exploiter des mesures météorologiques (distinguer météo et climat, prévoir).",
        "visuels": [
            {"type": "carte", "titre": "Une carte de bulletin météo (exemple fictif)",
             "legende": "Le bulletin traduit les mesures en symboles faciles à lire.",
             "spec": {"titre": "Carte de bulletin météo", "largeur": 360, "cible_mm": 66,
                      "etendue": [[-5.2, 41.3], [9.7, 51.2]], "pays_mis_en_avant": ["France"],
                      "points": [{"lonlat": ll, "nom": f"{n} {t}", "style": "symbole", "symbole": picto(k, 11), "pos": "s", "taille": 0.8}
                                 for n, ll, k, t in VILLES], "nord": False}},
            {"type": "svg", "etiquette": "Graphique", "titre": "Le climat de Dijon (normales 1991-2020)",
             "svg": climatogramme([2.7, 3.8, 7.5, 10.7, 14.6, 18.5, 20.8, 20.4, 16.4, 11.8, 6.5, 3.4],
                                  [56.8, 42.9, 48.2, 57.5, 76.1, 65.8, 64.9, 62.0, 56.4, 73.6, 77.6, 61.6]),
             "legende": "Le climat, c'est la moyenne sur 30 ans : 11,4 °C et 743 mm de pluie par an à Dijon.",
             "source": "Météo-France, normales 1991-2020, station Dijon-Longvic (valeurs publiées par Infoclimat)."},
            {"type": "schema", "titre": "De la mesure à la prévision"},
        ],
    },
}
