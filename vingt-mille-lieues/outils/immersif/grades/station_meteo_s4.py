"""Salle 4 « Le tableau des relevés » (fiche : releves)."""
from aide import *

F = "« Organiser et exploiter des relevés »"
Q1 = "Un tableau à double entrée croise les grandeurs mesurées (lignes) et les dates (colonnes)."
Q2 = "Une valeur sans unité ne veut rien dire : 12 peut être 12 °C, 12 km/h ou 12 mm."
Q3 = "On cherche le minimum et le maximum, on calcule l'écart (maximum − minimum) et le cumul (somme, pour la pluie)."
Q4 = "Un diagramme en barres convient aux quantités (pluie de chaque jour). Une courbe montre l'évolution d'une grandeur qui varie en continu, comme la température."
Q5 = "C'est une valeur impossible ou très éloignée des autres : un minimum plus élevé que le maximum du même jour, un chiffre recopié de travers."
Q6 = "On la repère, on cherche la cause et on ne l'utilise pas dans les calculs."

TAB = lambda lignes: ('<table class="tableau-releves"><tr><th></th><th>Lun</th><th>Mar</th><th>Mer</th><th>Jeu</th><th>Ven</th></tr>'
                      + "".join("<tr><th>" + l[0] + "</th>" + "".join(f"<td>{c}</td>" for c in l[1:]) + "</tr>" for l in lignes) + "</table>")


