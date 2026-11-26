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
