"""Salle 3 « L'atelier du Cloux » (fiche : leonard-de-vinci)."""
from aide import *

F = "« Léonard de Vinci, l'artiste invité »"
L1 = "Né le 15 avril 1452 à Vinci, près de Florence, Léonard se forme dans un atelier de peintre."
L2 = "Il peint des portraits (la Joconde, commencée vers 1503), dessine l'Homme de Vitruve (vers 1490), étudie l'anatomie, le vol des oiseaux, l'eau."
L3 = "Ingénieur, il imagine des machines, des fortifications, des canaux."
L4 = "Ses carnets, des milliers de pages, sont souvent écrits de droite à gauche, comme dans un miroir."
L5 = "Ses projets d'inventions (machine volante, char…) sont restés sur le papier."
L6 = "En 1516, à 64 ans, il arrive à Amboise. François Ier lui donne le manoir du Cloux et le titre de « premier peintre, ingénieur et architecte du roi »."
L7 = "Il meurt au Cloux le 2 mai 1519 ; il repose aujourd'hui dans la chapelle Saint-Hubert du château."


def donnees(svg, bloc=None):
    d = {}
    d["e3-1"] = {
        "mousse": assoc(
            "Relie chaque œuvre de Léonard au talent qu'elle montre : clique sur une œuvre, puis sur la bonne étiquette.",
            [("La Joconde", "un portrait peint"), ("La machine volante de ses carnets", "une invention restée sur le papier"), ("Le vol des oiseaux", "une observation de la nature")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "La Joconde est un tableau.", "Une machine dessinée est une invention."]),
        "lieutenant": vf(
            "Tommaso a noté cinq phrases sur Léonard. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui parle de ses carnets.",
            [("Léonard est né à Vinci, près de Florence.", True, "En 1452."), ("Il a toujours vécu à Amboise.", False, "Il y arrive en 1516, à 64 ans."), ("Ses carnets sont souvent écrits de droite à gauche.", True, "Comme dans un miroir."),
             ("Ses machines volantes ont toutes volé de son vivant.", False, "Elles sont restées sur le papier."), ("Il étudie l'anatomie, l'eau et le vol des oiseaux.", True, "En plus de peindre.")],
            ["Léonard naît en 1452.", "Il arrive à Amboise en 1516.", "Pour la justification : cherche la phrase qui parle d'un miroir."],
            J("Quelle phrase de la fiche parle des carnets de Léonard ?", L4, [L2, L5, L3], pos=1)),
        "second": qcm(
            carnet("Biographie de Léonard", "(d'après la fiche). Né le 15 avril 1452 à Vinci, il arrive à Amboise en 1516 à 64 ans, et meurt au Cloux le 2 mai 1519. Il repose dans la chapelle Saint-Hubert du château d'Amboise.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Combien de temps Léonard vit-il à Amboise ?", ["Environ 3 ans", "Environ 30 ans", "Environ 13 ans", "Environ 1 an"], 0, "1519 − 1516 = 3."),
             ("Quel titre le roi lui donne-t-il ?", ["Premier peintre, ingénieur et architecte du roi", "Roi d'Italie", "Maître d'armes", "Chevalier"], 0, "Avec le manoir du Cloux."),
             ("Où repose-t-il aujourd'hui ?", ["Dans la chapelle Saint-Hubert du château d'Amboise", "À Florence", "À Vinci", "Au Louvre"], 0, "Au château d'Amboise.")],
            ["1519 moins 1516.", "Le roi lui donne aussi un manoir.", "La chapelle porte le nom d'un saint chasseur."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", L6, [L7, L1, L3], pos=2)),
    }
    d["e3-2"] = {
        "mousse": tri(
            "Les pages de Léonard sont mélangées. Range chaque page : peintre ou inventeur ? Clique sur une page, puis sur une colonne.",
            [("peintre", "Le peintre"), ("inventeur", "L'inventeur")],
            [("Un visage de femme qui sourit", "peintre"), ("Les plis d'une robe, au crayon", "peintre"), ("Une machine à ailes", "inventeur"), ("Des engrenages et des roues dentées", "inventeur")],
            ["Ouvre la fiche " + F + ".", "Un portrait : le peintre.", "Une machine : l'inventeur."]),
        "lieutenant": tri(
            "Tommaso classe les pages des carnets. Range chaque page dans la bonne colonne, puis choisis la phrase de la fiche qui décrit le travail d'ingénieur de Léonard.",
            [("peintre", "Le peintre"), ("ingenieur", "L'ingénieur"), ("savant", "L'observateur")],
            [("Un portrait peint à l'huile", "peintre"), ("L'Homme de Vitruve", "peintre"), ("Un plan de fortification", "ingenieur"), ("Un projet de canal", "ingenieur"), ("Le vol d'un oiseau, aile par aile", "savant"), ("L'étude de l'eau qui tourbillonne", "savant")],
            ["Machines, fortifications, canaux : l'ingénieur.", "Oiseaux, eau, anatomie : l'observateur.", "Portraits : le peintre."],
            J("Quelle phrase de la fiche décrit le travail d'ingénieur de Léonard ?", L3, [L2, L4, L5], pos=0)),
        "second": ordre(
            "Tommaso retrace la vie de Léonard. Remets ces cinq étapes dans l'ordre, puis choisis la phrase de la fiche qui donne l'âge de Léonard à son arrivée à Amboise.",
            [("Naissance à Vinci", "1452"), ("Il dessine l'Homme de Vitruve", "vers 1490"), ("Il commence la Joconde", "vers 1503"), ("Il s'installe au Cloux, à Amboise", "1516"), ("Il meurt au Cloux", "2 mai 1519")],
            ["Compare les dates.", "Vitruve vers 1490, Joconde vers 1503.", "La mort vient en dernier."],
            J("Quelle phrase de la fiche donne l'âge de Léonard à son arrivée à Amboise ?", L6, [L1, L7, L2], pos=2)),
    }
    d["e3-3"] = {
        "mousse": intrus(
            "Trois de ces cartes sont vraies. Une seule est fausse à propos de Léonard. Clique sur l'intrus, puis vérifie.",
            [("Il naît en Italie, à Vinci", False), ("Il peint la Joconde", False), ("Il remplit des carnets de dessins", False), ("Il devient roi de France", True)],
            ["Ouvre la fiche " + F + ".", "Léonard est un artiste, pas un roi.", "Trois cartes sont vraies."]),
        "lieutenant": qcm(
            carnet("Le titre donné par le roi", "(d'après la fiche). En 1516, François Ier confie à Léonard le manoir du Cloux et le nomme « premier peintre, ingénieur et architecte du roi ».")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Qui donne ce titre à Léonard ?", ["François Ier", "Charles VIII", "Gutenberg", "Colombe"], 0, "Le roi."),
             ("Combien de métiers le titre cite-t-il ?", ["Trois : peintre, ingénieur, architecte", "Un", "Deux", "Quatre"], 0, "Peintre, ingénieur, architecte."),
             ("Où Léonard vit-il ses dernières années ?", ["Au manoir du Cloux, à Amboise", "À Florence", "À Chambord", "À Paris"], 0, "Le Cloux, aujourd'hui Clos Lucé.")],
            ["Le roi invite Léonard.", "Compte les métiers.", "Le manoir s'appelle aujourd'hui le Clos Lucé."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", L6, [L1, L3, L7], pos=1)),
        "second": vf(
            "Tommaso a noté six phrases sur Léonard. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui corrige la légende « ses machines ont volé ».",
            [("Léonard est né à Vinci le 15 avril 1452.", True, "Près de Florence."), ("Léonard a fait voler sa machine devant le roi.", False, "Elle est restée sur le papier."), ("Il arrive à Amboise en 1516, à 64 ans.", True, "Le roi lui donne le Cloux."),
             ("Il meurt à Amboise le 2 mai 1519.", True, "Au Cloux."), ("Les maquettes d'aujourd'hui datent de son époque.", False, "Elles ont été construites récemment."), ("Ses carnets ne contiennent que des tableaux.", False, "Machines, anatomie, eau, oiseaux.")],
            ["Ses inventions sont restées dessinées.", "Les maquettes sont récentes.", "Ses carnets sont variés."],
            J("Quelle phrase de la fiche corrige la légende « ses machines ont volé » ?", L5, [L3, L4, L2], pos=1)),
    }
    d["e3-4"] = {
        "lieutenant": lettres(
            "Trouve le mot qui correspond à cette définition : « Petits cahiers où Léonard note ses idées et ses dessins. » Ses lettres sont cachées en couleur dans le texte de Tommaso, dans le désordre. Clique-les dans l'ordre qui forme le mot (7 lettres). Deux lettres sont des pièges.",
            ["C", "A", "R", "N", "E", "T", "S"],
            marque("Tommaso écrit : « Le soir, Léonard [t]rempe sa plume et dessine un oiseau. Il [r]emplit des pages entières, de droite à gauche. Moi, je [c]ontemple ses croquis ; je n'ai jamais vu de dessins plus [e]xacts. Il se[n]t mon regard et sourit. Puis il [a]ttrape un autre feuillet. [S]a main ne s'arrête jamais. Je [p]ars me coucher ; [m]a plume est usée. »"),
            ["Le mot désigne de petits cahiers.", "Il commence par C.", "Il finit par S : il y en a des milliers de pages."],
            J("Quelle phrase de la fiche cite ce mot ?", L4, [L5, L3, L2], pos=2)),
        "second": lettres(
            "Trouve le mot qui correspond à cette définition : « L'étude du corps humain, que Léonard pratique en dessinant les muscles et les os. » Ses lettres sont cachées en couleur dans le texte de Tommaso, dans le désordre. Clique-les dans l'ordre qui forme le mot (8 lettres). Deux lettres sont des pièges.",
            ["A", "N", "A", "T", "O", "M", "I", "E"],
            marque("Tommaso écrit : « Léonard dessine le corps humain : les muscles, les os, les tendons. Il dit qu'il faut tout regarder avec soin. [A]u départ, j'ai peur ; mais je regarde. Il note chaque d[e]ssin, il [m]esure chaque os. Le [t]endon est dessiné à part ; je [n]ote son nom. Ses dessins d[o]nnent envie d'apprendre. Un [a]utre jour, il [i]ra voir des malades. Pour moi, c'est un jeu : je [p]ose ma plume, je [z]one un peu. »"),
            ["Le mot a huit lettres.", "Il commence par A et finit par E.", "C'est l'étude du corps humain."],
            J("Quelle phrase de la fiche cite ce mot ?", L2, [L1, L4, L6], pos=1)),
    }
    return d
