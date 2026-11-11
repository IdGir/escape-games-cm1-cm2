"""Identité du jeu « Les Archives du port » : grades, palette, voix, portraits, direction artistique.
Sujet sensible : les élèves sont des enquêteurs d'archives ; grades = métiers de l'archive et de l'histoire."""

# Grades : métiers des archives et de l'histoire ; aucune connotation maritime, militaire, servile ou commerciale.
NOMS = {
    "mousse":     {"nom": "Apprenti des archives", "icone": "🔎", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple, aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Enquêteur",             "icone": "📂", "equivalent": "≈ CM1", "profil": "cœur de programme CM1 : repères, trajets, produits"},
    "timonier":   {"nom": "Enquêteur confirmé",    "icone": "📜", "equivalent": "≈ CM2", "profil": "cœur de programme CM2 : chiffres sourcés, dates exactes, Code noir, marronnage"},
    "lieutenant": {"nom": "Historien",             "icone": "🖋️", "equivalent": "≈ 6ᵉ",  "profil": "raisonnement en deux étapes, documents à croiser, justification par la fiche"},
    "second":     {"nom": "Archiviste en chef",    "icone": "🏛️", "equivalent": "≈ 5ᵉ",  "profil": "synthèse, données chiffrées, critique de sources, justification"},
}

# Archives : encre ardoise, papier ancien, rouge de cire à cacheter, laiton des lampes.
PALETTE = {
    "--ocean": "#2f4858", "--abysse": "#15212a", "--laiton": "#c9a227", "--laiton-clair": "#f2e2a8", "--laiton-fonce": "#6b4f10",
    "--acajou": "#5c3b22", "--acajou-clair": "#7a5232", "--vertdegris": "#2f6b4a", "--ambre": "#ffe8a8", "--cyan": "#cfe3ee",
    "--papier": "#f6eedb", "--encre": "#2b2118", "--rouge": "#8c2f1c", "--vert": "#2f6b4a",
    "--panneau-haut": "#fbf6e9", "--panneau-bas": "#ece0c4", "--accent": "#2f4858", "--accent-clair": "#e6edf0",
    "--fond-carte": "#fffdf6", "--fond-colonne": "#efe6d2", "--bord-doux": "#a8916a", "--bord-clair": "#d6c7a6", "--rivet": "#c9a227",
    "--plaque-haut": "rgba(47,72,88,.96)", "--plaque-bas": "rgba(21,33,42,.97)", "--cadre-haut": "rgba(59,42,30,.94)", "--cadre-bas": "rgba(35,24,16,.96)",
    "--laiton-profond": "#9a7a1c", "--ombre-bouton": "#3b2a08", "--encre-bouton": "#1f1404", "--bareme-fond": "#2f4858",
}

# Une voix par personnage, la même du début à la fin (voix gratuites d'Edge ; `nom` : repli voix du navigateur).
VOIX = {
    "ines":   {"edge": "fr-FR-DeniseNeural",               "nom": "Denise",   "rate": 0.97, "pitch": 1.0},    # archiviste, posée
    "malik":  {"edge": "fr-FR-HenriNeural",                "nom": "Henri",    "rate": 0.92, "pitch": 0.92},   # historien, grave et calme
    "celia":  {"edge": "fr-FR-VivienneMultilingualNeural", "nom": "Vivienne", "rate": 0.97, "pitch": 1.04},   # historienne, claire
    "margot": {"edge": "fr-BE-CharlineNeural",             "nom": "Charline", "rate": 1.0,  "pitch": 1.0},    # conservatrice, nette
    "theo":   {"edge": "fr-FR-RemyMultilingualNeural",     "nom": "Remy",     "rate": 1.06, "pitch": 1.14},   # élève, enjoué
}

# Personnage guide de chaque salle (il parle pour toutes les énigmes de la salle).
GUIDES = {1: "ines", 2: "malik", 3: "celia", 4: "margot", 5: "theo"}

# Traits des portraits dessinés (remplacés par les images déposées dans assets/images/personnages/).
PORTRAITS = {
    "ines":   {"genre": "femme", "coiffure": "longue", "cheveux": "#2b1a10", "peau": "#c99a74", "habit": "#7d8a8f", "lunettes": True},
    "malik":  {"genre": "homme", "coiffure": "courte", "cheveux": "#141010", "peau": "#7a4e34", "habit": "#6b4a2c", "barbe": True, "lunettes": False},
    "celia":  {"genre": "femme", "coiffure": "longue", "cheveux": "#1a1210", "peau": "#8a5a3c", "habit": "#3e7a52", "lunettes": False},
    "margot": {"genre": "femme", "coiffure": "courte", "cheveux": "#b07a3a", "peau": "#f0c9ad", "habit": "#2f4858", "lunettes": False},
    "theo":   {"genre": "homme", "coiffure": "courte", "cheveux": "#c98a3a", "peau": "#f3d9c4", "habit": "#b8432a", "barbe": False, "lunettes": False},
}

STYLE_VISUEL = ("Photographie photoréaliste de cinéma, objectif 35 mm, intérieur d'un bâtiment d'archives ancien, boiseries, lampes vertes, "
                "lumière douce d'automne, papier ancien, couleurs sobres, aucune inscription lisible, grain fin.")
EPOQUE = ("Univers contemporain : les Archives imaginaires d'un port de la façade atlantique. Les documents étudiés datent des XVIIe, "
          "XVIIIe et XIXe siècles. Sujet sensible : aucune image de personnes réduites en esclavage, aucune violence.")
