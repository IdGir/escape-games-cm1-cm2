# -*- coding: utf-8 -*-
"""Schémas SVG du jeu « Les Lettres du poilu », tracés par script (jamais par IA) : coupe d'une tranchée, monument aux morts,
frise 1914-1922, deux alliances de 1914, le front et l'arrière. Aucun détail violent."""

POLICE = "font-family='Atkinson Hyperlegible,Arial,sans-serif'"
STYLE = "style='max-width:100%;height:auto;display:block;margin:10px auto'"
FOND, ENCRE = "#f3efe6", "#2a2620"


def repere(x, y, n, couleur="#3d4f6b"):
    return (f"<circle cx='{x}' cy='{y}' r='13' fill='{couleur}' stroke='#fff' stroke-width='2'/>"
            f"<text x='{x}' y='{y + 5}' text-anchor='middle' font-size='14' font-weight='700' fill='#fff' {POLICE}>{n}</text>")


def txt(x, y, s, taille=12, coul=ENCRE, gras=False, ancre="middle", halo=False):
    return (f"<text x='{x}' y='{y}' text-anchor='{ancre}' font-size='{taille}'" + (" font-weight='700'" if gras else "")
            + (" stroke='#fff' stroke-width='3' paint-order='stroke'" if halo else "") + f" fill='{coul}' {POLICE}>{s}</text>")


def cadre(titre, h=300, w=640):
    return [f"<svg viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg' role='img' aria-label=\"{titre}\" {STYLE}>",
            f"<rect width='{w}' height='{h}' rx='12' fill='{FOND}'/>", txt(w / 2, 24, titre, 15, gras=True)]


def fleche(x1, y1, x2, y2, coul=ENCRE):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - 10 * math.cos(a), y2 - 10 * math.sin(a)
    p1 = (bx + 6 * math.sin(a), by - 6 * math.cos(a))
    p2 = (bx - 6 * math.sin(a), by + 6 * math.cos(a))
    return (f"<line x1='{x1:.0f}' y1='{y1:.0f}' x2='{bx:.0f}' y2='{by:.0f}' stroke='{coul}' stroke-width='2.5'/>"
            f"<polygon points='{x2:.0f},{y2:.0f} {p1[0]:.0f},{p1[1]:.0f} {p2[0]:.0f},{p2[1]:.0f}' fill='{coul}'/>")


TRANCHEE = ["les sacs de sable", "les barbelés", "l'abri", "la banquette de tir", "le no man's land"]


def tranchee(n=3, titre="Coupe d'une tranchée (schéma simplifié)", avec_noms=False):
    """Repères : 1 sacs de sable, 2 barbelés, 3 abri, 4 banquette de tir, 5 no man's land."""
    o = cadre(titre, 300)
    o += ["<rect x='20' y='60' width='600' height='60' fill='#cfe0ea'/>", "<rect x='270' y='118' width='140' height='115' fill='#c9b48a'/>",
          "<path d='M20,120 L250,120 L250,130 L280,130 L280,230 L400,230 L400,120 L620,120 L620,285 L20,285 Z' fill='#8b6f4e'/>",
          "<rect x='280' y='200' width='120' height='30' fill='#6d5338'/>",
          "<rect x='280' y='178' width='34' height='22' fill='#a08560' stroke='#5a4630'/>",
          "<rect x='300' y='238' width='90' height='36' rx='4' fill='#3e3226' stroke='#2a2620'/>",
          "<path d='M318,238 l0,-8 l54,0 l0,8' fill='none' stroke='#2a2620' stroke-width='3'/>"]
    for i in range(5):
        o.append(f"<ellipse cx='{262 + (i % 2) * 6}' cy='{116 - i * 9}' rx='16' ry='6' fill='#c9b48a' stroke='#6d5a3a'/>")
    for x in (120, 160, 200):
        o.append(f"<path d='M{x},120 l0,-26 M{x - 14},106 l28,0 M{x - 14},98 l28,0' stroke='#555' stroke-width='2'/>")
        o.append(f"<path d='M{x - 20},102 q10,-8 20,0 q10,8 20,0' stroke='#777' stroke-width='1.5' fill='none'/>")
    o.append(txt(110, 140, "côté ennemi", 11, "#f3efe6"))
    o.append(txt(520, 140, "côté de l'arrière", 11, "#f3efe6"))
    pos = [(262, 62), (165, 72), (345, 262), (297, 170), (60, 100)]
    lbl = [(282, 58, "start"), (165, 52, "middle"), (365, 266, "start"), (420, 175, "start"), (60, 80, "middle")]
    for i in range(n):
        o.append(repere(*pos[i], i + 1))
        if avec_noms:
            o.append(txt(lbl[i][0], lbl[i][1], TRANCHEE[i], 11, gras=True, ancre=lbl[i][2], halo=True))
    return "".join(o) + "</svg>"


