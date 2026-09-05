/* =========================================================
   PÉRIODE 5 — LES USAGES DE L'EAU DOUCE
   Séances 14 à 16 (livret papier : pages 3 bis, 5 et 8)
   ========================================================= */

/* ---------------------------------------------------------
   SÉANCE 14 — Le trajet de l'eau, de la source à la mer
   (livret p. 3, seconde partie)
   --------------------------------------------------------- */
MISSION.session({
  id: "s14", numero: 14, periode: 5, livret: 3,
  titre: "Le trajet de l'eau, de la source à la mer",
  lieu: "Le bassin de la Seine",
  theme: "Les usages de l'eau douce",
  element: "Comprendre le trajet de l'eau, de l'amont vers l'aval",
  duree: 50,
  lecon: "l14",

  intro: {
    texte: `<p>Tu comprends vite que toute cette eau suit un long chemin avant d'arriver
      à la mer.</p>
      <p>Tu remontes la <b>Seine</b>, de son embouchure jusqu'à sa source, en notant
      soigneusement le vocabulaire employé par les hydrologues que tu croises.</p>`,
    media: { base: "s14-intro", legende: "La Seine, de la source à la mer" }
  },

  activites: [
    {
      type: "ordre",
      consigne: "Numérote ces paysages d'amont en aval de la Seine, de la source à la mer.",
      points: 4,
      media: { base: "s14-photos", legende: "Cinq paysages de la Seine" },
      items: [
        { id: "v1", texte: "La source aménagée, où l'eau sort du sol" },
        { id: "v2", texte: "Un petit village traversé par la rivière" },
        { id: "v3", texte: "La Seine à Paris, sous la tour Eiffel" },
        { id: "v4", texte: "L'estuaire et ses digues, près du Havre" },
        { id: "v5", texte: "L'embouchure à marée basse, face à la mer" }
      ],
      ordre: ["v1","v2","v3","v4","v5"],
      aide: "Amont = vers la source ; aval = vers la mer. Paris se trouve au milieu du parcours."
    },
    {
      type: "motscroises",
      consigne: "À l'aide de la vue d'ensemble d'un cours d'eau, complète les mots croisés.",
      points: 5,
      media: { base: "s14-schema", decor: "cours-eau", legende: "Vue d'ensemble d'un cours d'eau" },
      grille: { largeur: 13, hauteur: 11 },
      mots: [
        { num: 1, mot: "AFFLUENT",   definition: "Cours d'eau qui se jette dans un autre cours d'eau.", x: 6,  y: 2, dir: "v" },
        { num: 2, mot: "COURANT",    definition: "Déplacement de l'eau ; il peut être plus ou moins fort.", x: 10, y: 3, dir: "v" },
        { num: 3, mot: "FLEUVE",     definition: "Cours d'eau important qui se jette dans la mer.", x: 2,  y: 4, dir: "v" },
        { num: 4, mot: "EMBOUCHURE", definition: "Partie finale, simple (estuaire) ou ramifiée (delta), d'un cours d'eau qui se jette dans la mer.", x: 2, y: 6, dir: "h" },
        { num: 5, mot: "BERGE",      definition: "Bande de terre qui borde un cours d'eau.", x: 4,  y: 6, dir: "v" }
      ],
      aide: "Le mot horizontal compte dix lettres et commence par la lettre E."
    },
    {
      type: "relier",
      consigne: "Relie chaque définition au mot qui convient.",
      points: 4,
      gauche: [
        { id: "q1", texte: "Partie du cours d'eau comprise entre un point donné et la source" },
        { id: "q2", texte: "Partie du cours d'eau comprise entre un point donné et l'embouchure" },
        { id: "q3", texte: "Courbe formée par un cours d'eau" },
        { id: "q4", texte: "Cours d'eau qui se jette dans un autre plus grand" },
        { id: "q5", texte: "Zone où l'eau douce se mélange à l'eau salée" }
      ],
      droite: [
        { id: "w1", texte: "l'amont" },
        { id: "w2", texte: "l'aval" },
        { id: "w3", texte: "un méandre" },
        { id: "w4", texte: "une rivière" },
        { id: "w5", texte: "un estuaire" }
      ],
      paires: [["q1","w1"],["q2","w2"],["q3","w3"],["q4","w4"],["q5","w5"]],
      aide: "« Amont » et « montagne » commencent par les mêmes lettres : l'amont, c'est vers le haut."
    },
    {
      type: "etiquettes",
      consigne: "Place chaque mot au bon endroit sur le schéma du cours d'eau.",
      points: 5,
      fond: { decor: "cours-eau", base: "schema-cours-eau", alt: "Vue d'ensemble d'un cours d'eau" },
      zones: [
        { x: 27, y: 17, etiquette: "Amont" },
        { x: 31, y: 28, etiquette: "La source" },
        { x: 17, y: 44, etiquette: "Un torrent" },
        { x: 37, y: 62, etiquette: "Un méandre" },
        { x: 52, y: 71, etiquette: "Une confluence" },
        { x: 67, y: 80, etiquette: "Un affluent" },
        { x: 80, y: 72, etiquette: "Aval" },
        { x: 88, y: 86, etiquette: "L'estuaire" },
        { x: 93, y: 93, etiquette: "La mer" }
      ],
      aide: "La confluence est l'endroit où deux cours d'eau se rejoignent ; l'affluent est celui qui arrive."
    },
    {
      type: "qcm",
      consigne: "Pourquoi le débit d'un fleuve augmente-t-il quand on descend vers l'aval ?",
      disposition: "liste",
      points: 2,
      options: [
        { texte: "Parce que le fleuve reçoit l'eau de ses affluents.", correct: true },
        { texte: "Parce que l'eau va de plus en plus vite.", correct: false },
        { texte: "Parce qu'il pleut davantage près de la mer.", correct: false },
        { texte: "Parce que le lit du fleuve est plus profond.", correct: false }
      ],
      aide: "Chaque affluent apporte de l'eau supplémentaire au cours d'eau principal."
    }
  ],

  mediaCoeur: { base: "s14-coeur", decor: "cours-eau", legende: "De l'amont vers l'aval" },

  fin: {
    texte: `<p>Dix mots pour décrire une seule rivière. Le vocabulaire de l'eau est riche…
      et ce nombre-là, tu vas le noter.</p>`,
    media: { base: "s14-fin" }
  },

  indice: {
    type: "nombre", symbole: "coeur", valeur: 10,
    libelle: "Nombre de mots du vocabulaire du cours d'eau étudiés"
  }
});

