"""Identité du jeu « L'Observatoire des volcans » : grades, palette, voix, portraits, direction artistique.
Grades = étapes du parcours d'un scientifique de la station d'observation des Hauts (La Réunion, station inventée)."""

NOMS = {
    "mousse":     {"nom": "Visiteur de l'observatoire",  "icone": "🎒", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple (volcan, séisme, plaque, bons réflexes), aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Apprenti géologue",            "icone": "🔎", "equivalent": "≈ CM1", "profil": "repères : activité interne et externe, croûte, manteau, noyau, parties d'un volcan, foyer et épicentre, bons réflexes"},
    "timonier":   {"nom": "Observateur",                  "icone": "🌋", "equivalent": "≈ CM2", "profil": "cœur de programme CM2 : manifestations de l'activité terrestre, risque naturel, prévention et protection, dates et chiffres exacts"},
    "lieutenant": {"nom": "Volcanologue",                 "icone": "🧭", "equivalent": "≈ 6ᵉ",  "profil": "frontières de plaques, types d'éruptions, ondes et magnitude, justification par une phrase de la fiche"},
    "second":     {"nom": "Directeur de l'observatoire",  "icone": "🛰️", "equivalent": "≈ 5ᵉ",  "profil": "raisonnement en plusieurs étapes, limites d'un modèle, comparaisons de magnitudes, chaîne d'alerte, justification"},
}

# Basalte sombre, orange de la lave, bleu de l'océan Indien, vert des hauts.
PALETTE = {
    "--ocean": "#1f4e79", "--abysse": "#141a22", "--laiton": "#e8873a", "--laiton-clair": "#f8d2ac", "--laiton-fonce": "#7a3a12",
    "--acajou": "#4a3a33", "--acajou-clair": "#6e5a50", "--vertdegris": "#2f6f5a", "--ambre": "#fbe0c2", "--cyan": "#d4e6f1",
    "--papier": "#f7f3ee", "--encre": "#221a17", "--rouge": "#b03a2e", "--vert": "#2f7a4a",
    "--panneau-haut": "#fcfaf7", "--panneau-bas": "#ebe4dc", "--accent": "#1f4e79", "--accent-clair": "#dde9f3",
    "--fond-carte": "#ffffff", "--fond-colonne": "#f1ebe4", "--bord-doux": "#a8988c", "--bord-clair": "#d9cfc6", "--rivet": "#9b5a2a",
    "--plaque-haut": "rgba(31,78,121,.96)", "--plaque-bas": "rgba(20,26,34,.97)", "--cadre-haut": "rgba(74,58,51,.94)", "--cadre-bas": "rgba(34,26,23,.96)",
    "--laiton-profond": "#c0651f", "--ombre-bouton": "#3a1a06", "--encre-bouton": "#1c0f04", "--bareme-fond": "#1f4e79",
}

VOIX = {
    "ines":   {"edge": "fr-FR-DeniseNeural",               "nom": "Denise",   "rate": 0.98, "pitch": 1.0},    # géologue, posée
    "noe":    {"edge": "fr-FR-RemyMultilingualNeural",     "nom": "Rémy",     "rate": 1.03, "pitch": 1.0},    # géophysicien, enthousiaste
    "maeva":  {"edge": "fr-FR-VivienneMultilingualNeural", "nom": "Vivienne", "rate": 0.98, "pitch": 1.0},    # volcanologue, calme
    "samuel": {"edge": "fr-FR-HenriNeural",                "nom": "Henri",    "rate": 0.97, "pitch": 0.98},   # sismologue, méthodique
    "adele":  {"edge": "fr-BE-CharlineNeural",             "nom": "Charline", "rate": 1.02, "pitch": 1.0},    # pompière, énergique
}

GUIDES = {1: "ines", 2: "noe", 3: "maeva", 4: "samuel", 5: "adele"}

PORTRAITS = {
    "ines":   {"genre": "femme", "coiffure": "longue", "cheveux": "#2a1c14", "peau": "#c98e64", "habit": "#1f4e79", "lunettes": True},
    "noe":    {"genre": "homme", "coiffure": "courte", "cheveux": "#8a5a2b", "peau": "#f0cdb3", "habit": "#2f6f5a", "barbe": False, "lunettes": False},
    "maeva":  {"genre": "femme", "coiffure": "longue", "cheveux": "#141010", "peau": "#9a6342", "habit": "#e8873a", "lunettes": False},
    "samuel": {"genre": "homme", "coiffure": "courte", "cheveux": "#141010", "peau": "#5e3a24", "habit": "#4a3a33", "barbe": True, "lunettes": True},
    "adele":  {"genre": "femme", "coiffure": "courte", "cheveux": "#6b4a2b", "peau": "#e8bfa0", "habit": "#b03a2e", "lunettes": False},
}

STYLE_VISUEL = ("Photographie photoréaliste de cinéma, objectif 35 mm, île de La Réunion, hauts de l'île au-dessus de la mer de nuages, station d'observation "
                "scientifique moderne, anciennes coulées de lave noire, végétation tropicale d'altitude, lumière claire du matin, aucune inscription lisible, grain fin.")
EPOQUE = ("Univers contemporain : la station d'observation des Hauts (inventée) au-dessus du village inventé de Bois-Clair, sur l'île de La Réunion : galerie "
          "d'exposition, salle des cartes, sentier au bord de l'enclos du cratère, salle des sismographes, centre de secours. Aucune personne réelle, aucune catastrophe montrée.")
