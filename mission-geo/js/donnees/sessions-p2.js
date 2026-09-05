/* =========================================================
   PÉRIODE 2 — Une seconde région littorale, puis le monde
   Séances 6 à 8 (livret papier : pages 10, 12, 2)
   ========================================================= */

/* ---------------------------------------------------------
   SÉANCE 6 — Étretat, station balnéaire  (livret p. 10)
   --------------------------------------------------------- */
MISSION.session({
  id: "s06", numero: 6, periode: 2, livret: 10,
  titre: "Étretat, station balnéaire",
  lieu: "Étretat, Normandie",
  theme: "L'organisation du territoire français",
  element: "Caractéristiques d'une seconde région : le littoral touristique normand",
  duree: 50,
  lecon: "l06",

  intro: {
    texte: `<p>Tu es descendu(e) trop au sud. Tu remontes vers la Normandie, à
      <b>Étretat</b>, célèbre pour ses falaises et son Aiguille creuse.</p>
      <p>Pour gagner la confiance d'une source, tu te fais passer pour un guide
      touristique. Il va donc falloir connaître la ville… et proposer à chaque visiteur
      l'activité qui lui convient.</p>`,
    media: { base: "s06-intro", legende: "Les falaises d'Étretat" }
  },

  activites: [
    {
      type: "relier",
      consigne: "Propose à chaque touriste l'activité qui correspond à ses goûts.",
      points: 4,
      document: `<p><b>Étretat, mode d'emploi.</b> Randonnées sur le <b>GR21</b>, promenade en paddle
        ou kayak au pied des arches. Le <b>Vélo rail</b> offre de nouvelles vues sur la ville.
        À voir aussi : le <b>Clos Lupin</b>, maison de l'auteur Maurice Leblanc, le château
        <b>les Aygues</b>, ancienne résidence d'été des reines d'Espagne, le <b>marché couvert</b>
        et ses boutiques de souvenirs, ou le parc des <b>Roches</b>, espace de loisirs familial.</p>`,
      gauche: [
        { id: "t1", texte: "Elena : « Mi chiamo Elena, amo lo sport ! »" },
        { id: "t2", texte: "Tom : « I'm Tom ! I love shopping ! »" },
        { id: "t3", texte: "Zac : « J'aime me balader en famille. »" },
        { id: "t4", texte: "Isabelle : « Je suis une grande fan de littérature ! »" },
        { id: "t5", texte: "Richard : « Je suis un passionné d'histoire. »" }
      ],
      droite: [
        { id: "a1", texte: "Le GR21 (randonnée sur les falaises)" },
        { id: "a2", texte: "Le marché couvert" },
        { id: "a3", texte: "Le parc des Roches" },
        { id: "a4", texte: "Le Clos Lupin" },
        { id: "a5", texte: "Le château les Aygues" },
        { id: "a6", texte: "Le Vélo rail" }
      ],
      paires: [["t1","a1"],["t2","a2"],["t3","a3"],["t4","a4"],["t5","a5"]],
      aide: "Maurice Leblanc est l'auteur d'Arsène Lupin : sa maison intéressera une lectrice."
    },
    {
      type: "ordre",
      consigne: "Remets les mots dans l'ordre pour retrouver la définition d'une station balnéaire.",
      points: 3,
      items: [
        { id: "m1", texte: "lieu" },
        { id: "m2", texte: "de" },
        { id: "m3", texte: "séjour" },
        { id: "m4", texte: "situé" },
        { id: "m5", texte: "en" },
        { id: "m6", texte: "bord" },
        { id: "m7", texte: "de" },
        { id: "m8", texte: "mer" }
      ],
      ordre: ["m1","m2","m3","m4","m5","m6","m7","m8"],
      aide: "La définition commence par « lieu » et se termine par « mer »."
    },
    {
      type: "saisie",
      consigne: "Combien de lettres compte le premier mot de cette définition ?",
      points: 2,
      champs: [{ label: "Nombre de lettres du premier mot", solution: "4" }],
      aide: "L-I-E-U."
    },
    {
      type: "tri",
      consigne: "Trie les conséquences de la fréquentation touristique pour les habitants d'Étretat.",
      points: 4,
      document: `<p>Derrière ses falaises, Étretat est l'été envahie par les touristes.
        Le front de mer est noir de monde, des kilomètres de voitures sont stationnées.
        Chaque année, les 1 200 habitants doivent cohabiter avec un million de visiteurs.
        En 20 ans, près de 400 habitants ont quitté la station balnéaire.
        <br><i>Source : Francetvinfo.fr, août 2022</i></p>`,
      media: { base: "s06-photos", legende: "Six photographies prises à Étretat" },
      paniers: [
        { id: "p", titre: "👍 Points positifs pour les habitants" },
        { id: "n", titre: "👎 Points négatifs pour les habitants" }
      ],
      items: [
        { id: "c1", texte: "Embouteillages et stationnement difficile", panier: "n" },
        { id: "c2", texte: "Déchets abandonnés sur le front de mer",    panier: "n" },
        { id: "c3", texte: "Création d'emplois dans les restaurants",   panier: "p" },
        { id: "c4", texte: "Augmentation du prix des logements",        panier: "n" },
        { id: "c5", texte: "Animations et fêtes dans la ville",         panier: "p" },
        { id: "c6", texte: "Nouveaux aménagements (promenades, sentiers)", panier: "p" }
      ],
      aide: "Trois points positifs et trois points négatifs."
    },
    {
      type: "ouverte",
      consigne: "Le maire d'Étretat installe des panneaux annonçant « Étretat saturée pendant deux heures ». Selon toi, pourquoi ? Est-ce une bonne idée ?",
      points: 2,
      minimum: 15,
      pistes: [
        "Réguler la surfréquentation : étaler les visites dans la journée.",
        "Éviter les embouteillages et préserver la tranquillité des habitants.",
        "Risque : décourager des visiteurs, donc moins de recettes pour les commerçants."
      ]
    }
  ],

  mediaCoeur: { base: "s06-coeur", legende: "L'Aiguille creuse" },

  fin: {
    texte: `<p>Ta couverture de guide a tenu. La source t'a soufflé un mot, et tu repars
      avec un nombre en tête : celui des lettres du premier mot de la définition.</p>`,
    media: { base: "s06-fin" }
  },

  indice: {
    type: "nombre", symbole: "pentagone", valeur: 4,
    libelle: "Nombre de lettres du premier mot de la définition"
  }
});

