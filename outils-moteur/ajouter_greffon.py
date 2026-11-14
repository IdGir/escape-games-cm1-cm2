#!/usr/bin/env python3
"""Ajoute une balise <script> de greffon commun dans les index.html des 12 jeux « salles ».

    python outils-moteur/ajouter_greffon.py correction-collective.js            (après export-partie.js)
    python outils-moteur/ajouter_greffon.py mascotte.js --apres mode-duel.js --version c1
    python outils-moteur/ajouter_greffon.py x.js --fichier prof.html --apres '<script>' --avant

Idempotent : ne fait rien si le greffon est déjà chargé. Un greffon qui change de comportement :
augmenter son numéro de version (?c2…) avec --version et --remplacer.
"""
import argparse, pathlib, re, sys
JEUX = ["declaration", "tour-du-monde", "constitution", "moyen-age-abbaye", "station-meteo", "melanges",
        "objets-techniques", "chateau-fort", "versailles", "renaissance", "alimentation", "lumiere", "etats-matiere", "mouvement", "traite-colonies"]
IMMERSIFS = ["alimentation", "chateau-fort", "constitution", "electricite", "etats-matiere", "grandes-explorations", "lumiere", "melanges", "mouvement", "moyen-age-abbaye", "naissances-animaux", "objets-techniques", "renaissance", "station-meteo", "traite-colonies", "versailles"]
RACINE = pathlib.Path(__file__).resolve().parent.parent

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("greffon")
    ap.add_argument("--apres", default="export-partie.js", help="nom du script après lequel insérer")
    ap.add_argument("--version", default="c1")
    ap.add_argument("--fichier", default="index.html")
    ap.add_argument("--jeux", nargs="*", default=None)
    ap.add_argument("--base", default="", help="sous-dossier des jeux (ex. immersifs : les pages sont alors à ../../commun/)")
    ap.add_argument("--remplacer", action="store_true", help="met à jour le numéro de version si déjà présent")
    ap.add_argument("--dossier", default="js", help="js, donnees ou css (css : balise <link>)")
    a = ap.parse_args()
    if a.jeux is None:
        a.jeux = IMMERSIFS if a.base else JEUX
    n = 0
    for jeu in a.jeux:
        f = RACINE / a.base / jeu / a.fichier
        if not f.exists():
            continue
        t = f.read_text(encoding="utf-8")
        crlf = "\r\n" in t
        pre = "../../" if a.base else "../"
        balise = f'<script src="{pre}commun/{a.dossier}/{a.greffon}?{a.version}"></script>'
        if a.dossier == "css":
            balise = f'<link rel="stylesheet" href="{pre}commun/css/{a.greffon}?{a.version}">'
        deja = re.search(re.escape(f"commun/{a.dossier}/{a.greffon}") + r"\?\w+", t)
        if deja:
            if a.remplacer:
                t2 = t.replace(deja.group(0), f"commun/{a.dossier}/{a.greffon}?{a.version}")
                if t2 != t:
                    f.write_text(t2, encoding="utf-8", newline=""); n += 1
            continue
        m = re.search(r'^[ \t]*<(?:script|link)[^>]*' + re.escape(a.apres) + r'[^>]*>(?:</script>)?[ \t]*\r?\n', t, re.M)
        if not m:
            print(f"⚠ {jeu}/{a.fichier} : « {a.apres} » introuvable", file=sys.stderr); continue
        fin = "\r\n" if crlf else "\n"
        t = t[:m.end()] + balise + fin + t[m.end():]
        f.write_text(t, encoding="utf-8", newline=""); n += 1
    print(f"{n} fichier(s) modifié(s)")

main()
