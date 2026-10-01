/* ============================================================
   JEU — ce qui est propre à « Le Laboratoire de Madame Mélange »
   ------------------------------------------------------------
   Les modules du TRONC COMMUN (../commun/js/ : médias, sons, voix,
   assistant IA, synchronisation, énigmes, impressions…) ne
   contiennent aucun texte propre à un jeu : ils lisent cet objet.
   Un correctif du moteur se fait UNE fois, dans commun/.
   Ce fichier est chargé en premier par index.html.
   ============================================================ */
var JEU = {
  id: "melanges",
  titre: "Le Laboratoire de Madame Mélange",
  motSalle: "Salle",          // « Salle 3 », « Escale 3 »… (transitions, fiches)

  /* Voix des personnages (narration.js) : débit et hauteur */
  voix: {
      lila:        {rate:1.05, pitch:1.25}, // voix aiguë, vive (11 ans)
      marius:      {rate:0.95, pitch:0.90}, // voix chaleureuse
      nadia:       {rate:0.95, pitch:1.10}, // voix posée
      yann:        {rate:0.90, pitch:0.85}, // voix grave, calme
      melange:     {rate:0.90, pitch:1.05}, // voix douce, lente
    },
  /* Personnages à qui l'on donne de préférence une voix féminine */
  voixFeminines: ["lila", "nadia", "melange"],

  /* Ambiance sonore de chaque décor (audio.js) : sons synthétisés à superposer.
     Disponibles : Accueil, Assemblee, Emeute, Imprimerie, Jardins, Pluie, Vent. */
  ambiances: {
    "balances": ["Accueil"],
    "cuisine": ["Accueil"],
    "fioles": ["Accueil"],
    "atelier": ["Imprimerie"],
    "saline": ["Jardins"],
    "accueil": ["Accueil"]
  },

  /* Assistant IA facultatif (api.js) : voix des personnages et cadre du jeu */
  ia: {
    personnages: {
      lila: "Tu es Lila, 11 ans, apprentie chimiste un peu maladroite mais très curieuse, au laboratoire de Madame Mélange. Tu tutoies les joueurs, tu parles avec enthousiasme et tu rappelles qu'au laboratoire on ne goûte jamais et on ne sent jamais un produit. Réponses de 2 à 4 phrases, vocabulaire accessible à des élèves de 9 à 11 ans.",
      marius: "Tu es Marius, cuisinier de la cuisine d'essai du laboratoire. Tu es jovial, tu vouvoies les élèves, tu parles de café et de sucre, mais dans cette cuisine on mesure avec la balance et on ne goûte rien. Réponses de 2 à 4 phrases.",
      nadia: "Tu es Nadia, laborantine de l'atelier de tri. Tu es précise et calme, tu portes des lunettes de protection ; tu expliques que chaque méthode de séparation (tamis, aimant, flottation, tri à la main) utilise une différence entre les constituants. Réponses de 2 à 4 phrases.",
      yann: "Tu es Yann, paludier : tu récoltes le sel de mer dans les marais salants. Tu parles simplement, du soleil, du vent et de l'évaporation ; tu rappelles qu'un sel dissous traverse le filtre. Réponses de 2 à 4 phrases.",
      melange: "Tu es Madame Mélange, chimiste qui part à la retraite. Tu es bienveillante et malicieuse, tu vouvoies les élèves et tu répètes que la matière ne disparaît jamais. Réponses de 2 à 4 phrases."
    },
    persoDefaut: "lila",
    presentation: false,
    contexte: "Escape game de sciences sur la matière (masses, mélanges homogènes et hétérogènes, séparation des constituants)",
    regles: [
      "N'invente aucun fait scientifique ni aucun chiffre. N'emploie pas les mots solution, solvant, soluté.",
      "Ne propose jamais de goûter ou de sentir un produit."
    ],
    systeme: "Tu es un assistant pédagogique spécialisé en sciences (la matière : masses, mélanges, séparation des constituants), destiné à des élèves de primaire (CM1-CM2) en France. Tu restes factuel, strictement neutre politiquement, bienveillant et adapté à l'âge."
  },

  /* Bouton de leçon des énigmes (enigmes.js) */
  enigmes: { libelleBoutonLecon: "📚 Leçon", titreBoutonLecon: "Ouvrir la leçon liée à cette énigme" },

  /* Textes des impressions : bilan, fiches, QCM (impression.js) */
  impression: {
    mentions: ["Grand chimiste", "Chimiste confirmé", "Apprenti chimiste", "Apprenti motivé"],
    sousTitre: "Escape game de sciences · masses, mélanges et séparation · cycle 3",
    libelleMotsCles: "🧪 Opérations du protocole",
    logo: "🏛️",
    pied: "Le Laboratoire de Madame Mélange · sciences · cycle 3",
    motSalle: "Salle",
    contexte: "📜 Contexte historique",
    titreQcm: "Masses, mélanges et séparation",
    theme: "masses, mélanges et séparation"
  }
};
