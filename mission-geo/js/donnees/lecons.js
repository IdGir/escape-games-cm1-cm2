/* =========================================================
   REGISTRE DE LA MISSION + LES 16 LEÇONS
   ---------------------------------------------------------
   Une leçon par séance. Chaque leçon est consultable :
     - pendant l'énigme (icône 📚) ;
     - après la réussite, en trace écrite ;
     - à l'impression, au format A4, avec ou sans corrigé.
   Chaque leçon réserve un emplacement média (image ou vidéo)
   que l'enseignant peut remplir sans toucher au code.
   ========================================================= */

window.MISSION = window.MISSION || {
  sessions: [],
  lecons: {},
  final: null,
  session(o){ this.sessions.push(o); return o; },
  lecon(o){ this.lecons[o.id] = o; return o; },
  definirFinal(o){ this.final = o; return o; },
  parId(id){ return this.sessions.find(s => s.id === id); },
  ordre(){ return this.sessions.slice().sort((a, b) => a.numero - b.numero); },
  parPeriode(){
    const m = new Map();
    this.ordre().forEach(s => {
      if(!m.has(s.periode)) m.set(s.periode, []);
      m.get(s.periode).push(s);
    });
    return m;
  }
};

/* ---------------------------------------------------------
   PÉRIODE 1 — L'organisation du territoire français
   --------------------------------------------------------- */

MISSION.lecon({
  id: "l01",
  titre: "La commune, le premier échelon du territoire",
  objectifs: [
    "Savoir ce qu'est une commune et qui la dirige.",
    "Identifier la fonction des principaux lieux d'une commune.",
    "Se repérer sur le plan de sa commune."
  ],
  texte: `
    <p>La <b>commune</b> est le plus petit territoire administratif de France. Il y en a
    environ <b>34 800</b>. Elle peut compter quelques dizaines d'habitants ou plusieurs
    centaines de milliers : Paris et le plus petit village sont l'un comme l'autre des communes.</p>
    <p>Chaque commune est dirigée par un <b>maire</b>, élu par le <b>conseil municipal</b>,
    lui-même élu par les habitants. La commune s'occupe des écoles maternelles et élémentaires,
    des ordures ménagères, de l'eau, de la voirie, de l'urbanisme, du sport et de la culture.</p>
    <p>Dans une commune, les lieux n'ont pas tous la même <b>fonction</b> :</p>
    <ul>
      <li><b>administrative</b> : la mairie, la poste ;</li>
      <li><b>éducative</b> : l'école, la bibliothèque ;</li>
      <li><b>commerciale</b> : la boulangerie, le supermarché ;</li>
      <li><b>de santé</b> : le cabinet médical, la pharmacie ;</li>
      <li><b>de loisirs</b> : le parc, le stade, la salle des fêtes.</li>
    </ul>
    <p>Pour se déplacer d'un lieu à l'autre, on utilise un <b>plan</b> : il donne les rues,
    les bâtiments et souvent des <b>coordonnées</b> (une lettre et un chiffre) pour retrouver
    rapidement un endroit.</p>`,
  vocabulaire: [
    ["Commune", "Le plus petit territoire administratif français, dirigé par un maire."],
    ["Maire", "Personne élue qui dirige la commune."],
    ["Fonction d'un lieu", "Ce à quoi ce lieu sert : se soigner, apprendre, acheter, se distraire…"],
    ["Plan", "Représentation vue du dessus d'un espace réduit, comme une ville ou un quartier."]
  ],
  aRetenir: "Ma commune est le premier territoire où je vis. Elle est dirigée par un maire et rassemble des lieux aux fonctions différentes : administrative, éducative, commerciale, de santé, de loisirs.",
  media: { base: "lecon-01-commune", legende: "Ma commune vue du ciel" }
});

MISSION.lecon({
  id: "l02",
  titre: "Du plus petit au plus grand : commune, département, région, pays, continent",
  objectifs: [
    "Emboîter les différents territoires administratifs français.",
    "Nommer et situer sa région et son département.",
    "Distinguer les compétences de la commune, du département et de la région."
  ],
  texte: `
    <p>Le territoire français est découpé en territoires <b>emboîtés</b>, du plus petit au
    plus grand :</p>
    <p style="text-align:center"><b>commune → département → région → pays → continent</b></p>
    <p>La France métropolitaine compte <b>13 régions</b> et <b>96 départements</b>.
    En ajoutant les territoires d'outre-mer (Guadeloupe, Martinique, Guyane, La Réunion,
    Mayotte), on arrive à <b>18 régions</b> et <b>101 départements</b>.
    Chaque département porte un <b>numéro</b>, dans l'ordre alphabétique (01 : Ain,
    21 : Côte-d'Or, 75 : Paris…).</p>
    <p>Chaque échelon a ses <b>compétences</b>, c'est-à-dire ce qu'il a le droit de décider :</p>
    <ul>
      <li>la <b>commune</b> : les écoles maternelles et élémentaires, l'eau, les déchets, l'urbanisme ;</li>
      <li>le <b>département</b> : les collèges, l'action sociale, les routes départementales ;</li>
      <li>la <b>région</b> : les lycées, la formation, les transports (TER), l'aménagement du territoire.</li>
    </ul>
    <p>Certains domaines — le sport, la culture, le tourisme, l'environnement, les transports —
    sont partagés par plusieurs échelons : ils peuvent donc décider ensemble.</p>`,
  vocabulaire: [
    ["Département", "Territoire dirigé par un conseil départemental ; il porte un numéro."],
    ["Région", "Grand territoire regroupant plusieurs départements."],
    ["Compétence", "Domaine dans lequel une collectivité a le droit de décider."],
    ["Préfecture", "Ville principale d'un département, où siège le préfet."]
  ],
  aRetenir: "Je vis dans une commune, située dans un département, lui-même situé dans une région, dans le pays France, sur le continent européen. Chaque échelon décide de choses différentes.",
  media: { base: "lecon-02-decoupage", legende: "Les 13 régions de France métropolitaine" }
});

