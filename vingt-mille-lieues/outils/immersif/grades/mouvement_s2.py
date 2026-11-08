"""Salle 2 « Le stand des chronométreurs » : grades mousse, lieutenant, second (fiche : duree)."""
from aide import *

FICHE = "« Mesurer une durée »"
P_INSTANT = "Un instant est un moment précis, comme l'heure du départ."
P_DEF = "Une durée est l'intervalle entre deux instants : pour la connaître, il faut l'instant du départ et l'instant de l'arrivée."
P_INSTR = "L'horloge donne des instants ; le chronomètre et le sablier mesurent des durées."
P_CHRONO = "On remet le chronomètre à zéro, on le déclenche au moment exact du départ et on l'arrête quand l'objet franchit la ligne d'arrivée."
P_VERIF = "Refaire la mesure permet de vérifier : un chronométreur qui réagit en retard fausse le résultat."
P_RONDE = "Pour calculer une durée, on peut passer par une heure ronde : de 10 h 50 à 11 h 05, il y a 10 minutes puis 5 minutes, soit 15 minutes."
P_CONV = "Une heure vaut 60 minutes et une minute vaut 60 secondes : 2 min 30 s font 150 s, et 1 h 15 min font 75 min."
P_UNITE = "Pour comparer deux durées, on les convertit d'abord dans la même unité."


