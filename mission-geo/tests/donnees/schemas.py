# -*- coding: utf-8 -*-
"""Cartes et schémas SVG de la version immersive de « Mission géographique », tracés par script (jamais par IA).

Les fonds viennent de mission-geo/js/cartes.js (le même dessin que la version classique), lu par Node ;
on y ajoute des repères numérotés placés en POURCENTAGE de la boîte (les coordonnées des séances du livret).
"""
import json, os, re, subprocess

ICI = os.path.dirname(os.path.abspath(__file__))
CARTES_JS = os.path.join(ICI, "..", "..", "js", "cartes.js")
POLICE = "font-family='Atkinson Hyperlegible,Arial,sans-serif'"
STYLE = "style='max-width:100%;height:auto;display:block;margin:10px auto;border-radius:10px'"
_CACHE = {}


def fond(nom):
    """SVG d'un décor de cartes.js (« planisphere-muet », « france-regions », « village-aerien »…)."""
    if nom not in _CACHE:
        code = ("const fs=require('fs'),vm=require('vm');const c={};vm.createContext(c);"
                f"vm.runInContext(fs.readFileSync({json.dumps(CARTES_JS)},'utf8')+';this.CARTES=CARTES',c);"
                f"process.stdout.write(c.CARTES.decor({json.dumps(nom)})||'')")
        s = subprocess.run(["node", "-e", code], capture_output=True, text=True, encoding="utf-8", check=True).stdout
        if not s.startswith("<svg"):
            raise SystemExit(f"Décor introuvable dans cartes.js : {nom}")
        _CACHE[nom] = s
    return _CACHE[nom]


def _boite(svg):
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg)
    return int(m.group(1)), int(m.group(2))


def repere(x, y, n, r=15, couleur="#7a1f2b"):
    return (f"<circle cx='{x:.0f}' cy='{y:.0f}' r='{r}' fill='{couleur}' stroke='#fff' stroke-width='3'/>"
            f"<text x='{x:.0f}' y='{y + 6:.0f}' text-anchor='middle' font-size='{r + 3}' font-weight='700' fill='#fff' {POLICE}>{n}</text>")


def avec_reperes(nom, points, titre, mots=None, r=None):
    """Fond `nom` + repères 1, 2, 3… aux positions (x %, y %) ; `mots` : légende écrite à côté (schémas des leçons)."""
    s = fond(nom)
    w, h = _boite(s)
    o = []
    for i, (x, y) in enumerate(points, 1):
        X, Y = x * w / 100, y * h / 100
        o.append(repere(X, Y, i, r=r or max(13, round(w / 55))))
        if mots:
            o.append(f"<text x='{X + 20:.0f}' y='{Y + 5:.0f}' font-size='{max(12, round(w / 60))}' font-weight='700' fill='#1b2a3a' "
                     f"stroke='#fff' stroke-width='4' paint-order='stroke' {POLICE}>{mots[i - 1]}</text>")
    s = s.replace('style="width:100%;height:auto;background:#dceaf6"', STYLE + f' aria-label="{titre}"', 1)
    return s.replace("</svg>", "".join(o) + "</svg>")


def regions(titre="Les 13 régions de France métropolitaine (numérotées)"):
    """La carte des régions de cartes.js porte déjà ses numéros 1 à 13."""
    s = fond("france-regions")
    return s.replace('style="width:100%;height:auto;background:#dceaf6"', STYLE + f' aria-label="{titre}"', 1)


# ---------------------------------------------------------------- positions du livret (en %)
CONTINENTS = [("Amérique du Nord", 18, 26), ("Amérique du Sud", 33, 63), ("Europe", 54, 20), ("Afrique", 54.5, 53),
              ("Asie", 80, 28), ("Océanie", 86.5, 64), ("Antarctique", 50, 94)]
REGIONS = ["Bretagne", "Pays de la Loire", "Normandie", "Hauts-de-France", "Grand Est", "Île-de-France", "Centre-Val de Loire",
           "Bourgogne-Franche-Comté", "Auvergne-Rhône-Alpes", "Nouvelle-Aquitaine", "Occitanie", "Provence-Alpes-Côte d'Azur", "Corse"]
VILLAGE = [("L'église", 47, 40), ("Le centre-bourg", 47, 48), ("Le lotissement", 24, 62), ("Un commerce", 52, 52),
           ("La mairie", 41, 46), ("Un champ", 16, 17), ("La route principale", 80, 52)]
