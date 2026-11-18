# -*- coding: utf-8 -*-
"""Schémas SVG du jeu « L'Expédition biodiversité », tracés par script (jamais par IA) : attributs d'un oiseau, cellule végétale,
clé de détermination, groupes emboîtés, frise des temps géologiques, coupe de la mare, réseau alimentaire de l'étang."""

POLICE = "font-family='Atkinson Hyperlegible,Arial,sans-serif'"
STYLE = "style='max-width:100%;height:auto;display:block;margin:10px auto'"
FOND, ENCRE = "#f1f6ec", "#1d2a1b"


def repere(x, y, n, couleur="#b03a2e"):
    return (f"<circle cx='{x}' cy='{y}' r='13' fill='{couleur}' stroke='#fff' stroke-width='2'/>"
            f"<text x='{x}' y='{y + 5}' text-anchor='middle' font-size='14' font-weight='700' fill='#fff' {POLICE}>{n}</text>")


def txt(x, y, s, taille=12, coul=ENCRE, gras=False, ancre="middle", ital=False):
    return (f"<text x='{x}' y='{y}' text-anchor='{ancre}' font-size='{taille}'" + (" font-weight='700'" if gras else "")
            + (" font-style='italic'" if ital else "") + f" fill='{coul}' {POLICE}>{s}</text>")


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


# ------------------------------------------------------------------ salle 1
def oiseau(n, titre="La mésange du carnet de Lina"):
    """Repères : 1 bec, 2 œil, 3 plumes de l'aile, 4 patte, 5 queue."""
    o = cadre(titre, 280)
    o += ["<ellipse cx='320' cy='150' rx='120' ry='70' fill='#f2d04a' stroke='#1d2a1b' stroke-width='2'/>",
          "<circle cx='430' cy='105' r='48' fill='#2b4c7e' stroke='#1d2a1b' stroke-width='2'/>",
          "<ellipse cx='438' cy='112' rx='26' ry='20' fill='#ffffff'/>",
          "<circle cx='447' cy='95' r='7' fill='#111'/>",
          "<polygon points='476,100 506,108 476,116' fill='#3a3a3a'/>",
          "<path d='M240,120 q60,-40 140,10 q-60,40 -140,-10z' fill='#5b8fb9' stroke='#1d2a1b'/>",
          "<path d='M250,128 l120,6 M255,138 l110,2' stroke='#2b4c7e' stroke-width='2'/>",
          "<polygon points='205,140 120,120 125,175' fill='#2b4c7e' stroke='#1d2a1b'/>",
          "<path d='M300,215 l-8,40 M300,255 l-14,8 M300,255 l10,8 M350,215 l-6,40 M344,255 l-14,8 M344,255 l10,8' stroke='#6b4f35' stroke-width='4' fill='none'/>",
          "<rect x='80' y='262' width='480' height='6' rx='3' fill='#8f7155'/>"]
    pos = [(510, 80), (455, 60), (310, 92), (270, 245), (120, 100)]
    for i in range(n):
        o.append(repere(*pos[i], i + 1))
    return "".join(o) + "</svg>"


def cellule(n, titre="Une cellule de feuille vue au microscope"):
    """Repères : 1 paroi, 2 membrane, 3 cytoplasme, 4 noyau."""
    o = cadre(titre, 270)
    o += ["<rect x='170' y='55' width='300' height='190' rx='14' fill='#cfe8b0' stroke='#3f6b3a' stroke-width='9'/>",
          "<rect x='182' y='67' width='276' height='166' rx='10' fill='#e6f4d2' stroke='#2f5a2a' stroke-width='2'/>",
          "<circle cx='380' cy='150' r='32' fill='#c99a4c' stroke='#6b4f35' stroke-width='2'/>"]
    for x, y in [(220, 100), (250, 200), (300, 90), (320, 205), (420, 210), (230, 160), (430, 95)]:
        o.append(f"<ellipse cx='{x}' cy='{y}' rx='12' ry='7' fill='#3f8a3a'/>")
    pos = [(160, 50), (205, 250), (280, 150), (380, 150)]
    for i in range(n):
        o.append(repere(*pos[i], i + 1))
    o.append(txt(320, 263, "Dessin simplifié : une vraie cellule mesure moins d'un dixième de millimètre.", 11, ital=True))
    return "".join(o) + "</svg>"


