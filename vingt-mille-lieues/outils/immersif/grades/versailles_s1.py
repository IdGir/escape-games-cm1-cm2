"""Salle 1 « L'imprimerie de Suzanne » (fiche : reforme-guerres)."""
from aide import *

F = "« La Réforme et les guerres de Religion »"
G1 = "Le 31 octobre 1517, Martin Luther, moine allemand, publie 95 thèses contre la vente des indulgences (des remises de peine pour les péchés, accordées par l'Église contre de l'argent)."
G2 = "Pour lui, l'homme est sauvé par sa foi en Dieu, et non par ce qu'il paie ; la Bible seule doit guider le chrétien. Il refuse de se soumettre au pape."
G3 = "L'imprimerie diffuse ses écrits dans toute l'Europe."
G4 = "En 1536, le Français Jean Calvin publie un grand livre qui explique la foi réformée ; il organise une Église protestante à Genève."
G5 = "Les protestants français, surtout calvinistes, sont appelés huguenots."
G6 = "Catholiques et protestants sont tous chrétiens."
G7 = "Mais les protestants refusent l'autorité du pape, le culte des saints, la messe en latin ; ils se réunissent au temple et prient en français."
G8 = "De 1562 (massacre de Wassy) à 1598, huit guerres de Religion déchirent le royaume."
G9 = "Le 24 août 1572, à Paris puis dans d'autres villes, des milliers de protestants sont tués : c'est le massacre de la Saint-Barthélemy."
G10 = "En 1589, Henri de Navarre, chef des protestants, hérite de la couronne."
G12 = "Le 25 juillet 1593, à Saint-Denis, il se convertit au catholicisme ; il entre dans Paris en 1594. En 1598, il signe l'édit de Nantes."


