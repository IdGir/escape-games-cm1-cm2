# -*- coding: utf-8 -*-
"""Phrases des fiches (leçons) de la version immersive de « Mission géographique » (Année A).
Utilisées mot pour mot : (1) dans assets/data/lecons.json (gen_escales.py), (2) dans les justifications des grades Géographe et
Chef de mission (vingt-mille-lieues/outils/immersif/grades/mission_geo_s*.py). Ne modifier une phrase qu'ici.
Programme : histoire-géographie, cycle 3 (BO n° 22 du 28 mai 2026), « L'organisation du territoire français » (période 1).
Sources : Insee (populations de référence 2026, enquête Emploi 2024) ; DGCL, « Les structures territoriales au 1er janvier 2026 »
(34 875 communes) ; ministère de l'Agriculture, CEP, « La population paysanne, repères historiques » (2016, recensement de 1911) ;
Office de tourisme de la station des Rousses (La Dôle, 1 677 m) ; banatic.interieur.gouv.fr (Clamecy).
Période 2 (séances 6 à 8) : Insee (Étretat : 1 102 habitants, population municipale en vigueur au 1er janvier 2026 ; 1 469 en 2011 ; 4,07 km²) ;
Francetvinfo (août 2022) et presse 2023-2025 (plus d'un million de visiteurs par an à Étretat) ; office de tourisme Le Havre Étretat (Clos Lupin,
château des Aygues, marché couvert, parc des Roches) ; PNUD, Rapport sur le développement humain 2025 (données 2023) ; OIT et UNICEF,
« Travail des enfants : estimations mondiales 2024 » (juin 2025) ; World Inequality Lab, Rapport sur les inégalités mondiales 2022 ;
Convention internationale des droits de l'enfant (ONU, 1989, article 32).
Périodes 3 et 4 (séances 9 à 13) : livret « Mission géographique » (Année A) ; Sandre (Loire : 1 005,93 km) ; Chambre départementale des géomètres-experts de la
Haute-Savoie (mont Blanc : 4 807,47 m, mesure de septembre 2026) ; FAO, SOFI 2025 (sous-alimentation) ; voir A-VERIFIER.md, points 20 à 27."""

# ---------------------------------------------------------------- Séance 1 : la commune
C_COMMUNE = "La commune est le plus petit territoire administratif de France : au 1er janvier 2026, on en compte 34 875."
C_MAIRE = "Chaque commune est dirigée par un maire, élu par le conseil municipal, lui-même élu par les habitants."
C_ROLE = "La commune s'occupe des écoles maternelles et élémentaires, de l'eau, des déchets, des rues et des constructions."
C_FONCTION = "Dans une commune, chaque lieu a une fonction : administrative, éducative, commerciale, de santé ou de loisirs."
C_MAIRIE = "La mairie a une fonction administrative : on y demande des papiers officiels."
C_SERVICE = "Un service public rend un service à tous les habitants : la mairie, l'école publique et la bibliothèque municipale en sont des exemples."
C_VILLE = "On parle souvent de village pour une commune de moins de 2 000 habitants, et de ville au-delà."
C_PLAN = "Un plan représente, vu du dessus, un espace réduit comme une ville ou un quartier."
LECON_COMMUNE = [("Le premier territoire où je vis", [C_COMMUNE, C_MAIRE, C_ROLE]),
                 ("Les lieux de la commune", [C_FONCTION, C_MAIRIE, C_SERVICE]),
                 ("Village ou ville ?", [C_VILLE, C_PLAN])]

