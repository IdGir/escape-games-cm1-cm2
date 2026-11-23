#!/usr/bin/env python3
"""Génère evaluation-qcm.html (QCM imprimable + corrigé) à partir de assets/data/evaluations.json.
Usage : python generer-evaluation-qcm.py"""
import json, os, html
ICI = os.path.dirname(os.path.abspath(__file__))
d = {"qcm": json.load(open(os.path.join(ICI, "assets", "data", "qcm-cadres.json"), encoding="utf-8")), "metadata": json.load(open(os.path.join(ICI, "assets", "data", "evaluations.json"), encoding="utf-8"))["metadata"]}
L = "ABC"
SOUS_CORR = "Corrigé · réservé à l'enseignant"
e = html.escape

def entete(niv, sous):
    return (f'<header><div class="bandeau"><span class="logo">📜</span><div><div class="sur">Histoire · Cycle 3 · {niv}</div>'
            f'<h1>Le Manuscrit de l\'abbaye</h1></div><div class="pastille">{niv}</div></div>'
            f'<div class="sous">{sous}</div></header>')

def feuille(niv, qs):
    tot = sum(q.get("pts", 1) for q in qs)
    h = [f'<section class="page eleve n{niv}">', entete(niv, "Évaluation · QCM sur les leçons"),
         '<div class="id"><span>Nom <i></i></span><span>Prénom <i></i></span><span class="court">Date <i></i></span></div>',
         '<p class="cons">✎ <b>Consigne :</b> pour chaque question, coche <b>une seule</b> réponse.</p><div class="qs">']
    for i, q in enumerate(qs, 1):
        opts = "".join(f'<li><span class="bx"></span><span class="lt">{L[k]}</span><span class="tx">{e(o)}</span></li>' for k, o in enumerate(q["options"]))
        h.append(f'<div class="q"><div class="num">{i}</div><div class="cor"><p>{e(q["q"])}</p><ul>{opts}</ul></div></div>')
    h.append(f'</div><footer><span>Le Manuscrit de l\'abbaye — QCM {niv}</span><span class="score">Score : <i></i> / {tot}</span></footer></section>')
    return "".join(h)

def corrige(niv, qs):
    tot = sum(q.get("pts", 1) for q in qs)
    rows = "".join(f'<tr><td class="c">{i}</td><td>{e(q["q"])}</td><td class="ok"><b>{L[q["bonne"]]}</b> · {e(q["options"][q["bonne"]])}</td><td>{e(q.get("lecon",""))}</td><td class="c">{q.get("pts",1)}</td></tr>' for i, q in enumerate(qs, 1))
    return (f'<section class="page corrige n{niv}">{entete(niv, SOUS_CORR)}'
            f'<table><tr><th>N°</th><th>Question</th><th>Bonne réponse</th><th>Leçon</th><th>Pts</th></tr>{rows}</table>'
            f'<p class="tot">Total : {tot} points · 1 point par bonne réponse, 0 sinon. Questions tirées uniquement des encadrés des leçons du jeu.</p></section>')

