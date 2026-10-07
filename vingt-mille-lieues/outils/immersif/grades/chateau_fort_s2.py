"""Salle 2 « Les remparts » (fiche : les-defenses)."""
from aide import *

F = "« Les défenses du château »"
B1 = "Un château fort est conçu pour ralentir et arrêter l'assaillant, obstacle après obstacle."
B2 = "Douves : fossé, sec ou en eau, qui tient à distance les hommes et les machines de siège."
B3 = "Pont-levis : pont mobile dont le tablier se relève pour fermer l'accès."
B4 = "Herse : grille de bois et de fer qui coulisse de haut en bas et double le pont-levis."
B5 = "Chemin de ronde : passage au sommet des murs, protégé par des créneaux et des merlons."
B6 = "Mâchicoulis : galerie en surplomb dont le sol est percé, pour lâcher des projectiles à la verticale sur ceux qui sapent le pied du mur."
B7 = "Meurtrières ou archères : ouvertures étroites pour observer et tirer à l'abri."
B8 = "Le mot vient du latin dominus, « le seigneur » : le donjon est la tour maîtresse, résidence du seigneur et ultime refuge."
B9 = "Il n'est pas d'abord une prison, même si l'on a parfois enfermé des prisonniers dans des tours."
B10 = "Attention : il n'existe pas un seul modèle. Tous les châteaux n'ont pas toutes ces défenses, et elles apparaissent à des époques différentes."