# ---------------------------------------------------------------- Séance 2 : les territoires emboîtés
E_EMBOITE = "Les territoires sont emboîtés, du plus petit au plus grand : commune, département, région, pays, continent."
E_NOMBRES = "La France métropolitaine compte 13 régions et 96 départements ; avec l'outre-mer, on compte 18 régions et 101 départements."
E_NUMERO = "Chaque département porte un numéro : 01 pour l'Ain, 21 pour la Côte-d'Or, 75 pour Paris."
E_ECOLES = "La commune s'occupe des écoles, le département des collèges et la région des lycées."
E_REGION = "La région organise aussi les trains régionaux, les TER."
E_DEPT = "Le département s'occupe de l'aide sociale et des routes départementales."
E_DIJON = "Dijon est la préfecture de la Côte-d'Or et le chef-lieu de la région Bourgogne-Franche-Comté."
E_CONTINENTS = "On compte habituellement sept continents : l'Europe, l'Asie, l'Afrique, l'Amérique du Nord, l'Amérique du Sud, l'Océanie et l'Antarctique."
E_FRANCE = "La France est un pays d'Europe : sa capitale est Paris, sa monnaie l'euro, son hymne La Marseillaise et sa devise « Liberté, Égalité, Fraternité »."
E_CHIFFRES = "La France métropolitaine mesure environ 552 000 km² ; la France compte environ 69 millions d'habitants."
LECON_EMBOITE = [("Des territoires emboîtés", [E_EMBOITE, E_NOMBRES, E_NUMERO]),
                 ("Qui décide ?", [E_ECOLES, E_REGION, E_DEPT]),
                 ("La France dans le monde", [E_FRANCE, E_CHIFFRES, E_CONTINENTS, E_DIJON])]

# ---------------------------------------------------------------- Séance 3 : l'espace rural et la densité
R_RURAL = "Un espace rural est un espace où la densité de population est faible et où les champs, les prairies et les forêts occupent beaucoup de place."
R_AGRI = "L'espace rural est marqué par les activités agricoles."
R_DENSITE = "La densité de population est le nombre d'habitants par kilomètre carré : on divise le nombre d'habitants par la superficie en km²."
R_ECARTS = "Dans les grandes villes, la densité dépasse souvent 1 000 habitants par km² ; dans certains villages de montagne, elle est inférieure à 10."
R_VILLAGE = "Une commune rurale de moins de 2 000 habitants est un village ; une commune rurale plus grande, avec des commerces et des services utiles aux villages voisins, est un bourg."
R_AVANTAGES = "Vivre à la campagne offre des avantages : la nature, le calme, des logements plus grands et moins chers."
R_INCONV = "Vivre à la campagne a aussi des inconvénients : peu de commerces, de services et d'emplois, peu de transports en commun et une voiture souvent indispensable."
R_CLAMECY = "Clamecy est un bourg de la Nièvre, entouré de campagne, au bord de l'Yonne et du canal du Nivernais."
LECON_RURAL = [("L'espace rural", [R_RURAL, R_AGRI, R_VILLAGE, R_CLAMECY]),
               ("Calculer une densité", [R_DENSITE, R_ECARTS]),
               ("Vivre à la campagne", [R_AVANTAGES, R_INCONV])]

# ---------------------------------------------------------------- Séance 4 : la ville et les secteurs d'activité
V_VILLE = "Une ville est un espace où la densité de population est forte, avec beaucoup de logements, de commerces, de services et d'emplois."
V_ESPACES = "En ville, on distingue le centre-ville, les quartiers d'affaires, les grands équipements comme l'hôpital et, en périphérie, les centres commerciaux."
V_PRIMAIRE = "Le secteur primaire exploite directement les ressources de la nature : agriculteur, pêcheur, bûcheron."
V_SECONDAIRE = "Le secteur secondaire transforme les matières premières : ouvrier, soudeur, boulanger, maçon."
V_TERTIAIRE = "Le secteur tertiaire rend des services : infirmier, caissier, enseignant, guide, serveur."
V_1911 = "En 1911, près de 40 % des actifs travaillaient dans l'agriculture."
V_2024 = "En 2024, plus de 3 emplois sur 4 sont dans le secteur tertiaire (76,6 %), environ 1 sur 5 dans le secondaire et un peu plus de 2 sur 100 dans le primaire."
V_BESANCON = "Besançon est la préfecture du Doubs ; sa vieille ville est entourée par une boucle de la rivière."
LECON_VILLE = [("La ville et ses espaces", [V_VILLE, V_ESPACES, V_BESANCON]),
               ("Trois secteurs d'activité", [V_PRIMAIRE, V_SECONDAIRE, V_TERTIAIRE]),
               ("Un siècle de changements", [V_1911, V_2024])]

