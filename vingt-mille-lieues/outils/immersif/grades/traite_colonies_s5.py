"""Salle 5 « La salle de lecture » : grades mousse, lieutenant, second (fiche : résistances et abolitions)."""
from aide import *

FICHE = "« Résistances et abolitions »"
P_1791 = "En août 1791, une insurrection d'esclaves éclate dans la plaine du nord de Saint-Domingue."
P_TL = "Toussaint Louverture, né esclave vers 1740, devient l'un de ses chefs, puis gouverneur de la colonie en 1798."
P_HAITI = "Le 1er janvier 1804, Saint-Domingue devient Haïti, un pays indépendant fondé par d'anciens esclaves."
P_1794 = "Le 4 février 1794, la Convention abolit l'esclavage dans les colonies françaises."
P_1802 = "Le 20 mai 1802, Napoléon Bonaparte, Premier consul, rétablit l'esclavage et la traite."
P_1848 = "Le décret du 27 avril 1848 abolit définitivement l'esclavage dans toutes les colonies françaises."
P_SCH = "Victor Schœlcher a présidé la commission qui l'a préparé."
P_EFFET = "L'abolition prend effet dans chaque colonie deux mois après la promulgation du décret dans cette colonie."
P_2001 = "La loi du 21 mai 2001 reconnaît la traite et l'esclavage comme un crime contre l'humanité."
P_2006 = "Depuis 2006, le 10 mai est la journée nationale des mémoires de la traite, de l'esclavage et de leurs abolitions."
P_PESE = "Les révoltes des esclaves, comme celle de Saint-Domingue, ont pesé sur les décisions prises à Paris."


