"""Salle 5 « La galerie du phare » : grades mousse, lieutenant, second (fiche : lune)."""
from aide import *

FICHE = "« Les phases de la Lune »"
OBJET = "La Lune n'est pas une source de lumière : c'est un objet éclairé, qui renvoie la lumière du Soleil."
MOITIE = "Comme une balle éclairée par une lampe, elle a toujours une moitié éclairée et une moitié dans l'ombre."
PHASES = "Selon sa position, nous voyons une partie plus ou moins grande de sa moitié éclairée : ce sont les phases."
ECLIPSE = "Ce n'est pas l'ombre de la Terre qui la cache (cela, c'est une éclipse, un phénomène rare)."
ORDRE = ("Depuis la France, on observe : la nouvelle lune, presque invisible ; le premier croissant, éclairé à droite ; le premier quartier, "
         "moitié droite éclairée ; la Lune gibbeuse ; la pleine lune, environ 15 jours après la nouvelle lune ; puis la partie éclairée diminue : "
         "dernier quartier (moitié gauche), dernier croissant, et de nouveau la nouvelle lune.")
LUNAISON = "D'une nouvelle lune à la suivante, il s'écoule environ 29 jours et demi (29,53 jours) : c'est une lunaison."
MORSE = "Avec le code Morse, une lampe envoie des éclats courts et longs qui forment des lettres."
SIGNAUX = "La lumière transporte aussi des informations."
RYTHME = "Chaque phare a son propre rythme d'éclats : la nuit, les marins le reconnaissent."
CYCLE = "En dessinant la Lune chaque soir pendant deux lunaisons, on constate que le cycle se répète."


