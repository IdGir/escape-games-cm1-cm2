"""Séance 3 « Vivre à Clamecy » : grades mousse, lieutenant, second (fiche : L'espace rural et la densité)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "mission-geo", "tests", "donnees"))
from fiches import *
import schemas as S

FICHE = "« L'espace rural et la densité »"


def donnees(svg, bloc=None):
    d = {}
    d["e3-1"] = {
        "mousse": tri(
            "Malik aime la campagne, mais tout n'est pas facile. Range chaque carte : c'est agréable, ou c'est difficile ?",
            [("a", "C'est agréable"), ("i", "C'est difficile")],
            [("la nature tout près", "a"), ("le calme", "a"), ("peu de magasins", "i"), ("peu de bus", "i")],
            ["Ouvre la fiche " + FICHE + ".", "Le calme, c'est agréable.", "Sans bus, il faut une voiture : c'est difficile."]),
        "lieutenant": {"type": "plan", "titre": "Le bourg vu du ciel", "colonnes": 2,
                       "cases": [{"libelle": f"Repère {i + 1}", "reponse": v[0]} for i, v in enumerate(S.VILLAGE)],
                       "etiquettes": [v[0] for v in S.VILLAGE] + ["La gare TGV", "L'aéroport"],
                       "consigne": "Place chaque élément du bourg sur son repère (deux étiquettes sont en trop), puis choisis la phrase de la fiche qui définit un bourg." + S.village(range(7)),
                       "indices": ["Les maisons se serrent autour du clocher : c'est le centre-bourg.", "Un bourg rural n'a ni aéroport ni gare TGV.", "Pour la justification : cherche « bourg »."],
                       "justification": J("Quelle phrase de la fiche définit un bourg ?", R_VILLAGE, [R_RURAL, R_CLAMECY, R_AGRI], pos=2)},
        "second": ordre(
            "Malik compare des communes imaginaires. Calcule la densité de chacune, puis range-les de la moins dense à la plus dense, puis choisis la phrase de la fiche sur les écarts de densité.",
            [("Le hameau des Crêtes", "40 habitants sur 5 km²"), ("Le village A", "600 habitants sur 30 km²"),
             ("Le bourg C", "3 000 habitants sur 25 km²"), ("La ville B", "60 000 habitants sur 40 km²")],
            ["Compare les densités, pas les habitants : 40 ÷ 5 = 8.", "3 000 ÷ 25 = 120.", "Pour la justification : cherche « 1 000 habitants par km² »."],
            J("Quelle phrase de la fiche compare les densités des villes et des villages ?", R_ECARTS, [R_DENSITE, R_RURAL, R_VILLAGE], pos=0)),
    }
    d["e3-2"] = {
        "mousse": qcm(
            "Malik te pose une question sur la campagne.",
            [("À la campagne, il y a…", ["peu d'habitants et beaucoup de champs", "beaucoup d'immeubles", "des métros partout"], 0, "La densité y est faible.")],
            ["Ouvre la fiche " + FICHE + ".", "Regarde le paysage autour de Clamecy.", "Des champs, des prairies, des forêts."]),
        "lieutenant": trous(
            "Complète la fiche de Malik (deux étiquettes sont en trop), puis choisis la phrase de la fiche qui définit un espace rural.",
            "Un espace rural a une [[densité]] de population [[faible]]. Les [[champs]], les prairies et les [[forêts]] y occupent beaucoup de place. Il est marqué par les activités [[agricoles]].",
            ["densité", "faible", "champs", "forêts", "agricoles", "élevée", "gratte-ciel"],
            ["Le contraire de « faible » est un piège.", "On ne trouve pas de gratte-ciel à la campagne.", "Pour la justification : cherche « occupent beaucoup de place »."],
            J("Quelle phrase de la fiche définit un espace rural ?", R_RURAL, [R_AGRI, R_DENSITE, R_INCONV], pos=1)),
        "second": vf(
            "Malik relit sa définition. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui distingue village et bourg.",
            [("Une commune rurale de 1 200 habitants est un village.", True, "Moins de 2 000 habitants."),
             ("Un bourg n'a aucun commerce.", False, "Ses commerces et ses services servent aussi aux villages voisins."),
             ("Clamecy est un bourg de la Nièvre.", True, "Au bord de l'Yonne et du canal du Nivernais."),
             ("Un espace rural est marqué par les activités agricoles.", True, "Champs, prairies, élevage."),
             ("Plus une commune a d'habitants, plus elle est forcément dense.", False, "Tout dépend aussi de sa superficie.")],
            ["Le seuil est de 2 000 habitants.", "La densité dépend aussi de la surface.", "Pour la justification : cherche « villages voisins »."],
            J("Quelle phrase de la fiche distingue un village d'un bourg ?", R_VILLAGE, [R_CLAMECY, R_RURAL, R_ECARTS], pos=3)),
    }
    d["e3-3"] = {
        "mousse": code(
            "Calcule la densité : 4 habitants vivent sur 1 km². Puis : 4 habitants vivent sur 4 km².",
            [("4 habitants sur 1 km² : densité (hab/km²)", "4", 1), ("4 habitants sur 4 km² : densité (hab/km²)", "1", 1)],
            ["Ouvre la fiche " + FICHE + ".", "Sur 1 km², la densité est le nombre d'habitants.", "4 ÷ 4 = 1."]),
        "lieutenant": code(
            "Malik compare deux communes imaginaires : le village A (600 habitants sur 30 km²) et la ville B (60 000 habitants sur 40 km²). Calcule, puis choisis la phrase de la fiche qui dit comment calculer une densité.",
            [("Densité du village A (hab/km²)", "20", 2), ("Densité de la ville B (hab/km²)", "1500", 4), ("La ville B est combien de fois plus dense ?", "75", 2)],
            ["600 ÷ 30 : pense à 60 ÷ 3.", "60 000 ÷ 40 = 6 000 ÷ 4.", "Pour comparer : 1 500 ÷ 20. Pour la justification : cherche « on divise »."],
            J("Quelle phrase de la fiche dit comment calculer une densité ?", R_DENSITE, [R_ECARTS, R_RURAL, R_VILLAGE], pos=0)),
        "second": code(
            "Problème de Malik : combien d'habitants faudrait-il dans le village A (30 km²) pour qu'il soit aussi dense que la ville B (1 500 hab/km²) ? Et quelle serait la densité d'un hameau de 90 habitants sur 15 km² ? Choisis ensuite la phrase de la fiche sur le calcul de la densité.",
            [("Habitants nécessaires dans le village A", "45000", 5), ("Densité du hameau (hab/km²)", "6", 1)],
            ["Densité × superficie = habitants.", "1 500 × 30 = 45 000.", "90 ÷ 15 = 6. Pour la justification : cherche « superficie en km² »."],
            J("Quelle phrase de la fiche dit comment calculer une densité ?", R_DENSITE, [R_ECARTS, R_AGRI, R_INCONV], pos=2)),
    }
    d["e3-4"] = {
        "lieutenant": tri(
            "Range chaque proposition : avantage ou inconvénient de la vie à la campagne ? Choisis ensuite la phrase de la fiche sur les inconvénients.",
            [("a", "Avantages"), ("i", "Inconvénients")],
            [("la proximité de la nature", "a"), ("des logements moins coûteux", "a"), ("des logements et des terrains plus grands", "a"), ("peu de bruit", "a"),
             ("peu de transports en commun", "i"), ("peu d'emplois", "i"), ("du temps perdu dans les déplacements", "i"), ("une voiture nécessaire", "i"),
             ("peu de commerces", "i"), ("peu de services", "i")],
            ["Il y a 4 avantages et 6 inconvénients.", "Les déplacements longs sont un inconvénient.", "Pour la justification : cherche « inconvénients »."],
            J("Quelle phrase de la fiche cite les inconvénients de la vie à la campagne ?", R_INCONV, [R_AVANTAGES, R_RURAL, R_CLAMECY], pos=1)),
        "second": tri(
            "Malik compare la campagne et la ville. Range chaque caractéristique, puis choisis la phrase de la fiche qui définit l'espace rural.",
            [("r", "Plutôt l'espace rural"), ("u", "Plutôt la ville")],
            [("une faible densité de population", "r"), ("des champs et des forêts", "r"), ("des activités agricoles", "r"),
             ("une forte densité de population", "u"), ("des immeubles et des bureaux", "u"), ("beaucoup de transports en commun", "u")],
            ["La densité est le meilleur indice.", "Les bureaux sont nombreux en ville.", "Pour la justification : cherche « champs, les prairies »."],
            J("Quelle phrase de la fiche définit l'espace rural ?", R_RURAL, [R_AVANTAGES, R_DENSITE, R_VILLAGE], pos=3)),
    }
    return d
