"""Salle 3 « La chambre aux ombres » : grades mousse, lieutenant, second (fiche : ombres)."""
from aide import *

FICHE = "« Ombre propre, ombre portée »"
NAIT = "Une ombre se forme quand un objet opaque arrête une partie de la lumière d'une source."
DROITE = "Comme la lumière va en ligne droite, elle ne peut pas contourner l'objet : derrière lui reste une zone non éclairée."
TRANSP = "Un objet transparent, lui, ne donne presque pas d'ombre."
PROPRE = "Sur l'objet, la partie tournée vers la source est éclairée ; l'autre partie, non éclairée, est son ombre propre."
PORTEE = "Sur le sol, un mur ou un écran, la tache sombre dessinée par l'objet est son ombre portée."
ALIGNES = "La source, l'objet et l'ombre portée sont alignés : l'objet est entre la source et l'ombre, et l'ombre se forme à l'opposé de la source."
GAUCHE = "Si la source se déplace vers la gauche, l'ombre portée part vers la droite."
UN_SEUL = "Pour la faire varier, on déplace un seul élément à la fois (l'écran, la source ou l'objet) et on garde les deux autres immobiles."
PROCHE = "Plus l'objet est proche de la source, plus son ombre portée est grande."
MILIEU = "Placé à mi-distance entre la source et l'écran, il donne une ombre deux fois plus grande que lui."


