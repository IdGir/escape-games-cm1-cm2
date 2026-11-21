"""Message 2 « La gare » (juin 1940) : grades mousse, lieutenant, second (fiche : 1939-1940, la guerre, la défaite et Vichy)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "seconde-guerre", "tests", "donnees"))
from fiches import *
from schemas import carte_1940

FICHE = "« 1939-1940 : la guerre, la défaite et Vichy »"
CASES5 = ["la zone occupée", "la zone non occupée", "la ligne de démarcation", "Paris", "Vichy"]


def _cases(n):
    return [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(CASES5[:n])]


def donnees(svg, bloc=None):
    d = {}
    d["e2-1"] = {
        "mousse": vf(
            "Les familles parlent sur le quai. Pour chaque phrase, choisis vrai ou faux.",
            [("Beaucoup de familles fuient sur les routes.", True, "C'est l'exode."),
             ("L'armée française gagne en 1940.", False, "Elle est battue."),
             ("La guerre a commencé en 1939.", True, "En septembre 1939.")],
            ["Ouvre la fiche " + FICHE + ".", "Fuir : partir très vite.", "1939 : le début de la guerre."]),
        "lieutenant": vf(
            "Paul trie les nouvelles et les rumeurs. Choisis vrai ou faux, puis la phrase de la fiche qui décrit la fuite des Français.",
            [("Le 1er septembre 1939, l'armée allemande envahit la Pologne.", True, "La guerre commence."),
             ("Pendant la « drôle de guerre », il y a peu de combats à l'ouest.", True, "Pendant huit mois."),
             ("L'attaque allemande à l'ouest commence le 10 mai 1940.", True, "La défaite suit en six semaines."),
             ("L'armée française résiste pendant quatre ans en 1940.", False, "Elle est battue en six semaines."),
             ("L'armée allemande entre dans Paris le 14 juillet 1940.", False, "Le 14 juin 1940.")],
            ["Huit mois de « drôle de guerre ».", "Six semaines de combats.", "Pour la justification : cherche « exode »."],
            J("Quelle phrase de la fiche décrit la fuite de millions de Français ?", D_EXODE, [D_ATTAQUE, D_DROLE, D_PARIS], pos=0)),
        "second": vf(
            "Paul compare ce qu'il entend avec ce qu'il a vu. Choisis vrai ou faux, puis la phrase de la fiche qui date l'entrée en guerre de la France.",
            [("La France entre en guerre deux jours après l'invasion de la Pologne.", True, "Le 3 septembre 1939."),
             ("La « drôle de guerre » dure environ huit mois.", True, "De septembre 1939 à mai 1940."),
             ("Entre le 10 mai et le 22 juin 1940, il s'écoule environ six semaines.", True, "La défaite est très rapide."),
             ("Paris est occupé avant que Pétain demande l'arrêt des combats.", True, "Le 14 juin, puis le 17 juin."),
             ("L'exode a lieu après la Libération.", False, "En mai et juin 1940.")],
            ["Pologne : 1er septembre ; France : 3 septembre.", "Compte les mois de septembre à mai.", "Pour la justification : cherche « Pologne »."],
            J("Quelle phrase de la fiche date l'entrée en guerre de la France ?", D_DECLA, [D_DROLE, D_ATTAQUE, D_ARMISTICE], pos=2)),
    }
    d["e2-2"] = {
        "mousse": ordre(
            "Remets les nouvelles de la radio dans l'ordre.",
            [("Pétain dit qu'il faut arrêter de combattre", "17 juin"), ("de Gaulle dit de continuer le combat", "18 juin"), ("l'armistice est signé", "22 juin")],
            ["Ouvre la fiche " + FICHE + ".", "Regarde les jours : 17, 18, 22.", "Pétain parle le premier."]),
        "lieutenant": ordre(
            "Remets les nouvelles de juin et juillet 1940 dans l'ordre, puis choisis la phrase de la fiche qui décrit l'appel du général de Gaulle.",
            [("l'armée allemande entre dans Paris", "14 juin 1940"), ("Pétain annonce qu'il faut cesser le combat", "17 juin 1940"),
             ("de Gaulle lance l'appel du 18 Juin", "18 juin 1940"), ("l'armistice est signé à Rethondes", "22 juin 1940"), ("Pétain reçoit les pleins pouvoirs", "10 juillet 1940")],
            ["Paris d'abord.", "Juillet vient après juin.", "Pour la justification : cherche « BBC »."],
            J("Quelle phrase de la fiche décrit l'appel du général de Gaulle ?", D_APPEL, [D_PETAIN, D_ARMISTICE, D_VICHY], pos=3)),
        "second": ordre(
            "Remets dans l'ordre les étapes qui mènent de la défaite à la collaboration, puis choisis la phrase de la fiche qui explique la fin de la République.",
            [("l'attaque allemande à l'ouest", "10 mai 1940"), ("Pétain demande l'arrêt des combats", "17 juin 1940"), ("l'armistice coupe la France en deux", "22 juin 1940"),
             ("la République est remplacée par l'État français", "10 juillet 1940"), ("Pétain rencontre Hitler à Montoire", "octobre 1940")],
            ["L'attaque vient d'abord.", "Montoire est en automne.", "Pour la justification : cherche « pleins pouvoirs »."],
            J("Quelle phrase de la fiche explique comment la République disparaît ?", D_VICHY, [D_DICTA, D_COLLAB, D_ARMISTICE], pos=1)),
    }
    d["e2-3"] = {
        "mousse": {"type": "plan", "titre": "La France coupée en deux", "colonnes": 3, "cases": _cases(3), "etiquettes": CASES5[:3],
                   "consigne": "Place chaque mot sur son repère." + carte_1940(3),
                   "indices": ["Ouvre la fiche " + FICHE + ".", "La zone occupée est en gris.", "La ligne est en pointillés rouges."]},
        "lieutenant": {"type": "plan", "titre": "La France coupée en deux", "colonnes": 2, "cases": _cases(5), "etiquettes": CASES5 + ["Londres", "Berlin"],
                       "consigne": "Place chaque mot sur son repère (deux sont en trop), puis choisis la phrase de la fiche qui décrit la France coupée en deux." + carte_1940(5),
                       "indices": ["Paris est en zone occupée.", "Vichy est au sud de la ligne.", "Pour la justification : cherche « ligne de démarcation »."],
                       "justification": J("Quelle phrase de la fiche décrit la France coupée en deux ?", D_ARMISTICE, [D_VICHY, D_PARIS, D_EXODE], pos=0)},
        "second": {"type": "plan", "titre": "La France coupée en deux", "colonnes": 2, "cases": _cases(5), "etiquettes": CASES5 + ["Londres", "Rethondes", "Montoire"],
                   "consigne": "Place chaque mot sur son repère (trois sont en trop), puis choisis la phrase de la fiche qui décrit le régime installé à Vichy." + carte_1940(5),
                   "indices": ["Rethondes et Montoire ne sont pas des repères de cette carte.", "Vichy est une ville d'eaux du centre de la France.", "Pour la justification : cherche « Travail, Famille, Patrie »."],
                   "justification": J("Quelle phrase de la fiche décrit le régime installé à Vichy ?", D_DICTA, [D_ARMISTICE, D_COLLAB, D_APPEL], pos=2)},
    }
    d["e2-4"] = {
        "lieutenant": trous(
            "Complète le carnet de Paul, puis choisis la phrase de la fiche qui définit la collaboration.",
            "Le 17 juin, le maréchal [[Pétain]] demande l'arrêt des combats ; il gouverne depuis [[Vichy]]. Le 18 juin, depuis [[Londres]], le général [[de Gaulle]] appelle à continuer le combat. En octobre 1940, à Montoire, Pétain choisit la [[collaboration]].",
            ["Pétain", "Vichy", "Londres", "de Gaulle", "collaboration", "Berlin", "résistance"],
            ["Pétain reste en France.", "De Gaulle est au Royaume-Uni.", "Pour la justification : cherche « Montoire »."],
            J("Quelle phrase de la fiche définit la collaboration ?", D_COLLAB, [D_DICTA, D_PETAIN, D_VICHY], pos=1)),
        "second": trous(
            "Complète le carnet de Paul, qui compare les deux voix de juin 1940, puis choisis la phrase de la fiche sur l'annonce de Pétain.",
            "Le [[17]] juin 1940, Pétain annonce à la [[radio]] qu'il faut cesser le combat. Le lendemain, de Gaulle parle sur la [[BBC]]. L'[[armistice]] est signé le 22 juin à [[Rethondes]]. Le 10 juillet, la [[République]] est remplacée par l'État français.",
            ["17", "radio", "BBC", "armistice", "Rethondes", "République", "18", "paix", "Montoire"],
            ["Pétain parle la veille de l'appel.", "L'armistice n'est pas la paix.", "Pour la justification : cherche « nouveau chef du gouvernement »."],
            J("Quelle phrase de la fiche décrit l'annonce de Pétain ?", D_PETAIN, [D_APPEL, D_ARMISTICE, D_ATTAQUE], pos=3)),
    }
    return d
