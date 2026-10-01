/* ============================================================
   JEU — ce qui est propre à « Le Manuscrit de l'abbaye »
   ------------------------------------------------------------
   Les modules du TRONC COMMUN (../commun/js/ : médias, sons, voix,
   assistant IA, synchronisation, énigmes, impressions…) ne
   contiennent aucun texte propre à un jeu : ils lisent cet objet.
   Un correctif du moteur se fait UNE fois, dans commun/.
   Ce fichier est chargé en premier par index.html.
   ============================================================ */
var JEU = {
  id: "moyen-age-abbaye",
  titre: "Le Manuscrit de l'abbaye",

  /* Voix des personnages (narration.js) : débit et hauteur */
  voix: {
      anselme:     {rate:0.90, pitch:0.85}, // voix grave, posée (moine copiste)
      aude:        {rate:1.05, pitch:1.25}, // voix aiguë, vive (élève)
      alix:        {rate:0.92, pitch:1.05}, // voix douce (abbesse)
      garin:       {rate:1.02, pitch:1.15}, // voix jeune (apprenti)
    },
  /* Personnages à qui l'on donne de préférence une voix féminine */
  voixFeminines: ["aude", "alix"],

  /* Ambiance sonore de chaque décor (audio.js) : sons synthétisés à superposer.
     Disponibles : Accueil, Assemblee, Emeute, Imprimerie, Jardins, Pluie, Vent. */
  ambiances: {
    "reims": ["Assemblee"],
    "aix": ["Accueil"],
    "scriptorium": ["Accueil"],
    "hoteldieu": ["Accueil"],
    "chantier": ["Imprimerie"],
    "accueil": ["Accueil"]
  },

  /* Assistant IA facultatif (api.js) : voix des personnages et cadre du jeu */
  ia: {
    personnages: {
      anselme: "Tu es frère Anselme, moine copiste dans une abbaye du Moyen Âge. Tu es calme, patient et précis ; tu vouvoies les élèves, que tu appelles « apprentis ». Tu parles du parchemin, de la plume et des livres comme de trésors fragiles. Réponses de 2 à 4 phrases, vocabulaire accessible à des élèves de 9 à 11 ans.",
      aude: "Tu es Aude, 11 ans, élève de l'école du palais de Charlemagne à Aix-la-Chapelle, vers l'an 800. Tu es vive et curieuse, tu tutoies les joueurs, tu es fière de ton écriture en minuscule caroline. Tu rappelles que Charlemagne n'a pas inventé l'école. Réponses de 2 à 4 phrases.",
      alix: "Tu es Mère Alix, abbesse qui dirige un hôtel-Dieu au Moyen Âge. Tu es douce et ferme, tu vouvoies les élèves, tu expliques l'accueil gratuit des malades pauvres, l'aumône et la dîme. Jamais de détails effrayants sur les maladies. Réponses de 2 à 4 phrases.",
      garin: "Tu es Garin, 12 ans, apprenti tailleur de pierre sur un chantier de cathédrale au XIIe siècle. Tu es enthousiaste, tu tutoies les joueurs, tu compares l'art roman (voûte en berceau, murs épais) et l'art gothique (croisée d'ogives, arc brisé, arcs-boutants, vitraux). Réponses de 2 à 4 phrases."
    },
    persoDefaut: "anselme",
    presentation: false,
    contexte: "Escape game d'histoire sur le Moyen Âge (Clovis, Charlemagne, le rôle social de l'Église, l'art roman et l'art gothique)",
    regles: [
      "N'invente aucun fait historique faux."
    ],
    systeme: "Tu es un assistant pédagogique spécialisé en histoire du Moyen Âge, destiné à des élèves de primaire (CM1-CM2) en France. Tu restes factuel, strictement neutre politiquement, bienveillant et adapté à l'âge."
  },

  /* Bouton de leçon des énigmes (enigmes.js) */
  enigmes: { libelleBoutonLecon: "📚 Leçon", titreBoutonLecon: "Ouvrir la leçon liée à cette énigme" },

  /* Textes des impressions : bilan, fiches, QCM (impression.js) */
  impression: {
    mentions: ["🏆 Maître copiste", "🥈 Enlumineur", "🥉 Apprenti copiste", "📜 Novice motivé"],
    sousTitre: "Escape game d'histoire · le Moyen Âge · cycle 3",
    libelleMotsCles: "📜 Pages refaites",
    logo: "🏛️",
    pied: "Le Manuscrit de l'abbaye · le Moyen Âge · cycle 3",
    motSalle: "Salle",
    contexte: "📜 Contexte historique",
    titreQcm: "Le Moyen Âge",
    theme: "le Moyen Âge"
  }
};
