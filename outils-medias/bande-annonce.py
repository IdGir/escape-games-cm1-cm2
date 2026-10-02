# -*- coding: utf-8 -*-
"""Monte la bande-annonce (environ 16 s) de chaque jeu (amélioration B2) :
<jeu>/assets/videos/bande-annonce.mp4

    python outils-medias/bande-annonce.py            (les 9 jeux)
    python outils-medias/bande-annonce.py melanges   (un seul)
    (ffmpeg et Pillow requis : https://ffmpeg.org — « winget install ffmpeg » sous Windows ;
     pip install pillow)

Montage, sans voix ni musique (comme les décors filmés du jeu) :
  1. l'affiche du jeu (assets/images/affiche.jpg), lent zoom avant — 3 s ;
  2. quatre plans du jeu, en fondu enchaîné — 3,2 s chacun :
       le plan d'ouverture généré avec Agnes (assets/videos/bande-annonce-ouverture.mp4,
       entrée « bande-annonce-ouverture » des manifestes medias.json) s'il existe,
       puis des décors filmés du jeu (intro, salles…), ou à défaut leurs images fixes
       animées d'un lent zoom ;
  3. un carton de fin : titre, « À jouer en classe », adresse du site — 3 s.
Rien n'est inventé : uniquement les médias déjà présents dans le jeu, dont les crédits
s'appliquent (rappel ajouté à CREDITS-medias.md).
"""
import json, os, shutil, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFilter
ICI = os.path.dirname(os.path.abspath(__file__)); RACINE = os.path.dirname(ICI)
sys.path.insert(0, ICI)
from affiches import police, catalogue, lignes   # mêmes polices et même catalogue que les affiches
LV, HV, IPS = 1280, 720, 24
D_AFF, D_PLAN, D_FIN, FONDU = 3.0, 3.2, 3.0, 0.5

def duree(f):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True)
    try: return float(r.stdout.strip())
    except ValueError: return 0.0

