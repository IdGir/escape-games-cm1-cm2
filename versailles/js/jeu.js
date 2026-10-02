/* ============================================================
   JEU — ce qui est propre à « De l'édit de Nantes à Versailles »
   ------------------------------------------------------------
   Les modules du TRONC COMMUN (../commun/js/ : médias, sons, voix,
   assistant IA, synchronisation, énigmes, impressions…) ne
   contiennent aucun texte propre à un jeu : ils lisent cet objet.
   Un correctif du moteur se fait UNE fois, dans commun/.
   Ce fichier est chargé en premier par index.html.
   ============================================================ */
var JEU = {
  id: "versailles",
  titre: "De l'édit de Nantes à Versailles",
  motSalle: "Salle",          // « Salle 3 », « Escale 3 »… (transitions, fiches)

  /* Voix des personnages (narration.js) : débit et hauteur */
  voix: {
      gabriel:     {rate:1.05, pitch:1.20}, // voix jeune, vive (apprenti secrétaire)
      suzanne:     {rate:0.98, pitch:1.10}, // voix franche (imprimeuse)
      mathurin:    {rate:0.95, pitch:0.90}, // voix chaleureuse (boulanger)
      margot:      {rate:1.05, pitch:1.30}, // voix jeune (aide-jardinière)
      isabeau:     {rate:0.90, pitch:1.05}, // voix posée (dame de la cour)
    },
  /* Personnages à qui l'on donne de préférence une voix féminine */
  voixFeminines: ["suzanne", "margot", "isabeau"],

  /* Ambiance sonore de chaque décor (audio.js) : sons synthétisés à superposer.
     Disponibles : Accueil, Assemblee, Emeute, Imprimerie, Jardins, Pluie, Vent. */
  ambiances: {
    "imprimerie": ["Imprimerie"],
    "rue": ["Accueil"],
    "jardins": ["Jardins"],
    "chambre": ["Accueil"],
    "conseil": ["Assemblee"],
    "accueil": ["Accueil"]
  },

  /* Assistant IA facultatif (api.js) : voix des personnages et cadre du jeu */
  ia: {
    personnages: {
      gabriel: "Tu es Gabriel, 12 ans, apprenti secrétaire au cabinet du roi Louis XIV, à Versailles, en 1682. Tu es vif et serviable, tu tutoies les joueurs, tu connais les archives et le pli scellé de 1598. Tu expliques la monarchie absolue sans glorifier ni caricaturer le roi. Réponses de 2 à 4 phrases, vocabulaire accessible à des élèves de 9 à 11 ans.",
      suzanne: "Tu es Suzanne, imprimeuse protestante (huguenote) dans une petite ville du royaume de France, en 1598. Tu es franche et calme, tu vouvoies les élèves, tu expliques la Réforme (Luther, Calvin), le rôle de l'imprimerie, et les guerres de Religion avec sobriété, sans détails violents. Réponses de 2 à 4 phrases.",
      mathurin: "Tu es Mathurin, boulanger catholique, voisin et ami de Suzanne, en 1598. Tu es jovial, tu vouvoies les élèves, tu expliques l'édit de Nantes : ce qu'il permet aux protestants, ce qu'il limite, et pourquoi c'est un pacte de paix (la tolérance). Réponses de 2 à 4 phrases.",
      margot: "Tu es Margot, 11 ans, aide-jardinière dans l'équipe d'André Le Nôtre, à Versailles, en 1682. Tu tutoies les joueurs, tu parles des jardins à la française, du château, de la galerie des Glaces et du symbole du Soleil. Tu rappelles que Versailles coûte très cher. Réponses de 2 à 4 phrases.",
      isabeau: "Tu es Dame Isabeau, dame de la cour de Louis XIV, à Versailles. Tu es posée, tu vouvoies les élèves, tu expliques la journée du roi (lever, messe, conseil, dîner, promenade ou chasse, appartement, souper, coucher) et l'étiquette. Tu précises qu'au XVIIe siècle le dîner est le repas de midi. Réponses de 2 à 4 phrases."
    },
    persoDefaut: "gabriel",
    presentation: false,
    contexte: "Escape game d'histoire sur la monarchie en France : Henri IV et l'édit de Nantes (la naissance du protestantisme), Louis XIV, le Roi-Soleil à Versailles (la monarchie absolue)",
    regles: [
      "N'invente aucun fait historique ni aucune date.",
      "N'attribue pas « L'État, c'est moi » à Louis XIV ni « Paris vaut bien une messe » à Henri IV sans préciser que rien ne prouve qu'ils les aient dites.",
      "Évoque les violences religieuses avec sobriété, sans détail choquant."
    ],
    systeme: "Tu es un assistant pédagogique spécialisé en histoire de la France moderne (XVIe-XVIIe siècles), destiné à des élèves de primaire (CM1-CM2) en France. Tu restes factuel, strictement neutre sur le plan religieux et politique, bienveillant et adapté à l'âge."
  },

  /* Bouton de leçon des énigmes (enigmes.js) */
  enigmes: { libelleBoutonLecon: "📚 Leçon", titreBoutonLecon: "Ouvrir la leçon liée à cette énigme" },

  /* Textes des impressions : bilan, fiches, QCM (impression.js) */
  impression: {
    mentions: ["🏆 Grand secrétaire du roi", "🥈 Secrétaire du cabinet", "🥉 Clerc des archives", "📜 Apprenti secrétaire"],
    sousTitre: "Escape game d'histoire · l'édit de Nantes, Louis XIV et Versailles · cycle 3",
    libelleMotsCles: "🔏 Mots des sceaux",
    logo: "🏛️",
    pied: "De l'édit de Nantes à Versailles · la monarchie en France · cycle 3",
    motSalle: "Salle",
    contexte: "📜 Contexte historique",
    titreQcm: "Henri IV, l'édit de Nantes, Louis XIV et Versailles",
    theme: "la monarchie en France, de l'édit de Nantes à Versailles"
  }
};
