"""Salle 2 « La grande salle d'Amboise » (fiche : francois-mecene)."""
from aide import *

F = "« François Ier, roi mécène »"
M1 = "Né à Cognac le 12 septembre 1494, élevé à Amboise, François Ier devient roi le 1er janvier 1515."
M2 = "Les 13 et 14 septembre 1515, il remporte la bataille de Marignan, près de Milan."
M3 = "C'est un roi guerrier, qui mène plusieurs guerres en Italie."
M4 = "En mécène, il fait venir des artistes italiens : Léonard de Vinci (1516), plus tard le Primatice et Benvenuto Cellini."
M5 = "Il fait commencer Chambord (1519) et transformer Fontainebleau."
M6 = "1530 : les lecteurs royaux (futur Collège de France) enseignent gratuitement le grec, l'hébreu, les mathématiques."
M7 = "1537 : le dépôt légal : un exemplaire de chaque livre imprimé va à la bibliothèque du roi."
M8 = "1539 : l'ordonnance de Villers-Cotterêts impose le français dans les actes de justice et d'administration."
M9 = "Un mécène ne crée pas lui-même les œuvres : il choisit, protège et paie ceux qui les créent."


def donnees(svg, bloc=None):
    d = {}
    d["e2-1"] = {
        "mousse": vf(
            "Pour chaque phrase, clique sur « Vrai » ou sur « Faux », puis vérifie.",
            [("François Ier devient roi de France en 1515.", True, "Le 1er janvier 1515."), ("Léonard de Vinci est un roi d'Italie.", False, "C'est un artiste invité."), ("François Ier aide et protège les artistes : c'est un mécène.", True, "Il les invite et les paie.")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "François Ier devient roi en 1515.", "Un mécène aide et paie les artistes."]),
        "lieutenant": qcm(
            carnet("Journal de Dame Hélène", "(inventé pour le jeu). « Le roi est né à Cognac le 12 septembre 1494, il a grandi à Amboise et il est devenu roi le 1er janvier 1515. En septembre de la même année, il a gagné la bataille de Marignan, près de Milan. »")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("À quel âge François Ier devient-il roi ?", ["20 ans", "15 ans", "30 ans", "40 ans"], 0, "Né en septembre 1494, il a 20 ans le 1er janvier 1515."),
             ("Où se trouve Marignan ?", ["Près de Milan, en Italie", "Près d'Amboise", "Près de Cognac", "À Paris"], 0, "En Italie."),
             ("Quel type de roi est François Ier ?", ["Un roi guerrier qui mène des guerres en Italie", "Un roi qui ne quitte jamais Amboise", "Un roi sans armée", "Un roi qui refuse les arts"], 0, "Il mène plusieurs guerres.")],
            ["Il est né en 1494, roi en 1515.", "Milan est une ville d'Italie.", "Relis ce que fait le roi en septembre 1515."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", M3, [M1, M4, M9], pos=1)),
        "second": vf(
            "Dame Hélène a noté six phrases sur le règne de François Ier. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui définit un mécène.",
            [("François Ier devient roi le 1er janvier 1515.", True, "À 20 ans."), ("Un mécène crée lui-même les œuvres.", False, "Il choisit, protège et paie."), ("François Ier fait venir Léonard de Vinci en 1516.", True, "Puis le Primatice et Cellini."),
             ("Le dépôt légal date de 1537.", True, "Un exemplaire de chaque livre va à la bibliothèque du roi."), ("L'ordonnance de Villers-Cotterêts impose le latin.", False, "Le français."), ("Les lecteurs royaux sont créés en 1530.", True, "Ils enseignent gratuitement.")],
            ["Un mécène ne crée pas les œuvres.", "L'ordonnance impose le français.", "1530 : lecteurs royaux."],
            J("Quelle phrase de la fiche définit un mécène ?", M9, [M4, M6, M2], pos=1)),
    }
    d["e2-2"] = {
        "mousse": ordre(
            "Remets la vie de François Ier dans l'ordre, du plus ancien (en haut) au plus récent (en bas).",
            [("François naît à Cognac", "1494"), ("Il devient roi", "1515"), ("Il invite Léonard de Vinci", "1516")],
            ["Ouvre la fiche " + F + ".", "On naît avant de devenir roi.", "Regarde les années."]),
        "lieutenant": ordre(
            "Dame Hélène résume le règne. Remets ces cinq événements dans l'ordre, puis choisis la phrase de la fiche qui date la victoire de Marignan.",
            ["Naissance de François, à Cognac (1494)", "François devient roi (1er janvier 1515)", "Victoire de Marignan (13 et 14 septembre 1515)", "Début du chantier de Chambord (1519)", "Dépôt légal des livres imprimés (1537)"],
            ["Naissance, couronnement, victoire, chantier, dépôt légal.", "1er janvier 1515 vient avant septembre 1515.", "1519 vient avant 1537."],
            J("Quelle phrase de la fiche date la victoire de Marignan ?", M2, [M1, M5, M7], pos=2)),
        "second": tri(
            "Dame Hélène classe les actions du roi par domaine. Range chaque action dans la bonne colonne, puis choisis la phrase de la fiche qui parle des lecteurs royaux.",
            [("arts", "Les arts"), ("lettres", "Les lettres")],
            [("Faire venir Léonard de Vinci", "arts"), ("Faire commencer Chambord (1519)", "arts"), ("Transformer Fontainebleau", "arts"), ("Créer les lecteurs royaux (1530)", "lettres"), ("Créer le dépôt légal (1537)", "lettres"), ("Imposer le français dans les actes officiels (1539)", "lettres")],
            ["Chambord et Fontainebleau sont des châteaux : les arts.", "Les livres et les langues : les lettres.", "Les lecteurs royaux enseignent."],
            J("Quelle phrase de la fiche parle des lecteurs royaux ?", M6, [M7, M8, M4], pos=0)),
    }
    d["e2-3"] = {
        "mousse": tri(
            "Range chaque carte : est-ce pour les arts, ou pour les lettres ? Clique sur une carte, puis sur une colonne.",
            [("arts", "Les arts"), ("lettres", "Les lettres")],
            [("Il invite Léonard de Vinci", "arts"), ("Il fait construire Chambord", "arts"), ("Il crée les lecteurs royaux", "lettres"), ("Il impose le français", "lettres")],
            ["Ouvre la fiche " + F + ".", "Chambord est une œuvre d'architecture.", "Les lettres : les livres et les langues."]),
        "lieutenant": vf(
            "Dame Hélène affirme cinq choses sur le roi. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui parle de Villers-Cotterêts.",
            [("L'ordonnance de Villers-Cotterêts date de 1539.", True, "Elle impose le français."), ("Elle impose le latin dans les actes de justice.", False, "Elle impose le français."), ("Le dépôt légal date de 1537.", True, "Un exemplaire de chaque livre imprimé."),
             ("Les lecteurs royaux enseignent gratuitement.", True, "Grec, hébreu, mathématiques."), ("François Ier a vécu à Amboise.", True, "Il y a été élevé.")],
            ["Villers-Cotterêts : 1539.", "Le dépôt légal : 1537.", "Les lecteurs royaux : 1530."],
            J("Quelle phrase de la fiche parle de Villers-Cotterêts ?", M8, [M6, M7, M1], pos=2)),
        "second": qcm(
            carnet("Notes de Dame Hélène", "(d'après la fiche). 1530 : les lecteurs royaux enseignent gratuitement le grec, l'hébreu, les mathématiques. 1537 : le dépôt légal. 1539 : l'ordonnance de Villers-Cotterêts impose le français dans les actes de justice et d'administration.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("Combien d'années entre les lecteurs royaux et l'ordonnance de Villers-Cotterêts ?", ["9 ans", "7 ans", "19 ans", "2 ans"], 0, "1539 − 1530 = 9."),
             ("Quelle langue l'ordonnance de 1539 impose-t-elle dans les actes officiels ?", ["Le français", "Le latin", "L'italien", "Le grec"], 0, "Le français."),
             ("Que reçoit la bibliothèque du roi avec le dépôt légal ?", ["Un exemplaire de chaque livre imprimé", "Tous les tableaux", "Des armes", "Des impôts"], 0, "1537.")],
            ["Soustrais 1530 de 1539.", "Les actes sont écrits en français.", "Un exemplaire de chaque livre imprimé."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", M7, [M6, M8, M9], pos=1)),
    }
    d["e2-4"] = {
        "lieutenant": code(
            "Le coffret de Dame Hélène est fermé par un cadenas. Écris les deux années demandées, puis ouvre.",
            [("Année où François Ier remporte la bataille de Marignan", "1515", 4), ("Année du dépôt légal", "1537", 4)],
            ["Marignan : l'année où il devient roi.", "Le dépôt légal : 1537.", "Cherche les dates dans la fiche."],
            J("Quelle phrase de la fiche donne la date du dépôt légal ?", M7, [M2, M8, M6], pos=1)),
        "second": code(
            "Le coffret de Dame Hélène est fermé par un cadenas. Calcule : combien d'années séparent la naissance du roi (1494) de la bataille de Marignan (1515) ? Combien d'années séparent Marignan de l'ordonnance de Villers-Cotterêts (1539) ? Quel est le nom du château où le roi a été élevé (7 lettres) ?",
            [("Années entre 1494 et 1515", "21", 2), ("Années entre 1515 et 1539", "24", 2), ("Château où le roi a grandi", "AMBOISE", 7, False)],
            ["1515 − 1494.", "1539 − 1515.", "C'est dans la grande salle de ce château."],
            J("Quelle phrase de la fiche donne le lieu où le roi a grandi ?", M1, [M2, M5, M7], pos=0)),
    }
    return d
