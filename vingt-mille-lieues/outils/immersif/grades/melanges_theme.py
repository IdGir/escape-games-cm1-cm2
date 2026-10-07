"""Identité du jeu « Le Laboratoire de Madame Mélange » : grades, palette, voix, portraits, direction artistique."""

NOMS = {
    "mousse":     {"nom": "Préparateur", "icone": "🧪", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple, aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Laborantin",  "icone": "⚗️", "equivalent": "≈ CM1", "profil": "cœur de programme CM1"},
    "timonier":   {"nom": "Technicien",  "icone": "🔬", "equivalent": "≈ CM2", "profil": "cœur de programme CM2, plus d'éléments, vocabulaire précis"},
    "lieutenant": {"nom": "Chimiste",    "icone": "⚖️", "equivalent": "≈ 6ᵉ",  "profil": "raisonnement en deux étapes, documents à croiser, justification"},
    "second":     {"nom": "Chercheur",   "icone": "🔭", "equivalent": "≈ 5ᵉ",  "profil": "synthèse, données chiffrées, pièges de logique, justification"},
}

# Laboratoire : vert d'eau, turquoise, touches violettes.
PALETTE = {
    "--ocean": "#17303a", "--abysse": "#0a181d", "--laiton": "#35b8b0", "--laiton-clair": "#a8efe9", "--laiton-fonce": "#0e5a56",
    "--acajou": "#1f3b44", "--acajou-clair": "#2f5663", "--vertdegris": "#26474a", "--ambre": "#ffe08a", "--cyan": "#9be7ff",
    "--papier": "#f2f8f7", "--encre": "#12262b", "--rouge": "#c0392b", "--vert": "#2e8b57",
    "--panneau-haut": "#f4fbfa", "--panneau-bas": "#dcecea", "--accent": "#6a3fb5", "--accent-clair": "#ece4fa",
    "--fond-carte": "#ffffff", "--fond-colonne": "#e4f1ef", "--bord-doux": "#8fb7b3", "--bord-clair": "#bcd8d4", "--rivet": "#35b8b0",
    "--plaque-haut": "rgba(23,48,58,.96)", "--plaque-bas": "rgba(10,24,29,.97)", "--cadre-haut": "rgba(20,44,52,.94)", "--cadre-bas": "rgba(8,20,24,.96)",
    "--laiton-profond": "#1b8a84", "--ombre-bouton": "#0b3a37", "--encre-bouton": "#05201e", "--bareme-fond": "#1f3b44",
}

VOIX = {
    "lila":    {"edge": "fr-FR-EloiseNeural",               "nom": "Eloise",   "rate": 1.08, "pitch": 1.05},   # apprentie chimiste de 11 ans
    "marius":  {"edge": "fr-FR-HenriNeural",                "nom": "Henri",    "rate": 1.02, "pitch": 1.05},   # cuisinier gourmand et blagueur
    "nadia":   {"edge": "fr-FR-DeniseNeural",               "nom": "Denise",   "rate": 1.0,  "pitch": 1.0},    # laborantine précise
    "yann":    {"edge": "fr-FR-RemyMultilingualNeural",     "nom": "Remy",     "rate": 0.92, "pitch": 0.9},    # paludier posé
    "melange": {"edge": "fr-FR-VivienneMultilingualNeural", "nom": "Vivienne", "rate": 0.9,  "pitch": 0.92},   # directrice solennelle
}

GUIDES = {1: "lila", 2: "marius", 3: "lila", 4: "nadia", 5: "yann"}

PORTRAITS = {
    "lila":    {"genre": "fille", "coiffure": "longue", "cheveux": "#5a3a22", "peau": "#e6c2a6", "habit": "#e8e4da", "lunettes": True},
    "marius":  {"genre": "homme", "coiffure": "courte", "cheveux": "#2a1c14", "peau": "#dba680", "habit": "#e8e4da", "coiffe": "#f4f1ea", "barbe": False, "lunettes": False},
    "nadia":   {"genre": "femme", "coiffure": "longue", "cheveux": "#1a1a1a", "peau": "#b8805e", "habit": "#e8e4da", "lunettes": False},
    "yann":    {"genre": "homme", "coiffure": "courte", "cheveux": "#9c9c98", "peau": "#c08a64", "habit": "#2a4a6a", "barbe": True, "lunettes": False},
    "melange": {"genre": "femme", "coiffure": "longue", "cheveux": "#9c9c98", "peau": "#e6c2a6", "habit": "#5a3a62", "lunettes": True},
}

STYLE_VISUEL = ("Peinture numérique semi-réaliste de cinéma, ambiance de vieux laboratoire de chimie bien rangé et lumineux, verre, laiton et carrelage, "
                "reflets de fioles colorées, lumière douce turquoise contre ombres chaudes, détails scientifiques lisibles (sans inscriptions), grain fin.")
EPOQUE = "Univers contemporain mais chaleureux : un laboratoire d'enfants avec balances, fioles, atelier de tri et marais salants."
