"""Lettre 2 « L'abri de la tranchée » (1916) : grades mousse, lieutenant, second (fiche : Le front et les tranchées)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "grande-guerre", "tests", "donnees"))
from fiches import *
from schemas import tranchee

FICHE = "« Le front et les tranchées »"
CASES5 = ["les sacs de sable", "les barbelés", "l'abri", "la banquette de tir", "le no man's land"]


def _cases(n):
    return [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(CASES5[:n])]


def donnees(svg, bloc=None):
    d = {}
    d["e2-1"] = {
        "mousse": {"type": "plan", "titre": "Le croquis de Louis", "colonnes": 3, "cases": _cases(3), "etiquettes": CASES5[:3],
                   "consigne": "Place chaque mot sur son repère." + tranchee(3),
                   "indices": ["Ouvre la fiche " + FICHE + ".", "Les sacs de sable sont en haut.", "L'abri est sous la terre."]},
        "lieutenant": {"type": "plan", "titre": "Le croquis de Louis", "colonnes": 2, "cases": _cases(5),
                       "etiquettes": CASES5 + ["le boyau", "la cheminée"],
                       "consigne": "Place chaque mot sur son repère (deux sont en trop), puis choisis la phrase de la fiche qui décrit une tranchée." + tranchee(5),
                       "indices": ["La banquette de tir est une marche.", "Le no man's land est entre les deux lignes.", "Pour la justification : cherche « fossé »."],
                       "justification": J("Quelle phrase de la fiche décrit une tranchée ?", F_TRANCHEE, [F_FRONT, F_ABRI, F_VIE], pos=1)},
        "second": {"type": "plan", "titre": "Le croquis de Louis", "colonnes": 2, "cases": _cases(5),
                   "etiquettes": CASES5 + ["le boyau", "la mairie", "l'usine"],
                   "consigne": "Place chaque mot sur son repère (trois sont en trop), puis choisis la phrase de la fiche qui nomme l'espace entre les tranchées ennemies." + tranchee(5),
                   "indices": ["Le boyau relie la tranchée à l'arrière : il n'est pas sur une coupe.", "La mairie et l'usine sont à l'arrière.", "Pour la justification : cherche « terre de personne »."],
                   "justification": J("Quelle phrase de la fiche nomme l'espace entre les tranchées ennemies ?", F_ABRI, [F_TRANCHEE, F_FRONT, F_VERDUN], pos=2)},
    }
    d["e2-2"] = {
        "mousse": vf(
            "Louis raconte sa vie. Pour chaque phrase, choisis vrai ou faux.",
            [("Dans la tranchée, il y a souvent de la boue.", True, "La pluie remplit la tranchée."),
             ("Louis reçoit des lettres de Jeanne.", True, "Les lettres l'aident à tenir."),
             ("Louis dort dans un grand lit à l'hôtel.", False, "Il dort dans un abri sous la terre.")],
            ["Ouvre la fiche " + FICHE + ".", "Pense à la pluie.", "L'abri est creusé sous terre."]),
        "lieutenant": vf(
            "Une partie de la lettre de Louis a été barrée. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui explique pourquoi.",
            [("Le courrier des soldats est lu par la censure.", True, "Les autorités le surveillent."),
             ("Louis peut écrire le nom exact du lieu où il se trouve.", False, "C'est interdit par la censure."),
             ("Les colis de la famille aident les soldats à tenir.", True, "Avec les lettres et la camaraderie."),
             ("Les rats et les poux font partie de la vie des tranchées.", True, "Les conditions sont très dures."),
             ("« Poilu » est le nom d'une arme.", False, "C'est le surnom des soldats français.")],
            ["Qui lit les lettres avant Jeanne ?", "Les colis viennent de l'arrière.", "Pour la justification : cherche « surveillé »."],
            J("Quelle phrase de la fiche explique pourquoi une partie de la lettre est barrée ?", F_CENSURE, [F_LETTRES, F_VIE, F_POILU], pos=0)),
        "second": assoc(
            "Louis a dessiné des objets de son abri. Relie chaque objet à ce qu'il dit de la guerre, puis choisis la phrase de la fiche sur ce qui aide les soldats à tenir.",
            [("le masque dans sa boîte", "les gaz de combat employés à partir de 1915"), ("le colis de Jeanne", "le lien avec la famille à l'arrière"),
             ("la lettre aux lignes barrées", "la censure du courrier"), ("la bougie dans une boîte de conserve", "la vie sous terre, dans les abris"),
             ("les bottes couvertes de boue", "la pluie et le froid des tranchées")],
            ["Le masque protège des gaz.", "La censure barre des lignes.", "Pour la justification : cherche « camaraderie »."],
            J("Quelle phrase de la fiche dit ce qui aide les soldats à tenir ?", F_LETTRES, [F_VIE, F_CENSURE, F_GAZ], pos=3)),
    }
    d["e2-3"] = {
        "mousse": tri(
            "Range chaque carte sous la bonne bataille de 1916.",
            [("verdun", "Verdun"), ("somme", "La Somme")],
            [("commence en février", "verdun"), ("l'armée française résiste", "verdun"), ("commence en juillet", "somme"), ("Britanniques et Français ensemble", "somme")],
            ["Ouvre la fiche " + FICHE + ".", "Février vient avant juillet.", "À la Somme, les Britanniques sont là."]),
        "lieutenant": tri(
            "Range chaque note de Louis sous la bonne bataille, puis choisis la phrase de la fiche sur Verdun.",
            [("verdun", "Verdun"), ("somme", "La Somme"), ("deux", "Les deux")],
            [("commence le 21 février 1916", "verdun"), ("se termine le 18 décembre 1916", "verdun"), ("commence le 1er juillet 1916", "somme"),
             ("se termine le 18 novembre 1916", "somme"), ("premiers chars britanniques", "somme"), ("a lieu en 1916", "deux")],
            ["Verdun dure jusqu'en décembre.", "Les deux batailles ont lieu la même année.", "Pour la justification : cherche « résiste »."],
            J("Quelle phrase de la fiche donne les dates de Verdun ?", F_VERDUN, [F_SOMME, F_CHARS, F_FRONT], pos=0)),
        "second": ordre(
            "Remets dans l'ordre ces étapes de la guerre sur le front, de 1914 à fin 1916, puis choisis la phrase de la fiche sur l'apparition des chars.",
            [("les armées s'enterrent dans les tranchées", "fin 1914"), ("premiers gaz de combat", "1915"), ("début de la bataille de Verdun", "21 février 1916"),
             ("début de la bataille de la Somme", "1er juillet 1916"), ("fin de la bataille de Verdun", "18 décembre 1916")],
            ["Les tranchées apparaissent dès 1914.", "Verdun commence avant la Somme et finit après elle.", "Pour la justification : cherche « chars »."],
            J("Quelle phrase de la fiche situe l'apparition des chars ?", F_CHARS, [F_GAZ, F_ARMES, F_SOMME], pos=0)),
    }
    d["e2-4"] = {
        "lieutenant": qcm(
            "Louis parle de ses camarades et des armes nouvelles. Réponds, puis choisis la phrase de la fiche sur les soldats venus des colonies.",
            [("Amadou, le camarade de Louis, vient du Sénégal. D'où viennent aussi des soldats de l'armée française ?", ["d'Afrique du Nord, d'Afrique de l'Ouest, de Madagascar, d'Indochine", "seulement de Paris", "d'Allemagne", "du Japon"], 0, "Des colonies de la France."),
             ("Combien sont-ils environ ?", ["6 000", "60 000", "600 000", "6 millions"], 2, "Environ 600 000."),
             ("Quelle arme apparaît pour la première fois en 1916 ?", ["le char d'assaut", "la mitrailleuse", "le canon", "le fusil"], 0, "Les premiers chars, britanniques."),
             ("À quoi sert le masque ?", ["à se protéger des gaz", "à avoir chaud", "à se déguiser", "à voir la nuit"], 0, "Les gaz sont employés à partir de 1915.")],
            ["Pense à l'empire colonial de la France.", "600 000 soldats.", "Pour la justification : cherche « colonies »."],
            J("Quelle phrase de la fiche parle des soldats venus des colonies ?", F_COLONIES, [F_POILU, F_ARMES, F_LETTRES], pos=2)),
        "second": qcm(
            "Louis réfléchit à ce que la guerre a de nouveau. Réponds, puis choisis la phrase de la fiche qui énumère les armes.",
            [("Pourquoi les armées s'enterrent-elles à la fin de 1914 ?", ["pour se protéger des armes très puissantes, comme les mitrailleuses et les canons", "pour planter des légumes", "parce qu'il fait trop chaud", "pour cacher les lettres"], 0, "Les armes rendent les attaques à découvert très dangereuses."),
             ("Combien de temps dure la bataille de Verdun ?", ["environ 10 jours", "environ 10 mois", "environ 10 ans", "1 jour"], 1, "Du 21 février au 18 décembre 1916."),
             ("Environ combien de soldats venus des colonies combattent dans l'armée française ?", ["60 000", "600 000", "6 millions", "1,4 million"], 1, "D'Afrique, de Madagascar, d'Indochine."),
             ("Quelle arme n'est PAS une arme nouvelle ou nouvellement très utilisée en 1914-1918 ?", ["la mitrailleuse", "l'avion", "le char", "l'arbalète"], 3, "L'arbalète date du Moyen Âge.")],
            ["Une mitrailleuse tire très vite.", "Février à décembre : compte les mois.", "Pour la justification : cherche « mitrailleuses »."],
            J("Quelle phrase de la fiche énumère les armes de la guerre ?", F_ARMES, [F_GAZ, F_CHARS, F_FRONT], pos=1)),
    }
    return d
