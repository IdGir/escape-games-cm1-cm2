"""Salle 3 « Le sentier du cratère » : grades mousse, lieutenant, second (fiche : Les volcans)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "terre-active", "tests", "donnees"))
from fiches import *
from schemas import volcan

FICHE = "« Les volcans »"
VMOTS = ["le cratère", "la cheminée", "la chambre magmatique", "une coulée de lave", "le nuage de cendres et de gaz"]


def donnees(svg, bloc=None):
    d = {}
    d["e3-1"] = {
        "mousse": {"type": "plan", "titre": "Le carnet de Maëva", "colonnes": 3,
                   "cases": [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(VMOTS[:3])],
                   "etiquettes": VMOTS[:3],
                   "consigne": "Place chaque mot sur son repère." + volcan(3),
                   "indices": ["Ouvre la fiche " + FICHE + ".", "Le cratère est en haut.", "La chambre est tout en bas."]},
        "lieutenant": {"type": "plan", "titre": "Le carnet de Maëva", "colonnes": 2,
                       "cases": [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(VMOTS)],
                       "etiquettes": VMOTS + ["le noyau", "une nuée de pluie"],
                       "consigne": "Replace toutes les étiquettes du volcan (deux sont en trop), puis choisis la phrase de la fiche qui décrit le chemin du magma." + volcan(5),
                       "indices": ["La lave coule sur le flanc.", "Le nuage gris monte au-dessus.", "Pour la justification : cherche « cheminée »."],
                       "justification": J("Quelle phrase de la fiche décrit le chemin du magma ?", V_MONTE, [V_MAGMA, V_PRODUITS, V_EFFUSIF], pos=1)},
        "second": tri(
            "Maëva compare deux éruptions. Range chaque description, puis choisis la phrase de la fiche sur les éruptions explosives.",
            [("eff", "Éruption effusive"), ("exp", "Éruption explosive")],
            [("une lave fluide qui coule en longues coulées", "eff"), ("des fontaines et des fleuves de lave", "eff"), ("comme souvent au Piton de la Fournaise", "eff"),
             ("un magma épais et riche en gaz", "exp"), ("des cendres et des nuées ardentes", "exp"), ("comme à la montagne Pelée en 1902", "exp")],
            ["Effusive : ça coule.", "Explosive : ça projette.", "Pour la justification : cherche « riche en gaz »."],
            J("Quelle phrase de la fiche décrit une éruption explosive ?", V_EXPLOSIF, [V_EFFUSIF, V_PELEE, V_PRODUITS], pos=0)),
    }
    d["e3-2"] = {
        "mousse": ordre(
            "Remets l'éruption dans l'ordre.",
            ["Le magma est sous le volcan.", "Le magma monte.", "La lave sort du cratère."],
            ["Ouvre la fiche " + FICHE + ".", "Tout commence en bas.", "La sortie est la fin."]),
        "lieutenant": ordre(
            "Remets les étapes de l'éruption dans l'ordre, puis choisis la phrase de la fiche qui dit où le magma s'accumule.",
            [("Le magma s'accumule dans la chambre magmatique.", "sous le volcan"), ("De petits séismes sont enregistrés.", "le magma pousse les roches"),
             ("Le magma monte par la cheminée.", "vers la surface"), ("La lave sort par le cratère ou des fissures.", "l'éruption"), ("La lave refroidit en roche dure.", "après")],
            ["La chambre est le point de départ.", "Les capteurs sentent la montée avant l'éruption.", "Pour la justification : cherche « chambre magmatique »."],
            J("Quelle phrase de la fiche dit où le magma s'accumule ?", V_MAGMA, [V_MONTE, V_PRODUITS, V_FOURNAISE], pos=3)),
        "second": qcm(
            "Maëva forme les nouveaux observateurs. Choisis la bonne réponse, puis la phrase de la fiche sur le Piton de la Fournaise.",
            [("Les capteurs enregistrent de nombreux petits séismes sous le volcan. Que peut-on penser ?", ["le volcan est éteint", "le magma est peut-être en train de monter", "il va pleuvoir", "rien du tout"], 1, "C'est un signe surveillé."),
             ("Pourquoi un observatoire surveille-t-il le Piton de la Fournaise ?", ["parce qu'il est l'un des volcans les plus actifs du monde", "parce qu'il est éteint", "pour les touristes seulement", "parce qu'il est sous la mer"], 0, "Il entre souvent en éruption."),
             ("Que devient la lave en refroidissant ?", ["de l'eau", "une roche dure", "du gaz", "du sable mouillé"], 1, "Elle durcit."),
             ("Quel est le rôle des scientifiques quand le volcan se réveille ?", ["informer les autorités, qui décident de protéger les habitants", "arrêter l'éruption", "boucher le cratère", "ne rien dire"], 0, "Ils surveillent et informent.")],
            ["Petits séismes = magma qui pousse.", "La Fournaise est très active.", "Pour la justification : cherche « La Réunion »."],
            J("Quelle phrase de la fiche parle du Piton de la Fournaise ?", V_FOURNAISE, [V_PUYS, V_EFFUSIF, V_SOUFRIERE], pos=2)),
    }
    d["e3-3"] = {
        "mousse": assoc(
            "Relie chaque produit du volcan à sa description.",
            [("la lave", "elle coule, rouge et brûlante"), ("les cendres", "une poussière grise"), ("les gaz", "une fumée qui monte")],
            ["Ouvre la fiche " + FICHE + ".", "La lave coule.", "Les cendres sont comme de la poussière."]),
        "lieutenant": assoc(
            "Relie chaque volcan français à ce que l'on sait de lui, puis choisis la phrase de la fiche sur la Chaîne des Puys.",
            [("le Piton de la Fournaise", "La Réunion : l'un des volcans les plus actifs du monde"), ("la montagne Pelée", "Martinique : Saint-Pierre détruite en 1902"),
             ("la Soufrière", "Guadeloupe : évacuation de 1976"), ("la Chaîne des Puys", "Auvergne : 80 volcans endormis"),
             ("l'Unesco", "patrimoine mondial depuis 2018 pour la Chaîne des Puys")],
            ["L'Auvergne a des volcans endormis.", "1976 : Guadeloupe.", "Pour la justification : cherche « 80 volcans »."],
            J("Quelle phrase de la fiche parle de la Chaîne des Puys ?", V_PUYS, [V_FOURNAISE, V_SOUFRIERE, V_PELEE], pos=0)),
        "second": ordre(
            "Maëva prépare la frise des volcans français. Range ces événements du plus ancien au plus récent, puis choisis la phrase de la fiche sur la Soufrière.",
            [("Les dernières éruptions de la Chaîne des Puys", "il y a au moins 8 000 ans"), ("L'éruption de la montagne Pelée", "8 mai 1902"),
             ("L'évacuation lors de l'éruption de la Soufrière", "1976"), ("La Chaîne des Puys entre au patrimoine mondial", "2018")],
            ["8 000 ans, c'est très ancien.", "1902 est avant 1976.", "Pour la justification : cherche « évacués »."],
            J("Quelle phrase de la fiche parle de la Soufrière ?", V_SOUFRIERE, [V_PELEE, V_PUYS, V_FOURNAISE], pos=1)),
    }
    d["e3-4"] = {
        "lieutenant": qcm(
            "Maëva compare deux éruptions. Choisis la bonne réponse, puis la phrase de la fiche sur les éruptions effusives.",
            [("Une lave fluide qui coule en longues coulées : l'éruption est…", ["explosive", "effusive", "glaciaire", "souterraine"], 1, "La lave coule."),
             ("Qu'est-ce qu'une nuée ardente ?", ["un nuage de pluie", "un nuage brûlant de gaz et de cendres qui dévale la pente", "une rivière froide", "une fumée sans danger"], 1, "C'est ce qui a frappé Saint-Pierre."),
             ("L'éruption de la montagne Pelée en 1902 était…", ["effusive", "explosive", "sans danger", "sous la mer"], 1, "Magma épais et riche en gaz.")],
            ["Effusive : la lave coule.", "Nuée ardente : très chaude, très rapide.", "Pour la justification : cherche « fluide »."],
            J("Quelle phrase de la fiche décrit une éruption effusive ?", V_EFFUSIF, [V_EXPLOSIF, V_PRODUITS, V_FOURNAISE], pos=3)),
        "second": vf(
            "Maëva relit la fiche d'un stagiaire. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur les produits d'un volcan.",
            [("Un volcan rejette de la lave, des cendres et des gaz.", True, "Ce sont ses trois produits."),
             ("La lave refroidie devient une roche dure.", True, "On marche sur d'anciennes coulées."),
             ("Un volcan endormi depuis 8 000 ans ne peut jamais se réveiller.", False, "C'est pourquoi on le surveille."),
             ("La montagne Pelée a détruit Saint-Pierre le 8 mai 1902.", True, "Par une nuée ardente."),
             ("Les cendres sont des morceaux de lave liquide.", False, "Ce sont de fines poussières.")],
            ["Trois produits.", "Endormi n'est pas éteint.", "Pour la justification : cherche « en refroidissant »."],
            J("Quelle phrase de la fiche décrit les produits d'un volcan ?", V_PRODUITS, [V_MONTE, V_MAGMA, V_EXPLOSIF], pos=2)),
    }
    return d
