"""Lettre 3 « L'usine d'obus » (1917) : grades mousse, lieutenant, second (fiche : L'arrière, tout un pays en guerre)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "grande-guerre", "tests", "donnees"))
from fiches import *

FICHE = "« L'arrière : tout un pays en guerre »"


def donnees(svg, bloc=None):
    d = {}
    d["e3-1"] = {
        "mousse": intrus(
            "Marcelle montre des photos. Une carte ne montre pas un travail de femme pendant la guerre : trouve l'intruse.",
            [("Une femme fait la moisson.", False), ("Une ouvrière fabrique des obus.", False), ("Une infirmière soigne un soldat.", False), ("Une femme vote à l'élection.", True)],
            ["Ouvre la fiche " + FICHE + ".", "Trois cartes montrent un travail.", "Les femmes ne votent pas encore."]),
        "lieutenant": intrus(
            "Marcelle a écrit des légendes pour ses photos. Une légende est fausse : trouve l'intruse, puis choisis la phrase de la fiche qui le montre.",
            [("Des paysannes font les vendanges.", False), ("Une munitionnette remplit des obus.", False), ("Une conductrice de tramway fait sa tournée.", False),
             ("Une factrice distribue le courrier.", False), ("Une femme est élue maire en 1917.", True)],
            ["Les femmes remplacent les hommes au travail.", "Mais elles ne votent pas et ne sont pas élues.", "Pour la justification : cherche « 1944 »."],
            J("Quelle phrase de la fiche explique pourquoi une légende est fausse ?", A_VOTE, [A_METIERS, A_USINES, A_CHAMPS], pos=3)),
        "second": qcm(
            "Marcelle lit les chiffres du journal de l'usine. Réponds, puis choisis la phrase de la fiche qui donne le nombre de munitionnettes.",
            [("Combien de femmes travaillent dans les usines d'armement en 1918 ?", ["environ 4 300", "environ 43 000", "environ 430 000", "environ 4,3 millions"], 2, "Environ 430 000."),
             ("Combien d'ouvriers chinois sont employés en France ?", ["environ 400", "environ 40 000", "environ 4 millions", "aucun"], 1, "Par exemple au Creusot."),
             ("En quelle année les Françaises obtiennent-elles le droit de vote ?", ["1918", "1922", "1944", "1789"], 2, "Bien après la guerre."),
             ("Que fabrique d'abord l'économie de guerre ?", ["des jouets", "des obus, des canons et des uniformes", "des vélos de course", "des robes de bal"], 1, "Tout pour l'armée.")],
            ["430 000 : plus de quatre cent mille.", "Le Creusot est en Saône-et-Loire.", "Pour la justification : cherche « 1918 »."],
            J("Quelle phrase de la fiche donne le nombre de femmes dans les usines d'armement ?", A_430, [A_USINES, A_CHINOIS, A_ECONOMIE], pos=1)),
    }
    d["e3-2"] = {
        "mousse": tri(
            "Range chaque carte : sur le front, ou à l'arrière.",
            [("front", "Sur le front"), ("arriere", "À l'arrière")],
            [("la tranchée", "front"), ("les barbelés", "front"), ("l'usine", "arriere"), ("l'école", "arriere")],
            ["Ouvre la fiche " + FICHE + ".", "Le front : là où l'on combat.", "L'arrière : le reste du pays."]),
        "lieutenant": tri(
            "Marcelle trie les nouvelles de la semaine. Range chaque carte, puis choisis la phrase de la fiche qui définit l'arrière.",
            [("front", "Sur le front"), ("arriere", "À l'arrière")],
            [("la banquette de tir", "front"), ("le no man's land", "front"), ("l'abri creusé sous terre", "front"),
             ("l'école devenue hôpital", "arriere"), ("les vendanges", "arriere"), ("l'usine d'obus", "arriere"), ("la préparation des colis", "arriere")],
            ["L'hôpital de l'école est loin des tranchées.", "Les colis partent de l'arrière.", "Pour la justification : cherche « tout le pays »."],
            J("Quelle phrase de la fiche définit l'arrière ?", A_ARRIERE, [A_ECONOMIE, A_ATTENTE, A_HOPITAL], pos=0)),
        "second": tri(
            "Range chaque personne selon l'endroit où elle sert pendant la guerre, puis choisis la phrase de la fiche sur les travailleurs venus d'ailleurs.",
            [("front", "Sur le front"), ("arriere", "À l'arrière")],
            [("le poilu de la tranchée", "front"), ("le tirailleur venu du Sénégal", "front"), ("la munitionnette", "arriere"),
             ("l'ouvrier venu de Chine", "arriere"), ("l'écolière qui tricote pour les soldats", "arriere"), ("l'infirmière de l'hôpital de l'école", "arriere")],
            ["Les tirailleurs combattent.", "Les ouvriers venus de loin travaillent en France.", "Pour la justification : cherche « ports »."],
            J("Quelle phrase de la fiche parle des travailleurs venus d'ailleurs ?", A_TRAVAILLEURS, [A_CHINOIS, A_ECOLE, A_USINES], pos=2)),
    }
    d["e3-3"] = {
        "mousse": trous(
            "Complète le carnet de Marcelle.",
            "Les hommes sont au [[front]]. Les [[femmes]] travaillent à l'usine.",
            ["front", "femmes"],
            ["Ouvre la fiche " + FICHE + ".", "Où sont les soldats ?", "Qui remplace les hommes ?"]),
        "lieutenant": trous(
            "Le carnet de Marcelle a pris l'eau. Complète-le (des étiquettes sont en trop), puis choisis la phrase de la fiche sur l'économie de guerre.",
            "Toute l'[[économie]] travaille pour la guerre. Les usines fabriquent des [[obus]] et des [[uniformes]]. Les femmes qui fabriquent des obus sont appelées [[munitionnettes]]. Des écoles deviennent des [[hôpitaux]].",
            ["économie", "obus", "uniformes", "munitionnettes", "hôpitaux", "tranchées", "vacances"],
            ["Économie de guerre.", "Obus, canons, uniformes.", "Pour la justification : cherche « économie de guerre »."],
            J("Quelle phrase de la fiche définit l'économie de guerre ?", A_ECONOMIE, [A_USINES, A_ARRIERE, A_HOPITAL], pos=1)),
        "second": intrus(
            "Marcelle relit les phrases d'un journal. Une phrase est fausse : trouve l'intruse, puis choisis la phrase de la fiche sur les enfants.",
            [("Des écoles deviennent des hôpitaux.", False), ("Les élèves écrivent aux soldats.", False), ("Les élèves collectent de l'argent et des vêtements.", False),
             ("Les écoliers vont tous combattre dans les tranchées.", True), ("Les familles attendent les lettres du front.", False)],
            ["Les enfants restent à l'arrière.", "La guerre entre dans la classe.", "Pour la justification : cherche « la classe »."],
            J("Quelle phrase de la fiche décrit les enfants pendant la guerre ?", A_ECOLE, [A_ATTENTE, A_CHAMPS, A_HOPITAL], pos=0)),
    }
    d["e3-4"] = {
        "lieutenant": assoc(
            "Relie chaque personne à ce qu'elle fait pendant la guerre, puis choisis la phrase de la fiche sur les campagnes.",
            [("la munitionnette", "remplit des obus"), ("la paysanne", "moissonne à la place des hommes"), ("l'infirmière", "soigne les blessés"),
             ("l'écolier", "écrit aux soldats"), ("l'ouvrier venu de Chine", "travaille à l'usine du Creusot")],
            ["Moissons et vendanges : les campagnes.", "Les obus : la munitionnette.", "Pour la justification : cherche « moissons »."],
            J("Quelle phrase de la fiche décrit le travail dans les campagnes ?", A_CHAMPS, [A_USINES, A_METIERS, A_TRAVAILLEURS], pos=2)),
        "second": trous(
            "Marcelle écrit un article sur l'arrière. Complète-le (des étiquettes sont en trop), puis choisis la phrase de la fiche qui parle de la mort des soldats.",
            "À l'[[arrière]], tout le pays travaille. En 1918, environ [[430 000]] femmes travaillent dans les usines d'armement. Environ [[40 000]] ouvriers venus de [[Chine]] travaillent aussi en France. Pourtant, les femmes ne [[votent]] pas encore. Chaque village attend les [[lettres]] et apprend la mort de certains de ses soldats.",
            ["arrière", "430 000", "40 000", "Chine", "votent", "lettres", "4 300", "Russie", "chantent"],
            ["430 000 femmes, 40 000 ouvriers chinois.", "Le droit de vote arrive en 1944.", "Pour la justification : cherche « attendent »."],
            J("Quelle phrase de la fiche parle de l'attente des familles ?", A_ATTENTE, [A_ARRIERE, A_VOTE, A_ECOLE], pos=3)),
    }
    return d
