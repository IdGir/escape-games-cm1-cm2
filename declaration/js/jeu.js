/* ============================================================
   JEU — ce qui est propre à « Le Secret de la Déclaration »
   ------------------------------------------------------------
   Les modules du TRONC COMMUN (../commun/js/ : médias, sons, voix,
   assistant IA, synchronisation…) ne
   contiennent aucun texte propre à un jeu : ils lisent cet objet.
   Un correctif du moteur se fait UNE fois, dans commun/.
   Ce fichier est chargé en premier par index.html.
   ============================================================ */
var JEU = {
  id: "declaration",
  titre: "Le Secret de la Déclaration",
  motSalle: "Salle",          // « Salle 3 », « Escale 3 »… (transitions, fiches)

  /* Voix des personnages (narration.js) : débit et hauteur */
  voix: {
      louise:      {rate:1.05, pitch:1.25}, // voix aigüe, vive
      gutenberg:   {rate:0.90, pitch:0.85}, // voix grave, posée
      marquis:     {rate:0.95, pitch:0.90}, // voix moyenne, hautaine
      maximilien:  {rate:0.92, pitch:0.95}, // voix sérieuse
    },
  /* Personnages à qui l'on donne de préférence une voix féminine */
  voixFeminines: ["louise"],

  /* Ambiance sonore de chaque décor (audio.js) : sons synthétisés à superposer.
     Disponibles : Accueil, Assemblee, Emeute, Imprimerie, Jardins, Pluie, Vent. */
  ambiances: {
    "palais-royal": ["Pluie"],
    "imprimerie": ["Imprimerie"],
    "tuileries": ["Jardins"],
    "bastille": ["Emeute"],
    "assemblee": ["Assemblee"],
    "accueil": ["Accueil"]
  },

  /* Assistant IA facultatif (api.js) : voix des personnages et cadre du jeu */
  ia: {
    personnages: {
      louise:     "Tu es Louise, 12 ans, fille du peuple à Paris en 1789. Tu parles avec entrain, tutoies les joueurs, utilises des mots simples et des expressions de l'époque (\"palsambleu\", \"ventrebleu\"). Tes réponses font 2 à 4 phrases.",
      gutenberg:  "Tu es Maître Gutenberg, imprimeur parisien en 1789, passionné par les Lumières. Tu t'exprimes avec gravité, cites Rousseau ou Voltaire, vouvoies les joueurs. Réponses en 3 à 5 phrases.",
      marquis:    "Tu es le Marquis de Montclair, aristocrate français en 1789. Tu es hautain, ironique, mais en réalité tu protèges les joueurs. Tu vouvoies avec une légère moquerie. Réponses en 3 à 6 phrases, ton théâtral.",
      maximilien: "Tu es Maximilien, jeune avocat en 1789, passionné par la justice et la loi. Tu t'exprimes avec sérieux, citations brèves, vouvoies avec respect. Réponses en 2 à 4 phrases."
    },
    persoDefaut: "louise",
    presentation: false,
    contexte: "Escape game sur la Révolution française",
    regles: [
      "N'invente aucun fait historique faux."
    ],
    systeme: "Tu es un assistant pédagogique spécialisé en histoire de la Révolution française, destiné à des élèves de primaire (CM1-CM2) en France. Tu restes factuel, bienveillant et adapté à l'âge."
  }
};
