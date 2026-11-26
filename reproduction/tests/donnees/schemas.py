# -*- coding: utf-8 -*-
"""Schémas SVG du jeu « Le Jardin de la vie », tracés par script (jamais par IA) : fleur en coupe, de la fleur au fruit,
cycle de vie d'une plante à fleurs, fécondation interne et externe, œuf de poule en coupe, cycle de la grenouille.
Chaque fonction de jeu prend le nombre de repères numérotés à afficher ; la variante « lecon_… » écrit les mots."""
import math

POLICE = "font-family='Atkinson Hyperlegible,Arial,sans-serif'"
STYLE = "style='max-width:100%;height:auto;display:block;margin:10px auto'"
FOND, ENCRE = "#f5f7ee", "#22301c"


def repere(x, y, n, couleur="#2f5d2a"):
    return (f"<circle cx='{x}' cy='{y}' r='13' fill='{couleur}' stroke='#fff' stroke-width='2'/>"
            f"<text x='{x}' y='{y + 5}' text-anchor='middle' font-size='14' font-weight='700' fill='#fff' {POLICE}>{n}</text>")


def txt(x, y, s, taille=12, coul=ENCRE, gras=False, ancre="middle"):
    return (f"<text x='{x}' y='{y}' text-anchor='{ancre}' font-size='{taille}'" + (" font-weight='700'" if gras else "")
            + f" fill='{coul}' {POLICE}>{s}</text>")


def cadre(titre, h=300, w=640):
    return [f"<svg viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg' role='img' aria-label=\"{titre}\" {STYLE}>",
            f"<rect width='{w}' height='{h}' rx='12' fill='{FOND}'/>", txt(w / 2, 24, titre, 15, gras=True)]


def fleche(x1, y1, x2, y2, coul=ENCRE, ep=2.5):
    a = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - 10 * math.cos(a), y2 - 10 * math.sin(a)
    p1 = (bx + 6 * math.sin(a), by - 6 * math.cos(a))
    p2 = (bx - 6 * math.sin(a), by + 6 * math.cos(a))
    return (f"<line x1='{x1:.0f}' y1='{y1:.0f}' x2='{bx:.0f}' y2='{by:.0f}' stroke='{coul}' stroke-width='{ep}'/>"
            f"<polygon points='{x2:.0f},{y2:.0f} {p1[0]:.0f},{p1[1]:.0f} {p2[0]:.0f},{p2[1]:.0f}' fill='{coul}'/>")


def _reperes(o, pos, n, mots=None):
    for i in range(n):
        x, y = pos[i][:2]
        o.append(repere(x, y, i + 1))
        if mots:
            dx = pos[i][2] if len(pos[i]) > 2 else 18
            o.append(txt(x + dx, y + 5, mots[i], 12, gras=True, ancre="start" if dx > 0 else "end"))


# ------------------------------------------------------------------ salle 1 : fleur en coupe
FLEUR_MOTS = ["un pétale", "une étamine", "le pistil", "un sépale", "l'ovaire et ses ovules"]


