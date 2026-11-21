# -*- coding: utf-8 -*-
"""Phrases des fiches (leçons CM2) du jeu « Radio Londres » (Seconde Guerre mondiale).
Utilisées mot pour mot : (1) dans lecons.json (gen_lecons.py), (2) dans les justifications des grades Archiviste et Passeur de mémoire
(vingt-mille-lieues/outils/immersif/grades/seconde_guerre_s*.py). Ne modifier une phrase qu'ici.
SUJET TRÈS SENSIBLE : ton grave et sobre ; aucune image de camp ; aucune énigme notée sur les persécutions (elles sont traitées
dans la leçon 3 et en discussion) ; vocabulaire exact (Shoah, génocide des Juifs) ; Vichy et collaboration nuancent la résistance.
Sources : ministère des Armées (Chemins de mémoire ; « Hommage national aux Justes », 2026) ; USHMM, Encyclopédie de la Shoah, « France » ;
Encyclopædia Universalis, « Service du travail obligatoire » ; Ordre de la Libération ; Fondation de la Résistance ; Mémorial de Caen.
Points non relus en ligne pendant la production : A-VERIFIER.md."""

# ---------------------------------------------------------------- Leçon 1 : la montée des dictatures (1919-1939)
R_CRISE = "En octobre 1929, la Bourse de New York s'effondre : c'est le début d'une grave crise économique qui touche le monde entier."
R_CHOMAGE = "Des usines ferment, des millions de personnes perdent leur travail et beaucoup ont peur de l'avenir."
R_TOTAL = "Un régime totalitaire est une dictature qui veut contrôler toute la vie des habitants : un parti unique, un chef tout-puissant, la propagande, la police politique et aucune liberté."
R_MUSSO = "En Italie, Mussolini, chef du parti fasciste, prend le pouvoir en 1922."
R_HITLER = "En Allemagne, Hitler, chef du parti nazi, devient chancelier le 30 janvier 1933 et installe très vite une dictature."
R_RACISME = "Le nazisme repose sur le racisme et l'antisémitisme, c'est-à-dire la haine des Juifs."
R_STALINE = "En Union soviétique (URSS), Staline dirige une dictature communiste qui envoie des millions d'opposants dans des camps de travail."
R_DEMO = "La France et le Royaume-Uni restent des démocraties : on y vote librement, les journaux sont libres et on peut critiquer le gouvernement."
R_CONQUETE = "Hitler veut agrandir l'Allemagne par la force : en 1938, il annexe l'Autriche, puis une partie de la Tchécoslovaquie."
LECON_MONTEE = [("La crise de 1929", [R_CRISE, R_CHOMAGE]),
                ("Des dictatures en Europe", [R_TOTAL, R_MUSSO, R_HITLER, R_RACISME, R_STALINE]),
                ("La démocratie menacée", [R_DEMO, R_CONQUETE])]

# ---------------------------------------------------------------- Leçon 2 : 1939-1940, la défaite et Vichy
D_DECLA = "Le 1er septembre 1939, l'armée allemande envahit la Pologne ; le 3 septembre, le Royaume-Uni et la France déclarent la guerre à l'Allemagne."
D_DROLE = "Pendant huit mois, il y a peu de combats à l'ouest : on parle de « drôle de guerre »."
D_ATTAQUE = "Le 10 mai 1940, l'armée allemande attaque à l'ouest ; en six semaines, l'armée française est battue."
D_EXODE = "Des millions de Français fuient sur les routes devant l'avancée allemande : c'est l'exode."
D_PARIS = "Le 14 juin 1940, l'armée allemande entre dans Paris."
D_PETAIN = "Le 17 juin 1940, le maréchal Pétain, nouveau chef du gouvernement, annonce à la radio qu'il faut cesser le combat."
D_APPEL = "Le 18 juin 1940, depuis Londres, le général de Gaulle lance à la radio de la BBC un appel à continuer le combat."
D_ARMISTICE = "L'armistice est signé le 22 juin 1940 à Rethondes : la France est coupée en deux par une ligne de démarcation, le nord et l'ouest sont occupés par l'armée allemande."
D_VICHY = "Le 10 juillet 1940, les députés et les sénateurs donnent les pleins pouvoirs à Pétain : la République est remplacée par l'État français, installé à Vichy."
D_DICTA = "Le régime de Vichy est une dictature : il n'y a plus d'élections, les libertés sont supprimées et la devise devient « Travail, Famille, Patrie »."
D_COLLAB = "En octobre 1940, à Montoire, Pétain rencontre Hitler et choisit la collaboration, c'est-à-dire aider l'Allemagne nazie."
LECON_DEFAITE = [("La guerre commence", [D_DECLA, D_DROLE]),
                 ("La défaite de 1940", [D_ATTAQUE, D_EXODE, D_PARIS, D_PETAIN, D_APPEL, D_ARMISTICE]),
                 ("Le régime de Vichy", [D_VICHY, D_DICTA, D_COLLAB])]