BESANCON = [("Le parc technologique", 24, 25), ("Le centre-ville", 74, 22), ("Le centre commercial", 22, 72), ("Le CHU (hôpital)", 50, 68),
            ("Le quartier d'affaires", 80, 66)]


def planisphere(idx, titre="Le planisphère du Professeur Atlas"):
    return avec_reperes("planisphere-muet", [(x, y) for _, x, y in [CONTINENTS[i] for i in idx]], titre)


def village(idx, titre="Le bourg vu du ciel"):
    return avec_reperes("village-aerien", [(x, y) for _, x, y in [VILLAGE[i] for i in idx]], titre, r=11)


def ville(idx, titre="Les quartiers de la ville, vus du ciel (schéma)"):
    return avec_reperes("village-aerien", [(x, y) for _, x, y in [BESANCON[i] for i in idx]], titre)


def densites(titre="Trois espaces vus du dessus (1 carreau = 1 km sur 1 km)"):
    """Les espaces A, B, C du livret : carrés quadrillés en km, habitants figurés par des points."""
    o = [f"<svg viewBox='0 0 640 215' xmlns='http://www.w3.org/2000/svg' role='img' aria-label=\"{titre}\" {STYLE}>",
         "<rect width='640' height='215' rx='12' fill='#f4efe4'/>",
         f"<text x='320' y='26' text-anchor='middle' font-size='15' font-weight='700' fill='#1b2a3a' {POLICE}>{titre}</text>"]
    def espace(x, nom, cotes, habitants):
        u = 70
        for i in range(cotes):
            for j in range(cotes):
                o.append(f"<rect x='{x + i * u}' y='{60 + j * u}' width='{u}' height='{u}' fill='#dfe9cf' stroke='#6b7a4e' stroke-width='1.5'/>")
        for k, (px, py) in enumerate(habitants):
            o.append(f"<circle cx='{x + px}' cy='{60 + py}' r='7' fill='#7a1f2b'/>")
        o.append(f"<text x='{x + cotes * u / 2:.0f}' y='52' text-anchor='middle' font-size='15' font-weight='700' fill='#1b2a3a' {POLICE}>Espace {nom}</text>")
    espace(40, "A", 1, [(22, 30), (48, 44)])
    espace(180, "B", 1, [(18, 20), (50, 22), (24, 52), (52, 50)])
    espace(330, "C", 2, [(30, 30), (110, 40), (40, 110), (112, 104)])
    o.append(f"<text x='560' y='120' text-anchor='middle' font-size='13' fill='#1b2a3a' {POLICE}>● = 1 habitant</text>")
    o.append(f"<text x='560' y='142' text-anchor='middle' font-size='13' fill='#1b2a3a' {POLICE}>□ = 1 km²</text>")
    o.append("</svg>")
    return "".join(o)


# ---------------------------------------------------------------- période 2 (séances 6 à 8)
MERS = [("La mer du Nord", 58, 5), ("La Manche", 30, 11), ("L'océan Atlantique", 11, 55), ("La mer Méditerranée", 68, 91),
        ("Étretat", 38, 15), ("Biarritz", 26, 74), ("Marseille", 65, 75)]
PAYS = [("Les États-Unis", 20, 30), ("La Norvège", 56, 15), ("Le Tchad", 56, 44), ("Le Bangladesh", 76, 43), ("L'Australie", 87, 64),
        ("Le Mali", 49.5, 44.5), ("Le Japon", 93.5, 20)]
# PNUD, Rapport sur le développement humain 2025 (données 2023) : revenu national brut par habitant (dollars PPA 2021),
# espérance de vie à la naissance (années), durée attendue de scolarisation (années).
PNUD = {"la Norvège": (112710, 83.3, 18.8), "les États-Unis": (73650, 79.3, 15.9), "l'Australie": (58277, 83.9, 20.7),
        "le Koweït": (56612, 80.4, 15.9), "la France": (55060, 83.3, 16.1), "le Japon": (47775, 84.7, 15.5),
        "la Guinée équatoriale": (12762, 63.7, 12.5), "le Bangladesh": (8498, 74.7, 12.3), "Haïti": (2935, 64.9, 10.9),
        "le Mali": (2342, 60.4, 7.0), "le Tchad": (1748, 55.1, 8.3), "Madagascar": (1656, 63.6, 9.1)}
SOURCE_PNUD = "PNUD, Rapport sur le développement humain 2025 (données 2023)"


def mers(idx, titre="La France et les mers qui la bordent"):
    return avec_reperes("france-mers", [(x, y) for _, x, y in [MERS[i] for i in idx]], titre, r=14)


