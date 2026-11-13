"""Identité du jeu « La Centrale en panne » : grades, palette, voix, portraits, direction artistique.
Grades = métiers de la centrale (les élèves sont les apprentis électriciens de la centrale de Clairval)."""

NOMS = {
    "mousse":     {"nom": "Stagiaire",     "icone": "🔦", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple, aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Électricien",   "icone": "🔌", "equivalent": "≈ CM1", "profil": "cœur de programme : circuit à une boucle, conducteurs et isolants, sécurité"},
    "timonier":   {"nom": "Technicien",    "icone": "🛠️", "equivalent": "≈ CM2", "profil": "cœur de programme CM2 : schéma normalisé, court-circuit, chiffres de la production"},
    "lieutenant": {"nom": "Ingénieur",     "icone": "💡", "equivalent": "≈ 6ᵉ",  "profil": "raisonnement en deux étapes, montages à deux récepteurs, justification par la fiche"},
    "second":     {"nom": "Chef de quart", "icone": "⚡", "equivalent": "≈ 5ᵉ",  "profil": "dérivation, court-circuit, lecture de données, justification"},
}

# Gris acier des armoires, jaune de signalisation, bleu nuit de la panne, cuivre des fils.
PALETTE = {
    "--ocean": "#1f4e79", "--abysse": "#0d1b2a", "--laiton": "#f2c230", "--laiton-clair": "#fbe8a6", "--laiton-fonce": "#7a5c0c",
    "--acajou": "#3d4a57", "--acajou-clair": "#5d6d7e", "--vertdegris": "#2e7d6b", "--ambre": "#ffe9a0", "--cyan": "#cfe6f3",
    "--papier": "#f4f6f8", "--encre": "#1d2733", "--rouge": "#b03a2e", "--vert": "#2f7a4a",
    "--panneau-haut": "#fbfcfd", "--panneau-bas": "#e6ebf0", "--accent": "#1f4e79", "--accent-clair": "#e2edf6",
    "--fond-carte": "#ffffff", "--fond-colonne": "#e9eef3", "--bord-doux": "#9aa8b5", "--bord-clair": "#cfd8e0", "--rivet": "#c47a2c",
    "--plaque-haut": "rgba(31,78,121,.96)", "--plaque-bas": "rgba(13,27,42,.97)", "--cadre-haut": "rgba(61,74,87,.94)", "--cadre-bas": "rgba(29,39,51,.96)",
    "--laiton-profond": "#b8900f", "--ombre-bouton": "#3b2f08", "--encre-bouton": "#1d1604", "--bareme-fond": "#1f4e79",
}

VOIX = {
    "nour":   {"edge": "fr-FR-EloiseNeural",               "nom": "Eloise",   "rate": 1.04, "pitch": 1.1},    # élève du club, curieuse
    "maelle": {"edge": "fr-FR-DeniseNeural",               "nom": "Denise",   "rate": 1.0,  "pitch": 1.02},   # magasinière, pratique
    "helene": {"edge": "fr-FR-VivienneMultilingualNeural", "nom": "Vivienne", "rate": 0.97, "pitch": 1.0},    # ingénieure, posée
    "marius": {"edge": "fr-BE-GerardNeural",               "nom": "Gérard",   "rate": 0.96, "pitch": 0.94},   # électricien, ferme sur la sécurité
    "karim":  {"edge": "fr-FR-HenriNeural",                "nom": "Henri",    "rate": 1.0,  "pitch": 1.0},    # technicien du réseau
}

GUIDES = {1: "nour", 2: "maelle", 3: "helene", 4: "marius", 5: "karim"}

PORTRAITS = {
    "nour":   {"genre": "femme", "coiffure": "longue", "cheveux": "#1a1210", "peau": "#c99a74", "habit": "#f2c230", "lunettes": False},
    "maelle": {"genre": "femme", "coiffure": "courte", "cheveux": "#a0522d", "peau": "#f1cfb5", "habit": "#2e7d6b", "lunettes": True},
    "helene": {"genre": "femme", "coiffure": "longue", "cheveux": "#5a3a22", "peau": "#eac3a5", "habit": "#1f4e79", "lunettes": True},
    "marius": {"genre": "homme", "coiffure": "courte", "cheveux": "#8a8a8a", "peau": "#efc8ab", "habit": "#3d4a57", "barbe": True, "lunettes": False},
    "karim":  {"genre": "homme", "coiffure": "courte", "cheveux": "#1a1210", "peau": "#b98563", "habit": "#c47a2c", "barbe": False, "lunettes": False},
}

STYLE_VISUEL = ("Photographie photoréaliste de cinéma, objectif 35 mm, intérieur d'une centrale électrique de vallée pendant une panne nocturne, "
                "éclairage de secours, métal peint, câbles, voyants, pluie sur les vitres, aucune inscription lisible, grain fin.")
EPOQUE = ("Univers contemporain : la centrale et la petite ville inventée de Clairval, plongées dans le noir après un orage. "
          "Aucune expérience avec le secteur, aucune personne électrisée montrée, aucune personne réelle.")
