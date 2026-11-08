"""Salle 4 « La coupole de l'observatoire » : grades mousse, lieutenant, second (fiche : trajectoires)."""
from aide import *

FICHE = "« Trajectoires : droite, cercle ou courbe »"
P_DEF = "La trajectoire est l'ensemble des positions occupées par un objet au cours de son déplacement."
P_RECT = "Si c'est une droite, le mouvement est rectiligne : la bille qui tombe, l'ascenseur, le train sur une voie droite."
P_CIRC = "Si c'est un cercle, le mouvement est circulaire : la grande roue, le manège, la pale d'une éolienne."
P_CURV = "Si c'est une courbe qui n'est pas un cercle, le mouvement est curviligne : un ballon lancé vers le panier, une voiture dans un virage en S."
P_TERRE = "La Terre est la troisième planète du système solaire à partir du Soleil, après Mercure et Vénus."
P_AN = "Elle tourne autour du Soleil en environ un an, à peu près 365 jours ; sa trajectoire est presque un cercle."
P_ACC = "Quand la caisse à savon va de plus en plus vite dans la descente, son mouvement est accéléré."
P_RAL = "Quand elle freine, sa vitesse diminue : le mouvement est ralenti."
P_UNIF = "Si sa vitesse ne change pas, on dit que le mouvement est uniforme."
P_OBS = "La forme du trait dépend de la personne qui regarde : on précise toujours l'observateur."


def plan(titre, colonnes, cases, etiquettes, consigne, indices, j=None):
    b = {"type": "plan", "titre": titre, "colonnes": colonnes, "cases": [{"libelle": l, "reponse": r} for l, r in cases],
         "etiquettes": list(etiquettes), "consigne": consigne, "indices": list(indices)}
    if j:
        b["justification"] = j
    return b


SYS = [("Repère 1", "le Soleil"), ("Repère 2", "Mercure"), ("Repère 3", "la Terre"), ("Repère 4", "trajectoire de la Terre")]


