"""Salle 5 « Le cabinet du Conseil » (fiche : monarchie-absolue)."""
from aide import *

F = "« La monarchie absolue »"
A1 = "Roi en 1643, à 4 ans, Louis XIV gouverne d'abord avec sa mère et le cardinal Mazarin. À la mort de Mazarin, en 1661, il décide de régner sans Premier ministre."
A2 = "Il tient son pouvoir de Dieu (il est sacré à Reims) : c'est la monarchie absolue de droit divin."
A3 = "Il fait les lois, juge en dernier recours, décide de la guerre et des impôts."
A4 = "Des ministres comme Colbert (finances) le conseillent ; dans les provinces, des intendants appliquent ses ordres."
A5 = "Les guerres se succèdent pendant le règne. Elles coûtent très cher, comme la Cour. Les impôts pèsent surtout sur les paysans."
A6 = "Le grand hiver de 1709 provoque une terrible famine. À sa mort, en 1715, le royaume est agrandi, mais épuisé."
A7 = "Louis XIV veut une seule religion dans le royaume. Le 18 octobre 1685, par l'édit de Fontainebleau, il révoque l'édit de Nantes : le culte protestant est interdit, les temples sont détruits, les pasteurs chassés."
A8 = "Des soldats sont logés chez les protestants pour les forcer à se convertir (les dragonnades). Malgré l'interdiction, entre 200 000 et 300 000 protestants fuient à l'étranger."
A9 = "On prête à Louis XIV la phrase « L'État, c'est moi ». Aucun document ne prouve qu'il l'ait dite ; elle résume pourtant bien l'idée de monarchie absolue."


