"""Salle 4 « La cour du cadran solaire » : grades mousse, lieutenant, second (fiche : soleil)."""
from aide import *

FICHE = "« L'ombre d'un bâton au fil de la journée »"
TRAJET = "Depuis la cour de récréation, le Soleil semble se déplacer dans le ciel : il se lève du côté de l'est, monte jusqu'à son point le plus haut, du côté du sud, puis redescend et se couche du côté de l'ouest."
MIDI = "Le moment où il est le plus haut s'appelle le midi solaire."
OPPOSE = "Le Soleil est la source, le bâton est l'objet opaque : l'ombre portée est donc toujours à l'opposé du Soleil."
OMBRE = "Le matin, elle est longue et tournée vers l'ouest. Elle raccourcit jusqu'au midi solaire, où elle est la plus courte et tournée vers le nord. L'après-midi, elle s'allonge vers l'est. Plus le Soleil est haut, plus l'ombre est courte."
MONTRE = "En France, l'ombre la plus courte n'arrive pas à 12 h à nos montres : en été, c'est plutôt vers 14 h."
APPARENT = "Ce mouvement n'est qu'apparent : c'est la Terre qui tourne sur elle-même."


def donnees(svg, bloc=None):
    d = {}
    # ---------------------------------------------------------------- e4-1 : les photos d'Achille
    d["e4-1"] = {
        "mousse": ordre(
            "Achille a photographié l'ombre d'un bâton trois fois dans la même journée ensoleillée. Range ses photos du matin (en haut) au soir (en bas). Utilise les flèches ▲ et ▼, puis vérifie.",
            ["Le matin : l'ombre est longue.", "Au milieu de la journée : l'ombre est très courte.", "Le soir : l'ombre est de nouveau longue."],
            ["Ouvre la fiche " + FICHE + " dans la Bibliothèque.", "Quand le Soleil est haut dans le ciel, l'ombre est courte.", "Le Soleil est bas le matin et le soir."]),
        "lieutenant": ordre(
            "Achille décrit le trajet du Soleil dans la cour. Remets ses cinq observations dans l'ordre de la journée, puis choisis la phrase de la fiche qui décrit ce trajet.",
            ["Le Soleil se lève du côté de l'est.", "Le Soleil monte dans le ciel : l'ombre du bâton raccourcit.",
             "Midi solaire : le Soleil est au plus haut, au sud ; l'ombre est la plus courte, tournée vers le nord.",
             "Le Soleil descend vers l'ouest : l'ombre s'allonge vers l'est.", "Le Soleil se couche du côté de l'ouest : l'ombre est très longue."],
            ["Le Soleil se lève à l'est et se couche à l'ouest.", "L'ombre raccourcit tant que le Soleil monte.", "Au midi solaire, le Soleil est le plus haut."],
            J("Quelle phrase de la fiche décrit le trajet du Soleil ?", TRAJET, [OMBRE, MIDI, APPARENT], pos=0)),
        "second": qcm(
            "<div class='doc-carnet'><b>Notice du cadran solaire</b> (inventée pour le jeu). « Un cadran solaire indique l'heure grâce à l'ombre d'une tige, le gnomon. Dans la cour, la tige est plantée au centre du cadran. »</div>Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Qu'est-ce qui indique l'heure sur un cadran solaire ?", ["L'ombre de la tige", "La lumière de la lampe", "La couleur du ciel", "La température"], 0, "C'est l'ombre du gnomon."),
             ("Pourquoi l'ombre la plus courte n'arrive-t-elle pas à 12 h à nos montres, en France, en été ?", [
                 "Parce que nos montres ne donnent pas l'heure du Soleil : le midi solaire arrive plutôt vers 14 h", "Parce que le gnomon rétrécit à midi", "Parce que le Soleil s'arrête de bouger à 12 h", "Parce que l'ombre est à l'opposé de la montre"], 0, "L'heure de nos montres n'est pas l'heure du Soleil."),
             ("Dans la cour, une ombre est tournée vers le nord-est. De quel côté est le Soleil ?", ["Au sud-ouest", "Au nord-est", "Au sud-est", "Au nord-ouest"], 0, "L'ombre est à l'opposé du Soleil.")],
            ["Le gnomon est la tige dont on observe l'ombre.", "L'heure de nos montres n'est pas celle du Soleil.", "L'opposé du nord-est est le sud-ouest."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", MONTRE, [MIDI, TRAJET, OMBRE], pos=2)),
    }
    # ---------------------------------------------------------------- e4-2 : questions de l'horloger
    d["e4-2"] = {
        "mousse": qcm(
            "Achille te pose une question. Clique sur la bonne réponse, puis vérifie.",
            [("Le Soleil est haut dans le ciel. L'ombre du bâton est…", ["très courte", "très longue", "toujours de la même taille", "absente"], 0, "Plus le Soleil est haut, plus l'ombre est courte.")],
            ["Ouvre la fiche " + FICHE + ".", "Quand le Soleil est bas, l'ombre est longue.", "Quand le Soleil est haut, c'est l'inverse."]),
        "lieutenant": vf(
            "Achille a noté cinq affirmations dans son registre. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui définit le midi solaire.",
            [("Le matin, l'ombre du bâton est tournée vers l'ouest.", True, "L'ombre est à l'opposé du Soleil, qui est à l'est."),
             ("Au midi solaire, l'ombre est la plus longue de la journée.", False, "Elle est la plus courte."),
             ("En France, au midi solaire, l'ombre est tournée vers le nord.", True, "Le Soleil est au sud."),
             ("L'ombre du bâton reste immobile toute la journée.", False, "Elle tourne et change de longueur."),
             ("Le Soleil semble se déplacer parce que la Terre tourne sur elle-même.", True, "Son mouvement n'est qu'apparent.")],
            ["L'ombre est toujours à l'opposé du Soleil.", "Plus le Soleil est haut, plus l'ombre est courte.", "Le midi solaire, c'est le moment où le Soleil est le plus haut."],
            J("Quelle phrase de la fiche définit le midi solaire ?", MIDI, [APPARENT, OMBRE, MONTRE], pos=1)),
        "second": tri(
            "Achille classe des observations d'ombres faites dans la même journée. Range chaque observation dans la bonne colonne, puis choisis la phrase de la fiche qui décrit le trajet de l'ombre.",
            [("matin", "Avant le midi solaire"), ("apres", "Après le midi solaire")],
            [("L'ombre est tournée vers l'ouest.", "matin"), ("L'ombre est tournée vers le nord-ouest.", "matin"), ("L'ombre raccourcit d'une heure à l'autre.", "matin"),
             ("L'ombre est tournée vers l'est.", "apres"), ("L'ombre est tournée vers le nord-est.", "apres"), ("L'ombre s'allonge d'une heure à l'autre.", "apres")],
            ["Le matin, l'ombre part vers l'ouest.", "L'ombre tourne de l'ouest vers l'est en passant par le nord.", "Elle raccourcit jusqu'au midi solaire, puis s'allonge."],
            J("Quelle phrase de la fiche décrit le trajet de l'ombre au fil de la journée ?", OMBRE, [TRAJET, MIDI, OPPOSE], pos=3)),
    }
    # ---------------------------------------------------------------- e4-3 : le plan de la cour
    d["e4-3"] = {
        "mousse": assoc(
            "Achille a dessiné trois ombres du même bâton, vue de dessus. Regarde le plan, puis relie chaque moment à ce que tu vois. Clique sur un moment, puis sur sa description.\n" + svg("e4-3", "matelot"),
            [("le matin", "l'ombre est longue, du côté de l'ouest"), ("au midi solaire", "l'ombre est la plus courte"), ("le soir", "l'ombre est longue, du côté de l'est")],
            ["Ouvre la fiche " + FICHE + ".", "L'ombre est à l'opposé du Soleil.", "L'ombre la plus courte est celle de midi solaire."]),
        "lieutenant": qcm(
            "Achille a dessiné la cour vue de dessus, avec quatre ombres du même bâton (repères 1 à 4). Le nord est en haut. Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2." + svg("e4-3", "timonier"),
            [("Quel repère montre l'ombre la plus courte ?", ["Le repère 3", "Le repère 1", "Le repère 2", "Le repère 4"], 0, "Le Soleil est alors le plus haut : c'est le midi solaire."),
             ("Le repère 1 est l'ombre la plus longue, tournée vers l'ouest. Où est le Soleil à ce moment ?", ["Du côté de l'est", "Du côté de l'ouest", "Du côté du nord", "Juste au-dessus du bâton"], 0, "L'ombre est à l'opposé du Soleil."),
             ("Pourquoi les ombres changent-elles de longueur dans la journée ?", ["Parce que la hauteur du Soleil dans le ciel change", "Parce que le bâton grandit", "Parce que la cour penche", "Parce que le vent pousse l'ombre"], 0, "Plus le Soleil est haut, plus l'ombre est courte.")],
            ["Cherche l'ombre dont le trait est le plus court.", "Le Soleil et l'ombre sont de côtés opposés.", "Plus le Soleil est haut, plus l'ombre est courte."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", OPPOSE, [MIDI, TRAJET, APPARENT], pos=1)),
        "second": vf(
            "Achille a dessiné la cour vue de dessus, avec trois ombres du même bâton. Le nord est en haut. Pour chaque affirmation, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui contredit l'idée « le midi solaire est à 12 h ».\n" + svg("e4-3", "matelot"),
            [("L'ombre du repère 2 est la plus courte de la journée.", True, "C'est l'ombre du midi solaire."),
             ("L'ombre du repère 1 a été dessinée le matin.", True, "Elle est tournée vers l'ouest."),
             ("Au repère 1, le Soleil est du côté de l'est.", True, "L'ombre est à l'opposé du Soleil."),
             ("Au repère 3, l'ombre est tournée vers l'ouest.", False, "Elle est tournée vers l'est."),
             ("Au repère 2, le Soleil est au sud.", True, "Il est au plus haut, au sud."),
             ("En France, l'ombre du repère 2 apparaît toujours à 12 h à nos montres.", False, "Pas à 12 h : en été, plutôt vers 14 h.")],
            ["L'ombre est à l'opposé du Soleil.", "L'ombre du midi solaire est la plus courte, tournée vers le nord.", "L'heure des montres n'est pas l'heure du Soleil."],
            J("Quelle phrase de la fiche contredit l'idée « le midi solaire est à 12 h » ?", MONTRE, [MIDI, OMBRE, TRAJET], pos=2)),
    }
    # ---------------------------------------------------------------- e4-4 : le carnet de l'été (timonier, lieutenant, second)
    tab = lambda lignes: ("<table class=\"tableau-releves\"><tr><th>Heure (à la montre)</th><th>Longueur de l'ombre du bâton</th></tr>"
                          + "".join(f"<tr><td>{h}</td><td>{l}</td></tr>" for h, l in lignes) + "</table>")
    d["e4-4"] = {
        "lieutenant": code(
            "Achille a relevé l'ombre d'un bâton de 1 m, un autre jour.<div class=\"doc-titre\"><i>Relevé d'Achille, bâton de 1 m (valeurs fictives)</i></div>"
            + tab([("9 h", "135 cm"), ("11 h", "71 cm"), ("13 h", "52 cm"), ("15 h", "66 cm"), ("17 h", "128 cm")])
            + "<p class=\"question-doc\"><b>À quelle heure l'ombre était-elle la plus courte ? Quelle est la différence entre l'ombre la plus longue et l'ombre la plus courte ?</b></p>",
            [("Heure (en h)", "13", 2), ("Différence (en cm)", "83", 2)],
            ["Cherche le plus petit nombre de la deuxième colonne.", "Le plus petit nombre est 52 cm, mesuré à 13 h.", "La plus longue est 135 cm : 135 moins 52."],
            J("Quelle phrase de la fiche explique pourquoi l'ombre est la plus courte à ce moment ?", OMBRE, [TRAJET, MIDI, MONTRE], pos=2)),
        "second": code(
            "Achille a relevé l'ombre d'un bâton de 1 m, toutes les deux heures.<div class=\"doc-titre\"><i>Relevé d'Achille, bâton de 1 m (valeurs fictives)</i></div>"
            + tab([("9 h", "190 cm"), ("11 h", "76 cm"), ("13 h", "51 cm"), ("15 h", "58 cm"), ("17 h", "135 cm")])
            + "<p class=\"question-doc\"><b>À quelle heure l'ombre était-elle la plus courte ? Quelle est la différence entre l'ombre de 9 h et celle de 17 h ?</b></p>",
            [("Heure (en h)", "13", 2), ("Différence 9 h et 17 h (en cm)", "55", 2)],
            ["Cherche le plus petit nombre de la deuxième colonne.", "Le plus petit nombre est 51 cm, mesuré à 13 h.", "190 moins 135 : combien reste-t-il ?"],
            J("Quelle phrase de la fiche explique pourquoi le midi solaire n'est pas toujours à midi à la montre ?", MONTRE, [MIDI, OMBRE, APPARENT], pos=0)),
    }
    return d
