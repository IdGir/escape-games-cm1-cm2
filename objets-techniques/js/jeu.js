/* ============================================================
   JEU — ce qui est propre à « L'Atelier de l'inventeur »
   ------------------------------------------------------------
   Les modules du TRONC COMMUN (../commun/js/ : médias, sons, voix,
   assistant IA, synchronisation, énigmes, impressions…) ne
   contiennent aucun texte propre à un jeu : ils lisent cet objet.
   Un correctif du moteur se fait UNE fois, dans commun/.
   Ce fichier est chargé en premier par index.html.
   ============================================================ */
var JEU = {
  id: "objets-techniques",
  titre: "L'Atelier de l'inventeur",
  motSalle: "Salle",          // « Salle 3 », « Escale 3 »… (transitions, fiches)

  /* Voix des personnages (narration.js) : débit et hauteur */
  voix: {
      zoe:      {rate:1.05, pitch:1.25}, // voix vive, jeune
      awa:      {rate:0.98, pitch:1.10}, // voix claire, posée
      marcel:   {rate:0.90, pitch:0.85}, // voix grave, tranquille
      eleonore: {rate:0.95, pitch:1.05}, // voix chaleureuse
    },
  /* Personnages à qui l'on donne de préférence une voix féminine */
  voixFeminines: ["zoe", "awa", "eleonore"],

  /* Ambiance sonore de chaque décor (audio.js) : sons synthétisés à superposer.
     Disponibles : Accueil, Assemblee, Emeute, Imprimerie, Jardins, Pluie, Vent. */
  ambiances: {
    "atelier": ["Jardins"],
    "etabli": ["Accueil"],
    "materiaux": ["Accueil"],
    "machines": ["Assemblee"],
    "montage": ["Accueil"],
    "accueil": ["Accueil"]
  },

  /* Assistant IA facultatif (api.js) : voix des personnages et cadre du jeu */
  ia: {
    personnages: {
      zoe: "Tu es Zoé, 11 ans, apprentie ingénieure dans l'atelier d'une inventrice. Tu es curieuse, rapide et enthousiaste ; tu tutoies les joueurs et tu poses souvent une question à la fin. Réponses de 2 à 3 phrases, mots simples.",
      awa: "Tu es Awa, ouvrière de l'atelier. Tu es précise, patiente et concrète ; tu vouvoies les élèves et tu parles des pièces, des outils et des matériaux avec les mots justes. Réponses de 2 à 4 phrases.",
      marcel: "Tu es Monsieur Marcel, réparateur de vélos. Tu es chaleureux, un peu farceur, tu vouvoies les élèves et tu expliques la mécanique avec des exemples de vélos. Réponses de 2 à 4 phrases.",
      eleonore: "Tu es Éléonore Marchand, inventrice. Tu es bienveillante et enthousiaste ; tu vouvoies les élèves et tu insistes sur la démarche : besoin, fonction, matériau, énergie, notice. Réponses de 2 à 4 phrases."
    },
    persoDefaut: "zoe",
    presentation: false,
    contexte: "Escape game de sciences et technologie sur les objets techniques (besoin, fonctions, matériaux, énergie, notice)",
    regles: [
      "N'invente aucun fait scientifique ou technique faux."
    ],
    systeme: "Tu es un assistant pédagogique spécialisé en sciences et technologie (les objets techniques), destiné à des élèves de primaire (CM1-CM2) en France. Tu restes factuel, bienveillant et adapté à l'âge."
  },

  /* Bouton de leçon des énigmes (enigmes.js) */
  enigmes: { libelleBoutonLecon: "📚 Leçon", titreBoutonLecon: "Ouvrir la leçon liée à cette énigme" },

  /* Textes des impressions : bilan, fiches, QCM (impression.js) */
  impression: {
    mentions: ["🏆 Maître inventeur", "🥈 Ingénieur en herbe", "🥉 Apprenti technicien", "🔧 Apprenti motivé"],
    sousTitre: "Escape game de sciences et technologie · les objets techniques · cycle 3",
    libelleMotsCles: "🗝️ Serrures ouvertes",
    logo: "⚙️",
    pied: "L'Atelier de l'inventeur · les objets techniques · cycle 3",
    motSalle: "Salle",
    contexte: "🔧 Le lieu du jeu",
    titreQcm: "Les objets techniques",
    theme: "les objets techniques"
  }
};
