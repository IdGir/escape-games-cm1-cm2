"""Salle 5 « Le bureau du carnet de naissance » : grades mousse, lieutenant, second (fiche : Classer les animaux du zoo)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "naissances-animaux", "tests", "donnees"))
from fiches import *
from gen_enigmes import DOC5

FICHE = "« Classer les animaux du zoo »"


def donnees(svg, bloc=None):
    d = {}
    d["e5-1"] = {
        "mousse": tri(
            "Sacha refait les panneaux des enclos. Pour chaque animal : il pond des œufs, ou le petit naît vivant ?",
            [("ovi", "Il pond des œufs"), ("vivi", "Le petit naît vivant")],
            [("la poule", "ovi"), ("la tortue", "ovi"), ("la grenouille", "ovi"), ("le lion", "vivi"), ("la girafe", "vivi"), ("le dauphin", "vivi")],
            ["Ouvre la fiche " + FICHE + ".", "Le dauphin est un mammifère.", "La tortue pond sur la plage."]),
        "lieutenant": tri(
            "Sacha refait le grand tableau du zoo avec dix animaux. Place chacun dans la bonne case, puis choisis la phrase de la fiche qui donne les trois grands cas.",
            [("ext-ovi", "Fécondation externe, ovipare"), ("int-ovi", "Fécondation interne, ovipare"), ("int-vivi", "Fécondation interne, vivipare")],
            [("le crapaud", "ext-ovi"), ("la truite", "ext-ovi"), ("le saumon", "ext-ovi"), ("le manchot", "int-ovi"), ("le crocodile", "int-ovi"), ("le papillon", "int-ovi"),
             ("le kangourou", "int-vivi"), ("le zèbre", "int-vivi"), ("la chauve-souris", "int-vivi"), ("le dauphin", "int-vivi")],
            ["Le manchot est un oiseau.", "Le kangourou est un mammifère.", "Pour la justification : cherche « trois grands cas »."],
            J("Quelle phrase de la fiche donne les trois grands cas ?", K_TROIS, [K_DEUX, K_METHODE, K_INT_VIVI], pos=1)),
        "second": tri(
            "Sacha ajoute une colonne pour les animaux qui ne suivent pas la règle de leur groupe. Range chaque animal, puis choisis la phrase de la fiche sur les exceptions.",
            [("ext-ovi", "Fécondation externe, ovipare"), ("int-ovi", "Fécondation interne, ovipare"), ("int-vivi", "Fécondation interne, vivipare"), ("exc", "Exception dans son groupe")],
            [("la grenouille", "ext-ovi"), ("le saumon", "ext-ovi"), ("l'autruche", "int-ovi"), ("la tortue", "int-ovi"),
             ("la girafe", "int-vivi"), ("le lion", "int-vivi"), ("l'ornithorynque", "exc"), ("la vipère aspic", "exc")],
            ["L'ornithorynque est un mammifère qui pond.", "La vipère aspic : œufs éclos dans le ventre.", "Pour la justification : cherche « divers »."],
            J("Quelle phrase de la fiche parle des exceptions ?", K_REGLE, [K_IMPOSSIBLE, K_TROIS, K_OISEAUX], pos=2)),
    }
    d["e5-2"] = {
        "mousse": assoc(
            "Relie chaque petit à sa maman.",
            [("le têtard", "la grenouille"), ("le poussin", "la poule"), ("le chaton", "la chatte")],
            ["Ouvre la fiche " + FICHE + ".", "Le têtard vit dans la mare.", "Le poussin sort d'un œuf de poule."]),
        "lieutenant": assoc(
            "Relie chaque petit à la façon dont il a grandi avant de naître, puis choisis la phrase de la fiche sur le kangourou.",
            [("le petit kangourou", "naît tout petit, puis grandit dans la poche"), ("le poussin", "grandit 21 jours dans un œuf couvé"),
             ("le têtard", "sort d'un œuf fécondé dans l'eau"), ("le girafon", "grandit longtemps dans le ventre de sa mère"), ("le petit crocodile", "sort d'un œuf pondu sur la berge")],
            ["La poche est sur le ventre de la mère kangourou.", "Le crocodile pond sur la terre.", "Pour la justification : cherche « poche »."],
            J("Quelle phrase de la fiche parle du kangourou ?", K_KANGOUROU, [K_INT_VIVI, K_SOINS, K_TROIS], pos=0)),
        "second": assoc(
            "Relie chaque groupe d'animaux à son mode de reproduction, puis choisis la phrase de la fiche qui compare les oiseaux aux autres groupes.",
            [("les oiseaux", "tous ovipares"), ("les mammifères", "presque tous vivipares"), ("les amphibiens", "fécondation externe, ovipares"),
             ("les reptiles", "la plupart pondent, quelques-uns ont des petits formés"), ("les insectes", "fécondation interne, ovipares")],
            ["Aucun oiseau ne fait exception.", "Les amphibiens : la grenouille, le crapaud.", "Pour la justification : cherche « Tous les oiseaux »."],
            J("Quelle phrase de la fiche compare les oiseaux aux autres groupes ?", K_OISEAUX, [K_INT_OVI, K_REGLE, K_EXT_OVI], pos=3)),
    }
    d["e5-3"] = {
        "mousse": qcm(
            "Le carnet de naissance est presque complet. Réponds aux questions de Sacha.",
            [("Le chaton naît…", ["d'un œuf pondu", "vivant, du ventre de sa mère", "dans l'eau"], 1, "La chatte est vivipare."),
             ("La grenouille…", ["pond des œufs dans l'eau", "a un petit vivant", "pond dans un nid d'arbre"], 0, "Elle est ovipare.")],
            ["Ouvre la fiche " + FICHE + ".", "La chatte est un mammifère.", "Pense aux œufs de la mare."]),
        "lieutenant": qcm(
            "Sacha vérifie le carnet. Choisis la bonne réponse, puis la phrase de la fiche qui explique pourquoi une case reste vide.",
            [("Pourquoi aucun animal du tableau n'a-t-il une fécondation externe et un petit qui grandit dans le ventre ?", ["parce qu'un œuf fécondé dans l'eau ne peut pas être porté par la mère", "parce que l'eau est trop froide", "parce qu'on n'a pas encore cherché", "parce que ces animaux sont trop petits"], 0, "L'œuf est dehors, pas dans le ventre."),
             ("Une fécondation interne donne…", ["toujours un ovipare", "toujours un vivipare", "un ovipare ou un vivipare", "jamais de ponte"], 2, "La poule et le chat."),
             ("Pour ranger un animal dans le tableau, on cherche d'abord…", ["sa couleur", "la ligne de sa fécondation", "son poids", "son nom"], 1, "Puis la colonne de son mode de reproduction.")],
            ["Où est l'œuf après une fécondation externe ?", "Poule et chat : fécondation interne tous les deux.", "Pour la justification : cherche « ne peut pas porter »."],
            J("Quelle phrase de la fiche explique pourquoi une case reste vide ?", K_IMPOSSIBLE, [K_TROIS, K_REGLE, K_EXT_OVI], pos=1)),
        "second": qcm(
            "Les soigneurs préparent les naissances de l'année. Choisis la bonne réponse, puis la phrase de la fiche qui dit à quoi sert ce classement.",
            [("Une autruche va pondre. Que préparer ?", ["une couveuse ou un nid", "un bassin d'eau douce", "un enclos pour la mise bas", "rien"], 0, "L'autruche est ovipare."),
             ("Une girafe attend un petit. Que préparer ?", ["une couveuse", "un enclos calme", "une mare", "une capsule"], 1, "La girafe est vivipare."),
             ("Des grenouilles vont pondre. Que préparer ?", ["une mare propre au printemps", "un nid de paille", "une couveuse à 37 °C", "un enclos sec"], 0, "Fécondation externe, dans l'eau.")],
            ["Ovipare : on prépare pour des œufs.", "Vivipare : on prépare pour la mère.", "Pour la justification : cherche « soigneurs »."],
            J("Quelle phrase de la fiche dit à quoi sert ce classement ?", K_SOINS, [K_DEUX, K_METHODE, K_IMPOSSIBLE], pos=0)),
    }
    d["e5-4"] = {
        "lieutenant": code(
            "Pour ouvrir le carnet de naissance, compte trois nombres dans le registre, puis choisis la phrase de la fiche qui donne les deux questions à se poser." + DOC5,
            [("Animaux à fécondation interne et ovipares", "4", 1, True), ("Animaux à fécondation interne", "8", 1, True), ("Animaux qui ne pondent pas", "4", 1, True)],
            ["Interne = « dans le corps ».", "8 + 2 = 10 animaux.", "Pour la justification : cherche « deux questions »."],
            J("Quelle phrase de la fiche donne les deux questions ?", K_DEUX, [K_TROIS, K_METHODE, K_SOINS], pos=2)),
        "second": code(
            "Pour ouvrir le carnet de naissance, trouve trois nombres dans le registre, puis choisis la phrase de la fiche qui cite des ovipares à fécondation interne." + DOC5,
            [("Oiseaux du registre", "2", 1, True), ("Mammifères du registre", "4", 1, True), ("Animaux qui sortent d'un œuf après une fécondation dans le corps", "4", 1, True)],
            ["L'autruche et le manchot sont des oiseaux.", "Les mammifères sont ici les vivipares.", "Pour la justification : cherche « crocodile »."],
            J("Quelle phrase de la fiche cite des ovipares à fécondation interne ?", K_INT_OVI, [K_EXT_OVI, K_INT_VIVI, K_OISEAUX], pos=1)),
    }
    return d