MONUMENT = ["la statue du poilu", "la liste des noms", "les dates de la guerre", "la croix de guerre", "la gerbe de fleurs"]


def monument(n=3, titre="Le monument aux morts de Vaux-les-Tilleuls", avec_noms=False):
    """Repères : 1 statue, 2 liste des noms, 3 dates, 4 croix de guerre, 5 gerbe."""
    o = cadre(titre, 320)
    o += ["<rect x='220' y='270' width='200' height='20' fill='#b9b2a3'/>",
          "<rect x='250' y='130' width='140' height='140' fill='#d8d2c4' stroke='#8e877a' stroke-width='2'/>",
          "<rect x='240' y='118' width='160' height='14' fill='#c4bdae'/>",
          "<circle cx='320' cy='62' r='12' fill='#9aa0a6'/>",
          "<path d='M308,58 q12,-14 24,0 z' fill='#7d848b'/>",
          "<path d='M306,76 l28,0 l6,42 l-40,0 z' fill='#9aa0a6'/>",
          "<path d='M334,80 l14,-30' stroke='#7d848b' stroke-width='4'/>",
          txt(320, 150, "1914 - 1918", 13, gras=True)]
    for k in range(6):
        o.append(f"<rect x='272' y='{166 + k * 14}' width='96' height='5' rx='2' fill='#8e877a'/>")
    o += ["<path d='M215,130 l10,-10 l10,10 l-10,10 z' fill='#8a6d2b' stroke='#5a4620'/>",
          "<rect x='222' y='100' width='6' height='20' fill='#2e5a8a'/><rect x='228' y='100' width='6' height='20' fill='#b23a3a'/>",
          "<ellipse cx='320' cy='282' rx='46' ry='12' fill='#4e7d3a'/>",
          "<circle cx='296' cy='278' r='6' fill='#c0392b'/><circle cx='320' cy='274' r='6' fill='#e8e2d0'/><circle cx='344' cy='278' r='6' fill='#2e5a8a'/>"]
    pos = [(360, 60), (410, 200), (230, 150), (196, 120), (400, 290)]
    for i in range(n):
        o.append(repere(*pos[i], i + 1))
        if avec_noms:
            o.append(txt(pos[i][0] + (18 if pos[i][0] > 300 else -18), pos[i][1] + 5, MONUMENT[i], 11, gras=True,
                         ancre="start" if pos[i][0] > 300 else "end"))
    return "".join(o) + "</svg>"


