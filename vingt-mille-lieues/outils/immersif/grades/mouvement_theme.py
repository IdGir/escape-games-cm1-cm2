"""Identité du jeu « Le Grand Prix de l'observatoire » : grades, palette, voix, portraits, direction artistique."""

# Grades : rôles du Grand Prix, du plus simple au plus expert ; neutres (ni militaires, ni religieux, ni héréditaires).
NOMS = {
    "mousse":     {"nom": "Apprenti",              "icone": "🚩", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple, aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Commissaire",           "icone": "⏱️", "equivalent": "≈ CM1", "profil": "cœur de programme CM1"},
    "timonier":   {"nom": "Commissaire en chef",   "icone": "🏁", "equivalent": "≈ CM2", "profil": "cœur de programme CM2 : conversions, Terre et Soleil, observateur"},
    "lieutenant": {"nom": "Directeur de course",   "icone": "📏", "equivalent": "≈ 6ᵉ",  "profil": "raisonnement en deux étapes, comparaison des vitesses, justification"},
    "second":     {"nom": "Astronome du Grand Prix", "icone": "🔭", "equivalent": "≈ 5ᵉ", "profil": "synthèse, données chiffrées, pièges de logique, justification"},
}

# Plateau herbeux au matin, coupole blanche : bleu nuit, rouge course, vert piste, touches or.
PALETTE = {
    "--ocean": "#1d2f52", "--abysse": "#0e1a33", "--laiton": "#d9a23a", "--laiton-clair": "#f6dc9c", "--laiton-fonce": "#6e4a10",
    "--acajou": "#23406e", "--acajou-clair": "#34558a", "--vertdegris": "#2e6a4a", "--ambre": "#ffd58a", "--cyan": "#9fdcf2",
    "--papier": "#f6f7f2", "--encre": "#16212a", "--rouge": "#b3361f", "--vert": "#2d7d55",
    "--panneau-haut": "#f7f8f4", "--panneau-bas": "#e3e9ef", "--accent": "#23406e", "--accent-clair": "#e4ebf6",
    "--fond-carte": "#ffffff", "--fond-colonne": "#e8edf4", "--bord-doux": "#93a3bd", "--bord-clair": "#c3cfde", "--rivet": "#d9a23a",
    "--plaque-haut": "rgba(29,47,82,.96)", "--plaque-bas": "rgba(14,26,51,.97)", "--cadre-haut": "rgba(26,42,74,.94)", "--cadre-bas": "rgba(12,22,44,.96)",
    "--laiton-profond": "#a8761f", "--ombre-bouton": "#4a3008", "--encre-bouton": "#1f1404", "--bareme-fond": "#23406e",
}

# Une voix par personnage, la même du début à la fin (voix gratuites d'Edge ; `nom` : repli voix du navigateur).
VOIX = {
    "margaux": {"edge": "fr-FR-DeniseNeural",               "nom": "Denise",   "rate": 1.0,  "pitch": 1.0},    # commissaire, nette
    "yanis":   {"edge": "fr-FR-RemyMultilingualNeural",     "nom": "Remy",     "rate": 1.06, "pitch": 1.08},   # pilote, enjoué
    "salome":  {"edge": "fr-FR-EloiseNeural",               "nom": "Eloise",   "rate": 1.04, "pitch": 1.05},   # cycliste, vive
    "leonie":  {"edge": "fr-FR-VivienneMultilingualNeural", "nom": "Vivienne", "rate": 0.95, "pitch": 1.0},    # astronome, calme
    "hugo":    {"edge": "fr-FR-HenriNeural",                "nom": "Henri",    "rate": 0.94, "pitch": 0.92},   # contrôleur, chaleureux
}

# Personnage guide de chaque salle (il parle pour toutes les énigmes de la salle).
GUIDES = {1: "margaux", 2: "yanis", 3: "salome", 4: "leonie", 5: "hugo"}

# Traits des portraits dessinés (remplacés par les images déposées dans assets/images/personnages/).
PORTRAITS = {
    "margaux": {"genre": "femme", "coiffure": "longue", "cheveux": "#6b4226", "peau": "#f0c9ad", "habit": "#f2e33a", "lunettes": False},
    "yanis":   {"genre": "homme", "coiffure": "courte", "cheveux": "#1c120a", "peau": "#c99a74", "habit": "#c0392b", "barbe": False, "lunettes": False},
    "salome":  {"genre": "femme", "coiffure": "courte", "cheveux": "#1a1a1a", "peau": "#7a4e34", "habit": "#2e8b57", "lunettes": False},
    "leonie":  {"genre": "femme", "coiffure": "longue", "cheveux": "#b5541c", "peau": "#f3d9c4", "habit": "#23406e", "lunettes": True},
    "hugo":    {"genre": "homme", "coiffure": "courte", "cheveux": "#7a7a7a", "peau": "#f0c9ad", "habit": "#1d2f52", "barbe": True, "lunettes": False},
}

STYLE_VISUEL = ("Photographie photoréaliste de cinéma, objectif 35 mm, lumière claire d'un matin de printemps sur un plateau herbeux, "
                "coupole blanche d'observatoire, piste de course, plots orange, drapeaux à damier, couleurs franches, aucune inscription lisible, grain fin.")
EPOQUE = "Univers contemporain imaginaire : un plateau au pied d'un petit observatoire, où l'école organise chaque printemps un Grand Prix de véhicules sans moteur."
