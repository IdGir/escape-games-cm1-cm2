"""Salle 1 « La cour du Palais-Royal » : qu'est-ce qu'une Constitution ? (documents officiels cités dans les consignes)."""
from aide import *
from constitution_docs import *


def donnees(svg, bloc=None):
    d = {}
    d["e1-1"] = {
        "mousse": qcm(
            "Lis la question, clique sur la bonne réponse, puis vérifie.",
            [("Une Constitution, c'est…", ["l'ensemble des règles qui organisent la vie d'un pays", "le règlement intérieur d'une école", "la liste des habitants d'une ville"], 0, "C'est la règle du jeu d'un pays.")],
            ["Ouvre la fiche « La Constitution française » dans la Bibliothèque.", "Pense à la règle d'un jeu de société.", "Elle concerne tous les habitants."]),
        "lieutenant": qcm(
            ddhc(DDHC16, DDHC1, DDHC6) + " Réponds aux trois questions, puis choisis la phrase du document qui définit ce qu'est une Constitution.",
            [("Selon l'article 16, que faut-il pour qu'une société ait une Constitution ?", ["Garantir les droits et séparer les pouvoirs", "Avoir un roi", "Avoir une seule armée", "Voter chaque jour"], 0, "La garantie des droits et la séparation des pouvoirs."),
             ("Selon l'article 1, les hommes naissent…", ["libres et égaux en droits", "inégaux en droits", "soumis à un roi", "sans droits"], 0, "Libres et égaux en droits."),
             ("Pourquoi la séparation des pouvoirs est-elle essentielle ?", ["Si une seule personne détenait tous les pouvoirs, elle gouvernerait sans contrôle", "Pour avoir plus de ministres", "Pour changer de capitale", "Pour supprimer les lois"], 0, "Elle évite l'abus de pouvoir.")],
            ["Relis l'article 16.", "L'article 1 parle de liberté et d'égalité.", "Séparer les pouvoirs évite qu'un seul décide de tout."],
            J("Quelle phrase du document définit ce qu'est une Constitution ?", DDHC16, [DDHC1, DDHC6], pos=1)),
        "second": vf(
            c58(C3, C5, C6, C20) + " Maître Sylla affirme six choses. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase du document qui dit qui exerce la souveraineté.",
            [("Le Président de la République est élu au suffrage universel direct.", True, "Pour cinq ans."), ("Le Gouvernement détermine et conduit la politique de la Nation.", True, "Article 20."), ("La souveraineté nationale appartient au Président.", False, "Au peuple."),
             ("Le Président veille au respect de la Constitution.", True, "Article 5."), ("Le peuple n'exerce sa souveraineté que par référendum.", False, "Par ses représentants et par référendum."), ("Le mandat présidentiel dure sept ans.", False, "Cinq ans.")],
            ["La souveraineté appartient au peuple.", "Le peuple l'exerce par ses représentants et par référendum.", "Le mandat dure cinq ans."],
            J("Quelle phrase du document dit qui exerce la souveraineté nationale ?", C3, [C5, C6, C20], pos=2)),
    }
    d["e1-2"] = {
        "mousse": vf(
            "Pour chaque phrase, clique sur « Vrai » ou sur « Faux », puis vérifie.",
            [("La France est le seul pays du monde à avoir une Constitution.", False, "Presque tous les pays en ont une."), ("La Constitution est au-dessus de toutes les autres lois.", True, "C'est le texte le plus important."), ("En France, la Constitution est un texte écrit.", True, "On peut la lire.")],
            ["Ouvre la fiche « La Constitution française ».", "Presque tous les pays ont une Constitution.", "Elle est au sommet des lois."]),
        "lieutenant": vf(
            ddhc(DDHC4, DDHC6, DDHC11) + " Nour a noté cinq affirmations. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase du document qui définit la liberté.",
            [("La liberté consiste à pouvoir faire tout ce qui ne nuit pas à autrui.", True, "Article 4."), ("La loi est l'expression de la volonté générale.", True, "Article 6."), ("La libre communication des pensées est un droit précieux.", True, "Article 11."),
             ("La liberté permet de nuire aux autres.", False, "Elle s'arrête là où elle nuit à autrui."), ("La loi exprime la volonté d'un seul.", False, "De la volonté générale.")],
            ["La liberté s'arrête où commence celle des autres.", "La loi exprime la volonté générale.", "Article 4 : la liberté."],
            J("Quelle phrase du document définit la liberté ?", DDHC4, [DDHC6, DDHC11], pos=0)),
        "second": qcm(
            c58(C1, C1b, C2) + " Réponds aux trois questions, puis choisis la phrase du document qui définit la République.",
            [("Combien d'adjectifs qualifient la République à l'article 1 ?", ["4 : indivisible, laïque, démocratique et sociale", "2", "3", "5"], 0, "Quatre adjectifs."),
             ("Selon l'article 1, devant la loi, tous les citoyens sont…", ["égaux, sans distinction d'origine, de race ou de religion", "différents selon leur origine", "classés selon leur religion", "libres seulement s'ils votent"], 0, "Égalité devant la loi."),
             ("Quelle est la devise de la République ?", ["Liberté, Égalité, Fraternité", "Travail, Famille, Patrie", "Un pour tous, tous pour un", "Dieu et mon droit"], 0, "Article 2.")],
            ["Compte les adjectifs.", "L'égalité devant la loi est inscrite à l'article 1.", "La devise est à l'article 2."],
            J("Quelle phrase du document définit la République ?", C1, [C1b, C2], pos=0)),
    }
    d["e1-3"] = {
        "mousse": tri(
            "Range chaque carte dans la bonne colonne : clique sur une carte, puis sur une colonne.",
            [("leg", "Écrire et voter les lois"), ("exe", "Faire appliquer les lois")],
            [("Le Parlement", "leg"), ("Voter les lois", "leg"), ("Le Gouvernement", "exe"), ("Faire appliquer les lois", "exe")],
            ["Ouvre la fiche « La Constitution française ».", "« Législatif » vient de « loi ».", "« Exécutif » vient de « exécuter »."]),
        "lieutenant": tri(
            c58(C20, C24, C64) + " Nour range des tâches. Range chaque tâche dans la bonne colonne, puis choisis la phrase du document qui dit ce que fait le Parlement.",
            [("leg", "Pouvoir législatif"), ("exe", "Pouvoir exécutif"), ("jud", "Autorité judiciaire")],
            [("Voter la loi", "leg"), ("Contrôler l'action du Gouvernement", "leg"), ("Déterminer et conduire la politique de la Nation", "exe"), ("Appliquer les lois", "exe"), ("Rendre la justice", "jud"), ("Être indépendante du pouvoir politique", "jud")],
            ["Le Parlement vote et contrôle.", "Le Gouvernement conduit la politique.", "L'autorité judiciaire est indépendante."],
            J("Quelle phrase du document dit ce que fait le Parlement ?", C24, [C20, C64], pos=2)),
        "second": tri(
            ddhc(DDHC16, DDHC6, DDHC1) + " Nour classe des affirmations. Range chaque affirmation : le document l'affirme, ou il ne l'affirme pas. Puis choisis la phrase du document qui parle de séparation des pouvoirs.",
            [("oui", "Le document l'affirme"), ("non", "Le document ne l'affirme pas")],
            [("La loi est l'expression de la volonté générale.", "oui"), ("Une société sans séparation des pouvoirs n'a pas de Constitution.", "oui"), ("La garantie des droits doit être assurée.", "oui"),
             ("Le roi fait la loi seul.", "non"), ("La séparation des pouvoirs est facultative.", "non"), ("La loi exprime la volonté du plus fort.", "non")],
            ["Relis les deux articles.", "Article 16 : droits et séparation des pouvoirs.", "Article 6 : volonté générale."],
            J("Quelle phrase du document parle de séparation des pouvoirs ?", DDHC16, [DDHC6, DDHC1], pos=1)),
    }
    d["e1-4"] = {
        "lieutenant": lettres(
            ddhc(DDHC1, DDHC4, DDHC6) + " Trouve le mot qui correspond à cette définition : « Ce que garantit une Constitution à chacun : liberté, égalité… » Ses lettres sont cachées en couleur dans le texte de Maître Sylla, dans le désordre. Clique-les dans l'ordre qui forme le mot (6 lettres). Deux lettres sont des pièges.",
            ["D", "R", "O", "I", "T", "S"],
            marque("Maître Sylla écrit : « Une Constitution protège chacun. Le plus important est de [t]oujours respecter les [r]ègles que nous partageons. Je [d]is aux élèves : lisez, [o]bservez, [i]maginez, puis demandez-vous ce qui est [s]uffisant pour vivre ensemble. Et surtout, [p]osez des questions, même [m]aladroites. »"),
            ["Le mot a six lettres.", "Il commence par D.", "Liberté et égalité en sont deux exemples."],
            J("Quelle phrase du document dit que les hommes naissent égaux en… ce mot ?", DDHC1, [DDHC4, DDHC6], pos=0)),
        "second": lettres(
            ddhc(DDHC16, DDHC6, DDHC1) + " Trouve le mot qui correspond à cette définition : « Ce que la séparation garantit : exécutif, législatif, judiciaire. » Ses lettres sont cachées en couleur dans le texte de Maître Sylla, dans le désordre. Clique-les dans l'ordre qui forme le mot (8 lettres). Deux lettres sont des pièges.",
            ["P", "O", "U", "V", "O", "I", "R", "S"],
            marque("Maître Sylla écrit : « Dans notre République, la loi doit [v]aloir pour tous. Le [r]espect de la règle, c'est [o]béir à ce que nous avons voté. Que[l]le leçon ! [u]n principe : on [p]artage le pouvoir. Chaque [o]rgane, chaque [i]nstitution, a son rôle ; personne ne peut tout [s]eul décider. Voilà ! [m]erci à vous. »"),
            ["Le mot a huit lettres.", "Il commence par P et finit par S.", "On les sépare pour éviter l'abus."],
            J("Quelle phrase du document parle de la séparation de ces… ?", DDHC16, [DDHC6, DDHC1], pos=0)),
    }
    return d
