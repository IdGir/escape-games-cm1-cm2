"""Salle 5 « Le cabinet du cartographe » : grades mousse, lieutenant, second (fiche : Les premiers empires coloniaux)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "grandes-explorations", "tests", "donnees"))
from fiches import *

FICHE = "« Les premiers empires coloniaux »"


def donnees(svg, bloc=None):
    d = {}
    c3, c5 = svg("e5-1", "matelot"), svg("e5-1", "timonier")
    d["e5-1"] = {
        "mousse": {"type": "plan", "titre": "La carte du partage", "colonnes": 3,
                   "cases": [{"libelle": "Repère 1", "reponse": "ligne de partage"}, {"libelle": "Repère 2", "reponse": "pour l'Espagne"}, {"libelle": "Repère 3", "reponse": "pour le Portugal"}],
                   "etiquettes": ["ligne de partage", "pour l'Espagne", "pour le Portugal"],
                   "consigne": "Place chaque étiquette sur son repère de la carte du partage." + c3,
                   "indices": ["Ouvre la fiche " + FICHE + ".", "Le repère 1 est sur la ligne en pointillés.", "L'Espagne reçoit le côté gauche, l'ouest."]},
        "lieutenant": {"type": "plan", "titre": "La carte du partage", "colonnes": 2,
                       "cases": [{"libelle": "Repère 1", "reponse": "ligne de Tordesillas"}, {"libelle": "Repère 2", "reponse": "terres pour l'Espagne"}, {"libelle": "Repère 3", "reponse": "terres pour le Portugal"},
                                 {"libelle": "Repère 4", "reponse": "Brésil"}, {"libelle": "Repère 5", "reponse": "Nouvelle-France"}],
                       "etiquettes": ["ligne de Tordesillas", "terres pour l'Espagne", "terres pour le Portugal", "Brésil", "Nouvelle-France", "Virginie", "Inde", "Pérou"],
                       "consigne": "Place chaque étiquette sur son repère (trois sont en trop), puis choisis la phrase de la fiche qui explique pourquoi le repère 4 est portugais." + c5,
                       "indices": ["Le Brésil dépasse la ligne vers l'est.", "La Nouvelle-France est au nord.", "Pour la justification : cherche « Cabral »."],
                       "justification": J("Quelle phrase de la fiche explique le repère 4 ?", C_BRESIL, [C_PARTAGE, C_TORDE, C_SUCRE], pos=2)},
        "second": qcm(
            "Observe la carte du partage. Réponds aux questions, puis choisis la phrase de la fiche qui montre que ce partage n'a pas été accepté par tous." + c5,
            [("Où passe la ligne de Tordesillas ?", ["à 370 lieues à l'ouest des îles du Cap-Vert", "au milieu de l'Afrique", "le long de l'équateur", "au large de l'Inde"], 0, "D'après le traité de 1494."),
             ("Qui reçoit les terres à l'ouest de la ligne ?", ["le Portugal", "la France", "l'Espagne", "l'Angleterre"], 2, "L'ouest pour l'Espagne."),
             ("Le repère 5 est une colonie...", ["espagnole", "française", "portugaise", "aztèque"], 1, "La Nouvelle-France."),
             ("Les peuples d'Amérique ont-ils été consultés ?", ["oui, tous", "seulement les Incas", "non, jamais", "seulement les Iroquoiens"], 2, "Le partage est décidé en Europe.")],
            ["Relis la fiche : la ligne part des îles du Cap-Vert.", "La France s'installe malgré le partage.", "Pour la justification : cherche « refusent »."],
            J("Quelle phrase de la fiche montre que le partage n'a pas été accepté par tous ?", C_CONCUR, [C_PARTAGE, C_FRANCE, C_EMPIRE], pos=3)),
    }
    d["e5-2"] = {
        "mousse": assoc(
            "Relie chaque colonie au pays qui la domine.",
            [("le Mexique", "l'Espagne"), ("le Brésil", "le Portugal"), ("la Nouvelle-France", "la France")],
            ["Ouvre la fiche " + FICHE + ".", "Cortés est espagnol.", "Cartier est français."]),
        "lieutenant": qcm(
            "Simon interroge l'équipage sur les colonies. Réponds aux questions, puis choisis la phrase de la fiche qui définit un empire colonial.",
            [("Qui fonde Québec en 1608 ?", ["Jacques Cartier", "Samuel de Champlain", "Christophe Colomb", "Hernán Cortés"], 1, "Champlain, en 1608."),
             ("Que cultivent les Portugais au Brésil ?", ["le blé", "le café", "la canne à sucre", "la vigne"], 2, "Dans de grandes plantations."),
             ("Que font les Français en Nouvelle-France ?", ["le commerce des fourrures avec les Amérindiens", "l'exploitation de mines d'argent", "la culture du coton", "la pêche aux perles"], 0, "Fourrures de castor notamment."),
             ("Quelle est la première colonie anglaise durable ?", ["la Virginie, en 1607", "le Brésil, en 1500", "Québec, en 1608", "le Mexique, en 1521"], 0, "Sur la côte est de l'Amérique du Nord.")],
            ["Cartier arrive en 1534, mais ne fonde pas Québec.", "Le sucre vient de la canne.", "Pour la justification : cherche « ensemble des territoires »."],
            J("Quelle phrase de la fiche définit un empire colonial ?", C_EMPIRE, [C_ESPAGNE, C_PARTAGE, C_RICHE], pos=1)),
        "second": ordre(
            "Simon reconstitue la naissance des empires coloniaux. Remets les événements du plus ancien au plus récent, puis choisis la phrase de la fiche qui date le partage.",
            ["Le traité de Tordesillas partage les terres à découvrir.", "Cabral arrive au Brésil.", "Cortés et ses alliés prennent Tenochtitlan.",
             "Cartier plante une croix à Gaspé.", "Les Anglais fondent la Virginie.", "Champlain fonde Québec."],
            ["Le partage a lieu deux ans après le premier voyage de Colomb.", "Les colonies anglaise et française du nord naissent au début du XVIIe siècle.", "Pour la justification : cherche « 7 juin »."],
            J("Quelle phrase de la fiche date le partage ?", C_TORDE, [C_PARTAGE, C_BRESIL, C_CONCUR], pos=0)),
    }
    d["e5-3"] = {
        "mousse": code(
            "Le coffre de bord s'ouvre avec deux années : l'arrivée de Colomb aux Antilles, puis l'arrivée de Cartier au Canada.",
            [("Arrivée de Colomb aux Antilles", "1492", 4), ("Arrivée de Cartier au Canada", "1534", 4)],
            ["Ouvre la fiche « Les grands voyages » et relis la frise du capitaine.", "Colomb : fin du XVe siècle.", "Cartier : quarante-deux ans plus tard."]),
        "lieutenant": code(
            "Le coffre de bord s'ouvre en reliant chaque grand événement à son année. Écris les quatre années, puis choisis la phrase de la fiche qui donne la deuxième.",
            [("Arrivée de Colomb aux Antilles", "1492", 4), ("Traité de Tordesillas", "1494", 4), ("Arrivée de Vasco de Gama en Inde", "1498", 4), ("Arrivée de Cartier à Gaspé", "1534", 4)],
            ["Le traité est signé deux ans après le voyage de Colomb.", "Vasco de Gama arrive six ans après Colomb.", "Pour la justification : cherche « traité »."],
            J("Quelle phrase de la fiche donne l'année du deuxième événement ?", C_TORDE, [C_PARTAGE, C_FRANCE, C_BRESIL], pos=1)),
        "second": code(
            "Le coffre de bord s'ouvre avec cinq années : Tordesillas, l'arrivée de Cabral au Brésil, la prise de Tenochtitlan, la fondation de la Virginie, la fondation de Québec. Écris-les, puis choisis la phrase de la fiche qui donne la dernière.",
            [("Traité de Tordesillas", "1494", 4), ("Arrivée de Cabral au Brésil", "1500", 4), ("Prise de Tenochtitlan", "1521", 4),
             ("Fondation de la Virginie", "1607", 4), ("Fondation de Québec", "1608", 4)],
            ["Cabral arrive au tout début du XVIe siècle.", "La Virginie précède Québec d'un an.", "Pour la justification : cherche « Champlain »."],
            J("Quelle phrase de la fiche donne la dernière année ?", C_FRANCE, [C_ANGLE, C_BRESIL, C_TORDE], pos=2)),
    }
    d["e5-4"] = {
        "lieutenant": tri(
            "Simon trie les registres de marchandises. Range chaque carte sous le pays qui l'exploite, puis choisis la phrase de la fiche qui parle des mines.",
            [("espagne", "Espagne"), ("portugal", "Portugal"), ("france", "France")],
            [("l'argent des mines du Pérou", "espagne"), ("l'or du Mexique", "espagne"), ("le sucre des plantations du Brésil", "portugal"),
             ("le bois brésil, qui donne une teinture rouge", "portugal"), ("les fourrures de castor", "france"), ("la pêche à la morue près de Terre-Neuve", "france")],
            ["Le Mexique et le Pérou sont espagnols.", "Le Brésil est portugais.", "Pour la justification : cherche « argent »."],
            J("Quelle phrase de la fiche parle des mines ?", C_ESPAGNE, [C_SUCRE, C_FRANCE, C_EMPIRE], pos=0)),
        "second": tri(
            "Simon relie ce chapitre à l'histoire de la traite atlantique (jeu « Les Archives du port »). Range chaque carte : cause ou conséquence de l'exploitation des colonies ? Puis choisis la phrase de la fiche qui fait ce lien.",
            [("cause", "Ce qui pousse à exploiter les colonies"), ("consequence", "Ce que provoque cette exploitation")],
            [("la recherche d'or et d'argent", "cause"), ("la demande de sucre en Europe", "cause"), ("le partage de Tordesillas", "cause"),
             ("le travail forcé des Amérindiens", "consequence"), ("le début de la traite atlantique", "consequence"), ("l'enrichissement de l'Espagne", "consequence")],
            ["Une cause vient avant, une conséquence vient après.", "Le travail forcé est imposé pour exploiter mines et plantations.", "Pour la justification : cherche « traite atlantique »."],
            J("Quelle phrase de la fiche relie les colonies à la traite ?", C_TRAITE, [C_RICHE, C_SUCRE, C_ESPAGNE], pos=3)),
    }
    return d
