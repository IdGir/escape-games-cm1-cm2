# -*- coding: utf-8 -*-
"""Leçons imprimables — Le Manuscrit de l'abbaye (moyen-age-abbaye)."""
from graphiques import ouvrir, texte, taille, tableau

JEU = {
    "titre": "Le Manuscrit de l'abbaye",
    "matiere": "Histoire",
    "theme": "Le Moyen Âge : Clovis, Charlemagne, le rôle social de l'Église, l'art roman et l'art gothique",
    "couleur": "#16296b", "accent": "#a8261b",
    "couleur_pale": "#eceff8", "accent_pale": "#fbeeed",
}
BLEU, ROUGE, OR, VERT, VIOLET = "#1f3f8f", "#a8261b", "#b8860b", "#3d7a3a", "#6b4c9a"

ETENDUE_GAULE = [[-5.3, 41.6], [10.2, 51.6]]
MERS_GAULE = [{"lonlat": [-4.0, 45.2], "texte": "OCÉAN\nATLANTIQUE", "style": "mer"},
              {"lonlat": [5.3, 42.2], "texte": "MER MÉDITERRANÉE", "style": "mer"}]

# Tracés volontairement simplifiés (étendue approximative des royaumes vers 511).
FRANCS_511 = [(-1.8, 43.3), (-4.9, 47.8), (-2.0, 49.0), (2.0, 51.2), (4.5, 52.5), (6.8, 53.5), (8.8, 52.0),
              (9.4, 50.3), (8.5, 48.6), (7.6, 47.6), (6.8, 47.75), (5.4, 48.05), (4.2, 47.95), (3.1, 47.25),
              (3.0, 46.8), (3.3, 46.0), (3.3, 44.9), (2.6, 43.65), (1.9, 43.4), (1.8, 42.5), (-0.5, 42.7)]
BURGONDES = [(3.1, 47.25), (4.2, 47.95), (5.4, 48.05), (6.8, 47.75), (7.6, 47.6), (8.0, 46.3), (7.0, 45.2),
             (6.9, 44.4), (5.2, 44.25), (4.65, 44.3), (4.0, 45.0), (3.3, 46.0), (3.0, 46.8)]
WISIGOTHS = [(1.8, 42.5), (1.9, 43.4), (2.6, 43.65), (3.3, 44.3), (4.4, 44.15), (4.65, 43.5), (3.2, 42.4)]
OSTROGOTHS = [(4.65, 43.4), (4.65, 44.3), (5.2, 44.25), (6.9, 44.4), (7.7, 44.1), (7.5, 43.7)]

EMPIRE_814 = [(2.2, 41.3), (0.5, 42.6), (-1.8, 43.3), (-1.2, 46.2), (-2.2, 47.3), (-1.6, 48.7), (1.5, 50.9),
              (4.0, 51.8), (5.0, 53.3), (8.3, 54.0), (9.6, 54.8), (10.6, 54.0), (11.2, 53.0), (12.0, 51.9),
              (12.3, 50.6), (13.0, 49.6), (13.8, 48.8), (16.4, 48.3), (16.7, 47.2), (15.8, 46.4), (14.0, 45.5),
              (13.3, 44.8), (13.9, 42.6), (14.2, 42.3), (13.9, 41.5), (13.0, 41.3), (12.2, 41.8), (10.9, 42.5),
              (9.8, 44.0), (8.4, 44.2), (7.4, 43.8), (5.0, 43.3), (3.1, 42.5)]


def oeuvres_eglise():
    W, H = 360, 200
    fs = taille(W, 66)
    s = [ouvrir(W, H, "Le rôle social de l'Église au Moyen Âge")]
    cx, cy = W / 2, H / 2
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{fs*3.3:.1f}" fill="{BLEU}"/>')
    s.append(texte(cx, cy - fs * 0.2, "L'ÉGLISE", fs * 1.05, fill="#fff", poids=800))
    s.append(texte(cx, cy + fs * 1.1, "aide et enseigne", fs * 0.78, fill="#fff"))
    boites = [(8, 10, "SOIGNER", "hôtels-Dieu", ROUGE), (W - 128, 10, "HÉBERGER", "pèlerins, voyageurs", VERT),
              (8, H - 62, "NOURRIR", "aumônes aux pauvres", OR), (W - 128, H - 62, "INSTRUIRE", "écoles, monastères", VIOLET)]
    for x, y, t, st, c in boites:
        s.append(f'<line x1="{cx}" y1="{cy}" x2="{x+60}" y2="{y+26}" stroke="{c}" stroke-width="1.6"/>')
    for x, y, t, st, c in boites:
        s.append(f'<rect x="{x}" y="{y}" width="120" height="52" rx="7" fill="#fff" stroke="{c}" stroke-width="1.6"/>')
        s.append(texte(x + 60, y + fs * 1.45, t, fs, fill=c, poids=800))
        s.append(texte(x + 60, y + fs * 2.75, st, fs * 0.78, fill="#1f2328"))
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{fs*3.3:.1f}" fill="{BLEU}"/>')
    s.append(texte(cx, cy - fs * 0.2, "L'ÉGLISE", fs * 1.05, fill="#fff", poids=800))
    s.append(texte(cx, cy + fs * 1.1, "aide et enseigne", fs * 0.78, fill="#fff"))
    s.append("</svg>")
    return "".join(s)


