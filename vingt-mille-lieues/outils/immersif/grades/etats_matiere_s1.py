"""Salle 1 « Le hall des cuves » : grades mousse, lieutenant, second (fiche : etats)."""
from aide import *

FICHE = "« Solide, liquide ou gaz : comment les reconnaître ? »"
P_DUR = "Un solide n'est pas forcément dur : une éponge, un pull, de la pâte à modeler sont des solides."
P_GRAINS = "Le sable, la farine ou le sucre en poudre s'écoulent, mais ce sont des solides divisés : chaque grain garde sa forme, et versés, ils forment un tas."
P_SURFACE = "Au repos, sa surface libre est plane et horizontale."
P_COMPR = "Il est compressible : dans une seringue bouchée, on peut pousser un peu le piston."
P_INVIS = "La plupart des gaz sont invisibles, comme l'air et la vapeur d'eau."
P_GAZ = "Un gaz n'a ni forme ni volume propres : il occupe tout le volume du récipient qui le contient."
P_LITRE = "Il a un volume propre : un litre d'eau reste un litre, dans une bouteille comme dans une cuvette."
P_SOLIDE = "Un solide a une forme propre et un volume propre : il garde sa forme et la place qu'il occupe, quel que soit le récipient."


def donnees(svg, bloc=None):
    d = {}
    # ------------------------------------------------ e1-1 : le grand tri des réservoirs
    d["e1-1"] = {
        "mousse": tri(
            "Inès range les réservoirs. Range chaque carte : solide, liquide ou gaz. Clique sur une carte, puis sur une colonne.",
            [("solide", "Solide"), ("liquide", "Liquide"), ("gaz", "Gaz")],
            [("une pierre", "solide"), ("un glaçon", "solide"), ("de l'eau", "liquide"), ("du jus de pomme", "liquide"), ("l'air d'un ballon", "gaz")],
            ["Ouvre la fiche " + FICHE + " dans la Bibliothèque.", "Un solide garde sa forme, même si on le change de boîte.",
             "L'air ne se voit pas : c'est un gaz."]),
        "lieutenant": tri(
            "Inès vérifie le contenu de dix réservoirs, à la température de la pièce. Range chaque carte, puis choisis la phrase de la fiche qui justifie le classement de la farine.",
            [("solide", "Solide"), ("liquide", "Liquide"), ("gaz", "Gaz")],
            [("de la farine", "solide"), ("du sable", "solide"), ("une éponge", "solide"), ("de la pâte à modeler", "solide"),
             ("du miel", "liquide"), ("de l'huile", "liquide"), ("de l'eau salée", "liquide"),
             ("l'air d'un pneu", "gaz"), ("la vapeur d'eau", "gaz"), ("le gaz d'un ballon de fête", "gaz")],
            ["Mou ne veut pas dire liquide : une éponge garde sa forme.", "Ce qui s'écoule en grains forme un tas : regarde un seul grain.",
             "Pour la justification : cherche la phrase qui parle des grains."],
            J("Quelle phrase de la fiche prouve que la farine est un solide ?", P_GRAINS,
              [P_SURFACE, P_DUR, P_INVIS], pos=1)),
        "second": qcm(
            carnet("Carnet de contrôle d'Inès", "(essais inventés pour le jeu). Essai A : on verse la matière d'une boîte carrée dans un bol ; elle prend la forme du bol, sa surface devient plate. Essai B : la matière garde sa forme dans les deux récipients. Essai C : la matière remplit tout le flacon fermé ; dans une seringue bouchée, on pousse un peu le piston.")
            + "Réponds aux trois questions à partir du carnet et de la fiche.",
            [("Quel essai décrit un liquide ?", ["L'essai A", "L'essai B", "L'essai C", "Aucun"], 0, "Le liquide prend la forme du récipient ; sa surface au repos est plane."),
             ("Quel essai décrit un gaz ?", ["L'essai A", "L'essai B", "L'essai C", "Les essais A et C"], 2, "Un gaz occupe tout le volume et il est compressible."),
             ("Dans l'essai B, la matière est molle. Que peut-on dire ?", ["C'est un liquide, car elle est molle", "C'est un solide, même si elle est molle",
              "C'est un gaz", "On ne peut rien dire"], 1, "Un solide garde sa forme, qu'il soit dur ou mou.")],
            ["Compare chaque essai aux trois critères : forme, volume, compression.", "Seul un gaz se laisse comprimer dans la seringue.",
             "Une pâte à modeler est molle, mais elle garde sa forme."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", P_DUR, [P_GAZ, P_LITRE, P_COMPR], pos=2)),
    }
    # ------------------------------------------------ e1-2 : les critères de l'ingénieure
    d["e1-2"] = {
        "mousse": vf(
            "Inès a écrit trois phrases sur les états. Pour chaque phrase, choisis vrai ou faux.",
            [("L'eau prend la forme du verre dans lequel on la verse.", True, "Un liquide prend la forme du récipient."),
             ("Une pierre change de forme quand on la met dans une boîte.", False, "Un solide garde sa forme."),
             ("On ne voit pas l'air, mais il existe.", True, "L'air est un gaz invisible.")],
            ["Ouvre la fiche " + FICHE + ".", "Pense à de l'eau versée d'un verre dans un bol.", "Le vent fait bouger les feuilles : l'air existe."]),
        "lieutenant": qcm(
            "Inès a écrit ses critères pour reconnaître un état. Réponds aux quatre questions, puis choisis la phrase de la fiche qui décrit le liquide.",
            [("Quel état a un volume propre mais pas de forme propre ?", ["Le solide", "Le liquide", "Le gaz", "Aucun"], 1, "Le liquide garde son volume."),
             ("On verse 1 L d'eau d'une bouteille dans une cuvette. Quel volume d'eau dans la cuvette ?", ["Moins d'un litre", "Un litre", "Plus d'un litre", "Cela dépend de la cuvette"], 1, "Le volume d'un liquide ne change pas."),
             ("Quel état peut-on comprimer dans une seringue bouchée ?", ["Le solide", "Le liquide", "Le gaz", "Aucun"], 2, "Un gaz est compressible."),
             ("On penche une cuve d'eau. Au repos, la surface de l'eau est...", ["penchée comme la cuve", "plane et horizontale", "en bosse", "en creux"], 1, "La surface libre reste horizontale.")],
            ["Distingue bien « forme propre » et « volume propre ».", "Un litre reste un litre, quel que soit le récipient.", "Pour la justification : cherche « un litre d'eau »."],
            J("Quelle phrase de la fiche décrit le volume d'un liquide ?", P_LITRE, [P_GAZ, P_SOLIDE, P_INVIS], pos=0)),
        "second": assoc(
            "Inès a noté des observations dans son carnet. Relie chaque observation au critère qu'elle montre, puis choisis la phrase de la fiche qui explique la seringue.",
            [("le piston d'une seringue d'air bouchée avance un peu", "un gaz est compressible"),
             ("le parfum ouvert remplit toute la pièce", "un gaz occupe tout le volume"),
             ("l'eau d'une bouteille penchée reste horizontale", "la surface libre d'un liquide est plane"),
             ("une éponge garde sa forme dans tous les seaux", "un solide a une forme propre"),
             ("1 L de lait reste 1 L dans une casserole", "un liquide a un volume propre")],
            ["Chaque observation montre un seul critère.", "La seringue et le parfum parlent tous deux d'un gaz, mais pas du même critère.",
             "Pour la justification : cherche le mot « compressible »."],
            J("Quelle phrase de la fiche explique ce qui se passe dans la seringue ?", P_COMPR, [P_SURFACE, P_INVIS, P_DUR], pos=3)),
    }
    # ------------------------------------------------ e1-3 : la cuve à grains
    d["e1-3"] = {
        "mousse": intrus(
            "Dans la cuve à grains, tout coule... ou presque. Trouve l'intrus : la seule matière qui n'est pas un solide.",
            [("du sable", False), ("du sucre en poudre", False), ("de l'eau", True)],
            ["Ouvre la fiche " + FICHE + " : cherche le mot « grain ».", "Le sable versé fait un tas.", "L'eau ne fait jamais de tas."]),
        "lieutenant": intrus(
            "Cinq matières s'écoulent dans la cuve à grains. Une seule est un liquide : trouve-la, puis choisis la phrase de la fiche qui permet de la reconnaître.",
            [("de la semoule", False), ("du sel fin", False), ("de la farine", False), ("du sable sec", False), ("du lait", True)],
            ["Versée sur la table, quelle matière ne fait pas de tas ?", "À la loupe, quatre matières montrent des grains.", "Pour la justification : pense à la surface au repos."],
            J("Quelle phrase de la fiche permet de reconnaître le liquide ?", P_SURFACE, [P_SOLIDE, P_COMPR, P_GAZ], pos=1)),
        "second": tri(
            "Les pièges de la cuve à grains : range chaque matière selon son état à la température de la pièce, puis choisis la phrase de la fiche qui justifie le classement des poudres.",
            [("solide", "Solide"), ("liquide", "Liquide")],
            [("du sable", "solide"), ("de la farine", "solide"), ("du sel fin", "solide"), ("du gel douche", "liquide"),
             ("du sirop épais", "liquide"), ("du miel", "liquide"), ("une éponge mouillée", "solide")],
            ["Épais ne veut pas dire solide : regarde si la surface finit par devenir plate.", "Une poudre est faite de grains qui gardent leur forme.",
             "Mouillée ou non, l'éponge garde sa forme."],
            J("Quelle phrase de la fiche justifie le classement des poudres ?", P_GRAINS, [P_LITRE, P_SURFACE, P_DUR], pos=0)),
    }
    # ------------------------------------------------ e1-4 : le carnet de contrôle (6e, 5e)
    d["e1-4"] = {
        "lieutenant": vf(
            "Inès relit son carnet de contrôle. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui corrige l'erreur sur les solides.",
            [("Un solide est toujours dur.", False, "Une éponge ou de la pâte à modeler sont des solides mous."),
             ("Un gaz occupe tout le volume du récipient qui le contient.", True, "Il n'a pas de volume propre."),
             ("On ne peut presque pas comprimer un liquide.", True, "Un liquide est presque incompressible."),
             ("La vapeur d'eau est la fumée blanche au-dessus d'une casserole.", False, "La vapeur d'eau est invisible."),
             ("Le sucre en poudre est un liquide, car il s'écoule.", False, "Chaque grain de sucre garde sa forme : c'est un solide.")],
            ["Pense à une éponge, un pull, de la pâte à modeler.", "La vapeur d'eau est un gaz : la plupart des gaz ne se voient pas.", "Pour la justification : cherche « pas forcément dur »."],
            J("Quelle phrase de la fiche corrige l'erreur sur les solides ?", P_DUR, [P_GRAINS, P_SOLIDE, P_COMPR], pos=0)),
        "second": vf(
            "Inès prépare le contrôle final du hall. Pour chaque phrase, choisis vrai ou faux. Attention aux phrases presque justes.",
            [("Un gaz n'a pas de forme propre, mais il a un volume propre.", False, "Un gaz n'a ni forme ni volume propres."),
             ("Un liquide a un volume propre, mais pas de forme propre.", True, "Il prend la forme du récipient."),
             ("Dans un flacon fermé, l'air n'occupe que le bas du flacon.", False, "Un gaz occupe tout le volume."),
             ("Un pull est un solide, même s'il est mou.", True, "Il garde sa forme propre."),
             ("Si on ne voit rien dans un bocal, c'est qu'il est vide.", False, "Il peut contenir de l'air, invisible.")],
            ["Lis chaque phrase en entier : une seule moitié peut être fausse.", "Un gaz prend toute la place qu'on lui donne.", "La plupart des gaz sont invisibles."],
            J("Quelle phrase de la fiche corrige la première affirmation ?", P_GAZ, [P_LITRE, P_INVIS, P_SURFACE], pos=2)),
    }
    return d
