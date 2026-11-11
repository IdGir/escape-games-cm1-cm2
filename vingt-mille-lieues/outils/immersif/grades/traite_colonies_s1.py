"""Salle 1 « La salle des cartes » : grades mousse, lieutenant, second (fiche : le commerce triangulaire)."""
from aide import *

FICHE = "« Le commerce triangulaire »"
P_TRI = "Sur une carte, les trois trajets du navire dessinent un triangle : on parle de commerce triangulaire."
P_ARM = "L'armateur est le négociant qui finance le navire, recrute l'équipage et achète la cargaison."
P_CARG = "Le navire quitte un port français chargé de tissus, de fusils, de poudre et d'eau-de-vie."
P_ECH = "Sur les côtes d'Afrique, ces marchandises sont échangées contre des captifs."
P_TRAV = "La traversée de l'Atlantique avec les captifs dure en moyenne environ deux mois."
P_VENTE = "Aux Antilles, les captifs sont vendus comme esclaves à des propriétaires de plantations."
P_RET = "Le navire revient en Europe chargé de sucre, de café, de coton ou d'indigo, vendus très cher."
P_SD = "À partir de 1715, Saint-Domingue, l'actuelle Haïti, devient la principale destination des navires français : elle reçoit environ les trois quarts des expéditions."
P_NEUF = "Neuf voyages français sur dix vont aux Antilles ou en Guyane."
P_ROI = "Le roi autorise la traite et la confie d'abord à des compagnies, comme la Compagnie des Indes occidentales, créée en 1664."
P_CONT = "Du XVIIe au XIXe siècle, des négociants européens organisent un commerce qui relie trois continents autour de l'océan Atlantique."


