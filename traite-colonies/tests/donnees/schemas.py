# -*- coding: utf-8 -*-
"""Cartes et schémas SVG du jeu « Les Archives du port », dessinés par script (jamais par IA).
Cartes simplifiées : formes et distances non respectées (indiqué sous chaque carte)."""

POLICE = "font-family='Atkinson Hyperlegible,Arial,sans-serif'"
STYLE = "style='max-width:100%;height:auto;display:block;margin:10px auto'"
MER, TERRE, BORD, ENCRE = "#cfe3ee", "#e9dcc0", "#8a6d45", "#2b2118"


def repere(x, y, n, couleur="#7a2e1f"):
    return (f"<circle cx='{x}' cy='{y}' r='13' fill='{couleur}' stroke='#fff' stroke-width='2'/>"
            f"<text x='{x}' y='{y + 5}' text-anchor='middle' font-size='14' font-weight='700' fill='#fff' {POLICE}>{n}</text>")


def txt(x, y, s, taille=12, coul=ENCRE, gras=False, ancre="middle", ital=False):
    return (f"<text x='{x}' y='{y}' text-anchor='{ancre}' font-size='{taille}'" + (" font-weight='700'" if gras else "")
            + (" font-style='italic'" if ital else "") + f" fill='{coul}' {POLICE}>{s}</text>")


def fleche(x1, y1, x2, y2, coul, larg=4, tirets=False, cx=None, cy=None):
    """Flèche courbe (quadratique) avec pointe."""
    import math
    if cx is None:
        cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
    d = f"M{x1} {y1} Q{cx} {cy} {x2} {y2}"
    ang = math.atan2(y2 - cy, x2 - cx)
    a1 = (x2 - 14 * math.cos(ang - .45), y2 - 14 * math.sin(ang - .45))
    a2 = (x2 - 14 * math.cos(ang + .45), y2 - 14 * math.sin(ang + .45))
    return (f"<path d='{d}' fill='none' stroke='{coul}' stroke-width='{larg}'" + (" stroke-dasharray='9 6'" if tirets else "") + "/>"
            f"<polygon points='{x2},{y2} {a1[0]:.1f},{a1[1]:.1f} {a2[0]:.1f},{a2[1]:.1f}' fill='{coul}'/>")


def _continents():
    """Amériques (gauche), Europe (haut droite), Afrique (droite) : formes très simplifiées."""
    return ("<path d='M40 40 Q120 30 170 60 Q190 95 160 120 Q150 140 175 160 Q185 175 160 180 Q140 200 150 230 Q175 270 160 300 "
            "Q150 320 130 318 Q110 290 112 250 Q105 215 90 195 Q60 160 50 120 Q35 80 40 40 Z' fill='" + TERRE + "' stroke='" + BORD + "' stroke-width='2'/>"
            "<g fill='" + TERRE + "' stroke='" + BORD + "' stroke-width='1.5'><ellipse cx='205' cy='170' rx='9' ry='4'/><ellipse cx='222' cy='178' rx='6' ry='3'/><ellipse cx='236' cy='188' rx='4' ry='3'/></g>"
            "<path d='M470 40 Q520 30 580 45 Q610 70 600 95 Q580 115 545 120 Q520 128 505 118 Q480 110 470 95 Q455 70 470 40 Z' fill='" + TERRE + "' stroke='" + BORD + "' stroke-width='2'/>"
            "<path d='M470 140 Q520 128 575 140 Q610 160 615 200 Q612 240 590 270 Q570 305 545 312 Q525 300 520 270 Q515 240 495 220 Q470 205 462 180 Q458 155 470 140 Z' fill='" + TERRE + "' stroke='" + BORD + "' stroke-width='2'/>")


def carte_triangle(nb_reperes=3, titre="Le commerce triangulaire (XVIIe-XIXe siècle)", fleches=True, avec_noms=False):
    """Carte simplifiée de l'Atlantique ; repères 1 à 3 (CM1) ou 1 à 5 (CM2)."""
    t = [f"<svg viewBox='0 0 640 340' xmlns='http://www.w3.org/2000/svg' role='img' aria-label=\"{titre}\" {STYLE}>",
         f"<rect width='640' height='340' rx='12' fill='{MER}'/>", _continents(), txt(320, 22, titre, 15, gras=True)]
    if fleches:
        t.append(fleche(478, 100, 500, 162, "#1f5f8b", cx=430, cy=130))          # Europe -> Afrique
        t.append(fleche(470, 200, 230, 190, "#7a2e1f", 5, cx=350, cy=255))        # Afrique -> Amériques
        t.append(fleche(215, 160, 465, 80, "#2d7a3e", cx=320, cy=70))             # Amériques -> Europe
    if avec_noms:
        t += [txt(535, 82, "EUROPE", 13, gras=True), txt(555, 215, "AFRIQUE", 13, gras=True), txt(100, 110, "AMÉRIQUES", 13, gras=True),
              txt(330, 150, "océan Atlantique", 13, "#1f4f6b", ital=True)]
    pos = [(540, 70), (560, 230), (110, 140), (330, 150), (350, 238)]
    for i in range(nb_reperes):
        t.append(repere(*pos[i], i + 1))
    t.append(txt(320, 337, "Carte simplifiée : formes et distances non respectées.", 11, "#4a3d2e"))
    t.append("</svg>")
    return "".join(t)


