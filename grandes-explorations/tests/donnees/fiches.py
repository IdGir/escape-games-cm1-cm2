# -*- coding: utf-8 -*-
"""Phrases des fiches (leçons CM2) du jeu « La Caravelle du capitaine ».
Utilisées mot pour mot : (1) dans lecons.json (gen_lecons.py), (2) dans les justifications des grades lieutenant et second
(vingt-mille-lieues/outils/immersif/grades/grandes_explorations_s*.py). Ne modifier une phrase qu'ici."""

# ---------------------------------------------------------------- Leçon 1 : pourquoi partir ?
E_MONDE = "Vers 1450, les Européens connaissent l'Europe, le nord de l'Afrique et une partie de l'Asie ; ils ignorent l'existence des Amériques."
E_RONDE = "Les savants de cette époque savent déjà que la Terre est ronde, mais ils pensent qu'elle est plus petite qu'elle ne l'est."
E_EPICES = "Le poivre, la cannelle, le clou de girofle ou la muscade viennent d'Asie : ils servent à parfumer et à conserver les aliments, et se vendent très cher."
E_INTERM = "Ces épices arrivent en Europe après un long voyage par terre et par mer, en passant par de nombreux marchands qui augmentent leur prix."
E_1453 = "En 1453, les Turcs ottomans prennent Constantinople : ils contrôlent désormais une partie des routes vers l'Asie."
E_MER = "Les Européens cherchent donc une route par la mer pour aller directement chercher les épices en Asie."
E_OR = "Les rois et les marchands espèrent aussi trouver de l'or, de l'argent et de nouvelles terres."
E_FOI = "Les rois catholiques veulent répandre la religion chrétienne."
E_GLOIRE = "Les marins espèrent la gloire, des récompenses et des titres ; les savants veulent mieux connaître le monde."
E_PORTU = "Le Portugal et l'Espagne, tournés vers l'océan Atlantique, sont les premiers à lancer de grandes expéditions."
E_COTES = "Au XVe siècle, les marins portugais descendent peu à peu le long des côtes d'Afrique, à la recherche d'un passage vers l'Asie."
LECON_EPICES = [("Le monde connu vers 1450", [E_MONDE, E_RONDE]),
                ("Les pays de l'Atlantique en tête", [E_PORTU, E_COTES]),
                ("Les épices, des produits de luxe", [E_EPICES, E_INTERM, E_1453, E_MER]),
                ("D'autres raisons de partir", [E_OR, E_FOI, E_GLOIRE])]

# ---------------------------------------------------------------- Leçon 2 : les progrès techniques
T_CARA = "La caravelle est un navire léger d'une vingtaine de mètres, mis au point par les Portugais au XVe siècle."
T_LATINE = "Ses voiles triangulaires, appelées voiles latines, lui permettent d'avancer même quand le vent ne souffle pas dans son dos."
T_CARREE = "Les voiles carrées, elles, poussent vite le navire quand le vent vient de l'arrière."
T_GOUV = "À l'arrière, le gouvernail d'étambot, fixé dans l'axe du navire, permet de le diriger avec précision."
T_BOUSSOLE = "La boussole, inventée en Chine, indique le nord grâce à son aiguille aimantée : on garde le cap même sans voir les étoiles."
T_ASTRO = "L'astrolabe et le quadrant mesurent la hauteur du Soleil ou de l'étoile Polaire au-dessus de l'horizon."
T_LATI = "Avec cette mesure et des tables de calcul, le pilote trouve sa latitude, c'est-à-dire sa position entre le nord et le sud."
T_CARTE = "Les cartes marines, ou portulans, dessinent les côtes, les ports et les directions à suivre."
T_SABLIER = "Le sablier mesure le temps passé, ce qui aide à estimer la distance parcourue."
T_ARABE = "Beaucoup de ces instruments et de ces savoirs, comme l'astrolabe, ont été transmis aux Européens par les savants du monde arabe."
T_LARGE = "Grâce à eux, les marins osent s'éloigner des côtes et traverser les océans pendant des semaines."
T_EQUIP = "Une caravelle emporte une vingtaine de marins, de l'eau douce, du biscuit et des tonneaux de vivres pour des semaines de navigation."
LECON_TECH = [("Un navire nouveau", [T_CARA, T_LATINE, T_CARREE, T_GOUV]),
              ("Se diriger en pleine mer", [T_BOUSSOLE, T_ASTRO, T_LATI]),
              ("Des cartes et des mesures", [T_CARTE, T_SABLIER, T_EQUIP]),
              ("Des savoirs partagés", [T_ARABE, T_LARGE])]

