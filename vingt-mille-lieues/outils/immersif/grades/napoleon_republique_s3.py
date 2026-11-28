"""Salle 3 « Le bivouac » (1805-1821) : grades mousse, lieutenant, second (fiche : Les conquêtes et la chute)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "napoleon-republique", "tests", "donnees"))
from fiches import *
from schemas import carte_europe

FICHE = "« Les conquêtes et la chute »"
CASES5 = ["Paris", "Austerlitz", "Moscou", "Iéna", "Waterloo"]


def _cases(n):
    return [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(CASES5[:n])]


def donnees(svg, bloc=None):
    d = {}
    d["e3-1"] = {
        "mousse": {"type": "plan", "titre": "La carte de Jeanne", "colonnes": 3, "cases": _cases(3), "etiquettes": CASES5[:3],
                   "consigne": "Place chaque nom sur son repère." + carte_europe(3),
                   "indices": ["Ouvre la fiche " + FICHE + ".", "Paris est en France, à l'ouest.", "Moscou est tout à l'est."]},
        "lieutenant": {"type": "plan", "titre": "La carte de Jeanne", "colonnes": 2, "cases": _cases(5), "etiquettes": CASES5 + ["Londres", "Rome"],
                       "consigne": "Place chaque nom sur son repère (deux sont en trop), puis choisis la phrase de la fiche qui dit où et contre qui Napoléon est battu pour la dernière fois." + carte_europe(5),
                       "indices": ["Waterloo est en Belgique, près de la France.", "Iéna est en Allemagne.", "Pour la justification : cherche « Belgique »."],
                       "justification": J("Quelle phrase de la fiche dit où Napoléon est battu pour la dernière fois ?", C_WATERLOO, [C_ABDIC, C_AUSTER, C_HELENE], pos=2)},
        "second": {"type": "plan", "titre": "La carte de Jeanne", "colonnes": 2, "cases": _cases(5), "etiquettes": CASES5 + ["Londres", "Rome", "Sainte-Hélène"],
                   "consigne": "Place chaque nom sur son repère (trois sont en trop), puis choisis la phrase de la fiche qui décrit l'étendue de l'Empire vers 1811." + carte_europe(5),
                   "indices": ["Sainte-Hélène est hors de la carte, très loin au sud.", "Austerlitz est en Europe centrale.", "Pour la justification : cherche « 1811 »."],
                   "justification": J("Quelle phrase de la fiche décrit l'étendue de l'Empire vers 1811 ?", C_GRAND, [C_ARMEE, C_RUSSIE, C_WAGRAM], pos=0)},
    }
    d["e3-2"] = {
        "mousse": ordre(
            "Remets les pages du carnet de Jeanne dans l'ordre.",
            [("la victoire d'Austerlitz", "1805"), ("la campagne de Russie", "1812"), ("la défaite de Waterloo", "1815")],
            ["Ouvre la fiche " + FICHE + ".", "La plus petite année d'abord.", "Waterloo est la fin."]),
        "lieutenant": ordre(
            "Remets les victoires et les défaites dans l'ordre, puis choisis la phrase de la fiche qui date la victoire d'Austerlitz.",
            [("Austerlitz", "2 décembre 1805"), ("Iéna", "14 octobre 1806"), ("Wagram", "juillet 1809"), ("l'entrée dans Moscou", "septembre 1812"), ("Waterloo", "18 juin 1815")],
            ["Trois victoires avant la Russie.", "Waterloo est la dernière.", "Pour la justification : cherche « jour pour jour »."],
            J("Quelle phrase de la fiche date la victoire d'Austerlitz ?", C_AUSTER, [C_IENA, C_WAGRAM, C_WATERLOO], pos=1)),
        "second": ordre(
            "Remets dans l'ordre les étapes de la chute de l'Empereur, puis choisis la phrase de la fiche qui décrit son retour de 1815.",
            [("l'incendie de Moscou", "septembre 1812"), ("la première abdication", "avril 1814"), ("l'exil sur l'île d'Elbe", "1814"),
             ("le retour en France", "mars 1815"), ("la défaite de Waterloo", "18 juin 1815"), ("la mort à Sainte-Hélène", "5 mai 1821")],
            ["Elbe d'abord, Sainte-Hélène ensuite.", "Le retour précède Waterloo.", "Pour la justification : cherche « cent jours »."],
            J("Quelle phrase de la fiche décrit le retour de Napoléon en 1815 ?", C_CENTJ, [C_ABDIC, C_WATERLOO, C_HELENE], pos=3)),
    }
    d["e3-3"] = {
        "mousse": qcm(
            "Aide Jeanne à répondre aux jeunes soldats.",
            [("Comment s'appelle l'armée de Napoléon ?", ["la Grande Armée", "l'armée des rois", "la flotte anglaise"], 0, "Elle réunit des soldats de toute l'Europe."),
             ("Qu'est-ce qui tue beaucoup de soldats en Russie ?", ["le froid et la faim", "la chaleur", "la mer"], 0, "L'hiver russe est terrible."),
             ("Où meurt Napoléon ?", ["à Paris", "sur l'île de Sainte-Hélène", "à Moscou"], 1, "Une île de l'Atlantique.")],
            ["Ouvre la fiche " + FICHE + ".", "L'hiver en Russie est glacial.", "Sainte-Hélène est une île."]),
        "lieutenant": qcm(
            "Fais le bilan avec Jeanne, puis choisis la phrase de la fiche qui décrit le désastre de la retraite de Russie.",
            [("D'où viennent les soldats de la Grande Armée ?", ["seulement de Paris", "de France et des pays alliés ou conquis", "d'Amérique", "de Russie"], 1, "Beaucoup sont étrangers."),
             ("Où Napoléon est-il exilé en 1814 ?", ["sur l'île d'Elbe", "à Sainte-Hélène", "en Égypte", "à Londres"], 0, "En Méditerranée."),
             ("Qui bat Napoléon à Waterloo ?", ["les Espagnols", "les Britanniques et les Prussiens", "les Autrichiens seuls", "les Égyptiens"], 1, "Le 18 juin 1815."),
             ("Quand meurt-il ?", ["en 1815", "en 1821", "en 1840", "en 1804"], 1, "Le 5 mai 1821.")],
            ["Elbe en 1814, Sainte-Hélène en 1815.", "Waterloo est en Belgique.", "Pour la justification : cherche « retraite »."],
            J("Quelle phrase de la fiche décrit le désastre de la retraite de Russie ?", C_RETRAITE, [C_RUSSIE, C_MORTS, C_ARMEE], pos=2)),
        "second": qcm(
            "Jeanne réfléchit au prix des conquêtes. Réponds, puis choisis la phrase de la fiche qui donne le bilan humain des guerres.",
            [("Pourquoi les pays d'Europe s'unissent-ils contre Napoléon ?", ["pour arrêter ses conquêtes", "pour le couronner", "pour visiter Paris", "pour fêter Austerlitz"], 0, "Ils refusent sa domination."),
             ("Que trouve la Grande Armée en entrant dans Moscou ?", ["une ville en fête", "une ville incendiée", "une ville pleine de vivres", "le tsar qui l'attend"], 1, "La ville est incendiée."),
             ("Qui dirige certains pays dominés par l'Empire ?", ["des frères de Napoléon", "le pape", "des maires élus", "Marianne"], 0, "Ou des alliés de l'Empereur."),
             ("Pourquoi peut-on dire que les conquêtes ont coûté très cher ?", ["à cause des centaines de milliers de morts", "parce que les cartes sont chères", "parce que l'armée achète des tableaux", "elles n'ont rien coûté"], 0, "En France et dans toute l'Europe.")],
            ["L'Europe se coalise contre l'Empire.", "Moscou brûle.", "Pour la justification : cherche « centaines de milliers »."],
            J("Quelle phrase de la fiche donne le bilan humain des guerres de l'Empire ?", C_MORTS, [C_RETRAITE, C_GRAND, C_WATERLOO], pos=1)),
    }
    d["e3-4"] = {
        "lieutenant": code(
            "Ouvre le cadenas de la malle : le jour et l'année de la dernière bataille, puis l'année de la mort de l'Empereur. Choisis ensuite la phrase de la fiche qui parle de son dernier exil.",
            [("Jour de Waterloo", "18", 2, True), ("Année de Waterloo", "1815", 4, True), ("Année de sa mort", "1821", 4, True)],
            ["La dernière bataille est Waterloo, en juin.", "Il meurt six ans après Waterloo.", "Pour la justification : cherche « Atlantique »."],
            J("Quelle phrase de la fiche parle du dernier exil de Napoléon ?", C_HELENE, [C_ABDIC, C_WATERLOO, C_CENTJ], pos=0)),
        "second": code(
            "Le cadenas de la malle demande trois nombres : le nombre d'années entre le sacre (1804) et Waterloo, le jour de Waterloo, puis le nombre d'années passées par l'Empereur à Sainte-Hélène (de 1815 à 1821). Choisis ensuite la phrase de la fiche sur sa première abdication.",
            [("Années de 1804 à 1815", "11", 2, True), ("Jour de Waterloo", "18", 2, True), ("Années à Sainte-Hélène", "6", 1, True)],
            ["1815 - 1804.", "Waterloo : le 18 juin.", "Pour la justification : cherche « île d'Elbe »."],
            J("Quelle phrase de la fiche parle de la première abdication de Napoléon ?", C_ABDIC, [C_HELENE, C_CENTJ, C_RUSSIE], pos=3)),
    }
    return d
