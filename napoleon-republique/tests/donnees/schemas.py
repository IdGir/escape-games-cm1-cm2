# -*- coding: utf-8 -*-
"""Schémas SVG du jeu « Le Testament de l'Empereur », tracés par script (jamais par IA) : frise 1769-1821, carte simplifiée
de l'Europe napoléonienne, schéma de lecture du tableau du Sacre (David), plan de Paris impérial, place d'une commune
(lieux de la République). Aucune scène de combat."""

POLICE = "font-family='Atkinson Hyperlegible,Arial,sans-serif'"
STYLE = "style='max-width:100%;height:auto;display:block;margin:10px auto'"
FOND, ENCRE, BLEU, OR, ROUGE = "#f3eee2", "#262a2e", "#2f4a7a", "#b08a2e", "#9a2f2a"


def repere(x, y, n, couleur=BLEU):
    return (f"<circle cx='{x}' cy='{y}' r='13' fill='{couleur}' stroke='#fff' stroke-width='2'/>"
            f"<text x='{x}' y='{y + 5}' text-anchor='middle' font-size='14' font-weight='700' fill='#fff' {POLICE}>{n}</text>")


def txt(x, y, s, taille=12, coul=ENCRE, gras=False, ancre="middle", halo=False):
    return (f"<text x='{x}' y='{y}' text-anchor='{ancre}' font-size='{taille}'" + (" font-weight='700'" if gras else "")
            + (" stroke='#fff' stroke-width='3' paint-order='stroke'" if halo else "") + f" fill='{coul}' {POLICE}>{s}</text>")


def cadre(titre, h=360, w=640):
    return [f"<svg viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg' role='img' aria-label=\"{titre}\" {STYLE}>",
            f"<rect width='{w}' height='{h}' rx='12' fill='{FOND}'/>", txt(w / 2, 24, titre, 15, gras=True)]


def pts(l):
    return " ".join(f"{x:.0f},{y:.0f}" for x, y in l)


def _xy(lon, lat):
    return 30 + (lon + 10) * 11.6, 340 - (lat - 36) * 12.5


CONTINENT = [(-9, 37), (-9, 43.5), (-1.5, 43.5), (-4.5, 48.5), (2.6, 51), (8, 54), (10, 57.5), (12, 54.2), (21, 55), (24, 59.5), (30, 60), (40, 60),
             (40, 45), (34, 45), (28, 44), (26, 40.5), (23, 37.5), (20, 40), (13.5, 45.5), (12.5, 44), (15.5, 40), (16, 38), (12, 41.5), (8.5, 44.3),
             (3, 43.3), (0, 40), (-2, 36.8)]
BRETAGNE = [(-5, 50), (1, 51.2), (0.5, 53), (-3, 58.5), (-5.5, 57), (-3, 54.5), (-5, 52.5)]
LIEUX = {"Paris": (2.35, 48.85), "Austerlitz": (16.76, 49.15), "Moscou": (37.6, 55.75), "Iéna": (11.6, 50.9), "Waterloo": (4.4, 50.7),
         "Londres": (-0.1, 51.5), "Rome": (12.5, 41.9), "Vienne": (16.37, 48.2), "Ajaccio": (8.74, 41.92), "Toulon": (5.93, 43.12)}
CARTE_EUROPE = ["Paris", "Austerlitz", "Moscou", "Iéna", "Waterloo"]


def carte_europe(n=3, titre="L'Europe de Napoléon (carte simplifiée)", avec_noms=False):
    """Repères : 1 Paris, 2 Austerlitz, 3 Moscou, 4 Iéna, 5 Waterloo (Londres, Rome, Vienne non numérotées)."""
    o = cadre(titre)
    o.append(f"<rect x='12' y='34' width='616' height='314' rx='8' fill='#cfdde6'/>")
    o.append(f"<polygon points='{pts([_xy(*p) for p in CONTINENT])}' fill='#e8dcc0' stroke='{ENCRE}' stroke-width='1.5'/>")
    o.append(f"<polygon points='{pts([_xy(*p) for p in BRETAGNE])}' fill='#e8dcc0' stroke='{ENCRE}' stroke-width='1.5'/>")
    x, y = _xy(9, 42.1)
    o.append(f"<ellipse cx='{x:.0f}' cy='{y:.0f}' rx='5' ry='11' fill='#e8dcc0' stroke='{ENCRE}'/>")
    o.append(txt(70, 230, "océan", 10, "#4a6070") + txt(70, 243, "Atlantique", 10, "#4a6070") + txt(240, 300, "mer Méditerranée", 10, "#4a6070"))
    o.append(f"<rect x='22' y='300' width='150' height='40' rx='6' fill='#fff' stroke='{ENCRE}' stroke-dasharray='4 3'/>"
             + txt(97, 316, "Sainte-Hélène : une île", 9.5) + txt(97, 330, "très loin au sud, dans l'Atlantique", 9.5))
    for i in range(n):
        lx, ly = _xy(*LIEUX[CARTE_EUROPE[i]])
        o.append(f"<circle cx='{lx:.0f}' cy='{ly:.0f}' r='4' fill='{ENCRE}'/>")
        dx, dy = [(-18, 18), (16, 14), (-16, 16), (0, -20), (6, -22)][i]
        o.append(repere(round(lx + dx), round(ly + dy), i + 1))
        if avec_noms:
            o.append(txt(round(lx + dx), round(ly + dy + 27), CARTE_EUROPE[i], 11, gras=True, halo=True))
    for v in ("Londres", "Rome", "Vienne"):
        lx, ly = _xy(*LIEUX[v])
        o.append(f"<circle cx='{lx:.0f}' cy='{ly:.0f}' r='3' fill='#6b6b6b'/>")
    return "".join(o) + "</svg>"


