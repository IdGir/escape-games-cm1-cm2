# -*- coding: utf-8 -*-
"""Leçons imprimables — Le Secret de la Déclaration (declaration)."""
from graphiques import ouvrir, texte, taille, tableau, etapes

JEU = {
    "titre": "Le Secret de la Déclaration",
    "matiere": "Histoire",
    "theme": "Le temps de la Révolution : 1789, fin de la monarchie absolue et nouveaux principes",
    "couleur": "#1d3a8a", "accent": "#b22222",
    "couleur_pale": "#ecf0f9", "accent_pale": "#fbecec",
}
BLEU, ROUGE, OR, GRIS = "#1d3a8a", "#b22222", "#b8860b", "#8a8f98"


def trois_ordres():
    """Grille de 100 cases : 1 case = 1 % de la population."""
    W, H = 360, 250
    fs = taille(W, 66)
    s = [ouvrir(W, H, "Les trois ordres en 1789 : 100 cases = toute la population")]
    c, g, x0, y0 = 17, 2.5, 8, 8
    for k in range(100):
        i, j = k % 10, k // 10
        x, y = x0 + i * (c + g), y0 + j * (c + g)
        if k < 98:
            s.append(f'<rect x="{x}" y="{y}" width="{c}" height="{c}" rx="2" fill="{BLEU}" fill-opacity=".85"/>')
        elif k == 98:
            s.append(f'<rect x="{x}" y="{y}" width="{c}" height="{c}" rx="2" fill="{ROUGE}"/>')
        else:
            s.append(f'<rect x="{x}" y="{y}" width="{c/2}" height="{c}" fill="{ROUGE}"/>')
            s.append(f'<rect x="{x + c/2}" y="{y}" width="{c/2}" height="{c}" fill="{OR}"/>')
    lx = x0 + 10 * (c + g) + 10
    items = [(BLEU, "Tiers état", "≈ 98 %", "paysans, artisans,\nbourgeois : ils paient\nles impôts"),
             (ROUGE, "Noblesse", "≈ 1,5 %", "privilèges,\npas d'impôts directs"),
             (OR, "Clergé", "≈ 0,5 %", "privilèges,\nperçoit la dîme")]
    y = 18
    for col, nom, pct, det in items:
        s.append(f'<rect x="{lx}" y="{y - fs * 0.8:.1f}" width="{fs * 0.9:.1f}" height="{fs * 0.9:.1f}" fill="{col}"/>')
        s.append(texte(lx + fs * 1.3, y, f"{nom} {pct}", fs * 0.95, "start", col, 800))
        s.append(texte(lx + fs * 1.3, y + fs * 1.15, det, fs * 0.75, "start", "#1f2328"))
        y += fs * 5.2
    s.append(texte(x0, H - 6, "1 case = 1 % des habitants du royaume (environ 28 millions).", fs * 0.72, "start", "#5b6470", italique=True))
    s.append("</svg>")
    return "".join(s)


def vote_ordre_tete():
    W, H = 360, 200
    fs = taille(W, 66)
    s = [ouvrir(W, H, "Vote par ordre ou vote par tête")]
    s.append(texte(90, fs * 1.3, "VOTE PAR ORDRE", fs, fill=BLEU, poids=800))
    s.append(texte(270, fs * 1.3, "VOTE PAR TÊTE", fs, fill=ROUGE, poids=800))
    s.append(f'<line x1="180" y1="6" x2="180" y2="{H-6}" stroke="#c9ced4" stroke-dasharray="3 3"/>')
    # par ordre : 3 urnes = 3 voix
    for i, (nom, col) in enumerate([("clergé", OR), ("noblesse", ROUGE), ("tiers état", BLEU)]):
        x = 18 + i * 54
        s.append(f'<rect x="{x}" y="50" width="42" height="42" rx="5" fill="{col}"/>')
        s.append(texte(x + 21, 78, "1", fs * 1.4, fill="#fff", poids=800))
        s.append(texte(x + 21, 108, nom, fs * 0.75))
    s.append(texte(90, 140, "3 voix : le clergé et la\nnoblesse l'emportent 2 contre 1", fs * 0.8, fill="#1f2328"))
    # par tête : barres proportionnelles
    for i, (nom, n, col) in enumerate([("clergé", 300, OR), ("noblesse", 300, ROUGE), ("tiers état", 600, BLEU)]):
        y = 48 + i * 30
        w = n / 600 * 110
        s.append(texte(236, y + 14, nom, fs * 0.75, "end"))
        s.append(f'<rect x="240" y="{y}" width="{w:.1f}" height="20" rx="3" fill="{col}"/>')
        s.append(texte(244 + w, y + 14, f"≈ {n}", fs * 0.72, "start", "#1f2328", 700) if n < 600 else texte(240 + w / 2, y + 14, "≈ 600", fs * 0.72, fill="#fff", poids=700))
    s.append(texte(270, 162, "une voix par député : le tiers\nétat a autant de voix que les\ndeux autres ordres réunis", fs * 0.8))
    s.append("</svg>")
    return "".join(s)


