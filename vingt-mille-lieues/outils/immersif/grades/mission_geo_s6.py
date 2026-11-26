"""Séance 6 « Étretat, station balnéaire » : grades mousse, lieutenant, second (fiche : Le littoral touristique : la station balnéaire)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "mission-geo", "tests", "donnees"))
from fiches import *

FICHE = "« Le littoral touristique : la station balnéaire »"


def donnees(svg, bloc=None):
    d = {}
    d["e6-1"] = {
        "mousse": assoc(
            "Tu joues au guide. Relie chaque visiteur à l'activité qui lui plaira.",
            [("« Je veux marcher en haut des falaises. »", "le sentier GR21"), ("« Je veux acheter des souvenirs. »", "le marché couvert"),
             ("« J'adore les livres. »", "le Clos Lupin, maison d'un écrivain")],
            ["Ouvre la fiche " + FICHE + ".", "Le GR21 est un sentier de randonnée.", "Maurice Leblanc était écrivain."]),
        "lieutenant": tri(
            "Inès te confie le dépliant de l'office de tourisme. Range chaque proposition dans sa colonne, puis choisis la phrase de la fiche qui cite les activités d'Étretat.",
            [("nat", "Nature et sport"), ("pat", "Patrimoine"), ("loi", "Boutiques et loisirs")],
            [("la randonnée sur le sentier GR21", "nat"), ("le paddle au pied des arches", "nat"), ("le kayak le long des falaises", "nat"),
             ("le Clos Lupin, maison de Maurice Leblanc", "pat"), ("le château des Aygues, où ont séjourné des reines d'Espagne", "pat"),
             ("le marché couvert et ses boutiques", "loi"), ("le parc des Roches, pour les familles", "loi")],
            ["Le patrimoine, ce sont les richesses héritées du passé.", "Le paddle et le kayak se pratiquent sur la mer.", "Pour la justification : cherche « sentier GR21 »."],
            J("Quelle phrase de la fiche cite les activités proposées à Étretat ?", B_ACTIVITES, [B_DEF, B_ETRETAT, B_POSITIFS], pos=2)),
        "second": qcm(
            "La source teste ton déguisement de guide. Réponds à ses questions, puis choisis la phrase de la fiche qui présente Étretat.",
            [("Maurice Leblanc, qui vivait au Clos Lupin, a inventé quel personnage ?", ["Arsène Lupin", "Sherlock Holmes", "Tintin", "le capitaine Nemo"], 0,
              "L'une de ses aventures, « L'Aiguille creuse », se passe à Étretat."),
             ("Qui a séjourné au château des Aygues ?", ["des reines d'Espagne", "des rois de France", "des pêcheurs", "des moines"], 0, "C'était leur résidence d'été."),
             ("Au XIXᵉ siècle, Étretat s'est développée grâce à…", ["la mode des bains de mer", "une mine de charbon", "une grande usine", "un aéroport"], 0,
              "Les bains de mer ont attiré les premiers touristes."),
             ("Dans quelle région se trouve Étretat ?", ["la Normandie", "la Bretagne", "les Hauts-de-France", "la Nouvelle-Aquitaine"], 0, "En Seine-Maritime, au bord de la Manche.")],
            ["Arsène Lupin est un « gentleman cambrioleur ».", "Les reines venaient y passer l'été.", "Pour la justification : cherche « bains de mer »."],
            J("Quelle phrase de la fiche présente Étretat ?", B_ETRETAT, [B_ACTIVITES, B_DEF, B_CHIFFRES], pos=0)),
    }
    d["e6-2"] = {
        "mousse": trous(
            "Complète la définition du guide. Un mot est l'intrus.",
            "Une station balnéaire est un [[lieu]] de séjour situé en bord de [[mer]].",
            ["lieu", "mer", "montagne"],
            ["Ouvre la fiche " + FICHE + ".", "Balnéaire : qui concerne les bains de mer.", "La montagne est l'intrus."]),
        "lieutenant": ordre(
            "Le guide raconte l'histoire d'Étretat. Range les étapes dans l'ordre, de la plus ancienne à aujourd'hui, puis choisis la phrase de la fiche sur cette histoire.",
            ["Un village de pêcheurs au pied des falaises", "Au XIXᵉ siècle, la mode des bains de mer attire les premiers touristes",
             "On construit des villas, comme le château des Aygues et la maison de Maurice Leblanc", "Aujourd'hui, plus d'un million de visiteurs par an"],
            ["Avant les touristes, il y avait les pêcheurs.", "Les villas ont été construites pour les visiteurs fortunés.", "Pour la justification : cherche « XIXᵉ siècle »."],
            J("Quelle phrase de la fiche raconte comment Étretat s'est développée ?", B_ETRETAT, [B_CHIFFRES, B_ACTIVITES, B_DEPARTS], pos=1)),
        "second": trous(
            "Complète la fiche du guide (deux mots sont des intrus), puis choisis la phrase de la fiche qui définit une station balnéaire.",
            "Une station balnéaire est un lieu de [[séjour]] situé en bord de mer, [[aménagé]] pour accueillir des [[touristes]]. "
            "Quand il y a trop de visiteurs pour un lieu, on parle de [[surfréquentation]].",
            ["séjour", "aménagé", "touristes", "surfréquentation", "habitants", "industrie"],
            ["On vient y faire un séjour.", "Les touristes sont accueillis, pas les usines.", "Pour la justification : cherche « lieu de séjour »."],
            J("Quelle phrase de la fiche définit une station balnéaire ?", B_DEF, [B_SURFREQ, B_ETRETAT, B_CHIFFRES], pos=3)),
    }
    d["e6-3"] = {
        "mousse": tri(
            "Range chaque conséquence du tourisme : bonne ou mauvaise pour les habitants ?",
            [("p", "Bon pour les habitants"), ("n", "Mauvais pour les habitants")],
            [("des emplois dans les restaurants", "p"), ("des fêtes dans la ville", "p"), ("des embouteillages", "n"), ("des déchets sur la plage", "n")],
            ["Ouvre la fiche " + FICHE + ".", "Un emploi, c'est un travail : c'est bon.", "Les déchets salissent la plage."]),
        "lieutenant": vf(
            "Inès vérifie ce que tu as compris du témoignage. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur les effets négatifs.",
            [("Le tourisme crée des emplois dans les hôtels et les restaurants.", True, "C'est un effet positif."),
             ("Le tourisme fait baisser le prix des logements.", False, "Il le fait monter."),
             ("Les embouteillages gênent les habitants l'été.", True, "Des kilomètres de voitures cherchent une place."),
             ("Étretat reçoit moins de visiteurs qu'elle n'a d'habitants.", False, "Plus d'un million de visiteurs pour environ 1 100 habitants."),
             ("Des habitants partent car les logements coûtent trop cher.", True, "C'est ce que dit l'habitante.")],
            ["Relis le témoignage.", "1 000 000 de visiteurs, c'est beaucoup plus que 1 100 habitants.", "Pour la justification : cherche « hausse du prix des logements »."],
            J("Quelle phrase de la fiche cite les effets négatifs du tourisme ?", B_NEGATIFS, [B_POSITIFS, B_SURFREQ, B_CHIFFRES], pos=1)),
        "second": tri(
            "Chef de mission, classe les effets du tourisme selon ce qu'ils touchent. Range chaque carte, puis choisis la phrase de la fiche sur les effets positifs.",
            [("eco", "L'économie"), ("vie", "La vie des habitants"), ("nat", "L'environnement")],
            [("des emplois dans les hôtels et les restaurants", "eco"), ("des recettes pour les commerçants", "eco"),
             ("des logements de plus en plus chers", "vie"), ("des embouteillages et pas de place pour se garer", "vie"),
             ("des déchets abandonnés sur la plage", "nat"), ("l'air pollué par les files de voitures", "nat")],
            ["L'économie : le travail et l'argent.", "Les déchets et la pollution touchent l'environnement.", "Pour la justification : cherche « crée des emplois »."],
            J("Quelle phrase de la fiche cite les effets positifs du tourisme ?", B_POSITIFS, [B_NEGATIFS, B_ACTIVITES, B_DEF], pos=2)),
    }
    d["e6-4"] = {
        "lieutenant": code(
            "Inès a relevé les chiffres de l'Insee : Étretat comptait 1 469 habitants en 2011 et 1 102 en 2023. Calcule, puis choisis la phrase de la fiche qui donne ces chiffres.",
            [("Habitants perdus entre 2011 et 2023", "367", 3), ("Si elle en perdait encore autant, combien d'habitants resterait-il ?", "735", 3)],
            ["Pose la soustraction : 1 469 − 1 102.", "Puis 1 102 − 367.", "Pour la justification : cherche « 1 469 »."],
            J("Quelle phrase de la fiche donne l'évolution du nombre d'habitants ?", B_DEPARTS, [B_CHIFFRES, B_NEGATIFS, B_SURFREQ], pos=0)),
        "second": ordre(
            "Chef de mission, reconstitue l'enchaînement qui vide Étretat de ses habitants. Range les étapes dans l'ordre, puis choisis la phrase de la fiche sur la surfréquentation.",
            ["Plus d'un million de visiteurs viennent chaque année", "Les logements loués aux touristes se multiplient", "Le prix des logements augmente",
             "Des habitants ne trouvent plus à se loger et partent", "La commune cherche à mieux répartir les visites"],
            ["Tout commence par les visiteurs.", "Quand les prix montent, les habitants ont du mal à se loger.", "Pour la justification : cherche « mieux répartir »."],
            J("Quelle phrase de la fiche explique la surfréquentation ?", B_SURFREQ, [B_DEF, B_POSITIFS, B_ETRETAT], pos=3)),
    }
    return d
