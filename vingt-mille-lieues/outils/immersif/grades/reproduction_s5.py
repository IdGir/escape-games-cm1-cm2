"""Salle 5 « La bergerie et la mare » : grades mousse, lieutenant, second (fiche : Naître ou éclore)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "reproduction", "tests", "donnees"))
from fiches import *

FICHE = "« Naître ou éclore »"


def donnees(svg, bloc=None):
    d = {}
    d["e5-1"] = {
        "mousse": tri(
            "Range chaque animal : son petit sort d'un œuf, ou naît du ventre de sa mère ?",
            [("ovi", "Sort d'un œuf"), ("vivi", "Naît du ventre de sa mère")],
            [("la poule", "ovi"), ("la tortue", "ovi"), ("la vache", "vivi"), ("la brebis", "vivi")],
            ["Ouvre la fiche " + FICHE + ".", "La poule couve ses œufs.", "L'agneau naît du ventre de la brebis."]),
        "lieutenant": tri(
            "Range chaque animal : ovipare ou vivipare ? Puis choisis la phrase de la fiche sur les vivipares.",
            [("ovi", "Ovipare"), ("vivi", "Vivipare")],
            [("la poule", "ovi"), ("la grenouille", "ovi"), ("la truite", "ovi"), ("le papillon", "ovi"),
             ("la lapine", "vivi"), ("la chèvre", "vivi"), ("le dauphin", "vivi"), ("la chauve-souris", "vivi")],
            ["Le dauphin est un mammifère.", "La chauve-souris allaite ses petits.", "Pour la justification : cherche « ventre de sa mère »."],
            J("Quelle phrase de la fiche décrit les animaux vivipares ?", N_VIVIPARE, [N_OVIPARE, N_EMBRYON, N_LIEN], pos=1)),
        "second": assoc(
            "Nadia complète le tableau de la ferme. Relie chaque animal à son type de fécondation et à son mode de reproduction, puis choisis la phrase de la fiche qui relie les deux.",
            [("la poule", "fécondation interne, ovipare"), ("la vache", "fécondation interne, vivipare"), ("la grenouille", "fécondation externe, ovipare"),
             ("la tortue", "fécondation interne, ovipare, sur la terre"), ("la truite", "fécondation externe, ovipare, dans la rivière")],
            ["Deux animaux sont dans l'eau.", "Un seul est vivipare.", "Pour la justification : cherche « toujours »."],
            J("Quelle phrase de la fiche relie le type de fécondation et le mode de reproduction ?", N_LIEN, [N_OVIPARE, N_VIVIPARE, N_EMBRYON], pos=0)),
    }
    d["e5-2"] = {
        "mousse": vf(
            "Nadia a écrit trois phrases. Pour chacune, choisis vrai ou faux.",
            [("Le petit de la brebis est un agneau.", True, "C'est un petit mouton."),
             ("Un poussin peut naître d'un œuf de cane.", False, "D'un œuf de cane sort un caneton."),
             ("Les agneaux ressemblent à leurs parents.", True, "Mais chacun est un peu différent.")],
            ["Ouvre la fiche " + FICHE + ".", "Chaque petit est de la même espèce que ses parents.", "Le petit de la cane est le caneton."]),
        "lieutenant": qcm(
            "Nadia fait réviser les visiteurs. Choisis la bonne réponse, puis la phrase de la fiche qui relie la fécondation et le mode de reproduction.",
            [("La poule a une fécondation interne. Elle est…", ["vivipare", "ovipare", "ni l'un ni l'autre", "les deux"], 1, "Elle pond des œufs."),
             ("Un animal a une fécondation externe. Il est sûrement…", ["ovipare", "vivipare", "un mammifère", "un oiseau"], 0, "Les ovules sont pondus."),
             ("Qu'est-ce qu'une espèce ?", ["des animaux de la même couleur", "des êtres vivants qui peuvent se reproduire entre eux", "les animaux d'une même ferme", "les animaux qui pondent"], 1, "Définition du programme."),
             ("L'éclosion, c'est…", ["la naissance du veau", "la sortie du petit hors de l'œuf", "la fécondation", "la ponte"], 1, "Le poussin casse sa coquille.")],
            ["Interne ne veut pas dire vivipare.", "Externe : toujours des œufs.", "Pour la justification : cherche « toujours »."],
            J("Quelle phrase de la fiche relie la fécondation et le mode de reproduction ?", N_LIEN, [N_OVIPARE, N_ESPECE, N_EMBRYON], pos=2)),
        "second": ordre(
            "Nadia compare la durée de développement de trois petits. Range-les du plus court au plus long, puis choisis la phrase de la fiche qui donne ces durées.",
            [("le poussin", "environ 21 jours de couvaison"), ("l'agneau", "environ 5 mois dans le ventre de la brebis"), ("le veau", "environ 9 mois dans le ventre de la vache")],
            ["21 jours, c'est 3 semaines.", "5 mois est plus court que 9 mois.", "Pour la justification : cherche « 21 jours »."],
            J("Quelle phrase de la fiche donne les durées de développement ?", N_DUREES, [N_OVIPARE, N_VIVIPARE, N_EMBRYON], pos=3)),
    }
    d["e5-3"] = {
        "mousse": ordre(
            "Nadia montre comment naît un poussin. Remets les étapes dans l'ordre.",
            ["La poule pond un œuf.", "La poule couve l'œuf.", "Le poussin sort de l'œuf."],
            ["Ouvre la fiche " + FICHE + ".", "Il faut d'abord un œuf.", "La sortie de l'œuf est la fin."]),
        "lieutenant": ordre(
            "Remets dans l'ordre le développement de la grenouille, puis choisis la phrase de la fiche sur les larves.",
            [("Les ovules sont pondus et fécondés dans l'eau.", "fécondation externe"), ("L'embryon se développe dans l'œuf.", "dans la mare"),
             ("Le têtard sort de l'œuf.", "c'est une larve"), ("Les pattes poussent, la queue raccourcit.", "le têtard se transforme"),
             ("La jeune grenouille quitte l'eau.", "elle deviendra adulte")],
            ["Tout commence dans l'eau.", "Le têtard est une larve.", "Pour la justification : cherche « têtard »."],
            J("Quelle phrase de la fiche parle des larves ?", N_LARVE, [N_OVIPARE, N_EMBRYON, N_LIEN], pos=0)),
        "second": vf(
            "Nadia relit l'exposé d'un stagiaire sur les agneaux du troupeau. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur les différences entre individus.",
            [("Deux agneaux des mêmes parents sont toujours identiques.", False, "Chaque individu est unique."),
             ("Une partie des différences entre agneaux est héritée des parents.", True, "Elles viennent en partie du bélier et de la brebis."),
             ("Ces différences sont une richesse pour l'espèce.", True, "Tous ne réagiront pas de la même façon."),
             ("Un agneau peut appartenir à une autre espèce que ses parents.", False, "Il est toujours de la même espèce."),
             ("Une espèce est un ensemble d'êtres vivants qui peuvent se reproduire entre eux.", True, "C'est la définition.")],
            ["Chacun est unique.", "Même espèce que les parents.", "Pour la justification : cherche « richesse »."],
            J("Quelle phrase de la fiche parle des différences entre individus ?", N_DIVERSITE, [N_DIFFERENTS, N_ESPECE, N_EMBRYON], pos=1)),
    }
    d["e5-4"] = {
        "lieutenant": code(
            "Le portail du jardin est fermé par un cadenas à trois nombres. Retrouve-les dans la fiche, puis choisis la phrase qui les contient."
            + tableau("Le carnet de Nadia", ["Ce que dit le carnet", "Nombre"],
                      [["Jours de couvaison d'un œuf de poule (environ)", "?"], ["Mois avant la naissance d'un veau (environ)", "?"], ["Mois avant la naissance d'un agneau (environ)", "?"]]),
            [("Jours de couvaison", "21", 2, True), ("Mois pour un veau", "9", 1, True), ("Mois pour un agneau", "5", 1, True)],
            ["Fiche « Naître ou éclore » : « Combien de temps ? ».", "Trois semaines de couvaison.", "Pour la justification : cherche « couvaison »."],
            J("Quelle phrase de la fiche contient les trois nombres ?", N_DUREES, [N_VIVIPARE, N_OVIPARE, N_LARVE], pos=2)),
        "second": code(
            "Le cadenas du portail demande des calculs. Utilise les durées de la fiche, puis choisis la phrase qui les contient."
            + tableau("Le carnet de Nadia", ["Question", "Nombre"],
                      [["Nombre de semaines de couvaison d'un œuf de poule (environ)", "?"], ["Nombre de mois de plus pour un veau que pour un agneau", "?"], ["Nombre de jours de couvaison (environ)", "?"]]),
            [("Semaines de couvaison", "3", 1, True), ("Mois de différence", "4", 1, True), ("Jours de couvaison", "21", 2, True)],
            ["Une semaine, c'est 7 jours.", "9 moins 5.", "Pour la justification : cherche « agneau »."],
            J("Quelle phrase de la fiche donne les durées de développement ?", N_DUREES, [N_VIVIPARE, N_ESPECE, N_EMBRYON], pos=0)),
    }
    return d
