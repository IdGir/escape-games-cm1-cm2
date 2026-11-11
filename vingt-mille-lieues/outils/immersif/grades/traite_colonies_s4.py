"""Salle 4 « Le musée du port » : grades mousse, lieutenant, second (fiche : les échanges avec les colonies).
Aucun point n'est lié au profit : on reconstitue, on situe, on explique d'où vient la richesse."""
from aide import *

FICHE = "« Les échanges avec les colonies »"
P_PROD = "Dans les colonies d'Amérique, les esclaves cultivent des produits vendus très cher en Europe : le sucre de canne, le café, le cacao qui donne le chocolat, le coton qui sert à tisser des étoffes, l'indigo qui donne une teinture bleue."
P_CARG = "Pour acheter des captifs, les navires emportent des toiles et des draperies, des fusils et de la poudre, de l'eau-de-vie et du vin, du fer en barre."
P_LIC = "En janvier 1787, La Licorne quitte Bordeaux avec une telle cargaison."
P_TROIS = "Le même navire transporte donc, à chaque trajet, une cargaison différente : des marchandises, puis des captifs, puis des denrées coloniales."
P_NANTES = "Au XVIIIe siècle, Nantes est le premier port négrier français et devient un grand port colonial : la ville s'enrichit visiblement."
P_BDX = "Bordeaux s'enrichit aussi du commerce des produits coloniaux."
P_RICH = "Ces richesses viennent du travail forcé des esclaves."
P_GEN = "Chaque port a son histoire : on ne généralise pas l'histoire d'un port à toute la France."
P_MUSEES = "Ces lieux montrent aussi les personnes réduites en esclavage, leurs résistances et les combats pour l'abolition."
P_DIJON = "Une ville loin de la mer, comme Dijon, n'armait pas de navires."
P_PORTS = "Nantes, La Rochelle, Le Havre et Bordeaux sont des ports de l'Atlantique ou de la Manche."