# ---------------------------------------------------------------- Leçon 3 : les grands voyages
V_COLOMB = "Christophe Colomb, au service des souverains d'Espagne, quitte Palos le 3 août 1492 avec trois navires."
V_COLOMB2 = "Le 12 octobre 1492, il atteint une île des Bahamas ; il croit être arrivé en Asie, aux Indes."
V_GAMA = "Le Portugais Vasco de Gama quitte Lisbonne en juillet 1497, contourne l'Afrique par le cap de Bonne-Espérance et arrive à Calicut, en Inde, le 20 mai 1498."
V_MAG = "En 1519, Fernand de Magellan part d'Espagne avec cinq navires et environ 250 hommes pour atteindre l'Asie par l'ouest."
V_MAG2 = "Magellan est tué aux Philippines en 1521 ; Juan Sebastián Elcano ramène en Espagne le dernier navire, la Victoria, le 6 septembre 1522, avec 18 hommes."
V_TOUR = "C'est le premier tour du monde : il prouve que l'on peut faire le tour de la Terre par la mer."
V_CARTIER = "En 1534, Jacques Cartier, envoyé par le roi de France François Ier, part de Saint-Malo et arrive à Gaspé le 24 juillet ; il y plante une croix."
V_AMERIQUE = "Ces terres étaient habitées depuis des milliers d'années : on parle aujourd'hui de l'arrivée des Européens en Amérique."
V_QUATRE = "Colomb fait en tout quatre voyages vers ces terres."
V_ROUTE = "Vasco de Gama ouvre aux Portugais la route maritime des épices."
V_NOMS = "Les Européens donnent alors des noms nouveaux à des lieux qui en avaient déjà dans les langues de leurs habitants."
LECON_VOYAGES = [("Vers l'ouest : Christophe Colomb", [V_COLOMB, V_COLOMB2, V_QUATRE]),
                 ("Vers l'est : Vasco de Gama", [V_GAMA, V_ROUTE]),
                 ("Autour du monde : Magellan et Elcano", [V_MAG, V_MAG2, V_TOUR]),
                 ("Au nord : Jacques Cartier", [V_CARTIER, V_AMERIQUE, V_NOMS])]

# ---------------------------------------------------------------- Leçon 4 : rencontres et conquêtes
R_PEUPLES = "Vers 1500, des millions de personnes vivent en Amérique, dans des sociétés très différentes les unes des autres."
R_AZTEQUES = "Au Mexique, les Aztèques ont pour capitale Tenochtitlan, une très grande ville bâtie sur un lac."
R_INCAS = "Dans la cordillère des Andes, l'Empire inca, dont la capitale est Cuzco, est relié par un immense réseau de routes."
R_NORD = "Au nord, le long du fleuve Saint-Laurent, des Iroquoiens cultivent le maïs et vivent dans des villages de maisons longues."
R_CORTES = "Le conquistador Hernán Cortés et ses alliés amérindiens prennent Tenochtitlan en 1521."
R_PIZARRO = "En 1532, Francisco Pizarro capture l'empereur inca Atahualpa : c'est le début de la conquête de l'Empire inca."
R_ARMES = "Les conquistadors ont des chevaux, des armes en acier et des armes à feu, inconnus des Amérindiens."
R_MALADIES = "Les Européens apportent sans le savoir des maladies comme la variole, contre lesquelles les Amérindiens ne sont pas protégés : la population s'effondre."
R_ECHANGES = "Les échanges vont dans les deux sens : le maïs, la pomme de terre, la tomate et le cacao arrivent en Europe ; le cheval, le blé et la vache arrivent en Amérique."
R_RESIST = "Certains peuples résistent longtemps aux conquérants, et la conquête dure de nombreuses années."
R_TENO = "Tenochtitlan compte alors des dizaines de milliers d'habitants, avec des temples, des marchés et des canaux, ce qui étonne les Espagnols."
LECON_RENCONTRES = [("Des peuples nombreux", [R_PEUPLES, R_AZTEQUES, R_TENO, R_INCAS, R_NORD]),
                    ("Les conquêtes", [R_CORTES, R_PIZARRO, R_ARMES, R_RESIST]),
                    ("Un choc terrible", [R_MALADIES, R_ECHANGES])]

# ---------------------------------------------------------------- Leçon 5 : les premiers empires coloniaux
C_TORDE = "Le 7 juin 1494, par le traité de Tordesillas, l'Espagne et le Portugal se partagent les terres à découvrir de part et d'autre d'une ligne tracée à 370 lieues à l'ouest des îles du Cap-Vert."
C_PARTAGE = "Les terres à l'ouest de cette ligne reviennent à l'Espagne, celles à l'est au Portugal."
C_BRESIL = "Le Brésil, qui dépasse la ligne vers l'est, devient une colonie portugaise ; le Portugais Cabral y arrive en 1500."
C_ESPAGNE = "L'Espagne construit un immense empire, du Mexique au Pérou, et exploite les mines d'or et surtout d'argent."
C_SUCRE = "Au Brésil, les Portugais créent des plantations de canne à sucre."
C_FRANCE = "La France fonde la Nouvelle-France : Samuel de Champlain fonde Québec en 1608 ; on y fait le commerce des fourrures avec les Amérindiens."
C_ANGLE = "L'Angleterre fonde ses premières colonies sur la côte est de l'Amérique du Nord, comme la Virginie en 1607."
C_TRAITE = "Dans les mines et les plantations, les colons font travailler de force des Amérindiens, puis des Africains réduits en esclavage : c'est le début de la traite atlantique."
C_EMPIRE = "Un empire colonial est l'ensemble des territoires lointains dominés et exploités par un pays."
C_RICHE = "Les richesses venues d'Amérique, surtout l'argent des mines, enrichissent l'Espagne."
C_CONCUR = "Les autres pays d'Europe, comme la France et l'Angleterre, refusent ce partage et envoient à leur tour des expéditions."
LECON_EMPIRES = [("Le partage du monde", [C_TORDE, C_PARTAGE, C_BRESIL, C_CONCUR]),
                 ("Les premiers empires coloniaux", [C_EMPIRE, C_ESPAGNE, C_SUCRE, C_FRANCE, C_ANGLE]),
                 ("Exploiter les colonies", [C_RICHE, C_TRAITE])]


def html(sections):
    return "".join(f"<h4>{h}</h4><p>{' '.join(ps)}</p>" for h, ps in sections)