/* ---------------------------------------------------------
   SÉANCE 7 — Le littoral atlantique  (livret p. 12)
   --------------------------------------------------------- */
MISSION.session({
  id: "s07", numero: 7, periode: 2, livret: 12,
  titre: "Le littoral atlantique",
  lieu: "Biarritz, Nouvelle-Aquitaine",
  theme: "L'organisation du territoire français",
  element: "Les mers et océans bordant la France ; densité et population saisonnière",
  duree: 50,
  lecon: "l07",

  intro: {
    texte: `<p>La piste longe désormais les côtes françaises. Mais lesquelles ?
      La France est bordée par quatre grandes étendues d'eau, et tu dois savoir les nommer
      avant de choisir ta destination.</p>
      <p>Ton choix se portera finalement sur <b>Biarritz</b>, sur le littoral atlantique.</p>`,
    media: { base: "s07-intro", legende: "Le littoral atlantique" }
  },

  activites: [
    {
      type: "etiquettes",
      consigne: "Place le nom de chaque mer ou océan bordant la France.",
      points: 4,
      fond: { decor: "france-mers", base: "carte-mers", alt: "La France et ses mers" },
      zones: [
        { x: 58, y: 5,  etiquette: "Mer du Nord" },
        { x: 30, y: 11, etiquette: "La Manche" },
        { x: 11, y: 55, etiquette: "Océan Atlantique" },
        { x: 68, y: 91, etiquette: "Mer Méditerranée" }
      ],
      aide: "La Manche sépare la France du Royaume-Uni ; la mer du Nord est encore plus au nord."
    },
    {
      type: "tableau",
      consigne: "De quelle mer ou de quel océan parle-t-on ?",
      points: 5,
      entete: "Affirmation",
      colonnes: [{ titre: "Mer ou océan",
        options: ["Mer du Nord", "La Manche", "Océan Atlantique", "Mer Méditerranée"] }],
      lignes: [
        { titre: "On s'y baigne à Marseille.",                    solutions: ["Mer Méditerranée"] },
        { titre: "En le traversant, on arrive aux États-Unis.",   solutions: ["Océan Atlantique"] },
        { titre: "C'est la mer bordant la France la plus au sud.",solutions: ["Mer Méditerranée"] },
        { titre: "On s'y baigne en Aquitaine.",                   solutions: ["Océan Atlantique"] },
        { titre: "En la traversant, on arrive au Royaume-Uni.",   solutions: ["La Manche"] },
        { titre: "Elle se trouve au nord de la France et en Belgique.", solutions: ["Mer du Nord"] },
        { titre: "La Corse en est entourée.",                     solutions: ["Mer Méditerranée"] },
        { titre: "Il se situe à l'ouest de la France.",           solutions: ["Océan Atlantique"] },
        { titre: "On s'y baigne en Normandie.",                   solutions: ["La Manche"] }
      ],
      aide: "Un océan est bien plus vaste qu'une mer : l'Atlantique sépare deux continents."
    },
    {
      type: "relier",
      consigne: "Où vas-tu loger ? Relie chaque description au type d'hébergement.",
      points: 5,
      gauche: [
        { id: "h1", texte: "Une toile que l'on plante soi-même" },
        { id: "h2", texte: "Un véhicule aménagé, tracté par une voiture" },
        { id: "h3", texte: "Une maison de vacances louée entièrement" },
        { id: "h4", texte: "Un établissement avec réception et chambres numérotées" },
        { id: "h5", texte: "Un terrain aménagé pour tentes et caravanes" },
        { id: "h6", texte: "Une chambre chez l'habitant, petit-déjeuner compris" },
        { id: "h7", texte: "Une maison préfabriquée posée sur un terrain de camping" },
        { id: "h8", texte: "Des logements avec animations et clubs pour enfants" },
        { id: "h9", texte: "Un hébergement bon marché pour jeunes voyageurs" },
        { id: "h10",texte: "Un appartement loué à la semaine" }
      ],
      droite: [
        { id: "r1", texte: "une tente" },
        { id: "r2", texte: "une caravane" },
        { id: "r3", texte: "un gîte" },
        { id: "r4", texte: "un hôtel" },
        { id: "r5", texte: "un camping" },
        { id: "r6", texte: "une chambre d'hôtes" },
        { id: "r7", texte: "un mobil-home" },
        { id: "r8", texte: "un village de vacances" },
        { id: "r9", texte: "une auberge de jeunesse" },
        { id: "r10",texte: "une location" }
      ],
      paires: [["h1","r1"],["h2","r2"],["h3","r3"],["h4","r4"],["h5","r5"],
               ["h6","r6"],["h7","r7"],["h8","r8"],["h9","r9"],["h10","r10"]],
      aide: "Le mobil-home ne se déplace pas tout seul : il est posé et reste sur place."
    },
    {
      type: "saisie",
      consigne: "Mais que de monde ! Calcule la densité de population d'Étretat, hors vacances puis pendant l'été.",
      points: 4,
      document: `<p>Étretat fait en moyenne <b>4 km²</b>. La ville compte environ
        <b>1 100 habitants</b>. Sauf que l'été, elle accueille <b>15 000 touristes</b> en plus !</p>`,
      champs: [
        { label: "Densité hors vacances", solution: "275", tolerance: 1, unite: "hab/km²" },
        { label: "Densité pendant l'été", solution: "4025", tolerance: 5, unite: "hab/km²" },
        { label: "L'été, la densité est environ multipliée par", solution: "15", tolerance: 1 }
      ],
      aide: "Hors vacances : 1 100 ÷ 4. L'été : (1 100 + 15 000) ÷ 4. Puis compare les deux résultats."
    }
  ],

  mediaCoeur: { base: "s07-coeur", legende: "La grande plage de Biarritz" },

  fin: {
    texte: `<p>Multipliée par quinze ! Voilà ce que le tourisme fait à une petite commune
      du littoral. Un nouveau nombre rejoint ton carnet.</p>`,
    media: { base: "s07-fin" }
  },

  indice: {
    type: "nombre", symbole: "trapeze", valeur: 15,
    libelle: "Coefficient multiplicateur de la densité en été"
  }
});

