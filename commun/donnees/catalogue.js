/* ============================================================
   CATALOGUE DES JEUX — données publiques communes
   ------------------------------------------------------------
   Les 26 jeux de la progression (calendrier de production :
   prompts-opus/00-ORDRE-DE-PRODUCTION.md) et les jeux hors liste
   (Déclaration, Constitution, Mission géographique, Tour du monde) :
   matière, année A/B, période, points du programme, dossier s'il est
   déjà publié. Utilisé par l'accueil (frise, vue de l'année, FAQ,
   démonstration), les liens « jeu suivant » en fin de partie, le
   passeport de compétences et les fiches de période.
   Un nouveau jeu publié : renseigner son « dossier » (et ses couleurs).
   Fichier .js (et non .json) pour fonctionner aussi en double-clic.
   ============================================================ */
var CATALOGUE = {
 "genere": "2026-10-01",
 "source": "prompts-opus/00-ORDRE-DE-PRODUCTION.md (calendrier de production) et README des jeux",
 "periodes": {
  "P1": "septembre-octobre",
  "P2": "novembre-décembre",
  "P3": "janvier-février",
  "P4": "mars-avril",
  "P5": "mai-juin"
 },
 "jeux": [
  {
   "num": "01",
   "id": "moyen-age-abbaye",
   "titre": "Le Manuscrit de l'abbaye",
   "matiere": "Histoire",
   "annee": "A",
   "periodes": [
    "P1"
   ],
   "competences": "Décrire le rôle social de l'Église (pauvres et malades, enseignement) ; différencier art roman et art gothique.",
   "dossier": "moyen-age-abbaye",
   "icone": "📜",
   "couleurs": [
    "#7a3b1d",
    "#c9a227"
   ],
   "resume": "La veille de la visite de l'évêque, cinq pages d'un manuscrit enluminé ont disparu. De Clovis aux cathédrales gothiques, les apprentis copistes les refont une à une.",
   "prompt": "01-moyen-age-abbaye.md",
   "programme": [
    "hg2026"
   ]
  },
  {
   "num": "02",
   "id": "chateau-fort",
   "titre": "Le Secret du donjon",
   "matiere": "Histoire",
   "annee": "B",
   "periodes": [
    "P1"
   ],
   "competences": "Décrire les fonctions d'un château fort ; raconter la vie quotidienne des paysannes et des paysans.",
   "dossier": "chateau-fort",
   "icone": "🏰",
   "couleurs": [
    "#3d5266",
    "#c9a227"
   ],
   "resume": "Le seigneur est parti rejoindre le roi. Pages et jeunes paysans parcourent le château et le village pour retrouver les cinq clés de la seigneurie et relever la herse.",
   "prompt": "02-chateau-fort.md",
   "programme": [
    "hg2026"
   ]
  },
  {
   "num": "03",
   "id": "station-meteo",
   "titre": "La Station météo disparue",
   "matiere": "Sciences",
   "annee": "A",
   "periodes": [
    "P1"
   ],
   "competences": "Réaliser et exploiter des mesures météorologiques avec des capteurs (thermomètre, anémomètre, pluviomètre).",
   "dossier": "station-meteo",
   "icone": "🌦️",
   "couleurs": [
    "#1d5c8f",
    "#f2c14e"
   ],
   "resume": "Un orage a déréglé la station météo de l'école : cinq modules à remettre en service pour lancer le bulletin avant la sortie.",
   "prompt": "03-station-meteo.md",
   "programme": [
    "st2026"
   ]
  },
  {
   "num": "04",
   "id": "objets-techniques",
   "titre": "L'Atelier de l'inventeur",
   "matiere": "Sciences",
   "annee": "A",
   "periodes": [
    "P1"
   ],
   "competences": "Décrire le fonctionnement et la constitution d'objets techniques.",
   "dossier": "objets-techniques",
   "icone": "⚙️",
   "couleurs": [
    "#1e5a6e",
    "#a8461b"
   ],
   "resume": "L'inventrice est partie en voyage en laissant cinq machines démontées. Besoin, fonction, matériau, énergie, notice : cinq mots pour ouvrir son coffre-fort.",
   "prompt": "04-objets-techniques.md",
   "programme": [
    "st2026"
   ]
  },
  {
   "num": "05",
   "id": "melanges",
   "titre": "Le Laboratoire de Madame Mélange",
   "matiere": "Sciences",
   "annee": "B",
   "periodes": [
    "P1"
   ],
   "competences": "Comparer/mesurer des masses ; distinguer mélanges homogènes/hétérogènes ; séparer leurs constituants.",
   "dossier": "melanges",
   "icone": "⚗️",
   "couleurs": [
    "#1f5f6b",
    "#8e3b62"
   ],
   "resume": "L'apprentie de Madame Mélange a renversé toutes les fioles. Peser, observer, trier, filtrer, évaporer : cinq opérations à retrouver.",
   "prompt": "05-melanges.md",
   "programme": [
    "st2026"
   ]
  },
  {
   "num": "06",
   "id": "versailles",
   "titre": "De l'édit de Nantes à Versailles",
   "matiere": "Histoire",
   "annee": "A",
   "periodes": [
    "P2"
   ],
   "competences": "La naissance du protestantisme (édit de Nantes) ; la monarchie absolue à Versailles.",
   "dossier": "versailles",
   "icone": "👑",
   "couleurs": [
    "#2a3f6b",
    "#c9a227"
   ],
   "resume": "Un pli scellé de 1598 traverse un siècle de monarchie : de l'imprimerie d'une huguenote aux jardins de Versailles, les secrétaires du roi lèvent ses cinq sceaux.",
   "prompt": "06-versailles.md",
   "programme": [
    "hg2026"
   ]
  },
  {
   "num": "07",
   "id": "renaissance",
   "titre": "L'Atelier de Léonard à Amboise",
   "matiere": "Histoire",
   "annee": "B",
   "periodes": [
    "P2"
   ],
   "competences": "François Ier, protecteur des arts et des lettres à la Renaissance (Léonard de Vinci).",
   "dossier": "renaissance",
   "icone": "🎨",
   "couleurs": [
    "#8a4b1e",
    "#c9a227"
   ],
   "resume": "À Amboise, en 1518, un coup de vent disperse cinq pages du carnet de Léonard de Vinci : les élèves les retrouvent avant la grande fête de François Ier.",
   "prompt": "07-renaissance.md",
   "programme": [
    "hg2026"
   ]
  },
  {
   "num": "08",
   "id": "alimentation",
   "titre": "Le Grand Repas du chef",
   "matiere": "Sciences",
   "annee": "A",
   "periodes": [
    "P2"
   ],
   "competences": "Besoins alimentaires et nutrition humaine : grandir, des besoins qui varient, mâcher, digérer ; le sang livre les nutriments.",
   "dossier": "alimentation",
   "icone": "🍲",
   "couleurs": [
    "#2b5d6b",
    "#7fb3c8"
   ],
   "resume": "Au restaurant Le Grand Couvert, la cheffe Rosalie prépare le repas d'un coureur cycliste : les élèves, ses commis, retrouvent les cinq mots du coffre, de la croissance au sang qui livre les nutriments.",
   "prompt": "08-alimentation.md",
   "programme": [
    "st2026"
   ]
  },
  {
   "num": "09",
   "id": "lumiere",
   "titre": "Le Phare de l'île Lumière",
   "matiere": "Sciences",
   "annee": "A",
   "periodes": [
    "P2"
   ],
   "competences": "La lumière (matière, mouvement, énergie et information).",
   "dossier": null,
   "icone": "💡",
   "couleurs": [
    "#2b5d6b",
    "#7fb3c8"
   ],
   "resume": "",
   "prompt": "09-lumiere.md",
   "programme": [
    "st2026"
   ]
  },
  {
   "num": "10",
   "id": "etats-matiere",
   "titre": "La Fabrique des états",
   "matiere": "Sciences",
   "annee": "B",
   "periodes": [
    "P2"
   ],
   "competences": "États et constitution de la matière à l'échelle macroscopique ; propriétés de la matière.",
   "dossier": null,
   "icone": "🧊",
   "couleurs": [
    "#2b5d6b",
    "#7fb3c8"
   ],
   "resume": "",
   "prompt": "10-etats-matiere.md",
   "programme": [
    "st2026"
   ]
  },
  {
   "num": "11",
   "id": "mouvement",
   "titre": "Le Grand Prix de l'observatoire",
   "matiere": "Sciences",
   "annee": "B",
   "periodes": [
    "P2"
   ],
   "competences": "Mesurer une distance et une durée lors d'un déplacement ; différents types de mouvement.",
   "dossier": null,
   "icone": "⏱️",
   "couleurs": [
    "#2b5d6b",
    "#7fb3c8"
   ],
   "resume": "",
   "prompt": "11-mouvement.md",
   "programme": [
    "st2026"
   ]
  },
  {
   "num": "12",
   "id": "traite-colonies",
   "titre": "Les Archives du port",
   "matiere": "Histoire",
   "annee": "A",
   "periodes": [
    "P3"
   ],
   "competences": "La traite des esclaves Afrique-Amérique ; les échanges commerciaux avec les colonies.",
   "dossier": null,
   "icone": "⚓",
   "couleurs": [
    "#6b4a2b",
    "#c9a227"
   ],
   "resume": "",
   "prompt": "12-traite-colonies.md",
   "programme": [
    "hg2026"
   ]
  },
  {
   "num": "13",
   "id": "grandes-explorations",
   "titre": "La Caravelle du capitaine",
   "matiere": "Histoire",
   "annee": "B",
   "periodes": [
    "P3"
   ],
   "competences": "Les progrès techniques des explorations ; la constitution des premiers empires coloniaux.",
   "dossier": null,
   "icone": "⛵",
   "couleurs": [
    "#6b4a2b",
    "#c9a227"
   ],
   "resume": "",
   "prompt": "13-grandes-explorations.md",
   "programme": [
    "hg2026"
   ]
  },
  {
   "num": "14",
   "id": "electricite",
   "titre": "La Centrale en panne",
   "matiere": "Sciences",
   "annee": "A",
   "periodes": [
    "P3"
   ],
   "competences": "L'électricité.",
   "dossier": null,
   "icone": "🔌",
   "couleurs": [
    "#2b5d6b",
    "#7fb3c8"
   ],
   "resume": "",
   "prompt": "14-electricite.md",
   "programme": [
    "st2026"
   ]
  },
  {
   "num": "15",
   "id": "naissances-animaux",
   "titre": "La Nurserie du zoo",
   "matiere": "Sciences",
   "annee": "B",
   "periodes": [
    "P3"
   ],
   "competences": "Étapes du développement des animaux (fécondation à la naissance) ; reproduction ovipare/vivipare.",
   "dossier": null,
   "icone": "🐣",
   "couleurs": [
    "#2b5d6b",
    "#7fb3c8"
   ],
   "resume": "",
   "prompt": "15-naissances-animaux.md",
   "programme": [
    "st2026"
   ]
  },
  {
   "num": "16",
   "id": "napoleon-republique",
   "titre": "Le Testament de l'Empereur",
   "matiere": "Histoire",
   "annee": "B",
   "periodes": [
    "P4"
   ],
   "competences": "Napoléon, du général à l'empereur ; lieux, symboles et rites de la République ; lois protectrices des libertés.",
   "dossier": null,
   "icone": "🦅",
   "couleurs": [
    "#6b4a2b",
    "#c9a227"
   ],
   "resume": "",
   "prompt": "16-napoleon-republique.md",
   "programme": [
    "hg2026"
   ]
  },
  {
   "num": "17",
   "id": "vivant-ecosystemes",
   "titre": "L'Expédition biodiversité",
   "matiere": "Sciences",
   "annee": "A",
   "periodes": [
    "P4"
   ],
   "competences": "Panorama du vivant, biodiversité ; structure et dynamique d'un écosystème.",
   "dossier": null,
   "icone": "🦋",
   "couleurs": [
    "#2b5d6b",
    "#7fb3c8"
   ],
   "resume": "",
   "prompt": "17-vivant-ecosystemes.md",
   "programme": [
    "st2026"
   ]
  },
  {
   "num": "18",
   "id": "programmation-robot",
   "titre": "Le Robot de l'atelier",
   "matiere": "Sciences",
   "annee": "B",
   "periodes": [
    "P4"
   ],
   "competences": "Traduire un langage simple en langage naturel ; utiliser un programme pour agir sur un objet technique.",
   "dossier": null,
   "icone": "🤖",
   "couleurs": [
    "#2b5d6b",
    "#7fb3c8"
   ],
   "resume": "",
   "prompt": "18-programmation-robot.md",
   "programme": [
    "st2026"
   ]
  },
  {
   "num": "19",
   "id": "grande-guerre",
   "titre": "Les Lettres du poilu",
   "matiere": "Histoire",
   "annee": "A",
   "periodes": [
    "P5"
   ],
   "competences": "Première Guerre mondiale : causes, déroulement, conséquences.",
   "dossier": null,
   "icone": "✉️",
   "couleurs": [
    "#6b4a2b",
    "#c9a227"
   ],
   "resume": "",
   "prompt": "19-grande-guerre.md",
   "programme": [
    "hg2026"
   ]
  },
  {
   "num": "20",
   "id": "seconde-guerre",
   "titre": "Radio Londres",
   "matiere": "Histoire",
   "annee": "A",
   "periodes": [
    "P5"
   ],
   "competences": "Seconde Guerre mondiale : montée des extrêmes, collaboration et résistance, victoire des alliés.",
   "dossier": null,
   "icone": "📻",
   "couleurs": [
    "#6b4a2b",
    "#c9a227"
   ],
   "resume": "",
   "prompt": "20-seconde-guerre.md",
   "programme": [
    "hg2026"
   ]
  },
  {
   "num": "21",
   "id": "age-industriel",
   "titre": "L'Exposition universelle",
   "matiere": "Histoire",
   "annee": "B",
   "periodes": [
    "P5"
   ],
   "competences": "Énergies et machines ; la ville industrielle, révolution industrielle et progrès technique.",
   "dossier": null,
   "icone": "🏭",
   "couleurs": [
    "#6b4a2b",
    "#c9a227"
   ],
   "resume": "",
   "prompt": "21-age-industriel.md",
   "programme": [
    "hg2026"
   ]
  },
  {
   "num": "22",
   "id": "europe",
   "titre": "Le Traité perdu de Rome",
   "matiere": "Histoire",
   "annee": "B",
   "periodes": [
    "P5"
   ],
   "competences": "La construction européenne : CECA, CEE, UE (monnaie unique, institutions).",
   "dossier": null,
   "icone": "🇪🇺",
   "couleurs": [
    "#6b4a2b",
    "#c9a227"
   ],
   "resume": "",
   "prompt": "22-europe.md",
   "programme": [
    "hg2026"
   ]
  },
  {
   "num": "23",
   "id": "terre-active",
   "titre": "L'Observatoire des volcans",
   "matiere": "Sciences",
   "annee": "A",
   "periodes": [
    "P5"
   ],
   "competences": "La Terre, une planète active (activité interne).",
   "dossier": null,
   "icone": "🌋",
   "couleurs": [
    "#2b5d6b",
    "#7fb3c8"
   ],
   "resume": "",
   "prompt": "23-terre-active.md",
   "programme": [
    "st2026"
   ]
  },
  {
   "num": "24",
   "id": "reproduction",
   "titre": "Le Jardin de la vie",
   "matiere": "Sciences",
   "annee": "A",
   "periodes": [
    "P5"
   ],
   "competences": "La reproduction sexuelle chez le vivant.",
   "dossier": null,
   "icone": "🌱",
   "couleurs": [
    "#2b5d6b",
    "#7fb3c8"
   ],
   "resume": "",
   "prompt": "24-reproduction.md",
   "programme": [
    "st2026"
   ]
  },
  {
   "num": "25",
   "id": "cerveau",
   "titre": "Le Labo des illusions",
   "matiere": "Sciences",
   "annee": "B",
   "periodes": [
    "P5"
   ],
   "competences": "Le cerveau ; mécanismes perceptifs ; stratégies d'attention et de mémorisation.",
   "dossier": null,
   "icone": "🧠",
   "couleurs": [
    "#2b5d6b",
    "#7fb3c8"
   ],
   "resume": "",
   "prompt": "25-cerveau.md",
   "programme": [
    "st2026"
   ]
  },
  {
   "num": "26",
   "id": "climat",
   "titre": "Mission Climat",
   "matiere": "Sciences",
   "annee": "B",
   "periodes": [
    "P5"
   ],
   "competences": "Définir le climat local ; conséquences du changement climatique, atténuation/adaptation.",
   "dossier": null,
   "icone": "🌍",
   "couleurs": [
    "#2b5d6b",
    "#7fb3c8"
   ],
   "resume": "",
   "prompt": "26-climat.md",
   "programme": [
    "st2026"
   ]
  },
  {
   "num": "D",
   "id": "declaration",
   "titre": "Le Secret de la Déclaration",
   "matiere": "Histoire",
   "annee": "A",
   "periodes": [
    "P4"
   ],
   "competences": "Le temps de la Révolution et l'Empire : le contexte de 1789, la fin de la monarchie absolue, les nouveaux principes (Déclaration des droits de l'homme et du citoyen).",
   "dossier": "declaration",
   "icone": "🏛️",
   "suite": "constitution",
   "couleurs": [
    "#1d3a8a",
    "#b22222"
   ],
   "resume": "Paris, août 1789 : un article secret de la Déclaration des droits de l'homme a été volé. Quatre fragments à retrouver.",
   "programme": [
    "hg2026"
   ]
  },
  {
   "num": "C",
   "id": "constitution",
   "titre": "Le Sceau de la République",
   "matiere": "EMC",
   "annee": "B",
   "periodes": [
    "P4"
   ],
   "competences": "La Constitution du 4 octobre 1958 ; lois protectrices des droits et des libertés (EMC et histoire).",
   "dossier": "constitution",
   "icone": "⚖️",
   "precedent": "declaration",
   "couleurs": [
    "#5b2b6b",
    "#c9a227"
   ],
   "resume": "Au Palais-Royal, un coffre scellé le 4 octobre 1958 porte cinq serrures. Cinq mots à trouver, de la cour du Conseil constitutionnel à l'hémicycle.",
   "programme": [
    "emc2024",
    "hg2026"
   ]
  },
  {
   "num": "G",
   "id": "mission-geo",
   "titre": "Mission géographique",
   "matiere": "Géographie",
   "annee": "B",
   "periodes": [
    "P1",
    "P2",
    "P3",
    "P4",
    "P5"
   ],
   "competences": "L'organisation du territoire français (P1) ; les inégalités dans le monde (P2) ; se nourrir (P3-P4) ; les usages de l'eau douce (P4-P5). 16 séances sur l'année.",
   "dossier": "mission-geo",
   "icone": "🗺️",
   "toutelannee": true,
   "couleurs": [
    "#2f6b3a",
    "#d9a21b"
   ],
   "resume": "Une valise volée, seize séances pour réunir les indices, une piste finale en Corse et une récompense mystère.",
   "seancesParPeriode": {
    "P1": [
     1,
     2,
     3,
     4,
     5
    ],
    "P2": [
     6,
     7,
     8
    ],
    "P3": [
     9,
     10
    ],
    "P4": [
     11,
     12,
     13
    ],
    "P5": [
     14,
     15,
     16
    ]
   },
   "programme": [
    "hg2026"
   ]
  },
  {
   "num": "T",
   "id": "tour-du-monde",
   "titre": "Le Tour du Monde en 80 minutes",
   "matiere": "Géographie",
   "annee": "AB",
   "periodes": [],
   "competences": "Repères et méthodes : planisphère (continents, océans), itinéraire et canaux, climats et paysages, échelle et transports, méridiens et fuseaux horaires. Jeu de révision, à placer librement.",
   "dossier": "tour-du-monde",
   "icone": "🧭",
   "libre": true,
   "couleurs": [
    "#0f4c5c",
    "#c08a3e"
   ],
   "resume": "Le carnet de route de Phileas Fogg a disparu. Cinq escales, cinq énigmes de géographie, et le mystère du 80ᵉ jour.",
   "programme": [
    "hg2026"
   ]
  }
 ],
 "programmes": {
  "hg2026": {
   "discipline": "Histoire-géographie, cycle 3",
   "texte": "Arrêté du 22 avril 2026 — BO n° 22 du 28 mai 2026",
   "nor": "MENE2608631A",
   "lien": "https://www.education.gouv.fr/bo/2026/Hebdo22/MENE2608631A",
   "vigueur": "en CM1 à la rentrée 2026, en CM2 à la rentrée 2027"
  },
  "st2026": {
   "discipline": "Sciences et technologie, cycles 2 et 3",
   "texte": "Arrêté du 5 juin 2026 — BO n° 24 du 11 juin 2026",
   "nor": "MENE2611650A",
   "lien": "https://www.education.gouv.fr/bo/2026/Hebdo24/MENE2611650A",
   "vigueur": "en CM1 à la rentrée 2026, en CM2 à la rentrée 2027"
  },
  "emc2024": {
   "discipline": "Enseignement moral et civique, cycles 2 et 3",
   "texte": "Programme d'EMC — BO n° 24 du 13 juin 2024",
   "nor": "",
   "lien": "https://pia.ac-paris.fr/portail/jcms/p1_3697458/bo-n-24-du-13-juin-2024-programme-d-emc",
   "vigueur": "en vigueur depuis la rentrée 2024"
  }
 },
 "programmesVerifies": "2026-10-01"
};
