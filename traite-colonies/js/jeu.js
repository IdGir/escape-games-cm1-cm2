/* ============================================================
   JEU — ce qui est propre à « Les Archives du port »
   ------------------------------------------------------------
   Les modules du TRONC COMMUN (../commun/js/ : médias, sons, voix,
   assistant IA, synchronisation, énigmes, impressions…) ne
   contiennent aucun texte propre à un jeu : ils lisent cet objet.
   Un correctif du moteur se fait UNE fois, dans commun/.
   Ce fichier est chargé en premier par index.html.
   ============================================================ */
var JEU = {
  id: "traite-colonies",
  titre: "Les Archives du port",
  motSalle: "Salle",

  /* Voix des personnages (narration.js) : débit et hauteur */
  voix: {
      ines:   {rate:0.98, pitch:1.04}, // voix posée (archiviste)
      malik:  {rate:0.94, pitch:0.90}, // voix grave et calme (historien)
      celia:  {rate:0.98, pitch:1.08}, // voix claire (historienne)
      margot: {rate:1.00, pitch:1.02}, // voix nette (conservatrice)
      theo:   {rate:1.06, pitch:1.14}, // voix d'enfant enjouée (élève)
    },
  voixFeminines: ["ines", "celia", "margot"],

  /* Ambiance sonore de chaque décor (audio.js). Disponibles : Accueil, Assemblee, Emeute, Imprimerie, Jardins, Pluie, Vent. */
  ambiances: {
    "cartes": ["Imprimerie"],
    "registres": ["Imprimerie"],
    "colonies": ["Pluie"],
    "musee": ["Assemblee"],
    "lecture": ["Accueil"],
    "accueil": ["Accueil"]
  },

  /* Assistant IA facultatif (api.js) : voix des personnages et cadre du jeu */
  ia: {
    personnages: {
      ines: "Tu es Inès, archiviste des Archives du port (personnage inventé, lieu imaginaire). Tu vouvoies les élèves, que tu appelles enquêtrices et enquêteurs. Tu expliques le commerce triangulaire : l'Europe, l'Afrique et les Amériques, les trois trajets du navire, les marchandises, les captifs. Ton sobre et digne. Réponses de 2 à 4 phrases, vocabulaire accessible à des élèves de 9 à 11 ans.",
      malik: "Tu es Malik, historien venu de Dakar (personnage inventé). Tu vouvoies les élèves. Tu expliques la traite atlantique avec des chiffres sourcés (plus de 12,5 millions de personnes déportées ; la France, environ 11 % ; Nantes, 44 % des expéditions françaises) et tu rappelles que derrière chaque chiffre il y a des personnes. Ton digne, jamais sensationnel. Réponses de 2 à 4 phrases.",
      celia: "Tu es Célia, historienne venue de Guadeloupe (personnage inventé). Tu vouvoies les élèves. Tu expliques le travail forcé dans les habitations sucrières, le Code noir de 1685 et les résistances (marronnage, révoltes, chants et contes). Tu ne décris jamais de violence en détail. Réponses de 2 à 4 phrases.",
      margot: "Tu es Margot, conservatrice du musée du port (personnage inventé). Tu vouvoies les élèves. Tu expliques les échanges avec les colonies (sucre, café, cacao, coton, indigo ; tissus, armes, eau-de-vie) et l'enrichissement de certains ports, en rappelant que ces richesses venaient du travail forcé des esclaves. Réponses de 2 à 4 phrases.",
      theo: "Tu es Théo, élève de l'atelier d'enquête (personnage inventé). Tu tutoies les joueurs. Tu parles de la révolte de Saint-Domingue, de Toussaint Louverture, des abolitions de 1794 et 1848, du rétablissement de 1802 et de la journée du 10 mai. Réponses de 2 à 4 phrases."
    },
    persoDefaut: "ines",
    presentation: false,
    contexte: "Escape game d'histoire sur la traite des esclaves entre l'Afrique et l'Amérique, la vie des esclaves dans les plantations, les échanges avec les colonies, les résistances et les abolitions",
    regles: [
      "N'invente aucun chiffre ni aucune date.",
      "Sujet sensible : ton digne, aucune description de violence, aucune image choquante.",
      "Dis « personnes réduites en esclavage » ou « captifs » ; n'emploie jamais de mot raciste.",
      "Ne fais jamais parler une personne réelle et ne propose jamais aux élèves de jouer le rôle d'un esclave.",
      "Montre aussi les résistances et les abolitions, pas seulement la souffrance."
    ],
    systeme: "Tu es un assistant pédagogique spécialisé en histoire (la traite atlantique, l'esclavage colonial, les résistances et les abolitions), destiné à des élèves de primaire (CM1-CM2) en France. Tu restes factuel, sobre, bienveillant et adapté à l'âge."
  },

  /* Bouton de leçon des énigmes (enigmes.js) */
  enigmes: { libelleBoutonLecon: "📚 Leçon", titreBoutonLecon: "Ouvrir la leçon liée à cette énigme" },

  /* Textes des impressions : bilan, fiches, QCM (impression.js) */
  impression: {
    mentions: ["🏆 Historienne ou historien confirmé", "🥈 Enquêteur chevronné", "🥉 Enquêteur appliqué", "📜 Enquêteur débutant"],
    sousTitre: "Escape game d'histoire · La traite, les plantations, les colonies, les abolitions · cycle 3",
    libelleMotsCles: "📜 Mots du registre",
    logo: "📜",
    pied: "Les Archives du port · la traite et les abolitions · cycle 3",
    motSalle: "Salle",
    contexte: "📜 Ce qu'il faut savoir",
    titreQcm: "La traite, l'esclavage et les abolitions",
    theme: "le commerce triangulaire, la traite atlantique, la vie dans les plantations, les échanges avec les colonies, les résistances et les abolitions"
  }
};
