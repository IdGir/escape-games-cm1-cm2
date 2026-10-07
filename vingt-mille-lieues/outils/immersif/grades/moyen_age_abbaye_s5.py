"""Salle 5 « L'église romane et la cathédrale gothique » (fiche : roman-gothique)."""
from aide import *

F = "« Différencier l'art roman et l'art gothique »"
R1 = "Le poids de la voûte en berceau pousse sur toute la longueur des murs. Il faut donc des murs épais, des piliers massifs et des contreforts à l'extérieur."
R2 = "De grandes fenêtres affaibliraient le mur : les ouvertures restent petites, et l'église est sombre."
R3 = "Les arcs sont en plein cintre, c'est-à-dire en demi-cercle."
R4 = "La croisée d'ogives : deux arcs se croisent en diagonale et conduisent le poids de la voûte vers quatre piliers, et non plus sur tout le mur."
R5 = "L'arc brisé : un arc pointu, qui pousse moins vers l'extérieur et permet de monter plus haut."
R6 = "L'arc-boutant : un arc extérieur qui renvoie la poussée vers un gros pilier."
R7 = "Comme le mur porte moins, on peut l'ouvrir : apparaissent d'immenses vitraux et les rosaces."
R8 = "Le premier grand chantier gothique est le chœur de l'abbatiale de Saint-Denis, voulu par l'abbé Suger et consacré en 1144."
R9 = "À Vézelay, le chœur gothique (fin du XIIe siècle) prolonge la nef romane : on voit les deux arts dans le même bâtiment."


