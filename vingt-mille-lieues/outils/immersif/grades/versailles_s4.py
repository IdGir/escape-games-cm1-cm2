"""Salle 4 « La chambre du roi » (fiche : journee-du-roi)."""
from aide import *

F = "« Une journée du roi à Versailles »"
Y1 = "8 h 30 : le lever. Le premier valet de chambre réveille le roi ; les courtisans entrent ensuite, chacun selon son rang."
Y2 = "10 h : la messe. 11 h : le conseil avec les ministres."
Y3 = "13 h : le dîner, servi au petit couvert dans la chambre : le roi est seul à table."
Y4 = "22 h : le souper au grand couvert, en public, avec la famille royale. Vers 23 h : le coucher."
Y5 = "Le duc de Saint-Simon écrit qu'avec un almanach et une montre, on pouvait dire, de très loin, ce que faisait le roi."
Y6 = "Enfant, Louis XIV a connu la Fronde (1648-1653) : une révolte d'une partie des grands nobles. À Versailles, il les garde près de lui."
Y7 = "Ils deviennent des courtisans : ils dépensent beaucoup pour paraître et attendent ses faveurs (logement, pension, honneurs). Occupés à lui plaire, ils ne se révoltent plus."
Y8 = "L'étiquette, c'est l'ensemble des règles de la cour : elle montre que tout tourne autour du roi."
Y9 = "À 19 h, trois soirs par semaine, les soirées d'appartement : jeux, musique, danse."


