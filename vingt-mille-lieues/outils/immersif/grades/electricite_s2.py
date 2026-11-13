"""Salle 2 « Le magasin de matériel » : grades mousse, lieutenant, second (fiche : Conducteurs et isolants)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "electricite", "tests", "donnees"))
from fiches import *

FICHE = "« Conducteurs et isolants »"


def donnees(svg, bloc=None):
    d = {}
    d["e2-1"] = {
        "mousse": tri(
            "Maëlle a testé ces objets. Range chacun : conducteur (la lampe s'allume) ou isolant (elle reste éteinte).",
            [("cond", "Conducteur"), ("isol", "Isolant")],
            [("une clé en fer", "cond"), ("un trombone", "cond"), ("une règle en plastique", "isol"), ("un bouchon en liège", "isol"), ("une gomme", "isol")],
            ["Ouvre la fiche " + FICHE + ".", "Les métaux sont conducteurs.", "Le plastique, le liège et la gomme sont isolants."]),
        "lieutenant": tri(
            "Maëlle a testé huit objets du bac. Range chacun, puis choisis la phrase de la fiche qui explique le cas de la mine de crayon.",
            [("cond", "Conducteur"), ("isol", "Isolant")],
            [("la mine d'un crayon à papier", "cond"), ("une pièce de monnaie", "cond"), ("une vis en acier", "cond"), ("du papier d'aluminium", "cond"),
             ("le bois du crayon", "isol"), ("une bille en verre", "isol"), ("un élastique en caoutchouc", "isol"), ("une feuille de papier", "isol")],
            ["La mine est en graphite.", "L'acier est un métal.", "Pour la justification : cherche « graphite »."],
            J("Quelle phrase de la fiche explique le cas de la mine ?", I_GRAPHITE, [I_METAL, I_COND, I_TEST], pos=2)),
        "second": ordre(
            "Maëlle rédige le protocole pour tester un objet inconnu. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche qui dit comment conclure.",
            ["Monter un circuit avec une pile, une lampe et des fils, en laissant un trou dans la boucle.", "Vérifier que la lampe brille quand on relie les deux pinces entre elles.",
             "Placer l'objet entre les deux pinces, dans la boucle.", "Observer la lampe.", "Conclure : conducteur si la lampe brille, isolant sinon."],
            ["On prépare le testeur avant de tester l'objet.", "On vérifie que le testeur fonctionne.", "Pour la justification : cherche « testeur »."],
            J("Quelle phrase de la fiche dit comment conclure ?", I_TEST, [I_COND, I_ISOL, I_MEME], pos=0)),
    }
    d["e2-2"] = {
        "mousse": intrus(
            "Dans la boîte des objets en métal, un objet s'est glissé par erreur. Trouve l'intrus.",
            [("une fourchette en métal", False), ("un clou", False), ("une cuillère en bois", True), ("une clé", False)],
            ["Ouvre la fiche " + FICHE + ".", "Cherche l'objet qui n'est pas en métal.", "Le bois est isolant."]),
        "lieutenant": qcm(
            "Maëlle montre deux cuillères, l'une en métal, l'autre en bois. Réponds, puis choisis la phrase de la fiche qui résume cette idée.",
            [("Quelle cuillère fait briller la lampe du testeur ?", ["la cuillère en bois", "la cuillère en métal", "les deux", "aucune"], 1, "Le métal conduit."),
             ("Ce qui compte pour savoir si un objet conduit, c'est…", ["sa forme", "sa couleur", "le matériau dont il est fait", "son poids"], 2, "Un même objet peut être conducteur ou isolant."),
             ("Pourquoi les manches des casseroles sont-ils souvent en bois ou en plastique ?", ["pour la décoration", "parce que ces matériaux sont isolants, aussi pour la chaleur", "parce qu'ils sont plus lourds", "pour conduire le courant"], 1, "Les isolants protègent la main.")],
            ["Le métal laisse passer le courant.", "La forme ne change rien.", "Pour la justification : cherche « même objet »."],
            J("Quelle phrase de la fiche résume cette idée ?", I_MEME, [I_METAL, I_PROTEGE, I_ISOL], pos=3)),
        "second": tri(
            "Maëlle veut un classement plus précis. Range chaque matériau : conducteur métallique, conducteur non métallique ou isolant. Puis choisis la phrase de la fiche qui cite des métaux conducteurs.",
            [("metal", "Conducteur métallique"), ("autre", "Conducteur non métallique"), ("isol", "Isolant")],
            [("le cuivre", "metal"), ("l'aluminium", "metal"), ("le fer", "metal"), ("le graphite de la mine", "autre"), ("l'eau du robinet", "autre"),
             ("le verre", "isol"), ("le caoutchouc", "isol"), ("l'air sec", "isol")],
            ["Le graphite n'est pas un métal.", "L'eau du robinet conduit le courant du secteur.", "Pour la justification : cherche « cuivre, le fer »."],
            J("Quelle phrase de la fiche cite des métaux conducteurs ?", I_METAL, [I_GRAPHITE, I_COND, I_EAU], pos=1)),
    }
    d["e2-3"] = {
        "mousse": assoc(
            "Relie chaque partie du fil électrique à ce qu'elle fait.",
            [("le cœur en cuivre", "laisse passer le courant"), ("la gaine en plastique", "arrête le courant et protège"), ("le testeur", "dit si un objet conduit")],
            ["Ouvre la fiche " + FICHE + ".", "Le cuivre est un métal.", "Le plastique est isolant."]),
        "lieutenant": assoc(
            "Maëlle coupe un fil électrique en deux pour le montrer. Relie chaque élément à son rôle, puis choisis la phrase de la fiche qui décrit un fil.",
            [("le cœur en cuivre", "conduit le courant"), ("la gaine en plastique", "isole le fil"), ("la poignée d'un tournevis d'électricien", "protège la main"),
             ("l'air entre les lames d'un interrupteur ouvert", "coupe la boucle"), ("le corps humain", "conduit le courant")],
            ["Le cuivre est au centre du fil.", "L'air sec est isolant.", "Pour la justification : cherche « cœur en cuivre »."],
            J("Quelle phrase de la fiche décrit un fil électrique ?", I_FIL, [I_PROTEGE, I_METAL, I_AIR], pos=0)),
        "second": qcm(
            "Maëlle range les gants isolants des électriciens. Réponds aux questions, puis choisis la phrase de la fiche qui explique le danger du secteur.",
            [("Pourquoi les électriciens portent-ils des gants en caoutchouc ?", ["pour avoir chaud", "parce que le caoutchouc est isolant", "parce que le caoutchouc est conducteur", "pour mieux tenir les fils"], 1, "Il arrête le courant."),
             ("Pourquoi le courant du secteur est-il dangereux pour nous ?", ["parce que notre corps conduit le courant", "parce que notre corps est isolant", "parce que les fils sont longs", "parce qu'il est invisible"], 0, "Le corps humain conduit le courant."),
             ("Pourquoi ne faut-il pas toucher un appareil branché avec les mains mouillées ?", ["l'eau abîme l'appareil", "l'eau du robinet conduit le courant", "l'eau est isolante", "l'eau éteint l'appareil"], 1, "L'eau du robinet conduit.")],
            ["Le caoutchouc est isolant.", "Le courant peut traverser le corps.", "Pour la justification : cherche « corps humain »."],
            J("Quelle phrase de la fiche explique le danger du secteur ?", I_CORPS, [I_EAU, I_PROTEGE, I_ISOL], pos=2)),
    }
    d["e2-4"] = {
        "lieutenant": vf(
            "Maëlle vérifie ce que tu as retenu. Vrai ou faux ? Puis choisis la phrase de la fiche qui explique l'interrupteur ouvert.",
            [("Quand l'interrupteur est ouvert, c'est l'air qui coupe la boucle.", True, "L'air sec est isolant."),
             ("Tous les conducteurs sont des métaux.", False, "Le graphite de la mine de crayon conduit aussi."),
             ("La gaine du fil est en cuivre.", False, "Elle est en plastique ; le cœur est en cuivre."),
             ("Le verre est un isolant.", True, "Il ne laisse pas passer le courant.")],
            ["Entre les lames d'un interrupteur ouvert, il y a de l'air.", "Pense à la mine du crayon.", "Pour la justification : cherche « couche d'air »."],
            J("Quelle phrase de la fiche explique l'interrupteur ouvert ?", I_AIR, [I_ISOL, I_FIL, I_TEST], pos=1)),
        "second": assoc(
            "Maëlle fait l'inventaire des objets de sécurité de l'électricien. Relie chaque objet à sa raison d'être, puis choisis la phrase de la fiche qui parle de protection.",
            [("la poignée en plastique du tournevis", "isoler la main de l'électricien"), ("le boîtier en plastique d'une prise", "empêcher de toucher le métal"),
             ("les gants en caoutchouc", "arrêter le courant"), ("la gaine du fil", "empêcher le courant de sortir du fil"), ("le cœur en cuivre", "conduire le courant")],
            ["Tout ce qui protège est isolant.", "Le seul conducteur de la liste est le cuivre.", "Pour la justification : cherche « protéger les personnes »."],
            J("Quelle phrase de la fiche parle de protection ?", I_PROTEGE, [I_FIL, I_ISOL, I_CORPS], pos=3)),
    }
    return d
