# -*- coding: utf-8 -*-
"""Phrases des fiches (leçons CM2) du jeu « L'Expédition biodiversité ».
Utilisées mot pour mot : (1) dans lecons.json (gen_lecons.py), (2) dans les justifications des grades Écologue et Conservateur
(vingt-mille-lieues/outils/immersif/grades/vivant_ecosystemes_s*.py). Ne modifier une phrase qu'ici.
Programme : BO n° 24 du 11 juin 2026, annexe 2 (sciences et technologie, cycle 3). Vocabulaire du programme : « milieu de vie » et
« êtres vivants » (pas biotope ni biocénose) ; « réseau alimentaire », flèches de la proie vers le prédateur ; la cellule et la
décomposition relèvent de la 6e (sections « Pour aller plus loin »).
Sources : MNHN et INPN ; La main à la pâte ; Espace des sciences (Rennes) ; académie de Martinique, « Marche des temps géologiques » ;
Centre de ressources Espèces exotiques envahissantes (OFB-UICN) ; MNHN, inventaire du frelon asiatique (Villemant et al., 2011)."""

# ---------------------------------------------------------------- Leçon 1 : observer le vivant, l'espèce
A_OBSERVER = "Pour décrire un être vivant, on observe ses attributs : ce qu'il possède, comme des plumes, des poils, une coquille, des pattes ou des ailes."
A_COMPTER = "On compte et on décrit avec précision : six pattes, huit pattes, quatre ailes, une coquille enroulée."
A_PAS_FAIT = "Un attribut est une chose que l'on voit sur l'être vivant ; ce qu'il mange ou l'endroit où il vit ne sont pas des attributs."
A_ESPECE = "Une espèce est un ensemble d'êtres vivants qui se ressemblent et qui peuvent se reproduire entre eux : leurs petits pourront à leur tour avoir des petits."
A_RACES = "Un caniche et un berger allemand sont très différents, mais ils appartiennent à la même espèce : le chien."
A_MULET = "Un âne et une jument peuvent avoir un petit, le mulet, mais le mulet ne peut pas avoir de petits : l'âne et le cheval sont deux espèces différentes."
A_NOM = "Chaque espèce porte un nom scientifique en deux mots, le même dans tous les pays : le héron cendré s'appelle Ardea cinerea."
A_INVENTAIRE = "Faire l'inventaire d'un lieu, c'est noter toutes les espèces que l'on y trouve : c'est ainsi que l'on mesure sa biodiversité."
A_CELLULE = "Tous les êtres vivants sont faits de cellules : la cellule est l'unité commune à tout le vivant."
A_PARTIES = "Une cellule est entourée d'une membrane, contient du cytoplasme et, le plus souvent, un noyau ; les cellules des plantes ont en plus une paroi."
A_UNI = "Certains êtres vivants ne sont faits que d'une seule cellule, comme la paramécie de la mare ou la levure : on ne les voit qu'au microscope."
A_ORGANES = "Chez un animal ou une plante, des milliards de cellules forment des organes, comme le cœur, les feuilles ou les racines."
LECON_ESPECE = [("Observer", [A_OBSERVER, A_COMPTER, A_PAS_FAIT]),
                ("L'espèce", [A_ESPECE, A_RACES, A_MULET, A_NOM, A_INVENTAIRE]),
                ("Pour aller plus loin (6e) : la cellule", [A_CELLULE, A_PARTIES, A_UNI, A_ORGANES])]

