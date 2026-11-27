"""Séance 13 « L eau en France : fleuves et massifs » : grades mousse, lieutenant, second (fiche : Les principaux fleuves et massifs de France)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "mission-geo", "tests", "donnees"))
from fiches import *
import schemas as S

FICHE = "« Les principaux fleuves et massifs de France »"


def cases(idx):
    return [{"libelle": f"Repère {i + 1}", "reponse": S.FLEUVES[k][0]} for i, k in enumerate(idx)]


def donnees(svg, bloc=None):
    d = {}
    d["e13-1"] = {
        "mousse": {"type": "plan", "titre": "La carte de Rémi", "colonnes": 3, "cases": cases([0, 3, 5]), "etiquettes": [S.FLEUVES[k][0] for k in (0, 3, 5)],
                   "consigne": "Place chaque nom sur son repère." + S.fleuves([0, 3, 5]),
                   "indices": ["Ouvre la fiche " + FICHE + ".", "La Seine traverse Paris, au nord.", "Les Alpes sont à l'est, près de l'Italie."]},
        "lieutenant": assoc(
            "Rémi te décrit les massifs. Relie chaque massif à ce qui le caractérise, puis choisis la phrase de la fiche qui les nomme tous.",
            [("les Alpes", "les plus hautes montagnes de France"), ("les Pyrénées", "la frontière avec l'Espagne"), ("le Massif central", "d'anciens volcans"),
             ("le Jura", "la frontière avec la Suisse"), ("les Vosges", "des sommets arrondis, à l'est")],
            ["Le mont Blanc est dans les Alpes.", "Le Massif central est formé d'anciens volcans.", "Pour la justification : cherche « six grands massifs »."],
            J("Quelle phrase de la fiche nomme les six grands massifs ?", F_SIX, [F_ALPES, F_PYRENEES, F_NEIGE], pos=2)),
        "second": {"type": "plan", "titre": "La carte de Rémi", "colonnes": 2, "cases": cases(range(8)),
                   "etiquettes": [S.FLEUVES[k][0] for k in range(8)] + ["La Dordogne"],
                   "consigne": "Place les cinq fleuves et trois massifs sur leur repère (une étiquette est en trop), puis choisis la phrase de la fiche qui cite les cinq fleuves." + S.fleuves(range(8)),
                   "indices": ["La Dordogne n'est pas un des cinq grands fleuves.", "Le Massif central est au centre du pays.", "Pour la justification : cherche « cinq principaux fleuves »."],
                   "justification": J("Quelle phrase de la fiche cite les cinq principaux fleuves ?", F_CINQ, [F_SEINE, F_RHIN, F_GARONNE], pos=2)},
    }
    d["e13-2"] = {
        "mousse": qcm(
            "Rémi te pose deux questions.",
            [("Combien de grands massifs montagneux compte la France ?", ["six", "trois", "douze"], 0, "Alpes, Pyrénées, Massif central, Jura, Vosges et Corse."),
             ("Un fleuve se jette dans…", ["la mer ou l'océan", "un autre cours d'eau", "une montagne"], 0, "Une rivière, elle, se jette dans un autre cours d'eau.")],
            ["Ouvre la fiche " + FICHE + ".", "Compte les massifs sur la carte.", "Un fleuve finit sa course dans la mer."]),
        "lieutenant": tri(
            "Rémi te demande de distinguer fleuves et rivières. Range chaque cours d'eau, puis choisis la phrase de la fiche qui les distingue.",
            [("fl", "Un fleuve (se jette dans la mer ou l'océan)"), ("ri", "Une rivière (se jette dans un autre cours d'eau)")],
            [("la Seine", "fl"), ("la Loire", "fl"), ("la Garonne", "fl"), ("le Rhône", "fl"), ("la Marne (affluent de la Seine)", "ri"), ("l'Allier (affluent de la Loire)", "ri"),
             ("la Saône (affluent du Rhône)", "ri"), ("l'Oise (affluent de la Seine)", "ri")],
            ["Un affluent se jette dans un autre cours d'eau.", "Les cinq grands fleuves se jettent dans une mer ou dans l'océan.", "Pour la justification : cherche « une rivière se jette »."],
            J("Quelle phrase de la fiche distingue un fleuve d'une rivière ?", F_FLEUVE, [F_CINQ, F_NEIGE, F_SIX], pos=1)),
        "second": vf(
            "Rémi t'envoie des affirmations à vérifier. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur le rôle de la neige.",
            [("Une rivière se jette dans la mer.", False, "Une rivière se jette dans un autre cours d'eau."),
             ("La Garonne descend des Pyrénées.", True, "Elle se jette dans l'océan Atlantique par l'estuaire de la Gironde."),
             ("Le Rhône vient de Suisse.", True, "Il se jette dans la mer Méditerranée."),
             ("Le Massif central est formé d'anciens volcans.", True, "Il se trouve au centre du pays."),
             ("La Seine est le plus long fleuve de France.", False, "C'est la Loire, avec environ 1 006 km.")],
            ["Un fleuve se jette dans la mer ou l'océan.", "La Loire est plus longue que la Seine.", "Pour la justification : cherche « en fondant au printemps »."],
            J("Quelle phrase de la fiche explique le rôle de la neige ?", F_NEIGE, [F_FLEUVE, F_VOLCANS, F_SEINE], pos=1)),
    }
    d["e13-3"] = {
        "mousse": assoc(
            "Relie chaque fleuve à la mer dans laquelle il se jette.",
            [("La Seine", "La Manche"), ("Le Rhône", "La mer Méditerranée"), ("Le Rhin", "La mer du Nord")],
            ["Ouvre la fiche " + FICHE + ".", "Le Rhône descend vers le sud.", "Le Rhin longe l'Allemagne."]),
        "lieutenant": ordre(
            "Range les cinq fleuves du nord au sud, d'après l'endroit où ils se jettent, puis choisis la phrase de la fiche qui les cite.",
            ["le Rhin (mer du Nord)", "la Seine (Manche)", "la Loire (océan Atlantique)", "la Garonne (estuaire de la Gironde)", "le Rhône (mer Méditerranée)"],
            ["La mer du Nord est au nord, la Méditerranée au sud.", "La Loire se jette plus au nord que la Gironde.", "Pour la justification : cherche « cinq principaux fleuves »."],
            J("Quelle phrase de la fiche cite les cinq principaux fleuves ?", F_CINQ, [F_SEINE, F_RHIN, F_GARONNE], pos=2)),
        "second": qcm(
            "Rémi veut vérifier ta lecture de la carte. Réponds, puis choisis la phrase de la fiche sur le Jura.",
            [("Qu'est-ce qui alimente les fleuves au printemps ?", ["la neige qui fond en montagne", "les glaces de l'océan", "les canaux", "le vent"], 0, "Les montagnes retiennent la neige."),
             ("Quel fleuve longe la frontière avec l'Allemagne ?", ["le Rhin", "la Loire", "la Garonne", "le Rhône"], 0, "Il se jette dans la mer du Nord."),
             ("Quel massif longe la frontière avec la Suisse ?", ["le Jura", "les Pyrénées", "le Massif central", "les Vosges"], 0, "Les Vosges se trouvent à l'est, avec des sommets arrondis.")],
            ["La neige fond au printemps.", "Le Rhin est à l'est de la France.", "Pour la justification : cherche « la frontière avec la Suisse »."],
            J("Quelle phrase de la fiche parle du Jura ?", F_JURA, [F_PYRENEES, F_VOLCANS, F_ALPES], pos=0)),
    }
    d["e13-4"] = {
        "lieutenant": code(
            "Rémi te rappelle quelques repères. Réponds, puis choisis la phrase de la fiche sur les Alpes.",
            [("Nombre de grands massifs montagneux", "6", 1), ("Nombre de grands fleuves", "5", 1), ("Altitude du mont Blanc, en mètres (arrondie)", "4807", 4)],
            ["Alpes, Pyrénées, Massif central, Jura, Vosges, Corse.", "Seine, Loire, Garonne, Rhône, Rhin.", "Le mont Blanc culmine à environ 4 800 mètres. Pour la justification : cherche « les plus hautes »."],
            J("Quelle phrase de la fiche parle des Alpes ?", F_ALPES, [F_SIX, F_PYRENEES, F_VOLCANS], pos=3)),
        "second": code(
            "Rémi pousse la réflexion plus loin. Réponds, puis choisis la phrase de la fiche sur la Loire.",
            [("Longueur de la Loire (kilomètres, arrondie)", "1006", 4), ("Le mont Blanc dépasse 4 000 m de combien de mètres ? (arrondi)", "807", 3), ("Nombre de fleuves + nombre de massifs", "11", 2)],
            ["La Loire est le plus long fleuve de France.", "4 807 − 4 000.", "5 + 6. Pour la justification : cherche « plus long fleuve »."],
            J("Quelle phrase de la fiche parle de la Loire ?", F_LOIRE, [F_SEINE, F_GARONNE, F_RHONE], pos=2)),
    }
    return d
