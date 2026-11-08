# -*- coding: utf-8 -*-
"""Schémas SVG du jeu « Le Grand Prix de l'observatoire », dessinés par script (jamais par IA)."""

POLICE = "font-family='Atkinson Hyperlegible,Arial,sans-serif'"
STYLE = "style='max-width:100%;height:auto;display:block;margin:10px auto'"


def repere(x, y, n, couleur="#c0392b"):
    return (f"<circle cx='{x}' cy='{y}' r='13' fill='{couleur}' stroke='#fff' stroke-width='2'/>"
            f"<text x='{x}' y='{y + 5}' text-anchor='middle' font-size='14' font-weight='700' fill='#fff' {POLICE}>{n}</text>")


def txt(x, y, s, taille=12, coul="#24361d", gras=False, ancre="middle"):
    return (f"<text x='{x}' y='{y}' text-anchor='{ancre}' font-size='{taille}'" + (" font-weight='700'" if gras else "")
            + f" fill='{coul}' {POLICE}>{s}</text>")


def ruban(debut, fin, total=20, titre="Le décamètre de Margaux"):
    """Ruban gradué de 0 à `total` m ; drapeau vert au départ, damier à l'arrivée."""
    l, x0, w = 640, 40, 560
    pas = w / total
    t = [f"<svg viewBox='0 0 {l} 170' xmlns='http://www.w3.org/2000/svg' role='img' aria-label=\"{titre}\" {STYLE}>",
         f"<rect x='0' y='0' width='{l}' height='170' rx='12' fill='#f4f7ec'/>", txt(l / 2, 22, titre, 15, gras=True),
         f"<rect x='{x0 - 6}' y='92' width='{w + 12}' height='34' rx='4' fill='#f7d04a' stroke='#8a6d0b'/>"]
    for i in range(total + 1):
        x = x0 + i * pas
        t.append(f"<line x1='{x:.1f}' y1='92' x2='{x:.1f}' y2='{116 if i % 5 == 0 else 110}' stroke='#3a2f05' stroke-width='{2 if i % 5 == 0 else 1}'/>")
        t.append(txt(f"{x:.1f}", 142, i, 12, "#3a2f05"))
    t.append(txt(x0 + w + 4, 162, "graduations en mètres (m)", 11, "#3a2f05", ancre="end"))
    xd, xa = x0 + debut * pas, x0 + fin * pas
    t.append(f"<line x1='{xd}' y1='40' x2='{xd}' y2='92' stroke='#2d7d55' stroke-width='3'/><polygon points='{xd},40 {xd + 28},48 {xd},56' fill='#2d7d55'/>")
    t.append(txt(xd, 34, "départ", 12, "#2d7d55", True))
    t.append(f"<line x1='{xa}' y1='40' x2='{xa}' y2='92' stroke='#222' stroke-width='3'/>")
    for r in range(2):
        for c in range(3):
            t.append(f"<rect x='{xa + c * 9}' y='{40 + r * 8}' width='9' height='8' fill='{'#222' if (r + c) % 2 == 0 else '#fff'}' stroke='#222' stroke-width='.5'/>")
    t.append(txt(xa, 34, "arrivée", 12, "#222", True))
    t.append("</svg>")
    return "".join(t)


def rubans_report(n, reste):
    """CM2 : le décamètre (10 m) déroulé n fois en entier, puis `reste` mètres."""
    l = 640
    w = 540 / (n + 1)
    t = [f"<svg viewBox='0 0 {l} 150' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Les reports du décamètre' {STYLE}>",
         f"<rect width='{l}' height='150' rx='12' fill='#f4f7ec'/>", txt(l / 2, 22, "La piste mesurée avec un décamètre de 10 m", 15, gras=True)]
    x = 40
    for i in range(n):
        t.append(f"<rect x='{x:.1f}' y='60' width='{w - 4:.1f}' height='30' rx='3' fill='#f7d04a' stroke='#8a6d0b'/>"
                 + txt(f"{x + w / 2 - 2:.1f}", 80, "10 m", 13, "#3a2f05", True) + txt(f"{x + w / 2 - 2:.1f}", 110, f"report {i + 1}", 12, "#3a2f05"))
        x += w
    wr = w * reste / 10
    t.append(f"<rect x='{x:.1f}' y='60' width='{wr:.1f}' height='30' rx='3' fill='#fbe79a' stroke='#8a6d0b' stroke-dasharray='4 3'/>"
             + txt(f"{x + wr / 2:.1f}", 80, "?", 14, "#3a2f05", True) + txt(f"{x + wr / 2:.1f}", 110, "fin", 12, "#3a2f05"))
    t.append(f"<polygon points='40,40 64,47 40,54' fill='#2d7d55'/><line x1='40' y1='40' x2='40' y2='60' stroke='#2d7d55' stroke-width='3'/>"
             f"<line x1='{x + wr:.1f}' y1='40' x2='{x + wr:.1f}' y2='60' stroke='#222' stroke-width='3'/>"
             + txt(40, 134, "départ", 12, "#3a2f05", ancre="start") + txt(f"{x + wr:.1f}", 134, "arrivée", 12, "#3a2f05", ancre="end") + "</svg>")
    return "".join(t)


