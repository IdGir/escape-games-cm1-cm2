# -*- coding: utf-8 -*-
"""Leçons imprimables — De l'édit de Nantes à Versailles (versailles)."""
from graphiques import etapes, tableau

JEU = {
    "titre": "De l'édit de Nantes à Versailles",
    "matiere": "Histoire",
    "theme": "La monarchie en France : Henri IV et l'édit de Nantes, Louis XIV à Versailles",
    "couleur": "#2a3f6b", "accent": "#b8860b",
    "couleur_pale": "#e9edf5", "accent_pale": "#fbf4dd",
}

BLEU, OR, ROUGE, GRIS, VERT = "#2a3f6b", "#b8860b", "#8a2626", "#5e5e5e", "#3f7a3a"

JOURNEE = etapes([
    ("8 h 30 · le lever", "réveil et habillage", BLEU),
    ("10 h · la messe", "à la chapelle", GRIS),
    ("11 h · le conseil", "avec les ministres", ROUGE),
    ("13 h · le dîner", "au petit couvert", OR),
    ("après-midi", "chasse ou promenade", VERT),
    ("22 h · le souper", "en public (grand couvert)", OR),
    ("vers 23 h · le coucher", "dernière cérémonie", BLEU),
], label="La journée du roi à Versailles")

DEUX_ROIS = tableau(["", "Henri IV", "Louis XIV"], [
    ["Règne", "1589-1610", "1643-1715"],
    ["Religion", "protestant, puis\ncatholique (1593)", "catholique"],
    ["Les protestants", "édit de Nantes (1598) :\nla tolérance", "révocation (1685) :\nune seule religion"],
    ["Où il gouverne", "Paris (le Louvre)", "Versailles (1682)"],
    ["Comment", "il ramène la paix", "il décide seul :\nmonarchie absolue"],
], label="Deux rois, deux façons de régner", largeurs=[1.1, 1.5, 1.5], couleur=BLEU)

LECONS = {
    "reforme-guerres": {
        "competence": "Henri IV et l'édit de Nantes : la naissance du protestantisme (la Réforme, les guerres de Religion).",
        "visuels": [
            {"type": "carte", "titre": "Les lieux de la Réforme",
             "legende": "Frontières actuelles, pour se repérer. Au XVIe siècle, l'Allemagne et l'Italie sont divisées en de nombreux États.",
             "spec": {"titre": "Les lieux de la Réforme", "largeur": 360, "cible_mm": 66,
                      "etendue": [[-5.0, 40.5], [17.0, 55.5]], "pays_mis_en_avant": ["France"],
                      "fleuves": ["Rhin", "Rhein", "Rhine", "Rhône", "Rhne", "Seine", "Loire", "Elbe"],
                      "points": [
                          {"lonlat": [12.65, 51.87], "nom": "Wittenberg (Luther, 1517)", "style": "etoile", "couleur": ROUGE, "pos": "n"},
                          {"lonlat": [6.14, 46.20], "nom": "Genève (Calvin)", "style": "etoile", "couleur": ROUGE, "pos": "e"},
                          {"lonlat": [12.48, 41.90], "nom": "Rome (le pape)", "pos": "w"},
                          {"lonlat": [2.35, 48.86], "nom": "Paris", "style": "capitale", "pos": "w"}],
                      "textes": [{"lonlat": [-3.0, 45.0], "texte": "OCÉAN\nATLANTIQUE", "style": "mer"}],
                      "echelle_km": 300}},
        ],
    },
    "edit-de-nantes": {
        "competence": "Henri IV et l'édit de Nantes : la naissance du protestantisme (l'édit de 1598, un pacte de tolérance).",
        "visuels": [
            {"type": "schema"},
            {"type": "carte", "titre": "Henri IV, de Pau à Nantes",
             "legende": "Pau : naissance (1553). Chartres : sacre (1594). Paris : entrée en 1594 ; conversion à Saint-Denis, tout près (1593). Nantes : l'édit (1598). Frontières actuelles.",
             "spec": {"titre": "Henri IV, de Pau à Nantes", "largeur": 360, "cible_mm": 66,
                      "etendue": [[-5.2, 41.3], [9.7, 51.2]], "pays_mis_en_avant": ["France"],
                      "fleuves": ["Seine", "Loire", "Rhône", "Rhne", "Garonne"],
                      "points": [
                          {"lonlat": [-1.55, 47.22], "nom": "Nantes", "style": "etoile", "couleur": ROUGE, "pos": "w"},
                          {"lonlat": [-0.37, 43.30], "nom": "Pau", "pos": "e"},
                          {"lonlat": [1.49, 48.45], "nom": "Chartres", "pos": "w"},
                          {"lonlat": [2.35, 48.86], "nom": "Paris", "style": "capitale", "pos": "e"}],
                      "textes": [{"lonlat": [-3.3, 45.6], "texte": "OCÉAN\nATLANTIQUE", "style": "mer"}],
                      "echelle_km": 200}},
        ],
    },
    "chateau-versailles": {
        "competence": "Louis XIV, le roi soleil à Versailles (le château, la cour, le symbole du Soleil).",
        "visuels": [
            {"type": "schema", "legende": "Schéma simplifié, sans échelle : le château entre la ville (à l'est) et les jardins (à l'ouest)."},
            {"type": "carte", "titre": "Versailles et les résidences du roi",
             "legende": "Louis XIV naît à Saint-Germain-en-Laye (1638) ; il s'installe à Versailles en 1682 ; il signe la révocation de l'édit de Nantes à Fontainebleau (1685).",
             "spec": {"titre": "Versailles et les résidences du roi", "largeur": 360, "cible_mm": 66,
                      "etendue": [[1.55, 48.25], [3.05, 49.10]], "fleuves": ["Seine", "Marne", "Oise"],
                      "points": [
                          {"lonlat": [2.13, 48.80], "nom": "Versailles", "style": "etoile", "couleur": OR, "pos": "w"},
                          {"lonlat": [2.35, 48.86], "nom": "Paris", "style": "capitale", "pos": "e"},
                          {"lonlat": [2.09, 48.90], "nom": "Saint-Germain-en-Laye", "pos": "n"},
                          {"lonlat": [2.70, 48.40], "nom": "Fontainebleau", "pos": "e"}],
                      "echelle_km": 20}},
        ],
    },
    "journee-du-roi": {
        "competence": "Louis XIV, le roi soleil à Versailles : la monarchie absolue (la journée du roi, l'étiquette).",
        "visuels": [
            {"type": "svg", "etiquette": "Schéma", "titre": "La journée du roi", "svg": JOURNEE,
             "legende": "D'après le château de Versailles, « La journée du roi » (Mathieu da Vinha). Trois soirs par semaine, à 19 h : les soirées d'appartement.",
             "source": "Château de Versailles, ressources pédagogiques."},
        ],
    },
    "monarchie-absolue": {
        "competence": "Louis XIV, le roi soleil à Versailles : la monarchie absolue (comparaison avec Henri IV ; CM2 : la révocation de 1685).",
        "visuels": [
            {"type": "schema"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Deux rois, deux façons de régner", "svg": DEUX_ROIS},
        ],
    },
}
