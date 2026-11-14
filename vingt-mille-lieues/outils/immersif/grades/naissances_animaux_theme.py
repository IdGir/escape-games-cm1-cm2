"""Identité du jeu « La Nurserie du zoo » : grades, palette, voix, portraits, direction artistique.
Grades = métiers du zoo (les élèves sont les apprentis soigneurs du zoo des Trois-Sources)."""

NOMS = {
    "mousse":     {"nom": "Bénévole",            "icone": "🧺", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple (cellule du mâle, cellule de la femelle), aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Apprenti soigneur",   "icone": "🪣", "equivalent": "≈ CM1", "profil": "cœur de programme : fécondation, dans l'eau ou dans le corps, ovipares et vivipares, couvaison"},
    "timonier":   {"nom": "Soigneur",            "icone": "🐾", "equivalent": "≈ CM2", "profil": "cœur de programme CM2 : gamètes, tableau à deux entrées, exceptions, durées de gestation"},
    "lieutenant": {"nom": "Biologiste",          "icone": "🔬", "equivalent": "≈ 6ᵉ",  "profil": "raisonnement en deux étapes, contre-exemples, justification par la fiche"},
    "second":     {"nom": "Chef de la nurserie", "icone": "🥚", "equivalent": "≈ 5ᵉ",  "profil": "lecture de données, calculs de durées, exceptions expliquées, justification"},
}

# Vert feuillage du zoo, sable des enclos, bleu des bassins, brun des nids.
PALETTE = {
    "--ocean": "#3f6b3a", "--abysse": "#1c2b1a", "--laiton": "#e9b949", "--laiton-clair": "#f7e3a8", "--laiton-fonce": "#7a5a12",
    "--acajou": "#6b4f35", "--acajou-clair": "#8f7155", "--vertdegris": "#2f7a6b", "--ambre": "#fbe7b0", "--cyan": "#d3ebf2",
    "--papier": "#f8f6ef", "--encre": "#22281d", "--rouge": "#b03a2e", "--vert": "#2f7a4a",
    "--panneau-haut": "#fdfcf7", "--panneau-bas": "#ece8da", "--accent": "#3f6b3a", "--accent-clair": "#e4efdc",
    "--fond-carte": "#ffffff", "--fond-colonne": "#eef2e6", "--bord-doux": "#a3ad92", "--bord-clair": "#d6dccb", "--rivet": "#a0643a",
    "--plaque-haut": "rgba(63,107,58,.96)", "--plaque-bas": "rgba(28,43,26,.97)", "--cadre-haut": "rgba(107,79,53,.94)", "--cadre-bas": "rgba(55,40,27,.96)",
    "--laiton-profond": "#b88a1c", "--ombre-bouton": "#3b2d08", "--encre-bouton": "#1d1604", "--bareme-fond": "#3f6b3a",
}

VOIX = {
    "ines":   {"edge": "fr-FR-VivienneMultilingualNeural", "nom": "Vivienne", "rate": 0.98, "pitch": 1.0},    # vétérinaire, posée
    "theo":   {"edge": "fr-FR-HenriNeural",                "nom": "Henri",    "rate": 1.03, "pitch": 1.02},   # soigneur, enthousiaste
    "malo":   {"edge": "fr-BE-GerardNeural",               "nom": "Gérard",   "rate": 1.0,  "pitch": 0.96},   # soigneur des surprises, malicieux
    "jeanne": {"edge": "fr-FR-DeniseNeural",               "nom": "Denise",   "rate": 0.97, "pitch": 1.0},    # éleveuse, chaleureuse
    "sacha":  {"edge": "fr-FR-RemyMultilingualNeural",     "nom": "Rémy",     "rate": 1.05, "pitch": 1.15},   # élève de CM2
}

GUIDES = {1: "ines", 2: "theo", 3: "malo", 4: "jeanne", 5: "sacha"}

PORTRAITS = {
    "ines":   {"genre": "femme", "coiffure": "longue", "cheveux": "#2a1a12", "peau": "#c99a74", "habit": "#f2f2f2", "lunettes": True},
    "theo":   {"genre": "homme", "coiffure": "courte", "cheveux": "#a0522d", "peau": "#f1cfb5", "habit": "#2f7a6b", "barbe": False, "lunettes": False},
    "malo":   {"genre": "homme", "coiffure": "courte", "cheveux": "#1a1210", "peau": "#8d5a3b", "habit": "#3f6b3a", "barbe": True, "lunettes": False},
    "jeanne": {"genre": "femme", "coiffure": "courte", "cheveux": "#9a9a9a", "peau": "#efc8ab", "habit": "#a0643a", "lunettes": False},
    "sacha":  {"genre": "homme", "coiffure": "courte", "cheveux": "#d9b25f", "peau": "#f3d2b8", "habit": "#e9b949", "barbe": False, "lunettes": True},
}

STYLE_VISUEL = ("Photographie photoréaliste de cinéma, objectif 35 mm, coulisses d'un zoo pédagogique au petit matin après une tempête, "
                "nurserie, couveuse, bassins, vitrines, lumière douce, aucune inscription lisible, grain fin.")
EPOQUE = ("Univers contemporain : le zoo inventé des Trois-Sources, sa nurserie, sa mare, sa galerie et sa ferme. "
          "Aucune scène de naissance ni de mise bas, aucun animal blessé, aucune personne réelle.")