def pays(idx, titre="Le planisphère de Nour"):
    return avec_reperes("planisphere-muet", [(x, y) for _, x, y in [PAYS[i] for i in idx]], titre, r=14)


def nombre(n):
    return f"{n:,}".replace(",", " ") if isinstance(n, int) else str(n).replace(".", ",")


def revenus(noms, titre="Revenu moyen par habitant en 2023 (en dollars)"):
    """Diagramme en barres horizontales tracé par script, chiffres du PNUD."""
    h = 46 + 30 * len(noms) + 28
    mx = max(PNUD[n][0] for n in noms)
    o = [f"<svg viewBox='0 0 640 {h}' xmlns='http://www.w3.org/2000/svg' role='img' aria-label=\"{titre}\" {STYLE}>",
         f"<rect width='640' height='{h}' rx='12' fill='#f4efe4'/>",
         f"<text x='320' y='26' text-anchor='middle' font-size='15' font-weight='700' fill='#1b2a3a' {POLICE}>{titre}</text>"]
    for i, n in enumerate(sorted(noms, key=lambda k: -PNUD[k][0])):
        y = 46 + 30 * i
        w = max(4, round(PNUD[n][0] / mx * 330))
        nom = n[0].upper() + n[1:]
        o.append(f"<text x='176' y='{y + 15}' text-anchor='end' font-size='14' fill='#1b2a3a' {POLICE}>{nom}</text>")
        o.append(f"<rect x='186' y='{y}' width='{w}' height='20' rx='4' fill='#1d3b5c'/>")
        o.append(f"<text x='{192 + w}' y='{y + 15}' font-size='13' font-weight='700' fill='#1b2a3a' {POLICE}>{nombre(PNUD[n][0])} $</text>")
    o.append(f"<text x='320' y='{h - 10}' text-anchor='middle' font-size='11' font-style='italic' fill='#4b3a2c' {POLICE}>Source : {SOURCE_PNUD}</text>")
    o.append("</svg>")
    return "".join(o)


def tableau_pnud(noms, titre="Trois indicateurs du développement (2023)"):
    """Tableau HTML : revenu, espérance de vie, durée de scolarisation."""
    th = "".join(f"<th>{n[0].upper() + n[1:]}</th>" for n in noms)
    lignes = [("Revenu par habitant", lambda v: nombre(v[0]) + " $"), ("Espérance de vie", lambda v: nombre(v[1]) + " ans"),
              ("Durée de scolarisation", lambda v: nombre(v[2]) + " ans")]
    tr = "".join(f"<tr><th>{t}</th>" + "".join(f"<td>{f(PNUD[n])}</td>" for n in noms) + "</tr>" for t, f in lignes)
    return (f'<div class="doc-titre"><i>{titre}</i></div><table class="tableau-releves"><tr><th></th>{th}</tr>{tr}</table>'
            f'<p style="font-size:.85em"><i>Source : {SOURCE_PNUD}.</i></p>')


# ---------------------------------------------------------------- périodes 3 et 4 (séances 9 à 13)
# Repères de la carte « france-fleuves » (mêmes positions, en %, que la version classique) : 5 fleuves, 5 massifs, la Corse.
FLEUVES = [("La Seine", 50.3, 24.2), ("La Loire", 39.7, 38.1), ("La Garonne", 32.3, 63.5), ("Le Rhône", 66.5, 63.5), ("Le Rhin", 89.7, 23.1),
           ("Les Alpes", 76.5, 61.2), ("Les Pyrénées", 39.7, 81.5), ("Le Massif central", 52.9, 61.2), ("Le Jura", 72.9, 46.2), ("Les Vosges", 78.4, 34.2),
           ("La Corse", 93.5, 90.4)]
# Pays de la séance 9 sur le planisphère muet (en %).
PAYS9 = [("La France", 52.5, 22), ("Les États-Unis", 20, 30), ("Haïti", 29, 37), ("Le Tchad", 56, 44), ("Le Mali", 49.5, 44.5)]


def fleuves(idx, titre="La France : fleuves et massifs (repères numérotés)"):
    return avec_reperes("france-fleuves", [(x, y) for _, x, y in [FLEUVES[i] for i in idx]], titre, r=13)


def pays9(idx, titre="Le planisphère d'Aminata"):
    return avec_reperes("planisphere-muet", [(x, y) for _, x, y in [PAYS9[i] for i in idx]], titre, r=14)
