# -*- coding: utf-8 -*-
"""Leçons imprimables — Mission géographique (mission-geo), 16 séances.

Les leçons sont déclarées en JavaScript (js/donnees/lecons.js) : la page
d'impression charge ces scripts (SCRIPTS) et les convertit elle-même.
"""
from graphiques import ouvrir, texte, taille, tableau, etapes, barres

SCRIPTS = ["js/donnees/lecons.js"] + [f"js/donnees/sessions-p{i}.js" for i in range(1, 6)]

JEU = {
    "titre": "Mission géographique",
    "matiere": "Géographie",
    "theme": "Année B : territoire français, inégalités, se nourrir, eau douce",
    "unite": "Séance",
    "couleur": "#1b4d3e", "accent": "#d17a22",
    "couleur_pale": "#e9f2ee", "accent_pale": "#fcf1e6",
}
C1, C2, BLEU, ROUGE, VERT, GRIS = "#1b4d3e", "#d17a22", "#2f6690", "#b3261e", "#2e7d32", "#5b6470"
FRANCE = [[-5.2, 41.3], [9.7, 51.2]]
MERS = [{"lonlat": [-4.2, 45.4], "texte": "OCÉAN\nATLANTIQUE", "style": "mer"},
        {"lonlat": [5.4, 42.5], "texte": "MER MÉDITERRANÉE", "style": "mer"},
        {"lonlat": [-1.2, 50.1], "texte": "MANCHE", "style": "mer"},
        {"lonlat": [2.6, 51.0], "texte": "MER DU NORD", "style": "mer", "taille": 0.7}]
MASSIFS = {"fichier": "ne_10m_geography_regions_polys.geojson",
           "filtre": {"prop": "NAME", "valeurs": ["Vosges", "Jura", "ALPS", "PYRENEES", "Massif Central"]},
           "remplissage": "#c9a06a", "opacite": 0.75, "contour": "#a97f4a", "epaisseur": 0.5, "seuil": 0.4,
           "libelles": {"prop": "NAME", "taille": 0.85, "couleur": "#6b4a1f", "poids": 700,
                        "renommer": {"ALPS": "ALPES", "PYRENEES": "PYRÉNÉES", "Massif Central": "MASSIF\nCENTRAL",
                                     "Vosges": "VOSGES", "Jura": "JURA"},
                        "positions": {"ALPS": [6.9, 45.2], "PYRENEES": [0.6, 42.75], "Massif Central": [2.9, 45.3],
                                      "Vosges": [7.05, 48.1], "Jura": [5.9, 46.7]}}}
REGIONS_NOMS = {"Bourgogne-Franche-Comté": "Bourgogne-\nFranche-Comté", "Auvergne-Rhône-Alpes": "Auvergne-\nRhône-Alpes",
                "Provence-Alpes-Côte d'Azur": "PACA", "Nouvelle-Aquitaine": "Nouvelle-\nAquitaine",
                "Centre-Val de Loire": "Centre-\nVal de Loire", "Pays de la Loire": "Pays de\nla Loire",
                "Île-de-France": "Île-de-\nFrance", "Hauts-de-France": "Hauts-de-\nFrance"}


def spec_france(**k):
    base = {"largeur": 360, "cible_mm": 66, "etendue": FRANCE, "resolution": "50m"}
    base.update(k)
    return base


def emboitement():
    W, H = 360, 220
    fs = taille(W, 66)
    s = [ouvrir(W, H, "Des territoires emboîtés")]
    niv = [("CONTINENT", "l'Europe", "#dbe9e3"), ("PAYS", "la France", "#bcd8cb"), ("RÉGION", "Bourgogne-Franche-Comté", "#93c1ab"),
           ("DÉPARTEMENT", "la Côte-d'Or (21)", "#5f9f83"), ("COMMUNE", "Dijon", C1)]
    for i, (t, ex, c) in enumerate(niv):
        m = i * 18
        s.append(f'<rect x="{4 + m}" y="{4 + m * 0.95:.1f}" width="{W - 8 - 2 * m}" height="{H - 8 - 1.9 * m:.1f}" rx="8" fill="{c}" stroke="#fff" stroke-width="1.5"/>')
        fill = "#fff" if i >= 3 else "#1f2328"
        s.append(texte(12 + m, 4 + m * 0.95 + fs * 1.15, f"{t} : {ex}", fs * 0.8, "start", fill, 700))
    s.append("</svg>")
    return "".join(s)