def donnees(svg, bloc=None):
    d = {}
    d["e2-1"] = {
        "mousse": assoc(
            "Observe le plan du château vu de dessus, puis relie chaque élément à ce qu'il est. Clique sur un élément, puis sur sa description.\n" + svg("e2-1", "matelot"),
            [("le donjon", "la grande tour au centre"), ("les douves", "le fossé plein d'eau"), ("le pont-levis", "le pont devant l'entrée")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Le donjon est la tour la plus importante.", "Les douves sont pleines d'eau."]),
        "lieutenant": qcm(
            "Colin a dessiné le plan du château vu de dessus (repères 1 à 6). Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2." + svg("e2-1", "timonier"),
            [("Quel repère montre l'ouvrage qui double le pont-levis, juste derrière le passage ?", ["Le repère 5 : la herse", "Le repère 2 : les douves", "Le repère 4 : l'enceinte", "Le repère 1 : le donjon"], 0, "La herse est une grille."),
             ("Quel repère montre ce qui tient les hommes et les machines à distance du mur ?", ["Le repère 2 : les douves", "Le repère 6 : une tour", "Le repère 3 : le pont-levis", "Le repère 1 : le donjon"], 0, "Le fossé tient à distance."),
             ("Pourquoi un château n'a-t-il pas un seul obstacle ?", ["Pour ralentir l'assaillant obstacle après obstacle", "Pour décorer le plan", "Parce que le roi l'exige", "Pour loger plus de monde"], 0, "Défense en profondeur.")],
            ["La herse est derrière le pont-levis.", "Les douves sont autour du mur.", "Un seul obstacle ne suffit pas à arrêter un assaillant."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", B2, [B1, B4, B5], pos=2)),
        "second": qcm(
            carnet("Rapport de Colin", "(inventé pour le jeu). Un assaillant arrive à l'entrée : devant lui, des douves, puis un pont-levis relevé. Derrière la porte, une herse. Autour du château, une enceinte flanquée de tours, au sommet de laquelle court un chemin de ronde.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("Combien d'obstacles l'assaillant doit-il franchir avant d'atteindre la cour ?", ["4 : douves, pont-levis, herse, enceinte", "1", "2", "7"], 0, "Chaque ouvrage est un obstacle."),
             ("Pourquoi le pont-levis relevé arrête-t-il l'assaillant ?", ["Le fossé reste entre lui et la porte", "Il casse la porte", "Il éteint les torches", "Il appelle le roi"], 0, "Relevé, il ferme l'accès."),
             ("Pourquoi le chemin de ronde est-il utile aux défenseurs ?", ["Il permet de circuler au sommet des murs pour surveiller et défendre", "Il sert à stocker du blé", "Il relie le village au moulin", "Il loge les paysans"], 0, "Passage au sommet des murs.")],
            ["Compte les ouvrages sur le trajet.", "Le pont-levis fait partie des obstacles.", "Le chemin de ronde se trouve au sommet des murs."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", B5, [B3, B4, B7], pos=1)),
    }
    d["e2-2"] = {
        "mousse": tri(
            "Josselin range les défenses. Range chaque défense : elle ferme le passage, ou elle sert à tirer et à observer. Clique sur une carte, puis sur une colonne.",
            [("fermer", "Elle ferme le passage"), ("tirer", "Elle sert à tirer et à observer")],
            [("La herse", "fermer"), ("Le pont-levis relevé", "fermer"), ("La meurtrière", "tirer"), ("Le chemin de ronde", "tirer")],
            ["Ouvre la fiche " + F + ".", "La herse est une grille qui descend.", "La meurtrière est une fente étroite dans le mur."]),
        "lieutenant": tri(
            "Josselin classe les défenses selon l'endroit où elles agissent. Range chaque carte dans la bonne colonne, puis choisis la phrase de la fiche qui définit les mâchicoulis.",
            [("loin", "Tient l'ennemi à distance"), ("porte", "Ferme l'entrée"), ("mur", "Défend le mur")],
            [("Les douves", "loin"), ("Les tours qui flanquent l'enceinte", "loin"), ("Le pont-levis relevé", "porte"), ("La herse", "porte"), ("Les mâchicoulis", "mur"), ("Les meurtrières", "mur")],
            ["Les douves sont autour du château.", "Le pont-levis et la herse ferment l'entrée.", "Les mâchicoulis et les meurtrières sont dans le mur."],
            J("Quelle phrase de la fiche définit les mâchicoulis ?", B6, [B7, B5, B2], pos=0)),
        "second": ordre(
            "Un assaillant essaie d'entrer. Remets dans l'ordre les obstacles qu'il rencontre, de l'extérieur vers l'intérieur, puis choisis la phrase de la fiche qui justifie cet ordre.",
            ["Les douves", "Le pont-levis", "La herse", "L'enceinte et son chemin de ronde", "Le donjon"],
            ["On commence par ce qui est le plus loin du mur.", "La herse double le pont-levis.", "Le donjon est l'ultime refuge."],
            J("Quelle phrase de la fiche justifie cet enchaînement d'obstacles ?", B1, [B8, B3, B10], pos=1)),
    }
    d["e2-3"] = {
        "mousse": vf(
            "Pour chaque phrase, clique sur « Vrai » ou sur « Faux », puis vérifie.",
            [("Le pont-levis se relève pour fermer l'entrée.", True, "Relevé, il bouche l'entrée."), ("Le donjon est d'abord une prison.", False, "C'est la tour du seigneur."), ("Les douves sont un fossé.", True, "Elles tiennent l'ennemi loin.")],
            ["Ouvre la fiche " + F + ".", "Le donjon est la tour maîtresse.", "Les douves sont creusées autour du château."]),
        "lieutenant": vf(
            "Colin a noté cinq phrases. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui corrige l'idée « le donjon est une prison ».",
            [("Le mot donjon vient du latin dominus, « le seigneur ».", True, "C'est la tour du seigneur."), ("Le donjon est d'abord une prison.", False, "C'est la résidence du seigneur."), ("Tous les châteaux ont toutes les défenses.", False, "Il n'existe pas un seul modèle."),
             ("Le donjon est l'ultime refuge.", True, "Après la défaite des murs."), ("Des prisonniers ont parfois été enfermés dans des tours.", True, "Mais ce n'est pas son rôle premier.")],
            ["Dominus signifie « seigneur ».", "Chaque château a son plan.", "Pour la justification : cherche la phrase qui nie la prison."],
            J("Quelle phrase de la fiche corrige l'idée « le donjon est une prison » ?", B9, [B8, B10, B1], pos=2)),
        "second": vf(
            "Colin a noté six phrases sur la défense du château. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui corrige l'idée « tous les châteaux se ressemblent ».",
            [("Les mâchicoulis servent à lâcher des projectiles à la verticale.", True, "Sur ceux qui sapent le pied du mur."), ("Une meurtrière sert à observer et à tirer à l'abri.", True, "Ouverture étroite."),
             ("La herse remplace le pont-levis.", False, "Elle le double."), ("Les douves existent toujours en eau.", False, "Elles peuvent être sèches."),
             ("Les défenses apparaissent toutes au même moment.", False, "À des époques différentes."), ("Tous les châteaux ont toutes ces défenses.", False, "Il n'existe pas un seul modèle.")],
            ["La herse double le pont-levis.", "Un fossé peut être sec ou en eau.", "Les défenses évoluent avec les siècles."],
            J("Quelle phrase de la fiche corrige l'idée « tous les châteaux se ressemblent » ?", B10, [B1, B6, B4], pos=0)),
    }
    d["e2-4"] = {
        "lieutenant": code(
            "Le treuil de la herse est bloqué par un cadenas à mots. Écris les deux mots demandés (les accents ne comptent pas), puis ouvre.",
            [("Ouverture étroite dans le mur pour observer et tirer à l'abri (10 lettres)", "MEURTRIERE", 10, False), ("Muraille qui entoure le château (8 lettres)", "ENCEINTE", 8, False)],
            ["Les deux mots sont dans la fiche « Les défenses du château ».", "Le premier commence par M et finit par E.", "Le second commence par E."],
            J("Quelle phrase de la fiche définit le premier mot ?", B7, [B6, B5, B3], pos=1)),
        "second": code(
            "Le treuil de la herse est bloqué par un cadenas. Combien d'obstacles un assaillant franchit-il avant la cour (douves, pont-levis, herse, enceinte) ? Quel est le mot de 11 lettres pour la galerie en surplomb dont le sol est percé ? Écris-les pour ouvrir (les accents ne comptent pas).",
            [("Nombre d'obstacles", "4", 1), ("Galerie en surplomb dont le sol est percé", "MACHICOULIS", 11, False)],
            ["Compte douves, pont-levis, herse, enceinte.", "Le mot commence par M et finit par S.", "Le mot est dans la fiche, avec la définition « galerie en surplomb »."],
            J("Quelle phrase de la fiche donne la définition du mot ?", B6, [B7, B5, B2], pos=2)),
    }
    return d
