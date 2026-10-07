"""Identité du jeu « Le Secret du donjon » : grades, palette, voix, portraits, direction artistique."""

# Noms de grades : métiers et savoir-faire d'un chantier ; aucune connotation religieuse, militaire ou héréditaire.
NOMS = {
    "mousse":     {"nom": "Manœuvre",       "icone": "🧱", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple, aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Apprenti",       "icone": "🔨", "equivalent": "≈ CM1", "profil": "cœur de programme CM1"},
    "timonier":   {"nom": "Compagnon",      "icone": "📐", "equivalent": "≈ CM2", "profil": "cœur de programme CM2, plus d'éléments, vocabulaire précis"},
    "lieutenant": {"nom": "Artisan",        "icone": "🏗️", "equivalent": "≈ 6ᵉ",  "profil": "raisonnement en deux étapes, documents à croiser, justification"},
    "second":     {"nom": "Maître d'œuvre", "icone": "🧭", "equivalent": "≈ 5ᵉ",  "profil": "synthèse, données chiffrées, pièges de logique, justification"},
}

# Pierre, ardoise et bannière rouge : sobre et froid, accents rouge brique.
PALETTE = {
    "--ocean": "#2b2d35", "--abysse": "#14151a", "--laiton": "#b94a3a", "--laiton-clair": "#f2b3a0", "--laiton-fonce": "#5c1f16",
    "--acajou": "#2d2a33", "--acajou-clair": "#4a4654", "--vertdegris": "#3a4a42", "--ambre": "#ffb55a", "--cyan": "#a9c4e0",
    "--papier": "#f2eee6", "--encre": "#1f1d22", "--rouge": "#b3361f", "--vert": "#2e7d4f",
    "--panneau-haut": "#f1efe9", "--panneau-bas": "#dcd8cc", "--accent": "#8a2f24", "--accent-clair": "#f6e4df",
    "--fond-carte": "#fbfaf7", "--fond-colonne": "#e8e4da", "--bord-doux": "#a79f8e", "--bord-clair": "#c9c2b0", "--rivet": "#b94a3a",
    "--plaque-haut": "rgba(45,42,51,.96)", "--plaque-bas": "rgba(20,19,24,.97)", "--cadre-haut": "rgba(40,38,46,.94)", "--cadre-bas": "rgba(18,17,22,.96)",
    "--laiton-profond": "#8c2f22", "--ombre-bouton": "#4a150e", "--encre-bouton": "#220a07", "--bareme-fond": "#2d2a33",
}

VOIX = {
    "josselin": {"edge": "fr-FR-HenriNeural",               "nom": "Henri",    "rate": 0.92, "pitch": 0.9},     # maître maçon, franc
    "colin":    {"edge": "fr-FR-RemyMultilingualNeural",     "nom": "Remy",     "rate": 1.1,  "pitch": 1.25},    # page de 11 ans, vif et bavard
    "alienor":  {"edge": "fr-FR-VivienneMultilingualNeural", "nom": "Vivienne", "rate": 0.92, "pitch": 0.95},    # dame du château, posée
    "mahaut":   {"edge": "fr-FR-EloiseNeural",               "nom": "Eloise",   "rate": 1.08, "pitch": 1.05},    # paysanne de 11 ans, directe
    "perrine":  {"edge": "fr-FR-DeniseNeural",               "nom": "Denise",   "rate": 1.05, "pitch": 1.0},     # meunière maligne
}

GUIDES = {1: "josselin", 2: "colin", 3: "alienor", 4: "mahaut", 5: "perrine"}

PORTRAITS = {
    "josselin": {"genre": "homme", "coiffure": "courte", "cheveux": "#5a3a22", "peau": "#dba680", "habit": "#6a4428", "barbe": True, "lunettes": False},
    "colin":    {"genre": "garçon", "coiffure": "courte", "cheveux": "#a8844a", "peau": "#f0c9ad", "habit": "#7a2e3a", "barbe": False, "lunettes": False},
    "alienor":  {"genre": "femme", "coiffure": "longue", "cheveux": "#5a3a22", "peau": "#e6c2a6", "habit": "#3a3a52", "lunettes": False},
    "mahaut":   {"genre": "fille", "coiffure": "longue", "cheveux": "#2a1c14", "peau": "#dba680", "habit": "#4a5a2a", "lunettes": False},
    "perrine":  {"genre": "femme", "coiffure": "courte", "cheveux": "#9c9c98", "peau": "#e6c2a6", "habit": "#5a3a62", "lunettes": False},
}

STYLE_VISUEL = ("Peinture numérique semi-réaliste de cinéma, ambiance médiévale sobre et crédible, lumière rasante du petit matin ou des torches contre ombres froides de pierre, "
                "bois, fer, pierre et laine, détails artisanaux lisibles, grain fin, profondeur de champ.")
EPOQUE = "Moyen Âge central (Xe-XIIIe siècles), un château en construction et le village à ses pieds."
