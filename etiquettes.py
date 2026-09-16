"""etiquettes.py — Imprimer les badges sur planches d'étiquettes autocollantes,
et les leçons du classeur en cartes A6 / A7 pour porte-clés plastifiés.

Le principe est le même dans les deux cas : une page A4, une grille dont on
connaît exactement la géométrie en millimètres, et un contenu placé case par
case. Le navigateur se charge de l'impression.

IMPORTANT — le calage
    Aucune imprimante n'imprime exactement là où on lui dit : il y a toujours
    un décalage de un ou deux millimètres, variable d'une machine à l'autre.
    On propose donc un réglage de décalage (en mm, horizontal et vertical) et
    une impression d'essai sur papier ordinaire. C'est le seul moyen fiable :
    on tient la feuille d'essai devant la planche d'étiquettes à la lumière.
"""

# --------------------------------------------------------------------------
#  Planches d'étiquettes
#
#  Géométrie : tout en millimètres.
#    marge_h / marge_v : distance du bord de la feuille au bord de la 1re case
#    pas_h / pas_v     : distance entre deux débuts de case
# --------------------------------------------------------------------------
PLANCHES = {
    # ---- Rectangulaires, les plus répandues ----
    "L7160": {"nom": "Avery L7160 / 3652 — 21 par feuille (63,5 × 38,1 mm)",
              "l": 63.5, "h": 38.1, "cols": 3, "lignes": 7,
              "marge_h": 7.2, "marge_v": 15.1, "pas_h": 66.0, "pas_v": 38.1,
              "forme": "rect", "usage": "badges"},
    "L7161": {"nom": "Avery L7161 — 18 par feuille (63,5 × 46,6 mm)",
              "l": 63.5, "h": 46.6, "cols": 3, "lignes": 6,
              "marge_h": 7.2, "marge_v": 12.9, "pas_h": 66.0, "pas_v": 46.6,
              "forme": "rect", "usage": "badges"},
    "L7163": {"nom": "Avery L7163 / 3475 — 14 par feuille (99,1 × 38,1 mm)",
              "l": 99.1, "h": 38.1, "cols": 2, "lignes": 7,
              "marge_h": 5.0, "marge_v": 15.1, "pas_h": 101.6, "pas_v": 38.1,
              "forme": "rect", "usage": "badges"},
    "L7165": {"nom": "Avery L7165 / 3483 — 8 par feuille (99,1 × 67,7 mm)",
              "l": 99.1, "h": 67.7, "cols": 2, "lignes": 4,
              "marge_h": 5.0, "marge_v": 13.0, "pas_h": 101.6, "pas_v": 67.7,
              "forme": "rect", "usage": "badges"},
    "L7166": {"nom": "Avery L7166 — 6 par feuille (99,1 × 93,1 mm)",
              "l": 99.1, "h": 93.1, "cols": 2, "lignes": 3,
              "marge_h": 5.0, "marge_v": 4.7, "pas_h": 101.6, "pas_v": 93.1,
              "forme": "rect", "usage": "badges"},
    "L7651": {"nom": "Avery L7651 — 65 par feuille (38,1 × 21,2 mm)",
              "l": 38.1, "h": 21.2, "cols": 5, "lignes": 13,
              "marge_h": 4.8, "marge_v": 10.7, "pas_h": 40.6, "pas_v": 21.2,
              "forme": "rect", "usage": "badges"},
    "L7159": {"nom": "Avery L7159 — 24 par feuille (63,5 × 33,9 mm)",
              "l": 63.5, "h": 33.9, "cols": 3, "lignes": 8,
              "marge_h": 7.2, "marge_v": 13.0, "pas_h": 66.0, "pas_v": 33.9,
              "forme": "rect", "usage": "badges"},
    "L7169": {"nom": "Avery L7169 — 4 par feuille (99,1 × 139 mm)",
              "l": 99.1, "h": 139.0, "cols": 2, "lignes": 2,
              "marge_h": 5.0, "marge_v": 8.5, "pas_h": 101.6, "pas_v": 139.0,
              "forme": "rect", "usage": "lecons"},
    # ---- Rondes : très pratiques pour des badges de récompense ----
    "ROND40": {"nom": "Étiquettes rondes Ø 40 mm — 24 par feuille",
               "l": 40.0, "h": 40.0, "cols": 4, "lignes": 6,
               "marge_h": 13.0, "marge_v": 12.0, "pas_h": 46.0, "pas_v": 45.0,
               "forme": "rond", "usage": "badges"},
    "ROND60": {"nom": "Étiquettes rondes Ø 60 mm — 12 par feuille",
               "l": 60.0, "h": 60.0, "cols": 3, "lignes": 4,
               "marge_h": 12.0, "marge_v": 20.0, "pas_h": 65.0, "pas_v": 65.0,
               "forme": "rond", "usage": "badges"},
    "ROND30": {"nom": "Étiquettes rondes Ø 30 mm — 40 par feuille",
               "l": 30.0, "h": 30.0, "cols": 5, "lignes": 8,
               "marge_h": 15.0, "marge_v": 13.0, "pas_h": 36.0, "pas_v": 33.0,
               "forme": "rond", "usage": "badges"},
    # ---- Cartes pour porte-clés ----
    "A6": {"nom": "Cartes A6 — 4 par feuille (105 × 148 mm)",
           "l": 105.0, "h": 148.0, "cols": 2, "lignes": 2,
           "marge_h": 0.0, "marge_v": 0.5, "pas_h": 105.0, "pas_v": 148.5,
           "forme": "carte", "usage": "lecons"},
    "A7": {"nom": "Cartes A7 — 8 par feuille (74 × 105 mm)",
           "l": 74.0, "h": 105.0, "cols": 2, "lignes": 4,
           "marge_h": 31.0, "marge_v": 0.5, "pas_h": 74.0, "pas_v": 74.2,
           "forme": "carte", "usage": "lecons"},
    "CARTE_CLASSEUR": {
        "nom": "Format d'origine du classeur — 8 par feuille (105 × 74,2 mm)",
        "l": 105.0, "h": 74.2, "cols": 2, "lignes": 4,
        "marge_h": 0.0, "marge_v": 0.5, "pas_h": 105.0, "pas_v": 74.2,
        "forme": "carte", "usage": "lecons"},
    "LIBRE": {"nom": "Format personnalisé (à régler)",
              "l": 63.5, "h": 38.1, "cols": 3, "lignes": 7,
              "marge_h": 7.2, "marge_v": 15.1, "pas_h": 66.0, "pas_v": 38.1,
              "forme": "rect", "usage": "badges"},
}


