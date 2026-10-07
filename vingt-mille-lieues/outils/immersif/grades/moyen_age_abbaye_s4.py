"""Salle 4 « L'hôtel-Dieu et l'aumône » (fiche : hotel-dieu)."""
from aide import *

F = "« L'Église auprès des pauvres et des malades »"
O1 = "Il n'existe ni hôpital public ni aide de l'État. L'Église assure ce que nous appellerions aujourd'hui la solidarité : soigner, héberger, nourrir, instruire."
O2 = "Hôtel-Dieu : établissement, souvent tenu par des religieux et des religieuses, qui accueille gratuitement les malades pauvres. On y soigne peu, mais on nourrit, on réchauffe et on veille."
O3 = "Hospice : accueil des pèlerins, des voyageurs et des vieillards."
O4 = "Léproserie : maison à l'écart de la ville, pour les malades de la lèpre."
O5 = "Aumône : distribution de pain et d'argent aux pauvres."
O6 = "L'hôtel-Dieu de Beaune est fondé le 4 août 1443 par Nicolas Rolin, chancelier du duc de Bourgogne, et son épouse Guigone de Salins, « pour les pauvres malades »."
O7 = "Sa grande salle, longue d'environ cinquante mètres, s'ouvre sur une chapelle : les malades suivaient la messe depuis leur lit."
O8 = "Cette aide est payée par la dîme (environ le dixième des récoltes), par les revenus des terres de l'Église, et par les dons des seigneurs et des marchands, qui espèrent ainsi gagner le salut de leur âme."
O9 = "Les premiers malades y sont reçus le 1er janvier 1452."