def plans(jeu):
    """Quatre plans : (chemin, 'video'|'image')."""
    a = os.path.join(RACINE, jeu, "assets")
    v = lambda n: os.path.join(a, "videos", n + ".mp4")
    i = lambda n: next((os.path.join(a, "images", d, n + ".jpg") for d in ("decors", "") if os.path.exists(os.path.join(a, "images", d, n + ".jpg"))), None)
    noms = {"mission-geo": ["mission-intro", "s03-coeur", "s09-coeur", "s12-coeur", "s16-coeur", "final-intro"],
            "tour-du-monde": ["intro", "etape1", "etape3", "etape4", "etape5", "final"]}.get(jeu, ["intro", "salle1", "salle2", "salle3", "salle4", "salle5", "final"])
    out = []
    if os.path.exists(v("bande-annonce-ouverture")): out.append((v("bande-annonce-ouverture"), "video"))
    videos = [n for n in noms if os.path.exists(v(n)) and duree(v(n)) >= D_PLAN + 1.2]
    images = [n for n in noms if i(n) and n not in videos]
    choix = videos + images
    # étaler le choix sur tout le jeu (début, milieu, fin)
    while len(out) < 4 and choix:
        k = 0 if len(out) == 0 else min(len(choix) - 1, (len(choix) * len(out)) // 4 + (1 if len(choix) > 4 else 0))
        n = choix.pop(k)
        out.append((v(n), "video") if n in videos else (i(n), "image"))
    out = out[:4]
    # finir sur la dernière vidéo du jeu (le final) quand elle existe
    if videos and v(videos[-1]) not in [c for c, _ in out] and len(out) == 4:
        out[-1] = (v(videos[-1]), "video")
    return out

def carton_fin(j, chemin):
    aff = os.path.join(RACINE, j["dossier"], "assets", "images", "affiche.jpg")
    im = Image.open(aff).convert("RGB").resize((LV, HV)).filter(ImageFilter.GaussianBlur(14)) if os.path.exists(aff) else Image.new("RGB", (LV, HV), (20, 24, 40))
    voile = Image.new("RGBA", (LV, HV), (8, 12, 26, 190))
    im = Image.alpha_composite(im.convert("RGBA"), voile)
    d = ImageDraw.Draw(im)
    def centre(t, f, y, c=(255, 255, 255)):
        d.text(((LV - d.textlength(t, font=f)) / 2, y), t, font=f, fill=c)
    f_t = police(True, True, 66)
    y = 190
    for l in lignes(d, j["titre"], f_t, LV * 0.85):
        centre(l, f_t, y); y += 80
    centre(f"Un escape game de {j['matiere'].lower() if j['matiere'] != 'EMC' else 'EMC'} · CM1 – CM2", police(False, False, 32), y + 20, (230, 232, 240))
    centre("À jouer en classe, sans installation", police(True, False, 36), y + 90, hex_rgb(j["couleurs"][1]))
    centre("idgir.github.io/escape-games-cm1-cm2", police(False, False, 30), y + 150, (240, 240, 245))
    im.convert("RGB").save(chemin, "PNG")

def hex_rgb(c): c = c.lstrip("#"); return tuple(int(c[k:k + 2], 16) for k in (0, 2, 4))

def monter(j):
    jeu = j["dossier"]
    aff = os.path.join(RACINE, jeu, "assets", "images", "affiche.jpg")
    if not os.path.exists(aff): print(f"{jeu} : pas d'affiche (lancer d'abord affiches.py)"); return
    p = plans(jeu)
    if len(p) < 2: print(f"{jeu} : pas assez de médias pour une bande-annonce"); return
    tmp = tempfile.mkdtemp()
    fin = os.path.join(tmp, "fin.png"); carton_fin(j, fin)
    entrees, filtres, durees = [], [], []
    norme = f"scale={LV}:{HV}:force_original_aspect_ratio=increase,crop={LV}:{HV},setsar=1,fps={IPS},format=yuv420p"
    def fixe(chemin, d, zoom=True):
        entrees.extend(["-loop", "1", "-t", f"{d}", "-i", chemin])
        z = (f"scale={LV*2}:{HV*2}:force_original_aspect_ratio=increase,crop={LV*2}:{HV*2},zoompan=z='min(zoom+0.0009,1.12)':d={int(d*IPS)}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={LV}x{HV}:fps={IPS},"
             if zoom else "")
        filtres.append(f"[{len(durees)}:v]{z}{norme},trim=duration={d},setpts=PTS-STARTPTS[s{len(durees)}]"); durees.append(d)
    fixe(aff, D_AFF)
    for chemin, nature in p:
        if nature == "video":
            entrees.extend(["-ss", "1.0", "-t", f"{D_PLAN}", "-i", chemin])
            filtres.append(f"[{len(durees)}:v]{norme},trim=duration={D_PLAN},setpts=PTS-STARTPTS[s{len(durees)}]"); durees.append(D_PLAN)
        else:
            fixe(chemin, D_PLAN)
    fixe(fin, D_FIN, zoom=False)
    # fondus enchaînés
    courant, t = "s0", durees[0]
    for k in range(1, len(durees)):
        t -= FONDU
        filtres.append(f"[{courant}][s{k}]xfade=transition=fade:duration={FONDU}:offset={t:.2f}[x{k}]")
        courant, t = f"x{k}", t + durees[k]
    sortie = os.path.join(RACINE, jeu, "assets", "videos", "bande-annonce.mp4")
    os.makedirs(os.path.dirname(sortie), exist_ok=True)
    cmd = ["ffmpeg", "-y", "-loglevel", "error", *entrees, "-filter_complex", ";".join(filtres), "-map", f"[{courant}]",
           "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "27", "-pix_fmt", "yuv420p", "-movflags", "+faststart", sortie]
    subprocess.run(cmd, check=True)
    shutil.rmtree(tmp, ignore_errors=True)
    noter_credit(jeu, p)
    print(f"{jeu:18s} bande-annonce.mp4  {duree(sortie):.1f} s  {os.path.getsize(sortie) // 1024} Ko  plans : " + ", ".join(os.path.basename(c) for c, _ in p))

def noter_credit(jeu, p):
    f = os.path.join(RACINE, jeu, "assets", "medias", "CREDITS-medias.md")
    if not os.path.exists(f):   # jeu dont tous les médias sont générés : on crée le fichier de crédits
        os.makedirs(os.path.dirname(f), exist_ok=True)
        titre = next((j["titre"] for j in catalogue()["jeux"] if j.get("dossier") == jeu), jeu)
        open(f, "w", encoding="utf-8", newline="\n").write(
            f"# Crédits des médias - {titre}\n\nImages et vidéos créées avec Agnes AI (détail dans `journal-medias.txt`) ; "
            "scènes et personnages entièrement fictifs.\n")
    t = open(f, encoding="utf-8-sig").read()
    import re
    t = re.sub(r"\n## Bande-annonce\n[\s\S]*?(?=\n## |\Z)", "\n", t).rstrip() + "\n"
    t += ("\n## Bande-annonce\n\n`assets/videos/bande-annonce.mp4` : montage (outils-medias/bande-annonce.py) de l'affiche et des médias du jeu "
          + ", ".join(f"`{os.path.relpath(c, os.path.join(RACINE, jeu)).replace(os.sep, '/')}`" for c, _ in p)
          + " ; les crédits et licences de ces médias, indiqués ci-dessus, s'appliquent.\n")
    open(f, "w", encoding="utf-8", newline="\n").write(t)

if __name__ == "__main__":
    if not shutil.which("ffmpeg"): sys.exit("ffmpeg est introuvable : installez-le (Windows : « winget install ffmpeg »), puis relancez.")
    choix = sys.argv[1:]
    for j in catalogue()["jeux"]:
        if j.get("dossier") and (not choix or j["dossier"] in choix):
            monter(j)