def circuit():
    """CM1 : le circuit du Grand Prix vu d'en haut, 3 repères (ligne droite, virage, manège)."""
    trace = "M60 230 L330 230 Q420 230 430 160 Q440 90 560 90"
    return (f"<svg viewBox='0 0 640 300' xmlns='http://www.w3.org/2000/svg' role='img' aria-label=\"Le circuit vu du haut de l'observatoire\" {STYLE}>"
            "<rect width='640' height='300' rx='12' fill='#dfeccf'/>" + txt(320, 24, "Le circuit vu du haut de l'observatoire", 15, gras=True)
            + f"<path d='{trace}' fill='none' stroke='#6b6b6b' stroke-width='26' stroke-linecap='round'/>"
            + f"<path d='{trace}' fill='none' stroke='#fff' stroke-width='2' stroke-dasharray='10 8'/>"
            + "<line x1='60' y1='215' x2='60' y2='245' stroke='#2d7d55' stroke-width='5'/>"
            + "<circle cx='150' cy='110' r='55' fill='none' stroke='#b06a2b' stroke-width='5' stroke-dasharray='6 5'/>"
            + "<circle cx='150' cy='110' r='14' fill='#b06a2b'/><circle cx='205' cy='110' r='9' fill='#e8a33d' stroke='#6b3f12'/>"
            + txt(150, 186, "le manège", 12) + txt(70, 270, "départ", 12, "#2d7d55", True)
            + repere(200, 262, 1) + repere(466, 150, 2) + repere(240, 70, 3) + "</svg>")


def systeme_solaire():
    """CM2 : le Soleil et les trois premières planètes (distances non respectées), 4 repères."""
    t = [f"<svg viewBox='0 0 640 320' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Le Soleil et les trois premières planètes' {STYLE}>",
         "<rect width='640' height='320' rx='12' fill='#10172e'/>", txt(320, 24, "Le Soleil et les trois premières planètes", 15, "#ffe9a8", True),
         txt(320, 308, "Schéma : les tailles et les distances ne sont pas respectées.", 11, "#c9d3f5")]
    cx, cy = 320, 165
    for r in (55, 90, 125):
        t.append(f"<ellipse cx='{cx}' cy='{cy}' rx='{r * 1.6:.0f}' ry='{r:.0f}' fill='none' stroke='#6f7fb8' stroke-width='{3 if r == 125 else 1.2}'/>")
    t.append(f"<circle cx='{cx}' cy='{cy}' r='26' fill='#ffcc33' stroke='#ff9f1a' stroke-width='4'/>")
    t.append(f"<circle cx='{cx + 88}' cy='{cy}' r='6' fill='#b9aca0'/>")
    t.append(f"<circle cx='{cx - 102}' cy='{cy - 55}' r='9' fill='#e9c27a'/>")
    t.append(f"<circle cx='{cx + 141}' cy='{cy + 92}' r='11' fill='#3b82c4' stroke='#7ec26b' stroke-width='3'/>")
    t.append(repere(cx - 34, cy - 32, 1) + repere(cx + 88, cy - 24, 2) + repere(cx + 166, cy + 112, 3) + repere(cx - 200, cy, 4))
    t.append("</svg>")
    return "".join(t)


# ---------------------------------------------------------------- schémas des leçons
def lecon_distance():
    return ruban(4, 16, 20, "Distance parcourue : de la ligne de départ à la ligne d'arrivée")


def lecon_duree():
    return (f"<svg viewBox='0 0 640 175' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Une durée entre deux instants' {STYLE}>"
            "<rect width='640' height='175' rx='12' fill='#eef3fb'/>" + txt(320, 24, "Une durée est l'intervalle entre deux instants", 15, "#1d2f52", True)
            + "<line x1='50' y1='95' x2='600' y2='95' stroke='#1d2f52' stroke-width='3'/><polygon points='600,88 615,95 600,102' fill='#1d2f52'/>"
            + "<circle cx='170' cy='95' r='8' fill='#2d7d55'/><circle cx='470' cy='95' r='8' fill='#c0392b'/>"
            + txt(170, 70, "instant du départ", 13, "#2d7d55", True) + txt(170, 122, "10 h 15 min", 13, "#1d2f52")
            + txt(470, 70, "instant de l'arrivée", 13, "#c0392b", True) + txt(470, 122, "10 h 40 min", 13, "#1d2f52")
            + "<path d='M178 135 Q320 160 462 135' fill='none' stroke='#e08a1e' stroke-width='3'/>"
            + txt(320, 166, "durée : 25 min", 13, "#a85f12", True) + "</svg>")


