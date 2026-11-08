"""Salle 3 « Le tableau des temps » : grades mousse, lieutenant, second (fiche : comparer)."""
from aide import *

FICHE = "« Comparer des déplacements »"
P_GARDE = "Pour comparer deux déplacements, on garde une grandeur identique."
P_DIST = "Sur une même distance, le plus rapide met la durée la plus courte."
P_DUREE = "Pendant une même durée, le plus rapide parcourt la plus grande distance."
P_CONCL = "Si la distance et la durée changent toutes les deux, on ne peut pas conclure tout de suite : il faut d'abord ramener les deux déplacements à une même distance ou à une même durée."
P_CLASSE = "Pour classer des concurrents sur une même distance, on écrit toutes les durées dans la même unité, puis on les range de la plus courte à la plus longue : 38 s, 52 s, puis 1 min 05 s, c'est-à-dire 65 s."
P_KMH = "On peut l'exprimer en kilomètres par heure (km/h) : c'est la distance qui serait parcourue en une heure."
P_GUEP = "Le guépard peut dépasser 100 km/h, mais seulement sur quelques centaines de mètres."


def donnees(svg, bloc=None):
    d = {}
    d["e3-1"] = {
        "mousse": qcm(
            tableau("Course de 100 m (durées inventées pour le jeu)", ["Concurrent", "Durée"], [["Salomé à vélo", "20 s"], ["Mila à pied", "70 s"]])
            + "Réponds aux deux questions.",
            [("Qui est la plus rapide ?", ["Salomé", "Mila", "Elles vont aussi vite"], 0, "Salomé met moins de temps."),
             ("Qui met le plus de temps ?", ["Salomé", "Mila", "Personne"], 1, "Mila met 70 s.")],
            ["Ouvre la fiche " + FICHE + " dans la Bibliothèque.", "Elles ont parcouru la même distance.", "La plus rapide met le moins de temps."]),
        "lieutenant": qcm(
            tableau("Tableau des temps (mesures inventées pour le jeu)", ["Concurrent", "Distance", "Durée"],
                    [["Salomé à vélo", "100 m", "20 s"], ["Yanis en caisse à savon", "100 m", "25 s"], ["Léo à trottinette", "60 m", "20 s"], ["Le petit train", "300 m", "50 s"]])
            + "Réponds aux quatre questions, puis choisis la phrase de la fiche qui explique la dernière réponse.",
            [("Entre Salomé et Yanis (même distance), qui est le plus rapide ?", ["Yanis", "Salomé", "Ils vont aussi vite", "On ne peut pas savoir"], 1, "Même distance : Salomé met moins de temps."),
             ("Entre Salomé et Léo (même durée), qui est le plus rapide ?", ["Léo", "Ils vont aussi vite", "Salomé", "On ne peut pas savoir"], 2, "Même durée : Salomé va plus loin."),
             ("Pour comparer Salomé et Yanis, quelle grandeur est identique ?", ["La durée", "La distance", "Les deux", "Aucune"], 1, "Ils ont parcouru tous les deux 100 m."),
             ("Peut-on comparer directement Yanis et le petit train avec ce tableau ?", ["Oui, le train va plus vite", "Oui, Yanis va plus vite", "Non, ni la distance ni la durée ne sont les mêmes", "Oui, ils vont aussi vite"], 2, "Il faut d'abord ramener les deux à une même distance ou une même durée.")],
            ["Regarde quelle colonne est identique pour les deux concurrents comparés.", "Même distance : le plus rapide met le moins de temps.", "Pour la justification : cherche « on ne peut pas conclure »."],
            J("Quelle phrase de la fiche explique la dernière réponse ?", P_CONCL, [P_DIST, P_KMH, P_GUEP], pos=1)),
        "second": tri(
            carnet("Référence", "(mesures inventées pour le jeu) : Salomé parcourt 100 m en 20 s, à vitesse constante. Elle met donc 40 s pour 200 m, et parcourt 50 m en 10 s.")
            + "Range chaque concurrent : plus rapide ou moins rapide que Salomé ? Ramène-toi d'abord à une même distance ou à une même durée. Puis choisis la phrase de la fiche qui justifie ta méthode.",
            [("plus", "Plus rapide que Salomé"), ("moins", "Moins rapide que Salomé")],
            [("Yanis : 100 m en 18 s", "plus"), ("Mila : 100 m en 70 s", "moins"), ("Le petit train : 200 m en 30 s", "plus"),
             ("Léo : 30 m en 10 s", "moins"), ("Nour : 200 m en 50 s", "moins"), ("Tom : 70 m en 10 s", "plus")],
            ["Pour 200 m, compare avec 40 s.", "Pour 10 s, compare avec 50 m.", "Pour la justification : la méthode, c'est garder une grandeur identique."],
            J("Quelle phrase de la fiche justifie ta méthode ?", P_GARDE, [P_KMH, P_GUEP, P_CLASSE], pos=0)),
    }
    d["e3-2"] = {
        "mousse": ordre(
            "Trois concurrents ont fait la même descente (durées inventées pour le jeu). Range-les du plus rapide au plus lent.",
            ["Salomé : 40 s", "Yanis : 55 s", "Mila : 150 s"],
            ["Ouvre la fiche " + FICHE + ".", "Le plus rapide a la plus petite durée.", "Commence par 40 s."]),
        "lieutenant": ordre(
            "Cinq concurrents ont fait la même descente de 300 m (durées inventées pour le jeu), notées dans des unités différentes. Range-les du plus rapide au plus lent, puis choisis la phrase de la fiche qui décrit la méthode.",
            ["Yanis : 58 s", "Salomé : 1 min 05 s", "Le petit train : 70 s", "Léo : 1 min 20 s", "Mila : 3 min 10 s"],
            ["Convertis toutes les durées en secondes.", "1 min 05 s = 65 s ; 1 min 20 s = 80 s.", "Pour la justification : cherche la phrase sur le classement."],
            J("Quelle phrase de la fiche décrit la méthode ?", P_CLASSE, [P_KMH, P_DUREE, P_GUEP], pos=2)),
        "second": code(
            carnet("Le compteur de Salomé", "(données inventées pour le jeu) : sur la piste plate, Salomé roule à vitesse constante et parcourt 100 m en 20 s.")
            + "Calcule la distance qu'elle parcourt en 1 s, puis en 1 min, puis choisis la phrase de la fiche qui définit une vitesse en km/h.",
            [("Distance en 1 s (en m)", "5", 1), ("Distance en 1 min (en m)", "300", 3)],
            ["100 m en 20 s : divise par 20.", "1 min = 60 s.", "60 × 5 m."],
            J("Quelle phrase de la fiche définit une vitesse en km/h ?", P_KMH, [P_CONCL, P_DIST, P_GARDE], pos=1)),
    }
    d["e3-3"] = {
        "mousse": trous(
            "Salomé écrit sa règle. Complète-la avec les bonnes étiquettes.",
            "Sur une même distance, le plus rapide met le [[moins]] de temps. Pendant une même durée, le plus rapide va le plus [[loin]].",
            ["moins", "loin", "plus", "près"],
            ["Ouvre la fiche " + FICHE + ".", "Le plus rapide arrive le premier.", "Le plus rapide parcourt la plus grande distance."]),
        "lieutenant": trous(
            "Salomé écrit sa règle complète. Complète-la avec les bonnes étiquettes (il y en a en trop), puis choisis la phrase de la fiche qui parle d'une même durée.",
            "Pour comparer deux déplacements, on garde une grandeur [[identique]]. Sur une même distance, le plus rapide met la durée la plus [[courte]]. Pendant une même [[durée]], il parcourt la plus grande [[distance]]. Si les deux grandeurs changent, on ne peut pas [[conclure]] tout de suite.",
            ["identique", "courte", "durée", "distance", "conclure", "longue", "différente", "masse"],
            ["Deux façons de comparer : même distance ou même durée.", "Le plus rapide met le moins de temps.", "Pour la justification : cherche « pendant une même durée »."],
            J("Quelle phrase de la fiche parle d'une même durée ?", P_DUREE, [P_DIST, P_GARDE, P_KMH], pos=0)),
        "second": vf(
            "Salomé relit les remarques du public. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui résume la règle.",
            [("Celui qui part le premier est toujours le plus rapide.", False, "Il faut comparer les durées ou les distances."),
             ("Yanis met 25 s sur 100 m et Salomé 40 s sur 200 m : Salomé est plus rapide.", True, "Pour 200 m, Yanis mettrait 50 s à la même vitesse."),
             ("Un cycliste à 15 km/h va plus vite qu'un piéton à 4 km/h.", True, "En une heure, il irait plus loin."),
             ("Si deux concurrents ont la même durée, ils vont forcément aussi vite.", False, "Il faut aussi la même distance."),
             ("Le guépard peut garder plus de 100 km/h pendant une heure.", False, "Seulement sur quelques centaines de mètres.")],
            ["Ramène toujours les deux déplacements à une même distance ou une même durée.", "25 s pour 100 m, c'est 50 s pour 200 m à la même vitesse.", "Pour la justification : cherche « grandeur identique »."],
            J("Quelle phrase de la fiche résume la règle ?", P_GARDE, [P_GUEP, P_CLASSE, P_CONCL], pos=2)),
    }
    d["e3-4"] = {
        "lieutenant": assoc(
            "Salomé complète le panneau des records (ordres de grandeur). Relie chaque animal ou véhicule à sa vitesse, puis choisis la phrase de la fiche qui explique ce que veut dire km/h.",
            [("un escargot", "moins de 1 km/h"), ("un piéton", "environ 4 km/h"), ("un cycliste en ville", "environ 15 km/h"),
             ("une voiture en ville", "50 km/h au plus"), ("un TGV", "jusqu'à 320 km/h")],
            ["Range d'abord du plus lent au plus rapide.", "En ville, une voiture ne doit pas dépasser 50 km/h.", "Pour la justification : cherche « en une heure »."],
            J("Quelle phrase de la fiche explique ce que veut dire km/h ?", P_KMH, [P_DIST, P_GUEP, P_GARDE], pos=3)),
        "second": ordre(
            "Range ces vitesses de la vie réelle (ordres de grandeur) de la plus petite à la plus grande, puis choisis la phrase de la fiche qui explique pourquoi le guépard ne gagnerait pas une course de 10 km.",
            [("un escargot", "moins de 1 km/h"), ("un piéton", "environ 4 km/h"), ("un cycliste en ville", "environ 15 km/h"),
             ("une voiture en ville", "50 km/h au plus"), ("un guépard lancé", "plus de 100 km/h"), ("un TGV", "jusqu'à 320 km/h")],
            ["Le piéton va moins vite que le cycliste.", "Le plus rapide est le train.", "Pour la justification : cherche ce que la fiche dit du guépard."],
            J("Quelle phrase de la fiche explique pourquoi le guépard ne gagnerait pas une course de 10 km ?", P_GUEP, [P_KMH, P_CONCL, P_DUREE], pos=1)),
    }
    return d
