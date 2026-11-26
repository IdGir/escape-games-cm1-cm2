"""Séance 1 « Le grand départ » : grades mousse, lieutenant, second (fiche : La commune, le premier territoire)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "mission-geo", "tests", "donnees"))
from fiches import *

FICHE = "« La commune, le premier territoire »"


def donnees(svg, bloc=None):
    d = {}
    d["e1-1"] = {
        "mousse": assoc(
            "Relie chaque démarche au bon lieu de la commune.",
            [("Acheter du pain", "la boulangerie"), ("Se faire soigner", "le cabinet médical"), ("Apprendre à lire", "l'école")],
            ["Ouvre la fiche " + FICHE + ".", "Le pain se vend à la boulangerie.", "On apprend à l'école."]),
        "lieutenant": tri(
            "Le Professeur Atlas trie les lieux de la commune : service public, ou commerce ? Range chaque lieu, puis choisis la phrase de la fiche qui définit un service public.",
            [("pub", "Service public (ouvert à tous, sans rien acheter)"), ("com", "Commerce (on y achète quelque chose)")],
            [("la mairie", "pub"), ("l'école publique", "pub"), ("la bibliothèque municipale", "pub"), ("la boulangerie", "com"), ("la pharmacie", "com"), ("le supermarché", "com")],
            ["Dans un commerce, on paie ce que l'on emporte.", "La bibliothèque municipale prête des livres.", "Pour la justification : cherche « tous les habitants »."],
            J("Quelle phrase de la fiche définit un service public ?", C_SERVICE, [C_FONCTION, C_MAIRIE, C_ROLE], pos=1)),
        "second": assoc(
            "Le Professeur Atlas a ajouté des démarches inattendues. Relie chacune au lieu où elle se fait, puis choisis la phrase de la fiche qui explique le rôle de la mairie.",
            [("Demander une carte d'identité", "la mairie"), ("Faire un certificat médical", "le cabinet médical"), ("Emprunter un guide de voyage", "la bibliothèque"),
             ("Acheter une trousse de secours", "la pharmacie"), ("S'entraîner à la course à pied", "le parc"), ("Récupérer ses cahiers", "l'école")],
            ["Le certificat médical est signé par un médecin.", "La trousse de secours s'achète.", "Pour la justification : cherche « papiers officiels »."],
            J("Quelle phrase de la fiche explique ce que l'on fait à la mairie ?", C_MAIRIE, [C_SERVICE, C_PLAN, C_FONCTION], pos=2)),
    }
    d["e1-2"] = {
        "mousse": tri(
            "Range chaque lieu : pour se soigner, pour apprendre, ou pour acheter ?",
            [("san", "Se soigner"), ("edu", "Apprendre"), ("com", "Acheter")],
            [("la pharmacie", "san"), ("l'école", "edu"), ("la boulangerie", "com")],
            ["Ouvre la fiche " + FICHE + ".", "On achète des médicaments à la pharmacie pour se soigner.", "On apprend à l'école."]),
        "lieutenant": assoc(
            "Relie chaque fonction à deux lieux qui l'exercent, puis choisis la phrase de la fiche qui nomme les fonctions des lieux.",
            [("fonction administrative", "la mairie et la poste"), ("fonction éducative", "l'école et la bibliothèque"), ("fonction commerciale", "la boulangerie et le supermarché"),
             ("fonction de santé", "le cabinet médical et la pharmacie"), ("fonction de loisirs", "le parc et le stade")],
            ["La poste rend un service officiel.", "Le stade sert à faire du sport.", "Pour la justification : cherche « chaque lieu a une fonction »."],
            J("Quelle phrase de la fiche nomme les fonctions des lieux ?", C_FONCTION, [C_SERVICE, C_ROLE, C_COMMUNE], pos=0)),
        "second": tri(
            "Range chaque lieu selon sa fonction principale. Attention aux pièges, puis choisis la phrase de la fiche sur les fonctions des lieux.",
            [("adm", "Administrative"), ("edu", "Éducative"), ("com", "Commerciale"), ("san", "Santé"), ("loi", "Loisirs")],
            [("la mairie", "adm"), ("la poste", "adm"), ("le collège", "edu"), ("la médiathèque", "edu"), ("le marché couvert", "com"), ("la pharmacie", "san"),
             ("l'hôpital", "san"), ("la salle des fêtes", "loi"), ("la piscine", "loi")],
            ["La médiathèque prête des livres et des films : on y apprend.", "La pharmacie vend, mais sa fonction principale est la santé.", "Pour la justification : cherche « de santé ou de loisirs »."],
            J("Quelle phrase de la fiche nomme les fonctions des lieux ?", C_FONCTION, [C_MAIRIE, C_SERVICE, C_VILLE], pos=3)),
    }
    d["e1-3"] = {
        "mousse": qcm(
            "Le Professeur Atlas te donne un indice : la ville du rendez-vous commence par D, compte 5 lettres et elle est célèbre pour sa moutarde. Laquelle est-ce ?",
            [("Quelle est la ville du rendez-vous ?", ["Dijon", "Paris", "Nice"], 0, "D-I-J-O-N : 5 lettres.")],
            ["Ouvre la fiche " + FICHE + ".", "Elle commence par D.", "La moutarde de Dijon est connue dans le monde entier."]),
        "lieutenant": qcm(
            "Avant le départ, le Professeur Atlas vérifie ce que tu sais de la commune. Réponds, puis choisis la phrase de la fiche qui dit de quoi s'occupe la commune.",
            [("Les lettres marquées D, I, J, O, N forment le nom de la ville du rendez-vous. Laquelle ?", ["Dijon", "Dinan", "Digne", "Dole"], 0, "D-I-J-O-N."),
             ("De quoi la commune s'occupe-t-elle ?", ["des écoles élémentaires et de l'eau", "des lycées", "de l'armée", "des autoroutes"], 0, "Les lycées dépendent de la région."),
             ("Une commune de 1 500 habitants est plutôt…", ["un village", "une ville", "une métropole", "une région"], 0, "Moins de 2 000 habitants.")],
            ["Les cinq lettres sont données : remets-les dans l'ordre.", "La commune s'occupe aussi des déchets.", "Pour la justification : cherche « écoles maternelles »."],
            J("Quelle phrase de la fiche dit de quoi s'occupe la commune ?", C_ROLE, [C_COMMUNE, C_SERVICE, C_FONCTION], pos=1)),
        "second": vf(
            "Le Professeur Atlas relit les notes d'une nouvelle recrue. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui dit combien il y a de communes.",
            [("Paris et le plus petit village sont tous les deux des communes.", True, "La taille ne change rien : chacun a un maire."),
             ("La France compte environ 100 communes.", False, "Elle en compte 34 875 au 1er janvier 2026."),
             ("Le maire est directement nommé par le président de la République.", False, "Il est élu par le conseil municipal."),
             ("La commune s'occupe de l'eau et des déchets.", True, "Ce sont deux de ses compétences."),
             ("Un plan représente un espace vu du dessus.", True, "Comme le plan de la commune au mur du bureau.")],
            ["Chaque commune a son maire, petite ou grande.", "Le nombre de communes dépasse 30 000.", "Pour la justification : cherche « 34 875 »."],
            J("Quelle phrase de la fiche dit combien il y a de communes en France ?", C_COMMUNE, [C_MAIRE, C_VILLE, C_PLAN], pos=0)),
    }
    d["e1-4"] = {
        "lieutenant": ordre(
            "Comment le maire est-il choisi ? Range les étapes dans l'ordre, puis choisis la phrase de la fiche qui l'explique.",
            ["Les habitants votent aux élections municipales", "Ils élisent le conseil municipal", "Le conseil municipal élit le maire", "Le maire dirige la commune"],
            ["Tout commence par le vote des habitants.", "Le conseil municipal est élu avant le maire.", "Pour la justification : cherche « élu par le conseil municipal »."],
            J("Quelle phrase de la fiche explique comment le maire est choisi ?", C_MAIRE, [C_COMMUNE, C_ROLE, C_SERVICE], pos=2)),
        "second": ordre(
            "Range ces communes imaginaires de la moins peuplée à la plus peuplée, puis choisis la phrase de la fiche qui distingue village et ville.",
            [("Le hameau des Prés", "120 habitants"), ("Le village de Bois-Joli", "1 850 habitants"), ("La ville de Pont-Neuf", "2 300 habitants"),
             ("La ville de Saint-Clair", "48 000 habitants")],
            ["Compare d'abord le nombre de chiffres.", "1 850 est moins que 2 000 ; 2 300 est plus.", "Pour la justification : cherche « 2 000 habitants »."],
            J("Quelle phrase de la fiche distingue un village d'une ville ?", C_VILLE, [C_COMMUNE, C_PLAN, C_MAIRE], pos=3)),
    }
    return d
