"""Salle 5 « Le château d'eau de Ninon » : grades mousse, lieutenant, second (fiche : proprietes)."""
from aide import *

FICHE = "« Les propriétés de la matière et le cycle de l'eau »"
P_TAILLE = "Flotter ou couler : ce n'est pas la taille qui compte, mais la matière."
P_TRONC = "Un gros tronc flotte, une petite pièce coule."
P_LISTE = "Le bois, le liège et la glace flottent sur l'eau ; les métaux, le verre et les pierres coulent."
P_CHALEUR = "Conduire la chaleur : les métaux sont de bons conducteurs de la chaleur ; le bois, le plastique, la laine et l'air la conduisent mal : ce sont des isolants."
P_DISSOUT = "Se dissoudre : le sucre et le sel se dissolvent dans l'eau, ils ne se voient plus mais la masse totale se conserve."
P_FONDRE = "Dissoudre n'est pas fondre : il n'y a pas besoin de chauffer."
P_EVAP = "Chauffée par le Soleil, l'eau des mers, des lacs et des sols s'évapore."
P_NUAGES = "La vapeur invisible monte, se refroidit et se liquéfie en gouttelettes, ou forme de minuscules cristaux de glace : ce sont les nuages."
P_PRECIP = "Les gouttes grossissent et tombent : ce sont les précipitations (pluie, neige, grêle)."
P_RUISS = "L'eau ruisselle vers les rivières ou s'infiltre dans le sol, puis rejoint la mer."


