/* =========================================================
   PÉRIODE 1 — L'ORGANISATION DU TERRITOIRE FRANÇAIS
   Séances 1 à 5 (livret papier : pages 1, 14, 4, 11, 6)
   ========================================================= */

/* ---------------------------------------------------------
   SÉANCE 1 — Le grand départ  (livret p. 1)
   --------------------------------------------------------- */
MISSION.session({
  id: "s01", numero: 1, periode: 1, livret: 1,
  titre: "Le grand départ",
  lieu: "Ma commune",
  theme: "L'organisation du territoire français",
  element: "Découpage administratif du territoire : la commune et ses lieux",
  duree: 45,
  lecon: "l01",

  intro: {
    texte: `<p>Une valise contenant des informations sensibles a été volée. Le Professeur Atlas
      t'a choisi(e) pour la retrouver.</p>
      <p>Mais avant de partir en mission, tu as tout un ensemble de démarches à effectuer
      dans ta propre commune : papiers, matériel, entraînement… Chaque démarche te conduit
      dans un lieu précis.</p>
      <p>Attention : certaines lettres de ces lieux sont marquées. Remises dans l'ordre,
      elles t'indiqueront la ville où les autres agents t'attendent.</p>`,
    media: { base: "s01-intro", legende: "Le message du Professeur Atlas" }
  },

  activites: [
    {
      type: "relier",
      consigne: "Relie chaque démarche au lieu où tu dois te rendre.",
      points: 4,
      aide: "Pense à ce que l'on peut faire dans chaque bâtiment : on ne se soigne pas à la boulangerie !",
      gauche: [
        { id: "d1", texte: "1. Demander une carte d'identité" },
        { id: "d2", texte: "2. Réaliser un certificat médical" },
        { id: "d3", texte: "3. Emprunter un guide de voyage" },
        { id: "d4", texte: "4. S'entraîner à la course à pied" },
        { id: "d5", texte: "5. Acheter une trousse de secours" },
        { id: "d6", texte: "6. Acheter un goûter" },
        { id: "d7", texte: "7. Récupérer ses devoirs et ses cahiers" }
      ],
      droite: [
        { id: "l1", texte: "la mairie" },
        { id: "l2", texte: "le cabinet médical" },
        { id: "l3", texte: "la bibliothèque" },
        { id: "l4", texte: "le parc" },
        { id: "l5", texte: "la pharmacie" },
        { id: "l6", texte: "la boulangerie" },
        { id: "l7", texte: "l'école" }
      ],
      paires: [["d1","l1"],["d2","l2"],["d3","l3"],["d4","l4"],["d5","l5"],["d6","l6"],["d7","l7"]]
    },
    {
      type: "tableau",
      consigne: "Indique la fonction de chacun de ces lieux.",
      precision: "Administrative • Éducative • Commerciale • Santé • Loisirs",
      points: 4,
      aide: "La mairie sert à faire des papiers officiels : sa fonction est administrative.",
      entete: "Lieu",
      colonnes: [{
        titre: "Fonction du lieu",
        options: ["administrative", "éducative", "commerciale", "santé", "loisirs"]
      }],
      lignes: [
        { titre: "La mairie",            solutions: ["administrative"] },
        { titre: "Le cabinet médical",   solutions: ["santé"] },
        { titre: "La bibliothèque",      solutions: ["éducative"] },
        { titre: "Le parc",              solutions: ["loisirs"] },
        { titre: "La pharmacie",         solutions: ["santé"] },
        { titre: "La boulangerie",       solutions: ["commerciale"] },
        { titre: "L'école",              solutions: ["éducative"] }
      ]
    },
    {
      type: "anagramme",
      consigne: "Remets dans l'ordre les 5 lettres marquées pour trouver la ville où tu es attendu(e).",
      precision: "Lettres relevées : le D de mé̲Dical, le I de bI̲bliothèque, le J de la fonction du parc (loisirs = Jeux), le N de boulaNgerie, le O de écOle.",
      points: 3,
      lettres: "DIJNO",
      solution: "DIJON",
      aide: "C'est la capitale de la Bourgogne, célèbre pour sa moutarde.",
      aideLettres: "Clique sur les lettres dans l'ordre, puis clique sur une lettre placée pour la retirer."
    },
    {
      type: "saisie",
      consigne: "Avant de partir, complète ta fiche d'agent avec les informations sur TA commune.",
      precision: "Ces informations sont celles de votre école : votre enseignant les a enregistrées dans l'espace enseignant.",
      points: 4,
      champs: [
        { label: "Continent",   texte: true, solution: "{{profil.continent}}" },
        { label: "Pays",        texte: true, solution: "{{profil.pays}}" },
        { label: "Région",      texte: true, solution: "{{profil.region}}" },
        { label: "Département", texte: true, solution: "{{profil.departement}}" },
        { label: "Commune",     texte: true, solution: "{{profil.commune}}" }
      ],
      aide: "Du plus grand au plus petit : continent, pays, région, département, commune."
    },
    {
      type: "qcm",
      consigne: "Ta commune est-elle une ville ou un village ?",
      disposition: "liste",
      points: 2,
      options: [
        { texte: "Un village : moins de 2 000 habitants", correct: false },
        { texte: "Une ville : plus de 2 000 habitants",   correct: true }
      ],
      aide: "La limite habituelle entre village et ville se situe à 2 000 habitants."
    }
  ],

  mediaCoeur: { base: "s01-coeur", legende: "Le plan de notre commune" },

  fin: {
    texte: `<p>Les lettres marquées forment <b>DIJON</b> : c'est là que les autres agents t'attendent.</p>
      <p>Tu ranges ton sac. Premier indice déposé dans ton carnet de mission.</p>`,
    media: { base: "s01-fin", legende: "En route !" }
  },

  indice: {
    type: "nombre", symbole: "etoile", valeur: 5,
    libelle: "Nombre de lettres de la ville de rendez-vous"
  }
});

