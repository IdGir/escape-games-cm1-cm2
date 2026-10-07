"""Salle 5 « La salle des séances du Conseil constitutionnel » : valeurs, principes et gardien de la Constitution."""
from aide import *
from constitution_docs import *


def donnees(svg, bloc=None):
    d = {}
    d["e5-1"] = {
        "mousse": trous(
            "Complète les articles 1 et 2 de la Constitution. Clique sur une étiquette, puis sur le trou où elle va. Une étiquette est en trop.",
            "<b>Article 1er.</b> La France est une République [[indivisible]], [[laïque]], démocratique et sociale. <b>Article 2.</b> La devise de la République est « Liberté, [[Égalité]], Fraternité ».",
            ["indivisible", "laïque", "Égalité", "royale"],
            ["Ouvre la fiche « Les valeurs et principes de la République française ».", "Indivisible : on ne peut pas la couper en morceaux.", "Laïque : l'État ne préfère aucune religion."]),
        "lieutenant": qcm(
            c58(C1, C1b, C2) + " Réponds aux trois questions, puis choisis la phrase du document qui cite la devise.",
            [("Combien d'adjectifs qualifient la République ?", ["Quatre", "Deux", "Trois", "Cinq"], 0, "Indivisible, laïque, démocratique, sociale."), ("Que garantit la République devant la loi ?", ["L'égalité de tous les citoyens, sans distinction d'origine, de race ou de religion", "Les mêmes revenus pour tous", "Un seul métier pour tous", "L'interdiction de voter"], 0, "Article 1."),
             ("Quelle est la devise de la République ?", ["Liberté, Égalité, Fraternité", "Dieu et mon droit", "Travail, Famille, Patrie", "Un pour tous"], 0, "Article 2.")],
            ["Compte les adjectifs de l'article 1.", "Égalité devant la loi.", "La devise est à l'article 2."],
            J("Quelle phrase du document cite la devise ?", C2, [C1, C1b], pos=2)),
        "second": vf(
            c58(C1, C1b, C2, C3) + " Maître Sylla affirme six choses. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase du document qui dit que la République est laïque.",
            [("La France est une République indivisible, laïque, démocratique et sociale.", True, "Article 1."), ("La République assure l'égalité devant la loi sans distinction de religion.", True, "Article 1."), ("La devise de la République est « Liberté, Égalité, Fraternité ».", True, "Article 2."),
             ("La souveraineté nationale appartient au Président.", False, "Au peuple."), ("La République favorise une religion.", False, "Elle est laïque."), ("La République est une monarchie.", False, "Démocratique.")],
            ["Laïque : l'État est neutre.", "La souveraineté appartient au peuple.", "Article 1 : quatre adjectifs."],
            J("Quelle phrase du document dit que la République est laïque ?", C1, [C2, C3, C1b], pos=0)),
    }
    d["e5-2"] = {
        "mousse": tri(
            "Range chaque principe dans la bonne colonne : clique sur une carte, puis sur une colonne.",
            [("lib", "Liberté"), ("egal", "Égalité")],
            [("Parler et écrire librement", "lib"), ("Croire ou ne pas croire", "lib"), ("La loi est la même pour tous", "egal"), ("Les femmes et les hommes ont les mêmes droits", "egal")],
            ["Ouvre la fiche « Les valeurs et principes de la République française ».", "La liberté, c'est pouvoir faire ce qui ne nuit pas aux autres.", "L'égalité : les mêmes droits pour tous."]),
        "lieutenant": tri(
            ddhc(DDHC1, DDHC4, DDHC11) + " " + preambule(P46_1, P46_3) + " Maître Sylla range des droits. Range chaque droit dans la bonne colonne, puis choisis la phrase du document qui définit la liberté.",
            [("lib", "Liberté"), ("egal", "Égalité"), ("droit", "Droits sociaux")],
            [("Parler, écrire, imprimer librement", "lib"), ("Faire tout ce qui ne nuit pas à autrui", "lib"), ("Naître libres et égaux en droits", "egal"), ("Droits égaux des femmes et des hommes", "egal"), ("L'enseignement public gratuit et laïque", "droit"), ("L'égal accès à l'instruction", "droit")],
            ["La liberté s'arrête où commence celle des autres.", "L'égalité : les mêmes droits.", "L'école gratuite est un droit social."],
            J("Quelle phrase du document définit la liberté ?", DDHC4, [DDHC1, DDHC11, P46_3], pos=1)),
        "second": tri(
            preambule(P46_1, P46_2, P46_3, P46_5, P46_6) + " Maître Sylla classe les droits du Préambule de 1946. Range chaque droit dans la bonne colonne, puis choisis la phrase du document qui garantit la protection de la santé.",
            [("egalite", "Égalité et instruction"), ("travail", "Travail"), ("sante", "Santé et protection")],
            [("Des droits égaux pour la femme et pour l'homme", "egalite"), ("L'égal accès à l'instruction et à la culture", "egalite"), ("Un enseignement public gratuit et laïque", "egalite"), ("Le devoir de travailler et le droit d'obtenir un emploi", "travail"), ("La protection de la santé", "sante"), ("Le repos et les loisirs", "sante")],
            ["L'égalité et l'instruction : les trois premières phrases.", "Le travail : emploi.", "Santé, repos, loisirs : protection."],
            J("Quelle phrase du document garantit la protection de la santé ?", P46_5, [P46_6, P46_2, P46_1], pos=2)),
    }
    d["e5-3"] = {
        "mousse": qcm(
            "Tu vas à l'école publique sans rien payer. Quel devoir de l'État cela illustre-t-il ?",
            [("L'école publique gratuite et laïque est…", ["un devoir de l'État", "un choix des communes", "une tradition sans valeur"], 0, "Le Préambule de 1946 l'affirme.")],
            ["Ouvre la fiche « La Constitution au quotidien ».", "L'école est gratuite pour tous.", "C'est écrit dans le Préambule."]),
        "lieutenant": vf(
            preambule(P46_2, P46_3, P46_5, P46_6) + " " + charte(ENV1, ENV2) + " Nour a noté cinq situations. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase du document qui parle de l'environnement.",
            [("L'école publique est un devoir de l'État.", True, "Gratuite et laïque."), ("La Nation garantit la protection de la santé.", True, "Notamment à l'enfant."), ("Chacun a le droit d'obtenir un emploi.", True, "Et le devoir de travailler."),
             ("La protection de l'environnement n'intéresse pas la Constitution.", False, "Charte de 2004."), ("Seul l'État doit préserver l'environnement.", False, "Toute personne a ce devoir.")],
            ["L'école est un devoir de l'État.", "La santé est protégée.", "La Charte parle de l'environnement."],
            J("Quelle phrase du document parle du droit à un environnement équilibré ?", ENV1, [ENV2, P46_5, P46_3], pos=1)),
        "second": qcm(
            preambule(P46_3, P46_5, P46_6) + " " + charte(ENV1, ENV2) + " Réponds aux trois questions de la vie quotidienne, puis choisis la phrase du document qui justifie la question 3.",
            [("Pourquoi les vaccins obligatoires sont-ils conformes à la Constitution ?", ["Parce que la Nation garantit à tous la protection de la santé", "Parce que les médecins le demandent", "Parce que c'est écrit dans le règlement de l'école", "Parce qu'ils sont gratuits"], 0, "Préambule de 1946."), ("Ta classe plante des arbres. Quel texte est concerné ?", ["La Charte de l'environnement", "La Déclaration de 1789", "Le Préambule de 1946", "Aucun texte"], 0, "Charte de 2004."),
             ("Une personne a-t-elle le devoir de préserver l'environnement ?", ["Oui : toute personne a ce devoir", "Non : seulement l'État", "Non : seulement les entreprises", "On ne sait pas"], 0, "Article 2 de la Charte.")],
            ["La santé est protégée.", "Les arbres : l'environnement.", "Toute personne a un devoir."],
            J("Quelle phrase du document justifie ta réponse à la question 3 ?", ENV2, [ENV1, P46_5, P46_6], pos=2)),
    }
    d["e5-4"] = {
        "lieutenant": {
            "type": "plan", "titre": "Fiche d'identité du Conseil constitutionnel", "colonnes": 2,
            "cases": [{"libelle": "Nombre de membres", "reponse": "9"}, {"libelle": "Durée de leur mandat", "reponse": "9 ans"}, {"libelle": "Son surnom", "reponse": "Les Sages"},
                      {"libelle": "Nombre de députés qui peuvent le saisir", "reponse": "60"}, {"libelle": "Il examine les lois avant leur", "reponse": "promulgation"}],
            "etiquettes": ["9", "9 ans", "Les Sages", "60", "promulgation", "12", "5 ans", "577"],
            "consigne": c58(C61, C62, C5) + " Complète la fiche d'identité du Conseil constitutionnel en plaçant les étiquettes. Trois étiquettes sont en trop. Puis choisis la phrase du document qui dit qui peut le saisir.",
            "indices": ["Le nombre de membres est le même que la durée du mandat en années.", "Soixante députés peuvent le saisir.", "Il examine les lois avant leur promulgation."],
            "justification": J("Quelle phrase du document dit qui peut saisir le Conseil constitutionnel ?", C61, [C62, C5], pos=0)},
        "second": {
            "type": "plan", "titre": "Le rôle du Conseil constitutionnel", "colonnes": 2,
            "cases": [{"libelle": "Il vérifie que les lois respectent", "reponse": "la Constitution"}, {"libelle": "Une disposition déclarée inconstitutionnelle ne peut être", "reponse": "promulguée"},
                      {"libelle": "Peut le saisir avant la promulgation", "reponse": "le président de la République"}, {"libelle": "Nombre de sénateurs qui peuvent le saisir", "reponse": "60"}, {"libelle": "Année de sa création", "reponse": "1958"}],
            "etiquettes": ["la Constitution", "promulguée", "le président de la République", "60", "1958", "le Parlement européen", "577", "1789"],
            "consigne": c58(C61, C62, C64) + " Complète le tableau en plaçant les étiquettes. Trois étiquettes sont en trop. Puis choisis la phrase du document qui dit ce que devient une disposition inconstitutionnelle.",
            "indices": ["Le Conseil vérifie le respect de la Constitution.", "Une disposition inconstitutionnelle ne peut être ni promulguée ni appliquée.", "Le Conseil est créé en 1958."],
            "justification": J("Quelle phrase du document dit ce que devient une disposition inconstitutionnelle ?", C62, [C61, C64], pos=1)},
    }
    return d
