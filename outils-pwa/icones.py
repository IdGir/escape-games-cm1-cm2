# -*- coding: utf-8 -*-
"""Dessine les icônes de l'application installable (PWA) : commun/icones/*.png
    python outils-pwa/icones.py      (Pillow requis : pip install pillow)
Une serrure dorée (trou de serrure) sur fond bleu nuit : pas d'emoji, pas de logo existant."""
import os
from PIL import Image, ImageDraw
ICI = os.path.dirname(os.path.abspath(__file__))
DEST = os.path.join(os.path.dirname(ICI), "commun", "icones")

def dessiner(taille, masquable=False):
    s = 4 * taille   # sur-échantillonnage, puis réduction (bords lisses)
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    haut, bas = (29, 58, 138), (13, 24, 70)
    fond = Image.new("RGBA", (s, s))
    fd = ImageDraw.Draw(fond)
    for y in range(s):
        t = y / (s - 1)
        fd.line([(0, y), (s, y)], fill=tuple(int(haut[i] + (bas[i] - haut[i]) * t) for i in range(3)) + (255,))
    masque = Image.new("L", (s, s), 0)
    md = ImageDraw.Draw(masque)
    if masquable: md.rectangle([0, 0, s, s], fill=255)
    else: md.rounded_rectangle([0, 0, s - 1, s - 1], radius=int(s * 0.22), fill=255)
    img.paste(fond, (0, 0), masque)
    k = 0.72 if masquable else 1.0          # zone sûre des icônes « maskable »
    c, r = s / 2, s * 0.33 * k
    or_ = (230, 190, 70, 255)
    d.ellipse([c - r, c - r, c + r, c + r], outline=or_, width=int(s * 0.055 * k))
    # trou de serrure : un disque et un trapèze
    rt = s * 0.085 * k
    cy = c - s * 0.055 * k
    d.ellipse([c - rt, cy - rt, c + rt, cy + rt], fill=or_)
    d.polygon([(c - rt * 0.55, cy + rt * 0.3), (c + rt * 0.55, cy + rt * 0.3), (c + rt * 1.05, c + s * 0.17 * k), (c - rt * 1.05, c + s * 0.17 * k)], fill=or_)
    return img.resize((taille, taille), Image.LANCZOS)

os.makedirs(DEST, exist_ok=True)
for t in (192, 512):
    dessiner(t).save(os.path.join(DEST, f"icone-{t}.png"))
dessiner(512, masquable=True).save(os.path.join(DEST, "icone-masquable-512.png"))
dessiner(180).save(os.path.join(DEST, "icone-apple-180.png"))
print("Icônes écrites dans", DEST)