def donnees(svg, bloc=None):
    d = {}
    d["e4-1"] = {
        "mousse": ordre(
            "Remets la journée du roi dans l'ordre, du matin (en haut) au soir (en bas). Utilise les flèches ▲ et ▼.",
            [("Le lever", "8 h 30"), ("La messe", "10 h"), ("Le coucher", "23 h")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "8 h 30 vient avant 10 h.", "La journée se termine par le coucher."]),
        "lieutenant": ordre(
            "Dame Isabeau décrit la journée du roi. Remets ces six moments dans l'ordre, puis choisis la phrase de la fiche qui décrit le dîner du roi.",
            [("Le lever", "8 h 30"), ("Le conseil avec les ministres", "11 h"), ("Le dîner au petit couvert", "13 h"), ("La chasse ou la promenade", "l'après-midi"), ("Les soirées d'appartement", "19 h"), ("Le souper au grand couvert", "22 h")],
            ["Compare les heures.", "Le conseil vient avant le dîner.", "Le souper est en public, le soir."],
            J("Quelle phrase de la fiche décrit le dîner du roi ?", Y3, [Y2, Y4, Y9], pos=1)),
        "second": qcm(
            carnet("Saint-Simon", "(d'après la fiche). Le duc de Saint-Simon écrit qu'avec un almanach et une montre, on pouvait dire, de très loin, ce que faisait le roi. Le dîner a lieu à 13 h, le souper à 22 h, le coucher vers 23 h.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 1.",
            [("Que veut dire Saint-Simon ?", ["Les journées du roi étaient réglées comme une horloge", "Le roi n'avait pas d'horaires", "Le roi voyageait sans cesse", "Le roi dormait toute la journée"], 0, "Un almanach et une montre suffisent."),
             ("Combien d'heures séparent le dîner du souper ?", ["9 heures", "3 heures", "12 heures", "1 heure"], 0, "22 − 13 = 9."),
             ("Quel repas se prend seul à table ?", ["Le dîner au petit couvert", "Le souper au grand couvert", "Le déjeuner", "Le goûter"], 0, "Au petit couvert, le roi est seul.")],
            ["Une journée réglée comme une horloge.", "Soustrais 13 de 22.", "Petit couvert : dans la chambre."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 1 ?", Y5, [Y3, Y4, Y1], pos=2)),
    }
    d["e4-2"] = {
        "mousse": intrus(
            "Trois de ces cartes décrivent la vie du roi à Versailles. Une seule n'y correspond pas. Clique sur l'intrus, puis vérifie.",
            [("Il assiste à la messe", False), ("Il tient conseil avec ses ministres", False), ("Il est habillé devant des courtisans", False), ("Il prépare lui-même ses repas", True)],
            ["Ouvre la fiche " + F + ".", "Le roi a des serviteurs pour tout.", "Qui prépare les repas ?"]),
        "lieutenant": vf(
            "Dame Isabeau affirme cinq choses sur la cour. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui explique pourquoi les nobles ne se révoltent plus.",
            [("Louis XIV a connu la Fronde, enfant.", True, "Entre 1648 et 1653."), ("À Versailles, il garde les nobles près de lui.", True, "Ils deviennent courtisans."), ("Les courtisans attendent des faveurs.", True, "Logement, pension, honneurs."),
             ("Les soirées d'appartement ont lieu tous les soirs.", False, "Trois soirs par semaine."), ("Le roi soupe seul dans sa chambre.", False, "Au grand couvert, en public.")],
            ["La Fronde est une révolte de nobles.", "Les soirées d'appartement : trois soirs par semaine.", "Le souper est en public."],
            J("Quelle phrase de la fiche explique pourquoi les nobles ne se révoltent plus ?", Y7, [Y6, Y8, Y9], pos=1)),
        "second": ordre(
            "Dame Isabeau explique comment le roi apprivoise les nobles. Remets ces cinq étapes dans l'ordre, puis choisis la phrase de la fiche qui définit l'étiquette.",
            ["Enfant, Louis XIV connaît la Fronde (1648-1653).", "Il décide de garder les grands nobles près de lui.", "Les nobles deviennent des courtisans.", "Ils dépensent pour paraître et attendent des faveurs.", "Occupés à lui plaire, ils ne se révoltent plus."],
            ["La Fronde vient avant Versailles.", "Les nobles deviennent courtisans avant d'attendre des faveurs.", "La conséquence est la fin des révoltes."],
            J("Quelle phrase de la fiche définit l'étiquette ?", Y8, [Y6, Y7, Y5], pos=0)),
    }
    d["e4-3"] = {
        "mousse": assoc(
            "Relie chaque mot de la cour à sa définition : clique sur un mot, puis sur la bonne définition.",
            [("Un courtisan", "un noble qui vit à la cour"), ("Le lever", "le réveil du roi, devant des invités"), ("Le grand couvert", "le repas du soir du roi, en public")],
            ["Ouvre la fiche " + F + ".", "Un courtisan vit à la cour.", "Le lever a lieu le matin."]),
        "lieutenant": tri(
            "Dame Isabeau range les moments de la journée. Range chaque moment dans la bonne colonne, puis choisis la phrase de la fiche qui décrit le souper.",
            [("prive", "Seul ou presque"), ("public", "Devant la cour")],
            [("Le dîner au petit couvert", "prive"), ("Le conseil avec les ministres", "prive"), ("La messe du matin", "prive"), ("Le lever, avec les courtisans", "public"), ("Le souper au grand couvert", "public"), ("Le coucher, devant des invités", "public")],
            ["Le petit couvert : seul à table.", "Le grand couvert : en public.", "Le lever : les courtisans entrent selon leur rang."],
            J("Quelle phrase de la fiche décrit le souper ?", Y4, [Y3, Y1, Y2], pos=2)),
        "second": vf(
            "Dame Isabeau a noté six phrases sur l'étiquette. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui décrit l'ordre d'entrée au lever.",
            [("Au lever, le premier valet de chambre réveille le roi.", True, "Puis les courtisans entrent."), ("Les courtisans entrent au hasard.", False, "Chacun selon son rang."), ("Le souper est au petit couvert.", False, "Au grand couvert."),
             ("L'étiquette est l'ensemble des règles de la cour.", True, "Tout tourne autour du roi."), ("Les courtisans dépensent beaucoup pour paraître.", True, "Pour obtenir des faveurs."), ("Le dîner est servi à 22 h.", False, "À 13 h.")],
            ["Le premier valet de chambre réveille le roi.", "Chacun entre selon son rang.", "Le dîner : 13 h. Le souper : 22 h."],
            J("Quelle phrase de la fiche décrit l'ordre d'entrée au lever ?", Y1, [Y8, Y4, Y5], pos=1)),
    }
    d["e4-4"] = {
        "lieutenant": trous(
            "Dame Isabeau a rédigé son carnet, mais il manque des mots. Clique sur une étiquette, puis sur le trou où elle va. Trois étiquettes sont en trop. Puis choisis la phrase de la fiche qui justifie le mot « Fronde ».",
            "Enfant, Louis XIV a connu la [[Fronde]], une révolte d'une partie des grands [[nobles]]. À Versailles, ils deviennent des [[courtisans]] et attendent des [[faveurs]]. Le roi les garde près de lui.",
            ["Fronde", "nobles", "courtisans", "faveurs", "paysans", "Réforme", "tolérance"],
            ["Relis le début de la partie « Pourquoi tant de règles ? ».", "Les nobles qui vivent à la cour sont des courtisans.", "Un logement ou une pension sont des faveurs."],
            J("Quelle phrase de la fiche justifie le mot « Fronde » ?", Y6, [Y7, Y8, Y5], pos=1)),
        "second": trous(
            "Dame Isabeau résume la journée du roi. Clique sur une étiquette, puis sur le trou où elle va. Quatre étiquettes sont en trop. Puis choisis la phrase de la fiche qui justifie le mot « conseil ».",
            "Le roi se lève à 8 h 30. À 10 h, il va à la [[messe]]. À 11 h, il tient [[conseil]] avec ses ministres. À 13 h, il [[dîne]] au petit couvert, [[seul]] à table. À 22 h, il [[soupe]] au grand couvert.",
            ["messe", "conseil", "dîne", "seul", "soupe", "chasse", "petit", "courtisans", "Fronde"],
            ["Une journée réglée comme une horloge.", "Le dîner est à 13 h.", "Le souper est au grand couvert."],
            J("Quelle phrase de la fiche justifie le mot « conseil » ?", Y2, [Y1, Y3, Y9], pos=0)),
    }
    return d
