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
Convention internationale des droits de l'enfant (ONU, 1989, article 32)."""

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


def html(sections):
    """Texte CM2 d'une fiche : un titre et un paragraphe par section, phrases reprises telles quelles."""
    return "".join(f"<h4>{t}</h4><p>{' '.join(ph)}</p>" for t, ph in sections)
