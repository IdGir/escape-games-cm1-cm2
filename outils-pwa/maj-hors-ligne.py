# -*- coding: utf-8 -*-
"""Met à jour la liste des fichiers gardés hors connexion par l'application installable (PWA).

    python outils-pwa/maj-hors-ligne.py

À relancer après chaque modification du code ou des données d'un jeu, AVANT de publier :
écrit sw-fichiers.js à la racine (liste + numéro de version). Le numéro change dès qu'un
fichier change : les tablettes installées téléchargent alors la nouvelle version.
  - FICHIERS_CODE : pages, scripts, styles, polices, icônes, données JSON (toujours gardés, ~4 Mo) ;
  - IMAGES_JEUX   : images et documents PDF de chaque jeu (gardés à la demande, bouton de l'accueil) ;
  - les vidéos ne sont jamais gardées hors connexion (trop lourdes) : sans réseau, le jeu
    affiche l'image ou le décor dessiné à la place, comme quand une vidéo manque.
Seuls les fichiers suivis par git sont listés (rien de local ni de privé).
"""
import hashlib, json, os, subprocess
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCLUS = ("outils-", "prompts-opus/", "_a-supprimer/", ".claude/")
CODE = (".html", ".js", ".css", ".woff2", ".webmanifest", ".json")
IMAGES = (".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".pdf")

def suivis():
    sortie = subprocess.run(["git", "ls-files", "-z"], cwd=RACINE, capture_output=True, check=True).stdout
    return sorted(f for f in sortie.decode("utf-8").split("\0") if f)

def main():
    code, images = [], {}
    for f in suivis():
        if f.startswith(EXCLUS) or "/tests/" in f or f in ("sw-fichiers.js", "sw.js"):
            continue
        ext = os.path.splitext(f)[1].lower()
        if "/assets/" in f:
            jeu = f.split("/")[0]
            if "/assets/data/" in f or f.endswith("/assets/medias/medias.json"):
                if ext in CODE: code.append(f)
            elif ext in IMAGES:
                images.setdefault(jeu, []).append(f)
        elif ext in CODE or f.startswith("commun/icones/"):
            code.append(f)
    h = hashlib.sha1()
    for f in code + [x for l in images.values() for x in l]:
        with open(os.path.join(RACINE, f), "rb") as fh:
            h.update(f.encode("utf-8")); h.update(hashlib.sha1(fh.read()).digest())
    version = h.hexdigest()[:10]
    taille = sum(os.path.getsize(os.path.join(RACINE, f)) for f in code)
    js = ("/* Fichier GÉNÉRÉ par outils-pwa/maj-hors-ligne.py — ne pas modifier à la main.\n"
          "   Liste des fichiers gardés hors connexion par sw.js (application installable). */\n"
          f"self.VERSION_HORS_LIGNE = {json.dumps(version)};\n"
          f"self.FICHIERS_CODE = {json.dumps(code, ensure_ascii=False, indent=0)};\n"
          f"self.IMAGES_JEUX = {json.dumps(images, ensure_ascii=False, indent=0)};\n")
    with open(os.path.join(RACINE, "sw-fichiers.js"), "w", encoding="utf-8", newline="\n") as f:
        f.write(js)
    print(f"sw-fichiers.js : version {version}, {len(code)} fichiers de code ({taille/1e6:.1f} Mo), "
          f"{sum(len(l) for l in images.values())} images/documents dans {len(images)} jeux.")
    print("Pensez à ajouter sw-fichiers.js au prochain commit.")

if __name__ == "__main__":
    main()