def lignes_de_vie():
    W, H = 360, 190
    fs = taille(W, 66)
    a0, a1 = 1745, 1800
    g, d = 122, 10
    X = lambda a: g + (a - a0) / (a1 - a0) * (W - g - d)
    s = [ouvrir(W, H, "Les dates de vie des grands personnages")]
    s.append(f'<rect x="{X(1789):.1f}" y="4" width="{X(1794) - X(1789):.1f}" height="{H - 30}" fill="{ROUGE}" fill-opacity=".10"/>')
    s.append(texte((X(1789) + X(1794)) / 2, 16, "Révolution", fs * 0.7, fill=ROUGE, poids=700))
    pers = [("Olympe de Gouges", 1748, 1793), ("Mirabeau", 1749, 1791), ("Louis XVI", 1754, 1793),
            ("Robespierre", 1758, 1794), ("Danton", 1759, 1794)]
    for i, (n, b, m) in enumerate(pers):
        y = 26 + i * 26
        s.append(texte(g - 6, y + 12, n, fs * 0.8, "end", "#1f2328", 700))
        s.append(f'<rect x="{X(b):.1f}" y="{y}" width="{X(m) - X(b):.1f}" height="16" rx="3" fill="{BLEU}" fill-opacity=".8"/>')
        s.append(texte(X(b) + 3, y + 12, str(b), fs * 0.66, "start", "#fff", 700))
        s.append(texte(X(m) - 3, y + 12, str(m), fs * 0.66, "end", "#fff", 700))
    for a in range(1750, 1801, 10):
        s.append(f'<line x1="{X(a):.1f}" y1="{H - 26}" x2="{X(a):.1f}" y2="{H - 22}" stroke="#5b6470"/>')
        s.append(texte(X(a), H - 10, a, fs * 0.72, fill="#5b6470"))
    s.append(f'<line x1="{g}" y1="{H - 26}" x2="{W - d}" y2="{H - 26}" stroke="#5b6470"/>')
    s.append("</svg>")
    return "".join(s)


def devise():
    W, H = 360, 170
    fs = taille(W, 66)
    s = [ouvrir(W, H, "Liberté, Égalité, Fraternité")]
    cols = [("LIBERTÉ", "faire tout ce qui\nne nuit pas à autrui\n(DDHC, art. 4)", BLEU),
            ("ÉGALITÉ", "les mêmes droits\net la même loi\npour tous", "#f3f4f6"),
            ("FRATERNITÉ", "solidarité et\nentraide entre\ncitoyens", ROUGE)]
    w = (W - 8) / 3
    for i, (t, dt, c) in enumerate(cols):
        x = 4 + i * w
        clair = c == "#f3f4f6"
        s.append(f'<rect x="{x:.1f}" y="4" width="{w:.1f}" height="{H - 8}" fill="{c}" stroke="#c9ced4"/>')
        s.append(texte(x + w / 2, 4 + fs * 2, t, fs * 1.05, fill="#1f2328" if clair else "#fff", poids=800))
        s.append(texte(x + w / 2, 4 + fs * 4, dt, fs * 0.8, fill="#1f2328" if clair else "#fff"))
    s.append("</svg>")
    return "".join(s)


PARIS = [("Palais-Royal", [2.3371, 48.8637], "n"), ("Tuileries", [2.3275, 48.8625], "w"),
         ("Hôtel de Ville", [2.3522, 48.8566], "s"), ("Bastille", [2.3692, 48.8532], "e"),
         ("Invalides", [2.3125, 48.8566], "s"), ("Faubourg\nSaint-Antoine", [2.3830, 48.8505], "s")]

