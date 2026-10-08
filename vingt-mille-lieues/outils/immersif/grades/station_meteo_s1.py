"""Salle 1 « L'abri météo » (fiche : thermometre)."""
from aide import *

F = "« Mesurer la température de l'air »"
T1 = "On mesure la température de l'air avec un thermomètre ou un capteur électronique, en degrés Celsius (°C)."
T2 = "Météo-France la mesure sous abri, à 1,50 m du sol, dans un abri blanc et percé d'ouvertures : l'air y circule, mais le capteur est protégé du rayonnement du soleil et de la pluie."
T3 = "Toutes les stations suivent les mêmes règles, fixées par l'Organisation météorologique mondiale."
T4 = "On lit la graduation qui correspond au sommet du liquide, les yeux à sa hauteur."
T5 = "Sous le zéro, les températures sont négatives : plus le nombre après le signe moins est grand, plus il fait froid (−6 °C est plus froid que −1 °C)."
T6 = "La température minimale est la plus basse de la journée, la maximale la plus haute."
T7 = "Le maximum n'a pas lieu à midi : il arrive souvent en milieu d'après-midi, quand le sol a chauffé toute la journée."


def instrument(nom, unite, mn, mx, pas, etiq, items, consigne, indices, j=None):
    b = {"type": "instrument", "instrument": nom, "unite": unite, "min": mn, "max": mx, "pas": pas, "etiquettes": etiq, "items": items, "consigne": consigne, "indices": list(indices)}
    if j:
        b["justification"] = j
    return b