def donnees(svg, bloc=None):
    d = {}
    fig = svg("e3-1", "timonier")
    # ---------------------------------------------------------------- e3-1 : le schéma de Nils
    d["e3-1"] = {
        "mousse": assoc(
            "Nils a éclairé une balle avec une lampe, devant un écran blanc. Regarde le schéma, puis relie chaque mot à ce qu'il désigne. Clique sur un mot, puis sur sa description.\n" + svg("e3-1", "matelot"),
            [("la source de lumière", "la lampe allumée"), ("l'ombre portée", "la tache sombre sur l'écran"), ("l'ombre propre", "le côté sombre de la balle")],
            ["Ouvre la fiche " + FICHE + " dans la Bibliothèque.", "L'ombre portée est loin de l'objet, sur l'écran.", "L'ombre propre est sur l'objet lui-même."]),
        "lieutenant": qcm(
            "Nils a éclairé une balle avec une lampe, devant un écran blanc. Regarde son schéma (repères 1 à 4), réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2." + fig,
            [("Que désigne le repère 2, sur la balle ?", ["La partie de la balle qui n'est pas éclairée : l'ombre propre", "L'ombre portée", "La source de lumière", "L'écran"], 0, "L'ombre propre est sur l'objet."),
             ("Nils déplace la lampe vers la gauche. Dans quel sens l'ombre portée se déplace-t-elle ?", ["Vers la droite", "Vers la gauche", "Elle ne bouge pas", "Elle disparaît"], 0, "L'ombre est à l'opposé de la source."),
             ("Pourquoi la lumière ne contourne-t-elle pas la balle ?", ["Parce qu'elle va en ligne droite", "Parce que la balle est transparente", "Parce que la lampe est trop faible", "Parce qu'elle va en zigzag"], 0, "La lumière se propage en ligne droite.")],
            ["Le repère 2 est sur l'objet lui-même, pas sur l'écran.", "L'ombre est à l'opposé de la source.", "La lumière va en ligne droite : elle ne peut pas contourner l'objet."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", GAUCHE, [PROPRE, MILIEU, PORTEE], pos=2)),
        "second": assoc(
            "Nils a préparé des expériences. Relie chaque action à ce que tu observes sur l'écran, puis choisis la phrase de la fiche qui explique la dernière paire (lampe déplacée sur le côté).",
            [("J'approche la lampe de la balle (l'écran ne bouge pas)", "l'ombre portée devient plus grande"),
             ("J'éloigne la lampe de la balle (l'écran ne bouge pas)", "l'ombre portée devient plus petite"),
             ("Je remplace la balle opaque par une vitre claire", "on ne voit presque plus d'ombre"),
             ("Je déplace la lampe vers la gauche", "l'ombre portée part vers la droite")],
            ["Pense à une lampe qu'on approche d'une main : l'ombre grandit.", "Une vitre claire laisse passer presque toute la lumière.", "L'ombre est à l'opposé de la source."],
            J("Quelle phrase de la fiche explique la dernière paire ?", GAUCHE, [PROCHE, TRANSP, UN_SEUL], pos=1)),
    }
    # ---------------------------------------------------------------- e3-2 : les affirmations de Nils
    d["e3-2"] = {
        "mousse": vf(
            "Nils fait trois affirmations sur les ombres. Pour chacune, clique sur « Vrai » ou sur « Faux », puis vérifie.",
            [("Pour avoir une ombre, il faut de la lumière.", True, "Sans lumière, pas d'ombre."),
             ("L'ombre est du même côté que la lampe.", False, "L'ombre est à l'opposé de la lampe."),
             ("Une planche de bois donne une ombre.", True, "Elle arrête la lumière.")],
            ["Ouvre la fiche " + FICHE + ".", "L'ombre se forme derrière l'objet, loin de la lampe.", "Le bois ne laisse pas passer la lumière."]),
        "lieutenant": vf(
            "Nils a écrit cinq affirmations dans son carnet. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui explique pourquoi la lumière ne contourne pas l'objet.",
            [("Une ombre se forme quand un objet opaque arrête une partie de la lumière.", True, "C'est la définition de l'ombre."),
             ("Un objet transparent donne une ombre aussi noire qu'un objet opaque.", False, "Un objet transparent ne donne presque pas d'ombre."),
             ("L'ombre propre se trouve sur l'écran.", False, "Elle est sur l'objet ; sur l'écran, c'est l'ombre portée."),
             ("La source, l'objet et l'ombre portée sont alignés.", True, "L'objet est entre la source et l'ombre."),
             ("Si la lampe est à gauche de la balle, l'ombre portée est à gauche de la balle.", False, "Elle est à droite, à l'opposé de la source.")],
            ["Pour une ombre, il faut une source et un objet qui arrête la lumière.", "L'ombre propre est sur l'objet ; l'ombre portée est sur l'écran.", "Pour la justification : cherche la phrase qui parle de la ligne droite."],
            J("Quelle phrase de la fiche explique pourquoi la lumière ne contourne pas l'objet ?", DROITE, [NAIT, ALIGNES, TRANSP], pos=0)),
        "second": qcm(
            "<div class='doc-carnet'><b>Cahier d'expériences de Nils</b> (inventé pour le jeu). Nils veut savoir si la distance entre la lampe et la figurine change la taille de l'ombre portée. Il hésite entre trois montages.<br>A : il déplace la lampe ET l'écran.<br>B : il déplace seulement la lampe ; figurine et écran ne bougent pas.<br>C : il remplace la figurine par une plus grande, et déplace l'écran.</div>Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 1.",
            [("Quel montage permet d'étudier l'effet de la distance de la lampe ?", ["Le montage B", "Le montage A", "Le montage C", "Aucun des trois"], 0, "On ne change qu'un seul élément à la fois."),
             ("Dans le montage B, on rapproche la lampe de la figurine. L'ombre portée…", ["devient plus grande", "devient plus petite", "reste de la même taille", "change de couleur"], 0, "Plus l'objet est proche de la source, plus l'ombre est grande."),
             ("Pourquoi le montage C ne permet-il pas de conclure ?", ["Parce que plusieurs éléments changent en même temps", "Parce que la figurine est trop grande", "Parce qu'il n'y a pas d'écran", "Parce que la lampe est éteinte"], 0, "On ne saurait pas lequel des changements agit.")],
            ["Une expérience juste ne change qu'un seul élément.", "Rapproche ta main de la lampe : son ombre grossit.", "Si deux choses changent à la fois, on ne sait pas laquelle agit."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 1 ?", UN_SEUL, [PROCHE, MILIEU, ALIGNES], pos=2)),
    }
    # ---------------------------------------------------------------- e3-3 : le théâtre d'ombres
    d["e3-3"] = {
        "mousse": ordre(
            "Nils fait un théâtre d'ombres. La lampe et l'écran ne bougent pas ; Nils déplace seulement la figurine du bateau. Range les essais de la plus petite ombre (en haut) à la plus grande (en bas). Utilise les flèches ▲ et ▼, puis vérifie.",
            ["La figurine est collée contre l'écran.", "La figurine est entre la lampe et l'écran, à mi-chemin.", "La figurine est tout près de la lampe."],
            ["Ouvre la fiche " + FICHE + ".", "Plus la figurine est près de la lampe, plus l'ombre est grande.", "Contre l'écran, l'ombre a presque la taille de la figurine."]),
        "lieutenant": ordre(
            "Nils fait quatre essais, en ne changeant que la distance entre la lampe et la figurine (l'écran est toujours à 1 m de la lampe). Range-les de la plus petite ombre (en haut) à la plus grande (en bas), puis choisis la phrase de la fiche qui justifie le classement.",
            ["La figurine est à 90 cm de la lampe.", "La figurine est à 70 cm de la lampe.", "La figurine est à 40 cm de la lampe.", "La figurine est à 25 cm de la lampe."],
            ["Plus la figurine est près de la lampe, plus l'ombre est grande.", "90 cm : presque contre l'écran. 25 cm : tout près de la lampe.", "Compare les distances à la lampe, pas à l'écran."],
            J("Quelle phrase de la fiche justifie le classement ?", PROCHE, [MILIEU, UN_SEUL, GAUCHE], pos=3)),
        "second": ordre(
            "Nils étudie l'ombre d'une figurine de 10 cm. L'écran est toujours à 1 m de la lampe. Range les quatre essais de la plus petite ombre (en haut) à la plus grande (en bas), puis choisis la phrase de la fiche qui donne le cas de l'essai à mi-distance.",
            ["La figurine est à 80 cm de la lampe.", "La figurine est à 50 cm de la lampe (à mi-distance).", "La figurine est à 25 cm de la lampe.", "La figurine est à 20 cm de la lampe."],
            ["Plus la figurine est près de la lampe, plus l'ombre est grande.", "À mi-distance, l'ombre est deux fois plus grande que la figurine : 20 cm.", "À 20 cm de la lampe, l'ombre est cinq fois plus grande."],
            J("Quelle phrase de la fiche donne le cas de l'essai à mi-distance ?", MILIEU, [PROCHE, UN_SEUL, ALIGNES], pos=0)),
    }
    # ---------------------------------------------------------------- e3-4 : la boîte à ombres (timonier, lieutenant, second)
    d["e3-4"] = {
        "lieutenant": code(
            "Nils place une figurine de bateau de 12 cm à mi-distance entre la lampe et l'écran. Quelle est la hauteur de son ombre portée sur l'écran ? Puis, quelle est la différence avec la hauteur de la figurine ? Écris les deux nombres (en cm) pour ouvrir le cadenas. Aide-toi de la fiche.",
            [("Hauteur de l'ombre (cm)", "24", 2), ("Différence avec la figurine (cm)", "12", 2)],
            ["À mi-distance, l'ombre est deux fois plus grande que l'objet.", "Deux fois 12 cm, cela fait 24 cm.", "24 cm moins 12 cm : la différence est de 12 cm."],
            J("Quelle phrase de la fiche donne la règle utilisée ?", MILIEU, [PROCHE, UN_SEUL, GAUCHE], pos=1)),
        "second": lettres(
            "Trouve le mot qui manque : « Un objet qui arrête la lumière est … ». Ses lettres sont cachées en couleur dans le mot de Nils, dans le désordre. Clique-les dans l'ordre qui forme le mot (6 lettres). Deux lettres sont des pièges.",
            ["O", "P", "A", "Q", "U", "E"],
            "Ce soir, Nils range la <b data-l='P'>p</b>etite lamp<b data-l='E'>e</b> et le p<b data-l='O'>o</b>t de colle ; il vérifie que le volet <b data-l='Q'>q</b>ui ferme la fenêtre n'a pas de fente. Sur le m<b data-l='U'>u</b>r, <b data-l='A'>a</b>ucune lumière ne passe : <b data-l='T'>t</b>out reste <b data-l='S'>s</b>ombre.",
            ["Ce n'est ni « transparent » ni « translucide ».", "Le mot commence par O.", "C'est le contraire de « transparent » : il se termine par E."],
            J("Quelle phrase de la fiche définit la propriété de cet objet ?", NAIT, [TRANSP, PROPRE, PORTEE], pos=2)),
    }
    return d
