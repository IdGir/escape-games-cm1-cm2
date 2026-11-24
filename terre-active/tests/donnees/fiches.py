# -*- coding: utf-8 -*-
"""Phrases des fiches (leçons CM2) du jeu « L'Observatoire des volcans ».
Utilisées mot pour mot : (1) dans lecons.json (gen_lecons.py), (2) dans les justifications des grades Volcanologue et Directeur
de l'observatoire (vingt-mille-lieues/outils/immersif/grades/terre_active_s*.py). Ne modifier une phrase qu'ici.
Programme : BO n° 24 du 11 juin 2026, annexe 2, thème « La Terre, une planète active », CM2 « L'activité terrestre » :
repérer des manifestations de l'activité interne ou externe de la Terre ; définir le risque naturel, la prévention et la protection
à partir d'un exemple ; modéliser par une maquette. La structure interne du globe et les plaques ne sont pas nommées par le programme
de cycle 3 : elles servent ici de modèle simple pour comprendre l'activité interne (prolongement : cycle 4).
Sources : Futura-Sciences, « Structure de la Terre » ; culture.gouv.fr (Chaîne des Puys, 2018) ; Espace des sciences, Sciences Ouest n° 416
(montagne Pelée) ; Futura-Sciences (montagne Pelée, 2022 ; Piton de la Fournaise, 2020) ; IPGP (Soufrière 1976, communiqué de 2026) ;
SDES, Chiffres clés des risques naturels (séismes) ; préfectures du Puy-de-Dôme et de la Nièvre, consignes « séisme » ;
ministère de l'Europe et des Affaires étrangères, fiches « Que faire en cas de séisme / d'éruption volcanique »."""

# ---------------------------------------------------------------- Leçon 1 : une planète active
T_ACTIVE = "La Terre est une planète active : sa surface change, parfois lentement, parfois brusquement."
T_INTERNE = "Les volcans et les séismes sont des manifestations de l'activité interne : leur cause se trouve sous nos pieds, à l'intérieur de la Terre."
T_EXTERNE = "Les tempêtes, les inondations et l'érosion des falaises par les vagues sont des manifestations de l'activité externe : elles viennent de l'air et de l'eau, à la surface."
T_TSUNAMI = "Un tsunami est lié à l'activité interne : ces vagues géantes sont souvent provoquées par un séisme sous la mer."
T_COUCHES = "L'intérieur de la Terre est formé de trois grandes enveloppes : la croûte, le manteau et le noyau."
T_CROUTE = "La croûte est l'enveloppe la plus fine : sous les continents, elle mesure en moyenne environ 30 kilomètres d'épaisseur."
T_MANTEAU = "Le manteau, fait de roches très chaudes, descend jusqu'à environ 2 900 kilomètres de profondeur."
T_NOYAU = "Le noyau occupe le centre de la Terre ; le centre se trouve à environ 6 400 kilomètres sous nos pieds."
T_CHALEUR = "Plus on descend, plus il fait chaud : c'est cette chaleur interne qui fait bouger lentement les roches du manteau."
T_PERSONNE = "Personne n'est jamais allé dans le manteau : les scientifiques étudient l'intérieur de la Terre grâce aux ondes des séismes."
LECON_ACTIVE = [("Une planète active", [T_ACTIVE, T_INTERNE, T_EXTERNE, T_TSUNAMI]),
                ("Sous nos pieds", [T_COUCHES, T_CROUTE, T_MANTEAU, T_NOYAU]),
                ("Pour aller plus loin (cycle 4) : la chaleur interne", [T_CHALEUR, T_PERSONNE])]

# ---------------------------------------------------------------- Leçon 2 : les plaques
P_DECOUPE = "La surface de la Terre est découpée en grandes plaques, comme les morceaux d'un puzzle."
P_LENT = "Les plaques bougent très lentement, de quelques centimètres par an : on ne sent pas ce mouvement."
P_FRONTIERE = "La plupart des volcans et des séismes se trouvent près des frontières entre les plaques."
P_ANTILLES = "Les Antilles se trouvent à la frontière entre plusieurs plaques : c'est pourquoi il y a des volcans et des séismes en Guadeloupe et en Martinique."
P_MAQUETTE = "Une maquette est un modèle : elle aide à comprendre un phénomène trop grand ou trop lent pour être observé directement."
P_ECARTENT = "À certaines frontières, les plaques s'écartent : du magma monte et forme une nouvelle croûte au fond de l'océan."
P_RAPPROCHENT = "À d'autres frontières, les plaques se rapprochent : l'une peut s'enfoncer sous l'autre, ce qui provoque des séismes et des volcans."
P_MONTAGNES = "Quand deux plaques se poussent pendant des millions d'années, les roches se plissent et forment des montagnes."
LECON_PLAQUES = [("Un puzzle qui bouge", [P_DECOUPE, P_LENT, P_FRONTIERE, P_ANTILLES]),
                 ("Modéliser", [P_MAQUETTE]),
                 ("Pour aller plus loin (cycle 4) : les frontières de plaques", [P_ECARTENT, P_RAPPROCHENT, P_MONTAGNES])]

