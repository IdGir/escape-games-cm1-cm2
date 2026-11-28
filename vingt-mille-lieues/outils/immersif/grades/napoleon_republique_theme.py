"""Identité du jeu « Le Testament de l'Empereur » : grades, palette, voix, portraits, direction artistique.
Grades = étapes d'un visiteur du musée de l'Armée devenu conservateur (les élèves ouvrent le coffre du testament).
Bilan nuancé de l'Empire ; personnages inventés ; les personnes réelles ne parlent jamais."""

NOMS = {
    "mousse":     {"nom": "Jeune visiteur",   "icone": "🎟️", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple (général, empereur, roi, République ; avant, après), aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Guide du musée",   "icone": "🗺️", "equivalent": "≈ CM1", "profil": "repères : Toulon, le coup d'État de 1799, le sacre de 1804, Austerlitz, Waterloo, Code civil, symboles de la République"},
    "timonier":   {"nom": "Enquêteur d'histoire", "icone": "🔎", "equivalent": "≈ CM2", "profil": "cœur de programme : dates exactes, Consulat et Concordat, institutions de 1800-1804, bilan de l'Empire, article 2 de la Constitution"},
    "lieutenant": {"nom": "Archiviste",       "icone": "📜", "equivalent": "≈ 6ᵉ",  "profil": "lecture critique d'une œuvre et d'une carte, justification par la fiche, causes et conséquences enchaînées"},
    "second":     {"nom": "Conservateur",     "icone": "🏛️", "equivalent": "≈ 5ᵉ",  "profil": "raisonnement en plusieurs étapes, nuances (héritage et part d'ombre, propagande), mise en relation de l'Empire et de la République, justification"},
}

# Bleu impérial, or des abeilles, rouge du manteau du sacre, pierre des Invalides, papier ancien.
PALETTE = {
    "--ocean": "#2f4a7a", "--abysse": "#16223a", "--laiton": "#c9a24a", "--laiton-clair": "#f1e4bf", "--laiton-fonce": "#6e5420",
    "--acajou": "#6a3a2a", "--acajou-clair": "#8e5f4a", "--vertdegris": "#4f6a5c", "--ambre": "#f2e3c2", "--cyan": "#d9e2ef",
    "--papier": "#f6f0e2", "--encre": "#23262d", "--rouge": "#9a2f2a", "--vert": "#3f6a46",
    "--panneau-haut": "#fbf8f0", "--panneau-bas": "#e9e1cf", "--accent": "#2f4a7a", "--accent-clair": "#e0e6f1",
    "--fond-carte": "#ffffff", "--fond-colonne": "#eee8da", "--bord-doux": "#a69c86", "--bord-clair": "#d9d0bb", "--rivet": "#8a6a2c",
    "--plaque-haut": "rgba(47,74,122,.96)", "--plaque-bas": "rgba(22,34,58,.97)", "--cadre-haut": "rgba(106,58,42,.94)", "--cadre-bas": "rgba(56,30,22,.96)",
    "--laiton-profond": "#a8832f", "--ombre-bouton": "#3a2c10", "--encre-bouton": "#1d1606", "--bareme-fond": "#2f4a7a",
}

VOIX = {
    "antoine": {"edge": "fr-FR-HenriNeural",                "nom": "Henri",    "rate": 1.0,  "pitch": 1.0},   # grenadier, franc
    "rose":    {"edge": "fr-FR-DeniseNeural",               "nom": "Denise",   "rate": 1.0,  "pitch": 1.02},  # brodeuse, émerveillée
    "jeanne":  {"edge": "fr-BE-CharlineNeural",             "nom": "Charline", "rate": 0.97, "pitch": 1.0},   # cantinière, chaleureuse et grave
    "hugo":    {"edge": "fr-FR-RemyMultilingualNeural",     "nom": "Rémy",     "rate": 0.97, "pitch": 1.0},   # conservateur, posé
    "ines":    {"edge": "fr-FR-VivienneMultilingualNeural", "nom": "Vivienne", "rate": 1.0,  "pitch": 1.0},   # maire, accueillante
}

GUIDES = {1: "antoine", 2: "rose", 3: "jeanne", 4: "hugo", 5: "ines"}

PORTRAITS = {
    "antoine": {"genre": "homme", "coiffure": "courte", "cheveux": "#3a2416", "peau": "#e8c0a0", "habit": "#2f4a7a", "barbe": True, "lunettes": False},
    "rose":    {"genre": "femme", "coiffure": "longue", "cheveux": "#8a5a30", "peau": "#f0cdb3", "habit": "#9a2f2a", "lunettes": False},
    "jeanne":  {"genre": "femme", "coiffure": "courte", "cheveux": "#4a2f1e", "peau": "#c98f68", "habit": "#4f6a5c", "lunettes": False},
    "hugo":    {"genre": "homme", "coiffure": "courte", "cheveux": "#2a1c14", "peau": "#a8714e", "habit": "#23262d", "barbe": False, "lunettes": True},
    "ines":    {"genre": "femme", "coiffure": "longue", "cheveux": "#1e1410", "peau": "#d9a47e", "habit": "#2f4a7a", "lunettes": False},
}

STYLE_VISUEL = ("Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée du Paris du Consulat et du Premier Empire (1800-1815) "
                "pour les salles 1 à 3, lieux réels d'aujourd'hui pour les salles 4 et 5, couleurs chaudes et dorées, lumière naturelle douce, atmosphère de musée, "
                "aucune inscription lisible, grain fin.")
EPOQUE = ("France de 1800 à aujourd'hui : une antichambre du palais des Tuileries (1800), la cathédrale Notre-Dame décorée pour le sacre (1804), un bivouac "
          "de la Grande Armée, le dôme des Invalides et une salle des mariages de mairie (aujourd'hui). Aucune personne réelle (jamais Napoléon ni Joséphine "
          "en personne), aucun combat, aucune blessure.")
