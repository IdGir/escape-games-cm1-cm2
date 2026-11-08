"""Salle 1 « La ligne de départ » : grades mousse, lieutenant, second (fiche : distance)."""
from aide import *

FICHE = "« Mesurer une distance »"
P_DEF = "La distance parcourue est la longueur entre ces deux points, mesurée le long du trajet."
P_INSTR = "On choisit l'instrument selon la longueur à mesurer : la règle graduée pour quelques centimètres, le mètre ruban pour quelques mètres, le décamètre pour quelques dizaines de mètres."
P_ROUE = "Pour une très longue distance, on pousse une roue de mesure qui compte les mètres en roulant."
P_REPORT = "Quand la longueur dépasse celle du ruban, on le reporte plusieurs fois bout à bout, puis on additionne."
P_SOUS = "Si le départ n'est pas au zéro du ruban, la distance parcourue est égale à la graduation de l'arrivée moins la graduation du départ."
P_UNITE = "Une mesure s'écrit toujours avec son unité : un nombre seul ne veut rien dire."
P_CONV = "On utilise aussi le kilomètre (1 km = 1 000 m), le décamètre (1 dam = 10 m), le centimètre (1 m = 100 cm) et le millimètre (1 cm = 10 mm)."
P_COMP = "Pour comparer deux longueurs, on les écrit d'abord dans la même unité : 1 km et 20 m, c'est 1 020 m."


