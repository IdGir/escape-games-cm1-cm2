"""Salle 5 « Le moulin du seigneur » (fiche : seigneur-et-paysans)."""
from aide import *

F = "« Seigneurs et paysans »"
S1 = "La seigneurie est le domaine du seigneur. Elle se divise en deux : la réserve, que le seigneur fait cultiver pour lui, et les tenures, confiées aux familles paysannes."
S2 = "la corvée : journées de travail gratuit sur la réserve (labours, fenaison, charrois…) ;"
S3 = "le cens : somme d'argent fixe versée chaque année pour la tenure ;"
S4 = "le champart : une part de la récolte ;"
S5 = "les banalités : obligation d'utiliser, contre paiement, le moulin, le four et le pressoir du seigneur."
S6 = "La dîme (environ un dixième des récoltes) n'est pas due au seigneur mais à l'Église."
S7 = "Certains paysans sont des serfs : ils ne sont pas libres, car ils sont attachés à la terre du seigneur ; ils ne peuvent ni la quitter ni se marier hors de la seigneurie sans autorisation, et paient des taxes particulières."
S8 = "Un serf n'est pas un esclave : il a une maison, une famille, une terre à cultiver."
S9 = "En échange, le seigneur doit protéger les habitants, leur ouvrir le château en cas de danger et rendre la justice."
S10 = "C'est un échange, mais c'est le seigneur qui fixe les règles et qui en profite le plus."
S11 = "À partir des XIIe et XIIIe siècles, beaucoup de serfs obtiennent leur liberté ; les paysans libres sont appelés vilains, mais ils doivent eux aussi les redevances."
S12 = "Le meunier garde une partie de la farine pour payer ce service."


