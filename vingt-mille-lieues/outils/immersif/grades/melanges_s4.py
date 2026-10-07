"""Salle 4 « L'atelier de tri » (fiche : separer-solides)."""
from aide import *

F = "« Séparer un mélange de solides »"
T1 = "Pour séparer un mélange de solides, on cherche une différence entre les constituants."
T2 = "La taille → tamisage : les grains fins passent à travers le tamis, les gros restent."
T3 = "Le fer → aimantation : seuls le fer et les objets en acier (qui contient du fer) sont attirés."
T4 = "Flotter ou couler → flottation : dans l'eau, la sciure flotte, le sable coule."
T5 = "L'aspect (couleur, forme) → tri à la main."
T6 = "Un tamis ne peut pas séparer la limaille de fer et le sable : leurs grains ont à peu près la même taille. On utilise alors l'aimant."
T7 = "Dans les centres de tri des déchets, de gros aimants séparent les boîtes de conserve en acier des autres emballages ; les canettes en aluminium, elles, ne sont pas attirées."


def donnees(svg, bloc=None):
    d = {}
    d["e4-1"] = {
        "mousse": assoc(
            "Nadia a trois bacs à trier. Relie chaque mélange à la méthode qui permet de le séparer. Clique d'abord à gauche, puis à droite.",
            [("Des clous en acier et des perles en plastique", "l'aimant"), ("De gros cailloux et du sable fin", "le tamis"), ("De la sciure de bois et du sable", "une bassine d'eau")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "L'aimant attire l'acier.", "La sciure de bois flotte."]),
        "lieutenant": tri(
            "Nadia range des mélanges de solides selon la méthode qui les sépare. Range chaque mélange sous la bonne méthode, puis choisis la phrase de la fiche qui donne le principe général.",
            [("tamis", "Le tamis"), ("aimant", "L'aimant"), ("eau", "La bassine d'eau"), ("main", "Le tri à la main")],
            [("Gros cailloux et sable fin", "tamis"), ("Riz et gravier", "tamis"), ("Limaille de fer et sable", "aimant"), ("Clous en acier et sable", "aimant"),
             ("Copeaux de bois et sable", "eau"), ("Perles rouges et perles bleues", "main")],
            ["Cherche la différence entre les deux constituants.", "Le fer et l'acier sont attirés.", "Les copeaux flottent, le sable coule."],
            J("Quelle phrase de la fiche donne le principe général du tri ?", T1, [T2, T3, T5], pos=0)),
        "second": qcm(
            carnet("Centre de tri", "(d'après la fiche). Sur un tapis roulant défilent des boîtes de conserve en acier, des canettes en aluminium, des bouteilles en plastique et des cartons. Un gros aimant est suspendu au-dessus du tapis.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 1.",
            [("Que soulève l'aimant ?", ["Les boîtes de conserve en acier", "Les canettes en aluminium", "Les bouteilles en plastique", "Les cartons"], 0, "L'acier contient du fer."),
             ("Pourquoi les canettes en aluminium restent-elles sur le tapis ?", ["L'aluminium n'est pas attiré par l'aimant", "Elles sont trop légères", "Elles sont trop grandes", "Elles sont en fer"], 0, "L'aluminium est un métal non attiré."),
             ("Quelle autre méthode séparerait les cartons des bouteilles ?", ["Le tri à la main, d'après l'aspect", "L'aimant", "L'évaporation", "La filtration"], 0, "L'aspect (forme, couleur).")],
            ["L'acier contient du fer.", "Tous les métaux ne sont pas attirés.", "Pour des objets qui ont un aspect différent, on peut trier à la main."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 1 ?", T3, [T7, T4, T2], pos=1)),
    }
    d["e4-2"] = {
        "mousse": ordre(
            "Nadia veut séparer des cailloux du sable. Remets les étapes dans l'ordre avec ▲ et ▼, puis vérifie.",
            ["Poser le tamis au-dessus d'une bassine vide.", "Verser le mélange dans le tamis.", "Secouer doucement le tamis.", "Le sable est dans la bassine, les cailloux restent dans le tamis."],
            ["Ouvre la fiche " + F + ".", "Il faut une bassine sous le tamis.", "La dernière étape est le résultat."]),
        "lieutenant": ordre(
            "Nadia veut séparer un mélange de limaille de fer, de sable et de sciure. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche qui justifie le recours à l'aimant.",
            ["Passer l'aimant au-dessus du mélange : on retire la limaille.", "Verser le reste dans une bassine d'eau.", "Observer : la sciure flotte, le sable coule.", "Récupérer la sciure à la surface.", "Laisser sécher le sable et la sciure séparément."],
            ["L'aimant ne demande pas d'eau : on commence par lui.", "On met de l'eau avant d'observer ce qui flotte.", "Le séchage vient à la fin."],
            J("Quelle phrase de la fiche justifie le recours à l'aimant pour la limaille ?", T6, [T3, T4, T2], pos=0)),
        "second": tri(
            "Nadia choisit la méthode la mieux adaptée. Range chaque mélange dans la colonne de la méthode qui convient, puis choisis la phrase de la fiche qui explique pourquoi le tamis ne suffit pas pour un des mélanges.",
            [("tamis", "Le tamis suffit"), ("autre", "Le tamis ne suffit pas")],
            [("Gravier et sable fin", "tamis"), ("Gros cailloux et sable", "tamis"), ("Limaille de fer et sable", "autre"), ("Sciure et sable de même taille", "autre"), ("Perles rouges et perles bleues de même taille", "autre"), ("Boutons et sable fin", "tamis")],
            ["Le tamis trie selon la taille.", "Si les grains ont la même taille, il ne sépare pas.", "Pour les perles, c'est la couleur qui diffère."],
            J("Quelle phrase de la fiche explique pourquoi le tamis ne suffit pas ?", T6, [T2, T1, T5], pos=2)),
    }
    d["e4-3"] = {
        "mousse": qcm(
            "Nadia te prête son aimant. Lis la question, clique sur la bonne réponse, puis vérifie.",
            [("Un aimant attire…", ["les objets en fer et en acier", "tous les objets", "le bois"], 0, "Il attire le fer et l'acier.")],
            ["Ouvre la fiche " + F + ".", "L'acier contient du fer.", "Le bois n'est pas attiré."]),
        "lieutenant": vf(
            "Nadia affirme cinq choses. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui parle des canettes en aluminium.",
            [("L'aimant attire les objets en fer et en acier.", True, "L'acier contient du fer."), ("L'aimant attire tous les métaux.", False, "Pas l'aluminium."), ("Une canette en aluminium est attirée.", False, "L'aluminium n'est pas attiré."),
             ("Un centre de tri utilise de gros aimants.", True, "Pour les boîtes en acier."), ("Le tamis sépare bien la limaille de fer du sable.", False, "Les grains ont la même taille.")],
            ["L'acier est attiré, l'aluminium non.", "Un tamis trie selon la taille.", "Pour la justification : cherche la phrase qui nomme les canettes."],
            J("Quelle phrase de la fiche parle des canettes en aluminium ?", T7, [T3, T6, T4], pos=1)),
        "second": vf(
            "Nadia a noté six phrases sur les méthodes de tri. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui énumère les méthodes selon la différence.",
            [("La taille permet de séparer par tamisage.", True, "Les grains fins passent."), ("Le fer permet de séparer par aimantation.", True, "Il est attiré."), ("Flotter ou couler permet de séparer par flottation.", True, "Dans l'eau."),
             ("La couleur permet de séparer par aimantation.", False, "Par tri à la main."), ("Tous les métaux sont attirés par l'aimant.", False, "Seulement le fer et l'acier."), ("La flottation se fait dans l'huile.", False, "Dans l'eau.")],
            ["Une différence, une méthode.", "L'aspect se trie à la main.", "La flottation se fait dans l'eau."],
            J("Quelle phrase de la fiche donne la méthode pour des grains de tailles différentes ?", T2, [T3, T4, T5], pos=0)),
    }
    d["e4-4"] = {
        "lieutenant": {
            "type": "plan", "titre": "L'établi de Nadia", "colonnes": 2,
            "cases": [{"libelle": "Bac E : clous en acier et bouchons de liège", "reponse": "l'aimant"}, {"libelle": "Bac F : riz et gros gravier", "reponse": "le tamis"},
                      {"libelle": "Bac G : copeaux de bois et gravier", "reponse": "la bassine d'eau"}, {"libelle": "Bac H : perles rouges et perles bleues", "reponse": "les mains"}],
            "etiquettes": ["l'aimant", "le tamis", "la bassine d'eau", "les mains", "le filtre", "la balance"],
            "consigne": "Nadia prépare quatre autres bacs. Pose sur chaque bac l'outil qui permet de séparer son contenu. Deux étiquettes ne servent à rien. Puis choisis la phrase de la fiche qui justifie le bac F.",
            "indices": ["Le filtre et la balance ne séparent pas des solides secs.", "Les clous sont en acier.", "Le riz et le gravier n'ont pas la même taille."],
            "justification": J("Quelle phrase de la fiche justifie le bac F ?", T2, [T3, T4, T5], pos=2)},
        "second": ordre(
            "Nadia veut séparer un mélange de limaille de fer, de sable fin et de gravier. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche qui justifie qu'on passe d'abord l'aimant.",
            ["Observer : on distingue trois constituants.", "Passer l'aimant : on retire la limaille de fer.", "Verser le reste sur un tamis.", "Secouer : le sable passe, le gravier reste dans le tamis.", "Peser chaque constituant pour comparer avec la masse du départ."],
            ["On observe avant d'agir.", "L'aimant ne gêne pas le tamis, mais le tamis ne sépare pas le fer du sable.", "On vérifie à la fin."],
            J("Quelle phrase de la fiche justifie qu'on passe d'abord l'aimant ?", T6, [T2, T1, T7], pos=0)),
    }
    return d
