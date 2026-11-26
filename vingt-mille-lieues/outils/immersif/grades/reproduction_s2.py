"""Salle 2 « Le rucher » : grades mousse, lieutenant, second (fiche : Pollinisation et fécondation)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "reproduction", "tests", "donnees"))
from fiches import *

FICHE = "« Pollinisation et fécondation »"


def donnees(svg, bloc=None):
    d = {}
    d["e2-1"] = {
        "mousse": ordre(
            "Capucine raconte le voyage du pollen. Remets les trois images dans l'ordre.",
            ["L'abeille se pose sur une fleur et se couvre de pollen.", "L'abeille dépose le pollen sur une autre fleur.", "La fleur devient un fruit."],
            ["Ouvre la fiche " + FICHE + ".", "L'abeille se couvre de pollen d'abord.", "Le fruit arrive à la fin."]),
        "lieutenant": ordre(
            "Remets dans l'ordre la transformation de la fleur de cerisier en cerise, puis choisis la phrase de la fiche qui dit ce que deviennent l'ovaire et les ovules.",
            [("Le pollen des étamines se dépose sur le stigmate.", "pollinisation"), ("Le pollen permet de féconder les ovules.", "fécondation"),
             ("Les pétales et les étamines fanent.", "ils tombent"), ("L'ovaire grossit.", "il devient vert puis rouge"),
             ("La cerise est mûre ; son noyau contient la graine.", "l'ovule est devenu graine")],
            ["Pollinisation, puis fécondation.", "Les pétales tombent avant que le fruit grossisse.", "Pour la justification : cherche « devient le fruit »."],
            J("Quelle phrase de la fiche dit ce que deviennent l'ovaire et les ovules ?", P_FRUIT, [P_FECONDATION, P_FANER, P_POLLINISATION], pos=1)),
        "second": assoc(
            "Capucine compare une fleur et le fruit qu'elle deviendra. Relie chaque pièce de la fleur à ce qu'elle devient, puis choisis la phrase de la fiche sur les pétales.",
            [("l'ovaire", "devient le fruit"), ("les ovules", "deviennent les graines"), ("les pétales", "fanent et tombent"),
             ("les étamines", "fanent et tombent aussi"), ("le stigmate", "a reçu le pollen, puis se dessèche")],
            ["Le fruit vient de l'organe femelle.", "Deux pièces tombent : elles ne servent plus.", "Pour la justification : cherche « fanent »."],
            J("Quelle phrase de la fiche dit ce que deviennent les pétales ?", P_FANER, [P_FRUIT, P_FECONDATION, P_INSECTES], pos=2)),
    }
    d["e2-2"] = {
        "mousse": vf(
            "Capucine a écrit trois phrases sur ses abeilles. Pour chacune, choisis vrai ou faux.",
            [("Les abeilles transportent le pollen de fleur en fleur.", True, "Il se colle à leurs poils."),
             ("Les abeilles viennent boire le nectar des fleurs.", True, "C'est un liquide sucré."),
             ("Sans pollen, une fleur de pommier donne quand même une pomme.", False, "Il faut la pollinisation.")],
            ["Ouvre la fiche " + FICHE + ".", "Le nectar est sucré.", "Pas de pollen, pas de fruit."]),
        "lieutenant": qcm(
            "Capucine fait réviser les visiteurs du rucher. Choisis la bonne réponse, puis la phrase de la fiche qui définit la pollinisation.",
            [("Qu'est-ce que la pollinisation ?", ["la chute des pétales", "le transport du pollen des étamines au pistil", "la germination d'une graine", "la fabrication du miel"], 1, "Le pollen voyage jusqu'au pistil."),
             ("Le pollen doit arriver sur une fleur…", ["de n'importe quelle plante", "de la même espèce", "fanée", "sans pistil"], 1, "Le pollen de pommier sert aux fleurs de pommier."),
             ("Quels insectes pollinisent ?", ["les abeilles, les bourdons, les papillons", "seulement les fourmis", "aucun insecte", "seulement les moustiques"], 0, "Ils viennent boire le nectar.")],
            ["Pollinisation : un transport.", "Même espèce.", "Pour la justification : cherche « transport »."],
            J("Quelle phrase de la fiche définit la pollinisation ?", P_POLLINISATION, [P_FECONDATION, P_INSECTES, P_COOPERATION], pos=0)),
        "second": ordre(
            "Capucine explique aux agriculteurs une chaîne de conséquences. Remets-la dans l'ordre, puis choisis la phrase de la fiche sur les insecticides.",
            [("On utilise beaucoup d'insecticides dans les champs.", "pour tuer les insectes nuisibles"), ("Les abeilles et les bourdons deviennent moins nombreux.", "ils sont touchés aussi"),
             ("Moins de fleurs sont pollinisées.", "le pollen voyage moins"), ("Moins d'ovules sont fécondés.", "moins de graines se forment"),
             ("La récolte donne moins de fruits et de graines.", "le verger produit moins")],
            ["Tout part du traitement des champs.", "Pollinisation, puis fécondation.", "Pour la justification : cherche « insecticides »."],
            J("Quelle phrase de la fiche parle des insecticides ?", P_INSECTICIDES, [P_COOPERATION, P_INSECTES, P_FRUIT], pos=3)),
    }
    d["e2-3"] = {
        "mousse": tri(
            "Range chaque plante : son pollen voyage avec les abeilles ou avec le vent ?",
            [("ins", "Avec les abeilles"), ("vent", "Avec le vent")],
            [("le pommier", "ins"), ("le tournesol", "ins"), ("le maïs", "vent"), ("le noisetier", "vent")],
            ["Ouvre la fiche " + FICHE + ".", "Les fleurs colorées attirent les abeilles.", "Le maïs n'a pas de pétales colorés."]),
        "lieutenant": tri(
            "Range chaque indice : il montre une fleur pollinisée par les insectes ou par le vent ? Puis choisis la phrase de la fiche sur le vent.",
            [("ins", "Pollinisée par les insectes"), ("vent", "Pollinisée par le vent")],
            [("des pétales grands et colorés", "ins"), ("un parfum sucré", "ins"), ("du nectar", "ins"),
             ("des fleurs discrètes, sans couleur vive", "vent"), ("un pollen très abondant et léger", "vent"), ("des étamines qui pendent hors de la fleur", "vent")],
            ["Les insectes sont attirés par la couleur et le parfum.", "Le vent ne voit pas les couleurs.", "Pour la justification : cherche « vent »."],
            J("Quelle phrase de la fiche parle des plantes pollinisées par le vent ?", P_VENT, [P_INSECTES, P_POLLINISATION, P_FANER], pos=2)),
        "second": qcm(
            "Capucine pose des cas difficiles. Choisis la bonne réponse, puis la phrase de la fiche sur les insectes pollinisateurs.",
            [("Pourquoi le noisetier produit-il énormément de pollen ?", ["parce que le vent en perd beaucoup en route", "pour nourrir les abeilles", "pour colorer ses fleurs", "il n'en produit pas"], 0, "Le transport par le vent est peu précis."),
             ("Un champ de maïs n'a pas besoin de ruches pour être pollinisé, car…", ["le maïs n'a pas de fleurs", "le vent transporte son pollen", "il n'a pas d'ovules", "il pousse sous terre"], 1, "Le maïs est pollinisé par le vent."),
             ("Pourquoi les abeilles visitent-elles les fleurs ?", ["pour polliniser volontairement", "pour se nourrir de nectar et de pollen", "pour se réchauffer", "pour pondre"], 1, "Elles transportent le pollen sans le savoir."),
             ("Une fleur rouge, parfumée, pleine de nectar est sans doute pollinisée…", ["par le vent", "par des animaux", "par l'eau", "par personne"], 1, "Couleur, parfum, nectar attirent.")],
            ["Le vent est peu précis.", "L'abeille vient manger, pas « aider ».", "Pour la justification : cherche « nectar »."],
            J("Quelle phrase de la fiche parle des insectes pollinisateurs ?", P_INSECTES, [P_VENT, P_COOPERATION, P_POLLINISATION], pos=1)),
    }
    d["e2-4"] = {
        "lieutenant": vf(
            "Capucine relit le panneau « Protégeons les pollinisateurs ». Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur les insecticides.",
            [("Les insecticides peuvent tuer aussi les abeilles.", True, "Ils ne choisissent pas les insectes."),
             ("Moins de pollinisateurs, c'est plus de fruits.", False, "C'est moins de fruits."),
             ("La pollinisation est une coopération entre l'insecte et la plante.", True, "Les deux y gagnent."),
             ("Toutes les cultures ont besoin des abeilles.", False, "Le maïs est pollinisé par le vent."),
             ("Un verger sans pollinisateurs donne moins de graines.", True, "Moins d'ovules sont fécondés.")],
            ["Insecticide : il tue les insectes.", "Pense au maïs.", "Pour la justification : cherche « moins nombreux »."],
            J("Quelle phrase de la fiche parle des insecticides ?", P_INSECTICIDES, [P_COOPERATION, P_VENT, P_FRUIT], pos=0)),
        "second": tri(
            "Capucine explique la coopération entre l'abeille et la fleur. Range chaque carte : ce que gagne l'abeille, ou ce que gagne la plante ; puis choisis la phrase de la fiche sur la coopération.",
            [("abeille", "Ce que gagne l'abeille"), ("plante", "Ce que gagne la plante")],
            [("du nectar sucré", "abeille"), ("du pollen pour nourrir ses larves", "abeille"), ("de la nourriture pour la ruche", "abeille"),
             ("du pollen apporté sur son stigmate", "plante"), ("des ovules fécondés", "plante"), ("des fruits et des graines", "plante")],
            ["L'abeille vient se nourrir.", "La plante a besoin du pollen d'une autre fleur.", "Pour la justification : cherche « coopération »."],
            J("Quelle phrase de la fiche explique la coopération ?", P_COOPERATION, [P_INSECTES, P_INSECTICIDES, P_POLLINISATION], pos=2)),
    }
    return d
