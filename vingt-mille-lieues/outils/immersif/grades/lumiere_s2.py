"""Salle 2 « L'atelier des vitres » : grades mousse, lieutenant, second (fiche : matieres)."""
from aide import *

FICHE = "« Transparent, translucide, opaque »"
EXP = "Pour classer un matériau, on fait une expérience : on le place entre une lampe et ses yeux, puis on se pose deux questions. La lumière passe-t-elle ? Voit-on nettement à travers ?"
TRANSP = "Un matériau transparent laisse passer la lumière, et on voit nettement les objets à travers : une vitre, l'eau claire, le film alimentaire."
TRANSL = "Un matériau translucide laisse passer la lumière, mais elle est dispersée : on ne voit pas nettement à travers."
OPAQUE = "Un matériau opaque ne laisse pas passer la lumière : le bois, le carton, le métal."
MIROIR = "Un miroir aussi est opaque : il ne laisse pas passer la lumière, il la renvoie dans une direction précise."
ALU = "La feuille d'aluminium brille, et pourtant elle est opaque."
BAINS = "C'est le cas du papier calque, du papier sulfurisé ou du verre dépoli des salles de bains, qui laisse entrer le jour sans qu'on voie à l'intérieur."
PHARE = "Les vitres de la lanterne d'un phare doivent être transparentes : la lumière doit sortir vers la mer sans être arrêtée."