def fleur(n, titre="La planche de Basile : une fleur coupée en deux", mots=None):
    """Repères : 1 pétale, 2 étamine, 3 pistil (stigmate), 4 sépale, 5 ovaire avec ovules."""
    o = cadre(titre, 330)
    cx = 320
    o += [f"<rect x='{cx - 4}' y='250' width='8' height='70' fill='#4f8a3a'/>",
          f"<path d='M{cx - 40},250 Q{cx},285 {cx + 40},250 Z' fill='#6aa84f'/>",
          f"<path d='M{cx - 40},250 C{cx - 120},230 {cx - 150},170 {cx - 110},120 C{cx - 80},170 {cx - 50},210 {cx - 30},245 Z' fill='#e86f9a'/>",
          f"<path d='M{cx + 40},250 C{cx + 120},230 {cx + 150},170 {cx + 110},120 C{cx + 80},170 {cx + 50},210 {cx + 30},245 Z' fill='#e86f9a'/>",
          f"<path d='M{cx - 42},252 C{cx - 80},260 {cx - 95},250 {cx - 100},238 C{cx - 75},240 {cx - 55},243 {cx - 40},248 Z' fill='#4f8a3a'/>",
          f"<path d='M{cx + 42},252 C{cx + 80},260 {cx + 95},250 {cx + 100},238 C{cx + 75},240 {cx + 55},243 {cx + 40},248 Z' fill='#4f8a3a'/>",
          f"<ellipse cx='{cx}' cy='228' rx='22' ry='26' fill='#9bc76f' stroke='{ENCRE}' stroke-width='1.5'/>",
          f"<circle cx='{cx - 7}' cy='224' r='5' fill='#f6f1c8' stroke='{ENCRE}'/>", f"<circle cx='{cx + 7}' cy='232' r='5' fill='#f6f1c8' stroke='{ENCRE}'/>",
          f"<rect x='{cx - 4}' y='130' width='8' height='76' fill='#9bc76f'/>",
          f"<ellipse cx='{cx}' cy='128' rx='14' ry='7' fill='#7fb04f'/>"]
    for dx in (-42, -26, 26, 42):
        o += [f"<line x1='{cx + dx * 0.6}' y1='245' x2='{cx + dx}' y2='150' stroke='#c9a227' stroke-width='3'/>",
              f"<ellipse cx='{cx + dx}' cy='146' rx='7' ry='11' fill='#f2c230' stroke='#a07d10'/>"]
    o += [txt(560, 290, "Schéma simplifié", 11), txt(560, 305, "(vue en coupe)", 11)]
    pos = [(cx - 125, 165, -18), (cx + 66, 150, 18), (cx, 100, -18), (cx - 98, 268, -18), (cx + 34, 236, 22)]
    _reperes(o, pos, n, mots)
    return "".join(o) + "</svg>"


def lecon_fleur():
    return fleur(5, "Les organes d'une fleur (vue en coupe)", FLEUR_MOTS)


# ------------------------------------------------------------------ leçon 2 : de la fleur au fruit
def fleur_fruit():
    o = cadre("De la fleur au fruit : l'exemple de la cerise", 260)
    etapes = [(90, "la fleur", "#e86f9a"), (250, "le pollen se dépose", "#f2c230"), (410, "les pétales tombent,", "#9bc76f"), (560, "le fruit mûr", "#c0392b")]
    for i, (x, t, c) in enumerate(etapes):
        o.append(f"<circle cx='{x}' cy='120' r='{34 if i != 2 else 26}' fill='{c}' stroke='{ENCRE}' stroke-width='1.5'/>")
        o.append(txt(x, 185, t, 12, gras=True))
        if i < 3:
            o.append(fleche(x + 40, 120, etapes[i + 1][0] - 42, 120))
    o += [txt(250, 200, "sur le pistil", 12), txt(410, 200, "l'ovaire grossit", 12), txt(560, 200, "le noyau = la graine", 12),
          "<circle cx='560' cy='120' r='9' fill='#f3e3c3' stroke='#22301c'/>"]
    return "".join(o) + "</svg>"


# ------------------------------------------------------------------ leçon 3 : cycle de vie d'une plante à fleurs
def cycle_plante():
    o = cadre("Le cycle de vie d'une plante à fleurs", 320)
    cx, cy, r = 320, 175, 105
    noms = ["la graine", "la germination", "la jeune plante", "la plante fleurit", "le fruit", "la dispersion des graines"]
    for i, t in enumerate(noms):
        a = -math.pi / 2 + i * 2 * math.pi / len(noms)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        o.append(f"<circle cx='{x:.0f}' cy='{y:.0f}' r='12' fill='#6aa84f'/>")
        c = math.cos(a)
        o.append(txt(x + (20 if c > 0.2 else -20 if c < -0.2 else 0), y + (5 if abs(c) > 0.2 else (-18 if y < cy else 30)), t, 12, gras=True,
                     ancre="start" if c > 0.2 else "end" if c < -0.2 else "middle"))
        a2 = a + 2 * math.pi / len(noms)
        o.append(fleche(cx + r * math.cos(a + 0.18), cy + r * math.sin(a + 0.18), cx + r * math.cos(a2 - 0.2), cy + r * math.sin(a2 - 0.2), "#4f8a3a", 2))
    return "".join(o) + "</svg>"


