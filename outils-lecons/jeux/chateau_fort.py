# -*- coding: utf-8 -*-
"""Leçons imprimables — Le Secret du donjon (chateau-fort)."""
from graphiques import ouvrir, texte, calendrier, taille

JEU = {
    "titre": "Le Secret du donjon",
    "matiere": "Histoire",
    "theme": "Le Moyen Âge : le château fort et la vie des paysannes et des paysans",
    "couleur": "#7d2e22", "accent": "#b8860b",
    "couleur_pale": "#f7ece8", "accent_pale": "#fbf4dd",
}

C1, C2, BLEU, VERT = "#7d2e22", "#b8860b", "#3b6e9a", "#4f7d3a"


def plan_chateau():
    W, H = 360, 300
    fs = taille(W, 66)
    s = [ouvrir(W, H, "Plan d'un château fort vu de dessus")]
    s.append(f'<rect width="{W}" height="{H}" fill="#eef1e4"/>')
    cx, cy = 170, 150
    # douves
    s.append(f'<rect x="{cx-128}" y="{cy-112}" width="256" height="224" rx="40" fill="#9cc3de"/>')
    s.append(f'<rect x="{cx-110}" y="{cy-94}" width="220" height="188" rx="28" fill="#e7dfc9"/>')
    # enceinte (courtine) + chemin de ronde
    s.append(f'<rect x="{cx-100}" y="{cy-84}" width="200" height="168" fill="none" stroke="#6d6252" stroke-width="10"/>')
    s.append(f'<rect x="{cx-100}" y="{cy-84}" width="200" height="168" fill="none" stroke="#c9bfa6" stroke-width="2" stroke-dasharray="4 3"/>')
    # tours
    for tx, ty in [(cx-100, cy-84), (cx+100, cy-84), (cx-100, cy+84), (cx+100, cy+84), (cx+100, cy)]:
        s.append(f'<circle cx="{tx}" cy="{ty}" r="15" fill="#8a7d68" stroke="#4f463a" stroke-width="1.5"/>')
    # porte + pont-levis
    s.append(f'<rect x="{cx-18}" y="{cy+74}" width="36" height="22" fill="#8a7d68" stroke="#4f463a" stroke-width="1.5"/>')
    s.append(f'<rect x="{cx-9}" y="{cy+96}" width="18" height="30" fill="#a0703c" stroke="#5b3b1a" stroke-width="1"/>')
    s.append(f'<line x1="{cx-9}" y1="{cy+86}" x2="{cx+9}" y2="{cy+86}" stroke="#222" stroke-width="2.5" stroke-dasharray="2 1.5"/>')
    # donjon
    s.append(f'<rect x="{cx-72}" y="{cy-62}" width="58" height="58" fill="#6d6252" stroke="#3b342b" stroke-width="2"/>')
    s.append(f'<rect x="{cx-64}" y="{cy-54}" width="42" height="42" fill="#8a7d68"/>')
    # basse-cour : bâtiments
    s.append(f'<rect x="{cx+10}" y="{cy-66}" width="70" height="22" fill="#c8a877" stroke="#7a5d33"/>')
    s.append(f'<rect x="{cx+30}" y="{cy+20}" width="50" height="34" fill="#c8a877" stroke="#7a5d33"/>')
    s.append(f'<circle cx="{cx-30}" cy="{cy+40}" r="7" fill="#7aa6c7" stroke="#3b6e9a"/>')
    lab = lambda x, y, t, a="start": texte(x, y, t, fs * 0.85, a, "#1f2328", 700, extra='paint-order="stroke" stroke="#fff" stroke-width="2.6"')
    s.append(lab(cx-43, cy-30, "DONJON", "middle"))
    s.append(lab(cx+5, cy-5, "basse-cour", "start"))
    s.append(lab(cx-30, cy+62, "puits", "middle"))
    s.append(lab(cx+45, cy-72, "logis, chapelle", "middle"))
    s.append(lab(cx+55, cy+68, "écuries", "middle"))
    # étiquettes extérieures avec traits
    def fleche(x1, y1, x2, y2, t, a):
        s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#333" stroke-width="0.9"/>')
        s.append(lab(x2 + (4 if a == "start" else -4), y2 + fs * 0.3, t, a))
    fleche(cx+128, cy+40, cx+140, cy+118, "douves", "start")
    fleche(cx+9, cy+112, cx+48, cy+136, "pont-levis", "start")
    fleche(cx-5, cy+86, cx-60, cy+136, "herse", "end")
    fleche(cx+115, cy-84, cx+140, cy-118, "tour", "start")
    fleche(cx-100, cy+30, cx-122, cy+104, "enceinte", "end")
    fleche(cx-100, cy-40, cx-128, cy-124, "chemin de ronde", "start")
    s.append("</svg>")
    return "".join(s)


