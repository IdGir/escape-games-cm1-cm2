/* ============================================================
   JEU — ce qui est propre à « L'Atelier de Léonard à Amboise »
   ------------------------------------------------------------
   Les modules du TRONC COMMUN (../commun/js/ : médias, sons, voix,
   assistant IA, synchronisation, énigmes, impressions…) ne
   contiennent aucun texte propre à un jeu : ils lisent cet objet.
   Un correctif du moteur se fait UNE fois, dans commun/.
   Ce fichier est chargé en premier par index.html.
   ============================================================ */
var JEU = {
  id: "renaissance",
  titre: "L'Atelier de Léonard à Amboise",
  motSalle: "Salle",          // « Salle 3 », « Escale 3 »… (transitions, fiches)

  /* Voix des personnages (narration.js) : débit et hauteur */
  voix: {
      tommaso:     {rate:1.05, pitch:1.25}, // voix jeune, vive (apprenti)
      jacquet:     {rate:0.92, pitch:0.85}, // voix grave (imprimeur)
      helene:      {rate:0.92, pitch:1.05}, // voix posée (dame de la cour)
      colombe:     {rate:1.05, pitch:1.30}, // voix jeune (fille du maçon)
      bastien:     {rate:1.00, pitch:1.00}, // voix enthousiaste (jeune peintre)
    },
  /* Personnages à qui l'on donne de préférence une voix féminine */
  voixFeminines: ["helene", "colombe"],

  /* Ambiance sonore de chaque décor (audio.js) : sons synthétisés à superposer.
     Disponibles : Accueil, Assemblee, Emeute, Imprimerie, Jardins, Pluie, Vent. */
  ambiances: {
    "imprimerie": ["Imprimerie"],
    "salle": ["Assemblee"],
    "atelier": ["Jardins"],
    "plans": ["Accueil"],
    "galerie": ["Accueil"],
    "accueil": ["Accueil"]
  },

  /* Assistant IA facultatif (api.js) : voix des personnages et cadre du jeu */
  ia: {
    personnages: {
      tommaso: "Tu es Tommaso, 12 ans, apprenti (personnage inventé) de Léonard de Vinci au manoir du Cloux, à Amboise, en 1518. Tu tutoies les joueurs, tu admires ton maître : peintre, ingénieur, observateur de la nature. Tu précises que ses machines volantes sont restées des dessins. Réponses de 2 à 4 phrases, vocabulaire accessible à des élèves de 9 à 11 ans.",
      jacquet: "Tu es Maître Jacquet, imprimeur (personnage inventé) à Amboise en 1518. Tu vouvoies les élèves, tu expliques l'imprimerie, les livres des Anciens, la Renaissance venue d'Italie et les humanistes. Réponses de 2 à 4 phrases.",
      helene: "Tu es Dame Hélène, dame de la cour (personnage inventée) de François Ier à Amboise. Tu vouvoies les élèves, tu expliques que le roi est un mécène des arts et des lettres, mais aussi un roi guerrier (Marignan, 1515). Réponses de 2 à 4 phrases.",
      colombe: "Tu es Colombe, 11 ans, fille d'un maître maçon (personnage inventée). Tu tutoies les joueurs, tu compares le château fort et le château de la Renaissance (Amboise, Blois, Chambord) et tu parles de la salamandre, emblème du roi. Tu dis qu'on ne sait pas avec certitude si Léonard a dessiné l'escalier de Chambord. Réponses de 2 à 4 phrases.",
      bastien: "Tu es Bastien, jeune peintre de la cour (personnage inventé). Tu tutoies les joueurs, tu expliques la perspective (point de fuite, ligne d'horizon), les proportions (l'Homme de Vitruve), le portrait et le sfumato. Réponses de 2 à 4 phrases."
    },
    persoDefaut: "tommaso",
    presentation: false,
    contexte: "Escape game d'histoire sur la Renaissance : François Ier, protecteur des arts et des lettres, grâce à l'aide de Léonard de Vinci",
    regles: [
      "N'invente aucun fait historique ni aucune date.",
      "Ne présente pas comme réalisées les inventions de Léonard restées à l'état de dessin.",
      "Ne fais jamais parler Léonard de Vinci ni François Ier à la première personne."
    ],
    systeme: "Tu es un assistant pédagogique spécialisé en histoire de la Renaissance, destiné à des élèves de primaire (CM1-CM2) en France. Tu restes factuel, strictement neutre, bienveillant et adapté à l'âge."
  },

  /* Bouton de leçon des énigmes (enigmes.js) */
  enigmes: { libelleBoutonLecon: "📚 Leçon", titreBoutonLecon: "Ouvrir la leçon liée à cette énigme" },

  /* Textes des impressions : bilan, fiches, QCM (impression.js) */
  impression: {
    mentions: ["🏆 Maître de la Renaissance", "🥈 Compagnon de l'atelier", "🥉 Apprenti de Léonard", "📜 Jeune curieux"],
    sousTitre: "Escape game d'histoire · François Ier, Léonard de Vinci et la Renaissance · cycle 3",
    libelleMotsCles: "📜 Pages du carnet",
    logo: "🏛️",
    pied: "L'Atelier de Léonard à Amboise · la Renaissance · cycle 3",
    motSalle: "Salle",
    contexte: "📜 Contexte historique",
    titreQcm: "François Ier, Léonard de Vinci et la Renaissance",
    theme: "la Renaissance, François Ier et Léonard de Vinci"
  }
};
