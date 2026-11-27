"""Séance 11 « Chaînes de production » : grades mousse, lieutenant, second (fiche : La chaîne de production d un aliment)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "mission-geo", "tests", "donnees"))
from fiches import *
import schemas as S

FICHE = "« La chaîne de production d'un aliment »"
ETAPES = ("Les étapes du trajet : 1. les vaches pâturent ; 2. la traite ; 3. le camion-citerne collecte le lait ; 4. le lait arrive à l'usine et il est analysé ; "
          "5. le lait est chauffé et ensemencé de ferments ; 6. le yaourt est versé dans des pots ; 7. un camion frigorifique livre les magasins ; 8. le yaourt est vendu au rayon frais.")


def donnees(svg, bloc=None):
    d = {}
    d["e11-1"] = {
        "mousse": ordre(
            "Manon te montre le trajet du lait. Remets les étapes dans l'ordre.",
            ["La traite : le lait est recueilli", "Le camion-citerne apporte le lait à l'usine", "L'usine fabrique le yaourt", "Le yaourt est vendu au magasin"],
            ["Ouvre la fiche " + FICHE + ".", "Tout commence à la ferme.", "Le yaourt finit au magasin."]),
        "lieutenant": tri(
            "Manon range ses étapes selon l'endroit où elles se passent. Place chaque étape, puis choisis la phrase de la fiche qui dit ce qui se passe à la ferme.",
            [("fe", "À la ferme"), ("ca", "Dans un camion"), ("us", "À l'usine"), ("ma", "Au magasin")],
            [("La traite des vaches", "fe"), ("Le lait est refroidi dans un tank", "fe"), ("Le camion-citerne collecte le lait", "ca"), ("Un camion frigorifique livre les supermarchés", "ca"),
             ("Le lait est analysé", "us"), ("Des ferments sont ajoutés au lait", "us"), ("Le yaourt est versé dans des pots", "us"), ("Le yaourt est vendu au rayon frais", "ma")],
            ["Le tank est à la ferme.", "Il y a deux transports en camion.", "Pour la justification : cherche « tank réfrigéré »."],
            J("Quelle phrase de la fiche dit ce qui se passe à la ferme ?", Y_FERME, [Y_TRANSPORT, Y_USINE, Y_POTS], pos=0)),
        "second": ordre(
            "Reconstitue tout le trajet du lait, puis choisis la phrase de la fiche qui décrit la chaîne de production.",
            ["Les vaches pâturent au pré", "La traite : le lait est recueilli, puis refroidi", "Le camion-citerne réfrigéré collecte le lait", "Le lait arrive à l'usine et il est analysé",
             "Le lait est chauffé, ensemencé de ferments, puis il repose", "Le yaourt est versé dans des pots", "Un camion frigorifique livre les magasins", "Le yaourt est vendu au rayon frais"],
            ["Les vaches sont au pré avant la traite.", "Le lait est analysé avant d'être transformé.", "Pour la justification : cherche « séparent la matière première »."],
            J("Quelle phrase de la fiche décrit ce qu'est une chaîne de production ?", Y_CHAINE, [Y_FROID, Y_USINE, Y_DISTRI], pos=2)),
    }
    d["e11-2"] = {
        "mousse": trous(
            "Complète le texte de Manon. Un mot est un intrus.",
            "Le lait vient de la [[ferme]]. Un [[camion]] l'apporte à l'[[usine]]. Là, on fabrique le [[yaourt]]. Il est vendu au [[magasin]].",
            ["ferme", "camion", "usine", "yaourt", "magasin", "cuit"],
            ["Ouvre la fiche " + FICHE + ".", "Un camion transporte le lait.", "Le yaourt est fabriqué à l'usine."]),
        "lieutenant": qcm(
            "Manon vérifie ce que tu as retenu. Réponds, puis choisis la phrase de la fiche sur la chaîne du froid.",
            [("Pourquoi le camion-citerne est-il réfrigéré ?", ["pour que le lait ne tourne pas", "pour fabriquer des glaçons", "pour que le lait épaississe", "pour économiser de l'essence"], 0, "Sans froid, des microbes se développent."),
             ("Dans quel secteur classe-t-on l'usine de yaourts ?", ["le secteur secondaire", "le secteur primaire", "le secteur tertiaire", "aucun secteur"], 0, "Elle transforme une matière première."),
             ("Qu'est-ce qui fait fermenter le lait ?", ["les ferments ajoutés", "le sel", "la lumière", "le sucre"], 0, "Des ferments sont ajoutés, puis le mélange repose.")],
            ["Sans froid, le lait se gâte.", "Transformer, c'est du secondaire.", "Pour la justification : cherche « microbes »."],
            J("Quelle phrase de la fiche parle de la chaîne du froid ?", Y_FROID, [Y_FERME, Y_CHAINE, Y_SECTEUR], pos=2)),
        "second": vf(
            "Manon vérifie ta connaissance de la chaîne du froid. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur la chaîne du froid.",
            [("Le lait peut rester plusieurs heures sans froid avant d'arriver à l'usine.", False, "Sans réfrigération, des microbes se développent et le lait tourne."),
             ("Un camion-citerne réfrigéré collecte le lait.", True, "Le froid est maintenu pendant le transport."),
             ("À l'usine, des ferments transforment le lait en yaourt.", True, "Le mélange repose : le yaourt fermente."),
             ("La chaîne du froid s'arrête à la sortie de l'usine.", False, "Des camions frigorifiques livrent les supermarchés."),
             ("Le yaourt est vendu au rayon frais.", True, "Il reste au froid jusqu'au consommateur.")],
            ["Un lait qui tourne est impropre à la consommation.", "Les camions qui livrent les supermarchés sont frigorifiques.", "Pour la justification : cherche « jamais être interrompue »."],
            J("Quelle phrase de la fiche parle de la chaîne du froid ?", Y_FROID, [Y_FERME, Y_DISTRI, Y_TRANSPORT], pos=0)),
    }
    d["e11-3"] = {
        "mousse": vf(
            "Manon te pose trois questions. Pour chaque phrase, choisis vrai ou faux.",
            [("Le lait est transporté dans un camion réfrigéré.", True, "Le froid garde le lait en bon état."),
             ("Le lait n'a pas besoin de froid.", False, "Sans froid, le lait tourne."),
             ("Le yaourt est fabriqué à l'usine.", True, "Avec du lait et des ferments.")],
            ["Ouvre la fiche " + FICHE + ".", "Le froid garde le lait.", "L'usine transforme le lait."]),
        "lieutenant": ordre(
            "Manon te détaille le travail de l'usine. Range les étapes qui s'y déroulent dans l'ordre, puis choisis la phrase de la fiche qui les décrit.",
            ["Le lait arrive à l'usine et il est analysé", "Le lait est stocké dans de grands réservoirs", "Le lait est chauffé et des ferments sont ajoutés", "Le mélange repose : le yaourt fermente", "Le yaourt est versé dans des pots"],
            ["On analyse le lait dès son arrivée.", "Les ferments sont ajoutés quand le lait est chaud.", "Pour la justification : cherche « grands réservoirs »."],
            J("Quelle phrase de la fiche décrit ce que fait l'usine ?", Y_USINE, [Y_POTS, Y_FERME, Y_TRANSPORT], pos=1)),
        "second": trous(
            "Complète le carnet de Manon (deux mots sont des intrus), puis choisis la phrase de la fiche sur le tank réfrigéré.",
            "À la ferme, le lait est immédiatement [[refroidi]] puis stocké dans un [[tank]] réfrigéré. Un [[camion-citerne]] le collecte et l'apporte à l'[[usine]]. Là, il est chauffé, des [[ferments]] sont ajoutés et le yaourt [[fermente]].",
            ["refroidi", "tank", "camion-citerne", "usine", "ferments", "fermente", "congelé", "pots"],
            ["Le lait est refroidi, jamais congelé.", "Les ferments transforment le lait en yaourt.", "Pour la justification : cherche « tank »."],
            J("Quelle phrase de la fiche parle du tank réfrigéré ?", Y_FERME, [Y_TRANSPORT, Y_CHAINE, Y_USINE], pos=2)),
    }
    d["e11-4"] = {
        "lieutenant": code(
            "Le directeur te fait compter. " + ETAPES + " Compte, puis choisis la phrase de la fiche qui décrit la chaîne de production.",
            [("Étapes à l'intérieur de l'usine", "3", 1), ("Étapes en tout", "8", 1), ("Transports en camion", "2", 1)],
            ["L'analyse, la transformation et la mise en pots ont lieu à l'usine.", "Compte toutes les étapes de la liste.", "Cherche les mots « camion ». Pour la justification : cherche « de l'assiette »."],
            J("Quelle phrase de la fiche décrit ce qu'est une chaîne de production ?", Y_CHAINE, [Y_FROID, Y_USINE, Y_DISTRI], pos=0)),
        "second": assoc(
            "Chaque lieu du trajet du lait relève d'un secteur d'activité. Relie-les, puis choisis la phrase de la fiche qui les cite.",
            [("la ferme de Bray", "le secteur primaire"), ("l'usine de yaourts", "le secteur secondaire"), ("le supermarché", "le secteur tertiaire")],
            ["La ferme exploite directement la nature.", "L'usine transforme le lait.", "Pour la justification : cherche « le supermarché du secteur tertiaire »."],
            J("Quelle phrase de la fiche classe la ferme, l'usine et le supermarché ?", Y_SECTEUR, [Y_FROID, Y_CHAINE, Y_DISTRI], pos=3)),
    }
    return d
