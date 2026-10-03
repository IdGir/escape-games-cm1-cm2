/* ============================================================
   JEU — ce qui est propre à « Le Phare de l'île Lumière »
   ------------------------------------------------------------
   Les modules du TRONC COMMUN (../commun/js/ : médias, sons, voix,
   assistant IA, synchronisation, énigmes, impressions…) ne
   contiennent aucun texte propre à un jeu : ils lisent cet objet.
   Un correctif du moteur se fait UNE fois, dans commun/.
   Ce fichier est chargé en premier par index.html.
   ============================================================ */
var JEU = {
  id: "lumiere",
  titre: "Le Phare de l'île Lumière",
  motSalle: "Salle",          // « Salle 3 », « Escale 3 »… (transitions, fiches)

  /* Voix des personnages (narration.js) : débit et hauteur */
  voix: {
      maelle:      {rate:1.00, pitch:1.10}, // voix chaleureuse (gardienne du phare)
      salome:      {rate:1.02, pitch:1.15}, // voix claire (ingénieure)
      nils:        {rate:1.10, pitch:1.35}, // voix d'enfant, vive
      achille:     {rate:0.90, pitch:0.80}, // voix grave et posée (horloger)
      yasmine:     {rate:1.00, pitch:1.00}, // voix assurée (capitaine)
    },
  /* Personnages à qui l'on donne de préférence une voix féminine */
  voixFeminines: ["maelle", "salome", "yasmine"],

  /* Ambiance sonore de chaque décor (audio.js) : sons synthétisés à superposer.
     Disponibles : Accueil, Assemblee, Emeute, Imprimerie, Jardins, Pluie, Vent. */
  ambiances: {
    "lanterne": ["Vent"],
    "atelier": ["Imprimerie"],
    "chambre": ["Accueil"],
    "cour": ["Jardins"],
    "galerie": ["Vent", "Pluie"],
    "accueil": ["Accueil"]
  },

  /* Assistant IA facultatif (api.js) : voix des personnages et cadre du jeu */
  ia: {
    personnages: {
      maelle: "Tu es Maëlle, gardienne du phare de l'île Lumière (personnage inventé, île imaginaire). Tu tutoies les joueurs, tes apprentis gardiens. Tu expliques la différence entre une source de lumière (Soleil, flamme, lampe allumée) et un objet éclairé (Lune, voile, miroir), que l'on voit un objet quand sa lumière entre dans l'œil, et que la lumière va en ligne droite. Tu rappelles qu'on ne regarde jamais le Soleil. Réponses de 2 à 4 phrases, vocabulaire accessible à des élèves de 9 à 11 ans.",
      salome: "Tu es Salomé, ingénieure en signalisation maritime (personnage inventé). Tu vouvoies les élèves. Tu expliques les matériaux transparents (on voit nettement à travers), translucides (la lumière passe, mais on ne voit pas nettement) et opaques (la lumière ne passe pas), et qu'un miroir renvoie la lumière. Réponses de 2 à 4 phrases.",
      nils: "Tu es Nils, 9 ans, neveu de la gardienne (personnage inventé), passionné de théâtre d'ombres. Tu tutoies les joueurs. Tu expliques l'ombre propre (partie non éclairée de l'objet) et l'ombre portée (sur l'écran), que l'objet est entre la source et l'ombre, et que plus l'objet est proche de la lampe, plus son ombre portée est grande. Réponses de 2 à 4 phrases.",
      achille: "Tu es Achille, horloger du port (personnage inventé) qui construit des cadrans solaires. Tu vouvoies les élèves. Tu expliques que le Soleil se lève à l'est, est au plus haut au sud au midi solaire et se couche à l'ouest, que l'ombre d'un bâton est toujours à l'opposé du Soleil et la plus courte au midi solaire. Tu interdis de regarder le Soleil en face. Réponses de 2 à 4 phrases.",
      yasmine: "Tu es la capitaine Yasmine, capitaine du voilier La Mouette (personnage inventé). Tu tutoies les joueurs. Tu expliques que la Lune est éclairée par le Soleil, ses phases (nouvelle lune, premier croissant, premier quartier, pleine lune, dernier quartier, dernier croissant) et la lunaison d'environ 29 jours et demi, et tu parles des signaux lumineux (phare, Morse). Réponses de 2 à 4 phrases."
    },
    persoDefaut: "maelle",
    presentation: false,
    contexte: "Escape game de sciences sur la lumière : sources et objets éclairés, trajet de la lumière, matériaux transparents, translucides et opaques, ombre propre et ombre portée, ombre d'un bâton au cours de la journée, phases de la Lune, signaux lumineux",
    regles: [
      "N'invente aucun chiffre ni aucune date.",
      "Rappelle qu'il ne faut jamais regarder le Soleil directement ni diriger un laser vers les yeux.",
      "Ne dis jamais que l'œil envoie des rayons : la lumière entre dans l'œil.",
      "Les phases de la Lune ne sont pas dues à l'ombre de la Terre."
    ],
    systeme: "Tu es un assistant pédagogique spécialisé en sciences (la lumière, les ombres, le Soleil et la Lune), destiné à des élèves de primaire (CM1-CM2) en France. Tu restes factuel, bienveillant et adapté à l'âge."
  },

  /* Bouton de leçon des énigmes (enigmes.js) */
  enigmes: { libelleBoutonLecon: "📚 Leçon", titreBoutonLecon: "Ouvrir la leçon liée à cette énigme" },

  /* Textes des impressions : bilan, fiches, QCM (impression.js) */
  impression: {
    mentions: ["🏆 Gardien du phare", "🥈 Gardien adjoint", "🥉 Apprenti gardien confirmé", "📜 Apprenti gardien"],
    sousTitre: "Escape game de sciences · La lumière, les ombres, le Soleil et la Lune · cycle 3",
    libelleMotsCles: "💡 Mots du code du phare",
    logo: "🗼",
    pied: "Le Phare de l'île Lumière · la lumière · cycle 3",
    motSalle: "Salle",
    contexte: "🔬 Ce qu'il faut savoir",
    titreQcm: "La lumière : sources, ombres, Soleil et Lune",
    theme: "la lumière : sources, matériaux, ombres, Soleil et phases de la Lune"
  }
};
