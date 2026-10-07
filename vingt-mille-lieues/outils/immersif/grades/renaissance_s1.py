"""Salle 1 « L'imprimerie de Maître Jacquet » (fiche : renaissance-humanisme)."""
from aide import *

F = "« La Renaissance et l'humanisme »"
R1 = "La Renaissance commence en Italie, à Florence, au XVe siècle, puis gagne l'Europe au XVIe siècle."
R2 = "Artistes et savants prennent l'Antiquité grecque et romaine pour modèle : colonnes, symétrie, statues, textes anciens."
R3 = "Les humanistes apprennent le latin, le grec et l'hébreu pour lire les textes anciens dans leur langue."
R4 = "Ils pensent que l'homme peut progresser grâce au savoir."
R5 = "En France, Guillaume Budé, conseiller de François Ier, est l'un d'eux."
R6 = "Vers 1450, à Mayence, Gutenberg met au point l'imprimerie à caractères mobiles : des lettres de métal que l'on assemble, encre et presse."
R7 = "Un même texte est tiré en centaines d'exemplaires et circule dans toute l'Europe."
R8 = "Dès 1496, le roi Charles VIII revient d'Italie avec des artistes italiens et fait aménager Amboise."


def donnees(svg, bloc=None):
    d = {}
    d["e1-1"] = {
        "mousse": ordre(
            "Remets ces moments dans l'ordre, du plus ancien (en haut) au plus récent (en bas). Utilise les flèches ▲ et ▼, puis vérifie.",
            [("Les Grecs et les Romains bâtissent des temples", "l'Antiquité"), ("Gutenberg met au point l'imprimerie", "vers 1450"), ("François Ier devient roi de France", "1515")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Les Grecs et les Romains sont les plus anciens.", "François Ier est le plus récent."]),
        "lieutenant": qcm(
            carnet("La page de Maître Jacquet", "(inventée pour le jeu). Maître Jacquet imprime un livre à Amboise, au printemps 1518. Il explique : « Depuis que Gutenberg a mis au point l'imprimerie à caractères mobiles, vers 1450, un texte peut être tiré en centaines d'exemplaires. »")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("Où et vers quand Gutenberg met-il au point l'imprimerie ?", ["À Mayence, vers 1450", "À Florence, vers 1500", "À Amboise, en 1518", "À Rome, en 800"], 0, "À caractères mobiles."),
             ("Combien d'années séparent 1450 de 1518 ?", ["68 ans", "18 ans", "100 ans", "168 ans"], 0, "1518 − 1450 = 68."),
             ("Pourquoi l'imprimerie aide-t-elle les idées à circuler ?", ["Un même texte est tiré en centaines d'exemplaires", "Les livres deviennent secrets", "On n'écrit plus de livres", "Les livres sont copiés à la main"], 0, "Il circule dans toute l'Europe.")],
            ["Les lettres de métal se réassemblent.", "Soustrais 1450 de 1518.", "Pense au nombre d'exemplaires."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", R7, [R6, R3, R8], pos=1)),
        "second": qcm(
            carnet("Notes de Maître Jacquet", "(d'après la fiche). Charles VIII revient d'Italie en 1496 avec des artistes. François Ier devient roi en 1515. Léonard de Vinci s'installe à Amboise en 1516. La Renaissance commence en Italie au XVe siècle, puis gagne l'Europe au XVIe siècle.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Combien d'années entre le retour de Charles VIII (1496) et l'arrivée de Léonard (1516) ?", ["20 ans", "10 ans", "30 ans", "1 an"], 0, "1516 − 1496 = 20."),
             ("Dans quel pays la Renaissance commence-t-elle ?", ["En Italie", "En France", "En Allemagne", "En Grèce"], 0, "À Florence."),
             ("Qui est le premier roi à ramener des artistes italiens à Amboise ?", ["Charles VIII", "François Ier", "Louis XIV", "Charlemagne"], 0, "Dès 1496.")],
            ["Soustrais 1496 de 1516.", "Florence est en Italie.", "1496 vient avant 1515."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", R1, [R8, R2, R6], pos=2)),
    }
    d["e1-2"] = {
        "mousse": assoc(
            "Relie chaque mot à sa définition : clique sur un mot, puis sur la bonne définition.",
            [("La Renaissance", "on redécouvre l'art de l'Antiquité"), ("L'Antiquité", "l'époque des Grecs et des Romains"), ("L'imprimerie", "fabriquer beaucoup de livres")],
            ["Ouvre la fiche " + F + ".", "« Re-naissance » : quelque chose renaît.", "Les Grecs et les Romains : l'Antiquité."]),
        "lieutenant": ordre(
            "Maître Jacquet explique l'histoire du livre. Remets ces cinq étapes dans l'ordre, puis choisis la phrase de la fiche qui décrit l'invention de Gutenberg.",
            [("Les textes antiques sont recopiés à la main", "avant 1450"), ("Gutenberg met au point l'imprimerie", "vers 1450"), ("Charles VIII ramène des artistes d'Italie", "1496"), ("François Ier devient roi", "1515"), ("Les lecteurs royaux enseignent gratuitement", "1530")],
            ["Compare les dates.", "L'imprimerie vient vers 1450.", "1530 est la date la plus récente."],
            J("Quelle phrase de la fiche décrit l'invention de Gutenberg ?", R6, [R7, R3, R8], pos=2)),
        "second": tri(
            "Maître Jacquet classe des éléments. Range chaque carte : héritage de l'Antiquité, ou invention de la Renaissance ? Puis choisis la phrase de la fiche qui énumère ce qu'on imite de l'Antiquité.",
            [("antique", "Hérité de l'Antiquité"), ("renaissance", "Invention de la Renaissance")],
            [("Les colonnes", "antique"), ("La symétrie", "antique"), ("Les statues", "antique"), ("L'imprimerie à caractères mobiles", "renaissance"), ("Les lecteurs royaux", "renaissance"), ("Le dépôt légal", "renaissance")],
            ["Les artistes imitent colonnes, symétrie, statues.", "L'imprimerie date d'environ 1450.", "Les lecteurs royaux : 1530."],
            J("Quelle phrase de la fiche énumère ce qu'on imite de l'Antiquité ?", R2, [R6, R3, R7], pos=0)),
    }
    d["e1-3"] = {
        "mousse": qcm(
            "Lis la question, clique sur la bonne réponse, puis vérifie.",
            [("Où la Renaissance commence-t-elle ?", ["En Italie", "En Angleterre", "En Égypte"], 0, "À Florence, au XVe siècle.")],
            ["Ouvre la fiche " + F + ".", "C'est un pays au sud des Alpes.", "Léonard de Vinci vient de ce pays."]),
        "lieutenant": vf(
            "Colombe a noté cinq phrases sur l'humanisme. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui parle de Guillaume Budé.",
            [("Les humanistes apprennent le latin, le grec et l'hébreu.", True, "Pour lire les textes anciens."), ("Les humanistes refusent le savoir.", False, "Ils croient au progrès par le savoir."), ("Guillaume Budé est conseiller de François Ier.", True, "C'est un humaniste."),
             ("La Renaissance commence en Angleterre.", False, "En Italie."), ("Les textes anciens sont lus dans leur langue d'origine.", True, "C'est la méthode des humanistes.")],
            ["Les humanistes lisent les textes anciens.", "Ils pensent que l'homme progresse par le savoir.", "Budé conseille le roi."],
            J("Quelle phrase de la fiche parle de Guillaume Budé ?", R5, [R3, R4, R1], pos=1)),
        "second": vf(
            "Colombe a noté six phrases sur la Renaissance. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui explique ce que pensent les humanistes.",
            [("La Renaissance commence à Florence au XVe siècle.", True, "Puis gagne l'Europe au XVIe siècle."), ("Un même texte imprimé peut atteindre des centaines de lecteurs.", True, "Centaines d'exemplaires."), ("Les humanistes ne lisent que le français.", False, "Latin, grec, hébreu."),
             ("Gutenberg met au point l'imprimerie à Amboise.", False, "À Mayence."), ("Les humanistes croient que le savoir fait progresser l'homme.", True, "C'est leur idée centrale."), ("Charles VIII ramène des artistes italiens en 1496.", True, "Il fait aménager Amboise.")],
            ["Mayence, pas Amboise.", "Les humanistes lisent des langues anciennes.", "Le savoir fait progresser."],
            J("Quelle phrase de la fiche explique ce que pensent les humanistes ?", R4, [R3, R5, R2], pos=0)),
    }
    d["e1-4"] = {
        "lieutenant": trous(
            "Maître Jacquet imprime une page, mais il manque des mots. Clique sur une étiquette, puis sur le trou où elle va. Trois étiquettes sont en trop. Puis choisis la phrase de la fiche qui justifie le mot « humanistes ».",
            "La Renaissance commence en [[Italie]], à Florence. Artistes et savants prennent l'[[Antiquité]] pour modèle. Les [[humanistes]] apprennent le latin, le grec et l'[[hébreu]]. Grâce à l'[[imprimerie]], un même texte circule en centaines d'exemplaires.",
            ["Italie", "Antiquité", "humanistes", "hébreu", "imprimerie", "Égypte", "chevaliers", "télévision"],
            ["Relis le premier paragraphe de la fiche.", "Ils lisent les textes anciens.", "Un même texte en centaines d'exemplaires."],
            J("Quelle phrase de la fiche justifie le mot « humanistes » ?", R3, [R2, R6, R8], pos=2)),
        "second": trous(
            "Maître Jacquet résume la Renaissance, mais il manque des mots. Clique sur une étiquette, puis sur le trou où elle va. Quatre étiquettes sont en trop. Puis choisis la phrase de la fiche qui justifie le mot « Mayence ».",
            "Vers 1450, à [[Mayence]], Gutenberg met au point l'imprimerie à [[caractères]] mobiles : des lettres de [[métal]] que l'on assemble. Dès 1496, Charles VIII revient d'[[Italie]] avec des [[artistes]] et fait aménager Amboise.",
            ["Mayence", "caractères", "métal", "Italie", "artistes", "Florence", "papier", "chevaliers", "bois"],
            ["La ville de Gutenberg est en Allemagne.", "Les lettres sont mobiles.", "Charles VIII revient d'Italie."],
            J("Quelle phrase de la fiche justifie le mot « Mayence » ?", R6, [R8, R7, R1], pos=1)),
    }
    return d
