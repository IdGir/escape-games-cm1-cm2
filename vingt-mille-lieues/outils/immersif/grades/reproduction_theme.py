"""Identité du jeu « Le Jardin de la vie » : grades, palette, voix, portraits, direction artistique.
Grades = étapes du parcours d'un naturaliste du jardin des Coteaux (jardin botanique et ferme inventés, Bourgogne)."""

NOMS = {
    "mousse":     {"nom": "Visiteur du jardin",   "icone": "🎒", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple (fleur, pollen, graine, œuf, petit), aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Apprenti jardinier",   "icone": "🌱", "equivalent": "≈ CM1", "profil": "repères : pièces de la fleur, pollinisation, graines et germination, fécondation interne et externe, ovipares et vivipares"},
    "timonier":   {"nom": "Naturaliste",          "icone": "🔎", "equivalent": "≈ CM2", "profil": "cœur du programme : cycle de vie, fécondation, ovipares et vivipares, espèce ; vocabulaire précis (ovaire, stigmate, gamète, larve)"},
    "lieutenant": {"nom": "Botaniste",            "icone": "🌸", "equivalent": "≈ 6ᵉ",  "profil": "programme de 6e : rôle de la pollinisation dans la transformation de la fleur en fruit, coopération, pollinisateurs ; justification par une phrase de la fiche"},
    "second":     {"nom": "Directeur du jardin",  "icone": "🧑‍🌾", "equivalent": "≈ 5ᵉ",  "profil": "raisonnement en plusieurs étapes, démarche expérimentale, lien fécondation et mode de reproduction, diversité des individus, justification"},
}

# Vert des feuilles, rose des fleurs, miel, bois de la ferme.
PALETTE = {
    "--ocean": "#2f5d2a", "--abysse": "#16210f", "--laiton": "#e0a526", "--laiton-clair": "#f6dfa0", "--laiton-fonce": "#7a5a0e",
    "--acajou": "#5a4632", "--acajou-clair": "#7d664d", "--vertdegris": "#4f8a3a", "--ambre": "#fbecc2", "--cyan": "#e3f0d8",
    "--papier": "#f8f6ee", "--encre": "#1f261a", "--rouge": "#b0344f", "--vert": "#2f7a3a",
    "--panneau-haut": "#fcfbf6", "--panneau-bas": "#e9e6d6", "--accent": "#2f5d2a", "--accent-clair": "#e1eed8",
    "--fond-carte": "#ffffff", "--fond-colonne": "#eef1e2", "--bord-doux": "#9aa58a", "--bord-clair": "#d3dac4", "--rivet": "#a07d10",
    "--plaque-haut": "rgba(47,93,42,.96)", "--plaque-bas": "rgba(22,33,15,.97)", "--cadre-haut": "rgba(90,70,50,.94)", "--cadre-bas": "rgba(40,30,20,.96)",
    "--laiton-profond": "#b9860f", "--ombre-bouton": "#3a2a06", "--encre-bouton": "#1c1404", "--bareme-fond": "#2f5d2a",
}

VOIX = {
    "basile":   {"edge": "fr-FR-HenriNeural",               "nom": "Henri",    "rate": 0.97, "pitch": 0.98},  # botaniste, posé
    "capucine": {"edge": "fr-FR-DeniseNeural",              "nom": "Denise",   "rate": 1.0,  "pitch": 1.0},   # apicultrice, chaleureuse
    "tom":      {"edge": "fr-FR-RemyMultilingualNeural",    "nom": "Rémy",     "rate": 1.06, "pitch": 1.08},  # enfant jardinier, enthousiaste
    "yasmine":  {"edge": "fr-FR-VivienneMultilingualNeural", "nom": "Vivienne", "rate": 1.0, "pitch": 1.0},   # éleveuse, énergique
    "nadia":    {"edge": "fr-BE-CharlineNeural",            "nom": "Charline", "rate": 0.98, "pitch": 1.0},   # vétérinaire, douce et précise
}

GUIDES = {1: "basile", 2: "capucine", 3: "tom", 4: "yasmine", 5: "nadia"}

PORTRAITS = {
    "basile":   {"genre": "homme", "coiffure": "courte", "cheveux": "#9a9a9a", "peau": "#e9c4a4", "habit": "#2f5d2a", "barbe": True, "lunettes": True},
    "capucine": {"genre": "femme", "coiffure": "longue", "cheveux": "#b5652b", "peau": "#f0cdb3", "habit": "#e0a526", "lunettes": False},
    "tom":      {"genre": "homme", "coiffure": "courte", "cheveux": "#3a2414", "peau": "#c98e64", "habit": "#4f8a3a", "barbe": False, "lunettes": False},
    "yasmine":  {"genre": "femme", "coiffure": "longue", "cheveux": "#1a1410", "peau": "#b47a54", "habit": "#5a4632", "lunettes": False},
    "nadia":    {"genre": "femme", "coiffure": "courte", "cheveux": "#2a1c14", "peau": "#8a5a3a", "habit": "#b0344f", "lunettes": True},
}

STYLE_VISUEL = ("Photographie photoréaliste de cinéma, objectif 35 mm, jardin botanique et ferme de Bourgogne au printemps, après un orage de nuit, "
                "lumière douce du matin, gouttes de pluie, aucune inscription lisible, grain fin.")
EPOQUE = ("Univers contemporain : le jardin des Coteaux (inventé) et la ferme voisine, en Bourgogne : serre, rucher au bord d'un verger, potager d'école, "
          "cour de ferme avec étang, bergerie et mare. Aucune personne réelle, aucun animal blessé, aucun animal habillé ou qui parle.")