/* ---------------------------------------------------------
   SÉANCE 2 — Direction Dijon !  (livret p. 14)
   --------------------------------------------------------- */
MISSION.session({
  id: "s02", numero: 2, periode: 1, livret: 14,
  titre: "Direction Dijon !",
  lieu: "Dijon, Bourgogne-Franche-Comté",
  theme: "L'organisation du territoire français",
  element: "Découpage administratif : commune, département, région, pays, continent",
  duree: 55,
  lecon: "l02",

  intro: {
    texte: `<p>Te voilà à Dijon. Les autres agents t'attendent dans un lieu célèbre de la ville.</p>
      <p>Une fois retrouvé le point de rendez-vous, tu devras te présenter aux autres
      participants : ton continent, ton pays, ta région, ton département, ta commune.
      Un vrai passeport géographique !</p>`,
    media: { base: "s02-intro", legende: "Arrivée à Dijon" }
  },

  activites: [
    {
      type: "qcm",
      consigne: "Dans quel lieu célèbre de Dijon dois-tu te rendre ?",
      precision: "Aide-toi du plan du centre-ville projeté par ton enseignant.",
      points: 2,
      media: { base: "s02-plan-dijon", legende: "Plan du centre de Dijon" },
      options: [
        { texte: "Les caves voûtées", icone: "🕯️", correct: false },
        { texte: "L'église Notre-Dame", icone: "⛪", correct: false },
        { texte: "L'hôtel de Vogüé", icone: "🏠", correct: false },
        { texte: "Le musée Magnin", icone: "🖼️", correct: false },
        { texte: "Le palais des ducs de Bourgogne", icone: "🏛️", correct: true }
      ],
      aide: "C'est le bâtiment le plus vaste, sur la place de la Libération ; il abrite aujourd'hui la mairie et le musée des Beaux-Arts."
    },
    {
      type: "etiquettes",
      consigne: "Place le nom de chaque continent au bon endroit sur le planisphère.",
      points: 5,
      fond: { decor: "planisphere-muet", base: "planisphere", alt: "Planisphère muet" },
      zones: [
        { x: 18,  y: 26, etiquette: "Amérique du Nord" },
        { x: 33,  y: 63, etiquette: "Amérique du Sud" },
        { x: 54,  y: 20, etiquette: "Europe" },
        { x: 54.5, y: 53, etiquette: "Afrique" },
        { x: 80,  y: 28, etiquette: "Asie" },
        { x: 86.5, y: 64, etiquette: "Océanie" },
        { x: 50,  y: 94, etiquette: "Antarctique" }
      ],
      aide: "Il y a sept continents. L'Antarctique est tout au sud, autour du pôle Sud."
    },
    {
      type: "tableau",
      consigne: "Complète la carte d'identité de ton pays.",
      points: 4,
      entete: "Question",
      colonnes: [{
        titre: "Réponse",
        options: ["Europe", "Asie", "Afrique", "350 000 km²", "600 000 m²", "551 695 km²",
                  "68 millions", "55 millions", "7 milliards", "Londres", "Marseille", "Paris",
                  "anglais", "français", "espagnol", "le franc", "l'euro", "le dollar",
                  "L'hymne à la joie", "La liberté", "La Marseillaise",
                  "Liberté, égalité, fraternité", "Un pour tous, tous pour un"]
      }],
      lignes: [
        { titre: "Continent ?",      solutions: ["Europe"] },
        { titre: "Superficie ?",     solutions: ["551 695 km²"] },
        { titre: "Population ?",     solutions: ["68 millions"] },
        { titre: "Capitale ?",       solutions: ["Paris"] },
        { titre: "Langue ?",         solutions: ["français"] },
        { titre: "Monnaie ?",        solutions: ["l'euro"] },
        { titre: "Hymne national ?", solutions: ["La Marseillaise"] },
        { titre: "Devise ?",         solutions: ["Liberté, égalité, fraternité"] }
      ],
      aide: "La France mesure environ 552 000 km² et compte 68 millions d'habitants."
    },
    {
      type: "etiquettes",
      consigne: "Place le nom de chaque région métropolitaine sur le bon numéro.",
      precision: "Treize régions à replacer : commence par celle de ton école, puis par les régions voisines.",
      points: 6,
      fond: { decor: "france-regions", base: "carte-regions", alt: "Les 13 régions métropolitaines" },
      zones: [
        { x: 16.5, y: 30.4, etiquette: "Bretagne" },
        { x: 30,   y: 37.1, etiquette: "Pays de la Loire" },
        { x: 35.8, y: 21.7, etiquette: "Normandie" },
        { x: 53.2, y: 13.1, etiquette: "Hauts-de-France" },
        { x: 71.3, y: 25.6, etiquette: "Grand Est" },
        { x: 51.3, y: 25.6, etiquette: "Île-de-France" },
        { x: 46.1, y: 37.1, etiquette: "Centre-Val de Loire" },
        { x: 66.1, y: 40,   etiquette: "Bourgogne-Franche-Comté" },
        { x: 64.2, y: 56.3, etiquette: "Auvergne-Rhône-Alpes" },
        { x: 36.5, y: 59.2, etiquette: "Nouvelle-Aquitaine" },
        { x: 49.4, y: 72.7, etiquette: "Occitanie" },
        { x: 73.9, y: 71.7, etiquette: "Provence-Alpes-Côte d'Azur" },
        { x: 93.9, y: 88.1, etiquette: "Corse" }
      ],
      aide: "Repère d'abord la Bretagne (à l'ouest), la Corse (l'île) et les Hauts-de-France (tout au nord)."
    },
    {
      type: "saisie",
      consigne: "Termine ta présentation.",
      points: 3,
      champs: [
        { label: "Numéro de ton département", texte: true, solution: "{{profil.numeroDepartement}}" },
        { label: "Nombre de régions en France métropolitaine", solution: "13" },
        { label: "Nombre de continents", solution: "7" }
      ],
      aide: "Les départements sont numérotés par ordre alphabétique : l'Ain porte le 01."
    },
    {
      type: "tableau",
      consigne: "Qui peut décider ? Attribue chaque décision au bon échelon.",
      points: 4,
      entete: "Décision",
      colonnes: [{ titre: "Qui décide ?", options: ["la région", "le département", "la commune"] }],
      lignes: [
        { titre: "Agrandir un lycée",                    solutions: ["la région"] },
        { titre: "Rénover une école élémentaire",        solutions: ["la commune"] },
        { titre: "Construire un collège",                solutions: ["le département"] },
        { titre: "Créer une ligne de TER",               solutions: ["la région"] },
        { titre: "Organiser la collecte des déchets",    solutions: ["la commune"] }
      ],
      aide: "Écoles = commune, collèges = département, lycées = région. Un moyen de retenir : plus l'élève grandit, plus le territoire est grand."
    }
  ],

  mediaCoeur: { base: "s02-coeur", legende: "Le palais des ducs de Bourgogne" },

  fin: {
    texte: `<p>Les agents sont réunis. Sur la table, un planisphère : sept continents,
      sept pistes possibles. Le nombre reste gravé dans ton carnet.</p>`,
    media: { base: "s02-fin" }
  },

  indice: {
    type: "nombre", symbole: "cercle", valeur: 7,
    libelle: "Nombre de continents sur le planisphère"
  }
});

