"""Message 5 « La place de la mairie » (1944-1945) : grades mousse, lieutenant, second (fiche : La Libération et la victoire des Alliés)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "seconde-guerre", "tests", "donnees"))
from fiches import *
from schemas import carte_1944

FICHE = "« La Libération et la victoire des Alliés »"
CASES5 = ["les plages de Normandie", "Paris", "les côtes de Provence", "Dijon", "les forêts du Morvan"]


def _cases(n):
    return [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(CASES5[:n])]


def donnees(svg, bloc=None):
    d = {}
    d["e5-1"] = {
        "mousse": {"type": "plan", "titre": "La carte de Lucie", "colonnes": 3, "cases": _cases(3), "etiquettes": CASES5[:3],
                   "consigne": "Place chaque nom sur son repère." + carte_1944(3),
                   "indices": ["Ouvre la fiche " + FICHE + ".", "La Normandie est face au Royaume-Uni.", "La Provence est au bord de la Méditerranée."]},
        "lieutenant": {"type": "plan", "titre": "La carte de Lucie", "colonnes": 2, "cases": _cases(5), "etiquettes": CASES5 + ["Berlin", "Londres"],
                       "consigne": "Place chaque nom sur son repère (deux sont en trop), puis choisis la phrase de la fiche qui date le débarquement de Provence." + carte_1944(5),
                       "indices": ["Dijon est en Bourgogne.", "Le Morvan est une forêt, près de Dijon.", "Pour la justification : cherche « Provence »."],
                       "justification": J("Quelle phrase de la fiche date le débarquement de Provence ?", L_PROVENCE, [L_DEBARQ, L_PARIS, L_DIJON], pos=2)},
        "second": {"type": "plan", "titre": "La carte de Lucie", "colonnes": 2, "cases": _cases(5), "etiquettes": CASES5 + ["Vichy", "Berlin", "Londres"],
                   "consigne": "Place chaque nom sur son repère (trois sont en trop), puis choisis la phrase de la fiche qui dit quand la Bourgogne est libérée." + carte_1944(5),
                   "indices": ["Vichy n'est pas un lieu de débarquement.", "Les flèches montrent les deux débarquements.", "Pour la justification : cherche « Bourgogne »."],
                   "justification": J("Quelle phrase de la fiche dit quand la Bourgogne est libérée ?", L_DIJON, [L_PARIS, L_PROVENCE, L_GPRF], pos=1)},
    }
    d["e5-2"] = {
        "mousse": ordre(
            "Remets les grandes dates dans l'ordre.",
            [("le débarquement en Normandie", "juin 1944"), ("Paris est libéré", "août 1944"), ("la guerre est finie en Europe", "mai 1945")],
            ["Ouvre la fiche " + FICHE + ".", "1944 avant 1945.", "Juin avant août."]),
        "lieutenant": ordre(
            "Remets les dates de 1944 et 1945 dans l'ordre, puis choisis la phrase de la fiche qui décrit la libération de Paris.",
            [("le débarquement de Normandie", "6 juin 1944"), ("le débarquement de Provence", "15 août 1944"), ("la libération de Paris", "25 août 1944"),
             ("la libération de Dijon", "11 septembre 1944"), ("la capitulation de l'Allemagne nazie", "8 mai 1945")],
            ["Le 15 août avant le 25 août.", "Septembre après août.", "Pour la justification : cherche « Leclerc »."],
            J("Quelle phrase de la fiche décrit la libération de Paris ?", L_PARIS, [L_DEBARQ, L_DIJON, L_8MAI], pos=0)),
        "second": ordre(
            "Remets dans l'ordre ces étapes, du débarquement jusqu'à la paix dans le monde, puis choisis la phrase de la fiche qui date la fin de la guerre dans le monde.",
            [("les vers de Verlaine sur Radio Londres", "début juin 1944"), ("le Jour J en Normandie", "6 juin 1944"), ("Paris est libéré", "25 août 1944"),
             ("l'Allemagne nazie capitule", "8 mai 1945"), ("le Japon capitule", "2 septembre 1945")],
            ["Verlaine annonce le débarquement.", "La guerre finit en Europe avant le monde.", "Pour la justification : cherche « Japon »."],
            J("Quelle phrase de la fiche date la fin de la guerre dans le monde ?", L_JAPON, [L_8MAI, L_BILAN, L_JAMAIS], pos=3)),
    }
    d["e5-3"] = {
        "mousse": intrus(
            "Un drapeau n'est pas celui d'un allié. Trouve l'intrus.",
            [("le Royaume-Uni", False), ("les États-Unis", False), ("l'Italie de Mussolini", True)],
            ["Ouvre la fiche " + FICHE + ".", "Les Alliés combattent Hitler.", "Mussolini était avec Hitler."]),
        "lieutenant": intrus(
            "Lucie prépare la banderole des Alliés. Trouve l'intrus, puis choisis la phrase de la fiche qui nomme les Alliés.",
            [("le Royaume-Uni", False), ("l'Union soviétique", False), ("les États-Unis", False), ("la France libre", False), ("le Japon", True)],
            ["Le Japon combat avec l'Allemagne.", "Les États-Unis entrent en guerre en 1941.", "Pour la justification : cherche « décembre 1941 »."],
            J("Quelle phrase de la fiche nomme les Alliés ?", L_ALLIES, [L_DEBARQ, L_8MAI, L_JAMAIS], pos=1)),
        "second": intrus(
            "Lucie écrit sur des cartes ce qui change en France à la Libération. Une carte est fausse : trouve-la, puis choisis la phrase de la fiche sur le droit de vote.",
            [("la République est rétablie", False), ("les Françaises obtiennent le droit de vote", False), ("de Gaulle dirige le gouvernement provisoire", False),
             ("le régime de Vichy continue", True), ("la France occupée est libérée", False)],
            ["Vichy disparaît avec la Libération.", "Les femmes votent en 1945.", "Pour la justification : cherche « pour la première fois »."],
            J("Quelle phrase de la fiche parle du droit de vote des femmes ?", L_VOTE, [L_GPRF, L_PARIS, L_ALLIES], pos=2)),
    }
    d["e5-4"] = {
        "lieutenant": code(
            "Le poste ne s'allume qu'avec la date de la victoire en Europe : jour, mois en chiffres, année. Choisis ensuite la phrase de la fiche qui la donne.",
            [("Jour", "8", 1, True), ("Mois", "5", 1, True), ("Année", "1945", 4, True)],
            ["Mai est le cinquième mois.", "La guerre finit en Europe en 1945.", "Pour la justification : cherche « capitule »."],
            J("Quelle phrase de la fiche donne la date de la victoire en Europe ?", L_8MAI, [L_JAPON, L_PARIS, L_DEBARQ], pos=0)),
        "second": code(
            "Le cadran a deux réglages. Réglage 1 : le nombre de mois entre le Jour J (juin 1944) et la capitulation de l'Allemagne (mai 1945). Réglage 2 : l'année de création de l'ONU. Choisis ensuite la phrase de la fiche sur le « plus jamais ça ».",
            [("Réglage 1 : nombre de mois", "11", 2, True), ("Réglage 2 : année", "1945", 4, True)],
            ["De juin 1944 à juin 1945 : douze mois ; enlève un mois.", "L'ONU naît l'année de la victoire.", "Pour la justification : cherche « ONU »."],
            J("Quelle phrase de la fiche parle de construire la paix ?", L_JAMAIS, [L_BILAN, L_8MAI, L_JAPON], pos=3)),
    }
    return d
