#!/usr/bin/env python3
"""La mise à jour du moteur (migrer-jeu.py --maj-moteur) ne doit RIEN changer à une variante immersive à jour.

    python3 vingt-mille-lieues/tests/test-maj-moteur.py [jeu ...]      (sans argument : toutes les variantes de immersifs/)

Pourquoi : --maj-moteur recopiait index.html, prof.html et sw.js de la source vingt-mille-lieues/, plus ancienne ;
les boutons enseignant (coup de pouce, fin de séance, correction collective, séquence, bandeau serveur), les greffons
de commun/, le lien « Version classique » et les données du cache hors ligne disparaissaient.
Chaque variante est copiée dans .tmp-test-maj/ (même profondeur), mise à jour, comparée, puis la copie est effacée.
"""
import os, sys, shutil, subprocess, filecmp
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MIGRER = os.path.join(RACINE, "vingt-mille-lieues", "outils", "immersif", "migrer-jeu.py")
TMP = os.path.join(RACINE, ".tmp-test-maj")
jeux = sys.argv[1:] or sorted(d for d in os.listdir(os.path.join(RACINE, "immersifs")) if os.path.isfile(os.path.join(RACINE, "immersifs", d, "js", "jeu-config.js")))
echecs = 0
def differences(a, b):
    c = filecmp.dircmp(a, b); out = [os.path.relpath(os.path.join(a, f), a) for f in c.diff_files + c.left_only + c.right_only]
    for s in c.common_dirs: out += [os.path.join(s, x) for x in differences(os.path.join(a, s), os.path.join(b, s))]
    return out
try:
    for jeu in jeux:
        src = os.path.join(RACINE, "immersifs", jeu); dst = os.path.join(TMP, jeu)
        shutil.rmtree(dst, ignore_errors=True); shutil.copytree(src, dst, ignore=shutil.ignore_patterns("*.mp4", "*.mp3", "*.webm"))
        r = subprocess.run([sys.executable, MIGRER, "--maj-moteur", dst], capture_output=True, text=True, encoding="utf-8")
        if r.returncode: print(f"✖ {jeu} : --maj-moteur échoue : {r.stderr.strip()[-300:]}"); echecs += 1; continue
        d = [x for x in differences(src, dst) if not x.endswith((".mp4", ".mp3", ".webm"))]
        if d: print(f"✖ {jeu} : --maj-moteur modifie {len(d)} fichier(s) : {', '.join(d[:8])}"); echecs += 1
        else: print(f"✔ {jeu}")
finally:
    shutil.rmtree(TMP, ignore_errors=True)
print(f"\n{len(jeux)} variante(s), {echecs} échec(s)")
sys.exit(1 if echecs else 0)
