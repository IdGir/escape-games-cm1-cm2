# -*- coding: utf-8 -*-
"""Ajoute le bloc « Leçons à imprimer » dans ⚙️ Réglages (js/reglages.js) et un bouton
dans le tableau de bord (prof.html) de chaque jeu. Idempotent."""
import os, re, sys
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JEUX = ["chateau-fort", "moyen-age-abbaye", "station-meteo", "objets-techniques", "melanges",
        "constitution", "declaration", "tour-du-monde"]
SANS_SALLE = {"declaration", "tour-du-monde"}
MARQUE = "btn-lecons-a4"

for jeu in JEUX:
    p = os.path.join(RACINE, jeu, "js", "reglages.js")
    s = open(p, encoding="utf-8").read()
    if MARQUE not in s:
        m = re.search(r'<button class="btn ([a-z]+)" id="btn-imprimer-prepa">[^<(]*\(5 ([a-zé]+)s\)', s)
        classe, unite = m.group(1), m.group(2)
        options = "" if jeu in SANS_SALLE else "".join(
            f'<option value="salle={i}">{unite.capitalize()} {i}</option>' for i in range(1, 6))
        bloc = f'''<div class="reglages-group">
      <h4>📖 Leçons à imprimer (A4 illustrées)</h4>
      <p style="font-size:.85rem;opacity:.8;font-style:italic;margin-bottom:10px">Une page A4 par leçon : texte CM1 ou CM2, cartes, schémas, graphiques, frise, lexique et compétence du programme. L'aperçu s'ouvre dans un nouvel onglet ; cliquez ensuite sur « Imprimer ».</p>
      <div style="display:flex;flex-wrap:wrap;gap:8px;align-items:center">
        <select id="reg-lecon-a4" style="flex:1;min-width:150px"><option value="lecon=toutes">Toutes les leçons</option>{options}</select>
        <button class="btn {classe}" id="btn-lecons-a4-cm1">📖 CM1</button>
        <button class="btn {classe}" id="btn-lecons-a4-cm2">📖 CM2</button>
      </div>
    </div>

    '''
        i = s.index("<h4>🖨️ Impressions A4</h4>")
        d = s.rindex('<div class="reglages-group">', 0, i)
        s = s[:d] + bloc + s[d:]
        ancre = 'corps.querySelector("#btn-imprimer-tout").addEventListener("click", ()=>imprimerFiches("tout"));'
        js = ancre + '''
  const ouvrirLeconsA4 = n => window.open("lecons-imprimables.html?niveau=" + n + "&" + corps.querySelector("#reg-lecon-a4").value, "_blank");
  corps.querySelector("#btn-lecons-a4-cm1").addEventListener("click", ()=>ouvrirLeconsA4("CM1"));
  corps.querySelector("#btn-lecons-a4-cm2").addEventListener("click", ()=>ouvrirLeconsA4("CM2"));'''
        assert ancre in s, jeu
        s = s.replace(ancre, js, 1)
        with open(p, "w", encoding="utf-8", newline="") as f:
            f.write(s)
        print("réglages :", jeu)
    q = os.path.join(RACINE, jeu, "prof.html")
    h = open(q, encoding="utf-8").read()
    if "lecons-imprimables.html" not in h:
        a = """<button class="vert" onclick="window.open('index.html','_blank')">🎮 Ouvrir un poste élève</button>"""
        h = h.replace(a, a + """\n    <button class="bleu" onclick="window.open('lecons-imprimables.html','_blank')">📖 Leçons à imprimer (A4)</button>""", 1)
        with open(q, "w", encoding="utf-8", newline="") as f:
            f.write(h)
        print("tableau de bord :", jeu)