MISSION.lecon({
  id: "l03",
  titre: "Les espaces ruraux et la densité de population",
  objectifs: [
    "Reconnaître un espace rural sur une photographie.",
    "Calculer et comparer des densités de population.",
    "Repérer les avantages et les inconvénients de la vie à la campagne."
  ],
  texte: `
    <p>Un espace <b>rural</b> est un espace où la <b>densité de population</b> est faible et
    où l'on trouve beaucoup de champs, de prairies ou de forêts. Il est influencé par les
    activités <b>agricoles</b>.</p>
    <p>La densité de population est le <b>nombre d'habitants par kilomètre carré</b>.
    On la calcule ainsi :</p>
    <p style="text-align:center"><b>densité = nombre d'habitants ÷ superficie (en km²)</b></p>
    <p>En France, la densité moyenne est d'environ <b>106 habitants par km²</b>. Dans une
    grande ville, elle dépasse souvent 3 000 hab/km² ; dans certains villages de montagne,
    elle descend sous 10 hab/km².</p>
    <p>Une commune rurale peut être :</p>
    <ul>
      <li>un <b>village</b>, si elle compte moins de 2 000 habitants ;</li>
      <li>un <b>bourg</b>, si elle en compte plus de 2 000. Le bourg possède des commerces
      et des services qui servent aussi aux villages voisins.</li>
    </ul>
    <p>Vivre à la campagne présente des <b>avantages</b> (nature, calme, logements plus grands
    et moins chers) et des <b>inconvénients</b> (peu de commerces, peu de services, peu d'emplois,
    transports en commun rares, voiture indispensable).</p>`,
  vocabulaire: [
    ["Espace rural", "Espace peu peuplé, marqué par l'agriculture et les paysages naturels."],
    ["Densité de population", "Nombre d'habitants par km²."],
    ["Village", "Commune rurale de moins de 2 000 habitants."],
    ["Bourg", "Commune rurale de plus de 2 000 habitants, avec commerces et services."]
  ],
  aRetenir: "Un espace rural est peu densément peuplé et marqué par l'agriculture. La densité de population se calcule en divisant le nombre d'habitants par la superficie en km².",
  media: { base: "lecon-03-rural", decor: "village-aerien", legende: "Un village vu du ciel" }
});

MISSION.lecon({
  id: "l04",
  titre: "Travailler en ville : les trois secteurs d'activité",
  objectifs: [
    "Identifier les grands espaces d'une ville et leurs fonctions.",
    "Classer un métier dans le secteur primaire, secondaire ou tertiaire.",
    "Comprendre l'évolution des emplois en France."
  ],
  texte: `
    <p>Une <b>ville</b> est un espace où la densité de population est forte, avec de nombreux
    logements, commerces, services et emplois. On y distingue plusieurs espaces :</p>
    <ul>
      <li>le <b>centre-ville</b> : commerces, administrations, patrimoine ;</li>
      <li>le <b>centre commercial</b>, en périphérie, accessible en voiture ;</li>
      <li>le <b>quartier d'affaires</b> ou le <b>parc technologique</b> : bureaux, entreprises, recherche ;</li>
      <li>les grands <b>équipements</b> : hôpital (CHU), gare, université, stade.</li>
    </ul>
    <p>Les métiers se classent en <b>trois secteurs d'activité</b> :</p>
    <ul>
      <li><b>primaire</b> : on exploite directement les ressources naturelles
      (agriculteur, pêcheur, mineur, forestier) ;</li>
      <li><b>secondaire</b> : on transforme les matières premières
      (ouvrier, soudeur, boulanger, maçon) ;</li>
      <li><b>tertiaire</b> : on rend un service
      (infirmier, caissier, enseignant, guide, vendeur, conducteur de train).</li>
    </ul>
    <p>En France, la répartition a beaucoup changé : en 1911, près de 40 % des actifs
    travaillaient dans le secteur primaire ; aujourd'hui, ils sont environ <b>2 %</b>,
    contre <b>18 %</b> dans le secondaire et près de <b>80 %</b> dans le tertiaire.</p>`,
  vocabulaire: [
    ["Secteur primaire", "Activités qui exploitent les ressources naturelles."],
    ["Secteur secondaire", "Activités qui transforment les matières premières."],
    ["Secteur tertiaire", "Activités de services rendus aux personnes ou aux entreprises."],
    ["Quartier d'affaires", "Quartier regroupant bureaux et entreprises."]
  ],
  aRetenir: "En ville, on trouve des espaces aux fonctions différentes et des métiers des trois secteurs. Aujourd'hui, en France, près de 8 emplois sur 10 sont dans le secteur tertiaire.",
  media: { base: "lecon-04-ville", legende: "Une ville et ses quartiers" }
});

