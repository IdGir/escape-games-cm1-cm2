# -*- coding: utf-8 -*-
"""Leçons imprimables — Le Tour du monde en 80 minutes (tour-du-monde)."""
import re
from graphiques import ouvrir, texte, taille
import construire

JEU = {
    "titre": "Le Tour du monde en 80 minutes",
    "matiere": "Géographie",
    "theme": "Se repérer dans le monde : planisphère, orientation, échelle, climats, fuseaux horaires",
    "couleur": "#0f4c5c", "accent": "#e36414",
    "couleur_pale": "#e7f0f2", "accent_pale": "#fdf0e7",
}
C1, C2, BLEU, ROUGE = "#0f4c5c", "#e36414", "#2f6690", "#b3261e"
MONDE = [[-180, -60], [180, 84]]
W_PLEIN, MM_PLEIN = 720, 186

ROUTE_TRAIN = [
    [[-0.128, 51.507], [2.35, 48.86], [7.68, 45.07], [11.34, 44.49], [17.94, 40.63]],
    [[72.88, 19.08], [81.85, 25.44], [88.36, 22.57]],
    [[-122.42, 37.77], [-95.9, 41.26], [-87.6, 41.88], [-74.0, 40.71]],
    [[-8.29, 51.85], [-2.98, 53.41], [-0.128, 51.507]],
]
ROUTE_MER = [
    [[17.94, 40.63], [19.3, 38.8], [22.3, 35.9], [26.0, 33.9], [32.3, 31.26], [32.55, 29.97], [34.8, 27.0],
     [38.5, 21.0], [42.0, 15.5], [43.4, 12.6], [45.03, 12.8], [72.88, 19.08]],
    [[88.36, 22.57], [88.2, 21.0], [91.0, 16.0], [94.0, 10.0], [96.8, 6.2], [100.2, 3.2], [103.82, 1.29],
     [106.5, 7.5], [110.5, 14.0], [114.17, 22.3], [119.8, 24.5], [121.47, 31.23], [126.0, 31.5], [130.3, 30.6],
     [135.5, 33.2], [139.64, 35.44]],
    [[139.64, 35.44], [-122.42, 37.77]],
    [[-74.0, 40.71], [-8.29, 51.85]],
]
ESCALES = [("Londres", [-0.128, 51.507], "n"), ("Suez", [32.55, 29.97], "e"), ("Bombay", [72.88, 19.08], "s"),
           ("Calcutta", [88.36, 22.57], "n"), ("Hong Kong", [114.17, 22.3], "w"), ("Yokohama", [139.64, 35.44], "n"),
           ("San Francisco", [-122.42, 37.77], "s"), ("New York", [-74.0, 40.71], "s")]


def rose_des_vents():
    W = H = 300
    fs = taille(W, 66)
    cx = cy = 150
    s = [ouvrir(W, H, "La rose des vents")]
    import math
    for k in range(8):
        a = math.radians(k * 45)
        L = 118 if k % 2 == 0 else 78
        l = 18 if k % 2 == 0 else 12
        tip = (cx + L * math.sin(a), cy - L * math.cos(a))
        g = (cx + l * math.sin(a - math.pi / 2), cy - l * math.cos(a - math.pi / 2))
        d = (cx + l * math.sin(a + math.pi / 2), cy - l * math.cos(a + math.pi / 2))
        s.append(f'<polygon points="{cx},{cy} {g[0]:.1f},{g[1]:.1f} {tip[0]:.1f},{tip[1]:.1f}" fill="{C1 if k % 2 == 0 else "#7aa5b0"}"/>')
        s.append(f'<polygon points="{cx},{cy} {d[0]:.1f},{d[1]:.1f} {tip[0]:.1f},{tip[1]:.1f}" fill="{"#2c7a8c" if k % 2 == 0 else "#b9d2d8"}"/>')
    noms = ["N", "NE", "E", "SE", "S", "SO", "O", "NO"]
    for k, n in enumerate(noms):
        a = math.radians(k * 45)
        R = 136 if k % 2 == 0 else 96
        s.append(texte(cx + R * math.sin(a), cy - R * math.cos(a) + fs * 0.4, n, fs * (1.25 if k % 2 == 0 else 0.95), fill=C2 if n == "N" else "#1f2328", poids=800))
    s.append(f'<circle cx="{cx}" cy="{cy}" r="6" fill="#fff" stroke="{C1}" stroke-width="2"/>')
    s.append("</svg>")
    return "".join(s)


