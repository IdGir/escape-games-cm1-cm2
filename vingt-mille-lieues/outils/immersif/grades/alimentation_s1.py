"""Salle 1 « La cour du potager et du poulailler » (fiche : croissance)."""
from aide import *

F = "« Grandir, c'est fabriquer de la matière »"
C1 = "Tous les êtres vivants ont besoin de matière pour grandir et se développer."
C2 = "Les animaux, et donc les êtres humains, trouvent cette matière dans leur nourriture, qui vient elle-même d'autres êtres vivants."
C3 = "Une partie des aliments sert à construire le corps ; une autre fournit l'énergie pour vivre et bouger ; le reste est rejeté."
C4 = "C'est pourquoi un poussin qui a mangé 700 g de nourriture n'a grossi que de 410 g."
C5 = "Chez l'être humain, la croissance est très rapide les premières années, plus lente ensuite (5 à 6 cm par an vers 8-10 ans), puis de nouveau rapide à la puberté."
C6 = "Pour le vérifier, on mesure la masse (en grammes, sur une balance) et la taille (en centimètres, avec une toise) à intervalles réguliers, puis on compare les valeurs dans un tableau ou sur un graphique."


def donnees(svg, bloc=None):
    d = {}
    d["e1-1"] = {
        "mousse": code(
            "Nathan a noté la masse du poussin Caramel. Lis le tableau, calcule, puis écris ta réponse dans le cadenas."
            + tableau("Carnet de Nathan (relevé fictif)", ["Semaine", "Masse de Caramel"], [("0 (naissance)", "40 g"), ("1", "95 g")])
            + question("De combien de grammes Caramel a-t-il grossi pendant la semaine 1 ?"),
            [("Caramel a grossi de (en grammes)", "55", 2)],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Pour savoir de combien il a grossi, on fait une soustraction.", "Calcule 95 − 40."]),
        "lieutenant": qcm(
            "Nathan suit aussi la poussine Pâquerette. Lis son carnet, réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3."
            + tableau("Carnet de Nathan : la poussine Pâquerette (relevé fictif)", ["Semaine", "Masse de Pâquerette", "Nourriture mangée pendant la semaine"],
                      [("0 (naissance)", "35 g", "—"), ("1", "80 g", "60 g"), ("2", "150 g", "120 g"), ("3", "240 g", "180 g")]),
            [("De combien de grammes Pâquerette a-t-elle grossi en 3 semaines ?", ["205 g", "240 g", "360 g", "175 g"], 0, "240 − 35 = 205."),
             ("Combien de grammes de nourriture a-t-elle mangés en tout ?", ["360 g", "205 g", "180 g", "240 g"], 0, "60 + 120 + 180 = 360."),
             ("Pourquoi Pâquerette a-t-elle moins grossi que ce qu'elle a mangé ?", [
                 "Une partie des aliments sert à construire le corps, une autre fournit l'énergie, le reste est rejeté", "Elle a mangé des aliments sans matière",
                 "Sa masse a diminué à cause de la chaleur", "Elle n'a pas assez mangé pour grandir"], 0, "Tout ne sert pas à construire le corps.")],
            ["Gain de masse : masse finale moins masse de naissance.", "Additionne la dernière colonne.", "Compare 360 g mangés et 205 g gagnés : où est passé le reste ?"],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", C3, [C2, C1, C6], pos=1)),
        "second": code(
            "Nathan reprend les mesures de Caramel : en 4 semaines, il a mangé 700 g de nourriture et sa masse est passée de 40 g à 450 g. En semaine 5, il mange 350 g et grossit de 175 g. Calcule, puis ouvre le cadenas. Choisis aussi la phrase de la fiche qui explique pourquoi on ne retrouve pas dans la masse tout ce qui a été mangé.",
            [("Grammes mangés en 4 semaines qui n'ont pas servi à grossir", "290", 3), ("Masse de Caramel en semaine 5 (g)", "625", 3)],
            ["700 − 410 : combien de grammes ne se retrouvent pas dans la masse ?", "Le gain de masse en 4 semaines est 450 − 40.", "Masse en semaine 5 : 450 + 175."],
            J("Quelle phrase de la fiche explique l'écart entre ce qui est mangé et ce qui est gagné ?", C4, [C1, C2, C6], pos=2)),
    }
    d["e1-2"] = {
        "mousse": qcm(
            "Lis la question, clique sur la bonne réponse, puis vérifie.",
            [("Caramel grossit. Avec quoi son corps fabrique-t-il de la matière ?", ["Avec ce qu'il mange", "Avec la lumière du soleil", "Avec le bruit du poulailler", "Avec rien du tout"], 0, "La matière vient de la nourriture.")],
            ["Ouvre la fiche " + F + ".", "Un poussin ne grandit pas sans manger.", "Cherche ce que Caramel avale tous les jours."]),
        "lieutenant": vf(
            "Nathan a noté cinq affirmations sur l'origine de la matière. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui montre d'où vient la nourriture des animaux.",
            [("Les animaux trouvent la matière de leur corps dans leur nourriture.", True, "C'est le point de départ de la fiche."),
             ("La nourriture des animaux vient elle-même d'autres êtres vivants.", True, "Plantes et animaux."),
             ("Tout ce qu'un poussin mange sert à construire son corps.", False, "Une partie fournit l'énergie, le reste est rejeté."),
             ("Le poussin construit son corps avec la chaleur de la lampe.", False, "La chaleur ne fournit pas de matière."),
             ("La masse se mesure avec une balance, la taille avec une toise.", True, "Deux instruments, deux grandeurs.")],
            ["La matière du corps vient des aliments.", "Une partie des aliments sert à autre chose qu'à grossir.", "Pour la justification : cherche la phrase qui dit d'où vient la nourriture."],
            J("Quelle phrase de la fiche montre d'où vient la nourriture des animaux ?", C2, [C1, C3, C6], pos=0)),
        "second": qcm(
            "<div class='doc-carnet'><b>Questions de la docteure Inès</b> (inventées pour le jeu). Un enfant de 9 ans a grandi de 6 cm en un an. Un bébé de 6 mois a grandi de 10 cm en six mois.</div>Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Pour grandir de 6 cm, l'enfant a-t-il eu besoin de matière ?", ["Oui : il a fabriqué de la matière à partir de ses aliments", "Non : sa taille augmente toute seule", "Non : l'air suffit", "Seulement s'il fait du sport"], 0, "Grandir, c'est fabriquer de la matière."),
             ("Quelle période de la vie correspond à une croissance très rapide ?", ["Les premières années et la puberté", "Entre 8 et 10 ans uniquement", "L'âge adulte", "Aucune : on grandit toujours au même rythme"], 0, "Rapide, puis plus lente, puis rapide à la puberté."),
             ("Pourquoi le bébé a-t-il grandi plus vite que l'enfant de 9 ans ?", ["Parce que la croissance est plus rapide les premières années de la vie", "Parce qu'il mange moins", "Parce qu'il dort moins", "Parce qu'il est plus lourd"], 0, "La croissance ralentit après les premières années.")],
            ["Grandir demande de la matière, donc des aliments.", "La croissance n'a pas le même rythme à tous les âges.", "Compare les âges des deux enfants."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", C5, [C1, C3, C6], pos=3)),
    }
    d["e1-3"] = {
        "mousse": tri(
            "Lou est mesurée chaque année contre la porte de la cuisine. Lis le tableau, puis range chaque phrase : est-elle vraie ou fausse ? Clique sur une carte, puis sur une colonne."
            + tableau("Les marques de Lou (relevé fictif)", ["Âge", "Taille"], [("6 ans", "115 cm"), ("7 ans", "121 cm")]),
            [("vrai", "Vrai"), ("faux", "Faux")],
            [("Lou mesure plus à 7 ans qu'à 6 ans.", "vrai"), ("Lou a grandi de 6 cm.", "vrai"), ("Lou a perdu des centimètres.", "faux"), ("Lou a grandi de 20 cm.", "faux")],
            ["Ouvre la fiche " + F + ".", "Calcule la différence : 121 − 115.", "Deux phrases sont vraies, deux sont fausses."]),
        "lieutenant": tri(
            "Nathan classe les périodes de la vie. Range chaque période : la croissance y est-elle rapide ou plus lente ? Puis choisis la phrase de la fiche qui donne l'ordre de grandeur de la croissance vers 8-10 ans.",
            [("rapide", "Croissance rapide"), ("lente", "Croissance plus lente")],
            [("Les premières années de la vie", "rapide"), ("La puberté", "rapide"), ("Le premier anniversaire d'un bébé", "rapide"),
             ("Vers 8-10 ans", "lente"), ("L'année qui suit les premières années", "lente"), ("Entre la petite enfance et la puberté", "lente")],
            ["La croissance est rapide, puis plus lente, puis de nouveau rapide.", "La puberté est un moment de croissance rapide.", "Vers 8-10 ans, on grandit de 5 à 6 cm par an."],
            J("Quelle phrase de la fiche donne l'ordre de grandeur de la croissance vers 8-10 ans ?", C5, [C3, C1, C4], pos=2)),
        "second": tri(
            "Nathan lit le carnet de croissance de Lou. Range chaque phrase : le tableau permet-il de la conclure, ou non ? Puis choisis la phrase de la fiche qui explique comment on vérifie une croissance."
            + tableau("Les marques de Lou (relevé fictif)", ["Âge", "Taille"], [("6 ans", "115 cm"), ("7 ans", "121 cm"), ("8 ans", "126 cm"), ("9 ans", "132 cm"), ("10 ans", "137 cm")]),
            [("oui", "Le tableau le montre"), ("non", "Le tableau ne le montre pas")],
            [("Lou a grandi chaque année.", "oui"), ("Lou a grandi d'environ 5 à 6 cm par an.", "oui"), ("Entre 6 et 10 ans, Lou a grandi de 22 cm.", "oui"),
             ("Lou grandira de 5 cm par an toute sa vie.", "non"), ("Lou grandit grâce à ce qu'elle mange.", "non"), ("Lou grandira plus vite que ses camarades.", "non")],
            ["Un tableau donne des mesures, pas des explications ni l'avenir.", "Calcule 137 − 115.", "« Toute sa vie » : le tableau s'arrête à 10 ans."],
            J("Quelle phrase de la fiche explique comment on vérifie une croissance ?", C6, [C5, C2, C4], pos=1)),
    }
    d["e1-4"] = {
        "lieutenant": code(
            "Nathan a mesuré Sam chaque année. Lis le tableau, calcule, puis ouvre le cadenas."
            + tableau("Les marques de Sam (relevé fictif)", ["Âge", "Taille"], [("6 ans", "112 cm"), ("7 ans", "118 cm"), ("8 ans", "123 cm"), ("9 ans", "129 cm"), ("10 ans", "134 cm")])
            + question("Combien de centimètres Sam a-t-il grandi entre 6 et 10 ans ? Quelle est sa plus grande croissance en une seule année ?"),
            [("Croissance totale (cm)", "22", 2), ("Plus grande croissance en un an (cm)", "6", 1)],
            ["Taille à 10 ans moins taille à 6 ans.", "Calcule aussi chaque écart d'une année à la suivante : 6, 5, 6, 5.", "Le plus grand écart est 6 cm."],
            J("Quelle phrase de la fiche explique comment on compare des mesures ?", C6, [C5, C3, C1], pos=1)),
        "second": trous(
            "Nathan a rédigé son bilan de la semaine, mais il manque des mots. Clique sur une étiquette, puis sur le trou où elle va. Trois étiquettes sont en trop. Puis choisis la phrase de la fiche qui justifie le mot « nourriture ».",
            "Tous les êtres vivants ont besoin de [[matière]] pour grandir. Les animaux la trouvent dans leur [[nourriture]]. Une partie des aliments sert à construire le [[corps]], une autre fournit l'[[énergie]] pour vivre et bouger, et le reste est [[rejeté]].",
            ["matière", "nourriture", "corps", "énergie", "rejeté", "lumière", "bruit", "silence"],
            ["Relis la fiche : les mots sont dans le premier paragraphe.", "Le reste de ce qu'on mange ne reste pas dans le corps.", "Trois étiquettes n'ont aucun rapport avec les aliments."],
            J("Quelle phrase de la fiche justifie le mot « nourriture » ?", C2, [C1, C4, C6], pos=0)),
    }
    return d
