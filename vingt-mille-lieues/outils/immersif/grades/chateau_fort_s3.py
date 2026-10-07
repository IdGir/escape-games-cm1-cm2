"""Salle 3 « La grande salle » (fiche : vie-du-seigneur)."""
from aide import *

F = "« La vie au château »"
V1 = "Le château loge le seigneur, sa famille et toute une maisonnée : pages et écuyers (jeunes nobles en formation), chevaliers et hommes d'armes, chapelain, cuisiniers, palefreniers, servantes."
V2 = "La grande salle (ou salle d'honneur) est le cœur de la vie : on y mange, on y reçoit, on y juge."
V3 = "Elle dirige la maison, les réserves et les comptes, surveille l'éducation des enfants et, en l'absence de son époux, parti à la guerre ou auprès du roi, elle gouverne le domaine."
V4 = "Certaines femmes héritent elles-mêmes d'une seigneurie, comme Aliénor d'Aquitaine au XIIe siècle."
V5 = "Le seigneur commande, protège et juge les habitants de sa seigneurie."
V6 = "Le château est la marque visible de ce pouvoir : sa hauteur, ses tours, son blason peint au-dessus de la porte, ses fêtes, ses chasses et ses tournois affichent la richesse et le rang de la famille."
V7 = "Retiens les trois fonctions du château fort : lieu de protection, lieu de vie du seigneur, symbole de sa puissance."
V8 = "Le calendrier des Très Riches Heures s'ouvre sur un banquet : le duc de Berry reçoit à sa table, entouré de ses invités et de ses serviteurs."