def carte_legendee():
    """Une carte de France entourée de ses quatre éléments, légendés."""
    carte = construire.carte({"titre": "La France", "largeur": 300, "cible_mm": 50, "etendue": [[-5.2, 41.3], [9.7, 51.2]],
                               "pays_mis_en_avant": ["France"], "fleuves": ["Seine", "Loire", "Rhône", "Rhne", "Garonne"],
                               "points": [{"lonlat": [2.35, 48.86], "nom": "Paris", "style": "capitale", "pos": "e"},
                                          {"lonlat": [5.04, 47.32], "nom": "Dijon", "pos": "e"},
                                          {"lonlat": [5.37, 43.3], "nom": "Marseille", "pos": "w"}],
                               "legende": [{"type": "zone", "couleur": "#fbe9c8", "texte": "France", "opacite": 1},
                                           {"type": "ligne", "couleur": "#4f8fc4", "texte": "fleuve"},
                                           {"type": "point", "couleur": "#1f2328", "texte": "ville"}],
                               "echelle_km": 200})
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', carte)
    cw, ch = int(m.group(1)), int(m.group(2))
    W = 400
    fs = taille(W, 66)
    iw = 250
    ih = ch * iw / cw
    top, x0 = 34, 74
    H = top + ih + 8
    inner = carte.replace("<svg ", f'<svg x="{x0}" y="{top}" width="{iw}" height="{ih:.0f}" ', 1)
    s = [ouvrir(W, H, "Les quatre éléments d'une carte")]
    s.append(texte(x0 + 40, 22, "La France : villes et fleuves", fs * 0.85, "start", "#1f2328", 800))
    s.append(inner)
    def call(x1, y1, x2, y2, t, a):
        return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{C2}" stroke-width="1.4"/>' +
                texte(x2 + (-3 if a == "end" else 3), y2 + fs * 0.35, t, fs * 0.85, a, C2, 800))
    s.append(call(x0 + 36, 18, x0 - 6, 18, "① titre", "end"))
    s.append(call(x0 + iw - 8, top + 12, x0 + iw + 8, top + 12, "② orien-\ntation", "start"))
    s.append(call(x0 + iw - 40, top + ih - 25, x0 + iw + 8, top + ih - 25, "③ légende", "start"))
    s.append(call(x0 + 20, top + ih - 8, x0 - 6, top + ih - 38, "④ échelle", "end"))
    s.append("</svg>")
    return "".join(s)


def spec_monde(**k):
    base = {"largeur": W_PLEIN, "cible_mm": MM_PLEIN, "projection": "robinson", "etendue": MONDE, "nord": False,
            "frontieres": False, "resolution": "110m"}
    base.update(k)
    return base


CONTINENTS = [{"lonlat": ll, "texte": t, "style": "region", "taille": 1.1} for t, ll in
              [("AMÉRIQUE\nDU NORD", [-102, 48]), ("AMÉRIQUE\nDU SUD", [-60, -12]), ("EUROPE", [18, 53]),
               ("AFRIQUE", [20, 8]), ("ASIE", [92, 50]), ("OCÉANIE", [133, -24]), ("ANTARCTIQUE", [40, -80])]]
OCEANS = [{"lonlat": ll, "texte": t, "style": "mer", "taille": 1.05} for t, ll in
          [("OCÉAN PACIFIQUE", [-140, 8]), ("OCÉAN PACIFIQUE", [168, -12]), ("OCÉAN\nATLANTIQUE", [-33, 22]),
           ("OCÉAN INDIEN", [80, -22]), ("OCÉAN ARCTIQUE", [-10, 80]), ("OCÉAN AUSTRAL", [90, -58])]]

