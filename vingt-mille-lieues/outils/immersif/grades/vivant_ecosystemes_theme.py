"""Identité du jeu « L'Expédition biodiversité » : grades, palette, voix, portraits, direction artistique.
Grades = étapes du parcours d'un naturaliste (les élèves sont les jeunes naturalistes de la réserve du Val-des-Saules)."""

NOMS = {
    "mousse":     {"nom": "Promeneur",                "icone": "🥾", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple (attributs, même espèce, milieu, qui mange qui), aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Jeune naturaliste",        "icone": "🔎", "equivalent": "≈ CM1", "profil": "cœur de programme CM1 : espèce, groupes emboîtés, clé de détermination, écosystème, prédation et coopération, réseau alimentaire"},
    "timonier":   {"nom": "Naturaliste",              "icone": "🌿", "equivalent": "≈ CM2", "profil": "cœur de programme CM2 : fossiles, temps géologique en millions d'années, extinction massive, actions humaines"},
    "lieutenant": {"nom": "Écologue",                 "icone": "🦉", "equivalent": "≈ 6ᵉ",  "profil": "cellule, arbre de parenté, végétaux à la base du réseau, décomposition, justification par la fiche"},
    "second":     {"nom": "Conservateur de la réserve", "icone": "🗺️", "equivalent": "≈ 5ᵉ",  "profil": "raisonnement en plusieurs étapes, contre-exemples, prévisions sur un réseau, calculs de durées, justification"},
}

# Vert de la forêt, ocre de la carrière, bleu de l'étang, jaune des fleurs du pré.
PALETTE = {
    "--ocean": "#2f5f3a", "--abysse": "#15261a", "--laiton": "#e3b23c", "--laiton-clair": "#f5e2a6", "--laiton-fonce": "#76561a",
    "--acajou": "#6a4b2f", "--acajou-clair": "#8e6e50", "--vertdegris": "#2b6f78", "--ambre": "#f8e5b0", "--cyan": "#d2e9ef",
    "--papier": "#f7f6ee", "--encre": "#1f2a1d", "--rouge": "#ad3b2c", "--vert": "#2f7a4a",
    "--panneau-haut": "#fcfbf6", "--panneau-bas": "#e9e7d8", "--accent": "#2f5f3a", "--accent-clair": "#e1eedc",
    "--fond-carte": "#ffffff", "--fond-colonne": "#edf2e5", "--bord-doux": "#a0ac90", "--bord-clair": "#d4dbc9", "--rivet": "#9b6a3a",
    "--plaque-haut": "rgba(47,95,58,.96)", "--plaque-bas": "rgba(21,38,26,.97)", "--cadre-haut": "rgba(106,75,47,.94)", "--cadre-bas": "rgba(54,38,24,.96)",
    "--laiton-profond": "#b48a22", "--ombre-bouton": "#3a2c08", "--encre-bouton": "#1c1604", "--bareme-fond": "#2f5f3a",
}

VOIX = {
    "lina":  {"edge": "fr-FR-DeniseNeural",               "nom": "Denise",   "rate": 1.0,  "pitch": 1.0},    # biologiste, dynamique et précise
    "hugo":  {"edge": "fr-FR-HenriNeural",                "nom": "Henri",    "rate": 0.98, "pitch": 0.97},   # garde, calme
    "amara": {"edge": "fr-FR-VivienneMultilingualNeural", "nom": "Vivienne", "rate": 0.97, "pitch": 1.0},    # paléontologue, passionnée
    "rose":  {"edge": "fr-BE-CharlineNeural",             "nom": "Charline", "rate": 1.0,  "pitch": 1.02},   # apicultrice, chaleureuse
    "elio":  {"edge": "fr-FR-RemyMultilingualNeural",     "nom": "Rémy",     "rate": 1.03, "pitch": 1.0},    # pêcheur, jovial
}

GUIDES = {1: "lina", 2: "hugo", 3: "amara", 4: "rose", 5: "elio"}

PORTRAITS = {
    "lina":  {"genre": "femme", "coiffure": "longue", "cheveux": "#3a2416", "peau": "#a8714d", "habit": "#2f5f3a", "lunettes": False},
    "hugo":  {"genre": "homme", "coiffure": "courte", "cheveux": "#6b4a2b", "peau": "#efc9ac", "habit": "#5f6b2f", "barbe": True, "lunettes": False},
    "amara": {"genre": "femme", "coiffure": "courte", "cheveux": "#141010", "peau": "#6e4329", "habit": "#c08a3e", "lunettes": True},
    "rose":  {"genre": "femme", "coiffure": "longue", "cheveux": "#b9b2a6", "peau": "#f0cdb3", "habit": "#e3b23c", "lunettes": False},
    "elio":  {"genre": "homme", "coiffure": "courte", "cheveux": "#2a1c14", "peau": "#d9a47e", "habit": "#2b6f78", "barbe": False, "lunettes": False},
}

STYLE_VISUEL = ("Photographie photoréaliste de cinéma, objectif 35 mm, réserve naturelle de Bourgogne au printemps, matin lumineux après une nuit de pluie, "
                "campement d'expédition naturaliste, forêt de chênes, mare, pré fleuri, étang, lumière douce, aucune inscription lisible, grain fin.")
EPOQUE = ("Univers contemporain : la réserve naturelle inventée du Val-des-Saules, en Bourgogne, sa tente-laboratoire, la cabane du garde, une ancienne carrière, "
          "une mare, un pré avec des ruches et un étang. Aucune personne réelle, aucun animal blessé, aucun dinosaure vivant.")
