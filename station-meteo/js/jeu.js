/* ============================================================
   JEU — ce qui est propre à « La Station météo disparue »
   ------------------------------------------------------------
   Les modules du TRONC COMMUN (../commun/js/ : médias, sons, voix,
   assistant IA, synchronisation, énigmes, impressions…) ne
   contiennent aucun texte propre à un jeu : ils lisent cet objet.
   Un correctif du moteur se fait UNE fois, dans commun/.
   Ce fichier est chargé en premier par index.html.
   ============================================================ */
var JEU = {
  id: "station-meteo",
  titre: "La Station météo disparue",

  /* Voix des personnages (narration.js) : débit et hauteur */
  voix: {
      vasseur:     {rate:0.95, pitch:1.05}, // voix posée, claire
      tiago:       {rate:1.00, pitch:0.95}, // voix directe
      lina:        {rate:1.05, pitch:1.25}, // voix d'enfant, vive
      keita:       {rate:0.90, pitch:0.85}, // voix grave, lente
    },
  /* Personnages à qui l'on donne de préférence une voix féminine */
  voixFeminines: ["vasseur", "lina"],

  /* Ambiance sonore de chaque décor (audio.js) : sons synthétisés à superposer.
     Disponibles : Accueil, Assemblee, Emeute, Imprimerie, Jardins, Pluie, Vent. */
  ambiances: {
    "abri": ["Jardins"],
    "mat": ["Vent"],
    "pluvio": ["Pluie"],
    "bureau": ["Accueil"],
    "studio": ["Accueil"],
    "accueil": ["Accueil"]
  },

  /* Assistant IA facultatif (api.js) : voix des personnages et cadre du jeu */
  ia: {
    personnages: {
      vasseur: "Tu es Madame Vasseur, prévisionniste. Tu es calme, précise et encourageante ; tu vouvoies les élèves. Tu rappelles qu'une mesure n'a de valeur que si l'on sait où et quand elle a été prise. Réponses de 2 à 4 phrases, vocabulaire accessible à des élèves de 9 à 11 ans.",
      tiago: "Tu es Tiago, technicien de la station météo. Tu es concret, un peu bricoleur, tu tutoies les élèves et tu parles des instruments comme d'outils que l'on règle et que l'on entretient. Réponses de 2 à 3 phrases.",
      lina: "Tu es Lina, 10 ans, responsable de la station météo de l'école. Tu es curieuse et organisée, tu tutoies les joueurs et tu finis souvent par une question. Tu prends des exemples de la cour de récréation. Réponses de 2 à 3 phrases.",
      keita: "Tu es le capitaine Keïta, marin. Tu es posé et imagé ; tu vouvoies les élèves et tu expliques pourquoi la direction et la force du vent décident de la sortie en mer. Réponses de 2 à 4 phrases."
    },
    persoDefaut: "vasseur",
    presentation: false,
    contexte: "Escape game de sciences sur les mesures météorologiques (thermomètre, anémomètre, pluviomètre)",
    regles: [
      "N'invente aucune valeur de mesure ni aucun fait scientifique faux."
    ],
    systeme: "Tu es un assistant pédagogique en sciences et technologie au cycle 3 (mesures météorologiques : température, vent, précipitations), destiné à des élèves de CM1-CM2 en France. Tu restes factuel, tu n'inventes aucune valeur chiffrée, tu es bienveillant et adapté à l'âge."
  },

  /* Bouton de leçon des énigmes (enigmes.js) */
  enigmes: { libelleBoutonLecon: "📚 Leçon", titreBoutonLecon: "Ouvrir la leçon liée à cette énigme" },

  /* Textes des impressions : bilan, fiches, QCM (impression.js) */
  impression: {
    mentions: ["🏆 Chef de station", "🥈 Prévisionniste", "🥉 Technicien de station", "📜 Apprenti motivé"],
    sousTitre: "Escape game de sciences · mesures météorologiques · cycle 3",
    libelleMotsCles: "🛠️ Modules remis en service",
    logo: "🏛️",
    pied: "La Station météo disparue · mesures météorologiques · cycle 3",
    motSalle: "Module",
    contexte: "📜 Contexte historique",
    titreQcm: "Mesurer le temps qu'il fait",
    theme: "mesures météorologiques"
  }
};
