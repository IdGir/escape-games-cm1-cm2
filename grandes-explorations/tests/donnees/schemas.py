# -*- coding: utf-8 -*-
"""Cartes et schémas SVG du jeu « La Caravelle du capitaine », dessinés par script (jamais par IA).
Cartes très simplifiées : formes, distances et tracés approximatifs (indiqué sous chaque carte)."""
import math

POLICE = "font-family='Atkinson Hyperlegible,Arial,sans-serif'"
STYLE = "style='max-width:100%;height:auto;display:block;margin:10px auto'"
MER, TERRE, BORD, ENCRE = "#cfe3ee", "#e9dcc0", "#8a6d45", "#2b2118"
INCONNU = "#f3efe6"


def repere(x, y, n, couleur="#1f4f6b"):
    return (f"<circle cx='{x}' cy='{y}' r='13' fill='{couleur}' stroke='#fff' stroke-width='2'/>"
            f"<text x='{x}' y='{y + 5}' text-anchor='middle' font-size='14' font-weight='700' fill='#fff' {POLICE}>{n}</text>")


def txt(x, y, s, taille=12, coul=ENCRE, gras=False, ancre="middle", ital=False):
    return (f"<text x='{x}' y='{y}' text-anchor='{ancre}' font-size='{taille}'" + (" font-weight='700'" if gras else "")
            + (" font-style='italic'" if ital else "") + f" fill='{coul}' {POLICE}>{s}</text>")


def chemin(points, coul, larg=4, tirets=False):
    """Route en pointillés ou trait plein, avec pointe à la fin."""
    d = "M" + " L".join(f"{x} {y}" for x, y in points)
    (x1, y1), (x2, y2) = points[-2], points[-1]
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 13 * math.cos(a - .45), y2 - 13 * math.sin(a - .45))
    p2 = (x2 - 13 * math.cos(a + .45), y2 - 13 * math.sin(a + .45))
    return (f"<path d='{d}' fill='none' stroke='{coul}' stroke-width='{larg}' stroke-linejoin='round'" + (" stroke-dasharray='9 6'" if tirets else "") + "/>"
            f"<polygon points='{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}' fill='{coul}'/>")


def _terres(ameriques=True, inconnues=False):
    """Planisphère très simplifié (Amériques à gauche, Europe-Afrique au centre, Asie à droite)."""
    am = INCONNU if inconnues else TERRE
    t = []
    if ameriques:
        t.append(f"<path d='M70 50 Q150 40 190 70 Q205 100 175 125 Q160 140 185 160 Q190 175 168 182 Q150 200 160 225 Q190 255 180 290 "
                 f"Q170 330 150 345 Q130 320 128 285 Q120 245 105 220 Q75 180 62 130 Q55 85 70 50 Z' fill='{am}' stroke='{BORD}' stroke-width='2'"
                 + (" stroke-dasharray='5 4'" if inconnues else "") + "/>")
    t.append(f"<path d='M300 55 Q340 45 380 60 Q395 85 375 100 Q350 110 330 108 Q305 102 298 85 Q292 68 300 55 Z' fill='{TERRE}' stroke='{BORD}' stroke-width='2'/>")
    t.append(f"<path d='M300 125 Q350 112 395 128 Q420 150 418 190 Q412 235 392 268 Q372 300 352 305 Q335 290 330 260 Q326 230 308 210 Q288 190 286 160 Q286 136 300 125 Z' fill='{TERRE}' stroke='{BORD}' stroke-width='2'/>")
    t.append(f"<path d='M390 50 Q480 35 570 55 Q615 80 600 120 Q585 150 545 160 Q520 175 500 170 Q470 190 455 175 Q440 150 420 135 Q395 115 390 90 Q385 65 390 50 Z' fill='{TERRE}' stroke='{BORD}' stroke-width='2'/>")
    return "".join(t)


def _cadre(titre, h=360):
    return [f"<svg viewBox='0 0 640 {h}' xmlns='http://www.w3.org/2000/svg' role='img' aria-label=\"{titre}\" {STYLE}>",
            f"<rect width='640' height='{h}' rx='12' fill='{MER}'/>", txt(320, 22, titre, 15, gras=True)]