def donnees(svg, bloc=None):
    d = {}
    d["e5-1"] = {
        "mousse": tri(
            "Range chaque carte sous le bon roi. Clique sur une carte, puis sur une colonne.",
            [("h4", "Henri IV"), ("l14", "Louis XIV")],
            [("Il signe l'édit de Nantes en 1598", "h4"), ("Il met fin aux guerres de Religion", "h4"), ("Il s'installe à Versailles en 1682", "l14"), ("Il choisit le Soleil comme emblème", "l14")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "L'édit de Nantes : 1598.", "Versailles et le Soleil : Louis XIV."]),
        "lieutenant": tri(
            "Gabriel classe des décisions. Range chaque décision sous le bon roi, puis choisis la phrase de la fiche qui date le début du pouvoir personnel de Louis XIV.",
            [("h4", "Henri IV"), ("l14", "Louis XIV")],
            [("Il se convertit au catholicisme en 1593", "h4"), ("Il signe l'édit de Nantes", "h4"), ("Il est roi à 4 ans, en 1643", "l14"), ("Il règne sans Premier ministre à partir de 1661", "l14"), ("Il révoque l'édit de Nantes en 1685", "l14"), ("Il est sacré à Reims, selon le droit divin", "l14")],
            ["Henri IV : conversion et édit.", "Louis XIV : 1643, 1661, 1685.", "Mazarin meurt en 1661."],
            J("Quelle phrase de la fiche date le début du pouvoir personnel de Louis XIV ?", A1, [A2, A3, A4], pos=2)),
        "second": tri(
            "Gabriel classe des affirmations. Range chaque affirmation : la fiche l'affirme, ou elle ne l'affirme pas. Puis choisis la phrase de la fiche qui décrit les pouvoirs du roi.",
            [("oui", "La fiche l'affirme"), ("non", "La fiche ne l'affirme pas")],
            [("Le roi fait les lois et décide de la guerre et des impôts.", "oui"), ("Colbert conseille le roi pour les finances.", "oui"), ("Les impôts pèsent surtout sur les paysans.", "oui"),
             ("Le roi partage son pouvoir avec une assemblée élue.", "non"), ("Les nobles de la cour paient la plus grande part des impôts.", "non"), ("Mazarin gouverne seul après 1661.", "non")],
            ["Le roi fait les lois, juge, décide de la guerre et des impôts.", "Colbert s'occupe des finances.", "Aucune assemblée élue ne partage son pouvoir."],
            J("Quelle phrase de la fiche décrit les pouvoirs du roi ?", A3, [A4, A5, A2], pos=1)),
    }
    d["e5-2"] = {
        "mousse": qcm(
            "Réponds à la question, puis vérifie.",
            [("Dans une monarchie absolue, qui décide des lois, de la guerre et des impôts ?", ["Le roi", "Les habitants, par un vote", "Le pape"], 0, "Absolu veut dire sans limite.")],
            ["Ouvre la fiche " + F + ".", "Absolu veut dire « sans limite ».", "Le roi fait les lois."]),
        "lieutenant": qcm(
            carnet("Le règne de Louis XIV", "(d'après la fiche). Louis XIV est roi en 1643, à 4 ans. Il règne seul à partir de 1661. Il meurt en 1715. Des ministres comme Colbert le conseillent. Les guerres coûtent très cher, et les impôts pèsent surtout sur les paysans.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("Combien d'années Louis XIV règne-t-il au total ?", ["72 ans", "54 ans", "4 ans", "100 ans"], 0, "1715 − 1643 = 72."),
             ("Combien d'années gouverne-t-il seul ?", ["54 ans", "72 ans", "18 ans", "4 ans"], 0, "1715 − 1661 = 54."),
             ("Qui supporte surtout le poids des impôts ?", ["Les paysans", "Les nobles de la cour", "Les ministres", "Le roi"], 0, "Les paysans paient surtout.")],
            ["Soustrais 1643 de 1715.", "Soustrais 1661 de 1715.", "Les guerres coûtent cher."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", A5, [A4, A6, A3], pos=1)),
        "second": vf(
            "Gabriel a noté six phrases sur la fin du règne. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui résume l'état du royaume en 1715.",
            [("Les guerres se succèdent pendant le règne.", True, "Elles coûtent très cher."), ("Le grand hiver de 1709 provoque une famine.", True, "Une terrible famine."), ("Le royaume est agrandi à la mort du roi.", True, "Mais épuisé."),
             ("Le royaume est prospère en 1715.", False, "Il est épuisé."), ("La phrase « L'État, c'est moi » est prouvée par un document.", False, "Aucun document ne le prouve."), ("Louis XIV meurt en 1709.", False, "En 1715.")],
            ["La fin du règne est difficile.", "Aucun document ne prouve la phrase.", "Il meurt en 1715."],
            J("Quelle phrase de la fiche résume l'état du royaume en 1715 ?", A6, [A5, A9, A3], pos=2)),
    }
    d["e5-3"] = {
        "mousse": code(
            "Le coffre du Conseil est fermé par un cadenas. Écris le chiffre du roi de l'édit de Nantes (Henri …) et l'année où la cour s'installe à Versailles, puis ouvre.",
            [("Henri … (le chiffre)", "4", 1), ("Année de l'installation à Versailles", "1682", 4)],
            ["Ouvre la fiche " + F + ".", "Le roi de l'édit de Nantes : Henri IV.", "L'installation à Versailles : 1682."]),
        "lieutenant": tri(
            "Gabriel classe les causes et les conséquences de 1685. Range chaque carte, puis choisis la phrase de la fiche qui décrit la révocation de l'édit de Nantes.",
            [("mesures", "Les mesures de 1685"), ("consequences", "Les conséquences")],
            [("Le culte protestant est interdit", "mesures"), ("Les temples sont détruits", "mesures"), ("Les pasteurs sont chassés", "mesures"), ("Les dragonnades : soldats logés chez les protestants", "consequences"), ("Entre 200 000 et 300 000 protestants fuient à l'étranger", "consequences"), ("Le royaume perd des habitants", "consequences")],
            ["Les mesures : interdits, destruction, expulsion.", "Les conséquences : dragonnades, fuite.", "Relis la fiche."],
            J("Quelle phrase de la fiche décrit la révocation de l'édit de Nantes ?", A7, [A8, A1, A3], pos=2)),
        "second": code(
            "Le coffre du Conseil est fermé par un cadenas à trois cases. Combien d'années séparent la mort de Mazarin (1661) de la révocation de l'édit (1685) ? Combien d'années séparent l'édit de Nantes (1598) de sa révocation (1685) ? Quel est le nom du ministre des finances de Louis XIV (7 lettres) ?",
            [("Années entre 1661 et 1685", "24", 2), ("Années entre 1598 et 1685", "87", 2), ("Ministre des finances", "COLBERT", 7, False)],
            ["1685 − 1661.", "1685 − 1598.", "Son nom est dans la fiche."],
            J("Quelle phrase de la fiche cite le ministre des finances ?", A4, [A1, A5, A7], pos=0)),
    }
    d["e5-4"] = {
        "lieutenant": vf(
            "Gabriel a noté cinq phrases sur 1685. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui explique pourquoi les protestants fuient.",
            [("En 1685, Louis XIV révoque l'édit de Nantes.", True, "Par l'édit de Fontainebleau."), ("Après 1685, les protestants peuvent se réunir dans leurs temples.", False, "Les temples sont détruits."), ("Des soldats sont logés chez les protestants pour les forcer à se convertir.", True, "Ce sont les dragonnades."),
             ("Entre 200 000 et 300 000 protestants fuient à l'étranger.", True, "Malgré l'interdiction."), ("Louis XIV renforce la tolérance voulue par Henri IV.", False, "Il y met fin.")],
            ["Révoquer, c'est annuler.", "Les temples sont détruits.", "Les protestants fuient malgré l'interdiction."],
            J("Quelle phrase de la fiche explique pourquoi beaucoup de protestants fuient ?", A8, [A7, A5, A6], pos=1)),
        "second": qcm(
            carnet("Après 1685", "(d'après la fiche). Le 18 octobre 1685, par l'édit de Fontainebleau, Louis XIV révoque l'édit de Nantes. Le culte protestant est interdit, les temples sont détruits, les pasteurs chassés. Entre 200 000 et 300 000 protestants fuient à l'étranger.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Combien de temps l'édit de Nantes a-t-il duré ?", ["87 ans", "17 ans", "187 ans", "7 ans"], 0, "1685 − 1598."),
             ("Pourquoi Louis XIV révoque-t-il l'édit ?", ["Il veut une seule religion dans le royaume", "Il veut devenir pape", "Il veut quitter la France", "Il veut aider les protestants"], 0, "Une seule religion."),
             ("Que devient le culte protestant ?", ["Il est interdit", "Il est protégé", "Il devient la religion du roi", "Il est rendu obligatoire"], 0, "Les temples sont détruits.")],
            ["Soustrais 1598 de 1685.", "Il veut une seule religion.", "Les temples sont détruits."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", A7, [A8, A2, A9], pos=1)),
    }
    return d