MISSION.lecon({
  id: "l05",
  titre: "La montagne : un espace de loisirs à ménager",
  objectifs: [
    "Nommer les activités de loisirs pratiquées en montagne.",
    "Lire un plan des pistes.",
    "Identifier les effets du tourisme de montagne sur l'environnement."
  ],
  texte: `
    <p>La montagne est un espace de <b>loisirs</b> très fréquenté, été comme hiver.
    On y pratique le ski, le snowboard, la luge, la randonnée, l'escalade, le VTT,
    le parapente, le rafting, le trail, la raquette…</p>
    <p>Pour accueillir les visiteurs, on aménage des <b>stations de montagne</b> :
    remontées mécaniques (téléski, télésiège, téléphérique), pistes classées par
    <b>niveau de difficulté</b> (verte, bleue, rouge, noire), hébergements, commerces,
    parkings et routes d'accès.</p>
    <p>Ces aménagements ont un coût pour l'environnement :</p>
    <ul>
      <li><b>pollution</b> de l'air liée aux embouteillages ;</li>
      <li><b>consommation d'énergie</b> des remontées mécaniques ;</li>
      <li><b>prélèvement d'eau</b> important pour la neige de culture ;</li>
      <li><b>réduction de la biodiversité</b> par le déboisement et le dérangement des animaux ;</li>
      <li><b>pollution des sols</b> par les déchets laissés sur place.</li>
    </ul>
    <p>Un tourisme plus respectueux privilégie les transports collectifs, les activités
    sans moteur et le respect des espaces protégés.</p>`,
  vocabulaire: [
    ["Station de montagne", "Lieu aménagé pour accueillir des touristes en montagne."],
    ["Remontée mécanique", "Installation qui transporte les skieurs vers le haut des pistes."],
    ["Neige de culture", "Neige fabriquée artificiellement, qui consomme beaucoup d'eau."],
    ["Biodiversité", "Ensemble des espèces vivantes présentes dans un milieu."]
  ],
  aRetenir: "La montagne attire de nombreux touristes. Les aménagements nécessaires ont un impact fort sur l'environnement : pollution, énergie, eau, biodiversité.",
  media: { base: "lecon-05-montagne", legende: "Un domaine skiable" }
});

/* ---------------------------------------------------------
   PÉRIODE 2 — Régions littorales et inégalités mondiales
   --------------------------------------------------------- */

MISSION.lecon({
  id: "l06",
  titre: "Le littoral touristique : la station balnéaire",
  objectifs: [
    "Définir une station balnéaire.",
    "Identifier les activités proposées aux touristes.",
    "Peser les effets positifs et négatifs de la fréquentation touristique."
  ],
  texte: `
    <p>Une <b>station balnéaire</b> est un lieu de séjour situé en bord de mer, aménagé
    pour accueillir des touristes. Étretat, en Normandie, en est un bon exemple :
    ancien port de pêche, la ville s'est transformée au XIX<sup>e</sup> siècle grâce à la mode
    des <b>bains de mer</b>.</p>
    <p>Le tourisme y propose des activités variées : baignade, randonnée sur le GR21,
    kayak et paddle au pied des falaises, visite du musée, du Clos Lupin ou du marché couvert.</p>
    <p>Cette fréquentation a des <b>effets positifs</b> :</p>
    <ul>
      <li>création d'emplois (hôtels, restaurants, commerces, guides) ;</li>
      <li>animations et fêtes ;</li>
      <li>aménagements nouveaux (sentiers, promenades, équipements).</li>
    </ul>
    <p>… et des <b>effets négatifs</b> pour les habitants :</p>
    <ul>
      <li>embouteillages et stationnement difficile ;</li>
      <li>déchets et pollution ;</li>
      <li>augmentation des prix des logements, qui pousse des habitants à partir.</li>
    </ul>
    <p>Étretat compte environ <b>1 200 habitants</b> mais accueille près d'un
    <b>million de visiteurs par an</b> : la commune doit donc réguler la surfréquentation.</p>`,
  vocabulaire: [
    ["Station balnéaire", "Lieu de séjour situé en bord de mer, aménagé pour le tourisme."],
    ["Surfréquentation", "Présence de trop de visiteurs par rapport à la capacité d'un lieu."],
    ["Saisonnier", "Qui ne dure qu'une partie de l'année (l'été, par exemple)."],
    ["Patrimoine", "Ensemble des richesses naturelles et culturelles héritées du passé."]
  ],
  aRetenir: "Une station balnéaire est un lieu de séjour en bord de mer. Le tourisme y crée des emplois mais provoque aussi embouteillages, déchets et hausse des prix pour les habitants.",
  media: { base: "lecon-06-balneaire", legende: "Une station balnéaire" }
});

