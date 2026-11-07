"""Identité du jeu « La Fabrique des états » : grades, palette, voix, portraits, direction artistique."""

# Grades : métiers de la Fabrique, du plus simple au plus expert ; neutres (ni militaires, ni religieux, ni héréditaires).
NOMS = {
    "mousse":     {"nom": "Apprenti",   "icone": "🧤", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple, aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Technicien", "icone": "🔧", "equivalent": "≈ CM1", "profil": "cœur de programme CM1"},
    "timonier":   {"nom": "Ingénieur",  "icone": "⚙️", "equivalent": "≈ CM2", "profil": "cœur de programme CM2, plus d'éléments, vocabulaire précis"},
    "lieutenant": {"nom": "Physicien",  "icone": "🌡️", "equivalent": "≈ 6ᵉ",  "profil": "raisonnement en deux étapes, documents à croiser, justification"},
    "second":     {"nom": "Expert de la Fabrique", "icone": "🏭", "equivalent": "≈ 5ᵉ", "profil": "synthèse, données chiffrées, pièges de logique, justification"},
}

# Usine au bord d'un lac, après l'orage : bleu acier, glace, touches cuivre.
PALETTE = {
    "--ocean": "#1b2a36", "--abysse": "#0c141b", "--laiton": "#d98b4a", "--laiton-clair": "#f6c99c", "--laiton-fonce": "#6e3a14",
    "--acajou": "#22323f", "--acajou-clair": "#34495a", "--vertdegris": "#2b4652", "--ambre": "#ffd58a", "--cyan": "#9fdcf2",
    "--papier": "#f3f6f8", "--encre": "#16212a", "--rouge": "#b8382a", "--vert": "#2d7d55",
    "--panneau-haut": "#f5f8fa", "--panneau-bas": "#dfe8ee", "--accent": "#1f6a8f", "--accent-clair": "#e2f1f8",
    "--fond-carte": "#ffffff", "--fond-colonne": "#e6eef3", "--bord-doux": "#93aebd", "--bord-clair": "#c0d3de", "--rivet": "#d98b4a",
    "--plaque-haut": "rgba(27,42,54,.96)", "--plaque-bas": "rgba(12,20,27,.97)", "--cadre-haut": "rgba(24,38,49,.94)", "--cadre-bas": "rgba(10,17,23,.96)",
    "--laiton-profond": "#a85f26", "--ombre-bouton": "#4a2508", "--encre-bouton": "#1f1004", "--bareme-fond": "#22323f",
}

# Une voix par personnage, la même du début à la fin (voix gratuites d'Edge ; `nom` : repli voix du navigateur).
VOIX = {
    "ines":    {"edge": "fr-FR-DeniseNeural",               "nom": "Denise",   "rate": 0.97, "pitch": 1.0},    # ingénieure, posée
    "bastien": {"edge": "fr-FR-RemyMultilingualNeural",     "nom": "Remy",     "rate": 1.05, "pitch": 1.1},    # agent météo, enthousiaste
    "paolo":   {"edge": "fr-FR-HenriNeural",                "nom": "Henri",    "rate": 0.92, "pitch": 0.92},   # glacier, patient
    "fatou":   {"edge": "fr-FR-EloiseNeural",               "nom": "Eloise",   "rate": 1.05, "pitch": 1.05},   # cuisinière, vive
    "ninon":   {"edge": "fr-FR-VivienneMultilingualNeural", "nom": "Vivienne", "rate": 0.95, "pitch": 1.0},    # gardienne du château d'eau
}

# Personnage guide de chaque salle (il parle pour toutes les énigmes de la salle).
GUIDES = {1: "ines", 2: "bastien", 3: "paolo", 4: "fatou", 5: "ninon"}

# Traits des portraits dessinés (remplacés par les images déposées dans assets/images/personnages/).
PORTRAITS = {
    "ines":    {"genre": "femme", "coiffure": "longue", "cheveux": "#2a1c14", "peau": "#c99a74", "habit": "#1f6a8f", "lunettes": True},
    "bastien": {"genre": "homme", "coiffure": "courte", "cheveux": "#a8844a", "peau": "#f0c9ad", "habit": "#2d7d55", "barbe": False, "lunettes": False},
    "paolo":   {"genre": "homme", "coiffure": "courte", "cheveux": "#5a4a3a", "peau": "#dba680", "habit": "#e8eef2", "barbe": True, "lunettes": False},
    "fatou":   {"genre": "femme", "coiffure": "courte", "cheveux": "#1a1a1a", "peau": "#7a4e34", "habit": "#f4f1ea", "lunettes": False},
    "ninon":   {"genre": "femme", "coiffure": "longue", "cheveux": "#9a5a2a", "peau": "#f0c9ad", "habit": "#34495a", "lunettes": False},
}

STYLE_VISUEL = ("Photographie photoréaliste de cinéma, objectif 35 mm, lumière d'après l'orage, usine claire au bord d'un lac, "
                "cuves de verre, tuyauteries de cuivre, acier brossé, buée et reflets froids contre lueurs chaudes, aucune inscription lisible, grain fin.")
EPOQUE = "Univers contemporain imaginaire : une petite fabrique propre et sûre, où l'on fabrique de la glace et contrôle l'eau, au bord d'un lac."
