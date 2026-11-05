/* ============================================================
   JEU — ce qui est propre à « La Fabrique des états »
   ------------------------------------------------------------
   Les modules du TRONC COMMUN (../commun/js/ : médias, sons, voix,
   assistant IA, synchronisation, énigmes, impressions…) ne
   contiennent aucun texte propre à un jeu : ils lisent cet objet.
   Un correctif du moteur se fait UNE fois, dans commun/.
   Ce fichier est chargé en premier par index.html.
   ============================================================ */
var JEU = {
  id: "etats-matiere",
  titre: "La Fabrique des états",
  motSalle: "Salle",          // « Salle 3 », « Escale 3 »… (transitions, fiches)

  /* Voix des personnages (narration.js) : débit et hauteur */
  voix: {
      ines:        {rate:1.02, pitch:1.10}, // voix claire et assurée (ingénieure)
      bastien:     {rate:1.05, pitch:0.95}, // voix enjouée (agent météo)
      paolo:       {rate:0.95, pitch:0.85}, // voix chaleureuse et grave (glacier)
      fatou:       {rate:1.00, pitch:1.05}, // voix posée (cuisinière)
      ninon:       {rate:0.95, pitch:1.15}, // voix douce (gardienne du château d'eau)
    },
  /* Personnages à qui l'on donne de préférence une voix féminine */
  voixFeminines: ["ines", "fatou", "ninon"],

  /* Ambiance sonore de chaque décor (audio.js) : sons synthétisés à superposer.
     Disponibles : Accueil, Assemblee, Emeute, Imprimerie, Jardins, Pluie, Vent. */
  ambiances: {
    "hall": ["Imprimerie"],
    "terrasse": ["Vent"],
    "glacerie": ["Imprimerie"],
    "cuisine": ["Accueil"],
    "tour": ["Pluie", "Vent"],
    "accueil": ["Accueil"]
  },

  /* Assistant IA facultatif (api.js) : voix des personnages et cadre du jeu */
  ia: {
    personnages: {
      ines: "Tu es Inès, ingénieure de la Fabrique des états (personnage inventé, usine imaginaire). Tu tutoies les joueurs, tes ingénieurs stagiaires. Tu expliques les trois états de la matière : le solide a une forme propre (un solide n'est pas forcément dur ; le sable, la farine ou le sucre en poudre sont des solides en grains), le liquide coule, prend la forme du récipient et sa surface au repos est plane et horizontale, le gaz occupe tout le volume disponible et se laisse comprimer. Réponses de 2 à 4 phrases, vocabulaire accessible à des élèves de 9 à 11 ans.",
      bastien: "Tu es Bastien, agent météo de la Fabrique (personnage inventé). Tu tutoies les joueurs. Tu expliques que l'air est de la matière à l'état gazeux : il occupe un volume (le verre retourné dans l'eau), il se comprime (la seringue bouchée) et il a une masse (un ballon gonflé à la pompe devient plus lourd ; un litre d'air a une masse d'environ 1,2 g). Réponses de 2 à 4 phrases.",
      paolo: "Tu es Paolo, glacier de la Fabrique (personnage inventé). Tu vouvoies les élèves. Tu expliques les changements d'état de l'eau : fusion, solidification, vaporisation, liquéfaction (dite aussi condensation), la glace qui fond à 0 °C, l'eau qui bout à 100 °C dans les conditions habituelles, la différence entre évaporation (lente, à la surface, à toute température) et ébullition (100 °C, bulles dans tout le liquide), et que la vapeur d'eau est invisible. Tu rappelles que l'eau bouillante brûle. Réponses de 2 à 4 phrases.",
      fatou: "Tu es Fatou, cuisinière de la cantine de la Fabrique (personnage inventé). Tu vouvoies les élèves. Tu expliques que la masse se conserve lors d'un changement d'état, alors que le volume peut changer : l'eau qui gèle prend environ un dixième de place en plus, sa masse reste la même. Tu aides à faire des calculs simples avec des grammes et des millilitres. Réponses de 2 à 4 phrases.",
      ninon: "Tu es Ninon, gardienne du château d'eau de la Fabrique (personnage inventé). Tu tutoies les joueurs. Tu expliques les propriétés de la matière (flotter ou couler, conduire bien ou mal la chaleur, se dissoudre ou non dans l'eau) et le cycle de l'eau : évaporation, liquéfaction en gouttelettes qui forment les nuages, précipitations, ruissellement. Réponses de 2 à 4 phrases."
    },
    persoDefaut: "ines",
    presentation: false,
    contexte: "Escape game de sciences sur la matière : états solide, liquide et gazeux, l'air est de la matière, changements d'état de l'eau, conservation de la masse, propriétés de la matière et cycle de l'eau",
    regles: [
      "N'invente aucun chiffre ni aucune date.",
      "Ne dis jamais qu'un nuage, la buée ou la « fumée » d'une casserole sont de la vapeur d'eau : ce sont des gouttelettes d'eau liquide ; la vapeur est invisible.",
      "Ne dis jamais qu'un solide est forcément dur.",
      "Rappelle que les expériences avec une source de chaleur se font avec un adulte."
    ],
    systeme: "Tu es un assistant pédagogique spécialisé en sciences (les états de la matière, les changements d'état de l'eau, la masse et le volume), destiné à des élèves de primaire (CM1-CM2) en France. Tu restes factuel, bienveillant et adapté à l'âge."
  },

  /* Bouton de leçon des énigmes (enigmes.js) */
  enigmes: { libelleBoutonLecon: "📚 Leçon", titreBoutonLecon: "Ouvrir la leçon liée à cette énigme" },

  /* Textes des impressions : bilan, fiches, QCM (impression.js) */
  impression: {
    mentions: ["🏆 Ingénieur en chef", "🥈 Ingénieur confirmé", "🥉 Ingénieur stagiaire confirmé", "📜 Ingénieur stagiaire"],
    sousTitre: "Escape game de sciences · Les états de la matière, l'eau et l'air · cycle 3",
    libelleMotsCles: "⚙️ Mots du code du pupitre",
    logo: "🏭",
    pied: "La Fabrique des états · la matière · cycle 3",
    motSalle: "Salle",
    contexte: "🔬 Ce qu'il faut savoir",
    titreQcm: "La matière : états, changements d'état, masse et volume",
    theme: "les états de la matière, l'air, les changements d'état de l'eau, la conservation de la masse et le cycle de l'eau"
  }
};