def trois_fonctions():
    W, H = 360, 200
    fs = taille(W, 66)
    s = [ouvrir(W, H, "Les trois fonctions du château fort")]
    cols = [("PROTÉGER", "lieu de\nprotection", "murs, tours,\ndouves, refuge\npour les paysans", BLEU),
            ("HABITER", "lieu de vie\ndu seigneur", "le seigneur, la dame,\nla maisonnée ;\nla grande salle", VERT),
            ("MONTRER", "symbole de\nsa puissance", "hauteur, blason,\nfêtes, chasses,\njustice", C1)]
    w = (W - 16) / 3
    for i, (t, st, ex, c) in enumerate(cols):
        x = 4 + i * (w + 4)
        s.append(f'<rect x="{x:.1f}" y="4" width="{w:.1f}" height="{H-8}" rx="7" fill="#fff" stroke="{c}" stroke-width="1.6"/>')
        s.append(f'<rect x="{x:.1f}" y="4" width="{w:.1f}" height="{fs*2.2:.1f}" rx="7" fill="{c}"/>')
        s.append(texte(x + w / 2, 4 + fs * 1.5, t, fs * 1.05, fill="#fff", poids=800))
        s.append(texte(x + w / 2, 4 + fs * 3.6, st, fs * 0.85, fill=c, poids=700, italique=True))
        s.append(texte(x + w / 2, 4 + fs * 6.6, ex, fs * 0.82, fill="#1f2328"))
    s.append("</svg>")
    return "".join(s)


