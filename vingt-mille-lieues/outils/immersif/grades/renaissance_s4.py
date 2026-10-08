"""Salle 4 « Le cabinet des plans » (fiche : chateaux-renaissance)."""
from aide import *

F = "« Les châteaux de la Renaissance »"
H1 = "Les châteaux de la Renaissance gardent parfois des tours et un donjon, mais ils ne sont plus faits pour soutenir un siège."
H2 = "Ils montrent la richesse et le goût du roi : symétrie héritée de l'Antiquité, grandes fenêtres, lucarnes sculptées, escaliers monumentaux, jardins."
H3 = "Commencé en 1519 et achevé des dizaines d'années plus tard, Chambord compte plus de 400 pièces, environ 80 escaliers et 300 cheminées."
H4 = "Au centre du donjon, l'escalier à double révolution : deux escaliers tournent l'un au-dessus de l'autre, sans jamais se croiser."
H5 = "On pense qu'il s'inspire des idées de Léonard de Vinci, mais rien ne le prouve."
H6 = "À Blois, François Ier fait bâtir une aile nouvelle, avec un grand escalier à vis sculpté."
H7 = "La salamandre, emblème de François Ier, porte sa devise latine : « Nutrisco et extinguo », « Je m'en nourris et je l'éteins »."


def donnees(svg, bloc=None):
    d = {}
    d["e4-1"] = {
        "mousse": assoc(
            "Colombe déplie le plan de Chambord, vu de dessus. Regarde le plan, puis relie chaque nom à ce qu'il désigne. Clique sur un nom, puis sur sa description.\n" + svg("e4-1", "matelot"),
            [("le donjon", "le grand carré au centre"), ("l'escalier à double révolution", "l'escalier tout au centre"), ("une tour d'angle", "une tour ronde à un coin")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Le donjon est au centre.", "Les tours rondes sont aux angles."]),
        "lieutenant": qcm(
            "Colombe déplie le plan de Chambord vu de dessus (repères 1 à 6). Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 1." + svg("e4-1", "timonier"),
            [("Quel repère montre l'escalier à double révolution ?", ["Le repère 2", "Le repère 4", "Le repère 6", "Le repère 5"], 0, "Il est tout au centre du donjon."),
             ("Quel repère montre une tour d'angle ?", ["Le repère 4", "Le repère 1", "Le repère 3", "Le repère 2"], 0, "Les tours rondes sont aux angles."),
             ("Pourquoi Chambord garde-t-il un donjon et des tours ?", ["Pour le prestige : ce n'est plus un château fait pour un siège", "Pour se défendre contre une armée", "Pour surveiller la Loire", "Pour imiter Amboise"], 0, "Il garde des tours, mais n'est plus fait pour un siège.")],
            ["L'escalier est au centre.", "Les tours d'angle sont rondes.", "Un château de la Renaissance montre la richesse du roi."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 1 ?", H4, [H1, H3, H5], pos=1)),
        "second": qcm(
            carnet("Chambord en chiffres", "(d'après la fiche). Commencé en 1519, Chambord compte plus de 400 pièces, environ 80 escaliers et 300 cheminées. Au centre du donjon, l'escalier à double révolution : deux escaliers tournent l'un au-dessus de l'autre, sans jamais se croiser. On pense qu'il s'inspire de Léonard de Vinci, mais rien ne le prouve.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("Combien de cheminées compte Chambord environ ?", ["300", "80", "400", "30"], 0, "Environ 300."),
             ("Combien d'années séparent le début de Chambord (1519) de la mort de Léonard (2 mai 1519) ?", ["Aucune : la même année", "10 ans", "1 an", "20 ans"], 0, "Le chantier commence l'année de sa mort."),
             ("Peut-on affirmer que Léonard a dessiné l'escalier ?", ["Non : rien ne le prouve", "Oui : c'est certain", "Oui : il l'a signé", "On ne parle jamais de lui"], 0, "Les historiens disent « probablement ».")],
            ["Relis les chiffres.", "Léonard meurt en 1519.", "Pour affirmer, il faut des preuves."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", H5, [H4, H3, H2], pos=2)),
    }
    d["e4-2"] = {
        "mousse": tri(
            "Range chaque élément : château fort du Moyen Âge, ou château de la Renaissance ? Clique sur une carte, puis sur une colonne.",
            [("fort", "Château fort"), ("renaissance", "Château de la Renaissance")],
            [("Des meurtrières pour tirer", "fort"), ("Un pont-levis et une herse", "fort"), ("De grandes fenêtres", "renaissance"), ("Des jardins pour se promener", "renaissance")],
            ["Ouvre la fiche " + F + ".", "Les grandes fenêtres laissent entrer la lumière.", "Les meurtrières servent à tirer."]),
        "lieutenant": tri(
            "Colombe compare les deux sortes de châteaux. Range chaque élément dans la bonne colonne, puis choisis la phrase de la fiche qui décrit les châteaux de la Renaissance.",
            [("fort", "Fait pour soutenir un siège"), ("prestige", "Fait pour montrer la richesse")],
            [("Des meurtrières", "fort"), ("Des douves et un pont-levis", "fort"), ("Des murs très épais", "fort"), ("Une façade symétrique", "prestige"), ("Des lucarnes sculptées", "prestige"), ("Des jardins", "prestige")],
            ["Un siège : se défendre.", "La richesse : décorer.", "La symétrie vient de l'Antiquité."],
            J("Quelle phrase de la fiche décrit les châteaux de la Renaissance ?", H2, [H1, H3, H6], pos=0)),
        "second": tri(
            "Colombe classe des éléments de Chambord et de Blois. Range chaque carte dans la bonne colonne, puis choisis la phrase de la fiche qui décrit l'escalier de Blois.",
            [("chambord", "Chambord"), ("blois", "Blois")],
            [("Un donjon avec un escalier à double révolution", "chambord"), ("Plus de 400 pièces", "chambord"), ("Commencé en 1519", "chambord"), ("Une aile bâtie par François Ier", "blois"), ("Un grand escalier à vis sculpté", "blois"), ("Une façade ornée de l'emblème du roi", "blois")],
            ["Chambord : escalier à double révolution.", "Blois : escalier à vis.", "Chambord est commencé en 1519."],
            J("Quelle phrase de la fiche décrit l'escalier de Blois ?", H6, [H4, H3, H7], pos=1)),
    }
    d["e4-3"] = {
        "mousse": qcm(
            "Lis la question, clique sur la bonne réponse, puis vérifie.",
            [("Quel est l'emblème de François Ier ?", ["La salamandre", "Le lion", "L'aigle"], 0, "On la voit sculptée dans ses châteaux.")],
            ["Ouvre la fiche " + F + ".", "C'est un petit animal qui résiste au feu.", "On la sculpte à Chambord."]),
        "lieutenant": vf(
            "Colombe a noté cinq phrases sur la salamandre et Chambord. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui cite la devise du roi.",
            [("La salamandre est l'emblème de François Ier.", True, "Elle porte sa devise latine."), ("Sa devise est « Nutrisco et extinguo ».", True, "« Je m'en nourris et je l'éteins »."), ("Chambord compte moins de 100 pièces.", False, "Plus de 400."),
             ("L'escalier à double révolution de Chambord est certainement de Léonard.", False, "Rien ne le prouve."), ("Blois possède un grand escalier à vis sculpté.", True, "Dans l'aile de François Ier.")],
            ["La salamandre est son emblème.", "Plus de 400 pièces.", "Pour la justification : cherche la phrase en latin."],
            J("Quelle phrase de la fiche cite la devise du roi ?", H7, [H5, H6, H3], pos=2)),
        "second": vf(
            "Colombe a noté six phrases sur les châteaux de la Renaissance. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui explique ce que montre un château de la Renaissance.",
            [("Les châteaux de la Renaissance ne sont plus faits pour soutenir un siège.", True, "Ils montrent le goût du roi."), ("La symétrie est héritée de l'Antiquité.", True, "Comme les colonnes."), ("Chambord est commencé en 1519.", True, "Achevé des dizaines d'années plus tard."),
             ("Chambord est terminé du vivant de Léonard.", False, "Il meurt en 1519, année du début."), ("Les châteaux de la Renaissance n'ont jamais de tours.", False, "Ils en gardent parfois."), ("Le roi séjourne souvent à Chambord.", False, "Il y séjourne peu.")],
            ["Le château montre la richesse du roi.", "Chambord se construit pendant des dizaines d'années.", "Des tours peuvent rester."],
            J("Quelle phrase de la fiche explique ce que montre un château de la Renaissance ?", H2, [H1, H3, H5], pos=1)),
    }
    d["e4-4"] = {
        "lieutenant": assoc(
            "Colombe termine par des associations. Relie chaque lieu ou chaque emblème à sa description, puis choisis la phrase de la fiche qui explique l'escalier à double révolution.",
            [("Chambord", "commencé en 1519, plus de 400 pièces"), ("Blois", "une aile de François Ier avec un escalier à vis"), ("La salamandre", "l'emblème de François Ier"), ("L'escalier à double révolution", "deux escaliers qui tournent sans se croiser")],
            ["Chambord : 1519.", "Blois : escalier à vis.", "La salamandre : emblème du roi."],
            J("Quelle phrase de la fiche explique l'escalier à double révolution ?", H4, [H5, H3, H7], pos=1)),
        "second": ordre(
            "Colombe retrace la chronologie. Remets ces cinq repères dans l'ordre, puis choisis la phrase de la fiche qui date le début de Chambord.",
            [("Charles VIII ramène des artistes d'Italie", "1496"), ("François Ier devient roi", "1515"), ("Léonard de Vinci s'installe à Amboise", "1516"), ("Début du chantier de Chambord", "1519"), ("Création des lecteurs royaux", "1530")],
            ["Compare les dates.", "1519 vient après 1516.", "1530 est la date la plus récente."],
            J("Quelle phrase de la fiche date le début de Chambord ?", H3, [H6, H4, H5], pos=0)),
    }
    return d
