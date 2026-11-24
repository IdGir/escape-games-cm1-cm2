# -*- coding: utf-8 -*-
"""Schémas SVG du jeu « L'Observatoire des volcans », tracés par script (jamais par IA) : coupe de la Terre, maquette de deux plaques,
coupe d'un volcan, coupe d'un séisme, sismogramme. Chaque fonction prend le nombre de repères numérotés à afficher ;
la variante « lecon_… » écrit les mots à côté des repères (schéma légendé des leçons)."""
import math

POLICE = "font-family='Atkinson Hyperlegible,Arial,sans-serif'"
STYLE = "style='max-width:100%;height:auto;display:block;margin:10px auto'"
FOND, ENCRE = "#f6f1ea", "#2a1d17"


def repere(x, y, n, couleur="#1f4e79"):
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


# ------------------------------------------------------------------ salle 1 : coupe de la Terre
TERRE_MOTS = ["la croûte", "le manteau", "le noyau", "environ 2 900 km", "le centre, à environ 6 400 km"]


def terre(n, titre="La maquette d'Inès : la Terre coupée en deux", mots=None):
    """Repères : 1 croûte, 2 manteau, 3 noyau, 4 limite manteau-noyau (≈ 2 900 km), 5 centre (≈ 6 400 km)."""
    o = cadre(titre, 320)
    cx, cy = 230, 300
    o += [f"<path d='M{cx - 220},{cy} A220,220 0 0 1 {cx + 220},{cy} Z' fill='#7a5a3a'/>",
          f"<path d='M{cx - 210},{cy} A210,210 0 0 1 {cx + 210},{cy} Z' fill='#e07b39'/>",
          f"<path d='M{cx - 100},{cy} A100,100 0 0 1 {cx + 100},{cy} Z' fill='#f2c14e'/>",
          f"<path d='M{cx - 45},{cy} A45,45 0 0 1 {cx + 45},{cy} Z' fill='#fbe7a1'/>",
          f"<line x1='{cx - 230}' y1='{cy}' x2='{cx + 230}' y2='{cy}' stroke='{ENCRE}' stroke-width='2'/>",
          f"<circle cx='{cx}' cy='{cy}' r='4' fill='{ENCRE}'/>",
          txt(560, 70, "La croûte est dessinée", 11), txt(560, 85, "plus épaisse qu'en réalité", 11), txt(560, 100, "pour être visible.", 11)]
    pos = [(cx - 150, cy - 155, -18), (cx - 110, cy - 110, -18), (cx - 62, cy - 40, -18), (cx + 71, cy - 71, 18), (cx, cy - 22, 18)]
    _reperes(o, pos, n, mots)
    return "".join(o) + "</svg>"


def lecon_terre():
    return terre(5, "Les enveloppes de la Terre (échelle non respectée pour la croûte)", TERRE_MOTS)


# ------------------------------------------------------------------ salle 2 : maquette de deux plaques
PLAQUES_MOTS = ["une plaque", "le manteau", "un volcan", "le foyer d'un séisme", "la plaque qui s'enfonce"]


def plaques(n, titre="La maquette de Noé : deux plaques qui se rapprochent", mots=None):
    """Repères : 1 plaque (continent), 2 manteau, 3 volcan, 4 foyer d'un séisme, 5 plaque océanique qui s'enfonce."""
    o = cadre(titre, 300)
    o += ["<rect x='20' y='150' width='600' height='130' fill='#e8a46a'/>",
          "<rect x='20' y='118' width='300' height='22' fill='#5aa0c8'/>",
          "<polygon points='20,140 320,140 470,250 470,270 300,160 20,160' fill='#6b6b6b'/>",
          "<polygon points='330,120 620,120 620,170 470,170 330,140' fill='#8c6a46'/>",
          "<polygon points='470,120 500,72 530,120' fill='#7a4a2a'/>",
          "<ellipse cx='505' cy='58' rx='16' ry='10' fill='#9a9a9a'/>", "<ellipse cx='520' cy='44' rx='20' ry='12' fill='#b0b0b0'/>",
          "<line x1='500' y1='120' x2='470' y2='230' stroke='#d9481c' stroke-width='4' stroke-dasharray='6,4'/>",
          "<circle cx='400' cy='192' r='9' fill='#ffd23f' stroke='#b03a2e' stroke-width='3'/>",
          fleche(120, 105, 230, 105), fleche(600, 100, 545, 100), txt(175, 95, "lent mouvement", 11), txt(575, 90, "", 11)]
    pos = [(590, 145, -18), (120, 230, 18), (470, 80, -18), (400, 215, 18), (180, 150, 18)]
    _reperes(o, pos, n, mots)
    return "".join(o) + "</svg>"


def lecon_plaques():
    return plaques(5, "Deux plaques qui se rapprochent (modèle)", PLAQUES_MOTS)


