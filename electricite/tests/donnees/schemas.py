# -*- coding: utf-8 -*-
"""Dessins et schémas SVG du jeu « La Centrale en panne », tracés par script (jamais par IA).
Symboles normalisés simplifiés (pile, lampe, moteur, interrupteur) ; dessins réalistes stylisés."""

POLICE = "font-family='Atkinson Hyperlegible,Arial,sans-serif'"
STYLE = "style='max-width:100%;height:auto;display:block;margin:10px auto'"
FOND, ENCRE, FIL, CUIVRE = "#eef3f7", "#1d2733", "#2b3440", "#c47a2c"


def repere(x, y, n, couleur="#c0392b"):
    return (f"<circle cx='{x}' cy='{y}' r='13' fill='{couleur}' stroke='#fff' stroke-width='2'/>"
            f"<text x='{x}' y='{y + 5}' text-anchor='middle' font-size='14' font-weight='700' fill='#fff' {POLICE}>{n}</text>")


def txt(x, y, s, taille=12, coul=ENCRE, gras=False, ancre="middle", ital=False):
    return (f"<text x='{x}' y='{y}' text-anchor='{ancre}' font-size='{taille}'" + (" font-weight='700'" if gras else "")
            + (" font-style='italic'" if ital else "") + f" fill='{coul}' {POLICE}>{s}</text>")


def _cadre(titre, h=360):
    return [f"<svg viewBox='0 0 640 {h}' xmlns='http://www.w3.org/2000/svg' role='img' aria-label=\"{titre}\" {STYLE}>",
            f"<rect width='640' height='{h}' rx='12' fill='{FOND}'/>", txt(320, 24, titre, 15, gras=True)]


def ligne(x1, y1, x2, y2, coul=FIL, larg=3):
    return f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{coul}' stroke-width='{larg}' stroke-linecap='round'/>"


# ---------------------------------------------------------------- symboles normalisés (centrés en x, y)
def sym_pile_v(x, y):
    """Pile verticale : grand trait (borne +) en haut, petit trait (borne −) en bas ; fils au-dessus et au-dessous."""
    return (f"<rect x='{x - 30}' y='{y - 10}' width='60' height='20' fill='{FOND}'/>" + ligne(x - 26, y - 6, x + 26, y - 6, ENCRE, 4)
            + ligne(x - 13, y + 6, x + 13, y + 6, ENCRE, 7) + txt(x + 38, y - 2, "+", 15, gras=True) + txt(x + 38, y + 14, "−", 15, gras=True))


def sym_lampe(x, y, r=16):
    return (f"<circle cx='{x}' cy='{y}' r='{r}' fill='#fff' stroke='{ENCRE}' stroke-width='3'/>"
            + ligne(x - r * .7, y - r * .7, x + r * .7, y + r * .7, ENCRE, 3) + ligne(x - r * .7, y + r * .7, x + r * .7, y - r * .7, ENCRE, 3))


def sym_moteur(x, y, r=16):
    return f"<circle cx='{x}' cy='{y}' r='{r}' fill='#fff' stroke='{ENCRE}' stroke-width='3'/>" + txt(x, y + 6, "M", 17, gras=True)


def sym_inter_h(x, y, ouvert=True):
    """Interrupteur sur un fil horizontal (de x-24 à x+24)."""
    t = f"<rect x='{x - 24}' y='{y - 4}' width='48' height='8' fill='{FOND}'/>"
    t += f"<circle cx='{x - 22}' cy='{y}' r='3.5' fill='{ENCRE}'/><circle cx='{x + 22}' cy='{y}' r='3.5' fill='{ENCRE}'/>"
    t += ligne(x - 22, y, x + 16, y - 20, ENCRE, 3) if ouvert else ligne(x - 22, y, x + 22, y, ENCRE, 3)
    return t