def donnees(svg, bloc=None):
    d = {}
    d["e5-1"] = {
        "mousse": ordre(
            "Théo range sa frise. Remets les trois cartes dans l'ordre, de la plus ancienne à la plus récente. La date est sous chaque carte.",
            [("Première abolition de l'esclavage.", "1794"), ("Napoléon Bonaparte rétablit l'esclavage.", "1802"), ("Abolition définitive de l'esclavage.", "1848")],
            ["Ouvre la fiche " + FICHE + " : regarde la frise.", "La plus petite date est la plus ancienne.", "1794, puis 1802, puis 1848."]),
        "lieutenant": ordre(
            "Théo a perdu les dates de sa frise. Remets les sept événements dans l'ordre, puis choisis la phrase de la fiche qui explique pourquoi la révolte de Saint-Domingue est importante.",
            ["Le Code noir fixe les règles de l'esclavage.", "Les esclaves de Saint-Domingue se révoltent.", "La Convention abolit l'esclavage.",
             "Napoléon Bonaparte rétablit l'esclavage.", "Saint-Domingue devient Haïti, un pays indépendant.", "L'esclavage est aboli définitivement.",
             "Une loi reconnaît la traite et l'esclavage comme un crime contre l'humanité."],
            ["Le Code noir date de Louis XIV.", "L'indépendance d'Haïti suit le rétablissement de l'esclavage.", "Pour la justification : cherche « ont pesé »."],
            J("Quelle phrase de la fiche explique l'importance de la révolte de Saint-Domingue ?", P_PESE, [P_1791, P_HAITI, P_2006], pos=1)),
        "second": ordre(
            "L'archiviste en chef vous confie la frise complète. Remets les huit événements dans l'ordre, sans les dates, puis choisis la phrase de la fiche qui montre qu'une abolition n'est pas toujours définitive.",
            ["Signature du Code noir sous Louis XIV.", "Insurrection dans la plaine du nord de Saint-Domingue.", "Toussaint Louverture devient gouverneur de la colonie.",
             "Napoléon Bonaparte, Premier consul, rétablit l'esclavage.", "Haïti proclame son indépendance.", "Le décret d'abolition définitive est signé.",
             "Une loi reconnaît la traite et l'esclavage comme un crime contre l'humanité.", "Première journée nationale du 10 mai."],
            ["Toussaint Louverture devient gouverneur en 1798, avant le rétablissement.", "La loi de 2001 précède la journée de 2006.", "Pour la justification : cherche « rétablit »."],
            J("Quelle phrase de la fiche montre qu'une abolition n'est pas toujours définitive ?", P_1802, [P_1794, P_1848, P_EFFET], pos=0)),
    }
    d["e5-2"] = {
        "mousse": qcm(
            "Théo prépare des fiches sur des personnes réelles. Réponds aux trois questions.",
            [("Toussaint Louverture est né...", ["esclave à Saint-Domingue", "roi de France", "à Nantes"], 0, "Il devient un chef de la révolte."),
             ("Victor Schœlcher est lié à l'année...", ["1685", "1848", "1802"], 1, "L'abolition définitive."),
             ("Le 10 mai, la France...", ["fête le roi", "se souvient de la traite et de l'esclavage", "part en vacances"], 1, "Une journée de mémoire.")],
            ["Ouvre la fiche " + FICHE + ".", "Schœlcher a travaillé pour l'abolition définitive.", "Le 10 mai est une journée de mémoire."]),
        "lieutenant": qcm(
            "Théo vérifie ses fiches. Réponds aux quatre questions, puis choisis la phrase de la fiche qui parle du rôle de Victor Schœlcher.",
            [("Qui rétablit l'esclavage en 1802 ?", ["Louis XIV", "Napoléon Bonaparte", "Victor Schœlcher", "Toussaint Louverture"], 1, "Le 20 mai 1802."),
             ("Que devient Saint-Domingue le 1er janvier 1804 ?", ["une colonie anglaise", "Haïti, un pays indépendant", "un département français", "une île déserte"], 1, "Fondé par d'anciens esclaves."),
             ("Que fait Victor Schœlcher ?", ["il signe le Code noir", "il préside la commission qui prépare le décret de 1848", "il gouverne Saint-Domingue", "il arme des navires"], 1, "Le décret du 27 avril 1848."),
             ("Que reconnaît la loi du 21 mai 2001 ?", ["un crime contre l'humanité", "un commerce utile", "le Code noir", "la fin des musées"], 0, "La traite et l'esclavage.")],
            ["1802 : le Premier consul.", "Haïti est le nouveau nom de Saint-Domingue.", "Pour la justification : cherche « commission »."],
            J("Quelle phrase de la fiche parle du rôle de Victor Schœlcher ?", P_SCH, [P_1848, P_TL, P_2001], pos=2)),
        "second": vf(
            "Théo a écrit des phrases pour son exposé du 10 mai. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui précise quand l'abolition de 1848 s'applique.",
            [("Toussaint Louverture a été gouverneur de Saint-Domingue.", True, "En 1798."),
             ("Haïti est un pays fondé par d'anciens esclaves.", True, "Le 1er janvier 1804."),
             ("L'abolition de 1848 s'applique le jour même dans toutes les colonies.", False, "Deux mois après la promulgation du décret dans chaque colonie."),
             ("La traite et l'esclavage ont été reconnus comme un crime contre l'humanité en 1848.", False, "Par la loi du 21 mai 2001."),
             ("Le 10 mai est une journée nationale depuis 2006.", True, "Décret de 2006.")],
            ["Un décret doit arriver et être promulgué dans chaque colonie.", "Le crime contre l'humanité est reconnu au XXIe siècle.", "Pour la justification : cherche « deux mois »."],
            J("Quelle phrase de la fiche précise quand l'abolition de 1848 s'applique ?", P_EFFET, [P_1848, P_SCH, P_1794], pos=1)),
    }
    d["e5-3"] = {
        "mousse": code(
            "Le registre est fermé par un fermoir. Il s'ouvre avec l'année de l'abolition définitive de l'esclavage.",
            [("Abolition définitive", "1848", 4)],
            ["Ouvre la fiche " + FICHE + " : regarde la frise.", "C'est au milieu du XIXe siècle.", "Victor Schœlcher, 18…"]),
        "lieutenant": code(
            "Le fermoir du registre s'ouvre avec quatre années. Écris-les, puis choisis la phrase de la fiche qui donne la première.",
            [("Première abolition", "1794", 4), ("Rétablissement", "1802", 4), ("Indépendance d'Haïti", "1804", 4), ("Abolition définitive", "1848", 4)],
            ["Le rétablissement vient huit ans après la première abolition.", "Haïti devient indépendante deux ans après le rétablissement.", "Pour la justification : cherche « la Convention »."],
            J("Quelle phrase de la fiche donne la première année ?", P_1794, [P_1802, P_HAITI, P_1848], pos=0)),
        "second": code(
            "Le fermoir du registre demande des durées calculées à partir de la fiche. Écris-les, puis choisis la phrase de la fiche qui donne l'année du rétablissement.",
            [("Années entre la première abolition et le rétablissement", "8", 1), ("Années entre le rétablissement et l'indépendance d'Haïti", "2", 1),
             ("Années entre la première abolition et l'abolition définitive", "54", 2)],
            ["1802 − 1794.", "1804 − 1802.", "Pour la justification : cherche « Premier consul »."],
            J("Quelle phrase de la fiche donne l'année du rétablissement ?", P_1802, [P_HAITI, P_1794, P_2006], pos=3)),
    }
    d["e5-4"] = {
        "lieutenant": lettres(
            "Sur la dernière page du registre, des lettres sont marquées. Range dans les cases celles qui forment le mot qui résume le devoir des enquêteurs (attention aux lettres pièges), puis choisis la phrase de la fiche qui fixe une date pour ce devoir.",
            "MEMOIRE",
            marque("Chers enquêteurs, le [r]egistre est complet. Vous avez s[u]ivi les navires, lu les chiffres, étudié les plantati[o]ns et les lois. Des m[i]llions de personnes ont été arrachées à l'Afrique. Elles ont résisté, se sont ré[v]oltées, ont conquis leur liberté. À nous d[e] le transmettre, et de ne ja[m]ais l'oubli[e]r. [M]erci."),
            ["Le mot a sept lettres.", "C'est ce que l'on garde du passé pour ne pas l'oublier.", "Pour la justification : cherche « 10 mai »."],
            J("Quelle phrase de la fiche fixe une date pour ce devoir ?", P_2006, [P_2001, P_PESE, P_HAITI], pos=0)),
        "second": lettres(
            "Sur la dernière page, Inès a marqué des lettres. Range dans les cases celles qui forment le mot qui désigne la suppression de l'esclavage par la loi (attention aux lettres pièges), puis choisis la phrase de la fiche qui décrit cette suppression en 1848.",
            "ABOLITION",
            marque("Le regis[t]re se referme. Il a raconté la tr[a]ite, le travail f[o]rcé, les révo[l]tes et la [l]iberté conquise. Il nous rappelle qu'une l[o]i peut être [i]njuste, et qu'une autre lo[i] peut la [b]riser. Gardo[n]s-en la mém[o]ire, avec [a]ttention."),
            ["Le mot a neuf lettres.", "C'est le nom tiré du verbe « abolir ».", "Pour la justification : cherche « définitivement »."],
            J("Quelle phrase de la fiche décrit cette suppression en 1848 ?", P_1848, [P_1794, P_EFFET, P_2001], pos=2)),
    }
    return d
