"""Identité de « Mission géographique » (version immersive) : grades, palette, voix, portraits, direction artistique.
Grades = étapes de la carrière d'un agent du bureau du Professeur Atlas (personnages inventés). Une séance = une escale."""

NOMS = {
    "mousse":     {"nom": "Découverte",       "icone": "🎒", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple (commune, région, ville, campagne, montagne), aides renforcées"},
    "matelot":    {"nom": "Agent CM1",        "icone": "🔎", "equivalent": "≈ CM1", "profil": "repères : lieux et fonctions, territoires emboîtés, rural et urbain, secteurs, loisirs de montagne"},
    "timonier":   {"nom": "Agent CM2",        "icone": "🧭", "equivalent": "≈ CM2", "profil": "cœur de programme : 13 régions, compétences des collectivités, calculs de densité, chiffres exacts"},
    "lieutenant": {"nom": "Géographe",        "icone": "🗺️", "equivalent": "≈ 6ᵉ",  "profil": "documents à croiser, comparaisons chiffrées, justification par une phrase de la fiche"},
    "second":     {"nom": "Chef de mission",  "icone": "🛰️", "equivalent": "≈ 5ᵉ",  "profil": "raisonnement en plusieurs étapes, pièges, synthèse, justification"},
}

# Bleu nuit des cartes, papier kraft, rouge des épingles, vert des campagnes.
PALETTE = {
    "--ocean": "#1d3b5c", "--abysse": "#121b26", "--laiton": "#c9a24a", "--laiton-clair": "#efe0b4", "--laiton-fonce": "#6b5216",
    "--acajou": "#4b3a2c", "--acajou-clair": "#6f5a47", "--vertdegris": "#3f6f4a", "--ambre": "#f3e6c8", "--cyan": "#d6e4ef",
    "--papier": "#f6f1e6", "--encre": "#1b2430", "--rouge": "#a8323e", "--vert": "#2f7a4a",
    "--panneau-haut": "#fbf8f1", "--panneau-bas": "#ebe3d3", "--accent": "#1d3b5c", "--accent-clair": "#dde7f1",
    "--fond-carte": "#ffffff", "--fond-colonne": "#f0e9da", "--bord-doux": "#a39478", "--bord-clair": "#d8cdb8", "--rivet": "#8a6a2a",
    "--plaque-haut": "rgba(29,59,92,.96)", "--plaque-bas": "rgba(18,27,38,.97)", "--cadre-haut": "rgba(75,58,44,.94)", "--cadre-bas": "rgba(36,28,21,.96)",
    "--laiton-profond": "#a8832e", "--ombre-bouton": "#2e2106", "--encre-bouton": "#1a1204", "--bareme-fond": "#1d3b5c",
}

VOIX = {
    "atlas": {"edge": "fr-FR-HenriNeural",               "nom": "Henri",    "rate": 0.96, "pitch": 0.97},   # géographe, posé, un brin solennel
    "lena":  {"edge": "fr-FR-DeniseNeural",              "nom": "Denise",   "rate": 1.0,  "pitch": 1.0},    # agente de terrain, vive
    "malik": {"edge": "fr-FR-RemyMultilingualNeural",    "nom": "Rémy",     "rate": 1.02, "pitch": 1.0},    # agent infiltré, malicieux
    "zoe":   {"edge": "fr-FR-VivienneMultilingualNeural","nom": "Vivienne", "rate": 1.0,  "pitch": 1.0},    # agente des sources, précise
    "hugo":  {"edge": "fr-CH-FabriceNeural",             "nom": "Fabrice",  "rate": 1.0,  "pitch": 1.0},    # moniteur du Haut-Jura, chaleureux
    "ines":  {"edge": "fr-BE-CharlineNeural",            "nom": "Charline", "rate": 1.02, "pitch": 1.0},    # agente de la côte normande, enjouée
    "theo":  {"edge": "fr-BE-GerardNeural",              "nom": "Gérard",   "rate": 1.0,  "pitch": 1.0},    # sauveteur de Biarritz, décontracté
    "nour":  {"edge": "fr-CH-ArianeNeural",              "nom": "Ariane",   "rate": 0.98, "pitch": 1.0},    # agente à Dhaka, grave et attentive
    "aminata": {"edge": "fr-FR-JacquelineNeural",        "nom": "Jacqueline", "rate": 1.0, "pitch": 1.0},   # agente de Bamako, chaleureuse
    "camille": {"edge": "fr-FR-CelesteNeural",           "nom": "Céleste",  "rate": 1.02, "pitch": 1.0},    # cheffe de cantine, énergique
    "manon":   {"edge": "fr-FR-YvetteNeural",            "nom": "Yvette",   "rate": 0.98, "pitch": 1.0},    # éleveuse, posée
    "yanis":   {"edge": "fr-FR-AlainNeural",             "nom": "Alain",    "rate": 1.03, "pitch": 1.0},    # agent de Marseille, bavard
    "remi":    {"edge": "fr-FR-MauriceNeural",           "nom": "Maurice",  "rate": 0.97, "pitch": 0.98},   # guide de haute montagne, calme
}

# Une séance = une escale ; le guide parle pour toutes les énigmes de sa séance (P1 : séances 1 à 5 ; P2 : 6 à 8 ; P3-P4 : 9 à 13).
GUIDES = {1: "atlas", 2: "lena", 3: "malik", 4: "zoe", 5: "hugo", 6: "ines", 7: "theo", 8: "nour", 9: "aminata", 10: "camille", 11: "manon", 12: "yanis", 13: "remi"}

PORTRAITS = {
    "atlas": {"genre": "homme", "coiffure": "courte", "cheveux": "#d9d4cc", "peau": "#e9c4a6", "habit": "#1d3b5c", "barbe": True, "lunettes": True},
    "lena":  {"genre": "femme", "coiffure": "longue", "cheveux": "#5a3a22", "peau": "#f0cdb3", "habit": "#a8323e", "lunettes": False},
    "malik": {"genre": "homme", "coiffure": "courte", "cheveux": "#141010", "peau": "#a8704a", "habit": "#3f6f4a", "barbe": False, "lunettes": False},
    "zoe":   {"genre": "femme", "coiffure": "courte", "cheveux": "#141010", "peau": "#6e4630", "habit": "#c9a24a", "lunettes": True},
    "hugo":  {"genre": "homme", "coiffure": "courte", "cheveux": "#b8873e", "peau": "#f3d6bf", "habit": "#2a6f9e", "barbe": True, "lunettes": False},
    "ines":  {"genre": "femme", "coiffure": "longue", "cheveux": "#2b1a12", "peau": "#d9a57e", "habit": "#3a6f8f", "lunettes": False},
    "theo":  {"genre": "homme", "coiffure": "courte", "cheveux": "#e0c27a", "peau": "#e8b994", "habit": "#d9382c", "barbe": False, "lunettes": False},
    "nour":  {"genre": "femme", "coiffure": "longue", "cheveux": "#141010", "peau": "#9a6a4a", "habit": "#2f7a4a", "lunettes": True},
    "aminata": {"genre": "femme", "coiffure": "longue", "cheveux": "#141010", "peau": "#7a4a30", "habit": "#c9a24a", "lunettes": False},
    "camille": {"genre": "femme", "coiffure": "courte", "cheveux": "#8a5a2b", "peau": "#f0cdb3", "habit": "#e8e4da", "lunettes": False},
    "manon":   {"genre": "femme", "coiffure": "longue", "cheveux": "#7a4a22", "peau": "#f3d6bf", "habit": "#3f6f4a", "lunettes": False},
    "yanis":   {"genre": "homme", "coiffure": "courte", "cheveux": "#141010", "peau": "#c68a5e", "habit": "#8a6a2a", "barbe": False, "lunettes": False},
    "remi":    {"genre": "homme", "coiffure": "courte", "cheveux": "#9a9a9a", "peau": "#e8b994", "habit": "#3a6f8f", "barbe": True, "lunettes": False},
}

STYLE_VISUEL = ("Photographie photoréaliste de cinéma, objectif 35 mm, France d'aujourd'hui, lumière naturelle douce, couleurs franches, "
                "ambiance de film d'espionnage pour la jeunesse, aucune inscription lisible, grain fin.")
EPOQUE = ("Univers contemporain : le bureau du Professeur Atlas (inventé), puis Dijon (place de la Libération), Clamecy (Nièvre), Besançon (boucle du Doubs), "
          "la station des Rousses (Haut-Jura), Étretat (falaises, front de mer), Biarritz (Grande Plage), Dhaka (marché), Bamako (marché), la cantine d'une école, la ferme de Bray et l'usine d'Issenheim, un marché de Marseille, les Alpes (torrent). Personnages inventés, aucune personne réelle, aucune violence.")
