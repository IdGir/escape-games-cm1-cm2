# -*- coding: utf-8 -*-
"""Compose l'affiche 16:9 de chaque jeu (amélioration B4) : <jeu>/assets/images/affiche.jpg

    python outils-medias/affiches.py            (les 9 jeux)
    python outils-medias/affiches.py melanges   (un seul)
    (Pillow requis : pip install pillow)

Une vraie affiche, réutilisable hors du site (ENT, message aux familles, diaporama) :
image de fond du jeu + titre, matière, niveau, et la signature de la collection.
Fond choisi, dans l'ordre :
  1. <jeu>/assets/images/affiche-fond.jpg : illustration dédiée, générée avec Agnes par
     produire-medias.ps1 (entrée « affiche-fond » du manifeste medias.json) ;
  2. sinon une illustration du jeu déjà créée avec Agnes (intro, salle…) ;
  3. sinon une photographie libre du jeu, dont le crédit est alors écrit sur l'affiche.
Le crédit de l'affiche est ajouté à <jeu>/assets/medias/CREDITS-medias.md.
"""
import json, os, re, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont
ICI = os.path.dirname(os.path.abspath(__file__)); RACINE = os.path.dirname(ICI)
L, H = 1600, 900

def police(gras=True, serif=True, taille=40):
    noms = (["georgiab.ttf", "DejaVuSerif-Bold.ttf"] if serif and gras else ["georgia.ttf", "DejaVuSerif.ttf"] if serif
            else ["segoeuib.ttf", "arialbd.ttf", "DejaVuSans-Bold.ttf"] if gras else ["segoeui.ttf", "arial.ttf", "DejaVuSans.ttf"])
    dossiers = ["C:\\Windows\\Fonts", "/usr/share/fonts/truetype/dejavu", "/Library/Fonts", "/System/Library/Fonts/Supplemental"]
    for n in noms:
        for d in dossiers:
            p = os.path.join(d, n)
            if os.path.exists(p): return ImageFont.truetype(p, taille)
    return ImageFont.load_default()

def catalogue():
    t = open(os.path.join(RACINE, "commun", "donnees", "catalogue.js"), encoding="utf-8").read()
    return json.loads(t[t.index("var CATALOGUE = ") + 16: t.rindex(";")])

def fond(jeu):
    """(chemin, crédit ou None) de l'image de fond."""
    img = os.path.join(RACINE, jeu, "assets", "images")
    dediee = os.path.join(img, "affiche-fond.jpg")
    if os.path.exists(dediee): return dediee, None
    agnes, photos = [], {}
    try:
        m = json.load(open(os.path.join(RACINE, jeu, "assets", "medias", "medias.json"), encoding="utf-8"))
        agnes = [i["cible"] for i in m.get("images", [])]
        photos = {p["cible"]: p for p in m.get("photos", [])}
    except (OSError, ValueError):
        pass
    ordre = ["intro", "salle1", "etape1", "mission-intro", "salle2", "s03-coeur", "salle4", "final"]
    for nom in ordre:
        for cible in agnes:
            if os.path.basename(cible).split(".")[0] == nom and os.path.exists(os.path.join(RACINE, jeu, cible)):
                return os.path.join(RACINE, jeu, cible), None
    for nom in ordre:
        for cible in photos:
            if os.path.basename(cible).split(".")[0] == nom and os.path.exists(os.path.join(RACINE, jeu, cible)):
                return os.path.join(RACINE, jeu, cible), credit(jeu, cible)
    return None, None

def credit(jeu, cible):
    try:
        t = open(os.path.join(RACINE, jeu, "assets", "medias", "CREDITS-medias.md"), encoding="utf-8-sig").read()
        for l in t.splitlines():
            if f"`{cible}`" in l:
                c = [x.strip() for x in l.strip("|").split("|")]
                return f"Photo : {c[3]}, {c[4]}, Wikimedia Commons"
    except OSError:
        pass
    return "Photo : Wikimedia Commons (voir CREDITS-medias.md)"

def couvrir(im):
    r = max(L / im.width, H / im.height)
    im = im.resize((int(im.width * r + 1), int(im.height * r + 1)), Image.LANCZOS)
    x, y = (im.width - L) // 2, (im.height - H) // 2
    return im.crop((x, y, x + L, y + H))

def hexa(c): c = c.lstrip("#"); return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))

def lignes(d, texte, f, largeur):
    mots, out, cour = texte.split(), [], ""
    for m in mots:
        essai = (cour + " " + m).strip()
        if d.textlength(essai, font=f) <= largeur: cour = essai
        else: out.append(cour); cour = m
    return out + [cour]

