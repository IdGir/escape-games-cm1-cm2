"""Salle 2 « L'aquarium et la mare » : grades mousse, lieutenant, second (fiche : Fécondation externe et interne)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "naissances-animaux", "tests", "donnees"))
from fiches import *

FICHE = "« Fécondation externe et interne »"


def donnees(svg, bloc=None):
    d = {}
    d["e2-1"] = {
        "mousse": tri(
            "Théo range ses fiches. Où se rencontrent les cellules : dans l'eau, ou dans le corps de la femelle ?",
            [("ext", "Dans l'eau"), ("int", "Dans le corps de la femelle")],
            [("la grenouille", "ext"), ("la truite", "ext"), ("la poule", "int"), ("la vache", "int")],
            ["Ouvre la fiche " + FICHE + ".", "La grenouille pond dans la mare.", "La vache est un mammifère : dans le corps."]),
        "lieutenant": tri(
            "Théo a mis des pièges dans ses fiches : plusieurs animaux vivent dans l'eau. Range chacun selon son type de fécondation, puis choisis la phrase de la fiche qui explique le piège.",
            [("ext", "Fécondation externe"), ("int", "Fécondation interne")],
            [("la grenouille", "ext"), ("le crapaud", "ext"), ("la truite", "ext"), ("le saumon", "ext"),
             ("la tortue marine", "int"), ("le dauphin", "int"), ("le requin", "int"), ("le canard", "int")],
            ["Le dauphin est un mammifère.", "La tortue marine pond sur la plage.", "Pour la justification : cherche « ne suffit pas »."],
            J("Quelle phrase de la fiche explique le piège ?", X_EAU, [X_EX_EXT, X_LIEU, X_NOMBRE], pos=1)),
        "second": tri(
            "Théo classe dix animaux de tout le zoo. Range chacun selon son type de fécondation, puis choisis la phrase de la fiche qui cite les groupes à fécondation interne.",
            [("ext", "Fécondation externe"), ("int", "Fécondation interne")],
            [("la grenouille", "ext"), ("le crapaud", "ext"), ("la truite", "ext"), ("le saumon", "ext"),
             ("le papillon", "int"), ("la coccinelle", "int"), ("le crocodile", "int"), ("le requin", "int"), ("le manchot", "int"), ("la girafe", "int")],
            ["Les insectes s'accouplent.", "Le manchot est un oiseau.", "Pour la justification : cherche « insectes »."],
            J("Quelle phrase de la fiche cite les groupes à fécondation interne ?", X_EX_INT, [X_EX_EXT, X_INTERNE, X_EAU], pos=3)),
    }
    d["e2-2"] = {
        "mousse": qcm(
            "Théo montre la mare. Réponds à ses questions.",
            [("Où la grenouille pond-elle ses œufs ?", ["dans la mare", "dans un nid d'arbre", "dans le sable sec"], 0, "Dans l'eau."),
             ("Chez la vache, les cellules se rencontrent…", ["dans l'eau", "dans le corps de la vache", "dans l'herbe"], 1, "Dans le corps de la femelle.")],
            ["Ouvre la fiche " + FICHE + ".", "La grenouille vit près de la mare.", "La vache ne vit pas dans l'eau."]),
        "lieutenant": qcm(
            "Théo pose des questions plus difficiles. Choisis la bonne réponse, puis la phrase de la fiche qui explique les pontes nombreuses.",
            [("Une grenouille pond des centaines d'ovules. Pourquoi ?", ["parce que beaucoup de gamètes sont perdus dans l'eau", "pour nourrir le mâle", "parce que la mare est grande", "par hasard"], 0, "En fécondation externe, beaucoup de gamètes sont perdus."),
             ("Dans quel cas la fécondation suit-elle un accouplement ?", ["fécondation externe", "fécondation interne", "les deux", "aucun"], 1, "Le mâle dépose ses spermatozoïdes dans le corps de la femelle."),
             ("Pourquoi beaucoup d'œufs de la mare n'éclosent-ils pas ?", ["ils sont mangés par d'autres animaux", "ils gèlent toujours", "ils s'envolent", "ils deviennent des cailloux"], 0, "Les œufs pondus dans l'eau ne sont pas gardés.")],
            ["Dans l'eau, les gamètes se dispersent.", "Accouplement = fécondation dans le corps.", "Pour la justification : cherche « milliers »."],
            J("Quelle phrase de la fiche explique les pontes nombreuses ?", X_NOMBRE, [X_EXTERNE, X_RISQUE, X_GELEE], pos=2)),
        "second": qcm(
            "Théo compare la truite et le requin. Choisis la bonne réponse, puis la phrase de la fiche qui décrit la fécondation interne.",
            [("Où la truite pond-elle ses ovules ?", ["dans un creux du gravier de la rivière", "dans le corps du mâle", "sur une feuille", "dans un nid de paille"], 0, "Le mâle les arrose ensuite de ses spermatozoïdes."),
             ("Chez le requin, les gamètes se rencontrent…", ["dans l'eau de mer", "dans le corps de la femelle", "dans le sable", "dans une capsule déjà pondue"], 1, "Le requin a une fécondation interne."),
             ("Lequel de ces animaux pond le plus d'ovules à la fois ?", ["la truite", "la girafe", "la vache", "la chatte"], 0, "Fécondation externe : beaucoup de gamètes perdus.")],
            ["La truite fraie dans la rivière.", "Le requin s'accouple.", "Pour la justification : cherche « accouplement »."],
            J("Quelle phrase de la fiche décrit la fécondation interne ?", X_INTERNE, [X_EXTERNE, X_LIEU, X_EX_INT], pos=0)),
    }
    d["e2-3"] = {
        "mousse": trous(
            "Le panneau de la mare est mouillé. Complète-le.",
            "La grenouille pond ses œufs dans l'[[eau]]. Chez le chat, les cellules se rencontrent dans le [[corps]] de la femelle.",
            ["eau", "corps"],
            ["Ouvre la fiche " + FICHE + ".", "La grenouille vit près de la mare.", "Le chat ne pond pas dans l'eau."]),
        "lieutenant": trous(
            "Le panneau de la mare est mouillé. Complète-le (des étiquettes sont en trop), puis choisis la phrase de la fiche qui décrit la fécondation externe.",
            "Lors d'une fécondation [[externe]], la femelle [[pond]] ses ovules dans l'eau et le mâle y libère ses [[spermatozoïdes]]. Les œufs de grenouille sont entourés d'une [[gelée]] ; on les trouve au [[printemps]] dans les mares.",
            ["externe", "pond", "spermatozoïdes", "gelée", "printemps", "interne", "coquille", "hiver"],
            ["Dans l'eau : externe.", "La gelée protège les œufs.", "Pour la justification : cherche « libère »."],
            J("Quelle phrase de la fiche décrit la fécondation externe ?", X_EXTERNE, [X_INTERNE, X_GELEE, X_LIEU], pos=1)),
        "second": trous(
            "Théo écrit le panneau de la rivière. Complète-le (des étiquettes sont en trop), puis choisis la phrase de la fiche qui dit pourquoi tant d'œufs disparaissent.",
            "Chez la truite, la femelle pond ses [[ovules]] dans un creux du [[gravier]] et le mâle les arrose de ses spermatozoïdes. Les œufs ne sont pas [[gardés]] : beaucoup sont [[mangés]] par d'autres animaux. Chez le dauphin, au contraire, la fécondation est [[interne]], même s'il vit dans la mer.",
            ["ovules", "gravier", "gardés", "mangés", "interne", "externe", "couvés", "nid"],
            ["La truite pond dans la rivière.", "Personne ne surveille les œufs.", "Pour la justification : cherche « gardés »."],
            J("Quelle phrase de la fiche dit pourquoi tant d'œufs disparaissent ?", X_RISQUE, [X_NOMBRE, X_TRUITE, X_EAU], pos=0)),
    }
    d["e2-4"] = {
        "lieutenant": intrus(
            "Théo a regroupé des animaux à fécondation interne. Un seul n'a rien à faire là. Trouve l'intrus, puis choisis la phrase de la fiche qui cite des animaux à fécondation externe.",
            [("le chat", False), ("la poule", False), ("la truite", True), ("le requin", False)],
            ["Lequel ne s'accouple pas ?", "Ses gamètes se rencontrent dans la rivière.", "Pour la justification : cherche « saumon »."],
            J("Quelle phrase de la fiche cite des animaux à fécondation externe ?", X_EX_EXT, [X_EX_INT, X_EXTERNE, X_TRUITE], pos=2)),
        "second": intrus(
            "Théo a regroupé des animaux qui vivent dans l'eau et ont une fécondation externe. Un seul n'a rien à faire là. Trouve l'intrus, puis choisis la phrase de la fiche qui évite ce piège.",
            [("la grenouille", False), ("le crapaud", False), ("le saumon", False), ("le dauphin", True), ("la truite", False)],
            ["Tous vivent dans l'eau.", "L'un d'eux est un mammifère.", "Pour la justification : cherche « tortue marine »."],
            J("Quelle phrase de la fiche évite ce piège ?", X_EAU, [X_EX_EXT, X_NOMBRE, X_LIEU], pos=3)),
    }
    return d
