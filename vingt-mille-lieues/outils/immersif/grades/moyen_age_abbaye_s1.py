"""Salle 1 « Le baptême de Clovis » (fiche : clovis)."""
from aide import *

F = "« Après l'Empire romain : Clovis, roi des Francs »"
K1 = "L'Empire romain d'Occident disparaît en 476 : c'est le repère que l'on retient pour le début du Moyen Âge (476-1492)."
K2 = "Les peuples installés dans l'ancien empire fondent des royaumes : Wisigoths au sud, Burgondes à l'est, Francs au nord."
K3 = "486 : victoire de Soissons sur Syagrius, dernier chef romain du nord de la Gaule."
K4 = "Vers 500 : baptême à Reims par l'évêque Remi. La date est discutée : 496, 499 ou 508 selon les historiens. On écrit donc « vers l'an 500 »."
K5 = "507 : victoire de Vouillé sur Alaric II, roi des Wisigoths ; le royaume s'étend vers le sud-ouest."
K6 = "508 : Clovis fait de Paris sa résidence principale. Il meurt en 511."
K7 = "Les Gallo-Romains sont déjà chrétiens. En choisissant la même religion qu'eux, Clovis obtient l'appui des évêques, qui sont alors les personnages les plus influents des villes."
K8 = "Attention : on a longtemps parlé de « temps obscurs » pour ces siècles. Les historiens ne le disent plus : on y écrit, on y bâtit, on y enseigne."
K9 = "Grégoire écrit presque un siècle après les faits : son récit est un témoignage tardif."