# ---------------------------------------------------------------- Leçon 3 : les volcans
V_MAGMA = "Sous un volcan, une roche fondue très chaude, le magma, s'accumule dans une chambre magmatique."
V_MONTE = "Lors d'une éruption, le magma monte par la cheminée et sort par le cratère."
V_PRODUITS = "Un volcan rejette de la lave, des cendres et des gaz ; en refroidissant, la lave devient une roche dure."
V_FOURNAISE = "Le Piton de la Fournaise, à La Réunion, est l'un des volcans les plus actifs du monde ; ses coulées de lave sont surveillées par un observatoire."
V_PELEE = "Le 8 mai 1902, en Martinique, une nuée ardente de la montagne Pelée a détruit la ville de Saint-Pierre : près de 28 000 personnes sont mortes."
V_SOUFRIERE = "En 1976, lors de l'éruption de la Soufrière, en Guadeloupe, des dizaines de milliers d'habitants ont été évacués."
V_PUYS = "La Chaîne des Puys, en Auvergne, compte 80 volcans endormis depuis au moins 8 000 ans ; elle est inscrite au patrimoine mondial de l'Unesco depuis 2018."
V_EFFUSIF = "Quand la lave est fluide, elle coule doucement en longues coulées : l'éruption est effusive, comme souvent au Piton de la Fournaise."
V_EXPLOSIF = "Quand le magma est épais et riche en gaz, il explose en cendres et en nuées ardentes : l'éruption est explosive, comme à la montagne Pelée en 1902."
LECON_VOLCANS = [("Comment fonctionne un volcan", [V_MAGMA, V_MONTE, V_PRODUITS]),
                 ("Des volcans en France", [V_FOURNAISE, V_PELEE, V_SOUFRIERE, V_PUYS]),
                 ("Deux types d'éruptions", [V_EFFUSIF, V_EXPLOSIF])]

# ---------------------------------------------------------------- Leçon 4 : les séismes
S_FAILLE = "Un séisme se produit quand les roches, poussées par le mouvement des plaques, cassent brusquement le long d'une faille."
S_FOYER = "L'endroit sous terre où la roche casse s'appelle le foyer ; le point de la surface juste au-dessus est l'épicentre."
S_ONDES = "Depuis le foyer, des ondes sismiques partent dans toutes les directions et font vibrer le sol."
S_SISMO = "Un sismographe enregistre ces vibrations : le tracé obtenu s'appelle un sismogramme."
S_MAGNITUDE = "La magnitude est un nombre qui mesure l'énergie libérée par un séisme : plus elle est grande, plus le séisme est fort."
S_REPLIQUE = "Après un séisme, d'autres secousses plus faibles, les répliques, peuvent se produire."
S_TEIL = "Le 11 novembre 2019, un séisme de magnitude 4,8 a endommagé la commune du Teil, en Ardèche."
S_ZONES = "Depuis 2011, la France est découpée en cinq zones de sismicité ; la Guadeloupe et la Martinique sont entièrement en zone forte."
S_PREVOIR = "Les scientifiques savent où les séismes sont probables, mais personne ne sait prévoir le jour et l'heure d'un séisme."
S_TSUNAMI = "Si le sol tremble fort au bord de la mer, il faut s'éloigner de la côte et monter sur une hauteur : un tsunami peut suivre."
LECON_SEISMES = [("Quand la Terre tremble", [S_FAILLE, S_FOYER, S_ONDES, S_REPLIQUE]),
                 ("Mesurer un séisme", [S_SISMO, S_MAGNITUDE, S_TEIL]),
                 ("Où et quand ?", [S_ZONES, S_PREVOIR, S_TSUNAMI])]

# ---------------------------------------------------------------- Leçon 5 : prévenir et se protéger
R_RISQUE = "Un risque naturel existe quand un phénomène naturel, comme un séisme ou une éruption, peut toucher des personnes, des maisons ou des routes."
R_PREVENTION = "La prévention, c'est tout ce que l'on fait avant pour limiter les dégâts : surveiller, informer, construire solidement, s'entraîner."
R_OBSERVATOIRE = "Dans un observatoire, les scientifiques surveillent jour et nuit les volcans et les séismes avec des sismographes et d'autres capteurs."
R_CARTE = "Une carte des risques montre les zones où un phénomène peut se produire ; elle aide les communes à décider où construire."
R_AVANT = "Avant un séisme, on fixe les meubles lourds et on repère les endroits où s'abriter, loin des fenêtres."
R_PENDANT = "Pendant les secousses, on reste où l'on est : on s'abrite près d'un mur porteur ou sous un meuble solide, on protège sa tête avec les bras et on s'éloigne des fenêtres."
R_APRES = "Après les secousses, on sort du bâtiment par les escaliers, sans prendre l'ascenseur, et on écoute les consignes des autorités."
R_ECOLE = "Les parents ne doivent pas aller chercher leurs enfants : l'école les met en sécurité, et on s'y entraîne lors d'exercices."
R_VOLCAN = "Pendant une éruption, on suit les ordres d'évacuation des autorités ; si des cendres tombent, on reste à l'intérieur, fenêtres fermées."
R_PROTECTION = "La protection, c'est ce qui met les personnes à l'abri pendant et après le phénomène : abris, évacuation, secours."
LECON_PREVENTION = [("Le risque naturel", [R_RISQUE, R_PREVENTION, R_OBSERVATOIRE, R_CARTE]),
                    ("Les bons réflexes", [R_AVANT, R_PENDANT, R_APRES, R_ECOLE]),
                    ("Se protéger", [R_VOLCAN, R_PROTECTION])]


def html(sections):
    return "".join(f"<h4>{h}</h4><p>{' '.join(ps)}</p>" for h, ps in sections)