def composer(j):
    jeu = j["dossier"]
    src, cred = fond(jeu)
    base = couvrir(Image.open(src).convert("RGB")) if src else Image.new("RGB", (L, H), hexa(j["couleurs"][0]))
    # voile : sombre à gauche (texte), couleur du jeu en bas
    c0 = hexa(j["couleurs"][0])
    gauche = Image.new("RGBA", (L, H)); gd = ImageDraw.Draw(gauche)
    for x in range(L):
        gd.line([(x, 0), (x, H)], fill=(10, 14, 28, int(232 * max(0, 1 - x / (L * 0.8)) ** 1.1)))
    bas = Image.new("RGBA", (L, H)); bd = ImageDraw.Draw(bas)
    for y in range(H // 2, H):
        bd.line([(0, y), (L, y)], fill=c0 + (int(165 * ((y - H / 2) / (H / 2)) ** 1.5),))
    im = Image.alpha_composite(Image.alpha_composite(base.convert("RGBA"), gauche), bas)
    d = ImageDraw.Draw(im)
    marge = 90
    # bandeau de matière
    f_mat = police(True, False, 30)
    mat = f"{j['matiere'].upper()}  ·  CM1 – CM2"
    if j.get("periodes") and len(j["periodes"]) == 1 and len(j.get("annee", "")) == 1:
        mat += f"  ·  {j['periodes'][0]}, ANNÉE {j['annee']}"
    lm = d.textlength(mat, font=f_mat)
    d.rounded_rectangle([marge - 18, 120, marge + lm + 18, 172], radius=26, fill=hexa(j["couleurs"][1]) + (235,))
    d.text((marge, 128), mat, font=f_mat, fill=(20, 20, 28))
    # titre
    f_t = police(True, True, 104)
    ls = lignes(d, j["titre"], f_t, L * 0.62)
    if len(ls) > 3: f_t = police(True, True, 84); ls = lignes(d, j["titre"], f_t, L * 0.62)
    y = 215
    for l in ls:
        d.text((marge + 3, y + 4), l, font=f_t, fill=(0, 0, 0, 160))
        d.text((marge, y), l, font=f_t, fill=(255, 255, 255))
        y += int(f_t.size * 1.12)
    # accroche : thème du programme (court)
    f_s = police(False, False, 34)
    acc = re.split(r" ; |\. ", j.get("competences", ""))[0].rstrip(".")
    for l in lignes(d, acc, f_s, L * 0.55)[:3]:
        y += 6; d.text((marge + 2, y + 16), l, font=f_s, fill=(0, 0, 0, 170)); d.text((marge, y + 14), l, font=f_s, fill=(240, 242, 248)); y += int(f_s.size * 1.25)
    # signature de la collection
    f_sig = police(True, False, 28)
    try:
        ic = Image.open(os.path.join(RACINE, "commun", "icones", "icone-192.png")).convert("RGBA").resize((64, 64), Image.LANCZOS)
        im.alpha_composite(ic, (marge, H - 120))
    except OSError:
        pass
    d.text((marge + 82, H - 108), "Escape games pédagogiques", font=f_sig, fill=(255, 255, 255))
    d.text((marge + 82, H - 74), "idgir.github.io/escape-games-cm1-cm2", font=police(False, False, 24), fill=(225, 228, 235))
    if cred:
        f_c = police(False, False, 18)
        d.text((L - 23 - d.textlength(cred, font=f_c), H - 33), cred, font=f_c, fill=(0, 0, 0)); d.text((L - 24 - d.textlength(cred, font=f_c), H - 34), cred, font=f_c, fill=(245, 245, 245))
    sortie = os.path.join(RACINE, jeu, "assets", "images", "affiche.jpg")
    im.convert("RGB").save(sortie, "JPEG", quality=86, optimize=True, progressive=True)
    noter_credit(jeu, src, cred)
    return sortie, src, cred

def noter_credit(jeu, src, cred):
    p = os.path.join(RACINE, jeu, "assets", "medias", "CREDITS-medias.md")
    if not os.path.exists(p): return
    t = open(p, encoding="utf-8-sig").read()
    t = re.sub(r"\n## Affiche du jeu\n[\s\S]*?(?=\n## |\Z)", "\n", t).rstrip() + "\n"
    rel = os.path.relpath(src, os.path.join(RACINE, jeu)).replace("\\", "/") if src else "aplat de couleur"
    t += ("\n## Affiche du jeu\n\n`assets/images/affiche.jpg` : composée par `outils-medias/affiches.py` à partir de `" + rel + "` "
          + ("(" + cred + " ; l'affiche reprend cette licence)." if cred else "(illustration créée avec Agnes AI, scène et personnages fictifs).") + "\n")
    open(p, "w", encoding="utf-8", newline="\n").write(t)

if __name__ == "__main__":
    C = catalogue()
    choix = sys.argv[1:]
    for j in C["jeux"]:
        if j.get("dossier") and (not choix or j["dossier"] in choix):
            s, src, cred = composer(j)
            print(f"{j['dossier']:18s} affiche.jpg  ({os.path.getsize(s) // 1024} Ko)  fond : {os.path.relpath(src, RACINE) if src else '—'}{'  [' + cred + ']' if cred else ''}")