/* ---------------------------------------------------------
   SÉANCE 3 — Vivre à Clamecy, vivre dans une commune rurale
   (livret p. 4)
   --------------------------------------------------------- */
MISSION.session({
  id: "s03", numero: 3, periode: 1, livret: 4,
  titre: "Vivre à Clamecy, vivre dans une commune rurale",
  lieu: "Clamecy, Nièvre",
  theme: "L'organisation du territoire français",
  element: "Caractéristiques d'une région : les espaces ruraux et la densité de population",
  duree: 50,
  lecon: "l03",

  intro: {
    texte: `<p>Un ancien informaticien, soupçonné d'avoir aidé les malfaiteurs, se serait
      réfugié à <b>Clamecy</b>, une petite commune rurale de la Nièvre.</p>
      <p>Pour passer inaperçu(e), tu dois comprendre comment on vit ici : combien
      d'habitants, quels commerces, quels déplacements.</p>`,
    media: { base: "s03-intro", legende: "Arrivée à Clamecy" }
  },

  activites: [
    {
      type: "qcm",
      consigne: "D'après toi, quelle photographie a été prise à Clamecy ?",
      points: 2,
      media: { base: "s03-photos", legende: "Quatre paysages français" },
      options: [
        { texte: "Une rue commerçante piétonne, remplie de passants", icone: "🛍️", correct: false },
        { texte: "Un bourg aux toits serrés, entouré de verdure et de champs", icone: "🏘️", correct: true },
        { texte: "Un front de mer bordé d'immeubles et de bateaux", icone: "⛵", correct: false },
        { texte: "Un quartier d'affaires en verre au bord d'un bassin", icone: "🏢", correct: false }
      ],
      aide: "Une commune rurale est entourée de champs et de forêts, et compte peu de grands immeubles."
    },
    {
      type: "trous",
      consigne: "Complète la définition d'une commune rurale.",
      precision: "Attention : il y a un intrus dans la liste des mots !",
      points: 4,
      intrus: ["élevée"],
      texte: `Une commune rurale est une commune où la [[densité]] de population est [[faible]].
        Elle se situe dans une zone influencée par les activités [[agricoles]].
        Elle peut être : un [[village]] si elle comprend moins de 2 000 habitants,
        ou un [[bourg]] si elle accueille plus de 2 000 habitants.`,
      aide: "Rural = peu d'habitants sur beaucoup d'espace : la densité y est donc faible."
    },
    {
      type: "saisie",
      consigne: "Calcule la densité de population de chacun de ces trois espaces.",
      precision: "Densité = nombre d'habitants ÷ superficie en km².",
      points: 4,
      document: `<p><b>Espace A</b> : un carré de 1 km sur 1 km, dans lequel vivent 2 habitants.<br>
        <b>Espace B</b> : un carré de 1 km sur 1 km, dans lequel vivent 4 habitants.<br>
        <b>Espace C</b> : un carré de 2 km sur 2 km, dans lequel vivent 4 habitants.</p>`,
      champs: [
        { label: "Espace A", solution: "2", unite: "hab/km²" },
        { label: "Espace B", solution: "4", unite: "hab/km²" },
        { label: "Espace C", solution: "1", unite: "hab/km²" },
        { label: "Total des trois densités", solution: "7", unite: "hab/km²" }
      ],
      aide: "Attention à l'espace C : 2 km sur 2 km, cela fait 4 km² de surface !"
    },
    {
      type: "etiquettes",
      consigne: "Replace chaque élément du village au bon endroit sur la photographie aérienne.",
      points: 5,
      fond: { decor: "village-aerien", base: "village-clamecy", alt: "Un village vu du ciel" },
      zones: [
        { x: 47, y: 40, etiquette: "Église" },
        { x: 47, y: 48, etiquette: "Centre-bourg" },
        { x: 24, y: 62, etiquette: "Lotissement" },
        { x: 52, y: 52, etiquette: "Commerce" },
        { x: 41, y: 46, etiquette: "Mairie" },
        { x: 16, y: 17, etiquette: "Champ" },
        { x: 80, y: 52, etiquette: "Route principale" }
      ],
      aide: "Le centre-bourg est là où les maisons sont les plus serrées, autour du clocher."
    },
    {
      type: "tri",
      consigne: "Range chaque proposition dans la bonne colonne.",
      points: 4,
      paniers: [
        { id: "a", titre: "👍 Avantages de vivre à la campagne" },
        { id: "i", titre: "👎 Inconvénients de vivre à la campagne" }
      ],
      items: [
        { id: "t1", texte: "Proximité de la nature",              panier: "a" },
        { id: "t2", texte: "Transports en commun peu développés", panier: "i" },
        { id: "t3", texte: "Peu d'emplois",                       panier: "i" },
        { id: "t4", texte: "Perte de temps dans les déplacements",panier: "i" },
        { id: "t5", texte: "Logements moins coûteux",             panier: "a" },
        { id: "t6", texte: "Logements et terrains plus grands",   panier: "a" },
        { id: "t7", texte: "Peu de nuisances sonores",            panier: "a" },
        { id: "t8", texte: "Nécessité d'avoir une voiture",       panier: "i" },
        { id: "t9", texte: "Peu de commerces",                    panier: "i" },
        { id: "t10",texte: "Peu de services",                     panier: "i" }
      ],
      aide: "Compte à la fin : il y a 4 avantages et 6 inconvénients."
    }
  ],

  mediaCoeur: { base: "s03-coeur", legende: "Un bourg de la Nièvre" },

  fin: {
    texte: `<p>Fausse piste : l'informaticien a quitté Clamecy depuis longtemps.
      Mais tes calculs de densité, eux, valent de l'or : garde-les précieusement.</p>`,
    media: { base: "s03-fin" }
  },

  indice: {
    type: "nombre", symbole: "nuage", valeur: 7,
    libelle: "Total des trois densités calculées"
  }
});

