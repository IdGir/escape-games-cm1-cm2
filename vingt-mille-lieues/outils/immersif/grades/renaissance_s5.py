"""Salle 5 « La galerie des tableaux » (fiche : art-renaissance)."""
from aide import *

F = "« L'art de la Renaissance »"
A1 = "Les lignes qui s'enfoncent dans le tableau, les lignes de fuite, se rejoignent en un point de fuite placé sur la ligne d'horizon."
A2 = "Au premier plan, les objets sont grands ; à l'arrière-plan, ils sont petits. Ces règles de géométrie donnent l'illusion de la profondeur."
A3 = "Vers 1490, Léonard dessine l'Homme de Vitruve, d'après les écrits de Vitruve, un architecte romain : un corps humain inscrit dans un cercle et un carré."
A4 = "Les artistes mesurent, comparent, dessinent des modèles vivants : l'art devient aussi une science."
A5 = "La Joconde, portrait de la Florentine Lisa Gherardini, est peinte à l'huile sur bois."
A6 = "Léonard y utilise le sfumato, un léger flou qui adoucit les contours."
A7 = "Entrée dans les collections du roi, elle est aujourd'hui au musée du Louvre, où des millions de visiteurs viennent la voir chaque année."


def donnees(svg, bloc=None):
    d = {}
    d["e5-1"] = {
        "mousse": tri(
            "Bastien peint un tableau en perspective. Range chaque élément : est-il au premier plan (près de nous) ou à l'arrière-plan (loin) ? Clique sur une carte, puis sur une colonne.",
            [("premier", "Premier plan (tout près)"), ("arriere", "Arrière-plan (au loin)")],
            [("Un grand personnage en bas du tableau", "premier"), ("Un pavé du sol, tout près", "premier"), ("Un minuscule arbre sur la colline", "arriere"), ("Une petite maison au fond", "arriere")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Au premier plan, les objets sont grands.", "Plus c'est loin, plus c'est petit."]),
        "lieutenant": qcm(
            "Bastien a peint un tableau construit en perspective (repères 1 à 6). Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 1." + svg("e5-1", "timonier"),
            [("Que montre le repère 1, là où les lignes se rejoignent ?", ["Le point de fuite", "La ligne d'horizon", "Le premier plan", "L'arrière-plan"], 0, "Les lignes de fuite s'y rejoignent."),
             ("Que montre le repère 2, la ligne pointillée ?", ["La ligne d'horizon", "Le point de fuite", "Une ligne de fuite", "Le cadre"], 0, "Le point de fuite est placé sur elle."),
             ("Pourquoi le personnage au loin est-il dessiné plus petit ?", ["Parce que ce qui est loin paraît plus petit", "Parce que c'est un enfant", "Parce que le peintre manquait de place", "Parce qu'il est plus ancien"], 0, "C'est la perspective.")],
            ["Les lignes de fuite se rejoignent en un point.", "L'horizon est la ligne où il est placé.", "Ce qui est loin paraît plus petit."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 1 ?", A1, [A2, A3, A4], pos=2)),
        "second": vf(
            "Bastien a noté six phrases sur la perspective et les proportions. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui explique l'illusion de profondeur.",
            [("Les lignes de fuite se rejoignent en un point de fuite.", True, "Il est sur la ligne d'horizon."), ("Au premier plan, les objets sont petits.", False, "Ils sont grands."), ("Ces règles de géométrie donnent l'illusion de la profondeur.", True, "C'est la perspective."),
             ("Léonard dessine l'Homme de Vitruve vers 1490.", True, "Un corps dans un cercle et un carré."), ("Vitruve est un peintre italien de la Renaissance.", False, "Un architecte romain."), ("Les artistes de la Renaissance rejettent la science.", False, "L'art devient aussi une science.")],
            ["Premier plan : grand. Arrière-plan : petit.", "Vitruve vit dans l'Antiquité.", "Les artistes mesurent et comparent."],
            J("Quelle phrase de la fiche explique l'illusion de profondeur ?", A2, [A1, A4, A3], pos=0)),
    }
    d["e5-2"] = {
        "mousse": qcm(
            "Lis la question, clique sur la bonne réponse, puis vérifie.",
            [("Pourquoi les personnages au fond d'un tableau sont-ils plus petits ?", ["Pour montrer qu'ils sont loin : c'est la perspective", "Parce que ce sont des enfants", "Parce que le peintre manquait de place"], 0, "Cela donne l'illusion de la profondeur.")],
            ["Ouvre la fiche " + F + ".", "Ce qui est loin paraît plus petit.", "La perspective donne la profondeur."]),
        "lieutenant": vf(
            "Bastien a noté cinq phrases sur la Joconde. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui dit où se trouve la Joconde aujourd'hui.",
            [("La Joconde est un portrait de Lisa Gherardini.", True, "Une Florentine."), ("La Joconde est peinte à l'huile sur bois.", True, "Sur un panneau de bois."), ("Léonard y utilise le sfumato.", True, "Un léger flou."),
             ("La Joconde est aujourd'hui au château d'Amboise.", False, "Au musée du Louvre."), ("Le sfumato est une couleur très chère.", False, "C'est un léger flou.")],
            ["La Joconde est un portrait.", "Le sfumato adoucit les contours.", "Elle est à Paris."],
            J("Quelle phrase de la fiche dit où se trouve la Joconde aujourd'hui ?", A7, [A5, A6, A3], pos=1)),
        "second": qcm(
            carnet("Fiche du musée", "(d'après la fiche). La Joconde, portrait de la Florentine Lisa Gherardini, est peinte à l'huile sur bois. Léonard y utilise le sfumato, un léger flou qui adoucit les contours. Entrée dans les collections du roi, elle est aujourd'hui au musée du Louvre.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Qui est représentée ?", ["Lisa Gherardini, une Florentine", "François Ier", "Une reine de France", "Léonard lui-même"], 0, "C'est un portrait."),
             ("Quelle technique adoucit les contours ?", ["Le sfumato", "La perspective", "Le dépôt légal", "La symétrie"], 0, "Un léger flou."),
             ("Dans quelle collection la Joconde est-elle d'abord entrée ?", ["Celles du roi", "Celles du pape", "Celles de Florence", "Celles d'Amboise"], 0, "Puis au Louvre.")],
            ["Un portrait représente une personne.", "Un léger flou adoucit les contours.", "Entrée dans les collections du roi."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", A6, [A5, A7, A1], pos=1)),
    }
    d["e5-3"] = {
        "mousse": code(
            "La dernière page du carnet est fermée par un cadenas. Écris l'année où François Ier devient roi et le prénom de l'artiste invité (7 lettres), puis ouvre (les accents ne comptent pas).",
            [("Année où François Ier devient roi", "1515", 4), ("Prénom de l'artiste invité", "LEONARD", 7, False)],
            ["Ouvre la fiche " + F + ".", "L'année de Marignan.", "Le prénom commence par L."]),
        "lieutenant": tri(
            "Bastien classe des éléments d'art. Range chaque carte dans la bonne colonne, puis choisis la phrase de la fiche qui définit la perspective.",
            [("persp", "La perspective"), ("prop", "Les proportions")],
            [("Le point de fuite", "persp"), ("La ligne d'horizon", "persp"), ("Les lignes de fuite", "persp"), ("L'Homme de Vitruve", "prop"), ("Un corps dans un cercle et un carré", "prop"), ("Mesurer et comparer des modèles vivants", "prop")],
            ["Lignes, horizon, point de fuite : la perspective.", "L'Homme de Vitruve : les proportions.", "Mesurer et comparer : les proportions."],
            J("Quelle phrase de la fiche définit l'effet de la perspective ?", A2, [A3, A4, A6], pos=1)),
        "second": ordre(
            "Bastien décrit les étapes pour peindre une scène en perspective. Remets-les dans l'ordre, puis choisis la phrase de la fiche qui justifie la première étape.",
            ["Tracer la ligne d'horizon.", "Placer le point de fuite sur la ligne d'horizon.", "Tracer les lignes de fuite qui rejoignent le point de fuite.", "Dessiner les objets du premier plan, grands.", "Dessiner ceux de l'arrière-plan, petits."],
            ["L'horizon vient d'abord.", "Le point de fuite est sur l'horizon.", "Les objets proches sont grands."],
            J("Quelle phrase de la fiche justifie la première étape ?", A1, [A2, A3, A4], pos=2)),
    }
    d["e5-4"] = {
        "lieutenant": trous(
            "Bastien a rédigé sa leçon, mais il manque des mots. Clique sur une étiquette, puis sur le trou où elle va. Trois étiquettes sont en trop. Puis choisis la phrase de la fiche qui justifie le mot « Louvre ».",
            "Les lignes de [[fuite]] se rejoignent au point de fuite, sur la ligne d'[[horizon]]. Au premier plan, les objets sont [[grands]] ; à l'arrière-plan, ils sont petits. La Joconde est aujourd'hui au musée du [[Louvre]].",
            ["fuite", "horizon", "grands", "Louvre", "salamandre", "vitrail", "cadre"],
            ["Relis la fiche : les mots sont dans la partie « La perspective ».", "Au premier plan, tout est grand.", "La Joconde est à Paris."],
            J("Quelle phrase de la fiche justifie le mot « Louvre » ?", A7, [A5, A1, A3], pos=1)),
        "second": trous(
            "Bastien résume l'art de la Renaissance, mais il manque des mots. Clique sur une étiquette, puis sur le trou où elle va. Quatre étiquettes sont en trop. Puis choisis la phrase de la fiche qui justifie le mot « science ».",
            "Les artistes mesurent, comparent, dessinent des modèles vivants : l'art devient aussi une [[science]]. Vers 1490, Léonard dessine l'Homme de [[Vitruve]], un corps humain inscrit dans un [[cercle]] et un carré. Dans la Joconde, il utilise le [[sfumato]], un léger flou qui adoucit les contours.",
            ["science", "Vitruve", "cercle", "sfumato", "triangle", "salamandre", "château", "imprimerie", "dépôt"],
            ["Les mots viennent de trois paragraphes de la fiche.", "Vitruve est un architecte romain.", "Le sfumato est un léger flou."],
            J("Quelle phrase de la fiche justifie le mot « science » ?", A4, [A3, A6, A2], pos=0)),
    }
    return d
