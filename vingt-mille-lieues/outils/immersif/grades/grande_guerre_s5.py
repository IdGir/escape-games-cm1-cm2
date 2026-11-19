"""Lettre 5 « Le monument aux morts » (11 novembre 1922) : grades mousse, lieutenant, second (fiche : Se souvenir, et une paix fragile)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "grande-guerre", "tests", "donnees"))
from fiches import *
from schemas import monument

FICHE = "« Se souvenir, et une paix fragile »"
CASES5 = ["la statue du poilu", "la liste des noms", "les dates de la guerre", "la croix de guerre", "la gerbe de fleurs"]
REG = tableau("Le registre de la mairie (soldats inventés)", ["N°", "Nom", "Né en", "Mort pour la France en", "Lieu"],
              [["1", "Paul Bernard", "1894", "1914", "la Marne"], ["2", "Henri Colin", "1890", "1915", "l'Artois"],
               ["3", "Lucien Dubois", "1896", "1916", "Verdun"], ["4", "Marcel Fabre", "1897", "1916", "la Somme"],
               ["5", "Joseph Garnier", "1888", "1917", "le Chemin des Dames"], ["6", "René Masson", "1899", "1918", "la Champagne"],
               ["7", "Albert Petit", "1885", "1918", "l'Aisne"]])


def _cases(n):
    return [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(CASES5[:n])]


def donnees(svg, bloc=None):
    d = {}
    d["e5-1"] = {
        "mousse": {"type": "plan", "titre": "Le monument du village", "colonnes": 3, "cases": _cases(3), "etiquettes": CASES5[:3],
                   "consigne": "Place chaque mot sur son repère." + monument(3),
                   "indices": ["Ouvre la fiche " + FICHE + ".", "La statue est tout en haut.", "Les noms sont gravés sur la pierre."]},
        "lieutenant": {"type": "plan", "titre": "Le monument du village", "colonnes": 2, "cases": _cases(5),
                       "etiquettes": CASES5 + ["les barbelés", "l'affiche de mobilisation"],
                       "consigne": "Place chaque mot sur son repère (deux sont en trop), puis choisis la phrase de la fiche qui dit ce que l'on grave sur le monument." + monument(5),
                       "indices": ["La croix de guerre est une décoration.", "La gerbe est posée au pied du monument.", "Pour la justification : cherche « gravés »."],
                       "justification": J("Quelle phrase de la fiche dit ce que l'on grave sur le monument ?", M_NOMS, [M_MONUMENT, M_11NOV, M_BASE], pos=1)},
        "second": {"type": "plan", "titre": "Le monument du village", "colonnes": 2, "cases": _cases(5),
                   "etiquettes": CASES5 + ["les barbelés", "l'affiche de mobilisation", "le Soldat inconnu"],
                   "consigne": "Place chaque mot sur son repère (trois sont en trop), puis choisis la phrase de la fiche qui dit quand on construit les monuments." + monument(5),
                   "indices": ["Le Soldat inconnu repose à Paris, pas au village.", "Les dates sont au-dessus des noms.", "Pour la justification : cherche « années 1920 »."],
                   "justification": J("Quelle phrase de la fiche dit quand les communes construisent leur monument ?", M_MONUMENT, [M_NOMS, M_INCONNU, M_2012], pos=0)},
    }
    d["e5-2"] = {
        "mousse": vf(
            "Le maire parle aux enfants. Pour chaque phrase, choisis vrai ou faux.",
            [("Sur le monument, on grave les noms des soldats morts.", True, "Pour se souvenir d'eux."),
             ("Le 11 novembre, on se rassemble devant le monument.", True, "C'est un jour de souvenir."),
             ("Le monument sert à fêter la guerre.", False, "Il sert à se souvenir.")],
            ["Ouvre la fiche " + FICHE + ".", "Un monument aux morts garde les noms.", "On ne fête pas la guerre."]),
        "lieutenant": vf(
            "Le maire prépare son discours. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur le Soldat inconnu.",
            [("Le 11 novembre est un jour férié depuis la loi du 24 octobre 1922.", True, "On se rassemble devant le monument."),
             ("Le Soldat inconnu représente tous les morts de la guerre.", True, "Il repose sous l'Arc de Triomphe."),
             ("On connaît le nom du Soldat inconnu.", False, "Justement, il est inconnu : il représente tous les morts."),
             ("Depuis 2012, le 11 novembre honore tous les morts pour la France, de toutes les guerres.", True, "Pas seulement ceux de 1914-1918."),
             ("Presque aucune commune n'a de monument aux morts.", False, "Presque chaque commune en a un.")],
            ["Inconnu : on ne sait pas son nom.", "La loi de 1922.", "Pour la justification : cherche « Arc de Triomphe »."],
            J("Quelle phrase de la fiche parle du Soldat inconnu ?", M_INCONNU, [M_11NOV, M_2012, M_NOMS], pos=2)),
        "second": tri(
            "Le maire s'inquiète pour l'avenir. Range chaque fait : pour se souvenir, ou conséquence qui rend la paix fragile. Puis choisis la phrase de la fiche sur la montée des extrêmes.",
            [("souvenir", "Se souvenir"), ("fragile", "Une paix fragile")],
            [("le monument aux morts de la commune", "souvenir"), ("la cérémonie du 11 novembre", "souvenir"), ("le Soldat inconnu à l'Arc de Triomphe", "souvenir"),
             ("la colère des pays vaincus", "fragile"), ("Mussolini au pouvoir en Italie en 1922", "fragile"), ("la grave crise économique de 1929", "fragile")],
            ["Les cérémonies servent à se souvenir.", "La colère et la crise profitent aux extrémistes.", "Pour la justification : cherche « Mussolini »."],
            J("Quelle phrase de la fiche décrit la montée des extrêmes ?", M_EXTREMES, [M_CONSEQ, M_CRISE, M_SUITE], pos=1)),
    }
    d["e5-3"] = {
        "mousse": qcm(
            "Lis le registre du maire, puis réponds." + REG,
            [("Combien de noms y a-t-il ?", ["5", "7", "10"], 1, "Sept soldats du village."),
             ("En quelle année Paul Bernard est-il mort ?", ["1914", "1916", "1918"], 0, "La première année de la guerre.")],
            ["Ouvre la fiche " + FICHE + ".", "Compte les lignes.", "Regarde la ligne de Paul Bernard."]),
        "lieutenant": qcm(
            "Mène l'enquête dans le registre, puis choisis la phrase de la fiche qui explique comment retrouver un vrai soldat." + REG,
            [("Qui était le plus jeune au moment de sa mort ?", ["Paul Bernard", "René Masson", "Lucien Dubois", "Marcel Fabre"], 1, "1918 − 1899 : environ 19 ans."),
             ("Combien de soldats du registre sont morts en 1916 ?", ["1", "2", "3", "4"], 1, "À Verdun et dans la Somme."),
             ("Quel soldat est mort pendant la bataille commencée le 1er juillet 1916 ?", ["Lucien Dubois", "Marcel Fabre", "Henri Colin", "Albert Petit"], 1, "La Somme."),
             ("Les noms de ce registre sont inventés. Où chercher un vrai soldat mort pour la France ?", ["dans la base Mémoire des hommes", "dans un dictionnaire", "dans un roman", "nulle part"], 0, "Base du ministère des Armées.")],
            ["Année de la mort moins année de naissance.", "La Somme commence en juillet 1916.", "Pour la justification : cherche « Mémoire des hommes »."],
            J("Quelle phrase de la fiche explique comment retrouver un vrai soldat ?", M_BASE, [M_NOMS, M_MONUMENT, M_DEUIL], pos=0)),
        "second": qcm(
            "Mène l'enquête et calcule, puis choisis la phrase de la fiche sur les familles." + REG,
            [("Qui était le plus âgé au moment de sa mort ?", ["Joseph Garnier", "Albert Petit", "Henri Colin", "Paul Bernard"], 1, "1918 − 1885 : environ 33 ans."),
             ("Quel est l'écart d'âge entre le plus âgé et le plus jeune à leur mort ?", ["environ 4 ans", "environ 14 ans", "environ 24 ans", "environ 34 ans"], 1, "33 − 19 = 14."),
             ("En quelle année le registre compte-t-il autant de morts qu'en 1916 ?", ["1914", "1915", "1917", "1918"], 3, "Deux en 1916, deux en 1918."),
             ("Joseph Garnier porte le nom de Louis et de Jeanne. Que suggère cet indice à un historien ?", ["qu'il appartient peut-être à leur famille, à vérifier dans les archives", "qu'il est forcément leur père", "rien du tout", "qu'il est vivant"], 0, "Un même nom est une piste, pas une preuve.")],
            ["Le plus âgé est né le plus tôt.", "Compte les morts par année.", "Pour la justification : cherche « deuil »."],
            J("Quelle phrase de la fiche parle du deuil des familles ?", M_DEUIL, [M_CONSEQ, M_NOMS, M_BASE], pos=3)),
    }
    d["e5-4"] = {
        "lieutenant": code(
            "La dernière lettre est fermée par un cadenas à date. Jeanne a écrit : « Le même jour et le même mois que l'armistice, l'année où le 11 novembre est devenu un jour férié. » Trouve le jour, le mois (en chiffres) et l'année, puis choisis la phrase de la fiche qui donne l'année.",
            [("Jour", "11", 2, True), ("Mois", "11", 2, True), ("Année", "1922", 4, True)],
            ["L'armistice : le 11 novembre.", "Novembre est le onzième mois.", "Pour la justification : cherche « 24 octobre »."],
            J("Quelle phrase de la fiche donne l'année où le 11 novembre devient un jour férié ?", M_11NOV, [M_INCONNU, M_2012, M_MONUMENT], pos=1)),
        "second": code(
            "Le cadenas de la dernière lettre attend une date. Jeanne a écrit : « Le jour est l'heure à laquelle les combats se sont arrêtés. Le mois est celui de l'armistice. L'année est celle où Mussolini a pris le pouvoir en Italie. » Trouve la date, puis choisis la phrase de la fiche qui confirme l'année.",
            [("Jour", "11", 2, True), ("Mois", "11", 2, True), ("Année", "1922", 4, True)],
            ["Les combats s'arrêtent à 11 heures.", "Novembre : onzième mois.", "Pour la justification : cherche « Italie »."],
            J("Quelle phrase de la fiche confirme l'année ?", M_EXTREMES, [M_CRISE, M_SUITE, M_CONSEQ], pos=0)),
    }
    return d
