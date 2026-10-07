"""Salle 5 « Le coin montage » (fiche : notice-montage)."""
from aide import *

F = "« La notice et le montage »"
N1 = "Une notice est un document technique. Elle donne la liste des pièces et des outils, les étapes numérotées dans l'ordre du montage, des schémas qui montrent comment les pièces s'assemblent, et des pictogrammes de sécurité."
N2 = "Elle peut aussi expliquer l'entretien et la réparation."
N3 = "L'ordre compte : certaines étapes deviennent impossibles si on en saute une. On termine toujours par un essai de l'objet."
N4 = "Deux objets qui répondent au même besoin se comparent sur leurs avantages et leurs inconvénients : énergie utilisée, matériaux, facilité d'usage, prix, entretien."
N5 = "Un ouvre-boîte à manivelle fonctionne sans pile ni prise ; un ouvre-boîte électrique demande moins d'effort."


def donnees(svg, bloc=None):
    d = {}
    d["e5-1"] = {
        "mousse": ordre(
            "Remets les étapes du montage dans l'ordre avec ▲ et ▼, puis vérifie.",
            [("Vérifier les pièces avec la liste de la notice", "étape 1"), ("Placer les piles dans le bon sens", "étape 2"), ("Essayer l'interrupteur", "étape 3")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "On vérifie d'abord les pièces.", "L'essai vient à la fin."]),
        "lieutenant": ordre(
            "Éléonore monte un ouvre-boîte à manivelle. Remets les cinq étapes de sa notice dans l'ordre, puis choisis la phrase de la fiche qui explique pourquoi l'ordre compte.",
            [("Lire les pictogrammes de sécurité", "étape 1"), ("Vérifier la liste des pièces et des outils", "étape 2"), ("Assembler les pièces en suivant les schémas", "étape 3"), ("Serrer la manivelle", "étape 4"), ("Essayer l'objet sur une boîte vide", "étape 5")],
            ["La sécurité d'abord, puis la liste des pièces.", "On assemble avant de serrer.", "L'essai termine le montage."],
            J("Quelle phrase de la fiche explique pourquoi l'ordre compte ?", N3, [N1, N2, N4], pos=1)),
        "second": tri(
            "Éléonore classe le contenu d'une notice. Range chaque élément : ce que la notice contient, ou ce qu'elle ne contient pas. Puis choisis la phrase de la fiche qui énumère le contenu d'une notice.",
            [("oui", "La notice le contient"), ("non", "La notice ne le contient pas")],
            [("La liste des pièces et des outils", "oui"), ("Des étapes numérotées", "oui"), ("Des pictogrammes de sécurité", "oui"), ("L'histoire de l'inventeur", "non"), ("La publicité de la marque", "non"), ("Le prix de chaque pièce", "non")],
            ["Une notice sert à monter et à utiliser l'objet.", "Elle contient des schémas et des pictogrammes.", "Elle ne raconte pas l'histoire de l'inventeur."],
            J("Quelle phrase de la fiche énumère le contenu d'une notice ?", N1, [N3, N2, N4], pos=2)),
    }
    d["e5-2"] = {
        "mousse": vf(
            "Pour chaque phrase, clique sur « Vrai » ou sur « Faux », puis vérifie.",
            [("On lit la notice avant de commencer le montage.", True, "Cela évite de tout démonter."), ("Les étapes peuvent se faire dans n'importe quel ordre.", False, "L'ordre compte."), ("La notice donne la liste des pièces.", True, "On les vérifie avant de commencer.")],
            ["Ouvre la fiche " + F + ".", "Une notice se lit d'abord.", "Les étapes sont numérotées."]),
        "lieutenant": qcm(
            carnet("Extrait de notice", "(inventé pour le jeu). Pièces : 1 manivelle, 1 lame, 1 boîtier. Outil : 1 tournevis. Attention ! Ne pas toucher la lame. Étape 1 : poser le boîtier. Étape 2 : fixer la lame. Étape 3 : visser la manivelle. Étape 4 : essayer.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("Combien de pièces la notice liste-t-elle ?", ["3", "4", "1", "5"], 0, "Manivelle, lame, boîtier."),
             ("Quel outil est nécessaire ?", ["Un tournevis", "Un marteau", "Une scie", "Une pince"], 0, "C'est écrit dans l'extrait."),
             ("Pourquoi la lame se fixe-t-elle avant la manivelle ?", ["Parce que l'ordre compte : on ne peut pas sauter ni inverser une étape", "Parce que la lame est plus lourde", "Parce que la manivelle est fragile", "Parce que la notice est courte"], 0, "Certaines étapes deviennent impossibles.")],
            ["Compte les pièces listées.", "Cherche l'outil.", "L'ordre est numéroté."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", N3, [N1, N4, N2], pos=2)),
        "second": qcm(
            carnet("Comparaison d'Éléonore", "(d'après la fiche). Un ouvre-boîte à manivelle fonctionne sans pile ni prise ; un ouvre-boîte électrique demande moins d'effort. Les deux répondent au même besoin : ouvrir une boîte.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Les deux objets répondent-ils au même besoin ?", ["Oui : ouvrir une boîte", "Non", "Seulement le modèle électrique", "On ne peut pas savoir"], 0, "Même besoin."),
             ("Quel avantage a le modèle à manivelle ?", ["Il fonctionne sans pile ni prise", "Il demande moins d'effort", "Il est plus rapide", "Il est plus joli"], 0, "Il n'a pas besoin d'énergie extérieure."),
             ("Quel avantage a le modèle électrique ?", ["Il demande moins d'effort", "Il fonctionne sans pile", "Il est toujours moins cher", "Il se règle tout seul"], 0, "Moins d'effort.")],
            ["Même besoin, solutions différentes.", "Pense à l'énergie nécessaire.", "Compare efforts et sources d'énergie."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", N5, [N4, N1, N3], pos=2)),
    }
    d["e5-3"] = {
        "mousse": qcm(
            "Compare les deux objets et choisis la bonne réponse, puis vérifie.",
            [("Une bougie et une lampe torche…", ["répondent au même besoin : éclairer", "n'ont rien en commun", "marchent avec une pile"], 0, "Même fonction d'usage.")],
            ["Ouvre la fiche " + F + ".", "À quoi servent les deux objets ?", "Les deux éclairent."]),
        "lieutenant": vf(
            "Éléonore compare des objets. Pour chaque affirmation, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui dit sur quoi on compare deux objets.",
            [("Deux objets qui répondent au même besoin se comparent sur leurs avantages et inconvénients.", True, "Énergie, matériaux, usage, prix, entretien."), ("On compare deux objets seulement sur leur couleur.", False, "Plusieurs critères."),
             ("Un ouvre-boîte à manivelle fonctionne sans pile ni prise.", True, "Pas d'énergie extérieure."), ("Un ouvre-boîte électrique demande plus d'effort.", False, "Moins d'effort."),
             ("Le prix est un critère de comparaison.", True, "Comme l'entretien.")],
            ["Plusieurs critères : énergie, matériaux, prix...", "Le modèle électrique demande moins d'effort.", "Pour la justification : cherche la phrase qui énumère les critères."],
            J("Quelle phrase de la fiche dit sur quoi on compare deux objets ?", N4, [N5, N1, N3], pos=0)),
        "second": ordre(
            "Éléonore compare deux ouvre-boîtes. Remets les étapes de sa démarche dans l'ordre, puis choisis la phrase de la fiche qui justifie le dernier maillon.",
            ["Identifier le besoin : ouvrir une boîte de conserve.", "Lister les solutions : manivelle ou électrique.", "Comparer l'énergie, les matériaux, la facilité d'usage, le prix, l'entretien.", "Choisir selon l'usage prévu.", "Rédiger la notice."],
            ["On commence par le besoin.", "On compare avant de choisir.", "La notice vient à la fin."],
            J("Quelle phrase de la fiche justifie l'étape de comparaison ?", N4, [N1, N3, N2], pos=1)),
    }
    d["e5-4"] = {
        "lieutenant": trous(
            "Éléonore a rédigé le cycle de l'inventrice, mais il manque des mots. Clique sur une étiquette, puis sur le trou où elle va. Trois étiquettes sont en trop. Puis choisis la phrase de la fiche qui justifie le mot « essai ».",
            "Une notice donne la liste des [[pièces]] et des [[outils]], des étapes [[numérotées]], des [[schémas]] et des pictogrammes de sécurité. On termine toujours par un [[essai]] de l'objet.",
            ["pièces", "outils", "numérotées", "schémas", "essai", "décorations", "marques", "prix"],
            ["Relis le premier paragraphe de la fiche.", "Les étapes ont un numéro.", "La dernière étape est un essai."],
            J("Quelle phrase de la fiche justifie le mot « essai » ?", N3, [N1, N4, N2], pos=1)),
        "second": trous(
            "Éléonore résume ce qu'elle sait de la notice. Clique sur une étiquette, puis sur le trou où elle va. Quatre étiquettes sont en trop. Puis choisis la phrase de la fiche qui justifie le mot « entretien ».",
            "Une notice est un document [[technique]]. Elle peut aussi expliquer l'[[entretien]] et la [[réparation]]. Un ouvre-boîte à manivelle fonctionne sans [[pile]] ni [[prise]].",
            ["technique", "entretien", "réparation", "pile", "prise", "couleur", "marque", "histoire", "décoration"],
            ["Une notice peut expliquer plus que le montage.", "Un modèle sans pile ni prise.", "Un document technique."],
            J("Quelle phrase de la fiche justifie le mot « entretien » ?", N2, [N1, N3, N5], pos=0)),
    }
    return d