# ---------------------------------------------------------------- Séance 5 : la montagne et le tourisme
M_LOISIRS = "La montagne est un espace de loisirs, été comme hiver : ski, snowboard et raquette, mais aussi randonnée, escalade, parapente ou rafting."
M_STATION = "Une station de montagne est aménagée pour accueillir les touristes : remontées mécaniques, pistes, hébergements, commerces et parkings."
M_PISTES = "Les pistes de ski sont classées par couleur, de la plus facile à la plus difficile : verte, bleue, rouge, noire."
M_AIR = "Les embouteillages à l'entrée des stations polluent l'air."
M_EAU = "Les canons à neige prélèvent beaucoup d'eau, et les remontées mécaniques consomment de l'énergie."
M_BIO = "Les constructions sur les forêts et le dérangement des animaux réduisent la biodiversité ; les déchets abandonnés polluent les sols."
M_EMPLOIS = "Le tourisme apporte aussi des emplois et des revenus, et il aide les villages de montagne à rester habités toute l'année."
M_ROUSSES = "La station des Rousses, dans le Haut-Jura, est reliée au domaine de la Dôle, un sommet suisse de 1 677 mètres."
M_HEMI = "Les saisons sont inversées entre les deux hémisphères : quand c'est l'hiver en France, c'est l'été dans l'hémisphère sud."
LECON_MONTAGNE = [("Un espace de loisirs", [M_LOISIRS, M_STATION, M_PISTES, M_ROUSSES]),
                  ("Le prix du tourisme", [M_AIR, M_EAU, M_BIO, M_EMPLOIS]),
                  ("Pour aller plus loin : les saisons", [M_HEMI])]

# ---------------------------------------------------------------- Séance 6 : Étretat, la station balnéaire
B_DEF = "Une station balnéaire est un lieu de séjour situé en bord de mer, aménagé pour accueillir des touristes."
B_ETRETAT = "Étretat, en Normandie, est célèbre pour ses falaises de craie et son Aiguille ; la ville s'est développée au XIXᵉ siècle avec la mode des bains de mer."
B_ACTIVITES = "On y propose des activités variées : randonnée sur le sentier GR21, kayak ou paddle au pied des falaises, visite du Clos Lupin, maison de l'écrivain Maurice Leblanc, ou du château des Aygues."
B_POSITIFS = "Le tourisme crée des emplois dans les hôtels, les restaurants et les commerces ; il apporte aussi des animations et de nouveaux aménagements."
B_NEGATIFS = "Il provoque aussi des embouteillages, des déchets et une hausse du prix des logements, qui pousse des habitants à partir."
B_CHIFFRES = "Étretat compte environ 1 100 habitants mais reçoit plus d'un million de visiteurs par an."
B_DEPARTS = "Entre 2011 et 2023, Étretat est passée de 1 469 à 1 102 habitants."
B_SURFREQ = "Quand il y a trop de visiteurs pour un lieu, on parle de surfréquentation : la commune cherche alors à mieux répartir les visites."
LECON_BALNEAIRE = [("La station balnéaire", [B_DEF, B_ETRETAT, B_ACTIVITES]),
                   ("Ce que le tourisme apporte et ce qu'il coûte", [B_POSITIFS, B_NEGATIFS]),
                   ("Trop de visiteurs ?", [B_CHIFFRES, B_DEPARTS, B_SURFREQ])]

