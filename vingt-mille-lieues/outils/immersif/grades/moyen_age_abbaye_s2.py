"""Salle 2 « La cour de Charlemagne » (fiche : charlemagne)."""
from aide import *

F = "« Charlemagne, son empire et les écoles »"
G1 = "Charlemagne devient roi des Francs en 768."
G2 = "Par la guerre, il réunit un territoire immense : la France et la Belgique actuelles, une grande partie de l'Allemagne, le nord de l'Italie, une bande du nord de l'Espagne."
G3 = "Le 25 décembre 800, dans la basilique Saint-Pierre de Rome, le pape Léon III le couronne empereur. Pour la première fois depuis 476, un empereur règne de nouveau en Occident."
G4 = "Charlemagne installe sa cour à Aix-la-Chapelle. Il confie chaque région à un comte et envoie des inspecteurs, les missi dominici (« envoyés du maître »), vérifier que ses ordres sont appliqués."
G5 = "Ses décisions écrites s'appellent des capitulaires."
G6 = "Le capitulaire Admonitio generalis (789) demande que des écoles soient ouvertes dans les monastères et les évêchés."
G7 = "Charlemagne fait venir des savants, dont Alcuin."
G8 = "Dans les ateliers de copie se répand une écriture régulière et facile à lire : la minuscule caroline, avec des espaces entre les mots."
G9 = "Charlemagne n'a pas « inventé l'école ». Les écoles des monastères et des évêchés existaient avant lui, elles restaient réservées à peu d'enfants, et lui-même savait lire mais écrivait très mal."