/* ---------------------------------------------------------
   SÉANCE 4 — Besançon, travailler en ville  (livret p. 11)
   --------------------------------------------------------- */
MISSION.session({
  id: "s04", numero: 4, periode: 1, livret: 11,
  titre: "Besançon, travailler en ville",
  lieu: "Besançon, Doubs",
  theme: "L'organisation du territoire français",
  element: "Caractéristiques d'une région : les espaces urbains et les secteurs d'activité",
  duree: 50,
  lecon: "l04",

  intro: {
    texte: `<p>Direction <b>Besançon</b>, la préfecture du Doubs. Une source t'a donné
      rendez-vous… sans dire laquelle.</p>
      <p>Tu vas devoir rencontrer un maximum de professionnels de la ville pour recueillir
      des informations. Encore faut-il savoir où chacun travaille !</p>`,
    media: { base: "s04-intro", legende: "Besançon depuis la citadelle" }
  },

  activites: [
    {
      type: "motsmeles",
      consigne: "Retrouve dans la grille dix professions que l'on peut exercer en ville.",
      precision: "Les mots se lisent horizontalement ou verticalement.",
      points: 5,
      grille: [
        "AQCAISSIER",
        "MSOUDEURPU",
        "BINFIRMIER",
        "UASRAVANDS",
        "LGUIDEGFIO",
        "ALLSGUAIAU",
        "NATELRSRTD",
        "CCARAGIMRE",
        "IINVCUNIEU",
        "EETEIIIENR",
        "RRTUEDERET",
        "QUARRERTRE"
      ],
      mots: ["CAISSIER","SOUDEUR","INFIRMIER","GUIDE","AMBULANCIER",
             "GLACIER","PEDIATRE","SERVEUR","MAGASINIER","CONSULTANT"],
      aide: "Regarde la première colonne de haut en bas : elle cache un métier de 11 lettres."
    },
    {
      type: "tableau",
      consigne: "Pour chaque métier trouvé, indique le lieu d'exercice et le secteur d'activité.",
      points: 6,
      document: `<p><b>Lieux :</b> centre commercial • centre-ville • quartier d'affaires • CHU • SNCF</p>
        <p><b>Secteurs :</b> primaire (on exploite la nature) • secondaire (on transforme) •
        tertiaire (on rend un service)</p>`,
      entete: "Métier",
      colonnes: [
        { titre: "Lieu d'exercice", options: ["centre commercial","centre-ville","quartier d'affaires","CHU","SNCF"] },
        { titre: "Secteur",         options: ["primaire","secondaire","tertiaire"] }
      ],
      lignes: [
        { titre: "Caissier",    solutions: ["centre commercial", "tertiaire"] },
        { titre: "Soudeur",     solutions: ["SNCF", "secondaire"] },
        { titre: "Infirmier",   solutions: ["CHU", "tertiaire"] },
        { titre: "Guide",       solutions: ["centre-ville", "tertiaire"] },
        { titre: "Ambulancier", solutions: ["CHU", "tertiaire"] },
        { titre: "Glacier",     solutions: ["centre-ville", "secondaire"] },
        { titre: "Pédiatre",    solutions: ["CHU", "tertiaire"] },
        { titre: "Serveur",     solutions: ["centre-ville", "tertiaire"] },
        { titre: "Magasinier",  solutions: ["centre commercial", "tertiaire"] },
        { titre: "Consultant",  solutions: ["quartier d'affaires", "tertiaire"] }
      ],
      aide: "Le glacier fabrique ses glaces : il transforme une matière première, c'est du secondaire."
    },
    {
      type: "qcm",
      consigne: "Quel secteur d'activité emploie le plus de personnes en France aujourd'hui ?",
      points: 2,
      disposition: "liste",
      document: `<p>En 1911, près de 40 % des actifs travaillaient dans le secteur primaire.
        Aujourd'hui : primaire 2,1 % • secondaire 18,2 % • tertiaire 79,7 %.</p>`,
      options: [
        { texte: "Le secteur primaire",    correct: false },
        { texte: "Le secteur secondaire",  correct: false },
        { texte: "Le secteur tertiaire",   correct: true }
      ],
      aide: "Regarde le document : près de 8 emplois sur 10."
    },
    {
      type: "etiquettes",
      consigne: "Place chaque espace de Besançon au bon endroit sur la vue aérienne.",
      points: 3,
      fond: { decor: "village-aerien", base: "besancon-aerien", alt: "Besançon vue du ciel" },
      zones: [
        { x: 24, y: 25, etiquette: "Parc technologique" },
        { x: 74, y: 22, etiquette: "Centre-ville" },
        { x: 22, y: 72, etiquette: "Centre commercial" },
        { x: 50, y: 68, etiquette: "CHU" },
        { x: 80, y: 66, etiquette: "Quartier d'affaires" }
      ],
      aide: "Le centre commercial se trouve en périphérie, près des grands axes routiers."
    },
    {
      type: "ouverte",
      consigne: "Une source glisse une phrase avant de disparaître : « Ce que vous cherchez n'est plus en Europe. » Que peux-tu en déduire ?",
      points: 2,
      minimum: 10,
      pistes: [
        "La valise a quitté le continent européen.",
        "Il faut chercher sur un autre continent : Amérique, Afrique, Asie, Océanie.",
        "Croiser cette information avec les indices déjà récoltés."
      ]
    }
  ],

  mediaCoeur: { base: "s04-coeur", legende: "Les quartiers de Besançon" },

  fin: {
    texte: `<p>La source a parlé. La valise n'est plus en Europe : elle a traversé
      l'océan. On te murmure une région du monde…</p>`,
    media: { base: "s04-fin" }
  },

  indice: {
    type: "fait",
    texte: "Le pays recherché se trouve en Amérique latine.",
    libelle: "Confidence d'une source à Besançon"
  }
});