SACRE = ["Napoléon", "Joséphine", "le pape Pie VII", "la couronne de l'impératrice", "la tribune de la famille"]


def sacre(n=3, titre="Le Sacre, d'après le tableau de David (schéma simplifié)", avec_noms=False):
    """Repères : 1 Napoléon debout, 2 Joséphine à genoux, 3 le pape assis, 4 la couronne, 5 la tribune."""
    o = cadre(titre)
    o.append("<rect x='30' y='40' width='580' height='300' rx='6' fill='#e9dfc9' stroke='#8a7550'/>")
    for x in (70, 170, 470, 570):
        o.append(f"<rect x='{x - 12}' y='44' width='24' height='290' fill='#d8caa8'/>")
    o.append(f"<rect x='250' y='60' width='150' height='55' rx='4' fill='#cdb98f' stroke='#8a7550'/>")
    for x in (275, 300, 325, 350, 375):
        o.append(f"<circle cx='{x}' cy='80' r='7' fill='#a58c63'/><rect x='{x - 7}' y='87' width='14' height='18' fill='#a58c63'/>")
    o.append(f"<rect x='480' y='170' width='90' height='80' fill='#c9b78e' stroke='#8a7550'/><line x1='525' y1='130' x2='525' y2='170' stroke='{OR}' stroke-width='5'/>"
             f"<line x1='510' y1='142' x2='540' y2='142' stroke='{OR}' stroke-width='5'/>")
    o.append(f"<rect x='60' y='290' width='520' height='30' fill='#bda97f'/><rect x='200' y='265' width='300' height='25' fill='#c8b48a'/>")
    for x in (80, 110, 140, 170):
        o.append(f"<circle cx='{x}' cy='190' r='10' fill='#8f7a5a'/><rect x='{x - 12}' y='200' width='24' height='60' rx='6' fill='#7a5f45'/>")
    # Napoléon debout, la couronne levée
    o.append(f"<circle cx='330' cy='160' r='14' fill='#e7c7a6'/><path d='M300,175 L360,175 L380,265 L280,265 Z' fill='{ROUGE}'/>"
             f"<line x1='318' y1='180' x2='300' y2='150' stroke='#e7c7a6' stroke-width='6'/><line x1='342' y1='180' x2='300' y2='150' stroke='#e7c7a6' stroke-width='6'/>")
    o.append(f"<ellipse cx='296' cy='146' rx='13' ry='6' fill='none' stroke='{OR}' stroke-width='4'/>")
    # Joséphine à genoux
    o.append(f"<circle cx='250' cy='215' r='12' fill='#efd2b6'/><path d='M228,228 L272,228 L285,268 L215,268 Z' fill='#f6f1e7' stroke='#999'/>")
    # le pape assis
    o.append(f"<circle cx='420' cy='175' r='12' fill='#e2bf9e'/><rect x='402' y='188' width='36' height='60' rx='6' fill='#fbfbf7' stroke='#999'/>"
             f"<rect x='396' y='245' width='48' height='14' fill='#8a7550'/>")
    pos = [(392, 205), (222, 196), (452, 160), (296, 122), (325, 54)]
    for i in range(n):
        x, y = pos[i]
        o.append(repere(x, y, i + 1))
        if avec_noms:
            o.append(txt(x, y + (-18 if i == 4 else 28), SACRE[i], 11, gras=True, halo=True))
    return "".join(o) + "</svg>"


def paris():
    """Plan de Paris simplifié : monuments de l'Empire (schéma de la leçon 4)."""
    o = cadre("Paris : les monuments de l'Empire (plan simplifié)")
    o.append("<path d='M20,250 C140,230 200,170 300,175 C400,180 450,230 620,200' fill='none' stroke='#8fb3cf' stroke-width='18'/>")
    o.append(txt(560, 232, "la Seine", 11, "#3e6787", True))
    o.append("<ellipse cx='420' cy='196' rx='26' ry='9' fill='#e8dcc0' stroke='#8fb3cf'/>")
    lieux = [(110, 120, "l'Arc de triomphe de l'Étoile"), (290, 115, "la colonne Vendôme"), (350, 155, "l'Arc du Carrousel (Louvre)"),
             (420, 196, "Notre-Dame"), (230, 255, "les Invalides : le tombeau")]
    for x, y, t in lieux:
        o.append(f"<rect x='{x - 7}' y='{y - 7}' width='14' height='14' fill='{OR}' stroke='{ENCRE}'/>" + txt(x, y - 14, t, 11, gras=True, halo=True))
    o.append(txt(320, 335, "Schéma sans échelle : les distances ne sont pas exactes.", 10, "#555"))
    return "".join(o) + "</svg>"