MISSION.lecon({
  id: "l07",
  titre: "Les mers et les océans qui bordent la France",
  objectifs: [
    "Nommer et situer les quatre mers et océans qui bordent la France.",
    "Nommer différents types d'hébergements touristiques.",
    "Calculer une densité de population et mesurer l'effet d'un afflux touristique."
  ],
  texte: `
    <p>La France métropolitaine est bordée par <b>quatre</b> grandes étendues d'eau :</p>
    <ul>
      <li>la <b>mer du Nord</b>, tout au nord, vers la Belgique ;</li>
      <li>la <b>Manche</b>, entre la France et le Royaume-Uni ;</li>
      <li>l'<b>océan Atlantique</b>, à l'ouest ; en le traversant, on rejoint l'Amérique ;</li>
      <li>la <b>mer Méditerranée</b>, au sud ; la Corse en est entourée.</li>
    </ul>
    <p>Le littoral <b>atlantique</b> (Biarritz, Arcachon, La Rochelle) attire beaucoup de vacanciers.
    Pour se loger, on trouve : hôtel, camping, caravane, mobil-home, gîte, chambre d'hôtes,
    village de vacances, location, auberge de jeunesse, tente, résidence.</p>
    <p>L'été, la population d'une commune littorale peut être multipliée par plusieurs fois.
    Exemple : Étretat mesure environ <b>4 km²</b> et compte <b>1 100 habitants</b>,
    soit une densité de <b>275 hab/km²</b>. Avec 15 000 touristes supplémentaires,
    la densité passe à <b>4 025 hab/km²</b> : elle est environ <b>multipliée par 15</b>.</p>`,
  vocabulaire: [
    ["Littoral", "Zone de contact entre la terre et la mer."],
    ["Hébergement", "Lieu où l'on dort pendant un séjour."],
    ["Densité", "Nombre d'habitants par km²."],
    ["Population saisonnière", "Population présente seulement pendant une partie de l'année."]
  ],
  aRetenir: "La France est bordée par la mer du Nord, la Manche, l'océan Atlantique et la mer Méditerranée. Sur le littoral, la population peut être multipliée par plus de dix pendant l'été.",
  media: { base: "lecon-07-littoral", decor: "france-mers", legende: "Les mers et océans bordant la France" }
});

MISSION.lecon({
  id: "l08",
  titre: "Les inégalités de niveau de vie dans le monde",
  objectifs: [
    "Identifier les manifestations des inégalités de niveau de vie.",
    "Localiser sur un planisphère les aires les plus riches et les plus pauvres.",
    "Lire un tableau d'indicateurs de développement."
  ],
  texte: `
    <p>Le <b>niveau de vie</b> n'est pas le même partout dans le monde. Pour le mesurer,
    on utilise plusieurs <b>indicateurs</b> :</p>
    <ul>
      <li>le <b>revenu par habitant</b> (combien d'argent chaque personne gagne en moyenne) ;</li>
      <li>l'<b>espérance de vie</b> (nombre d'années que l'on peut espérer vivre) ;</li>
      <li>le <b>nombre d'années de scolarisation</b> (combien d'années on va à l'école).</li>
    </ul>
    <p>Les pays les plus riches se trouvent surtout en <b>Amérique du Nord</b>, en
    <b>Europe</b>, en <b>Océanie</b> et dans quelques pays d'<b>Asie de l'Est</b>
    (Japon, Corée du Sud). Les pays les plus pauvres se trouvent majoritairement en
    <b>Afrique</b>, ainsi que dans certaines régions d'Asie du Sud.</p>
    <p>Une minorité de la population mondiale se partage la plus grande partie des richesses :
    c'est ce que montre la célèbre caricature du <b>gâteau</b> partagé très inégalement.</p>
    <p>Pour les enfants, la pauvreté a des conséquences graves : <b>travail des enfants</b>
    (décharges, fabriques de briques), <b>déscolarisation</b>, <b>malnutrition</b>,
    problèmes de <b>santé</b>.</p>`,
  vocabulaire: [
    ["Niveau de vie", "Ce que les habitants d'un pays peuvent se procurer avec leurs revenus."],
    ["Espérance de vie", "Nombre moyen d'années que peut vivre une personne dans un pays."],
    ["Pays développé", "Pays où le niveau de vie, la santé et l'école sont élevés."],
    ["Pays en développement", "Pays où le niveau de vie progresse mais reste faible."]
  ],
  aRetenir: "Le monde est marqué par de fortes inégalités : les pays riches se trouvent surtout en Amérique du Nord, en Europe et en Océanie ; les plus pauvres surtout en Afrique. On les compare grâce au revenu, à l'espérance de vie et à la scolarisation.",
  media: { base: "lecon-08-inegalites", decor: "planisphere-richesses", legende: "Les inégalités de richesse dans le monde" }
});

