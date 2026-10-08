"""Salle 4 « La navette parlementaire » : le parcours d'une loi."""
from aide import *
from constitution_docs import *


def donnees(svg, bloc=None):
    d = {}
    d["e4-1"] = {
        "mousse": assoc(
            "Relie chaque mot à sa définition : clique à gauche, puis à droite.",
            [("Un projet de loi", "un texte proposé par le Gouvernement"), ("Une proposition de loi", "un texte proposé par un député ou un sénateur"), ("Promulguer", "rendre la loi officielle")],
            ["Ouvre la fiche « Le parcours d'une loi » dans la Bibliothèque.", "PROjet = Gouvernement.", "PROposition = parlementaires."]),
        "lieutenant": tri(
            c58(C39, C44, C10) + " Madame Ferrand range des actions. Range chaque action dans la bonne colonne, puis choisis la phrase du document qui dit qui a l'initiative des lois.",
            [("initiative", "Proposer un texte de loi"), ("amender", "Modifier le texte"), ("promulguer", "Rendre la loi officielle")],
            [("Le Premier ministre dépose un projet de loi", "initiative"), ("Un député dépose une proposition de loi", "initiative"), ("Les parlementaires votent un amendement", "amender"), ("Le Gouvernement propose un amendement", "amender"),
             ("Le Président promulgue la loi dans les quinze jours", "promulguer"), ("La loi devient officielle", "promulguer")],
            ["L'initiative appartient au Premier ministre et aux parlementaires.", "Le droit d'amendement : modifier le texte.", "Quinze jours pour promulguer."],
            J("Quelle phrase du document dit qui a l'initiative des lois ?", C39, [C44, C10], pos=1)),
        "second": qcm(
            c58(C45, C44, C10) + " Réponds aux trois questions, puis choisis la phrase du document qui décrit la navette.",
            [("Dans combien d'assemblées le texte est-il examiné successivement ?", ["Deux", "Une", "Trois", "Quatre"], 0, "Assemblée nationale et Sénat."), ("Qui a le droit d'amendement ?", ["Les membres du Parlement et le Gouvernement", "Les juges", "Les citoyens directement", "Le Conseil constitutionnel"], 0, "Article 44."),
             ("Combien de jours le Président a-t-il pour promulguer la loi ?", ["Quinze", "Trente", "Sept", "Un"], 0, "Article 10.")],
            ["Deux assemblées.", "Article 44 : droit d'amendement.", "Quinze jours."],
            J("Quelle phrase du document décrit la navette ?", C45, [C44, C10], pos=1)),
    }
    d["e4-2"] = {
        "mousse": ordre(
            "Remets les étapes du parcours d'une loi dans l'ordre, avec les flèches ▲▼.",
            ["Un texte de loi est déposé.", "Le texte est étudié et modifié.", "L'Assemblée nationale et le Sénat votent.", "Le président promulgue la loi."],
            ["Ouvre la fiche « Le parcours d'une loi ».", "Tout commence par un texte déposé.", "On promulgue à la fin."]),
        "lieutenant": ordre(
            c58(C45, C10) + " Madame Ferrand décrit le parcours d'une loi. Remets les cinq étapes dans l'ordre, puis choisis la phrase du document qui date la promulgation.",
            ["Dépôt d'un projet ou d'une proposition de loi.", "Étude en commission et dépôt d'amendements.", "Examen successif dans les deux assemblées.", "Promulgation par le Président dans les quinze jours.", "Publication au Journal officiel."],
            ["Le dépôt vient d'abord.", "L'étude en commission précède le vote.", "La promulgation vient après le vote."],
            J("Quelle phrase du document donne le délai de promulgation ?", C10, [C45, C39], pos=0)),
        "second": ordre(
            c58(C45, C10, C61, C62) + " Madame Ferrand décrit le contrôle du Conseil constitutionnel. Remets ces cinq étapes dans l'ordre, puis choisis la phrase du document qui dit ce que devient une loi déclarée inconstitutionnelle.",
            ["Le Parlement adopte définitivement la loi.", "Le Conseil constitutionnel est saisi avant la promulgation.", "Le Conseil examine si la loi respecte la Constitution.", "Une disposition inconstitutionnelle ne peut pas être promulguée.", "Le Président promulgue le reste de la loi dans les quinze jours."],
            ["La saisine a lieu avant la promulgation.", "Le Conseil vérifie le respect de la Constitution.", "Une disposition inconstitutionnelle est écartée."],
            J("Quelle phrase du document dit ce que devient une loi déclarée inconstitutionnelle ?", C62, [C61, C45], pos=0)),
    }
    d["e4-3"] = {
        "mousse": vf(
            "Pour chaque phrase, clique sur « Vrai » ou sur « Faux », puis vérifie.",
            [("Un projet de loi vient du Gouvernement.", True, "Une proposition vient d'un parlementaire."), ("La loi s'applique avant d'être publiée.", False, "Elle est publiée d'abord."), ("Le président promulgue la loi.", True, "Il rend la loi officielle.")],
            ["Ouvre la fiche « Le parcours d'une loi ».", "PROjet = Gouvernement.", "On publie avant d'appliquer."]),
        "lieutenant": qcm(
            c58(C10, C39, C44, C45) + " Réponds aux trois questions, puis choisis la phrase du document qui justifie la question 3.",
            [("Qui a l'initiative des lois ?", ["Le Premier ministre et les membres du Parlement", "Les juges", "Les maires", "Le Conseil constitutionnel"], 0, "Article 39."), ("Que permet le droit d'amendement ?", ["Modifier le texte de la loi", "Annuler la Constitution", "Élire le Président", "Juger les procès"], 0, "Article 44."),
             ("Pourquoi la loi passe-t-elle par les deux assemblées ?", ["Pour adopter un texte identique", "Pour doubler les impôts", "Pour changer de président", "Pour réduire le nombre de députés"], 0, "Article 45.")],
            ["Premier ministre et parlementaires.", "Un amendement modifie le texte.", "Un texte identique dans les deux assemblées."],
            J("Quelle phrase du document justifie ta réponse à la question 3 ?", C45, [C44, C39, C10], pos=1)),
        "second": vf(
            c58(C10, C39, C44, C61, C62) + " Madame Ferrand a noté six phrases. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase du document qui dit qui peut saisir le Conseil constitutionnel.",
            [("Le Président promulgue la loi dans les quinze jours.", True, "Article 10."), ("L'initiative des lois appartient aux juges.", False, "Au Premier ministre et aux parlementaires."), ("Soixante députés peuvent saisir le Conseil constitutionnel.", True, "Article 61."),
             ("Une disposition inconstitutionnelle peut être promulguée.", False, "Elle ne peut être ni promulguée ni appliquée."), ("Le Gouvernement a le droit d'amendement.", True, "Comme les parlementaires."), ("Seul le Président peut saisir le Conseil.", False, "Plusieurs autorités le peuvent.")],
            ["Quinze jours pour promulguer.", "Soixante députés ou soixante sénateurs.", "Une disposition inconstitutionnelle est écartée."],
            J("Quelle phrase du document dit qui peut saisir le Conseil constitutionnel ?", C61, [C62, C10, C44], pos=3)),
    }
    d["e4-4"] = {
        "lieutenant": code(
            c58(C10, C61) + " Le cadenas du Parlement demande trois nombres. Combien de jours le président a-t-il pour promulguer une loi ? Combien de députés au minimum peuvent saisir le Conseil constitutionnel ? Combien de sénateurs au minimum ?",
            [("Jours pour promulguer", "15", 2), ("Députés qui peuvent saisir le Conseil", "60", 2), ("Sénateurs qui peuvent saisir le Conseil", "60", 2)],
            ["Quinze jours.", "Soixante députés.", "Soixante sénateurs."],
            J("Quelle phrase du document donne le délai de promulgation ?", C10, [C61, C62], pos=0)),
        "second": code(
            c58(C10, C61) + " Le cadenas du Parlement demande trois nombres. Combien de jours dure le délai de promulgation ? Combien de députés au moins peuvent saisir le Conseil constitutionnel ? Combien de parlementaires au total (60 députés ou 60 sénateurs) faut-il compter pour deux saisines distinctes (une de chaque assemblée) ?",
            [("Délai de promulgation (jours)", "15", 2), ("Députés qui peuvent saisir le Conseil", "60", 2), ("Parlementaires pour deux saisines (une par assemblée)", "120", 3)],
            ["Quinze jours.", "Soixante députés.", "60 + 60."],
            J("Quelle phrase du document donne le nombre de parlementaires nécessaire ?", C61, [C10, C62], pos=1)),
    }
    return d