PLACE = ["la mairie", "l'école", "le monument aux morts", "la devise au fronton de la mairie", "le drapeau tricolore"]


def place(n=3, titre="La place de la commune : des lieux de la République", avec_noms=False):
    """Repères : 1 mairie, 2 école, 3 monument aux morts, 4 devise au fronton, 5 drapeau."""
    o = cadre(titre)
    o.append("<rect x='20' y='275' width='600' height='70' fill='#d9d2c3'/>")
    # mairie
    o.append(f"<rect x='230' y='130' width='180' height='145' fill='#efe7d6' stroke='{ENCRE}'/><polygon points='220,130 320,85 420,130' fill='#e2d6bd' stroke='{ENCRE}'/>"
             f"<rect x='255' y='112' width='130' height='14' fill='#fff' stroke='#777'/><line x1='265' y1='119' x2='375' y2='119' stroke='#999' stroke-width='3' stroke-dasharray='14 6'/>"
             f"<rect x='300' y='220' width='40' height='55' fill='#7a5f45'/>")
    for x in (250, 360):
        o.append(f"<rect x='{x}' y='160' width='30' height='40' fill='#bcd0dc' stroke='#777'/>")
    o.append(f"<line x1='320' y1='85' x2='320' y2='45' stroke='{ENCRE}' stroke-width='2'/>"
             f"<rect x='321' y='46' width='10' height='18' fill='{BLEU}'/><rect x='331' y='46' width='10' height='18' fill='#fff' stroke='#ccc'/><rect x='341' y='46' width='10' height='18' fill='{ROUGE}'/>")
    # école
    o.append(f"<rect x='460' y='170' width='140' height='105' fill='#f2ecdf' stroke='{ENCRE}'/><polygon points='452,170 530,140 608,170' fill='#e2d6bd' stroke='{ENCRE}'/>"
             f"<rect x='475' y='195' width='30' height='30' fill='#bcd0dc'/><rect x='555' y='195' width='30' height='30' fill='#bcd0dc'/><rect x='515' y='225' width='30' height='50' fill='#7a5f45'/>")
    # monument aux morts
    o.append(f"<rect x='95' y='235' width='70' height='18' fill='#b8b2a6'/><rect x='112' y='160' width='36' height='75' fill='#c9c3b7' stroke='#777'/>"
             f"<polygon points='112,160 130,140 148,160' fill='#c9c3b7' stroke='#777'/>")
    pos = [(250, 255), (500, 260), (130, 205), (225, 112), (360, 55)]
    for i in range(n):
        x, y = pos[i]
        o.append(repere(x, y, i + 1))
        if avec_noms:
            o.append(txt(x, y + 28 if i not in (3, 4) else y - 17, PLACE[i], 11, gras=True, halo=True))
    return "".join(o) + "</svg>"


def frise(evts, titre="La vie de Napoléon Bonaparte (1769-1821)", debut=1765, fin=1825, bande=(1804.4, 1815.5), pas=5):
    """evts : liste de (année décimale, texte court). La bande colorée marque l'Empire (1804-1815)."""
    o = cadre(titre, 230)
    x0, x1, y = 40, 600, 125
    ech = (x1 - x0) / (fin - debut)
    o.append(f"<line x1='{x0}' y1='{y}' x2='{x1}' y2='{y}' stroke='{ENCRE}' stroke-width='3'/>")
    if bande:
        o.append(f"<rect x='{x0 + (bande[0] - debut) * ech:.0f}' y='{y - 8}' width='{(bande[1] - bande[0]) * ech:.0f}' height='16' fill='{OR}' opacity='.35'/>")
    a = debut - debut % pas + pas
    while a < fin:
        xa = x0 + (a - debut) * ech
        o.append(f"<line x1='{xa:.0f}' y1='{y - 5}' x2='{xa:.0f}' y2='{y + 5}' stroke='{ENCRE}'/>" + txt(round(xa), y + 20, str(a), 10, "#555"))
        a += pas
    for i, (an, t) in enumerate(evts):
        xa = x0 + (an - debut) * ech
        haut = i % 2 == 0
        yt = y - 30 - (i % 4 // 2) * 24 if haut else y + 46 + (i % 4 // 2) * 24
        o.append(f"<line x1='{xa:.0f}' y1='{y}' x2='{xa:.0f}' y2='{yt + (6 if haut else -12)}' stroke='{BLEU}' stroke-width='1.5'/>")
        o.append(f"<circle cx='{xa:.0f}' cy='{y}' r='5' fill='{BLEU}'/>" + txt(round(xa), yt, t, 10, gras=True, halo=True))
    return "".join(o) + "</svg>"
