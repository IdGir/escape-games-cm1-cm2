/* ============================================================
   JEU — ce qui est propre à « Le Secret du donjon »
   ------------------------------------------------------------
   Les modules du TRONC COMMUN (../commun/js/ : médias, sons, voix,
   assistant IA, synchronisation, énigmes, impressions…) ne
   contiennent aucun texte propre à un jeu : ils lisent cet objet.
   Un correctif du moteur se fait UNE fois, dans commun/.
   Ce fichier est chargé en premier par index.html.
   ============================================================ */
var JEU = {
  id: "chateau-fort",
  titre: "Le Secret du donjon",
  motSalle: "Salle",          // « Salle 3 », « Escale 3 »… (transitions, fiches)

  /* Voix des personnages (narration.js) : débit et hauteur */
  voix: {
      colin:       {rate:1.05, pitch:1.25}, // voix jeune, vive (page)
      josselin:    {rate:0.90, pitch:0.85}, // voix grave, posée (maître maçon)
      alienor:     {rate:0.92, pitch:1.05}, // voix posée (dame du château)
      mahaut:      {rate:1.05, pitch:1.30}, // voix jeune (paysanne)
      perrine:     {rate:0.98, pitch:1.10}, // voix franche (meunière)
    },
  /* Personnages à qui l'on donne de préférence une voix féminine */
  voixFeminines: ["alienor", "mahaut", "perrine"],

  /* Ambiance sonore de chaque décor (audio.js) : sons synthétisés à superposer.
     Disponibles : Accueil, Assemblee, Emeute, Imprimerie, Jardins, Pluie, Vent. */
  ambiances: {
    "motte": ["Jardins"],
    "remparts": ["Pluie"],
    "grandesalle": ["Accueil"],
    "village": ["Jardins"],
    "moulin": ["Imprimerie"],
    "accueil": ["Accueil"]
  },

  /* Assistant IA facultatif (api.js) : voix des personnages et cadre du jeu */
  ia: {
    personnages: {
      colin: "Tu es Colin, 11 ans, page au service d'un seigneur dans un château fort du XIIIe siècle. Tu es vif et serviable, tu tutoies les joueurs, tu connais chaque défense du château (douves, pont-levis, herse, meurtrières, mâchicoulis) et tu rappelles que le donjon est le logis du seigneur, pas une prison. Réponses de 2 à 4 phrases, vocabulaire accessible à des élèves de 9 à 11 ans.",
      josselin: "Tu es Maître Josselin, maître maçon sur le chantier d'un château fort. Tu es calme et précis, tu vouvoies les élèves, tu expliques la motte de terre et de bois, puis le passage à la pierre, et les métiers du chantier. Réponses de 2 à 4 phrases.",
      alienor: "Tu es Dame Aliénor, dame d'un château fort : tu gouvernes le domaine quand ton époux est absent (récoltes, comptes, hommes d'armes, justice). Tu es ferme et bienveillante, tu vouvoies les élèves. Tu expliques les trois fonctions du château : protection, lieu de vie, symbole de puissance. Réponses de 2 à 4 phrases.",
      mahaut: "Tu es Mahaut, 11 ans, jeune paysanne d'un village au pied d'un château. Tu tutoies les joueurs, tu racontes ta maison de torchis, le pain, les travaux des saisons et le travail de ta mère aux champs et à la maison. Réponses de 2 à 4 phrases.",
      perrine: "Tu es Perrine, meunière du moulin du seigneur. Tu es franche et précise, tu vouvoies les élèves, tu expliques la corvée, le cens, les banalités, la dîme versée à l'Église, et ce que le seigneur doit en échange. Tu fais remarquer que l'échange est inégal, sans violence. Réponses de 2 à 4 phrases."
    },
    persoDefaut: "colin",
    presentation: false,
    contexte: "Escape game d'histoire sur le Moyen Âge (les fonctions du château fort, la vie quotidienne des paysannes et des paysans, les relations entre seigneurs et paysans)",
    regles: [
      "N'invente aucun fait historique faux."
    ],
    systeme: "Tu es un assistant pédagogique spécialisé en histoire du Moyen Âge, destiné à des élèves de primaire (CM1-CM2) en France. Tu restes factuel, strictement neutre politiquement, bienveillant et adapté à l'âge."
  },

  /* Bouton de leçon des énigmes (enigmes.js) */
  enigmes: { libelleBoutonLecon: "📚 Leçon", titreBoutonLecon: "Ouvrir la leçon liée à cette énigme" },

  /* Textes des impressions : bilan, fiches, QCM (impression.js) */
  impression: {
    mentions: ["🏆 Gardien du donjon", "🥈 Chevalier du domaine", "🥉 Écuyer", "📜 Page en formation"],
    sousTitre: "Escape game d'histoire · le château fort et la vie des paysans · cycle 3",
    libelleMotsCles: "🗝️ Clés trouvées",
    logo: "🏛️",
    pied: "Le Secret du donjon · le château fort · cycle 3",
    motSalle: "Salle",
    contexte: "📜 Contexte historique",
    titreQcm: "Le château fort et la vie des paysans",
    theme: "le château fort et la vie des paysans"
  }
};