def donnees(svg, bloc=None):
    d = {}
    d["e3-1"] = {
        "mousse": tri(
            "Dame Aliénor range ce qu'on trouve au château. Range chaque carte : elle sert à se défendre, ou à vivre. Clique sur une carte, puis sur une colonne.",
            [("def", "Se défendre"), ("vie", "Vivre au château")],
            [("La herse", "def"), ("Les meurtrières", "def"), ("Les cuisines", "vie"), ("La chapelle", "vie")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Ce qui arrête l'ennemi sert à se défendre.", "On mange et on prie dans la colonne « Vivre »."]),
        "lieutenant": qcm(
            carnet("Les Très Riches Heures du duc de Berry", "(vers 1411-1416). Le mois de janvier montre un banquet : le duc reçoit à sa table, entouré de ses invités et de ses serviteurs. Une image faite pour montrer sa richesse.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("Où se passe un banquet comme celui-ci au château ?", ["Dans la grande salle", "Dans les douves", "Sur le chemin de ronde", "Au moulin"], 0, "On y mange, on y reçoit, on y juge."),
             ("Pourquoi cette image est-elle faite ?", ["Pour montrer la richesse du seigneur", "Pour apprendre à cuisiner", "Pour dater le château", "Pour indiquer les prix"], 0, "Le banquet affiche le rang."),
             ("Quelle fonction du château l'image illustre-t-elle surtout ?", ["Le symbole de puissance", "La protection", "Le logement des paysans", "Le marché"], 0, "Fêtes et banquets affichent la richesse.")],
            ["Le banquet se tient dans la pièce principale.", "Le duc est entouré de ses invités et de ses serviteurs.", "Les fêtes affichent la richesse et le rang."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", V6, [V2, V7, V1], pos=1)),
        "second": tri(
            "Dame Aliénor classe les éléments du château selon leur fonction. Range chaque carte dans la bonne colonne, puis choisis la phrase de la fiche qui énumère les trois fonctions.",
            [("pro", "Protection"), ("vie", "Vie du seigneur"), ("pui", "Symbole de puissance")],
            [("Le donjon, ultime refuge", "pro"), ("L'enceinte et ses tours", "pro"), ("La grande salle et ses repas", "vie"), ("Les chambres et la chapelle", "vie"), ("Le blason peint au-dessus de la porte", "pui"), ("Les tournois et les fêtes", "pui")],
            ["Trois fonctions : protéger, vivre, montrer.", "Le blason et les fêtes affichent le rang.", "Le donjon protège en dernier recours."],
            J("Quelle phrase de la fiche énumère les trois fonctions du château ?", V7, [V6, V2, V5], pos=2)),
    }
    d["e3-2"] = {
        "mousse": qcm(
            "Lis la question, clique sur la bonne réponse, puis vérifie.",
            [("Où le seigneur reçoit-il ses invités et prend-il ses repas ?", ["Dans la grande salle", "Dans les douves", "Dans le moulin"], 0, "La grande salle est le cœur de la vie.")],
            ["Ouvre la fiche " + F + ".", "C'est la plus grande pièce du donjon.", "On y mange, on y reçoit."]),
        "lieutenant": tri(
            "Dame Aliénor classe les gens du château. Range chaque personne : jeune noble en formation ou personnel de la maison ? Puis choisis la phrase de la fiche qui énumère les habitants du château.",
            [("jeune", "Jeune noble en formation"), ("maison", "Personnel de la maison")],
            [("Un page", "jeune"), ("Un écuyer", "jeune"), ("Un cuisinier", "maison"), ("Un palefrenier", "maison"), ("Une servante", "maison"), ("Un chapelain", "maison")],
            ["Les pages et les écuyers sont de jeunes nobles.", "Le palefrenier s'occupe des chevaux.", "Le chapelain assure les offices religieux."],
            J("Quelle phrase de la fiche énumère les habitants du château ?", V1, [V2, V5, V7], pos=0)),
        "second": qcm(
            carnet("Journal de Colin", "(inventé pour le jeu). « Aujourd'hui, le seigneur est parti auprès du roi. Dame Aliénor dirige la maison, les réserves et les comptes, et elle rend la justice dans la grande salle. »")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 1.",
            [("Qui gouverne le domaine pendant l'absence du seigneur ?", ["La dame du château", "Le meunier", "Le roi", "Les paysans"], 0, "Elle gouverne le domaine."),
             ("Où Dame Aliénor rend-elle la justice ?", ["Dans la grande salle", "Au moulin", "Dans la chapelle seulement", "Au village"], 0, "On y juge."),
             ("Une femme peut-elle posséder une seigneurie ?", ["Oui : certaines en héritent", "Non, jamais", "Seulement une veuve du roi", "Seulement si elle est chevalier"], 0, "Comme Aliénor d'Aquitaine au XIIe siècle.")],
            ["Le seigneur est absent : qui le remplace ?", "La grande salle sert à juger.", "Certaines femmes héritent elles-mêmes d'une seigneurie."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 1 ?", V3, [V4, V2, V5], pos=1)),
    }
    d["e3-3"] = {
        "mousse": vf(
            "Pour chaque phrase, clique sur « Vrai » ou sur « Faux », puis vérifie.",
            [("Un page est un jeune garçon noble au service du seigneur.", True, "Il apprend le métier de chevalier."), ("La dame du château ne s'occupe que de sa toilette.", False, "Elle dirige la maison."), ("Au château vivent aussi des cuisiniers.", True, "C'est une grande maison.")],
            ["Ouvre la fiche " + F + ".", "Colin est un page.", "Un château est une grande maison : qui cuisine ?"]),
        "lieutenant": vf(
            "Dame Aliénor affirme cinq choses sur la vie au château. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui dit ce que fait la dame en l'absence du seigneur.",
            [("La dame dirige la maison, les réserves et les comptes.", True, "C'est son rôle."), ("En l'absence du seigneur, la dame gouverne le domaine.", True, "Elle le remplace."),
             ("La dame n'a aucun pouvoir.", False, "Elle gouverne en l'absence de son époux."), ("Aliénor d'Aquitaine a hérité d'une seigneurie au XIIe siècle.", True, "Certaines femmes héritent."),
             ("Le château n'abrite que le seigneur.", False, "Une maisonnée entière y vit.")],
            ["La dame dirige la maison.", "Certaines femmes héritent d'une seigneurie.", "Pour la justification : cherche la phrase qui parle de l'absence de l'époux."],
            J("Quelle phrase de la fiche dit ce que fait la dame en l'absence du seigneur ?", V3, [V4, V1, V5], pos=2)),
        "second": ordre(
            "Colin explique comment un jeune noble devient chevalier. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche qui définit le page.",
            ["Le jeune garçon noble entre au service d'un seigneur : il est page.", "Il apprend le métier de chevalier au château.", "Il devient écuyer.", "Il devient chevalier."],
            ["Le page est le plus jeune.", "L'écuyer est entre le page et le chevalier.", "Le chevalier est l'aboutissement de la formation."],
            J("Quelle phrase de la fiche cite le page et l'écuyer ?", V1, [V3, V4, V6], pos=1)),
    }
    d["e3-4"] = {
        "lieutenant": intrus(
            "Quatre de ces activités montrent la puissance du seigneur. Une seule n'en fait pas partie. Trouve l'intrus, puis choisis la phrase de la fiche qui justifie ton choix.",
            [("Rendre la justice", False), ("Organiser un tournoi", False), ("Afficher son blason au-dessus de la porte", False), ("Faire construire un grand château visible de loin", False), ("Labourer lui-même ses champs", True)],
            ["Le château est la marque visible du pouvoir du seigneur.", "Le seigneur commande et juge.", "Qui travaille la terre de la seigneurie ?"],
            J("Quelle phrase de la fiche justifie ton choix ?", V6, [V5, V2, V7], pos=1)),
        "second": vf(
            "Dame Aliénor termine par six phrases. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui résume les fonctions du château.",
            [("Le château est un lieu de protection.", True, "Enceinte, tours, herse, donjon."), ("Le château est un lieu de vie du seigneur.", True, "Grande salle, chambres, chapelle, cuisines."),
             ("Le château est un symbole de puissance.", True, "Blason, fêtes, tournois."), ("Le château ne sert qu'à se défendre.", False, "Il sert aussi à vivre et à montrer."),
             ("Le seigneur commande, protège et juge les habitants.", True, "Il exerce le pouvoir."), ("Le seigneur est élu par les habitants.", False, "Son pouvoir vient de sa terre.")],
            ["Trois fonctions à retenir.", "Le château ne sert pas qu'à la guerre.", "Le seigneur n'est pas élu."],
            J("Quelle phrase de la fiche résume les fonctions du château ?", V7, [V6, V2, V5], pos=0)),
    }
    return d