def donnees(svg, bloc=None):
    d = {}
    d["e4-1"] = {
        "mousse": tri(
            "Léonie regarde le parc depuis la coupole. Chaque objet va-t-il tout droit ou en rond ? Range chaque carte.",
            [("droite", "Tout droit"), ("cercle", "En rond")],
            [("une bille qui tombe", "droite"), ("l'ascenseur", "droite"), ("la grande roue", "cercle"), ("le manège", "cercle")],
            ["Ouvre la fiche " + FICHE + " dans la Bibliothèque.", "Ce qui tourne autour d'un centre va en rond.", "Une bille lâchée tombe tout droit."]),
        "lieutenant": tri(
            "Pour une personne immobile au sol, range chaque mouvement selon sa trajectoire, puis choisis la phrase de la fiche qui justifie le classement du ballon.",
            [("rect", "Rectiligne"), ("circ", "Circulaire"), ("curv", "Curviligne")],
            [("une bille lâchée", "rect"), ("l'ascenseur de l'observatoire", "rect"), ("le petit train sur la voie droite", "rect"),
             ("la nacelle de la grande roue", "circ"), ("la pointe d'une pale d'éolienne", "circ"), ("un cheval de bois du manège", "circ"),
             ("un ballon lancé vers le panier", "curv"), ("la caisse à savon dans le virage en S", "curv")],
            ["Imagine le trait laissé par l'objet.", "Curviligne : une courbe qui n'est pas un cercle.", "Pour la justification : cherche le mot « curviligne »."],
            J("Quelle phrase de la fiche justifie le classement du ballon ?", P_CURV, [P_RECT, P_CIRC, P_DEF], pos=2)),
        "second": assoc(
            "Léonie a noté des situations, chacune avec son observateur. Relie chaque situation à la trajectoire vue par cet observateur, puis choisis la phrase de la fiche qui explique pourquoi on précise l'observateur.",
            [("la valve d'une roue de vélo, pour le cycliste", "un cercle autour de l'axe de la roue"), ("la bille que Hugo lâche dans le train qui roule tout droit, pour Hugo", "une droite verticale"),
             ("la Terre, vue depuis l'espace au-dessus du système solaire", "presque un cercle autour du Soleil"), ("un ballon lancé vers le panier, pour un spectateur assis", "une courbe qui monte puis descend"),
             ("l'ascenseur, pour une personne restée dans le hall", "une droite verticale qui monte")],
            ["Lis bien qui regarde dans chaque situation.", "Pour celui qui lâche la bille, elle tombe tout droit.", "Pour la justification : cherche le mot « observateur »."],
            J("Quelle phrase de la fiche explique pourquoi on précise l'observateur ?", P_OBS, [P_DEF, P_AN, P_UNIF], pos=0)),
    }
    d["e4-2"] = {
        "mousse": plan(
            "Le circuit vu du haut de l'observatoire", 3,
            [("Repère 1", "ligne droite"), ("Repère 2", "virage"), ("Repère 3", "cercle du manège")], ["ligne droite", "virage", "cercle du manège"],
            "Léonie a dessiné le circuit. Place chaque étiquette sur le bon repère. Clique sur une étiquette, puis sur la case du repère." + svg("e4-2", "matelot"),
            ["Ouvre la fiche " + FICHE + ".", "Le repère 1 est sur la partie toute droite.", "Le manège tourne en rond."]),
        "lieutenant": plan(
            "Le Soleil et les trois premières planètes", 2, SYS,
            ["le Soleil", "Mercure", "la Terre", "trajectoire de la Terre", "Vénus", "la Lune", "Mars"],
            "Sur le grand écran, Léonie montre le Soleil et les trois premières planètes. Place chaque étiquette sur le bon repère (trois sont en trop), puis choisis la phrase de la fiche qui situe la Terre." + svg("e4-2", "timonier"),
            ["Le Soleil est au centre.", "Compte les cercles à partir du Soleil : Mercure, Vénus, la Terre.", "Pour la justification : cherche « troisième planète »."],
            J("Quelle phrase de la fiche situe la Terre ?", P_TERRE, [P_AN, P_CIRC, P_DEF], pos=0)),
        "second": plan(
            "Le Soleil et les trois premières planètes", 2, SYS,
            ["le Soleil", "Mercure", "la Terre", "trajectoire de la Terre", "Vénus", "trajectoire de Mercure", "la Lune", "Mars"],
            "Léonie prépare la séance de ce soir. Place chaque étiquette sur le bon repère (quatre sont en trop), puis choisis la phrase de la fiche qui décrit le mouvement du repère 3." + svg("e4-2", "timonier"),
            ["Mercure est la planète la plus proche du Soleil.", "Le repère 4 est posé sur le plus grand des trois cercles.", "Pour la justification : cherche « environ un an »."],
            J("Quelle phrase de la fiche décrit le mouvement du repère 3 ?", P_AN, [P_TERRE, P_RECT, P_UNIF], pos=1)),
    }
    d["e4-3"] = {
        "mousse": intrus(
            "Léonie a noté des choses qui tournent en rond. Trouve l'intrus : celle qui va tout droit.",
            [("la grande roue", False), ("le manège", False), ("l'ascenseur", True)],
            ["Ouvre la fiche " + FICHE + ".", "Un ascenseur monte et descend.", "L'intrus ne fait pas de cercle."]),
        "lieutenant": intrus(
            "Léonie a noté cinq mouvements circulaires. Un seul n'en est pas un, pour une personne immobile au sol : trouve-le, puis choisis la phrase de la fiche qui décrit les mouvements circulaires.",
            [("la Terre autour du Soleil", False), ("la pointe d'une pale d'éolienne", False), ("le bout de l'aiguille de l'horloge", False),
             ("un ballon lancé vers le panier", True), ("la nacelle de la grande roue", False)],
            ["Cherche ce qui tourne autour d'un centre.", "Un ballon lancé monte puis redescend.", "Pour la justification : cherche le mot « circulaire »."],
            J("Quelle phrase de la fiche décrit les mouvements circulaires ?", P_CIRC, [P_CURV, P_RECT, P_TERRE], pos=3)),
        "second": vf(
            "Léonie relit ses notes avant la séance publique. Pour chaque phrase, choisis vrai ou faux. Attention aux phrases presque justes.",
            [("La Terre est la deuxième planète à partir du Soleil.", False, "C'est la troisième, après Mercure et Vénus."),
             ("La Terre fait le tour du Soleil en environ 365 jours.", True, "Environ un an."),
             ("Une caisse à savon dont la vitesse ne change pas a un mouvement uniforme.", True, "Uniforme : la vitesse ne change pas."),
             ("Un mouvement circulaire est forcément accéléré.", False, "La grande roue peut tourner toujours à la même vitesse."),
             ("Pour décrire une trajectoire, il faut préciser l'observateur.", True, "La forme du trait dépend de celui qui regarde.")],
            ["Mercure, Vénus, puis la Terre.", "Uniforme veut dire : la vitesse reste la même.", "La forme et la vitesse sont deux choses différentes."],
            J("Quelle phrase de la fiche corrige la quatrième affirmation ?", P_UNIF, [P_ACC, P_CIRC, P_TERRE], pos=0)),
    }
    d["e4-4"] = {
        "lieutenant": qcm(
            "Léonie observe la descente de Yanis à la lunette. Réponds aux quatre questions, puis choisis la phrase de la fiche qui décrit le freinage.",
            [("Dans la pente, Yanis va de plus en plus vite. Son mouvement est...", ["ralenti", "uniforme", "accéléré", "circulaire"], 2, "Sa vitesse augmente."),
             ("Sur le plat, sa vitesse ne change plus. Son mouvement est...", ["uniforme", "accéléré", "ralenti", "immobile"], 0, "La vitesse reste la même."),
             ("Avant la ligne d'arrivée, il freine. Son mouvement est...", ["accéléré", "ralenti", "uniforme", "circulaire"], 1, "Sa vitesse diminue."),
             ("En combien de temps la Terre fait-elle le tour du Soleil ?", ["Environ un jour", "Environ un mois", "Environ un an", "Environ un siècle"], 2, "Environ 365 jours.")],
            ["Accéléré : la vitesse augmente.", "Ralenti : la vitesse diminue ; uniforme : elle ne change pas.", "Pour la justification : cherche le mot « freine »."],
            J("Quelle phrase de la fiche décrit le freinage ?", P_RAL, [P_ACC, P_UNIF, P_OBS], pos=1)),
        "second": ordre(
            "Léonie décrit toute la descente de Yanis, du départ à l'arrêt. Remets les phases dans l'ordre, puis choisis la phrase de la fiche qui décrit la phase de la pente.",
            [("Yanis attend sur la ligne de départ", "immobile"), ("la caisse prend de la vitesse dans la pente", "mouvement accéléré"),
             ("sur la partie plate, la vitesse reste la même", "mouvement uniforme"), ("Yanis freine avant la barrière", "mouvement ralenti"), ("la caisse s'arrête", "immobile")],
            ["La course commence à l'arrêt et finit à l'arrêt.", "On freine à la fin, pas au début.", "Pour la justification : cherche « de plus en plus vite »."],
            J("Quelle phrase de la fiche décrit la phase de la pente ?", P_ACC, [P_RAL, P_UNIF, P_RECT], pos=2)),
    }
    return d
