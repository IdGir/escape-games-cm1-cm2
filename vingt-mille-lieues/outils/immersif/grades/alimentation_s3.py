"""Salle 3 « La table de dégustation » (fiche : mastication)."""
from aide import *

F = "« Dans la bouche : mâcher »"
M1 = "Les dents assurent la mastication : incisives (couper), canines (déchirer), prémolaires et molaires (broyer)."
M2 = "Un enfant a 20 dents de lait ; un adulte a 32 dents."
M3 = "La salive, fabriquée par les glandes salivaires, mouille les aliments."
M4 = "Tout au long du trajet, la texture change : du morceau dur au bol alimentaire, puis à la bouillie de l'estomac et au liquide de l'intestin."
M5 = "Avec un miroir, on repère de l'avant vers le fond : les incisives, plates et coupantes ; les canines, pointues ; puis les prémolaires et les molaires, larges, avec des bosses qui écrasent."
M6 = "Vers 6 ans, les dents de lait commencent à tomber et les dents définitives les remplacent, plus nombreuses : c'est pourquoi l'adulte a des prémolaires et l'enfant n'en a pas."
M7 = "Mâcher longtemps aide l'estomac."


def donnees(svg, bloc=None):
    d = {}
    d["e3-1"] = {
        "mousse": tri(
            "Rosalie montre à quoi servent les dents. Range chaque dent : elle coupe ou déchire, ou elle écrase. Clique sur une carte, puis sur une colonne.",
            [("couper", "Elle coupe ou déchire"), ("ecraser", "Elle écrase")],
            [("Les incisives", "couper"), ("Les canines", "couper"), ("Les molaires", "ecraser"), ("Les prémolaires", "ecraser")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Les dents de devant coupent.", "Les dents du fond sont larges : elles écrasent."]),
        "lieutenant": vf(
            "Rosalie affiche cinq affirmations sur les dents. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui donne le nombre de dents d'un enfant et d'un adulte.",
            [("Un enfant a 20 dents de lait.", True, "Les dents de lait sont moins nombreuses."), ("Un adulte a 32 dents.", True, "Les dents définitives sont plus nombreuses."),
             ("Les canines servent à écraser.", False, "Elles déchirent."), ("L'enfant a des prémolaires comme l'adulte.", False, "Il n'en a pas : elles viennent avec les dents définitives."),
             ("Les incisives sont plates et coupantes.", True, "Ce sont les dents de devant.")],
            ["Compte : 20 dents de lait, 32 dents définitives.", "Les canines sont pointues.", "Les prémolaires apparaissent avec les dents définitives."],
            J("Quelle phrase de la fiche donne le nombre de dents d'un enfant et d'un adulte ?", M2, [M1, M6, M5], pos=1)),
        "second": qcm(
            carnet("Fiche dentaire de Léo, 7 ans", "(inventée pour le jeu). Léo vient de perdre une incisive de lait. Sa dentiste lui dit : « Tu as encore 20 dents de lait, et les dents définitives vont prendre leur place. »")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Pourquoi Léo perd-il des dents de lait vers 6 ans ?", ["Elles sont remplacées par les dents définitives", "Il mâche trop longtemps", "Il ne mange pas assez", "Elles fondent avec la salive"], 0, "Les dents définitives les remplacent."),
             ("Combien de dents aura Léo une fois adulte ?", ["32", "20", "28", "40"], 0, "32 dents définitives."),
             ("Léo a-t-il déjà des prémolaires ?", ["Non : elles viennent avec les dents définitives", "Oui : dès la naissance", "Oui : ce sont ses incisives", "On ne peut pas savoir"], 0, "L'enfant n'a pas de prémolaires.")],
            ["Les dents de lait tombent et sont remplacées.", "Compare 20 dents de lait et dents définitives.", "Les prémolaires n'existent pas chez l'enfant."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", M2, [M1, M5, M3], pos=0)),
    }
    d["e3-2"] = {
        "mousse": assoc(
            "Rosalie montre le moulage d'une mâchoire. Regarde le moulage, puis relie chaque dent à son rôle. Clique sur une dent, puis sur son rôle.\n" + svg("e3-2", "matelot"),
            [("une incisive", "couper"), ("une canine", "déchirer"), ("une molaire", "écraser")],
            ["Ouvre la fiche " + F + ".", "Les incisives sont tout devant.", "Les molaires, tout au fond, sont larges."]),
        "lieutenant": qcm(
            "Rosalie montre le moulage d'une mâchoire d'adulte, vue de dessus (repères 1 à 4). Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3."
            + svg("e3-2", "timonier"),
            [("Quel repère montre la dent qui déchire ?", ["Le repère 4 : la canine", "Le repère 2 : l'incisive", "Le repère 1 : la molaire", "Le repère 3 : la prémolaire"], 0, "La canine est pointue."),
             ("Quel repère montre une dent qui sert à broyer, tout au fond ?", ["Le repère 1", "Le repère 2", "Le repère 4", "Aucun"], 0, "Les molaires sont au fond."),
             ("Quelles dents manquent sur la mâchoire d'un enfant de 5 ans ?", ["Les prémolaires", "Les incisives", "Les canines", "Toutes les dents"], 0, "Il n'en a pas avant les dents définitives.")],
            ["Les canines sont pointues.", "Les molaires sont tout au fond.", "Les prémolaires viennent avec les dents définitives."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", M6, [M2, M1, M5], pos=2)),
        "second": tri(
            "Rosalie teste ses dents sur différents aliments. Range chaque action avec la dent qui s'en charge, puis choisis la phrase de la fiche qui donne le rôle de chaque famille de dents.",
            [("inc", "Incisives"), ("can", "Canines"), ("mol", "Prémolaires et molaires")],
            [("Couper une tranche de pain", "inc"), ("Croquer le bord d'une pomme", "inc"), ("Déchirer un morceau de viande", "can"), ("Arracher un bout de baguette dure", "can"),
             ("Écraser des noix", "mol"), ("Broyer des céréales", "mol")],
            ["Devant : couper. Pointues : déchirer. Au fond : broyer.", "Les prémolaires et les molaires ont des bosses qui écrasent.", "Les canines sont pointues."],
            J("Quelle phrase de la fiche donne le rôle de chaque famille de dents ?", M1, [M2, M5, M7], pos=1)),
    }
    d["e3-3"] = {
        "mousse": lettres(
            "Trouve le mot qui correspond à cette définition : « Elle sert à mâcher et sort de la gencive. » Ses lettres sont cachées en couleur dans le texte de Rosalie, dans le désordre. Clique-les dans l'ordre qui forme le mot (4 lettres). Deux lettres sont des pièges.",
            ["D", "E", "N", "T"],
            marque("Avant de manger, Rosalie lav[e] la pomme, la coupe, puis la croque : le bruit mon[t]e jusqu'à ses oreilles. Elle mâche lentement, sans [n]ul souci, en regardant [d]ehors, et [s]ourit. [M]iam !"),
            ["Ouvre la fiche " + F + ".", "Le mot commence par D.", "On en a 20 quand on est petit, 32 quand on est grand."]),
        "lieutenant": tri(
            "Rosalie classe ce qui se passe dans la bouche et ce qui se passe plus loin. Range chaque carte, puis choisis la phrase de la fiche qui explique le rôle de la salive.",
            [("bouche", "Dans la bouche"), ("loin", "Plus loin dans le tube digestif")],
            [("Couper avec les incisives", "bouche"), ("Mouiller avec la salive", "bouche"), ("Écraser avec les molaires", "bouche"),
             ("Brasser en bouillie dans l'estomac", "loin"), ("Faire passer les nutriments dans le sang", "loin"), ("Récupérer l'eau dans le gros intestin", "loin")],
            ["La salive est fabriquée dans la bouche.", "L'estomac et l'intestin sont plus loin.", "Trois cartes dans chaque colonne."],
            J("Quelle phrase de la fiche explique le rôle de la salive ?", M3, [M1, M4, M7], pos=2)),
        "second": vf(
            "Rosalie a noté six phrases dans son carnet de dégustation. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui décrit le changement de texture de la bouchée.",
            [("La salive est fabriquée par les glandes salivaires.", True, "Elle mouille les aliments."), ("La salive fait grossir les dents.", False, "Elle mouille les aliments."),
             ("La bouchée devient un bol alimentaire dans la bouche.", True, "Mâchée et mouillée."), ("La bouchée devient une bouillie dans l'estomac.", True, "Elle est brassée."),
             ("La texture de la bouchée reste la même pendant tout le voyage.", False, "Elle change du dur au liquide."), ("Mâcher longtemps n'a aucun effet sur la digestion.", False, "Mâcher longtemps aide l'estomac.")],
            ["La texture change : dur, mou, bouillie, liquide.", "Les glandes salivaires fabriquent la salive.", "Mâcher longtemps aide l'estomac."],
            J("Quelle phrase de la fiche décrit le changement de texture de la bouchée ?", M4, [M3, M7, M1], pos=0)),
    }
    d["e3-4"] = {
        "lieutenant": lettres(
            "Trouve le mot qui correspond à cette définition : « Ce qui change tout au long du trajet de la bouchée : dur, mou, liquide. » Ses lettres sont cachées en couleur dans le texte de Rosalie, dans le désordre. Clique-les dans l'ordre qui forme le mot (7 lettres). Trois lettres sont des pièges.",
            ["T", "E", "X", "T", "U", "R", "E"],
            marque("Au dessert, Rosalie sert une pomme : on la cro[q]ue, c'est dur ; on la mâche, c'e[s]t mou ; pu[i]s la bouchée avance dans le [t]ube. Rosalie not[e] e[x]actement ce qu'elle sent : plus rien n'est pa[r]eil d'une étape à l'autre, le [t]out change. Elle sourit, un peu s[u]rprise, mais ravie. Et r[e]vient la salive."),
            ["Le mot désigne la façon dont l'aliment est : dure, molle, liquide.", "Il commence par T et finit par E.", "Deux lettres se répètent : le T et le E."],
            J("Quelle phrase de la fiche cite ce mot ?", M4, [M3, M1, M7], pos=2)),
        "second": lettres(
            "Trouve le mot qui correspond à cette définition : « Organes qui fabriquent la salive. » Ses lettres sont cachées en couleur dans le texte de Rosalie, dans le désordre. Clique-les dans l'ordre qui forme le mot (7 lettres). Trois lettres sont des pièges.",
            ["G", "L", "A", "N", "D", "E", "S"],
            marque("Au [d]épart du repas, Rosalie [l]ève le nez : l'o[d]eur du pain frais lui fait venir l'eau à la bouche. Il y a des [g]ens qui disent que c'est magique ; Rosalie explique : « c'est un [e]ffet des gla[n]des, qui fabriquent la salive. » Pui[s] elle croque, [a]vec bonheur, un [p]etit morceau de [z]este."),
            ["Le mot est un pluriel : il finit par S.", "Ce sont des organes, comme les glandes salivaires.", "Il commence par G et se termine par DES."],
            J("Quelle phrase de la fiche cite ces organes ?", M3, [M1, M4, M7], pos=1)),
    }
    return d
