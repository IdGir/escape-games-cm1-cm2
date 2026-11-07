"""Salle 3 « La glacerie de Paolo » : grades mousse, lieutenant, second (fiche : changements)."""
from aide import *

FICHE = "« Les changements d'état de l'eau »"
P_REVERS = "Ces changements sont réversibles : on peut revenir à l'état de départ."
P_CONDENS = "Dans la vie courante, on dit souvent condensation (la buée sur un miroir)."
P_ZERO = "Tant qu'il reste de la glace dans l'eau, le thermomètre reste à 0 °C."
P_CENT = "L'eau bout à 100 °C."
P_EVAP = "L'évaporation est lente, se fait à la surface de l'eau et à toute température : le linge sèche, une flaque disparaît."
P_EBUL = "L'ébullition se produit à 100 °C, avec des bulles de vapeur qui naissent dans tout le liquide."
P_INVIS = "La vapeur d'eau est un gaz invisible."
P_FUMEE = "La « fumée » blanche d'une casserole, la buée, le brouillard et les nuages sont faits de gouttelettes d'eau liquide : la vapeur s'est liquéfiée au contact de l'air plus froid."


def thermo(items, consigne, indices, j=None):
    b = {"type": "instrument", "instrument": "thermometre", "unite": "°C", "min": -20, "max": 110, "pas": 5, "etiquettes": 20,
         "items": items, "consigne": consigne, "indices": list(indices)}
    if j:
        b["justification"] = j
    return b


