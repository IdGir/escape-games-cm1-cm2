#!/usr/bin/env python3
"""Dépose dans le jeu une image ou une vidéo venue de N'IMPORTE QUELLE source (Agnes, Midjourney, ChatGPT, Runway, photo, dessin…).

Une image déposée peut servir :
  --decor <id>       de FOND d'un décor            → assets/images/decors/<id>.webp          (1920×1080, recadrée au centre)
  --portrait <id>    de portrait de personnage     → assets/images/personnages/<id>.webp     (1200×1600)
  --depart <nom>     de POINT DE DÉPART d'une vidéo → assets/medias-depart/<nom>.jpg          (1280×720) ; une vidéo de départ « transition-e3 »
  --video <nom>      une vidéo déjà faite          → assets/videos/<nom>.mp4                 (piste audio retirée si ffmpeg est présent)
On peut cumuler : --decor sas --depart transition-e3 (le même fichier sert de fond ET de départ de vidéo).

Le fichier peut être un chemin ou une adresse (http…). Le moteur prend le fichier déposé aussitôt (sinon il garde le décor de secours dessiné).

Exemples :
  python importer-image.py ~/Téléchargements/atelier.png --decor imprimerie --source "Midjourney v6"
  python importer-image.py atelier.png --decor imprimerie --depart transition-e1
  python importer-image.py proposition.webp --portrait tommaso
  python importer-image.py clip.mp4 --video transition-e2 --source "Runway Gen-3"
  python importer-image.py --dossier                     traite assets/medias-a-importer/ d'après les noms de fichiers :
        decor-<id>.png · portrait-<id>.jpg · depart-<nom>.jpg · video-<nom>.mp4
"""
import argparse, csv, datetime, os, re, shutil, subprocess, sys, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import medias_lib as L

DOSSIER_ENTREE = os.path.join(L.JEU, "assets", "medias-a-importer")
EXT_IMG = (".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif", ".tif", ".tiff")


def chemin_local(entree):
    if re.match(r"https?://", entree):
        os.makedirs(L.SORTIE, exist_ok=True)
        tmp = os.path.join(L.SORTIE, "_import" + (os.path.splitext(entree.split("?")[0])[1] or ".img"))
        req = urllib.request.Request(entree, headers={"User-Agent": "escape-games-medias/1.0"})
        with urllib.request.urlopen(req, timeout=300) as r, open(tmp, "wb") as f:
            f.write(r.read())
        return tmp, True
    if not os.path.isfile(entree):
        raise L.ErreurSource(f"Fichier introuvable : {entree}")
    return entree, False


def maj_csv(identifiant, source):
    """Passe la ligne de medias.csv à « déposé » (si le jeu a un medias.csv)."""
    chemin = os.path.join(L.JEU, "medias.csv")
    if not os.path.isfile(chemin):
        return
    with open(chemin, encoding="utf-8", newline="") as f:
        lecteur = csv.DictReader(f, delimiter=";")
        champs, lignes = lecteur.fieldnames, list(lecteur)
    for l in lignes:
        if l["id"] == identifiant:
            l["statut"] = f"déposé ({source or 'source non précisée'}, {datetime.date.today().isoformat()})"
    with open(chemin, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=champs, delimiter=";")
        w.writeheader()
        w.writerows(lignes)


def crediter(fichier, source, licence):
    chemin = os.path.join(L.JEU, "assets", "medias", "CREDITS-medias.md")
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    nouveau = not os.path.isfile(chemin)
    with open(chemin, "a", encoding="utf-8") as f:
        if nouveau:
            f.write("# Crédits des médias\n\nChaque média déposé avec importer-image.py ajoute une ligne : fichier · source · licence/droits · date.\n\n")
        f.write(f"- `{fichier}` · {source or 'source non précisée'} · {licence or 'à préciser (droits d’usage)'} · {datetime.date.today().isoformat()}\n")