# ---------------------------------------------------------------- Séance 7 : le littoral, les mers et les océans
O_QUATRE = "La France métropolitaine est bordée par quatre grandes étendues d'eau : la mer du Nord, la Manche, l'océan Atlantique et la mer Méditerranée."
O_NORD = "La mer du Nord borde le nord de la France, vers la Belgique."
O_MANCHE = "La Manche sépare la France du Royaume-Uni ; on s'y baigne en Normandie."
O_ATLANTIQUE = "L'océan Atlantique borde l'ouest de la France ; en le traversant, on arrive en Amérique."
O_MEDITERRANEE = "La mer Méditerranée borde le sud de la France ; on s'y baigne à Marseille, et la Corse en est entourée."
O_LITTORAL = "Le littoral est la zone de contact entre la terre et la mer."
O_BIARRITZ = "Biarritz est une station balnéaire du Pays basque, dans les Pyrénées-Atlantiques, sur le littoral atlantique."
O_HEBERG = "Pour se loger en vacances, on peut choisir un hôtel, un camping, un gîte, une chambre d'hôtes, un village de vacances, une location ou une auberge de jeunesse."
O_ETE = "L'été, la population d'une commune du littoral peut être multipliée par dix ou plus : les touristes s'ajoutent aux habitants, sur la même surface."
O_CALCUL = "Étretat mesure environ 4 km² pour environ 1 100 habitants : sa densité est d'environ 275 habitants par km² ; avec 15 000 visiteurs de plus, elle passerait à 4 025, environ 15 fois plus."
LECON_LITTORAL = [("Les mers et l'océan qui bordent la France", [O_QUATRE, O_NORD, O_MANCHE, O_ATLANTIQUE, O_MEDITERRANEE]),
                  ("Le littoral touristique", [O_LITTORAL, O_BIARRITZ, O_HEBERG]),
                  ("Une population qui change avec les saisons", [O_ETE, O_CALCUL])]

# ---------------------------------------------------------------- Séance 8 : les inégalités de niveau de vie dans le monde
I_NIVEAU = "Le niveau de vie n'est pas le même partout dans le monde."
I_INDICATEURS = "Pour comparer les pays, on utilise plusieurs indicateurs : le revenu par habitant, l'espérance de vie et la durée de la scolarisation."
I_RICHES = "Les pays les plus riches se trouvent surtout en Amérique du Nord, en Europe, en Océanie et en Asie de l'Est, comme le Japon."
I_PAUVRES = "Les pays les plus pauvres se trouvent surtout en Afrique et dans certaines régions d'Asie du Sud."
I_ECART = "En 2023, selon le PNUD, le revenu moyen d'un habitant de la Norvège était plus de 13 fois plus élevé que celui d'un habitant du Bangladesh."
I_SEULE = "La richesse ne suffit pas à mesurer le développement : le Bangladesh a un revenu par habitant plus faible que la Guinée équatoriale, mais une espérance de vie plus longue."
I_PARTAGE = "Les richesses sont très mal partagées : les 10 % les plus riches de la population mondiale possèdent environ les trois quarts du patrimoine."
I_ENFANTS = "Pour les enfants, la pauvreté a des conséquences graves : travail au lieu de l'école, malnutrition, problèmes de santé."
I_OIT = "En 2024, près de 138 millions d'enfants travaillaient dans le monde, selon l'OIT et l'UNICEF."
I_DROITS = "La Convention internationale des droits de l'enfant, adoptée par l'ONU en 1989, protège les enfants contre le travail qui nuit à leur santé ou à leur éducation."
LECON_INEGALITES = [("Des niveaux de vie très différents", [I_NIVEAU, I_INDICATEURS, I_ECART, I_SEULE]),
                    ("Où sont les pays riches et les pays pauvres ?", [I_RICHES, I_PAUVRES, I_PARTAGE]),
                    ("La pauvreté et les enfants", [I_ENFANTS, I_OIT, I_DROITS])]

