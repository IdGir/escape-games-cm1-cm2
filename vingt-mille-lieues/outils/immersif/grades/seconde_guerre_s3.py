"""Message 3 « L'épicerie » (1942-1943) : grades mousse, lieutenant, second (fiche : Vivre sous l'Occupation).
Aucune énigme notée sur les persécutions : elles restent dans la fiche et la discussion."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "seconde-guerre", "tests", "donnees"))
from fiches import *

FICHE = "« Vivre sous l'Occupation »"
CAT = tableau("Les catégories de la carte d'alimentation (barème simplifié de 1942)", ["Lettre", "Qui ?"],
              [["E", "moins de 3 ans"], ["J1", "3 à 6 ans"], ["J2", "6 à 13 ans"], ["J3", "13 à 21 ans"], ["A", "21 à 70 ans"], ["V", "plus de 70 ans"]])


def donnees(svg, bloc=None):
    d = {}
    d["e3-1"] = {
        "mousse": code(
            "Lis le tableau, puis écris la lettre de la carte de Madeleine (42 ans) et celle de Lucienne (8 ans)." + CAT,
            [("Madeleine, 42 ans", "A", 1), ("Lucienne, 8 ans", "J2", 2)],
            ["Ouvre la fiche " + FICHE + ".", "42 ans : entre 21 et 70 ans.", "8 ans : entre 6 et 13 ans."]),
        "lieutenant": code(
            "Écris la catégorie de chaque carte de la famille, puis choisis la phrase de la fiche qui explique à quoi servent les tickets." + CAT,
            [("Madeleine, 42 ans", "A", 1), ("Robert, 19 ans", "J3", 2), ("Lucienne, 8 ans", "J2", 2), ("Firmin, 74 ans", "V", 1)],
            ["Plus de 70 ans : V.", "19 ans : entre 13 et 21 ans.", "Pour la justification : cherche « selon son âge »."],
            J("Quelle phrase de la fiche explique à quoi servent les tickets ?", O_TICKETS, [O_RATION, O_QUEUE, O_ERSATZ], pos=1)),
        "second": code(
            "En 1943, Lucienne fête ses 13 ans et le petit Jean ses 3 ans. Écris leur nouvelle catégorie, puis celle de Robert et de Madeleine. Choisis enfin la phrase de la fiche sur le marché noir." + CAT,
            [("Lucienne, 13 ans", "J3", 2), ("Jean, 3 ans", "J1", 2), ("Robert, 20 ans", "J3", 2), ("Madeleine, 43 ans", "A", 1)],
            ["13 ans : la catégorie des jeunes de 13 à 21 ans.", "3 ans : la catégorie des enfants de 3 à 6 ans.", "Pour la justification : cherche « en cachette »."],
            J("Quelle phrase de la fiche parle du marché noir ?", O_QUEUE, [O_TICKETS, O_RATION, O_STO], pos=2)),
    }
    d["e3-2"] = {
        "mousse": tri(
            "Range chaque produit : avec des tickets, ou ce qui le remplace ?",
            [("ration", "Avec des tickets"), ("ersatz", "Ce qui le remplace")],
            [("le pain", "ration"), ("le sucre", "ration"), ("l'orge grillée à la place du café", "ersatz")],
            ["Ouvre la fiche " + FICHE + ".", "Le pain s'achète avec un ticket.", "L'orge remplace le café."]),
        "lieutenant": tri(
            "Range chaque étiquette : produit rationné ou ersatz ? Puis choisis la phrase de la fiche qui définit les ersatz.",
            [("ration", "Produit rationné"), ("ersatz", "Ersatz")],
            [("la viande", "ration"), ("le charbon", "ration"), ("les vêtements", "ration"),
             ("l'orge grillée à la place du café", "ersatz"), ("des semelles de bois", "ersatz"), ("le rutabaga à la place de la pomme de terre", "ersatz")],
            ["Le charbon chauffe la maison : il manque.", "Le bois remplace le cuir.", "Pour la justification : cherche « orge »."],
            J("Quelle phrase de la fiche définit les ersatz ?", O_ERSATZ, [O_RATION, O_TICKETS, O_QUEUE], pos=0)),
        "second": tri(
            "Madeleine classe ce que vivent les clients : effet du manque, ou réponse pour se débrouiller ? Puis choisis la phrase de la fiche sur ce qui manque.",
            [("manque", "Ce qui manque"), ("debrouille", "Comment on se débrouille")],
            [("la nourriture", "manque"), ("le charbon", "manque"), ("les vêtements", "manque"),
             ("acheter très cher au marché noir", "debrouille"), ("des semelles de bois", "debrouille"), ("l'orge grillée à la place du café", "debrouille")],
            ["Le marché noir est une façon de se débrouiller, interdite.", "Le charbon manque pour se chauffer.", "Pour la justification : cherche « rationnés »."],
            J("Quelle phrase de la fiche dit ce qui manque ?", O_RATION, [O_ERSATZ, O_QUEUE, O_TICKETS], pos=3)),
    }
    d["e3-3"] = {
        "mousse": vf(
            "Robert a reçu une lettre. Pour chaque phrase, choisis vrai ou faux.",
            [("Robert doit partir travailler en Allemagne.", True, "C'est le STO."),
             ("Robert part en vacances.", False, "Il est obligé de partir travailler."),
             ("Certains jeunes refusent et se cachent.", True, "Ce sont les réfractaires.")],
            ["Ouvre la fiche " + FICHE + ".", "Obligatoire : on n'a pas le choix.", "Se cacher, c'est refuser."]),
        "lieutenant": vf(
            "Robert lit sa convocation. Choisis vrai ou faux, puis la phrase de la fiche qui date le STO.",
            [("Le STO est créé par une loi du 16 février 1943.", True, "Sous le régime de Vichy."),
             ("Les jeunes du STO travaillent en Allemagne.", True, "Dans les usines."),
             ("Le STO est une décision de la Résistance.", False, "C'est le régime de Vichy."),
             ("Ceux qui refusent de partir sont appelés réfractaires.", True, "Ils se cachent."),
             ("Le STO commence en 1939.", False, "En 1943.")],
            ["STO : février 1943.", "Réfractaire : qui refuse.", "Pour la justification : cherche « 16 février 1943 »."],
            J("Quelle phrase de la fiche date la création du STO ?", O_STO, [O_REFRACT, O_RATION, O_TICKETS], pos=2)),
        "second": vf(
            "Robert hésite. Choisis vrai ou faux, puis la phrase de la fiche qui explique le lien entre le STO et les maquis.",
            [("Le STO pousse beaucoup de jeunes à se cacher.", True, "Ce sont les réfractaires."),
             ("Certains réfractaires rejoignent les maquis.", True, "Les maquis grandissent à partir de 1943."),
             ("Refuser le STO ne comporte aucun risque.", False, "Les réfractaires sont recherchés."),
             ("Le STO montre que le régime de Vichy aide l'Allemagne.", True, "C'est une forme de collaboration."),
             ("Tous les jeunes Français partent au STO.", False, "Beaucoup refusent.")],
            ["Les maquis accueillent les réfractaires.", "Le STO sert l'Allemagne.", "Pour la justification : cherche « réfractaires »."],
            J("Quelle phrase de la fiche relie le STO et les maquis ?", O_REFRACT, [O_STO, O_QUEUE, O_ERSATZ], pos=1)),
    }
    d["e3-4"] = {
        "lieutenant": assoc(
            "Relie chaque mot à sa définition, puis choisis la phrase de la fiche qui parle du marché noir et des queues.",
            [("le rationnement", "chacun n'a droit qu'à une petite quantité"), ("le marché noir", "le commerce caché, très cher"),
             ("un ersatz", "un produit de remplacement"), ("un réfractaire", "un jeune qui refuse le STO"), ("la collaboration", "aider l'occupant")],
            ["Noir : caché.", "Réfractaire : qui refuse.", "Pour la justification : cherche « queue »."],
            J("Quelle phrase de la fiche parle des queues et du marché noir ?", O_QUEUE, [O_RATION, O_ERSATZ, O_REFRACT], pos=0)),
        "second": assoc(
            "Relie chaque situation à son mot, puis choisis la phrase de la fiche qui décrit les tickets de rationnement.",
            [("Madeleine compte les tickets de chaque client", "le rationnement"), ("un client achète du beurre en cachette, très cher", "le marché noir"),
             ("Lucienne boit de l'orge grillée au petit déjeuner", "un ersatz"), ("Robert se cache pour ne pas partir en Allemagne", "un réfractaire au STO"),
             ("un voisin travaille pour la police de l'occupant", "la collaboration")],
            ["Compter les tickets : rationnement.", "En cachette et très cher : marché noir.", "Pour la justification : cherche « carte »."],
            J("Quelle phrase de la fiche décrit les tickets de rationnement ?", O_TICKETS, [O_QUEUE, O_ERSATZ, O_STO], pos=3)),
    }
    return d