def deposer(entree, decor=None, portrait=None, depart=None, video=None, source="", licence=""):
    chemin, temporaire = chemin_local(entree)
    faits = []
    try:
        if video:
            sortie = os.path.join(L.JEU, "assets", "videos", video + ".mp4")
            os.makedirs(os.path.dirname(sortie), exist_ok=True)
            try:
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", chemin, "-an", "-c:v", "copy", sortie], check=True)
            except (FileNotFoundError, subprocess.CalledProcessError):
                shutil.copy2(chemin, sortie)
            faits.append(sortie)
            maj_csv("video-" + video, source)
        if decor:
            sortie = L.convertir_image(chemin, os.path.join(L.JEU, "assets", "images", "decors", decor + ".webp"), 1920, 1080)
            faits.append(sortie)
            maj_csv("decor-" + decor, source)
        if portrait:
            sortie = L.convertir_image(chemin, os.path.join(L.JEU, "assets", "images", "personnages", portrait + ".webp"), 1200, 1600)
            faits.append(sortie)
            maj_csv("portrait-" + portrait, source)
        if depart:
            sortie = L.convertir_image(chemin, os.path.join(L.JEU, "assets", "medias-depart", depart + ".jpg"), 1280, 720, 82)
            faits.append(sortie)
        if not faits:
            raise L.ErreurSource("Précisez où déposer : --decor, --portrait, --depart ou --video.")
        for f in faits:
            rel = os.path.relpath(f, L.JEU).replace("\\", "/")
            crediter(rel, source, licence)
            print("✔ déposé :", rel)
        if depart:
            print("  Pour une vidéo « image de départ » : publiez ce fichier (git add / commit / push) ; le service le lira à l'adresse")
            try:
                print("  ", L.url_publique(os.path.relpath(faits[-1], L.JEU)))
            except L.ErreurSource:
                pass
    finally:
        if temporaire and os.path.isfile(chemin):
            os.remove(chemin)
    return faits


def traiter_dossier(dossier, source, licence):
    if not os.path.isdir(dossier):
        os.makedirs(dossier, exist_ok=True)
        print(f"Dossier créé : {os.path.relpath(dossier, L.JEU)} — déposez-y vos fichiers (decor-<id>.png, portrait-<id>.jpg, depart-<nom>.jpg, video-<nom>.mp4) puis relancez.")
        return
    faits = 0
    for nom in sorted(os.listdir(dossier)):
        p = os.path.join(dossier, nom)
        if not os.path.isfile(p):
            continue
        base, ext = os.path.splitext(nom)
        m = re.match(r"(decor|portrait|depart|video)-(.+)$", base, re.I)
        if not m or not (ext.lower() in EXT_IMG or (m.group(1).lower() == "video" and ext.lower() in (".mp4", ".webm", ".mov"))):
            print(f"· ignoré : {nom} (nom attendu : decor-<id>, portrait-<id>, depart-<nom> ou video-<nom>)")
            continue
        genre, ident = m.group(1).lower(), m.group(2)
        deposer(p, **{genre: ident}, source=source, licence=licence)
        os.makedirs(os.path.join(dossier, "importes"), exist_ok=True)
        shutil.move(p, os.path.join(dossier, "importes", nom))
        faits += 1
    print(f"{faits} fichier(s) déposé(s).")


def main():
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("fichier", nargs="?", help="chemin ou adresse du fichier")
    a.add_argument("--decor"), a.add_argument("--portrait"), a.add_argument("--depart"), a.add_argument("--video")
    a.add_argument("--source", default="", help="d'où vient le média (pour les crédits), ex. « Midjourney v6 »")
    a.add_argument("--licence", default="", help="droits d'usage, ex. « usage libre par le compte », « CC-BY »")
    a.add_argument("--dossier", nargs="?", const=DOSSIER_ENTREE, help="traite tout un dossier (défaut : assets/medias-a-importer)")
    o = a.parse_args()
    try:
        if o.dossier:
            return traiter_dossier(o.dossier, o.source, o.licence)
        if not o.fichier:
            a.error("indiquez un fichier (ou --dossier)")
        deposer(o.fichier, o.decor, o.portrait, o.depart, o.video, o.source, o.licence)
    except L.ErreurSource as e:
        sys.exit("✖ " + L.masquer(e))


if __name__ == "__main__":
    main()
