"""Salle 3 « Le potager de l'école » : grades mousse, lieutenant, second (fiche : Graines, dispersion et germination)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "reproduction", "tests", "donnees"))
from fiches import *

FICHE = "« Graines, dispersion et germination »"


def donnees(svg, bloc=None):
    d = {}
    d["e3-1"] = {
        "mousse": tri(
            "Tom a ramassé des graines. Range chaque graine : emportée par le vent, ou par un animal ?",
            [("vent", "Le vent"), ("ani", "Un animal")],
            [("le pissenlit", "vent"), ("l'érable", "vent"), ("la bardane", "ani"), ("le gland", "ani")],
            ["Ouvre la fiche " + FICHE + ".", "Le pissenlit a de petits parachutes.", "La bardane s'accroche aux poils."]),
        "lieutenant": tri(
            "Range chaque fruit ou graine selon son moyen de dispersion, puis choisis la phrase de la fiche sur les animaux.",
            [("vent", "Le vent"), ("ani", "Les animaux"), ("eau", "L'eau")],
            [("le pissenlit", "vent"), ("le tilleul", "vent"), ("la bardane", "ani"), ("le gland oublié par le geai", "ani"),
             ("la cerise mangée par un merle", "ani"), ("la noix de coco", "eau"), ("l'aulne, au bord de la rivière", "eau")],
            ["Une aile ou une aigrette : le vent.", "Accrochée, cachée ou mangée : un animal.", "Pour la justification : cherche « geai »."],
            J("Quelle phrase de la fiche parle des graines transportées par les animaux ?", G_ANIMAUX, [G_VENT, G_EAU, G_DISPERSION], pos=1)),
        "second": qcm(
            "Tom se demande à quoi sert la dispersion. Choisis la bonne réponse, puis la phrase de la fiche qui explique la dispersion.",
            [("Pourquoi est-ce utile que les graines s'éloignent de la plante mère ?", ["pour que l'espèce s'installe dans de nouveaux lieux", "pour que la plante mère grandisse", "pour que les graines sèchent", "ce n'est pas utile"], 0, "Elles colonisent de nouveaux endroits."),
             ("Un fruit à crochets est sans doute dispersé…", ["par l'eau", "par le vent", "par les animaux", "par la pluie seulement"], 2, "Les crochets s'accrochent aux poils."),
             ("Le geai cache des glands et en oublie. Que se passe-t-il ?", ["les glands pourrissent tous", "certains germent et donnent de jeunes chênes", "le geai les replante volontairement", "rien"], 1, "L'oubli aide la dispersion."),
             ("Une graine très légère, avec une aigrette, voyage…", ["avec le vent", "dans l'estomac d'un oiseau", "sur l'eau seulement", "elle ne voyage pas"], 0, "Comme le pissenlit.")],
            ["La dispersion fait voyager l'espèce.", "Le geai n'a pas de projet : il oublie.", "Pour la justification : cherche « nouveaux lieux »."],
            J("Quelle phrase de la fiche explique la dispersion ?", G_DISPERSION, [G_ANIMAUX, G_CYCLE, G_CONTIENT], pos=0)),
    }
    d["e3-2"] = {
        "mousse": vf(
            "Tom a écrit trois phrases sur ses haricots. Pour chacune, choisis vrai ou faux.",
            [("Une graine a besoin d'eau pour germer.", True, "Sur du coton sec, rien ne pousse."),
             ("Une graine germe très bien dans le réfrigérateur.", False, "Il y fait trop froid."),
             ("Quand la graine germe, la racine sort.", True, "Puis la tige et les feuilles.")],
            ["Ouvre la fiche " + FICHE + ".", "Le froid empêche de germer.", "La racine sort en premier."]),
        "lieutenant": qcm(
            "Tom veut prouver qu'une graine a besoin d'air pour germer. Choisis la bonne réponse, puis la phrase de la fiche sur les besoins de la graine.",
            [("Quelle expérience est la bonne ?", ["un pot avec de l'eau et un pot sans eau", "un pot mouillé à l'air et un pot rempli d'eau jusqu'en haut, sans air", "un pot au soleil et un pot à l'ombre", "un seul pot"], 1, "On ne change qu'une chose : l'air."),
             ("Dans une expérience, on change…", ["tout à la fois", "une seule chose à la fois", "rien du tout", "deux choses"], 1, "Sinon on ne sait pas ce qui a joué."),
             ("De quoi la graine n'a-t-elle presque jamais besoin pour germer ?", ["d'eau", "d'air", "de lumière", "d'une température douce"], 2, "Elle germe même dans le noir.")],
            ["Une seule différence entre les deux pots.", "Noyée, la graine manque d'air.", "Pour la justification : cherche « température douce »."],
            J("Quelle phrase de la fiche donne les besoins de la germination ?", G_BESOINS, [G_GERMINATION, G_LUMIERE, G_CONTIENT], pos=2)),
        "second": tri(
            "Tom range ses étiquettes. Pour chaque besoin, est-il nécessaire pour germer, ou seulement ensuite, pour que la jeune plante grandisse ? Puis choisis la phrase de la fiche sur la lumière.",
            [("germer", "Nécessaire pour germer"), ("ensuite", "Nécessaire ensuite pour grandir")],
            [("de l'eau", "germer"), ("de l'air", "germer"), ("une température douce", "germer"), ("de la lumière", "ensuite"), ("des feuilles vertes au soleil", "ensuite")],
            ["Le pot D a germé dans le noir.", "La jeune plante fabrique sa nourriture à la lumière.", "Pour la justification : cherche « grandir »."],
            J("Quelle phrase de la fiche parle de la lumière ?", G_LUMIERE, [G_BESOINS, G_CYCLE, G_GERMINATION], pos=3)),
    }
    d["e3-3"] = {
        "mousse": ordre(
            "Tom raconte la vie de son haricot. Remets les étapes dans l'ordre.",
            ["La graine est plantée.", "La graine germe.", "La plante grandit.", "La plante fleurit."],
            ["Ouvre la fiche " + FICHE + ".", "La graine d'abord.", "Les fleurs viennent à la fin."]),
        "lieutenant": ordre(
            "Remets dans l'ordre le cycle de vie complet du haricot, puis choisis la phrase de la fiche qui le résume.",
            [("La graine germe.", "racine, tige, feuilles"), ("La plante grandit à la lumière.", "elle fabrique sa nourriture"), ("La plante fleurit.", "étamines et pistil"),
             ("Les fleurs sont pollinisées.", "par les insectes"), ("Les fleurs deviennent des gousses.", "ce sont les fruits"), ("Les graines sont récoltées et semées.", "le cycle recommence")],
            ["La gousse est le fruit du haricot.", "La pollinisation précède le fruit.", "Pour la justification : cherche « cycle de vie »."],
            J("Quelle phrase de la fiche résume le cycle de vie d'une plante à fleurs ?", G_CYCLE, [G_GERMINATION, G_DISPERSION, G_LUMIERE], pos=0)),
        "second": vf(
            "Tom vérifie les phrases de son exposé. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur la germination.",
            [("Pendant la germination, la racine sort avant la tige.", True, "Elle fixe la jeune plante et puise l'eau."),
             ("Au début, la jeune plante se nourrit des réserves de la graine.", True, "Avant d'avoir de vraies feuilles."),
             ("Une graine sèche, rangée dans une boîte, est morte.", False, "Elle attend l'eau pour germer."),
             ("La gousse du haricot est un fruit.", True, "Elle vient de l'ovaire de la fleur."),
             ("Une plante ne fleurit qu'une fois qu'elle a fait ses graines.", False, "Les graines viennent après les fleurs.")],
            ["La racine d'abord.", "Une graine sèche est en sommeil.", "Pour la justification : cherche « se réveille »."],
            J("Quelle phrase de la fiche décrit la germination ?", G_GERMINATION, [G_CYCLE, G_BESOINS, G_CONTIENT], pos=1)),
    }
    d["e3-4"] = {
        "lieutenant": assoc(
            "Tom ouvre une graine de haricot trempée. Relie chaque partie ou chaque besoin à son rôle, puis choisis la phrase de la fiche sur le contenu de la graine.",
            [("l'enveloppe", "protège la graine"), ("l'embryon", "est la future plante"), ("les réserves", "nourrissent la jeune plante au début"),
             ("l'eau", "réveille la graine"), ("la lumière", "sert ensuite à la jeune plante pour grandir")],
            ["L'embryon est une plante miniature.", "La lumière sert après la germination.", "Pour la justification : cherche « embryon »."],
            J("Quelle phrase de la fiche dit ce que contient une graine ?", G_CONTIENT, [G_GERMINATION, G_BESOINS, G_LUMIERE], pos=3)),
        "second": ordre(
            "Tom prépare une vraie démarche expérimentale sur la température. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche sur les besoins de la germination.",
            [("Poser une question : la graine a-t-elle besoin de chaleur pour germer ?", "le problème"), ("Proposer une hypothèse : il faut une température douce.", "ce que l'on pense"),
             ("Préparer deux pots identiques, mouillés, l'un dans la classe, l'autre au réfrigérateur.", "une seule différence"),
             ("Observer les deux pots chaque jour pendant une semaine.", "noter les résultats"), ("Conclure en comparant les deux pots.", "l'hypothèse est validée ou non")],
            ["La question vient en premier.", "On observe avant de conclure.", "Pour la justification : cherche « température douce »."],
            J("Quelle phrase de la fiche donne les besoins de la germination ?", G_BESOINS, [G_LUMIERE, G_GERMINATION, G_DISPERSION], pos=1)),
    }
    return d
