"""Salle 3 « La matériauthèque » (fiche : materiaux)."""
from aide import *

F = "« Les matériaux »"
X1 = "La matière est ce dont une chose est faite. Un matériau est une matière choisie et préparée pour fabriquer un objet."
X2 = "On classe les matériaux en familles : les métaux, les matières plastiques, les matériaux d'origine végétale ou animale, le verre et les céramiques."
X3 = "Propriétés utiles : dur ou souple, léger ou lourd, transparent ou opaque, conducteur (laisse passer le courant ou la chaleur) ou isolant (les arrête), cassant ou résistant aux chocs."
X4 = "La poignée d'une casserole est en bois ou en plastique parce que ces matériaux conduisent mal la chaleur."
X5 = "On pense aussi au poids, au prix et à l'environnement : le verre et les métaux peuvent être recyclés pour fabriquer de nouveaux objets."


def donnees(svg, bloc=None):
    d = {}
    d["e3-1"] = {
        "mousse": tri(
            "Awa range les échantillons. Range chaque objet dans la bonne famille : clique sur une carte, puis sur un casier.",
            [("metal", "Métaux"), ("plast", "Matières plastiques"), ("vegan", "Origine végétale ou animale")],
            [("Une cuillère en acier", "metal"), ("Une bouteille en plastique", "plast"), ("Une planche de bois", "vegan"), ("Un pull en laine", "vegan")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Le bois vient d'un arbre.", "La laine vient du mouton."]),
        "lieutenant": tri(
            "Awa teste des matériaux. Range chaque objet selon qu'il laisse passer le courant ou non, puis choisis la phrase de la fiche qui définit le conducteur et l'isolant.",
            [("cond", "Conducteur"), ("isol", "Isolant")],
            [("Un fil de cuivre", "cond"), ("Un clou en acier", "cond"), ("Une casserole en aluminium", "cond"), ("La gaine en plastique d'un câble", "isol"), ("Un manche en bois", "isol"), ("Une vitre en verre", "isol")],
            ["Les métaux laissent passer le courant.", "Le plastique, le bois et le verre l'arrêtent.", "Conducteur : laisse passer. Isolant : arrête."],
            J("Quelle phrase de la fiche définit conducteur et isolant ?", X3, [X1, X4, X5], pos=1)),
        "second": qcm(
            carnet("Notes d'Awa", "(inventées pour le jeu). Une casserole : corps en aluminium, poignée en plastique. Une fenêtre : vitre en verre. Une canette : aluminium, recyclable.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 1.",
            [("Pourquoi la poignée de la casserole est-elle en plastique ?", ["Le plastique conduit mal la chaleur", "Il est plus lourd", "Il est brillant", "Il est conducteur"], 0, "C'est un isolant."),
             ("Pourquoi une vitre est-elle en verre ?", ["Le verre est transparent", "Le verre est souple", "Le verre est léger", "Le verre est opaque"], 0, "Il laisse passer la lumière."),
             ("Que permet de recycler une canette en aluminium ?", ["Fabriquer de nouveaux objets", "La rendre transparente", "La transformer en bois", "La rendre plus lourde"], 0, "Les métaux peuvent être recyclés.")],
            ["Une poignée ne doit pas transmettre la chaleur.", "Le verre laisse passer la lumière.", "Le recyclage fabrique de nouveaux objets."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 1 ?", X4, [X3, X5, X2], pos=2)),
    }
    d["e3-2"] = {
        "mousse": vf(
            "Pour chaque phrase, clique sur « Vrai » ou sur « Faux », puis vérifie.",
            [("Les métaux laissent passer le courant électrique.", True, "Ils sont conducteurs."), ("Le verre est transparent.", True, "Il laisse passer la lumière."), ("Le bois est plus lourd que l'acier.", False, "Il est beaucoup plus léger.")],
            ["Ouvre la fiche " + F + ".", "Les fils électriques sont en cuivre.", "Le bois flotte sur l'eau."]),
        "lieutenant": qcm(
            carnet("Choix de matériaux", "(inventé pour le jeu). Marcel veut fabriquer une poignée de casserole, une vitre et une boîte de conserve. Il hésite entre bois, verre, acier.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 1.",
            [("Quel matériau pour la poignée de casserole ?", ["Le bois, qui conduit mal la chaleur", "L'acier, qui la conduit bien", "Le verre", "Le cuivre"], 0, "Un isolant thermique."),
             ("Quel matériau pour la vitre ?", ["Le verre, transparent", "Le bois, léger", "L'acier, dur", "Le cuir"], 0, "Il faut laisser passer la lumière."),
             ("Quel matériau pour la boîte de conserve, qu'on peut recycler ?", ["L'acier", "Le bois", "Le cuir", "La laine"], 0, "Les métaux peuvent être recyclés.")],
            ["Une poignée doit rester froide.", "Une vitre laisse passer la lumière.", "Les métaux se recyclent."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 1 ?", X4, [X3, X5, X1], pos=1)),
        "second": tri(
            "Marcel choisit des matériaux pour des usages. Range chaque usage dans la colonne du matériau qui convient, puis choisis la phrase de la fiche qui explique le choix d'un matériau.",
            [("verre", "Verre"), ("metal", "Métal"), ("plast", "Plastique")],
            [("Une fenêtre", "verre"), ("Un bocal transparent", "verre"), ("Un fil électrique (âme)", "metal"), ("Une casserole", "metal"), ("La gaine d'un câble", "plast"), ("La poignée d'une casserole", "plast")],
            ["Transparent : verre.", "Conducteur : métal.", "Isolant : plastique."],
            J("Quelle phrase de la fiche explique le choix d'un matériau ?", X3, [X1, X5, X2], pos=0)),
    }
    d["e3-3"] = {
        "mousse": intrus(
            "Trois de ces échantillons sont des métaux. Un seul n'en est pas un. Clique sur l'intrus, puis vérifie.",
            [("Une cuillère en acier", False), ("Un fil de cuivre", False), ("Une vis en acier", False), ("Un bocal en verre", True)],
            ["Ouvre la fiche " + F + ".", "Le verre n'est pas un métal.", "L'acier et le cuivre sont des métaux."]),
        "lieutenant": vf(
            "Éléonore classe des échantillons. Pour chacune de ces affirmations, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui énumère les familles de matériaux.",
            [("L'acier et le cuivre sont des métaux.", True, "Ils conduisent le courant."), ("Le bois est un matériau d'origine végétale.", True, "Il vient d'un arbre."), ("La laine est un métal.", False, "Elle vient d'un animal."),
             ("Le verre et la porcelaine sont des matériaux d'origine animale.", False, "Verre et céramiques."), ("Le plastique est un matériau d'origine végétale.", False, "C'est une matière plastique.")],
            ["Quatre familles : métaux, plastiques, végétal ou animal, verre et céramiques.", "La laine vient du mouton.", "Le plastique forme une famille à part."],
            J("Quelle phrase de la fiche énumère les familles de matériaux ?", X2, [X1, X3, X5], pos=2)),
        "second": vf(
            "Éléonore a noté six affirmations. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui distingue matière et matériau.",
            [("Une matière est ce dont une chose est faite.", True, "Un matériau est une matière choisie et préparée."), ("Un matériau est une matière choisie et préparée pour fabriquer un objet.", True, "C'est la définition."), ("Matière et matériau veulent dire exactement la même chose.", False, "Un matériau est choisi et préparé."),
             ("Le verre peut être recyclé.", True, "Les métaux aussi."), ("Un isolant laisse passer le courant.", False, "Il l'arrête."), ("Un matériau cassant résiste aux chocs.", False, "Il casse.")],
            ["Un matériau est choisi et préparé.", "Un isolant arrête le courant.", "Cassant : casse facilement."],
            J("Quelle phrase de la fiche distingue matière et matériau ?", X1, [X2, X3, X4], pos=1)),
    }
    d["e3-4"] = {
        "lieutenant": intrus(
            "Quatre de ces matériaux conduisent mal la chaleur. Un seul la conduit bien. Trouve l'intrus, puis choisis la phrase de la fiche qui justifie ton choix.",
            [("Le bois d'une poignée", False), ("Le plastique d'une poignée", False), ("La laine d'un pull", False), ("Le cuir d'une semelle", False), ("L'aluminium d'une casserole", True)],
            ["Un métal conduit la chaleur.", "Une poignée ne doit pas la conduire.", "Cherche le matériau d'un récipient qui chauffe."],
            J("Quelle phrase de la fiche justifie ton choix ?", X4, [X3, X5, X2], pos=0)),
        "second": intrus(
            "Quatre de ces matériaux peuvent être recyclés pour fabriquer de nouveaux objets. Un seul n'est pas cité dans la fiche. Trouve l'intrus, puis choisis la phrase de la fiche qui justifie ton choix.",
            [("Le verre d'un bocal", False), ("L'aluminium d'une canette", False), ("L'acier d'une boîte de conserve", False), ("Le cuivre d'un fil", False), ("Le papier peint collé au mur", True)],
            ["La fiche parle du verre et des métaux.", "Le papier peint n'est pas dans la liste.", "Cherche la phrase qui parle de recyclage."],
            J("Quelle phrase de la fiche justifie ton choix ?", X5, [X2, X3, X4], pos=3)),
    }
    return d
