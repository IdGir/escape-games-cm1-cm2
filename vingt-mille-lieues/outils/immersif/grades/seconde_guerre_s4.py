"""Message 4 « Le maquis » (printemps 1944) : grades mousse, lieutenant, second (fiche : La Résistance)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "seconde-guerre", "tests", "donnees"))
from fiches import *

FICHE = "« La Résistance »"
ALPHA = "<div class='doc-titre'><i>L'alphabet de Marc</i></div><p style='font-family:monospace;letter-spacing:.2em'>A B C D E F G H I J K L M N O P Q R S T U V W X Y Z</p>"


def donnees(svg, bloc=None):
    d = {}
    d["e4-1"] = {
        "mousse": code(
            "Marc a reçu le mot chiffré <b>N B R V J T</b>. Chaque lettre a été remplacée par la lettre suivante de l'alphabet. Recule chaque lettre d'une place pour trouver le mot." + ALPHA,
            [("Le mot en clair", "MAQUIS", 6)],
            ["Ouvre la fiche " + FICHE + ".", "N devient M, B devient A.", "C'est un groupe caché dans la forêt."]),
        "lieutenant": code(
            "Marc a reçu deux mots chiffrés : <b>Q N G W J</b> et <b>W J X N X Y J W</b>. Ici, chaque lettre a été avancée de <b>cinq</b> places. Recule-les de cinq places. Choisis ensuite la phrase de la fiche qui explique ce que sont les messages personnels." + ALPHA,
            [("Premier mot", "LIBRE", 5), ("Second mot", "RESISTER", 8)],
            ["Recule de cinq : F devient A.", "W devient R, J devient E.", "Pour la justification : cherche « ordres codés »."],
            J("Quelle phrase de la fiche explique ce que sont les messages personnels ?", S_MESSAGES, [S_RADIO, S_JOURNAUX, S_RESEAUX], pos=2)),
        "second": code(
            "Marc a reçu un message chiffré avec un décalage inconnu : <b>Y L F W R L U H</b>. Il sait que le message est un mot de huit lettres qui commence par V. Trouve le décalage, puis le mot. Choisis enfin la phrase de la fiche sur Radio Londres." + ALPHA,
            [("Décalage (nombre de places)", "3", 1, True), ("Le mot en clair", "VICTOIRE", 8)],
            ["Y est trois places après V.", "Recule chaque lettre de trois places.", "Pour la justification : cherche « Les Français parlent aux Français »."],
            J("Quelle phrase de la fiche décrit Radio Londres ?", S_RADIO, [S_MESSAGES, S_LONDRES, S_JOURNAUX], pos=0)),
    }
    d["e4-2"] = {
        "mousse": assoc(
            "Relie chaque mot à ce qu'il veut dire.",
            [("un maquis", "des résistants cachés dans la forêt"), ("un journal clandestin", "un journal imprimé en cachette"), ("Radio Londres", "la radio de la France libre")],
            ["Ouvre la fiche " + FICHE + ".", "Clandestin : en cachette.", "La radio parle depuis Londres."]),
        "lieutenant": assoc(
            "Relie chaque groupe à son rôle, puis choisis la phrase de la fiche qui décrit les réseaux de renseignement.",
            [("un maquis", "se cache dans la forêt"), ("un journal clandestin", "dit la vérité en cachette"), ("un réseau de renseignement", "informe les Alliés"),
             ("une agente de liaison", "transporte les messages"), ("la France libre", "continue la guerre depuis Londres")],
            ["Renseigner, c'est informer.", "La liaison relie les groupes.", "Pour la justification : cherche « observent l'occupant »."],
            J("Quelle phrase de la fiche décrit les réseaux de renseignement ?", S_RESEAUX, [S_JOURNAUX, S_MAQUIS, S_FEMMES], pos=1)),
        "second": assoc(
            "Relie chaque personne ou date à son rôle dans la Résistance, puis choisis la phrase de la fiche qui décrit le rôle de Jean Moulin.",
            [("le général de Gaulle", "dirige la France libre depuis Londres"), ("Jean Moulin", "unifie les mouvements de résistance"),
             ("27 mai 1943", "première réunion du CNR à Paris"), ("21 juin 1943", "arrestation de Jean Moulin près de Lyon"), ("les agentes de liaison", "transportent messages, tracts et papiers")],
            ["Moulin est envoyé par de Gaulle.", "Le CNR se réunit avant l'arrestation.", "Pour la justification : cherche « unifie »."],
            J("Quelle phrase de la fiche décrit le rôle de Jean Moulin ?", S_MOULIN, [S_ARRET, S_LONDRES, S_REFUS], pos=3)),
    }
    d["e4-3"] = {
        "mousse": tri(
            "Range chaque fiche : résister ou aider l'occupant ?",
            [("res", "Résister"), ("col", "Aider l'occupant")],
            [("écouter Radio Londres", "res"), ("cacher un jeune qui refuse de partir", "res"), ("dénoncer un voisin", "col")],
            ["Ouvre la fiche " + FICHE + ".", "Écouter Londres est interdit.", "Dénoncer aide l'occupant."]),
        "lieutenant": tri(
            "Range chaque fiche : résistance ou collaboration ? Puis choisis la phrase de la fiche qui définit le mot « résister ».",
            [("res", "Résistance"), ("col", "Collaboration")],
            [("imprimer des tracts", "res"), ("renseigner les Alliés", "res"), ("cacher un réfractaire", "res"),
             ("la rencontre de Montoire", "col"), ("la Milice qui pourchasse les résistants", "col"), ("dénoncer un voisin", "col")],
            ["Montoire : Pétain et Hitler.", "La Milice aide l'occupant.", "Pour la justification : cherche « refuser la défaite »."],
            J("Quelle phrase de la fiche définit le mot « résister » ?", S_REFUS, [S_RISQUE, S_LONDRES, S_MAQUIS], pos=0)),
        "second": tri(
            "En 1943, tous les Français ne font pas le même choix. Range chaque situation, puis choisis la phrase de la fiche qui dit combien de Français résistent.",
            [("res", "Résister"), ("col", "Collaborer"), ("attente", "Attendre et essayer de vivre")],
            [("rejoindre un maquis", "res"), ("transporter des messages à vélo", "res"), ("travailler pour la police de l'occupant", "col"),
             ("dénoncer un voisin", "col"), ("faire la queue et se taire", "attente"), ("attendre la fin de la guerre sans agir", "attente")],
            ["Beaucoup de Français attendent.", "Les résistants sont peu nombreux au début.", "Pour la justification : cherche « minorité »."],
            J("Quelle phrase de la fiche dit si les résistants sont nombreux ?", S_RISQUE, [S_REFUS, S_MAQUIS, S_FEMMES], pos=2)),
    }
    d["e4-4"] = {
        "lieutenant": qcm(
            "Marc écoute Londres. Réponds, puis choisis la phrase de la fiche qui décrit les maquis.",
            [("Comment s'appelle l'émission de la BBC en français ?", ["« Les Français parlent aux Français »", "« Ici Vichy »", "« Radio Paris »", "« La voix du maquis »"], 0, "Depuis Londres."),
             ("Pourquoi les messages sont-ils codés ?", ["pour que l'occupant ne les comprenne pas", "pour amuser les auditeurs", "pour aller plus vite", "parce que la radio est en anglais"], 0, "Ce sont des ordres secrets."),
             ("Qui forme les maquis à partir de 1943 ?", ["des soldats allemands", "des jeunes réfractaires au STO", "les ministres de Vichy", "des touristes"], 1, "Ils se cachent dans les forêts."),
             ("Qui réunit le Conseil national de la Résistance ?", ["Jean Moulin", "Pétain", "Leclerc", "Hitler"], 0, "Le 27 mai 1943.")],
            ["Les messages sont des ordres secrets.", "Les maquis accueillent les réfractaires.", "Pour la justification : cherche « Morvan »."],
            J("Quelle phrase de la fiche décrit les maquis ?", S_MAQUIS, [S_RESEAUX, S_REFUS, S_MOULIN], pos=3)),
        "second": qcm(
            "Marc interroge les messagers avant de les envoyer en mission. Réponds, puis choisis la phrase de la fiche sur le sort de Jean Moulin.",
            [("Pourquoi le CNR est-il important ?", ["il unit des mouvements de résistance très différents", "il signe l'armistice", "il dirige Vichy", "il crée le STO"], 0, "Le 27 mai 1943."),
             ("Combien de temps sépare la première réunion du CNR et l'arrestation de Jean Moulin ?", ["moins d'un mois", "un an", "cinq ans", "deux jours"], 0, "Du 27 mai au 21 juin 1943."),
             ("Quel risque prend un résistant ?", ["aucun", "l'arrestation, la déportation ou la mort", "une amende", "perdre son vélo"], 1, "Ils risquent leur vie."),
             ("Pourquoi les résistants sont-ils plus nombreux à partir de 1943 ?", ["à cause du STO et de l'espoir d'une victoire des Alliés", "parce que la guerre est finie", "parce que Vichy le demande", "parce que l'occupant est parti"], 0, "Le STO pousse des jeunes vers les maquis.")],
            ["Le CNR unit les mouvements.", "Mai, puis juin 1943.", "Pour la justification : cherche « sans avoir parlé »."],
            J("Quelle phrase de la fiche raconte le sort de Jean Moulin ?", S_ARRET, [S_MOULIN, S_RISQUE, S_LONDRES], pos=1)),
    }
    return d
