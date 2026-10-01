# -*- coding: utf-8 -*-
"""Moteur v2 : fichiers communs pour les jeux à moteur propre (Déclaration, Tour du monde).

    python outils-moteur/installer_anciens.py

- copie v2-ancien.js → <jeu>/js/v2.js et fiche-mission.js → <jeu>/js/fiche-mission.js ;
- écrit <jeu>/css/v2.css (styles du moteur v2) ;
- restaure les feuilles de style absentes du dépôt à partir de celles de
  Constitution (même structure de page) ; le Tour du monde reçoit en plus sa
  charte (outils-moteur/theme-tour-du-monde.css) ;
- branche les scripts dans index.html (avant app.js) et le bouton
  « Fiche de mission » dans ⚙️ Réglages.
Idempotent. Les énigmes elles-mêmes sont réécrites à la main dans chaque jeu.
"""
import os
import re
import shutil
import sys

# Depuis le tronc commun (amélioration A3, octobre 2026), le moteur n'existe plus qu'en UN
# exemplaire dans commun/js/ : ce script d'installation du moteur v2 a déjà été appliqué et
# recopierait des fichiers devenus inutiles dans les jeux. Il est conservé pour mémoire.
if os.path.exists(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "commun", "js", "enigmes.js")):
    print("Moteur v2 déjà installé. Depuis le tronc commun, corrigez directement commun/js/ (voir commun/README.md).")
    sys.exit(0)

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M = os.path.join(RACINE, "outils-moteur")
JEUX = ["declaration", "tour-du-monde"]

CSS_EXTRA = """
/* ---- Bandeau « mot à noter » et coffre final (jeux à moteur propre) ---- */
.mot-cle{margin:16px auto;max-width:460px;text-align:center;
  background:linear-gradient(135deg,#fff6d8,#f2e3ad);border:3px double #c9a227;border-radius:14px;padding:14px}
.mot-cle .lib{font-size:.8rem;letter-spacing:2px;text-transform:uppercase;opacity:.7}
.mot-cle .val{font-size:1.9rem;font-weight:bold;letter-spacing:6px;color:#14285a}
.zone-enigme.secoue{animation:secoue-v2 .4s}
@keyframes secoue-v2{0%,100%{transform:translateX(0)}25%{transform:translateX(-7px)}75%{transform:translateX(7px)}}
.zone-enigme.resolue .btn.vert{opacity:.5}
.coffre-final h3{text-align:center}
"""


def lire(p):
    with open(p, encoding="utf-8", newline="") as f:
        return f.read()


def ecrire(p, s):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(s)


def installer(jeu):
    d = os.path.join(RACINE, jeu)
    shutil.copyfile(os.path.join(M, "v2-ancien.js"), os.path.join(d, "js", "v2.js"))
    shutil.copyfile(os.path.join(M, "fiche-mission.js"), os.path.join(d, "js", "fiche-mission.js"))
    ecrire(os.path.join(d, "css", "v2.css"), lire(os.path.join(M, "enigmes-v2.css")) + CSS_EXTRA)
    # Feuilles de style absentes du dépôt : base commune (Constitution, issue de la
    # Déclaration) ; le Tour du monde y ajoute sa charte « carnet de voyage ».
    for f in ("style", "video", "animations", "personnages", "print"):
        cible = os.path.join(d, "css", f + ".css")
        if not os.path.exists(cible):
            shutil.copyfile(os.path.join(RACINE, "constitution", "css", f + ".css"), cible)
    if jeu == "tour-du-monde":
        p = os.path.join(d, "css", "style.css")
        s = lire(p)
        if "LE TOUR DU MONDE EN 80 JOURS" not in s:
            ecrire(p, s.rstrip() + "\n" + lire(os.path.join(M, "theme-tour-du-monde.css")))
    # index.html
    p = os.path.join(d, "index.html")
    s = lire(p)
    nl = "\r\n" if "\r\n" in s else "\n"
    if "css/v2.css" not in s:
        s = re.sub(r'(<link rel="stylesheet" href="css/print\.css[^"]*"[^>]*>)',
                   r'<link rel="stylesheet" href="css/v2.css?m2">' + nl.replace("\\", "\\\\") + r'\1', s, count=1)
    if "js/v2.js" not in s:
        s = re.sub(r'(<script src="js/enigmes\.js[^"]*"></script>)',
                   r'<script src="js/v2.js?m2"></script>' + nl.replace("\\", "\\\\") + r'\1', s, count=1)
    if "js/fiche-mission.js" not in s:
        s = re.sub(r'(<script src="js/impression\.js[^"]*"></script>)',
                   r'\1' + nl.replace("\\", "\\\\") + r'<script src="js/fiche-mission.js?m2"></script>', s, count=1)
    for f in ("js/enigmes.js", "js/app.js", "js/reglages.js", "js/impression.js", "css/style.css"):
        s = re.sub(r'(%s)\?[^"]*"' % re.escape(f), r'\1?m2"', s)
    for f in ("js/v2.js", "js/enigmes.js", "js/app.js"):
        if f not in s:
            raise RuntimeError(jeu + " : script absent de index.html : " + f)
    ecrire(p, s)
    # reglages.js : bouton « Fiche de mission »
    p = os.path.join(d, "js", "reglages.js")
    s = lire(p)
    if "btn-imprimer-mission" not in s:
        s = re.sub(r'(\n(\s*)<button class="btn [\w-]+" id="btn-imprimer-tout">)',
                   r'\n\2<button class="btn vert" id="btn-imprimer-mission">✍️ Fiche de mission (1 par équipe)</button>\1', s, count=1)
        s = s.replace('  corps.querySelector("#btn-imprimer-tout").addEventListener(',
                      '  corps.querySelector("#btn-imprimer-mission").addEventListener("click", ()=>imprimerFicheMission());\n'
                      '  corps.querySelector("#btn-imprimer-tout").addEventListener(', 1)
        if 'btn-imprimer-mission").addEventListener' not in s or 'id="btn-imprimer-mission"' not in s:
            raise RuntimeError(jeu + " : bouton fiche de mission non branché")
        ecrire(p, s)
    print("moteur v2 (fichiers communs) :", jeu)


if __name__ == "__main__":
    for j in JEUX:
        installer(j)
