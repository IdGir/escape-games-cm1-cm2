"""Salle 3 « Le fonds des colonies » : grades mousse, lieutenant, second (fiche : la vie dans les plantations).
Aucune description de violence : on parle du travail forcé, de la loi et des résistances."""
from aide import *

FICHE = "« La vie dans les plantations »"
P_HAB = "Aux Antilles, la plantation s'appelle une habitation."
P_RECOLTE = "Pendant la récolte, de janvier à juin environ, les esclaves coupent la canne, enlèvent les feuilles et la mettent en paquets."
P_MOULIN = "Au moulin, la canne est broyée pour récolter le vesou, le jus de canne."
P_SUCRE = "Le vesou est transformé en sucre dans la sucrerie, puis le sucre passe par la purgerie."
P_18 = "Pendant la récolte, la journée de travail pouvait dépasser 18 heures."
P_EDIT = "Le Code noir est un édit du roi Louis XIV, signé en mars 1685."
P_CADRE = "Il donne un cadre légal à l'esclavage dans les colonies."
P_MEUBLE = "Il considère les esclaves comme des « biens meubles », privés de tout droit."
P_OBJET = "Il traite l'esclave comme un objet que l'on possède, et non comme une personne."
P_MARR = "Le marronnage est la fuite des esclaves hors de la plantation."
P_PETIT = "Le petit marronnage est une fuite de quelques jours."
P_GRAND = "Le grand marronnage est une fuite sans retour : les marrons forment des groupes qui vivent dans la forêt ou les montagnes."
P_MOT = "Le mot marron vient de l'espagnol cimarrón, qui veut dire « fuir »."
P_REVOLTE = "Les révoltes sont une autre forme de résistance."
P_SOCIETE = "Sur l'habitation, la grande majorité des esclaves travaillent dans les champs."
P_ECONOME = "Un économe organise le travail des ateliers."


