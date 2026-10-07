"""Identité du jeu « La Station météo disparue » : grades, palette, voix, portraits, direction artistique."""

NOMS = {
    "mousse":     {"nom": "Observateur",   "icone": "🌤️", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple, aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Releveur",      "icone": "🌡️", "equivalent": "≈ CM1", "profil": "cœur de programme CM1"},
    "timonier":   {"nom": "Météorologue",  "icone": "🌬️", "equivalent": "≈ CM2", "profil": "cœur de programme CM2, plus d'éléments, vocabulaire précis"},
    "lieutenant": {"nom": "Prévisionniste", "icone": "📡", "equivalent": "≈ 6ᵉ",  "profil": "raisonnement en deux étapes, documents à croiser, justification"},
    "second":     {"nom": "Climatologue",  "icone": "🌍", "equivalent": "≈ 5ᵉ",  "profil": "synthèse, données chiffrées, pièges de logique, justification"},
}

# Ciel et orage : bleus clairs, ardoise, éclair orangé.
PALETTE = {
    "--ocean": "#243746", "--abysse": "#0f1c26", "--laiton": "#3d9be9", "--laiton-clair": "#b5dcff", "--laiton-fonce": "#14507f",
    "--acajou": "#1f3345", "--acajou-clair": "#35516b", "--vertdegris": "#2f5560", "--ambre": "#ffd166", "--cyan": "#bfe7ff",
    "--papier": "#f2f7fb", "--encre": "#14212b", "--rouge": "#c0392b", "--vert": "#2e8b57",
    "--panneau-haut": "#eaf4fb", "--panneau-bas": "#cfe4f3", "--accent": "#c0502a", "--accent-clair": "#fbe7dd",
    "--fond-carte": "#ffffff", "--fond-colonne": "#dcebf6", "--bord-doux": "#8fb0c9", "--bord-clair": "#b9d2e4", "--rivet": "#3d9be9",
    "--plaque-haut": "rgba(36,55,70,.96)", "--plaque-bas": "rgba(15,28,38,.97)", "--cadre-haut": "rgba(32,50,64,.94)", "--cadre-bas": "rgba(13,24,32,.96)",
    "--laiton-profond": "#2477b8", "--ombre-bouton": "#0e3a5e", "--encre-bouton": "#06223a", "--bareme-fond": "#1f3345",
}

VOIX = {
    "vasseur": {"edge": "fr-FR-VivienneMultilingualNeural", "nom": "Vivienne", "rate": 0.95, "pitch": 1.0},    # prévisionniste rassurante
    "tiago":   {"edge": "fr-FR-HenriNeural",                "nom": "Henri",    "rate": 1.0,  "pitch": 1.0},    # technicien pragmatique
    "lina":    {"edge": "fr-FR-EloiseNeural",               "nom": "Eloise",   "rate": 1.05, "pitch": 1.05},   # élève de CM2 sérieuse
    "keita":   {"edge": "fr-FR-RemyMultilingualNeural",     "nom": "Remy",     "rate": 0.92, "pitch": 0.9},    # capitaine du vent
}

GUIDES = {1: "vasseur", 2: "keita", 3: "tiago", 4: "lina", 5: "vasseur"}

PORTRAITS = {
    "vasseur": {"genre": "femme", "coiffure": "courte", "cheveux": "#9c9c98", "peau": "#e6c2a6", "habit": "#3a3a52", "lunettes": True},
    "tiago":   {"genre": "homme", "coiffure": "courte", "cheveux": "#2a1c14", "peau": "#c08a64", "habit": "#2a5a8a", "barbe": False, "lunettes": False},
    "lina":    {"genre": "fille", "coiffure": "longue", "cheveux": "#1a1a1a", "peau": "#b8805e", "habit": "#c0502a", "lunettes": False},
    "keita":   {"genre": "homme", "coiffure": "chauve", "cheveux": "#1a1a1a", "peau": "#6e4630", "habit": "#1b2a4a", "barbe": True, "lunettes": False},
}

STYLE_VISUEL = ("Peinture numérique semi-réaliste de cinéma, ambiance de petite station météo d'école après un orage, ciel contrasté, lumière rasante contre ombres bleutées, "
                "instruments de mesure lisibles (sans inscriptions), herbe, abri blanc, mât et pluviomètre, grain fin, profondeur de champ.")
EPOQUE = "Univers contemporain : la station météo d'une école, après un orage qui a dérangé les instruments."
