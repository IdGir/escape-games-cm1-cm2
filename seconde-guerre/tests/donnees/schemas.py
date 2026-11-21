# -*- coding: utf-8 -*-
"""Schémas SVG du jeu « Radio Londres », tracés par script (jamais par IA) : carte simplifiée de la France coupée en deux (1940),
carte de la Libération (1944), frise 1919-1945, organisation de la Résistance. Aucune image de guerre, aucun symbole nazi."""

POLICE = "font-family='Atkinson Hyperlegible,Arial,sans-serif'"
STYLE = "style='max-width:100%;height:auto;display:block;margin:10px auto'"
FOND, ENCRE = "#f1ede4", "#262a2e"


def repere(x, y, n, couleur="#3b4a5a"):
    return (f"<circle cx='{x}' cy='{y}' r='13' fill='{couleur}' stroke='#fff' stroke-width='2'/>"
            f"<text x='{x}' y='{y + 5}' text-anchor='middle' font-size='14' font-weight='700' fill='#fff' {POLICE}>{n}</text>")


def txt(x, y, s, taille=12, coul=ENCRE, gras=False, ancre="middle", halo=False):
    return (f"<text x='{x}' y='{y}' text-anchor='{ancre}' font-size='{taille}'" + (" font-weight='700'" if gras else "")
            + (" stroke='#fff' stroke-width='3' paint-order='stroke'" if halo else "") + f" fill='{coul}' {POLICE}>{s}</text>")


def cadre(titre, h=360, w=640):
    return [f"<svg viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg' role='img' aria-label=\"{titre}\" {STYLE}>",
            f"<rect width='{w}' height='{h}' rx='12' fill='{FOND}'/>", txt(w / 2, 24, titre, 15, gras=True)]


def pts(l):
    return " ".join(f"{x},{y}" for x, y in l)


COTE_NORD = [(195, 318), (188, 240), (170, 198), (120, 162), (60, 128), (120, 106), (185, 76), (192, 100), (245, 88), (316, 44), (382, 70), (470, 110), (458, 165), (452, 216)]
SUD = [(482, 292), (402, 312), (312, 334)]
LIGNE = [(452, 216), (410, 202), (360, 194), (300, 182), (242, 172), (216, 232), (195, 318)]
VILLES = {"Paris": (300, 122), "Vichy": (338, 228), "Dijon": (396, 172), "Morvan": (362, 180), "Normandie": (200, 92), "Provence": (452, 300), "Lyon": (400, 238)}


def _france(o, zones=True):
    o.append(f"<polygon points='{pts(COTE_NORD + SUD)}' fill='#e7dcc2' stroke='{ENCRE}' stroke-width='2'/>")
    if zones:
        o.append(f"<polygon points='{pts(COTE_NORD + LIGNE[1:-1])}' fill='#b9c2cc' stroke='none'/>")
        o.append(f"<polygon points='{pts(COTE_NORD + SUD)}' fill='none' stroke='{ENCRE}' stroke-width='2'/>")
        o.append(f"<polyline points='{pts(LIGNE)}' fill='none' stroke='#8a2f2a' stroke-width='3' stroke-dasharray='8 5'/>")
    o.append("<path d='M40,60 Q30,30 60,20 L120,30 Q140,50 110,60 Z' fill='#d5dde3' stroke='#7b8792'/>")


CARTE1940 = ["la zone occupée", "la zone non occupée", "la ligne de démarcation", "Paris", "Vichy"]


def carte_1940(n=3, titre="La France coupée en deux (juin 1940, carte simplifiée)", avec_noms=False):
    """Repères : 1 zone occupée, 2 zone non occupée (dite « zone libre »), 3 ligne de démarcation, 4 Paris, 5 Vichy."""
    o = cadre(titre)
    _france(o)
    o.append(txt(85, 45, "Royaume-Uni", 10, "#4a5560"))
    for v in ("Paris", "Vichy"):
        x, y = VILLES[v]
        o.append(f"<circle cx='{x}' cy='{y}' r='5' fill='{ENCRE}'/>")
    pos = [(250, 140), (380, 275), (432, 208), (300, 122), (338, 228)]
    for i in range(n):
        x, y = pos[i]
        o.append(repere(x + (16 if i in (3, 4) else 0), y - (16 if i in (3, 4) else 0), i + 1))
        if avec_noms:
            o.append(txt(x + 34, y - 10, CARTE1940[i], 11, gras=True, ancre="start", halo=True) if i in (3, 4) else txt(x, y + (42 if i == 2 else 28), CARTE1940[i], 11, gras=True, halo=True))
    o.append("<rect x='470' y='320' width='16' height='10' fill='#b9c2cc'/>" + txt(492, 329, "occupée", 10, ancre="start")
             + "<rect x='545' y='320' width='16' height='10' fill='#e7dcc2' stroke='#999'/>" + txt(567, 329, "non occupée", 10, ancre="start"))
    return "".join(o) + "</svg>"


