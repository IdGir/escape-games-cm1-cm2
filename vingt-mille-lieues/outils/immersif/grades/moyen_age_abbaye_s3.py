"""Salle 3 « Le scriptorium de l'abbaye » (fiche : scriptorium)."""
from aide import *

F = "« Les moines : prier, copier, enseigner »"
S1 = "La plupart des moines suivent la règle de saint Benoît : prière, travail et lecture se partagent la journée, rythmée par les offices, de la nuit jusqu'au soir."
S2 = "En Bourgogne, l'abbaye de Cluny, fondée en 910, rayonne sur toute l'Europe ; l'abbaye cistercienne de Fontenay, fondée en 1118, a conservé la salle voûtée où travaillaient les moines."
S3 = "Le parcheminier prépare les peaux (mouton, veau) : c'est le parchemin."
S4 = "Le copiste trace des lignes, puis écrit à la plume d'oie. Un petit canif gratte les erreurs et taille la plume."
S5 = "Le rubricateur ajoute en rouge les titres et les débuts de chapitres."
S6 = "L'enlumineur peint les lettrines et les décors, parfois avec de l'or."
S7 = "Le relieur assemble les cahiers entre deux plats de bois."
S8 = "On travaille à la lumière du jour, près des fenêtres : un incendie détruirait la bibliothèque."
S9 = "Il n'existe pas d'école publique. L'enseignement est assuré par l'Église : écoles monastiques dans les abbayes, écoles cathédrales auprès des évêques, puis, au XIIIe siècle, les premières universités."
S10 = "C'est en partie grâce aux copistes que des textes de l'Antiquité sont parvenus jusqu'à nous."
S11 = "On y apprend d'abord le latin, la langue de l'Église et des livres."