def profil_cours_eau():
    W, H = 360, 190
    fs = taille(W, 66)
    s = [ouvrir(W, H, "De la source à la mer")]
    s.append(f'<rect width="{W}" height="{H}" fill="#f4f7f2"/>')
    s.append('<path d="M0,40 L40,30 L90,70 L150,110 L230,138 L300,150 L360,152 L360,190 L0,190 Z" fill="#d9c9a3"/>')
    s.append(f'<path d="M300,150 L360,150 L360,190 L300,190 Z" fill="#9cc3de"/>')
    s.append(f'<path d="M40,34 Q70,50 90,68 T150,108 T230,136 T300,148" fill="none" stroke="{BLEU}" stroke-width="2"/>')
    s.append(f'<path d="M150,108 T230,136 T300,148" fill="none" stroke="{BLEU}" stroke-width="5"/>')
    lab = [(40, 22, "source"), (72, 48, "torrent"), (118, 82, "ruisseau"), (175, 112, "rivière"), (250, 132, "fleuve"),
           (305, 140, "estuaire"), (335, 172, "mer")]
    for x, y, t in lab:
        s.append(texte(x, y, t, fs * 0.85, fill="#1f2328", poids=700, extra='paint-order="stroke" stroke="#fff" stroke-width="2.4"'))
    s.append('<defs><marker id="ar" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#444"/></marker></defs>')
    s.append(f'<line x1="20" y1="{H-14}" x2="{W-70}" y2="{H-14}" stroke="#444" stroke-width="1.4" marker-end="url(#ar)"/>')
    s.append(texte(20, H - 20, "AMONT", fs * 0.8, "start", C1, 800))
    s.append(texte(W - 74, H - 20, "AVAL", fs * 0.8, "end", C1, 800))
    s.append("</svg>")
    return "".join(s)


def conflit_usages():
    import math
    W, H = 360, 230
    fs = taille(W, 66)
    s = [ouvrir(W, H, "Qui a besoin de l'eau ?")]
    cx, cy = 180, 118
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{fs*3.2:.1f}" fill="{BLEU}"/>')
    s.append(texte(cx, cy + fs * 0.1, "L'EAU", fs * 1.05, fill="#fff", poids=800))
    s.append(texte(cx, cy + fs * 1.3, "en sécheresse", fs * 0.7, fill="#fff"))
    us = [("habitants", "boire, se laver", ROUGE), ("agriculteurs", "irriguer", VERT), ("industrie", "refroidir, laver", GRIS),
          ("énergie", "centrales", "#6b4c9a"), ("loisirs", "piscines, pêche", C2), ("nature", "rivières, poissons", "#1e8449")]
    for i, (t, d, c) in enumerate(us):
        a = -math.pi / 2 + i * 2 * math.pi / len(us)
        x, y = cx + 130 * math.cos(a), cy + 88 * math.sin(a)
        s.append(f'<line x1="{cx + fs*3.2*math.cos(a):.1f}" y1="{cy + fs*3.2*math.sin(a):.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="{c}" stroke-width="1.4"/>')
        s.append(f'<rect x="{x - 48:.1f}" y="{y - 16:.1f}" width="96" height="32" rx="6" fill="#fff" stroke="{c}" stroke-width="1.5"/>')
        s.append(texte(x, y - 2, t, fs * 0.82, fill=c, poids=800))
        s.append(texte(x, y + fs * 0.85, d, fs * 0.65))
    s.append("</svg>")
    return "".join(s)


ORIGINES = [("fraises", "Espagne", [-3.6, 40.0]), ("bananes", "Cameroun", [12.4, 5.6]), ("noisettes", "Turquie", [34.8, 39.0]),
            ("oranges", "Afrique du Sud", [24.8, -29.5]), ("citrons", "Argentine", [-64.5, -34.5]), ("feta", "Grèce", [22.0, 39.5]),
            ("poires", "Chili", [-71.0, -33.5]), ("myrtilles", "Portugal", [-8.1, 39.6]),
            ("kiwis", "Nouvelle-Zélande", [174.0, -41.0]), ("mangues", "Brésil", [-47.9, -15.8])]
PARIS = [2.35, 48.86]

