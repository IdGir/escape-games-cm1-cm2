"""Identité du jeu « L'Atelier de l'inventeur » : grades, palette, voix, portraits, direction artistique."""

NOMS = {
    "mousse":     {"nom": "Bricoleur",  "icone": "🔧", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple, aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Monteur",    "icone": "🔩", "equivalent": "≈ CM1", "profil": "cœur de programme CM1"},
    "timonier":   {"nom": "Mécanicien", "icone": "⚙️", "equivalent": "≈ CM2", "profil": "cœur de programme CM2, plus d'éléments, vocabulaire précis"},
    "lieutenant": {"nom": "Ingénieur",  "icone": "📐", "equivalent": "≈ 6ᵉ",  "profil": "raisonnement en deux étapes, documents à croiser, justification"},
    "second":     {"nom": "Inventeur",  "icone": "💡", "equivalent": "≈ 5ᵉ",  "profil": "synthèse, données chiffrées, pièges de logique, justification"},
}

# Atelier : acier bleuté et cuivre.
PALETTE = {
    "--ocean": "#26323b", "--abysse": "#11181d", "--laiton": "#c0732a", "--laiton-clair": "#f0b98a", "--laiton-fonce": "#5a2f0c",
    "--acajou": "#2c3a44", "--acajou-clair": "#46596a", "--vertdegris": "#34504a", "--ambre": "#ffc46b", "--cyan": "#8fd0e8",
    "--papier": "#eef1f2", "--encre": "#1b2328", "--rouge": "#b3361f", "--vert": "#2e7d4f",
    "--panneau-haut": "#f2f5f6", "--panneau-bas": "#d8dfe2", "--accent": "#1f6f8b", "--accent-clair": "#e1f0f5",
    "--fond-carte": "#fbfcfc", "--fond-colonne": "#e4eaed", "--bord-doux": "#93a7b1", "--bord-clair": "#bccad1", "--rivet": "#c0732a",
    "--plaque-haut": "rgba(38,50,59,.96)", "--plaque-bas": "rgba(17,24,29,.97)", "--cadre-haut": "rgba(34,46,55,.94)", "--cadre-bas": "rgba(14,20,24,.96)",
    "--laiton-profond": "#8f4f14", "--ombre-bouton": "#3e1f06", "--encre-bouton": "#1d0d03", "--bareme-fond": "#2c3a44",
}

VOIX = {
    "zoe":      {"edge": "fr-FR-EloiseNeural",               "nom": "Eloise",   "rate": 1.08, "pitch": 1.1},     # apprentie ingénieure de 11 ans
    "awa":      {"edge": "fr-FR-DeniseNeural",               "nom": "Denise",   "rate": 1.05, "pitch": 1.0},     # ouvrière efficace
    "marcel":   {"edge": "fr-FR-HenriNeural",                "nom": "Henri",    "rate": 0.9,  "pitch": 0.88},    # réparateur bourru mais bienveillant
    "eleonore": {"edge": "fr-FR-VivienneMultilingualNeural", "nom": "Vivienne", "rate": 0.95, "pitch": 1.0},     # inventrice rêveuse et précise
}

GUIDES = {1: "zoe", 2: "awa", 3: "awa", 4: "marcel", 5: "eleonore"}

PORTRAITS = {
    "zoe":      {"genre": "fille", "coiffure": "longue", "cheveux": "#a04a22", "peau": "#f0c9ad", "habit": "#1f6f8b", "lunettes": True},
    "awa":      {"genre": "femme", "coiffure": "courte", "cheveux": "#1a1a1a", "peau": "#8a5e42", "habit": "#c0732a", "lunettes": False},
    "marcel":   {"genre": "homme", "coiffure": "chauve", "cheveux": "#9c9c98", "peau": "#dba680", "habit": "#3a3a52", "barbe": True, "lunettes": False},
    "eleonore": {"genre": "femme", "coiffure": "longue", "cheveux": "#5a3a22", "peau": "#e6c2a6", "habit": "#2a4a3a", "lunettes": False},
}

STYLE_VISUEL = ("Photographie photoréaliste de cinéma, appareil plein format, objectif 35 mm, lumière naturelle crédible, ambiance d'atelier de bricolage chaleureux et bien rangé, acier, cuivre, bois et verre, "
                "lumière de lampe d'établi contre ombres bleutées, outils et pièces mécaniques lisibles (sans inscriptions), grain fin, profondeur de champ.")
EPOQUE = "Univers contemporain : un atelier de réparation de vélos et de fabrication d'objets du quotidien."