CARTE1944 = ["les plages de Normandie", "Paris", "les côtes de Provence", "Dijon", "les forêts du Morvan"]


def carte_1944(n=3, titre="La Libération de la France (1944, carte simplifiée)", avec_noms=False):
    """Repères : 1 plages de Normandie, 2 Paris, 3 côtes de Provence, 4 Dijon, 5 Morvan."""
    o = cadre(titre)
    _france(o, zones=False)
    o.append(txt(85, 45, "Royaume-Uni", 10, "#4a5560"))
    o.append("<path d='M120,50 Q170,55 195,85' fill='none' stroke='#3b4a5a' stroke-width='2.5' stroke-dasharray='6 4'/>")
    o.append("<path d='M560,340 Q500,330 462,305' fill='none' stroke='#3b4a5a' stroke-width='2.5' stroke-dasharray='6 4'/>")
    for k in ("Paris", "Dijon"):
        x, y = VILLES[k]
        o.append(f"<circle cx='{x}' cy='{y}' r='5' fill='{ENCRE}'/>")
    o.append("<ellipse cx='362' cy='184' rx='18' ry='12' fill='#7d9467' opacity='.8'/>")
    pos = [(200, 92), (300, 122), (452, 300), (396, 172), (362, 184)]
    dec = [(0, -18), (18, -16), (-20, -14), (18, -16), (-20, 16)]
    for i in range(n):
        x, y = pos[i]
        dx, dy = dec[i]
        o.append(repere(x + dx, y + dy, i + 1))
        if avec_noms:
            o.append(txt(x + dx, y + dy + 28, CARTE1944[i], 11, gras=True, halo=True))
    return "".join(o) + "</svg>"


def frise(evts, titre="De la crise à la victoire (1919-1945)", debut=1918, fin=1946):
    """evts : liste de (année décimale, texte court). Les étiquettes alternent au-dessus et au-dessous de l'axe."""
    o = cadre(titre, 220)
    x0, x1, y = 40, 600, 120
    ech = (x1 - x0) / (fin - debut)
    o.append(f"<line x1='{x0}' y1='{y}' x2='{x1}' y2='{y}' stroke='{ENCRE}' stroke-width='3'/>")
    o.append(f"<rect x='{x0 + (1939.67 - debut) * ech:.0f}' y='{y - 8}' width='{(1945.35 - 1939.67) * ech:.0f}' height='16' fill='#8a2f2a' opacity='.25'/>")
    for a in range(1920, fin, 5):
        xa = x0 + (a - debut) * ech
        o.append(f"<line x1='{xa:.0f}' y1='{y - 5}' x2='{xa:.0f}' y2='{y + 5}' stroke='{ENCRE}'/>" + txt(round(xa), y + 20, str(a), 10, "#555"))
    for i, (a, t) in enumerate(evts):
        xa = x0 + (a - debut) * ech
        haut = i % 2 == 0
        yt = y - 30 - (i % 4 // 2) * 22 if haut else y + 44 + (i % 4 // 2) * 22
        o.append(f"<line x1='{xa:.0f}' y1='{y}' x2='{xa:.0f}' y2='{yt + (6 if haut else -12)}' stroke='#3b4a5a' stroke-width='1.5'/>")
        o.append(f"<circle cx='{xa:.0f}' cy='{y}' r='5' fill='#3b4a5a'/>" + txt(round(xa), yt, t, 10, gras=True, halo=True))
    return "".join(o) + "</svg>"


def resistance():
    """Organisation de la Résistance : Londres, CNR, mouvements, réseaux, maquis, radio."""
    o = cadre("Comment la Résistance s'organise (schéma simplifié)", 300)
    boites = [(320, 60, "Londres : de Gaulle et la France libre"), (320, 130, "Jean Moulin et le CNR (27 mai 1943)"),
              (120, 215, "les mouvements et leurs journaux"), (320, 215, "les réseaux de renseignement"), (520, 215, "les maquis")]
    for x, y, t in boites:
        o.append(f"<rect x='{x - 95}' y='{y - 20}' width='190' height='38' rx='8' fill='#fff' stroke='#3b4a5a' stroke-width='2'/>" + txt(x, y + 4, t, 10.5, gras=True))
    o.append("<line x1='320' y1='78' x2='320' y2='110' stroke='#3b4a5a' stroke-width='2.5'/>")
    for x in (120, 320, 520):
        o.append(f"<line x1='320' y1='149' x2='{x}' y2='195' stroke='#3b4a5a' stroke-width='2'/>")
    o.append("<path d='M425,60 Q560,70 560,190' fill='none' stroke='#8a2f2a' stroke-width='2' stroke-dasharray='6 4'/>" + txt(585, 120, "Radio Londres", 10.5, "#8a2f2a", True))
    o.append(txt(320, 275, "Les agentes et agents de liaison relient tous ces groupes.", 11))
    return "".join(o) + "</svg>"