def donnees(svg, bloc=None):
    d = {}
    d["e5-1"] = {
        "mousse": intrus(
            "Le paysan doit trois de ces charges au seigneur. Une autre est versée à l'Église. Trouve-la. Clique sur l'intrus, puis vérifie.",
            [("La corvée", False), ("Le cens", False), ("Le four banal", False), ("La dîme", True)],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Le mot dîme fait penser au nombre dix.", "Elle ne va pas au château mais à l'église."]),
        "lieutenant": intrus(
            "Perrine a noté cinq charges. Quatre sont dues au seigneur. Une est due à l'Église. Trouve l'intrus, puis choisis la phrase de la fiche qui justifie ton choix.",
            [("La corvée", False), ("Le cens", False), ("Le champart", False), ("Les banalités", False), ("La dîme", True)],
            ["Une charge ne va pas au château.", "La dîme représente environ un dixième des récoltes.", "Pour la justification : cherche la phrase qui nomme l'Église."],
            J("Quelle phrase de la fiche justifie ton choix ?", S6, [S4, S5, S3], pos=1)),
        "second": qcm(
            carnet("Registre de Perrine", "(inventé pour le jeu). Mahaut doit une journée de travail gratuit par semaine sur la réserve, 12 deniers par an pour sa tenure, et une part de sa récolte. Elle verse aussi un dixième de sa récolte à l'église.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Comment s'appelle la journée de travail gratuit sur la réserve ?", ["La corvée", "Le cens", "La dîme", "La banalité"], 0, "Travail gratuit sur la réserve."),
             ("Qui reçoit le dixième de la récolte ?", ["L'Église", "Le seigneur", "Le roi", "Le meunier"], 0, "La dîme est due à l'Église."),
             ("Les 12 deniers par an pour la tenure sont…", ["le cens", "la dîme", "la corvée", "le champart"], 0, "Somme d'argent fixe versée chaque année.")],
            ["Une charge est un travail, une autre de l'argent, une autre une part de récolte.", "Le dixième ne va pas au seigneur.", "Le cens est une somme d'argent fixe."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", S6, [S2, S4, S3], pos=0)),
    }
    d["e5-2"] = {
        "mousse": trous(
            "Complète le registre de Perrine. Clique sur une étiquette, puis sur le trou où elle va. Une étiquette est en trop.",
            "Le paysan travaille gratuitement pour le seigneur : c'est la [[corvée]]. Il doit moudre son grain au [[moulin]] du seigneur. En échange, le seigneur doit le [[protéger]].",
            ["corvée", "moulin", "protéger", "école"],
            ["Ouvre la fiche " + F + ".", "Le travail gratuit s'appelle la corvée.", "Le seigneur doit aider les habitants en cas de danger."]),
        "lieutenant": trous(
            "Perrine a écrit le registre de la seigneurie, mais il manque des mots. Clique sur une étiquette, puis sur le trou où elle va. Quatre étiquettes sont en trop. Puis choisis la phrase de la fiche qui justifie le mot « banalités ».",
            "La seigneurie se divise en deux : la [[réserve]], que le seigneur fait cultiver pour lui, et les [[tenures]], confiées aux familles paysannes. Les paysans doivent utiliser, contre paiement, le moulin, le four et le pressoir du seigneur : ce sont les [[banalités]]. Ils versent aussi chaque année le [[cens]].",
            ["réserve", "tenures", "banalités", "cens", "dîme", "école", "marché", "salaire"],
            ["La fiche commence par la définition de la seigneurie.", "Moulin, four, pressoir : ce sont des obligations.", "Le cens est une somme d'argent."],
            J("Quelle phrase de la fiche justifie le mot « banalités » ?", S5, [S3, S6, S2], pos=1)),
        "second": trous(
            "Perrine compare deux paysans. Complète son texte. Clique sur une étiquette, puis sur le trou où elle va. Quatre étiquettes sont en trop. Puis choisis la phrase de la fiche qui explique ce que le meunier garde.",
            "Dans la seigneurie, les paysans n'ont pas le droit de [[moudre]] leur grain ailleurs qu'au moulin du seigneur. Le meunier garde une partie de la [[farine]] pour payer ce service. Cette obligation s'appelle une [[banalité]]. Le serf est attaché à la [[terre]] du seigneur, mais il n'est pas un [[esclave]].",
            ["moudre", "farine", "banalité", "terre", "esclave", "dîme", "château", "marché", "école"],
            ["Le moulin est la banalité la plus connue.", "Le serf n'est pas libre, mais il a une maison et une famille.", "La farine sort du moulin."],
            J("Quelle phrase de la fiche explique ce que le meunier garde ?", S12, [S5, S8, S10], pos=3)),
    }
    d["e5-3"] = {
        "mousse": tri(
            "Range chaque étiquette : ce que le paysan doit au seigneur, ou ce que le seigneur doit au paysan. Clique sur une carte, puis sur une colonne.",
            [("pay", "Le paysan doit au seigneur"), ("sei", "Le seigneur doit au paysan")],
            [("Travailler gratuitement sur ses terres", "pay"), ("Payer le cens", "pay"), ("Le protéger en cas de guerre", "sei"), ("Rendre la justice", "sei")],
            ["Ouvre la fiche " + F + ".", "Qui travaille sur les terres de l'autre ?", "Le seigneur doit protéger et juger."]),
        "lieutenant": tri(
            "Perrine range les redevances selon leur nature. Range chaque carte, puis choisis la phrase de la fiche qui définit le cens.",
            [("trav", "Du travail"), ("arg", "De l'argent"), ("part", "Une part de produit")],
            [("La corvée", "trav"), ("Les journées de labour sur la réserve", "trav"), ("Le cens", "arg"), ("La somme versée chaque année pour la tenure", "arg"), ("Le champart", "part"), ("Une part de la récolte", "part")],
            ["Corvée : on donne des journées. Cens : on donne de l'argent. Champart : on donne une part.", "Le cens est une somme fixe.", "Le champart est proportionnel à la récolte."],
            J("Quelle phrase de la fiche définit le cens ?", S3, [S2, S4, S5], pos=1)),
        "second": tri(
            "Perrine classe des situations selon le statut du paysan. Range chaque carte : serf, vilain (paysan libre), ou les deux. Puis choisis la phrase de la fiche qui définit le serf.",
            [("serf", "Serf seulement"), ("vilain", "Vilain seulement"), ("deux", "Serf et vilain")],
            [("Attaché à la terre du seigneur", "serf"), ("Ne peut pas se marier hors de la seigneurie sans autorisation", "serf"), ("Paysan libre", "vilain"), ("Peut quitter la seigneurie", "vilain"), ("Doit des redevances au seigneur", "deux"), ("A une maison et une famille", "deux")],
            ["Un serf n'est pas libre.", "Un vilain est libre, mais il doit les redevances.", "Les deux ont une maison et une famille."],
            J("Quelle phrase de la fiche définit le serf ?", S7, [S11, S8, S10], pos=2)),
    }
    d["e5-4"] = {
        "lieutenant": {
            "type": "plan", "titre": "Libre ou serf ?", "colonnes": 2,
            "cases": [{"libelle": "Un serf est…", "reponse": "attaché à la terre du seigneur"}, {"libelle": "Un serf n'est pas…", "reponse": "un esclave"},
                      {"libelle": "Un vilain est…", "reponse": "un paysan libre"}, {"libelle": "Un vilain doit…", "reponse": "les redevances"},
                      {"libelle": "La dîme est due…", "reponse": "à l'Église"}, {"libelle": "Le seigneur doit…", "reponse": "protéger et rendre la justice"}],
            "etiquettes": ["attaché à la terre du seigneur", "un esclave", "un paysan libre", "les redevances", "à l'Église", "protéger et rendre la justice", "au roi", "des vacances"],
            "consigne": "Perrine complète un tableau sur les statuts des paysans. Place chaque étiquette dans la bonne case. Deux étiquettes sont en trop. Puis choisis la phrase de la fiche qui explique ce qu'est un serf.",
            "indices": ["Le serf n'est pas libre, mais ce n'est pas un esclave.", "Un vilain est un paysan libre, mais il doit tout de même les redevances.", "La dîme n'est pas due au seigneur."],
            "justification": J("Quelle phrase de la fiche explique ce qu'est un serf ?", S7, [S8, S11, S9], pos=1)},
        "second": vf(
            "Perrine termine par six phrases sur l'échange entre le seigneur et les paysans. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui juge cet échange.",
            [("En échange des redevances, le seigneur doit protéger les habitants.", True, "Et leur ouvrir le château en cas de danger."), ("Le seigneur doit aussi rendre la justice.", True, "C'est un de ses devoirs."),
             ("Les règles de l'échange sont fixées à égalité entre le seigneur et le paysan.", False, "C'est le seigneur qui fixe les règles."), ("Le serf est un esclave.", False, "Il a une maison, une famille, une terre à cultiver."),
             ("Beaucoup de serfs obtiennent leur liberté aux XIIe et XIIIe siècles.", True, "Les paysans libres sont appelés vilains."), ("La dîme est due au seigneur.", False, "Elle est due à l'Église.")],
            ["Le seigneur a des devoirs, mais il fixe les règles.", "Un serf n'est pas un esclave.", "La dîme va à l'Église."],
            J("Quelle phrase de la fiche juge l'échange entre seigneur et paysans ?", S10, [S9, S1, S11], pos=0)),
    }
    return d