def donnees(svg, bloc=None):
    d = {}
    d["e3-1"] = {
        "mousse": tri(
            "Range chaque activité de la journée d'un moine dans la bonne colonne : clique sur une carte, puis sur sa colonne.",
            [("prier", "Prier"), ("copier", "Copier les livres"), ("travail", "Travailler de ses mains")],
            [("Chanter à l'église", "prier"), ("Recopier un livre à la plume", "copier"), ("Cultiver le potager", "travail"), ("Faire le pain", "travail")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Ce qui se fait à l'église va dans « Prier ».", "Un livre et une plume : « Copier »."]),
        "lieutenant": vf(
            "Frère Anselme décrit la vie de l'abbaye en cinq affirmations. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui décrit la journée des moines.",
            [("La plupart des moines suivent la règle de saint Benoît.", True, "Prière, travail et lecture."), ("Les moines ne travaillent jamais de leurs mains.", False, "Le travail fait partie de la journée."),
             ("La journée est rythmée par les offices, de la nuit jusqu'au soir.", True, "C'est le rythme de l'abbaye."), ("L'abbaye de Cluny a été fondée en 910.", True, "En Bourgogne."), ("L'abbaye de Fontenay a été fondée en 910.", False, "En 1118.")],
            ["Prière, travail et lecture se partagent la journée.", "Cluny : 910. Fontenay : 1118.", "Pour la justification : cherche la phrase qui nomme la règle."],
            J("Quelle phrase de la fiche décrit la journée des moines ?", S1, [S2, S4, S9], pos=1)),
        "second": qcm(
            carnet("Journal de Frère Anselme", "(inventé pour le jeu). « Je me lève à la nuit pour l'office. Puis je copie jusqu'à midi, près d'une fenêtre : la lumière du jour est précieuse, et jamais de bougie près des livres. L'après-midi, je travaille au potager. »")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Quelles sont les trois activités citées dans la journée ?", ["Prière, copie, travail de la terre", "Chasse, guerre, commerce", "École, marché, voyage", "Peinture, forge, pêche"], 0, "Prière, travail et lecture."),
             ("Pourquoi copie-t-on près d'une fenêtre, sans bougie ?", ["Pour éviter un incendie qui détruirait la bibliothèque", "Pour regarder dehors", "Parce que le parchemin brille", "Parce que les moines n'aiment pas le feu"], 0, "On travaille à la lumière du jour."),
             ("L'abbaye de Fontenay est…", ["cistercienne, fondée en 1118", "clunisienne, fondée en 910", "romaine, fondée en 476", "royale, fondée en 800"], 0, "Fontenay : 1118.")],
            ["Prière, copie, potager : trois activités.", "Un incendie détruirait les livres.", "Cluny : 910. Fontenay : 1118."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", S8, [S1, S2, S4], pos=2)),
    }
    d["e3-2"] = {
        "mousse": trous(
            "Complète le texte : clique sur une étiquette, puis sur le trou où elle va. Une étiquette est en trop.",
            "Il n'y a pas d'imprimerie : les livres sont recopiés à la [[main]]. Le moine écrit sur du [[parchemin]], une peau d'animal préparée, avec une [[plume]] d'oie.",
            ["main", "parchemin", "plume", "stylo"],
            ["Ouvre la fiche " + F + ".", "Le parchemin est une peau d'animal.", "Le stylo n'existe pas au Moyen Âge."]),
        "lieutenant": ordre(
            "Frère Anselme explique comment naît un livre. Remets les cinq étapes dans l'ordre, puis choisis la phrase de la fiche qui décrit le travail du copiste.",
            ["Le parcheminier prépare les peaux : c'est le parchemin.", "Le copiste trace des lignes, puis écrit à la plume d'oie.", "Le rubricateur ajoute en rouge les titres.", "L'enlumineur peint les lettrines.", "Le relieur assemble les cahiers entre deux plats de bois."],
            ["On prépare le support avant d'écrire.", "On écrit avant de décorer.", "On relie à la fin."],
            J("Quelle phrase de la fiche décrit le travail du copiste ?", S4, [S3, S5, S6], pos=0)),
        "second": tri(
            "Frère Anselme classe les métiers du livre selon leur outil ou leur matière. Range chaque carte dans la bonne colonne, puis choisis la phrase de la fiche qui parle du rouge.",
            [("peau", "Prépare ou assemble le support"), ("ecrit", "Écrit ou décore")],
            [("Le parcheminier prépare les peaux", "peau"), ("Le relieur assemble les cahiers entre deux plats de bois", "peau"), ("Le copiste écrit à la plume d'oie", "ecrit"), ("Le rubricateur ajoute les titres en rouge", "ecrit"), ("L'enlumineur peint les lettrines", "ecrit"), ("Le canif gratte les erreurs", "ecrit")],
            ["Le parcheminier et le relieur travaillent sur le support.", "Les autres écrivent ou décorent.", "« Rubrique » vient du mot « rouge »."],
            J("Quelle phrase de la fiche parle du rouge ?", S5, [S3, S6, S7], pos=1)),
    }
    d["e3-3"] = {
        "mousse": assoc(
            "Relie chaque lieu à ce qu'on y fait : clique sur un lieu, puis sur sa phrase.",
            [("Le scriptorium", "on y recopie les livres"), ("L'école de l'abbaye", "les moines apprennent à lire"), ("L'école de la cathédrale", "on y forme auprès de l'évêque")],
            ["Ouvre la fiche " + F + ".", "Le scriptorium est la salle où l'on copie.", "La cathédrale est l'église de l'évêque."]),
        "lieutenant": qcm(
            carnet("La plainte d'un copiste", "(au bas d'une page de manuscrit, traduction adaptée). « Celui qui ne sait pas écrire croit que ce n'est pas un travail. Trois doigts tiennent la plume, mais tout le corps peine. »")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("Que dit le copiste de son travail ?", ["Il est pénible, même si on ne le croit pas", "Il est facile", "Il est inutile", "Il est payé très cher"], 0, "« Tout le corps peine. »"),
             ("Combien de doigts tiennent la plume ?", ["Trois", "Un", "Cinq", "Deux"], 0, "Trois doigts."),
             ("Pourquoi les copistes sont-ils importants pour nous aujourd'hui ?", ["Grâce à eux, des textes de l'Antiquité sont parvenus jusqu'à nous", "Ils ont inventé l'imprimerie", "Ils ont bâti les cathédrales", "Ils ont écrit toutes les lois"], 0, "Ils ont recopié des textes anciens.")],
            ["Relis la plainte : « tout le corps peine ».", "Trois doigts tiennent la plume.", "Pense à ce que les copistes nous ont transmis."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", S10, [S4, S9, S11], pos=1)),
        "second": vf(
            "Frère Anselme a noté six phrases sur l'enseignement au Moyen Âge. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui décrit les lieux d'enseignement.",
            [("Il n'existe pas d'école publique.", True, "L'enseignement est assuré par l'Église."), ("Les écoles monastiques sont dans les abbayes.", True, "Les moines enseignent."), ("Les écoles cathédrales sont auprès des évêques.", True, "Elles forment surtout les futurs prêtres."),
             ("Les premières universités apparaissent au XIIe siècle.", False, "Au XIIIe siècle."), ("On y apprend d'abord le latin.", True, "La langue de l'Église et des livres."), ("L'État organise l'école.", False, "C'est l'Église.")],
            ["L'Église assure l'enseignement.", "Les universités apparaissent plus tard : XIIIe siècle.", "Le latin est la langue des livres."],
            J("Quelle phrase de la fiche décrit les lieux d'enseignement ?", S9, [S10, S11, S2], pos=2)),
    }
    d["e3-4"] = {
        "lieutenant": code(
            "L'armoire aux livres est fermée par un cadenas à deux roues. Combien d'années séparent la fondation de Cluny (910) de celle de Fontenay (1118) ? Combien d'étapes compte la fabrication d'un manuscrit, du parcheminier au relieur ? Écris les deux nombres.",
            [("Années entre Cluny et Fontenay", "208", 3), ("Étapes de fabrication d'un manuscrit", "5", 1)],
            ["1118 − 910.", "Compte les métiers : parcheminier, copiste, rubricateur, enlumineur, relieur.", "Le relieur est le dernier."],
            J("Quelle phrase de la fiche donne les deux dates de fondation ?", S2, [S1, S3, S9], pos=2)),
        "second": code(
            "L'armoire aux livres est fermée par un cadenas à trois roues. De quel siècle date Cluny (910) ? Combien de siècles séparent 910 des premières universités (XIIIe siècle) ? Combien de grandes activités se partagent la journée selon la règle des moines (prière, travail, lecture) ? Écris les trois nombres.",
            [("Siècle de la fondation de Cluny (en chiffres)", "10", 2), ("Siècles entre le Xe et le XIIIe siècle", "3", 1), ("Activités de la règle", "3", 1)],
            ["910 est au Xe siècle.", "XIII − X.", "Prière, travail, lecture."],
            J("Quelle phrase de la fiche donne les trois activités de la règle ?", S1, [S2, S9, S4], pos=1)),
    }
    return d
