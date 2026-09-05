/* =========================================================
   PÉRIODE 4 — SE NOURRIR (suite) ET LE RELIEF DE LA FRANCE
   Séances 11 à 13 (livret papier : pages 9, 7 et 3)
   ========================================================= */

/* ---------------------------------------------------------
   SÉANCE 11 — Chaînes de production  (livret p. 9)
   --------------------------------------------------------- */
MISSION.session({
  id: "s11", numero: 11, periode: 4, livret: 9,
  titre: "Chaînes de production",
  lieu: "Ferme de Bray, puis usine d'Issenheim",
  theme: "Se nourrir",
  element: "La chaîne de production d'un aliment consommé : le yaourt",
  duree: 50,
  lecon: "l11",

  intro: {
    texte: `<p>Les malfaiteurs sont partout en France : tu suis leurs petits cailloux.
      Pour t'approcher, tu te fais passer pour un producteur de la <b>ferme de Bray</b>
      et tu suis le lait qu'elle vend.</p>
      <p>Cap sur l'usine de yaourts d'<b>Issenheim</b>, en Alsace.</p>`,
    media: { base: "s11-intro", legende: "La ferme de Bray" }
  },

  activites: [
    {
      type: "ordre",
      consigne: "Remets le trajet du lait dans l'ordre, de la production à la consommation du yaourt.",
      points: 5,
      media: { base: "s11-etapes", legende: "Les huit étapes, dans le désordre" },
      items: [
        { id: "e1", texte: "Les vaches pâturent au pré" },
        { id: "e2", texte: "La traite : le lait est recueilli, puis refroidi" },
        { id: "e3", texte: "Le camion-citerne réfrigéré collecte le lait" },
        { id: "e4", texte: "Le lait arrive à l'usine et il est analysé" },
        { id: "e5", texte: "Le lait est chauffé, ensemencé de ferments, puis il repose" },
        { id: "e6", texte: "Le yaourt est versé dans des pots, qui sont operculés" },
        { id: "e7", texte: "Un camion frigorifique livre les magasins" },
        { id: "e8", texte: "Le yaourt est vendu au rayon frais du supermarché" }
      ],
      ordre: ["e1","e2","e3","e4","e5","e6","e7","e8"],
      aide: "Tout part du pré et tout finit dans ton frigo. Entre les deux : un camion, l'usine, un autre camion."
    },
    {
      type: "trous",
      consigne: "Avant de te laisser entrer, le directeur te donne ce texte à trous à remplir.",
      precision: "Attention, deux mots de la liste ne servent à rien.",
      points: 5,
      intrus: ["congelé", "cuit"],
      texte: `Tout commence à la [[ferme]]. Les vaches produisent le lait chaque jour.
        Le lait est [[trait]] puis immédiatement refroidi. Il est ensuite transporté
        dans un camion-citerne [[réfrigéré]] jusqu'à l'[[usine]].
        À l'usine, le lait est [[analysé]] et stocké dans de grands réservoirs.
        Le lait est alors chauffé, des ferments sont ajoutés et le mélange repose :
        le yaourt [[fermente]]. Le yaourt est versé dans des [[pots]] et fermé avec un
        couvercle. Il est ensuite transporté jusqu'aux [[supermarchés]].
        Enfin, il est vendu en [[magasin]] et arrive dans ton frigo !`,
      aide: "Le lait n'est jamais congelé ni cuit : il est refroidi, transporté au frais, puis chauffé doucement."
    },
    {
      type: "saisie",
      consigne: "Combien d'étapes se déroulent à l'intérieur de l'usine ?",
      points: 2,
      champs: [{ label: "Nombre d'étapes se passant à l'usine", solution: "3" }],
      aide: "Reprends la liste : l'analyse, la transformation et la mise en pots ont lieu à l'usine."
    },
    {
      type: "ouverte",
      consigne: "À ton avis, que se passerait-il si le lait n'était pas transporté au frais jusqu'à l'usine ?",
      points: 3,
      minimum: 20,
      pistes: [
        "Des micro-organismes se développeraient dans le lait.",
        "Le lait tournerait, il deviendrait aigre et impropre à la consommation.",
        "Il faudrait le jeter : perte pour l'agriculteur et pour l'usine.",
        "La chaîne du froid protège la santé des consommateurs."
      ]
    },
    {
      type: "qcm",
      consigne: "Dans quel secteur d'activité classe-t-on l'usine de yaourts ?",
      disposition: "liste",
      points: 2,
      options: [
        { texte: "Secteur primaire : elle exploite une ressource naturelle", correct: false },
        { texte: "Secteur secondaire : elle transforme une matière première", correct: true },
        { texte: "Secteur tertiaire : elle rend un service", correct: false }
      ],
      aide: "Souviens-toi de la séance de Besançon : transformer, c'est du secondaire."
    }
  ],

  mediaCoeur: { base: "s11-coeur", legende: "Dans l'usine" },

  fin: {
    texte: `<p>Dans le vestiaire de l'usine, une radio grésille dans une langue que tu
      ne comprends pas… mais que tu reconnais.</p>`,
    media: { base: "s11-fin" }
  },

  indice: {
    type: "fait",
    texte: "Dans le pays recherché, on parle espagnol.",
    libelle: "Radio entendue dans le vestiaire de l'usine"
  }
});