# ------------------------------------------------------------------ leçon 4 : fécondation interne et externe
def fecondation():
    o = cadre("Deux façons de féconder", 250)
    o += ["<rect x='30' y='45' width='280' height='190' rx='10' fill='#fff' stroke='#22301c'/>",
          "<rect x='330' y='45' width='280' height='190' rx='10' fill='#e6f2fa' stroke='#22301c'/>",
          txt(170, 70, "Fécondation interne", 14, gras=True), txt(470, 70, "Fécondation externe", 14, gras=True),
          txt(170, 100, "dans le corps de la femelle", 12), txt(470, 100, "dans l'eau, hors du corps", 12),
          "<ellipse cx='170' cy='155' rx='80' ry='35' fill='#f3d9c2' stroke='#22301c'/>",
          "<circle cx='190' cy='155' r='12' fill='#f6e7a0' stroke='#22301c'/>", "<circle cx='150' cy='150' r='4' fill='#2f5d2a'/>",
          txt(170, 215, "poule, vache, brebis, tortue", 12),
          "<path d='M360,150 q20,-20 40,0 t40,0 t40,0 t40,0 t40,0' stroke='#5aa0c8' stroke-width='3' fill='none'/>"]
    for x in range(390, 590, 30):
        o.append(f"<circle cx='{x}' cy='170' r='8' fill='#f6e7a0' stroke='#22301c'/>")
    o.append(txt(470, 215, "grenouille, truite", 12))
    return "".join(o) + "</svg>"


# ------------------------------------------------------------------ leçon 5 : œuf de poule en coupe
OEUF_MOTS = ["la coquille", "l'embryon", "le jaune (réserves)", "le blanc", "la poche d'air"]


def oeuf(n=5, titre="Un œuf de poule fécondé, en coupe", mots=OEUF_MOTS):
    o = cadre(titre, 280)
    o += ["<ellipse cx='300' cy='160' rx='150' ry='105' fill='#fbf6ea' stroke='#8a6d3b' stroke-width='6'/>",
          "<ellipse cx='300' cy='160' rx='138' ry='94' fill='#eef3e6'/>",
          "<path d='M430,120 Q455,160 430,200 Q445,160 430,120 Z' fill='#dfe8f0'/>",
          "<circle cx='290' cy='165' r='55' fill='#f2c230'/>",
          "<ellipse cx='275' cy='120' rx='16' ry='9' fill='#c0392b'/>"]
    pos = [(160, 90, -18), (275, 98, 18), (290, 190, 18), (360, 225, 18), (448, 160, 18)]
    _reperes(o, pos, n, mots)
    return "".join(o) + "</svg>"


# ------------------------------------------------------------------ leçon 5 bis : cycle de la grenouille
def cycle_grenouille():
    o = cadre("Le développement de la grenouille", 220)
    et = ["les œufs dans l'eau", "le têtard (larve)", "le têtard à pattes", "la jeune grenouille", "la grenouille adulte"]
    for i, t in enumerate(et):
        x = 70 + i * 125
        o.append(f"<circle cx='{x}' cy='110' r='26' fill='#9bc76f' stroke='#22301c'/>")
        o.append(txt(x, 165, t, 11, gras=True))
        if i < 4:
            o.append(fleche(x + 30, 110, x + 93, 110))
    return "".join(o) + "</svg>"