# ---------------------------------------------------------------- Leçon 2 : classer le vivant
C_CLASSER = "Classer, c'est ranger les êtres vivants dans des groupes selon les attributs qu'ils possèdent en commun."
C_EMBOITE = "Les groupes sont emboîtés comme des boîtes rangées les unes dans les autres : le groupe des animaux à poils est rangé dans le groupe des animaux à squelette interne."
C_PAS_ABSENCE = "On ne fait jamais un groupe avec ce qu'un être vivant ne possède pas : « les animaux sans pattes » n'est pas un groupe de classification."
C_PAS_MILIEU = "Le lieu de vie et la nourriture ne servent pas à classer : le dauphin vit dans la mer, mais il respire avec des poumons et allaite ses petits : il est rangé avec la vache et le renard, pas avec les poissons."
C_PARENTE = "Deux espèces qui partagent beaucoup d'attributs sont proches parentes : le renard est plus proche du loup que du hérisson."
C_CLE = "Une clé de détermination sert à identifier un être vivant : on répond à une suite de questions simples jusqu'à trouver son nom."
C_CLE_PAS = "Identifier n'est pas classer : la clé donne le nom d'une espèce, la classification montre ses liens de parenté avec les autres."
C_PATTES = "Les insectes ont six pattes, les araignées huit pattes, le cloporte quatorze pattes, et les mille-pattes de très nombreuses paires de pattes."
C_APPLI = "Une application d'identification par intelligence artificielle propose un nom à partir d'une photo, mais elle peut se tromper : on vérifie avec une clé."
C_ARBRE = "Un arbre de parenté relie les espèces : plus deux espèces se sont séparées tard d'un ancêtre commun, plus elles sont proches parentes."
C_ANCETRE = "Un ancêtre commun est une espèce disparue dont descendent plusieurs espèces actuelles."
LECON_CLASSER = [("Classer", [C_CLASSER, C_EMBOITE, C_PAS_ABSENCE, C_PAS_MILIEU, C_PARENTE]),
                 ("Identifier", [C_CLE, C_PATTES, C_APPLI, C_CLE_PAS]),
                 ("Pour aller plus loin (6e) : l'arbre de parenté", [C_ARBRE, C_ANCETRE])]

# ---------------------------------------------------------------- Leçon 3 : la biodiversité passée
P_FOSSILE = "Un fossile est un reste ou une trace d'un être vivant ancien, conservé dans une roche : une coquille, un os, une dent, une empreinte de feuille."
P_ROCHE = "La plupart des fossiles se forment au fond de l'eau : l'être vivant mort est vite recouvert de sable ou de boue qui deviennent de la roche."
P_TERRE = "La Terre s'est formée il y a environ 4,6 milliards d'années ; les premières traces de vie datent d'environ 3,8 milliards d'années."
P_TRILO = "Les trilobites, des animaux marins à carapace, vivaient il y a 540 millions d'années ; ils ont disparu il y a 252 millions d'années."
P_DINOS = "Les dinosaures ont vécu pendant plus de 150 millions d'années, puis ont disparu il y a environ 66 millions d'années, avec les ammonites."
P_SAPIENS = "Notre espèce, Homo sapiens, est apparue en Afrique il y a environ 300 000 ans : aucun humain n'a jamais vu de dinosaure vivant."
P_ECHELLE = "Le temps géologique se compte en millions et en milliards d'années, alors que l'histoire des humains se compte en siècles et en milliers d'années."
P_CRISE = "Il y a 66 millions d'années, une crise a fait disparaître un très grand nombre d'espèces : c'est une extinction massive."
P_CAUSES = "Les scientifiques en cherchent les causes : la chute d'une météorite géante au Mexique et d'énormes éruptions volcaniques en Inde."
P_REMPLACE = "Après cette crise, de nouvelles espèces sont apparues rapidement, en particulier chez les mammifères, qui se sont diversifiés."
P_OISEAUX = "Les oiseaux descendent de petits dinosaures à plumes : ce sont les seuls dinosaures qui n'ont pas disparu."
P_CHANGE = "Les fossiles montrent que la biodiversité change au cours du temps : des espèces apparaissent, d'autres disparaissent."
LECON_FOSSILES = [("Les fossiles", [P_FOSSILE, P_ROCHE, P_CHANGE]),
                  ("Une très longue histoire", [P_ECHELLE, P_TERRE, P_TRILO, P_DINOS, P_SAPIENS]),
                  ("Une extinction massive", [P_CRISE, P_CAUSES, P_REMPLACE, P_OISEAUX])]

