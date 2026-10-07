"""Identité du jeu « Le Grand Repas du chef » : noms des grades, palette, voix, portraits, direction artistique."""

NOMS = {
    "mousse":     {"nom": "Marmiton",   "icone": "🥄", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple, aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Commis",     "icone": "🥕", "equivalent": "≈ CM1", "profil": "cœur de programme CM1"},
    "timonier":   {"nom": "Cuisinier",  "icone": "🍳", "equivalent": "≈ CM2", "profil": "cœur de programme CM2, plus d'éléments, vocabulaire précis"},
    "lieutenant": {"nom": "Sous-chef",  "icone": "🍲", "equivalent": "≈ 6ᵉ",  "profil": "raisonnement en deux étapes, documents à croiser, justification"},
    "second":     {"nom": "Chef",       "icone": "👨‍🍳", "equivalent": "≈ 5ᵉ", "profil": "synthèse, données chiffrées, pièges de logique, justification"},
}

# Cuisine et potager : vert profond, orange carotte, crème.
PALETTE = {
    "--ocean": "#1f3326", "--abysse": "#0e1a12", "--laiton": "#e8803a", "--laiton-clair": "#ffc48a", "--laiton-fonce": "#7a3a10",
    "--acajou": "#3b2412", "--acajou-clair": "#5a3a22", "--vertdegris": "#2f4a35", "--ambre": "#ffd08a", "--cyan": "#bde6a8",
    "--papier": "#fbf3e3", "--encre": "#2a1d14", "--rouge": "#b3361f", "--vert": "#2e7d4f",
    "--panneau-haut": "#fff7ea", "--panneau-bas": "#f3e5cc", "--accent": "#b4532a", "--accent-clair": "#fde9d5",
    "--fond-carte": "#fffdf8", "--fond-colonne": "#f6e8d0", "--bord-doux": "#c9a77a", "--bord-clair": "#e0c9a0", "--rivet": "#e8803a",
    "--plaque-haut": "rgba(46,30,20,.96)", "--plaque-bas": "rgba(26,16,10,.97)", "--cadre-haut": "rgba(36,50,38,.94)", "--cadre-bas": "rgba(18,30,22,.96)",
    "--laiton-profond": "#b05a1c", "--ombre-bouton": "#5a2c0a", "--encre-bouton": "#2a1405", "--bareme-fond": "#2a3a2c",
}

VOIX = {
    "rosalie": {"edge": "fr-FR-DeniseNeural",               "nom": "Denise",   "rate": 0.98, "pitch": 1.0},     # cheffe exigeante, chaleureuse
    "nathan":  {"edge": "fr-FR-RemyMultilingualNeural",     "nom": "Remy",     "rate": 1.05, "pitch": 1.15},    # jeune commis enthousiaste
    "ines":    {"edge": "fr-FR-VivienneMultilingualNeural", "nom": "Vivienne", "rate": 0.95, "pitch": 1.0},     # médecin calme, pédagogue
    "basile":  {"edge": "fr-FR-HenriNeural",                "nom": "Henri",    "rate": 1.08, "pitch": 1.0},     # coureur essoufflé, plein d'humour
}

GUIDES = {1: "nathan", 2: "ines", 3: "rosalie", 4: "ines", 5: "basile"}

PORTRAITS = {
    "rosalie": {"genre": "femme", "coiffure": "courte", "cheveux": "#2a1c14", "peau": "#dba680", "habit": "#e8e4da", "coiffe": "#f4f1ea", "lunettes": False},
    "nathan":  {"genre": "garçon", "coiffure": "courte", "cheveux": "#5a3a22", "peau": "#f0c9ad", "habit": "#2a4a3a", "barbe": False, "lunettes": False},
    "ines":    {"genre": "femme", "coiffure": "longue", "cheveux": "#1a1a1a", "peau": "#8a5e42", "habit": "#3a3a52", "lunettes": True},
    "basile":  {"genre": "homme", "coiffure": "courte", "cheveux": "#a04a22", "peau": "#e6c2a6", "habit": "#b3361f", "barbe": False, "lunettes": False},
}

STYLE_VISUEL = ("Peinture numérique semi-réaliste de cinéma, ambiance chaleureuse de restaurant et de potager, lumière dorée de fin d'après-midi contre ombres vertes, "
                "bois, cuivre et céramique, détails gourmands lisibles, grain fin, profondeur de champ.")
EPOQUE = "Univers contemporain, un restaurant de campagne, « Le Grand Couvert », et une équipe cycliste en préparation d'étape."