/* ---------------------------------------------------------
   PÉRIODE 3 — Se nourrir
   --------------------------------------------------------- */

MISSION.lecon({
  id: "l09",
  titre: "Se nourrir ici et ailleurs : des pratiques alimentaires différentes",
  objectifs: [
    "Comparer l'alimentation dans un pays riche et dans un pays pauvre.",
    "Comprendre le lien entre revenus et alimentation.",
    "Lire une carte de la sous-alimentation."
  ],
  texte: `
    <p>On ne mange pas la même chose partout. Les <b>pratiques alimentaires</b> dépendent
    du <b>climat</b>, des <b>cultures locales</b>, des <b>habitudes</b> et surtout des
    <b>revenus</b>.</p>
    <p>Au <b>Mali</b>, on mange surtout ce qui est produit sur place : mil, riz, arachides,
    haricots, gombo, mangue. Les aliments importés (pâtes, fromage, yaourt, pomme) coûtent
    très cher : un kilo de pâtes importées vaut environ cinq fois le prix d'un kilo de mil.
    Peu de familles possèdent un réfrigérateur, ce qui limite la conservation de la viande
    et du poisson.</p>
    <p>En <b>France</b>, un budget de 25 € permet d'acheter une grande variété d'aliments ;
    au Mali, une famille dispose souvent de moins de 10 € pour la même semaine.</p>
    <p>Quand l'alimentation est insuffisante, on parle de <b>sous-alimentation</b> :
    la personne ne mange pas assez pour couvrir ses besoins. Elle touche surtout l'Afrique
    subsaharienne (Tchad, Soudan, Madagascar) et certains pays comme <b>Haïti</b>.
    En France et aux États-Unis, elle concerne moins de 2,5 % de la population.</p>`,
  vocabulaire: [
    ["Pratique alimentaire", "Manière de se nourrir propre à un pays ou à une région."],
    ["Sous-alimentation", "Le fait de ne pas manger suffisamment pour couvrir ses besoins."],
    ["Malnutrition", "Alimentation déséquilibrée, insuffisante ou trop peu variée."],
    ["Importer", "Faire venir un produit depuis un autre pays."]
  ],
  aRetenir: "Les pratiques alimentaires diffèrent selon le climat, les habitudes et surtout les revenus. Dans les pays pauvres, la sous-alimentation touche encore une part importante de la population.",
  media: { base: "lecon-09-alimentation", legende: "Un marché au Mali" }
});

MISSION.lecon({
  id: "l10",
  titre: "Produits agricoles et produits transformés",
  objectifs: [
    "Distinguer un produit agricole d'un produit transformé.",
    "Relier un produit transformé à son produit agricole d'origine.",
    "Nommer les espaces de production et les métiers correspondants."
  ],
  texte: `
    <p>Un <b>produit agricole</b> vient directement de la nature : il est cultivé ou élevé,
    puis consommé presque tel quel. Exemples : une pomme, une carotte, des haricots verts,
    du blé, du lait, un œuf.</p>
    <p>Un <b>produit transformé</b> (ou produit dérivé) est fabriqué <b>à partir</b> d'un
    produit agricole, dans un atelier ou une usine. Exemples : le pain (blé), le fromage
    et le yaourt (lait), le jus de raisin (raisin), la sauce tomate (tomate), le sucre
    (canne à sucre ou betterave), le chocolat (cacao).</p>
    <p>Chaque aliment vient d'un <b>espace de production</b> et d'un <b>métier</b> :</p>
    <ul>
      <li>l'<b>élevage</b> → l'éleveur (volailles, œufs, lait, viande) ;</li>
      <li>le <b>champ de céréales</b> → le céréalier (blé, maïs) ;</li>
      <li>l'<b>exploitation maraîchère</b> → le maraîcher (carottes, salades, haricots) ;</li>
      <li>le <b>verger</b> → l'arboriculteur (pommes, poires, cerises).</li>
    </ul>`,
  vocabulaire: [
    ["Produit agricole", "Produit qui vient directement de la culture ou de l'élevage."],
    ["Produit transformé", "Produit fabriqué à partir d'un ou de plusieurs produits agricoles."],
    ["Maraîcher", "Agriculteur qui cultive des légumes."],
    ["Verger", "Terrain planté d'arbres fruitiers."]
  ],
  aRetenir: "Un produit agricole vient directement de la nature ; un produit transformé est fabriqué à partir d'un produit agricole. Chaque aliment est lié à un espace de production et à un métier.",
  media: { base: "lecon-10-produits", legende: "Un plateau de cantine" }
});

/* ---------------------------------------------------------
   PÉRIODE 4 — Chaîne de production, circuits, relief et fleuves
   --------------------------------------------------------- */

