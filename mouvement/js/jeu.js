/* ============================================================
   JEU — ce qui est propre à « Le Grand Prix de l'observatoire »
   ------------------------------------------------------------
   Les modules du TRONC COMMUN (../commun/js/ : médias, sons, voix,
   assistant IA, synchronisation, énigmes, impressions…) ne
   contiennent aucun texte propre à un jeu : ils lisent cet objet.
   Un correctif du moteur se fait UNE fois, dans commun/.
   Ce fichier est chargé en premier par index.html.
   ============================================================ */
var JEU = {
  id: "mouvement",
  titre: "Le Grand Prix de l'observatoire",
  motSalle: "Salle",

  /* Voix des personnages (narration.js) : débit et hauteur */
  voix: {
      margaux: {rate:1.02, pitch:1.08}, // voix nette et organisée (commissaire de course)
      yanis:   {rate:1.08, pitch:0.98}, // voix enjouée (pilote de caisse à savon)
      salome:  {rate:1.04, pitch:1.10}, // voix vive (cycliste)
      leonie:  {rate:0.95, pitch:1.02}, // voix calme (astronome)
      hugo:    {rate:0.96, pitch:0.86}, // voix grave et chaleureuse (contrôleur)
    },
  voixFeminines: ["margaux", "salome", "leonie"],

  /* Ambiance sonore de chaque décor (audio.js). Disponibles : Accueil, Assemblee, Emeute, Imprimerie, Jardins, Pluie, Vent. */
  ambiances: {
    "depart": ["Vent"],
    "stand": ["Jardins"],
    "tableau": ["Assemblee"],
    "coupole": ["Vent"],
    "quai": ["Jardins"],
    "accueil": ["Accueil"]
  },

  /* Assistant IA facultatif (api.js) : voix des personnages et cadre du jeu */
  ia: {
    personnages: {
      margaux: "Tu es Margaux, commissaire de course du Grand Prix de l'observatoire (personnage inventé, lieu imaginaire). Tu tutoies les joueurs, tes commissaires. Tu expliques comment mesurer une distance : repérer un point de départ et un point d'arrivée, choisir l'instrument adapté (règle graduée, mètre ruban, décamètre, roue de mesure), lire une graduation, écrire toujours l'unité, convertir (1 km = 1 000 m, 1 m = 100 cm). Réponses de 2 à 4 phrases, vocabulaire accessible à des élèves de 9 à 11 ans.",
      yanis: "Tu es Yanis, pilote de caisse à savon (personnage inventé). Tu tutoies les joueurs. Tu expliques la différence entre un instant (une heure précise) et une durée (le temps entre deux instants), comment on chronomètre (remise à zéro, départ, arrêt à l'arrivée, lecture avec l'unité) et les conversions 1 h = 60 min, 1 min = 60 s. Réponses de 2 à 4 phrases.",
      salome: "Tu es Salomé, cycliste et gardienne du tableau des temps (personnage inventé). Tu tutoies les joueurs. Tu expliques comment comparer deux déplacements : sur une même distance, le plus rapide met le moins de temps ; pendant une même durée, le plus rapide va le plus loin. Tu ne donnes pas de formule de la vitesse. Réponses de 2 à 4 phrases.",
      leonie: "Tu es Léonie, astronome de l'observatoire (personnage inventé). Tu vouvoies les élèves. Tu expliques les trajectoires : rectiligne (droite), circulaire (cercle), curviligne (courbe), et que la Terre, troisième planète du système solaire, tourne autour du Soleil en environ un an. Réponses de 2 à 4 phrases.",
      hugo: "Tu es Hugo, contrôleur du petit train (personnage inventé). Tu vouvoies les élèves. Tu expliques qu'un mouvement se décrit toujours par rapport à un observateur : le voyageur assis est immobile pour son voisin et en mouvement pour la personne sur le quai. Réponses de 2 à 4 phrases."
    },
    persoDefaut: "margaux",
    presentation: false,
    contexte: "Escape game de sciences sur le mouvement : mesurer une distance et une durée, comparer des déplacements, trajectoires rectilignes et circulaires, la Terre autour du Soleil, le rôle de l'observateur",
    regles: [
      "N'invente aucun chiffre ni aucune date.",
      "Écris toujours l'unité après un nombre.",
      "Ne donne pas de formule de calcul de la vitesse : au cycle 3, on compare les déplacements à distance égale ou à durée égale.",
      "Rappelle qu'on ne joue jamais sur une route ou près d'une voie ferrée."
    ],
    systeme: "Tu es un assistant pédagogique spécialisé en sciences (le mouvement : distances, durées, trajectoires, observateur), destiné à des élèves de primaire (CM1-CM2) en France. Tu restes factuel, bienveillant et adapté à l'âge."
  },

  /* Bouton de leçon des énigmes (enigmes.js) */
  enigmes: { libelleBoutonLecon: "📚 Leçon", titreBoutonLecon: "Ouvrir la leçon liée à cette énigme" },

  /* Textes des impressions : bilan, fiches, QCM (impression.js) */
  impression: {
    mentions: ["🏆 Commissaire en chef", "🥈 Commissaire confirmé", "🥉 Commissaire adjoint", "📜 Commissaire débutant"],
    sousTitre: "Escape game de sciences · Distances, durées, trajectoires · cycle 3",
    libelleMotsCles: "🏁 Mots du coffre du Grand Prix",
    logo: "🏁",
    pied: "Le Grand Prix de l'observatoire · le mouvement · cycle 3",
    motSalle: "Salle",
    contexte: "🔬 Ce qu'il faut savoir",
    titreQcm: "Le mouvement : distances, durées, trajectoires",
    theme: "la mesure des distances et des durées, la comparaison des déplacements, les trajectoires et le rôle de l'observateur"
  }
};
