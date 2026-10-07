"""Salle 3 « Le pluviomètre » (fiche : pluie)."""
from aide import *
from station_meteo_s1 import instrument

F = "« Mesurer la pluie avec un pluviomètre »"
P1 = "Le pluviomètre mesure la hauteur de précipitations, en millimètres : c'est l'épaisseur de la couche d'eau qui couvrirait un sol plat si rien ne s'écoulait ni ne s'évaporait."
P2 = "1 mm sur 1 m² = 1 litre, car 1 mm × 1 m² = 1 dm³."
P3 = "Pour connaître le volume tombé sur une surface, on multiplie : 7 mm sur une cour de 200 m² font 7 × 200 = 1 400 litres."
P4 = "On le place en terrain dégagé : un arbre ou un mur arrête ou renvoie la pluie."
P5 = "On le lit à heure fixe (souvent le matin, pour les 24 heures écoulées), puis on le vide ; sinon, on lirait la somme de plusieurs jours."
P6 = "Le cumul est la somme des hauteurs relevées sur une période : semaine, mois, année."
P7 = "Il permet de comparer des périodes ou des lieux."


def donnees(svg, bloc=None):
    d = {}
    d["e3-1"] = {
        "mousse": instrument("pluviometre", "mm", 0, 20, 1, 5,
                             [{"libelle": "Mardi matin", "mode": "lire", "valeur": 4}, {"libelle": "Mercredi matin", "mode": "lire", "valeur": 9}],
                             "Voici deux relevés du pluviomètre. Regarde le haut de l'eau et écris la hauteur de pluie en <b>millimètres</b>. Une petite graduation vaut <b>1 mm</b>.",
                             ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Les grands traits portent 0, 5, 10, 15 et 20.", "Compte les petits traits au-dessus du grand trait."]),
        "lieutenant": instrument("pluviometre", "mm", 0, 20, 0.5, 5,
                                 [{"libelle": "Lundi matin", "mode": "lire", "valeur": 6.5}, {"libelle": "Mardi matin", "mode": "lire", "valeur": 11}, {"libelle": "Règle : 14,5 mm", "mode": "regler", "valeur": 14.5, "depart": 10}],
                                 "Lis les deux premiers pluviomètres. Ici, une petite graduation vaut <b>0,5 mm</b>. Pour le troisième, règle le niveau d'eau avec ▲ et ▼. Puis choisis la phrase de la fiche qui définit ce que mesure un pluviomètre.",
                                 ["Entre deux grands traits (5 mm), il y a 10 petites graduations.", "Deux petites graduations font 1 mm.", "14,5 mm : un petit trait sous le 15."],
                                 J("Quelle phrase de la fiche définit ce que mesure un pluviomètre ?", P1, [P2, P4, P6], pos=1)),
        "second": instrument("pluviometre", "mm", 0, 30, 0.5, 5,
                             [{"libelle": "Un jour d'orage", "mode": "lire", "valeur": 18.5}, {"libelle": "La semaine d'automne", "mode": "lire", "valeur": 23}, {"libelle": "Règle : 27,5 mm", "mode": "regler", "valeur": 27.5, "depart": 20}],
                             "Lis les deux premiers pluviomètres : ici, une petite graduation vaut <b>0,5 mm</b>. Pour le troisième, règle le niveau d'eau avec ▲ et ▼. Puis choisis la phrase de la fiche qui explique pourquoi on lit le pluviomètre à heure fixe.",
                             ["Entre deux grands traits (5 mm), il y a 10 petites graduations.", "23 mm : trois grands traits et demi.", "27,5 mm : un petit trait sous le 28."],
                             J("Quelle phrase de la fiche explique pourquoi on lit à heure fixe ?", P5, [P1, P3, P7], pos=2)),
    }
    d["e3-2"] = {
        "mousse": qcm(
            "Tiago te pose une question sur son pluviomètre. Clique sur la bonne réponse, puis vérifie.",
            [("Dans quelle unité lit-on une hauteur de pluie ?", ["en millimètres (mm)", "en degrés (°C)", "en kilomètres par heure (km/h)"], 0, "On mesure une hauteur d'eau.")],
            ["Ouvre la fiche " + F + ".", "La règle graduée est en millimètres.", "Les degrés mesurent la température."]),
        "lieutenant": vf(
            "Tiago a noté cinq phrases sur la pluie. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui donne l'équivalent de 1 mm en litres.",
            [("1 mm de pluie sur 1 m² représente 1 litre.", True, "1 mm × 1 m² = 1 dm³."), ("Le pluviomètre se place sous un arbre pour le protéger.", False, "Un arbre arrête la pluie."), ("On le lit à heure fixe, puis on le vide.", True, "Sinon, on lirait la somme de plusieurs jours."),
             ("Le pluviomètre mesure la température.", False, "Il mesure la hauteur de pluie."), ("5 mm de pluie sur 10 m² font 50 litres.", True, "5 × 10 = 50.")],
            ["1 mm = 1 litre par m².", "Un arbre ou un mur fausse la mesure.", "Pour la justification : cherche la phrase avec « 1 dm³ »."],
            J("Quelle phrase de la fiche donne l'équivalent de 1 mm en litres ?", P2, [P1, P3, P5], pos=1)),
        "second": qcm(
            carnet("Relevé de la cour", "(inventé pour le jeu). Un matin, le pluviomètre indique 4,5 mm. La cour de l'école mesure 200 m². Rappel : 1 mm sur 1 m² = 1 litre.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 1.",
            [("Combien de litres tombent sur 1 m² ?", ["4,5 litres", "45 litres", "0,45 litre", "4 litres"], 0, "1 mm = 1 litre par m²."),
             ("Combien de litres tombent sur la cour de 200 m² ?", ["900 litres", "200 litres", "450 litres", "9 000 litres"], 0, "4,5 × 200 = 900."),
             ("Pourquoi vide-t-on le pluviomètre après la lecture ?", ["Pour ne pas additionner la pluie de plusieurs jours", "Pour arroser les plantes", "Pour éviter le gel", "Parce qu'il est plein"], 0, "Sinon on lirait une somme.")],
            ["1 mm sur 1 m² : 1 litre.", "Multiplie 4,5 par 200.", "Le pluviomètre se lit à heure fixe, puis se vide."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 1 ?", P2, [P3, P5, P6], pos=2)),
    }
    d["e3-3"] = {
        "mousse": ordre(
            "Range les jours du plus sec (en haut) au plus arrosé (en bas) avec les flèches ▲ ▼.",
            ["Lundi : 0 mm", "Mardi : 4 mm", "Mercredi : 9 mm"],
            ["Ouvre la fiche " + F + ".", "Le jour le plus sec n'a pas de pluie.", "9 est le plus grand."]),
        "lieutenant": ordre(
            "Tiago range des pluies, parfois données en litres par mètre carré. Convertis-les en millimètres, puis range-les de la plus faible (en haut) à la plus forte (en bas). Puis choisis la phrase de la fiche qui justifie la conversion.",
            ["Une bruine : 1 mm", "Mardi : 4,5 mm", "Mercredi : 8 litres tombés sur 1 m²", "Jeudi : 11 mm", "Un orage : 20 litres tombés sur 1 m²"],
            ["8 litres sur 1 m² = 8 mm.", "20 litres sur 1 m² = 20 mm.", "Ordre : 1 ; 4,5 ; 8 ; 11 ; 20."],
            J("Quelle phrase de la fiche justifie la conversion litres par m² en mm ?", P2, [P1, P3, P6], pos=0)),
        "second": ordre(
            "Tiago range des pluies en mm et en litres sur des surfaces différentes. Pour chacune, calcule le nombre de litres, puis range de la plus petite (en haut) à la plus grande quantité d'eau (en bas), puis choisis la phrase de la fiche qui donne la méthode.",
            ["3 mm sur 10 m² : 30 litres", "5 mm sur 10 m² : 50 litres", "2 mm sur 100 m² : 200 litres", "7 mm sur 100 m² : 700 litres", "7 mm sur 200 m² : 1 400 litres"],
            ["Multiplie les mm par les m².", "30 ; 50 ; 200 ; 700 ; 1 400.", "1 mm sur 1 m² = 1 litre."],
            J("Quelle phrase de la fiche donne la méthode de calcul ?", P3, [P2, P1, P6], pos=2)),
    }
    d["e3-4"] = {
        "lieutenant": code(
            "Le cahier de Tiago indique pour la semaine : lundi 2 mm, mardi 0 mm, mercredi 5 mm, jeudi 9 mm, vendredi 4 mm. Ouvre le cadenas avec deux nombres : le cumul de la semaine et le nombre de litres tombés mercredi sur un potager de 15 m².",
            [("Cumul de la semaine (en mm)", "20", 3), ("Litres tombés mercredi sur 15 m²", "75", 3)],
            ["Cumuler, c'est additionner : 2 + 0 + 5 + 9 + 4.", "5 mm = 5 litres par m².", "5 × 15."],
            J("Quelle phrase de la fiche définit le cumul ?", P6, [P2, P7, P3], pos=1)),
        "second": code(
            "Le cahier de Tiago indique pour la semaine : lundi 1,5 mm, mardi 0 mm, mercredi 6 mm, jeudi 10,5 mm, vendredi 3 mm. Ouvre le cadenas avec deux nombres : le cumul de la semaine en mm et le nombre de litres tombés jeudi sur un terrain de 40 m².",
            [("Cumul de la semaine (en mm)", "21", 3), ("Litres tombés jeudi sur 40 m²", "420", 4)],
            ["Additionne : 1,5 + 0 + 6 + 10,5 + 3.", "10,5 mm = 10,5 litres par m².", "10,5 × 40."],
            J("Quelle phrase de la fiche explique à quoi sert le cumul ?", P7, [P6, P2, P3], pos=0)),
    }
    return d
