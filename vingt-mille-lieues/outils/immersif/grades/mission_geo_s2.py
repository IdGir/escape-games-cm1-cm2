"""Séance 2 « Direction Dijon ! » : grades mousse, lieutenant, second (fiche : Des territoires emboîtés)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "mission-geo", "tests", "donnees"))
from fiches import *
import schemas as S

FICHE = "« Des territoires emboîtés »"


def donnees(svg, bloc=None):
    d = {}
    d["e2-1"] = {
        "mousse": tri(
            "Léna te montre trois bâtiments. Range chacun chez celui qui s'en occupe.",
            [("com", "La commune"), ("dep", "Le département"), ("reg", "La région")],
            [("l'école", "com"), ("le collège", "dep"), ("le lycée", "reg")],
            ["Ouvre la fiche " + FICHE + ".", "L'école est la plus proche de chez toi : c'est la commune.", "Le lycée, pour les plus grands : la région."]),
        "lieutenant": ordre(
            "Léna te demande de te présenter comme un agent. Range ces territoires du plus vaste au plus petit, puis choisis la phrase de la fiche qui les emboîte.",
            [("L'Europe", "continent"), ("La France", "pays"), ("La Bourgogne-Franche-Comté", "région"), ("La Côte-d'Or", "département"), ("Dijon", "commune")],
            ["Le continent contient tous les autres.", "Dijon est en Côte-d'Or.", "Pour la justification : cherche « emboîtés »."],
            J("Quelle phrase de la fiche explique comment les territoires s'emboîtent ?", E_EMBOITE, [E_NOMBRES, E_FRANCE, E_DIJON], pos=1)),
        "second": qcm(
            "Léna vérifie que tu sais lire les numéros et les nombres du territoire. Réponds, puis choisis la phrase de la fiche sur les numéros des départements.",
            [("Le département numéro 21 est…", ["la Côte-d'Or", "le Doubs", "la Nièvre", "le Jura"], 0, "Dijon en est la préfecture."),
             ("Avec l'outre-mer, combien la France compte-t-elle de départements ?", ["101", "96", "13", "18"], 0, "96 en métropole et 5 en outre-mer."),
             ("Avec l'outre-mer, combien la France compte-t-elle de régions ?", ["18", "13", "22", "101"], 0, "13 en métropole et 5 en outre-mer."),
             ("Quel est le numéro de l'Ain ?", ["01", "21", "75", "10"], 0, "C'est le premier.")],
            ["Le numéro de la Côte-d'Or est écrit dans la fiche.", "96 + 5 = 101.", "Pour la justification : cherche « 01 pour l'Ain »."],
            J("Quelle phrase de la fiche parle des numéros des départements ?", E_NUMERO, [E_NOMBRES, E_EMBOITE, E_DIJON], pos=2)),
    }
    d["e2-2"] = {
        "mousse": {"type": "plan", "titre": "Le planisphère de Léna", "colonnes": 3,
                   "cases": [{"libelle": "Repère 1", "reponse": "l'Europe"}, {"libelle": "Repère 2", "reponse": "l'Afrique"}, {"libelle": "Repère 3", "reponse": "l'Asie"}],
                   "etiquettes": ["l'Europe", "l'Afrique", "l'Asie"],
                   "consigne": "Place chaque continent sur son repère." + S.planisphere([2, 3, 4]),
                   "indices": ["Ouvre la fiche " + FICHE + ".", "La France est en Europe, en haut au milieu.", "L'Asie est le plus grand continent, à droite."]},
        "lieutenant": {"type": "plan", "titre": "Les régions de France métropolitaine", "colonnes": 3,
                       "cases": [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(S.REGIONS)],
                       "etiquettes": S.REGIONS + ["Alsace", "Bourgogne"],
                       "consigne": "Place les 13 régions sur leur numéro. Deux étiquettes sont d'anciennes régions qui n'existent plus : laisse-les de côté. Choisis ensuite la phrase de la fiche qui donne le nombre de régions." + S.regions(),
                       "indices": ["L'Alsace fait partie du Grand Est.", "La Bourgogne fait partie de la Bourgogne-Franche-Comté.", "Pour la justification : cherche « 13 régions »."],
                       "justification": J("Quelle phrase de la fiche donne le nombre de régions ?", E_NOMBRES, [E_EMBOITE, E_NUMERO, E_CONTINENTS], pos=0)},
        "second": {"type": "plan", "titre": "Le planisphère de Léna", "colonnes": 2,
                   "cases": [{"libelle": f"Repère {i + 1}", "reponse": c[0]} for i, c in enumerate(S.CONTINENTS)],
                   "etiquettes": [c[0] for c in S.CONTINENTS] + ["L'océan Atlantique", "L'Arctique"],
                   "consigne": "Place les sept continents sur le planisphère. Deux étiquettes ne sont pas des continents. Choisis ensuite la phrase de la fiche qui les nomme." + S.planisphere(range(7)),
                   "indices": ["Un océan n'est pas un continent.", "L'Arctique est un océan glacé, sans terre au pôle Nord.", "Pour la justification : cherche « sept continents »."],
                   "justification": J("Quelle phrase de la fiche nomme les continents ?", E_CONTINENTS, [E_FRANCE, E_EMBOITE, E_CHIFFRES], pos=3)},
    }
    d["e2-3"] = {
        "mousse": qcm(
            "Léna te pose deux questions sur la France.",
            [("Quelle est la capitale de la France ?", ["Paris", "Dijon", "Lyon"], 0, "Paris est la capitale."),
             ("Quelle est la monnaie de la France ?", ["l'euro", "le dollar", "le franc"], 0, "L'euro, comme en Espagne et en Allemagne.")],
            ["Ouvre la fiche " + FICHE + ".", "La capitale est la ville du président de la République.", "On paie en euros."]),
        "lieutenant": trous(
            "Complète la carte d'identité de la France (trois étiquettes sont en trop), puis choisis la phrase de la fiche qui donne sa superficie et sa population.",
            "Continent : [[Europe]]. Capitale : [[Paris]]. Superficie de la métropole : environ [[552 000 km²]]. Population : environ [[69 millions]] d'habitants. Devise : [[Liberté, Égalité, Fraternité]].",
            ["Europe", "Paris", "552 000 km²", "69 millions", "Liberté, Égalité, Fraternité", "55 millions", "552 000 m²", "Un pour tous, tous pour un"],
            ["Une superficie de pays se mesure en km².", "Près de 70 millions d'habitants.", "Pour la justification : cherche « 552 000 »."],
            J("Quelle phrase de la fiche donne la superficie et la population ?", E_CHIFFRES, [E_FRANCE, E_NOMBRES, E_CONTINENTS], pos=1)),
        "second": vf(
            "Un faux passeport circule. Pour chaque ligne, choisis vrai ou faux, puis la phrase de la fiche qui décrit la France.",
            [("La capitale de la France est Paris.", True, "Paris est la capitale."),
             ("La monnaie de la France est le franc.", False, "C'est l'euro depuis 2002."),
             ("L'hymne de la France est La Marseillaise.", True, "Son titre vient des soldats venus de Marseille."),
             ("La France métropolitaine mesure environ 552 000 m².", False, "552 000 km² : des kilomètres carrés."),
             ("La France compte environ 69 millions d'habitants.", True, "Environ 69 millions.")],
            ["Une monnaie européenne commune.", "m² ou km² : regarde bien l'unité.", "Pour la justification : cherche « sa devise »."],
            J("Quelle phrase de la fiche décrit la France ?", E_FRANCE, [E_CHIFFRES, E_CONTINENTS, E_EMBOITE], pos=2)),
    }
    d["e2-4"] = {
        "lieutenant": tri(
            "Range chaque décision chez celui qui décide, puis choisis la phrase de la fiche sur le département.",
            [("com", "La commune"), ("dep", "Le département"), ("reg", "La région")],
            [("Rénover une école élémentaire", "com"), ("Organiser la collecte des déchets", "com"), ("Construire un collège", "dep"),
             ("Verser une aide sociale", "dep"), ("Entretenir une route départementale", "dep"), ("Agrandir un lycée", "reg"), ("Créer une ligne de TER", "reg")],
            ["L'aide sociale dépend du département.", "Les trains régionaux s'appellent les TER.", "Pour la justification : cherche « aide sociale »."],
            J("Quelle phrase de la fiche dit de quoi s'occupe le département ?", E_DEPT, [E_REGION, E_ECOLES, E_NUMERO], pos=0)),
        "second": tri(
            "Léna a mélangé des décisions vraies et des pièges. Range chacune chez celui qui décide, puis choisis la phrase de la fiche qui répartit écoles, collèges et lycées.",
            [("com", "La commune"), ("dep", "Le département"), ("reg", "La région")],
            [("Ouvrir une classe de maternelle", "com"), ("Changer les tuyaux d'eau d'une rue", "com"), ("Rénover le gymnase d'un collège", "dep"),
             ("Verser une aide sociale", "dep"), ("Construire un lycée professionnel", "reg"), ("Ajouter des trains TER le matin", "reg")],
            ["Le gymnase du collège suit le collège.", "Le lycée professionnel est un lycée.", "Pour la justification : cherche « des collèges »."],
            J("Quelle phrase de la fiche répartit les écoles, les collèges et les lycées ?", E_ECOLES, [E_DEPT, E_REGION, E_EMBOITE], pos=3)),
    }
    return d