# ---------------------------------------------------------------- dessin réaliste d'un montage (salle 1)
def _pile_plate(x, y):
    return (f"<rect x='{x}' y='{y}' width='110' height='70' rx='6' fill='#1f6fb2' stroke='{ENCRE}' stroke-width='2'/>"
            f"<rect x='{x}' y='{y + 46}' width='110' height='24' rx='4' fill='#f2c230' stroke='{ENCRE}' stroke-width='2'/>"
            + txt(x + 55, y + 34, "4,5 V", 15, "#fff", gras=True)
            + f"<rect x='{x + 22}' y='{y - 26}' width='12' height='28' fill='#b9bfc6' stroke='{ENCRE}'/>"
            + f"<rect x='{x + 74}' y='{y - 34}' width='12' height='36' fill='#b9bfc6' stroke='{ENCRE}'/>")


def _lampe_douille(x, y, allumee=False):
    halo = f"<circle cx='{x}' cy='{y - 30}' r='34' fill='#ffe066' opacity='.55'/>" if allumee else ""
    return (halo + f"<circle cx='{x}' cy='{y - 30}' r='20' fill='{'#fff4b0' if allumee else '#f4f6f8'}' stroke='{ENCRE}' stroke-width='2'/>"
            f"<path d='M{x - 6} {y - 26} Q{x} {y - 40} {x + 6} {y - 26}' fill='none' stroke='#7a5a2a' stroke-width='2'/>"
            f"<rect x='{x - 12}' y='{y - 12}' width='24' height='16' fill='#b9bfc6' stroke='{ENCRE}'/>"
            f"<rect x='{x - 30}' y='{y + 4}' width='60' height='18' rx='3' fill='#6b4f3a' stroke='{ENCRE}'/>")


def _interrupteur(x, y, ouvert=True):
    t = f"<rect x='{x - 40}' y='{y}' width='80' height='16' rx='3' fill='#6b4f3a' stroke='{ENCRE}'/>"
    t += f"<circle cx='{x - 28}' cy='{y}' r='5' fill='#b9bfc6' stroke='{ENCRE}'/><circle cx='{x + 28}' cy='{y}' r='5' fill='#b9bfc6' stroke='{ENCRE}'/>"
    t += (ligne(x - 28, y - 2, x + 20, y - 26, '#8a9099', 6) if ouvert else ligne(x - 28, y - 2, x + 28, y - 2, '#8a9099', 6))
    return t


def dessin_montage(nb=3, titre="Le montage de Nour", avec_noms=False, ouvert=True):
    """Salle 1 : 1 pile, 2 lampe, 3 interrupteur ; CM2 : 4 fil de connexion, 5 borne de la pile (lame)."""
    t = _cadre(titre, 330)
    t.append(_pile_plate(90, 182))
    t.append(_lampe_douille(480, 140, allumee=not ouvert))
    t.append(_interrupteur(300, 270, ouvert))
    t.append(f"<path d='M174 166 L174 110 L455 110 L455 150' fill='none' stroke='{CUIVRE}' stroke-width='4' stroke-linejoin='round'/>")
    t.append(f"<path d='M505 150 L540 150 L540 270 L333 270' fill='none' stroke='{CUIVRE}' stroke-width='4' stroke-linejoin='round'/>")
    t.append(f"<path d='M267 270 L50 270 L50 150 L118 150 L118 174' fill='none' stroke='{CUIVRE}' stroke-width='4' stroke-linejoin='round'/>")
    if avec_noms:
        t += [txt(145, 292, "pile plate", 12, gras=True), txt(480, 196, "lampe sur sa douille", 12, gras=True),
              txt(300, 305, "interrupteur", 12, gras=True), txt(320, 100, "fil de connexion", 12, gras=True), txt(206, 160, "borne", 12, gras=True)]
    pos = [(222, 240), (530, 100), (300, 235), (330, 110), (200, 175)]
    for i in range(nb):
        t.append(repere(*pos[i], i + 1))
    t.append(txt(320, 324, "Dessin simplifié." + (" Interrupteur ouvert." if ouvert else " Interrupteur fermé."), 11, "#4a5560"))
    t.append("</svg>")
    return "".join(t)