def donnees(svg, bloc=None):
    d = {}
    carte = svg("e1-1", "timonier")
    d["e1-1"] = {
        "mousse": {"type": "plan", "titre": "La carte du registre", "colonnes": 3,
                   "cases": [{"libelle": "Repère 1", "reponse": "Europe"}, {"libelle": "Repère 2", "reponse": "Afrique"}, {"libelle": "Repère 3", "reponse": "Amériques"}],
                   "etiquettes": ["Europe", "Afrique", "Amériques"],
                   "consigne": "Inès montre la carte du registre. Place chaque nom de continent sur son repère. Les repères 4 et 5 ne comptent pas ici." + carte,
                   "indices": ["Ouvre la fiche " + FICHE + " : regarde la carte.", "L'Europe est en haut à droite.", "Les Amériques sont à gauche, de l'autre côté de l'océan."]},
        "lieutenant": {"type": "plan", "titre": "La carte du registre", "colonnes": 2,
                       "cases": [{"libelle": "Repère 1", "reponse": "Europe"}, {"libelle": "Repère 2", "reponse": "Afrique"}, {"libelle": "Repère 3", "reponse": "Amériques"},
                                 {"libelle": "Repère 4", "reponse": "océan Atlantique"}, {"libelle": "Repère 5", "reponse": "trajet des captifs"}],
                       "etiquettes": ["Europe", "Afrique", "Amériques", "océan Atlantique", "trajet des captifs", "trajet du sucre", "océan Indien", "Asie"],
                       "consigne": "Inès a retrouvé la carte du registre. Place chaque étiquette sur son repère (trois étiquettes sont en trop), puis choisis la phrase de la fiche qui explique le nom de ce commerce." + carte,
                       "indices": ["Le repère 5 est posé sur la flèche qui part d'Afrique.", "Le trajet du sucre va des Amériques vers l'Europe : ce n'est pas le repère 5.", "Pour la justification : cherche le mot « triangle »."],
                       "justification": J("Quelle phrase de la fiche explique le nom de ce commerce ?", P_TRI, [P_CONT, P_NEUF, P_TRAV], pos=1)},
        "second": tri(
            "Sur la carte, chaque flèche est un trajet. Range chaque cargaison ou chaque étape sous le bon trajet, puis choisis la phrase de la fiche qui décrit le deuxième trajet." + carte,
            [("t1", "Trajet 1 : Europe → Afrique"), ("t2", "Trajet 2 : Afrique → Amériques"), ("t3", "Trajet 3 : Amériques → Europe")],
            [("des fusils et de la poudre", "t1"), ("de l'eau-de-vie", "t1"), ("des captifs emmenés de force", "t2"), ("environ deux mois de traversée", "t2"),
             ("du sucre et du café", "t3"), ("de l'indigo", "t3")],
            ["Suis les flèches dans l'ordre : 1, 2, 3.", "Les marchandises européennes servent à acheter des captifs.", "Pour la justification : cherche la durée de la traversée."],
            J("Quelle phrase de la fiche décrit le deuxième trajet ?", P_TRAV, [P_RET, P_CARG, P_ARM], pos=2)),
    }
    d["e1-2"] = {
        "mousse": assoc(
            "Relie chaque trajet à ce que transporte le navire.",
            [("de l'Europe vers l'Afrique", "des tissus et des armes"), ("de l'Afrique vers les Amériques", "des captifs"), ("des Amériques vers l'Europe", "du sucre et du café")],
            ["Ouvre la fiche " + FICHE + ".", "Le sucre pousse aux Amériques.", "Les captifs sont emmenés d'Afrique."]),
        "lieutenant": vf(
            "Inès relit les fiches d'un enquêteur débutant. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui dit qui organise l'expédition.",
            [("Le navire part d'Europe chargé de marchandises.", True, "Tissus, fusils, poudre, eau-de-vie."),
             ("Les marchandises sont échangées contre des captifs en Amérique.", False, "L'échange a lieu sur les côtes d'Afrique."),
             ("La traversée avec les captifs dure environ deux mois.", True, "En moyenne."),
             ("Le capitaine finance seul le navire.", False, "C'est l'armateur qui finance le navire."),
             ("Au retour, le navire rapporte du sucre et du café.", True, "Des denrées vendues très cher.")],
            ["Repère où a lieu chaque étape du voyage.", "Un armateur n'est pas un capitaine.", "Pour la justification : cherche le mot « armateur »."],
            J("Quelle phrase de la fiche dit qui organise l'expédition ?", P_ARM, [P_CARG, P_VENTE, P_TRI], pos=0)),
        "second": qcm(
            carnet("Extrait du registre", "(résumé pour l'enquête, d'après la BnF) : les navires français vont surtout aux Antilles ; Saint-Domingue reçoit le plus d'expéditions.")
            + "Réponds aux trois questions, puis choisis la phrase de la fiche qui confirme l'extrait.",
            [("Saint-Domingue est aujourd'hui...", ["la Guadeloupe", "Haïti", "la Guyane", "Cuba"], 1, "L'actuelle Haïti."),
             ("Quelle part des expéditions françaises va à Saint-Domingue ?", ["environ un quart", "environ la moitié", "environ les trois quarts", "presque toutes"], 2, "Environ les trois quarts, à partir de 1715."),
             ("Sur dix voyages français, combien vont aux Antilles ou en Guyane ?", ["deux", "cinq", "sept", "neuf"], 3, "Neuf sur dix.")],
            ["Saint-Domingue a pris un autre nom en devenant indépendante.", "Trois quarts, c'est 75 sur 100.", "Pour la justification : cherche la date 1715."],
            J("Quelle phrase de la fiche confirme l'extrait du registre ?", P_SD, [P_NEUF, P_VENTE, P_CONT], pos=0)),
    }
    d["e1-3"] = {
        "mousse": ordre(
            "Remets les quatre étapes du voyage dans l'ordre.",
            ["Le navire quitte la France avec des marchandises.", "En Afrique, on échange les marchandises contre des captifs.",
             "Le navire traverse l'océan Atlantique.", "Le navire revient en France avec du sucre."],
            ["Ouvre la fiche " + FICHE + ".", "Le voyage commence et finit en France.", "L'océan est traversé après l'Afrique."]),
        "lieutenant": ordre(
            "Les pages du journal de bord sont mélangées. Remets les six étapes dans l'ordre, puis choisis la phrase de la fiche qui décrit la vente aux Antilles.",
            ["L'armateur finance le navire et achète la cargaison.", "Le navire quitte un port français.", "Sur les côtes d'Afrique, les marchandises sont échangées contre des captifs.",
             "La traversée de l'Atlantique dure environ deux mois.", "Aux Antilles, les captifs sont vendus comme esclaves.", "Le navire revient en Europe chargé de sucre et de café."],
            ["Tout commence avant le départ, chez l'armateur.", "Suis le triangle : Europe, Afrique, Amériques, Europe.", "Pour la justification : cherche le mot « propriétaires »."],
            J("Quelle phrase de la fiche décrit la vente aux Antilles ?", P_VENTE, [P_ECH, P_RET, P_ARM], pos=3)),
        "second": ordre(
            "Inès reconstitue l'histoire de ce commerce, de son autorisation à son fonctionnement. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche qui date la première étape.",
            ["Le roi confie la traite à des compagnies (1664).", "D'autres ports, dont Bordeaux, obtiennent le droit de pratiquer la traite (1713-1721).",
             "Pour un voyage, un armateur finance un navire et achète sa cargaison.", "Sur les côtes d'Afrique, la cargaison est échangée contre des captifs.",
             "Aux Antilles, les captifs sont vendus ; le navire rentre avec du sucre et du café."],
            ["Commence par la décision du roi.", "Les compagnies viennent d'abord, puis d'autres ports participent ; ensuite, suis un voyage.", "Pour la justification : cherche l'année 1664."],
            J("Quelle phrase de la fiche date la première étape ?", P_ROI, [P_SD, P_ARM, P_CONT], pos=1)),
    }
    d["e1-4"] = {
        "lieutenant": qcm(
            "Inès vérifie vos connaissances avant de quitter la salle des cartes. Réponds aux quatre questions, puis choisis la phrase de la fiche qui cite les marchandises du départ.",
            [("Pourquoi parle-t-on de commerce triangulaire ?", ["parce que les navires ont trois mâts", "parce que les trois trajets dessinent un triangle", "parce qu'il dure trois ans", "parce qu'il y a trois ports"], 1, "Trois trajets, trois continents."),
             ("Quel océan les navires traversent-ils ?", ["l'océan Indien", "l'océan Pacifique", "l'océan Atlantique", "l'océan Arctique"], 2, "D'où le nom de traite atlantique."),
             ("Que charge-t-on en France pour l'Afrique ?", ["du sucre", "des tissus, des fusils et de l'eau-de-vie", "du café", "des captifs"], 1, "Ces marchandises servent à acheter des captifs."),
             ("Qui finance l'expédition ?", ["l'armateur", "les captifs", "le capitaine seul", "les planteurs"], 0, "L'armateur est un négociant.")],
            ["Regarde la forme des trois flèches.", "Le sucre est rapporté au retour, pas emporté au départ.", "Pour la justification : cherche « fusils »."],
            J("Quelle phrase de la fiche cite les marchandises du départ ?", P_CARG, [P_RET, P_ECH, P_TRI], pos=2)),
        "second": code(
            "Le cadenas de la carte s'ouvre avec trois nombres tirés de la fiche. Écris-les, puis choisis la phrase de la fiche qui donne le deuxième nombre.",
            [("Expéditions françaises vers Saint-Domingue, sur 100 (environ)", "75", 2), ("Voyages français vers les Antilles ou la Guyane, sur 100", "90", 2),
             ("Année de création de la Compagnie des Indes occidentales", "1664", 4)],
            ["Les trois quarts de 100, c'est 75.", "Neuf sur dix, c'est 90 sur 100.", "Pour la justification : cherche « Neuf voyages »."],
            J("Quelle phrase de la fiche donne le deuxième nombre ?", P_NEUF, [P_SD, P_ROI, P_TRAV], pos=3)),
    }
    return d