/* ---------------------------------------------------------
   SÉANCE 12 — L'heure du ravitaillement  (livret p. 7)
   --------------------------------------------------------- */
MISSION.session({
  id: "s12", numero: 12, periode: 4, livret: 7,
  titre: "L'heure du ravitaillement",
  lieu: "Marseille, Provence-Alpes-Côte d'Azur",
  theme: "Se nourrir",
  element: "La provenance des aliments et les kilomètres alimentaires",
  duree: 55,
  lecon: "l12",

  intro: {
    texte: `<p>De retour à Marseille, tu te rends compte que nous avons la chance d'habiter
      un pays où la nourriture est abondante…</p>
      <p>Mais en lisant les étiquettes du marché, une question surgit : combien de kilomètres
      ces aliments ont-ils parcourus avant d'arriver dans ton panier ?</p>`,
    media: { base: "s12-intro", legende: "Un étal de marché" }
  },

  activites: [
    {
      type: "tri",
      consigne: "Classe chaque produit selon le continent d'où il vient.",
      points: 5,
      media: { base: "s12-etals", legende: "Les étiquettes du marché" },
      paniers: [
        { id: "eu", titre: "Europe" },
        { id: "af", titre: "Afrique" },
        { id: "as", titre: "Amérique du Sud" },
        { id: "asie", titre: "Asie" },
        { id: "oc", titre: "Océanie" }
      ],
      items: [
        { id: "p1", texte: "Fraises (Espagne)",            panier: "eu" },
        { id: "p2", texte: "Avocats (Espagne)",            panier: "eu" },
        { id: "p3", texte: "Salade (Espagne)",             panier: "eu" },
        { id: "p4", texte: "Feta (Grèce)",                 panier: "eu" },
        { id: "p5", texte: "Myrtilles (Portugal)",         panier: "eu" },
        { id: "p6", texte: "Figues (Italie)",              panier: "eu" },
        { id: "p7", texte: "Bananes (Cameroun)",           panier: "af" },
        { id: "p8", texte: "Oranges (Afrique du Sud)",     panier: "af" },
        { id: "p9", texte: "Tomates (Maroc)",              panier: "af" },
        { id: "p10",texte: "Citrons (Argentine)",          panier: "as" },
        { id: "p11",texte: "Poires (Chili)",               panier: "as" },
        { id: "p12",texte: "Mangues (Brésil)",             panier: "as" },
        { id: "p13",texte: "Noisettes (Turquie)",          panier: "asie" },
        { id: "p14",texte: "Kiwis (Nouvelle-Zélande)",     panier: "oc" }
      ],
      aide: "Le Maroc est en Afrique du Nord ; la Turquie se trouve surtout en Asie."
    },
    {
      type: "saisie",
      consigne: "Calcule les kilomètres alimentaires nécessaires pour réaliser cette salade.",
      points: 5,
      document: `<p><b>Recette — salade fraîcheur :</b> 1 poire (Chili) • 100 g de feta (Grèce) •
        1 salade (Espagne) • 100 g de noisettes (Turquie) • 200 g de tomates (Maroc).</p>
        <div class="enveloppe-tableau"><table class="donnees">
        <tr><th>Distance jusqu'en France</th><th>Chili</th><th>Grèce</th><th>Espagne</th><th>Turquie</th><th>Maroc</th></tr>
        <tr><th>en kilomètres</th><td>11 702</td><td>2 585</td><td>1 013</td><td>3 422</td><td>2 292</td></tr>
        </table></div>`,
      champs: [
        { label: "Total des kilomètres alimentaires de la recette", solution: "21014", tolerance: 0, unite: "km" },
        { label: "Chiffre des unités de ce total", solution: "4" },
        { label: "Nombre de produits du marché issus d'Amérique du Sud", solution: "3" }
      ],
      aide: "11 702 + 2 585 + 1 013 + 3 422 + 2 292. Pose l'addition en colonnes !"
    },
    {
      type: "qcm",
      consigne: "Pour réduire ces kilomètres alimentaires, on peut…",
      precision: "Plusieurs réponses attendues.",
      multiple: true,
      points: 4,
      options: [
        { texte: "manger moins de viande", correct: true },
        { texte: "acheter en circuit court", correct: true },
        { texte: "acheter des fruits et légumes de saison", correct: true },
        { texte: "manger moins d'aliments salés", correct: false },
        { texte: "ne pas laver les fruits et légumes", correct: false },
        { texte: "privilégier la consommation de produits locaux", correct: true }
      ],
      aide: "Quatre bonnes réponses. Deux propositions n'ont aucun rapport avec la distance parcourue."
    },
    {
      type: "ouverte",
      consigne: "Un kiwi de Nouvelle-Zélande a parcouru plus de 19 000 km. Propose deux façons de le remplacer dans un goûter, sans perdre en vitamines.",
      points: 2,
      minimum: 15,
      pistes: [
        "Un kiwi français (Adour, Corse) : même fruit, quelques centaines de kilomètres.",
        "Une orange, un pamplemousse ou une clémentine d'Espagne ou de Corse en hiver.",
        "Choisir un fruit de saison produit près de chez soi."
      ]
    }
  ],

  mediaCoeur: { base: "s12-coeur", legende: "D'où viennent nos aliments ?" },

  fin: {
    texte: `<p>21 014 kilomètres pour une seule salade. Le chiffre des unités de ce total
      rejoint ton carnet : il te servira plus tard.</p>`,
    media: { base: "s12-fin" }
  },

  indice: {
    type: "nombre", symbole: "hexagone", valeur: 4,
    libelle: "Chiffre des unités des kilomètres alimentaires"
  }
});