def carte_ports():
    """CM2 : la façade atlantique et la Manche, quatre ports repérés (positions approximatives)."""
    t = [f"<svg viewBox='0 0 640 360' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Les grands ports de la traite et du commerce colonial' {STYLE}>",
         f"<rect width='640' height='360' rx='12' fill='{MER}'/>", txt(320, 22, "Ports de l'Atlantique et de la Manche", 15, gras=True),
         # France très simplifiée (hexagone arrondi)
         f"<path d='M300 60 Q360 45 420 70 Q470 80 500 110 Q520 160 505 205 Q500 250 470 290 Q420 320 360 318 Q330 330 300 310 "
         f"Q285 270 270 240 Q262 210 250 180 Q225 165 200 150 Q215 135 250 132 Q262 110 270 95 Q285 70 300 60 Z' fill='{TERRE}' stroke='{BORD}' stroke-width='2'/>",
         txt(400, 200, "FRANCE", 14, gras=True), txt(150, 260, "océan Atlantique", 13, "#1f4f6b", ital=True), txt(360, 44, "la Manche", 12, "#1f4f6b", ital=True)]
    # Le Havre (embouchure de la Seine), Nantes (Loire), La Rochelle, Bordeaux (Garonne)
    t.append("<path d='M330 70 Q350 82 372 80' fill='none' stroke='#5a8fb0' stroke-width='3'/>")
    t.append("<path d='M226 165 Q270 175 320 170' fill='none' stroke='#5a8fb0' stroke-width='3'/>")
    t.append("<path d='M282 262 Q300 270 330 268' fill='none' stroke='#5a8fb0' stroke-width='3'/>")
    t.append(repere(326, 72, 1) + repere(250, 168, 2) + repere(262, 208, 3) + repere(288, 262, 4))
    t.append(txt(320, 352, "Carte simplifiée : formes et positions approximatives.", 11, "#4a3d2e"))
    t.append("</svg>")
    return "".join(t)


# ---------------------------------------------------------------- schémas des leçons
def lecon_triangle():
    return carte_triangle(0, "Les trois trajets du commerce triangulaire", True, True).replace(
        "</svg>", txt(470, 128, "1", 13, "#1f5f8b", True) + txt(350, 252, "2", 13, "#7a2e1f", True) + txt(320, 64, "3", 13, "#2d7a3e", True)
        + "<rect x='232' y='270' width='210' height='56' rx='6' fill='#fffaf0' stroke='#8a6d45'/>"
        + txt(240, 286, "1 : marchandises vers l'Afrique", 11, "#1f5f8b", True, "start")
        + txt(240, 302, "2 : captifs vers les Amériques", 11, "#7a2e1f", True, "start")
        + txt(240, 318, "3 : sucre, café vers l'Europe", 11, "#2d7a3e", True, "start") + "</svg>")


def lecon_traite():
    """Frise : la traite atlantique du XVIe au XIXe siècle, avec deux repères."""
    t = [f"<svg viewBox='0 0 640 170' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='La traite atlantique dure plus de trois siècles' {STYLE}>",
         "<rect width='640' height='170' rx='12' fill='#f6efe2'/>", txt(320, 24, "La traite atlantique : plus de trois siècles", 15, gras=True)]
    x0, w = 50, 540
    sie = ["XVIe", "XVIIe", "XVIIIe", "XIXe"]
    for i, s in enumerate(sie):
        t.append(f"<rect x='{x0 + i * w / 4:.0f}' y='70' width='{w / 4:.0f}' height='30' fill='{['#e9d7b4', '#e0c595', '#d1a86a', '#e0c595'][i]}' stroke='#8a6d45'/>")
        t.append(txt(x0 + i * w / 4 + w / 8, 90, s + " siècle", 12, gras=True))
    t.append(txt(x0, 120, "1501", 11, ancre="start") + txt(x0 + w, 120, "1900", 11, ancre="end"))
    xm = x0 + 2.5 * w / 4
    t.append(f"<polygon points='{xm - 7},58 {xm + 7},58 {xm},68' fill='#7a2e1f'/>" + txt(xm, 52, "la traite française est la plus forte", 11, "#7a2e1f", True))
    t.append(txt(320, 150, "Plus de 12,5 millions de personnes déportées d'Afrique vers les Amériques (source : BnF, d'après Slave Voyages).", 11, "#4a3d2e"))
    t.append("</svg>")
    return "".join(t)


