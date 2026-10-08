"""Salle 5 « Le bulletin du jour » (fiche : bulletin)."""
from aide import *

F = "« De la mesure à la prévision : météo et climat »"
U1 = "Une prévision s'appuie sur des milliers de mesures fiables, prises partout de la même façon."
U2 = "À l'école, nos trois capteurs donnent déjà l'essentiel : température, vent, pluie."
U3 = "Météo : l'état de l'atmosphère à un endroit et à un moment donnés ; il change d'heure en heure."
U4 = "Climat : une moyenne statistique de ces conditions sur une longue période."
U5 = "Les climatologues utilisent des périodes de référence de trente ans ; les moyennes obtenues s'appellent les « normales »."
U6 = "Une journée froide ne dit rien, à elle seule, du climat : il faut de longues séries de mesures."


def donnees(svg, bloc=None):
    d = {}
    d["e5-1"] = {
        "mousse": tri(
            "Madame Vasseur a mélangé ses fiches. Range chaque phrase : météo (un jour précis) ou climat (le temps habituel) ? Clique sur une carte, puis sur une colonne.",
            [("meteo", "Météo"), ("climat", "Climat")],
            [("Demain, il pleuvra l'après-midi.", "meteo"), ("Ce matin, il fait 12 °C dans la cour.", "meteo"), ("Au Sahara, il pleut très peu tout au long de l'année.", "climat"), ("Chez nous, l'hiver est en général plus froid que l'été.", "climat")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "« Demain » ou « ce matin » : météo.", "« En général » : climat."]),
        "lieutenant": tri(
            "Madame Vasseur classe des phrases. Range chaque phrase : météo ou climat ? Puis choisis la phrase de la fiche qui définit le climat.",
            [("meteo", "Météo"), ("climat", "Climat")],
            [("Hier, il est tombé 12 mm de pluie.", "meteo"), ("Ce soir, le vent va tourner au nord.", "meteo"), ("Samedi, il gèle à −4 °C.", "meteo"),
             ("À Brest, il pleut plus qu'à Marseille en moyenne.", "climat"), ("Les normales sont calculées sur trente ans.", "climat"), ("Sous l'équateur, il fait chaud toute l'année.", "climat")],
            ["Un jour précis : météo.", "Une moyenne sur des années : climat.", "Trente ans : les normales."],
            J("Quelle phrase de la fiche définit le climat ?", U4, [U3, U1, U6], pos=1)),
        "second": tri(
            "Madame Vasseur classe des affirmations. Range chaque affirmation : la fiche l'affirme, ou elle ne l'affirme pas. Puis choisis la phrase de la fiche qui explique pourquoi une journée froide ne dit rien du climat.",
            [("oui", "La fiche l'affirme"), ("non", "La fiche ne l'affirme pas")],
            [("Une prévision s'appuie sur des milliers de mesures fiables.", "oui"), ("Les normales sont calculées sur trente ans.", "oui"), ("Il faut de longues séries de mesures pour parler du climat.", "oui"),
             ("Une seule journée froide suffit à décrire le climat.", "non"), ("La météo est une moyenne sur trente ans.", "non"), ("Le climat change d'heure en heure.", "non")],
            ["La météo change d'heure en heure.", "Le climat est une moyenne sur une longue période.", "Une seule journée ne suffit pas."],
            J("Quelle phrase de la fiche explique pourquoi une journée froide ne dit rien du climat ?", U6, [U4, U5, U3], pos=1)),
    }
    d["e5-2"] = {
        "mousse": assoc(
            "Pour la sortie, relie chaque prévision au bon conseil. Clique à gauche, puis à droite.",
            [("Pluie annoncée l'après-midi", "prendre un vêtement de pluie"), ("Soleil et 21 °C", "casquette et gourde d'eau"), ("−2 °C au petit matin", "bonnet, gants, sol glissant")],
            ["Ouvre la fiche " + F + ".", "Contre la pluie, un vêtement qui ne laisse pas passer l'eau.", "Sous zéro, on se couvre."]),
        "lieutenant": qcm(
            carnet("Bulletin de la station", "(inventé pour le jeu). « Mercredi : température maximale 21 °C, vent moyen 24 km/h, pluie 7 mm. Pour la sortie, matinée sèche, puis averses en fin de journée. »")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("Quelle température maximale annonce le bulletin ?", ["21 °C", "24 °C", "7 °C", "12 °C"], 0, "Maximale : 21 °C."), ("Quel conseil pour la fin de journée ?", ["Prendre un vêtement de pluie", "Prendre un chapeau de soleil", "Prendre des gants", "Rester à l'ombre"], 0, "Averses en fin de journée."),
             ("Sur quoi s'appuie la prévision ?", ["Sur des milliers de mesures fiables, prises partout de la même façon", "Sur une seule mesure", "Sur le hasard", "Sur la couleur du ciel"], 0, "Une prévision repose sur des mesures.")],
            ["Relis la température maximale.", "Averses : vêtement de pluie.", "La prévision s'appuie sur des mesures."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", U1, [U2, U3, U5], pos=1)),
        "second": vf(
            "Madame Vasseur a noté six phrases sur le bulletin. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui cite les trois capteurs de l'école.",
            [("Nos trois capteurs de l'école mesurent la température, le vent et la pluie.", True, "L'essentiel."), ("Le bulletin traduit les nombres en décisions.", True, "Par exemple, prendre un vêtement de pluie."), ("Une prévision s'appuie sur une seule mesure.", False, "Sur des milliers."),
             ("Les mesures sont prises partout de la même façon.", True, "Pour être fiables."), ("La météo est une moyenne sur trente ans.", False, "C'est le climat."), ("Les normales sont des moyennes sur dix ans.", False, "Sur trente ans.")],
            ["Trois capteurs : température, vent, pluie.", "Une prévision repose sur de nombreuses mesures.", "Les normales : trente ans."],
            J("Quelle phrase de la fiche cite les trois capteurs de l'école ?", U2, [U1, U3, U5], pos=0)),
    }
    d["e5-3"] = {
        "lieutenant": lettres(
            "Trouve le mot qui correspond à cette définition : « Le temps habituel d'une région, calculé sur une longue période. » Ses lettres sont cachées en couleur dans le bulletin de Lina, dans le désordre. Clique-les dans l'ordre qui forme le mot (6 lettres). Deux lettres sont des pièges.",
            ["C", "L", "I", "M", "A", "T"],
            marque("Bonjour à tous. Ce [m]atin, le thermomètre indique 12 °C. Le vent est faible, la pluie [l]oin. Demain, une [t]rès belle journée. Pour le [c]limat, il faut des années de mesures : [i]l ne suffit pas d'un jour. Nous [a]ttendons des nuages ce soir. Et [s]oyez prudents ! [p]as de panique."),
            ["Le mot a six lettres.", "Il commence par C.", "Météo : un jour. … : une longue période."],
            J("Quelle phrase de la fiche cite ce mot ?", U4, [U3, U1, U2], pos=2)),
        "second": lettres(
            "Trouve le mot qui correspond à cette définition : « Valeur moyenne calculée sur trente ans. » Ses lettres sont cachées en couleur dans le bulletin de Lina, dans le désordre. Clique-les dans l'ordre qui forme le mot (8 lettres). Deux lettres sont des pièges.",
            ["N", "O", "R", "M", "A", "L", "E", "S"],
            marque("Bonjour à tous. Mercredi, le vent a soufflé à 24 km/h. Pour comparer nos [m]esures aux moyennes de trente ans, les climatologues l[e]s ordonnent [r]égulièrement. [S]elon la station, [o]n note aussi la pluie. Le [l]ong travail est [a]ttentif ; l'[n]ormalité se calcule sur trente ans. [p]ar contre, la météo d'un jour ne dit rien. [t]out le monde est invité."),
            ["Le mot a huit lettres.", "Il commence par N et finit par S.", "On parle des « … » de température sur trente ans."],
            J("Quelle phrase de la fiche cite ce mot ?", U5, [U4, U3, U6], pos=1)),
    }
    d["e5-4"] = {
        "mousse": code(
            "Pour lancer le bulletin, entre la valeur de vérité de mercredi : la température maximale et la hauteur de pluie, lues dans les modules précédents.",
            [("Température maximale (°C)", "21", 2), ("Hauteur de pluie (mm)", "7", 1)],
            ["Ouvre la fiche " + F + ".", "La température maximale a été lue à 15 h.", "La pluie de mercredi : un nombre plus petit que 10."]),
        "lieutenant": code(
            "Pour lancer le bulletin, entre la valeur de vérité de jeudi, relue dans le tableau : le maximum, le vent moyen et la hauteur de pluie. Jeudi : minimum 8 °C, maximum 14 °C, vent 30 km/h, pluie 12 mm.",
            [("Température maximale (°C)", "14", 2), ("Vent moyen (km/h)", "30", 2), ("Hauteur de pluie (mm)", "12", 2)],
            ["Relis la ligne « Maximum » du tableau.", "Le vent de jeudi est le plus fort de la semaine.", "La pluie de jeudi : 12 mm."],
            J("Quelle phrase de la fiche cite les trois mesures du bulletin ?", U2, [U1, U3, U6], pos=1)),
        "second": code(
            "Pour lancer le bulletin, entre la valeur de vérité de mardi, relue dans le tableau : l'écart de température (maximum 19 °C, minimum 11 °C), le vent moyen et le cumul de pluie de lundi et mardi (lundi 0 mm, mardi 3 mm). Mardi : vent 18 km/h.",
            [("Écart de température (°C)", "8", 1), ("Vent moyen (km/h)", "18", 2), ("Cumul de pluie lundi et mardi (mm)", "3", 1)],
            ["Écart : 19 − 11.", "Le vent de mardi est donné.", "Cumul : 0 + 3."],
            J("Quelle phrase de la fiche explique pourquoi les mesures doivent être fiables ?", U1, [U2, U3, U4], pos=2)),
    }
    return d
