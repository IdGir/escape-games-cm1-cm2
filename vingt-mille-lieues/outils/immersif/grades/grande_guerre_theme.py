"""Identité du jeu « Les Lettres du poilu » : grades, palette, voix, portraits, direction artistique.
Grades = étapes du parcours d'un historien de la mémoire (les élèves enquêtent sur les lettres de la boîte de Jeanne).
SUJET SENSIBLE : ton du souvenir, aucun détail violent."""

NOMS = {
    "mousse":     {"nom": "Lecteur",               "icone": "📖", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple (avant, pendant, après la guerre ; le front, l'arrière ; se souvenir), aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Apprenti historien",    "icone": "✉️", "equivalent": "≈ CM1", "profil": "repères : causes, mobilisation, tranchées, arrière, armistice, monument aux morts"},
    "timonier":   {"nom": "Historien",             "icone": "🗂️", "equivalent": "≈ CM2", "profil": "cœur de programme CM2 : dates exactes, chiffres officiels, traité de Versailles, début de la montée des extrêmes"},
    "lieutenant": {"nom": "Archiviste",            "icone": "🔎", "equivalent": "≈ 6ᵉ",  "profil": "lecture critique des documents, justification par la fiche, causes et conséquences enchaînées"},
    "second":     {"nom": "Gardien de la mémoire", "icone": "🕯️", "equivalent": "≈ 5ᵉ",  "profil": "raisonnement en plusieurs étapes, calculs de durées, mise en relation des faits, justification"},
}

# Bleu horizon, kaki, pierre du monument, coquelicot (rouge sourd), papier ancien.
PALETTE = {
    "--ocean": "#3d4f6b", "--abysse": "#1b222e", "--laiton": "#c9a45c", "--laiton-clair": "#efe0bd", "--laiton-fonce": "#6e5528",
    "--acajou": "#5e4a36", "--acajou-clair": "#87705a", "--vertdegris": "#5d6b4a", "--ambre": "#f1e3c4", "--cyan": "#d9e2ec",
    "--papier": "#f6f1e6", "--encre": "#2a2620", "--rouge": "#9e3a32", "--vert": "#4f6b3a",
    "--panneau-haut": "#fbf8f1", "--panneau-bas": "#e8e1d2", "--accent": "#3d4f6b", "--accent-clair": "#e3e8ef",
    "--fond-carte": "#ffffff", "--fond-colonne": "#eeeae0", "--bord-doux": "#a49b8a", "--bord-clair": "#d8d1c2", "--rivet": "#8a6d3b",
    "--plaque-haut": "rgba(61,79,107,.96)", "--plaque-bas": "rgba(27,34,46,.97)", "--cadre-haut": "rgba(94,74,54,.94)", "--cadre-bas": "rgba(48,38,28,.96)",
    "--laiton-profond": "#a8853f", "--ombre-bouton": "#3a2e14", "--encre-bouton": "#1d1708", "--bareme-fond": "#3d4f6b",
}

VOIX = {
    "jeanne":   {"edge": "fr-FR-EloiseNeural",                "nom": "Eloise",   "rate": 1.0,  "pitch": 1.04},   # petite sœur, 10 ans, sérieuse
    "louis":    {"edge": "fr-FR-HenriNeural",                 "nom": "Henri",    "rate": 0.96, "pitch": 1.0},    # soldat, voix posée, tendre
    "marcelle": {"edge": "fr-FR-DeniseNeural",                "nom": "Denise",   "rate": 1.0,  "pitch": 1.0},    # ouvrière, énergique
    "odette":   {"edge": "fr-FR-VivienneMultilingualNeural",  "nom": "Vivienne", "rate": 0.97, "pitch": 1.0},    # infirmière, douce
    "emile":    {"edge": "fr-FR-RemyMultilingualNeural",      "nom": "Rémy",     "rate": 0.95, "pitch": 0.97},   # maire, grave
}

GUIDES = {1: "jeanne", 2: "louis", 3: "marcelle", 4: "odette", 5: "emile"}

PORTRAITS = {
    "jeanne":   {"genre": "femme", "coiffure": "longue", "cheveux": "#6b4a2b", "peau": "#f0cdb3", "habit": "#3d4f6b", "lunettes": False},
    "louis":    {"genre": "homme", "coiffure": "courte", "cheveux": "#3a2416", "peau": "#e8c0a0", "habit": "#7f93ad", "barbe": False, "lunettes": False},
    "marcelle": {"genre": "femme", "coiffure": "longue", "cheveux": "#2a1c14", "peau": "#d9a47e", "habit": "#5e4a36", "lunettes": False},
    "odette":   {"genre": "femme", "coiffure": "courte", "cheveux": "#9b7a4e", "peau": "#efc9ac", "habit": "#f6f1e6", "lunettes": True},
    "emile":    {"genre": "homme", "coiffure": "courte", "cheveux": "#b9b2a6", "peau": "#efc9ac", "habit": "#2a2620", "barbe": True, "lunettes": True},
}

STYLE_VISUEL = ("Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France de 1914-1922, village de Bourgogne, "
                "couleurs sourdes et douces, lumière naturelle, atmosphère de souvenir et de recueillement, aucune inscription lisible, grain fin.")
EPOQUE = ("France de 1914 à 1922 : le village inventé de Vaux-les-Tilleuls (Côte-d'Or), sa place et sa mairie, un abri de tranchée calme, "
          "une usine d'obus, une salle de classe devenue hôpital, le monument aux morts. Aucune personne réelle, aucun blessé visible, aucun combat, aucune explosion.")
