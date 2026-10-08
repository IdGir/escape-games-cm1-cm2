"""Salle 2 « La salle des menus » (fiche : besoins)."""
from aide import *

F = "« Des besoins qui changent »"
B1 = "L'énergie apportée par les aliments se mesure en kilocalories (kcal)."
B2 = "Les besoins varient selon l'âge, la croissance et l'activité physique."
B3 = "Ordres de grandeur : un enfant de 10 ans a besoin d'environ 1 800 à 2 200 kcal par jour ; un adulte, de 2 000 à 2 700 kcal ; un coureur cycliste un jour d'étape de montagne, environ 6 000 kcal, soit à peu près deux fois plus qu'un jour de repos."
B4 = "Manger équilibré, c'est varier les aliments et adapter les quantités à ses besoins ; il n'y a pas d'aliment interdit."
B5 = "Le corps dépense de l'énergie en permanence, même pendant le sommeil : pour respirer, faire battre le cœur, garder sa température."
B6 = "Un enfant en a besoin en plus pour grandir."
B7 = "Quand les muscles travaillent fort et longtemps, comme pendant une étape de montagne, la dépense augmente beaucoup."


def donnees(svg, bloc=None):
    d = {}
    d["e2-1"] = {
        "mousse": tri(
            "Range chaque activité selon l'énergie que le corps dépense. Clique sur une carte, puis sur une colonne.",
            [("peu", "Le corps dépense peu d'énergie"), ("beaucoup", "Le corps dépense beaucoup d'énergie")],
            [("Faire la sieste", "peu"), ("Regarder la télévision", "peu"), ("Courir très vite", "beaucoup"), ("Faire du vélo en montagne", "beaucoup")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Quand on est allongé, les muscles se reposent.", "Quand on court, les muscles travaillent fort."]),
        "lieutenant": vf(
            "La docteure Inès affiche cinq affirmations dans la salle des menus. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui montre que le corps dépense de l'énergie même au repos.",
            [("Le corps dépense de l'énergie même pendant le sommeil.", True, "Respirer, faire battre le cœur, garder sa température."),
             ("Un enfant n'a besoin d'énergie que pour bouger.", False, "Il en a aussi besoin pour grandir."),
             ("Les besoins en énergie sont les mêmes pour tout le monde.", False, "Ils varient selon l'âge, la croissance et l'activité."),
             ("Quand les muscles travaillent fort et longtemps, la dépense augmente beaucoup.", True, "Comme pendant une étape de montagne."),
             ("L'énergie des aliments se mesure en kilocalories.", True, "Abréviation : kcal.")],
            ["Le corps travaille même quand on dort.", "Un enfant dépense de l'énergie pour vivre, bouger et grandir.", "Pour la justification : cherche la phrase qui parle du sommeil."],
            J("Quelle phrase de la fiche montre que le corps dépense de l'énergie même au repos ?", B5, [B1, B7, B2], pos=1)),
        "second": qcm(
            carnet("Menu du jour de Rosalie", "(inventé pour le jeu). Un enfant de 10 ans dort 9 heures, passe 6 heures assis à l'école, joue 1 heure dans la cour. Un coureur passe 5 heures à pédaler en montagne.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 1.",
            [("Ce garçon dort 9 heures : dépense-t-il de l'énergie pendant ce temps ?", ["Oui : le corps travaille en permanence", "Non : l'énergie ne se dépense qu'en bougeant", "Seulement s'il rêve", "Seulement l'été"], 0, "Respirer et faire battre le cœur coûte de l'énergie."),
             ("Pourquoi le coureur a-t-il besoin de beaucoup plus d'énergie que l'enfant ?", ["Ses muscles travaillent fort et longtemps", "Il est plus âgé", "Il dort plus longtemps", "Il mange plus lentement"], 0, "Effort long et fort."),
             ("Pour l'enfant, qu'est-ce qui s'ajoute aux besoins de l'adulte ?", ["La croissance", "La couleur des yeux", "Le poids du sac", "La vitesse du vent"], 0, "Un enfant a besoin d'énergie en plus pour grandir.")],
            ["Le corps dépense de l'énergie en permanence.", "Plus l'effort est long et intense, plus la dépense augmente.", "Un enfant grandit : que lui faut-il en plus ?"],
            J("Quelle phrase de la fiche justifie ta réponse à la question 1 ?", B5, [B7, B6, B2], pos=2)),
    }
    d["e2-2"] = {
        "mousse": ordre(
            "Range ces personnes, de celle qui a le plus petit besoin d'énergie par jour à celle qui a le plus grand. Le plus petit besoin en haut. Utilise les flèches ▲ et ▼, puis vérifie.",
            ["Un bébé d'un an", "Un enfant de 10 ans", "Un coureur cycliste un jour d'étape de montagne"],
            ["Ouvre la fiche " + F + ".", "Les besoins grandissent avec le corps et avec l'effort.", "Le coureur en course est tout en bas."]),
        "lieutenant": ordre(
            "Inès range ces besoins par jour, du plus petit au plus grand (le plus petit en haut). Utilise les flèches ▲ et ▼, puis choisis la phrase de la fiche qui donne ces ordres de grandeur.",
            ["Un enfant de 10 ans (environ 1 800 à 2 200 kcal)", "Un adulte (2 000 à 2 700 kcal)", "Basile un jour de repos (environ 2 800 kcal)", "Basile un jour d'étape de montagne (environ 6 000 kcal)"],
            ["Compare les nombres de kcal.", "Un adulte a besoin de plus qu'un enfant de 10 ans.", "L'étape de montagne est la plus grande dépense."],
            J("Quelle phrase de la fiche donne ces ordres de grandeur ?", B3, [B1, B2, B7], pos=0)),
        "second": ordre(
            "Basile prépare son étape de montagne. Remets dans l'ordre ce qui explique pourquoi il doit manger beaucoup, puis choisis la phrase de la fiche qui justifie le dernier maillon.",
            ["Il pédale longtemps dans la montagne.", "Ses muscles travaillent fort et longtemps.", "Son corps dépense beaucoup d'énergie.", "Il doit manger un grand repas la veille et pendant la course."],
            ["Commence par l'effort, termine par ce qu'il faut manger.", "Les muscles travaillent avant que le corps ne dépense beaucoup.", "Un seul maillon parle de ce qu'on mange."],
            J("Quelle phrase de la fiche justifie l'enchaînement « effort, puis dépense » ?", B7, [B3, B4, B6], pos=2)),
    }
    d["e2-3"] = {
        "mousse": intrus(
            "Trois de ces raisons font changer la quantité d'aliments dont une personne a besoin. Trouve celle qui n'a rien à voir. Clique sur l'intrus, puis vérifie.",
            [("L'âge", False), ("L'effort physique", False), ("Le prénom", True)],
            ["Ouvre la fiche " + F + ".", "Un bébé et un adulte n'ont pas les mêmes besoins.", "Un prénom ne change pas le travail du corps."]),
        "lieutenant": tri(
            "Inès classe des situations selon leur effet sur les besoins en énergie. Range chaque carte, puis choisis la phrase de la fiche qui cite les trois facteurs.",
            [("aug", "Fait augmenter les besoins"), ("non", "Ne change pas les besoins")],
            [("Grandir vite", "aug"), ("Pédaler une journée entière en montagne", "aug"), ("Faire un effort long et intense", "aug"),
             ("La couleur du vélo", "non"), ("Le nom du coureur", "non"), ("Le jour de la semaine", "non")],
            ["Les besoins varient selon trois choses.", "Grandir et bouger demandent de l'énergie.", "Une couleur ou un nom ne font pas travailler le corps."],
            J("Quelle phrase de la fiche cite les facteurs qui font varier les besoins ?", B2, [B1, B5, B4], pos=1)),
        "second": vf(
            "Rosalie a noté six phrases sur l'alimentation. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui contredit l'idée « il existe des aliments interdits ».",
            [("Manger équilibré, c'est varier les aliments.", True, "Et adapter les quantités à ses besoins."),
             ("Il existe des aliments interdits à tous les enfants.", False, "Il n'y a pas d'aliment interdit."),
             ("Un enfant de 10 ans a besoin d'environ 1 800 à 2 200 kcal par jour.", True, "C'est un ordre de grandeur."),
             ("Un adulte a besoin de 6 000 kcal par jour.", False, "Seulement un coureur en étape de montagne."),
             ("Les nombres de kcal sont des ordres de grandeur : chacun a ses propres besoins.", True, "On ne calcule pas les calories de ses repas."),
             ("Tous les adultes ont exactement les mêmes besoins.", False, "Ils varient d'une personne à l'autre.")],
            ["Les kcal donnent des ordres de grandeur, pas des règles exactes.", "Les besoins sont personnels.", "Pour la justification : cherche la phrase qui parle d'aliments interdits."],
            J("Quelle phrase de la fiche contredit l'idée « il existe des aliments interdits » ?", B4, [B2, B3, B1], pos=0)),
    }
    d["e2-4"] = {
        "lieutenant": qcm(
            "La docteure Inès a noté les besoins de Basile pour trois journées. Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3."
            + tableau("Besoins en énergie de Basile (ordres de grandeur, journée plate fictive)", ["Journée", "Besoin en énergie"],
                      [("Jour de repos", "environ 2 800 kcal"), ("Étape plate", "environ 4 500 kcal"), ("Étape de montagne", "environ 6 000 kcal")]),
            [("Quelle journée demande le plus d'énergie ?", ["L'étape de montagne", "Le jour de repos", "L'étape plate", "Elles sont égales"], 0, "6 000 est le plus grand nombre."),
             ("De combien de kcal l'étape de montagne dépasse-t-elle le jour de repos ?", ["3 200 kcal", "1 500 kcal", "8 800 kcal", "6 000 kcal"], 0, "6 000 − 2 800 = 3 200."),
             ("Pourquoi l'étape de montagne demande-t-elle plus que l'étape plate ?", ["Les muscles travaillent plus fort et plus longtemps", "Basile est plus âgé ce jour-là", "Il dort moins", "Il pèse plus"], 0, "L'effort est plus grand.")],
            ["Compare les trois nombres.", "Soustrais : grand nombre moins petit nombre.", "Pense à l'effort fourni."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", B7, [B3, B6, B4], pos=1)),
        "second": qcm(
            "Rosalie organise les repas de Basile pour l'étape de montagne (environ 6 000 kcal). Elle prépare des repas de 1 500 kcal chacun. Réponds aux trois questions, puis choisis la phrase de la fiche qui donne l'ordre de grandeur utilisé."
            + tableau("Besoins de Basile (ordres de grandeur)", ["Journée", "Besoin en énergie"], [("Jour de repos", "environ 2 800 kcal"), ("Jour d'étape de montagne", "environ 6 000 kcal")]),
            [("Combien de repas de 1 500 kcal faut-il pour couvrir l'étape de montagne ?", ["4", "2", "6", "3"], 0, "6 000 ÷ 1 500 = 4."),
             ("Combien de repas de 1 500 kcal pour un jour de repos (environ 2 800 kcal) ?", ["environ 2", "environ 4", "environ 6", "environ 1"], 0, "2 800 ÷ 1 500 est proche de 2."),
             ("Ce calcul donne-t-il le besoin exact de Basile ?", ["Non : ce sont des ordres de grandeur", "Oui : au gramme près", "Oui : c'est une loi", "Non : Basile ne mange pas"], 0, "Chacun a ses propres besoins.")],
            ["Divise le besoin par l'énergie d'un repas.", "2 800 est proche de 3 000 ÷ 1 500.", "Relis la fin de la fiche : que dit-elle des nombres ?"],
            J("Quelle phrase de la fiche donne l'ordre de grandeur de l'étape de montagne ?", B3, [B2, B5, B7], pos=1)),
    }
    return d