LECONS = {
    "causes": {
        "competence": "Décrire le contexte social, économique et intellectuel du royaume en France en 1789.",
        "visuels": [{"type": "svg", "etiquette": "Graphique", "titre": "Les trois ordres en 1789", "svg": trois_ordres(),
                     "legende": "Estimations des historiens : le tiers état forme presque toute la population."}],
    },
    "etats-generaux": {
        "competence": "Fin de la monarchie absolue et de l'Ancien Régime : les États généraux, le serment du Jeu de paume.",
        "masquer": ["document"],
        "visuels": [
            {"type": "svg", "titre": "Pourquoi le tiers état proteste", "svg": vote_ordre_tete(),
             "legende": "Le tiers état a obtenu deux fois plus de députés, mais le roi maintient le vote par ordre."},
            {"type": "photo", "etiquette": "Document", "src": "assets/images/documents/etats-generaux.jpg",
             "titre": "Le Serment du Jeu de paume (J.-L. David)", "facultatif": False},
        ],
    },
    "bastille": {
        "competence": "Fin de la monarchie absolue et de l'Ancien Régime : la prise de la Bastille.",
        "masquer": ["document"],
        "visuels": [{"type": "photo", "etiquette": "Document", "src": "assets/images/documents/bastille.jpg",
                     "titre": "La prise de la Bastille, 14 juillet 1789", "facultatif": False},
                    {"type": "photo", "src": "assets/images/decors/salle4.jpg", "titre": "La Bastille prise d'assaut (J.-P. Houel, 1789)"}],
    },
    "declaration": {
        "competence": "Affirmation des nouveaux principes d'organisation de la société : la Déclaration des droits de l'homme et du citoyen.",
        "masquer": ["document"],
        "visuels": [{"type": "photo", "etiquette": "Document", "src": "assets/images/documents/declaration.jpg",
                     "titre": "La Déclaration des droits de l'homme et du citoyen", "facultatif": False,
                     "legende": "Tableau de Jean-Jacques Le Barbier, vers 1789."}],
    },
    "personnages": {
        "competence": "Contexte de 1789 : les acteurs de la Révolution.",
        "visuels": [{"type": "svg", "etiquette": "Graphique", "titre": "Des vies pendant la Révolution", "svg": lignes_de_vie(),
                     "legende": "Chaque barre va de la naissance à la mort. Plusieurs meurent pendant la Révolution."}],
    },
    "devise": {
        "competence": "Affirmation des nouveaux principes d'organisation de la société : la devise républicaine.",
        "visuels": [{"type": "svg", "titre": "La devise de la République", "svg": devise()},
                    {"type": "photo", "src": "assets/images/decors/salle1.jpg", "titre": "Le Palais-Royal, à Paris"}],
    },
    "femmes": {
        "competence": "Affirmation des nouveaux principes d'organisation de la société, et leurs limites : la place des femmes.",
        "visuels": [{"type": "svg", "titre": "Qui peut voter ?",
                     "svg": etapes([("1791", "hommes payant\nun impôt", GRIS), ("1848", "tous les hommes\n(21 ans)", BLEU),
                                    ("1944", "les femmes\naussi", ROUGE)], sens="h", numeros=False),
                     "legende": "Le droit de vote des femmes est accordé en 1944 ; elles votent pour la première fois en 1945."}],
    },
    "paris": {
        "competence": "Situer les lieux de la Révolution à Paris et à Versailles.",
        "masquer": ["document"],
        "visuels": [
            {"type": "carte", "titre": "Les lieux de 1789 dans Paris",
             "legende": "Paris vers 1789 : les lieux de l'escape game, au bord de la Seine.",
             "spec": {"titre": "Les lieux de 1789 dans Paris", "largeur": 360, "cible_mm": 66, "resolution": "10m",
                      "etendue": [[2.285, 48.835], [2.405, 48.880]], "frontieres": False, "epaisseur_fleuve": 5,
                      "couleurs": {"terre": "#f3efe6", "mer": "#f3efe6"}, "fleuves": ["Seine"],
                      "points": [{"lonlat": ll, "nom": n, "pos": p, "couleur": ROUGE} for n, ll, p in PARIS],
                      "textes": [{"lonlat": [2.338, 48.8505], "texte": "la Seine", "style": "mer"}],
                      "echelle_km": 1}},
            {"type": "carte", "titre": "De Versailles à Paris",
             "legende": "5-6 octobre 1789 : les Parisiennes marchent sur Versailles et ramènent la famille royale aux Tuileries.",
             "spec": {"titre": "De Versailles à Paris", "largeur": 360, "cible_mm": 66, "resolution": "10m",
                      "etendue": [[2.05, 48.76], [2.45, 48.92]], "frontieres": False, "epaisseur_fleuve": 3,
                      "couleurs": {"terre": "#f3efe6", "mer": "#f3efe6"}, "fleuves": ["Seine"],
                      "lignes": [{"coords": [[2.3522, 48.8566], [2.2300, 48.8330], [2.1204, 48.8049]], "couleur": ROUGE, "fleches": True, "pointille": True}],
                      "points": [{"lonlat": [2.3522, 48.8566], "nom": "Paris", "style": "capitale", "pos": "e"},
                                 {"lonlat": [2.1204, 48.8049], "nom": "Versailles", "style": "etoile", "couleur": ROUGE, "pos": "s"}],
                      "echelle_km": 5}},
            {"type": "photo", "src": "assets/images/decors/salle3.jpg", "titre": "Le jardin des Tuileries"},
        ],
    },
}