# ---------------------------------------------------------------- schéma normalisé (salle 3)
def schema_normalise(nb=3, titre="Le schéma du pupitre", avec_noms=False, ouvert=True):
    """Rectangle : pile à gauche (+ en haut), interrupteur en haut, lampe à droite, moteur en bas.
    Repères : 1 pile, 2 interrupteur, 3 lampe, 4 moteur, 5 fil de connexion."""
    t = _cadre(titre, 320)
    x1, y1, x2, y2 = 150, 80, 490, 260
    t.append(f"<rect x='{x1}' y='{y1}' width='{x2 - x1}' height='{y2 - y1}' fill='none' stroke='{FIL}' stroke-width='3'/>")
    t.append(sym_pile_v(x1, (y1 + y2) // 2))
    t.append(sym_inter_h((x1 + x2) // 2, y1, ouvert))
    t.append(f"<rect x='{x2 - 4}' y='{(y1 + y2) // 2 - 18}' width='8' height='36' fill='{FOND}'/>" + sym_lampe(x2, (y1 + y2) // 2))
    t.append(f"<rect x='{(x1 + x2) // 2 - 18}' y='{y2 - 4}' width='36' height='8' fill='{FOND}'/>" + sym_moteur((x1 + x2) // 2, y2))
    if avec_noms:
        t += [txt(x1 - 50, (y1 + y2) // 2 + 4, "pile", 12, gras=True, ancre="end"), txt((x1 + x2) // 2, y1 - 26, "interrupteur " + ("ouvert" if ouvert else "fermé"), 12, gras=True),
              txt(x2 + 26, (y1 + y2) // 2 + 4, "lampe", 12, gras=True, ancre="start"), txt((x1 + x2) // 2, y2 + 34, "moteur", 12, gras=True),
              txt(x2 - 60, y1 - 8, "fil", 12, gras=True)]
    pos = [(x1 - 62, (y1 + y2) // 2), ((x1 + x2) // 2, y1 - 34), (x2 + 40, (y1 + y2) // 2), ((x1 + x2) // 2 + 44, y2 + 22), (x2 - 60, y1 - 18)]
    for i in range(nb):
        t.append(repere(*pos[i], i + 1, "#1f6fb2"))
    t.append(txt(320, 312, "Schéma normalisé : on suit le courant de la borne + à la borne −.", 11, "#4a5560"))
    t.append("</svg>")
    return "".join(t)


# ---------------------------------------------------------------- de la centrale à la prise (salle 5)
def schema_reseau(nb=0, titre="De la centrale à la prise", avec_noms=True):
    t = _cadre(titre, 300)
    t.append(f"<rect x='20' y='150' width='90' height='70' fill='#9aa5b1' stroke='{ENCRE}'/><path d='M40 150 Q50 100 70 150 Z' fill='#cfd6dd' stroke='{ENCRE}'/>"
             f"<rect x='80' y='110' width='14' height='40' fill='#7a858f' stroke='{ENCRE}'/>")
    t.append(f"<rect x='140' y='170' width='40' height='50' fill='#5d6d7e' stroke='{ENCRE}'/>")
    for px in (240, 330, 420):
        t.append(f"<path d='M{px} 220 L{px + 12} 110 L{px + 24} 220 M{px + 4} 180 L{px + 20} 180 M{px - 6} 125 L{px + 30} 125' fill='none' stroke='{ENCRE}' stroke-width='2'/>")
    t.append(f"<path d='M180 185 Q210 135 246 125 Q290 140 336 125 Q380 140 426 125 Q455 140 470 175' fill='none' stroke='{FIL}' stroke-width='2'/>")
    t.append(f"<rect x='465' y='175' width='36' height='45' fill='#5d6d7e' stroke='{ENCRE}'/>")
    t.append(f"<path d='M501 200 L540 200' stroke='{FIL}' stroke-width='2'/><path d='M540 220 L540 175 L570 150 L600 175 L600 220 Z' fill='#e9d8b4' stroke='{ENCRE}'/>"
             f"<rect x='563' y='195' width='14' height='25' fill='#8a5a32'/>")
    if avec_noms:
        noms = [(65, 240, "centrale"), (160, 240, "transformateur"), (335, 240, "lignes à très haute tension"), (483, 240, "poste"), (570, 240, "maison")]
        t += [txt(x, y, s, 12, gras=True) for x, y, s in noms]
        t.append(txt(320, 270, "Le transformateur élève la tension ; le poste l'abaisse ; le réseau de distribution va jusqu'au compteur.", 11, "#4a5560"))
    t.append("</svg>")
    return "".join(t)


# ---------------------------------------------------------------- schémas des leçons
def lecon_circuit():
    return dessin_montage(0, "Un circuit fermé : la lampe brille", avec_noms=True, ouvert=False)


def lecon_conducteurs():
    t = _cadre("Le circuit testeur", 300)
    t.append(_pile_plate(70, 170))
    t.append(_lampe_douille(470, 120, allumee=True))
    t.append(f"<path d='M154 136 L154 70 L445 70 L445 130' fill='none' stroke='{CUIVRE}' stroke-width='4'/>")
    t.append(f"<path d='M495 130 L540 130 L540 240 L380 240' fill='none' stroke='{CUIVRE}' stroke-width='4'/><path d='M98 150 L98 130 L40 130 L40 240 L260 240' fill='none' stroke='{CUIVRE}' stroke-width='4'/>")
    t.append("<rect x='262' y='232' width='116' height='16' rx='4' fill='#b9bfc6' stroke='#1d2733'/>")
    t += [txt(320, 225, "objet à tester (ici une clé en fer)", 12, gras=True), txt(470, 190, "la lampe brille : conducteur", 12, gras=True),
          txt(320, 280, "Si la lampe reste éteinte, l'objet est isolant.", 12, "#4a5560")]
    t.append("</svg>")
    return "".join(t)


def lecon_symboles():
    t = _cadre("Les symboles normalisés", 260)
    cases = [(90, "pile", ligne(90, 92, 90, 114) + ligne(90, 126, 90, 148) + sym_pile_v(90, 120)), (220, "lampe", sym_lampe(220, 120)), (340, "moteur", sym_moteur(340, 120)),
             (460, "interrupteur ouvert", ligne(420, 120, 436, 120) + sym_inter_h(460, 120, True) + ligne(484, 120, 500, 120)),
             (580, "interrupteur fermé", ligne(540, 120, 556, 120) + sym_inter_h(580, 120, False) + ligne(604, 120, 620, 120))]
    for x, nom, s in cases:
        t.append(s)
        t.append(txt(x, 190, nom, 12, gras=True))
    t.append(ligne(60, 228, 140, 228))
    t.append(txt(250, 232, "fil de connexion : un trait droit", 12, ancre="start"))
    t.append("</svg>")
    return "".join(t)


def lecon_securite():
    t = _cadre("Pile ou secteur ?", 250)
    t.append(_pile_plate(80, 110))
    t.append(txt(135, 215, "pile plate 4,5 V : sans danger", 13, "#2f6b4a", gras=True))
    t.append("<rect x='420' y='80' width='110' height='110' rx='16' fill='#f4f6f8' stroke='#1d2733' stroke-width='2'/>"
             "<circle cx='455' cy='135' r='8' fill='#1d2733'/><circle cx='495' cy='135' r='8' fill='#1d2733'/>")
    t.append("<path d='M560 70 L600 140 L520 140 Z' fill='#f2c230' stroke='#1d2733' stroke-width='2'/>" + txt(560, 132, "!", 30, gras=True))
    t.append(txt(475, 215, "prise du secteur 230 V : DANGER", 13, "#9a2a1a", gras=True))
    t.append("</svg>")
    return "".join(t)


def lecon_reseau():
    return schema_reseau()
