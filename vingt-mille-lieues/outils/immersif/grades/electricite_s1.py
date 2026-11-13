"""Salle 1 « L'atelier du club sciences » : grades mousse, lieutenant, second (fiche : Le circuit électrique)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "electricite", "tests", "donnees"))
from fiches import *

FICHE = "« Le circuit électrique »"


def circuit(consigne, composants, fils, attendu, solution, indices, j=None):
    b = {"type": "circuit", "consigne": consigne, "composants": composants, "fils": fils, "attendu": attendu, "solution": solution, "indices": list(indices)}
    if j:
        b["justification"] = j
    return b


def donnees(svg, bloc=None):
    d = {}
    d5 = svg("e1-1", "timonier")
    d["e1-1"] = {
        "mousse": circuit(
            "Nour a déjà posé un fil entre la pile et sa lampe. Clique une borne, puis une autre, pour poser le fil qui manque. Puis mets sous tension : la lampe doit briller.",
            [{"id": "P", "type": "pile", "libelle": "Pile plate", "x": 18, "y": 50}, {"id": "L1", "type": "lampe", "libelle": "Lampe de Nour", "x": 72, "y": 50}],
            [{"de": "P+", "a": "L1a", "fixe": True}], {"allumes": ["L1"]}, {"fils": [["L1b", "P-"]], "fermes": {}},
            ["Ouvre la fiche " + FICHE + ".", "Le courant part de la borne + et doit revenir à la borne −.", "Relie la deuxième borne de la lampe à la borne − de la pile."]),
        "lieutenant": {"type": "plan", "titre": "Le montage de Nour", "colonnes": 2,
                       "cases": [{"libelle": "Repère 1", "reponse": "pile"}, {"libelle": "Repère 2", "reponse": "lampe"}, {"libelle": "Repère 3", "reponse": "interrupteur"},
                                 {"libelle": "Repère 4", "reponse": "fil de connexion"}, {"libelle": "Repère 5", "reponse": "borne de la pile"}],
                       "etiquettes": ["pile", "lampe", "interrupteur", "fil de connexion", "borne de la pile", "moteur", "prise", "générateur du secteur"],
                       "consigne": "Place chaque étiquette sur son repère (trois sont en trop), puis choisis la phrase de la fiche qui parle des bornes." + d5,
                       "indices": ["La pile est le générateur de ce montage.", "Une borne est une lame métallique.", "Pour la justification : cherche « culot »."],
                       "justification": J("Quelle phrase de la fiche parle des bornes ?", C_BORNES, [C_ELEM, C_INTER, C_FERME], pos=1)},
        "second": tri(
            "Nour a décrit six montages. Range chacun : la lampe brille, la lampe reste éteinte, ou court-circuit. Puis choisis la phrase de la fiche qui explique quand une lampe brille.",
            [("brille", "La lampe brille"), ("eteinte", "La lampe reste éteinte"), ("court", "Court-circuit")],
            [("pile, fil, lampe, fil vers l'autre borne", "brille"), ("pile, fil, interrupteur fermé, lampe, fil vers l'autre borne", "brille"),
             ("pile, fil, lampe, fil laissé libre", "eteinte"), ("pile, fil, interrupteur ouvert, lampe, fil vers l'autre borne", "eteinte"),
             ("un fil relie seul les deux bornes de la pile", "court"), ("un fil relie les deux bornes, une lampe est posée à côté sans fil", "court")],
            ["Cherche la boucle complète.", "Un fil seul entre les deux bornes : court-circuit.", "Pour la justification : cherche « ininterrompue »."],
            J("Quelle phrase de la fiche explique quand une lampe brille ?", C_BOUCLE, [C_ELEM, C_USE, C_DEUX], pos=2)),
    }
    d["e1-2"] = {
        "mousse": vf(
            "Nour te dit ce qu'elle a vu. Vrai ou faux ?",
            [("La lampe brille quand le circuit fait une boucle complète.", True, "D'une borne de la pile à l'autre."),
             ("Un seul fil suffit pour allumer la lampe.", False, "Il faut deux fils, un vers chaque borne."),
             ("Quand l'interrupteur est ouvert, la lampe s'éteint.", True, "La boucle est coupée.")],
            ["Ouvre la fiche " + FICHE + ".", "Compte les bornes de la pile.", "L'interrupteur ouvert coupe le chemin."]),
        "lieutenant": qcm(
            "La lampe de poche de Nour éclaire de moins en moins. Réponds aux questions, puis choisis la phrase de la fiche qui explique pourquoi.",
            [("Qu'est-ce qui s'use dans la lampe de poche ?", ["le courant", "la pile", "les fils", "l'interrupteur"], 1, "C'est la pile qui s'use."),
             ("Le courant qui sort de la lampe est-il « plus faible » que celui qui y entre ?", ["oui, la lampe l'a mangé", "non, le courant ne s'use pas", "oui, il s'arrête dans la lampe", "on ne peut pas savoir"], 1, "Le courant ne s'use pas en traversant la lampe."),
             ("Que faire pour que la lampe brille de nouveau ?", ["changer la pile", "ajouter un fil", "dévisser la lampe", "ouvrir l'interrupteur"], 0, "Une pile neuve.")],
            ["La lampe brille de moins en moins : quelque chose s'épuise.", "Ce n'est pas le courant.", "Pour la justification : cherche « ne s'use pas »."],
            J("Quelle phrase de la fiche explique pourquoi la lampe faiblit ?", C_USE, [C_COURT, C_OUVERT, C_BOUCLE], pos=0)),
        "second": ordre(
            "La lampe de secours du couloir ne s'allume pas. Remets dans l'ordre la démarche de Nour pour trouver la panne, puis choisis la phrase de la fiche sur le rôle de l'interrupteur.",
            ["Vérifier que l'interrupteur est bien fermé.", "Vérifier que chaque fil est bien branché sur sa borne.", "Remplacer la lampe par une lampe qui fonctionne.",
             "Remplacer la pile par une pile neuve.", "Fermer l'interrupteur et observer la lampe."],
            ["On commence par le plus simple.", "Les fils avant les pièces à changer.", "Pour la justification : cherche « sans débrancher »."],
            J("Quelle phrase de la fiche dit à quoi sert l'interrupteur ?", C_INTER, [C_OUVERT, C_FERME, C_BORNES], pos=3)),
    }
    d["e1-3"] = {
        "mousse": tri(
            "Nour a fait quatre essais. Range chacun : la lampe brille ou la lampe reste éteinte.",
            [("brille", "La lampe brille"), ("eteinte", "La lampe reste éteinte")],
            [("deux fils relient la lampe aux deux bornes", "brille"), ("deux fils et l'interrupteur fermé", "brille"),
             ("un seul fil, sur une seule borne", "eteinte"), ("deux fils mais l'interrupteur ouvert", "eteinte")],
            ["Ouvre la fiche " + FICHE + ".", "Il faut une boucle complète.", "Interrupteur ouvert : lampe éteinte."]),
        "lieutenant": vf(
            "Nour a écrit ses conclusions. Vrai ou faux ? Puis choisis la phrase de la fiche qui explique ce qui se passe quand un fil est débranché.",
            [("Un fil débranché coupe la boucle : la lampe s'éteint.", True, "Le circuit est ouvert."),
             ("Relier directement les deux bornes de la pile fait briller la lampe plus fort.", False, "C'est un court-circuit : le fil chauffe."),
             ("Une lampe a deux bornes.", True, "Sur son culot."),
             ("Le courant s'arrête dans la lampe.", False, "Il revient à l'autre borne de la pile.")],
            ["Débranché = boucle coupée.", "Court-circuit : danger pour la pile.", "Pour la justification : cherche « débranché »."],
            J("Quelle phrase de la fiche explique l'effet d'un fil débranché ?", C_OUVERT, [C_FERME, C_INTER, C_COURT], pos=1)),
        "second": qcm(
            carnet("Cahier de Nour", ": « Ma pile neuve a chauffé et s'est vidée en quelques minutes. Ma lampe, elle, n'a jamais brillé. »") + "Réponds aux questions, puis choisis la phrase de la fiche qui explique ce qui s'est passé.",
            [("Quelle erreur Nour a-t-elle sans doute faite ?", ["elle a relié les deux bornes de la pile par un fil, sans la lampe", "elle a fermé l'interrupteur", "elle a utilisé deux fils", "elle a mis la lampe à droite"], 0, "Un court-circuit."),
             ("Pourquoi la lampe n'a-t-elle pas brillé ?", ["le courant passait par le fil seul, sans passer par la lampe", "la lampe était trop loin", "le courant s'est usé", "il faisait jour"], 0, "Le courant prend le chemin du fil."),
             ("Ce montage avec une pile de classe est-il dangereux pour Nour ?", ["oui, elle risque d'être électrocutée", "non pour elle, mais la pile s'abîme et le fil chauffe", "oui, la pile peut exploser à coup sûr", "non, c'est un bon montage"], 1, "La pile de 4,5 V est sans danger pour le corps, mais le court-circuit l'abîme.")],
            ["La pile a chauffé : signe de court-circuit.", "Le courant ne traverse pas la lampe.", "Pour la justification : cherche « court-circuit »."],
            J("Quelle phrase de la fiche explique ce qui s'est passé ?", C_COURT, [C_USE, C_OUVERT, C_BOUCLE], pos=2)),
    }
    d["e1-4"] = {
        "lieutenant": circuit(
            "Nour veut allumer les deux lampes du couloir avec un seul interrupteur. Relie les bornes pour former <b>une seule boucle</b> qui passe par l'interrupteur et les deux lampes. Ferme l'interrupteur (clique dessus), puis mets sous tension. Choisis ensuite la phrase de la fiche qui décrit ce montage.",
            [{"id": "P", "type": "pile", "libelle": "Pile plate", "x": 14, "y": 50}, {"id": "K1", "type": "interrupteur", "libelle": "Interrupteur", "x": 42, "y": 20, "ferme": False},
             {"id": "L1", "type": "lampe", "libelle": "Lampe 1", "x": 78, "y": 30}, {"id": "L2", "type": "lampe", "libelle": "Lampe 2", "x": 52, "y": 78}],
            [], {"allumes": ["L1", "L2"], "fermes": ["K1"], "commande": {"K1": ["L1", "L2"]}, "serie": ["L1", "L2"]},
            {"fils": [["P+", "K1a"], ["K1b", "L1a"], ["L1b", "L2a"], ["L2b", "P-"]], "fermes": {"K1": True}},
            ["Pars de la borne + de la pile.", "Une seule boucle : pile, interrupteur, lampe 1, lampe 2, retour à la pile.", "Pour la justification : cherche « deux lampes »."],
            J("Quelle phrase de la fiche décrit ce montage ?", C_DEUX, [C_DERIV, C_BOUCLE, C_INTER], pos=0)),
        "second": circuit(
            "Hélène exige pour le couloir : les deux lampes fonctionnent, <b>si l'une est dévissée, l'autre reste allumée</b>, l'interrupteur K2 ne commande <b>que</b> le ventilateur, <b>et aucun court-circuit</b>. Un fil déjà posé peut être retiré (clique dessus). Ferme K2, mets sous tension, puis justifie.",
            [{"id": "P", "type": "pile", "libelle": "Pile plate", "x": 10, "y": 50}, {"id": "L1", "type": "lampe", "libelle": "Lampe du couloir", "x": 56, "y": 16},
             {"id": "L2", "type": "lampe", "libelle": "Lampe de l'atelier", "x": 56, "y": 48}, {"id": "K2", "type": "interrupteur", "libelle": "Interrupteur K2", "x": 40, "y": 82, "ferme": False},
             {"id": "M", "type": "moteur", "libelle": "Ventilateur", "x": 74, "y": 82}],
            [{"de": "P+", "a": "P-", "fixe": False, "libelle": "fil oublié"}],
            {"allumes": ["L1", "L2", "M"], "fermes": ["K2"], "independants": ["L1", "L2"], "commande": {"K2": ["M"]}},
            {"retirer": True, "fils": [["P+", "L1a"], ["L1b", "P-"], ["P+", "L2a"], ["L2b", "P-"], ["P+", "K2a"], ["K2b", "Ma"], ["Mb", "P-"]], "fermes": {"K2": True}},
            ["Chaque lampe a sa propre boucle reliée à la pile.", "Le « fil oublié » relie directement les deux bornes.", "Pour la justification : cherche « court-circuit »."],
            J("Pourquoi fallait-il retirer le « fil oublié » ?", C_COURT, [C_DERIV, C_DEUX, C_USE], pos=1)),
    }
    return d
