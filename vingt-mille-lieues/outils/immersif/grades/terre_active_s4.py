"""Salle 4 « La salle des sismographes » : grades mousse, lieutenant, second (fiche : Les séismes)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "terre-active", "tests", "donnees"))
from fiches import *
from schemas import seisme

FICHE = "« Les séismes »"
SMOTS = ["le foyer", "l'épicentre", "la faille", "les ondes sismiques", "un sismographe"]


def donnees(svg, bloc=None):
    d = {}
    d["e4-1"] = {
        "mousse": assoc(
            "Relie chaque mot à sa définition.",
            [("un séisme", "le sol qui tremble"), ("le foyer", "là où la roche casse, sous terre"), ("le sismographe", "l'appareil qui enregistre")],
            ["Ouvre la fiche " + FICHE + ".", "Le foyer est sous terre.", "Le sismographe écrit les secousses."]),
        "lieutenant": assoc(
            "Relie chaque mot à sa définition, puis choisis la phrase de la fiche sur les ondes sismiques.",
            [("le foyer", "l'endroit sous terre où la roche casse"), ("l'épicentre", "le point de la surface juste au-dessus du foyer"),
             ("les ondes sismiques", "les vibrations qui partent du foyer"), ("un sismogramme", "le tracé obtenu par le sismographe"), ("une réplique", "une secousse plus faible qui suit")],
            ["Les ondes partent du foyer.", "Le sismogramme est un tracé.", "Pour la justification : cherche « dans toutes les directions »."],
            J("Quelle phrase de la fiche décrit les ondes sismiques ?", S_ONDES, [S_FOYER, S_SISMO, S_REPLIQUE], pos=2)),
        "second": ordre(
            "Samuel explique un séisme du début à la fin. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche qui dit pourquoi les roches cassent.",
            [("Le mouvement des plaques pousse les roches.", "pendant des années"), ("Les roches se déforment et résistent.", "la tension monte"),
             ("Les roches cassent brusquement au foyer, le long d'une faille.", "le séisme"), ("Les ondes sismiques font vibrer le sol.", "quelques secondes"),
             ("Les sismographes enregistrent le séisme.", "le sismogramme"), ("Des répliques plus faibles peuvent suivre.", "les jours suivants")],
            ["Tout commence par une poussée lente.", "La cassure vient avant les ondes.", "Pour la justification : cherche « brusquement »."],
            J("Quelle phrase de la fiche explique pourquoi les roches cassent ?", S_FAILLE, [S_FOYER, S_ONDES, S_PREVOIR], pos=0)),
    }
    d["e4-2"] = {
        "mousse": {"type": "plan", "titre": "Le tableau de Samuel", "colonnes": 3,
                   "cases": [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(SMOTS[:3])],
                   "etiquettes": SMOTS[:3],
                   "consigne": "Place chaque mot sur son repère." + seisme(3),
                   "indices": ["Ouvre la fiche " + FICHE + ".", "Le foyer est l'étoile jaune.", "L'épicentre est sur le sol."]},
        "lieutenant": {"type": "plan", "titre": "Le tableau de Samuel", "colonnes": 2,
                       "cases": [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(SMOTS)],
                       "etiquettes": SMOTS + ["le cratère", "la magnitude"],
                       "consigne": "Replace les étiquettes du schéma (deux sont en trop), puis choisis la phrase de la fiche qui définit le foyer et l'épicentre." + seisme(5),
                       "indices": ["La magnitude est un nombre, pas un endroit.", "Les cercles sont les ondes.", "Pour la justification : cherche « juste au-dessus »."],
                       "justification": J("Quelle phrase de la fiche définit le foyer et l'épicentre ?", S_FOYER, [S_FAILLE, S_ONDES, S_SISMO], pos=1)},
        "second": qcm(
            "Samuel compare des séismes enregistrés en France. Choisis la bonne réponse, puis la phrase de la fiche sur la magnitude.",
            [("Martinique 2007 : magnitude 7,4 ; Guadeloupe (Les Saintes) 2004 : 6,3 ; Le Teil 2019 : 4,8. Lequel a libéré le plus d'énergie ?", ["Le Teil", "Les Saintes", "la Martinique", "ils sont égaux"], 2, "7,4 est la plus grande magnitude."),
             ("Lequel a la plus petite magnitude ?", ["Le Teil", "Les Saintes", "la Martinique", "aucun"], 0, "4,8."),
             ("Le séisme du Teil a pourtant causé des dégâts. Pourquoi est-ce possible ?", ["la magnitude ne dit pas tout : la profondeur et les bâtiments comptent aussi", "la magnitude est fausse", "il n'y a pas eu de dégâts", "c'était un volcan"], 0, "Les dégâts dépendent aussi du lieu."),
             ("Que mesure la magnitude ?", ["la durée", "l'énergie libérée", "le nombre de répliques", "la distance à la mer"], 1, "Plus elle est grande, plus le séisme est fort.")],
            ["Compare les nombres.", "Les dégâts ne dépendent pas que de la magnitude.", "Pour la justification : cherche « énergie »."],
            J("Quelle phrase de la fiche définit la magnitude ?", S_MAGNITUDE, [S_SISMO, S_TEIL, S_ZONES], pos=3)),
    }
    d["e4-3"] = {
        "mousse": vf(
            "Samuel a écrit trois phrases. Pour chacune, choisis vrai ou faux.",
            [("Pendant un séisme, le sol tremble.", True, "Les ondes le font vibrer."),
             ("On connaît toujours le jour du prochain séisme.", False, "Personne ne sait le prévoir."),
             ("Le sismographe enregistre les secousses.", True, "Il trace un sismogramme.")],
            ["Ouvre la fiche " + FICHE + ".", "Le jour d'un séisme est inconnu.", "Le sismographe écrit."]),
        "lieutenant": qcm(
            "Samuel prépare les réponses aux habitants. Choisis la bonne réponse, puis la phrase de la fiche sur les zones de sismicité.",
            [("Combien de zones de sismicité compte la France depuis 2011 ?", ["deux", "trois", "cinq", "huit"], 2, "De « très faible » à « forte »."),
             ("Quels départements sont entièrement en zone forte ?", ["la Guadeloupe et la Martinique", "la Côte-d'Or et la Nièvre", "Paris", "la Bretagne"], 0, "Aux Antilles."),
             ("Quelle commune a été endommagée le 11 novembre 2019 ?", ["Le Teil, en Ardèche", "Saint-Pierre", "Dijon", "Brest"], 0, "Magnitude 4,8.")],
            ["Cinq zones.", "Les Antilles sont en zone forte.", "Pour la justification : cherche « cinq zones »."],
            J("Quelle phrase de la fiche parle des zones de sismicité ?", S_ZONES, [S_TEIL, S_PREVOIR, S_MAGNITUDE], pos=0)),
        "second": tri(
            "Les habitants demandent : « Que savez-vous faire ? » Range chaque affirmation, puis choisis la phrase de la fiche sur la prévision des séismes.",
            [("oui", "Les scientifiques savent le faire"), ("non", "Personne ne sait le faire")],
            [("dire où les séismes sont probables", "oui"), ("mesurer la magnitude d'un séisme", "oui"), ("enregistrer les ondes sismiques", "oui"),
             ("annoncer le jour exact du prochain séisme", "non"), ("donner l'heure du prochain séisme", "non"), ("empêcher un séisme", "non")],
            ["On sait où, pas quand.", "On mesure après coup.", "Pour la justification : cherche « le jour et l'heure »."],
            J("Quelle phrase de la fiche parle de la prévision des séismes ?", S_PREVOIR, [S_ZONES, S_SISMO, S_FAILLE], pos=2)),
    }
    d["e4-4"] = {
        "lieutenant": trous(
            "Complète la consigne « tsunami » de la plage (des étiquettes sont en trop), puis choisis la phrase de la fiche qui la donne.",
            "Un tsunami est une série de vagues géantes, souvent provoquée par un [[séisme]] sous la mer. Si le sol tremble fort au bord de la mer, il faut s'éloigner de la [[côte]] et monter sur une [[hauteur]], puis écouter les [[consignes]] des autorités.",
            ["séisme", "côte", "hauteur", "consignes", "tempête", "cave", "plage"],
            ["On s'éloigne de l'eau.", "On monte.", "Pour la justification : cherche « au bord de la mer »."],
            J("Quelle phrase de la fiche donne la consigne en bord de mer ?", S_TSUNAMI, [S_PREVOIR, S_ZONES, S_REPLIQUE], pos=3)),
        "second": vf(
            "Samuel relit le compte rendu de la nuit. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur les répliques.",
            [("Après un séisme, des secousses plus faibles peuvent suivre.", True, "Ce sont les répliques."),
             ("Une réplique est toujours plus forte que le séisme.", False, "Elle est en général plus faible."),
             ("Le foyer est à la surface du sol.", False, "C'est l'épicentre qui est à la surface."),
             ("Un sismogramme est le tracé d'un sismographe.", True, "Il montre les vibrations."),
             ("Les ondes partent du foyer dans toutes les directions.", True, "Elles font vibrer le sol.")],
            ["Une réplique suit le séisme.", "Foyer en profondeur, épicentre en surface.", "Pour la justification : cherche « répliques »."],
            J("Quelle phrase de la fiche parle des répliques ?", S_REPLIQUE, [S_ONDES, S_FOYER, S_SISMO], pos=1)),
    }
    return d