def donnees(svg, bloc=None):
    d = {}
    d["e3-1"] = {
        "mousse": ordre(
            "Célia montre le plan de l'habitation. Remets dans l'ordre le chemin de la canne, du champ au sucre.",
            ["Couper la canne dans les champs.", "Broyer la canne au moulin.", "Transformer le jus en sucre dans la sucrerie."],
            ["Ouvre la fiche " + FICHE + " : regarde le plan.", "Tout commence dans les champs.", "Le sucre est fabriqué à la fin."]),
        "lieutenant": ordre(
            "Célia suit le plan de l'habitation. Remets dans l'ordre les étapes du travail forcé, puis choisis la phrase de la fiche qui décrit ce qui se passe après le moulin.",
            ["Couper la canne pendant la récolte.", "Enlever les feuilles et mettre la canne en paquets.", "Broyer la canne au moulin pour récolter le vesou.",
             "Transformer le vesou en sucre dans la sucrerie.", "Faire passer le sucre par la purgerie.", "Mettre le sucre en barriques pour les navires."],
            ["Le vesou sort du moulin.", "La purgerie vient après la sucrerie.", "Pour la justification : cherche « purgerie »."],
            J("Quelle phrase de la fiche décrit ce qui se passe après le moulin ?", P_SUCRE, [P_MOULIN, P_RECOLTE, P_HAB], pos=2)),
        "second": ordre(
            "Célia relie le calendrier de l'habitation au voyage des navires. Remets dans l'ordre, puis choisis la phrase de la fiche qui situe la récolte dans l'année.",
            ["De janvier à juin environ : la canne est coupée, dépaillée et mise en paquets.", "Au moulin, la canne est broyée : on récolte le vesou.",
             "Dans la sucrerie puis la purgerie, le vesou devient du sucre.", "Le sucre est chargé sur un navire au troisième trajet.",
             "En Europe, le sucre est vendu très cher."],
            ["Le travail des champs vient en premier.", "Le troisième trajet va des Amériques vers l'Europe.", "Pour la justification : cherche « janvier »."],
            J("Quelle phrase de la fiche situe la récolte dans l'année ?", P_RECOLTE, [P_18, P_SOCIETE, P_MOULIN], pos=1)),
    }
    d["e3-2"] = {
        "mousse": qcm(
            "Célia explique le Code noir avec des mots simples. Réponds aux trois questions.",
            [("Le Code noir est...", ["une loi", "un journal", "un bateau"], 0, "Une loi du roi."),
             ("Quel roi l'a signé ?", ["Louis XIV", "Napoléon", "François Ier"], 0, "Louis XIV, en 1685."),
             ("Pour cette loi, l'esclave est...", ["un ami", "un bien que l'on peut vendre", "un citoyen"], 1, "Il le traite comme une chose.")],
            ["Ouvre la fiche " + FICHE + ".", "C'est le roi de Versailles.", "Un « bien », c'est une chose que l'on possède."]),
        "lieutenant": qcm(
            "Célia vérifie que vous avez compris le Code noir. Réponds aux quatre questions, puis choisis la phrase de la fiche qui date ce texte.",
            [("En quelle année le Code noir a-t-il été signé ?", ["1492", "1685", "1789", "1848"], 1, "En mars 1685."),
             ("Un « édit », c'est...", ["une loi signée par le roi", "un journal de bord", "une révolte", "un port"], 0, "Le Code noir est un édit."),
             ("Le Code noir considère les esclaves comme...", ["des citoyens", "des soldats", "des « biens meubles »", "des marins"], 2, "Privés de tout droit."),
             ("Pendant la récolte, la journée de travail pouvait dépasser...", ["4 heures", "8 heures", "12 heures", "18 heures"], 3, "Plus de 18 heures.")],
            ["1685 : fin du XVIIe siècle.", "« Biens meubles » : des choses que l'on peut déplacer et vendre.", "Pour la justification : cherche « mars 1685 »."],
            J("Quelle phrase de la fiche date ce texte ?", P_EDIT, [P_CADRE, P_MEUBLE, P_18], pos=0)),
        "second": vf(
            "Célia fait lire le document de la fiche, « Le Code noir, expliqué simplement ». Pour chaque phrase, choisis vrai ou faux, puis la phrase du document qui montre que cette loi niait l'humanité des esclaves.",
            [("Le Code noir a été écrit par les esclaves eux-mêmes.", False, "C'est un édit du roi Louis XIV."),
             ("Le Code noir a rendu l'esclavage légal dans les colonies.", True, "Il lui donne un cadre légal."),
             ("Pour le Code noir, l'esclave a les mêmes droits qu'un sujet libre.", False, "Il est privé de tout droit."),
             ("Une loi peut être injuste : le Code noir en est un exemple.", True, "Il traite une personne comme un objet."),
             ("Le Code noir était encore appliqué après 1848.", False, "L'esclavage est aboli en 1848.")],
            ["Une loi est écrite par ceux qui gouvernent.", "Légal ne veut pas dire juste.", "Pour la justification : cherche « objet »."],
            J("Quelle phrase du document montre que cette loi niait l'humanité des esclaves ?", P_OBJET, [P_CADRE, P_EDIT, P_HAB], pos=2)),
    }
    d["e3-3"] = {
        "mousse": tri(
            "Les esclaves ont résisté. Range chaque carte : est-ce une forme de résistance ou une règle imposée par les maîtres ?",
            [("resiste", "Résistance"), ("impose", "Règle imposée")],
            [("s'enfuir", "resiste"), ("garder ses chants", "resiste"), ("travailler sans salaire", "impose"), ("être vendu", "impose")],
            ["Ouvre la fiche " + FICHE + ".", "Résister, c'est refuser ce qu'on vous impose.", "Un marron est un esclave qui s'est enfui."]),
        "lieutenant": tri(
            "Célia classe les formes de résistance. Range chaque carte, puis choisis la phrase de la fiche qui définit le grand marronnage.",
            [("petit", "Petit marronnage"), ("grand", "Grand marronnage"), ("revolte", "Révolte")],
            [("fuir quelques jours, puis revenir", "petit"), ("se cacher un moment près de l'habitation", "petit"), ("fuir sans retour dans la forêt", "grand"),
             ("vivre en groupe dans les montagnes", "grand"), ("se soulever à plusieurs contre les maîtres", "revolte"), ("l'insurrection de Saint-Domingue en 1791", "revolte")],
            ["Le petit marronnage dure quelques jours.", "Le grand marronnage est sans retour.", "Pour la justification : cherche « sans retour »."],
            J("Quelle phrase de la fiche définit le grand marronnage ?", P_GRAND, [P_PETIT, P_MARR, P_MOT], pos=3)),
        "second": tri(
            "Célia distingue ce qui organise le système de l'habitation et ce qui le combat. Range chaque carte, puis choisis la phrase de la fiche qui montre que la fuite menaçait le système.",
            [("systeme", "Organise le système esclavagiste"), ("combat", "Combat ou refuse le système")],
            [("le Code noir de 1685", "systeme"), ("l'économe qui organise les ateliers", "systeme"), ("des journées de plus de 18 heures", "systeme"),
             ("le grand marronnage", "combat"), ("les révoltes", "combat"), ("garder des chants et des contes venus d'Afrique", "combat")],
            ["Le Code noir est une loi qui rend l'esclavage légal.", "Les marrons forment des groupes libres, hors de l'habitation.", "Pour la justification : cherche « groupes »."],
            J("Quelle phrase de la fiche montre que la fuite créait des groupes libres, hors du système ?", P_GRAND, [P_ECONOME, P_SOCIETE, P_PETIT], pos=0)),
    }
    d["e3-4"] = {
        "lieutenant": assoc(
            "Célia prépare le lexique des archives. Relie chaque mot à sa définition, puis choisis la phrase de la fiche qui explique l'origine du mot « marron ».",
            [("un édit", "une loi signée par le roi"), ("une habitation", "le nom de la plantation aux Antilles"), ("le vesou", "le jus de la canne à sucre"),
             ("un marron", "un esclave qui s'est enfui"), ("un affranchi", "un esclave devenu libre")],
            ["« Habitation » n'est pas ici une simple maison.", "Affranchir, c'est rendre libre.", "Pour la justification : cherche « espagnol »."],
            J("Quelle phrase de la fiche explique l'origine du mot « marron » ?", P_MOT, [P_MARR, P_HAB, P_PETIT], pos=0)),
        "second": assoc(
            "Célia croise les informations de la fiche. Relie chaque élément à ce qu'il nous apprend, puis choisis la phrase de la fiche qui dit qui travaillait le plus.",
            [("le Code noir (1685)", "la loi rendait l'esclavage légal"), ("l'économe", "il organisait le travail des ateliers"),
             ("la récolte", "des journées de plus de 18 heures"), ("les champs", "là où travaillait la grande majorité des esclaves"),
             ("le grand marronnage", "des groupes libres dans la forêt ou les montagnes")],
            ["La récolte dure de janvier à juin environ.", "Les champs occupent la plupart des esclaves.", "Pour la justification : cherche « grande majorité »."],
            J("Quelle phrase de la fiche dit qui travaillait le plus ?", P_SOCIETE, [P_ECONOME, P_18, P_CADRE], pos=1)),
    }
    return d
