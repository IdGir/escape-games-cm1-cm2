"""Salle 2 « Notre-Dame de Paris » (1804) : grades mousse, lieutenant, second (fiche : Le sacre et la naissance de l'Empire)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "napoleon-republique", "tests", "donnees"))
from fiches import *
from schemas import sacre

FICHE = "« Le sacre et la naissance de l'Empire »"
CASES5 = ["Napoléon", "Joséphine", "le pape Pie VII", "la couronne de l'impératrice", "la tribune de la famille"]


def _cases(n):
    return [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(CASES5[:n])]


def donnees(svg, bloc=None):
    d = {}
    d["e2-1"] = {
        "mousse": trous(
            "Complète le registre de Rose.",
            "En 1804, Bonaparte devient [[empereur]]. Il est sacré dans la cathédrale [[Notre-Dame]].",
            ["empereur", "Notre-Dame", "roi"],
            ["Ouvre la fiche " + FICHE + ".", "Ce n'est pas un roi.", "La cathédrale de Paris."]),
        "lieutenant": trous(
            "Complète le registre de Rose, puis choisis la phrase de la fiche qui décrit le geste de Napoléon pendant la cérémonie.",
            "Le 18 mai 1804, Bonaparte devient [[empereur]] sous le nom de [[Napoléon Ier]]. Le 2 décembre, il est sacré à [[Notre-Dame]] en présence du [[pape]]. Il couronne ensuite l'impératrice [[Joséphine]].",
            ["empereur", "Napoléon Ier", "Notre-Dame", "pape", "Joséphine", "roi", "Versailles"],
            ["Mai : la proclamation ; décembre : le sacre.", "L'impératrice s'appelle Joséphine.", "Pour la justification : cherche « lui-même »."],
            J("Quelle phrase de la fiche décrit le geste de Napoléon pendant la cérémonie ?", S_COURONNE, [S_SACRE, S_CHOIX, S_PROCLAME], pos=2)),
        "second": trous(
            "Complète l'explication de Rose, puis choisis la phrase de la fiche qui montre que l'Empire ressemble à une monarchie.",
            "Les Français approuvent l'Empire par un [[plébiscite]]. L'Empire est [[héréditaire]] : le pouvoir doit passer au [[fils]] de l'empereur. Napoléon crée une [[noblesse]] d'Empire, avec des comtes et des [[barons]].",
            ["plébiscite", "héréditaire", "fils", "noblesse", "barons", "élection libre", "Constitution", "députés"],
            ["Plébiscite : on répond oui ou non.", "Héréditaire : comme pour un roi.", "Pour la justification : cherche « monarchie »."],
            J("Quelle phrase de la fiche montre que l'Empire ressemble à une monarchie ?", S_HEREDITAIRE, [S_PLEBISCITE, S_COUR, S_PROCLAME], pos=0)),
    }
    d["e2-2"] = {
        "mousse": {"type": "plan", "titre": "Le tableau du Sacre", "colonnes": 3, "cases": _cases(3), "etiquettes": CASES5[:3],
                   "consigne": "Place chaque nom sur son repère." + sacre(3),
                   "indices": ["Ouvre la fiche " + FICHE + ".", "Napoléon est debout et tient la couronne.", "Le pape est assis, en blanc."]},
        "lieutenant": {"type": "plan", "titre": "Le tableau du Sacre", "colonnes": 2, "cases": _cases(5), "etiquettes": CASES5 + ["Louis XVI", "Marianne"],
                       "consigne": "Place chaque nom sur son repère (deux sont en trop), puis choisis la phrase de la fiche qui dit quel moment David a peint." + sacre(5),
                       "indices": ["La couronne est levée au-dessus de Joséphine.", "La tribune est au fond, en hauteur.", "Pour la justification : cherche « a choisi »."],
                       "justification": J("Quelle phrase de la fiche dit quel moment David a choisi de peindre ?", S_CHOIX, [S_DAVID, S_COURONNE, S_SACRE], pos=1)},
        "second": {"type": "plan", "titre": "Le tableau du Sacre", "colonnes": 2, "cases": _cases(5), "etiquettes": CASES5 + ["Louis XVI", "Marianne", "le roi d'Angleterre"],
                   "consigne": "Place chaque nom sur son repère (trois sont en trop), puis choisis la phrase de la fiche qui présente le peintre du tableau." + sacre(5),
                   "indices": ["Aucun roi n'assiste au sacre.", "Marianne est un symbole de la République.", "Pour la justification : cherche « premier peintre »."],
                   "justification": J("Quelle phrase de la fiche présente le peintre du tableau ?", S_DAVID, [S_CHOIX, S_SACRE, S_INSIGNES], pos=3)},
    }
    d["e2-3"] = {
        "mousse": intrus(
            "Un motif n'est pas un symbole de l'Empire : trouve l'intrus.",
            [("l'aigle", False), ("les abeilles d'or", False), ("le bonnet phrygien", True)],
            ["Ouvre la fiche " + FICHE + ".", "L'aigle est l'emblème de l'Empire.", "Marianne porte le bonnet phrygien."]),
        "lieutenant": intrus(
            "Trouve le motif qui n'appartient pas à l'Empire, puis choisis la phrase de la fiche qui explique le choix des abeilles.",
            [("l'aigle", False), ("les abeilles d'or", False), ("la couronne de lauriers d'or", False), ("la main de justice", False), ("la fleur de lys", True)],
            ["La fleur de lys est le symbole des rois.", "Les abeilles la remplacent.", "Pour la justification : cherche « fleur de lys »."],
            J("Quelle phrase de la fiche explique le choix des abeilles ?", S_ABEILLE, [S_AIGLE, S_INSIGNES, S_COUR], pos=0)),
        "second": intrus(
            "Trouve l'objet qui n'a pas été porté ou tenu par l'empereur au sacre, puis choisis la phrase de la fiche qui explique le choix de l'aigle.",
            [("la couronne de lauriers d'or", False), ("le sceptre", False), ("la main de justice", False), ("le manteau brodé d'abeilles", False), ("l'écharpe tricolore du maire", True)],
            ["Le sceptre et la main de justice sont des insignes du pouvoir.", "Le maire appartient à la République.", "Pour la justification : cherche « Rome antique »."],
            J("Quelle phrase de la fiche explique le choix de l'aigle ?", S_AIGLE, [S_ABEILLE, S_INSIGNES, S_HEREDITAIRE], pos=2)),
    }
    d["e2-4"] = {
        "lieutenant": ordre(
            "Remets dans l'ordre le chemin de Bonaparte vers la couronne, puis choisis la phrase de la fiche qui date la proclamation de l'Empire.",
            [("le coup d'État du 18 brumaire", "9 novembre 1799"), ("le Concordat avec le pape", "15 juillet 1801"), ("Bonaparte consul à vie", "1802"),
             ("Bonaparte proclamé empereur", "18 mai 1804"), ("le sacre à Notre-Dame", "2 décembre 1804")],
            ["1799, 1801, 1802, puis 1804.", "Mai avant décembre.", "Pour la justification : cherche « 18 mai »."],
            J("Quelle phrase de la fiche date la proclamation de l'Empire ?", S_PROCLAME, [S_SACRE, S_PLEBISCITE, S_HEREDITAIRE], pos=1)),
        "second": ordre(
            "Du général au souverain : remets dans l'ordre ces titres et ces honneurs, puis choisis la phrase de la fiche qui décrit la nouvelle noblesse.",
            [("général de la République", "1793"), ("commandant de l'armée d'Italie", "1796"), ("Premier consul", "1799"),
             ("consul à vie", "1802"), ("empereur des Français", "1804")],
            ["Toulon fait de lui un général.", "Consul, puis consul à vie.", "Pour la justification : cherche « comtes »."],
            J("Quelle phrase de la fiche décrit la nouvelle noblesse ?", S_COUR, [S_HEREDITAIRE, S_PROCLAME, S_AIGLE], pos=3)),
    }
    return d
