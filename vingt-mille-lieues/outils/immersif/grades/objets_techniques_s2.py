"""Salle 2 « L'établi » (fiche : constituants)."""
from aide import *

F = "« De quoi l'objet est-il fait ? »"
C1 = "Un objet technique est un assemblage de constituants."
C2 = "Pour le décrire, on nomme chaque pièce et on dit son rôle dans le fonctionnement de l'objet : c'est sa fonction technique."
C3 = "Fonction d'usage : à quoi sert l'objet entier (éclairer)."
C4 = "Fonction technique : à quoi sert une pièce (fournir l'énergie, renvoyer la lumière vers l'avant)."
C5 = "Solution technique : la pièce choisie pour remplir cette fonction (une pile, un réflecteur)."
C6 = "Pour « ouvrir et fermer le circuit », on peut choisir un bouton-poussoir ou un interrupteur à glissière. Pour « freiner » un vélo, des patins sur la jante ou un frein à disque."
C7 = "On représente ces choix par un schéma légendé."


def donnees(svg, bloc=None):
    d = {}
    d["e2-1"] = {
        "mousse": {
            "type": "plan", "titre": "Complète le schéma de la lampe torche", "colonnes": 2,
            "cases": [{"libelle": "Elle fournit l'énergie", "reponse": "La pile"}, {"libelle": "Elle produit la lumière", "reponse": "L'ampoule"}, {"libelle": "Il ouvre et ferme le circuit", "reponse": "L'interrupteur"}],
            "etiquettes": ["La pile", "L'ampoule", "L'interrupteur", "Le moteur"],
            "consigne": "Awa démonte une lampe torche. Clique sur une étiquette, puis sur la case où elle doit se placer. Une étiquette est en trop.",
            "indices": ["Ouvre la fiche " + F + " dans la Bibliothèque.", "La pile donne l'énergie.", "L'interrupteur sert à allumer."]},
        "lieutenant": vf(
            "Awa a noté cinq phrases sur la lampe torche. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui définit la fonction technique.",
            [("Un objet technique est un assemblage de constituants.", True, "Chaque pièce a un rôle."), ("La fonction technique décrit à quoi sert l'objet entier.", False, "Elle décrit le rôle d'une pièce."),
             ("Le réflecteur renvoie la lumière vers l'avant.", True, "C'est une fonction technique."), ("Une pile est la solution technique choisie pour fournir l'énergie.", True, "Elle remplit la fonction."),
             ("Éclairer est la fonction technique du réflecteur.", False, "Éclairer est la fonction d'usage de la lampe.")],
            ["La fonction technique concerne une pièce.", "La fonction d'usage concerne l'objet entier.", "Une solution est la pièce choisie."],
            J("Quelle phrase de la fiche définit la fonction technique ?", C2, [C3, C5, C1], pos=2)),
        "second": qcm(
            carnet("Schéma légendé d'Awa", "(inventé pour le jeu). Lampe torche : pile (fournit l'énergie), interrupteur (ouvre et ferme le circuit), ampoule (produit la lumière), réflecteur (renvoie la lumière vers l'avant), boîtier (protège et tient les pièces).")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("Combien de constituants cite le schéma ?", ["5", "3", "4", "6"], 0, "Pile, interrupteur, ampoule, réflecteur, boîtier."),
             ("Quelle est la fonction technique du réflecteur ?", ["Renvoyer la lumière vers l'avant", "Fournir l'énergie", "Ouvrir le circuit", "Protéger les pièces"], 0, "C'est son rôle."),
             ("Pourquoi représente-t-on l'objet par un schéma légendé ?", ["Pour montrer les pièces, leur rôle et leur place", "Pour décorer", "Pour le vendre", "Pour le cacher"], 0, "On représente ces choix par un schéma légendé.")],
            ["Compte les pièces citées.", "Relis la légende du réflecteur.", "Un schéma montre les pièces et leur place."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", C7, [C4, C5, C1], pos=1)),
    }
    d["e2-2"] = {
        "mousse": assoc(
            "Monsieur Marcel démonte un vélo. Relie chaque pièce à son rôle. Clique sur une pièce, puis sur son rôle.",
            [("Le guidon", "diriger le vélo"), ("Les freins", "ralentir et arrêter le vélo"), ("La chaîne", "transmettre le mouvement à la roue")],
            ["Ouvre la fiche " + F + ".", "Le guidon sert à choisir la direction.", "Les freins servent à ralentir."]),
        "lieutenant": {
            "type": "plan", "titre": "Fonctions et solutions", "colonnes": 2,
            "cases": [{"libelle": "Fonction d'usage de la lampe torche", "reponse": "éclairer"}, {"libelle": "Fonction technique de la pile", "reponse": "fournir l'énergie"}, {"libelle": "Fonction technique du réflecteur", "reponse": "renvoyer la lumière vers l'avant"},
                      {"libelle": "Solution technique pour ouvrir et fermer le circuit", "reponse": "un bouton-poussoir"}, {"libelle": "Solution technique pour freiner un vélo", "reponse": "des patins sur la jante"}, {"libelle": "Autre solution pour freiner un vélo", "reponse": "un frein à disque"}],
            "etiquettes": ["éclairer", "fournir l'énergie", "renvoyer la lumière vers l'avant", "un bouton-poussoir", "des patins sur la jante", "un frein à disque", "une couleur", "un prix"],
            "consigne": "Monsieur Marcel complète sa fiche. Place chaque étiquette dans la bonne case. Deux étiquettes sont en trop. Puis choisis la phrase de la fiche qui donne plusieurs solutions pour freiner.",
            "indices": ["Fonction d'usage : l'objet entier.", "Une fonction technique concerne une pièce.", "Une même fonction peut avoir plusieurs solutions."],
            "justification": J("Quelle phrase de la fiche donne plusieurs solutions pour une même fonction ?", C6, [C4, C5, C7], pos=1)},
        "second": {
            "type": "plan", "titre": "Le vocabulaire de l'objet technique", "colonnes": 2,
            "cases": [{"libelle": "Décrit à quoi sert l'objet entier", "reponse": "fonction d'usage"}, {"libelle": "Décrit le rôle d'une pièce", "reponse": "fonction technique"}, {"libelle": "La pièce choisie pour remplir la fonction", "reponse": "solution technique"},
                      {"libelle": "Pièce d'une lampe qui renvoie la lumière", "reponse": "réflecteur"}, {"libelle": "Dessin simplifié qui montre les pièces et leur place", "reponse": "schéma"}],
            "etiquettes": ["fonction d'usage", "fonction technique", "solution technique", "réflecteur", "schéma", "fonction d'estime", "matériau", "notice"],
            "consigne": "Awa fait réviser le vocabulaire. Place chaque étiquette dans la bonne case. Trois étiquettes sont en trop. Puis choisis la phrase de la fiche qui définit la solution technique.",
            "indices": ["Usage : l'objet entier. Technique : une pièce.", "Une solution est une pièce choisie.", "Le schéma est un dessin."],
            "justification": J("Quelle phrase de la fiche définit la solution technique ?", C5, [C3, C4, C7], pos=2)},
    }
    d["e2-3"] = {
        "mousse": qcm(
            "Lis la question, clique sur la bonne réponse, puis vérifie.",
            [("« Fournir l'énergie », pour la pile d'une lampe, c'est…", ["le rôle d'une pièce", "à quoi sert l'objet entier", "une couleur"], 0, "C'est une fonction technique.")],
            ["Ouvre la fiche " + F + ".", "La pile est une seule pièce.", "On parle du rôle d'une pièce."]),
        "lieutenant": qcm(
            carnet("Commande d'Éléonore", "(inventée pour le jeu). Éléonore veut un ouvre-boîte. Elle hésite entre un modèle à manivelle et un modèle électrique. Les deux doivent remplir la même fonction technique : couper le couvercle.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3.",
            [("Quelle est la fonction d'usage de l'ouvre-boîte ?", ["Ouvrir une boîte de conserve", "Couper le couvercle", "Tourner la manivelle", "Brancher le fil"], 0, "Elle concerne l'objet entier."),
             ("Quelle est la fonction technique à remplir ?", ["Couper le couvercle", "Ouvrir une boîte de conserve", "Être joli", "Se brancher"], 0, "Elle concerne une pièce."),
             ("Les deux modèles remplissent-ils cette fonction de la même façon ?", ["Non : les solutions techniques sont différentes", "Oui : ce sont les mêmes pièces", "Oui : ils ont la même énergie", "On ne peut pas savoir"], 0, "Une même fonction, plusieurs solutions.")],
            ["Usage : l'objet entier. Technique : une pièce.", "Une pièce coupe le couvercle.", "Même fonction, solutions différentes."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", C6, [C4, C5, C2], pos=1)),
        "second": vf(
            "Awa a noté six phrases de vocabulaire. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui distingue fonction d'usage et fonction technique.",
            [("Fonction d'usage : à quoi sert l'objet entier.", True, "Par exemple, éclairer."), ("Fonction technique : à quoi sert une pièce.", True, "Par exemple, fournir l'énergie."), ("Solution technique : la pièce choisie pour remplir une fonction.", True, "Une pile, un réflecteur."),
             ("Une fonction technique n'a qu'une seule solution possible.", False, "Plusieurs solutions sont souvent possibles."), ("La fonction d'usage et la fonction technique désignent la même chose.", False, "L'une parle de l'objet, l'autre d'une pièce."), ("Un schéma légendé sert à décorer l'atelier.", False, "Il montre les pièces et leur place.")],
            ["Usage : l'objet entier.", "Technique : une pièce.", "Solution : la pièce choisie."],
            J("Quelle phrase de la fiche distingue fonction d'usage et fonction technique ?", C4, [C3, C5, C1], pos=1)),
    }
    d["e2-4"] = {
        "lieutenant": trous(
            "Zoé a rédigé le carnet de l'inventrice, mais il manque des mots. Clique sur une étiquette, puis sur le trou où elle va. Trois étiquettes sont en trop. Puis choisis la phrase de la fiche qui justifie le mot « solution technique ».",
            "Je veux éclairer : c'est la [[fonction d'usage]]. Une pièce doit renvoyer la lumière vers l'avant : c'est une [[fonction technique]]. Pour la remplir, je choisis un réflecteur : c'est la [[solution technique]]. Je fais un [[schéma]] légendé pour montrer mes choix.",
            ["fonction d'usage", "fonction technique", "solution technique", "schéma", "fonction d'estime", "matériau", "notice"],
            ["Relis les définitions de la fiche.", "Un réflecteur est une pièce.", "Un schéma est un dessin."],
            J("Quelle phrase de la fiche justifie le mot « solution technique » ?", C5, [C3, C4, C2], pos=1)),
        "second": trous(
            "Awa a rédigé son rapport de démontage, mais il manque des mots. Clique sur une étiquette, puis sur le trou où elle va. Quatre étiquettes sont en trop. Puis choisis la phrase de la fiche qui justifie le mot « assemblage ».",
            "Un objet technique est un [[assemblage]] de constituants. On nomme chaque [[pièce]] et on dit son rôle : c'est sa [[fonction technique]]. Pour « freiner » un vélo, on peut choisir des [[patins]] sur la jante ou un frein à [[disque]].",
            ["assemblage", "pièce", "fonction technique", "patins", "disque", "décoration", "marque", "notice", "énergie"],
            ["Les mots viennent de la partie « Décrire un objet technique ».", "Un vélo a deux solutions pour freiner.", "Une pièce a un rôle."],
            J("Quelle phrase de la fiche justifie le mot « assemblage » ?", C1, [C2, C6, C7], pos=0)),
    }
    return d
