"""Séance 5 « Les loisirs de la montagne » : grades mousse, lieutenant, second (fiche : La montagne, un espace de loisirs à ménager)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "mission-geo", "tests", "donnees"))
from fiches import *

FICHE = "« La montagne, un espace de loisirs à ménager »"


def donnees(svg, bloc=None):
    d = {}
    d["e5-1"] = {
        "mousse": assoc(
            "Hugo t'apprend trois mots de la montagne. Relie chaque mot à sa définition.",
            [("un chalet", "une maison en bois"), ("un télésiège", "un siège qui monte les skieurs"), ("le sommet", "le haut de la montagne")],
            ["Ouvre la fiche " + FICHE + ".", "On s'assoit sur le télésiège.", "Le sommet est tout en haut."]),
        "lieutenant": ordre(
            "Hugo prépare les débutants. Range les couleurs des pistes de la plus facile à la plus difficile, puis choisis la phrase de la fiche qui les classe.",
            ["la piste verte", "la piste bleue", "la piste rouge", "la piste noire"],
            ["Les débutants commencent par le vert.", "La noire est réservée aux skieurs très habiles.", "Pour la justification : cherche « par couleur »."],
            J("Quelle phrase de la fiche classe les pistes ?", M_PISTES, [M_STATION, M_LOISIRS, M_ROUSSES], pos=0)),
        "second": assoc(
            "Hugo relie chaque aménagement de la station à son effet sur l'environnement. Relie-les à ton tour, puis choisis la phrase de la fiche sur l'eau et l'énergie.",
            [("le canon à neige", "il prélève beaucoup d'eau"), ("le télésiège", "il consomme de l'énergie"), ("le grand parking plein", "les voitures polluent l'air"),
             ("la résidence bâtie sur la forêt", "elle réduit la biodiversité"), ("les mégots sur les rochers", "ils polluent les sols")],
            ["Le canon à neige fabrique de la neige avec de l'eau.", "Le télésiège marche à l'électricité.", "Pour la justification : cherche « canons à neige »."],
            J("Quelle phrase de la fiche parle de l'eau et de l'énergie ?", M_EAU, [M_AIR, M_BIO, M_STATION], pos=2)),
    }
    d["e5-2"] = {
        "mousse": tri(
            "Range chaque loisir : sur la neige, ou sans neige ?",
            [("n", "Sur la neige"), ("s", "Sans neige")],
            [("le ski", "n"), ("la luge", "n"), ("la randonnée", "s"), ("l'escalade", "s")],
            ["Ouvre la fiche " + FICHE + ".", "La luge glisse sur la neige.", "On grimpe sur la roche pour l'escalade."]),
        "lieutenant": tri(
            "Le tourisme est-il bon pour la montagne ? Range chaque proposition, puis choisis la phrase de la fiche sur ce que le tourisme apporte.",
            [("p", "Effets positifs"), ("n", "Effets négatifs")],
            [("des emplois de moniteurs et de saisonniers", "p"), ("des revenus pour les hôtels et les restaurants", "p"), ("des villages habités toute l'année", "p"),
             ("des files de voitures qui polluent l'air", "n"), ("des résidences construites sur la forêt", "n"), ("de l'eau prélevée pour les canons à neige", "n")],
            ["Trois effets positifs, trois effets négatifs.", "Les négatifs sont ceux des photos d'Hugo.", "Pour la justification : cherche « emplois et des revenus »."],
            J("Quelle phrase de la fiche dit ce que le tourisme apporte à la montagne ?", M_EMPLOIS, [M_BIO, M_AIR, M_LOISIRS], pos=1)),
        "second": tri(
            "Hugo classe les dégâts du tourisme selon ce qu'ils touchent. Range chaque carte, puis choisis la phrase de la fiche sur la biodiversité.",
            [("air", "L'air"), ("res", "L'eau et l'énergie"), ("viv", "Le vivant et les sols")],
            [("les embouteillages à l'entrée de la station", "air"), ("les canons à neige", "res"), ("les remontées mécaniques toute la journée", "res"),
             ("une résidence construite sur un versant boisé", "viv"), ("des animaux dérangés par les skieurs hors-piste", "viv"), ("des mégots sur les rochers", "viv")],
            ["Les voitures rejettent des gaz.", "Les animaux et la forêt font partie du vivant.", "Pour la justification : cherche « biodiversité »."],
            J("Quelle phrase de la fiche parle de la biodiversité ?", M_BIO, [M_EAU, M_AIR, M_EMPLOIS], pos=3)),
    }
    d["e5-3"] = {
        "mousse": qcm(
            "Hugo montre un canon à neige.",
            [("Pour fabriquer de la neige, le canon à neige utilise…", ["beaucoup d'eau", "du sable", "du pétrole"], 0, "Il pulvérise de l'eau dans l'air froid.")],
            ["Ouvre la fiche " + FICHE + ".", "La neige, c'est de l'eau gelée.", "Le canon à neige pulvérise de l'eau."]),
        "lieutenant": trous(
            "Complète le rapport d'Hugo (un mot est l'intrus), puis choisis la phrase de la fiche sur la biodiversité et les sols.",
            "Les constructions sur les [[forêts]] et le dérangement des [[animaux]] réduisent la [[biodiversité]] ; les [[déchets]] abandonnés polluent les [[sols]].",
            ["forêts", "animaux", "biodiversité", "déchets", "sols", "écologie"],
            ["La biodiversité, ce sont les êtres vivants d'un milieu.", "Les mégots sont des déchets.", "Pour la justification : cherche « déchets abandonnés »."],
            J("Quelle phrase de la fiche parle de la biodiversité et des sols ?", M_BIO, [M_EAU, M_EMPLOIS, M_STATION], pos=0)),
        "second": vf(
            "Un guide touristique contient des erreurs. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui décrit une station.",
            [("Une station de montagne a des remontées mécaniques, des pistes et des hébergements.", True, "Elle est aménagée pour les touristes."),
             ("La montagne n'attire des touristes qu'en hiver.", False, "Randonnée, escalade, rafting : été comme hiver."),
             ("La station des Rousses est dans le Haut-Jura.", True, "Elle est reliée au domaine de la Dôle."),
             ("Le sommet de la Dôle se trouve en France.", False, "Il est en Suisse, à 1 677 mètres."),
             ("La piste rouge est plus facile que la piste bleue.", False, "Verte, bleue, rouge, noire : de la plus facile à la plus difficile.")],
            ["Pense à l'été à la montagne.", "La Dôle est juste de l'autre côté de la frontière.", "Pour la justification : cherche « aménagée »."],
            J("Quelle phrase de la fiche décrit une station de montagne ?", M_STATION, [M_ROUSSES, M_LOISIRS, M_PISTES], pos=1)),
    }
    d["e5-4"] = {
        "lieutenant": qcm(
            "Le skieur a dit : « Là où va votre valise, c'est l'hiver quand c'est l'hiver ici. » Réponds, puis choisis la phrase de la fiche sur les saisons.",
            [("En décembre, quelle saison est-ce en Australie, dans l'hémisphère sud ?", ["l'été", "l'hiver", "l'automne", "le printemps"], 0, "Les saisons sont inversées."),
             ("Si c'est l'hiver là-bas en même temps qu'en France, le pays est…", ["dans l'hémisphère nord", "dans l'hémisphère sud", "sur l'équateur", "en Antarctique"], 0, "Mêmes saisons, même hémisphère."),
             ("Quel pays la remarque du skieur élimine-t-elle ?", ["l'Argentine", "le Mexique", "le Canada", "l'Espagne"], 0, "L'Argentine est dans l'hémisphère sud.")],
            ["L'Australie est dans l'hémisphère sud.", "L'Argentine aussi.", "Pour la justification : cherche « inversées »."],
            J("Quelle phrase de la fiche parle des saisons ?", M_HEMI, [M_LOISIRS, M_ROUSSES, M_STATION], pos=3)),
        "second": ordre(
            "Chef de mission, reconstitue le raisonnement des agents depuis Besançon : range les étapes dans l'ordre, puis choisis la phrase de la fiche sur les saisons.",
            ["À Besançon, la source dit que la valise n'est plus en Europe", "On cherche donc sur un autre continent", "Le skieur dit que là-bas, c'est l'hiver en même temps qu'ici",
             "Le pays a donc les mêmes saisons que la France", "Il se trouve dans l'hémisphère nord"],
            ["Tout commence à Besançon.", "Une saison identique veut dire le même hémisphère.", "Pour la justification : cherche « hémisphère sud »."],
            J("Quelle phrase de la fiche explique les saisons ?", M_HEMI, [M_ROUSSES, M_EMPLOIS, M_LOISIRS], pos=2)),
    }
    return d