/* ---------------------------------------------------------
   SÉANCE 15 — Besoin en eau  (livret p. 5)
   --------------------------------------------------------- */
MISSION.session({
  id: "s15", numero: 15, periode: 5, livret: 5,
  titre: "Besoin en eau",
  lieu: "Toulouse, Occitanie",
  theme: "Les usages de l'eau douce",
  element: "Décrire les différents usages de l'eau douce en France",
  duree: 55,
  lecon: "l15",

  intro: {
    texte: `<p>Maintenant que tu connais le trajet de l'eau, tu t'intéresses à son
      utilisation. Peut-être est-ce là la clé de tout ce mystère ?</p>
      <p>Tu te rends à <b>Toulouse</b>, où l'agence de l'eau tient ses statistiques.</p>`,
    media: { base: "s15-intro", legende: "La Garonne à Toulouse" }
  },

  activites: [
    {
      type: "diagramme",
      consigne: "À l'aide du document, légende le diagramme circulaire des usages de l'eau.",
      points: 5,
      document: `<p><b>Usage domestique</b> — eau utilisée par les humains pour boire, l'hygiène
        corporelle, les sanitaires et les tâches ménagères : 24 % de l'eau consommée.<br>
        <b>Usage agricole</b> — eau utilisée par l'agriculture, notamment l'irrigation des
        champs : 48 %.<br>
        <b>Usage industriel</b> — lavage, évacuation des déchets, refroidissement,
        chaudières : 6 %.<br>
        <b>Usage énergétique</b> — centrales hydroélectriques, refroidissement des centrales
        thermiques ou nucléaires : 22 %.<br>
        <b>Usage lié aux loisirs</b> — piscines, patinoires, stations de ski, parcs
        d'attractions.</p>`,
      secteurs: [
        { label: "Usage agricole",     pourcentage: 48 },
        { label: "Usage domestique",   pourcentage: 24 },
        { label: "Usage énergétique",  pourcentage: 22 },
        { label: "Usage industriel",   pourcentage: 6 }
      ],
      intrus: ["Usage lié aux loisirs"],
      aide: "Commence par la part la plus grande : presque la moitié de l'eau part dans les champs."
    },
    {
      type: "saisie",
      consigne: "Quelques ordres de grandeur à retenir.",
      points: 4,
      document: `<p>Consommation moyenne quotidienne d'un Français : bain et douche 58,5 L •
        sanitaires 30 L • lave-linge 18 L • vaisselle 15 L • lavage voiture 9 L •
        arrosage 9 L • cuisine 9 L • boisson 1,5 L.</p>`,
      champs: [
        { label: "L'eau quotidienne des habitants représente environ 1/… de la consommation française", solution: "4" },
        { label: "Consommation moyenne d'un Français, en litres par jour", solution: "150", tolerance: 5, unite: "L" },
        { label: "Pourcentage de l'usage domestique", solution: "24", unite: "%" },
        { label: "Nombre de litres bus chaque jour par un Français", solution: "1.5", tolerance: 0.1, unite: "L" }
      ],
      aide: "24 %, c'est un peu moins d'un quart. Additionne les huit postes pour la consommation totale."
    },
    {
      type: "vraifaux",
      consigne: "Tu cherches des informations sur cette consommation. Vrai ou faux ?",
      points: 4,
      media: { base: "s15-trajet", decor: "paysage-eau", legende: "Le trajet de l'eau consommée en France" },
      items: [
        { texte: "L'eau est rejetée en aval de là où elle est prélevée.", reponse: true },
        { texte: "L'eau arrivant au service d'assainissement est potable.", reponse: false },
        { texte: "L'eau consommée est en grande majorité utilisée pour être bue.", reponse: false },
        { texte: "L'eau prélevée n'est pas potable.", reponse: true },
        { texte: "Un Français consomme en moyenne 150 L d'eau par jour.", reponse: true },
        { texte: "Les eaux usées sont traitées avant d'être rejetées.", reponse: true },
        { texte: "L'eau épurée est impropre à la consommation.", reponse: true }
      ],
      aide: "L'eau épurée est propre pour la nature, mais on ne peut pas la boire : elle n'est pas potable."
    },
    {
      type: "ordre",
      consigne: "Remets dans l'ordre les sept étapes du trajet de l'eau consommée.",
      points: 4,
      items: [
        { id: "u1", texte: "Prélèvement dans la rivière ou dans la nappe" },
        { id: "u2", texte: "Potabilisation dans l'usine d'eau potable" },
        { id: "u3", texte: "Stockage dans le château d'eau" },
        { id: "u4", texte: "Distribution jusqu'aux habitations" },
        { id: "u5", texte: "Collecte des eaux usées" },
        { id: "u6", texte: "Traitement à la station d'épuration" },
        { id: "u7", texte: "Rejet de l'eau épurée dans le milieu naturel" }
      ],
      ordre: ["u1","u2","u3","u4","u5","u6","u7"],
      aide: "On prélève, on rend potable, on stocke, on distribue… puis on récupère et on nettoie."
    },
    {
      type: "etiquettes",
      consigne: "Place chaque usage de l'eau au bon endroit sur le paysage.",
      points: 4,
      fond: { decor: "paysage-eau", base: "paysage-usages", alt: "Où va cette eau ?" },
      zones: [
        { x: 15, y: 70, etiquette: "Usage domestique" },
        { x: 60, y: 53, etiquette: "Usage agricole" },
        { x: 88, y: 60, etiquette: "Usage industriel" },
        { x: 45, y: 88, etiquette: "Usage énergétique" },
        { x: 22, y: 30, etiquette: "Usage lié aux loisirs" }
      ],
      aide: "L'usage énergétique se trouve au niveau du barrage, en bas de la vallée."
    }
  ],

  mediaCoeur: { base: "s15-coeur", legende: "Les usages de l'eau" },

  fin: {
    texte: `<p>Un quart seulement pour les habitants. Le pourcentage de l'usage domestique
      s'ajoute à ton carnet — c'est un grand nombre, il comptera double dans tes calculs.</p>`,
    media: { base: "s15-fin" }
  },

  indice: {
    type: "nombre", symbole: "carre", valeur: 24,
    libelle: "Pourcentage de l'eau consommée pour l'usage domestique"
  }
});

