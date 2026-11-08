"""Salle 5 « Le quai du petit train » : grades mousse, lieutenant, second (fiche : observateur)."""
from aide import *

FICHE = "« Tout dépend de l'observateur »"
P_DEF = "Le mouvement d'un objet est toujours décrit par rapport à un observateur."
P_VOY = "Le même voyageur peut être immobile pour son voisin assis dans le wagon et en mouvement pour la personne restée sur le quai."
P_QUAI = "Pour les voyageurs, c'est le quai qui défile."
P_CHOIX = "Avant de dire qu'un objet bouge, on choisit donc toujours qui le regarde."
P_LACHE = "Dans un train qui roule tout droit à vitesse constante, un objet qu'on lâche décrit une droite verticale par rapport à la personne qui le lâche."
P_QUAI2 = "Pour la personne sur le quai, il avance en même temps que le train pendant sa chute."
P_CLASSE = "Pour classer des concurrents sur une même distance, on convertit leurs durées dans la même unité et on les range de la plus courte à la plus longue."
P_ECART = "L'écart entre deux concurrents est la différence de leurs durées."

RES = lambda lignes: tableau("Résultats officiels de la descente de 200 m (durées inventées pour le jeu)", ["Dossard", "Véhicule", "Durée"], lignes)


def donnees(svg, bloc=None):
    d = {}
    d["e5-1"] = {
        "mousse": vf(
            "Hugo est assis dans le petit train qui roule, en face d'un voyageur. Margaux est sur le quai. Pour chaque phrase, choisis vrai ou faux.",
            [("Pour Hugo, le voyageur assis ne bouge pas.", True, "Ils roulent ensemble."),
             ("Pour Margaux, le voyageur s'éloigne.", True, "Il part avec le train."),
             ("Tout le monde voit le voyageur bouger de la même façon.", False, "Cela dépend de qui regarde.")],
            ["Ouvre la fiche " + FICHE + " dans la Bibliothèque.", "Hugo et le voyageur sont dans le même wagon.", "Margaux, elle, reste sur le quai."]),
        "lieutenant": vf(
            "Le petit train roule tout droit, à vitesse constante. Hugo lâche son stylo dans le wagon ; Margaux regarde depuis le quai. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui décrit la chute du stylo pour Hugo.",
            [("Pour Hugo, le stylo tombe en ligne droite verticale.", True, "Pour celui qui lâche l'objet, il tombe tout droit."),
             ("Pour Margaux, le stylo avance avec le train pendant sa chute.", True, "Elle voit le train et le stylo avancer."),
             ("Le quai est immobile pour les voyageurs du train.", False, "Pour eux, le quai défile."),
             ("Le voyageur assis est immobile pour son voisin.", True, "Ils roulent ensemble."),
             ("On peut dire qu'un objet bouge sans préciser qui le regarde.", False, "Il faut toujours un observateur.")],
            ["Demande-toi toujours : qui regarde ?", "Pour celui qui lâche le stylo, il tombe tout droit vers ses pieds.", "Pour la justification : cherche le mot « lâche »."],
            J("Quelle phrase de la fiche décrit la chute du stylo pour Hugo ?", P_LACHE, [P_QUAI2, P_VOY, P_CHOIX], pos=0)),
        "second": qcm(
            "Hugo pose des questions pièges à ses voyageurs. Le train roule tout droit, à vitesse constante. Réponds aux quatre questions, puis choisis la phrase de la fiche qui décrit la chute du stylo pour Margaux, sur le quai.",
            [("Pour Hugo, le stylo qu'il lâche tombe...", ["en arrière", "en ligne droite verticale", "en cercle", "il ne tombe pas"], 1, "Pour celui qui lâche l'objet, il tombe tout droit."),
             ("Pour Margaux sur le quai, ce même stylo...", ["est immobile", "tombe en reculant", "avance avec le train pendant sa chute", "tourne en rond"], 2, "Elle voit le stylo avancer en même temps qu'il tombe."),
             ("Pour le conducteur assis, la locomotive est...", ["immobile", "en mouvement", "en mouvement circulaire", "ralentie"], 0, "Il roule avec elle."),
             ("Pour décrire le mouvement de la Terre autour du Soleil, on se place...", ["sur la Terre, sans bouger", "comme si on regardait depuis l'espace", "dans le petit train", "on ne peut pas le décrire"], 1, "On regarde le système solaire depuis l'espace.")],
            ["Le même objet peut avoir deux trajectoires différentes pour deux observateurs.", "Margaux voit le train avancer.", "Pour la justification : cherche « la personne sur le quai »."],
            J("Quelle phrase de la fiche décrit la chute du stylo pour Margaux ?", P_QUAI2, [P_LACHE, P_QUAI, P_DEF], pos=3)),
    }
    d["e5-2"] = {
        "mousse": tri(
            "Hugo est assis dans le train qui roule. Pour Hugo, chaque chose bouge-t-elle ou non ? Range chaque carte.",
            [("immobile", "Ne bouge pas pour Hugo"), ("mouvement", "Bouge pour Hugo")],
            [("son voisin assis", "immobile"), ("son sac sur le siège", "immobile"), ("l'arbre dehors", "mouvement"), ("la gare", "mouvement")],
            ["Ouvre la fiche " + FICHE + ".", "Ce qui roule avec Hugo ne bouge pas pour lui.", "Par la fenêtre, les arbres défilent."]),
        "lieutenant": tri(
            "Le petit train roule ; Margaux est sur le quai. Range chaque situation selon ce que voit l'observateur indiqué, puis choisis la phrase de la fiche qui justifie le classement du voyageur.",
            [("immobile", "Immobile pour l'observateur"), ("mouvement", "En mouvement pour l'observateur")],
            [("le voyageur assis, pour son voisin", "immobile"), ("le voyageur assis, pour Margaux", "mouvement"), ("le quai, pour Margaux", "immobile"),
             ("le quai, pour Hugo", "mouvement"), ("la fenêtre du wagon, pour Hugo", "immobile"), ("la vache couchée dans le pré, pour Hugo", "mouvement")],
            ["Lis bien qui regarde sur chaque carte.", "Le même voyageur peut aller dans les deux colonnes.", "Pour la justification : cherche « le même voyageur »."],
            J("Quelle phrase de la fiche justifie le classement du voyageur ?", P_VOY, [P_LACHE, P_CLASSE, P_ECART], pos=1)),
        "second": tri(
            "Hugo se lève et marche vers la locomotive, dans le train qui roule. Range chaque situation selon ce que voit l'observateur indiqué, puis choisis la phrase de la fiche qui justifie le classement du quai.",
            [("immobile", "Immobile pour l'observateur"), ("mouvement", "En mouvement pour l'observateur")],
            [("Hugo qui marche, pour un voyageur assis", "mouvement"), ("Hugo qui marche, pour Margaux sur le quai", "mouvement"), ("le voyageur assis, pour un autre voyageur assis", "immobile"),
             ("le quai, pour le voyageur assis", "mouvement"), ("la gare, pour Margaux", "immobile"), ("le siège vide, pour le voyageur assis", "immobile"), ("le siège vide, pour Margaux", "mouvement")],
            ["Pour chaque carte, demande-toi si la distance entre l'objet et l'observateur change.", "Hugo qui marche s'éloigne du voyageur assis.", "Pour la justification : cherche « le quai qui défile »."],
            J("Quelle phrase de la fiche justifie le classement du quai ?", P_QUAI, [P_QUAI2, P_DEF, P_LACHE], pos=2)),
    }
    d["e5-3"] = {
        "mousse": code(
            "Le chronomètre officiel s'ouvre avec le classement : écris les numéros de dossard, du premier arrivé au dernier." + RES([["2", "le petit train", "75 s"], ["4", "le vélo de Salomé", "41 s"], ["5", "la voiture solaire de l'école", "90 s"], ["7", "la caisse à savon de Yanis", "48 s"], ["9", "la trottinette de Léo", "63 s"]]),
            [("Code du chronomètre officiel", "47925", 5)],
            ["Ouvre la fiche " + FICHE + " : cherche le classement.", "Le premier a la plus petite durée : le dossard 4.", "Ensuite 7, puis 9, puis 2, puis 5."]),
        "lieutenant": code(
            "Le chronomètre officiel ne s'ouvre qu'avec le classement de la descente : écris les dossards du plus rapide au plus lent, puis l'écart entre le premier et le dernier, et choisis la phrase de la fiche qui dit comment calculer l'écart." + RES([["2", "le petit train", "1 min 15 s"], ["4", "le vélo de Salomé", "41 s"], ["5", "la voiture solaire de l'école", "1 min 30 s"], ["7", "la caisse à savon de Yanis", "48 s"], ["9", "la trottinette de Léo", "1 min 03 s"]]),
            [("Code du chronomètre officiel", "47925", 5), ("Écart entre le premier et le dernier (en s)", "49", 2)],
            ["Convertis toutes les durées en secondes.", "1 min 03 s = 63 s ; 1 min 15 s = 75 s ; 1 min 30 s = 90 s.", "Pour la justification : cherche le mot « écart »."],
            J("Quelle phrase de la fiche dit comment calculer l'écart ?", P_ECART, [P_CLASSE, P_DEF, P_CHOIX], pos=1)),
        "second": code(
            RES([["2", "le petit train", "75 s"], ["4", "le vélo de Salomé", "0 min 41 s"], ["5", "la voiture solaire de l'école", "1 min 30 s"],
                 ["7", "la caisse à savon de Yanis", "48 s"], ["9", "la trottinette de Léo", "1 min 03 s"]])
            + "Le chronomètre officiel demande le classement complet (dossards du plus rapide au plus lent), puis l'écart entre le 2e et le 4e. Choisis enfin la phrase de la fiche qui décrit la méthode de classement.",
            [("Code du chronomètre officiel", "47925", 5), ("Écart entre le 2e et le 4e (en s)", "27", 2)],
            ["Convertis tout en secondes avant de ranger.", "Le 2e est le dossard 7, le 4e le dossard 2.", "75 s − 48 s."],
            J("Quelle phrase de la fiche décrit la méthode de classement ?", P_CLASSE, [P_ECART, P_VOY, P_QUAI], pos=0)),
    }
    d["e5-4"] = {
        "lieutenant": lettres(
            "Léonie envoie un message au quai. Certaines lettres sont marquées : clique dans l'ordre celles qui forment le verbe qui manque à toute description d'un mouvement. Attention aux lettres pièges. Choisis ensuite la phrase de la fiche qui résume le message.",
            list("REGARDER"),
            marque("Commissaires, une dernière chose. Quand vous dites « il bouge », pensez à celui qui re[g]arde. Le voyag[e]ur assis ne bouge pas pour son voisin, m[a]is il s'éloigne pou[r] la personne sur le qua[i]. Le stylo lâché tombe tout [d]roit pour celui qui le lâche. Mon conseil : avant de déc[r]ire un mouvement, choisiss[e]z toujours un obse[r]vateur, puis [n]otez ce qu'il voit."),
            ["Le mot a huit lettres.", "C'est ce que fait l'observateur avec ses yeux.", "Il commence par R et finit par R."],
            J("Quelle phrase de la fiche résume ce message ?", P_CHOIX, [P_QUAI, P_ECART, P_LACHE], pos=0)),
        "second": lettres(
            "Le haut-parleur du quai diffuse le dernier message de Léonie. Certaines lettres sont marquées : clique dans l'ordre celles qui forment le mot de la règle d'or du Grand Prix. Attention aux lettres pièges. Choisis ensuite la phrase de la fiche qui énonce cette règle.",
            list("OBSERVATEUR"),
            marque("Le Grand Prix est terminé, et l'éc[r]an de la coupole s'allume. On y voit la Terre [t]ourner autour du Soleil, comme si on la regardait depuis l'espace. Pour un voyageur [a]ssis, le quai défile ; pour la personne restée s[u]r le quai, c'est le train qui part. Chaque phrase juste commence par la même [q]uestion : qui [o]bserve ? Le mouvement n'e[x]iste pas sans quelqu'un qui le décrit. Gardez ce [v]ieux carnet, il est à vous : il [b]rillera dans votre classe. R[e]ndez-vous l'an prochain, [s]i vous voulez bi[e]n, pour une nouvelle cou[r]se."),
            ["Le mot a onze lettres.", "C'est le mot-clé de cette salle.", "Il commence par O et finit par R."],
            J("Quelle phrase de la fiche énonce la règle d'or ?", P_DEF, [P_VOY, P_CLASSE, P_QUAI2], pos=2)),
    }
    return d