def donnees(svg, bloc=None):
    d = {}
    d["e1-1"] = {
        "mousse": ordre(
            "Remets les événements dans l'ordre, du plus ancien (en haut) au plus récent (en bas). Utilise les flèches ▲ et ▼, puis vérifie.",
            [("Luther critique l'Église catholique", "1517"), ("Les guerres de Religion commencent en France", "1562"), ("Henri IV signe l'édit de Nantes", "1598")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Lis les années : la plus petite est la plus ancienne.", "L'édit de Nantes est le dernier."]),
        "lieutenant": vf(
            "Suzanne vérifie cinq affirmations sur la Réforme. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui résume les idées de Luther.",
            [("Luther publie ses 95 thèses en 1517.", True, "Contre la vente des indulgences."), ("Luther obéit au pape.", False, "Il refuse de se soumettre au pape."), ("L'imprimerie diffuse les écrits de Luther dans toute l'Europe.", True, "Un même texte circule."),
             ("Les protestants français sont appelés huguenots.", True, "Surtout calvinistes."), ("Calvin organise une Église protestante à Rome.", False, "À Genève.")],
            ["1517 : début de la Réforme.", "Luther refuse l'autorité du pape.", "Pour la justification : cherche la phrase qui parle de la Bible seule."],
            J("Quelle phrase de la fiche résume les idées de Luther ?", G2, [G1, G3, G4], pos=2)),
        "second": qcm(
            carnet("Chronique de Suzanne", "(inventée pour le jeu). « Luther publie ses 95 thèses en 1517. Les guerres de Religion éclatent en 1562 et se terminent par l'édit de Nantes en 1598. Huit guerres, en trente-six ans. »")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 1.",
            [("Combien d'années durent les guerres de Religion ?", ["36 ans", "81 ans", "8 ans", "100 ans"], 0, "1598 − 1562 = 36."),
             ("Combien d'années séparent 1517 et 1562 ?", ["45 ans", "36 ans", "81 ans", "15 ans"], 0, "1562 − 1517 = 45."),
             ("Quel événement du 24 août 1572 est célèbre ?", ["Le massacre de la Saint-Barthélemy", "L'édit de Nantes", "La conversion d'Henri IV", "La mort de Luther"], 0, "Des milliers de protestants sont tués.")],
            ["Soustrais 1562 de 1598.", "Soustrais 1517 de 1562.", "Cherche la date dans la fiche."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 1 ?", G8, [G9, G12, G10], pos=1)),
    }
    d["e1-2"] = {
        "mousse": assoc(
            "Relie chaque nom à sa définition : clique sur un nom, puis sur la bonne définition.",
            [("Martin Luther", "moine allemand qui critique l'Église en 1517"), ("Les protestants", "chrétiens qui suivent Luther ou Calvin"), ("Le pape", "chef de l'Église catholique, à Rome")],
            ["Ouvre la fiche " + F + ".", "Luther est allemand.", "Le pape habite à Rome."]),
        "lieutenant": ordre(
            "Suzanne imprime la chronologie. Remets ces cinq événements dans l'ordre, puis choisis la phrase de la fiche qui date la conversion d'Henri IV.",
            [("Luther publie ses 95 thèses", "1517"), ("Massacre de Wassy", "1562"), ("Massacre de la Saint-Barthélemy", "1572"), ("Henri de Navarre devient roi", "1589"), ("Henri IV se convertit au catholicisme", "1593")],
            ["Compare les années.", "Le massacre de la Saint-Barthélemy : 1572.", "La conversion vient après qu'il est devenu roi."],
            J("Quelle phrase de la fiche date la conversion d'Henri IV ?", G12, [G10, G9, G8], pos=2)),
        "second": tri(
            "Suzanne classe des éléments. Range chaque carte : ce que les protestants refusent, ou ce qu'ils gardent. Puis choisis la phrase de la fiche qui énumère ce que refusent les protestants.",
            [("refusent", "Ce que les protestants refusent"), ("gardent", "Ce que les protestants gardent")],
            [("L'autorité du pape", "refusent"), ("Le culte des saints", "refusent"), ("La messe en latin", "refusent"), ("La Bible comme guide", "gardent"), ("Le temple pour se réunir", "gardent"), ("La prière en français", "gardent")],
            ["Ils refusent le pape, les saints et la messe en latin.", "La Bible seule guide le chrétien.", "Ils prient en français."],
            J("Quelle phrase de la fiche énumère ce que refusent les protestants ?", G7, [G6, G2, G5], pos=0)),
    }
    d["e1-3"] = {
        "mousse": qcm(
            "Lis la question, clique sur la bonne réponse, puis vérifie.",
            [("Quel roi met fin aux guerres de Religion ?", ["Henri IV", "Louis XIV", "Charlemagne"], 0, "Il signe l'édit de Nantes en 1598.")],
            ["Ouvre la fiche " + F + ".", "Il a signé l'édit de Nantes.", "Il est le premier des Bourbons."]),
        "lieutenant": qcm(
            carnet("Une chronique de 1572", "(inventée pour le jeu). « Le 24 août, à Paris puis dans d'autres villes, des milliers de protestants ont été tués. On l'appelle le massacre de la Saint-Barthélemy. Beaucoup n'ont pas oublié. »")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("En quelle année a lieu ce massacre ?", ["1572", "1562", "1598", "1517"], 0, "Le 24 août 1572."),
             ("Qui est visé ?", ["Des protestants", "Des catholiques", "Des Gaulois", "Des nobles"], 0, "Des milliers de protestants."),
             ("Ce massacre fait-il partie des guerres de Religion ?", ["Oui : de 1562 à 1598, huit guerres déchirent le royaume", "Non : c'est une fête", "Non : il a lieu en 1517", "Oui : il date de 1598"], 0, "1572 est entre 1562 et 1598.")],
            ["Le 24 août 1572.", "Des milliers de protestants.", "1572 est entre 1562 et 1598."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", G8, [G9, G12, G2], pos=1)),
        "second": vf(
            "Suzanne a noté six phrases sur Henri IV. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui explique pourquoi beaucoup refusent Henri IV.",
            [("Henri de Navarre est chef des protestants.", True, "Il hérite de la couronne en 1589."), ("Beaucoup de catholiques refusent Henri de Navarre.", True, "Il est protestant."), ("Henri IV se convertit au catholicisme en 1593.", True, "À Saint-Denis."),
             ("Henri IV entre dans Paris en 1589.", False, "En 1594."), ("L'édit de Nantes est signé en 1593.", False, "En 1598."), ("Henri IV hérite de la couronne en 1562.", False, "En 1589.")],
            ["Il est protestant avant de se convertir.", "Il entre dans Paris en 1594.", "L'édit : 1598."],
            J("Quelle phrase de la fiche explique pourquoi beaucoup refusent Henri IV ?", "Beaucoup de catholiques le refusent.", [G10, G12, G9], pos=1)),
    }
    d["e1-4"] = {
        "lieutenant": tri(
            "Suzanne classe des éléments. Range chaque carte : propre aux catholiques, propre aux protestants, ou commun aux deux. Puis choisis la phrase de la fiche qui dit ce qu'ont en commun catholiques et protestants.",
            [("cath", "Catholiques"), ("prot", "Protestants"), ("deux", "Les deux")],
            [("Ils reconnaissent l'autorité du pape", "cath"), ("Ils disent la messe en latin", "cath"), ("Ils se réunissent au temple", "prot"), ("Ils prient en français", "prot"), ("Ils sont chrétiens", "deux"), ("La Bible est leur livre", "deux")],
            ["Le pape et le latin : catholiques.", "Le temple et le français : protestants.", "Ce qu'ils partagent : être chrétiens, la Bible."],
            J("Quelle phrase de la fiche dit ce qu'ont en commun catholiques et protestants ?", G6, [G7, G5, G2], pos=1)),
        "second": tri(
            "Suzanne classe les affirmations. Range chaque affirmation : la fiche l'affirme, ou elle ne l'affirme pas. Puis choisis la phrase de la fiche qui parle de Calvin.",
            [("oui", "La fiche l'affirme"), ("non", "La fiche ne l'affirme pas")],
            [("Calvin organise une Église protestante à Genève.", "oui"), ("Les protestants français sont appelés huguenots.", "oui"), ("Huit guerres de Religion déchirent le royaume.", "oui"),
             ("Luther est un roi allemand.", "non"), ("Calvin dirige l'Église catholique.", "non"), ("L'imprimerie interdit les écrits de Luther.", "non")],
            ["Genève, c'est la ville de Calvin.", "Luther est un moine.", "L'imprimerie diffuse ses écrits."],
            J("Quelle phrase de la fiche parle de Calvin ?", G4, [G5, G8, G3], pos=2)),
    }
    return d