pages = {n: feuille(n, d["qcm"][n]) for n in ("CM1", "CM2")}
corr = {n: corrige(n, d["qcm"][n]) for n in ("CM1", "CM2")}
src = e(d["metadata"].get("programme", ""))
CSS = '''
:root{--c:#111;--c2:#fff;--t:#111}
*{box-sizing:border-box}body{margin:0;font:13.5px/1.35 Georgia,"Times New Roman",serif;color:var(--t);background:#e6e6e6}
.barre{position:sticky;top:0;z-index:9;background:#fff;padding:10px 14px;border-bottom:1px solid #ccc;display:flex;gap:8px;flex-wrap:wrap;align-items:center;font-family:system-ui,Arial,sans-serif}
.barre button{font-size:15px;padding:8px 14px;border:0;border-radius:8px;background:#111;color:#fff;cursor:pointer}
.barre button.p{background:#1a7f37}
.page{width:210mm;min-height:297mm;margin:12px auto;padding:12mm 14mm;background:#fff;box-shadow:0 2px 10px #0003;display:flex;flex-direction:column;page-break-after:always}
header{margin-bottom:6px}
.bandeau{display:flex;align-items:center;gap:12px;background:#fff;color:#111;border:2.5px solid #111;border-radius:10px;padding:10px 16px;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.logo{font-size:30px;filter:grayscale(1)}.sur{font:11px system-ui,Arial,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#444}
h1{font-size:23px;margin:0;font-weight:700}
.pastille{margin-left:auto;background:#fff;color:#111;border:2px solid #111;font:700 18px system-ui,Arial,sans-serif;border-radius:20px;padding:4px 16px}
.sous{margin:6px 2px 0;font:600 13px system-ui,Arial,sans-serif;color:var(--c);letter-spacing:.06em;text-transform:uppercase;border-bottom:2px solid var(--c);padding-bottom:4px}
.id{display:flex;gap:16px;margin:10px 0 4px;font:13px system-ui,Arial,sans-serif}
.id span{flex:1;display:flex;align-items:flex-end;gap:6px}.id span.court{flex:.55}
.id i{flex:1;border-bottom:1.5px solid #333;height:14px}
.cons{margin:6px 0 8px;padding:6px 10px;background:#fff;border:1px solid #111;border-left:5px solid #111;border-radius:4px;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.qs{flex:1;display:flex;flex-direction:column;justify-content:space-evenly}
.q{display:flex;gap:10px;align-items:flex-start;break-inside:avoid;padding:3px 0}
.num{flex:none;width:26px;height:26px;border-radius:50%;background:#fff;color:#111;border:2px solid #111;font:700 14px system-ui,Arial,sans-serif;display:flex;align-items:center;justify-content:center;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.cor{flex:1}.cor p{margin:2px 0 4px;font-weight:700;font-size:14px}
ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:6px}
li{display:flex;align-items:center;gap:6px;border:1px solid #555;border-radius:6px;padding:4px 8px}
.bx{flex:none;width:13px;height:13px;border:1.8px solid #111;border-radius:3px}
.lt{flex:none;font:700 12px system-ui,Arial,sans-serif;color:var(--c)}
footer{display:flex;justify-content:space-between;align-items:flex-end;border-top:1px solid #999;padding-top:6px;margin-top:8px;font:11px system-ui,Arial,sans-serif;color:#555}
.score{font:700 15px system-ui,Arial,sans-serif;color:#111;border:2px solid var(--c);border-radius:8px;padding:5px 12px;display:inline-flex;gap:6px;align-items:flex-end}
.score i{display:inline-block;width:44px;border-bottom:1.5px solid #333;height:15px}
table{border-collapse:collapse;width:100%;margin-top:10px;font-family:system-ui,Arial,sans-serif;font-size:13px}
th{background:#fff;color:#111;border-top:2px solid #111;border-bottom:2px solid #111;text-align:left;padding:6px 8px;-webkit-print-color-adjust:exact;print-color-adjust:exact}
td{border-bottom:1px solid #ccc;padding:6px 8px}td.c{text-align:center}td.ok{background:#fff;font-weight:600;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.tot{font:600 13px system-ui,Arial,sans-serif;margin-top:10px}
body[data-show="CM1"] .nCM2,body[data-show="CM2"] .nCM1{display:none}
body[data-show="eleve"] .corrige{display:none}body[data-show="corrige"] .eleve{display:none}
@page{size:A4;margin:0}
@media print{body{background:#fff}.barre{display:none}.page{margin:0;box-shadow:none;width:210mm;height:297mm;min-height:0;overflow:hidden}}
'''
doc = f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>QCM — Le Manuscrit de l'abbaye</title>
<style>{CSS}</style></head><body data-show="tout">
<div class="barre"><b>Afficher / imprimer :</b>
<button onclick="m('CM1')">CM1</button><button onclick="m('CM2')">CM2</button>
<button onclick="m('eleve')">Feuilles élèves</button><button onclick="m('corrige')">Corrigés</button><button onclick="m('tout')">Tout</button>
<button class="p" onclick="print()">🖨️ Imprimer</button></div>
{pages["CM1"]}{corr["CM1"]}{pages["CM2"]}{corr["CM2"]}
<script>function m(v){{document.body.dataset.show=v}}</script>
<!-- Programme : {src} -->
</body></html>'''
open(os.path.join(ICI, "evaluation-qcm.html"), "w", encoding="utf-8").write(doc)
print("OK : evaluation-qcm.html")