def donnees(svg, bloc=None):
    d = {}
    d["e2-1"] = {
        "mousse": ordre(
            "Yanis explique comment on chronomètre sa descente. Remets les trois étapes dans l'ordre.",
            ["Remettre le chronomètre à zéro.", "Appuyer au départ de la caisse.", "Appuyer de nouveau à l'arrivée et lire la durée."],
            ["Ouvre la fiche " + FICHE + " dans la Bibliothèque.", "Avant tout, l'écran affiche zéro.", "On arrête le chronomètre à l'arrivée."]),
        "lieutenant": ordre(
            "Yanis forme deux nouveaux chronométreurs. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche qui décrit le bon geste.",
            ["Se placer à côté de la ligne d'arrivée, en voyant la ligne de départ.", "Remettre le chronomètre à zéro.", "Le déclencher au moment exact du signal de départ.",
             "L'arrêter quand l'avant de la caisse franchit la ligne d'arrivée.", "Noter la durée lue, avec son unité.", "Comparer avec la mesure de l'autre chronométreur."],
            ["Le chronométreur doit voir le départ et l'arrivée.", "Le zéro vient avant le départ.", "Pour la justification : cherche la phrase qui commence par « On remet »."],
            J("Quelle phrase de la fiche décrit le bon geste ?", P_CHRONO, [P_INSTANT, P_RONDE, P_UNITE], pos=1)),
        "second": ordre(
            carnet("Feuille du stand", "(horaires inventés pour le jeu) : arrivée de Salomé 11 h 05 ; ouverture du stand 9 h 30 ; départ de Yanis 10 h 15 ; arrivée de Yanis 10 h 40 ; départ de Salomé 10 h 50.")
            + "Range ces cinq instants du plus tôt au plus tard, puis choisis la phrase de la fiche qui dit ce qu'est un instant.",
            [("9 h 30", "ouverture du stand"), ("10 h 15", "départ de Yanis"), ("10 h 40", "arrivée de Yanis"), ("10 h 50", "départ de Salomé"), ("11 h 05", "arrivée de Salomé")],
            ["Compare d'abord les heures, puis les minutes.", "10 h 40 vient avant 10 h 50.", "Pour la justification : un instant, c'est un moment précis."],
            J("Quelle phrase de la fiche dit ce qu'est un instant ?", P_INSTANT, [P_DEF, P_INSTR, P_VERIF], pos=0)),
    }
    d["e2-2"] = {
        "mousse": vf(
            "Yanis a écrit trois phrases sur son tableau. Pour chaque phrase, choisis vrai ou faux.",
            [("Le chronomètre mesure une durée.", True, "Il mesure le temps entre le départ et l'arrivée."),
             ("« 10 h 15 » est une durée.", False, "C'est un instant : une heure précise."),
             ("Un sablier mesure toujours la même durée.", True, "Quand le sable est tombé, la durée est passée.")],
            ["Ouvre la fiche " + FICHE + ".", "Une heure lue sur l'horloge est un instant.", "Le sablier coule toujours de la même façon."]),
        "lieutenant": qcm(
            "Yanis interroge ses chronométreurs. Réponds aux quatre questions, puis choisis la phrase de la fiche qui définit une durée.",
            [("Pour connaître la durée de la descente, il faut...", ["l'heure d'arrivée seulement", "l'instant du départ et l'instant de l'arrivée", "la longueur de la piste", "l'heure qu'il est"], 1, "Une durée est l'intervalle entre deux instants."),
             ("1 min 45 s, cela fait...", ["145 s", "105 s", "85 s", "60 s"], 1, "60 s + 45 s = 105 s."),
             ("2 h, cela fait...", ["120 min", "200 min", "60 min", "20 min"], 0, "2 × 60 min = 120 min."),
             ("L'écran affiche 02:10. La durée est de...", ["2 min 10 s, soit 130 s", "210 s", "2 h 10 min", "21 s"], 0, "02:10 se lit deux minutes et dix secondes.")],
            ["Une minute vaut 60 secondes.", "Une heure vaut 60 minutes.", "Pour la justification : cherche le mot « intervalle »."],
            J("Quelle phrase de la fiche définit une durée ?", P_DEF, [P_INSTANT, P_INSTR, P_CHRONO], pos=2)),
        "second": code(
            carnet("Registre de la matinée", "(horaires inventés pour le jeu) : premier départ à 9 h 35 ; dernière arrivée à 11 h 10. La pause de midi commence 25 min après la dernière arrivée.")
            + "Calcule la durée totale des courses, en minutes, puis l'heure de la pause (heures et minutes), et choisis la phrase de la fiche qui aide à calculer.",
            [("Durée des courses (en min)", "95", 2), ("Pause : heures", "11", 2), ("Pause : minutes", "35", 2)],
            ["De 9 h 35 à 10 h, il y a 25 min.", "De 10 h à 11 h 10, il y a 70 min.", "11 h 10 + 25 min = 11 h 35."],
            J("Quelle phrase de la fiche aide à faire ce calcul ?", P_RONDE, [P_CONV, P_DEF, P_VERIF], pos=0)),
    }
    d["e2-3"] = {
        "mousse": code(
            tableau("Registre des départs (horaires inventés pour le jeu)", ["Pilote", "Départ", "Arrivée"], [["Yanis", "10 h 00 min", "10 h 20 min"]])
            + "Combien de minutes a duré l'essai de Yanis ?",
            [("Durée de l'essai (en min)", "20", 2)],
            ["Ouvre la fiche " + FICHE + " : regarde le schéma des deux instants.", "Compte de 0 à 20 minutes.", "Il s'est écoulé 20 minutes."]),
        "lieutenant": code(
            tableau("Registre des essais (durées inventées pour le jeu)", ["Essai", "Mesure"],
                    [["Descente de Yanis", "3 min 15 s"], ["Séance d'essais", "1 h 40 min"], ["Tour de Salomé", "de 9 h 45 min à 10 h 20 min"]])
            + "Convertis ou calcule chaque durée dans l'unité demandée, puis choisis la phrase de la fiche qui aide pour le tour de Salomé.",
            [("Descente de Yanis (en s)", "195", 3), ("Séance d'essais (en min)", "100", 3), ("Tour de Salomé (en min)", "35", 2)],
            ["3 min = 180 s.", "1 h = 60 min.", "Pour Salomé, passe par 10 h."],
            J("Quelle phrase de la fiche aide pour le tour de Salomé ?", P_RONDE, [P_INSTANT, P_CHRONO, P_UNITE], pos=1)),
        "second": qcm(
            carnet("Deux chronométreurs, une même descente", "(mesures inventées pour le jeu). Chronométreur A : 48 s. Chronométreur B : 50 s. B a appuyé après avoir entendu le signal de départ ; A regardait le drapeau.")
            + "Réponds aux trois questions, puis choisis la phrase de la fiche qui explique pourquoi on refait la mesure.",
            [("Quelle mesure est sans doute la plus juste ?", ["Celle de A", "Celle de B", "Les deux sont fausses", "On ne peut rien dire"], 0, "B a déclenché en retard : sa durée est trop longue."),
             ("Quel est l'écart entre les deux mesures ?", ["2 s", "98 s", "1 s", "20 s"], 0, "50 s − 48 s = 2 s."),
             ("Que faire pour vérifier ?", ["Garder la plus grande", "Refaire la mesure", "Faire la moyenne avec l'heure de départ", "Ne rien noter"], 1, "On refait la mesure sur une autre descente.")],
            ["Celui qui déclenche en retard trouve une durée trop longue.", "Fais une soustraction pour l'écart.", "Pour la justification : cherche « vérifier »."],
            J("Quelle phrase de la fiche explique pourquoi on refait la mesure ?", P_VERIF, [P_CHRONO, P_DEF, P_INSTR], pos=2)),
    }
    d["e2-4"] = {
        "lieutenant": tri(
            "Les étiquettes du tableau d'affichage sont tombées. Range chaque étiquette, puis choisis la phrase de la fiche qui justifie le classement de l'horloge.",
            [("instant", "Un instant"), ("duree", "Une durée")],
            [("l'heure lue sur la grande horloge : 10 h 15", "instant"), ("midi, heure limite", "instant"), ("le signal du départ, à 10 h 50", "instant"),
             ("le temps du sablier : 3 min", "duree"), ("le temps de la descente : 48 s", "duree"), ("de 10 h 50 à 11 h 05 : 15 min", "duree"), ("la pause de 25 min", "duree")],
            ["Un instant répond à « à quelle heure ? ».", "Une durée répond à « combien de temps ? ».", "Pour la justification : cherche la phrase qui parle de l'horloge."],
            J("Quelle phrase de la fiche justifie le classement de l'horloge ?", P_INSTR, [P_DEF, P_RONDE, P_VERIF], pos=0)),
        "second": assoc(
            "Yanis prépare les fiches de conversion du stand. Relie chaque durée à la durée égale, puis choisis la phrase de la fiche qui donne la règle.",
            [("90 s", "1 min 30 s"), ("2 h", "120 min"), ("150 s", "2 min 30 s"), ("75 min", "1 h 15 min"), ("3 600 s", "1 h")],
            ["1 min = 60 s ; 1 h = 60 min.", "Une heure, c'est 60 fois 60 secondes.", "Pour la justification : cherche « une heure vaut »."],
            J("Quelle phrase de la fiche donne la règle de conversion ?", P_CONV, [P_UNITE, P_RONDE, P_INSTANT], pos=3)),
    }
    return d
