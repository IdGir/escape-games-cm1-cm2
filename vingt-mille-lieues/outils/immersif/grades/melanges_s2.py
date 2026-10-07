"""Salle 2 « La cuisine d'essai » (fiche : conservation)."""
from aide import *

F = "« La masse se conserve »"
C1 = "Certains solides, comme le sucre ou le sel, se dissolvent dans l'eau : ils se séparent en particules si petites qu'on ne les voit plus, même à la loupe."
C2 = "D'autres, comme le sable, ne se dissolvent pas."
C3 = "On ne peut pas dissoudre une quantité illimitée de sel : au bout d'un moment, il reste au fond."
C4 = "masse de l'eau + masse du solide = masse du mélange."
C5 = "250 g d'eau + 20 g de sel → 270 g d'eau salée."
C6 = "Fondre, c'est passer de l'état solide à l'état liquide sous l'effet de la chaleur (la glace fond)."
C7 = "Le sucre qui disparaît dans l'eau froide ne fond pas : il se dissout."
C8 = "L'air est un mélange de gaz. Il a une masse : un litre d'air pèse environ 1,2 g à 20 °C."
C9 = "Sécurité : au laboratoire, on ne goûte jamais et on ne sent jamais un produit."


def donnees(svg, bloc=None):
    d = {}
    d["e2-1"] = {
        "mousse": vf(
            "Marius met du sucre dans l'eau. Pour chaque phrase, clique sur « Vrai » ou sur « Faux », puis vérifie.",
            [("Le sucre dissous est toujours dans l'eau.", True, "On ne le voit plus, mais il est là."), ("Le sable se dissout dans l'eau comme le sucre.", False, "Le sable ne se dissout pas."), ("Au laboratoire, on goûte pour vérifier.", False, "On ne goûte jamais.")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Le sucre dissous ne disparaît pas.", "Au laboratoire, on ne goûte jamais."]),
        "lieutenant": qcm(
            carnet("Essai de Marius", "(inventé pour le jeu). Un verre contient 150 g d'eau. Marius y verse 12 g de sel et remue. Après dissolution, la balance affiche 162 g.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("Que donne 150 + 12 ?", ["162 g, la masse totale", "138 g", "12 g", "150 g"], 0, "La masse se conserve."),
             ("Où est le sel après dissolution ?", ["Toujours dans l'eau, en particules très petites", "Il a disparu", "Il a fondu", "Il s'est transformé en eau"], 0, "Il est dissous."),
             ("Comment Marius vérifie-t-il, au laboratoire, qu'il y a du sel dans l'eau ?", ["Avec la balance ou en faisant évaporer l'eau, jamais en goûtant", "En goûtant", "En sentant le verre", "En le touchant"], 0, "On ne goûte jamais.")],
            ["Additionne les masses.", "Dissoudre n'est pas faire disparaître.", "Une règle de sécurité répond à la question 3."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", C9, [C1, C4, C7], pos=1)),
        "second": vf(
            "Marius a noté six phrases sur la dissolution. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui parle de la limite de dissolution.",
            [("On peut dissoudre une quantité illimitée de sel dans un verre d'eau.", False, "Au bout d'un moment, le sel reste au fond."), ("Le sucre dissous pèse toujours.", True, "La masse se conserve."),
             ("Le sable se dissout dans l'eau chaude.", False, "Le sable ne se dissout pas."), ("Le sucre dans l'eau froide fond.", False, "Il se dissout : fondre demande de la chaleur."),
             ("250 g d'eau et 20 g de sel donnent 270 g d'eau salée.", True, "250 + 20."), ("Les particules dissoutes se voient à la loupe.", False, "Même à la loupe, on ne les voit plus.")],
            ["Il y a une limite à la dissolution.", "Fondre et se dissoudre sont deux choses différentes.", "Les particules dissoutes sont trop petites."],
            J("Quelle phrase de la fiche parle de la limite de dissolution ?", C3, [C1, C2, C7], pos=0)),
    }
    d["e2-2"] = {
        "mousse": {
            "type": "plan", "titre": "L'expérience de Marius", "colonnes": 2,
            "cases": [{"libelle": "1. Le verre d'eau, seul sur la balance", "reponse": "100 g"}, {"libelle": "2. Le sucre, pesé seul", "reponse": "10 g"}, {"libelle": "3. Le sucre est dissous : la balance affiche…", "reponse": "110 g"}],
            "etiquettes": ["100 g", "10 g", "110 g", "90 g"],
            "consigne": "Marius a noté son expérience, mais son cahier est taché. Il se souvient : l'eau pesait 100 g et le sucre 10 g. Clique sur une étiquette, puis sur la case où elle va. Une étiquette est en trop.",
            "indices": ["Ouvre la fiche " + F + ".", "À la fin, la masse est égale à : eau + sucre.", "100 + 10 = 110."]},
        "lieutenant": {
            "type": "plan", "titre": "L'expérience du sel", "colonnes": 2,
            "cases": [{"libelle": "1. Le verre d'eau, seul", "reponse": "300 g"}, {"libelle": "2. Le sel, pesé seul", "reponse": "25 g"}, {"libelle": "3. L'eau salée après dissolution", "reponse": "325 g"}, {"libelle": "4. Si l'on fait évaporer toute l'eau, il reste", "reponse": "25 g de sel"}],
            "etiquettes": ["300 g", "25 g", "325 g", "25 g de sel", "275 g", "0 g de sel"],
            "consigne": "Le cahier de Marius est taché. Il reste une mesure : l'eau salée pèse 325 g, et le sel pesait 25 g. Place chaque étiquette sur la bonne case. Deux étiquettes sont en trop. Puis choisis la phrase de la fiche qui justifie la case 3.",
            "indices": ["Pour retrouver l'eau : 325 − 25.", "Le sel dissous reste quand l'eau part.", "Eau + sel = eau salée."],
            "justification": J("Quelle phrase de la fiche justifie la case 3 ?", C4, [C1, C3, C6], pos=2)},
        "second": {
            "type": "plan", "titre": "L'expérience du sucre", "colonnes": 2,
            "cases": [{"libelle": "1. Le verre d'eau, seul", "reponse": "400 g"}, {"libelle": "2. Le sucre, pesé seul", "reponse": "30 g"}, {"libelle": "3. Après dissolution, la balance affiche", "reponse": "430 g"},
                      {"libelle": "4. Le mélange obtenu est", "reponse": "homogène"}, {"libelle": "5. En laissant évaporer l'eau, on retrouve", "reponse": "30 g de sucre"}],
            "etiquettes": ["400 g", "30 g", "430 g", "homogène", "30 g de sucre", "370 g", "hétérogène", "0 g de sucre"],
            "consigne": "Marius a noté une expérience à l'envers : le mélange final pèse 430 g et le sucre pesait 30 g. Complète le schéma. Trois étiquettes sont en trop. Puis choisis la phrase de la fiche qui explique pourquoi le sucre n'a pas disparu.",
            "indices": ["400 + 30 = 430.", "On ne distingue plus les constituants : le mélange est homogène.", "Le sucre dissous reste quand l'eau s'évapore."],
            "justification": J("Quelle phrase de la fiche explique pourquoi le sucre n'a pas disparu ?", C7, [C4, C6, C3], pos=1)},
    }
    d["e2-3"] = {
        "mousse": qcm(
            "Marius prépare son café. Lis la question, clique sur la bonne réponse, puis vérifie.",
            [("Une tasse de café pèse 180 g. Marius ajoute un sucre de 5 g et remue. La balance affiche…", ["185 g", "175 g", "180 g"], 0, "180 + 5 = 185 g.")],
            ["Ouvre la fiche " + F + ".", "Le sucre dissous pèse toujours.", "Calcule 180 + 5."]),
        "lieutenant": vf(
            "Marius a noté cinq phrases. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui distingue fondre et se dissoudre.",
            [("La glace fond sous l'effet de la chaleur.", True, "Solide vers liquide."), ("Le sucre dans l'eau froide fond.", False, "Il se dissout."),
             ("Le sel dissous a une masse.", True, "La masse se conserve."), ("Quand on fait fondre un solide, il passe de l'état solide à l'état liquide.", True, "Sous l'effet de la chaleur."),
             ("Le sel se dissout parce qu'on le chauffe.", False, "Dissoudre n'est pas chauffer.")],
            ["Fondre demande de la chaleur.", "Le sucre dans l'eau froide ne fond pas.", "Pour la justification : cherche la phrase avec « la glace fond »."],
            J("Quelle phrase de la fiche définit « fondre » ?", C6, [C7, C1, C4], pos=1)),
        "second": qcm(
            carnet("Notes de Marius sur l'air", "(d'après la fiche). Un litre d'air pèse environ 1,2 g à 20 °C. Une salle de classe contient environ 150 000 litres d'air.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 1.",
            [("L'air a-t-il une masse ?", ["Oui : environ 1,2 g par litre", "Non : il est invisible", "Oui : 12 g par litre", "Seulement quand il y a du vent"], 0, "C'est de la matière."),
             ("Quelle est la masse d'air dans 10 litres ?", ["environ 12 g", "environ 1,2 g", "environ 120 g", "environ 0,12 g"], 0, "10 × 1,2 = 12."),
             ("L'air est…", ["un mélange de gaz", "un solide", "un liquide", "du vide"], 0, "C'est un mélange de gaz.")],
            ["Un gaz a une masse, mais petite.", "Multiplie 1,2 par 10.", "L'air est un mélange."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 1 ?", C8, [C2, C1, C9], pos=2)),
    }
    d["e2-4"] = {
        "lieutenant": code(
            "Le placard des épices est fermé par un cadenas à deux nombres. Calcule chaque masse en grammes, puis ouvre.",
            [("400 g d'eau + 20 g de sucre, après dissolution", "420", 3), ("Eau salée : 520 g, dont 20 g de sel. Masse de l'eau ?", "500", 3)],
            ["Premier nombre : 400 + 20.", "Deuxième nombre : 520 − 20.", "La masse se conserve."],
            J("Quelle phrase de la fiche donne la formule ?", C4, [C5, C3, C1], pos=1)),
        "second": code(
            "Le placard des épices est fermé par un cadenas à trois nombres. Un bol de sel dissous dans l'eau pèse 600 g au total. Le bol vide pèse 180 g, le sel 25 g. Calcule, en grammes : la masse de l'eau, la masse de sel retrouvée si l'on fait tout évaporer, la masse du bol avec le sel après évaporation.",
            [("Masse de l'eau (g)", "395", 3), ("Masse de sel retrouvée (g)", "25", 2), ("Bol avec le sel après évaporation (g)", "205", 3)],
            ["Eau = total − bol vide − sel : 600 − 180 − 25.", "L'eau part, le sel reste.", "Bol + sel : 180 + 25."],
            J("Quelle phrase de la fiche donne la formule de la masse du mélange ?", C4, [C5, C1, C3], pos=2)),
    }
    return d