/* ---------------------------------------------------------
   SÉANCE 13 — L'eau en France : fleuves et massifs (livret p. 3)
   --------------------------------------------------------- */
MISSION.session({
  id: "s13", numero: 13, periode: 4, livret: 3,
  titre: "L'eau en France : fleuves et massifs",
  lieu: "Les Alpes",
  theme: "Les usages de l'eau douce",
  element: "Repérer les principaux fleuves et massifs montagneux",
  duree: 50,
  lecon: "l13",

  intro: {
    texte: `<p>La piste des produits agricoles n'a rien donné. Tu décides de suivre ta
      dernière piste : <b>l'eau</b>.</p>
      <p>Tu te rends dans les <b>Alpes</b> pour comprendre d'où elle vient. Avant tout,
      il faut savoir lire une carte du relief et des cours d'eau.</p>`,
    media: { base: "s13-intro", legende: "Un torrent alpin" }
  },

  activites: [
    {
      type: "etiquettes",
      consigne: "Replace les étiquettes des fleuves et des massifs au bon endroit.",
      precision: "Cinq fleuves (en bleu sur la carte) et six massifs montagneux (en brun).",
      points: 6,
      fond: { decor: "france-fleuves", base: "carte-fleuves-montagnes",
              alt: "La France, fleuves et montagnes" },
      zones: [
        { x: 50.3, y: 24.2, etiquette: "La Seine" },
        { x: 39.7, y: 38.1, etiquette: "La Loire" },
        { x: 32.3, y: 63.5, etiquette: "La Garonne" },
        { x: 66.5, y: 63.5, etiquette: "Le Rhône" },
        { x: 89.7, y: 23.1, etiquette: "Le Rhin" },
        { x: 78.4, y: 34.2, etiquette: "Les Vosges" },
        { x: 72.9, y: 46.2, etiquette: "Le Jura" },
        { x: 76.5, y: 61.2, etiquette: "Les Alpes" },
        { x: 52.9, y: 61.2, etiquette: "Le Massif central" },
        { x: 39.7, y: 81.5, etiquette: "Les Pyrénées" },
        { x: 93.5, y: 90.4, etiquette: "La Corse" }
      ],
      aide: "La Seine traverse Paris, au nord. La Garonne descend des Pyrénées vers l'Atlantique."
    },
    {
      type: "qcm",
      consigne: "Quelle est la différence entre un fleuve et une rivière ?",
      disposition: "liste",
      points: 2,
      options: [
        { texte: "Un fleuve est plus long qu'une rivière.", correct: false },
        { texte: "Un fleuve se jette dans la mer ou l'océan ; une rivière se jette dans un autre cours d'eau.", correct: true },
        { texte: "Un fleuve prend sa source en montagne, une rivière en plaine.", correct: false },
        { texte: "Un fleuve est plus large qu'une rivière.", correct: false }
      ],
      aide: "Ce n'est pas une question de taille, mais de destination."
    },
    {
      type: "relier",
      consigne: "Relie chaque fleuve à la mer ou à l'océan dans lequel il se jette.",
      points: 4,
      gauche: [
        { id: "f1", texte: "La Seine" },
        { id: "f2", texte: "La Loire" },
        { id: "f3", texte: "La Garonne" },
        { id: "f4", texte: "Le Rhône" },
        { id: "f5", texte: "Le Rhin" }
      ],
      droite: [
        { id: "m1", texte: "La Manche" },
        { id: "m2", texte: "L'océan Atlantique (estuaire de la Loire)" },
        { id: "m3", texte: "L'océan Atlantique (estuaire de la Gironde)" },
        { id: "m4", texte: "La mer Méditerranée" },
        { id: "m5", texte: "La mer du Nord" }
      ],
      paires: [["f1","m1"],["f2","m2"],["f3","m3"],["f4","m4"],["f5","m5"]],
      aide: "Le Rhône descend vers le sud : il ne peut se jeter que dans la Méditerranée."
    },
    {
      type: "saisie",
      consigne: "Quelques repères à connaître par cœur.",
      points: 4,
      champs: [
        { label: "Nombre de grands massifs montagneux en France", solution: "6" },
        { label: "Le plus long fleuve de France", texte: true, solution: "la Loire", variantes: ["Loire"] },
        { label: "Altitude du mont Blanc, en mètres", solution: "4806", tolerance: 10 },
        { label: "Massif situé à la frontière avec l'Espagne", texte: true,
          solution: "les Pyrénées", variantes: ["Pyrénées", "Pyrenees"] }
      ],
      aide: "Alpes, Pyrénées, Massif central, Jura, Vosges, Corse : compte-les."
    }
  ],

  mediaCoeur: { base: "s13-coeur", decor: "france-fleuves", legende: "Fleuves et massifs de France" },

  fin: {
    texte: `<p>Six massifs, cinq fleuves. La carte de France n'a plus de secret pour toi.
      Le nombre de massifs rejoint ton carnet.</p>`,
    media: { base: "s13-fin" }
  },

  indice: {
    type: "nombre", symbole: "losange", valeur: 6,
    libelle: "Nombre de grands massifs montagneux français"
  }
});