def donnees(svg, bloc=None):
    d = {}
    # ------------------------------------------------ e3-1 : les étiquettes des machines
    d["e3-1"] = {
        "mousse": assoc(
            "Paolo a perdu les étiquettes de ses machines. Relie chaque machine à ce qu'elle fait à l'eau. Clique sur une machine, puis sur ce qu'elle fait.",
            [("le congélateur", "l'eau devient de la glace"), ("le chauffe-glace", "la glace devient de l'eau"), ("la bouilloire", "l'eau devient de la vapeur")],
            ["Ouvre la fiche " + FICHE + " dans la Bibliothèque.", "Le congélateur refroidit, la bouilloire chauffe.", "Chauffer de la glace la fait fondre."]),
        "lieutenant": assoc(
            "Paolo range ses observations. Relie chaque situation au changement d'état qu'elle montre, puis choisis la phrase de la fiche qui parle de la buée.",
            [("les glaçons se forment dans le bac", "solidification"), ("le sorbet coule dans le cornet au soleil", "fusion"),
             ("la flaque de la cour disparaît", "vaporisation"), ("de la buée apparaît sur la vitre froide", "liquéfaction"),
             ("l'eau de la casserole bout", "vaporisation par ébullition")],
            ["Repère l'état de départ et l'état d'arrivée de l'eau.", "Une flaque qui disparaît et une casserole qui bout : deux façons de se vaporiser.",
             "Pour la justification : cherche le mot « condensation »."],
            J("Quelle phrase de la fiche parle de la buée ?", P_CONDENS, [P_REVERS, P_EVAP, P_CENT], pos=1)),
        "second": tri(
            "Paolo affiche le tableau des changements d'état de la glacerie. Range chaque situation dans la bonne colonne, puis choisis la phrase de la fiche qui justifie la colonne « liquéfaction ».",
            [("fusion", "Fusion"), ("solidification", "Solidification"), ("vaporisation", "Vaporisation"), ("liquefaction", "Liquéfaction")],
            [("la neige fond sur le toit", "fusion"), ("un glaçon fond dans le verre", "fusion"),
             ("la flaque gèle pendant la nuit", "solidification"), ("l'eau du bac à glaçons durcit", "solidification"),
             ("le linge sèche sur le fil", "vaporisation"), ("l'eau bout dans la bouilloire", "vaporisation"),
             ("la buée sur le miroir de la salle de bains", "liquefaction"), ("des gouttes sur une canette sortie du réfrigérateur", "liquefaction")],
            ["Pour chaque situation : quel état au départ, quel état à l'arrivée ?", "Les gouttes sur la canette viennent de l'air, pas de la canette.",
             "Pour la justification : la buée est une liquéfaction de tous les jours."],
            J("Quelle phrase de la fiche justifie la colonne « Liquéfaction » ?", P_CONDENS, [P_EVAP, P_ZERO, P_REVERS], pos=3)),
    }
    # ------------------------------------------------ e3-2 : les thermomètres
    d["e3-2"] = {
        "mousse": qcm(
            "Paolo montre deux thermomètres. Réponds aux deux questions.",
            [("La glace fond. Le thermomètre dans la glace indique...", ["0 °C", "50 °C", "100 °C"], 0, "La glace fond à 0 °C."),
             ("L'eau bout dans la casserole. Le thermomètre indique...", ["0 °C", "20 °C", "100 °C"], 2, "L'eau bout à 100 °C.")],
            ["Ouvre la fiche " + FICHE + " : cherche « températures repères ».", "La glace fond quand il fait 0 degré.", "L'eau bout quand elle est très chaude : 100 degrés."]),
        "lieutenant": thermo(
            [{"libelle": "Glace et eau mélangées, après 5 minutes", "mode": "lire", "valeur": 0},
             {"libelle": "Bac où il reste quelques glaçons", "mode": "regler", "valeur": 0, "depart": 30},
             {"libelle": "Eau qui bout depuis 3 minutes", "mode": "regler", "valeur": 100, "depart": 30}],
            "Paolo contrôle trois cuves. Lis le premier thermomètre, puis règle les deux autres avec les flèches. Enfin, choisis la phrase de la fiche qui explique le deuxième thermomètre.",
            ["Chaque petit trait vaut 5 °C.", "Tant que la glace n'a pas fini de fondre, la température ne monte pas.", "L'eau qui bout reste à la même température."],
            J("Quelle phrase de la fiche explique le deuxième thermomètre ?", P_ZERO, [P_CENT, P_EVAP, P_REVERS], pos=0)),
        "second": qcm(
            tableau("Relevé de Paolo : un bloc de glace chauffé doucement (relevé inventé pour le jeu)", ["Temps", "Température", "Ce qu'on voit"],
                    [["0 min", "−10 °C", "glace"], ["2 min", "−4 °C", "glace"], ["4 min", "0 °C", "glace et eau"], ["6 min", "0 °C", "glace et eau"],
                     ["8 min", "0 °C", "glace et eau"], ["10 min", "5 °C", "eau liquide"], ["12 min", "12 °C", "eau liquide"]])
            + "Réponds aux trois questions à partir du relevé et de la fiche.",
            [("Entre quels moments la glace fond-elle ?", ["Entre 0 et 2 min", "Entre 4 et 8 min environ", "Entre 10 et 12 min", "Pendant tout le relevé"], 1, "Glace et eau mélangées : c'est la fusion."),
             ("Pendant la fusion, la température...", ["monte vite", "reste à 0 °C", "descend", "monte jusqu'à 100 °C"], 1, "Tant qu'il reste de la glace, elle reste à 0 °C."),
             ("À 10 min, dans quel état est l'eau ?", ["Solide", "Liquide", "Gazeux", "Solide et liquide"], 1, "Toute la glace a fondu.")],
            ["Regarde la colonne « Ce qu'on voit » en même temps que la température.", "Trois mesures de suite donnent la même température.", "Après la fusion, l'eau liquide se réchauffe."],
            J("Quelle phrase de la fiche explique les trois mesures à 0 °C ?", P_ZERO, [P_CENT, P_REVERS, P_INVIS], pos=2)),
    }
    # ------------------------------------------------ e3-3 : du glaçon à la vapeur
    d["e3-3"] = {
        "mousse": ordre(
            "Paolo chauffe un glaçon dans une casserole. Remets les trois étapes dans l'ordre (flèches ▲ et ▼).",
            ["Le glaçon est solide.", "Le glaçon fond : il devient de l'eau.", "L'eau bout : elle devient de la vapeur."],
            ["Ouvre la fiche " + FICHE + ".", "Au début, le glaçon sort du congélateur.", "La vapeur vient en dernier."]),
        "lieutenant": ordre(
            "Paolo chauffe un bloc de glace jusqu'à l'ébullition. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche qui décrit la dernière étape visible.",
            ["La glace sort du congélateur, bien en dessous de 0 °C.", "La glace se réchauffe jusqu'à 0 °C.",
             "Fusion : glace et eau mélangées, le thermomètre reste à 0 °C.", "Toute la glace a fondu : l'eau liquide se réchauffe.",
             "Ébullition à 100 °C : des bulles naissent dans tout le liquide.", "La vapeur d'eau, invisible, part dans l'air."],
            ["La fusion ne commence qu'à 0 °C.", "Tant qu'il reste de la glace, la température ne monte pas.", "Pour la justification : cherche le mot « bulles »."],
            J("Quelle phrase de la fiche décrit l'ébullition ?", P_EBUL, [P_EVAP, P_FUMEE, P_ZERO], pos=1)),
        "second": ordre(
            "Paolo fait le chemin inverse : de la vapeur de la bouilloire jusqu'à un glaçon. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche qui prouve que c'est possible.",
            ["La bouilloire envoie de la vapeur d'eau invisible.", "La vapeur touche une assiette froide posée au-dessus.",
             "Liquéfaction : des gouttelettes d'eau apparaissent sur l'assiette.", "On recueille l'eau liquide dans un petit moule.",
             "On met le moule au congélateur.", "Solidification : l'eau devient un glaçon."],
            ["On part du gaz pour arriver au solide.", "Il faut une surface froide pour retrouver de l'eau liquide.", "Pour la justification : cherche le mot « réversibles »."],
            J("Quelle phrase de la fiche prouve qu'on peut revenir à l'état de départ ?", P_REVERS, [P_CENT, P_EBUL, P_INVIS], pos=0)),
    }
    # ------------------------------------------------ e3-4 : la fumée blanche (6e, 5e)
    d["e3-4"] = {
        "lieutenant": trous(
            "Paolo explique ce qu'on voit au-dessus de la casserole. Complète son texte (il y a des étiquettes en trop), puis choisis la phrase de la fiche qui le justifie.",
            "La vapeur d'eau est un gaz [[invisible]]. La « fumée » blanche au-dessus de la casserole n'est donc pas de la vapeur : ce sont de fines [[gouttelettes]] d'eau [[liquide]]. "
            "La vapeur s'est [[liquéfiée]] au contact de l'air plus [[froid]].",
            ["invisible", "gouttelettes", "liquide", "liquéfiée", "froid", "blanche", "solidifiée", "chaud", "fumée"],
            ["Ce qu'on voit ne peut pas être un gaz invisible.", "De la buée, c'est de l'eau liquide.", "Pour la justification : cherche « fumée » dans la fiche."],
            J("Quelle phrase de la fiche justifie le texte de Paolo ?", P_FUMEE, [P_EBUL, P_CONDENS, P_EVAP], pos=0)),
        "second": trous(
            "Paolo compare deux façons de vaporiser l'eau. Complète son carnet (il y a des étiquettes en trop), puis choisis la phrase de la fiche qui décrit l'évaporation.",
            "Le linge sèche dehors, même en hiver : c'est l'[[évaporation]]. Elle est [[lente]], se fait à la [[surface]] de l'eau et à toute température. "
            "Dans la casserole, à [[100]] °C, des bulles de vapeur naissent dans [[tout]] le liquide : c'est l'[[ébullition]].",
            ["évaporation", "lente", "surface", "100", "tout", "ébullition", "rapide", "fusion", "0", "liquéfaction"],
            ["Le linge ne bout pas : il sèche doucement.", "L'ébullition de l'eau a une température repère.", "Pour la justification : cherche « à toute température »."],
            J("Quelle phrase de la fiche décrit l'évaporation ?", P_EVAP, [P_EBUL, P_CENT, P_FUMEE], pos=1)),
    }
    return d
