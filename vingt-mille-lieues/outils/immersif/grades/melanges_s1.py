"""Salle 1 « La salle des balances » (fiche : masses)."""
from aide import *

F = "« Mesurer et comparer des masses »"
M1 = "La balance à plateaux compare deux masses : à l'équilibre, elles sont égales."
M2 = "Avec des masses marquées, on détermine la masse d'un objet par addition."
M4 = "La touche « tare » (ou « zéro ») remet l'affichage à 0 quand un récipient est posé : on ne pèse ensuite que ce que l'on y verse."
M5 = "Sans tare, on calcule : masse du contenu = récipient plein − récipient vide."
M6 = "1 t = 1 000 kg · 1 kg = 1 000 g · 1 g = 1 000 mg"
M7 = "Pour comparer des masses, on les écrit dans la même unité : 0,2 kg = 200 g ; 1,05 kg = 1 050 g."
M8 = "Le litre mesure un volume (la place occupée), pas une masse."
M9 = "1 litre d'eau pèse environ 1 kg, mais 1 litre d'huile pèse environ 920 g : c'est pour cela que l'huile flotte sur l'eau."


def donnees(svg, bloc=None):
    d = {}
    d["e1-1"] = {
        "mousse": ordre(
            "Lila a posé trois fioles sur la balance et a noté leur masse. Range les fioles de la plus légère (en haut) à la plus lourde (en bas) avec ▲ et ▼, puis vérifie.",
            [("La fiole jaune", "80 g"), ("La fiole verte", "140 g"), ("La fiole rouge", "420 g")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Compare d'abord les nombres de chiffres.", "Le plus petit nombre est la fiole la plus légère."]),
        "lieutenant": ordre(
            "Lila a noté les masses de cinq flacons avec des unités différentes. Range-les du plus léger (en haut) au plus lourd (en bas), puis choisis la phrase de la fiche qui explique comment comparer.",
            [("Le flacon D", "1 500 mg"), ("Le flacon C", "0,075 kg"), ("Le flacon E", "0,4 kg"), ("Le flacon A", "480 g"), ("Le flacon B", "0,52 kg")],
            ["Écris toutes les masses en grammes.", "1 000 mg = 1 g, donc 1 500 mg = 1,5 g.", "0,075 kg = 75 g et 0,52 kg = 520 g."],
            J("Quelle phrase de la fiche explique comment comparer des masses ?", M7, [M6, M4, M2], pos=1)),
        "second": qcm(
            carnet("Relevé de Lila", "(inventé pour le jeu). Un bidon vide pèse 0,4 kg. Rempli d'eau (1 litre), il pèse 1 400 g. Rempli d'huile (1 litre), il pèse 1 320 g.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("Quelle est la masse de 1 litre d'eau ?", ["1 000 g", "1 400 g", "400 g", "1 320 g"], 0, "1 400 − 400 = 1 000 g."),
             ("Quelle est la masse de 1 litre d'huile ?", ["920 g", "1 320 g", "400 g", "1 000 g"], 0, "1 320 − 400 = 920 g."),
             ("Pourquoi l'huile flotte-t-elle sur l'eau ?", ["Pour un même volume, l'huile est plus légère", "L'huile est plus lourde", "L'huile n'a pas de masse", "L'eau est un solide"], 0, "920 g contre 1 000 g.")],
            ["Masse du liquide = bidon plein − bidon vide.", "Convertis 0,4 kg en 400 g.", "Compare 920 g et 1 000 g pour 1 litre."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", M9, [M8, M5, M4], pos=2)),
    }
    d["e1-2"] = {
        "mousse": qcm(
            "Lis la question, clique sur la bonne réponse, puis vérifie.",
            [("Sur une balance à deux plateaux, le plateau qui descend porte…", ["l'objet le plus lourd", "l'objet le plus léger", "l'objet le plus beau"], 0, "Le plateau le plus chargé descend.")],
            ["Ouvre la fiche " + F + ".", "Pense à une balançoire à bascule.", "Le côté le plus lourd descend."]),
        "lieutenant": vf(
            "Marius affirme cinq choses sur les balances. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui explique la touche « tare ».",
            [("La touche tare remet l'affichage à zéro quand un récipient est posé.", True, "On ne pèse ensuite que ce qu'on y verse."), ("Sans tare, on peut calculer : récipient plein moins récipient vide.", True, "C'est la masse du contenu."),
             ("À l'équilibre d'une balance à plateaux, les deux masses sont égales.", True, "C'est le principe."), ("Avec la tare, la balance pèse aussi le récipient.", False, "Elle l'ignore."),
             ("Le litre est une unité de masse.", False, "C'est une unité de volume.")],
            ["La tare évite de peser le récipient.", "Le litre mesure la place occupée.", "Pour la justification : cherche la phrase qui nomme la touche « tare »."],
            J("Quelle phrase de la fiche explique la touche « tare » ?", M4, [M1, M5, M2], pos=1)),
        "second": ordre(
            "Nadia pèse un liquide avec une balance électronique. Remets ces étapes dans l'ordre, puis choisis la phrase de la fiche qui justifie la deuxième étape.",
            ["Poser le bécher vide sur la balance.", "Appuyer sur « tare » : l'écran affiche 0.", "Verser lentement le liquide dans le bécher.", "Lire la masse du liquide seul.", "Noter la masse avec son unité."],
            ["Le bécher est posé avant la tare.", "La tare vient avant de verser.", "On lit après avoir versé."],
            J("Quelle phrase de la fiche justifie la deuxième étape ?", M4, [M5, M2, M1], pos=0)),
    }
    d["e1-3"] = {
        "mousse": code(
            "Un liquide ne tient pas tout seul sur la balance : on le pèse dans un récipient. Calcule la masse de l'eau seule : récipient plein moins récipient vide. Un bécher vide pèse 100 g, plein d'eau il pèse 220 g. Écris le résultat en grammes.",
            [("Masse de l'eau seule (g)", "120", 3)],
            ["Ouvre la fiche " + F + ".", "Récipient plein moins récipient vide.", "Calcule 220 − 100."]),
        "lieutenant": code(
            "Lila a pesé trois récipients. Calcule la masse du contenu seul, en grammes. Attention aux unités.",
            [("Eau : bécher vide 90 g, bécher plein 360 g", "270", 3), ("Sirop : bouteille vide 0,25 kg, pleine 1 000 g", "750", 3), ("Miel : pot vide 0,3 kg, pot plein 1,1 kg", "800", 3)],
            ["Pour l'eau : 360 − 90.", "Pour le sirop, convertis 0,25 kg en 250 g.", "Pour le miel : 1,1 kg = 1 100 g et 0,3 kg = 300 g."],
            J("Quelle phrase de la fiche donne la méthode de calcul ?", M5, [M4, M7, M6], pos=1)),
        "second": code(
            "Un bidon contient 5 litres d'huile (1 litre d'huile pèse environ 920 g) et un autre 5 litres d'eau (1 litre d'eau pèse environ 1 kg). Calcule les deux masses, en grammes.",
            [("Masse de 5 litres d'huile (g)", "4600", 4), ("Masse de 5 litres d'eau (g)", "5000", 4)],
            ["5 × 920 pour l'huile.", "5 × 1 000 pour l'eau.", "L'huile est plus légère que l'eau."],
            J("Quelle phrase de la fiche donne les masses d'un litre d'eau et d'un litre d'huile ?", M9, [M8, M7, M5], pos=2)),
    }
    d["e1-4"] = {
        "lieutenant": trous(
            "Lila a rédigé la leçon sur les unités, mais il manque des mots. Clique sur une étiquette, puis sur le trou où elle va. Trois étiquettes sont en trop. Puis choisis la phrase de la fiche qui donne les unités de masse.",
            "1 kg = [[1 000]] g. 1 g = 1 000 [[mg]]. 1 [[t]] = 1 000 kg. Pour comparer deux masses, on les écrit dans la même [[unité]].",
            ["1 000", "mg", "t", "unité", "100", "mètre", "litre"],
            ["« kilo » veut dire mille.", "Les petites masses se donnent en milligrammes.", "Pour comparer, on convertit."],
            J("Quelle phrase de la fiche donne les unités de masse ?", M6, [M7, M8, M4], pos=0)),
        "second": vf(
            "Lila a noté six phrases sur les unités. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui distingue masse et volume.",
            [("1 kg = 1 000 g.", True, "kilo = mille."), ("1 g = 1 000 mg.", True, "Milligramme : un millième de gramme."), ("1 t = 100 kg.", False, "1 t = 1 000 kg."),
             ("Le litre mesure une masse.", False, "Il mesure un volume."), ("1 litre d'huile et 1 litre d'eau ont la même masse.", False, "920 g contre environ 1 kg."), ("0,2 kg = 200 g.", True, "Conversion.")],
            ["Masse et volume sont deux grandeurs différentes.", "1 tonne, c'est mille kilogrammes.", "L'huile est plus légère que l'eau."],
            J("Quelle phrase de la fiche distingue masse et volume ?", M8, [M9, M6, M7], pos=1)),
    }
    return d