def donnees(svg, bloc=None):
    d = {}
    # ---------------------------------------------------------------- e2-1 : les mots de Salomé
    d["e2-1"] = {
        "mousse": assoc(
            "Salomé montre trois matériaux de l'atelier. Relie chaque matériau à ce qui se passe quand on le regarde devant une lampe. Clique sur un matériau, puis sur sa description.",
            [("une vitre claire", "la lumière passe et on voit nettement à travers"), ("le papier calque", "la lumière passe, mais tout est flou"),
             ("une planche de bois", "la lumière ne passe pas")],
            ["Ouvre la fiche " + FICHE + " dans la Bibliothèque.", "Pense à une fenêtre : on voit dehors.", "Derrière une planche de bois, il fait sombre."]),
        "lieutenant": vf(
            "Salomé a affiché cinq affirmations sur les matériaux de l'atelier. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui prouve que le miroir est opaque.",
            [("Un matériau transparent laisse passer la lumière.", True, "Et on voit nettement à travers."),
             ("Un matériau translucide ne laisse passer aucune lumière.", False, "Il laisse passer de la lumière dispersée."),
             ("La feuille d'aluminium brille, donc elle est transparente.", False, "Elle brille, et pourtant elle est opaque."),
             ("Un miroir est opaque et renvoie la lumière.", True, "Il ne la laisse pas passer : il la renvoie."),
             ("Le verre dépoli laisse entrer le jour sans qu'on voie nettement à l'intérieur.", True, "C'est un matériau translucide.")],
            ["Deux questions pour classer : la lumière passe-t-elle ? Voit-on nettement à travers ?", "Brillant n'est pas transparent.", "Un miroir ne se laisse pas traverser."],
            J("Quelle phrase de la fiche prouve que le miroir est opaque ?", MIROIR, [ALU, TRANSL, PHARE], pos=1)),
        "second": qcm(
            "<div class='doc-carnet'><b>Essais de Salomé</b> (résultats inventés pour le jeu). Chaque matériau est placé entre une lampe et l'œil.<table><tr><th>Matériau</th><th>La lumière passe-t-elle ?</th><th>Voit-on nettement la lampe ?</th></tr><tr><td>A</td><td>oui</td><td>oui</td></tr><tr><td>B</td><td>oui</td><td>non</td></tr><tr><td>C</td><td>non</td><td>non</td></tr><tr><td>D</td><td>non</td><td>non, mais il brille</td></tr></table></div>Réponds aux trois questions, puis choisis la phrase de la fiche qui explique la question 2.",
            [("Quel matériau convient pour les vitres de la lanterne ?", ["A", "B", "C", "D"], 0, "Il faut que la lumière sorte vers la mer sans être arrêtée : transparent."),
             ("Quel matériau peut être du verre dépoli ?", ["B", "A", "C", "D"], 0, "La lumière passe, mais on ne voit pas nettement : translucide."),
             ("Le matériau D brille. Peut-on en conclure qu'il laisse passer la lumière ?", ["Non : il est opaque, comme la feuille d'aluminium", "Oui : s'il brille, la lumière passe",
                                                                                           "Oui : il est transparent", "On ne peut rien dire"], 0, "Brillant ne veut pas dire transparent.")],
            ["Utilise les deux colonnes du tableau comme les deux questions de la fiche.", "« Oui, mais flou » : c'est la signature du translucide.", "Un objet peut briller et rester opaque."],
            J("Quelle phrase de la fiche explique ta réponse à la question 2 ?", TRANSL, [TRANSP, OPAQUE, BAINS], pos=2)),
    }
    # ---------------------------------------------------------------- e2-2 : banc d'essai
    d["e2-2"] = {
        "mousse": tri(
            "Salomé place chaque matériau devant une lampe. Range les quatre matériaux : la lumière passe, ou elle ne passe pas.",
            [("passe", "La lumière passe"), ("nepasse", "La lumière ne passe pas")],
            [("la vitre de la lanterne", "passe"), ("l'eau claire d'un verre", "passe"), ("le carton", "nepasse"), ("la planche de bois", "nepasse")],
            ["Ouvre la fiche " + FICHE + ".", "Derrière le carton, on n'a plus de lumière.", "À travers l'eau claire, on voit la lumière."]),
        "lieutenant": tri(
            "Salomé a testé neuf matériaux devant sa lampe. Range-les dans les trois colonnes, puis choisis la phrase de la fiche qui explique comment on classe un matériau.",
            [("transparent", "Transparent"), ("translucide", "Translucide"), ("opaque", "Opaque")],
            [("la bouteille en plastique incolore", "transparent"), ("le verre de lunettes", "transparent"), ("le papier de soie", "translucide"),
             ("le papier sulfurisé", "translucide"), ("le verre dépoli du phare", "translucide"), ("le miroir", "opaque"),
             ("la porte en métal", "opaque"), ("la feuille d'aluminium", "opaque"), ("le carton épais", "opaque")],
            ["Deux questions : la lumière passe-t-elle ? Voit-on nettement à travers ?", "Le miroir et l'aluminium brillent, mais ne laissent rien passer.", "Pour la justification : cherche la phrase qui parle d'expérience."],
            J("Quelle phrase de la fiche explique comment classer un matériau ?", EXP, [TRANSL, MIROIR, PHARE], pos=0)),
        "second": tri(
            "Salomé n'a pas noté le nom des matériaux, seulement ce qu'elle a observé à travers chacun. Range chaque observation dans la bonne colonne, puis choisis la phrase de la fiche qui définit la colonne du milieu.",
            [("transparent", "Transparent"), ("translucide", "Translucide"), ("opaque", "Opaque")],
            [("La lampe se voit nettement, mais plus faible.", "transparent"), ("On devine seulement une tache lumineuse sans contour.", "translucide"),
             ("On voit un halo flou, jamais les contours de la lampe.", "translucide"), ("Le matériau brille, mais on ne voit rien derrière.", "opaque"),
             ("Derrière le matériau, une ombre se forme.", "opaque"), ("On voit la flamme d'une bougie très nettement à travers.", "transparent")],
            ["Une ombre se forme derrière un matériau qui arrête la lumière.", "Contours nets : transparent. Contours flous : translucide.", "Brillant n'est pas transparent."],
            J("Quelle phrase de la fiche définit un matériau translucide ?", TRANSL, [TRANSP, OPAQUE, MIROIR], pos=1)),
    }
    # ---------------------------------------------------------------- e2-3 : carnet d'essais
    d["e2-3"] = {
        "mousse": trous(
            "Le carnet de Salomé est tâché : il manque des mots. Clique sur une étiquette, puis sur le trou où elle va. Une étiquette est en trop.",
            "Une vitre claire est [[transparente]] : on voit nettement à travers. Le carton est [[opaque]] : la lumière ne passe pas. Derrière lui, il y a de l'[[ombre]].",
            ["transparente", "opaque", "ombre", "brillant"],
            ["Ouvre la fiche " + FICHE + ".", "Le carton arrête toute la lumière.", "Derrière un objet qui arrête la lumière, on trouve de l'ombre."]),
        "lieutenant": trous(
            "Salomé a écrit un compte rendu d'essais, mais il manque des mots. Clique sur une étiquette, puis sur le trou où elle va. Trois étiquettes sont en trop. Puis choisis la phrase de la fiche qui justifie le dernier trou.",
            "On place chaque matériau entre une lampe et l'œil. Le plastique incolore laisse passer la lumière et on voit nettement : il est [[transparent]]. Le papier sulfurisé laisse passer la lumière, mais on ne voit pas nettement à travers : il est [[translucide]]. Le métal est [[opaque]]. Le miroir est lui aussi opaque : il ne laisse pas passer la lumière, il la [[renvoie]].",
            ["transparent", "translucide", "opaque", "renvoie", "produit", "absorbe", "traverse"],
            ["Reprends les trois définitions de la fiche.", "Un miroir ne laisse rien passer : que fait-il de la lumière ?", "« Produit » est réservé aux sources de lumière."],
            J("Quelle phrase de la fiche justifie le dernier trou ?", MIROIR, [ALU, TRANSL, PHARE], pos=3)),
        "second": trous(
            "Salomé a rédigé la méthode de ses essais, mais il manque des mots. Clique sur une étiquette, puis sur le trou où elle va. Trois étiquettes sont en trop. Puis choisis la phrase de la fiche qui justifie le choix du verre de la lanterne.",
            "Pour classer un matériau, on se pose deux questions : la [[lumière]] passe-t-elle ? Voit-on [[nettement]] à travers ? Pour la lanterne du phare, Salomé choisit un verre [[transparent]], afin que la lumière sorte vers la [[mer]] sans être arrêtée. Une feuille d'aluminium brille, mais elle est [[opaque]].",
            ["lumière", "nettement", "transparent", "mer", "opaque", "translucide", "ombre", "chaleur"],
            ["La méthode se trouve au début de la fiche, dans l'explication de l'expérience.", "Un verre qui arrête ou disperse la lumière gênerait le phare.", "Brillant ne veut pas dire transparent."],
            J("Quelle phrase de la fiche justifie le choix du verre de la lanterne ?", PHARE, [TRANSP, EXP, ALU], pos=3)),
    }
    # ---------------------------------------------------------------- e2-4 : questions de l'ingénieure (timonier, lieutenant, second)
    d["e2-4"] = {
        "lieutenant": qcm(
            "<div class='doc-carnet'><b>Commande à l'atelier</b> (inventée pour le jeu). Salomé doit choisir trois matériaux : une vitre pour la lanterne, un volet pour la nuit, un rideau pour la salle de repos qui laisse entrer le jour sans qu'on voie à l'intérieur.</div>Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("Quel matériau pour la vitre de la lanterne ?", ["Du verre transparent", "Du verre dépoli", "Une planche de bois", "Une feuille d'aluminium"], 0, "La lumière doit sortir sans être arrêtée."),
             ("Quel matériau pour le volet de nuit ?", ["Une planche de bois, qui est opaque", "Du film alimentaire", "Du papier calque", "Du verre transparent"], 0, "Un volet doit arrêter la lumière."),
             ("Quel matériau pour le rideau de la salle de repos ?", ["Un tissu translucide", "Un verre transparent", "Une plaque de métal", "Un miroir"], 0, "Le jour entre, mais on ne voit pas nettement à l'intérieur.")],
            ["Un matériau pour chaque besoin : laisser tout passer, tout arrêter, ou laisser passer en cachant.", "Le volet doit faire de l'ombre.", "Pour la salle de repos : la lumière passe, mais pas l'image."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", BAINS, [TRANSP, OPAQUE, PHARE], pos=2)),
        "second": vf(
            "Salomé conclut ses essais en six phrases. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui contredit l'idée « tout ce qui brille laisse passer la lumière ».",
            [("Une feuille d'aluminium brille : elle laisse donc passer la lumière.", False, "Elle brille, et pourtant elle est opaque."),
             ("Le verre dépoli est un bon choix pour une fenêtre de salle de bains.", True, "Il laisse entrer le jour sans qu'on voie à l'intérieur."),
             ("Un matériau translucide ne laisse passer aucune lumière.", False, "Il en laisse passer, dispersée."),
             ("Derrière un objet opaque se forme une ombre.", True, "L'objet arrête la lumière."),
             ("Un miroir placé derrière une lampe renvoie vers l'avant la lumière qui partait vers l'arrière.", True, "C'est le rôle du miroir d'un projecteur."),
             ("Les vitres de la lanterne d'un phare doivent être opaques.", False, "Elles doivent être transparentes.")],
            ["Brillant et transparent sont deux choses différentes.", "Un phare a besoin que sa lumière sorte.", "Un miroir renvoie, il ne laisse pas passer."],
            J("Quelle phrase de la fiche contredit l'idée « tout ce qui brille laisse passer la lumière » ?", ALU, [TRANSP, TRANSL, PHARE], pos=1)),
    }
    return d