LECONS = {
    "l01": {"competence": "Découpage administratif : la commune et ses lieux.",
            "visuels": [
                {"type": "svg", "titre": "Qui dirige la commune ?",
                 "svg": etapes([("Les habitants", "votent tous\nles 6 ans", C1), ("Le conseil municipal", "est élu", BLEU),
                                ("Le maire", "est élu par\nle conseil", C2)], sens="h", numeros=False)},
                {"type": "svg", "etiquette": "Tableau", "titre": "Les fonctions des lieux d'une commune",
                 "svg": tableau(["Fonction", "Exemples de lieux"], [
                     ["administrative", "mairie, poste"], ["éducative", "école, bibliothèque"],
                     ["commerciale", "boulangerie, supermarché"], ["de santé", "cabinet médical, pharmacie"],
                     ["de loisirs", "parc, stade, salle des fêtes"]], couleur=C1, largeurs=[1, 1.6])}]},
    "l02": {"competence": "Découpage administratif : commune, département, région, pays, continent ; les régions françaises.",
            "visuels": [
                {"type": "carte", "titre": "Les 13 régions de France métropolitaine",
                 "legende": "La Bourgogne-Franche-Comté, région de l'école, est en couleur.",
                 "source": "Contours des régions : france-geojson (IGN, Licence ouverte) ; fond : Natural Earth.",
                 "spec": spec_france(frontieres=False, couleurs={"terre": "#eef0ea"},
                                     couches=[{"fichier": "fr-regions-version-simplifiee.geojson", "remplissage": "#f7f1e1",
                                               "couleurs_individuelles": {"prop": "nom", "table": {"Bourgogne-Franche-Comté": "#f2c38b"}},
                                               "contour": "#8a7a5a", "epaisseur": 0.8,
                                               "libelles": {"prop": "nom", "taille": 0.62, "renommer": REGIONS_NOMS,
                                                            "positions": {"Provence-Alpes-Côte d'Azur": [6.0, 43.95], "Île-de-France": [2.5, 48.72]}}}],
                                     points=[{"lonlat": [5.04, 47.32], "nom": "Dijon", "style": "capitale", "pos": "s", "taille": 0.75}],
                                     nord=False)},
                {"type": "svg", "titre": "Des territoires emboîtés", "svg": emboitement()}]},
    "l03": {"competence": "Les espaces ruraux et la densité de population.",
            "visuels": [
                {"type": "svg", "etiquette": "Tableau", "titre": "La densité de population",
                 "svg": tableau(["Lieu", "Densité (hab/km²)"], [
                     ["une grande ville", "souvent plus de 3 000"], ["la France (moyenne)", "environ 106"],
                     ["un village de montagne", "parfois moins de 10"]], couleur=C1, largeurs=[1.2, 1.2]),
                 "legende": "densité = nombre d'habitants ÷ superficie (km²)"},
                {"type": "photo", "src": "assets/images/s03-intro.jpg", "titre": "Clamecy (Nièvre)",
                 "legende": "Une petite ville entourée d'un espace rural : champs, prairies, forêts."}]},
    "l04": {"competence": "Les espaces urbains et les secteurs d'activité.",
            "visuels": [
                {"type": "svg", "etiquette": "Graphique", "titre": "Les actifs par secteur en France aujourd'hui",
                 "svg": barres([("primaire", 2, VERT), ("secondaire", 18, GRIS), ("tertiaire", 80, BLEU)], unite="%",
                               titre_y="Part des actifs", vmax=100, graduation=20),
                 "legende": "En 1911, près de 40 % des actifs travaillaient dans le secteur primaire."},
                {"type": "photo", "src": "assets/images/s04-intro.jpg", "titre": "Besançon vue de la citadelle"}]},
    "l05": {"competence": "Les espaces de montagne et le tourisme.",
            "visuels": [
                {"type": "carte", "titre": "Les grands massifs montagneux",
                 "spec": spec_france(pays_mis_en_avant=["France"], couches=[MASSIFS],
                                     points=[{"lonlat": [6.865, 45.833], "nom": "mont Blanc\n4 806 m", "style": "etoile", "couleur": ROUGE, "pos": "e", "taille": 0.75},
                                             {"lonlat": [6.08, 46.50], "nom": "Les Rousses", "pos": "w", "taille": 0.75}],
                                     textes=[{"lonlat": [9.1, 42.1], "texte": "CORSE", "style": "region", "taille": 0.7, "couleur": "#6b4a1f"}])},
                {"type": "photo", "src": "assets/images/s05-coeur.jpg", "titre": "Le domaine skiable des Rousses (Jura)"}]},
    "l06": {"competence": "Principales caractéristiques d'une seconde région : le littoral touristique normand.",
            "visuels": [
                {"type": "carte", "titre": "Étretat, en Normandie",
                 "source": "Contours des régions : france-geojson (IGN, Licence ouverte) ; fond : Natural Earth.",
                 "spec": spec_france(frontieres=False, couleurs={"terre": "#eef0ea"},
                                     couches=[{"fichier": "fr-regions-version-simplifiee.geojson", "remplissage": "#f7f1e1",
                                               "couleurs_individuelles": {"prop": "nom", "table": {"Normandie": "#9fd0c0", "Bourgogne-Franche-Comté": "#f2c38b"}},
                                               "contour": "#8a7a5a", "epaisseur": 0.6,
                                               "libelles": {"prop": "nom", "taille": 0.8, "positions": {n: None for n in [
                                                   "Hauts-de-France", "Grand Est", "Île-de-France", "Centre-Val de Loire", "Pays de la Loire", "Bretagne",
                                                   "Nouvelle-Aquitaine", "Occitanie", "Auvergne-Rhône-Alpes", "Provence-Alpes-Côte d'Azur", "Corse",
                                                   "Bourgogne-Franche-Comté"]} | {"Normandie": [0.2, 48.95]}}}],
                                     points=[{"lonlat": [0.204, 49.707], "nom": "Étretat", "style": "etoile", "couleur": ROUGE, "pos": "n"},
                                             {"lonlat": [5.04, 47.32], "nom": "Dijon", "style": "capitale", "pos": "s"}],
                                     textes=MERS[2:3] + MERS[:1], nord=False)},
                {"type": "photo", "src": "assets/images/s06-intro.jpg", "titre": "Les falaises d'Étretat"}]},
    "l07": {"competence": "Les mers et les océans qui bordent la France ; le littoral touristique.",
            "visuels": [
                {"type": "carte", "titre": "Les mers et l'océan qui bordent la France",
                 "spec": spec_france(pays_mis_en_avant=["France"], textes=MERS,
                                     points=[{"lonlat": [-1.559, 43.483], "nom": "Biarritz", "pos": "e"},
                                             {"lonlat": [-1.168, 44.661], "nom": "Arcachon", "pos": "e"},
                                             {"lonlat": [-1.151, 46.160], "nom": "La Rochelle", "pos": "e"},
                                             {"lonlat": [0.204, 49.707], "nom": "Étretat", "pos": "e"}], echelle_km=200)},
                {"type": "photo", "src": "assets/images/s07-coeur.jpg", "titre": "La grande plage de Biarritz"}]},
    "l08": {"competence": "Identifier les manifestations des inégalités de niveau de vie ; localiser sur un planisphère les aires géographiques.",
            "visuels": [
                {"type": "carte", "largeur": "pleine", "titre": "Les niveaux de revenu des pays du monde",
                 "legende": "Pays classés selon le revenu moyen par habitant. Les pays les plus pauvres sont surtout en Afrique et en Asie du Sud.",
                 "source": "Groupes de revenu de la Banque mondiale, repris par Natural Earth (domaine public).",
                 "spec": {"largeur": 720, "cible_mm": 186, "projection": "robinson", "etendue": [[-180, -58], [180, 84]],
                          "nord": False, "resolution": "110m", "frontieres": False,
                          "couches": [{"fichier": "ne_50m_admin_0_countries.geojson", "contour": "#ffffff", "epaisseur": 0.3, "seuil": 0.7,
                                       "couleurs_par": {"prop": "INCOME_GRP", "defaut": "#dddddd", "table": {
                                           "1. High income: OECD": "#1e8449", "2. High income: nonOECD": "#1e8449",
                                           "3. Upper middle income": "#8cc084", "4. Lower middle income": "#f5b041", "5. Low income": "#c0392b"}}}],
                          "legende": [{"type": "zone", "couleur": "#1e8449", "texte": "revenu élevé", "opacite": 1},
                                      {"type": "zone", "couleur": "#8cc084", "texte": "revenu intermédiaire (haut)", "opacite": 1},
                                      {"type": "zone", "couleur": "#f5b041", "texte": "revenu intermédiaire (bas)", "opacite": 1},
                                      {"type": "zone", "couleur": "#c0392b", "texte": "revenu faible", "opacite": 1}],
                          "position_legende": "bas-gauche"}},
                {"type": "photo", "src": "assets/images/s08-intro.jpg", "titre": "Dhaka (Bangladesh)"}]},
    "l09": {"competence": "Différences de pratiques alimentaires entre pays riches et pays pauvres.",
            "visuels": [
                {"type": "svg", "etiquette": "Graphique", "titre": "Le budget alimentation d'une semaine (exemple de la leçon)",
                 "svg": barres([("France", 25, BLEU), ("Mali", 10, C2)], unite="€", titre_y="Budget", vmax=30, graduation=5),
                 "legende": "Au Mali, une famille dispose souvent de moins de 10 € pour la semaine."},
                {"type": "photo", "src": "assets/images/s09-intro.jpg", "titre": "Un marché de Bamako (Mali)"}]},
    "l10": {"competence": "Différence entre produits agricoles et produits dérivés.",
            "visuels": [
                {"type": "svg", "etiquette": "Tableau", "titre": "Du produit agricole au produit transformé",
                 "svg": tableau(["Produit agricole", "", "Produit transformé"], [
                     ["blé", "→", "pain, pâtes"], ["lait", "→", "yaourt, fromage, beurre"], ["raisin", "→", "jus de raisin"],
                     ["tomate", "→", "sauce tomate"], ["betterave, canne", "→", "sucre"], ["cacao", "→", "chocolat"]],
                     couleur=C1, largeurs=[1.1, 0.3, 1.4])},
                {"type": "svg", "etiquette": "Tableau", "titre": "Un espace de production, un métier",
                 "svg": tableau(["Espace", "Métier", "Produits"], [
                     ["élevage", "éleveur", "volailles, œufs, lait"], ["champ de céréales", "céréalier", "blé, maïs"],
                     ["exploitation maraîchère", "maraîcher", "carottes, salades"], ["verger", "arboriculteur", "pommes, poires"]],
                     couleur=C2, largeurs=[1.3, 1, 1.2])}]},
    "l11": {"competence": "La chaîne de production d'un aliment consommé (le yaourt).",
            "visuels": [
                {"type": "svg", "titre": "Du lait au yaourt",
                 "svg": etapes([("À la ferme", "traite, lait refroidi dans un tank", VERT),
                                ("Transport", "camion-citerne réfrigéré", GRIS),
                                ("À l'usine", "analyse, pasteurisation, ferments", BLEU),
                                ("Conditionnement", "pots, couvercles, palettes", "#6b4c9a"),
                                ("Distribution", "camions frigorifiques vers les magasins", GRIS),
                                ("Consommation", "achat, frigo à la maison", C2)], sens="v"),
                 "legende": "La chaîne du froid ne doit jamais être interrompue."}]},
    "l12": {"competence": "La chaîne de production d'un aliment : provenance des aliments et kilomètres alimentaires.",
            "visuels": [
                {"type": "carte", "largeur": "pleine", "titre": "D'où viennent les fruits et produits d'un supermarché ?",
                 "legende": "Exemples d'origines lues sur les étiquettes (leçon). Plus la ligne est longue, plus le transport rejette de CO₂.",
                 "spec": {"largeur": 720, "cible_mm": 186, "projection": "robinson", "etendue": [[-180, -58], [180, 84]],
                          "nord": False, "resolution": "110m", "pays_mis_en_avant": ["France"],
                          "lignes": [{"coords": [ll, PARIS], "couleur": C2, "epaisseur": 1.3, "fleches": True} for _, _, ll in ORIGINES],
                          "points": [{"lonlat": ll, "nom": f"{p}\n{pays}", "pos": ("w" if ll[0] < 0 else "e"), "couleur": C1, "taille": 0.8} for p, pays, ll in ORIGINES] +
                                    [{"lonlat": PARIS, "nom": "France", "style": "capitale", "couleur": ROUGE, "pos": "n"}]}},
                {"type": "svg", "titre": "Réduire ses kilomètres alimentaires",
                 "svg": etapes([("Circuit court", "acheter au producteur", VERT), ("Local", "produits de la région", C1),
                                ("De saison", "fruits et légumes du moment", C2), ("Moins de viande", "", ROUGE)], sens="h", numeros=False)}]},
    "l13": {"competence": "Repérer les principaux fleuves et massifs montagneux.",
            "visuels": [
                {"type": "carte", "titre": "Les cinq fleuves et les grands massifs de France",
                 "spec": spec_france(pays_mis_en_avant=["France"], resolution="50m",
                                     fleuves=["Seine", "Loire", "Garonne", "Rhône", "Rhne", "Rhin", "Rhein"], epaisseur_fleuve=1.8,
                                     couches=[MASSIFS],
                                     textes=[{"lonlat": [1.2, 49.55], "texte": "Seine", "style": "mer", "couleur": BLEU, "taille": 0.9},
                                             {"lonlat": [0.2, 47.05], "texte": "Loire", "style": "mer", "couleur": BLEU, "taille": 0.9},
                                             {"lonlat": [-0.2, 44.6], "texte": "Garonne", "style": "mer", "couleur": BLEU, "taille": 0.9},
                                             {"lonlat": [4.35, 44.4], "texte": "Rhône", "style": "mer", "couleur": BLEU, "taille": 0.9},
                                             {"lonlat": [8.25, 49.1], "texte": "Rhin", "style": "mer", "couleur": BLEU, "taille": 0.9}] + MERS[:3],
                                     points=[{"lonlat": [6.865, 45.833], "nom": "mont Blanc", "style": "etoile", "couleur": ROUGE, "pos": "e", "taille": 0.7}])}]},
    "l14": {"competence": "Repérer les principaux fleuves : le trajet de l'eau, amont et aval.",
            "visuels": [
                {"type": "svg", "titre": "Le trajet de l'eau", "svg": profil_cours_eau()},
                {"type": "carte", "titre": "La Seine, de sa source à la Manche",
                 "spec": {"largeur": 360, "cible_mm": 66, "etendue": [[-0.4, 47.3], [5.2, 49.9]], "resolution": "10m",
                          "pays_mis_en_avant": ["France"], "fleuves": ["Seine", "Yonne", "Marne"], "epaisseur_fleuve": 1.6,
                          "points": [{"lonlat": [4.716, 47.487], "nom": "source\n(Source-Seine)", "style": "etoile", "couleur": BLEU, "pos": "s"},
                                     {"lonlat": [2.35, 48.86], "nom": "Paris", "style": "capitale", "pos": "s"},
                                     {"lonlat": [1.099, 49.443], "nom": "Rouen", "pos": "s"},
                                     {"lonlat": [0.107, 49.494], "nom": "Le Havre\n(estuaire)", "pos": "s"},
                                     {"lonlat": [5.04, 47.32], "nom": "Dijon", "pos": "e"}],
                          "textes": [{"lonlat": [0.3, 49.8], "texte": "MANCHE", "style": "mer"},
                                     {"lonlat": [3.9, 48.1], "texte": "amont", "style": "region", "couleur": C1, "taille": 0.8},
                                     {"lonlat": [1.6, 49.25], "texte": "aval", "style": "region", "couleur": C1, "taille": 0.8}],
                          "echelle_km": 50}},
                {"type": "photo", "src": "assets/images/s14-intro.jpg", "titre": "Les sources de la Seine (Côte-d'Or)"}]},
    "l15": {"competence": "Décrire les différents usages de l'eau douce en France.",
            "visuels": [
                {"type": "svg", "etiquette": "Graphique", "titre": "À quoi sert l'eau douce consommée en France ?",
                 "svg": barres([("agricole", 48, VERT), ("domestique", 24, BLEU), ("énergétique", 22, "#6b4c9a"), ("industriel", 6, GRIS)],
                               unite="%", titre_y="Part de l'eau consommée", vmax=60, graduation=10),
                 "legende": "Les loisirs utilisent aussi de l'eau (piscines, stations de ski…). Un Français consomme en moyenne 150 litres par jour."},
                {"type": "photo", "src": "assets/images/s15-intro.jpg", "titre": "La Garonne à Toulouse"}]},
    "l16": {"competence": "L'eau, une ressource convoitée faisant l'objet de conflits d'usages.",
            "visuels": [
                {"type": "svg", "titre": "Quand l'eau manque, tous la veulent", "svg": conflit_usages(),
                 "legende": "Le préfet peut limiter les usages ; l'eau potable reste prioritaire."},
                {"type": "photo", "src": "assets/images/s16-coeur.jpg", "titre": "Un lac à son plus bas niveau"}]},
}
