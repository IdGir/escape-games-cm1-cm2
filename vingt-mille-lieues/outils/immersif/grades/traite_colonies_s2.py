"""Salle 2 « Le cabinet des registres » : grades mousse, lieutenant, second (fiche : la traite atlantique).
Ton digne : on mesure l'ampleur d'un crime ; aucun calcul ne porte sur les morts ou les enfants."""
from aide import *

FICHE = "« La traite atlantique »"
P_DEF = "La traite négrière est le commerce de captifs achetés en Afrique et vendus comme esclaves en Amérique."
P_DUREE = "La traite atlantique a duré du XVIe au XIXe siècle."
P_NB = "Plus de 12,5 millions de personnes ont été déportées d'Afrique vers les Amériques."
P_FORCE = "Les captifs ne partaient pas de leur plein gré : ils étaient achetés sur les côtes d'Afrique, comme le Sénégal, le golfe du Bénin ou la côte de Loango, puis transportés de force."
P_FR = "Les navires français ont transporté environ 11 % des captifs de la traite atlantique, soit plus de 1,3 million de personnes."
P_NANTES = "Nantes, premier port négrier français, a armé 44 % des expéditions françaises ; d'autres partaient du Havre, de La Rochelle, de Saint-Malo, d'Honfleur ou de Bordeaux."
P_320 = "En moyenne, un navire français transportait environ 320 captifs."
P_DIRECT = "Les captifs ne passaient pas par la France : ils étaient conduits directement d'Afrique aux Amériques."
P_ARCH = "Les historiens reconstituent cette histoire grâce aux registres des navires, aux journaux de bord et aux archives des ports."
P_SV = "La base de données Slave Voyages rassemble les informations connues sur des dizaines de milliers de voyages."
P_REV = "Des révoltes éclatent parfois à bord, et l'équipage les réprime avec violence."


