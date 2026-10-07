"""Salle 2 « La rue des deux voisins » (fiche : edit-de-nantes)."""
from aide import *

F = "« L'édit de Nantes (1598) »"
E1 = "En avril 1598, à Nantes, Henri IV signe l'édit de Nantes. C'est un compromis : chacun doit céder un peu pour que la paix revienne."
E2 = "La liberté de conscience : on ne peut forcer personne à changer de religion."
E3 = "Une liberté de culte limitée : seulement dans des lieux fixés par l'édit ; jamais à Paris, autour de Paris, ni à la cour."
E4 = "L'égalité civile : ils peuvent exercer tous les métiers et toutes les charges (juge, officier du roi…)."
E5 = "Des places de sûreté (des villes fortifiées) pour leur protection."
E6 = "La messe est rétablie dans tout le royaume, les églises sont rendues, et tous paient la dîme à l'Église catholique."
E7 = "L'édit ne crée pas l'égalité entre les religions : le catholicisme reste la religion du roi et de la majorité. C'est une tolérance, un pacte pour vivre ensemble. Il durera jusqu'en 1685."


def donnees(svg, bloc=None):
    d = {}
    d["e2-1"] = {
        "mousse": vf(
            "Mathurin lit l'édit de Nantes (extraits simplifiés) : « Personne ne doit être forcé à changer de religion. Les protestants peuvent célébrer leur culte dans certains lieux. Leur culte reste interdit à Paris. » Pour chaque phrase, clique sur « Vrai » ou sur « Faux », puis vérifie.",
            [("Personne ne doit être forcé à changer de religion.", True, "C'est la liberté de conscience."), ("Les protestants peuvent célébrer leur culte partout, même à Paris.", False, "Il reste interdit à Paris."), ("Les protestants peuvent célébrer leur culte dans certains lieux.", True, "Fixés par l'édit.")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Relis la troisième ligne du document.", "Cherche le mot « Paris »."]),
        "lieutenant": qcm(
            carnet("L'édit de Nantes, avril 1598", "(extraits simplifiés). Les protestants peuvent vivre dans tout le royaume sans être forcés à changer de religion. Ils peuvent célébrer leur culte dans certains lieux fixés par l'édit. Leur culte reste interdit à Paris, autour de Paris et à la cour. Ils peuvent exercer tous les métiers et toutes les charges.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Un protestant peut-il être juge ?", ["Oui : toutes les charges sont ouvertes", "Non : seuls les catholiques peuvent l'être", "Seulement à Paris", "Seulement à la cour"], 0, "Égalité civile."),
             ("Où le culte protestant est-il interdit ?", ["À Paris, autour de Paris et à la cour", "Partout", "Dans les villes de province", "Nulle part"], 0, "Lieux limités."),
             ("L'édit rend-il les deux religions égales ?", ["Non : le catholicisme reste la religion du roi", "Oui : elles sont égales", "Non : le protestantisme devient religion du roi", "On ne sait pas"], 0, "C'est une tolérance, pas l'égalité.")],
            ["Toutes les charges sont ouvertes.", "Relis l'interdiction.", "Le roi est catholique."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", E3, [E4, E2, E5], pos=1)),
        "second": vf(
            "Mathurin a noté six phrases sur l'édit. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui définit la liberté de conscience.",
            [("L'édit est un compromis : chacun doit céder un peu.", True, "Pour que la paix revienne."), ("L'édit crée l'égalité entre les religions.", False, "Le catholicisme reste la religion du roi."), ("La messe est rétablie dans tout le royaume.", True, "Les églises sont rendues."),
             ("Les protestants reçoivent des places de sûreté.", True, "Des villes fortifiées."), ("L'édit dure jusqu'en 1789.", False, "Jusqu'en 1685."), ("Les protestants sont dispensés de la dîme.", False, "Tous paient la dîme à l'Église catholique.")],
            ["Un compromis : chacun cède un peu.", "L'édit dure jusqu'en 1685.", "Tous paient la dîme."],
            J("Quelle phrase de la fiche définit la liberté de conscience ?", E2, [E1, E3, E7], pos=1)),
    }
    d["e2-2"] = {
        "mousse": tri(
            "Range chaque carte : ce que l'édit permet aux protestants, ou ce qui leur reste interdit. Clique sur une carte, puis sur une colonne.",
            [("oui", "Permis aux protestants"), ("non", "Interdit aux protestants")],
            [("Croire ce qu'ils veulent sans être punis", "oui"), ("Exercer tous les métiers", "oui"), ("Célébrer leur culte à Paris", "non"), ("Célébrer leur culte à la cour du roi", "non")],
            ["Ouvre la fiche " + F + ".", "La liberté de croire est permise partout.", "Paris et la cour : interdit."]),
        "lieutenant": tri(
            "Mathurin range les clauses de l'édit. Range chaque clause dans la bonne colonne, puis choisis la phrase de la fiche qui énumère ce que gagnent les catholiques.",
            [("prot", "Pour les protestants"), ("cath", "Pour les catholiques")],
            [("La liberté de conscience", "prot"), ("Des places de sûreté", "prot"), ("Toutes les charges et tous les métiers", "prot"), ("La messe rétablie dans tout le royaume", "cath"), ("Les églises rendues", "cath"), ("La dîme payée à l'Église catholique", "cath")],
            ["Les protestants : conscience, places de sûreté, charges.", "Les catholiques : messe, églises, dîme.", "Chacun cède un peu."],
            J("Quelle phrase de la fiche énumère ce que gagnent les catholiques ?", E6, [E4, E5, E3], pos=2)),
        "second": ordre(
            "Mathurin explique l'édit à Suzanne. Remets ces cinq étapes de sa démarche dans l'ordre, puis choisis la phrase de la fiche qui justifie le recours à un compromis.",
            ["Les guerres de Religion déchirent le royaume (1562-1598).", "Henri IV se convertit au catholicisme (1593).", "Henri IV signe l'édit de Nantes (1598).", "Les protestants obtiennent la liberté de conscience et un culte limité.", "Les catholiques voient la messe rétablie partout."],
            ["Les guerres avant l'édit.", "La conversion avant la signature.", "Chacun obtient quelque chose."],
            J("Quelle phrase de la fiche justifie le recours à un compromis ?", E1, [E7, E2, E6], pos=0)),
    }
    d["e2-3"] = {
        "mousse": trous(
            "Mathurin écrit à son cousin. Clique sur une étiquette, puis sur le trou où elle va. Une étiquette est en trop.",
            "Cher cousin, pendant plus de trente ans, catholiques et protestants se sont fait la [[guerre]]. En [[1598]], le roi Henri IV a signé l'édit de Nantes. Nous vivons côte à côte, en [[paix]].",
            ["guerre", "1598", "paix", "1789"],
            ["Ouvre la fiche " + F + ".", "L'année de l'édit est sur la frise.", "Le contraire de la guerre."]),
        "lieutenant": vf(
            "Mathurin a noté cinq phrases sur la vie après l'édit. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui parle des places de sûreté.",
            [("Les protestants ont des places de sûreté pour leur protection.", True, "Des villes fortifiées."), ("Les protestants peuvent exercer toutes les charges.", True, "Juge, officier du roi."), ("Le culte protestant est permis à Paris.", False, "Interdit."),
             ("La dîme est supprimée.", False, "Tous la paient à l'Église catholique."), ("L'édit crée l'égalité entre les religions.", False, "Le catholicisme reste la religion du roi.")],
            ["Des villes fortifiées pour les protéger.", "Le culte est limité.", "La dîme continue."],
            J("Quelle phrase de la fiche parle des places de sûreté ?", E5, [E3, E4, E6], pos=1)),
        "second": qcm(
            carnet("Lettre de Mathurin à son cousin", "(inventée pour le jeu). « Le roi a signé l'édit en avril 1598. Il durera jusqu'en 1685. Ce n'est pas l'égalité, mais un pacte pour vivre ensemble. »")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("Combien d'années l'édit dure-t-il ?", ["87 ans", "17 ans", "97 ans", "7 ans"], 0, "1685 − 1598 = 87."),
             ("Pourquoi Mathurin parle-t-il d'un pacte ?", ["Chacun doit céder un peu pour vivre en paix", "Le roi punit les protestants", "Les catholiques s'enfuient", "L'édit interdit la messe"], 0, "C'est un compromis."),
             ("L'édit crée-t-il l'égalité entre les religions ?", ["Non : le catholicisme reste la religion du roi", "Oui : elles sont égales", "Non : le protestantisme devient religion du roi", "On ne sait pas"], 0, "C'est une tolérance.")],
            ["Soustrais 1598 de 1685.", "Un pacte : chacun cède un peu.", "L'édit ne crée pas l'égalité."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", E7, [E1, E2, E6], pos=1)),
    }
    d["e2-4"] = {
        "lieutenant": code(
            "Le coffret de Mathurin est fermé par un cadenas. Écris l'année de l'édit, puis l'année jusqu'à laquelle il durera, puis ouvre.",
            [("Année de l'édit de Nantes", "1598", 4), ("Année de la fin de l'édit", "1685", 4)],
            ["L'édit est signé en avril 1598.", "Il durera jusqu'en 1685.", "Cherche les deux dates dans la fiche."],
            J("Quelle phrase de la fiche donne la durée de l'édit ?", E7, [E1, E3, E6], pos=1)),
        "second": code(
            "Le coffret de Mathurin est fermé par un cadenas à trois cases. Combien d'années dure l'édit de Nantes (de 1598 à 1685) ? Combien d'années séparent le début des guerres de Religion (1562) de l'édit ? Quel mot désigne le fait d'accepter, pour vivre en paix, une religion que l'on ne partage pas (9 lettres) ?",
            [("Années de l'édit", "87", 2), ("Années de guerre (1562 à 1598)", "36", 2), ("Mot : acceptation d'une autre religion", "TOLERANCE", 9, False)],
            ["1685 − 1598.", "1598 − 1562.", "Le mot est dans la fiche : « une … »."],
            J("Quelle phrase de la fiche donne le mot demandé ?", E7, [E1, E2, E3], pos=1)),
    }
    return d