def carte_monde_1450(nb=3, titre="Le monde connu des Européens vers 1450", avec_noms=False):
    """Salle 1 : Europe, Afrique, Asie ; CM2 : + mer Méditerranée, route des épices (terre)."""
    t = _cadre(titre)
    t.append(_terres(ameriques=True, inconnues=True))
    t.append(txt(125, 200, "terres inconnues", 11, "#7a6a55", ital=True) + txt(125, 214, "des Européens", 11, "#7a6a55", ital=True))
    t.append("<ellipse cx='345' cy='116' rx='38' ry='7' fill='" + MER + "' stroke='#5a8fb0' stroke-width='1.5'/>")
    t.append(chemin([(560, 120), (480, 128), (420, 122), (370, 112)], "#a0522d", 4, tirets=True))
    if avec_noms:
        t += [txt(338, 80, "EUROPE", 12, gras=True), txt(360, 200, "AFRIQUE", 12, gras=True), txt(510, 95, "ASIE", 12, gras=True),
              txt(250, 160, "océan Atlantique", 12, "#1f4f6b", ital=True), txt(470, 145, "route des épices", 11, "#a0522d", ital=True)]
    pos = [(340, 78), (360, 205), (520, 90), (345, 116), (470, 128)]
    for i in range(nb):
        t.append(repere(*pos[i], i + 1))
    t.append(txt(320, 352, "Carte simplifiée : formes et distances non respectées.", 11, "#4a3d2e"))
    t.append("</svg>")
    return "".join(t)


def schema_caravelle(nb=3, titre="Une caravelle (schéma simplifié)", avec_noms=False):
    """Salle 2 : 1 voile latine, 2 mât, 3 gouvernail d'étambot ; CM2 : 1 voile latine, 2 voile carrée, 3 gouvernail, 4 château arrière, 5 coque."""
    t = _cadre(titre, 340)
    t.append("<path d='M0 270 Q160 258 320 270 T640 270 V340 H0 Z' fill='#9cc3d8'/>")
    t.append(f"<path d='M120 230 L520 230 Q505 285 440 292 L200 292 Q140 285 120 230 Z' fill='#8a5a32' stroke='{BORD}' stroke-width='2'/>")
    t.append(f"<rect x='130' y='200' width='95' height='30' fill='#7a4e2a' stroke='{BORD}' stroke-width='2'/>")
    t.append("<path d='M122 250 L104 296 L120 298 L134 262 Z' fill='#5c3b22'/>")
    t.append("<line x1='420' y1='230' x2='420' y2='60' stroke='#5c3b22' stroke-width='6'/><line x1='300' y1='230' x2='300' y2='50' stroke='#5c3b22' stroke-width='6'/>"
             "<line x1='200' y1='200' x2='200' y2='80' stroke='#5c3b22' stroke-width='5'/>")
    t.append("<rect x='370' y='75' width='100' height='110' fill='#f6eedb' stroke='#a8916a' stroke-width='2'/>")
    t.append("<path d='M240 60 L345 220 L240 220 Z' fill='#f6eedb' stroke='#a8916a' stroke-width='2'/><line x1='230' y1='55' x2='350' y2='225' stroke='#5c3b22' stroke-width='3'/>")
    t.append("<path d='M150 90 L245 195 L150 195 Z' fill='#f6eedb' stroke='#a8916a' stroke-width='2'/>")
    if nb == 3:
        pos = [(275, 175), (420, 210), (110, 278)]
        noms = ["voile triangulaire (latine)", "mât", "gouvernail"]
    else:
        pos = [(275, 175), (420, 130), (110, 278), (178, 215), (330, 262)]
        noms = ["voile latine", "voile carrée", "gouvernail d'étambot", "château arrière", "coque"]
    for i, (x, y) in enumerate(pos[:nb]):
        t.append(repere(x, y, i + 1))
        if avec_noms:
            lx, ly = (x, y + 30) if y < 250 else (x, y - 22)
            if "gouvernail" in noms[i]:
                lx, ly = x + 40, y + 34
            t.append(txt(lx, ly, noms[i], 11, gras=True))
    t.append(txt(320, 334, "Schéma simplifié : proportions non respectées.", 11, "#4a3d2e"))
    t.append("</svg>")
    return "".join(t)