# ---------------------------------------------------------------- Leçon 3 : la vie sous l'Occupation
O_RATION = "La nourriture, le charbon et les vêtements manquent : ils sont rationnés."
O_TICKETS = "Chaque Français reçoit une carte et des tickets de rationnement selon son âge : sans ticket, on ne peut pas acheter de pain, de viande ou de sucre."
O_QUEUE = "On fait la queue pendant des heures devant les magasins ; certains achètent en cachette, très cher, au marché noir."
O_ERSATZ = "On remplace ce qui manque par des ersatz : de l'orge grillée à la place du café, des semelles de bois pour les chaussures."
O_STO = "Le 16 février 1943, une loi crée le Service du travail obligatoire (STO) : des jeunes Français doivent partir travailler en Allemagne."
O_REFRACT = "Beaucoup de jeunes refusent de partir : ces réfractaires se cachent, et certains rejoignent les maquis."
O_PERSEC = "Les nazis et le régime de Vichy persécutent les Juifs : ils sont exclus de nombreux métiers et, en zone occupée, ils doivent porter une étoile jaune à partir de 1942."
O_RAFLE = "Les 16 et 17 juillet 1942, à Paris, environ 13 000 Juifs, dont des enfants, sont arrêtés par la police française : c'est la rafle du Vél d'Hiv."
O_SHOAH = "75 721 Juifs sont déportés de France vers les camps d'extermination ; seuls 2 566 survivent : c'est la Shoah, le génocide des Juifs d'Europe."
O_AUTRES = "Les nazis persécutent aussi les Tsiganes et leurs opposants politiques."
O_JUSTES = "Des Français cachent et sauvent des Juifs, souvent des enfants, en risquant leur vie : on les honore du titre de Justes parmi les Nations."
LECON_OCCUPATION = [("Vivre avec des tickets", [O_RATION, O_TICKETS, O_QUEUE, O_ERSATZ]),
                    ("Le travail forcé", [O_STO, O_REFRACT]),
                    ("Les persécutions", [O_PERSEC, O_RAFLE, O_SHOAH, O_AUTRES, O_JUSTES])]

# ---------------------------------------------------------------- Leçon 4 : la Résistance
S_REFUS = "Résister, c'est refuser la défaite, l'occupation allemande et la collaboration, en prenant de très grands risques."
S_LONDRES = "À Londres, le général de Gaulle organise la France libre, qui continue la guerre aux côtés des Alliés."
S_RADIO = "Chaque soir, la radio de Londres, la BBC, diffuse l'émission « Les Français parlent aux Français » ; en France, l'écouter est interdit."
S_MESSAGES = "Radio Londres envoie aussi des messages personnels : des phrases étranges qui sont des ordres codés pour les résistants."
S_JOURNAUX = "Des résistants impriment en cachette des journaux et des tracts clandestins pour dire la vérité."
S_RESEAUX = "Les réseaux de renseignement observent l'occupant et transmettent des informations aux Alliés."
S_MAQUIS = "À partir de 1943, des jeunes réfractaires au STO se cachent dans les forêts et les montagnes : ce sont les maquis, comme dans le Morvan."
S_MOULIN = "Envoyé par de Gaulle, Jean Moulin unifie les mouvements de résistance ; le 27 mai 1943, il réunit à Paris le Conseil national de la Résistance (CNR)."
S_ARRET = "Jean Moulin est arrêté le 21 juin 1943 près de Lyon ; il meurt quelques semaines plus tard, sans avoir parlé."
S_FEMMES = "Des femmes jouent un grand rôle : agentes de liaison, elles transportent des messages, des tracts et des papiers."
S_RISQUE = "Les résistants risquent l'arrestation, la déportation ou la mort ; ils sont une minorité, qui grandit à partir de 1943."
LECON_RESISTANCE = [("Dire non", [S_REFUS, S_LONDRES, S_RISQUE]),
                    ("Les armes de l'ombre", [S_RADIO, S_MESSAGES, S_JOURNAUX, S_RESEAUX, S_FEMMES]),
                    ("Maquis et unité", [S_MAQUIS, S_MOULIN, S_ARRET])]

# ---------------------------------------------------------------- Leçon 5 : la Libération et la victoire des Alliés
L_ALLIES = "Les Alliés, dont le Royaume-Uni, l'Union soviétique et les États-Unis (entrés en guerre en décembre 1941), combattent l'Allemagne nazie."
L_DEBARQ = "Le 6 juin 1944, les Alliés débarquent sur les plages de Normandie : c'est le Jour J."
L_VERLAINE = "Les jours précédents, Radio Londres diffuse des vers de Verlaine, « Les sanglots longs des violons de l'automne », pour prévenir les résistants."
L_PROVENCE = "Le 15 août 1944, d'autres troupes alliées, dont l'armée française, débarquent en Provence."
L_PARIS = "Le 25 août 1944, Paris est libéré par la 2e division blindée du général Leclerc, les Alliés et les résistants."
L_DIJON = "En Bourgogne, Dijon est libérée le 11 septembre 1944."
L_GPRF = "Le général de Gaulle dirige le Gouvernement provisoire de la République française : la République est rétablie."
L_VOTE = "En 1944, les Françaises obtiennent le droit de vote ; elles votent pour la première fois en 1945."
L_8MAI = "Le 8 mai 1945, l'Allemagne nazie capitule : la guerre est finie en Europe."
L_JAPON = "La guerre se termine dans le monde le 2 septembre 1945, avec la capitulation du Japon."
L_BILAN = "La guerre a fait des dizaines de millions de morts dans le monde, en majorité des civils."
L_JAMAIS = "Pour que cela ne recommence jamais, les pays vainqueurs créent l'ONU en 1945 ; plus tard, des pays d'Europe autrefois ennemis construiront ensemble la paix."
LECON_LIBERATION = [("Les débarquements", [L_ALLIES, L_DEBARQ, L_VERLAINE, L_PROVENCE]),
                    ("La France libérée", [L_PARIS, L_DIJON, L_GPRF, L_VOTE]),
                    ("La victoire et la paix", [L_8MAI, L_JAPON, L_BILAN, L_JAMAIS])]


def html(sections):
    return "".join(f"<h4>{h}</h4><p>{' '.join(ps)}</p>" for h, ps in sections)