def donnees(svg, bloc=None):
    d = {}
    d["e1-1"] = {
        "mousse": tri(
            "Margaux range ses instruments. Range chaque longueur sous le bon instrument. Clique sur une carte, puis sur une colonne.",
            [("regle", "Règle"), ("ruban", "Mètre ruban"), ("deca", "Décamètre")],
            [("un crayon", "regle"), ("une caisse à savon", "ruban"), ("la piste de 50 m", "deca"), ("une feuille", "regle")],
            ["Ouvre la fiche " + FICHE + " dans la Bibliothèque.", "La règle sert pour les petites choses.", "Le décamètre est un très long ruban."]),
        "lieutenant": tri(
            "Margaux prépare le matériel pour toute la journée. Range chaque longueur sous l'instrument le plus adapté, puis choisis la phrase de la fiche qui justifie le choix pour la route d'accès.",
            [("regle", "Règle graduée"), ("ruban", "Mètre ruban"), ("deca", "Décamètre"), ("roue", "Roue de mesure")],
            [("l'épaisseur d'un dossard", "regle"), ("la longueur d'une gomme", "regle"), ("la largeur de la caisse à savon", "ruban"), ("la hauteur de la banderole", "ruban"),
             ("la ligne droite (30 m)", "deca"), ("l'écart entre deux plots (15 m)", "deca"), ("la route d'accès (2 km)", "roue"), ("un tour du circuit (400 m)", "roue")],
            ["Compare chaque longueur avec la longueur de l'instrument.", "Le décamètre sert pour quelques dizaines de mètres.", "Pour la justification : cherche la phrase sur les très longues distances."],
            J("Quelle phrase de la fiche justifie l'instrument choisi pour la route d'accès ?", P_ROUE, [P_SOUS, P_UNITE, P_DEF], pos=2)),
        "second": ordre(
            "Margaux rédige le protocole pour mesurer la ligne droite, plus longue que son décamètre de 10 m. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche qui justifie la méthode.",
            ["Repérer la ligne de départ et la ligne d'arrivée.", "Poser le zéro du décamètre sur la ligne de départ.", "Dérouler le ruban en entier et marquer le bout d'un plot.",
             "Reporter le ruban à partir du plot, autant de fois que nécessaire.", "Lire la graduation au niveau de la ligne d'arrivée.",
             "Additionner les reports et la dernière lecture, puis écrire le résultat avec l'unité."],
            ["On ne peut rien mesurer sans savoir où la distance commence et finit.", "Chaque report commence là où le précédent s'arrête.", "Le calcul et l'unité viennent à la fin."],
            J("Quelle phrase de la fiche justifie cette méthode ?", P_REPORT, [P_INSTR, P_SOUS, P_CONV], pos=1)),
    }
    d["e1-2"] = {
        "mousse": vf(
            "Margaux a écrit trois phrases dans son carnet. Pour chaque phrase, choisis vrai ou faux.",
            [("La distance parcourue se mesure du départ à l'arrivée.", True, "C'est la longueur entre ces deux points."),
             ("On mesure une longueur en secondes.", False, "Une longueur se mesure en mètres ou en centimètres."),
             ("Il faut écrire l'unité après le nombre.", True, "On écrit par exemple 15 m.")],
            ["Ouvre la fiche " + FICHE + ".", "La seconde sert à mesurer une durée.", "« 15 » tout seul ne dit pas si ce sont des mètres."]),
        "lieutenant": qcm(
            "Margaux vérifie les conversions de ses commissaires. Réponds aux quatre questions, puis choisis la phrase de la fiche qui permet de comparer des longueurs.",
            [("3 km et 400 m, cela fait...", ["340 m", "3 400 m", "34 000 m", "3 004 m"], 1, "3 km = 3 000 m ; 3 000 + 400 = 3 400 m."),
             ("2 m et 5 cm, cela fait...", ["25 cm", "250 cm", "205 cm", "2 005 cm"], 2, "2 m = 200 cm ; 200 + 5 = 205 cm."),
             ("Quelle longueur est la plus courte ?", ["1 km", "990 m", "100 dam", "1 000 m"], 1, "1 km = 100 dam = 1 000 m : seule 990 m est plus courte."),
             ("4 dam, cela fait...", ["4 m", "400 m", "40 m", "40 cm"], 2, "1 dam = 10 m.")],
            ["Convertis tout en mètres (ou en centimètres) avant de comparer.", "1 km = 1 000 m ; 1 dam = 10 m ; 1 m = 100 cm.", "Pour la justification : cherche « même unité »."],
            J("Quelle phrase de la fiche permet de comparer des longueurs ?", P_COMP, [P_DEF, P_ROUE, P_UNITE], pos=0)),
        "second": vf(
            "Margaux relit le carnet d'un commissaire débutant. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui corrige la note « piste : 50 ».",
            [("« Piste : 50 » est une mesure complète.", False, "On ne sait pas si ce sont des mètres, des centimètres ou des kilomètres."),
             ("Si le départ est à 3 m sur le ruban et l'arrivée à 18 m, la distance est de 21 m.", False, "C'est 18 − 3 = 15 m."),
             ("Un décamètre déroulé 5 fois en entier mesure 50 m.", True, "5 × 10 m = 50 m."),
             ("1 km et 20 m est plus long que 1 010 m.", True, "1 km et 20 m = 1 020 m."),
             ("Pour la route d'accès de 2 km, la règle de 30 cm est l'instrument le plus adapté.", False, "On prend une roue de mesure, qui compte les mètres en roulant.")],
            ["Méfie-toi des phrases presque justes : vérifie chaque calcul.", "Arrivée moins départ, jamais arrivée plus départ.", "Pour la justification : cherche la phrase sur l'unité."],
            J("Quelle phrase de la fiche corrige la note « piste : 50 » ?", P_UNITE, [P_REPORT, P_COMP, P_INSTR], pos=3)),
    }
    d["e1-3"] = {
        "mousse": code(
            "Margaux a posé son ruban le long de la piste. Le départ est au drapeau vert, l'arrivée au damier. Compte les mètres entre les deux." + svg("e1-3", "matelot"),
            [("Distance parcourue (en m)", "15", 2)],
            ["Ouvre la fiche " + FICHE + " : regarde le schéma du ruban.", "Le départ est à 3, l'arrivée à 18.", "18 moins 3, cela fait 15."]),
        "lieutenant": code(
            "La piste de la descente est plus longue : Margaux reporte son décamètre de 10 m sept fois en entier, puis il reste 3 m jusqu'à l'arrivée. Calcule la longueur en mètres, puis en centimètres, et choisis la phrase de la fiche qui justifie le calcul.",
            [("Longueur de la descente (en m)", "73", 2), ("La même longueur (en cm)", "7300", 4)],
            ["Sept reports de 10 m : 70 m.", "Ajoute les 3 m qui restent.", "1 m = 100 cm : multiplie par 100."],
            J("Quelle phrase de la fiche justifie ce calcul ?", P_REPORT, [P_SOUS, P_ROUE, P_DEF], pos=0)),
        "second": code(
            "Sur le ruban ci-dessous, la voiture A est partie du drapeau vert et a franchi le damier. "
            + carnet("Carnet de Margaux", "(mesure inventée pour le jeu) : la voiture B, partie de la même ligne, s'est arrêtée 2 m et 40 cm avant le damier.")
            + "Calcule la distance de chaque voiture, puis choisis la phrase de la fiche qui permet de lire la distance de la voiture A." + svg("e1-3", "matelot"),
            [("Distance de la voiture A (en m)", "15", 2), ("Distance de la voiture B (en cm)", "1260", 4)],
            ["Le départ n'est pas au zéro : arrivée moins départ.", "15 m = 1 500 cm.", "1 500 cm − 240 cm."],
            J("Quelle phrase de la fiche permet de lire la distance de la voiture A ?", P_SOUS, [P_REPORT, P_UNITE, P_COMP], pos=2)),
    }
    d["e1-4"] = {
        "lieutenant": assoc(
            "Margaux recolle les fiches de conversion de son carnet. Relie chaque longueur à la longueur égale, puis choisis la phrase de la fiche qui donne les équivalences.",
            [("2 km et 50 m", "2 050 m"), ("3 dam", "30 m"), ("2 m et 50 cm", "250 cm"), ("4 cm et 5 mm", "45 mm"), ("1 km et 500 m", "1 500 m")],
            ["1 km = 1 000 m.", "1 dam = 10 m ; 1 cm = 10 mm.", "Pour la justification : cherche la phrase qui cite le kilomètre et le millimètre."],
            J("Quelle phrase de la fiche donne ces équivalences ?", P_CONV, [P_COMP, P_DEF, P_INSTR], pos=1)),
        "second": qcm(
            carnet("Fiches des circuits", "(longueurs inventées pour le jeu). Circuit vert : 1 km et 20 m. Circuit bleu : 1 010 m. Circuit rouge : 98 dam. Circuit jaune : 102 500 cm.")
            + "Réponds aux trois questions, puis choisis la phrase de la fiche qui explique la méthode.",
            [("Quel circuit est le plus long ?", ["Le vert", "Le bleu", "Le rouge", "Le jaune"], 3, "102 500 cm = 1 025 m."),
             ("Quel circuit est le plus court ?", ["Le vert", "Le rouge", "Le bleu", "Le jaune"], 1, "98 dam = 980 m."),
             ("Quel est l'écart entre le circuit vert et le circuit bleu ?", ["10 m", "1 m", "100 m", "20 m"], 0, "1 020 m − 1 010 m = 10 m.")],
            ["Convertis les quatre longueurs en mètres.", "1 dam = 10 m ; 100 cm = 1 m.", "Pour la justification : cherche « même unité »."],
            J("Quelle phrase de la fiche explique la méthode ?", P_COMP, [P_ROUE, P_SOUS, P_DEF], pos=0)),
    }
    return d