def donnees(svg, bloc=None):
    d = {}
    d["e4-1"] = {
        "mousse": assoc(
            "Margot remet trois produits dans la vitrine. Relie chaque produit à ce que l'on en fait.",
            [("le sucre", "sucrer les desserts"), ("le café", "une boisson chaude"), ("le coton", "fabriquer des tissus")],
            ["Ouvre la fiche " + FICHE + ".", "Le café se boit.", "Le coton est une fibre."]),
        "lieutenant": assoc(
            "Margot reconstitue la vitrine des produits des colonies. Relie chaque produit à son usage ou à sa plante, puis choisis la phrase de la fiche qui cite ces produits.",
            [("le sucre", "tiré de la canne"), ("le cacao", "donne le chocolat"), ("le coton", "sert à tisser des étoffes"), ("l'indigo", "donne une teinture bleue"), ("le café", "se boit chaud")],
            ["Le chocolat se fabrique avec du cacao.", "L'indigo colore en bleu.", "Pour la justification : cherche « teinture bleue »."],
            J("Quelle phrase de la fiche cite ces produits ?", P_PROD, [P_CARG, P_TROIS, P_BDX], pos=1)),
        "second": qcm(
            "Margot prépare le cartel de la vitrine (le petit texte qui l'explique). Réponds aux trois questions, puis choisis la phrase de la fiche qu'un musée doit absolument afficher.",
            [("Qui cultivait le sucre, le café et le cacao vendus en Europe ?", ["des ouvriers payés", "des esclaves, de force", "des marins", "des armateurs"], 1, "Le travail forcé des esclaves."),
             ("Pourquoi ces produits étaient-ils vendus très cher en Europe ?", ["parce qu'ils venaient de loin et étaient recherchés", "parce qu'ils étaient fabriqués en France", "parce qu'ils étaient gratuits", "parce que le roi les interdisait"], 0, "Des produits rares en Europe, venus des colonies."),
             ("Que doit dire le cartel d'un musée sur ces richesses ?", ["rien", "qu'elles venaient du travail forcé des esclaves", "qu'elles étaient méritées", "qu'elles venaient de Dijon"], 1, "Un musée dit d'où vient la richesse.")],
            ["Relis qui travaille dans les plantations.", "Un produit lointain et recherché est cher.", "Pour la justification : cherche « richesses »."],
            J("Quelle phrase de la fiche un musée doit-il absolument afficher ?", P_RICH, [P_BDX, P_NANTES, P_LIC], pos=3)),
    }
    d["e4-2"] = {
        "mousse": intrus(
            "Trouve l'intrus : la seule ville qui n'est pas un port de mer.",
            [("Nantes", False), ("Le Havre", False), ("Dijon", True)],
            ["Ouvre la fiche " + FICHE + ".", "Un navire part d'un port.", "Dijon est loin de la mer."]),
        "lieutenant": intrus(
            "Margot prépare la vitrine « Ports de l'Atlantique et de la Manche ». Trouve l'intrus, puis choisis la phrase de la fiche qui le justifie.",
            [("Nantes", False), ("La Rochelle", False), ("Le Havre", False), ("Bordeaux", False), ("Dijon", True)],
            ["Les quatre ports sont au bord de l'océan ou de la Manche.", "Bordeaux est sur la Garonne, près de l'océan.", "Pour la justification : cherche « loin de la mer »."],
            J("Quelle phrase de la fiche justifie l'intrus ?", P_DIJON, [P_PORTS, P_GEN, P_NANTES], pos=0)),
        "second": intrus(
            "Margot relit quatre phrases pour le panneau du musée. Trouve l'intrus : la seule phrase fausse ou trop générale, puis choisis la phrase de la fiche qui explique pourquoi.",
            [("Nantes est le premier port négrier français.", False), ("Bordeaux s'enrichit du commerce des produits coloniaux.", False),
             ("Les musées de Nantes et de Bordeaux présentent cette histoire.", False), ("Toutes les villes de France ont armé des navires négriers.", True)],
            ["Cherche la phrase qui parle de « toutes » les villes.", "Une ville loin de la mer n'armait pas de navires.", "Pour la justification : cherche « généralise »."],
            J("Quelle phrase de la fiche explique pourquoi cette phrase est fausse ?", P_GEN, [P_MUSEES, P_NANTES, P_RICH], pos=2)),
    }
    d["e4-3"] = {
        "mousse": tri(
            "Range chaque marchandise : part-elle de France ou revient-elle des colonies ?",
            [("depart", "Part de France"), ("retour", "Revient des colonies")],
            [("des tissus", "depart"), ("des fusils", "depart"), ("du sucre", "retour"), ("du café", "retour")],
            ["Ouvre la fiche " + FICHE + " : regarde le schéma.", "Le sucre pousse aux Antilles.", "Les armes sont fabriquées en Europe."]),
        "lieutenant": tri(
            "Margot reconstitue la cargaison de La Licorne, partie de Bordeaux en 1787. Range chaque marchandise, puis choisis la phrase de la fiche qui dit à quoi servait la cargaison du départ.",
            [("depart", "Chargé en France pour l'Afrique"), ("retour", "Rapporté des colonies d'Amérique")],
            [("des toiles et des draperies", "depart"), ("des fusils et de la poudre", "depart"), ("de l'eau-de-vie et du vin", "depart"), ("du fer en barre", "depart"),
             ("du sucre", "retour"), ("du café", "retour"), ("du cacao", "retour"), ("de l'indigo", "retour")],
            ["Ce qui se cultive dans les plantations revient en Europe.", "Le vin et l'eau-de-vie viennent de France.", "Pour la justification : cherche « Pour acheter des captifs »."],
            J("Quelle phrase de la fiche dit à quoi servait la cargaison du départ ?", P_CARG, [P_PROD, P_LIC, P_BDX], pos=0)),
        "second": tri(
            "Un même navire change de cargaison à chaque trajet. Range chaque élément sous le bon trajet, puis choisis la phrase de la fiche qui résume ce changement.",
            [("t1", "Trajet 1 : France → Afrique"), ("t2", "Trajet 2 : Afrique → Amériques"), ("t3", "Trajet 3 : Amériques → France")],
            [("des toiles et des draperies", "t1"), ("du fer en barre", "t1"), ("des captifs emmenés de force", "t2"),
             ("du sucre et du cacao", "t3"), ("de l'indigo", "t3")],
            ["Le premier trajet emporte des marchandises.", "Le deuxième trajet transporte des personnes.", "Pour la justification : cherche « à chaque trajet »."],
            J("Quelle phrase de la fiche résume ce changement de cargaison ?", P_TROIS, [P_CARG, P_PROD, P_LIC], pos=1)),
    }
    plan_ports = svg("e4-4", "timonier")
    d["e4-4"] = {
        "lieutenant": {"type": "plan", "titre": "Ports de l'Atlantique et de la Manche", "colonnes": 2,
                       "cases": [{"libelle": "Repère 1", "reponse": "Le Havre"}, {"libelle": "Repère 2", "reponse": "Nantes"},
                                 {"libelle": "Repère 3", "reponse": "La Rochelle"}, {"libelle": "Repère 4", "reponse": "Bordeaux"}],
                       "etiquettes": ["Le Havre", "Nantes", "La Rochelle", "Bordeaux", "Marseille", "Lyon"],
                       "consigne": "Margot accroche la carte des ports. Place chaque nom sur son repère (deux étiquettes sont en trop), puis choisis la phrase de la fiche qui situe ces ports." + plan_ports,
                       "indices": ["Le Havre est sur la Manche, tout au nord.", "Nantes est sur la Loire, Bordeaux sur la Garonne.", "Pour la justification : cherche « de l'Atlantique ou de la Manche »."],
                       "justification": J("Quelle phrase de la fiche situe ces ports ?", P_PORTS, [P_DIJON, P_GEN, P_NANTES], pos=3)},
        "second": {"type": "plan", "titre": "Ports de l'Atlantique et de la Manche", "colonnes": 2,
                   "cases": [{"libelle": "Repère 1", "reponse": "Le Havre"}, {"libelle": "Repère 2", "reponse": "Nantes : premier port négrier"},
                             {"libelle": "Repère 3", "reponse": "La Rochelle"}, {"libelle": "Repère 4", "reponse": "Bordeaux : départ de La Licorne"}],
                   "etiquettes": ["Le Havre", "Nantes : premier port négrier", "La Rochelle", "Bordeaux : départ de La Licorne", "Marseille", "Nantes : départ de La Licorne", "Bordeaux : premier port négrier"],
                   "consigne": "Margot veut une carte annotée. Place chaque étiquette sur son repère (trois étiquettes sont en trop), puis choisis la phrase de la fiche qui confirme l'annotation du repère 4." + plan_ports,
                   "indices": ["Le premier port négrier français est sur la Loire.", "La Licorne part en 1787 du port de la Garonne.", "Pour la justification : cherche « La Licorne »."],
                   "justification": J("Quelle phrase de la fiche confirme l'annotation du repère 4 ?", P_LIC, [P_BDX, P_NANTES, P_PORTS], pos=2)},
    }
    return d