# ------------------------------------------------------------------ salle 2
def cle(n, titre="La clé des petites bêtes de la litière"):
    """Feuilles numérotées : 1 escargot, 2 fourmi (insecte), 3 araignée, 4 cloporte, 5 mille-pattes."""
    o = cadre(titre, 330)
    boite = lambda x, y, w, s: [f"<rect x='{x - w / 2}' y='{y - 16}' width='{w}' height='30' rx='8' fill='#fff' stroke='#3f6b3a' stroke-width='2'/>", txt(x, y + 4, s, 12, gras=True)]
    o += boite(320, 58, 220, "A-t-il des pattes ?")
    o += boite(320, 140, 250, "Combien de pattes ?")
    o += [fleche(260, 74, 130, 230), txt(180, 150, "non", 12, ital=True), fleche(330, 74, 330, 122), txt(345, 104, "oui", 12, ital=True, ancre="start")]
    feuilles = [(130, 260, ""), (250, 260, "6"), (360, 260, "8"), (470, 260, "14"), (580, 260, "plus de 30")]
    for i, (x, y, lab) in enumerate(feuilles):
        if i:
            o.append(fleche(320, 156, x, y - 30))
            o.append(txt((320 + x) / 2 + 8, (156 + y - 30) / 2, lab, 12, ital=True, ancre="start"))
        o.append(f"<rect x='{x - 45}' y='{y - 22}' width='90' height='44' rx='10' fill='#fbe7b0' stroke='#7a5a12' stroke-width='2'/>")
        if i < n:
            o.append(repere(x, y, i + 1))
    o.append(txt(320, 318, "Lis la clé de haut en bas : chaque réponse t'envoie vers une case.", 11, ital=True))
    return "".join(o) + "</svg>"


def emboitement(titre="Des groupes emboîtés"):
    o = cadre(titre, 300)
    o += ["<rect x='20' y='40' width='600' height='245' rx='16' fill='#e4efdc' stroke='#3f6b3a' stroke-width='2'/>", txt(320, 60, "Squelette interne", 13, gras=True),
          "<rect x='40' y='72' width='330' height='200' rx='14' fill='#d3ebf2' stroke='#2f7a6b' stroke-width='2'/>", txt(205, 92, "Quatre membres", 13, gras=True),
          "<rect x='55' y='105' width='145' height='150' rx='12' fill='#fbe7b0' stroke='#7a5a12' stroke-width='2'/>", txt(127, 125, "Poils", 13, gras=True),
          "<rect x='210' y='105' width='145' height='150' rx='12' fill='#f6e0d0' stroke='#a0644a' stroke-width='2'/>", txt(282, 125, "Plumes", 13, gras=True),
          txt(127, 160, "renard", 12), txt(127, 185, "hérisson", 12), txt(127, 210, "chauve-souris", 12),
          txt(282, 160, "héron", 12), txt(282, 185, "mésange", 12), txt(282, 210, "canard", 12),
          txt(205, 266, "grenouille, lézard", 12, ital=True),
          txt(495, 160, "truite", 12), txt(495, 185, "perche", 12), txt(495, 230, "(nageoires)", 11, ital=True)]
    return "".join(o) + "</svg>"


def arbre(titre="Un arbre de parenté"):
    o = cadre(titre, 290)
    R = (340, 262)
    tige = lambda t: (R[0] + 240 * t, R[1] - 192 * t)
    o.append(f"<line x1='{R[0]}' y1='{R[1]}' x2='580' y2='70' stroke='{ENCRE}' stroke-width='3'/>")
    o.append(f"<line x1='{R[0]}' y1='{R[1]}' x2='100' y2='70' stroke='{ENCRE}' stroke-width='3'/>")
    for t, x in [(.3, 220), (.55, 340), (.8, 460)]:
        bx, by = tige(t)
        o.append(f"<line x1='{bx:.0f}' y1='{by:.0f}' x2='{x}' y2='70' stroke='{ENCRE}' stroke-width='3'/>")
    for x, s in [(100, "truite"), (220, "grenouille"), (340, "lézard"), (460, "renard"), (580, "loup")]:
        o.append(txt(x, 58, s, 13, gras=True))
    ax, ay = tige(.8)
    o += [f"<circle cx='{ax:.0f}' cy='{ay:.0f}' r='7' fill='#b03a2e'/>", txt(ax, ay + 30, "ancêtre commun", 11, ital=True),
          txt(320, 284, "Plus le point de séparation est haut, plus les espèces sont proches parentes.", 11, ital=True)]
    return "".join(o) + "</svg>"


# ------------------------------------------------------------------ salle 3
def frise(titre="Quelques repères du temps géologique"):
    o = cadre(titre, 230)
    o += ["<rect x='40' y='110' width='560' height='16' rx='8' fill='#c9b48a' stroke='#6b4f35'/>"]
    reps = [(50, "Terre", "4,6 milliards"), (130, "premières traces de vie", "3,8 milliards"), (330, "trilobites", "540 millions"),
            (470, "fin des dinosaures", "66 millions"), (590, "Homo sapiens", "300 000 ans")]
    for i, (x, a, b) in enumerate(reps):
        y = 80 if i % 2 == 0 else 160
        o += [f"<line x1='{x}' y1='118' x2='{x}' y2='{y + (8 if i % 2 == 0 else -14)}' stroke='{ENCRE}' stroke-width='2'/>",
              txt(x, y - 12 if i % 2 == 0 else y + 4, a, 12, gras=True), txt(x, y + 2 if i % 2 == 0 else y + 20, b, 11)]
    o.append(txt(320, 218, "Frise non proportionnelle : les derniers repères sont très serrés.", 11, ital=True))
    return "".join(o) + "</svg>"


