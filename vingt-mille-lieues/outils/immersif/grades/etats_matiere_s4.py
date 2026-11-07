"""Salle 4 « La cuisine de Fatou » : grades mousse, lieutenant, second (fiche : conservation)."""
from aide import *

FICHE = "« Ce qui change et ce qui se conserve »"
P_CONSERVE = "Pendant un changement d'état, la matière ne disparaît pas et n'apparaît pas : la masse se conserve."
P_FERME = "200 g de glaçons donnent 200 g d'eau liquide, à condition de travailler dans un récipient fermé pour ne rien perdre par évaporation."
P_LITRE = "1 000 mL d'eau liquide donnent environ 1 090 mL de glace."
P_BOUTEILLE = "C'est pourquoi une bouteille pleine gonfle au congélateur, et pourquoi les canalisations peuvent éclater en hiver."
P_FLOTTE = "À masse égale, la glace prend plus de place que l'eau liquide : c'est aussi pour cela que les glaçons et les icebergs flottent."
P_MESURE = "Pour savoir ce qui change, on mesure avant et après : avec une balance pour la masse, avec un récipient gradué pour le volume."
P_CHANGE = "Ce qui change : l'état, la forme, parfois le volume."
P_RESTE = "Ce qui reste : la masse, et la nature de la matière (la glace, c'est encore de l'eau)."


def plan(titre, colonnes, cases, etiquettes, consigne, indices, j=None):
    b = {"type": "plan", "titre": titre, "colonnes": colonnes, "cases": [{"libelle": l, "reponse": r} for l, r in cases],
         "etiquettes": list(etiquettes), "consigne": consigne, "indices": list(indices)}
    if j:
        b["justification"] = j
    return b


