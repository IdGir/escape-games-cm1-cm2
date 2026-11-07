#!/usr/bin/env python3
"""Met à jour le tableau « jeu par jeu » de enseignant.html (espace enseignant).

    python outils-docs/maj-espace-enseignant.py

Lit commun/donnees/catalogue.js (via Node) et sequences/donnees.js, et ne met un lien
que si le fichier existe. Réécrit uniquement ce qui est entre <!-- JEUX:DEBUT --> et
<!-- JEUX:FIN --> : le reste de la page est écrit à la main.
"""
import json, os, re, subprocess, sys, html

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GITHUB = "https://github.com/IdGir/escape-games-cm1-cm2/blob/escape-games/"
# Jeux présents dans le dépôt mais absents du catalogue (modèle de référence du moteur immersif).
EXTRAS = [{"dossier": "vingt-mille-lieues", "titre": "Le Journal du Nautilus", "matiere": "Modèle immersif", "icone": "🔱"}]

def catalogue():
    js = ("const fs=require('fs');const t=fs.readFileSync('commun/donnees/catalogue.js','utf8');"
          "console.log(JSON.stringify(new Function(t+';return CATALOGUE')().jeux))")
    # Node écrit en UTF-8 : le dire à Python, sinon Windows lit en cp1252 et plante.
    out = subprocess.run(["node", "-e", js], cwd=RACINE, capture_output=True, encoding="utf-8", check=True).stdout
    return [j for j in json.loads(out) if j.get("dossier")]

def sequences():
    t = open(os.path.join(RACINE, "sequences", "donnees.js"), encoding="utf-8").read()
    return set(re.findall(r'^\s{1,4}"([a-z0-9-]+)":\s*\{', t, re.M))

def existe(*p):
    return os.path.exists(os.path.join(RACINE, *p))

def lien(texte, href, externe=False):
    cible = ' target="_blank" rel="noopener"' if externe else ""
    return f'<a href="{html.escape(href)}"{cible}>{texte}</a>'

def vide():
    return '<td class="vide">—</td>'

def ligne(j, seq):
    d = j["dossier"]
    jouer = []
    if j.get("immersif") and existe(j["immersif"], "index.html"):
        jouer.append(lien("Immersif", j["immersif"] + "/"))
    if existe(d, "index.html"):
        jouer.append(lien("Classique", d + "/"))
    tdb = []
    if existe(d, "prof.html"):
        tdb.append(lien("Classique", d + "/prof.html"))
    if j.get("immersif") and existe(j["immersif"], "prof.html"):
        tdb.append(lien("Immersif", j["immersif"] + "/prof.html"))
    guide = lien("Guide", GITHUB + d + "/GUIDE-PEDAGOGIQUE.md", True) if existe(d, "GUIDE-PEDAGOGIQUE.md") else None
    readme = lien("README (solutions)", GITHUB + d + "/README.md", True) if existe(d, "README.md") else None
    docs = " ".join(x for x in (guide, readme) if x)
    lecons = lien("Imprimer", d + "/lecons-imprimables.html") if existe(d, "lecons-imprimables.html") else None
    sequence = lien("Fiche", "sequences/fiche.html?jeu=" + d) if d in seq else None
    averifier = lien("À vérifier", GITHUB + d + "/A-VERIFIER.md", True) if existe(d, "A-VERIFIER.md") else None
    cell = lambda v: f"<td>{v}</td>" if v else vide()
    titre = f'<td class="jeu">{j.get("icone", "")} <b>{html.escape(j["titre"])}</b><small>{html.escape(j.get("matiere", ""))}</small></td>'
    return "<tr>" + titre + cell(" ".join(jouer)) + cell(" ".join(tdb)) + cell(docs) + cell(lecons) + cell(sequence) + cell(averifier) + "</tr>"

def main():
    seq = sequences()
    jeux = catalogue() + [e for e in EXTRAS if existe(e["dossier"], "index.html")]
    lignes = "\n".join("      " + ligne(j, seq) for j in jeux)
    tableau = ("<table>\n    <thead><tr><th>Jeu</th><th>Jouer</th><th>Tableau de bord</th><th>Guide et solutions</th>"
               "<th>Leçons A4</th><th>Séquence</th><th>À vérifier</th></tr></thead>\n    <tbody>\n" + lignes + "\n    </tbody>\n  </table>")
    chemin = os.path.join(RACINE, "enseignant.html")
    page = open(chemin, encoding="utf-8").read()
    neuf, n = re.subn(r"(<!-- JEUX:DEBUT -->).*?(<!-- JEUX:FIN -->)", lambda m: m.group(1) + "\n  " + tableau + "\n" + m.group(2), page, flags=re.S)
    if n != 1:
        sys.exit("Repères JEUX:DEBUT / JEUX:FIN introuvables dans enseignant.html")
    with open(chemin, "w", encoding="utf-8", newline="\n") as f:
        f.write(neuf)
    print(f"enseignant.html mis à jour : {len(jeux)} jeux.")

if __name__ == "__main__":
    main()
