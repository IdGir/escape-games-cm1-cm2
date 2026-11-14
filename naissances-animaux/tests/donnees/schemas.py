# -*- coding: utf-8 -*-
"""Schémas SVG du jeu « La Nurserie du zoo », tracés par script (jamais par IA) : fécondation, coupe de l'œuf,
milieux de fécondation, tableau à deux entrées, frise du poussin, durées de gestation."""

POLICE = "font-family='Atkinson Hyperlegible,Arial,sans-serif'"
STYLE = "style='max-width:100%;height:auto;display:block;margin:10px auto'"
FOND, ENCRE = "#f3f7ee", "#1f2a1c"


def repere(x, y, n, couleur="#b03a2e"):
    return (f"<circle cx='{x}' cy='{y}' r='13' fill='{couleur}' stroke='#fff' stroke-width='2'/>"
            f"<text x='{x}' y='{y + 5}' text-anchor='middle' font-size='14' font-weight='700' fill='#fff' {POLICE}>{n}</text>")


def txt(x, y, s, taille=12, coul=ENCRE, gras=False, ancre="middle", ital=False):
    return (f"<text x='{x}' y='{y}' text-anchor='{ancre}' font-size='{taille}'" + (" font-weight='700'" if gras else "")
            + (" font-style='italic'" if ital else "") + f" fill='{coul}' {POLICE}>{s}</text>")


def cadre(titre, h=300, w=640):
    return [f"<svg viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg' role='img' aria-label=\"{titre}\" {STYLE}>",
            f"<rect width='{w}' height='{h}' rx='12' fill='{FOND}'/>", txt(w / 2, 24, titre, 15, gras=True)]


def fleche(x1, y, x2):
    return (f"<line x1='{x1}' y1='{y}' x2='{x2 - 8}' y2='{y}' stroke='{ENCRE}' stroke-width='3'/>"
            f"<polygon points='{x2},{y} {x2 - 10},{y - 6} {x2 - 10},{y + 6}' fill='{ENCRE}'/>")


def _sperma(x, y, s=1.0):
    return (f"<ellipse cx='{x}' cy='{y}' rx='{7 * s}' ry='{5 * s}' fill='#5b7db1' stroke='{ENCRE}'/>"
            f"<path d='M{x - 7 * s},{y} q-10,-8 -20,0 t-20,0' fill='none' stroke='#5b7db1' stroke-width='2'/>")


def _ovule(x, y, r=34, noyau=True):
    return (f"<circle cx='{x}' cy='{y}' r='{r}' fill='#f6d7a7' stroke='{ENCRE}' stroke-width='2'/>"
            + (f"<circle cx='{x + 4}' cy='{y - 3}' r='{r * .3}' fill='#d99a3c' stroke='{ENCRE}'/>" if noyau else ""))


def _embryon(x, y):
    out = [f"<circle cx='{x}' cy='{y}' r='34' fill='#f6d7a7' stroke='{ENCRE}' stroke-width='2'/>"]
    for dx, dy in [(-12, -12), (12, -12), (-12, 12), (12, 12), (0, 0), (0, -22), (0, 22), (-22, 0), (22, 0)]:
        out.append(f"<circle cx='{x + dx}' cy='{y + dy}' r='9' fill='#eab676' stroke='{ENCRE}'/>")
    return "".join(out)


def schema_fecondation(n, titre="De deux cellules à un embryon", legendes=False):
    """Repères : 1 gamète mâle, 2 gamète femelle, 3 cellule-œuf, 4 embryon, 5 flagelle."""
    o = cadre(titre, 250)
    o += [_sperma(95, 120, 1.3), _ovule(160, 130), fleche(205, 130, 265), _ovule(320, 130), fleche(365, 130, 425), _embryon(480, 130)]
    o += [txt(160, 200, "rencontre", 12, ital=True), txt(320, 200, "fusion", 12, ital=True), txt(480, 200, "divisions", 12, ital=True)]
    pos = [(80, 92), (160, 80), (320, 80), (480, 80), (40, 140)]
    for i in range(n):
        o.append(repere(*pos[i], i + 1))
    o.append(txt(320, 236, "Dessin simplifié : les cellules sont invisibles à l'œil nu (tailles non respectées).", 11, ital=True))
    return "".join(o) + "</svg>"


def coupe_oeuf(n, titre="Coupe d'un œuf de poule fécondé"):
    """Repères : 1 coquille, 2 jaune, 3 blanc, 4 chambre à air, 5 embryon."""
    o = cadre(titre, 300)
    o += ["<ellipse cx='320' cy='165' rx='170' ry='118' fill='#f7f1e3' stroke='#8c6d46' stroke-width='9'/>",
          "<ellipse cx='320' cy='165' rx='158' ry='106' fill='#fbfdf5' stroke='#d8d2b8' stroke-width='2'/>",
          "<path d='M465,120 q22,45 0,90 q-26,-45 0,-90z' fill='#e6eef7' stroke='#8c9fb5' stroke-width='2'/>",
          "<circle cx='300' cy='168' r='55' fill='#f2b632' stroke='#b37d10' stroke-width='3'/>",
          "<path d='M286,124 q14,-12 26,0 q-4,12 -13,12 q-10,0 -13,-12z' fill='#d1495b' stroke='#7a1f2b'/>"]
    pos = [(156, 90), (300, 205), (395, 250), (520, 165), (299, 108)]
    for i in range(n):
        o.append(repere(*pos[i], i + 1))
    return "".join(o) + "</svg>"