MISSION.lecon({
  id: "l11",
  titre: "La chaîne de production d'un aliment : du lait au yaourt",
  objectifs: [
    "Remettre dans l'ordre les étapes de la production d'un yaourt.",
    "Identifier ce qui se passe à la ferme, à l'usine et au magasin.",
    "Comprendre le rôle de la chaîne du froid."
  ],
  texte: `
    <p>La <b>chaîne de production</b> décrit toutes les étapes qui séparent la matière
    première de l'assiette du consommateur. Pour un yaourt :</p>
    <ol>
      <li><b>À la ferme</b> : les vaches sont <b>traites</b>, chaque jour. Le lait est
      immédiatement <b>refroidi</b> et stocké dans un tank réfrigéré.</li>
      <li><b>Transport</b> : un camion-citerne <b>réfrigéré</b> collecte le lait et l'apporte à l'usine.</li>
      <li><b>À l'usine</b> : le lait est <b>analysé</b>, puis stocké dans de grands réservoirs.
      Il est chauffé (pasteurisation), des <b>ferments</b> sont ajoutés, et le mélange repose :
      le yaourt <b>fermente</b> et s'épaissit.</li>
      <li><b>Conditionnement</b> : le yaourt est versé dans des <b>pots</b>, fermés par un couvercle,
      puis rangés en palettes.</li>
      <li><b>Distribution</b> : des camions frigorifiques livrent les <b>supermarchés</b>.</li>
      <li><b>Consommation</b> : le yaourt est vendu, puis conservé au frigo à la maison.</li>
    </ol>
    <p>La <b>chaîne du froid</b> ne doit jamais être interrompue : sans réfrigération,
    des microbes se développent dans le lait, qui tourne et devient impropre à la consommation.</p>`,
  vocabulaire: [
    ["Chaîne de production", "Suite des étapes de la matière première au produit consommé."],
    ["Traite", "Action de recueillir le lait de la vache."],
    ["Ferment", "Micro-organisme ajouté au lait pour le transformer en yaourt."],
    ["Chaîne du froid", "Maintien du froid tout au long du transport et du stockage."]
  ],
  aRetenir: "Du pré au frigo, un yaourt passe par la ferme, le transport réfrigéré, l'usine, le conditionnement, la distribution puis la vente. La chaîne du froid ne doit jamais être rompue.",
  media: { base: "lecon-11-chaine", legende: "De la ferme à l'usine" }
});

MISSION.lecon({
  id: "l12",
  titre: "Les kilomètres alimentaires et la consommation responsable",
  objectifs: [
    "Calculer les kilomètres alimentaires d'un repas.",
    "Localiser sur un planisphère l'origine des produits consommés.",
    "Proposer des gestes pour réduire l'impact de son alimentation."
  ],
  texte: `
    <p>Les <b>kilomètres alimentaires</b> représentent la distance totale parcourue par un
    aliment avant d'arriver dans notre assiette. Plus cette distance est grande, plus le
    transport rejette de <b>CO₂</b> dans l'atmosphère, ce qui dégrade la qualité de l'air
    et contribue au <b>réchauffement climatique</b>.</p>
    <p>Dans un supermarché français, les étiquettes révèlent des origines très variées :
    fraises d'Espagne, bananes du Cameroun, noisettes de Turquie, oranges d'Afrique du Sud,
    citrons d'Argentine, feta de Grèce, poires du Chili, myrtilles du Portugal,
    kiwis de Nouvelle-Zélande, mangues du Brésil.</p>
    <p>Pour réduire ces kilomètres, on peut :</p>
    <ul>
      <li>acheter en <b>circuit court</b>, directement au producteur ;</li>
      <li>privilégier les <b>produits locaux</b> ;</li>
      <li>choisir des fruits et légumes <b>de saison</b> ;</li>
      <li>manger <b>moins de viande</b>.</li>
    </ul>
    <p>Attention : « manger moins salé » ou « ne pas laver ses fruits » n'a aucun effet sur
    les kilomètres alimentaires !</p>`,
  vocabulaire: [
    ["Kilomètres alimentaires", "Distance totale parcourue par un aliment jusqu'au consommateur."],
    ["Circuit court", "Vente directe, ou avec un seul intermédiaire, entre producteur et consommateur."],
    ["Produit de saison", "Produit récolté au moment naturel de sa production."],
    ["CO₂", "Gaz rejeté par les transports, responsable du réchauffement climatique."]
  ],
  aRetenir: "Chaque aliment parcourt une distance avant d'arriver dans notre assiette. Acheter local, de saison et en circuit court réduit fortement ces kilomètres alimentaires.",
  media: { base: "lecon-12-km", decor: "planisphere", legende: "D'où viennent nos aliments ?" }
});

