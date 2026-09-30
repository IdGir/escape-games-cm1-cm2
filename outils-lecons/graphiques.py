# -*- coding: utf-8 -*-
"""Graphiques et schémas SVG pour les leçons imprimables (A4).

Toutes les fonctions renvoient une chaîne <svg …>. La taille du texte est
calculée pour la largeur imprimée visée (cible_mm) : environ 7,5 points à
l'impression, quelle que soit la largeur du dessin en pixels.
Colonne de droite d'une leçon ≈ 66 mm ; pleine largeur ≈ 186 mm.
"""
from html import escape as _e

POLICE = "Segoe UI, Helvetica, Arial, sans-serif"
PALETTE = ["#2f6690", "#c0392b", "#d68910", "#1e8449", "#7d3c98", "#566573"]


def taille(W, cible_mm):
    return 2.6 * W / cible_mm


def e(t):
    return _e(str(t), quote=False)


def ouvrir(W, H, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" role="img" '
            f'aria-label="{_e(label)}" font-family="{POLICE}">')


def texte(x, y, t, fs, anchor="middle", fill="#1f2328", poids=400, italique=False, extra=""):
    lignes = str(t).split("\n")
    it = ' font-style="italic"' if italique else ""
    out = []
    for k, ln in enumerate(lignes):
        out.append(f'<text x="{x:.1f}" y="{y + k * fs * 1.15:.1f}" font-size="{fs:.1f}" text-anchor="{anchor}" '
                   f'fill="{fill}" font-weight="{poids}"{it} {extra}>{e(ln)}</text>')
    return "".join(out)


# ------------------------------------------------------------------ barres
def barres(donnees, unite="", titre_y="", cible_mm=66, W=360, H=230, vmax=None, couleur="#2f6690",
           valeurs=True, graduation=None, label="Diagramme en barres"):
    """donnees : liste de (libellé, valeur[, couleur])."""
    fs = taille(W, cible_mm)
    g, d, h, b = fs * 2.8, 8, fs * 1.6, fs * 2.6
    vmax = vmax or max(v[1] for v in donnees) * 1.15
    graduation = graduation or _pas(vmax)
    ph, pw = H - h - b, W - g - d
    s = [ouvrir(W, H, label)]
    v = 0
    while v <= vmax + 1e-9:
        y = h + ph - v / vmax * ph
        s.append(f'<line x1="{g}" y1="{y:.1f}" x2="{W - d}" y2="{y:.1f}" stroke="#dde2e7" stroke-width="0.8"/>')
        s.append(texte(g - 4, y + fs * 0.33, _fmt(v), fs * 0.85, "end", "#5b6470"))
        v += graduation
    n = len(donnees)
    lb = pw / n
    for i, it in enumerate(donnees):
        lib, val = it[0], it[1]
        c = it[2] if len(it) > 2 else couleur
        bh = val / vmax * ph
        x = g + i * lb + lb * 0.18
        s.append(f'<rect x="{x:.1f}" y="{h + ph - bh:.1f}" width="{lb * 0.64:.1f}" height="{bh:.1f}" fill="{c}" rx="1.5"/>')
        if valeurs:
            s.append(texte(x + lb * 0.32, h + ph - bh - 4, f"{_fmt(val)}", fs * 0.9, poids=700, fill="#1f2328"))
        s.append(texte(x + lb * 0.32, h + ph + fs * 1.15, lib, fs * 0.88, fill="#1f2328"))
    s.append(f'<line x1="{g}" y1="{h + ph}" x2="{W - d}" y2="{h + ph}" stroke="#5b6470" stroke-width="1"/>')
    if titre_y or unite:
        s.append(texte(4, h - fs * 0.6, f"{titre_y}{' (' + unite + ')' if unite else ''}", fs * 0.85, "start", "#5b6470", 600))
    s.append("</svg>")
    return "".join(s)


