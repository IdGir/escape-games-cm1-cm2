"""Séance 7 « Le littoral atlantique » : grades mousse, lieutenant, second (fiche : Les mers et l'océan qui bordent la France)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "mission-geo", "tests", "donnees"))
from fiches import *
import schemas as S

FICHE = "« Les mers et l'océan qui bordent la France »"


def donnees(svg, bloc=None):
    d = {}
    d["e7-1"] = {
        "mousse": {"type": "plan", "titre": "La carte de Théo", "colonnes": 3,
                   "cases": [{"libelle": f"Repère {i + 1}", "reponse": S.MERS[k][0]} for i, k in enumerate([1, 2, 3])],
                   "etiquettes": [S.MERS[k][0] for k in (1, 2, 3)],
                   "consigne": "Place chaque mer ou océan sur son repère." + S.mers([1, 2, 3]),
                   "indices": ["Ouvre la fiche " + FICHE + ".", "La Méditerranée est au sud.", "L'océan Atlantique est à l'ouest."]},
        "lieutenant": ordre(
            "Théo fait le tour des côtes de France en bateau, de la Belgique à l'Italie. Range les eaux qu'il longe dans l'ordre, puis choisis la phrase de la fiche qui les cite toutes.",
            ["la mer du Nord", "la Manche", "l'océan Atlantique", "la mer Méditerranée"],
            ["La Belgique est au nord.", "Après la Manche, on longe la Bretagne vers l'ouest et le sud.", "Pour la justification : cherche « quatre grandes étendues d'eau »."],
            J("Quelle phrase de la fiche cite les eaux qui bordent la France ?", O_QUATRE, [O_LITTORAL, O_NORD, O_ATLANTIQUE], pos=1)),
        "second": {"type": "plan", "titre": "La France, ses mers et ses stations", "colonnes": 2,
                   "cases": [{"libelle": f"Repère {i + 1}", "reponse": S.MERS[i][0]} for i in range(7)],
                   "etiquettes": [m[0] for m in S.MERS] + ["Dunkerque", "La mer Baltique"],
                   "consigne": "Place les mers, l'océan et les trois stations sur leur repère (deux étiquettes sont en trop), puis choisis la phrase de la fiche qui situe l'océan Atlantique." + S.mers(range(7)),
                   "indices": ["La mer Baltique ne borde pas la France.", "Étretat est en Normandie, Biarritz près de l'Espagne.", "Pour la justification : cherche « en Amérique »."],
                   "justification": J("Quelle phrase de la fiche situe l'océan Atlantique ?", O_ATLANTIQUE, [O_MANCHE, O_QUATRE, O_MEDITERRANEE], pos=2)},
    }
    d["e7-2"] = {
        "mousse": qcm(
            "Théo te pose deux questions avant de partir.",
            [("Où se baigne-t-on à Marseille ?", ["dans la mer Méditerranée", "dans la Manche", "dans la mer du Nord"], 0, "Marseille est au sud."),
             ("Où se baigne-t-on à Biarritz ?", ["dans l'océan Atlantique", "dans la mer Méditerranée", "dans la Manche"], 0, "Biarritz est à l'ouest.")],
            ["Ouvre la fiche " + FICHE + ".", "Marseille est au bord de la mer, au sud.", "Biarritz est au bord de l'océan."]),
        "lieutenant": qcm(
            "Théo veut savoir si tu connais les villes du littoral. Réponds, puis choisis la phrase de la fiche sur la Méditerranée.",
            [("Dunkerque, tout au nord, est au bord de…", ["la mer du Nord", "la Manche", "l'océan Atlantique", "la mer Méditerranée"], 0, "Près de la Belgique."),
             ("Étretat est au bord de…", ["la Manche", "la mer du Nord", "l'océan Atlantique", "la mer Méditerranée"], 0, "Comme toute la Normandie."),
             ("La Rochelle et Biarritz sont au bord de…", ["l'océan Atlantique", "la Manche", "la mer Méditerranée", "la mer du Nord"], 0, "Sur la côte ouest."),
             ("Nice et Ajaccio sont au bord de…", ["la mer Méditerranée", "l'océan Atlantique", "la Manche", "la mer du Nord"], 0, "Ajaccio est en Corse.")],
            ["La mer du Nord est près de la Belgique.", "La Corse est entourée par la Méditerranée.", "Pour la justification : cherche « Corse »."],
            J("Quelle phrase de la fiche parle de la mer Méditerranée ?", O_MEDITERRANEE, [O_NORD, O_MANCHE, O_ATLANTIQUE], pos=3)),
        "second": vf(
            "Le message du voleur contient des erreurs. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur la Manche.",
            [("La Manche est un océan.", False, "C'est une mer, entre la France et le Royaume-Uni."),
             ("En traversant l'océan Atlantique, on arrive en Amérique.", True, "Il sépare l'Europe de l'Amérique."),
             ("La Corse est entourée par la mer Méditerranée.", True, "Elle est au sud-est de la France."),
             ("La mer du Nord borde la Bretagne.", False, "La Bretagne est bordée par la Manche et l'océan Atlantique."),
             ("Biarritz est au bord de la Manche.", False, "Biarritz est au bord de l'océan Atlantique.")],
            ["La Manche est une mer.", "La Bretagne est à l'ouest, pas au nord.", "Pour la justification : cherche « Royaume-Uni »."],
            J("Quelle phrase de la fiche parle de la Manche ?", O_MANCHE, [O_NORD, O_ATLANTIQUE, O_LITTORAL], pos=0)),
    }
    d["e7-3"] = {
        "mousse": assoc(
            "Relie chaque description au bon hébergement.",
            [("une toile que l'on plante soi-même", "une tente"), ("des chambres et une réception", "un hôtel"), ("un terrain pour les tentes", "un camping")],
            ["Ouvre la fiche " + FICHE + ".", "La tente se plante.", "À l'hôtel, on est accueilli à la réception."]),
        "lieutenant": tri(
            "Théo trie les hébergements de Biarritz. Range chacun : en plein air (sur un camping) ou dans un bâtiment ? Choisis ensuite la phrase de la fiche sur les hébergements.",
            [("air", "En plein air, sur un camping"), ("bat", "Dans un bâtiment")],
            [("une tente", "air"), ("une caravane", "air"), ("un mobil-home", "air"),
             ("un hôtel", "bat"), ("un gîte", "bat"), ("une chambre d'hôtes", "bat"), ("une auberge de jeunesse", "bat")],
            ["Le mobil-home est posé sur un terrain de camping.", "Le gîte est une maison louée entièrement.", "Pour la justification : cherche « Pour se loger »."],
            J("Quelle phrase de la fiche cite des hébergements de vacances ?", O_HEBERG, [O_BIARRITZ, O_LITTORAL, O_ETE], pos=1)),
        "second": assoc(
            "Six agents arrivent cet été. Relie le souhait de chacun à l'hébergement qui lui convient, puis choisis la phrase de la fiche sur les hébergements.",
            [("« Je voyage seul, avec très peu d'argent. »", "une auberge de jeunesse"), ("« Je veux dormir chez des habitants, petit-déjeuner compris. »", "une chambre d'hôtes"),
             ("« Je viens avec ma caravane et ma tente. »", "un camping"), ("« Je veux une maison entière pour ma famille. »", "un gîte"),
             ("« Je veux des clubs et des animations pour mes enfants. »", "un village de vacances"), ("« Je veux une réception et le ménage fait chaque jour. »", "un hôtel")],
            ["Le village de vacances propose des animations.", "La caravane et la tente vont sur un terrain aménagé.", "Pour la justification : cherche « village de vacances »."],
            J("Quelle phrase de la fiche cite des hébergements de vacances ?", O_HEBERG, [O_LITTORAL, O_ETE, O_BIARRITZ], pos=2)),
    }
    d["e7-4"] = {
        "lieutenant": code(
            "Un jour d'été, Étretat (environ 4 km², environ 1 100 habitants) peut recevoir jusqu'à 10 000 visiteurs. Calcule, puis choisis la phrase de la fiche qui explique pourquoi la densité augmente.",
            [("Densité hors vacances (hab/km²)", "275", 3), ("Densité avec 10 000 visiteurs de plus (hab/km²)", "2775", 4), ("Multipliée par environ", "10", 2)],
            ["1 100 ÷ 4 = 275.", "(1 100 + 10 000) ÷ 4 = 11 100 ÷ 4.", "2 775 ÷ 275, arrondi à l'unité. Pour la justification : cherche « sur la même surface »."],
            J("Quelle phrase de la fiche explique pourquoi la densité augmente l'été ?", O_ETE, [O_LITTORAL, O_BIARRITZ, O_HEBERG], pos=0)),
        "second": code(
            "Problème de Théo : Étretat mesure environ 4 km² et compte environ 1 100 habitants. Combien de visiteurs faudrait-il pour que sa densité atteigne 1 500 habitants par km², comme dans une ville ? "
            "Et quelle est la densité d'une commune imaginaire de 2 000 habitants sur 8 km² ? Choisis ensuite la phrase de la fiche qui donne l'exemple d'Étretat.",
            [("Personnes nécessaires sur 4 km²", "6000", 4), ("Visiteurs à ajouter aux habitants", "4900", 4), ("Densité de la commune imaginaire (hab/km²)", "250", 3)],
            ["Densité × surface = nombre de personnes : 1 500 × 4.", "Retire les 1 100 habitants.", "2 000 ÷ 8. Pour la justification : cherche « 275 habitants par km² »."],
            J("Quelle phrase de la fiche donne l'exemple d'Étretat ?", O_CALCUL, [O_ETE, O_QUATRE, O_HEBERG], pos=1)),
    }
    return d