def donnees(svg, bloc=None):
    d = {}
    d["e2-1"] = {
        "mousse": vf(
            "Malik a écrit trois phrases sur ses fiches. Pour chaque phrase, choisis vrai ou faux.",
            [("Les captifs étaient emmenés de force.", True, "Ils ne partaient pas de leur plein gré."),
             ("Des navires partaient de Nantes.", True, "Nantes était un port de la traite."),
             ("La traversée durait deux jours.", False, "Elle durait environ deux mois.")],
            ["Ouvre la fiche " + FICHE + ".", "Les captifs n'avaient pas choisi de partir.", "Traverser l'océan à la voile prend longtemps."]),
        "lieutenant": vf(
            "Malik relit les fiches d'un enquêteur. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui corrige l'erreur sur le trajet des captifs.",
            [("La traite atlantique a duré plus de trois siècles.", True, "Du XVIe au XIXe siècle."),
             ("Les captifs débarquaient à Nantes avant d'aller aux Antilles.", False, "Ils allaient directement d'Afrique aux Amériques."),
             ("Les navires français ont transporté environ un captif sur dix.", True, "Environ 11 %."),
             ("Nantes a armé moins d'une expédition française sur dix.", False, "Nantes en a armé 44 %."),
             ("Plus de 12,5 millions de personnes ont été déportées.", True, "C'est l'estimation des historiens.")],
            ["Du XVIe au XIXe siècle : compte les siècles.", "44 %, c'est presque la moitié.", "Pour la justification : cherche « directement »."],
            J("Quelle phrase de la fiche corrige l'erreur sur le trajet des captifs ?", P_DIRECT, [P_FORCE, P_320, P_DEF], pos=1)),
        "second": vf(
            "Malik soumet des affirmations à l'archiviste en chef. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui montre que les captifs résistaient déjà à bord.",
            [("Plus de 1,3 million de personnes ont été transportées par des navires français.", True, "Environ 11 % de la traite atlantique."),
             ("Si la France a transporté environ 11 % des captifs, les autres pays en ont transporté environ 89 %.", True, "100 − 11 = 89."),
             ("Nantes a armé la majorité des expéditions françaises.", False, "44 %, c'est moins de la moitié : la majorité vient des autres ports."),
             ("Les captifs ne se révoltaient jamais.", False, "Des révoltes éclataient parfois à bord."),
             ("Un navire français transportait en moyenne quelques milliers de captifs.", False, "Environ 320 en moyenne.")],
            ["La majorité, c'est plus de la moitié.", "100 % moins la part de la France donne la part des autres pays.", "Pour la justification : cherche le mot « révoltes »."],
            J("Quelle phrase de la fiche montre que les captifs résistaient déjà à bord ?", P_REV, [P_FORCE, P_ARCH, P_DIRECT], pos=3)),
    }
    d["e2-2"] = {
        "mousse": tri(
            "Range chaque lieu sur son continent.",
            [("europe", "Europe"), ("afrique", "Afrique"), ("amerique", "Amériques")],
            [("Nantes", "europe"), ("le Sénégal", "afrique"), ("la Martinique", "amerique"), ("La Rochelle", "europe")],
            ["Ouvre la fiche " + FICHE + ".", "Nantes et La Rochelle sont des ports français.", "La Martinique est une île des Antilles."]),
        "lieutenant": tri(
            "Les fiches de lieux du registre sont mélangées. Range chaque lieu sur son continent, puis choisis la phrase de la fiche qui nomme des côtes d'Afrique.",
            [("europe", "Europe"), ("afrique", "Afrique"), ("amerique", "Amériques")],
            [("Le Havre", "europe"), ("Saint-Malo", "europe"), ("Honfleur", "europe"), ("le golfe du Bénin", "afrique"), ("la côte de Loango", "afrique"), ("le Sénégal", "afrique"),
             ("Saint-Domingue", "amerique"), ("la Guadeloupe", "amerique"), ("la Guyane", "amerique")],
            ["Saint-Malo et Honfleur sont des ports de la Manche.", "La Guyane est en Amérique du Sud.", "Pour la justification : cherche « Loango »."],
            J("Quelle phrase de la fiche nomme des côtes d'Afrique ?", P_FORCE, [P_NANTES, P_DEF, P_NB], pos=0)),
        "second": tri(
            "Malik classe des sources. Range chaque source : nous apprend-elle surtout sur les navires et leurs voyages, ou sur l'ampleur totale de la traite ? Puis choisis la phrase de la fiche qui dit comment les historiens travaillent.",
            [("voyage", "Un voyage, un navire"), ("ampleur", "L'ampleur totale de la traite")],
            [("le journal de bord d'un capitaine", "voyage"), ("le registre d'un navire au départ du port", "voyage"), ("la liste de la cargaison d'un navire", "voyage"),
             ("une base de données de dizaines de milliers de voyages", "ampleur"), ("l'estimation de 12,5 millions de personnes déportées", "ampleur"), ("la part de la France : environ 11 %", "ampleur")],
            ["Un document de bord raconte un seul voyage.", "Pour une estimation totale, il faut rassembler beaucoup de voyages.", "Pour la justification : cherche « journaux de bord »."],
            J("Quelle phrase de la fiche dit comment les historiens travaillent ?", P_ARCH, [P_SV, P_NB, P_DUREE], pos=2)),
    }
    d["e2-3"] = {
        "mousse": trous(
            "Une page du registre est déchirée. Remets les mots à leur place. Un mot est en trop.",
            "La traite est le commerce de [[captifs]] achetés en [[Afrique]] et vendus comme esclaves en Amérique.",
            ["captifs", "Afrique", "Asie"],
            ["Ouvre la fiche " + FICHE + ".", "Les captifs sont achetés sur la côte d'un continent.", "L'Asie n'est pas sur la carte du commerce triangulaire."]),
        "lieutenant": trous(
            "Une page du registre est déchirée. Remets les mots à leur place (trois étiquettes sont en trop), puis choisis la phrase de la fiche qui donne la durée de la traite.",
            "La traite atlantique a duré du [[XVIe]] au [[XIXe]] siècle. Plus de 12,5 [[millions]] de personnes ont été déportées. Les navires français ont transporté environ [[11]] % des captifs. Nantes a armé [[44]] % des expéditions françaises.",
            ["XVIe", "XIXe", "millions", "11", "44", "XIIe", "milliers", "90"],
            ["Trois siècles au moins.", "Un peu plus d'un captif sur dix pour la France.", "Pour la justification : cherche « a duré »."],
            J("Quelle phrase de la fiche donne la durée de la traite ?", P_DUREE, [P_NB, P_FR, P_SV], pos=1)),
        "second": qcm(
            tableau("Fiche de Malik (d'après la BnF et Slave Voyages)", ["Mesure", "Résultat"],
                    [["personnes déportées par la traite atlantique", "plus de 12,5 millions"], ["captifs transportés par des navires français", "plus de 1,3 million"],
                     ["expéditions françaises parties de Nantes", "44 %"], ["captifs par navire français, en moyenne", "environ 320"]])
            + "Réponds aux trois questions, puis choisis la phrase de la fiche qui relie les deux premières lignes.",
            [("1,3 million sur 12,5 millions, c'est environ...", ["un dixième", "la moitié", "un centième", "les trois quarts"], 0, "Environ 11 %."),
             ("Sur 100 expéditions françaises, combien ne partent pas de Nantes ?", ["44", "56", "4", "100"], 1, "100 − 44 = 56."),
             ("Pourquoi écrit-on « environ » ou « plus de » ?", ["parce que les chiffres sont inventés", "parce que ce sont des estimations d'historiens", "parce qu'on ne sait rien", "pour faire joli"], 1, "Les historiens reconstituent à partir des archives.")],
            ["12,5 divisé par 10, c'est 1,25.", "Fais une soustraction.", "Pour la justification : cherche « 11 % »."],
            J("Quelle phrase de la fiche relie les deux premières lignes ?", P_FR, [P_NANTES, P_320, P_NB], pos=2)),
    }
    d["e2-4"] = {
        "lieutenant": code(
            "Le tiroir du registre ne s'ouvre qu'avec trois nombres de la fiche. Écris-les, puis choisis la phrase de la fiche qui donne le deuxième nombre.",
            [("Captifs transportés par la France (sur 100)", "11", 2), ("Expéditions françaises parties de Nantes (sur 100)", "44", 2),
             ("Captifs moyens par navire français", "320", 3)],
            ["« Sur 100 », c'est le pourcentage.", "Nantes : un peu moins de la moitié.", "Pour la justification : cherche « premier port négrier »."],
            J("Quelle phrase de la fiche donne le deuxième nombre ?", P_NANTES, [P_FR, P_320, P_DIRECT], pos=1)),
        "second": vf(
            "L'archiviste en chef rappelle comment lire des chiffres d'histoire. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui explique d'où viennent ces chiffres.",
            [("Les chiffres de la traite sont des estimations construites à partir des archives.", True, "Registres, journaux de bord, archives des ports."),
             ("Derrière chaque chiffre, il y a des personnes.", True, "C'est pour elles que l'on compte avec soin."),
             ("Un seul journal de bord suffit pour connaître toute la traite.", False, "Il faut rassembler des dizaines de milliers de voyages."),
             ("Si Nantes a armé 44 % des expéditions françaises, son histoire est celle de tous les ports.", False, "Chaque port a son histoire.")],
            ["Un document raconte un voyage ; une base en rassemble beaucoup.", "On ne généralise pas un port à toute la France.", "Pour la justification : cherche « Slave Voyages »."],
            J("Quelle phrase de la fiche explique d'où viennent ces chiffres ?", P_SV, [P_NB, P_FR, P_DEF], pos=0)),
    }
    return d
