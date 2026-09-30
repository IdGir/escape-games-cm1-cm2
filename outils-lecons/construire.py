# -*- coding: utf-8 -*-
"""Construit <jeu>/assets/data/lecons-a4.json à partir de outils-lecons/jeux/<jeu>.py.

    python outils-lecons/construire.py chateau-fort      (un jeu)
    python outils-lecons/construire.py tous               (tous les jeux configurés)

Chaque configuration de jeu définit :
  JEU     : en-tête (titre, matière, thème, couleurs…)
  LECONS  : {id_leçon: {"competence": "...", "visuels": [...], "masquer": [...]}}
  LECONS_BASE (facultatif) : leçons rédigées pour l'impression quand le jeu
                             n'a pas de leçons texte (constitution).

Types de visuels :
  {"type":"carte", "spec":{…}}  → carte SVG générée par carte.mjs (Natural Earth)
  {"type":"svg", "svg":"<svg…>"} → schéma ou graphique (voir graphiques.py)
  {"type":"photo", "src":"assets/images/…"} → photo du jeu ; le crédit est lu
                                   dans assets/medias/CREDITS-medias.md
  {"type":"schema"}             → place le schéma déjà présent dans lecons.json
Options communes : titre, etiquette, legende, source/credit, largeur:"pleine".
"""
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
SOURCE_CARTE = "Fond de carte : Natural Earth (domaine public)."


def credits(jeu):
    """Lit le tableau de CREDITS-medias.md → {chemin: texte du crédit}."""
    chemin = os.path.join(RACINE, jeu, "assets", "medias", "CREDITS-medias.md")
    res = {}
    if not os.path.exists(chemin):
        return res
    for ligne in open(chemin, encoding="utf-8-sig"):
        if not ligne.startswith("| `"):
            continue
        cols = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if len(cols) < 5:
            continue
        fichier = cols[0].strip("`")
        m = re.search(r"\[(.*?)\]\((.*?)\)", cols[2])
        url = m.group(2) if m else ""
        site = ("Wikimedia Commons" if "wikimedia" in url else "Pixabay" if "pixabay" in url
                else "Gallica (BnF)" if "gallica" in url else (m.group(1) if m else cols[2]))
        res[fichier] = {"sujet": cols[1], "auteur": cols[3], "licence": cols[4], "site": site}
    return res


def credit_photo(info):
    return f"Photo : {info['auteur']} — {info['licence']} — {info['site']}."


def carte(spec):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(spec, f, ensure_ascii=False)
        nom = f.name
    try:
        out = subprocess.run(["node", os.path.join(ICI, "carte.mjs"), nom], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as err:
        print(err.stderr)
        raise
    finally:
        os.unlink(nom)
    return out.stdout


def copier_modele(jeu, scripts):
    """Copie la page, le script et la feuille de style communs dans le dossier du jeu."""
    mod = os.path.join(ICI, "modele")
    html = open(os.path.join(mod, "lecons-imprimables.html"), encoding="utf-8").read()
    if scripts:
        tags = "".join(f'  <script src="{s}"></script>\n' for s in scripts)
        html = html.replace('  <script src="js/lecons-a4.js"></script>', tags + '  <script src="js/lecons-a4.js"></script>')
    ecrire(os.path.join(RACINE, jeu, "lecons-imprimables.html"), html)
    for src, dst in (("lecons-a4.js", "js"), ("lecons-a4.css", "css")):
        ecrire(os.path.join(RACINE, jeu, dst, src), open(os.path.join(mod, src), encoding="utf-8").read())


def ecrire(chemin, contenu):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, "w", encoding="utf-8", newline="\n") as f:
        f.write(contenu)


def charger(jeu):
    chemin = os.path.join(ICI, "jeux", jeu.replace("-", "_") + ".py")
    spec = importlib.util.spec_from_file_location("cfg_" + jeu.replace("-", "_"), chemin)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, ICI)
    spec.loader.exec_module(mod)
    return mod


def construire(jeu):
    cfg = charger(jeu)
    cred = credits(jeu)
    sortie = {"_commentaire": "Généré par outils-lecons/construire.py — ne pas modifier à la main : "
                              "éditer outils-lecons/jeux/" + jeu.replace("-", "_") + ".py puis relancer.",
              "jeu": cfg.JEU, "lecons": {}}
    if getattr(cfg, "LECONS_BASE", None):
        sortie["lecons_base"] = cfg.LECONS_BASE
    manquants = []
    for lid, l in cfg.LECONS.items():
        visuels = []
        for v in l.get("visuels", []):
            v = dict(v)
            if v["type"] == "carte":
                v["svg"] = carte(v.pop("spec"))
                v["type"] = "svg"
                v.setdefault("etiquette", "Carte")
                v.setdefault("source", SOURCE_CARTE)
            elif v["type"] == "photo":
                if not os.path.exists(os.path.join(RACINE, jeu, v["src"])):
                    manquants.append(v["src"])
                info = cred.get(v["src"])
                if info:
                    v.setdefault("credit", credit_photo(info))
                    v.setdefault("titre", info["sujet"])
                v.setdefault("etiquette", "Photo")
            elif v["type"] == "svg":
                v.setdefault("etiquette", "Schéma")
            visuels.append(v)
        entree = {k: val for k, val in l.items() if k != "visuels"}
        entree["visuels"] = visuels
        sortie["lecons"][lid] = entree
    copier_modele(jeu, getattr(cfg, "SCRIPTS", []))
    dest = os.path.join(RACINE, jeu, "assets", "data", "lecons-a4.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8", newline="\n") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
    taille = os.path.getsize(dest) // 1024
    print(f"{jeu} : {len(sortie['lecons'])} leçons, {taille} Ko → {os.path.relpath(dest, RACINE)}")
    for m in manquants:
        print(f"  !! photo introuvable : {m}")


if __name__ == "__main__":
    cibles = sys.argv[1:] or ["tous"]
    if cibles == ["tous"]:
        cibles = sorted(f[:-3].replace("_", "-") for f in os.listdir(os.path.join(ICI, "jeux")) if f.endswith(".py") and not f.startswith("_"))
    for j in cibles:
        construire(j)
