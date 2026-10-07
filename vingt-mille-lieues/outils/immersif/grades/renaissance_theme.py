"""Identité du jeu « L'Atelier de Léonard à Amboise » : grades, palette, voix, portraits, direction artistique."""

NOMS = {
    "mousse":     {"nom": "Dessinateur", "icone": "✏️", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple, aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Graveur",     "icone": "🖋️", "equivalent": "≈ CM1", "profil": "cœur de programme CM1"},
    "timonier":   {"nom": "Peintre",     "icone": "🎨", "equivalent": "≈ CM2", "profil": "cœur de programme CM2, plus d'éléments, vocabulaire précis"},
    "lieutenant": {"nom": "Architecte",  "icone": "📐", "equivalent": "≈ 6ᵉ",  "profil": "raisonnement en deux étapes, documents à croiser, justification"},
    "second":     {"nom": "Humaniste",   "icone": "📖", "equivalent": "≈ 5ᵉ",  "profil": "synthèse, données chiffrées, pièges de logique, justification"},
}

# Italie de la Renaissance : olive, ocre et ivoire.
PALETTE = {
    "--ocean": "#26271a", "--abysse": "#12130a", "--laiton": "#a8872c", "--laiton-clair": "#e8d48a", "--laiton-fonce": "#55430f",
    "--acajou": "#3a3a1f", "--acajou-clair": "#5a5a2e", "--vertdegris": "#46553a", "--ambre": "#ffd27a", "--cyan": "#b9d8c0",
    "--papier": "#f6f1df", "--encre": "#26271a", "--rouge": "#a3261b", "--vert": "#4d7a2c",
    "--panneau-haut": "#f8f4e4", "--panneau-bas": "#e6dfc2", "--accent": "#5d6b1f", "--accent-clair": "#eef0d6",
    "--fond-carte": "#fdfbf1", "--fond-colonne": "#ece6cc", "--bord-doux": "#b3a56e", "--bord-clair": "#d3c997", "--rivet": "#a8872c",
    "--plaque-haut": "rgba(46,46,26,.96)", "--plaque-bas": "rgba(20,21,11,.97)", "--cadre-haut": "rgba(40,41,24,.94)", "--cadre-bas": "rgba(17,18,9,.96)",
    "--laiton-profond": "#7a621a", "--ombre-bouton": "#3e320a", "--encre-bouton": "#1d1805", "--bareme-fond": "#3a3a1f",
}

VOIX = {
    "tommaso":  {"edge": "fr-FR-RemyMultilingualNeural",     "nom": "Remy",     "rate": 1.08, "pitch": 1.2},    # apprenti de 12 ans, émerveillé
    "jacquet":  {"edge": "fr-FR-HenriNeural",                "nom": "Henri",    "rate": 0.88, "pitch": 0.9},    # imprimeur grave mais passionné
    "helene":   {"edge": "fr-FR-VivienneMultilingualNeural", "nom": "Vivienne", "rate": 0.95, "pitch": 1.0},    # dame de la cour, fine
    "colombe":  {"edge": "fr-FR-EloiseNeural",               "nom": "Eloise",   "rate": 1.05, "pitch": 1.05},   # fille de maçon, directe
    "bastien":  {"edge": "fr-BE-GerardNeural",               "nom": "Gerard",   "rate": 1.0,  "pitch": 1.0},    # jeune peintre fier
}

GUIDES = {1: "jacquet", 2: "helene", 3: "tommaso", 4: "colombe", 5: "bastien"}

PORTRAITS = {
    "tommaso":  {"genre": "garçon", "coiffure": "courte", "cheveux": "#2a1c14", "peau": "#dba680", "habit": "#7a2e3a", "barbe": False, "lunettes": False},
    "jacquet":  {"genre": "homme", "coiffure": "courte", "cheveux": "#9c9c98", "peau": "#e6c2a6", "habit": "#3a3a52", "barbe": True, "lunettes": True},
    "helene":   {"genre": "femme", "coiffure": "longue", "cheveux": "#5a3a22", "peau": "#e6c2a6", "habit": "#5a3a62", "lunettes": False},
    "colombe":  {"genre": "fille", "coiffure": "longue", "cheveux": "#a04a22", "peau": "#f0c9ad", "habit": "#4a5a2a", "lunettes": False},
    "bastien":  {"genre": "garçon", "coiffure": "courte", "cheveux": "#1a1a1a", "peau": "#dba680", "habit": "#2a4a6a", "barbe": False, "lunettes": False},
}

STYLE_VISUEL = ("Peinture numérique semi-réaliste de cinéma, ambiance de la Renaissance, lumière dorée de fin de journée contre ombres brunes, "
                "pierre claire, bois, papier et pigments, détails d'atelier lisibles (sans inscriptions), grain fin, profondeur de champ.")
EPOQUE = "Début du XVIe siècle, règne de François Ier : Amboise, l'imprimerie, l'atelier de Léonard, Chambord et la galerie de peinture."