def donnees(svg, bloc=None):
    d = {}
    # ------------------------------------------------ e5-1 : le bassin d'essai
    d["e5-1"] = {
        "mousse": tri(
            "Ninon plonge des objets dans le bassin. Range chaque objet : il flotte ou il coule ?",
            [("flotte", "Il flotte"), ("coule", "Il coule")],
            [("un bouchon en liège", "flotte"), ("un glaçon", "flotte"), ("une clé en fer", "coule"), ("un caillou", "coule")],
            ["Ouvre la fiche " + FICHE + " dans la Bibliothèque.", "Le bois et le liège flottent.", "Le fer et les pierres coulent."]),
        "lieutenant": tri(
            "Ninon prépare le bassin d'essai. Range chaque objet, puis choisis la phrase de la fiche qui explique le piège de la taille.",
            [("flotte", "Il flotte"), ("coule", "Il coule")],
            [("une grosse bûche", "flotte"), ("un iceberg", "flotte"), ("un bouchon en liège", "flotte"), ("une règle en bois", "flotte"),
             ("une petite pièce de monnaie", "coule"), ("un trombone en métal", "coule"), ("une bille en verre", "coule"), ("un petit gravier", "coule")],
            ["Ne regarde pas la taille : regarde la matière.", "Bois, liège, glace d'un côté ; métal, verre, pierre de l'autre.", "Pour la justification : cherche « ce n'est pas la taille »."],
            J("Quelle phrase de la fiche explique le piège de la taille ?", P_TAILLE, [P_DISSOUT, P_CHALEUR, P_NUAGES], pos=2)),
        "second": qcm(
            tableau("Essais de Ninon dans le bassin (inventés pour le jeu)", ["Objet", "Matière", "Taille"],
                    [["A", "bois", "très grand"], ["B", "fer", "très petit"], ["C", "glace", "moyen"], ["D", "verre", "petit"]])
            + "Réponds aux trois questions à partir du tableau et de la fiche.",
            [("Quels objets flottent ?", ["A et C", "B et D", "A seulement", "Tous"], 0, "Le bois et la glace flottent."),
             ("L'objet B coule. Pourquoi ?", ["Parce qu'il est petit", "Parce qu'il est en métal", "Parce qu'il est froid", "Parce qu'il coule toujours au fond du bassin"], 1,
              "C'est la matière qui compte, pas la taille."),
             ("On remplace A par un bout de bois minuscule. Il...", ["coule, car il est petit", "flotte, car il est en bois", "fond", "se dissout"], 1, "La matière n'a pas changé.")],
            ["Pour chaque objet, regarde d'abord la colonne « Matière ».", "Un gros tronc flotte, une petite pièce coule.", "Changer la taille ne change pas la matière."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", P_TAILLE, [P_LISTE, P_FONDRE, P_PRECIP], pos=1)),
    }
    # ------------------------------------------------ e5-2 : les fiches des matériaux
    d["e5-2"] = {
        "mousse": assoc(
            "Ninon range ses fiches. Relie chaque propriété à l'exemple qui la montre.",
            [("conduit bien la chaleur", "la cuillère en métal devient chaude"), ("se dissout dans l'eau", "le sucre ne se voit plus dans l'eau"),
             ("ne se dissout pas", "le sable reste au fond du verre")],
            ["Ouvre la fiche " + FICHE + ".", "Le métal chauffe jusqu'au bout.", "Le sucre disparaît à la vue, le sable non."]),
        "lieutenant": assoc(
            "Ninon range ses fiches de matériaux. Relie chaque propriété à l'expérience qui la montre, puis choisis la phrase de la fiche qui distingue dissoudre et fondre.",
            [("bon conducteur de la chaleur", "la casserole en métal chauffe vite"), ("isolant", "le gant en laine protège de la casserole chaude"),
             ("se dissout dans l'eau", "le sel ne se voit plus, mais l'eau est salée"), ("ne se dissout pas", "le sable se dépose au fond"),
             ("flotte sur l'eau", "le glaçon reste à la surface")],
            ["Un isolant conduit mal la chaleur.", "Le sel ne disparaît pas : on le goûte encore.", "Pour la justification : cherche « pas besoin de chauffer »."],
            J("Quelle phrase de la fiche distingue dissoudre et fondre ?", P_FONDRE, [P_DISSOUT, P_TRONC, P_EVAP], pos=3)),
        "second": tri(
            "Ninon doit choisir les matériaux d'une nouvelle cuve chauffée. Range chaque matériau selon sa propriété, puis choisis la phrase de la fiche qui justifie ton classement.",
            [("conducteur", "Conduit bien la chaleur"), ("isolant", "Conduit mal la chaleur (isolant)")],
            [("le cuivre", "conducteur"), ("l'aluminium", "conducteur"), ("le fer", "conducteur"),
             ("le bois", "isolant"), ("le plastique", "isolant"), ("la laine", "isolant"), ("l'air", "isolant")],
            ["Les métaux d'un côté.", "L'air conduit mal la chaleur : c'est pour cela qu'un pull qui garde de l'air tient chaud.", "Pour la justification : cherche « isolants »."],
            J("Quelle phrase de la fiche justifie ton classement ?", P_CHALEUR, [P_LISTE, P_DISSOUT, P_TAILLE], pos=0)),
    }
    # ------------------------------------------------ e5-3 : le grand voyage de l'eau
    d["e5-3"] = {
        "mousse": ordre(
            "Ninon montre le voyage de l'eau. Remets les quatre étapes dans l'ordre, en partant de la mer (flèches ▲ et ▼).",
            ["Le Soleil chauffe la mer : l'eau s'évapore.", "La vapeur monte et forme un nuage.", "Il pleut.", "La rivière ramène l'eau à la mer."],
            ["Ouvre la fiche " + FICHE + " : cherche « cycle de l'eau ».", "Le Soleil commence le voyage.", "La pluie tombe du nuage."]),
        "lieutenant": ordre(
            "Ninon montre le cycle de l'eau autour de la Fabrique, en partant du lac. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche qui décrit la formation des nuages.",
            ["Chauffée par le Soleil, l'eau du lac s'évapore.", "La vapeur invisible monte et se refroidit.",
             "Elle se liquéfie en gouttelettes : un nuage se forme.", "Les gouttes grossissent et tombent : il pleut.",
             "Une partie de l'eau s'infiltre dans le sol, l'autre ruisselle vers la rivière.", "La rivière rejoint le lac : le cycle recommence."],
            ["La vapeur doit se refroidir pour former des gouttelettes.", "Les précipitations viennent après les nuages.", "Pour la justification : cherche « ce sont les nuages »."],
            J("Quelle phrase de la fiche décrit la formation des nuages ?", P_NUAGES, [P_EVAP, P_PRECIP, P_RUISS], pos=0)),
        "second": ordre(
            "Une goutte de pluie tombe sur la colline, en hiver. Ninon retrace son voyage jusqu'à la tour. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche qui décrit la première étape.",
            ["Chauffée par le Soleil, l'eau de la mer s'évapore.", "La vapeur monte très haut et se refroidit beaucoup.",
             "Elle forme de minuscules cristaux de glace dans le nuage.", "Il fait très froid : la précipitation tombe en neige sur la colline.",
             "Au printemps, la neige fond : c'est la fusion.", "L'eau liquide s'infiltre dans le sol et rejoint la nappe qui alimente la tour."],
            ["La neige vient d'un nuage où il fait très froid.", "La fusion de la neige vient après sa chute.", "Pour la justification : la première étape parle du Soleil."],
            J("Quelle phrase de la fiche décrit la première étape ?", P_EVAP, [P_NUAGES, P_RUISS, P_FONDRE], pos=1)),
    }
    # ------------------------------------------------ e5-4 : le message de la tour (6e, 5e)
    d["e5-4"] = {
        "lieutenant": lettres(
            "Ninon a laissé un message. Des lettres sont marquées : clique dans l'ordre celles qui forment ce que contient un nuage quand il fait très froid. Attention aux lettres pièges. Puis choisis la phrase de la fiche qui le dit.",
            "GLACE",
            marque("Du haut de la tour, je regarde le [n]uage. Il n'est pas fait de vapeur : la vapeur est invisible. Tout en haut, où il fait très froid, "
                   "la vapeur forme de minuscu[l]es [c]ristaux de [g]lace, et [a]ussi des gouttel[e]ttes. Un jour, ils tomberont en neige ou en [p]luie."),
            ["Le mot a cinq lettres.", "Il fait très froid en haut du nuage : l'eau y est solide.", "Pour la justification : cherche « cristaux »."],
            J("Quelle phrase de la fiche dit ce que contient un nuage ?", P_NUAGES, [P_PRECIP, P_EVAP, P_DISSOUT], pos=2)),
        "second": lettres(
            "Dernier message de Ninon. Des lettres sont marquées : clique dans l'ordre celles qui forment l'état de l'eau dans les gouttelettes d'un nuage. Attention aux lettres pièges. Puis choisis la phrase de la fiche qui montre comment l'eau du nuage revient à la mer.",
            "LIQUIDE",
            marque("Mon carnet [d]it vrai : la vapeur ne se voit [p]as. Le nuage blanc est fait d'eau [l]iquide, en gouttelettes, ou de petits cristaux [q]uand il fait très froid. "
                   "Les gouttes grossissent, pu[i]s tombent : c'est la pl[u]ie. Elle [r]uisselle jusqu'aux rivières, s'[i]nfiltre dans le sol, et r[e]joint la mer. [S]i tu as trouvé, bravo !"),
            ["Le mot a sept lettres.", "Une gouttelette n'est ni solide ni gazeuse.", "Pour la justification : cherche « ruisselle »."],
            J("Quelle phrase de la fiche montre comment l'eau du nuage revient à la mer ?", P_RUISS, [P_NUAGES, P_EVAP, P_TAILLE], pos=0)),
    }
    return d
