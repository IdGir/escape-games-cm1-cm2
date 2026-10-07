"""Identité du jeu « Le Sceau de la République » : grades, palette, voix, portraits, direction artistique."""

# Noms de grades : rôles civiques neutres (aucun parti, aucune religion).
NOMS = {
    "mousse":     {"nom": "Électeur",    "icone": "🗳️", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple, aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Délégué",     "icone": "📋", "equivalent": "≈ CM1", "profil": "cœur de programme CM1"},
    "timonier":   {"nom": "Rapporteur",  "icone": "📝", "equivalent": "≈ CM2", "profil": "cœur de programme CM2, plus d'éléments, vocabulaire précis"},
    "lieutenant": {"nom": "Juriste",     "icone": "⚖️", "equivalent": "≈ 6ᵉ",  "profil": "raisonnement en deux étapes, documents à croiser, justification"},
    "second":     {"nom": "Constituant", "icone": "📜", "equivalent": "≈ 5ᵉ",  "profil": "synthèse, données chiffrées, pièges de logique, justification"},
}

# République : bleu de France, ivoire et rouge sobre.
PALETTE = {
    "--ocean": "#1d2a4a", "--abysse": "#0c1226", "--laiton": "#c9302c", "--laiton-clair": "#f2a6a2", "--laiton-fonce": "#6a1512",
    "--acajou": "#1d2a4a", "--acajou-clair": "#34457a", "--vertdegris": "#2f4a5a", "--ambre": "#ffd27a", "--cyan": "#b9cdfa",
    "--papier": "#f6f4ee", "--encre": "#141a2e", "--rouge": "#b3261b", "--vert": "#2e7d4f",
    "--panneau-haut": "#f7f6f1", "--panneau-bas": "#e4e2d8", "--accent": "#1d3f8f", "--accent-clair": "#e3e9fa",
    "--fond-carte": "#ffffff", "--fond-colonne": "#ebe9df", "--bord-doux": "#a4a89a", "--bord-clair": "#c8cabb", "--rivet": "#c9302c",
    "--plaque-haut": "rgba(29,42,74,.96)", "--plaque-bas": "rgba(12,18,38,.97)", "--cadre-haut": "rgba(26,38,68,.94)", "--cadre-bas": "rgba(10,15,32,.96)",
    "--laiton-profond": "#9b1f1b", "--ombre-bouton": "#4a0d0b", "--encre-bouton": "#2a0605", "--bareme-fond": "#1d2a4a",
}

VOIX = {
    "berthier": {"edge": "fr-FR-HenriNeural",           "nom": "Henri",  "rate": 0.88, "pitch": 0.88},     # gardien-archiviste solennel
    "nour":     {"edge": "fr-FR-EloiseNeural",           "nom": "Eloise", "rate": 1.1,  "pitch": 1.1},      # déléguée de classe, 10 ans
    "ferrand":  {"edge": "fr-FR-DeniseNeural",           "nom": "Denise", "rate": 1.05, "pitch": 1.0},      # députée passionnée
    "sylla":    {"edge": "fr-FR-RemyMultilingualNeural", "nom": "Remy",   "rate": 0.95, "pitch": 0.95},     # juriste précis
}

GUIDES = {1: "berthier", 2: "sylla", 3: "ferrand", 4: "ferrand", 5: "sylla"}

PORTRAITS = {
    "berthier": {"genre": "homme", "coiffure": "chauve", "cheveux": "#9c9c98", "peau": "#e6c2a6", "habit": "#3a3a52", "barbe": True, "lunettes": True},
    "nour":     {"genre": "fille", "coiffure": "longue", "cheveux": "#1a1a1a", "peau": "#b8805e", "habit": "#1d3f8f", "lunettes": False},
    "ferrand":  {"genre": "femme", "coiffure": "courte", "cheveux": "#5a3a22", "peau": "#dba680", "habit": "#c9302c", "lunettes": False},
    "sylla":    {"genre": "homme", "coiffure": "courte", "cheveux": "#1a1a1a", "peau": "#6e4630", "habit": "#1d2a4a", "barbe": False, "lunettes": True},
}

STYLE_VISUEL = ("Peinture numérique semi-réaliste de cinéma, ambiance institutionnelle solennelle et lumineuse, pierre de taille, boiseries, drapeaux et dorures sobres, "
                "lumière de fenêtre haute contre ombres bleutées, détails architecturaux lisibles (sans inscriptions), grain fin, profondeur de champ.")
EPOQUE = "Univers contemporain : le Palais-Royal, la salle des textes, l'hémicycle, le Sénat et la salle des séances du Conseil constitutionnel."