MISSION.lecon({
  id: "l13",
  titre: "Les principaux fleuves et massifs montagneux de France",
  objectifs: [
    "Situer et nommer les cinq principaux fleuves français.",
    "Situer et nommer les six grands massifs montagneux.",
    "Distinguer un fleuve d'une rivière."
  ],
  texte: `
    <p>Un <b>fleuve</b> est un cours d'eau qui se jette dans la <b>mer</b> ou dans l'océan.
    Une <b>rivière</b>, elle, se jette dans un autre cours d'eau.</p>
    <p>Les <b>cinq principaux fleuves</b> français :</p>
    <ul>
      <li>la <b>Seine</b> : traverse Paris, se jette dans la Manche au Havre ;</li>
      <li>la <b>Loire</b> : le plus long fleuve de France (1 006 km), se jette dans l'Atlantique ;</li>
      <li>la <b>Garonne</b> : vient des Pyrénées, se jette dans l'Atlantique par l'estuaire de la Gironde ;</li>
      <li>le <b>Rhône</b> : vient de Suisse, se jette dans la Méditerranée ;</li>
      <li>le <b>Rhin</b> : à la frontière avec l'Allemagne, se jette dans la mer du Nord.</li>
    </ul>
    <p>Les <b>six grands massifs</b> :</p>
    <ul>
      <li>les <b>Alpes</b> : les plus hautes (mont Blanc, 4 806 m) ;</li>
      <li>les <b>Pyrénées</b> : frontière avec l'Espagne ;</li>
      <li>le <b>Massif central</b> : au centre, formé d'anciens volcans ;</li>
      <li>le <b>Jura</b> : à la frontière suisse ;</li>
      <li>les <b>Vosges</b> : à l'est, aux sommets arrondis (les ballons) ;</li>
      <li>les montagnes de <b>Corse</b>.</li>
    </ul>
    <p>Les montagnes retiennent la neige : en fondant au printemps, elle alimente les fleuves.</p>`,
  vocabulaire: [
    ["Fleuve", "Cours d'eau qui se jette dans la mer ou dans l'océan."],
    ["Rivière", "Cours d'eau qui se jette dans un autre cours d'eau."],
    ["Massif montagneux", "Ensemble de montagnes formant un même relief."],
    ["Sommet", "Point le plus élevé d'une montagne."]
  ],
  aRetenir: "Cinq grands fleuves (Seine, Loire, Garonne, Rhône, Rhin) et six grands massifs (Alpes, Pyrénées, Massif central, Jura, Vosges, Corse) organisent le relief et les eaux de la France.",
  media: { base: "lecon-13-fleuves", decor: "france-fleuves", legende: "Fleuves et massifs de France" }
});

/* ---------------------------------------------------------
   PÉRIODE 5 — Les usages de l'eau douce
   --------------------------------------------------------- */

MISSION.lecon({
  id: "l14",
  titre: "Le trajet de l'eau, de la source à la mer",
  objectifs: [
    "Nommer les éléments d'un cours d'eau, de l'amont vers l'aval.",
    "Ordonner des paysages de la source à l'embouchure.",
    "Employer le vocabulaire du cours d'eau."
  ],
  texte: `
    <p>L'eau d'un fleuve vient de la pluie et de la fonte des neiges en montagne.
    Elle descend ensuite jusqu'à la mer en suivant toujours le même trajet :</p>
    <p style="text-align:center"><b>source → torrent → ruisseau → rivière → fleuve → estuaire → mer</b></p>
    <ul>
      <li>la <b>source</b> : l'endroit où l'eau sort du sol ;</li>
      <li>l'<b>amont</b> : la partie du cours d'eau située entre un point donné et la source ;</li>
      <li>l'<b>aval</b> : la partie située entre un point donné et l'embouchure ;</li>
      <li>un <b>affluent</b> : un cours d'eau qui se jette dans un autre ;</li>
      <li>une <b>confluence</b> : l'endroit où deux cours d'eau se rejoignent ;</li>
      <li>un <b>méandre</b> : une courbe formée par un cours d'eau ;</li>
      <li>la <b>berge</b> (ou rive) : la bande de terre qui borde le cours d'eau ;</li>
      <li>l'<b>embouchure</b> : l'endroit où le fleuve se jette dans la mer ; elle est simple
      (<b>estuaire</b>) ou ramifiée (<b>delta</b>) ;</li>
      <li>l'<b>estuaire</b> : zone où l'eau douce se mélange à l'eau salée.</li>
    </ul>
    <p>En descendant, le cours d'eau devient plus large et son <b>débit</b> augmente,
    parce qu'il reçoit l'eau de ses affluents.</p>`,
  vocabulaire: [
    ["Amont", "Vers la source."],
    ["Aval", "Vers l'embouchure."],
    ["Affluent", "Cours d'eau qui se jette dans un autre cours d'eau."],
    ["Embouchure", "Endroit où un fleuve se jette dans la mer."],
    ["Débit", "Quantité d'eau qui passe en un point en une seconde."]
  ],
  aRetenir: "De la source à l'embouchure, l'eau descend de l'amont vers l'aval, grossie par ses affluents. Elle rejoint la mer par un estuaire ou par un delta.",
  media: { base: "lecon-14-cours-eau", decor: "cours-eau", legende: "Vue d'ensemble d'un cours d'eau" }
});