def donnees(svg, bloc=None):
    d = {}
    d["e4-1"] = {
        "mousse": {
            "type": "plan", "titre": "Cases à retrouver", "colonnes": 2,
            "cases": [{"libelle": "Case A : maximum de lundi", "reponse": "17 °C"}, {"libelle": "Case B : vent de mardi", "reponse": "18 km/h"}, {"libelle": "Case C : pluie de mercredi", "reponse": "7 mm"}],
            "etiquettes": ["17 °C", "18 km/h", "7 mm", "17 mm"],
            "consigne": "La pluie a effacé trois cases du tableau de Lina (A, B, C). Retrouve-les grâce à son carnet, puis place les étiquettes. Une étiquette est en trop. Attention aux <b>unités</b>."
                        + '<table class="tableau-releves"><tr><th></th><th>Lun</th><th>Mar</th><th>Mer</th></tr><tr><th>Maximum (°C)</th><td><b>A</b></td><td>19</td><td>21</td></tr><tr><th>Vent (km/h)</th><td>12</td><td><b>B</b></td><td>24</td></tr><tr><th>Pluie (mm)</th><td>0</td><td>3</td><td><b>C</b></td></tr></table>'
                        + "<p><i>Carnet de Lina :</i> « Lundi, au plus chaud : 17 °C. Mardi, le vent soufflait à 18 km/h. Mercredi, le pluviomètre indiquait 7 mm. »</p>",
            "indices": ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Lis le nom de la ligne pour trouver l'unité.", "Une température ne s'écrit pas en mm."]},
        "lieutenant": {
            "type": "plan", "titre": "Cases à retrouver", "colonnes": 2,
            "cases": [{"libelle": "Case A : minimum de jeudi", "reponse": "8 °C"}, {"libelle": "Case B : maximum de vendredi", "reponse": "16 °C"}, {"libelle": "Case C : vent de lundi", "reponse": "12 km/h"}, {"libelle": "Case D : écart de jeudi", "reponse": "6 °C"}],
            "etiquettes": ["8 °C", "16 °C", "12 km/h", "6 °C", "12 mm", "9 °C"],
            "consigne": "La pluie a effacé quatre cases du tableau (A à D). Retrouve-les grâce au carnet de Lina, calcule celle qui manque, puis place les étiquettes. Deux étiquettes sont en trop. Puis choisis la phrase de la fiche qui définit l'écart."
                        + TAB([("Minimum (°C)", 9, 11, 12, "<b>A</b>", 7), ("Maximum (°C)", 17, 19, 21, 14, "<b>B</b>"), ("Écart (°C)", 8, 8, 9, "<b>D</b>", 9), ("Vent (km/h)", "<b>C</b>", 18, 24, 30, 8)])
                        + "<p><i>Carnet de Lina :</i> « Jeudi, au lever du jour : 8 °C. Vendredi, au plus chaud : 16 °C. Lundi, vent moyen : 12 km/h. » La ligne « Écart » donne la différence entre le maximum et le minimum du jour.</p>",
            "indices": ["L'unité dépend de la ligne.", "Écart de jeudi : 14 − 8.", "Les deux étiquettes en trop n'ont pas la bonne unité ou la bonne valeur."],
            "justification": J("Quelle phrase de la fiche définit l'écart ?", Q3, [Q1, Q2, Q4], pos=1)},
        "second": qcm(
            "Lina a rempli un tableau. Lis-le, réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3."
            + TAB([("Minimum (°C)", 4, 6, 3, 5, 2), ("Maximum (°C)", 12, 15, 11, 14, 10), ("Vent (km/h)", 15, 22, 35, 20, 10), ("Pluie (mm)", 0, 2, 9, 4, 0)]),
            [("Quel est l'écart de température le plus grand de la semaine ?", ["9 °C (mardi)", "8 °C (lundi)", "10 °C (vendredi)", "7 °C"], 0, "15 − 6 = 9."),
             ("Quel est le cumul de la pluie ?", ["15 mm", "9 mm", "4 mm", "13 mm"], 0, "0 + 2 + 9 + 4 + 0 = 15."),
             ("Pourquoi faut-il toujours écrire l'unité dans le tableau ?", ["12 peut être 12 °C, 12 km/h ou 12 mm", "Pour décorer le tableau", "Parce que les nombres sont petits", "Parce que le vent a une unité seulement"], 0, "Une valeur sans unité ne veut rien dire.")],
            ["Écart : maximum − minimum, jour par jour.", "Additionne la ligne « Pluie ».", "Une valeur sans unité ne veut rien dire."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", Q2, [Q1, Q3, Q5], pos=2)),
    }
    d["e4-2"] = {
        "mousse": intrus(
            "Un relevé a été mal noté : le thermomètre avait été posé en plein soleil. Clique sur la valeur qui ne va pas avec les autres, puis vérifie.",
            [("Lundi : 15 °C", False), ("Mardi : 17 °C", False), ("Mercredi : 16 °C", False), ("Jeudi : 38 °C", True)],
            ["Ouvre la fiche " + F + ".", "Compare les nombres.", "Un thermomètre au soleil chauffe beaucoup plus que l'air."]),
        "lieutenant": intrus(
            "Un relevé de la semaine contient une erreur : il est impossible. Clique dessus, puis choisis la phrase de la fiche qui définit une valeur aberrante.",
            [("Lundi : minimum 8 °C, maximum 15 °C", False), ("Mardi : minimum 10 °C, maximum 17 °C", False), ("Mercredi : minimum 18 °C, maximum 11 °C", True), ("Jeudi : minimum 7 °C, maximum 13 °C", False), ("Vendredi : minimum 6 °C, maximum 12 °C", False)],
            ["Pour chaque jour, le minimum est plus petit que le maximum.", "Un jour a des valeurs inversées.", "Pour la justification : cherche la phrase qui parle d'un minimum plus élevé que le maximum."],
            J("Quelle phrase de la fiche définit une valeur aberrante ?", Q5, [Q3, Q6, Q2], pos=1)),
        "second": vf(
            "Lina a noté six phrases sur les valeurs aberrantes et les graphiques. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui dit ce qu'on fait d'une valeur aberrante.",
            [("Un minimum plus élevé que le maximum du même jour est une valeur aberrante.", True, "C'est impossible."), ("On utilise une valeur aberrante dans les calculs.", False, "On ne l'utilise pas."), ("On cherche la cause d'une valeur aberrante.", True, "On la repère d'abord."),
             ("Un diagramme en barres convient à la pluie de chaque jour.", True, "Pour les quantités."), ("Une courbe convient à la température.", True, "Elle varie en continu."), ("Un chiffre recopié de travers peut donner une valeur aberrante.", True, "C'est une erreur de recopie.")],
            ["Une valeur aberrante est impossible.", "On ne la prend pas dans les calculs.", "Barres : quantités. Courbe : évolution."],
            J("Quelle phrase de la fiche dit ce qu'on fait d'une valeur aberrante ?", Q6, [Q5, Q4, Q3], pos=1)),
    }
    d["e4-3"] = {
        "mousse": trous(
            "Complète le résumé de la semaine à l'aide du tableau (minimum : 9, 11, 12 ; maximum : 17, 19, 21). Clique sur une étiquette, puis sur le trou où elle va. Une étiquette est en trop.",
            "La température la plus basse est [[9 °C]]. La plus haute est [[21 °C]]. L'écart entre les deux est de [[12 °C]].",
            ["9 °C", "21 °C", "12 °C", "30 °C"],
            ["Ouvre la fiche " + F + ".", "Écart : plus grande valeur moins plus petite valeur.", "21 − 9."]),
        "lieutenant": trous(
            "Complète le résumé de la semaine à l'aide du tableau de la case précédente. Clique sur une étiquette, puis sur le trou où elle va. Trois étiquettes sont en trop. Puis choisis la phrase de la fiche qui définit le cumul.",
            "Le minimum le plus bas est [[7 °C]], le maximum le plus haut [[21 °C]] : l'écart total est de [[14 °C]]. Le [[cumul]] de pluie se calcule en additionnant les jours.",
            ["7 °C", "21 °C", "14 °C", "cumul", "écart", "9 °C", "28 °C"],
            ["Plus petit minimum, plus grand maximum.", "21 − 7.", "Le cumul est une somme."],
            J("Quelle phrase de la fiche définit le cumul ?", Q3, [Q1, Q4, Q6], pos=2)),
        "second": tri(
            "Lina a rempli un tableau (minimum : 4, 6, 3, 5, 2 ; maximum : 12, 15, 11, 14, 10 ; vent : 15, 22, 35, 20, 10 ; pluie : 0, 2, 9, 4, 0). Range chaque résumé : exact ou faux d'après le tableau ? Puis choisis la phrase de la fiche qui décrit le tableau à double entrée.",
            [("exact", "Exact d'après le tableau"), ("faux", "Faux d'après le tableau")],
            [("Le minimum le plus bas est 2 °C.", "exact"), ("Le cumul de pluie est de 15 mm.", "exact"), ("Le vent le plus fort a soufflé mercredi.", "exact"),
             ("Le maximum le plus haut est 14 °C.", "faux"), ("L'écart de lundi est de 7 °C.", "faux"), ("Il a plu tous les jours.", "faux")],
            ["Le plus petit des minimums, le plus grand des maximums.", "Additionne la ligne « Pluie ».", "Écart de lundi : 12 − 4."],
            J("Quelle phrase de la fiche décrit le tableau à double entrée ?", Q1, [Q3, Q2, Q4], pos=0)),
    }
    d["e4-4"] = {
        "lieutenant": qcm(
            "Lina a tracé la ligne « pluie » en diagramme : lundi 0 mm, mardi 2 mm, mercredi 9 mm, jeudi 4 mm, vendredi 0 mm. Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie le choix du diagramme en barres.",
            [("Quel jour a été le plus arrosé ?", ["Mercredi", "Jeudi", "Mardi", "Lundi"], 0, "9 mm."), ("De combien de millimètres mercredi dépasse-t-il jeudi ?", ["5 mm", "9 mm", "4 mm", "13 mm"], 0, "9 − 4 = 5."), ("Combien de jours sans pluie ?", ["2", "1", "3", "0"], 0, "Lundi et vendredi.")],
            ["Suis le haut de chaque barre.", "Soustrais 4 de 9.", "Les barres de lundi et de vendredi sont vides."],
            J("Quelle phrase de la fiche justifie le diagramme en barres ?", Q4, [Q1, Q3, Q5], pos=2)),
        "second": trous(
            "Lina rédige la fiche de méthode, mais il manque des mots. Clique sur une étiquette, puis sur le trou où elle va. Quatre étiquettes sont en trop. Puis choisis la phrase de la fiche qui justifie le mot « unité ».",
            "Un tableau à double entrée croise les [[grandeurs]] mesurées et les [[dates]]. Une valeur sans [[unité]] ne veut rien dire. On calcule l'[[écart]] et le [[cumul]].",
            ["grandeurs", "dates", "unité", "écart", "cumul", "couleur", "prix", "vent", "courbe"],
            ["Les lignes : les grandeurs. Les colonnes : les dates.", "12 peut être 12 °C, 12 km/h ou 12 mm.", "Écart et cumul : deux calculs."],
            J("Quelle phrase de la fiche justifie le mot « unité » ?", Q2, [Q1, Q3, Q6], pos=1)),
    }
    return d