def frise(titre="De 1914 à 1922"):
    o = cadre(titre, 250, 680)
    x0, x1, a0, a1 = 50, 640, 1914, 1923
    o.append(f"<rect x='{x0}' y='120' width='{x1 - x0}' height='12' rx='6' fill='#8e877a'/>")
    o.append(f"<rect x='{x0 + (1914.59 - a0) / (a1 - a0) * (x1 - x0):.0f}' y='120' width='{(1918.86 - 1914.59) / (a1 - a0) * (x1 - x0):.0f}' height='12' fill='#b23a3a' opacity='.75'/>")
    for a in range(a0, a1 + 1):
        x = x0 + (a - a0) / (a1 - a0) * (x1 - x0)
        o.append(f"<line x1='{x:.0f}' y1='114' x2='{x:.0f}' y2='138' stroke='{ENCRE}'/>")
        o.append(txt(x, 152, str(a), 11))
    ev = [(1914.49, "28 juin 1914 : Sarajevo", 60), (1914.59, "3 août 1914 : la guerre", 180), (1916.14, "1916 : Verdun, la Somme", 82),
          (1917.27, "avril 1917 : les États-Unis", 204), (1918.86, "11 novembre 1918 : armistice", 60), (1919.49, "28 juin 1919 : traité de Versailles", 180),
          (1920.86, "1920 : Soldat inconnu", 82), (1922.81, "1922 : 11 novembre férié", 204)]
    for a, s, y in ev:
        x = x0 + (a - a0) / (a1 - a0) * (x1 - x0)
        haut = y < 100
        o.append(f"<line x1='{x:.0f}' y1='{(y + 5) if haut else (y - 13)}' x2='{x:.0f}' y2='{116 if haut else 136}' stroke='#3d4f6b' stroke-dasharray='3 2'/>")
        o.append(txt(min(max(x, 80), 600), y, s, 11, "#3d4f6b", True))
    o.append(txt(340, 238, "En rouge : les combats (pour la France, du 3 août 1914 au 11 novembre 1918)", 11))
    return "".join(o) + "</svg>"


def camps(titre="Deux alliances face à face en 1914"):
    o = cadre(titre, 230)
    o += ["<rect x='30' y='50' width='270' height='150' rx='10' fill='#dfe7f1' stroke='#3d4f6b' stroke-width='2'/>",
          "<rect x='340' y='50' width='270' height='150' rx='10' fill='#efe0d6' stroke='#8a4b2b' stroke-width='2'/>",
          txt(165, 76, "La Triple-Entente", 14, "#3d4f6b", True), txt(475, 76, "L'Allemagne et ses alliés", 14, "#8a4b2b", True)]
    for i, p in enumerate(["la France", "le Royaume-Uni", "la Russie"]):
        o.append(txt(165, 108 + i * 28, p, 13))
    for i, p in enumerate(["l'Allemagne", "l'Autriche-Hongrie"]):
        o.append(txt(475, 108 + i * 28, p, 13))
    o.append(fleche(305, 125, 335, 125, "#2a2620"))
    o.append(fleche(335, 140, 305, 140, "#2a2620"))
    o.append(txt(320, 222, "D'autres pays rejoignent ensuite les deux camps (Italie 1915, États-Unis 1917…).", 11))
    return "".join(o) + "</svg>"


def front_arriere(titre="Le front et l'arrière"):
    o = cadre(titre, 240)
    o += ["<rect x='30' y='50' width='220' height='160' rx='10' fill='#e6dccb' stroke='#6d5338' stroke-width='2'/>",
          "<rect x='390' y='50' width='220' height='160' rx='10' fill='#dde9dc' stroke='#3f6b3a' stroke-width='2'/>",
          txt(140, 76, "LE FRONT", 14, "#6d5338", True), txt(500, 76, "L'ARRIÈRE", 14, "#3f6b3a", True),
          txt(140, 110, "les soldats", 12), txt(140, 132, "les tranchées", 12), txt(140, 154, "les batailles", 12),
          txt(500, 110, "les usines et les champs", 12), txt(500, 132, "les familles, l'école", 12), txt(500, 154, "les hôpitaux", 12),
          fleche(385, 100, 255, 100), txt(320, 92, "obus, vivres, colis", 11),
          fleche(385, 150, 255, 150), txt(320, 142, "lettres de la famille", 11),
          fleche(255, 185, 385, 185), txt(320, 177, "lettres des soldats, blessés", 11)]
    return "".join(o) + "</svg>"