# ---------------------------------------------------------------- Leçon 4 : l'écosystème
E_DEF = "Un écosystème, c'est un milieu de vie, les êtres vivants qui l'habitent, et toutes les relations entre eux."
E_MILIEU = "Le milieu de vie se décrit par ses caractéristiques physiques : la température, la lumière, l'humidité, la quantité de pluie, l'altitude."
E_PRESENCE = "Les êtres vivants d'un lieu dépendent de son milieu : les nénuphars ont besoin d'une eau calme et ensoleillée, les mousses d'un endroit humide et ombragé."
E_GRENOUILLE = "La grenouille a besoin de la mare pour pondre ses œufs dans l'eau, et de la prairie voisine pour chasser les insectes."
E_PREDATION = "La prédation est la relation entre un prédateur et sa proie : le héron cendré attrape les grenouilles et les poissons de la mare."
E_COOPERATION = "La coopération est une relation où chacun gagne : l'abeille boit le nectar de la fleur et, en échange, transporte son pollen vers une autre fleur."
E_EXEMPLES = "Une mare, une forêt, une prairie ou une vigne de Bourgogne sont des écosystèmes."
E_CHANGE = "Un écosystème change au fil des saisons et peut se rétablir après une perturbation, mais seulement dans certaines limites."
E_AQUA = "Dans un écosystème aquatique, comme la mare, les êtres vivants respirent l'oxygène dissous dans l'eau ou remontent à la surface."
E_SAISON = "À la mauvaise saison, beaucoup d'êtres vivants ralentissent : la grenouille s'enfouit dans la vase, l'arbre perd ses feuilles, la graine attend le printemps."
LECON_ECO = [("Un milieu et des êtres vivants", [E_DEF, E_MILIEU, E_PRESENCE, E_GRENOUILLE, E_EXEMPLES]),
             ("Des relations", [E_PREDATION, E_COOPERATION]),
             ("Un écosystème qui change", [E_CHANGE, E_SAISON, E_AQUA])]

# ---------------------------------------------------------------- Leçon 5 : le réseau alimentaire
R_MANGER = "Pour grandir et produire leur propre matière, les animaux mangent d'autres êtres vivants, plantes ou animaux."
R_FLECHE = "On représente « est mangé par » par une flèche qui va de la proie vers celui qui la mange."
R_RESEAU = "Les chaînes de « est mangé par » se croisent : elles forment un réseau alimentaire."
R_PLANTE = "Au départ de chaque chaîne, on trouve une plante ou une algue : les végétaux fabriquent leur propre matière grâce à la lumière."
R_EXEMPLE = "Dans l'étang, les algues sont mangées par les têtards, les têtards par les larves de libellule, les larves par les perches et les perches par le héron."
R_VARIATION = "Si le nombre d'individus d'une espèce change beaucoup, tout le réseau est touché."
R_SURPECHE = "Si l'on pêche trop de perches, les larves de libellule ne sont plus assez mangées et deviennent trop nombreuses, alors le héron manque de poissons."
R_INVASIVE = "L'écrevisse de Louisiane, venue d'Amérique et introduite en France en 1976, détruit les plantes de l'eau et mange les petits animaux de la mare."
R_FRELON = "Le frelon asiatique, observé en France depuis 2004, chasse surtout les abeilles près des ruches."
R_PROTEGER = "Les humains peuvent aussi protéger les écosystèmes : creuser une mare, laisser des haies, éviter les pesticides, ne jamais relâcher un animal exotique dans la nature."
R_DECOMPOSE = "Les feuilles mortes, les cadavres et les excréments sont décomposés par des champignons, des vers et des êtres vivants microscopiques : leur matière retourne au sol."
LECON_RESEAU = [("Qui mange qui ?", [R_MANGER, R_FLECHE, R_RESEAU, R_EXEMPLE, R_PLANTE]),
                ("Quand une espèce change", [R_VARIATION, R_SURPECHE, R_INVASIVE, R_FRELON, R_PROTEGER]),
                ("Pour aller plus loin (6e) : la décomposition", [R_DECOMPOSE])]


def html(sections):
    return "".join(f"<h4>{h}</h4><p>{' '.join(ps)}</p>" for h, ps in sections)