def lecon_fecondation():
    return schema_fecondation(0, "La fécondation", True).replace("</svg>", "") + "".join([
        txt(95, 172, "spermatozoïde", 11, gras=True), txt(160, 80, "ovule", 11, gras=True), txt(320, 80, "cellule-œuf", 11, gras=True),
        txt(480, 80, "embryon", 11, gras=True)]) + "</svg>"


def lecon_milieux():
    o = cadre("Où se rencontrent les gamètes ?", 230)
    o += ["<rect x='30' y='45' width='280' height='150' rx='10' fill='#cfe6f3' stroke='#4a7aa0'/>",
          "<rect x='330' y='45' width='280' height='150' rx='10' fill='#f6e0d0' stroke='#a0644a'/>",
          txt(170, 70, "Fécondation externe : dans l'eau", 13, gras=True), txt(470, 70, "Fécondation interne : dans le corps", 13, gras=True)]
    for i in range(9):
        o.append(f"<circle cx='{70 + (i % 5) * 45}' cy='{110 + (i // 5) * 40}' r='9' fill='#f6d7a7' stroke='{ENCRE}'/>")
    o += [_sperma(120, 132, .8), _sperma(220, 100, .8), _sperma(260, 148, .8)]
    o += ["<ellipse cx='470' cy='130' rx='90' ry='45' fill='#f9ece2' stroke='#a0644a' stroke-width='2'/>", _ovule(470, 130, 18), _sperma(430, 125, .8)]
    o += [txt(170, 215, "grenouille, crapaud, truite, saumon", 12, ital=True), txt(470, 215, "oiseaux, reptiles, mammifères, requins", 12, ital=True)]
    return "".join(o) + "</svg>"


def lecon_tableau():
    o = cadre("Fécondation et mode de reproduction", 250)
    cols, lig = ["", "ovipare (pond)", "vivipare (naît vivant)"], ["fécondation externe", "fécondation interne"]
    cel = [["grenouille, truite", "aucun"], ["poule, crocodile, papillon", "chat, vache, dauphin"]]
    for j, c in enumerate(cols):
        o.append(txt(110 + j * 210, 66, c, 13, gras=True))
    for i, l in enumerate(lig):
        y = 85 + i * 75
        o.append(f"<rect x='20' y='{y}' width='600' height='68' rx='8' fill='#fff' stroke='#9db08a'/>")
        o.append(txt(110, y + 40, l, 12, gras=True))
        for j, v in enumerate(cel[i]):
            o.append(txt(320 + j * 210, y + 40, v, 12, ital=(v == "aucun")))
    o.append(txt(320, 240, "Exceptions : l'ornithorynque pond ; la vipère aspic garde ses œufs dans son ventre.", 11, ital=True))
    return "".join(o) + "</svg>"


def lecon_poussin():
    o = cadre("21 jours de couvaison", 200)
    o.append("<line x1='40' y1='110' x2='600' y2='110' stroke='#7a5c0c' stroke-width='5' stroke-linecap='round'/>")
    for j, t in [(1, "jaune seul"), (3, "le cœur bat"), (7, "forme du poussin"), (18, "plumes"), (21, "éclosion")]:
        x = 40 + (j - 1) * 28
        o += [f"<circle cx='{x}' cy='110' r='9' fill='#f2b632' stroke='#7a5c0c' stroke-width='2'/>", txt(x, 92, f"jour {j}", 12, gras=True), txt(x, 140, t, 11)]
    return "".join(o) + "</svg>"


def lecon_gestation():
    data = [("lapine", 31), ("chatte", 64), ("vache", 280), ("jument", 336), ("éléphante", 640)]
    o = cadre("Durée de la gestation (en jours, valeurs moyennes)", 260)
    for i, (nom, j) in enumerate(data):
        y = 55 + i * 38
        o += [txt(120, y + 17, nom, 13, ancre="end"), f"<rect x='130' y='{y}' width='{j * 0.7:.0f}' height='24' rx='5' fill='#6a994e'/>",
              txt(138 + j * 0.7, y + 17, str(j) if nom != "éléphante" else "600 à 660", 12, ancre="start", gras=True)]
    o.append(txt(320, 250, "chatte : 63 à 65 jours ; éléphante : 20 à 22 mois.", 11, ital=True))
    return "".join(o) + "</svg>"


def lecon_classe():
    return lecon_tableau().replace("Fécondation et mode de reproduction", "Le carnet de naissance du zoo")