# ---------------------------------------------------------------- Séance 9 : les pratiques alimentaires
P_PRATIQUES = "Les pratiques alimentaires, c'est-à-dire la manière de se nourrir, dépendent du climat, des cultures locales, des habitudes et surtout des revenus."
P_MALI = "Au Mali, on mange surtout ce qui est produit sur place : le millet, le riz, les arachides, les haricots, le gombo et la mangue."
P_ENCLAVE = "Le Mali est un pays enclavé, sans accès à la mer : le poisson de mer y est rare et cher."
P_CLIMAT = "Le climat est chaud et sec une grande partie de l'année et la saison des pluies est courte : les cultures y sont peu variées."
P_IMPORT = "Les aliments importés, comme les pâtes, le fromage ou le yaourt, coûtent très cher au Mali : un kilo de pâtes importées vaut environ cinq fois le prix d'un kilo de millet."
P_FRIGO = "Peu de familles maliennes possèdent un réfrigérateur, ce qui limite la conservation de la viande et du poisson."
P_BUDGET = "En France, un budget de 25 € permet d'acheter une grande variété d'aliments ; au Mali, une famille dispose souvent de moins de 10 € pour la même semaine."
P_SOUS = "La sous-alimentation, c'est le fait de ne pas manger assez pour couvrir ses besoins."
P_ZONES = "Elle touche surtout l'Afrique subsaharienne, comme le Tchad, le Soudan et Madagascar, et certains pays comme Haïti."
P_FRANCE = "En France et aux États-Unis, elle concerne moins de 2,5 % de la population."
LECON_ALIM = [("Se nourrir ici et ailleurs", [P_PRATIQUES, P_MALI, P_ENCLAVE, P_CLIMAT, P_IMPORT, P_FRIGO, P_BUDGET]),
              ("La sous-alimentation", [P_SOUS, P_ZONES, P_FRANCE])]

# ---------------------------------------------------------------- Séance 10 : produits agricoles et produits transformés
A_AGRI = "Un produit agricole vient directement de la nature : il est cultivé ou élevé, puis consommé presque tel quel, comme une pomme, une carotte, un œuf ou du lait."
A_TRANS = "Un produit transformé est fabriqué à partir d'un ou de plusieurs produits agricoles, dans un atelier ou une usine."
A_EX = "Le pain vient du blé, le fromage et le yaourt du lait, le jus du raisin, la sauce de la tomate, le sucre de la canne à sucre ou de la betterave, et le chocolat du cacao."
A_ESPACE = "Chaque aliment vient d'un espace de production et d'un métier."
A_ELEV = "L'éleveur travaille dans un élevage : il produit les volailles, les œufs, le lait et la viande."
A_CEREAL = "Le céréalier cultive des céréales, comme le blé et le maïs, dans des champs."
A_MARAIC = "Le maraîcher cultive des légumes, comme les carottes, les salades et les haricots, dans une exploitation maraîchère."
A_ARBO = "L'arboriculteur s'occupe d'un verger : il produit des fruits, comme les pommes, les poires et les cerises."
LECON_PRODUITS = [("Agricole ou transformé ?", [A_AGRI, A_TRANS, A_EX]),
                  ("Espaces de production et métiers", [A_ESPACE, A_ELEV, A_CEREAL, A_MARAIC, A_ARBO])]

# ---------------------------------------------------------------- Séance 11 : la chaîne de production du yaourt
Y_CHAINE = "La chaîne de production d'un aliment décrit toutes les étapes qui séparent la matière première de l'assiette du consommateur."
Y_FERME = "À la ferme, les vaches sont traites chaque jour : le lait est immédiatement refroidi et stocké dans un tank réfrigéré."
Y_TRANSPORT = "Un camion-citerne réfrigéré collecte le lait et l'apporte à l'usine."
Y_USINE = "À l'usine, le lait est analysé, puis stocké dans de grands réservoirs ; il est chauffé, des ferments sont ajoutés et le mélange repose : le yaourt fermente et s'épaissit."
Y_POTS = "Le yaourt est ensuite versé dans des pots, fermés par un couvercle, puis rangés sur des palettes."
Y_DISTRI = "Des camions frigorifiques livrent les supermarchés, où le yaourt est vendu au rayon frais."
Y_FROID = "La chaîne du froid ne doit jamais être interrompue : sans réfrigération, des microbes se développent dans le lait, qui tourne et devient impropre à la consommation."
Y_SECTEUR = "Une usine qui transforme une matière première, comme le lait, fait partie du secteur secondaire, alors que la ferme relève du secteur primaire et le supermarché du secteur tertiaire."
LECON_YAOURT = [("Du lait au yaourt", [Y_CHAINE, Y_FERME, Y_TRANSPORT, Y_USINE, Y_POTS, Y_DISTRI]),
                ("Le froid et les secteurs d'activité", [Y_FROID, Y_SECTEUR])]