# ------------------------------------------------------------------ courbes
def courbes(etiquettes, series, unite="", titre_y="", cible_mm=66, W=360, H=230, vmin=None, vmax=None,
            graduation=None, label="Graphique", valeurs=True):
    """series : liste de (nom, [valeurs], couleur)."""
    fs = taille(W, cible_mm)
    toutes = [x for _, vals, _ in series for x in vals]
    vmin = min(toutes) - 2 if vmin is None else vmin
    vmax = max(toutes) + 2 if vmax is None else vmax
    graduation = graduation or _pas(vmax - vmin)
    g, d, h, b = fs * 2.8, 10, fs * 3.0, fs * 2.2
    ph, pw = H - h - b, W - g - d
    Y = lambda v: h + ph - (v - vmin) / (vmax - vmin) * ph
    X = lambda i: g + pw * (i + 0.5) / len(etiquettes)
    s = [ouvrir(W, H, label)]
    v = vmin
    while v <= vmax + 1e-9:
        s.append(f'<line x1="{g}" y1="{Y(v):.1f}" x2="{W - d}" y2="{Y(v):.1f}" stroke="#dde2e7" stroke-width="0.8"/>')
        s.append(texte(g - 4, Y(v) + fs * 0.33, _fmt(v), fs * 0.85, "end", "#5b6470"))
        v += graduation
    for i, et in enumerate(etiquettes):
        s.append(texte(X(i), h + ph + fs * 1.2, et, fs * 0.88))
    for nom, vals, c in series:
        pts = " ".join(f"{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(vals))
        s.append(f'<polyline points="{pts}" fill="none" stroke="{c}" stroke-width="2.2" stroke-linejoin="round"/>')
        for i, v in enumerate(vals):
            s.append(f'<circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="3" fill="#fff" stroke="{c}" stroke-width="1.8"/>')
            if valeurs:
                s.append(texte(X(i), Y(v) - 6, _fmt(v), fs * 0.8, fill=c, poids=700))
    # légende en haut
    x = g
    for nom, _, c in series:
        s.append(f'<line x1="{x}" y1="{fs * 0.9}" x2="{x + 16}" y2="{fs * 0.9}" stroke="{c}" stroke-width="2.5"/>')
        s.append(texte(x + 20, fs * 1.2, nom, fs * 0.85, "start"))
        x += 26 + len(nom) * fs * 0.5
    if titre_y or unite:
        s.append(texte(4, h - fs * 0.7, f"{titre_y}{' (' + unite + ')' if unite else ''}", fs * 0.85, "start", "#5b6470", 600))
    s.append(f'<line x1="{g}" y1="{h + ph}" x2="{W - d}" y2="{h + ph}" stroke="#5b6470" stroke-width="1"/>')
    s.append("</svg>")
    return "".join(s)


# ------------------------------------------------------------------ calendrier circulaire
def calendrier(mois, cible_mm=66, W=360, label="Calendrier"):
    """mois : 12 tuples (nom_court, activité, couleur)."""
    import math
    fs = taille(W, cible_mm)
    H = W
    cx, cy = W / 2, H / 2
    R, r = W / 2 - 4, W * 0.2
    s = [ouvrir(W, H, label)]
    for i, (nom, act, c) in enumerate(mois):
        a0 = -math.pi / 2 + i * math.pi / 6
        a1 = a0 + math.pi / 6
        p = lambda a, rr: (cx + rr * math.cos(a), cy + rr * math.sin(a))
        x0, y0 = p(a0, R); x1, y1 = p(a1, R); x2, y2 = p(a1, r); x3, y3 = p(a0, r)
        s.append(f'<path d="M{x0:.1f},{y0:.1f} A{R},{R} 0 0 1 {x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f} '
                 f'A{r},{r} 0 0 0 {x3:.1f},{y3:.1f} Z" fill="{c}" stroke="#fff" stroke-width="1.5"/>')
        am = (a0 + a1) / 2
        xm, ym = p(am, R - fs * 1.05)
        s.append(texte(xm, ym + fs * 0.3, nom, fs * 0.9, poids=700, fill="#1f2328"))
        xa, ya = p(am, (R + r) / 2 - fs * 0.35)
        s.append(texte(xa, ya, act, fs * 0.72, fill="#1f2328"))
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{r - 2}" fill="#fff"/>')
    s.append("</svg>")
    return "".join(s)


# ------------------------------------------------------------------ chaîne d'étapes
def etapes(liste, cible_mm=66, W=360, sens="v", label="Étapes", largeur_boite=None, couleur="#2f6690",
           numeros=True):
    """liste : (titre, détail[, couleur]). sens : 'v' vertical, 'h' horizontal, 'cycle'."""
    import math
    fs = taille(W, cible_mm)
    n = len(liste)
    s = []
    if sens == "v":
        bh, gap = fs * 3.3, fs * 1.4
        H = n * bh + (n - 1) * gap + 4
        s.append(ouvrir(W, H, label))
        s.append(f'<defs><marker id="fl" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#6b7580"/></marker></defs>')
        for i, it in enumerate(liste):
            t, dt = it[0], it[1]
            c = it[2] if len(it) > 2 else couleur
            y = 2 + i * (bh + gap)
            s.append(f'<rect x="2" y="{y:.1f}" width="{W - 4}" height="{bh:.1f}" rx="5" fill="#fff" stroke="{c}" stroke-width="1.4"/>')
            s.append(f'<rect x="2" y="{y:.1f}" width="{fs * 2.2:.1f}" height="{bh:.1f}" rx="5" fill="{c}"/>')
            if numeros:
                s.append(texte(2 + fs * 1.1, y + bh / 2 + fs * 0.38, i + 1, fs * 1.1, fill="#fff", poids=700))
            s.append(texte(fs * 2.9, y + fs * 1.35, t, fs, "start", c, 700))
            s.append(texte(fs * 2.9, y + fs * 2.55, dt, fs * 0.82, "start", "#3b434b"))
            if i < n - 1:
                s.append(f'<line x1="{W / 2}" y1="{y + bh + 1:.1f}" x2="{W / 2}" y2="{y + bh + gap - 3:.1f}" stroke="#6b7580" stroke-width="1.6" marker-end="url(#fl)"/>')
    elif sens == "h":
        gap = fs * 1.6
        bw = (W - 4 - (n - 1) * gap) / n
        lignes = max(len(it[1].split("\n")) for it in liste) if liste else 1
        bh = fs * (2.6 + 1.05 * lignes)
        H = bh + 4
        s.append(ouvrir(W, H, label))
        s.append(f'<defs><marker id="fl" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#6b7580"/></marker></defs>')
        for i, it in enumerate(liste):
            t, dt = it[0], it[1]
            c = it[2] if len(it) > 2 else couleur
            x = 2 + i * (bw + gap)
            s.append(f'<rect x="{x:.1f}" y="2" width="{bw:.1f}" height="{bh:.1f}" rx="5" fill="#fff" stroke="{c}" stroke-width="1.4"/>')
            s.append(f'<rect x="{x:.1f}" y="2" width="{bw:.1f}" height="{fs * 1.7:.1f}" rx="5" fill="{c}"/>')
            ft = min(fs * 0.92, bw / (max(len(t), 1) * 0.56))
            s.append(texte(x + bw / 2, 2 + fs * 1.2, t, ft, fill="#fff", poids=700))
            fd = min(fs * 0.8, bw / (max(max(len(z) for z in dt.split("\n")), 1) * 0.52))
            s.append(texte(x + bw / 2, 2 + fs * 2.9, dt, fd, fill="#2b3036"))
            if i < n - 1:
                s.append(f'<line x1="{x + bw + 1:.1f}" y1="{2 + bh / 2:.1f}" x2="{x + bw + gap - 3:.1f}" y2="{2 + bh / 2:.1f}" stroke="#6b7580" stroke-width="1.6" marker-end="url(#fl)"/>')
    else:  # cycle
        H = W * 0.9
        cx, cy, R = W / 2, H / 2, min(W, H) / 2 - fs * 3.2
        s.append(ouvrir(W, H, label))
        s.append(f'<defs><marker id="fl" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#6b7580"/></marker></defs>')
        for i, it in enumerate(liste):
            a = -math.pi / 2 + 2 * math.pi * i / n
            a2 = -math.pi / 2 + 2 * math.pi * (i + 1) / n
            # arc fléché
            m0, m1 = a + 0.35, a2 - 0.35
            x0, y0 = cx + R * math.cos(m0), cy + R * math.sin(m0)
            x1, y1 = cx + R * math.cos(m1), cy + R * math.sin(m1)
            s.append(f'<path d="M{x0:.1f},{y0:.1f} A{R},{R} 0 0 1 {x1:.1f},{y1:.1f}" fill="none" stroke="#9aa4ad" stroke-width="1.6" marker-end="url(#fl)"/>')
        for i, it in enumerate(liste):
            t, dt = it[0], it[1]
            c = it[2] if len(it) > 2 else couleur
            a = -math.pi / 2 + 2 * math.pi * i / n
            x, y = cx + R * math.cos(a), cy + R * math.sin(a)
            bw, bh = fs * 7.4, fs * 2.9
            s.append(f'<rect x="{x - bw / 2:.1f}" y="{y - bh / 2:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="5" fill="#fff" stroke="{c}" stroke-width="1.5"/>')
            s.append(texte(x, y - fs * 0.15, t, fs * 0.95, fill=c, poids=700))
            s.append(texte(x, y + fs * 0.95, dt, fs * 0.75, fill="#3b434b"))
    s.append("</svg>")
    return "".join(s)


# ------------------------------------------------------------------ tableau
def tableau(entetes, lignes, cible_mm=66, W=360, couleur="#2f6690", label="Tableau", largeurs=None):
    fs = taille(W, cible_mm)
    n = len(entetes)
    largeurs = largeurs or [1] * n
    tot = sum(largeurs)
    cols = [W * l / tot for l in largeurs]
    hh = fs * (0.8 + 1.1 * max(len(str(t).split("\n")) for t in entetes))
    hauteurs = [fs * (0.9 + 1.15 * max(len(str(c).split("\n")) for c in ln)) for ln in lignes]
    H = hh + sum(hauteurs) + 2
    s = [ouvrir(W, H, label)]
    x = 0
    s.append(f'<rect x="0.5" y="0.5" width="{W - 1}" height="{hh:.1f}" fill="{couleur}"/>')
    for j, t in enumerate(entetes):
        nl = len(str(t).split("\n"))
        s.append(texte(x + cols[j] / 2, hh / 2 + fs * 0.35 - (nl - 1) * fs * 0.5, t, fs * 0.9, fill="#fff", poids=700))
        x += cols[j]
    y = hh
    for i, ln in enumerate(lignes):
        hl = hauteurs[i]
        if i % 2:
            s.append(f'<rect x="0.5" y="{y:.1f}" width="{W - 1}" height="{hl:.1f}" fill="#f2f5f8"/>')
        x = 0
        for j, c in enumerate(ln):
            s.append(texte(x + 5, y + fs * 1.15, c, fs * 0.85, "start", "#1f2328", 700 if j == 0 else 400))
            x += cols[j]
        y += hl
    x = 0
    for j in range(n - 1):
        x += cols[j]
        s.append(f'<line x1="{x:.1f}" y1="0" x2="{x:.1f}" y2="{H - 1:.1f}" stroke="#c9d1d9" stroke-width="0.8"/>')
    s.append(f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1:.1f}" fill="none" stroke="#9aa4ad" stroke-width="1"/>')
    s.append("</svg>")
    return "".join(s)


def _pas(etendue):
    for p in (0.5, 1, 2, 5, 10, 20, 25, 50, 100, 200, 250, 500, 1000):
        if etendue / p <= 6:
            return p
    return etendue / 5


def _fmt(v):
    if abs(v - round(v)) < 1e-9:
        return f"{int(round(v))}"
    return f"{v:.1f}".replace(".", ",")


# ------------------------------------------------------------------ climatogramme
def climatogramme(temp, pluie, cible_mm=66, W=360, H=250, label="Diagramme climatique",
                  mois=("J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D")):
    """Barres de précipitations (mm, axe de droite) + courbe de température (°C, axe de gauche).
    Convention : 1 °C pour 2 mm (diagramme ombrothermique)."""
    fs = taille(W, cible_mm)
    g, d, h, b = fs * 2.6, fs * 2.8, fs * 2.4, fs * 1.8
    ph, pw = H - h - b, W - g - d
    tmax, pmax = 45, 90
    Y_t = lambda t: h + ph - t / tmax * ph
    Y_p = lambda p: h + ph - p / pmax * ph
    X = lambda i: g + pw * (i + 0.5) / 12
    s = [ouvrir(W, H, label)]
    for t in range(0, tmax + 1, 10):
        s.append(f'<line x1="{g}" y1="{Y_t(t):.1f}" x2="{W - d}" y2="{Y_t(t):.1f}" stroke="#dde2e7" stroke-width="0.8"/>')
        s.append(texte(g - 4, Y_t(t) + fs * 0.33, t, fs * 0.8, "end", "#c0392b"))
        s.append(texte(W - d + 4, Y_t(t) + fs * 0.33, t * 2, fs * 0.8, "start", "#2f6690"))
    for i, p in enumerate(pluie):
        bw = pw / 12 * 0.62
        s.append(f'<rect x="{X(i) - bw / 2:.1f}" y="{Y_p(p):.1f}" width="{bw:.1f}" height="{h + ph - Y_p(p):.1f}" fill="#5b9bd5"/>')
    pts = " ".join(f"{X(i):.1f},{Y_t(t):.1f}" for i, t in enumerate(temp))
    s.append(f'<polyline points="{pts}" fill="none" stroke="#c0392b" stroke-width="2.4" stroke-linejoin="round"/>')
    for i, t in enumerate(temp):
        s.append(f'<circle cx="{X(i):.1f}" cy="{Y_t(t):.1f}" r="2.4" fill="#c0392b"/>')
        s.append(texte(X(i), h + ph + fs * 1.15, mois[i], fs * 0.85))
    s.append(f'<line x1="{g}" y1="{h + ph}" x2="{W - d}" y2="{h + ph}" stroke="#5b6470"/>')
    s.append(texte(4, h - fs * 0.9, "Température (°C)", fs * 0.8, "start", "#c0392b", 700))
    s.append(texte(W - 4, h - fs * 0.9, "Précipitations (mm)", fs * 0.8, "end", "#2f6690", 700))
    s.append("</svg>")
    return "".join(s)


# ------------------------------------------------------------------ pictogrammes météo
def picto(kind, r=9):
    """Petits symboles météo centrés sur (0,0)."""
    soleil = (f'<circle r="{r*0.55}" fill="#f4b400" stroke="#d68910" stroke-width="1"/>' +
              "".join(f'<line x1="0" y1="{-r*0.75}" x2="0" y2="{-r}" stroke="#d68910" stroke-width="1.4" transform="rotate({a})"/>' for a in range(0, 360, 45)))
    nuage = lambda dx=0, dy=0, c="#b8c2cc": (f'<g transform="translate({dx},{dy})"><ellipse cx="0" cy="0" rx="{r*0.95}" ry="{r*0.55}" fill="{c}" stroke="#7f8c96" stroke-width="0.8"/>'
                                          f'<circle cx="{-r*0.25}" cy="{-r*0.35}" r="{r*0.45}" fill="{c}" stroke="#7f8c96" stroke-width="0.8"/>'
                                          f'<ellipse cx="0" cy="0" rx="{r*0.9}" ry="{r*0.5}" fill="{c}"/></g>')
    gouttes = "".join(f'<line x1="{x}" y1="{r*0.6}" x2="{x-2}" y2="{r*1.1}" stroke="#2f6690" stroke-width="1.5" stroke-linecap="round"/>' for x in (-r*0.4, 0, r*0.4))
    if kind == "soleil":
        return soleil
    if kind == "eclaircies":
        return f'<g transform="translate({-r*0.35},{-r*0.35})">{soleil}</g>' + nuage(r * 0.25, r * 0.2, "#dfe5ea")
    if kind == "nuages":
        return nuage()
    if kind == "pluie":
        return nuage(0, -r * 0.15) + gouttes
    return ""
