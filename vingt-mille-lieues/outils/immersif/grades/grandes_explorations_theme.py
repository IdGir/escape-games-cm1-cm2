"""Identité du jeu « La Caravelle du capitaine » : grades, palette, voix, portraits, direction artistique.
Grades = métiers de bord (les élèves sont les mousses de la Rose des vents, copie d'une caravelle amarrée à Saint-Malo)."""

NOMS = {
    "mousse":     {"nom": "Mousse",       "icone": "🪢", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple, aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Matelot",      "icone": "⚓", "equivalent": "≈ CM1", "profil": "cœur de programme CM1 : repères, instruments, grands voyages"},
    "timonier":   {"nom": "Timonier",     "icone": "🧭", "equivalent": "≈ CM2", "profil": "cœur de programme CM2 : dates exactes, routes, conquêtes, Tordesillas"},
    "lieutenant": {"nom": "Pilote",       "icone": "🔭", "equivalent": "≈ 6ᵉ",  "profil": "raisonnement en deux étapes, documents à croiser, justification par la fiche"},
    "second":     {"nom": "Cartographe",  "icone": "🗺️", "equivalent": "≈ 5ᵉ",  "profil": "synthèse, chiffres et dates, critique du vocabulaire, justification"},
}

# Bois de navire, toile de voile, laiton des instruments, bleu de l'Atlantique.
PALETTE = {
    "--ocean": "#1f4f6b", "--abysse": "#0f2433", "--laiton": "#c9a227", "--laiton-clair": "#f2e2a8", "--laiton-fonce": "#6b4f10",
    "--acajou": "#6b4226", "--acajou-clair": "#8a5a32", "--vertdegris": "#2f6b5a", "--ambre": "#ffe8a8", "--cyan": "#cfe3ee",
    "--papier": "#f6eedb", "--encre": "#2b2118", "--rouge": "#9a3b22", "--vert": "#2f6b4a",
    "--panneau-haut": "#fbf6e9", "--panneau-bas": "#ece0c4", "--accent": "#1f4f6b", "--accent-clair": "#e3eef3",
    "--fond-carte": "#fffdf6", "--fond-colonne": "#efe6d2", "--bord-doux": "#a8916a", "--bord-clair": "#d6c7a6", "--rivet": "#c9a227",
    "--plaque-haut": "rgba(31,79,107,.96)", "--plaque-bas": "rgba(15,36,51,.97)", "--cadre-haut": "rgba(75,48,28,.94)", "--cadre-bas": "rgba(45,28,16,.96)",
    "--laiton-profond": "#9a7a1c", "--ombre-bouton": "#3b2a08", "--encre-bouton": "#1f1404", "--bareme-fond": "#1f4f6b",
}

VOIX = {
    "amaury":  {"edge": "fr-FR-HenriNeural",                "nom": "Henri",    "rate": 1.0,  "pitch": 1.0},    # guide, chaleureux
    "rosa":    {"edge": "fr-FR-DeniseNeural",               "nom": "Denise",   "rate": 0.97, "pitch": 1.02},   # cartographe, précise
    "bastien": {"edge": "fr-BE-GerardNeural",               "nom": "Gérard",   "rate": 0.94, "pitch": 0.92},   # capitaine, posé
    "itzel":   {"edge": "fr-FR-VivienneMultilingualNeural", "nom": "Vivienne", "rate": 0.96, "pitch": 1.04},   # conteuse, calme
    "simon":   {"edge": "fr-FR-RemyMultilingualNeural",     "nom": "Remy",     "rate": 1.06, "pitch": 1.14},   # mousse, enjoué
}

GUIDES = {1: "amaury", 2: "rosa", 3: "bastien", 4: "itzel", 5: "simon"}

PORTRAITS = {
    "amaury":  {"genre": "homme", "coiffure": "courte", "cheveux": "#5a3a22", "peau": "#e8c4a6", "habit": "#7a4e2a", "barbe": True, "lunettes": False},
    "rosa":    {"genre": "femme", "coiffure": "longue", "cheveux": "#2b1a10", "peau": "#d9a882", "habit": "#2f6b5a", "lunettes": True},
    "bastien": {"genre": "homme", "coiffure": "courte", "cheveux": "#9a9a9a", "peau": "#f0c9ad", "habit": "#1f4f6b", "barbe": True, "lunettes": False},
    "itzel":   {"genre": "femme", "coiffure": "longue", "cheveux": "#141010", "peau": "#a8734e", "habit": "#9a3b22", "lunettes": False},
    "simon":   {"genre": "homme", "coiffure": "courte", "cheveux": "#c98a3a", "peau": "#f3d9c4", "habit": "#c9a227", "barbe": False, "lunettes": False},
}

STYLE_VISUEL = ("Photographie photoréaliste de cinéma, objectif 35 mm, réplique d'une caravelle du XVe siècle amarrée dans un port breton, "
                "bois patiné, cordages, laiton, lumière dorée de fin d'après-midi, aucune inscription lisible, grain fin.")
EPOQUE = ("Univers contemporain : un festival de la mer à Saint-Malo, à bord d'une copie de caravelle. Le journal de bord lu aux visiteurs "
          "raconte les explorations et les conquêtes des XVe et XVIe siècles. Aucune scène de violence, aucune personne réelle.")