/* ---------------------------------------------------------
   SÉANCE 16 — Au secours, il n'y a plus d'eau !  (livret p. 8)
   --------------------------------------------------------- */
MISSION.session({
  id: "s16", numero: 16, periode: 5, livret: 8,
  titre: "Au secours, il n'y a plus d'eau !",
  lieu: "Le Var, Provence-Alpes-Côte d'Azur",
  theme: "Les usages de l'eau douce",
  element: "Expliquer que l'eau est une ressource convoitée faisant l'objet de conflits d'usages",
  duree: 55,
  lecon: "l16",

  intro: {
    texte: `<p>Ton enquête se termine dans le <b>Var</b>. Tu es à deux doigts d'attraper
      les malfaiteurs et de récupérer la valise !</p>
      <p>Cette année, il n'a presque pas plu. La rivière est à sec, le niveau du lac a
      beaucoup baissé et toute la végétation est très sèche. Il va falloir faire des choix.</p>`,
    media: { base: "s16-intro", legende: "Une rivière à sec dans le Var" }
  },

  activites: [
    {
      type: "repartition",
      consigne: "Tu n'as que 10 gouttes d'eau à répartir. Selon toi, comment devraient-elles l'être ?",
      precision: "Il n'y a pas de bonne réponse : ton choix devra être justifié devant la classe.",
      points: 3,
      total: 10,
      unite: "goutte(s)",
      media: { base: "s16-paysage", legende: "La vallée en pénurie d'eau" },
      categories: [
        { id: "agri", titre: "🌾 Agriculture", description: "Pour irriguer les cultures" },
        { id: "indu", titre: "🏭 Industrie",  description: "Pour faire tourner les usines" },
        { id: "habi", titre: "🏘️ Habitants", description: "Pour boire, cuisiner, se laver" },
        { id: "elec", titre: "⚡ Électricité", description: "Pour produire de l'énergie" }
      ]
    },
    {
      type: "ouverte",
      consigne: "Discutons de vos choix. À ton avis, est-ce que cela convient à tout le monde ?",
      points: 3,
      minimum: 20,
      pistes: [
        "Chaque groupe a des besoins réels : personne n'accepte facilement de manquer d'eau.",
        "L'agriculteur perd sa récolte, l'usine ferme, les habitants ne peuvent plus se laver.",
        "C'est un conflit d'usage : il faut un arbitrage, ici celui du préfet.",
        "La règle retenue : l'eau potable pour la consommation humaine est prioritaire."
      ]
    },
    {
      type: "vraifaux",
      consigne: "Le préfet du Var prend des décisions pour protéger l'eau. Vrai ou faux ?",
      points: 4,
      document: `<p><b>Arrêté préfectoral simplifié — sécheresse dans le Var.</b>
        Niveau d'alerte : <b>alerte renforcée</b>. L'eau potable pour la consommation humaine
        est <b>prioritaire</b>. Chacun doit économiser l'eau au quotidien.</p>
        <div class="enveloppe-tableau"><table class="donnees">
        <tr><th>Usage</th><th>Décision</th></tr>
        <tr><td>Boire, cuisiner</td><td>AUTORISÉ</td></tr>
        <tr><td>Abreuver les animaux</td><td>AUTORISÉ</td></tr>
        <tr><td>Lutter contre un incendie</td><td>AUTORISÉ</td></tr>
        <tr><td>Arroser les cultures</td><td>AUTORISÉ AVEC RESTRICTIONS (la nuit)</td></tr>
        <tr><td>Faire fonctionner une usine</td><td>AUTORISÉ AVEC RESTRICTIONS</td></tr>
        <tr><td>Arroser son jardin, sa pelouse</td><td>INTERDIT</td></tr>
        <tr><td>Remplir une piscine privée</td><td>INTERDIT</td></tr>
        <tr><td>Laver sa voiture (hors station)</td><td>INTERDIT</td></tr>
        <tr><td>Nettoyer terrasses, façades, voiries</td><td>INTERDIT</td></tr>
        <tr><td>Loisirs nautiques</td><td>INTERDIT</td></tr>
        </table></div>`,
      items: [
        { texte: "Les habitants peuvent continuer à boire de l'eau.", reponse: true },
        { texte: "Il est autorisé de remplir sa piscine.", reponse: false },
        { texte: "Les agriculteurs peuvent continuer à arroser leurs cultures, mais avec des restrictions.", reponse: true },
        { texte: "Les usines doivent obligatoirement fermer.", reponse: false },
        { texte: "Les animaux d'élevage peuvent continuer à être abreuvés.", reponse: true },
        { texte: "Les activités nautiques peuvent être interdites lorsque la sécheresse est importante.", reponse: true },
        { texte: "Le préfet prend ces décisions dans son intérêt personnel.", reponse: false }
      ],
      aide: "Relis bien la colonne de droite du tableau : « autorisé avec restrictions » n'est pas « interdit »."
    },
    {
      type: "tri",
      consigne: "Range chaque usage selon la décision du préfet.",
      points: 4,
      paniers: [
        { id: "ok",  titre: "✅ Autorisé" },
        { id: "res", titre: "⚠️ Autorisé avec restrictions" },
        { id: "non", titre: "⛔ Interdit" }
      ],
      items: [
        { id: "u1", texte: "Boire et cuisiner",                    panier: "ok" },
        { id: "u2", texte: "Abreuver les animaux d'élevage",       panier: "ok" },
        { id: "u3", texte: "Lutter contre un incendie",            panier: "ok" },
        { id: "u4", texte: "Arroser les cultures",                 panier: "res" },
        { id: "u5", texte: "Faire fonctionner une usine",          panier: "res" },
        { id: "u6", texte: "Arroser son jardin",                   panier: "non" },
        { id: "u7", texte: "Remplir une piscine privée",           panier: "non" },
        { id: "u8", texte: "Laver sa voiture chez soi",            panier: "non" },
        { id: "u9", texte: "Nettoyer sa terrasse au jet",          panier: "non" },
        { id: "u10",texte: "Pratiquer des loisirs nautiques",      panier: "non" }
      ],
      aide: "Trois usages autorisés, deux avec restrictions, cinq interdits."
    },
    {
      type: "qcm",
      consigne: "Pourquoi ces épisodes de sécheresse risquent-ils de devenir plus fréquents ?",
      disposition: "liste",
      points: 2,
      options: [
        { texte: "À cause du changement climatique.", correct: true },
        { texte: "Parce que les rivières s'usent avec le temps.", correct: false },
        { texte: "Parce que la Terre s'éloigne du Soleil.", correct: false },
        { texte: "Parce que les nappes phréatiques se déplacent.", correct: false }
      ],
      aide: "Réchauffement, évaporation plus forte, pluies moins régulières."
    }
  ],

  mediaCoeur: { base: "s16-coeur", legende: "Le lac à son plus bas niveau" },

  fin: {
    texte: `<p>Sur la berge à sec, les malfaiteurs ont abandonné une carte marine.
      Une côte, un océan immense, et un mot entouré au feutre rouge : <b>Pacifique</b>.</p>
      <p>Ta mission touche à sa fin : il est temps d'ouvrir la piste finale.</p>`,
    media: { base: "s16-fin", legende: "La carte marine abandonnée" }
  },

  indice: {
    type: "fait",
    texte: "Le pays recherché est bordé par l'océan Pacifique.",
    libelle: "Carte marine abandonnée sur la berge"
  }
});
