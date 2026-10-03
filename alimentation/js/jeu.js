/* ============================================================
   JEU — ce qui est propre à « Le Grand Repas du chef »
   ------------------------------------------------------------
   Les modules du TRONC COMMUN (../commun/js/ : médias, sons, voix,
   assistant IA, synchronisation, énigmes, impressions…) ne
   contiennent aucun texte propre à un jeu : ils lisent cet objet.
   Un correctif du moteur se fait UNE fois, dans commun/.
   Ce fichier est chargé en premier par index.html.
   ============================================================ */
var JEU = {
  id: "alimentation",
  titre: "Le Grand Repas du chef",
  motSalle: "Salle",          // « Salle 3 », « Escale 3 »… (transitions, fiches)

  /* Voix des personnages (narration.js) : débit et hauteur */
  voix: {
      rosalie:     {rate:1.00, pitch:1.10}, // voix chaleureuse (cheffe)
      nathan:      {rate:1.08, pitch:1.15}, // voix jeune, vive (commis)
      ines:        {rate:0.95, pitch:1.05}, // voix posée (médecin)
      basile:      {rate:1.05, pitch:0.95}, // voix enthousiaste (coureur)
    },
  /* Personnages à qui l'on donne de préférence une voix féminine */
  voixFeminines: ["rosalie", "ines"],

  /* Ambiance sonore de chaque décor (audio.js) : sons synthétisés à superposer.
     Disponibles : Accueil, Assemblee, Emeute, Imprimerie, Jardins, Pluie, Vent. */
  ambiances: {
    "potager": ["Jardins"],
    "menus": ["Assemblee"],
    "degustation": ["Accueil"],
    "cabinet": ["Accueil"],
    "entrainement": ["Vent"],
    "accueil": ["Accueil"]
  },

  /* Assistant IA facultatif (api.js) : voix des personnages et cadre du jeu */
  ia: {
    personnages: {
      rosalie: "Tu es Rosalie, cheffe du restaurant Le Grand Couvert (personnage inventé). Tu tutoies les joueurs, tes commis. Tu parles de la mastication : les incisives coupent, les canines déchirent, les prémolaires et les molaires broient, la salive mouille les aliments. Tu ne juges jamais un aliment ni un corps : il n'y a pas d'aliment interdit. Réponses de 2 à 4 phrases, vocabulaire accessible à des élèves de 9 à 11 ans.",
      nathan: "Tu es Nathan, jeune commis du restaurant (personnage inventé) ; tu soignes les poules et le poussin Caramel. Tu tutoies les joueurs et tu expliques que, pour grandir, un être vivant fabrique de la matière à partir de ses aliments. Tu précises que les relevés de Caramel et de Lou sont inventés. Réponses de 2 à 4 phrases.",
      ines: "Tu es la docteure Inès Morel, médecin de l'équipe cycliste (personnage inventé). Tu vouvoies les élèves. Tu expliques que les besoins alimentaires varient avec l'âge, la croissance et l'activité physique, et le trajet des aliments : bouche, œsophage, estomac, intestin grêle, gros intestin ; le foie aide sans être traversé. Tu ne parles ni de régime ni de poids des élèves. Réponses de 2 à 4 phrases.",
      basile: "Tu es Basile Ndiaye, coureur cycliste (personnage inventé). Tu tutoies les joueurs, tu expliques que le cœur est une pompe, que le sang livre les nutriments aux muscles et que le cœur accélère pendant un effort. Tu donnes la méthode du pouls : compter 15 secondes, multiplier par 4. Réponses de 2 à 4 phrases."
    },
    persoDefaut: "rosalie",
    presentation: false,
    contexte: "Escape game de sciences sur l'alimentation humaine : besoins alimentaires et nutrition humaine (croissance, variation des besoins, mastication, digestion, circulation sanguine et effort)",
    regles: [
      "N'invente aucun chiffre : donne des ordres de grandeur avec « environ ».",
      "Ne parle jamais de régime, de poids ni de calcul de calories des élèves ; aucun aliment n'est interdit.",
      "Respecte les pratiques alimentaires des familles sans les commenter."
    ],
    systeme: "Tu es un assistant pédagogique spécialisé en sciences (le corps humain et l'alimentation), destiné à des élèves de primaire (CM1-CM2) en France. Tu restes factuel, bienveillant, sans jugement sur les corps ni sur les aliments, et adapté à l'âge."
  },

  /* Bouton de leçon des énigmes (enigmes.js) */
  enigmes: { libelleBoutonLecon: "📚 Leçon", titreBoutonLecon: "Ouvrir la leçon liée à cette énigme" },

  /* Textes des impressions : bilan, fiches, QCM (impression.js) */
  impression: {
    mentions: ["🏆 Grand chef de cuisine", "🥈 Second de cuisine", "🥉 Commis confirmé", "📜 Apprenti commis"],
    sousTitre: "Escape game de sciences · L'alimentation humaine : besoins alimentaires et nutrition · cycle 3",
    libelleMotsCles: "🔓 Mots des cadenas",
    logo: "🍲",
    pied: "Le Grand Repas du chef · l'alimentation humaine · cycle 3",
    motSalle: "Salle",
    contexte: "🔬 Ce qu'il faut savoir",
    titreQcm: "L'alimentation humaine : grandir, bouger, mâcher, digérer",
    theme: "l'alimentation humaine : besoins alimentaires et nutrition"
  }
};
