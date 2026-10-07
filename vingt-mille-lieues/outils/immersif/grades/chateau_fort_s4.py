"""Salle 4 « Le village et les champs » (fiche : vie-des-paysans)."""
from aide import *

F = "« La vie des paysannes et des paysans »"
P1 = "Au Moyen Âge, l'immense majorité de la population vit à la campagne."
P2 = "Les paysans habitent des villages groupés autour de l'église, souvent au pied du château."
P3 = "L'habitat : une maison basse, souvent d'une seule pièce, en torchis sur une armature de bois, couverte de chaume ; un foyer au centre, peu de meubles."
P4 = "L'alimentation : le pain est la base, avec la bouillie, la soupe de légumes et de fèves ; la viande est rare."
P5 = "Pomme de terre, maïs et tomate sont inconnus : ils viennent d'Amérique, après 1492."
P6 = "Les outils : araire ou charrue pour préparer la terre, faucille pour moissonner, faux pour faucher, fléau pour battre le grain."
P7 = "Le calendrier des Très Riches Heures du duc de Berry (vers 1411-1416) montre les travaux des mois : labour et taille de la vigne en mars, fenaison en juin, moisson et tonte des moutons en juillet, vendanges en septembre, semailles en octobre, glandée en novembre."
P8 = "Pour ne pas épuiser le sol, on laisse une partie des champs au repos : c'est la jachère."
P9 = "Les paysannes participent à presque tous les travaux des champs (fenaison, moisson, vendanges)."
P10 = "Elles tiennent aussi la maison, la basse-cour, le jardin et le four, filent et tissent la laine, et vendent les produits au marché."


