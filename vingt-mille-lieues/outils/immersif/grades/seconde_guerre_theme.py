"""Identité du jeu « Radio Londres » : grades, palette, voix, portraits, direction artistique.
Grades = étapes d'un jeune messager de la Résistance devenu historien (les élèves reconstituent un message de Londres).
SUJET TRÈS SENSIBLE : ton grave et sobre, aucune énigme notée sur les persécutions."""

NOMS = {
    "mousse":     {"nom": "Jeune auditeur",     "icone": "📻", "equivalent": "≈ CE2", "profil": "énigmes courtes, vocabulaire simple (avant, pendant, après la guerre ; dictature, liberté ; résister), aides renforcées (premier indice offert, fiche mise en évidence)"},
    "matelot":    {"nom": "Messager",           "icone": "✉️", "equivalent": "≈ CM1", "profil": "repères : dictatures, défaite de 1940, appel du 18 Juin, Occupation, Résistance, Libération"},
    "timonier":   {"nom": "Agent de liaison",   "icone": "🚲", "equivalent": "≈ CM2", "profil": "cœur de programme CM2 : dates exactes, Vichy et la collaboration, STO, Jean Moulin et le CNR, 8 mai 1945"},
    "lieutenant": {"nom": "Archiviste",         "icone": "🔎", "equivalent": "≈ 6ᵉ",  "profil": "lecture critique des documents, justification par la fiche, causes et conséquences enchaînées"},
    "second":     {"nom": "Passeur de mémoire", "icone": "🕯️", "equivalent": "≈ 5ᵉ",  "profil": "raisonnement en plusieurs étapes, nuances (résistance, collaboration, attentisme), mise en relation des faits, justification"},
}

# Bleu nuit de la radio, gris de l'Occupation, kaki des maquis, bois du poste, papier jauni, rouge sourd.
PALETTE = {
    "--ocean": "#3b4a5a", "--abysse": "#1a2029", "--laiton": "#c2a061", "--laiton-clair": "#ede0c2", "--laiton-fonce": "#6b5427",
    "--acajou": "#5a4632", "--acajou-clair": "#846d55", "--vertdegris": "#5b6a4c", "--ambre": "#efe2c6", "--cyan": "#d6dee6",
    "--papier": "#f4efe4", "--encre": "#262a2e", "--rouge": "#8a2f2a", "--vert": "#4d6a3c",
    "--panneau-haut": "#faf7f0", "--panneau-bas": "#e6e0d3", "--accent": "#3b4a5a", "--accent-clair": "#e1e6ec",
    "--fond-carte": "#ffffff", "--fond-colonne": "#ece8df", "--bord-doux": "#a29a8b", "--bord-clair": "#d6cfc1", "--rivet": "#86693a",
    "--plaque-haut": "rgba(59,74,90,.96)", "--plaque-bas": "rgba(26,32,41,.97)", "--cadre-haut": "rgba(90,70,50,.94)", "--cadre-bas": "rgba(46,36,26,.96)",
    "--laiton-profond": "#a5833f", "--ombre-bouton": "#382c14", "--encre-bouton": "#1c1608", "--bareme-fond": "#3b4a5a",
}

VOIX = {
    "bastien":   {"edge": "fr-FR-RemyMultilingualNeural",     "nom": "Rémy",     "rate": 0.96, "pitch": 1.0},   # instituteur, posé
    "paul":      {"edge": "fr-BE-GerardNeural",               "nom": "Gérard",   "rate": 1.0,  "pitch": 0.97},  # cheminot, chaleureux
    "madeleine": {"edge": "fr-FR-DeniseNeural",               "nom": "Denise",   "rate": 0.98, "pitch": 1.0},   # épicière, discrète
    "marc":      {"edge": "fr-FR-HenriNeural",                "nom": "Henri",    "rate": 0.95, "pitch": 1.06},  # jeune opérateur, à voix basse
    "lucie":     {"edge": "fr-FR-VivienneMultilingualNeural", "nom": "Vivienne", "rate": 1.02, "pitch": 1.04},  # agente de liaison, 17 ans
}

GUIDES = {1: "bastien", 2: "paul", 3: "madeleine", 4: "marc", 5: "lucie"}

PORTRAITS = {
    "bastien":   {"genre": "homme", "coiffure": "courte", "cheveux": "#4a3626", "peau": "#efc9ac", "habit": "#5a4632", "barbe": False, "lunettes": True},
    "paul":      {"genre": "homme", "coiffure": "courte", "cheveux": "#2a1c14", "peau": "#d9a47e", "habit": "#3b4a5a", "barbe": True, "lunettes": False},
    "madeleine": {"genre": "femme", "coiffure": "courte", "cheveux": "#7a5a3a", "peau": "#f0cdb3", "habit": "#8a2f2a", "lunettes": False},
    "marc":      {"genre": "homme", "coiffure": "courte", "cheveux": "#b08a55", "peau": "#e8c0a0", "habit": "#5b6a4c", "barbe": False, "lunettes": False},
    "lucie":     {"genre": "femme", "coiffure": "longue", "cheveux": "#3a2416", "peau": "#efc9ac", "habit": "#3b4a5a", "lunettes": False},
}

STYLE_VISUEL = ("Photographie photoréaliste de cinéma, objectif 35 mm, reconstitution historique soignée de la France rurale de 1938-1945, village du Morvan, "
                "couleurs sourdes et froides, lumière naturelle, atmosphère grave et retenue, aucune inscription lisible, grain fin.")
EPOQUE = ("France de 1938 à 1945 : le village inventé de Chantelune-en-Morvan (Nièvre), sa salle de classe, sa petite gare, l'épicerie, une cabane de maquis "
          "dans la forêt, la place de la mairie pavoisée. Aucune personne réelle, aucun uniforme allemand, aucun symbole nazi, aucun combat, aucune image de camp.")