LECONS = {
    "clovis": {
        "competence": "Repère chronologique : la fin de l'Empire romain (476) et l'avènement des royaumes francs.",
        "visuels": [
            {"type": "carte", "titre": "Les royaumes de la Gaule vers 511",
             "legende": "À la mort de Clovis (511), les Francs dominent presque toute la Gaule. Tracés simplifiés et approximatifs.",
             "spec": {"titre": "Les royaumes de la Gaule vers 511", "largeur": 360, "cible_mm": 66,
                      "etendue": ETENDUE_GAULE, "frontieres": False, "fleuves": ["Seine", "Loire", "Rhône", "Rhne", "Rhin", "Rhein", "Garonne"],
                      "zones": [{"coords": FRANCS_511, "couleur": BLEU, "opacite": 0.28},
                                {"coords": BURGONDES, "couleur": OR, "opacite": 0.35},
                                {"coords": WISIGOTHS, "couleur": VERT, "opacite": 0.35},
                                {"coords": OSTROGOTHS, "couleur": VIOLET, "opacite": 0.35}],
                      "points": [{"lonlat": [4.034, 49.258], "nom": "Reims", "pos": "e"},
                                 {"lonlat": [3.323, 49.381], "nom": "Soissons\n(486)", "pos": "w"},
                                 {"lonlat": [2.35, 48.857], "nom": "Paris", "style": "capitale", "pos": "s"},
                                 {"lonlat": [0.23, 46.64], "nom": "Vouillé (507)", "pos": "w"}],
                      "textes": MERS_GAULE[:1],
                      "legende": [{"type": "zone", "couleur": BLEU, "texte": "Francs", "opacite": 0.3},
                                  {"type": "zone", "couleur": OR, "texte": "Burgondes"},
                                  {"type": "zone", "couleur": VERT, "texte": "Wisigoths"},
                                  {"type": "zone", "couleur": VIOLET, "texte": "Ostrogoths"}],
                      "position_legende": "bas-droite"}},
            {"type": "photo", "src": "assets/images/cartes/e1-2.jpg", "titre": "Le baptême de Clovis",
             "legende": "Le baptême de Clovis vu par un enlumineur, des siècles plus tard."},
        ],
    },
    "charlemagne": {
        "competence": "Repère chronologique : Charlemagne et son empire, dans la continuité de l'Empire romain.",
        "visuels": [
            {"type": "carte", "titre": "L'empire de Charlemagne en 814",
             "legende": "À sa mort (814), l'empire s'étend de l'Èbre à l'Elbe et jusqu'au centre de l'Italie. Tracé simplifié.",
             "spec": {"titre": "L'empire de Charlemagne en 814", "largeur": 360, "cible_mm": 66,
                      "etendue": [[-5.5, 38.5], [19.5, 56.0]], "frontieres": False,
                      "fleuves": ["Rhin", "Rhein", "Elbe", "Donau", "Loire", "Rhône", "Rhne", "Po", "Ebro"],
                      "zones": [{"coords": EMPIRE_814, "couleur": ROUGE, "opacite": 0.25}],
                      "points": [{"lonlat": [6.083, 50.776], "nom": "Aix-la-Chapelle", "style": "capitale", "couleur": ROUGE, "pos": "e"},
                                 {"lonlat": [12.49, 41.9], "nom": "Rome (800)", "pos": "w"},
                                 {"lonlat": [2.35, 48.857], "nom": "Paris", "pos": "w"},
                                 {"lonlat": [0.69, 47.39], "nom": "Tours", "pos": "s"}],
                      "textes": [{"lonlat": [-3.2, 45.3], "texte": "OCÉAN\nATLANTIQUE", "style": "mer"},
                                 {"lonlat": [6.0, 40.2], "texte": "MER MÉDITERRANÉE", "style": "mer"}],
                      "legende": [{"type": "zone", "couleur": ROUGE, "texte": "Empire en 814", "opacite": 0.3},
                                  {"type": "point", "couleur": "#1f2328", "texte": "Ville"}],
                      "position_legende": "haut-gauche", "echelle_km": 300}},
            {"type": "photo", "src": "assets/images/decors/salle2.jpg", "titre": "La chapelle palatine d'Aix-la-Chapelle",
             "legende": "Construite pour Charlemagne vers 800, elle est aujourd'hui dans la cathédrale d'Aix-la-Chapelle."},
        ],
    },
    "scriptorium": {
        "competence": "Décrire le rôle social de l'Église : l'enseignement.",
        "visuels": [
            {"type": "schema"},
            {"type": "carte", "titre": "Grandes abbayes de Bourgogne",
             "legende": "Cluny (910), Cîteaux (1098) et Fontenay (1118) : la Bourgogne, terre d'abbayes.",
             "spec": {"titre": "Grandes abbayes de Bourgogne", "largeur": 360, "cible_mm": 66, "resolution": "10m",
                      "etendue": [[2.7, 46.15], [5.6, 48.05]], "fleuves": ["Saône", "Sane", "Yonne", "Loire", "Seine", "Doubs"],
                      "points": [{"lonlat": [4.659, 46.434], "nom": "Cluny", "style": "etoile", "couleur": ROUGE, "pos": "w"},
                                 {"lonlat": [5.096, 47.128], "nom": "Cîteaux", "style": "etoile", "couleur": ROUGE, "pos": "e"},
                                 {"lonlat": [4.389, 47.639], "nom": "Fontenay", "style": "etoile", "couleur": ROUGE, "pos": "e"},
                                 {"lonlat": [3.748, 47.466], "nom": "Vézelay", "style": "etoile", "couleur": ROUGE, "pos": "w"},
                                 {"lonlat": [5.041, 47.322], "nom": "Dijon", "style": "capitale", "pos": "n"},
                                 {"lonlat": [3.567, 47.798], "nom": "Auxerre", "pos": "e"},
                                 {"lonlat": [4.299, 46.951], "nom": "Autun", "pos": "w"},
                                 {"lonlat": [4.835, 45.764], "nom": "Lyon", "pos": "e"}],
                      "legende": [{"type": "etoile", "couleur": ROUGE, "texte": "Abbaye"}],
                      "position_legende": "bas-droite", "echelle_km": 50}},
            {"type": "photo", "src": "assets/images/cartes/e3-2.jpg", "titre": "Une lettrine historiée",
             "legende": "Une lettre ornée d'une scène, peinte par un enlumineur."},
        ],
    },
    "hotel-dieu": {
        "competence": "Décrire le rôle social de l'Église : l'assistance aux pauvres et aux malades.",
        "visuels": [
            {"type": "svg", "titre": "Ce que fait l'Église pour les plus pauvres", "svg": oeuvres_eglise()},
            {"type": "photo", "src": "assets/images/cartes/e4-1.jpg", "titre": "La grande salle des « pôvres » à Beaune",
             "legende": "L'hôtel-Dieu de Beaune, fondé en 1443 : les lits des malades alignés face à la chapelle.",
             "facultatif": False},
        ],
    },
    "roman-gothique": {
        "competence": "Différencier l'art roman et l'art gothique.",
        "visuels": [
            {"type": "schema"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Roman ou gothique ?",
             "svg": tableau(["", "Roman", "Gothique"], [
                 ["Époque", "XIe - XIIe siècle", "à partir du milieu\ndu XIIe siècle"],
                 ["Voûte", "en berceau", "sur croisées d'ogives"],
                 ["Arc", "plein cintre\n(demi-cercle)", "brisé\n(en pointe)"],
                 ["Murs", "épais, contreforts", "fins, arcs-boutants"],
                 ["Fenêtres", "petites :\néglise sombre", "grandes, vitraux :\néglise lumineuse"],
             ], couleur=BLEU, largeurs=[0.9, 1.2, 1.3])},
            {"type": "carte", "titre": "Quelques églises romanes et gothiques",
             "spec": {"titre": "Églises romanes et gothiques", "largeur": 360, "cible_mm": 66,
                      "etendue": [[-5.2, 41.3], [9.7, 51.2]], "pays_mis_en_avant": ["France"],
                      "points": [{"lonlat": [3.748, 47.466], "nom": "Vézelay", "couleur": OR, "pos": "w"},
                                 {"lonlat": [4.659, 46.434], "nom": "Cluny", "couleur": OR, "pos": "e"},
                                 {"lonlat": [2.398, 44.599], "nom": "Conques", "couleur": OR, "pos": "e"},
                                 {"lonlat": [1.442, 43.608], "nom": "Toulouse", "couleur": OR, "pos": "w"},
                                 {"lonlat": [2.360, 48.936], "nom": "Saint-Denis", "couleur": BLEU, "pos": "w", "style": "capitale"},
                                 {"lonlat": [1.488, 48.448], "nom": "Chartres", "couleur": BLEU, "pos": "w", "style": "capitale"},
                                 {"lonlat": [4.034, 49.254], "nom": "Reims", "couleur": BLEU, "pos": "e", "style": "capitale"},
                                 {"lonlat": [2.302, 49.895], "nom": "Amiens", "couleur": BLEU, "pos": "e", "style": "capitale"}],
                      "legende": [{"type": "point", "couleur": OR, "texte": "Église romane"},
                                  {"type": "zone", "couleur": BLEU, "texte": "Cathédrale ou basilique gothique", "opacite": 1}],
                      "position_legende": "bas-droite"}},
            {"type": "photo", "src": "assets/images/decors/salle5.jpg", "titre": "Vézelay : nef romane, chœur gothique"},
        ],
    },
}
