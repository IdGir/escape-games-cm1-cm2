"""Salle 1 « La serre du botaniste » : grades mousse, lieutenant, second (fiche : La fleur)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "reproduction", "tests", "donnees"))
from fiches import *
from schemas import fleur

FICHE = "« La fleur »"
MOTS5 = ["un pétale", "une étamine", "le pistil", "un sépale", "l'ovaire et ses ovules"]


def donnees(svg, bloc=None):
    d = {}
    d["e1-1"] = {
        "mousse": {"type": "plan", "titre": "La planche de Basile", "colonnes": 3,
                   "cases": [{"libelle": "Repère 1", "reponse": "un pétale"}, {"libelle": "Repère 2", "reponse": "une étamine"}, {"libelle": "Repère 3", "reponse": "le pistil"}],
                   "etiquettes": ["un pétale", "une étamine", "le pistil"],
                   "consigne": "La planche de Basile est tombée. Place chaque mot sur son repère." + fleur(3),
                   "indices": ["Ouvre la fiche " + FICHE + ".", "Le pétale est la grande pièce rose.", "Le pistil est au milieu."]},
        "lieutenant": {"type": "plan", "titre": "La planche de Basile", "colonnes": 2,
                       "cases": [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(MOTS5)],
                       "etiquettes": MOTS5 + ["le stigmate seul", "une graine"],
                       "consigne": "Replace toutes les étiquettes de la planche (deux sont en trop), puis choisis la phrase de la fiche sur le pistil." + fleur(5),
                       "indices": ["Le sépale est vert, sous les pétales.", "L'ovaire est le bas renflé du pistil.", "Pour la justification : cherche « organe femelle »."],
                       "justification": J("Quelle phrase de la fiche décrit le pistil ?", F_PISTIL, [F_ETAMINES, F_ENVELOPPES, F_STIGMATE], pos=1)},
        "second": tri(
            "Basile trie les pièces détachées d'une fleur disséquée. Range chaque pièce : organe mâle, organe femelle, ou ni l'un ni l'autre ; puis choisis la phrase de la fiche sur les étamines.",
            [("male", "Organe mâle"), ("fem", "Organe femelle"), ("ni", "Ni mâle ni femelle")],
            [("les étamines", "male"), ("le pollen", "male"), ("le pistil", "fem"), ("l'ovaire", "fem"), ("les ovules", "fem"), ("les pétales", "ni"), ("les sépales", "ni")],
            ["Le pollen vient d'un organe mâle.", "Pétales et sépales protègent ou attirent.", "Pour la justification : cherche « poudre »."],
            J("Quelle phrase de la fiche décrit les étamines ?", F_ETAMINES, [F_PISTIL, F_DEUX, F_ORGANE], pos=0)),
    }
    d["e1-2"] = {
        "mousse": vf(
            "Basile a écrit trois phrases sur la fleur. Pour chacune, choisis vrai ou faux.",
            [("Le pollen est une poudre souvent jaune.", True, "On le voit sur les doigts."),
             ("Les pétales colorés attirent les insectes.", True, "Les abeilles les voient de loin."),
             ("Le pistil se trouve sous la terre.", False, "Il est au centre de la fleur.")],
            ["Ouvre la fiche " + FICHE + ".", "Touche une étamine : tes doigts jaunissent.", "Le centre de la fleur, c'est le pistil."]),
        "lieutenant": assoc(
            "Relie chaque pièce de la fleur à son rôle, puis choisis la phrase de la fiche sur le stigmate.",
            [("les sépales", "protègent le bouton"), ("les pétales", "attirent les insectes"), ("les étamines", "fabriquent le pollen"),
             ("le stigmate", "retient le pollen"), ("l'ovaire", "contient les ovules")],
            ["Le bouton fermé est vert.", "Collant : le stigmate.", "Pour la justification : cherche « collant »."],
            J("Quelle phrase de la fiche décrit le stigmate ?", F_STIGMATE, [F_PISTIL, F_ENVELOPPES, F_ETAMINES], pos=2)),
        "second": vf(
            "Basile corrige le panneau de la serre. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur les fleurs mâles et femelles.",
            [("Chez le noisetier, les fleurs mâles et les fleurs femelles sont séparées.", True, "Les chatons sont les fleurs mâles."),
             ("Une fleur sans pétales ne peut pas avoir de pollen.", False, "Les fleurs du noisetier, sans pétales colorés, en produisent beaucoup."),
             ("Le pollen doit se déposer sur le stigmate.", True, "C'est le haut collant du pistil."),
             ("Les ovules se trouvent dans les étamines.", False, "Ils sont dans l'ovaire."),
             ("Les sépales sont souvent verts.", True, "Ils protègent le bouton.")],
            ["Pense aux chatons du noisetier.", "Ovules : organe femelle.", "Pour la justification : cherche « noisetier »."],
            J("Quelle phrase de la fiche parle des fleurs mâles et femelles séparées ?", F_DEUX, [F_ORGANE, F_STIGMATE, F_PISTIL], pos=3)),
    }
    d["e1-3"] = {
        "mousse": qcm(
            "Basile pose ses questions aux visiteurs. Choisis la bonne réponse.",
            [("À quoi sert la fleur pour la plante ?", ["à se reproduire", "à boire", "à respirer la nuit", "à faire du bruit"], 0, "Elle donnera des graines."),
             ("Qui fabrique le pollen ?", ["les pétales", "les étamines", "les racines", "les feuilles"], 1, "Les étamines portent le pollen."),
             ("Où sont les ovules ?", ["dans le pistil", "dans les pétales", "dans la tige", "dans le pollen"], 0, "Au centre de la fleur.")],
            ["Ouvre la fiche " + FICHE + ".", "Le pollen est au bout des étamines.", "Le pistil est au centre."]),
        "lieutenant": qcm(
            "Basile prépare un quiz pour les élèves de 6e. Choisis la bonne réponse, puis la phrase de la fiche sur le rôle de la fleur.",
            [("Quel organe femelle contient les ovules ?", ["l'ovaire", "l'étamine", "le sépale", "le pétale"], 0, "C'est le bas renflé du pistil."),
             ("Où le pollen doit-il se déposer ?", ["sur un pétale", "sur le stigmate", "sur une feuille", "sur la tige"], 1, "Le stigmate est collant."),
             ("À quoi servent les pétales colorés ?", ["à attirer les insectes", "à fabriquer le pollen", "à protéger la racine", "à contenir les ovules"], 0, "Couleurs et parfums attirent.")],
            ["Ovaire : organe femelle.", "Le stigmate retient le pollen.", "Pour la justification : cherche « organe de la reproduction »."],
            J("Quelle phrase de la fiche dit à quoi sert la fleur ?", F_ORGANE, [F_ENVELOPPES, F_DEUX, F_OBSERVER], pos=0)),
        "second": assoc(
            "Basile compare la fleur à d'autres organes de la plante. Relie chaque organe à son rôle, puis choisis la phrase de la fiche sur les sépales et les pétales.",
            [("la racine", "puise l'eau dans le sol"), ("la feuille", "fabrique la nourriture de la plante à la lumière"),
             ("la fleur", "sert à la reproduction"), ("les étamines", "produisent le pollen"), ("l'ovaire", "abrite les ovules")],
            ["Une seule partie sert à la reproduction.", "La feuille a besoin de lumière.", "Pour la justification : cherche « bouton »."],
            J("Quelle phrase de la fiche décrit les sépales et les pétales ?", F_ENVELOPPES, [F_ORGANE, F_ETAMINES, F_STIGMATE], pos=1)),
    }
    d["e1-4"] = {
        "lieutenant": ordre(
            "Basile dissèque une fleur de tulipe devant les élèves. Remets ses gestes dans l'ordre, puis choisis la phrase de la fiche sur la dissection.",
            [("Détacher les sépales.", "à l'extérieur"), ("Détacher les pétales.", "les grandes pièces colorées"),
             ("Détacher les étamines.", "les organes mâles"), ("Garder le pistil, au centre.", "l'organe femelle"),
             ("Coller chaque pièce sur une feuille et l'étiqueter.", "la planche est prête")],
            ["De l'extérieur vers le centre.", "Le pistil est le dernier.", "Pour la justification : cherche « dissèque »."],
            J("Quelle phrase de la fiche explique comment observer une fleur ?", F_OBSERVER, [F_ORGANE, F_DEUX, F_ENVELOPPES], pos=2)),
        "second": qcm(
            "Basile pose des questions difficiles aux futurs botanistes. Choisis la bonne réponse, puis la phrase de la fiche sur l'ovaire.",
            [("Une fleur femelle de noisetier n'a pas d'étamines. Que lui faut-il pour faire des noisettes ?", ["rien de plus", "du pollen venu d'une fleur mâle", "plus de pétales", "de l'engrais"], 1, "Le vent apporte ce pollen."),
             ("Une tulipe a des étamines et un pistil. On dit que sa fleur est…", ["seulement mâle", "seulement femelle", "à la fois mâle et femelle", "ni mâle ni femelle"], 2, "Elle porte les deux organes."),
             ("Si l'on coupe tous les pistils d'un massif de fleurs, il n'y aura pas…", ["de pétales", "de graines", "de feuilles", "de racines"], 1, "Les ovules sont dans le pistil."),
             ("Le pollen se dépose d'abord…", ["sur l'ovaire", "sur le stigmate", "dans les ovules", "sur les sépales"], 1, "Le stigmate est en haut du pistil.")],
            ["Une fleur femelle seule ne fabrique pas de pollen.", "Pistil = ovules = futures graines.", "Pour la justification : cherche « renflée »."],
            J("Quelle phrase de la fiche situe les ovules ?", F_PISTIL, [F_STIGMATE, F_ETAMINES, F_DEUX], pos=3)),
    }
    return d
