"""Salle 4 « Le cabinet du Grand Tunnel » (fiche : digestion)."""
from aide import *

F = "« Le trajet des aliments »"
D1 = "Le tube digestif comprend la bouche, l'œsophage, l'estomac, l'intestin grêle et le gros intestin."
D2 = "Des organes annexes, comme le foie et le pancréas, fabriquent des liquides qui aident la digestion, sans que les aliments les traversent."
D3 = "Les aliments sont transformés en nutriments, assez petits pour passer dans le sang à travers la paroi de l'intestin grêle, long d'environ 6 m."
D4 = "Le gros intestin récupère de l'eau et forme les excréments."
D5 = "Le sang les emporte ensuite vers tous les organes."
D6 = "La digestion d'un repas dure plusieurs heures."
D7 = "Les aliments ne passent jamais par le cœur ni par les poumons, ni dans le foie : celui-ci aide la digestion sans être traversé."


def donnees(svg, bloc=None):
    d = {}
    d["e4-1"] = {
        "mousse": ordre(
            "La docteure Inès montre le voyage d'une bouchée. Remets les étapes dans l'ordre : le début en haut. Utilise les flèches ▲ et ▼, puis vérifie.",
            ["La bouche", "L'œsophage", "L'estomac", "L'intestin grêle"],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Tout commence par la bouche.", "L'intestin grêle vient après l'estomac."]),
        "lieutenant": qcm(
            "La docteure Inès montre sa maquette du corps, vue de face (repères 1 à 6). Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2." + svg("e4-1", "timonier"),
            [("Quel repère montre l'organe où les nutriments passent dans le sang ?", ["Le repère 5 : l'intestin grêle", "Le repère 1 : l'estomac", "Le repère 3 : le gros intestin", "Le repère 6 : le foie"], 0, "Ils traversent la paroi de l'intestin grêle."),
             ("Quel repère montre un organe que les aliments ne traversent pas ?", ["Le repère 6 : le foie", "Le repère 4 : l'œsophage", "Le repère 1 : l'estomac", "Le repère 5 : l'intestin grêle"], 0, "Le foie aide la digestion sans être traversé."),
             ("Quel repère montre l'organe qui récupère l'eau et forme les excréments ?", ["Le repère 3", "Le repère 5", "Le repère 1", "Le repère 2"], 0, "C'est le gros intestin.")],
            ["Suis le tube de la bouche vers le bas.", "Le foie n'est pas sur le tube digestif.", "Le gros intestin forme un cadre autour de l'intestin grêle."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", D2, [D1, D4, D6], pos=1)),
        "second": tri(
            "Inès classe les organes de sa maquette. Range chaque organe dans la bonne colonne, puis choisis la phrase de la fiche qui définit les organes annexes.",
            [("tube", "Tube digestif"), ("annexe", "Organe annexe (aide la digestion)"), ("autre", "Hors du trajet des aliments (circulation, respiration)")],
            [("La bouche", "tube"), ("L'estomac", "tube"), ("L'intestin grêle", "tube"), ("Le foie", "annexe"), ("Le pancréas", "annexe"), ("Le cœur", "autre"), ("Les poumons", "autre")],
            ["Les aliments traversent le tube digestif.", "Le foie et le pancréas fabriquent des liquides.", "Le cœur et les poumons ne sont pas sur le trajet."],
            J("Quelle phrase de la fiche définit les organes annexes ?", D2, [D1, D7, D3], pos=0)),
    }
    d["e4-2"] = {
        "mousse": assoc(
            "Relie chaque organe à son travail. Clique sur un organe, puis sur son travail.",
            [("La bouche", "mâcher les aliments"), ("L'estomac", "brasser les aliments en bouillie"), ("L'intestin grêle", "faire passer les nutriments dans le sang")],
            ["Ouvre la fiche " + F + ".", "L'estomac est une poche qui brasse.", "Les nutriments passent dans le sang dans l'intestin grêle."]),
        "lieutenant": ordre(
            "Inès décrit la transformation d'un repas. Remets dans l'ordre ces cinq étapes, puis choisis la phrase de la fiche qui donne la longueur de l'intestin grêle.",
            ["Les aliments sont mâchés et mouillés dans la bouche.", "Ils descendent par l'œsophage jusqu'à l'estomac.", "L'estomac les brasse en bouillie.",
             "Dans l'intestin grêle, les nutriments passent dans le sang.", "Le gros intestin récupère l'eau et forme les excréments."],
            ["Suis le trajet de la bouche à la fin du tube.", "Les nutriments passent dans le sang avant le gros intestin.", "Le gros intestin est le dernier organe du tube."],
            J("Quelle phrase de la fiche donne la longueur de l'intestin grêle ?", D3, [D4, D2, D6], pos=0)),
        "second": qcm(
            carnet("Notes d'Inès sur la maquette", "(d'après la fiche). L'intestin grêle déplié mesure environ 6 m chez un adulte. Un enfant de 10 ans mesure 1,40 m. Un repas met plusieurs heures à être digéré.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 1.",
            [("L'intestin grêle déplié mesure environ 6 m. Environ combien de fois la taille d'un enfant de 1,40 m ?", ["4 fois", "2 fois", "10 fois", "1 fois"], 0, "6 ÷ 1,4 est proche de 4."),
             ("Pourquoi une paroi de l'intestin grêle est-elle importante ?", ["Les nutriments la traversent pour passer dans le sang", "Elle fabrique la salive", "Elle pompe le sang", "Elle broie les aliments"], 0, "Les nutriments passent dans le sang à travers la paroi."),
             ("La digestion d'un repas dure…", ["plusieurs heures", "quelques secondes", "exactement une minute", "plusieurs semaines"], 0, "Elle dure plusieurs heures.")],
            ["Divise 6 m par 1,4 m.", "Les nutriments sont petits pour traverser la paroi.", "Pense au temps entre un repas et le suivant."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 1 ?", D3, [D4, D1, D6], pos=1)),
    }
    d["e4-3"] = {
        "mousse": vf(
            "La docteure Inès fait trois affirmations. Pour chacune, clique sur « Vrai » ou sur « Faux », puis vérifie.",
            [("Les aliments passent dans l'estomac.", True, "Après l'œsophage."), ("Les aliments passent dans le cœur.", False, "Le cœur pompe le sang."), ("Le gros intestin est le dernier organe du tube.", True, "Il forme les excréments.")],
            ["Ouvre la fiche " + F + ".", "Le cœur n'est pas sur le tube digestif.", "Le tube se termine par le gros intestin."]),
        "lieutenant": vf(
            "Inès fait cinq affirmations sur le trajet des aliments. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui montre que les aliments ne passent pas dans le foie.",
            [("Les aliments passent par le foie.", False, "Le foie aide la digestion sans être traversé."), ("Le foie et le pancréas fabriquent des liquides qui aident la digestion.", True, "Ce sont des organes annexes."),
             ("L'intestin grêle mesure environ 6 m.", True, "Il est long et replié."), ("Les nutriments traversent la paroi du gros intestin pour passer dans le sang.", False, "C'est la paroi de l'intestin grêle."),
             ("Le gros intestin récupère de l'eau.", True, "Et forme les excréments.")],
            ["Un organe annexe n'est pas traversé par les aliments.", "Les nutriments passent dans l'intestin grêle.", "Pour la justification : cherche la phrase qui parle de cœur, de poumons et de foie."],
            J("Quelle phrase de la fiche montre que les aliments ne passent pas dans le foie ?", D7, [D2, D3, D4], pos=2)),
        "second": vf(
            "Inès a noté six phrases dans son carnet. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui dit ce que devient ce qui n'a pas été utilisé.",
            [("Les aliments sont transformés en nutriments pendant la digestion.", True, "Ils deviennent assez petits pour passer dans le sang."), ("Les nutriments passent dans le sang dans l'estomac.", False, "C'est dans l'intestin grêle."),
             ("Ce qui n'a pas été utilisé continue sa route dans le gros intestin.", True, "Puis il est rejeté."), ("Le sang emporte les nutriments vers tous les organes.", True, "C'est la circulation."),
             ("Les aliments passent par le cœur et par les poumons.", False, "Jamais."), ("La digestion d'un repas dure quelques secondes.", False, "Elle dure plusieurs heures.")],
            ["Le sang emporte les nutriments vers les organes.", "Ce qui n'est pas utilisé continue sa route.", "Une digestion complète prend du temps."],
            J("Quelle phrase de la fiche dit ce que devient ce qui n'a pas été utilisé ?", "Ce qui n'a pas été utilisé continue sa route dans le gros intestin, puis est rejeté.", [D5, D4, D6], pos=2)),
    }
    d["e4-4"] = {
        "lieutenant": intrus(
            "Les aliments passent dans quatre de ces organes, mais pas dans le cinquième. Trouve l'intrus, puis choisis la phrase de la fiche qui le justifie.",
            [("La bouche", False), ("L'œsophage", False), ("L'estomac", False), ("Le pancréas", True), ("L'intestin grêle", False)],
            ["Un organe annexe fabrique un liquide, mais ne laisse rien passer.", "Le tube digestif commence à la bouche.", "Le foie et le pancréas sont des organes annexes."],
            J("Quelle phrase de la fiche justifie ton choix ?", D2, [D1, D3, D6], pos=1)),
        "second": assoc(
            "Inès termine par un dernier tableau. Relie chaque organe à son rôle précis, puis choisis la phrase de la fiche qui énumère le tube digestif.",
            [("Le pancréas", "fabrique un liquide qui aide la digestion, sans être traversé"), ("Le foie", "aide la digestion sans que les aliments le traversent"),
             ("L'intestin grêle", "d'environ 6 m, les nutriments y passent dans le sang"), ("Le gros intestin", "récupère de l'eau et forme les excréments"),
             ("L'œsophage", "conduit la bouchée de la bouche à l'estomac")],
            ["Deux organes annexes : un liquide, mais pas de passage des aliments.", "L'intestin grêle est long et replié.", "Le gros intestin est le dernier organe du tube."],
            J("Quelle phrase de la fiche énumère le tube digestif ?", D1, [D2, D4, D7], pos=0)),
    }
    return d
