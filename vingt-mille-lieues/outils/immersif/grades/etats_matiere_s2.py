"""Salle 2 « La terrasse du ballon-sonde » : grades mousse, lieutenant, second (fiche : air)."""
from aide import *

FICHE = "« L'air est de la matière »"
P_VENT = "On ne le voit pas, mais c'est de la matière : on le sent quand le vent souffle, il fait tourner une girouette et gonfle les voiles des bateaux."
P_VERRE = "Enfoncé à l'envers dans l'eau, il garde sec le mouchoir collé au fond : l'air enfermé occupe la place."
P_BULLES = "Si on incline le verre, des bulles d'air s'échappent et l'eau entre."
P_BALANCE = "La balance affiche une masse plus grande : l'air ajouté a une masse."
P_LITRE = "Dans les conditions habituelles, un litre d'air a une masse d'environ 1,2 g."
P_PRECIS = "C'est peu : il faut une balance précise au gramme pour voir la différence."
P_CLASSE = "Une salle de classe contient pourtant plus de 200 kg d'air."
P_METHODE = "Pour prouver quelque chose par une expérience, on compare un « avant » et un « après » en ne changeant qu'une seule chose."
P_MELANGE = "L'air est un mélange de gaz."


def donnees(svg, bloc=None):
    d = {}
    # ------------------------------------------------ e2-1 : les idées de Bastien
    d["e2-1"] = {
        "mousse": vf(
            "Bastien prépare son ballon-sonde. Pour chaque phrase sur l'air, choisis vrai ou faux.",
            [("Le vent, c'est de l'air qui bouge.", True, "Le vent est de l'air en mouvement."),
             ("Un verre « vide » contient de l'air.", True, "L'air occupe la place."),
             ("L'air n'est rien du tout.", False, "L'air est de la matière.")],
            ["Ouvre la fiche " + FICHE + " dans la Bibliothèque.", "Le vent fait tourner la girouette : il pousse quelque chose.",
             "Ce qu'on ne voit pas peut quand même exister."]),
        "lieutenant": vf(
            "Bastien note ses idées sur l'air avant le lâcher. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui prouve que l'air est de la matière.",
            [("L'air est un mélange de gaz.", True, "C'est la première phrase de la fiche."),
             ("La girouette tourne parce que l'air la pousse.", True, "Le vent est de l'air en mouvement."),
             ("Un ballon dégonflé ne contient plus du tout d'air.", False, "Il en reste un peu : le ballon n'est jamais vide."),
             ("L'air n'a pas de masse, puisqu'il ne se voit pas.", False, "Invisible ne veut pas dire sans masse."),
             ("L'air se laisse un peu comprimer.", True, "Comme tous les gaz, il est compressible.")],
            ["Le vent agit sur la girouette et sur les voiles : il pousse.", "Ne pas voir une chose ne prouve pas qu'elle n'existe pas.",
             "Pour la justification : cherche la phrase de la girouette."],
            J("Quelle phrase de la fiche prouve que l'air est de la matière ?", P_VENT, [P_PRECIS, P_BULLES, P_LITRE], pos=2)),
        "second": qcm(
            carnet("Relevé de Bastien", "(inventé pour le jeu). La terrasse de la Fabrique mesure environ la taille d'une salle de classe.")
            + "Réponds aux trois questions à partir du relevé et de la fiche.",
            [("Une salle de classe contient de l'air. Quelle masse environ ?", ["Moins de 1 g", "Environ 1,2 g", "Plus de 200 kg", "0 g : l'air ne pèse rien"], 2,
              "Un litre d'air, c'est peu ; mais une salle contient beaucoup de litres."),
             ("Pourquoi ne sent-on pas le poids de l'air dans la main ?", ["Parce qu'un litre d'air n'a qu'une très petite masse", "Parce que l'air n'a pas de masse",
              "Parce que l'air est un liquide", "Parce que l'air est toujours en mouvement"], 0, "Environ 1,2 g par litre."),
             ("De quoi l'air est-il fait ?", ["D'un seul gaz", "D'un mélange de gaz", "De vapeur seulement", "De vide"], 1, "L'air est un mélange de gaz.")],
            ["Une petite masse multipliée par beaucoup de litres donne une grande masse.", "Pour voir la masse d'un litre d'air, il faut une balance précise.",
             "Relis la première phrase de la fiche."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 1 ?", P_CLASSE, [P_VENT, P_BALANCE, P_BULLES], pos=1)),
    }
    # ------------------------------------------------ e2-2 : peser l'air
    d["e2-2"] = {
        "mousse": ordre(
            "Bastien veut montrer que l'air a une masse. Remets ses trois étapes dans l'ordre (flèches ▲ et ▼).",
            ["Peser le ballon peu gonflé.", "Ajouter de l'air avec la pompe.", "Peser à nouveau : la masse a augmenté."],
            ["Ouvre la fiche " + FICHE + " : cherche « L'air a une masse ».", "On pèse d'abord, avant de changer quelque chose.", "La conclusion vient à la fin."]),
        "lieutenant": ordre(
            "Bastien écrit le protocole pour peser l'air. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche qui explique pourquoi on ne change qu'une seule chose.",
            ["Régler la balance électronique au gramme près.", "Poser le ballon de basket peu gonflé et noter sa masse.",
             "Gonfler le même ballon avec la pompe, sans rien ajouter d'autre.", "Reposer le même ballon sur la même balance et noter la masse.",
             "Comparer : la deuxième masse est plus grande.", "Conclure : l'air ajouté a une masse."],
            ["Une balance précise se prépare avant la première pesée.", "« Avant » vient avant « après ».", "Pour la justification : cherche le mot « Méthode »."],
            J("Pourquoi Bastien garde-t-il le même ballon et la même balance ?", P_METHODE, [P_PRECIS, P_VERRE, P_MELANGE], pos=0)),
        "second": ordre(
            "Bastien veut aussi montrer que l'air occupe la place, avec un verre et un mouchoir. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche qui décrit ce qu'on voit à la fin.",
            ["Coller un mouchoir sec au fond d'un verre.", "Retourner le verre, ouverture vers le bas.", "L'enfoncer bien droit dans la cuve d'eau.",
             "Le ressortir bien droit : le mouchoir est sec.", "Recommencer en inclinant le verre sous l'eau.", "Observer les bulles d'air qui remontent : l'eau entre."],
            ["Le mouchoir doit être en place avant de retourner le verre.", "Le premier essai se fait verre bien droit.", "Pour la justification : cherche « incline »."],
            J("Quelle phrase de la fiche décrit la dernière étape ?", P_BULLES, [P_VERRE, P_BALANCE, P_CLASSE], pos=2)),
    }
    # ------------------------------------------------ e2-3 : le verre et la seringue
    d["e2-3"] = {
        "mousse": qcm(
            "Bastien enfonce un verre à l'envers dans l'eau, avec un mouchoir collé au fond. Réponds aux deux questions.",
            [("Quand on ressort le verre, le mouchoir est...", ["mouillé", "sec", "déchiré"], 1, "L'air enfermé a gardé la place."),
             ("Qu'est-ce qui empêche l'eau d'entrer ?", ["L'air dans le verre", "Le mouchoir", "Rien"], 0, "L'air occupe la place.")],
            ["Ouvre la fiche " + FICHE + " : cherche le mouchoir.", "Le verre n'est pas vide : il contient de l'air.", "L'air prend de la place, même invisible."]),
        "lieutenant": qcm(
            "Bastien compare deux seringues bouchées : l'une pleine d'air, l'autre pleine d'eau. Réponds, puis choisis la phrase de la fiche qui explique le verre au mouchoir.",
            [("On pousse les deux pistons. Lequel avance un peu ?", ["Celui de la seringue d'air", "Celui de la seringue d'eau", "Les deux autant", "Aucun"], 0, "Un gaz est compressible."),
             ("On lâche le piston de la seringue d'air. Il...", ["reste enfoncé", "revient en arrière", "sort de la seringue", "fond"], 1, "L'air comprimé repousse le piston."),
             ("Le mouchoir collé au fond du verre enfoncé à l'envers reste sec. Pourquoi ?", ["L'air enfermé occupe la place", "Le verre est imperméable", "L'eau est trop froide", "Le mouchoir repousse l'eau"], 0,
              "L'air est de la matière : il occupe un volume.")],
            ["Un liquide ne se laisse presque pas comprimer ; un gaz, un peu.", "L'air écrasé pousse dans l'autre sens.", "Pour la justification : cherche le mot « mouchoir »."],
            J("Quelle phrase de la fiche explique l'expérience du mouchoir ?", P_VERRE, [P_BULLES, P_MELANGE, P_PRECIS], pos=3)),
        "second": vf(
            "Bastien relit le compte rendu de l'équipe d'avant. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui justifie la balance.",
            [("Pour peser l'air d'un ballon, une balance de cuisine graduée de 100 g en 100 g suffit.", False, "Il faut une balance précise au gramme."),
             ("Le ballon gonflé est plus lourd parce que l'air ajouté a une masse.", True, "Seul l'air a changé."),
             ("On a changé de ballon entre les deux pesées : la preuve est bonne.", False, "On ne change qu'une seule chose."),
             ("Les bulles qui sortent d'un verre incliné sous l'eau sont de l'air.", True, "L'air enfermé s'échappe."),
             ("L'air de la seringue disparaît quand on pousse le piston.", False, "Il est comprimé, pas détruit : il repousse le piston.")],
            ["Une différence de quelques grammes ne se voit pas sur n'importe quelle balance.", "Pour comparer, une seule chose doit changer.", "Pour la justification : cherche « précise »."],
            J("Quelle phrase de la fiche justifie ta réponse à la première affirmation ?", P_PRECIS, [P_LITRE, P_METHODE, P_VENT], pos=0)),
    }
    # ------------------------------------------------ e2-4 : le calcul du ballon (6e, 5e)
    d["e2-4"] = {
        "lieutenant": code(
            "Bastien fait un essai avec un ballon de 450 g. Il y ajoute 10 litres d'air. Un litre d'air a une masse d'environ 1,2 g. Calcule, puis choisis la phrase de la fiche qui donne la masse d'un litre d'air.",
            [("Masse de l'air ajouté (en g)", "12", 2), ("Nouvelle masse du ballon (en g)", "462", 3)],
            ["10 litres, c'est dix fois 1,2 g.", "10 × 1,2 g = 12 g.", "Ajoute la masse de l'air à celle du ballon : 450 + 12."],
            J("Quelle phrase de la fiche donne la valeur utilisée ?", P_LITRE, [P_CLASSE, P_BALANCE, P_PRECIS], pos=0)),
        "second": code(
            "Bastien pèse le ballon de basket : 600 g. Il le gonfle, et la balance affiche 612 g. Un litre d'air a une masse d'environ 1,2 g. Retrouve la masse de l'air ajouté, puis le nombre de litres d'air ajoutés.",
            [("Masse de l'air ajouté (en g)", "12", 2), ("Volume d'air ajouté (en litres)", "10", 2)],
            ["Masse ajoutée = masse après − masse avant.", "612 − 600 = 12 g.", "Combien de fois 1,2 g dans 12 g ? 12 ÷ 1,2."],
            J("Quelle phrase de la fiche permet de passer de la masse au volume ?", P_LITRE, [P_BALANCE, P_CLASSE, P_METHODE], pos=2)),
    }
    return d