def strates(titre="Les couches de l'ancienne carrière"):
    o = cadre(titre, 280)
    couches = [("#e8d9b0", "couche récente : coquilles d'escargots actuels"), ("#d8c08a", "argile : os de mammifères"),
               ("#c9a86a", "limite : la couche de la crise"), ("#b9945a", "calcaire : ammonites"), ("#a37e4a", "calcaire profond : trilobites")]
    for i, (c, s) in enumerate(couches):
        o += [f"<rect x='60' y='{45 + i * 40}' width='520' height='40' fill='{c}' stroke='#6b4f35'/>", txt(320, 70 + i * 40, s, 12)]
    o.append(txt(320, 268, "Dessin simplifié : en général, plus une couche est profonde, plus elle est ancienne.", 11, ital=True))
    return "".join(o) + "</svg>"


# ------------------------------------------------------------------ salle 4
def mare(n, titre="La coupe de la mare de la réserve"):
    """Repères : 1 la lumière du soleil, 2 l'eau, 3 un roseau, 4 une grenouille, 5 la vase."""
    o = cadre(titre, 300)
    o += ["<circle cx='560' cy='70' r='28' fill='#f7d046'/>",
          "<rect x='0' y='140' width='640' height='160' fill='#8f7155'/>",
          "<path d='M60,140 q260,170 520,0z' fill='#7fb6d6' stroke='#2f5f80' stroke-width='2'/>",
          "<path d='M140,230 q180,70 360,0 q-180,40 -360,0z' fill='#5d4a33'/>",
          "<path d='M110,140 l0,-70 M120,140 l2,-80 M130,140 l-3,-60' stroke='#4f7a2a' stroke-width='4'/>",
          "<ellipse cx='470' cy='136' rx='22' ry='12' fill='#5c8f3a' stroke='#1d2a1b'/><circle cx='462' cy='126' r='4' fill='#fff'/><circle cx='478' cy='126' r='4' fill='#fff'/>",
          "<ellipse cx='320' cy='142' rx='40' ry='6' fill='#3f8a3a'/>"]
    pos = [(520, 60), (300, 190), (90, 80), (500, 115), (320, 255)]
    for i in range(n):
        o.append(repere(*pos[i], i + 1))
    return "".join(o) + "</svg>"


# ------------------------------------------------------------------ salle 5
NOEUDS = {"algues": (90, 220), "têtard": (230, 220), "larve de libellule": (380, 220), "perche": (380, 110), "héron": (540, 70),
          "roseau": (90, 110), "ragondin": (230, 110), "grenouille": (540, 180)}
LIENS = [("algues", "têtard"), ("têtard", "larve de libellule"), ("larve de libellule", "perche"), ("perche", "héron"),
         ("roseau", "ragondin"), ("larve de libellule", "grenouille"), ("grenouille", "héron"), ("têtard", "perche")]


def reseau(n=0, titre="Le réseau alimentaire de l'étang", cacher=()):
    """Repères (n > 0) posés sur les espèces de `cacher`, dans l'ordre donné."""
    o = cadre(titre, 290)
    for a, b in LIENS:
        (x1, y1), (x2, y2) = NOEUDS[a], NOEUDS[b]
        import math
        dx, dy = x2 - x1, y2 - y1
        k = min(68 / abs(dx) if dx else 9, 23 / abs(dy) if dy else 9)
        o.append(fleche(x1 + dx * k, y1 + dy * k, x2 - dx * k, y2 - dy * k, "#2f5f80"))
    for nom, (x, y) in NOEUDS.items():
        o.append(f"<rect x='{x - 62}' y='{y - 17}' width='124' height='34' rx='10' fill='#fff' stroke='#3f6b3a' stroke-width='2'/>")
        if nom in cacher:
            i = list(cacher).index(nom)
            if i < n:
                o.append(repere(x, y, i + 1))
        else:
            o.append(txt(x, y + 5, nom, 12, gras=True))
    o.append(txt(320, 280, "Chaque flèche va de celui qui est mangé vers celui qui le mange.", 11, ital=True))
    return "".join(o) + "</svg>"


# ------------------------------------------------------------------ schémas des leçons
def lecon_oiseau():
    s = oiseau(0, "Observer les attributs").replace("</svg>", "")
    return s + "".join([txt(540, 85, "bec", 12, gras=True), txt(460, 50, "œil", 12, gras=True), txt(310, 82, "plumes", 12, gras=True),
                        txt(250, 245, "pattes", 12, gras=True), txt(115, 100, "queue", 12, gras=True)]) + "</svg>"


def lecon_mare():
    s = mare(0, "La mare : un milieu de vie et des êtres vivants").replace("</svg>", "")
    return s + "".join([txt(560, 115, "lumière", 12, gras=True), txt(320, 185, "eau", 12, gras=True), txt(135, 62, "roseaux", 12, gras=True),
                        txt(470, 112, "grenouille", 12, gras=True), txt(320, 285, "vase", 12, gras=True, coul="#fff")]) + "</svg>"