def donnees(svg, bloc=None):
    d = {}
    # ------------------------------------------------ e4-1 : les glaçons de la cantine
    d["e4-1"] = {
        "mousse": qcm(
            "Fatou pèse des glaçons dans une boîte fermée, avant et après qu'ils ont fondu. Réponds aux deux questions.",
            [("Avant : 100 g de glaçons. Après la fusion, la balance affiche...", ["50 g", "100 g", "150 g"], 1, "La masse ne change pas."),
             ("Quand les glaçons ont fondu, la boîte contient...", ["de l'eau liquide", "de l'air seulement", "du sable"], 0, "La glace devient de l'eau liquide.")],
            ["Ouvre la fiche " + FICHE + " dans la Bibliothèque.", "La boîte est fermée : rien ne sort, rien n'entre.", "La glace, c'est encore de l'eau."]),
        "lieutenant": qcm(
            "Fatou compare des masses avant et après un changement d'état. Réponds aux quatre questions, puis choisis la phrase de la fiche qui explique la question 2.",
            [("Boîte fermée : 300 g de glaçons fondent. La balance affiche...", ["250 g", "300 g", "330 g", "0 g"], 1, "La masse se conserve."),
             ("Bol ouvert au soleil toute la journée : la masse d'eau a un peu baissé. Pourquoi ?", ["La masse ne se conserve pas", "Un peu d'eau s'est évaporée dans l'air",
              "La glace était plus lourde", "La balance est cassée"], 1, "L'eau partie dans l'air n'est plus pesée."),
             ("Quand l'eau gèle, qu'est-ce qui augmente ?", ["La masse", "Le volume", "La quantité d'eau", "Rien"], 1, "Elle augmente de volume d'environ un dixième."),
             ("Pourquoi un glaçon flotte-t-il ?", ["Il est creux", "À masse égale, la glace prend plus de place que l'eau liquide", "Il est plus lourd que l'eau", "Il est froid"], 1,
              "La glace est moins dense que l'eau liquide.")],
            ["Un récipient fermé empêche l'eau de partir en vapeur.", "Dans un bol ouvert, l'eau s'évapore lentement.", "Pour la justification : cherche « récipient fermé »."],
            J("Quelle phrase de la fiche explique la question 2 ?", P_FERME, [P_CONSERVE, P_FLOTTE, P_CHANGE], pos=1)),
        "second": vf(
            "Fatou relit les conclusions d'une équipe. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui résume ce qui se conserve.",
            [("En gelant, l'eau devient plus lourde, puisqu'elle prend plus de place.", False, "Le volume augmente, la masse reste la même."),
             ("Un iceberg flotte parce que, à masse égale, la glace prend plus de place que l'eau liquide.", True, "C'est écrit dans la fiche."),
             ("La glace n'est plus de l'eau : c'est une autre matière.", False, "La glace, c'est encore de l'eau."),
             ("Pour comparer des volumes, on utilise un récipient gradué.", True, "La balance mesure la masse, le récipient gradué le volume."),
             ("Si la masse baisse dans un bol ouvert, c'est que la matière a disparu.", False, "Elle est partie dans l'air par évaporation.")],
            ["Prendre plus de place ne veut pas dire peser plus.", "Une balance pour la masse ; un récipient gradué pour le volume.", "Pour la justification : cherche « Ce qui reste »."],
            J("Quelle phrase de la fiche résume ce qui se conserve ?", P_RESTE, [P_CHANGE, P_MESURE, P_BOUTEILLE], pos=2)),
    }
    # ------------------------------------------------ e4-2 : le carnet de Fatou
    d["e4-2"] = {
        "mousse": code(
            "Fatou met 3 glaçons de 20 g chacun dans un bol fermé. Ils fondent. Quelle est la masse de l'eau obtenue ?",
            [("Masse de l'eau (en g)", "60", 2)],
            ["Ouvre la fiche " + FICHE + " : cherche « Calculer ».", "La masse ne change pas : calcule la masse des glaçons.", "20 + 20 + 20."]),
        "lieutenant": code(
            "Fatou met au congélateur une bouteille de 2 000 g d'eau (2 000 mL). Son carnet dit : 1 000 mL d'eau donnent environ 1 090 mL de glace. Calcule la masse de la glace, puis son volume. Choisis enfin la phrase de la fiche que tu as utilisée pour le volume.",
            [("Masse de la glace (en g)", "2000", 4), ("Volume de la glace (en mL)", "2180", 4)],
            ["La masse se conserve : elle ne change pas.", "2 000 mL, c'est deux fois 1 000 mL.", "2 × 1 090 mL = 2 180 mL."],
            J("Quelle phrase de la fiche as-tu utilisée pour le volume ?", P_LITRE, [P_FERME, P_CONSERVE, P_MESURE], pos=0)),
        "second": code(
            "Dans le bac de Fatou, il y a 2 180 mL de glace. Son carnet dit : 1 000 mL d'eau donnent environ 1 090 mL de glace, et 1 mL d'eau liquide a une masse de 1 g. Quand toute la glace aura fondu, dans un bac fermé, quel volume d'eau liquide obtiendra-t-elle ? Quelle masse ?",
            [("Volume d'eau liquide (en mL)", "2000", 4), ("Masse de l'eau (en g)", "2000", 4)],
            ["Fais le calcul à l'envers : 1 090 mL de glace redonnent 1 000 mL d'eau.", "2 180, c'est deux fois 1 090.", "Bac fermé : la masse de la glace est celle de l'eau."],
            J("Quelle phrase de la fiche permet de trouver la masse ?", P_CONSERVE, [P_FLOTTE, P_LITRE, P_CHANGE], pos=1)),
    }
    # ------------------------------------------------ e4-3 : la bouteille oubliée au congélateur
    d["e4-3"] = {
        "mousse": plan(
            "La bouteille avant et après le congélateur", 3,
            [("Repère 1", "eau liquide"), ("Repère 2", "glace"), ("Repère 3", "500 g : même masse")],
            ["eau liquide", "glace", "500 g : même masse"],
            "Fatou a oublié une bouteille d'eau au congélateur. Place chaque étiquette sur le bon repère du schéma. Clique sur une étiquette, puis sur la case du repère.\n" + svg("e4-3", "matelot"),
            ["Ouvre la fiche " + FICHE + ".", "Avant le congélateur, l'eau coule ; après, elle est dure.", "La balance montre la même masse avant et après."]),
        "lieutenant": plan(
            "La bouteille avant et après le congélateur", 2,
            [("Repère 1", "eau liquide"), ("Repère 2", "glace"), ("Repère 3", "500 g : même masse"), ("Repère 4", "volume plus grand")],
            ["eau liquide", "glace", "500 g : même masse", "volume plus grand", "550 g : masse plus grande", "volume plus petit", "vapeur d'eau"],
            "Fatou compare la bouteille bouchée avant et après le congélateur. Place chaque étiquette sur le bon repère (trois sont en trop), puis choisis la phrase de la fiche qui explique le bouchon soulevé.\n" + svg("e4-3", "timonier"),
            ["La masse ne change pas pendant un changement d'état.", "Regarde le bouchon de la bouteille de droite.", "Pour la justification : cherche « bouteille pleine »."],
            J("Quelle phrase de la fiche explique le bouchon soulevé ?", P_BOUTEILLE, [P_FERME, P_RESTE, P_MESURE], pos=2)),
        "second": plan(
            "La bouteille avant et après le congélateur", 2,
            [("Repère 1", "eau liquide"), ("Repère 2", "glace"), ("Repère 3", "500 g : même masse"), ("Repère 4", "volume plus grand")],
            ["eau liquide", "glace", "500 g : même masse", "volume plus grand", "545 g : masse plus grande", "même volume", "eau solide et vapeur", "450 g : masse plus petite"],
            "Fatou a noté dans son carnet : « Mercredi matin, la bouteille est gonflée, le bouchon s'est soulevé. Sur la balance : 500 g. » Place chaque étiquette sur le bon repère (quatre sont en trop), puis choisis la phrase de la fiche qui dit ce qui change.\n" + svg("e4-3", "timonier"),
            ["545, c'est le volume en mL de la glace, pas sa masse.", "La bouteille gonflée montre un changement de volume.", "Pour la justification : cherche « Ce qui change »."],
            J("Quelle phrase de la fiche dit ce qui change pendant la congélation ?", P_CHANGE, [P_RESTE, P_CONSERVE, P_LITRE], pos=0)),
    }
    # ------------------------------------------------ e4-4 : ce qui change, ce qui reste (6e, 5e)
    d["e4-4"] = {
        "lieutenant": tri(
            "Fatou fait fondre un bloc de glace de 1 kg dans une casserole fermée. Range chaque carte, puis choisis la phrase de la fiche qui justifie la colonne « Ce qui reste ».",
            [("change", "Ce qui change"), ("reste", "Ce qui reste pareil")],
            [("l'état : solide puis liquide", "change"), ("la forme : celle du bloc, puis celle de la casserole", "change"), ("le volume", "change"),
             ("la masse : 1 kg", "reste"), ("la matière : c'est toujours de l'eau", "reste")],
            ["La balance donne la même masse avant et après.", "L'eau liquide prend la forme de la casserole.", "Pour la justification : cherche « Ce qui reste »."],
            J("Quelle phrase de la fiche justifie la colonne « Ce qui reste pareil » ?", P_RESTE, [P_CHANGE, P_MESURE, P_FLOTTE], pos=1)),
        "second": qcm(
            carnet("Carnet de Fatou", "(expériences inventées pour le jeu). Lundi : 4 glaçons de 25 g dans un bol fermé : 100 g ; une heure plus tard, de l'eau liquide : 100 g. Mardi : un bol ouvert de 100 g d'eau, laissé au soleil : 92 g le soir.")
            + "Réponds aux trois questions à partir du carnet et de la fiche.",
            [("Lundi, pourquoi la masse n'a-t-elle pas changé ?", ["La glace et l'eau ont la même masse, car la matière n'a pas disparu", "La balance n'est pas assez précise",
              "La glace pèse moins que l'eau", "Il faisait froid"], 0, "La masse se conserve."),
             ("Mardi, où sont passés les 8 g manquants ?", ["Ils ont disparu", "Dans l'air, sous forme de vapeur", "Dans la balance", "Ils sont devenus de la glace"], 1, "Bol ouvert : l'eau s'est évaporée."),
             ("Quelle expérience permet de vérifier que la masse se conserve ?", ["Celle de lundi", "Celle de mardi", "Les deux", "Aucune"], 0, "Il faut un récipient fermé.")],
            ["Compare : bol fermé le lundi, bol ouvert le mardi.", "100 − 92 = 8 g sont partis quelque part.", "Une expérience de conservation se fait sans rien perdre."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", P_FERME, [P_CONSERVE, P_MESURE, P_BOUTEILLE], pos=2)),
    }
    return d