MISSION.lecon({
  id: "l15",
  titre: "Les usages de l'eau douce en France",
  objectifs: [
    "Nommer les cinq grands usages de l'eau douce.",
    "Lire un diagramme circulaire de répartition.",
    "Décrire le trajet de l'eau consommée, du prélèvement au rejet."
  ],
  texte: `
    <p>L'eau douce est utilisée pour cinq grands <b>usages</b> :</p>
    <ul>
      <li><b>agricole</b> : irrigation des cultures — <b>48 %</b> de l'eau consommée ;</li>
      <li><b>domestique</b> : boisson, hygiène, sanitaires, ménage — <b>24 %</b> ;</li>
      <li><b>énergétique</b> : centrales hydroélectriques, refroidissement des centrales — <b>22 %</b> ;</li>
      <li><b>industriel</b> : lavage, refroidissement, chaudières — <b>6 %</b> ;</li>
      <li><b>de loisirs</b> : piscines, patinoires, stations de ski, parcs d'attractions.</li>
    </ul>
    <p>L'usage domestique ne représente donc qu'environ <b>un quart</b> de la consommation.</p>
    <p>Un Français consomme en moyenne <b>150 litres par jour</b>. Le bain et la douche
    (58,5 L) et les sanitaires (30 L) en représentent la plus grande part ; la boisson
    ne compte que <b>1,5 L</b>.</p>
    <p>Le trajet de l'eau consommée comprend six étapes : <b>prélèvement</b> dans la rivière
    ou la nappe, <b>potabilisation</b>, <b>stockage</b> (château d'eau), <b>distribution</b>,
    <b>collecte</b> des eaux usées, <b>traitement</b> à la station d'épuration, puis
    <b>rejet</b> en aval du point de prélèvement. L'eau épurée n'est pas potable, mais
    elle peut être rendue au milieu naturel sans le polluer.</p>`,
  vocabulaire: [
    ["Eau potable", "Eau que l'on peut boire sans danger."],
    ["Potabilisation", "Traitement qui rend l'eau propre à la consommation."],
    ["Assainissement", "Collecte et traitement des eaux usées."],
    ["Station d'épuration", "Installation qui nettoie les eaux usées avant leur rejet."]
  ],
  aRetenir: "L'agriculture consomme près de la moitié de l'eau douce en France, l'usage domestique un quart seulement. L'eau prélevée est potabilisée, distribuée, puis épurée avant d'être rejetée en aval.",
  media: { base: "lecon-15-usages", decor: "paysage-eau", legende: "Le trajet de l'eau consommée" }
});

MISSION.lecon({
  id: "l16",
  titre: "L'eau, une ressource convoitée : les conflits d'usage",
  objectifs: [
    "Comprendre pourquoi l'eau peut manquer.",
    "Identifier les usages prioritaires en cas de sécheresse.",
    "Lire un arrêté préfectoral et en tirer des règles."
  ],
  texte: `
    <p>L'eau douce n'est pas illimitée. Quand il pleut trop peu, les rivières baissent,
    les nappes se vident : c'est la <b>sécheresse</b>. Tous les usagers veulent alors
    la même eau : c'est un <b>conflit d'usage</b>.</p>
    <p>Dans chaque département, le <b>préfet</b> peut prendre un <b>arrêté</b> qui limite
    les usages. Il ne décide pas dans son intérêt personnel : il applique la loi et protège
    l'intérêt général. Selon le niveau d'alerte :</p>
    <ul>
      <li>restent <b>autorisés</b> : boire et cuisiner, abreuver les animaux d'élevage,
      lutter contre les incendies ;</li>
      <li>sont <b>autorisés avec restrictions</b> : l'irrigation des cultures (souvent la nuit
      seulement), le fonctionnement des usines ;</li>
      <li>sont <b>interdits</b> : arroser son jardin ou sa pelouse, remplir une piscine privée,
      laver sa voiture hors station professionnelle, nettoyer les terrasses et façades,
      pratiquer certaines activités nautiques.</li>
    </ul>
    <p>La règle générale est simple : <b>l'eau potable destinée à la consommation humaine
    est prioritaire</b>, et chacun doit économiser l'eau au quotidien.</p>
    <p>Le changement climatique rend ces épisodes plus fréquents : mieux partager l'eau
    devient une question essentielle pour l'avenir.</p>`,
  vocabulaire: [
    ["Sécheresse", "Manque durable de pluie qui réduit les réserves d'eau."],
    ["Conflit d'usage", "Désaccord entre plusieurs utilisateurs d'une même ressource."],
    ["Préfet", "Représentant de l'État dans le département."],
    ["Arrêté préfectoral", "Décision écrite du préfet, applicable dans le département."]
  ],
  aRetenir: "En cas de sécheresse, l'eau devient une ressource convoitée. Le préfet fixe des priorités : l'eau potable d'abord, puis les animaux et la sécurité ; les usages de confort sont interdits.",
  media: { base: "lecon-16-secheresse", legende: "Une rivière à sec" }
});
