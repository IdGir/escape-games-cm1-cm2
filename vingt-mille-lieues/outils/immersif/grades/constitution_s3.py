"""Salle 3 « L'hémicycle » : la vie démocratique."""
from aide import *
from constitution_docs import *


def donnees(svg, bloc=None):
    d = {}
    d["e3-1"] = {
        "mousse": {
            "type": "plan", "titre": "Complète le schéma de la République", "colonnes": 2,
            "cases": [{"libelle": "Chef de l'État, élu par tous les Français", "reponse": "Le président de la République"}, {"libelle": "Il dirige le Gouvernement", "reponse": "Le Premier ministre"}, {"libelle": "Les députés y siègent", "reponse": "L'Assemblée nationale"}],
            "etiquettes": ["Le président de la République", "Le Premier ministre", "L'Assemblée nationale", "Le juge"],
            "consigne": "Madame Ferrand te montre le schéma de la République. Clique sur une étiquette, puis sur la case où elle doit aller. Une étiquette est en trop.",
            "indices": ["Ouvre la fiche « Comment la Constitution organise la vie démocratique ».", "Le chef de l'État est élu par tous les Français.", "Les députés siègent à l'Assemblée nationale."]},
        "lieutenant": qcm(
            c58(C5, C6, C20, C24) + " Réponds aux trois questions, puis choisis la phrase du document qui dit comment est élu le Président.",
            [("Qui détermine et conduit la politique de la Nation ?", ["Le Gouvernement", "Le Président seul", "Le Sénat", "Les juges"], 0, "Article 20."), ("Qui vote la loi ?", ["Le Parlement", "Le Gouvernement", "Le Président", "Le Conseil constitutionnel"], 0, "Article 24."),
             ("Pour combien de temps le Président est-il élu ?", ["Cinq ans", "Sept ans", "Dix ans", "Un an"], 0, "Article 6.")],
            ["Le Gouvernement conduit la politique.", "Le Parlement vote la loi.", "Cinq ans : le quinquennat."],
            J("Quelle phrase du document dit comment est élu le Président ?", C6, [C5, C20, C24], pos=1)),
        "second": vf(
            c58(C3, C6, C20, C24, C64) + " Madame Ferrand affirme six choses. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase du document qui parle de l'indépendance des juges.",
            [("Le peuple exerce la souveraineté par ses représentants et par référendum.", True, "Article 3."), ("Le Président est élu par le Parlement.", False, "Au suffrage universel direct."), ("Le Parlement contrôle l'action du Gouvernement.", True, "Article 24."),
             ("Le Président est garant de l'indépendance de l'autorité judiciaire.", True, "Article 64."), ("Le Gouvernement vote la loi à la place du Parlement.", False, "Le Parlement vote la loi."), ("Le mandat du Président dure cinq ans.", True, "Article 6.")],
            ["Le Président est élu au suffrage universel direct.", "Le Parlement vote la loi.", "Article 64 : les juges."],
            J("Quelle phrase du document parle de l'indépendance des juges ?", C64, [C20, C24, C3], pos=2)),
    }
    d["e3-2"] = {
        "mousse": qcm(
            "Réponds à la question, puis vérifie.",
            [("Comment le président de la République est-il élu ?", ["Par tous les citoyens, qui votent directement", "Par les députés seulement", "Par les juges"], 0, "C'est le suffrage universel direct.")],
            ["Ouvre la fiche « Le président de la République ».", "Tous les citoyens votent.", "Le mandat dure cinq ans."]),
        "lieutenant": tri(
            c58(C20, C24, C64) + " Maître Sylla range des pouvoirs. Range chaque pouvoir dans la bonne colonne, puis choisis la phrase du document qui parle du Gouvernement.",
            [("gouv", "Le Gouvernement"), ("parl", "Le Parlement"), ("just", "L'autorité judiciaire")],
            [("Déterminer la politique de la Nation", "gouv"), ("Conduire la politique de la Nation", "gouv"), ("Voter la loi", "parl"), ("Contrôler l'action du Gouvernement", "parl"), ("Rendre la justice", "just"), ("Être indépendante", "just")],
            ["Le Gouvernement détermine et conduit.", "Le Parlement vote et contrôle.", "Les juges sont indépendants."],
            J("Quelle phrase du document parle du Gouvernement ?", C20, [C24, C64], pos=1)),
        "second": qcm(
            c58(C3, C6, C24) + " Réponds aux trois questions, puis choisis la phrase du document qui dit ce que fait le Parlement.",
            [("Selon l'article 3, la souveraineté appartient…", ["au peuple", "au Président", "au Sénat", "au Gouvernement"], 0, "Au peuple."), ("Comment le Président est-il élu ?", ["Au suffrage universel direct", "Au suffrage indirect", "Par tirage au sort", "Par le Sénat"], 0, "Article 6."),
             ("Que fait le Parlement ?", ["Il vote la loi et contrôle le Gouvernement", "Il juge les procès", "Il élit le Président", "Il nomme les ministres"], 0, "Article 24.")],
            ["Souveraineté : le peuple.", "Suffrage universel direct.", "Voter et contrôler."],
            J("Quelle phrase du document dit ce que fait le Parlement ?", C24, [C3, C6], pos=1)),
    }
    d["e3-3"] = {
        "mousse": intrus(
            "Toutes ces élections se font au suffrage universel direct, sauf une. Clique sur l'intrus, puis vérifie.",
            [("Le président de la République", False), ("Les députés", False), ("Les conseillers municipaux", False), ("Les sénateurs", True)],
            ["Ouvre la fiche « Comment la Constitution organise la vie démocratique ».", "Pour trois élections, les citoyens votent eux-mêmes.", "Les sénateurs sont élus par de grands électeurs."]),
        "lieutenant": vf(
            c58(C3, C6, C24) + " Madame Ferrand affirme cinq choses sur les élections. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase du document qui parle des représentants du peuple.",
            [("Le peuple exerce la souveraineté par ses représentants.", True, "Et par référendum."), ("Le Président est élu au suffrage universel direct.", True, "Pour cinq ans."), ("Les sénateurs sont élus au suffrage universel direct.", False, "Par de grands électeurs."),
             ("Le Parlement contrôle l'action du Gouvernement.", True, "Article 24."), ("Le référendum n'existe pas en France.", False, "Il existe : article 3.")],
            ["Le peuple vote ses représentants.", "Les sénateurs sont élus par de grands électeurs.", "Le référendum est dans l'article 3."],
            J("Quelle phrase du document parle des représentants du peuple ?", C3, [C6, C24], pos=2)),
        "second": tri(
            c58(C3, C6, C24) + " Madame Ferrand classe des élections. Range chaque élection dans la bonne colonne : suffrage direct ou indirect. Puis choisis la phrase du document qui parle du suffrage universel direct.",
            [("direct", "Suffrage universel direct"), ("indirect", "Suffrage indirect")],
            [("Le président de la République", "direct"), ("Les députés", "direct"), ("Les conseillers municipaux", "direct"), ("Les représentants au Parlement européen", "direct"), ("Les sénateurs", "indirect"), ("Les grands électeurs votent pour eux", "indirect")],
            ["Le citoyen glisse lui-même son bulletin : direct.", "Les sénateurs sont élus par de grands électeurs.", "Article 6 : suffrage universel direct."],
            J("Quelle phrase du document parle du suffrage universel direct ?", C6, [C3, C24], pos=0)),
    }
    d["e3-4"] = {
        "lieutenant": ordre(
            "Madame Ferrand retrace l'histoire des textes et du mandat. Remets ces cinq repères dans l'ordre chronologique.",
            [("Déclaration des droits de l'homme et du citoyen", "1789"), ("Préambule de la IVe République", "1946"), ("Constitution de la Ve République", "1958"), ("Le septennat devient un quinquennat par référendum", "2000"), ("Charte de l'environnement", "2004")],
            ["Compare les années.", "Le quinquennat est de 2000.", "La Charte est la plus récente."]),
        "second": code(
            c58(C6, C6b, C5) + " Madame Ferrand te demande trois nombres. Combien d'années dure le mandat du Président ? Combien de mandats consécutifs maximum le Président peut-il exercer ? Combien d'années séparent 2000 (quinquennat) de la Constitution de 1958 ?",
            [("Durée du mandat (ans)", "5", 1), ("Nombre de mandats consécutifs maximum", "2", 1), ("Années entre 1958 et 2000", "42", 2)],
            ["Article 6 : cinq ans.", "Le mandat est renouvelable une fois : deux mandats.", "2000 − 1958."],
            J("Quelle phrase du document donne la durée du mandat ?", C6, [C5, C6b], pos=0)),
    }
    return d