def donnees(svg, bloc=None):
    d = {}
    d["e1-1"] = {
        "mousse": qcm(
            "Lis la question, clique sur la bonne réponse, puis vérifie.",
            [("Dans quelle ville Clovis est-il baptisé ?", ["À Reims", "À Rome", "À Aix-la-Chapelle"], 0, "Il est baptisé à Reims par l'évêque Remi.")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "C'est une ville de l'est de la France actuelle.", "L'évêque de cette ville s'appelle Remi."]),
        "lieutenant": vf(
            "Frère Anselme vérifie cinq affirmations sur les débuts du Moyen Âge. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui corrige l'expression « temps obscurs ».",
            [("L'Empire romain d'Occident disparaît en 476.", True, "C'est le repère du début du Moyen Âge."), ("Le Moyen Âge va de 476 à 1492.", True, "Repères retenus."),
             ("Les Francs fondent un royaume au sud de la Gaule.", False, "Au nord ; les Wisigoths sont au sud."), ("On peut encore dire que le Moyen Âge est une période de « temps obscurs ».", False, "On y écrit, on y bâtit, on y enseigne."),
             ("Clovis meurt en 511.", True, "Après avoir fait de Paris sa résidence.")],
            ["476 : début. 1492 : fin.", "Wisigoths au sud, Burgondes à l'est, Francs au nord.", "Pour la justification : cherche la phrase qui parle de « temps obscurs »."],
            J("Quelle phrase de la fiche corrige l'expression « temps obscurs » ?", K8, [K1, K2, K6], pos=1)),
        "second": qcm(
            carnet("Chronique de Frère Anselme", "(inventée pour le jeu). « Le roi Clovis a été baptisé par Remi, évêque de Reims. Les historiens hésitent sur l'année : 496, 499 ou 508. La résidence du roi est à Paris à partir de 508, et il meurt en 511. »")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 1.",
            [("Pourquoi écrit-on « vers l'an 500 » ?", ["Les historiens ne sont pas d'accord sur l'année exacte", "Le baptême a eu lieu plusieurs fois", "Le texte est effacé", "Clovis n'a pas été baptisé"], 0, "496, 499 ou 508 selon les historiens."),
             ("Combien d'années séparent 508 de la mort de Clovis ?", ["3 ans", "8 ans", "11 ans", "1 an"], 0, "511 − 508 = 3."),
             ("Pourquoi le choix de Clovis facilite-t-il son pouvoir ?", ["Il obtient l'appui des évêques, déjà influents", "Il devient empereur", "Il évite la guerre pour toujours", "Il reçoit Rome"], 0, "Les Gallo-Romains sont déjà chrétiens.")],
            ["Les sources donnent trois dates différentes.", "Soustrais : 511 − 508.", "Les évêques sont influents dans les villes."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 1 ?", K4, [K3, K7, K6], pos=2)),
    }
    d["e1-2"] = {
        "mousse": ordre(
            "Remets les événements dans l'ordre, du plus ancien (en haut) au plus récent (en bas), avec les flèches ▲▼.",
            [("L'Empire romain disparaît en Occident", "476"), ("Clovis devient roi des Francs", "481"), ("Clovis est baptisé à Reims", "vers l'an 500")],
            ["Ouvre la fiche " + F + ".", "Compare les nombres : le plus petit est le plus ancien.", "« Vers 500 » vient après 481."]),
        "lieutenant": ordre(
            "Frère Anselme recopie la frise de la première page. Remets les cinq événements dans l'ordre chronologique, puis choisis la phrase de la fiche qui date la victoire de Soissons.",
            [("Victoire de Soissons", "486"), ("Baptême de Clovis à Reims", "vers l'an 500"), ("Victoire de Vouillé sur Alaric II", "507"), ("Paris, résidence principale", "508"), ("Mort de Clovis", "511")],
            ["Les dates sont données : compare-les.", "« Vers 500 » se place entre 486 et 507.", "La mort de Clovis vient en dernier."],
            J("Quelle phrase de la fiche date la victoire de Soissons ?", K3, [K5, K4, K6], pos=2)),
        "second": tri(
            "Frère Anselme classe les événements du règne de Clovis. Range chaque événement dans la bonne colonne, puis choisis la phrase de la fiche qui date la victoire de Vouillé.",
            [("avant", "Avant le baptême (vers 500)"), ("apres", "Après le baptême (vers 500)")],
            [("Victoire de Soissons sur Syagrius (486)", "avant"), ("Clovis devient roi des Francs (481)", "avant"), ("Fin de l'Empire romain d'Occident (476)", "avant"),
             ("Victoire de Vouillé sur Alaric II (507)", "apres"), ("Paris devient la résidence principale (508)", "apres"), ("Mort de Clovis (511)", "apres")],
            ["Compare chaque date avec 500.", "476, 481 et 486 sont avant.", "507, 508 et 511 sont après."],
            J("Quelle phrase de la fiche date la victoire de Vouillé ?", K5, [K3, K6, K4], pos=0)),
    }
    d["e1-3"] = {
        "mousse": assoc(
            "Relie chaque personnage à ce qu'il a fait : clique sur un nom à gauche, puis sur sa phrase à droite.",
            [("Clovis", "roi des Francs, baptisé à Reims"), ("Remi", "évêque de Reims, il baptise le roi"), ("Syagrius", "chef romain vaincu à Soissons")],
            ["Ouvre la fiche " + F + ".", "Un évêque est un chef religieux : c'est lui qui baptise.", "Syagrius est romain, pas franc."]),
        "lieutenant": qcm(
            carnet("Le récit du baptême", "(d'après Grégoire de Tours, évêque, fin du VIe siècle). « Le roi demanda le premier à être baptisé par l'évêque. » Grégoire écrit presque un siècle après les faits.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Qui raconte le baptême dans ce document ?", ["Grégoire de Tours", "Remi", "Clovis", "Syagrius"], 0, "Il écrit à la fin du VIe siècle."),
             ("Ce récit est-il un témoin direct du baptême ?", ["Non : il est écrit presque un siècle plus tard", "Oui : Grégoire était présent", "Oui : il est signé de Clovis", "On ne peut pas savoir"], 0, "C'est un témoignage tardif."),
             ("Qui baptise Clovis ?", ["L'évêque Remi", "Le pape Léon III", "Alcuin", "Syagrius"], 0, "Remi est l'évêque de Reims.")],
            ["Qui écrit ? Quand ?", "Presque un siècle après : est-ce un témoin direct ?", "L'évêque de Reims s'appelle Remi."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", K9, [K4, K7, K8], pos=0)),
        "second": vf(
            "Frère Anselme a noté six phrases sur Clovis. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui explique pourquoi le baptême compte pour le pouvoir de Clovis.",
            [("Clovis a été roi de 481 à 511.", True, "Trente ans de règne."), ("Syagrius était le roi des Francs.", False, "Dernier chef romain du nord de la Gaule."), ("Alaric II était roi des Wisigoths.", True, "Il est vaincu à Vouillé en 507."),
             ("Grégoire de Tours a vu le baptême de Clovis.", False, "Il écrit presque un siècle après."), ("Les Gallo-Romains sont déjà chrétiens.", True, "Clovis choisit la même religion."), ("Les évêques n'ont aucune influence.", False, "Ils sont les personnages les plus influents des villes.")],
            ["Clovis : 481 à 511.", "Syagrius est romain.", "Les évêques comptent dans les villes."],
            J("Quelle phrase de la fiche explique pourquoi le baptême compte pour le pouvoir de Clovis ?", K7, [K4, K9, K2], pos=3)),
    }
    d["e1-4"] = {
        "lieutenant": {
            "type": "plan", "titre": "Les royaumes après 476", "colonnes": 2,
            "cases": [{"libelle": "Le royaume du sud de la Gaule", "reponse": "les Wisigoths"}, {"libelle": "Le royaume de l'est", "reponse": "les Burgondes"}, {"libelle": "Le royaume du nord", "reponse": "les Francs"},
                      {"libelle": "La ville de l'évêque qui baptise Clovis", "reponse": "Reims"}, {"libelle": "Le roi wisigoth vaincu à Vouillé", "reponse": "Alaric II"}],
            "etiquettes": ["les Wisigoths", "les Burgondes", "les Francs", "Reims", "Alaric II", "les Huns", "Rome"],
            "consigne": "Frère Anselme dessine la carte des royaumes après la fin de l'Empire romain. Place chaque étiquette dans la bonne case. Deux étiquettes sont en trop. Puis choisis la phrase de la fiche qui situe les trois peuples.",
            "indices": ["Wisigoths au sud, Burgondes à l'est, Francs au nord.", "Reims est la ville du baptême.", "Vouillé : Alaric II."],
            "justification": J("Quelle phrase de la fiche situe les trois peuples ?", K2, [K1, K5, K7], pos=1)},
        "second": {
            "type": "plan", "titre": "Les lieux et les personnages de Clovis", "colonnes": 2,
            "cases": [{"libelle": "Victoire sur Syagrius en 486", "reponse": "Soissons"}, {"libelle": "Victoire sur Alaric II en 507", "reponse": "Vouillé"}, {"libelle": "Résidence principale à partir de 508", "reponse": "Paris"},
                      {"libelle": "Baptême vers l'an 500", "reponse": "Reims"}, {"libelle": "Dernier chef romain du nord de la Gaule", "reponse": "Syagrius"}, {"libelle": "Roi des Wisigoths vaincu en 507", "reponse": "Alaric II"}],
            "etiquettes": ["Soissons", "Vouillé", "Paris", "Reims", "Syagrius", "Alaric II", "Aix-la-Chapelle", "Charlemagne"],
            "consigne": "Frère Anselme complète sa carte des lieux et des personnages. Place chaque étiquette dans la bonne case. Deux étiquettes sont en trop. Puis choisis la phrase de la fiche qui situe la victoire de Soissons.",
            "indices": ["Soissons : 486. Vouillé : 507.", "Paris : à partir de 508.", "Aix-la-Chapelle et Charlemagne sont à la page suivante."],
            "justification": J("Quelle phrase de la fiche situe la victoire de Soissons ?", K3, [K5, K6, K4], pos=2)},
    }
    return d