def donnees(svg, bloc):
    d = {}
    mat = bloc("e5-1", "matelot")["items"]
    tim = bloc("e5-1", "timonier")["items"]
    # ---------------------------------------------------------------- e5-1 : le carnet de la Lune
    d["e5-1"] = {
        "mousse": ordre(
            "La capitaine Yasmine dessine la Lune tous les soirs. Range ces trois phases dans l'ordre, en commençant par la nouvelle lune (en haut). Utilise les flèches ▲ et ▼, puis vérifie.",
            [(mat[0]["txt"], mat[0]["sous"]), (mat[1]["txt"], mat[1]["sous"]), (mat[2]["txt"], mat[2]["sous"])],
            ["Ouvre la fiche " + FICHE + " dans la Bibliothèque.", "Après la nouvelle lune, la partie éclairée grandit.", "La pleine lune arrive après le premier quartier."]),
        "lieutenant": ordre(
            "La capitaine Yasmine a dessiné la Lune quatre soirs, depuis la France, mais les noms sont effacés. Range les dessins dans l'ordre d'une lunaison, en commençant par la nouvelle lune (en haut), puis choisis la phrase de la fiche qui donne l'ordre des phases.",
            [(tim[0]["txt"], tim[0]["sous"]), (tim[2]["txt"], tim[2]["sous"]), (tim[3]["txt"], tim[3]["sous"]), (tim[5]["txt"], tim[5]["sous"])],
            ["La nouvelle lune est presque invisible.", "La partie éclairée grandit à droite, puis diminue : il ne reste que la gauche.", "Le dernier dessin est le mince croissant éclairé à gauche."],
            J("Quelle phrase de la fiche donne l'ordre des phases, vues depuis la France ?", ORDRE, [PHASES, LUNAISON, MOITIE], pos=1)),
        "second": ordre(
            "Yasmine note les phases et le nombre de jours écoulés depuis la nouvelle lune. Remets ces cinq étapes dans l'ordre de la lunaison, puis choisis la phrase de la fiche qui donne le moment de la pleine lune.",
            ["Nouvelle lune : la Lune est presque invisible (jour 0).", "Premier quartier : la moitié droite est éclairée (environ 7 jours plus tard).",
             "Pleine lune : tout le disque est éclairé (environ 15 jours après la nouvelle lune).", "Dernier quartier : la moitié gauche est éclairée (environ 22 jours après la nouvelle lune).",
             "Nouvelle lune suivante (environ 29 jours et demi après la première)."],
            ["Compte les jours : 0, 7, 15, 22, 29 et demi.", "La partie éclairée grandit jusqu'à la pleine lune, puis diminue.", "Le cycle recommence à la nouvelle lune suivante."],
            J("Quelle phrase de la fiche donne le moment de la pleine lune ?", ORDRE, [LUNAISON, PHASES, CYCLE], pos=2)),
    }
    # ---------------------------------------------------------------- e5-2 : les mots de la capitaine
    d["e5-2"] = {
        "mousse": assoc(
            "Relie chaque phase de la Lune à ce que l'on voit dans le ciel. Clique sur une phase, puis sur sa description.",
            [("la nouvelle lune", "on ne la voit presque pas"), ("la pleine lune", "on voit tout le disque éclairé"), ("le premier quartier", "on voit la moitié droite éclairée")],
            ["Ouvre la fiche " + FICHE + ".", "« Pleine » veut dire « complète ».", "La nouvelle lune est presque invisible."]),
        "lieutenant": qcm(
            "<div class='doc-carnet'><b>Carnet de Yasmine</b> (inventé pour le jeu). Mardi soir, depuis la France : un mince croissant de Lune, éclairé à droite, juste après le coucher du Soleil.</div>Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Dans les jours qui viennent, la partie éclairée visible va…", ["grandir", "diminuer", "rester identique", "disparaître aussitôt"], 0, "Après le premier croissant, la partie éclairée grandit."),
             ("Pourquoi voit-on seulement un croissant et pas toute la Lune ?", ["Parce que, vue d'ici, seule une petite partie de la moitié éclairée est tournée vers nous",
                                                                                  "Parce que l'ombre de la Terre cache le reste", "Parce que la Lune est éteinte aux trois quarts", "Parce qu'un nuage la recouvre toujours"], 0, "Nous voyons une partie plus ou moins grande de la moitié éclairée."),
             ("Quelle phase vient après le premier quartier ?", ["La pleine lune, en passant par la Lune gibbeuse", "La nouvelle lune", "Le premier croissant", "Le dernier quartier tout de suite"], 0, "Après le premier quartier, la partie éclairée grandit encore.")],
            ["Le croissant éclairé à droite est le début du cycle.", "La Lune a toujours une moitié éclairée ; on n'en voit qu'une partie.", "Après le premier quartier, la partie éclairée grandit encore."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", PHASES, [ECLIPSE, OBJET, LUNAISON], pos=0)),
        "second": qcm(
            "<div class='doc-carnet'><b>Carnet de bord de Yasmine</b> (inventé pour le jeu). Lundi 1er : mince croissant éclairé à droite, juste après le coucher du Soleil. Dimanche 7 : la moitié droite est éclairée, c'est le premier quartier. Dimanche 14 : pleine lune.</div>Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("Combien de jours séparent le premier quartier de la pleine lune ?", ["7 jours", "14 jours", "1 jour", "29 jours"], 0, "Du dimanche 7 au dimanche 14 : 7 jours."),
             ("Le dimanche 14, quelle est la partie éclairée visible ?", ["Tout le disque", "La moitié gauche", "La moitié droite", "Un mince croissant"], 0, "C'est la pleine lune."),
             ("La prochaine nouvelle lune aura lieu environ…", ["15 jours après la pleine lune", "1 jour après la pleine lune", "7 jours après la pleine lune", "29 jours après la pleine lune"], 0, "La lunaison dure environ 29 jours et demi : après la pleine lune, il reste environ 15 jours.")],
            ["Du dimanche 7 au dimanche 14, compte les jours.", "À la pleine lune, on voit tout le disque éclairé.", "Une lunaison dure environ 29 jours et demi ; la pleine lune est au milieu."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", LUNAISON, [CYCLE, ORDRE, PHASES], pos=1)),
    }
    # ---------------------------------------------------------------- e5-3 : le message lumineux
    ENTETE = "Le bateau de la capitaine, <i>La Mouette</i>, répond au phare avec sa lampe à signaux. Un éclat court s'écrit •, un éclat long s'écrit —. "
    d["e5-3"] = {
        "mousse": code(
            ENTETE + "Décode le mot avec le tableau, puis écris-le dans le cadenas." + morse(["NUIT"], "NUITES"),
            [("Le mot décodé", "NUIT", 4, False)],
            ["Le message a 4 lettres, séparées par de grands espaces.", "La première lettre est — • : c'est le N.", "La dernière lettre est un seul éclat long : le T."]),
        "lieutenant": code(
            ENTETE + "Décode le mot avec le tableau (attention, il contient des lettres inutiles), puis ouvre le cadenas." + morse(["PHASE"], "PHASELN"),
            [("Le mot décodé", "PHASE", 5, False)],
            ["Le message a 5 lettres.", "Quatre éclats courts, c'est le H.", "La dernière lettre est un seul éclat court : le E."],
            J("Quelle phrase de la fiche explique comment ce message est fait ?", MORSE, [SIGNAUX, RYTHME, "Pour voir un objet, il faut que de la lumière parte de cet objet et entre dans notre œil."], pos=1)),
        "second": code(
            ENTETE + "Décode le mot avec le tableau (attention, il contient des lettres inutiles), puis ouvre le cadenas." + morse(["QUARTIER"], "QUARTIELNS"),
            [("Le mot décodé", "QUARTIER", 8, False)],
            ["Le message a 8 lettres.", "La première lettre est — — • — : le Q.", "Le mot est le nom des deux phases où l'on voit la moitié du disque éclairée."],
            J("Quelle phrase de la fiche explique comment ce message est fait ?", MORSE, [SIGNAUX, RYTHME, "Pour voir un objet, il faut que de la lumière parte de cet objet et entre dans notre œil."], pos=0)),
    }
    # ---------------------------------------------------------------- e5-4 : le journal de bord (timonier, lieutenant, second)
    d["e5-4"] = {
        "lieutenant": vf(
            "La capitaine a noté cinq phrases dans son journal de bord. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui montre que la Lune a toujours une moitié éclairée.",
            [("La Lune est un objet éclairé : elle renvoie la lumière du Soleil.", True, "Ce n'est pas une source."),
             ("La Lune a toujours une moitié éclairée.", True, "Comme une balle éclairée par une lampe."),
             ("Les phases dépendent de la position de la Lune autour de la Terre.", True, "Nous voyons une partie plus ou moins grande de la moitié éclairée."),
             ("La pleine lune arrive environ 15 jours après la nouvelle lune.", True, "C'est le milieu de la lunaison."),
             ("Le dernier quartier est éclairé sur sa moitié droite.", False, "Il est éclairé sur sa moitié gauche.")],
            ["La Lune est comme une balle éclairée par une lampe.", "Le premier quartier est à droite, le dernier à gauche.", "Pour la justification : cherche la phrase qui parle de la balle."],
            J("Quelle phrase de la fiche montre que la Lune a toujours une moitié éclairée ?", MOITIE, [OBJET, PHASES, ORDRE], pos=0)),
        "second": vf(
            "La capitaine a noté six phrases dans son journal de bord. Pour chacune, réponds « Vrai » ou « Faux ». Attention aux idées répandues. Puis choisis la phrase de la fiche qui corrige l'idée « les phases viennent de l'ombre de la Terre ».",
            [("Les phases de la Lune sont dues à l'ombre de la Terre.", False, "Une éclipse est un phénomène rare, différent des phases."),
             ("Une éclipse est un phénomène rare, différent des phases de chaque mois.", True, "Les phases reviennent chaque lunaison."),
             ("Une lunaison dure environ 29 jours et demi.", True, "D'une nouvelle lune à la suivante."),
             ("Après la pleine lune, la partie éclairée visible diminue.", True, "On passe au dernier quartier, puis au dernier croissant."),
             ("En France, un premier croissant est éclairé à gauche.", False, "Il est éclairé à droite."),
             ("En dessinant la Lune chaque soir pendant deux lunaisons, on constate que le cycle se répète.", True, "C'est une observation à la portée d'une classe.")],
            ["Une éclipse n'arrive pas chaque mois.", "Le croissant du début est à droite, depuis la France.", "Après la pleine lune, tout recommence en sens inverse."],
            J("Quelle phrase de la fiche corrige l'idée « les phases viennent de l'ombre de la Terre » ?", ECLIPSE, [PHASES, OBJET, LUNAISON], pos=1)),
    }
    return d