def echange_inegal():
    W, H = 360, 250
    fs = taille(W, 66)
    s = [ouvrir(W, H, "Ce que se doivent le seigneur et les paysans")]
    s.append('<defs><marker id="ar" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#444"/></marker></defs>')
    box = lambda x, y, w, h, c, t: (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{c}"/>' + texte(x + w / 2, y + h / 2 + fs * 0.38, t, fs * 1.05, fill="#fff", poids=800))
    s.append(box(110, 6, 140, 34, C1, "LE SEIGNEUR"))
    s.append(box(110, 206, 140, 34, VERT, "LES PAYSANS"))
    s.append(box(274, 206, 82, 34, "#6b5b95", "L'ÉGLISE"))
    # paysans -> seigneur (gauche, montant)
    s.append(f'<line x1="140" y1="204" x2="140" y2="44" stroke="#444" stroke-width="1.6" marker-end="url(#ar)"/>')
    s.append(texte(132, 80, "corvée\ncens\nchampart\nbanalités\n(moulin, four,\npressoir)", fs * 0.85, "end", "#1f2328", 600))
    # seigneur -> paysans (droite, descendant)
    s.append(f'<line x1="220" y1="44" x2="220" y2="204" stroke="#444" stroke-width="1.6" marker-end="url(#ar)"/>')
    s.append(texte(228, 110, "protection\njustice", fs * 0.9, "start", "#1f2328", 600))
    s.append(f'<line x1="252" y1="223" x2="272" y2="223" stroke="#444" stroke-width="1.6" marker-end="url(#ar)"/>')
    s.append(texte(315, 196, "dîme", fs * 0.85, "middle", "#6b5b95", 700))
    s.append("</svg>")
    return "".join(s)


HIVER, PRINTEMPS, ETE, AUTOMNE = "#c9d9e8", "#cfe6c2", "#f6dd9a", "#eec39c"
CALENDRIER = calendrier([
    ("Janv.", "bois,\noutils", HIVER), ("Févr.", "veillées,\nbois", HIVER), ("Mars", "labour,\nvigne", PRINTEMPS),
    ("Avril", "jardin", PRINTEMPS), ("Mai", "troupeaux", PRINTEMPS), ("Juin", "fenaison", ETE),
    ("Juil.", "moisson,\ntonte", ETE), ("Août", "battage", ETE), ("Sept.", "vendanges", AUTOMNE),
    ("Oct.", "semailles", AUTOMNE), ("Nov.", "glandée", AUTOMNE), ("Déc.", "tuer le\ncochon", HIVER),
], label="Le calendrier des travaux des champs")

LECONS = {
    "construire-un-chateau": {
        "competence": "Décrire les fonctions d'un château fort : lieu de protection (sa construction).",
        "visuels": [
            {"type": "schema"},
            {"type": "carte", "titre": "Quelques châteaux forts en France",
             "legende": "Guédelon (Yonne) : un château fort construit aujourd'hui avec les techniques du XIIIe siècle.",
             "spec": {"titre": "Quelques châteaux forts en France", "largeur": 360, "cible_mm": 66,
                      "etendue": [[-5.2, 41.3], [9.7, 51.2]], "pays_mis_en_avant": ["France"],
                      "fleuves": ["Seine", "Loire", "Rhône", "Rhne", "Garonne", "Rhin", "Rhein"],
                      "points": [
                          {"lonlat": [3.158, 47.584], "nom": "Guédelon", "style": "etoile", "couleur": C1, "pos": "w"},
                          {"lonlat": [1.403, 49.239], "nom": "Château-Gaillard", "pos": "w"},
                          {"lonlat": [2.364, 43.206], "nom": "Carcassonne", "pos": "e"},
                          {"lonlat": [3.320, 49.520], "nom": "Coucy", "pos": "e"},
                          {"lonlat": [4.639, 47.218], "nom": "Châteauneuf", "pos": "e"},
                          {"lonlat": [2.35, 48.857], "nom": "Paris", "style": "capitale", "pos": "s"}],
                      "textes": [{"lonlat": [-3.3, 45.6], "texte": "OCÉAN\nATLANTIQUE", "style": "mer"}],
                      "echelle_km": 200}},
            {"type": "photo", "src": "assets/images/cartes/e1-2.jpg", "titre": "Le chantier de Guédelon"},
        ],
    },
    "les-defenses": {
        "competence": "Décrire les fonctions d'un château fort : lieu de protection.",
        "visuels": [
            {"type": "svg", "titre": "Plan d'un château fort (vue de dessus)", "svg": plan_chateau(),
             "legende": "Schéma simplifié : chaque château a son propre plan."},
            {"type": "schema"},
        ],
    },
    "vie-du-seigneur": {
        "competence": "Décrire les fonctions d'un château fort : lieu de vie du seigneur, symbole de sa puissance.",
        "visuels": [
            {"type": "svg", "titre": "Les trois fonctions du château fort", "svg": trois_fonctions()},
            {"type": "photo", "src": "assets/images/decors/salle3.jpg", "titre": "La grande salle de Guédelon",
             "legende": "La grande salle : on y mange, on y reçoit, on y rend la justice."},
        ],
    },
    "vie-des-paysans": {
        "competence": "Raconter la vie quotidienne des paysannes et des paysans.",
        "visuels": [
            {"type": "svg", "etiquette": "Graphique", "titre": "L'année des paysans", "svg": CALENDRIER,
             "legende": "D'après les calendriers des livres d'heures (Très Riches Heures du duc de Berry). "
                        "Les travaux varient selon les régions."},
        ],
    },
    "seigneur-et-paysans": {
        "competence": "Raconter la vie quotidienne des paysannes et des paysans (les relations avec le seigneur).",
        "visuels": [
            {"type": "svg", "titre": "Un échange inégal", "svg": echange_inegal(),
             "legende": "Les paysans doivent des redevances et des services ; le seigneur protège et rend la justice."},
            {"type": "schema"},
            {"type": "photo", "src": "assets/images/cartes/e5-2.jpg", "titre": "Un moulin à eau",
             "legende": "Photo d'illustration : le moulin du seigneur est « banal », on paie pour l'utiliser."},
        ],
    },
}