def carte_routes(nb=3, titre="Les grands voyages (1492-1534)", avec_noms=False):
    """Salle 3 : routes de Colomb (1), Vasco de Gama (2), Cartier (3) ; CM2 : + Magellan-Elcano (4), cap de Bonne-Espérance (5)."""
    t = _cadre(titre)
    t.append(_terres())
    t.append(chemin([(300, 92), (250, 120), (200, 150)], "#b8432a", 4))                                       # Colomb : Palos -> Antilles
    t.append(chemin([(298, 85), (270, 180), (300, 290), (360, 318), (420, 250), (470, 175)], "#2d7a3e", 4))  # Gama : Lisbonne -> Calicut
    t.append(chemin([(300, 75), (240, 70), (185, 82)], "#1f4f6b", 4))                                          # Cartier : Saint-Malo -> Saint-Laurent
    if nb > 3:
        t.append(chemin([(298, 95), (240, 230), (175, 335), (120, 345), (60, 300), (20, 220)], "#7a3e8c", 3, tirets=True))  # Magellan
    if avec_noms:
        t += [txt(225, 112, "Colomb, 1492", 11, "#b8432a", gras=True), txt(470, 300, "Vasco de Gama, 1498", 11, "#2d7a3e", gras=True),
              txt(225, 60, "Cartier, 1534", 11, "#1f4f6b", gras=True)]
        if nb > 3:
            t.append(txt(110, 330, "Magellan et Elcano, 1519-1522", 11, "#7a3e8c", gras=True))
    pos = [(230, 130), (445, 212), (240, 72), (150, 330), (352, 318)]
    for i in range(nb):
        t.append(repere(*pos[i], i + 1, "#5c3b22"))
    t.append(txt(320, 352, "Carte simplifiée : tracés approximatifs, formes et distances non respectées.", 11, "#4a3d2e"))
    t.append("</svg>")
    return "".join(t)


def carte_tordesillas(nb=3, titre="Le partage du monde à Tordesillas (1494)", avec_noms=False):
    """Salle 5 : 1 ligne de partage, 2 terres pour l'Espagne (ouest), 3 terres pour le Portugal (est) ; CM2 : + 4 Brésil, 5 Nouvelle-France."""
    t = _cadre(titre)
    t.append(_terres())
    t.append("<rect x='0' y='30' width='172' height='330' fill='#d9a441' opacity='.13'/><rect x='172' y='30' width='468' height='330' fill='#2d7a3e' opacity='.10'/>")
    t.append("<line x1='172' y1='34' x2='172' y2='350' stroke='#7a2e1f' stroke-width='3' stroke-dasharray='10 6'/>")
    t.append("<path d='M172 222 Q196 246 189 284 Q180 298 172 296 Z' fill='#cfe7d4' stroke='#2d7a3e' stroke-width='1.5'/>")
    if avec_noms:
        t += [txt(200, 46, "ligne de Tordesillas", 11, "#7a2e1f", gras=True), txt(80, 330, "pour l'Espagne", 12, "#8a5a10", gras=True),
              txt(470, 330, "pour le Portugal", 12, "#2d6b3e", gras=True)]
    pos = [(172, 120), (95, 150), (470, 230), (205, 262), (120, 68)]
    for i in range(nb):
        t.append(repere(*pos[i], i + 1, "#5c3b22"))
    t.append(txt(320, 352, "Carte simplifiée : formes et distances non respectées.", 11, "#4a3d2e"))
    t.append("</svg>")
    return "".join(t)


# Schémas des leçons (mêmes dessins, noms écrits)
def lecon_monde():
    return carte_monde_1450(5, avec_noms=True)


def lecon_caravelle():
    return schema_caravelle(5, avec_noms=True)


def lecon_routes():
    return carte_routes(4, avec_noms=True)


def lecon_rencontres():
    t = _cadre("Trois peuples d'Amérique vers 1500", 340)
    t.append(_terres())
    t += [repere(120, 80, "N"), txt(120, 112, "Iroquoiens du Saint-Laurent", 11, gras=True),
          repere(140, 165, "A"), txt(140, 196, "Aztèques (Tenochtitlan)", 11, gras=True),
          repere(150, 270, "I"), txt(150, 300, "Incas (Cuzco, Andes)", 11, gras=True),
          txt(320, 334, "Carte simplifiée : positions approximatives.", 11, "#4a3d2e"), "</svg>"]
    return "".join(t)


def lecon_partage():
    return carte_tordesillas(3, avec_noms=True)
