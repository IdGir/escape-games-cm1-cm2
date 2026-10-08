"""Salle 2 « La salle des Textes » : les textes de la Constitution."""
from aide import *
from constitution_docs import *


def donnees(svg, bloc=None):
    d = {}
    d["e2-1"] = {
        "mousse": ordre(
            "Remets les textes dans l'ordre, du plus ancien (en haut) au plus récent (en bas) avec les flèches ▲▼, puis vérifie.",
            [("La Déclaration des droits de l'homme et du citoyen", "1789"), ("Le Préambule de la Constitution de 1946", "1946"), ("La Constitution de la Ve République", "1958")],
            ["Ouvre la fiche « Les textes de notre Constitution » dans la Bibliothèque.", "Le plus ancien date de la Révolution.", "1958 est le plus récent des trois."]),
        "lieutenant": ordre(
            "Maître Sylla range cinq dates de l'histoire des textes. Remets-les dans l'ordre chronologique, du plus ancien au plus récent.",
            [("Déclaration des droits de l'homme et du citoyen", "26 août 1789"), ("Préambule de la Constitution de 1946", "27 octobre 1946"), ("Constitution de la Ve République", "4 octobre 1958"), ("Référendum sur le quinquennat", "2000"), ("Charte de l'environnement", "2004")],
            ["Compare les années.", "Le Préambule est écrit après la guerre.", "La Charte de l'environnement est la plus récente."]),
        "second": tri(
            "Maître Sylla classe les textes. Range chaque élément dans la bonne colonne : texte de 1789, de 1946, de 1958 ou de 2004.",
            [("t1789", "1789"), ("t1946", "1946"), ("t1958", "1958"), ("t2004", "2004")],
            [("Les hommes naissent libres et égaux en droits", "t1789"), ("L'égalité entre les femmes et les hommes", "t1946"), ("L'organisation des pouvoirs publics", "t1958"), ("Le droit de vivre dans un environnement équilibré", "t2004")],
            ["Chaque texte a son apport.", "Les droits civils sont de 1789.", "L'environnement est le plus récent."]),
    }
    d["e2-2"] = {
        "mousse": assoc(
            "Clique sur un texte dans la colonne de gauche, puis sur ce qu'il apporte, dans la colonne de droite.",
            [("La Déclaration de 1789", "l'égalité devant la loi"), ("Le Préambule de 1946", "le droit à l'instruction"), ("La Charte de l'environnement", "le droit à un environnement équilibré")],
            ["Ouvre la fiche « Les textes de notre Constitution ».", "1946 : l'école pour tous.", "La Charte parle de la nature."]),
        "lieutenant": qcm(
            preambule(P46_1, P46_2, P46_3, P46_4) + " Réponds aux trois questions, puis choisis la phrase du document qui parle de l'enseignement public.",
            [("Que garantit la loi à la femme, selon le Préambule ?", ["Des droits égaux à ceux de l'homme", "Aucun droit", "Moins de droits", "Seulement le droit de vote"], 0, "Dans tous les domaines."),
             ("Quel devoir de l'État concerne l'école publique ?", ["Organiser un enseignement public gratuit et laïque", "Faire payer l'école", "Choisir la religion des élèves", "Supprimer l'école"], 0, "À tous les degrés."),
             ("Qui a droit d'asile sur les territoires de la République ?", ["Tout homme persécuté en raison de son action en faveur de la liberté", "Tous les voyageurs", "Seulement les citoyens français", "Personne"], 0, "Droit d'asile.")],
            ["Relis la première phrase du Préambule.", "Un enseignement gratuit et laïque.", "Le droit d'asile protège les personnes persécutées."],
            J("Quelle phrase du document parle de l'enseignement public ?", P46_3, [P46_1, P46_4], pos=1)),
        "second": qcm(
            c58(C1, C1b, C3, C6) + " Maître Sylla pose trois questions. Réponds, puis choisis la phrase du document qui dit comment est élu le Président.",
            [("Selon l'article 3, à qui appartient la souveraineté nationale ?", ["Au peuple", "Au Président", "Au Gouvernement", "Au Conseil constitutionnel"], 0, "Au peuple, par ses représentants et par référendum."),
             ("Pour combien de temps le Président est-il élu ?", ["Cinq ans", "Sept ans", "Dix ans", "Trois ans"], 0, "Article 6."),
             ("Selon l'article 1, la République est…", ["indivisible, laïque, démocratique et sociale", "royale et héréditaire", "fédérale et religieuse", "militaire"], 0, "Quatre adjectifs.")],
            ["Le peuple exerce la souveraineté.", "Cinq ans : le quinquennat.", "Article 1 : quatre adjectifs."],
            J("Quelle phrase du document dit comment est élu le Président ?", C6, [C3, C1b, C1], pos=2)),
    }
    d["e2-3"] = {
        "mousse": trous(
            "Clique sur une étiquette, puis sur le trou où elle doit aller. Une étiquette est en trop.",
            "En 1958, la France change de Constitution. Le texte est adopté par les Français lors d'un [[référendum]]. Il commence par une introduction appelée le [[préambule]]. C'est la Constitution de la [[Ve République]].",
            ["référendum", "préambule", "Ve République", "élection"],
            ["Ouvre la fiche « Le texte de la Constitution de la Ve République ».", "Les Français ont voté directement.", "Le texte d'introduction d'une Constitution est un préambule."]),
        "lieutenant": vf(
            c58(C1, C2, C3, C20) + " Maître Sylla affirme cinq choses. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase du document qui cite la devise.",
            [("La devise de la République est « Liberté, Égalité, Fraternité ».", True, "Article 2."), ("La France est une République indivisible, laïque, démocratique et sociale.", True, "Article 1."), ("La souveraineté nationale appartient au peuple.", True, "Article 3."),
             ("Le Gouvernement détermine la politique de la Nation.", True, "Article 20."), ("La devise de la République est « Liberté, Égalité, Autorité ».", False, "Fraternité.")],
            ["La devise a trois mots.", "Le dernier est « Fraternité ».", "Article 2."],
            J("Quelle phrase du document cite la devise ?", C2, [C1, C20, C3], pos=1)),
        "second": ordre(
            "Maître Sylla retrace l'adoption de la Constitution. Remets ces cinq étapes dans l'ordre, puis choisis la phrase du document qui dit qui détermine la politique de la Nation. " + c58(C20, C5, C1),
            ["Dans les années 1950, les gouvernements se succèdent trop vite.", "Le général de Gaulle, chef du Gouvernement, lance la rédaction d'une nouvelle Constitution.", "Le texte est adopté par référendum (septembre 1958).", "La Constitution est promulguée le 4 octobre 1958.", "Le Gouvernement détermine et conduit la politique de la Nation."],
            ["Avant la rédaction, il y a l'instabilité.", "On promulgue après le référendum.", "Le fonctionnement vient après la promulgation."],
            J("Quelle phrase du document dit qui détermine la politique de la Nation ?", C20, [C5, C1], pos=0)),
    }
    d["e2-4"] = {
        "lieutenant": code(
            "Le cadenas à chiffres demande deux années. Quelle est l'année de la Constitution actuelle ? Quelle est l'année du Préambule de la IVe République (27 octobre) ? Puis choisis la phrase du document qui date le Préambule."
            + carnet("Frise", "26 août 1789 : Déclaration des droits de l'homme et du citoyen. 27 octobre 1946 : Préambule de la Constitution de la IVe République. 4 octobre 1958 : Constitution de la Ve République."),
            [("Année de la Constitution actuelle", "1958", 4), ("Année du Préambule de la IVe République", "1946", 4)],
            ["La Constitution actuelle est de 1958.", "Le Préambule est de 1946.", "Lis la frise."],
            J("Quelle phrase du document date le Préambule ?", "27 octobre 1946 : Préambule de la Constitution de la IVe République.", ["26 août 1789 : Déclaration des droits de l'homme et du citoyen.", "4 octobre 1958 : Constitution de la Ve République."], pos=1)),
        "second": code(
            "Le cadenas à chiffres demande trois nombres. Combien d'années séparent la Déclaration (1789) de la Constitution actuelle (1958) ? Combien d'années séparent le Préambule (1946) de la Constitution actuelle ? Combien d'années séparent la Constitution actuelle (1958) de la Charte de l'environnement (2004) ?"
            + carnet("Frise", "1789 : Déclaration. 1946 : Préambule. 1958 : Constitution de la Ve République. 2004 : Charte de l'environnement."),
            [("Années entre 1789 et 1958", "169", 3), ("Années entre 1946 et 1958", "12", 2), ("Années entre 1958 et 2004", "46", 2)],
            ["1958 − 1789.", "1958 − 1946.", "2004 − 1958."],
            J("Quelle phrase du document donne la date de la Charte ?", "2004 : Charte de l'environnement.", ["1789 : Déclaration.", "1946 : Préambule."], pos=2)),
    }
    return d