# ------------------------------------------------------------------ salle 3 : coupe d'un volcan
VOLCAN_MOTS = ["le cratère", "la cheminée", "la chambre magmatique", "une coulée de lave", "le nuage de cendres et de gaz"]


def volcan(n, titre="Le carnet de Maëva : un volcan en coupe", mots=None):
    """Repères : 1 cratère, 2 cheminée, 3 chambre magmatique, 4 coulée de lave, 5 nuage de cendres et de gaz."""
    o = cadre(titre, 320)
    o += ["<rect x='20' y='230' width='600' height='75' fill='#a37c58'/>",
          "<polygon points='90,230 290,90 350,90 550,230' fill='#6e5240'/>",
          "<polygon points='300,92 340,92 330,110 310,110' fill='#d9481c'/>",
          "<rect x='313' y='108' width='14' height='160' fill='#d9481c'/>",
          "<ellipse cx='320' cy='275' rx='85' ry='24' fill='#e8572a'/>",
          "<path d='M340,96 C380,130 400,170 470,215 L480,230 L455,230 C400,190 370,150 335,104 Z' fill='#f08a24'/>",
          "<path d='M300,86 C250,40 330,30 320,58 C340,20 410,40 360,80 Z' fill='#8d8d8d'/>"]
    pos = [(270, 94, -18), (345, 175, 18), (420, 278, 18), (470, 200, 18), (380, 44, 18)]
    _reperes(o, pos, n, mots)
    return "".join(o) + "</svg>"


def lecon_volcan():
    return volcan(5, "Un volcan en coupe", VOLCAN_MOTS)


# ------------------------------------------------------------------ salle 4 : coupe d'un séisme
SEISME_MOTS = ["le foyer", "l'épicentre", "la faille", "les ondes sismiques", "un sismographe"]


def seisme(n, titre="Le tableau de Samuel : un séisme en coupe", mots=None):
    """Repères : 1 foyer, 2 épicentre, 3 faille, 4 ondes sismiques, 5 sismographe (station)."""
    o = cadre(titre, 300)
    o += ["<rect x='20' y='110' width='600' height='175' fill='#c9a27a'/>",
          "<rect x='20' y='104' width='600' height='8' fill='#6fae5a'/>",
          "<line x1='250' y1='110' x2='350' y2='285' stroke='#5a3b24' stroke-width='5'/>",
          "<circle cx='305' cy='210' r='10' fill='#ffd23f' stroke='#b03a2e' stroke-width='3'/>"]
    for r in (35, 65, 95):
        o.append(f"<circle cx='305' cy='210' r='{r}' fill='none' stroke='#b03a2e' stroke-width='2' stroke-dasharray='5,5'/>")
    o += ["<polygon points='290,104 305,92 320,104' fill='#b03a2e'/>",
          "<rect x='500' y='78' width='60' height='26' fill='#ffffff' stroke='#2a1d17' stroke-width='2'/>",
          "<path d='M505,92 l8,0 l4,-8 l5,16 l5,-12 l4,8 l25,0' stroke='#2a1d17' stroke-width='1.5' fill='none'/>"]
    pos = [(330, 230, 18), (305, 74, 18), (262, 150, -18), (390, 180, 18), (530, 60, -18)]
    _reperes(o, pos, n, mots)
    return "".join(o) + "</svg>"


def lecon_seisme():
    return seisme(5, "Un séisme en coupe", SEISME_MOTS)


# ------------------------------------------------------------------ salle 5 : carte des risques (fictive) du village de Bois-Clair
def carte_risques(titre="La carte des risques de Bois-Clair (village inventé)"):
    o = cadre(titre, 300)
    o += ["<rect x='30' y='45' width='580' height='235' fill='#e9f1df' stroke='#2a1d17'/>",
          "<path d='M30,45 L250,45 L180,280 L30,280 Z' fill='#f4b6a6'/>",
          "<path d='M250,45 L420,45 L330,280 L180,280 Z' fill='#f9dfa8'/>",
          "<polygon points='70,90 100,55 130,90' fill='#7a4a2a'/>", txt(100, 105, "volcan", 11, gras=True),
          "<rect x='470' y='170' width='40' height='30' fill='#ffffff' stroke='#2a1d17'/>", txt(490, 215, "école", 11, gras=True),
          "<rect x='380' y='230' width='40' height='26' fill='#ffffff' stroke='#2a1d17'/>", txt(400, 272, "mairie", 11),
          "<circle cx='540' cy='90' r='10' fill='#2f7a4a'/>", txt(540, 78, "point de rassemblement", 10),
          txt(110, 200, "zone A", 13, gras=True), txt(110, 216, "danger fort", 11),
          txt(270, 200, "zone B", 13, gras=True), txt(270, 216, "danger moyen", 11),
          txt(500, 140, "zone C", 13, gras=True), txt(500, 156, "danger faible", 11)]
    return "".join(o) + "</svg>"
