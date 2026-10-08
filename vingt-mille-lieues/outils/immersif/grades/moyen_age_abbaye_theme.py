"""Identité du jeu « Le Manuscrit de l'abbaye » : grades, palette, voix, portraits, direction artistique."""

# Noms de grades : métiers du livre ; aucune connotation religieuse.
NOMS = {
    "mousse":     {"nom": "Porte-plume", "icone": "🪶", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple, aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Copiste",     "icone": "✒️", "equivalent": "≈ CM1", "profil": "cœur de programme CM1"},
    "timonier":   {"nom": "Enlumineur",  "icone": "🎨", "equivalent": "≈ CM2", "profil": "cœur de programme CM2, plus d'éléments, vocabulaire précis"},
    "lieutenant": {"nom": "Calligraphe", "icone": "📜", "equivalent": "≈ 6ᵉ",  "profil": "raisonnement en deux étapes, documents à croiser, justification"},
    "second":     {"nom": "Érudit",      "icone": "📚", "equivalent": "≈ 5ᵉ",  "profil": "synthèse, données chiffrées, pièges de logique, justification"},
}

# Manuscrit enluminé : bordeaux, or, parchemin, touches de bleu lapis.
PALETTE = {
    "--ocean": "#3a1c24", "--abysse": "#1d0d12", "--laiton": "#d1a43a", "--laiton-clair": "#f5de9a", "--laiton-fonce": "#6d4f10",
    "--acajou": "#4a1f2c", "--acajou-clair": "#6b2f40", "--vertdegris": "#3d4a3a", "--ambre": "#ffcf7a", "--cyan": "#a8c4f0",
    "--papier": "#f7efdc", "--encre": "#2a1a1f", "--rouge": "#a3261b", "--vert": "#2e7d4f",
    "--panneau-haut": "#faf3e0", "--panneau-bas": "#ecdcb8", "--accent": "#2c4a8a", "--accent-clair": "#e3eaf8",
    "--fond-carte": "#fffcf3", "--fond-colonne": "#f1e5c8", "--bord-doux": "#b89a68", "--bord-clair": "#d9c398", "--rivet": "#d1a43a",
    "--plaque-haut": "rgba(58,28,36,.96)", "--plaque-bas": "rgba(29,13,18,.97)", "--cadre-haut": "rgba(50,24,32,.94)", "--cadre-bas": "rgba(24,10,15,.96)",
    "--laiton-profond": "#a37a1c", "--ombre-bouton": "#4a3408", "--encre-bouton": "#241505", "--bareme-fond": "#3a1c24",
}

VOIX = {
    "anselme": {"edge": "fr-FR-HenriNeural",               "nom": "Henri",    "rate": 0.9,  "pitch": 0.92},    # moine copiste, doux et érudit
    "aude":    {"edge": "fr-FR-EloiseNeural",               "nom": "Eloise",   "rate": 1.1,  "pitch": 1.05},    # élève de 11 ans, parle vite
    "alix":    {"edge": "fr-FR-DeniseNeural",               "nom": "Denise",   "rate": 0.95, "pitch": 0.97},    # abbesse ferme et bienveillante
    "garin":   {"edge": "fr-FR-RemyMultilingualNeural",     "nom": "Remy",     "rate": 1.05, "pitch": 1.15},    # apprenti tailleur de pierre de 12 ans
}

GUIDES = {1: "anselme", 2: "aude", 3: "anselme", 4: "alix", 5: "garin"}

PORTRAITS = {
    "anselme": {"genre": "homme", "coiffure": "chauve", "cheveux": "#9c9c98", "peau": "#e6c2a6", "habit": "#5a3a22", "barbe": False, "lunettes": False},
    "aude":    {"genre": "fille", "coiffure": "longue", "cheveux": "#5a3a22", "peau": "#e6c2a6", "habit": "#2c4a8a", "lunettes": False},
    "alix":    {"genre": "femme", "coiffure": "courte", "cheveux": "#9c9c98", "peau": "#e6c2a6", "habit": "#e8e4da", "coiffe": "#f4f1ea", "lunettes": False},
    "garin":   {"genre": "garçon", "coiffure": "courte", "cheveux": "#2a1c14", "peau": "#dba680", "habit": "#6a4428", "barbe": False, "lunettes": False},
}

STYLE_VISUEL = ("Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance médiévale chaleureuse et crédible, lumière de bougie et de fenêtre étroite contre ombres brunes, "
                "parchemin, bois, pierre et vitraux, détails d'artisanat lisibles (sans inscriptions), grain fin, profondeur de champ.")
EPOQUE = "Haut et central Moyen Âge (Ve-XIIIe siècles) : Reims, le palais d'Aix, l'abbaye et son scriptorium, un hôtel-Dieu, un chantier d'église."
