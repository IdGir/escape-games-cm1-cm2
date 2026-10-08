"""Salle 5 « La salle d'entraînement » (fiche : circulation)."""
from aide import *

F = "« Le sang livre les nutriments »"
K1 = "Le cœur pompe le sang dans des vaisseaux qui atteignent tous les organes."
K2 = "Le sang leur apporte les nutriments venus de l'intestin grêle (et le dioxygène venu des poumons)."
K3 = "Pendant un effort, les muscles travaillent davantage et ont besoin de plus de nutriments : le cœur accélère."
K4 = "Au repos, le cœur d'un enfant bat environ 90 fois par minute ; après un effort intense, il peut dépasser 160."
K5 = "Pour mesurer son pouls : compter les battements pendant 15 secondes et multiplier par 4."
K6 = "Le cœur s'adapte aux besoins des muscles."


def donnees(svg, bloc=None):
    d = {}
    d["e5-1"] = {
        "mousse": code(
            "Basile apprend à Lou à mesurer son pouls. On compte les battements pendant 15 secondes, puis on multiplie par 4. Au repos, Lou compte 20 battements en 15 secondes." + question("Combien de battements en 1 minute ?"),
            [("Battements en 1 minute", "80", 2)],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Une minute, c'est 4 fois 15 secondes.", "Calcule 20 × 4."]),
        "lieutenant": qcm(
            "Basile a noté trois relevés de pouls de Lou. Lis le tableau, réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3."
            + tableau("Relevés de Lou (fictifs)", ["Situation", "Battements en 15 secondes"], [("Assise depuis 5 minutes", "22"), ("Juste après une minute de course sur place", "38"), ("5 minutes plus tard, au repos", "23")]),
            [("Combien de battements par minute juste après la course ?", ["152", "38", "95", "22"], 0, "38 × 4 = 152."),
             ("De combien de battements par minute le pouls a-t-il augmenté, entre le repos (22 en 15 s) et la course ?", ["64", "16", "152", "88"], 0, "152 − 88 = 64."),
             ("Pourquoi le cœur accélère-t-il pendant la course ?", ["Les muscles ont besoin de plus de nutriments", "Le cœur a froid", "Le sang devient plus lourd", "Les poumons se vident"], 0, "Les muscles travaillent davantage.")],
            ["Multiplie par 4.", "Compare les pouls par minute.", "Quels organes réclament plus quand on court ?"],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", K3, [K2, K1, K6], pos=1)),
        "second": code(
            "Basile mesure son pouls autrement : il compte pendant 30 secondes au lieu de 15. Au repos, il compte 31 battements en 30 secondes. Après sa montée du col, il compte 78 battements en 30 secondes. Calcule les deux pouls par minute, puis ouvre le cadenas.",
            [("Pouls au repos (par minute)", "62", 2), ("Pouls après le col (par minute)", "156", 3)],
            ["30 secondes, c'est une demi-minute : multiplie par 2.", "31 × 2, puis 78 × 2.", "Compare avec la méthode de la fiche (15 secondes × 4)."],
            J("Quelle phrase de la fiche donne la méthode de mesure du pouls ?", K5, [K4, K6, K3], pos=2)),
    }
    d["e5-2"] = {
        "mousse": qcm(
            "Lis la question, clique sur la bonne réponse, puis vérifie.",
            [("Qui envoie le sang dans tout le corps ?", ["Le cœur", "L'estomac", "Les dents", "Les poumons"], 0, "Le cœur pompe le sang.")],
            ["Ouvre la fiche " + F + ".", "Le cœur bat dans la poitrine.", "Le cœur est comme une pompe."]),
        "lieutenant": vf(
            "Basile a noté cinq phrases sur le sang. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui dit ce que le sang apporte aux organes.",
            [("Le cœur pompe le sang dans des vaisseaux qui atteignent tous les organes.", True, "Il est au centre de la circulation."), ("Le sang apporte aux organes les nutriments venus de l'intestin grêle.", True, "Et le dioxygène venu des poumons."),
             ("Le cœur bat moins vite pendant un effort.", False, "Il accélère."), ("Les nutriments passent dans le sang à travers la paroi de l'intestin grêle.", True, "C'est la fin de la digestion."),
             ("Les aliments passent par le cœur.", False, "Jamais : le cœur pompe le sang.")],
            ["Le cœur est une pompe pour le sang.", "Pendant un effort, le cœur s'adapte.", "Pour la justification : cherche la phrase qui parle de l'intestin grêle et des organes."],
            J("Quelle phrase de la fiche dit ce que le sang apporte aux organes ?", K2, [K1, K3, K6], pos=2)),
        "second": qcm(
            carnet("Schéma de Basile", "(chaîne de livraison). Aliments, puis digestion, puis nutriments dans le sang, puis cœur, puis organes et muscles.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Où les nutriments entrent-ils dans le sang ?", ["Dans l'intestin grêle", "Dans l'estomac", "Dans la bouche", "Dans le cœur"], 0, "Ils traversent sa paroi."),
             ("Pourquoi le cœur est-il indispensable à la livraison ?", ["Il pompe le sang vers tous les organes", "Il digère les aliments", "Il fabrique les nutriments", "Il mâche les aliments"], 0, "Le cœur pompe le sang."),
             ("Que se passe-t-il quand les muscles travaillent davantage ?", ["Ils ont besoin de plus de nutriments et le cœur accélère", "Le cœur ralentit", "Le sang s'arrête", "Les muscles n'ont plus besoin de rien"], 0, "C'est la fin de la chaîne.")],
            ["Suis la chaîne dans l'ordre.", "Le cœur est une pompe.", "Plus d'effort, plus de besoins."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", K1, [K2, K5, K4], pos=3)),
    }
    d["e5-3"] = {
        "mousse": tri(
            "Range chaque situation. Le cœur bat-il vite ou lentement ? Clique sur une carte, puis sur une colonne.",
            [("vite", "Le cœur bat vite"), ("lent", "Le cœur bat lentement")],
            [("Faire un sprint", "vite"), ("Monter l'escalier en courant", "vite"), ("Dormir", "lent"), ("Écouter une histoire", "lent")],
            ["Ouvre la fiche " + F + ".", "Quand on court, le cœur s'accélère.", "Quand on dort, le corps se repose."]),
        "lieutenant": tri(
            "Basile compare des pouls. Range chaque relevé : pouls bas (au repos) ou pouls élevé (après effort) ? Puis choisis la phrase de la fiche qui donne la valeur au repos d'un enfant.",
            [("repos", "Pouls au repos (environ 90 par minute ou moins)"), ("effort", "Pouls après un effort intense")],
            [("22 battements en 15 secondes, assis", "repos"), ("23 battements en 15 secondes, après 5 minutes de repos", "repos"), ("15 battements en 15 secondes pour un coureur au repos", "repos"),
             ("40 battements en 15 secondes après la course", "effort"), ("45 battements en 15 secondes dans un sprint", "effort"), ("41 battements en 15 secondes après l'escalier en courant", "effort")],
            ["Multiplie par 4 pour comparer avec 90 et 160.", "Plus de 40 battements en 15 secondes : plus de 160 par minute.", "Moins de 25 en 15 secondes : moins de 100 par minute."],
            J("Quelle phrase de la fiche donne la valeur du pouls au repos d'un enfant ?", K4, [K3, K5, K1], pos=1)),
        "second": ordre(
            "Remets dans l'ordre la livraison des nutriments, de l'aliment au muscle, puis choisis la phrase de la fiche qui justifie le passage « dans le sang ».",
            ["Basile mange un repas.", "La digestion transforme les aliments en nutriments.", "Les nutriments passent dans le sang à travers la paroi de l'intestin grêle.", "Le cœur pompe le sang dans les vaisseaux.", "Le sang apporte les nutriments aux muscles."],
            ["Commence par l'aliment et termine par le muscle.", "Les nutriments passent dans le sang avant d'être pompés.", "Le cœur est une étape vers les organes."],
            J("Quelle phrase de la fiche justifie le passage « dans le sang » ?", K2, [K1, K4, K3], pos=0)),
    }
    d["e5-4"] = {
        "lieutenant": code(
            "Basile compare deux pouls. Au repos, il compte 15 battements en 15 secondes. Dans un sprint, il en compte 45 en 15 secondes. Calcule, puis ouvre le cadenas.",
            [("Battements par minute dans le sprint", "180", 3), ("Différence avec le repos (battements par minute)", "120", 3)],
            ["Multiplie chaque relevé par 4.", "Repos : 60 par minute ; sprint : 180 par minute.", "180 − 60."],
            J("Quelle phrase de la fiche donne la méthode de calcul ?", K5, [K4, K3, K6], pos=2)),
        "second": vf(
            "Basile a noté six phrases dans son carnet. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui dit que le cœur s'adapte aux muscles.",
            [("Au repos, le cœur d'un enfant bat environ 90 fois par minute.", True, "Ordre de grandeur."), ("Après un effort intense, le cœur peut dépasser 160 battements par minute.", True, "Il accélère."),
             ("Le cœur garde le même rythme quel que soit l'effort.", False, "Il s'adapte."), ("Le sang transporte les aliments tels qu'ils ont été mangés.", False, "Il transporte les nutriments."),
             ("Le pouls se prend au poignet ou au cou.", True, "On y sent le battement du sang."), ("Le cœur s'adapte aux besoins des muscles.", True, "C'est la fin de la chaîne.")],
            ["Le cœur accélère pendant un effort.", "Le sang transporte des nutriments, pas des aliments entiers.", "Pour la justification : cherche la phrase la plus courte."],
            J("Quelle phrase de la fiche dit que le cœur s'adapte aux muscles ?", K6, [K1, K3, K5], pos=3)),
    }
    return d
