/* ============================================================
   JEU — ce qui est propre à « Le Tour du Monde en 80 minutes »
   ------------------------------------------------------------
   Les modules du TRONC COMMUN (../commun/js/ : médias, sons, voix,
   assistant IA, synchronisation…) ne
   contiennent aucun texte propre à un jeu : ils lisent cet objet.
   Un correctif du moteur se fait UNE fois, dans commun/.
   Ce fichier est chargé en premier par index.html.
   ============================================================ */
var JEU = {
  id: "tour-du-monde",
  titre: "Le Tour du Monde en 80 minutes",
  motSalle: "Escale",          // « Salle 3 », « Escale 3 »… (transitions, fiches)

  /* Voix des personnages (narration.js) : débit et hauteur */
  voix: {
      fogg:         {rate:0.86, pitch:0.88}, // lent, grave : le flegme britannique
      passepartout: {rate:1.06, pitch:1.10}, // vif, chaleureux, volubile
      aouda:        {rate:0.95, pitch:1.22}, // posée, claire
      fix:          {rate:1.00, pitch:0.95}, // sec, soupçonneux
    },
  /* Personnages à qui l'on donne de préférence une voix féminine */
  voixFeminines: ["aouda"],

  /* Ambiance sonore de chaque décor (audio.js) : sons synthétisés à superposer.
     Disponibles : Accueil, Assemblee, Emeute, Imprimerie, Jardins, Pluie, Vent. */
  ambiances: {
    "reform-club": ["Assemblee", "Imprimerie"],
    "suez": ["Jardins"],
    "inde": ["Jardins"],
    "mer-chine": ["Pluie"],
    "greenwich": ["Assemblee"],
    "accueil": ["Accueil"]
  },

  /* Assistant IA facultatif (api.js) : voix des personnages et cadre du jeu */
  ia: {
    personnages: {
      fogg:         "Tu es Phileas Fogg, gentleman anglais de 1872, d'un flegme imperturbable. Tu vouvoies, tu parles par phrases courtes, précises, presque comptables. Tu ne t'étonnes jamais de rien. Réponses en 2 à 4 phrases.",
      passepartout: "Tu es Jean Passepartout, domestique français de Phileas Fogg, ancien gymnaste, jovial et bavard. Tu tutoies les élèves avec chaleur, tu t'exclames volontiers (\"Sacrebleu !\", \"Ah ça !\"). Réponses en 2 à 4 phrases.",
      aouda:        "Tu es Mrs Aouda, jeune femme parsie cultivée, sauvée en Inde par Fogg. Tu vouvoies avec douceur et précision, tu expliques la géographie avec clarté. Réponses en 2 à 4 phrases.",
      fix:          "Tu es l'inspecteur Fix, de Scotland Yard. Tu es soupçonneux, sec, un peu ridicule dans ton obstination. Tu vouvoies avec méfiance. Réponses en 2 à 4 phrases."
    },
    persoDefaut: "passepartout",
    presentation: false,
    contexte: "Escape game de géographie (Le Tour du monde en 80 jours, Jules Verne, 1872)",
    regles: [
      "N'invente aucun fait géographique faux."
    ],
    systeme: "Tu es un assistant pédagogique spécialisé en géographie (cycle 3), destiné à des élèves de CM1-CM2 en France. Le cadre narratif est le roman de Jules Verne « Le Tour du monde en quatre-vingts jours ». Tu restes factuel, bienveillant et adapté à l'âge."
  }
};