def lecon_habitation():
    """Plan simplifié d'une habitation sucrière des Antilles (lieux, sans personnage)."""
    t = [f"<svg viewBox='0 0 640 230' xmlns='http://www.w3.org/2000/svg' role='img' aria-label=\"Plan simplifié d'une habitation sucrière\" {STYLE}>",
         "<rect width='640' height='230' rx='12' fill='#eef3e2'/>", txt(320, 22, "Une habitation sucrière aux Antilles (plan simplifié)", 15, gras=True)]
    t.append("<rect x='20' y='40' width='250' height='170' rx='6' fill='#a9c77a' stroke='#5f7d3a'/>")
    for i in range(9):
        t.append(f"<line x1='{35 + i * 27}' y1='55' x2='{35 + i * 27}' y2='195' stroke='#5f7d3a' stroke-width='2'/>")
    t.append(txt(145, 130, "champs de canne", 13, "#22340f", True))
    for x, y, w, h, nom, c in [(300, 50, 90, 60, "moulin", "#c9a37a"), (410, 50, 100, 60, "sucrerie", "#b98a5a"), (530, 50, 90, 60, "purgerie", "#c9a37a"),
                               (300, 140, 140, 70, "cases des esclaves", "#d8c7a4"), (460, 140, 160, 70, "maison du maître", "#f2ead6")]:
        t.append(f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='5' fill='{c}' stroke='#6b5032'/>" + txt(x + w / 2, y + h / 2 + 5, nom, 12, gras=True))
    t.append(fleche(272, 80, 298, 80, "#6b5032", 3) + fleche(392, 80, 408, 80, "#6b5032", 3) + fleche(512, 80, 528, 80, "#6b5032", 3))
    t.append("</svg>")
    return "".join(t)


def lecon_produits():
    """Deux colonnes : ce qui part de France vers l'Afrique, ce qui revient des colonies."""
    t = [f"<svg viewBox='0 0 640 190' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Marchandises au départ et au retour' {STYLE}>",
         "<rect width='640' height='190' rx='12' fill='#f6efe2'/>", txt(320, 24, "Ce qui part des ports, ce qui y revient", 15, gras=True),
         "<rect x='30' y='40' width='270' height='135' rx='8' fill='#e3edf5' stroke='#1f5f8b'/>", txt(165, 62, "Chargé en France pour l'Afrique", 13, "#1f5f8b", True),
         "<rect x='340' y='40' width='270' height='135' rx='8' fill='#e6f1e3' stroke='#2d7a3e'/>", txt(475, 62, "Rapporté des colonies d'Amérique", 13, "#2d7a3e", True)]
    for i, m in enumerate(["tissus et toiles", "fusils et poudre", "eau-de-vie et vin", "fer en barre"]):
        t.append(txt(165, 90 + i * 22, m, 13))
    for i, m in enumerate(["sucre", "café", "cacao et coton", "indigo (teinture bleue)"]):
        t.append(txt(475, 90 + i * 22, m, 13))
    t.append(txt(320, 186, "D'après la cargaison de La Licorne (Bordeaux, 1787) et les denrées citées par l'académie de Bordeaux.", 10, "#4a3d2e"))
    t.append("</svg>")
    return "".join(t)


def lecon_abolitions():
    """Frise des résistances et des abolitions, 1685-2006."""
    ev = [(1685, "Code noir"), (1791, "révolte de Saint-Domingue"), (1794, "1re abolition"), (1802, "rétablissement"),
          (1804, "indépendance d'Haïti"), (1848, "abolition définitive"), (2001, "loi : crime contre l'humanité"), (2006, "1er 10 mai")]
    t = [f"<svg viewBox='0 0 640 210' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Frise des résistances et des abolitions' {STYLE}>",
         "<rect width='640' height='210' rx='12' fill='#f6efe2'/>", txt(320, 24, "Résistances et abolitions", 15, gras=True),
         "<line x1='30' y1='110' x2='610' y2='110' stroke='#2b2118' stroke-width='3'/><polygon points='610,103 624,110 610,117' fill='#2b2118'/>"]
    xs = [40, 115, 190, 265, 340, 415, 490, 565]
    for i, ((a, e), x) in enumerate(zip(ev, xs)):
        haut = i % 2 == 0
        y = 70 if haut else 150
        t.append(f"<circle cx='{x + 20}' cy='110' r='6' fill='#7a2e1f'/><line x1='{x + 20}' y1='110' x2='{x + 20}' y2='{y + (8 if haut else -16)}' stroke='#7a2e1f'/>")
        t.append(txt(x + 20, y - 6 if haut else y, str(a), 13, "#7a2e1f", True) + txt(x + 20, (y + 8) if haut else (y + 16), e, 10))
    t.append(txt(320, 202, "La frise n'est pas à l'échelle.", 10, "#4a3d2e"))
    t.append("</svg>")
    return "".join(t)