def donnees(svg, bloc=None):
    d = {}
    d["e4-1"] = {
        "mousse": tri(
            "Des personnes frappent à la porte de l'abbaye. Range chacune là où elle doit aller : clique sur une carte, puis sur une colonne.",
            [("soigner", "Soigner : l'hôtel-Dieu"), ("heberger", "Héberger : l'hospice")],
            [("Un malade pauvre qui a de la fièvre", "soigner"), ("Un vieillard très faible", "soigner"), ("Un pèlerin qui cherche un lit", "heberger"), ("Un marchand surpris par la nuit", "heberger")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Les malades vont à l'hôtel-Dieu.", "Ceux qui voyagent vont à l'hospice."]),
        "lieutenant": tri(
            "Mère Alix reçoit neuf personnes. Range chacune dans le lieu qui l'accueillera, puis choisis la phrase de la fiche qui définit l'hospice.",
            [("soigner", "Hôtel-Dieu"), ("heberger", "Hospice"), ("ecart", "Léproserie")],
            [("Une paysanne pauvre qui a de la fièvre", "soigner"), ("Un tailleur de pierre blessé sur un chantier", "soigner"), ("Un pèlerin en route vers Vézelay", "heberger"), ("Un vieillard sans famille", "heberger"),
             ("Un voyageur surpris par la nuit", "heberger"), ("Un malade de la lèpre", "ecart")],
            ["Un malade pauvre va à l'hôtel-Dieu.", "L'hospice accueille pèlerins, voyageurs et vieillards.", "La lèpre se soigne à l'écart de la ville."],
            J("Quelle phrase de la fiche définit l'hospice ?", O3, [O2, O4, O5], pos=1)),
        "second": qcm(
            carnet("Acte de fondation de l'hôtel-Dieu de Beaune", "(extrait). « Je fonde, et dote irrévocablement en la ville de Beaune, un hôpital pour les pauvres malades. » Nicolas Rolin, 4 août 1443. Les premiers malades y sont reçus le 1er janvier 1452.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Combien d'années séparent la fondation de l'arrivée des premiers malades ?", ["Environ 9 ans", "Environ 1 an", "Environ 50 ans", "Environ 100 ans"], 0, "1452 − 1443 = 9."),
             ("Pour qui l'hôpital est-il fondé ?", ["Pour les pauvres malades", "Pour les seigneurs", "Pour les soldats", "Pour les marchands"], 0, "« Pour les pauvres malades »."),
             ("Pourquoi la grande salle s'ouvre-t-elle sur une chapelle ?", ["Les malades suivaient la messe depuis leur lit", "Pour cacher les malades", "Pour chauffer la salle", "Pour loger les pèlerins"], 0, "Les soins comprennent la prière.")],
            ["Soustrais 1443 de 1452.", "Relis l'acte de fondation.", "La chapelle s'ouvre sur la grande salle."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", O6, [O7, O9, O8], pos=1)),
    }
    d["e4-2"] = {
        "mousse": vf(
            "Pour chaque phrase, clique sur « Vrai » ou sur « Faux », puis vérifie.",
            [("À l'hôtel-Dieu, les malades pauvres sont accueillis gratuitement.", True, "C'est le sens de la charité."), ("Le roi construit tous les hôpitaux.", False, "C'est l'Église."), ("L'aumône est un don de pain ou d'argent.", True, "On l'offre aux pauvres.")],
            ["Ouvre la fiche " + F + ".", "À l'hôtel-Dieu, les pauvres ne paient pas.", "L'aumône est un don."]),
        "lieutenant": qcm(
            carnet("Les ressources de l'hôtel-Dieu", "(d'après la fiche). L'aide aux pauvres est payée par la dîme (environ un dixième des récoltes), par les revenus des terres de l'Église et par les dons des seigneurs et des marchands.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Qui paie l'aide aux pauvres ?", ["L'Église, grâce à la dîme, à ses terres et aux dons", "L'État", "Les malades eux-mêmes", "Le roi seul"], 0, "Ressources de l'Église."),
             ("Que représente la dîme ?", ["Environ un dixième des récoltes", "La moitié des récoltes", "Un centième des récoltes", "Toute la récolte"], 0, "Un dixième."),
             ("Pourquoi les seigneurs et les marchands font-ils des dons ?", ["Ils espèrent gagner le salut de leur âme", "Ils sont obligés par le roi", "Ils veulent être soignés gratuitement", "Ils veulent des terres"], 0, "Ils espèrent ainsi le salut.")],
            ["L'Église assure la solidarité.", "« Le dixième » : un sur dix.", "Les dons ont une raison religieuse."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", O8, [O1, O5, O2], pos=1)),
        "second": tri(
            "Mère Alix classe les moyens de l'aide aux pauvres. Range chaque carte : ce que l'Église reçoit, ou ce que l'Église donne. Puis choisis la phrase de la fiche qui énumère les ressources.",
            [("recoit", "Ce que l'Église reçoit"), ("donne", "Ce que l'Église donne")],
            [("La dîme", "recoit"), ("Les revenus de ses terres", "recoit"), ("Les dons des seigneurs et des marchands", "recoit"), ("Les soins gratuits à l'hôtel-Dieu", "donne"), ("Le pain de l'aumône", "donne"), ("L'accueil à l'hospice", "donne")],
            ["Ressources : dîme, terres, dons.", "L'aumône est un don de pain ou d'argent.", "L'hospice accueille pèlerins et voyageurs."],
            J("Quelle phrase de la fiche énumère les ressources de l'aide aux pauvres ?", O8, [O1, O5, O3], pos=2)),
    }
    d["e4-3"] = {
        "mousse": tri(
            "Range chaque phrase : l'Église soigne, héberge ou nourrit ? Clique sur une carte, puis sur une colonne.",
            [("soigner", "Soigner"), ("nourrir", "Nourrir")],
            [("Accueillir les malades pauvres", "soigner"), ("Veiller les malades la nuit", "soigner"), ("Distribuer du pain à la porte de l'abbaye", "nourrir"), ("Donner de la soupe aux pauvres", "nourrir")],
            ["Ouvre la fiche " + F + ".", "L'aumône est un don de pain.", "L'hôtel-Dieu soigne."]),
        "lieutenant": vf(
            "Mère Alix affirme cinq choses sur l'aide aux pauvres. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui parle des soins.",
            [("Il n'existe ni hôpital public ni aide de l'État.", True, "L'Église assure la solidarité."), ("À l'hôtel-Dieu, on soigne beaucoup avec des médicaments modernes.", False, "On soigne peu : on nourrit, on réchauffe, on veille."),
             ("Une léproserie est à l'écart de la ville.", True, "Pour les malades de la lèpre."), ("L'hospice accueille les pèlerins.", True, "Et les voyageurs et les vieillards."), ("L'hôtel-Dieu fait payer les malades.", False, "Il les accueille gratuitement.")],
            ["Il n'y a pas de médicaments modernes.", "L'hôtel-Dieu est gratuit.", "Pour la justification : cherche la phrase qui dit « on y soigne peu »."],
            J("Quelle phrase de la fiche parle des soins à l'hôtel-Dieu ?", O2, [O1, O4, O3], pos=2)),
        "second": vf(
            "Mère Alix a noté six phrases sur l'hôtel-Dieu de Beaune. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui situe la fondation.",
            [("L'hôtel-Dieu de Beaune est fondé en 1443.", True, "Le 4 août."), ("Il est fondé par Nicolas Rolin et son épouse Guigone de Salins.", True, "« Pour les pauvres malades »."), ("Nicolas Rolin est chancelier du roi de France.", False, "Du duc de Bourgogne."),
             ("La grande salle fait environ cinquante mètres.", True, "Longue d'environ cinquante mètres."), ("Les premiers malades sont reçus en 1443.", False, "Le 1er janvier 1452."), ("La grande salle s'ouvre sur une chapelle.", True, "Les malades suivaient la messe.")],
            ["Fondation en 1443, premiers malades en 1452.", "Rolin est chancelier du duc de Bourgogne.", "La grande salle s'ouvre sur une chapelle."],
            J("Quelle phrase de la fiche situe la fondation ?", O6, [O9, O7, O8], pos=0)),
    }
    d["e4-4"] = {
        "lieutenant": assoc(
            "Mère Alix termine par des définitions. Relie chaque mot à sa définition précise, puis choisis la phrase de la fiche qui définit l'aumône.",
            [("L'hôtel-Dieu", "accueille gratuitement les malades pauvres"), ("L'hospice", "héberge pèlerins, voyageurs et vieillards"), ("La léproserie", "maison à l'écart de la ville pour la lèpre"), ("L'aumône", "distribution de pain et d'argent aux pauvres")],
            ["Le mot « aumône » parle d'un don.", "L'hospice accueille ceux qui voyagent.", "La léproserie est à l'écart."],
            J("Quelle phrase de la fiche définit l'aumône ?", O5, [O3, O4, O2], pos=1)),
        "second": assoc(
            "Mère Alix termine par un dernier tableau. Relie chaque date ou chaque nombre à ce qu'il désigne, puis choisis la phrase de la fiche qui donne la date de fondation.",
            [("4 août 1443", "fondation de l'hôtel-Dieu de Beaune"), ("1er janvier 1452", "arrivée des premiers malades"), ("Environ cinquante mètres", "longueur de la grande salle"), ("Un dixième des récoltes", "la dîme")],
            ["1443 : fondation.", "1452 : premiers malades.", "La dîme est environ un dixième."],
            J("Quelle phrase de la fiche donne la date de fondation ?", O6, [O9, O7, O8], pos=2)),
    }
    return d