def donnees(svg, bloc=None):
    d = {}
    d["e5-1"] = {
        "mousse": assoc(
            "Garin montre deux églises. Relie chaque élément à l'art auquel il appartient. Clique sur un élément, puis sur son art.",
            [("la voûte en berceau", "art roman : un demi-tonneau"), ("l'arc en plein cintre", "art roman : un demi-cercle"), ("l'arc brisé", "art gothique : un arc pointu")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "« Plein cintre » veut dire arrondi.", "« Brisé » veut dire pointu."]),
        "lieutenant": {
            "type": "plan", "titre": "Légende les deux églises", "colonnes": 2,
            "cases": [{"libelle": "Gothique : deux arcs qui se croisent sous la voûte", "reponse": "croisée d'ogives"}, {"libelle": "Roman : massif de pierre collé contre le mur", "reponse": "contrefort"},
                      {"libelle": "Gothique : arc extérieur qui renvoie la poussée", "reponse": "arc-boutant"}, {"libelle": "Gothique : grande fenêtre ronde", "reponse": "rosace"},
                      {"libelle": "Roman : arc en demi-cercle", "reponse": "arc en plein cintre"}, {"libelle": "Gothique : arc pointu", "reponse": "arc brisé"}],
            "etiquettes": ["croisée d'ogives", "contrefort", "arc-boutant", "rosace", "arc en plein cintre", "arc brisé", "donjon", "créneau"],
            "consigne": "Garin légende le schéma des deux églises. Place chaque étiquette dans la bonne case. Deux étiquettes sont en trop. Puis choisis la phrase de la fiche qui décrit l'arc-boutant.",
            "indices": ["Le contrefort est collé au mur.", "Un arc brisé est pointu.", "Donjon et créneau : c'est le château fort."],
            "justification": J("Quelle phrase de la fiche décrit l'arc-boutant ?", R6, [R4, R5, R1], pos=1)},
        "second": vf(
            "Garin a noté six phrases sur les églises. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui explique pourquoi l'église romane est sombre.",
            [("Dans une église romane, la voûte pousse sur toute la longueur des murs.", True, "D'où les murs épais."), ("L'église romane a de grandes fenêtres.", False, "Les ouvertures restent petites."), ("L'arc brisé est pointu.", True, "Il permet de monter plus haut."),
             ("Les arcs-boutants sont à l'intérieur de l'église.", False, "Ils sont à l'extérieur."), ("La croisée d'ogives conduit le poids vers quatre piliers.", True, "Et non sur tout le mur."), ("L'art gothique commence avant l'an 1000.", False, "À partir du milieu du XIIe siècle.")],
            ["Un mur épais porte la voûte.", "Les arcs-boutants sont dehors.", "Le gothique naît au XIIe siècle."],
            J("Quelle phrase de la fiche explique pourquoi l'église romane est sombre ?", R2, [R1, R7, R3], pos=1)),
    }
    d["e5-2"] = {
        "mousse": intrus(
            "Trois de ces éléments appartiennent à l'église romane. Un seul est gothique. Trouve l'intrus, puis vérifie.",
            [("Murs épais", False), ("Petites fenêtres", False), ("Arc en plein cintre", False), ("Arc brisé", True)],
            ["Ouvre la fiche " + F + ".", "L'art roman a des murs épais et peu de lumière.", "Un arc pointu est gothique."]),
        "lieutenant": intrus(
            "Quatre de ces éléments appartiennent à l'art gothique. Un seul est roman. Trouve l'intrus, puis choisis la phrase de la fiche qui justifie ton choix.",
            [("Croisée d'ogives", False), ("Arc brisé", False), ("Arc-boutant", False), ("Rosace", False), ("Voûte en berceau", True)],
            ["Les éléments gothiques ouvrent le mur.", "La voûte en berceau est lourde et pousse sur les murs.", "Pour la justification : cherche la phrase qui parle de murs épais."],
            J("Quelle phrase de la fiche justifie ton choix ?", R1, [R4, R6, R7], pos=2)),
        "second": tri(
            "Garin classe les éléments selon le problème qu'ils résolvent. Range chaque carte dans la bonne colonne, puis choisis la phrase de la fiche qui explique pourquoi on peut ouvrir de grandes fenêtres dans une cathédrale gothique.",
            [("poids", "Faire porter le poids de la voûte"), ("lumiere", "Laisser entrer la lumière")],
            [("Les murs épais et les contreforts", "poids"), ("Les arcs-boutants", "poids"), ("La croisée d'ogives", "poids"), ("Les grands vitraux", "lumiere"), ("Les rosaces", "lumiere"), ("L'ouverture des murs", "lumiere")],
            ["Les arcs-boutants et les ogives portent le poids.", "Les vitraux et les rosaces laissent entrer la lumière.", "Le mur porte moins : on peut l'ouvrir."],
            J("Quelle phrase de la fiche explique pourquoi on peut ouvrir de grandes fenêtres ?", R7, [R2, R5, R6], pos=0)),
    }
    d["e5-3"] = {
        "mousse": tri(
            "Range chaque élément dans la bonne colonne : art roman ou art gothique. Clique sur une carte, puis sur une colonne.",
            [("roman", "Art roman"), ("gothique", "Art gothique")],
            [("Arc arrondi", "roman"), ("Murs épais et petites fenêtres", "roman"), ("Arc pointu", "gothique"), ("Grands vitraux colorés", "gothique")],
            ["Ouvre la fiche " + F + ".", "Arrondi : roman. Pointu : gothique.", "Beaucoup de verre : gothique."]),
        "lieutenant": tri(
            "Garin classe des éléments et des monuments. Range chaque carte dans la bonne colonne, puis choisis la phrase de la fiche qui parle de Saint-Denis.",
            [("roman", "Art roman"), ("gothique", "Art gothique")],
            [("Intérieur sombre, piliers massifs", "roman"), ("La nef de Vézelay (vers 1120-1140)", "roman"), ("Cluny III (1088-1130)", "roman"),
             ("Le chœur de Saint-Denis (consacré en 1144)", "gothique"), ("Le chœur de Vézelay (fin du XIIe siècle)", "gothique"), ("Les rosaces", "gothique")],
            ["Vézelay : nef romane, chœur gothique.", "Saint-Denis est le premier grand chantier gothique.", "Cluny III date de 1088 à 1130."],
            J("Quelle phrase de la fiche parle de Saint-Denis ?", R8, [R9, R7, R5], pos=1)),
        "second": qcm(
            carnet("Ce que voulait l'abbé Suger", "(formule résumée). « Faire entrer plus de lumière dans l'église, car Dieu est lumière. » Le chœur de Saint-Denis est consacré en 1144.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Quelle idée est à l'origine du chœur de Saint-Denis ?", ["Faire entrer plus de lumière dans l'église", "Construire une forteresse", "Loger des pèlerins", "Copier un livre"], 0, "Plus de lumière."),
             ("Quel élément gothique permet cela ?", ["Des murs ouverts par de grands vitraux", "Des murs plus épais", "Des fenêtres plus petites", "Des voûtes en berceau"], 0, "Le mur porte moins : on peut l'ouvrir."),
             ("Combien d'années séparent 1144 de la fin du XIIe siècle (1200) ?", ["environ 56 ans", "environ 6 ans", "environ 100 ans", "environ 156 ans"], 0, "1200 − 1144 = 56.")],
            ["Le chœur de Saint-Denis laisse entrer la lumière.", "Relis : « comme le mur porte moins ».", "Soustrais 1144 de 1200."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", R7, [R8, R6, R2], pos=3)),
    }
    d["e5-4"] = {
        "lieutenant": qcm(
            carnet("Vézelay", "(d'après la fiche). La nef de la basilique date d'environ 1120-1140. Le chœur a été rebâti à la fin du XIIe siècle. On voit les deux arts dans le même bâtiment.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 1.",
            [("De quel art est la nef de Vézelay ?", ["Roman", "Gothique", "Classique", "Antique"], 0, "Vers 1120-1140."),
             ("De quel art est le chœur ?", ["Gothique", "Roman", "Classique", "Antique"], 0, "Fin du XIIe siècle."),
             ("Que prouve la présence des deux arts dans un même bâtiment ?", ["Le chantier a duré et le style a changé", "Les deux arts sont identiques", "Le gothique est avant le roman", "L'église n'a jamais été finie"], 0, "Le gothique prolonge le roman.")],
            ["La nef est la plus ancienne partie.", "Le chœur a été rebâti plus tard.", "Les styles changent avec le temps."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 1 ?", R9, [R8, R5, R2], pos=1)),
        "second": {
            "type": "plan", "titre": "Les monuments et l'art", "colonnes": 2,
            "cases": [{"libelle": "Style de la nef de Vézelay (vers 1120-1140)", "reponse": "roman"}, {"libelle": "Style du chœur de Vézelay (fin du XIIe siècle)", "reponse": "gothique"},
                      {"libelle": "Abbé qui veut plus de lumière à Saint-Denis", "reponse": "Suger"}, {"libelle": "Année de consécration du chœur de Saint-Denis", "reponse": "1144"},
                      {"libelle": "Arc extérieur qui renvoie la poussée de la voûte", "reponse": "arc-boutant"}],
            "etiquettes": ["roman", "gothique", "Suger", "1144", "arc-boutant", "classique", "1088", "contrefort"],
            "consigne": "Garin termine son dossier. Place chaque étiquette dans la bonne case. Trois étiquettes sont en trop. Puis choisis la phrase de la fiche qui date le chœur de Saint-Denis.",
            "indices": ["Vézelay mêle deux arts.", "Saint-Denis est le premier grand chantier gothique.", "Le contrefort est collé au mur, l'arc-boutant en est séparé."],
            "justification": J("Quelle phrase de la fiche date le chœur de Saint-Denis ?", R8, [R9, R6, R7], pos=2)},
    }
    return d
