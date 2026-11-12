"""Salle 3 « La chambre des cartes » : grades mousse, lieutenant, second (fiche : Les grands voyages)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "grandes-explorations", "tests", "donnees"))
from fiches import *

FICHE = "« Les grands voyages »"


def donnees(svg, bloc=None):
    d = {}
    c3, c5 = svg("e3-3", "matelot"), svg("e3-3", "timonier")
    d["e3-1"] = {
        "mousse": ordre(
            "Range les trois voyages du plus ancien au plus récent. La date est écrite sous chaque carte.",
            [("Colomb arrive aux Antilles.", "1492"), ("Vasco de Gama arrive en Inde.", "1498"), ("Cartier arrive au Canada.", "1534")],
            ["Ouvre la fiche " + FICHE + ".", "La plus petite date est la plus ancienne.", "1534 est la plus grande date."]),
        "lieutenant": ordre(
            "Le capitaine a mélangé les pages de son journal. Range les six événements du plus ancien au plus récent (sans les dates), puis choisis la phrase de la fiche qui date l'arrivée en Inde.",
            ["Colomb quitte Palos avec trois navires.", "Colomb atteint une île des Bahamas.", "Vasco de Gama arrive à Calicut, en Inde.",
             "Magellan part d'Espagne avec cinq navires.", "Magellan est tué aux Philippines.", "Cartier arrive à Gaspé."],
            ["Colomb part en août et arrive en octobre de la même année.", "Magellan meurt deux ans après son départ.", "Pour la justification : cherche « Calicut »."],
            J("Quelle phrase de la fiche date l'arrivée en Inde ?", V_GAMA, [V_ROUTE, V_COLOMB2, V_MAG], pos=2)),
        "second": ordre(
            "Le capitaine veut une frise au mois près. Range les événements du plus ancien au plus récent, puis choisis la phrase de la fiche qui donne la date du départ de Colomb.",
            [("Colomb quitte Palos.", "3 août 1492"), ("Colomb atteint une île des Bahamas.", "12 octobre 1492"), ("Vasco de Gama quitte Lisbonne.", "juillet 1497"),
             ("Vasco de Gama arrive à Calicut.", "20 mai 1498"), ("Elcano rentre en Espagne.", "6 septembre 1522"), ("Cartier arrive à Gaspé.", "24 juillet 1534")],
            ["Compare d'abord les années, puis les mois.", "Août vient avant octobre.", "Pour la justification : cherche « Palos »."],
            J("Quelle phrase de la fiche donne la date du départ de Colomb ?", V_COLOMB, [V_COLOMB2, V_QUATRE, V_CARTIER], pos=0)),
    }
    d["e3-2"] = {
        "mousse": assoc(
            "Relie chaque explorateur à son voyage.",
            [("Colomb", "traverse l'Atlantique vers l'ouest"), ("Vasco de Gama", "fait le tour de l'Afrique"), ("Cartier", "arrive au Canada")],
            ["Ouvre la fiche " + FICHE + ".", "Colomb part vers l'ouest.", "Cartier est français."]),
        "lieutenant": qcm(
            "Le capitaine vérifie votre lecture du journal. Réponds aux questions, puis choisis la phrase de la fiche qui explique pourquoi on parle d'« arrivée des Européens ».",
            [("Où Colomb croit-il être arrivé ?", ["en Afrique", "en Asie, aux Indes", "au Canada", "en Australie"], 1, "Il croit être aux Indes."),
             ("Par où passe Vasco de Gama pour aller en Inde ?", ["par le cap de Bonne-Espérance", "par le canal de Suez", "par le détroit de Magellan", "par le Saint-Laurent"], 0, "Au sud de l'Afrique."),
             ("Qui envoie Jacques Cartier ?", ["les souverains d'Espagne", "le roi du Portugal", "le roi de France François Ier", "le pape"], 2, "François Ier."),
             ("Combien d'hommes rentrent avec Elcano ?", ["250", "18", "3", "180"], 1, "18 hommes.")],
            ["Les Antilles ont gardé le nom d'« Indes occidentales ».", "Le canal de Suez n'existait pas.", "Pour la justification : cherche « habitées »."],
            J("Quelle phrase de la fiche explique l'expression « arrivée des Européens » ?", V_AMERIQUE, [V_TOUR, V_COLOMB2, V_NOMS], pos=3)),
        "second": trous(
            "Le capitaine dicte le bilan du premier tour du monde. Complète avec les bonnes étiquettes (il y en a en trop), puis choisis la phrase de la fiche qui dit ce que ce voyage prouve.",
            "En [[1519]], Magellan part d'Espagne avec [[cinq]] navires et environ [[250]] hommes. Il est tué aux [[Philippines]] en 1521. Elcano rentre le 6 septembre 1522 sur la [[Victoria]] avec [[18]] hommes : moins d'un homme sur dix est revenu.",
            ["1519", "cinq", "250", "Philippines", "Victoria", "18", "1492", "trois", "Antilles", "Santa Maria", "180"],
            ["Le voyage dure trois ans.", "Un seul navire revient.", "Pour la justification : cherche « faire le tour »."],
            J("Que prouve ce voyage, d'après la fiche ?", V_TOUR, [V_MAG, V_MAG2, V_ROUTE], pos=1)),
    }
    d["e3-3"] = {
        "mousse": {"type": "plan", "titre": "La carte du capitaine", "colonnes": 3,
                   "cases": [{"libelle": "Repère 1", "reponse": "Colomb"}, {"libelle": "Repère 2", "reponse": "Vasco de Gama"}, {"libelle": "Repère 3", "reponse": "Cartier"}],
                   "etiquettes": ["Colomb", "Vasco de Gama", "Cartier"],
                   "consigne": "Place chaque explorateur sur le repère de sa route." + c3,
                   "indices": ["Ouvre la fiche " + FICHE + " : regarde la carte.", "La route qui fait le tour de l'Afrique est celle de Vasco de Gama.", "La route du nord va au Canada."]},
        "lieutenant": {"type": "plan", "titre": "La carte du capitaine", "colonnes": 2,
                       "cases": [{"libelle": "Repère 1", "reponse": "Colomb"}, {"libelle": "Repère 2", "reponse": "Vasco de Gama"}, {"libelle": "Repère 3", "reponse": "Cartier"},
                                 {"libelle": "Repère 4", "reponse": "Magellan et Elcano"}, {"libelle": "Repère 5", "reponse": "cap de Bonne-Espérance"}],
                       "etiquettes": ["Colomb", "Vasco de Gama", "Cartier", "Magellan et Elcano", "cap de Bonne-Espérance", "détroit de Gibraltar", "Marco Polo", "Cabral"],
                       "consigne": "Place chaque étiquette sur son repère (trois sont en trop), puis choisis la phrase de la fiche qui décrit la route du repère 2." + c5,
                       "indices": ["La route en pointillés passe au sud de l'Amérique.", "Le repère 5 est une pointe de terre au sud de l'Afrique.", "Pour la justification : cherche « contourne »."],
                       "justification": J("Quelle phrase de la fiche décrit la route du repère 2 ?", V_GAMA, [V_ROUTE, V_MAG, V_COLOMB], pos=1)},
        "second": {"type": "plan", "titre": "La carte du capitaine", "colonnes": 2,
                   "cases": [{"libelle": "Repère 1", "reponse": "vers les Antilles (1492)"}, {"libelle": "Repère 2", "reponse": "vers Calicut (1498)"}, {"libelle": "Repère 3", "reponse": "vers Gaspé (1534)"},
                             {"libelle": "Repère 4", "reponse": "autour du monde (1519-1522)"}, {"libelle": "Repère 5", "reponse": "cap de Bonne-Espérance"}],
                   "etiquettes": ["vers les Antilles (1492)", "vers Calicut (1498)", "vers Gaspé (1534)", "autour du monde (1519-1522)", "cap de Bonne-Espérance", "vers Québec (1608)", "vers le Brésil (1500)"],
                   "consigne": "Sur la carte, nomme chaque route par sa destination et sa date (deux étiquettes sont en trop), puis choisis la phrase de la fiche qui décrit la route du repère 3." + c5,
                   "indices": ["Québec n'est pas une route du journal : c'est une fondation.", "La route du Brésil n'est pas tracée.", "Pour la justification : cherche « Saint-Malo »."],
                   "justification": J("Quelle phrase de la fiche décrit la route du repère 3 ?", V_CARTIER, [V_AMERIQUE, V_COLOMB, V_NOMS], pos=2)},
    }
    d["e3-4"] = {
        "lieutenant": trous(
            "Une page mouillée raconte le premier tour du monde. Complète (il y a des étiquettes en trop), puis choisis la phrase de la fiche qui dit qui ramène le navire.",
            "En [[1519]], Magellan quitte l'Espagne avec [[cinq]] navires. Il est tué aux [[Philippines]] en 1521. Le 6 septembre [[1522]], Elcano rentre sur la [[Victoria]] avec [[18]] hommes.",
            ["1519", "cinq", "Philippines", "1522", "Victoria", "18", "1492", "Antilles", "180", "Santa Maria"],
            ["Le départ a lieu trois ans avant le retour.", "Les survivants sont moins de vingt.", "Pour la justification : cherche « Elcano »."],
            J("Quelle phrase de la fiche dit qui ramène le navire ?", V_MAG2, [V_MAG, V_TOUR, V_GAMA], pos=0)),
        "second": code(
            "Le coffre de la chambre des cartes s'ouvre avec quatre nombres tirés du journal. Écris-les, puis choisis la phrase de la fiche qui donne le dernier.",
            [("Nombre de navires au départ de Magellan", "5", 1), ("Durée du tour du monde, en années (1519 → 1522)", "3", 1),
             ("Année de l'arrivée de Vasco de Gama à Calicut", "1498", 4), ("Nombre d'hommes revenus avec Elcano", "18", 2)],
            ["Compte de 1519 à 1522.", "Les survivants sont moins de vingt.", "Pour la justification : cherche « Victoria »."],
            J("Quelle phrase de la fiche donne le nombre d'hommes revenus ?", V_MAG2, [V_MAG, V_TOUR, V_QUATRE], pos=3)),
    }
    return d
