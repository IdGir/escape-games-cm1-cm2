"""Identité du jeu « Le Phare de l'île Lumière » : noms des grades, palette, voix des personnages."""

# Noms de grades : métiers et degrés de maîtrise liés à la lumière ; neutres (aucune connotation religieuse, militaire ou héréditaire).
NOMS = {
    "mousse":     {"nom": "Allumeur",      "icone": "🕯️", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple, aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Veilleur",      "icone": "🔦", "equivalent": "≈ CM1", "profil": "cœur de programme CM1"},
    "timonier":   {"nom": "Gardien",       "icone": "💡", "equivalent": "≈ CM2", "profil": "cœur de programme CM2, plus d'éléments, vocabulaire précis"},
    "lieutenant": {"nom": "Opticien",      "icone": "🔭", "equivalent": "≈ 6ᵉ",  "profil": "raisonnement en deux étapes, documents à croiser, justification"},
    "second":     {"nom": "Expert du phare", "icone": "🏮", "equivalent": "≈ 5ᵉ", "profil": "synthèse, données chiffrées, pièges de logique, justification"},
}

# Charte graphique : nuit sur l'île, lampe jaune du phare, fenêtre d'énigme claire à accents bleu marine.
PALETTE = {
    "--ocean": "#101a33", "--abysse": "#070c1a", "--laiton": "#f2b84b", "--laiton-clair": "#ffe29a", "--laiton-fonce": "#6b4a10",
    "--acajou": "#1a2547", "--acajou-clair": "#2a3a6b", "--vertdegris": "#1f3a4d", "--ambre": "#ffd27a", "--cyan": "#8fd3ff",
    "--papier": "#f4f1e6", "--encre": "#1a1e2b", "--rouge": "#b3361f", "--vert": "#2b7a4b",
    "--panneau-haut": "#f3f6fb", "--panneau-bas": "#dfe7f3", "--accent": "#274a8c", "--accent-clair": "#e6eefc",
    "--fond-carte": "#ffffff", "--fond-colonne": "#e8eef8", "--bord-doux": "#8fa3c7", "--bord-clair": "#b9c7e0", "--rivet": "#f2b84b",
    "--plaque-haut": "rgba(26,37,71,.96)", "--plaque-bas": "rgba(10,16,38,.97)", "--cadre-haut": "rgba(22,32,64,.94)", "--cadre-bas": "rgba(8,13,32,.96)",
    "--laiton-profond": "#b8801a", "--ombre-bouton": "#4a3408", "--encre-bouton": "#1d1503", "--bareme-fond": "#16203d",
}

# Une voix par personnage, la même du début à la fin du jeu (voix gratuites d'Edge ; `nom` : repli voix du navigateur).
VOIX = {
    "maelle":  {"edge": "fr-FR-DeniseNeural",               "nom": "Denise",   "rate": 0.95, "pitch": 1.0},    # gardienne, posée
    "salome":  {"edge": "fr-FR-VivienneMultilingualNeural", "nom": "Vivienne", "rate": 1.0,  "pitch": 1.0},    # ingénieure, précise
    "nils":    {"edge": "fr-FR-RemyMultilingualNeural",     "nom": "Remy",     "rate": 1.08, "pitch": 1.2},    # jeune gardien, curieux
    "achille": {"edge": "fr-FR-HenriNeural",                "nom": "Henri",    "rate": 0.88, "pitch": 0.9},    # horloger, patient
    "yasmine": {"edge": "fr-FR-EloiseNeural",               "nom": "Eloise",   "rate": 1.05, "pitch": 1.0},    # capitaine, vive et rieuse
}

# Personnage guide de chaque salle (il parle pour toutes les énigmes de la salle).
GUIDES = {1: "maelle", 2: "salome", 3: "nils", 4: "achille", 5: "yasmine"}

# Traits des portraits dessinés (remplacés par les images déposées dans assets/images/personnages/).
PORTRAITS = {
    "maelle":  {"genre": "femme", "coiffure": "longue", "cheveux": "#5a3a22", "peau": "#b8805e", "habit": "#1f3a4d", "lunettes": False},
    "salome":  {"genre": "femme", "coiffure": "courte", "cheveux": "#1a1a1a", "peau": "#dba680", "habit": "#7a2e3a", "lunettes": True},
    "nils":    {"genre": "garçon", "coiffure": "courte", "cheveux": "#a8844a", "peau": "#f0c9ad", "habit": "#2a4a3a", "barbe": False, "lunettes": False},
    "achille": {"genre": "homme", "coiffure": "courte", "cheveux": "#9c9c98", "peau": "#e6c2a6", "habit": "#3a3a52", "barbe": False, "lunettes": True},
    "yasmine": {"genre": "femme", "coiffure": "longue", "cheveux": "#1a1a1a", "peau": "#8a5e42", "habit": "#1b2a4a", "lunettes": False},
}