def donnees(svg, bloc=None):
    d = {}
    d["e4-1"] = {
        "mousse": ordre(
            "Mahaut raconte son année. Remets ces travaux dans l'ordre de l'année, du début (en haut) à la fin (en bas). Utilise les flèches ▲ et ▼.",
            ["Labourer et tailler la vigne (mars)", "Faucher les foins (juin)", "Moissonner le blé (juillet)"],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Mars vient avant juin.", "Le blé se coupe après les foins."]),
        "lieutenant": ordre(
            "Mahaut décrit l'année d'après le calendrier des Très Riches Heures. Remets ces cinq travaux dans l'ordre des mois, puis choisis la phrase de la fiche qui donne ce calendrier.",
            ["Labourer et tailler la vigne (mars)", "Faire les foins (juin)", "Moissonner et tondre les moutons (juillet)", "Vendanger (septembre)", "Semer le blé d'hiver (octobre)"],
            ["Mars, juin, juillet, septembre, octobre.", "La moisson suit la fenaison.", "Les semailles d'automne viennent après les vendanges."],
            J("Quelle phrase de la fiche donne le calendrier des travaux ?", P7, [P8, P6, P9], pos=2)),
        "second": qcm(
            carnet("Calendrier de Mahaut", "(d'après les Très Riches Heures, vers 1411-1416). Mars : labour et taille de la vigne. Juin : fenaison. Juillet : moisson et tonte des moutons. Septembre : vendanges. Octobre : semailles. Novembre : glandée.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Combien de mois s'écoulent entre la fenaison et les vendanges ?", ["3 mois", "1 mois", "6 mois", "9 mois"], 0, "De juin à septembre : 3 mois."),
             ("Pourquoi les paysans laissent-ils une partie des champs au repos ?", ["Pour ne pas épuiser le sol", "Parce qu'ils sont fatigués", "Parce que le seigneur l'interdit", "Parce que le blé ne pousse pas l'été"], 0, "C'est la jachère."),
             ("Quel travail vient juste après les semailles dans ce calendrier ?", ["La glandée", "Les vendanges", "La moisson", "Le labour"], 0, "Novembre.")],
            ["Compte les mois entre juin et septembre.", "On laisse une partie des champs en jachère.", "Regarde l'ordre : octobre puis novembre."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", P8, [P7, P6, P4], pos=1)),
    }
    d["e4-2"] = {
        "mousse": assoc(
            "Relie chaque outil au travail qu'il sert à faire. Clique sur un outil, puis sur son travail.",
            [("La faux", "couper l'herbe"), ("La faucille", "couper le blé"), ("Le fléau", "battre le grain")],
            ["Ouvre la fiche " + F + ".", "La faux a un long manche.", "La faucille est petite et courbée."]),
        "lieutenant": qcm(
            carnet("La journée de Mahaut", "(inventée pour le jeu). À l'aube, Mahaut prend sa faux pour faucher l'herbe d'un pré. L'après-midi, elle tient le four, puis elle vend des œufs au marché.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("Quel travail correspond à la faux ?", ["La fenaison", "La moisson", "Le battage du grain", "Les semailles"], 0, "Faucher l'herbe pour faire le foin."),
             ("Quelle partie de la journée est liée à la maison ?", ["Tenir le four", "Faucher le pré", "Aller à la moisson", "Labourer"], 0, "Elle tient la maison, le jardin et le four."),
             ("Les paysannes se limitent-elles aux tâches de la maison ?", ["Non : elles participent à presque tous les travaux des champs", "Oui, uniquement", "Oui, car les hommes sont plus forts", "On ne sait pas"], 0, "Fenaison, moisson, vendanges.")],
            ["La faux sert à faucher l'herbe.", "Le four fait partie de la maison.", "Relis ce que font les paysannes aux champs."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", P9, [P10, P6, P2], pos=1)),
        "second": tri(
            "Mahaut classe les travaux des paysannes. Range chaque carte : travail des champs ou travail de la maison ? Puis choisis la phrase de la fiche qui décrit le travail dans la maison.",
            [("champs", "Aux champs"), ("maison", "À la maison")],
            [("Faire les foins", "champs"), ("Moissonner", "champs"), ("Vendanger", "champs"), ("Tenir la basse-cour", "maison"), ("Soigner le jardin", "maison"), ("Filer la laine", "maison")],
            ["Les paysannes font presque tous les travaux des champs.", "Elles tiennent la basse-cour, le jardin et le four.", "Elles filent et tissent la laine."],
            J("Quelle phrase de la fiche décrit le travail à la maison ?", P10, [P9, P6, P8], pos=0)),
    }
    d["e4-3"] = {
        "mousse": trous(
            "Mahaut décrit sa maison. Clique sur une étiquette, puis sur le trou où elle va. Une étiquette est en trop.",
            "Ma maison n'a qu'une seule [[pièce]]. Les murs sont en [[torchis]]. Le toit est en [[chaume]]. Nous mangeons surtout du [[pain]].",
            ["pièce", "torchis", "chaume", "pain", "béton"],
            ["Ouvre la fiche " + F + ".", "Le toit est fait de paille.", "On mange surtout du pain."]),
        "lieutenant": tri(
            "Mahaut fait la liste de ce qu'on mange au village. Range chaque aliment : connu au Moyen Âge, ou inconnu en Europe ? Puis choisis la phrase de la fiche qui date l'arrivée des aliments d'Amérique.",
            [("connu", "Connu au Moyen Âge"), ("inconnu", "Inconnu en Europe à cette époque")],
            [("Le pain", "connu"), ("La soupe de légumes", "connu"), ("Les fèves", "connu"), ("La pomme de terre", "inconnu"), ("Le maïs", "inconnu"), ("La tomate", "inconnu")],
            ["Ces trois aliments viennent d'Amérique.", "Le pain est la base de l'alimentation.", "L'Amérique est atteinte en 1492."],
            J("Quelle phrase de la fiche date l'arrivée des aliments d'Amérique ?", P5, [P4, P3, P8], pos=2)),
        "second": vf(
            "Mahaut a noté six phrases sur la vie au village. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui décrit l'habitat.",
            [("Les paysans habitent des villages groupés autour de l'église.", True, "Souvent au pied du château."), ("Les maisons sont souvent d'une seule pièce.", True, "En torchis, couvertes de chaume."),
             ("La viande est la base de l'alimentation.", False, "C'est le pain."), ("La pomme de terre fait partie du repas.", False, "Elle vient d'Amérique, après 1492."),
             ("L'immense majorité de la population vit à la campagne.", True, "Au Moyen Âge."), ("Les maisons ont beaucoup de meubles.", False, "Peu de meubles.")],
            ["Le pain est la base.", "L'habitat est simple.", "La pomme de terre n'est pas encore en Europe."],
            J("Quelle phrase de la fiche décrit l'habitat ?", P3, [P4, P2, P1], pos=2)),
    }
    d["e4-4"] = {
        "lieutenant": lettres(
            "Trouve le mot qui correspond à cette définition : « Champ laissé au repos pour que la terre redevienne fertile. » Ses lettres sont cachées en couleur dans le texte de Mahaut, dans le désordre. Clique-les dans l'ordre qui forme le mot (7 lettres). Trois lettres sont des pièges.",
            ["J", "A", "C", "H", "E", "R", "E"],
            marque("Le soir, Mahaut raconte : « Chez nous, on laisse un champ en repos une année sur deux. [J]'aime ce champ sauvage : les fleurs y p[o]ussent, les oiseaux s'y [c]achent. Avec mon frère, nous y cueillons des [h]erbes. L'[a]utre jour, mon père a dit : à l'automne, on [e]n fera un [p]ré. Ma mère [r]it, car l'herbe y est haute ; au retour, [e]lle est ravie. »"),
            ["Le mot désigne un champ qu'on laisse se reposer.", "Il commence par J.", "Il finit par ERE."],
            J("Quelle phrase de la fiche définit ce mot ?", P8, [P6, P7, P9], pos=2)),
        "second": lettres(
            "Trouve le mot qui correspond à cette définition : « Mélange de terre et de paille qui forme les murs des maisons. » Ses lettres sont cachées en couleur dans le texte de Mahaut, dans le désordre. Clique-les dans l'ordre qui forme le mot (7 lettres). Trois lettres sont des pièges.",
            ["T", "O", "R", "C", "H", "I", "S"],
            marque("Mahaut décrit sa maison : « Le soir, on [h]abille les enfants près du foyer, au centre de la pièce, car il n'y a qu'une seule pièce. Mon père [t]ouche le mur de terre et de paille pour voir s'il tient. On [i]nstalle la paille, on [c]ouvre le feu, on [s]ouffle la chandelle. Ma mère [r]épète : « un seul [o]util ne suffit pas ». Le [p]ain est sur la table, [m]ais la soupe est chaude. »"),
            ["Le mot est dans la fiche, partie « L'habitat ».", "Il commence par T.", "Il finit par S."],
            J("Quelle phrase de la fiche décrit les murs de la maison ?", P3, [P4, P8, P6], pos=0)),
    }
    return d
