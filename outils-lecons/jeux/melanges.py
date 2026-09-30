# -*- coding: utf-8 -*-
"""Leçons imprimables — Le Laboratoire de Madame Mélange (melanges)."""
from graphiques import ouvrir, texte, taille, tableau

JEU = {
    "titre": "Le Laboratoire de Madame Mélange",
    "matiere": "Sciences et technologie",
    "theme": "La matière : masses, mélanges et séparation des constituants",
    "couleur": "#154650", "accent": "#a8456f",
    "couleur_pale": "#e8f1f2", "accent_pale": "#f8ecf2",
}
C1, C2, BLEU, SABLE, SEL = "#1f5f6b", "#a8456f", "#5b9bd5", "#d8b36a", "#9aa4ad"


def conservation():
    """Barres empilées : eau + sel avant, mélange après (valeurs de la leçon)."""
    W, H = 360, 230
    fs = taille(W, 66)
    s = [ouvrir(W, H, "La masse se conserve : 250 g + 20 g = 270 g")]
    base, ech = 190, 0.55
    def barre(x, parts, titre):
        y = base
        for val, c, lab in parts:
            h = val * ech
            s.append(f'<rect x="{x}" y="{y-h:.1f}" width="70" height="{h:.1f}" fill="{c}" stroke="#fff"/>')
            s.append(texte(x + 35, y - h / 2 + fs * 0.35, lab, fs * 0.85, fill="#fff" if val > 60 else "#1f2328", poids=700))
            y -= h
        s.append(texte(x + 35, y - 6, f"{sum(p[0] for p in parts)} g", fs, poids=800, fill=C1))
        s.append(texte(x + 35, base + fs * 1.3, titre, fs * 0.9, poids=700))
    barre(40, [(250, BLEU, "eau 250 g"), (20, "#7f8c8d", "sel 20 g")], "AVANT")
    barre(240, [(270, "#6fa8dc", "eau salée")], "APRÈS")
    s.append(f'<line x1="20" y1="{base}" x2="{W-20}" y2="{base}" stroke="#5b6470"/>')
    s.append('<defs><marker id="ar" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#444"/></marker></defs>')
    s.append(f'<line x1="130" y1="120" x2="228" y2="120" stroke="#444" stroke-width="1.6" marker-end="url(#ar)"/>')
    s.append(texte(179, 112, "on dissout", fs * 0.85, italique=True))
    s.append(texte(179, base + fs * 2.8, "La masse totale ne change pas.", fs * 0.9, fill=C2, poids=700))
    s.append("</svg>")
    return "".join(s)


LECONS = {
    "masses": {
        "competence": "Comparer et mesurer des masses de différents objets ou liquides de diverses manières.",
        "visuels": [
            {"type": "schema", "titre": "Deux balances"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Les unités de masse",
             "svg": tableau(["t", "kg", "hg", "dag", "g", "dg", "cg", "mg"], [
                 ["tonne", "kilo-\ngramme", "", "", "gramme", "", "", "milli-\ngramme"],
             ], couleur=C1),
             "legende": "1 kg = 1 000 g ; 1 g = 1 000 mg ; 1 t = 1 000 kg."},
            {"type": "svg", "etiquette": "Tableau", "titre": "Peser un liquide avec la tare",
             "svg": tableau(["Étape", "Affichage"], [
                 ["1. Je pose le récipient vide", "150 g"],
                 ["2. J'appuie sur « tare »", "0 g"],
                 ["3. Je verse le liquide", "masse du liquide"],
             ], couleur=C1, largeurs=[1.6, 1]),
             "legende": "Sans tare : masse du liquide = masse totale − masse du récipient."},
        ],
    },
    "conservation": {
        "competence": "Distinguer mélanges homogènes et hétérogènes (la dissolution).",
        "visuels": [
            {"type": "svg", "etiquette": "Graphique", "titre": "Avant et après la dissolution", "svg": conservation(),
             "legende": "Le sel dissous ne se voit plus, mais il est toujours là : la balance le prouve."},
            {"type": "schema", "titre": "La conservation de la masse"},
        ],
    },
    "melanges": {
        "competence": "Distinguer mélanges homogènes et hétérogènes (l'observation).",
        "visuels": [
            {"type": "schema", "titre": "Homogène ou hétérogène ?"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Exemples de mélanges",
             "svg": tableau(["Homogène\n(un seul aspect)", "Hétérogène\n(plusieurs aspects)"], [
                 ["eau salée", "eau et huile"],
                 ["sirop à l'eau", "vinaigrette"],
                 ["eau du robinet", "eau boueuse"],
                 ["air", "riz et semoule"],
             ], couleur=C1),
             "legende": "On observe à l'œil nu : distingue-t-on au moins deux constituants ?"},
        ],
    },
    "separer-solides": {
        "competence": "Séparer les constituants de mélanges solides (le tri, l'aimantation).",
        "visuels": [
            {"type": "schema", "titre": "Trois méthodes de séparation"},
            {"type": "svg", "etiquette": "Tableau", "titre": "Une différence, une méthode",
             "svg": tableau(["Différence", "Méthode", "Exemple"], [
                 ["la taille", "tamisage", "sable et cailloux"],
                 ["le fer", "aimantation", "sable et limaille"],
                 ["flotte ou coule", "flottation", "sciure et sable"],
                 ["l'aspect", "tri à la main", "perles de couleur"],
             ], couleur=C1, largeurs=[1, 1, 1.15])},
        ],
    },
    "separer-liquide": {
        "competence": "Séparer les constituants de mélanges solides et solide-liquide (filtration, décantation, évaporation).",
        "visuels": [
            {"type": "schema", "titre": "Le montage de filtration"},
            {"type": "carte", "titre": "Où récolte-t-on le sel en France ?",
             "legende": "Sel de mer : l'eau s'évapore au soleil dans les marais salants. Salines de l'Est : on faisait chauffer une eau salée venue du sous-sol.",
             "spec": {"titre": "Le sel en France", "largeur": 360, "cible_mm": 66,
                      "etendue": [[-5.2, 41.3], [9.7, 51.2]], "pays_mis_en_avant": ["France"],
                      "points": [{"lonlat": [-2.43, 47.33], "nom": "Guérande", "couleur": BLEU, "pos": "n"},
                                 {"lonlat": [-1.43, 46.20], "nom": "Île de Ré", "couleur": BLEU, "pos": "w"},
                                 {"lonlat": [4.19, 43.57], "nom": "Aigues-Mortes", "couleur": BLEU, "pos": "w"},
                                 {"lonlat": [4.73, 43.41], "nom": "Salin-de-Giraud", "couleur": BLEU, "pos": "e"},
                                 {"lonlat": [5.879, 46.946], "nom": "Salins-les-Bains", "couleur": C2, "style": "capitale", "pos": "s"},
                                 {"lonlat": [5.776, 47.031], "nom": "Arc-et-Senans", "couleur": C2, "style": "capitale", "pos": "n"}],
                      "legende": [{"type": "point", "couleur": BLEU, "texte": "Marais salant (sel de mer)"},
                                  {"type": "zone", "couleur": C2, "texte": "Saline (eau salée du sous-sol)", "opacite": 1}],
                      "position_legende": "bas-droite"}},
            {"type": "photo", "src": "assets/images/cartes/e5-1.jpg", "titre": "Les marais salants de Guérande"},
        ],
    },
}
