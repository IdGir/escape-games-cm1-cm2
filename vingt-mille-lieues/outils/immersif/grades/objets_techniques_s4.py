"""Salle 4 « La salle des machines » (fiche : energie-mouvement)."""
from aide import *

F = "« Énergie et mouvement »"
E1 = "Tout objet qui fonctionne utilise une source d'énergie : les muscles, une pile ou une batterie, le courant du secteur, le vent, l'eau ou le soleil."
E2 = "L'énergie passe par une commande, est transmise, puis transformée en effet utile : lumière, mouvement, chaleur."
E3 = "Vélo : les muscles des jambes font tourner le pédalier ; la chaîne transmet le mouvement au pignon ; le pignon entraîne la roue arrière ; le vélo avance."
E4 = "Engrenage : deux roues dentées en contact, qui tournent en sens contraire."
E5 = "Poulies et courroie : deux roues à gorge éloignées, reliées par une courroie."
E6 = "Chaîne : relie deux roues dentées éloignées."
E7 = "Levier : barre qui pivote autour d'un point d'appui."
E8 = "Manivelle : transforme un va-et-vient en rotation."
E9 = "Le moteur électrique fournit un mouvement de rotation."


def donnees(svg, bloc=None):
    d = {}
    d["e4-1"] = {
        "mousse": ordre(
            "Remets les étapes dans l'ordre avec ▲ et ▼, puis vérifie.",
            [("La pile contient l'énergie", "source"), ("On appuie sur l'interrupteur", "commande"), ("L'ampoule s'allume", "effet")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Tout commence par ce qui contient l'énergie.", "La lumière est la dernière étape."]),
        "lieutenant": ordre(
            "Monsieur Marcel explique le fonctionnement d'une perceuse à batterie. Remets les cinq étapes dans l'ordre, puis choisis la phrase de la fiche qui donne le schéma général de la chaîne d'énergie.",
            [("La batterie contient l'énergie", "source"), ("On appuie sur la gâchette", "commande"), ("Le courant circule jusqu'au moteur", "transmission"), ("Le moteur électrique fournit un mouvement de rotation", "transformation"), ("Le foret tourne et perce le mur", "effet utile")],
            ["Source, commande, transmission, effet.", "La gâchette commande.", "Le moteur donne la rotation."],
            J("Quelle phrase de la fiche donne le schéma général de la chaîne d'énergie ?", E2, [E1, E9, E3], pos=2)),
        "second": qcm(
            carnet("Chaîne d'énergie du vélo", "(d'après la fiche). Les muscles des jambes font tourner le pédalier ; la chaîne transmet le mouvement au pignon ; le pignon entraîne la roue arrière ; le vélo avance.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Quelle est la source d'énergie du vélo ?", ["Les muscles des jambes", "La chaîne", "La roue", "Le pignon"], 0, "Ils font tourner le pédalier."),
             ("Quel élément transmet le mouvement vers l'arrière ?", ["La chaîne", "Le guidon", "La selle", "Les freins"], 0, "Elle relie deux roues dentées éloignées."),
             ("Combien d'étapes compte le trajet de l'énergie, des muscles à l'avancée ?", ["4", "2", "3", "6"], 0, "Pédalier, chaîne, pignon, vélo qui avance.")],
            ["Les muscles fournissent l'énergie.", "Une chaîne relie deux roues dentées éloignées.", "Compte les verbes de la phrase."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", E6, [E3, E1, E4], pos=1)),
    }
    d["e4-2"] = {
        "mousse": assoc(
            "Relie chaque machine à l'énergie qui la fait fonctionner. Clique sur une machine, puis sur son énergie.",
            [("Une trottinette", "les muscles"), ("Une télécommande", "une pile"), ("Une éolienne", "le vent")],
            ["Ouvre la fiche " + F + ".", "La trottinette n'a ni pile ni prise.", "L'éolienne a besoin d'air en mouvement."]),
        "lieutenant": qcm(
            carnet("Machines de l'atelier", "(inventées pour le jeu). Une lampe frontale (pile), un ventilateur (prise), un moulin (eau de la rivière), une calculatrice (soleil).")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("Quelle machine utilise le courant du secteur ?", ["Le ventilateur", "La lampe frontale", "Le moulin", "La calculatrice"], 0, "Il se branche à une prise."),
             ("Quelle machine s'arrête dans le noir ?", ["La calculatrice solaire", "Le ventilateur", "Le moulin", "La lampe frontale"], 0, "Elle utilise la lumière du soleil."),
             ("Quelles sources d'énergie la fiche énumère-t-elle ?", ["Les muscles, une pile ou une batterie, le courant du secteur, le vent, l'eau, le soleil", "Seulement la pile", "Seulement le courant de la prise", "Seulement les muscles"], 0, "Tout objet utilise une source d'énergie.")],
            ["La prise fournit le courant du secteur.", "Solaire : lumière du soleil.", "La fiche donne une liste de sources."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", E1, [E2, E3, E9], pos=1)),
        "second": tri(
            "Éléonore classe des objets selon leur source d'énergie. Range chaque objet dans la bonne colonne, puis choisis la phrase de la fiche qui énumère les sources.",
            [("humaine", "Les muscles"), ("elec", "Pile ou prise"), ("nature", "Vent, eau ou soleil")],
            [("Une trottinette classique", "humaine"), ("Un ouvre-boîte à manivelle", "humaine"), ("Une télécommande", "elec"), ("Un réfrigérateur", "elec"), ("Un moulin à eau", "nature"), ("Une calculatrice solaire", "nature")],
            ["Une pile et une prise : électrique.", "L'eau, le vent, le soleil : la nature.", "Les muscles : la force humaine."],
            J("Quelle phrase de la fiche énumère les sources d'énergie ?", E1, [E2, E3, E9], pos=2)),
    }
    d["e4-3"] = {
        "mousse": qcm(
            "Lis la question, clique sur la bonne réponse, puis vérifie.",
            [("Deux roues dentées en contact forment…", ["un engrenage", "un levier", "une poulie"], 0, "Elles tournent en sens contraire.")],
            ["Ouvre la fiche " + F + ".", "Les dents s'entraînent.", "Elles tournent en sens contraire."]),
        "lieutenant": {
            "type": "plan", "titre": "Les organes de transmission", "colonnes": 2,
            "cases": [{"libelle": "Relie le pédalier au pignon d'un vélo", "reponse": "une chaîne"}, {"libelle": "Deux roues dentées en contact", "reponse": "un engrenage"}, {"libelle": "Barre qui pivote autour d'un point d'appui", "reponse": "un levier"},
                      {"libelle": "Transforme un va-et-vient en rotation", "reponse": "une manivelle"}, {"libelle": "Deux roues à gorge reliées par une courroie", "reponse": "des poulies"}, {"libelle": "Fournit un mouvement de rotation à partir de l'électricité", "reponse": "un moteur électrique"}],
            "etiquettes": ["une chaîne", "un engrenage", "un levier", "une manivelle", "des poulies", "un moteur électrique", "un ressort", "une vis"],
            "consigne": "Monsieur Marcel complète le tableau. Place chaque étiquette dans la bonne case. Deux étiquettes sont en trop. Puis choisis la phrase de la fiche qui définit la manivelle.",
            "indices": ["Le levier a un point d'appui.", "La manivelle change un va-et-vient en rotation.", "Le moteur électrique donne une rotation."],
            "justification": J("Quelle phrase de la fiche définit la manivelle ?", E8, [E7, E4, E5], pos=1)},
        "second": vf(
            "Marcel a noté six phrases sur les transmissions. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui décrit l'engrenage.",
            [("Deux roues dentées en contact tournent dans le même sens.", False, "Elles tournent en sens contraire."), ("Une chaîne relie deux roues dentées éloignées.", True, "Comme sur un vélo."), ("Un levier est une barre qui pivote autour d'un point d'appui.", True, "C'est la définition."),
             ("Une manivelle transforme une rotation en va-et-vient.", False, "Elle fait l'inverse."), ("Deux poulies éloignées sont reliées par une courroie.", True, "Roues à gorge."), ("Le moteur électrique fournit un mouvement de rotation.", True, "À partir de l'électricité.")],
            ["Les engrenages s'entraînent en sens contraire.", "La manivelle part du va-et-vient.", "Une courroie relie deux poulies."],
            J("Quelle phrase de la fiche décrit l'engrenage ?", E4, [E5, E6, E8], pos=2)),
    }
    d["e4-4"] = {
        "lieutenant": code(
            "Le cadenas de la salle des machines demande deux mots (les accents et les majuscules n'ont pas d'importance).",
            [("Barre rigide qui pivote autour d'un point d'appui (6 lettres)", "levier", 6, False), ("Elle transforme un va-et-vient en rotation (9 lettres)", "manivelle", 9, False)],
            ["Les deux mots sont dans la fiche « Énergie et mouvement ».", "Le premier commence par L.", "Le second commence par M."],
            J("Quelle phrase de la fiche définit le levier ?", E7, [E4, E8, E6], pos=2)),
        "second": code(
            "Le cadenas de la salle des machines demande trois nombres. Combien d'étapes la fiche donne-t-elle pour la chaîne du vélo (muscles, pédalier, chaîne, pignon, roue arrière, avance) ? Combien de roues dentées un engrenage compte-t-il au minimum ? Combien de sources d'énergie la fiche cite-t-elle (muscles, pile ou batterie, secteur, vent, eau, soleil) ?",
            [("Étapes de la chaîne du vélo", "4", 1), ("Roues dentées d'un engrenage", "2", 1), ("Sources d'énergie citées", "6", 1)],
            ["Relis le texte du vélo.", "Un engrenage est fait de deux roues dentées en contact.", "Compte : muscles, pile, secteur, vent, eau, soleil."],
            J("Quelle phrase de la fiche cite les sources d'énergie ?", E1, [E2, E3, E9], pos=1)),
    }
    return d
