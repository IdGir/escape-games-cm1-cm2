"""Salle 3 « La salle des fioles » (fiche : melanges)."""
from aide import *

F = "« Mélanges homogènes et hétérogènes »"
H1 = "Un mélange est formé de plusieurs constituants. Pour le décrire, on l'observe à l'œil nu."
H2 = "Homogène : on ne peut pas distinguer les constituants à l'œil nu (eau salée, sirop à l'eau, eau du robinet qui contient des sels minéraux, air)."
H3 = "Hétérogène : on distingue au moins deux constituants (eau et huile, vinaigrette, eau boueuse, riz et semoule)."
H4 = "Un mélange peut changer : du sel versé dans l'eau forme d'abord un mélange hétérogène (on voit les grains) ; une fois dissous, il devient homogène."
H5 = "L'huile et l'eau ne se mélangent pas : pour un même volume, l'huile est plus légère, elle reste au-dessus."
H6 = "Bien observer permet de choisir la méthode de séparation : un mélange hétérogène se sépare souvent par tamisage, aimantation, décantation ou filtration ; pour un solide dissous, il faut l'évaporation."


def donnees(svg, bloc=None):
    d = {}
    d["e3-1"] = {
        "mousse": tri(
            "Observe chaque mélange avec tes yeux. Range chaque carte : je ne vois qu'une chose, ou j'en vois au moins deux. Clique sur une carte, puis sur une colonne.",
            [("homo", "Homogène : une seule chose"), ("hetero", "Hétérogène : au moins deux choses")],
            [("Eau salée", "homo"), ("Sirop à l'eau", "homo"), ("Eau et huile", "hetero"), ("Eau et sable", "hetero")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Dans l'eau salée, on ne voit pas le sel.", "Le sable se voit au fond."]),
        "lieutenant": tri(
            "Lila observe neuf mélanges à l'œil nu. Range chaque mélange dans la bonne colonne, puis choisis la phrase de la fiche qui définit le mélange hétérogène.",
            [("homo", "Mélange homogène"), ("hetero", "Mélange hétérogène")],
            [("Eau du robinet", "homo"), ("Eau sucrée", "homo"), ("L'air de la salle", "homo"), ("Du sel dissous dans l'eau", "homo"),
             ("Vinaigrette", "hetero"), ("Eau boueuse", "hetero"), ("Riz et semoule", "hetero"), ("Du sel versé dans l'eau, avant de remuer", "hetero"), ("Jus d'orange avec pulpe", "hetero")],
            ["On observe à l'œil nu.", "Avant de remuer, on voit les grains de sel.", "L'air et l'eau du robinet sont homogènes."],
            J("Quelle phrase de la fiche définit un mélange hétérogène ?", H3, [H2, H1, H4], pos=2)),
        "second": qcm(
            carnet("Fiole n° 7", "(inventée pour le jeu). Lila verse 20 g de sel dans 250 g d'eau. À l'instant du versement, on voit des grains au fond. Après avoir remué, le liquide est transparent.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("À l'instant du versement, le mélange est…", ["hétérogène : on voit les grains", "homogène", "pur", "solide"], 0, "On distingue deux constituants."),
             ("Après avoir remué, le mélange est…", ["homogène : on ne voit plus le sel", "hétérogène", "de l'eau pure", "plus léger"], 0, "Le sel est dissous."),
             ("Quelle est la masse du mélange après dissolution ?", ["270 g", "250 g", "230 g", "20 g"], 0, "250 + 20.")],
            ["Avant de remuer, on voit les grains de sel.", "Après la dissolution, on ne distingue plus rien à l'œil nu.", "La masse se conserve."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", H4, [H2, H3, H6], pos=1)),
    }
    d["e3-2"] = {
        "mousse": intrus(
            "Sur cette étagère, Lila a rangé trois mélanges où l'on ne voit qu'une seule chose. Un autre n'a rien à faire là. Clique sur l'intrus, puis vérifie.",
            [("Eau salée", False), ("Eau sucrée", False), ("Sirop à l'eau", False), ("Eau et sable", True)],
            ["Ouvre la fiche " + F + ".", "Cherche le mélange où l'on voit deux choses.", "Les grains de sable se voient."]),
        "lieutenant": vf(
            "Marius a rangé des mélanges. Pour chaque affirmation, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui explique pourquoi l'huile reste au-dessus de l'eau.",
            [("L'eau du robinet est un mélange homogène.", True, "Elle contient des sels minéraux dissous."), ("La vinaigrette laissée au repos se sépare en deux couches.", True, "L'huile reste au-dessus."),
             ("L'huile et l'eau forment un mélange homogène.", False, "On distingue deux couches."), ("L'air est un mélange.", True, "Un mélange de gaz."),
             ("Si on ne voit pas un constituant, il n'y est pas.", False, "Il peut être dissous.")],
            ["L'huile est plus légère que l'eau.", "L'eau du robinet contient des sels minéraux dissous.", "Un constituant dissous ne se voit plus."],
            J("Quelle phrase de la fiche explique pourquoi l'huile reste au-dessus de l'eau ?", H5, [H2, H3, H6], pos=1)),
        "second": tri(
            "Lila reprend deux fioles : A (eau salée, sel dissous) et B (eau et sable, avant de remuer). Range chaque observation dans la bonne colonne, puis choisis la phrase de la fiche qui énumère les mélanges homogènes.",
            [("a", "Fiole A (eau salée)"), ("b", "Fiole B (eau et sable)")],
            [("On ne distingue qu'un seul liquide", "a"), ("Un constituant est invisible, mais présent", "a"), ("Le mélange est homogène", "a"), ("Des grains se déposent au fond", "b"), ("On distingue deux constituants à l'œil nu", "b"), ("Le mélange est hétérogène", "b")],
            ["Le sel dissous ne se voit plus.", "Le sable ne se dissout pas.", "Homogène : un seul aspect."],
            J("Quelle phrase de la fiche énumère les mélanges homogènes ?", H2, [H3, H5, H1], pos=2)),
    }
    d["e3-3"] = {
        "mousse": assoc(
            "Relie chaque mélange à ce que l'on observe. Clique d'abord à gauche, puis à droite.",
            [("Eau et huile", "deux couches : l'huile reste au-dessus"), ("Eau et sable", "des grains au fond"), ("Eau salée", "un liquide transparent")],
            ["Ouvre la fiche " + F + ".", "L'huile reste au-dessus.", "Le sel dissous ne se voit plus."]),
        "lieutenant": qcm(
            carnet("Étagère de Lila", "(inventée pour le jeu). Fiole 1 : eau et sirop de menthe, vert partout. Fiole 2 : eau et pulpe d'orange. Fiole 3 : eau, huile et sable.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("La fiole 1 est…", ["homogène", "hétérogène", "pure", "solide"], 0, "Un seul aspect."), ("La fiole 2 est…", ["hétérogène", "homogène", "pure", "gazeuse"], 0, "On voit la pulpe."),
             ("Dans la fiole 3, combien de constituants distingue-t-on ?", ["3 : eau, huile et sable", "1", "2", "4"], 0, "Eau, huile, sable.")],
            ["Un mélange homogène a un seul aspect.", "La pulpe se voit.", "Compte les constituants visibles."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", H1, [H5, H6, H2], pos=1)),
        "second": vf(
            "Lila a noté six phrases. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui lie observation et méthode de séparation.",
            [("Un mélange est formé de plusieurs constituants.", True, "Au moins deux."), ("On l'observe à l'œil nu pour le décrire.", True, "C'est la première étape."),
             ("Un mélange hétérogène se sépare par évaporation seulement.", False, "Tamisage, aimantation, décantation, filtration."), ("Pour un solide dissous, il faut l'évaporation.", True, "L'eau part, le solide reste."),
             ("Bien observer ne sert à rien pour choisir la méthode.", False, "Observer permet de choisir."), ("La filtration retient un solide dissous.", False, "Il traverse le filtre.")],
            ["Observer, puis choisir.", "Un solide dissous passe à travers le filtre.", "L'évaporation sépare un solide dissous."],
            J("Quelle phrase de la fiche lie observation et méthode de séparation ?", H6, [H4, H3, H5], pos=0)),
    }
    d["e3-4"] = {
        "lieutenant": assoc(
            "Lila termine sa visite des fioles. Relie chaque situation à sa description précise, puis choisis la phrase de la fiche qui explique le changement d'un mélange de sel et d'eau.",
            [("Du sel versé dans l'eau, avant de remuer", "mélange hétérogène : on voit les grains"), ("Le même sel, une fois dissous", "mélange homogène"), ("Une vinaigrette au repos", "deux couches : l'huile reste au-dessus"),
             ("L'eau du robinet", "mélange homogène : sels minéraux dissous")],
            ["Le sel dissous ne se voit plus.", "Avant de remuer, on voit les grains.", "L'huile est plus légère que l'eau."],
            J("Quelle phrase de la fiche explique le changement d'un mélange de sel et d'eau ?", H4, [H2, H5, H6], pos=1)),
        "second": intrus(
            "Lila range cinq exemples de mélanges homogènes. Un seul n'en est pas un. Trouve l'intrus, puis choisis la phrase de la fiche qui le justifie.",
            [("L'eau salée", False), ("Le sirop à l'eau", False), ("L'eau du robinet", False), ("L'air", False), ("La vinaigrette", True)],
            ["Un mélange homogène a un seul aspect à l'œil nu.", "L'air est un mélange de gaz.", "La vinaigrette se sépare en deux couches."],
            J("Quelle phrase de la fiche justifie ton choix ?", H3, [H2, H1, H4], pos=0)),
    }
    return d