def donnees(svg, bloc=None):
    d = {}
    d["e1-1"] = {
        "mousse": instrument("thermometre", "°C", 0, 30, 1, 5,
                             [{"libelle": "Lundi, 8 h", "mode": "lire", "valeur": 10}, {"libelle": "Lundi, 15 h", "mode": "lire", "valeur": 20}],
                             "Voici deux relevés du thermomètre de l'école. Regarde où s'arrête le liquide rouge et écris la température lue sous chaque thermomètre. Une petite graduation vaut <b>1 degré</b>.",
                             ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Les grands traits portent un nombre : 0, 5, 10, 15, 20…", "Le plus chaud est celui de l'après-midi."]),
        "lieutenant": instrument("thermometre", "°C", 0, 30, 0.5, 5,
                                 [{"libelle": "Jeudi, 8 h", "mode": "lire", "valeur": 8.5}, {"libelle": "Jeudi, 15 h", "mode": "lire", "valeur": 14.5}, {"libelle": "Règle : 11,5 °C", "mode": "regler", "valeur": 11.5, "depart": 5}],
                                 "Voici deux relevés de jeudi. Ici, une petite graduation vaut <b>0,5 °C</b> : écris la température avec une virgule si besoin. Pour le troisième, règle le liquide avec ▲ et ▼. Puis choisis la phrase de la fiche qui explique comment lire un thermomètre.",
                                 ["Entre deux grands traits (5 °C), il y a 10 petites graduations.", "Deux petites graduations font 1 degré.", "Lis la graduation au sommet du liquide."],
                                 J("Quelle phrase de la fiche explique comment lire un thermomètre ?", T4, [T1, T5, T6], pos=1)),
        "second": instrument("thermometre", "°C", -20, 40, 2, 10,
                             [{"libelle": "Un matin d'hiver", "mode": "lire", "valeur": -8}, {"libelle": "Un après-midi d'été", "mode": "lire", "valeur": 26}, {"libelle": "Règle : une nuit de gel à −12 °C", "mode": "regler", "valeur": -12, "depart": 0}],
                             "Voici deux relevés et un réglage. Ici, une petite graduation vaut <b>2 °C</b> : attention au signe <b>moins</b> sous zéro. Pour le troisième, règle le liquide avec ▲ et ▼. Puis choisis la phrase de la fiche qui explique les températures négatives.",
                             ["Repère le trait du 0.", "Sous le zéro, compte les graduations en descendant.", "Chaque petite graduation vaut 2 °C."],
                             J("Quelle phrase de la fiche explique les températures négatives ?", T5, [T4, T6, T7], pos=2)),
    }
    d["e1-2"] = {
        "mousse": qcm(
            "Le thermomètre a été retrouvé en plein soleil. Lis la question, clique sur la bonne réponse, puis vérifie.",
            [("Pour mesurer la température de l'air, le thermomètre doit être…", ["à l'ombre, dans son abri", "en plein soleil", "posé sur le sol"], 0, "Au soleil, il chauffe lui-même.")],
            ["Ouvre la fiche " + F + ".", "Au soleil, un objet chauffe beaucoup.", "L'abri est blanc."]),
        "lieutenant": vf(
            "Tiago a noté cinq phrases sur l'abri météo. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui décrit l'abri.",
            [("L'abri est blanc et percé d'ouvertures.", True, "L'air y circule."), ("Le thermomètre est placé au ras du sol.", False, "À 1,50 m du sol."), ("Le capteur est protégé du soleil et de la pluie.", True, "Par l'abri."),
             ("Toutes les stations suivent les mêmes règles.", True, "Fixées par l'Organisation météorologique mondiale."), ("Le thermomètre se met en plein soleil pour être plus précis.", False, "Il indiquerait plus que la température de l'air.")],
            ["Un abri blanc renvoie la lumière.", "La hauteur est de 1,50 m.", "Pour la justification : cherche la phrase qui nomme Météo-France."],
            J("Quelle phrase de la fiche décrit l'abri météo ?", T2, [T3, T1, T7], pos=1)),
        "second": qcm(
            carnet("Rapport de Tiago", "(inventé pour le jeu). Deux élèves comparent leurs relevés. Léo mesure sous abri à 1,50 m ; Hugo pose son thermomètre sur le muret, en plein soleil. Léo relève 18 °C, Hugo 27 °C.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Quelle mesure est la plus fiable ?", ["Celle de Léo, sous abri", "Celle de Hugo, au soleil", "Les deux", "Aucune"], 0, "Le soleil fausse la mesure."),
             ("Pourquoi les deux mesures ne sont-elles pas comparables ?", ["Elles ne suivent pas les mêmes règles de mesure", "Les élèves sont différents", "Les thermomètres sont en verre", "Il fait nuit"], 0, "Toutes les stations suivent les mêmes règles."),
             ("Quel est l'écart entre les deux mesures ?", ["9 °C", "18 °C", "27 °C", "45 °C"], 0, "27 − 18 = 9.")],
            ["Un thermomètre au soleil chauffe lui-même.", "Pour comparer, il faut les mêmes règles.", "Soustrais 18 de 27."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", T3, [T2, T4, T6], pos=1)),
    }
    d["e1-3"] = {
        "mousse": ordre(
            "Le cahier de relevés est mélangé. Range les températures de la plus froide (en haut) à la plus chaude (en bas) avec les flèches ▲ ▼.",
            [("5 °C", "lundi, 8 h"), ("12 °C", "lundi, midi"), ("19 °C", "lundi, 15 h")],
            ["Ouvre la fiche " + F + ".", "Compare les nombres : le plus petit est le plus froid.", "19 est le plus grand."]),
        "lieutenant": ordre(
            "Lina a noté cinq températures de la semaine, avec des signes moins. Range-les de la plus froide (en haut) à la plus chaude (en bas), puis choisis la phrase de la fiche qui explique l'ordre des températures négatives.",
            [("−9 °C", "une nuit de janvier"), ("−2 °C", "un matin de gel"), ("0 °C", "l'eau commence à geler"), ("6 °C", "un matin d'avril"), ("17 °C", "un après-midi de mai")],
            ["Les températures négatives sont les plus froides.", "−9 est plus bas que −2.", "Le plus chaud est 17 °C."],
            J("Quelle phrase de la fiche explique l'ordre des températures négatives ?", T5, [T4, T6, T3], pos=0)),
        "second": ordre(
            "Lina range des mesures d'une même journée. Range-les de la plus froide (en haut) à la plus chaude (en bas), puis choisis la phrase de la fiche qui explique pourquoi le maximum n'est pas à midi.",
            [("−3 °C", "minimum, à 6 h"), ("2 °C", "à 9 h"), ("9 °C", "à midi"), ("12 °C", "à 17 h"), ("14 °C", "maximum, à 15 h")],
            ["Compare d'abord les signes.", "Le maximum est atteint en milieu d'après-midi.", "−3 est le plus bas."],
            J("Quelle phrase de la fiche explique pourquoi le maximum n'est pas à midi ?", T7, [T6, T5, T2], pos=1)),
    }
    d["e1-4"] = {
        "lieutenant": tri(
            "Lina a noté comment chaque camarade a mesuré la température. Range chaque mesure : fiable ou faussée ? Puis choisis la phrase de la fiche qui donne la hauteur de mesure.",
            [("fiable", "Mesure fiable"), ("faussee", "Mesure faussée")],
            [("Zoé lit le thermomètre sous abri, à 1,50 m.", "fiable"), ("Karim note l'heure à côté de chaque mesure.", "fiable"), ("Iris attend un peu avant de lire, sans toucher le thermomètre.", "fiable"),
             ("Paul pose le thermomètre sur le sol en plein soleil.", "faussee"), ("Alix tient le thermomètre serré dans sa main.", "faussee"), ("Nora accroche le thermomètre contre un mur chauffé.", "faussee")],
            ["Le soleil, la main et un mur chaud faussent la mesure.", "La mesure fiable respecte les règles de la station.", "Pour la justification : cherche la phrase qui cite 1,50 m."],
            J("Quelle phrase de la fiche donne la hauteur de mesure ?", T2, [T4, T3, T7], pos=2)),
        "second": tri(
            "Lina classe des affirmations sur la température. Range chaque carte : la fiche l'affirme, ou elle ne l'affirme pas. Puis choisis la phrase de la fiche qui définit minimum et maximum.",
            [("oui", "La fiche l'affirme"), ("non", "La fiche ne l'affirme pas")],
            [("La température se mesure en degrés Celsius.", "oui"), ("Le maximum arrive souvent en milieu d'après-midi.", "oui"), ("−6 °C est plus froid que −1 °C.", "oui"),
             ("Le thermomètre se lit à midi seulement.", "non"), ("La température se mesure en kilomètres par heure.", "non"), ("Le minimum est la valeur la plus haute.", "non")],
            ["Les degrés Celsius sont l'unité.", "Le maximum est la valeur la plus haute.", "Plus le nombre après le moins est grand, plus il fait froid."],
            J("Quelle phrase de la fiche définit minimum et maximum ?", T6, [T7, T5, T1], pos=1)),
    }
    return d