def lecon_comparer():
    lignes = [("Salomé à vélo", 40, "#2d7d55"), ("Yanis en caisse à savon", 55, "#1f6a8f"), ("Mila à pied", 150, "#a85f12")]
    t = [f"<svg viewBox='0 0 640 190' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Même distance, durées différentes' {STYLE}>",
         "<rect width='640' height='190' rx='12' fill='#f6f1e8'/>", txt(320, 24, "Même distance (200 m) : le plus rapide met le moins de temps", 14, "#4a2f12", True)]
    for i, (nom, s, c) in enumerate(lignes):
        y = 50 + i * 42
        t.append(txt(20, y + 17, nom, 13, "#4a2f12", ancre="start") + f"<rect x='200' y='{y}' width='{s * 2.6:.0f}' height='24' rx='4' fill='{c}'/>"
                 + txt(f"{208 + s * 2.6:.0f}", y + 17, f"{s} s", 13, "#4a2f12", True, "start"))
    t.append(txt(320, 182, "Durées inventées pour le jeu.", 11, "#6b5a44") + "</svg>")
    return "".join(t)


def lecon_trajectoires():
    return (f"<svg viewBox='0 0 640 180' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Trois formes de trajectoire' {STYLE}>"
            "<rect width='640' height='180' rx='12' fill='#eef3fb'/>" + txt(320, 24, "Trois formes de trajectoire", 15, "#1d2f52", True)
            + "<line x1='30' y1='105' x2='190' y2='105' stroke='#1f6a8f' stroke-width='4' stroke-dasharray='8 6'/><circle cx='190' cy='105' r='9' fill='#1f6a8f'/>"
            + txt(110, 160, "rectiligne (droite)", 13, "#1d2f52", True)
            + "<circle cx='320' cy='100' r='42' fill='none' stroke='#c0392b' stroke-width='4' stroke-dasharray='8 6'/><circle cx='362' cy='100' r='9' fill='#c0392b'/>"
            + txt(320, 160, "circulaire (cercle)", 13, "#1d2f52", True)
            + "<path d='M450 130 Q490 50 540 100 T620 70' fill='none' stroke='#2d7d55' stroke-width='4' stroke-dasharray='8 6'/><circle cx='620' cy='70' r='9' fill='#2d7d55'/>"
            + txt(535, 160, "curviligne (courbe)", 13, "#1d2f52", True) + "</svg>")


def lecon_observateur():
    return (f"<svg viewBox='0 0 640 200' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Le même voyageur vu par deux observateurs' {STYLE}>"
            "<rect width='640' height='200' rx='12' fill='#f4f7ec'/>" + txt(320, 22, "Le même voyageur, vu par deux observateurs", 15, gras=True)
            + "<rect x='0' y='150' width='640' height='14' fill='#8d8d8d'/><rect x='0' y='164' width='640' height='36' fill='#c9b48a'/>"
            + "<rect x='170' y='70' width='300' height='70' rx='10' fill='#c0392b'/>"
            + "".join(f"<rect x='{x}' y='82' width='60' height='34' fill='#d9eef8'/>" for x in (190, 270, 350))
            + "<circle cx='300' cy='96' r='8' fill='#f0c9ad'/><rect x='292' y='104' width='16' height='12' fill='#1f6a8f'/>"
            + "<circle cx='220' cy='96' r='8' fill='#7a4e34'/><rect x='212' y='104' width='16' height='12' fill='#2d7d55'/>"
            + "<circle cx='200' cy='146' r='10' fill='#333'/><circle cx='440' cy='146' r='10' fill='#333'/>"
            + "<polygon points='480,105 520,105 520,95 545,110 520,125 520,115 480,115' fill='#1d2f52'/>"
            + "<circle cx='80' cy='120' r='9' fill='#f0c9ad'/><rect x='72' y='129' width='16' height='22' fill='#e08a1e'/>"
            + txt(80, 50, "pour la personne", 12) + txt(80, 64, "sur le quai :", 12) + txt(80, 80, "il bouge", 12, "#c0392b", True)
            + txt(300, 50, "pour son voisin assis :", 12) + txt(300, 64, "il est immobile", 12, "#2d7d55", True) + "</svg>")