/* ---------------------------------------------------------
   SÉANCE 5 — Profitons des loisirs de la montagne (livret p. 6)
   --------------------------------------------------------- */
MISSION.session({
  id: "s05", numero: 5, periode: 1, livret: 6,
  titre: "Profitons des loisirs de la montagne",
  lieu: "Massif de la Dôle, Jura",
  theme: "L'organisation du territoire français",
  element: "Caractéristiques d'une région : les espaces de montagne et le tourisme",
  duree: 50,
  lecon: "l05",

  intro: {
    texte: `<p>Une filature aussi longue, cela use. Tu t'accordes une pause dans le
      <b>massif de la Dôle</b>, dans le Jura, à 1 678 mètres d'altitude.</p>
      <p>Pas si facile de se repérer sur les pistes… et impossible de ne pas voir ce que
      le tourisme fait à la montagne.</p>`,
    media: { base: "s05-intro", legende: "Le massif de la Dôle" }
  },

  activites: [
    {
      type: "motscroises",
      consigne: "Retrouve chaque mot du vocabulaire de la montagne.",
      points: 5,
      grille: { largeur: 9, hauteur: 11 },
      mots: [
        { num: 1, mot: "PISTE",     definition: "Chemin balisé sur lequel on descend à ski.",           x: 8, y: 0, dir: "v" },
        { num: 2, mot: "CHALET",    definition: "Maison de montagne construite en bois.",               x: 2, y: 1, dir: "v" },
        { num: 3, mot: "NEIGE",     definition: "Elle recouvre les pistes en hiver.",                   x: 6, y: 3, dir: "v" },
        { num: 4, mot: "TELESIEGE", definition: "Remontée mécanique où l'on monte assis.",              x: 0, y: 4, dir: "h" },
        { num: 4, mot: "TORRENT",   definition: "Cours d'eau rapide qui dévale la montagne.",           x: 0, y: 4, dir: "v" },
        { num: 5, mot: "SOMMET",    definition: "Point le plus élevé d'une montagne.",                  x: 4, y: 4, dir: "v" }
      ],
      aide: "Le mot horizontal se termine par les lettres G et E."
    },
    {
      type: "motsmeles",
      consigne: "Retrouve les dix loisirs que l'on peut pratiquer à la montagne.",
      points: 5,
      grille: [
        "RANDONNEEB",
        "PARAPENTEI",
        "ESCALADELA",
        "SDTRAILVUT",
        "KPADDLETGH",
        "IRAQUETTEL",
        "SNOWBOARDO",
        "IRAFTINGXN"
      ],
      mots: ["RANDONNEE","PARAPENTE","ESCALADE","TRAIL","PADDLE",
             "RAQUETTE","SNOWBOARD","RAFTING","SKI","BIATHLON"],
      aide: "La première colonne et la dernière colonne cachent chacune un sport."
    },
    {
      type: "trous",
      consigne: "Légende chaque photographie prise pendant ton séjour.",
      precision: "Un mot de la liste ne sert à rien : c'est l'intrus.",
      points: 5,
      intrus: ["écologie"],
      texte: `Photo 1 — File de voitures à l'entrée de la station : pollution [[atmosphérique]].
        Photo 2 — Construction d'une nouvelle résidence sur un versant boisé : réduction de la [[biodiversité]].
        Photo 3 — Mégots abandonnés sur les rochers : [[pollution]] des sols.
        Photo 4 — Canon à neige en action : prélèvement d'[[eau]].
        Photo 5 — Télésiège en fonctionnement toute la journée : consommation d'[[énergie]].`,
      media: { base: "s05-photos", legende: "Cinq photographies prises en station" },
      aide: "L'intrus est le mot qui désigne la science, pas une conséquence : « écologie »."
    },
    {
      type: "saisie",
      consigne: "Combien de lettres compte le mot intrus ?",
      points: 2,
      champs: [{ label: "Nombre de lettres du mot intrus", solution: "9" }],
      aide: "Compte les lettres de « écologie »… puis vérifie : é-c-o-l-o-g-i-e."
    },
    {
      type: "ouverte",
      consigne: "Sur la terrasse du refuge, un skieur commente une carte du monde punaisée au mur : « Là où va votre valise, c'est l'hiver quand c'est l'hiver ici. » Qu'en déduis-tu ?",
      points: 2,
      minimum: 10,
      pistes: [
        "Les saisons sont inversées entre les deux hémisphères.",
        "Si les saisons sont les mêmes qu'en France, le pays est dans l'hémisphère nord.",
        "Cela élimine l'Australie, l'Argentine, le Chili, l'Afrique du Sud…"
      ]
    }
  ],

  mediaCoeur: { base: "s05-coeur", legende: "Le domaine skiable" },

  fin: {
    texte: `<p>Pause terminée. Tu repars avec une certitude de plus sur le pays recherché,
      et une conscience aiguë de ce que coûte une journée de ski à la montagne.</p>`,
    media: { base: "s05-fin" }
  },

  indice: {
    type: "fait",
    texte: "Le pays recherché est situé dans l'hémisphère nord.",
    libelle: "Remarque d'un skieur au refuge"
  }
});