def donnees(svg, bloc=None):
    d = {}
    d["e2-1"] = {
        "mousse": ordre(
            "Remets les événements dans l'ordre, du plus ancien (en haut) au plus récent (en bas), avec les flèches ▲▼.",
            [("Charlemagne devient roi des Francs", "768"), ("Charlemagne est couronné empereur à Rome", "800"), ("Charlemagne meurt à Aix-la-Chapelle", "814")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "On devient roi avant de devenir empereur.", "La mort vient en dernier : 814."]),
        "lieutenant": qcm(
            carnet("Un ordre de Charlemagne", "(d'après l'Admonitio generalis, 789, texte adapté). « Qu'il y ait des écoles pour apprendre à lire aux enfants. Que dans chaque monastère et chaque évêché, on enseigne les psaumes, les notes, le chant, le calcul et la grammaire. »")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("En quelle année cet ordre est-il donné ?", ["789", "800", "768", "814"], 0, "L'Admonitio generalis date de 789."),
             ("Où demande-t-il d'ouvrir des écoles ?", ["Dans les monastères et les évêchés", "Dans tous les villages", "Dans le palais seulement", "À Rome"], 0, "Il s'adresse aux monastères et aux évêchés."),
             ("Charlemagne a-t-il « inventé l'école » ?", ["Non : des écoles existaient avant lui", "Oui : avant lui, il n'y avait aucune école", "Oui : il a ouvert une école dans chaque village", "On ne sait pas"], 0, "Les écoles étaient réservées à peu d'enfants.")],
            ["La date est dans le document de la fiche.", "Le document cite deux sortes de lieux.", "Relis la fin de la fiche : « à ne pas croire »."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", G6, [G5, G7, G8], pos=1)),
        "second": vf(
            "Aude a noté six phrases sur Charlemagne et les écoles. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui corrige l'idée « Charlemagne a inventé l'école ».",
            [("Charlemagne devient roi des Francs en 768.", True, "Puis empereur en 800."), ("Charlemagne a inventé l'école.", False, "Elle existait avant lui."), ("Les écoles des monastères existaient avant Charlemagne.", True, "Elles restaient réservées à peu d'enfants."),
             ("Charlemagne écrivait très bien.", False, "Il savait lire mais écrivait très mal."), ("Alcuin est un savant venu au palais.", True, "Charlemagne fait venir des savants."), ("L'Admonitio generalis date de 800.", False, "Elle date de 789.")],
            ["Les écoles existaient avant lui.", "Il écrivait très mal.", "789, pas 800."],
            J("Quelle phrase de la fiche corrige l'idée « Charlemagne a inventé l'école » ?", G9, [G6, G7, G4], pos=2)),
    }
    d["e2-2"] = {
        "mousse": trous(
            "Complète le texte : clique sur une étiquette, puis sur le trou où elle va. Une étiquette est en trop.",
            "Charlemagne est le roi des [[Francs]]. Le jour de [[Noël]] de l'an 800, à [[Rome]], le pape le couronne empereur. Il vit à Aix-la-Chapelle.",
            ["Francs", "Noël", "Rome", "Paris"],
            ["Ouvre la fiche " + F + ".", "Le couronnement a lieu un 25 décembre.", "Le pape habite à Rome."]),
        "lieutenant": ordre(
            "Aude explique comment Charlemagne gouverne. Remets ces cinq étapes dans l'ordre, puis choisis la phrase de la fiche qui décrit le gouvernement de l'empire.",
            ["Charlemagne devient roi des Francs (768).", "Il réunit un territoire immense par la guerre.", "Il demande des écoles dans les monastères et les évêchés (789).", "Il est couronné empereur à Rome (800).", "Il confie chaque région à un comte et envoie des missi dominici."],
            ["768 vient avant 789, qui vient avant 800.", "On gouverne un empire après l'avoir couronné.", "Les missi dominici contrôlent les comtes."],
            J("Quelle phrase de la fiche décrit le gouvernement de l'empire ?", G4, [G2, G5, G3], pos=0)),
        "second": tri(
            "Aude classe des éléments selon qu'ils existent avant ou grâce à Charlemagne. Range chaque carte, puis choisis la phrase de la fiche qui parle de l'écriture.",
            [("avant", "Existait avant Charlemagne"), ("grace", "Se répand sous Charlemagne")],
            [("Des écoles dans les monastères", "avant"), ("Des écoles dans les évêchés", "avant"), ("Des écoles réservées à peu d'enfants", "avant"), ("La minuscule caroline", "grace"), ("Des espaces entre les mots", "grace"), ("Les capitulaires envoyés dans l'empire", "grace")],
            ["Les écoles existaient avant lui.", "La minuscule caroline se répand dans les ateliers de copie.", "Les capitulaires sont ses décisions écrites."],
            J("Quelle phrase de la fiche parle de la minuscule caroline ?", G8, [G6, G9, G5], pos=1)),
    }
    d["e2-3"] = {
        "mousse": assoc(
            "Relie chaque nom à ce qu'il désigne. Clique sur un nom, puis sur sa description.",
            [("Aix-la-Chapelle", "la ville du palais de Charlemagne"), ("Rome", "la ville où Charlemagne est couronné"), ("Léon III", "le pape qui couronne Charlemagne")],
            ["Ouvre la fiche " + F + ".", "Le palais et la chapelle donnent son nom à la ville.", "Le pape habite à Rome."]),
        "lieutenant": {
            "type": "plan", "titre": "La cour de Charlemagne", "colonnes": 2,
            "cases": [{"libelle": "Le pape qui couronne Charlemagne", "reponse": "Léon III"}, {"libelle": "Le savant venu au palais", "reponse": "Alcuin"}, {"libelle": "Les inspecteurs envoyés par l'empereur", "reponse": "les missi dominici"},
                      {"libelle": "Les décisions écrites de l'empereur", "reponse": "les capitulaires"}, {"libelle": "L'écriture ronde et régulière des copistes", "reponse": "la minuscule caroline"}, {"libelle": "L'homme qui gouverne une région", "reponse": "le comte"}],
            "etiquettes": ["Léon III", "Alcuin", "les missi dominici", "les capitulaires", "la minuscule caroline", "le comte", "Remi", "Syagrius"],
            "consigne": "Aude complète le tableau de la cour de Charlemagne. Place chaque étiquette dans la bonne case. Deux étiquettes sont en trop. Puis choisis la phrase de la fiche qui définit les missi dominici.",
            "indices": ["Les capitulaires sont des décisions écrites.", "Le comte gouverne une région.", "Remi et Syagrius sont de l'époque de Clovis."],
            "justification": J("Quelle phrase de la fiche définit les missi dominici ?", G4, [G5, G7, G8], pos=1)},
        "second": qcm(
            carnet("Notes d'Aude", "(d'après la fiche). Le territoire de Charlemagne couvre la France et la Belgique actuelles, une grande partie de l'Allemagne, le nord de l'Italie et une bande du nord de l'Espagne. Pour la première fois depuis 476, un empereur règne en Occident.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Combien d'années sans empereur en Occident entre 476 et 800 ?", ["324 ans", "300 ans", "476 ans", "800 ans"], 0, "800 − 476 = 324."),
             ("Pourquoi le couronnement de 800 est-il important ?", ["Un empereur règne de nouveau en Occident", "Charlemagne devient roi des Francs", "L'empire disparaît", "Rome est détruite"], 0, "Pour la première fois depuis 476."),
             ("Quelle partie de l'Espagne l'empire prend-il ?", ["Une bande du nord", "Toute l'Espagne", "Le sud seulement", "Aucune"], 0, "Une bande du nord.")],
            ["Soustrais 476 de 800.", "Un empereur manquait depuis 476.", "Relis la liste des territoires."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", G3, [G2, G1, G4], pos=0)),
    }
    d["e2-4"] = {
        "lieutenant": lettres(
            "Trouve le mot qui correspond à cette définition : « Écriture ronde et régulière des ateliers de copie, avec des espaces entre les mots. » C'est un adjectif tiré du nom de l'empereur. Ses lettres sont cachées en couleur dans le texte d'Aude, dans le désordre. Clique-les dans l'ordre qui forme le mot (8 lettres). Deux lettres sont des pièges.",
            ["C", "A", "R", "O", "L", "I", "N", "E"],
            marque("Aude raconte sa journée au palais : « Le matin, je [r]épète mes lettres sous la direction d'Alcuin. Mon [l]ivre est neuf, ses pages sont [c]laires, et chaque mot est séparé par un espace. Le soir, on [i]nspecte nos cahiers ; Alcuin [n]ote nos progrès. [E]nfin, je range ma [p]lume, car je suis f[a]tiguée. Puis je lis [o]u je dessine, [s]ans bruit. »"),
            ["Le mot a huit lettres.", "Il commence par C et finit par E.", "C'est le nom de l'écriture de l'époque de Charlemagne : minuscule…"],
            J("Quelle phrase de la fiche cite ce mot ?", G8, [G6, G7, G5], pos=1)),
        "second": lettres(
            "Trouve le mot qui correspond à cette définition : « Savant que Charlemagne fait venir au palais pour enseigner. » Ses lettres sont cachées en couleur dans le texte d'Aude, dans le désordre. Clique-les dans l'ordre qui forme le mot (6 lettres). Deux lettres sont des pièges.",
            ["A", "L", "C", "U", "I", "N"],
            marque("Au palais, l'empereur fait venir des savants. Aude écrit : « Le plus [c]élèbre m'a appris [l]es lettres. Il parle de [n]ombreux sujets ; je [u]se de ma plume, en [i]nclinant la tête. L'hiver, nous [a]llons près du feu. Je [m]arque mes cahiers, [p]uis je dors. »"),
            ["Le mot a six lettres.", "Il commence par A et finit par N.", "C'est le nom du savant cité dans la fiche."],
            J("Quelle phrase de la fiche cite ce savant ?", G7, [G6, G8, G9], pos=2)),
    }
    return d
