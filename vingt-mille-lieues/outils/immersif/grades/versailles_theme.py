"""Identité du jeu « De l'édit de Nantes à Versailles » : grades, palette, voix, portraits, direction artistique."""

# Noms de grades : métiers liés au château et à l'écrit ; aucune connotation religieuse, nobiliaire ou de servitude.
NOMS = {
    "mousse":     {"nom": "Jardinier",   "icone": "🌳", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple, aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Imprimeur",   "icone": "🖨️", "equivalent": "≈ CM1", "profil": "cœur de programme CM1"},
    "timonier":   {"nom": "Secrétaire",  "icone": "🖋️", "equivalent": "≈ CM2", "profil": "cœur de programme CM2, plus d'éléments, vocabulaire précis"},
    "lieutenant": {"nom": "Chroniqueur", "icone": "📜", "equivalent": "≈ 6ᵉ",  "profil": "raisonnement en deux étapes, documents à croiser, justification"},
    "second":     {"nom": "Historien",   "icone": "🏛️", "equivalent": "≈ 5ᵉ",  "profil": "synthèse, données chiffrées, pièges de logique, justification"},
}

# Versailles : prune, champagne et marbre clair.
PALETTE = {
    "--ocean": "#33263d", "--abysse": "#17101c", "--laiton": "#cfa86a", "--laiton-clair": "#f3e0b5", "--laiton-fonce": "#6e5528",
    "--acajou": "#43304f", "--acajou-clair": "#61486f", "--vertdegris": "#3f5a52", "--ambre": "#ffd98a", "--cyan": "#cdb8e8",
    "--papier": "#f8f3ea", "--encre": "#281b2e", "--rouge": "#a3261b", "--vert": "#2e7d4f",
    "--panneau-haut": "#fbf7ee", "--panneau-bas": "#ece3d2", "--accent": "#7b3f8c", "--accent-clair": "#f1e6f5",
    "--fond-carte": "#fffdf8", "--fond-colonne": "#efe6d6", "--bord-doux": "#b9a58a", "--bord-clair": "#d8c9ad", "--rivet": "#cfa86a",
    "--plaque-haut": "rgba(51,38,61,.96)", "--plaque-bas": "rgba(23,16,28,.97)", "--cadre-haut": "rgba(45,33,55,.94)", "--cadre-bas": "rgba(20,13,25,.96)",
    "--laiton-profond": "#a47c35", "--ombre-bouton": "#4a3814", "--encre-bouton": "#241606", "--bareme-fond": "#33263d",
}

VOIX = {
    "suzanne":  {"edge": "fr-FR-DeniseNeural",               "nom": "Denise",   "rate": 0.95, "pitch": 0.97},    # imprimeuse courageuse, voix calme
    "mathurin": {"edge": "fr-FR-HenriNeural",                "nom": "Henri",    "rate": 1.0,  "pitch": 0.95},    # boulanger chaleureux
    "margot":   {"edge": "fr-FR-EloiseNeural",               "nom": "Eloise",   "rate": 1.08, "pitch": 1.05},    # aide-jardinière malicieuse, 11 ans
    "isabeau":  {"edge": "fr-FR-VivienneMultilingualNeural", "nom": "Vivienne", "rate": 0.95, "pitch": 1.0},     # dame de la cour, ironique
    "gabriel":  {"edge": "fr-FR-RemyMultilingualNeural",     "nom": "Remy",     "rate": 1.05, "pitch": 1.2},     # apprenti secrétaire de 12 ans, intimidé
}

GUIDES = {1: "suzanne", 2: "mathurin", 3: "margot", 4: "isabeau", 5: "gabriel"}

PORTRAITS = {
    "suzanne":  {"genre": "femme", "coiffure": "longue", "cheveux": "#5a3a22", "peau": "#e6c2a6", "habit": "#3a3a52", "lunettes": False},
    "mathurin": {"genre": "homme", "coiffure": "courte", "cheveux": "#2a1c14", "peau": "#dba680", "habit": "#e8e4da", "barbe": True, "lunettes": False},
    "margot":   {"genre": "fille", "coiffure": "longue", "cheveux": "#a04a22", "peau": "#f0c9ad", "habit": "#4a5a2a", "lunettes": False},
    "isabeau":  {"genre": "femme", "coiffure": "longue", "cheveux": "#1a1a1a", "peau": "#e6c2a6", "habit": "#7b3f8c", "lunettes": False},
    "gabriel":  {"genre": "garçon", "coiffure": "courte", "cheveux": "#5a3a22", "peau": "#f0c9ad", "habit": "#2a4a6a", "barbe": False, "lunettes": False},
}

STYLE_VISUEL = ("Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance du Grand Siècle, lumière dorée contre ombres prune, "
                "marbre, miroirs, boiseries dorées, jardins géométriques, détails d'époque lisibles (sans inscriptions), grain fin, profondeur de champ.")
EPOQUE = "1598 puis 1682-1715 : une imprimerie et une rue de la fin des guerres de Religion, puis les jardins, la chambre et le cabinet du Conseil à Versailles."