def planches(usage=None):
    return [{"cle": k, **v} for k, v in PLANCHES.items()
            if not usage or v["usage"] == usage]


def _esc(s):
    return (str(s or "").replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;"))


def _css_grille(g, dx=0.0, dy=0.0):
    """La feuille et sa grille, calées au millimètre."""
    rond = "border-radius:50%;" if g["forme"] == "rond" else \
           ("border-radius:3mm;" if g["forme"] == "carte" else "border-radius:2mm;")
    return f"""
@page {{ size: A4; margin: 0; }}
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{font-family:"Segoe UI",system-ui,Arial,sans-serif;background:#e9edf3;}}
.feuille{{
  position:relative; width:210mm; height:297mm; background:#fff;
  margin:0 auto 8mm; page-break-after:always; overflow:hidden;
}}
.feuille:last-child{{page-break-after:auto;}}
.case{{
  position:absolute; width:{g['l']}mm; height:{g['h']}mm; {rond}
  overflow:hidden; display:flex; align-items:center; justify-content:center;
}}
/* Repères de découpe : visibles à l'essai, masqués à l'impression réelle */
.contour{{border:0.2mm dashed #c8cedb;}}
@media print{{
  body{{background:#fff;}}
  .feuille{{margin:0;box-shadow:none;}}
  .noprint{{display:none !important;}}
  .contour{{border-color:transparent;}}
  .contour.garder{{border-color:#c8cedb;}}
}}
@media screen{{.feuille{{box-shadow:0 2px 14px rgba(0,0,0,.16);}}}}
.barre{{position:sticky;top:0;background:#1E2233;color:#fff;padding:10px 18px;
 display:flex;gap:14px;align-items:center;font-size:13px;z-index:9;flex-wrap:wrap;}}
.barre button{{background:#2563EB;color:#fff;border:none;padding:9px 18px;
 border-radius:8px;cursor:pointer;font-weight:600;font-family:inherit;}}
.barre label{{display:flex;align-items:center;gap:6px;}}
.barre input{{width:62px;padding:5px;border-radius:6px;border:0;}}
"""


def _position(g, i, dx=0.0, dy=0.0):
    col = i % g["cols"]
    ligne = i // g["cols"]
    x = g["marge_h"] + col * g["pas_h"] + dx
    y = g["marge_v"] + ligne * g["pas_v"] + dy
    return x, y


# Le script de calage est gardé hors des f-strings : ses accolades
# entreraient en conflit avec celles du formatage Python.
_SCRIPT_CALAGE = """
<script>
function caler(){
  var dx = parseFloat(document.getElementById('dx').value) || 0;
  var dy = parseFloat(document.getElementById('dy').value) || 0;
  document.querySelectorAll('.case').forEach(function(c){
    c.style.left = (parseFloat(c.dataset.x) + dx) + 'mm';
    c.style.top  = (parseFloat(c.dataset.y) + dy) + 'mm';
  });
}
function contours(){
  var on = document.getElementById('ct').checked;
  document.querySelectorAll('.contour').forEach(function(c){
    c.classList.toggle('garder', on);
  });
}
</script>
"""


def _barre(titre, montrer_contours=True):
    case_contours = ('<label><input type="checkbox" id="ct" onchange="contours()">'
                     ' Imprimer les repères de découpe</label>'
                     if montrer_contours else "")
    return f"""<div class="barre noprint">
  <b>{_esc(titre)}</b>
  <span>Faites un essai sur papier ordinaire avant d'utiliser les planches.</span>
  <label>Décalage ↔ <input type="number" id="dx" value="0" step="0.5"> mm</label>
  <label>Décalage ↕ <input type="number" id="dy" value="0" step="0.5"> mm</label>
  <button onclick="caler()">Appliquer le décalage</button>
  {case_contours}
  <button onclick="window.print()">🖨️ Imprimer</button>
</div>""" + _SCRIPT_CALAGE


# --------------------------------------------------------------------------
#  Badges
# --------------------------------------------------------------------------
def html_badges(items, planche="L7160", decalage=(0.0, 0.0), depart=0):
    """items : [{prenom, emoji, titre, objectif, couleur}] — un par étiquette.

    `depart` permet de commencer à la case N : très utile pour réutiliser une
    planche déjà entamée.
    """
    g = PLANCHES.get(planche) or PLANCHES["L7160"]
    par_page = g["cols"] * g["lignes"]
    dx, dy = decalage
    petit = g["l"] < 50 or g["h"] < 30

    cases = [None] * max(0, depart) + list(items)
    pages = [cases[i:i + par_page] for i in range(0, len(cases), par_page)] or [[]]

    corps = ""
    for page in pages:
        corps += '<div class="feuille">'
        for i in range(par_page):
            b = page[i] if i < len(page) else None
            x, y = _position(g, i, dx, dy)
            if not b:
                corps += (f'<div class="case contour" data-x="{x - dx}" '
                          f'data-y="{y - dy}" style="left:{x}mm;top:{y}mm"></div>')
                continue
            coul = b.get("couleur") or "#2563EB"
            taille_emo = "9mm" if petit else "13mm"
            taille_titre = "3.1mm" if petit else "4.4mm"
            taille_nom = "2.9mm" if petit else "3.8mm"
            objectif = "" if petit else (
                f'<div style="font-size:2.9mm;color:#5B6478;line-height:1.25;'
                f'margin-top:0.8mm">{_esc(b.get("objectif", ""))}</div>')
            corps += f"""<div class="case contour" data-x="{x - dx}" data-y="{y - dy}"
              style="left:{x}mm;top:{y}mm;
                     border:0.5mm solid {coul};background:#fff;
                     flex-direction:column;text-align:center;padding:2mm 2.5mm;">
              <div style="font-size:{taille_emo};line-height:1">{b.get('emoji','🏅')}</div>
              <div style="font-size:{taille_titre};font-weight:800;color:{coul};
                          line-height:1.15;margin-top:0.8mm">{_esc(b.get('titre',''))}</div>
              {objectif}
              <div style="font-size:{taille_nom};font-weight:700;margin-top:auto;
                          color:#1E2233">{_esc(b.get('prenom',''))}</div>
            </div>"""
        corps += "</div>"

    return f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
<title>Badges à imprimer</title><style>{_css_grille(g, dx, dy)}</style></head>
<body>{_barre('Badges — ' + g['nom'])}{corps}</body></html>"""


# --------------------------------------------------------------------------
#  Leçons du classeur en cartes
# --------------------------------------------------------------------------
def html_lecons(fiches, css_classeur, planche="A7", decalage=(0.0, 0.0),
                recto_verso=False):
    """fiches : [{titre, html}] — une carte par leçon, au format demandé."""
    g = PLANCHES.get(planche) or PLANCHES["A7"]
    par_page = g["cols"] * g["lignes"]
    dx, dy = decalage
    # La carte d'origine fait 105 × 74,2 mm : on l'adapte au format visé.
    echelle = min(g["l"] / 105.0, g["h"] / 74.2)

    pages = [fiches[i:i + par_page] for i in range(0, len(fiches), par_page)] or [[]]
    corps = ""
    for page in pages:
        corps += '<div class="feuille">'
        for i in range(par_page):
            f = page[i] if i < len(page) else None
            x, y = _position(g, i, dx, dy)
            if not f:
                corps += (f'<div class="case contour" data-x="{x - dx}" '
                          f'data-y="{y - dy}" style="left:{x}mm;top:{y}mm"></div>')
                continue
            corps += f"""<div class="case contour" data-x="{x - dx}" data-y="{y - dy}"
              style="left:{x}mm;top:{y}mm;background:#fff;align-items:flex-start;">
              <div class="porte" style="transform:scale({echelle:.4f});
                   transform-origin:top left;width:105mm;height:74.2mm;">
                {f.get('html', '')}
              </div>
              <div class="trou"></div>
            </div>"""
        corps += "</div>"

    return f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
<title>Leçons à plastifier</title><style>
{css_classeur}
{_css_grille(g, dx, dy)}
.case .card{{border:0 !important;width:105mm !important;height:74.2mm !important;}}
.case .card .punch{{display:none;}}
.case .card::before{{display:none;}}
/* Emplacement de la perforation pour l'anneau du porte-clé */
.trou{{position:absolute;top:3mm;right:3mm;width:4mm;height:4mm;
  border:0.3mm dashed #94a3b8;border-radius:50%;}}
</style></head>
<body>{_barre('Leçons — ' + g['nom'])}{corps}</body></html>"""