LECONS = {
    "planisphere": {
        "competence": "Se repérer sur un planisphère : nommer et localiser les continents et les océans.",
        "visuels": [
            {"type": "carte", "largeur": "pleine", "titre": "Le planisphère : 7 continents et 5 océans",
             "spec": spec_monde(titre="Planisphère", graticule=30, textes=CONTINENTS + OCEANS,
                                couleurs={"terre": "#efe3c8"})},
            {"type": "photo", "src": "assets/images/decors/etape1.jpg", "titre": "Le Reform Club, à Londres",
             "legende": "Le point de départ du pari de Phileas Fogg (roman de Jules Verne, 1872)."},
        ],
    },
    "orientation": {
        "competence": "Se repérer : les points cardinaux et la rose des vents.",
        "visuels": [
            {"type": "svg", "titre": "La rose des vents", "svg": rose_des_vents(),
             "legende": "4 points cardinaux et 4 directions intermédiaires. Le soleil se lève à l'est."},
            {"type": "carte", "largeur": "pleine", "titre": "Phileas Fogg voyage toujours vers l'est",
             "spec": spec_monde(titre="Le sens du voyage", graticule=30,
                                lignes=[{"coords": c, "couleur": C2, "epaisseur": 2, "fleches": True} for c in ROUTE_TRAIN + ROUTE_MER],
                                points=[{"lonlat": ll, "nom": n, "pos": p, "couleur": C1} for n, ll, p in ESCALES],
                                textes=[{"lonlat": [-175, 70], "texte": "OUEST", "style": "region", "couleur": C1},
                                        {"lonlat": [172, 70], "texte": "EST", "style": "region", "couleur": C1}])},
        ],
    },
    "carte": {
        "competence": "Utiliser l'échelle d'une carte ; lire une légende.",
        "visuels": [
            {"type": "svg", "titre": "Les quatre éléments d'une carte", "svg": carte_legendee(),
             "legende": "Titre, orientation, légende, échelle : sans eux, une carte est illisible.",
             "source": construire.SOURCE_CARTE},
        ],
    },
    "climats": {
        "competence": "Identifier et localiser les grands types de climats et de paysages dans le monde.",
        "visuels": [
            {"type": "carte", "largeur": "pleine", "titre": "Les grandes zones climatiques de la Terre",
             "legende": "Zone chaude entre les tropiques, zones tempérées aux latitudes moyennes, zones froides autour des pôles. "
                        "L'altitude refroidit aussi le climat (montagnes).",
             "spec": spec_monde(titre="Zones climatiques",
                                bandes=[{"lat": [-23.44, 23.44], "couleur": "#f4a259"},
                                        {"lat": [23.44, 66.56], "couleur": "#8cc084"}, {"lat": [-66.56, -23.44], "couleur": "#8cc084"},
                                        {"lat": [66.56, 90], "couleur": "#a9cce3"}, {"lat": [-90, -66.56], "couleur": "#a9cce3"}],
                                meridiens=[],
                                lignes=[{"coords": [[-180, la], [-90, la], [0, la], [90, la], [180, la]], "couleur": "#5b6470", "epaisseur": 0.8, "pointille": True}
                                        for la in (23.44, -23.44, 66.56, -66.56)] +
                                       [{"coords": [[-180, 0], [-90, 0], [0, 0], [90, 0], [180, 0]], "couleur": ROUGE, "epaisseur": 1.2}],
                                textes=[{"lonlat": [-168, 1.5], "texte": "équateur", "style": "mer", "couleur": ROUGE},
                                        {"lonlat": [-163, 25], "texte": "tropique du Cancer", "style": "mer", "couleur": "#3b434b"},
                                        {"lonlat": [-163, -22], "texte": "tropique du Capricorne", "style": "mer", "couleur": "#3b434b"},
                                        {"lonlat": [-160, 68], "texte": "cercle polaire", "style": "mer", "couleur": "#3b434b"}],
                                legende=[{"type": "zone", "couleur": "#a9cce3", "texte": "zone froide", "opacite": 1},
                                         {"type": "zone", "couleur": "#8cc084", "texte": "zone tempérée", "opacite": 1},
                                         {"type": "zone", "couleur": "#f4a259", "texte": "zone chaude", "opacite": 1}],
                                position_legende="bas-gauche")},
            {"type": "photo", "src": "assets/images/cartes/paysage-desert.jpg", "titre": "Climat aride : le Sahara"},
            {"type": "photo", "src": "assets/images/cartes/paysage-jungle.jpg", "titre": "Climat équatorial : la forêt"},
        ],
    },
    "deplacer": {
        "competence": "Identifier un itinéraire, les moyens de transport et le rôle des canaux et des détroits.",
        "visuels": [
            {"type": "carte", "largeur": "pleine", "titre": "Le tour du monde de Phileas Fogg (1872) et les grands passages",
             "spec": spec_monde(titre="Itinéraire de Phileas Fogg",
                                lignes=[{"coords": c, "couleur": BLEU, "epaisseur": 2} for c in ROUTE_MER] +
                                       [{"coords": c, "couleur": ROUGE, "epaisseur": 2, "pointille": True} for c in ROUTE_TRAIN],
                                points=[{"lonlat": ll, "nom": n, "pos": p} for n, ll, p in ESCALES] +
                                       [{"lonlat": [-79.7, 9.1], "nom": "canal de Panama", "style": "etoile", "couleur": C2, "pos": "s"},
                                        {"lonlat": [-5.6, 35.95], "nom": "Gibraltar", "style": "etoile", "couleur": C2, "pos": "w"},
                                        {"lonlat": [101.0, 2.5], "nom": "Malacca", "style": "etoile", "couleur": C2, "pos": "s"},
                                        {"lonlat": [32.4, 30.6], "nom": "", "style": "etoile", "couleur": C2}],
                                legende=[{"type": "ligne", "couleur": BLEU, "texte": "en paquebot"},
                                         {"type": "ligne", "couleur": ROUGE, "texte": "en train", "pointille": True},
                                         {"type": "etoile", "couleur": C2, "texte": "canal ou détroit"}],
                                position_legende="bas-gauche")},
            {"type": "photo", "src": "assets/images/decors/etape2.jpg", "titre": "Le canal de Suez",
             "legende": "Ouvert en 1869, il relie la mer Méditerranée à la mer Rouge."},
        ],
    },
    "fuseaux": {
        "competence": "Repères géographiques : les méridiens et les fuseaux horaires.",
        "visuels": [
            {"type": "carte", "largeur": "pleine", "titre": "Quand il est midi à Londres… (fuseaux théoriques de 15°)",
             "legende": "Vers l'est, on ajoute une heure tous les 15° ; vers l'ouest, on en retire une. "
                        "Les vrais fuseaux suivent souvent les frontières des pays.",
             "spec": spec_monde(titre="Fuseaux horaires", projection="equirect", graticule=None, etendue=[[-180, -56], [180, 76]],
                                meridiens=[{"lon": lo, "couleur": ROUGE if lo == 0 else "#7a8691", "epaisseur": 1.6 if lo == 0 else 0.6,
                                            "pointille": lo != 0, "libelle": f"{(12 + lo // 15) % 24} h", "lat_libelle": -52}
                                           for lo in range(-165, 181, 15)],
                                points=[{"lonlat": [-0.128, 51.507], "nom": "Londres (Greenwich)", "style": "capitale", "couleur": ROUGE, "pos": "e"},
                                        {"lonlat": [139.64, 35.44], "nom": "Yokohama", "pos": "w"},
                                        {"lonlat": [-74.0, 40.71], "nom": "New York", "pos": "w"}])},
            {"type": "photo", "src": "assets/images/decors/etape5.jpg", "titre": "L'observatoire royal de Greenwich"},
        ],
    },
}