# ---------------------------------------------------------------- Séance 12 : les kilomètres alimentaires
K_KM = "Les kilomètres alimentaires sont la distance totale parcourue par un aliment avant d'arriver dans notre assiette."
K_CO2 = "Plus cette distance est grande, plus le transport rejette de CO₂ dans l'atmosphère, ce qui dégrade l'air et contribue au réchauffement climatique."
K_ORIGINES = ("Dans un supermarché français, les étiquettes révèlent des origines très variées : fraises d'Espagne, bananes du Cameroun, noisettes de Turquie, oranges d'Afrique du Sud, "
              "citrons d'Argentine, feta de Grèce, poires du Chili, myrtilles du Portugal, kiwis de Nouvelle-Zélande et mangues du Brésil.")
K_CIRCUIT = "Pour réduire ces kilomètres, on peut acheter en circuit court, directement au producteur."
K_LOCAL = "On peut aussi privilégier les produits locaux, choisir des fruits et des légumes de saison et manger moins de viande."
K_SANS = "Manger moins salé ou ne pas laver ses fruits n'a aucun effet sur les kilomètres alimentaires."
LECON_KM = [("Les kilomètres alimentaires", [K_KM, K_CO2, K_ORIGINES]),
            ("Consommer autrement", [K_CIRCUIT, K_LOCAL, K_SANS])]

# ---------------------------------------------------------------- Séance 13 : fleuves et massifs montagneux
F_FLEUVE = "Un fleuve est un cours d'eau qui se jette dans la mer ou dans l'océan ; une rivière se jette dans un autre cours d'eau."
F_CINQ = "Les cinq principaux fleuves français sont la Seine, la Loire, la Garonne, le Rhône et le Rhin."
F_SEINE = "La Seine traverse Paris et se jette dans la Manche, près du Havre."
F_LOIRE = "La Loire est le plus long fleuve de France, avec environ 1 006 km ; elle se jette dans l'océan Atlantique."
F_GARONNE = "La Garonne descend des Pyrénées et se jette dans l'océan Atlantique par l'estuaire de la Gironde."
F_RHONE = "Le Rhône vient de Suisse et se jette dans la mer Méditerranée."
F_RHIN = "Le Rhin longe la frontière avec l'Allemagne et se jette dans la mer du Nord."
F_SIX = "Les six grands massifs montagneux sont les Alpes, les Pyrénées, le Massif central, le Jura, les Vosges et les montagnes de Corse."
F_ALPES = "Les Alpes sont les plus hautes montagnes de France : le mont Blanc culmine à environ 4 807 mètres."
F_PYRENEES = "Les Pyrénées forment la frontière avec l'Espagne."
F_JURA = "Le Jura longe la frontière avec la Suisse, et les Vosges se trouvent à l'est, avec des sommets arrondis."
F_VOLCANS = "Le Massif central, au centre du pays, est formé d'anciens volcans."
F_NEIGE = "Les montagnes retiennent la neige : en fondant au printemps, elle alimente les fleuves."
LECON_FLEUVES = [("Fleuves et rivières", [F_FLEUVE, F_CINQ, F_SEINE, F_LOIRE, F_GARONNE, F_RHONE, F_RHIN]),
                 ("Les grands massifs montagneux", [F_SIX, F_ALPES, F_PYRENEES, F_JURA, F_VOLCANS, F_NEIGE])]


def html(sections):
    """Texte CM2 d'une fiche : un titre et un paragraphe par section, phrases reprises telles quelles."""
    return "".join(f"<h4>{t}</h4><p>{' '.join(ph)}</p>" for t, ph in sections)