/* ---------------------------------------------------------
   SÉANCE 8 — Niveaux de vie dans le monde  (livret p. 2)
   --------------------------------------------------------- */
MISSION.session({
  id: "s08", numero: 8, periode: 2, livret: 2,
  titre: "Niveaux de vie dans le monde",
  lieu: "Bangladesh",
  theme: "Les inégalités dans le monde",
  element: "Identifier les manifestations des inégalités de niveau de vie et les localiser sur un planisphère",
  duree: 55,
  lecon: "l08",

  intro: {
    texte: `<p>La piste de ta source t'emmène au <b>Bangladesh</b>. Là-bas, tu te rends
      compte que la misère est omniprésente.</p>
      <p>Tu réalises alors que tout le monde n'a pas le même niveau de vie… et tu cherches
      à comprendre pourquoi.</p>`,
    media: { base: "s08-intro", legende: "Dhaka, Bangladesh" }
  },

  activites: [
    {
      type: "vraifaux",
      consigne: "Lis la carte des inégalités de richesse, puis réponds par vrai ou faux.",
      points: 4,
      media: { base: "carte-richesses", decor: "planisphere-richesses",
               legende: "Doc. 1 : Les inégalités de richesse dans le monde" },
      items: [
        { texte: "L'Europe est majoritairement composée de pays riches.", reponse: true },
        { texte: "L'Afrique est le continent où l'on trouve le plus de pays pauvres.", reponse: true },
        { texte: "Le Canada est classé parmi les pays riches.", reponse: true },
        { texte: "Toute l'Asie est composée de pays très pauvres.", reponse: false },
        { texte: "Il n'existe aucun pays pauvre en Afrique du Nord.", reponse: false },
        { texte: "La carte montre que tous les pays du monde ont le même niveau de richesse.", reponse: false }
      ],
      aide: "Observe bien les couleurs de la légende avant de répondre : l'Asie n'est pas d'une seule couleur."
    },
    {
      type: "qcm",
      consigne: "Le célèbre gâteau de la caricature de Selçuk représente…",
      points: 2,
      disposition: "liste",
      media: { base: "s08-gateau", legende: "La répartition des richesses, caricature de Selçuk (1997)" },
      options: [
        { texte: "La population mondiale", correct: false },
        { texte: "La répartition des richesses du monde", correct: true },
        { texte: "La nourriture consommée chaque année", correct: false }
      ],
      aide: "Sur le dessin, quelques convives se servent une part énorme, la foule se partage les miettes."
    },
    {
      type: "qcm",
      consigne: "Quelles sont les grandes aires géographiques qui se partagent le plus de richesses ?",
      precision: "Plusieurs réponses attendues.",
      multiple: true,
      points: 3,
      options: [
        { texte: "Amérique du Nord", correct: true },
        { texte: "Europe", correct: true },
        { texte: "Océanie", correct: true },
        { texte: "Afrique", correct: false },
        { texte: "Amérique du Sud", correct: false }
      ],
      aide: "Trois aires seulement : regarde les zones rouges de la carte."
    },
    {
      type: "tri",
      consigne: "Classe ces pays selon leur niveau de richesse.",
      points: 4,
      paniers: [
        { id: "riche",  titre: "Pays riches" },
        { id: "pauvre", titre: "Pays pauvres ou très pauvres" }
      ],
      items: [
        { id: "n1", texte: "Norvège",     panier: "riche" },
        { id: "n2", texte: "États-Unis",  panier: "riche" },
        { id: "n3", texte: "Japon",       panier: "riche" },
        { id: "n4", texte: "Australie",   panier: "riche" },
        { id: "n5", texte: "France",      panier: "riche" },
        { id: "n6", texte: "Tchad",       panier: "pauvre" },
        { id: "n7", texte: "Mali",        panier: "pauvre" },
        { id: "n8", texte: "Haïti",       panier: "pauvre" },
        { id: "n9", texte: "Bangladesh",  panier: "pauvre" },
        { id: "n10",texte: "Madagascar",  panier: "pauvre" }
      ],
      aide: "Cinq pays dans chaque colonne."
    },
    {
      type: "relier",
      consigne: "D'après le tableau, relie chaque pays à son niveau de développement.",
      points: 4,
      document: `<div class="enveloppe-tableau"><table class="donnees">
        <tr><th></th><th>Norvège</th><th>Koweït</th><th>Guinée équatoriale</th><th>Bangladesh</th></tr>
        <tr><th>Revenu par habitant</th><td>112 710 $</td><td>58 056 $</td><td>12 762 $</td><td>8 498 $</td></tr>
        <tr><th>Espérance de vie</th><td>83,3 ans</td><td>79,2 ans</td><td>63,7 ans</td><td>74,7 ans</td></tr>
        <tr><th>Années de scolarisation</th><td>18,8 ans</td><td>15,3 ans</td><td>12,5 ans</td><td>12,3 ans</td></tr>
        </table><p><i>PNUD — Rapport sur le développement humain 2025, données 2023</i></p></div>`,
      gauche: [
        { id: "p1", texte: "Norvège" },
        { id: "p2", texte: "Koweït" },
        { id: "p3", texte: "Guinée équatoriale" },
        { id: "p4", texte: "Bangladesh" }
      ],
      droite: [
        { id: "d1", texte: "Pays très développé" },
        { id: "d2", texte: "Pays développé" },
        { id: "d3", texte: "Pays en voie de développement" },
        { id: "d4", texte: "Pays pauvre" }
      ],
      paires: [["p1","d1"],["p2","d2"],["p3","d3"],["p4","d4"]],
      aide: "Classe d'abord les pays du revenu le plus élevé au plus faible."
    },
    {
      type: "ouverte",
      consigne: "Lors de ton transfert, tu croises un enfant qui trie des déchets dans une décharge et un autre qui porte des briques. Que vois-tu ? Quelles conséquences la pauvreté a-t-elle sur ces enfants ?",
      points: 3,
      minimum: 20,
      media: { base: "s08-enfants", legende: "Enfants au travail" },
      pistes: [
        "Ces enfants travaillent au lieu d'aller à l'école.",
        "Conséquences : déscolarisation, fatigue, blessures, maladies.",
        "Le travail des enfants est interdit en France et par la Convention des droits de l'enfant.",
        "La pauvreté se transmet : sans école, il est plus difficile de sortir de la pauvreté."
      ]
    }
  ],

  mediaCoeur: { base: "s08-coeur", legende: "Inégalités mondiales" },

  fin: {
    texte: `<p>Dans la poussière d'un marché de Dhaka, un homme te tend une photographie
      froissée : un drapeau. Tu n'en distingues que deux couleurs.</p>`,
    media: { base: "s08-fin" }
  },

  indice: {
    type: "fait",
    texte: "Le drapeau du pays recherché comporte du vert et du blanc.",
    libelle: "Photographie froissée récupérée à Dhaka"
  }
});
