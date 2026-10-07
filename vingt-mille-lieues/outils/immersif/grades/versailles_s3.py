"""Salle 3 « Les jardins de Versailles » (fiche : chateau-versailles)."""
from aide import *

F = "« Versailles, le château du Roi-Soleil »"
V1 = "Louis XIV agrandit le pavillon de chasse de son père, Louis XIII. L'architecte Louis Le Vau commence les travaux, poursuivis par Jules Hardouin-Mansart."
V2 = "Le peintre Charles Le Brun dirige les décors ; André Le Nôtre dessine les jardins. Le ministre Colbert surveille les travaux et les dépenses."
V3 = "Le 6 mai 1682, le roi s'installe à Versailles avec la cour et le gouvernement."
V4 = "Construite de 1678 à 1684 par Hardouin-Mansart, elle mesure 73 mètres. Ses 357 miroirs font face aux 17 fenêtres qui donnent sur les jardins."
V5 = "Au plafond, trente tableaux de Le Brun racontent les victoires et le gouvernement du roi."
V6 = "Le Nôtre organise les jardins selon un grand axe : parterres, bosquets, bassins, jusqu'au Grand Canal en forme de croix."
V7 = "Au bout de l'allée royale, le bassin d'Apollon montre le dieu du Soleil sur son char."
V8 = "Le Soleil et Apollon, dieu grec de la lumière et des arts, sont partout : Versailles est une immense image du pouvoir du roi."


def donnees(svg, bloc=None):
    d = {}
    d["e3-1"] = {
        "mousse": assoc(
            "Margot montre le plan du domaine, vu de dessus. Regarde le plan, puis relie chaque nom à ce qu'il désigne. Clique sur un nom, puis sur sa description.\n" + svg("e3-1", "matelot"),
            [("le château", "le grand bâtiment où vit le roi"), ("la galerie des Glaces", "la longue salle dorée côté jardins"), ("le Grand Canal", "le plan d'eau en forme de croix")],
            ["Ouvre la fiche " + F + " dans la Bibliothèque.", "Le château est entre la ville et les jardins.", "Le Grand Canal est un plan d'eau en forme de croix."]),
        "lieutenant": qcm(
            "Margot déplie le plan du domaine, vu de dessus (repères 1 à 6). Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 3." + svg("e3-1", "timonier"),
            [("Quel repère montre le bassin d'Apollon ?", ["Le repère 5", "Le repère 6", "Le repère 3", "Le repère 1"], 0, "Il est au bout de l'allée royale."),
             ("Quel repère montre la galerie des Glaces ?", ["Le repère 2", "Le repère 3", "Le repère 4", "Le repère 6"], 0, "La longue salle dorée."),
             ("Quel est l'axe organisateur des jardins ?", ["Un grand axe qui va jusqu'au Grand Canal", "Des chemins sans ordre", "Un labyrinthe", "Des ruelles"], 0, "Jardins à la française.")],
            ["Le bassin d'Apollon est ovale.", "La galerie est côté jardins.", "Pense au mot « axe »."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 3 ?", V6, [V7, V4, V2], pos=1)),
        "second": vf(
            "Margot a noté six phrases sur le chantier de Versailles. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui date l'installation de la cour.",
            [("Louis XIV agrandit le pavillon de chasse de son père, Louis XIII.", True, "C'est le point de départ."), ("Le Nôtre dessine les jardins.", True, "Comme Le Brun dirige les décors."), ("Colbert dessine les jardins.", False, "Il surveille les dépenses."),
             ("La cour s'installe à Versailles le 6 mai 1682.", True, "Avec le gouvernement."), ("La galerie des Glaces est construite de 1678 à 1684.", True, "Par Hardouin-Mansart."), ("Louis Le Vau termine la galerie des Glaces.", False, "Hardouin-Mansart.")],
            ["Le Vau commence, Hardouin-Mansart poursuit.", "Colbert surveille.", "1682 : la cour s'installe."],
            J("Quelle phrase de la fiche date l'installation de la cour ?", V3, [V1, V4, V2], pos=1)),
    }
    d["e3-2"] = {
        "mousse": tri(
            "Range chaque personne dans le bon métier : clique sur une carte, puis sur une colonne.",
            [("jardin", "Dessine les jardins"), ("peinture", "Dirige les décors et peint")],
            [("André Le Nôtre", "jardin"), ("Un jardinier du roi", "jardin"), ("Charles Le Brun", "peinture"), ("Un peintre de la galerie", "peinture")],
            ["Ouvre la fiche " + F + ".", "Le Nôtre dessine les jardins.", "Le Brun dirige les décors."]),
        "lieutenant": tri(
            "Margot classe les personnes qui ont travaillé à Versailles. Range chaque personne dans la bonne colonne, puis choisis la phrase de la fiche qui énumère leurs rôles.",
            [("archi", "Bâtiments"), ("deco", "Décors et jardins"), ("compte", "Dépenses")],
            [("Louis Le Vau", "archi"), ("Jules Hardouin-Mansart", "archi"), ("Charles Le Brun", "deco"), ("André Le Nôtre", "deco"), ("Colbert", "compte"), ("Le ministre qui surveille les travaux", "compte")],
            ["Un architecte dessine les bâtiments.", "Le Brun et Le Nôtre : décors et jardins.", "Colbert surveille les dépenses."],
            J("Quelle phrase de la fiche énumère les rôles des artistes et du ministre ?", V2, [V1, V3, V5], pos=1)),
        "second": ordre(
            "Margot retrace le chantier. Remets ces cinq repères dans l'ordre, puis choisis la phrase de la fiche qui date la galerie des Glaces.",
            ["Louis Le Vau commence les travaux", "Jules Hardouin-Mansart poursuit les travaux", "Début de la galerie des Glaces (1678)", "Fin de la galerie des Glaces (1684)", "Louis XIV s'installe avec la cour (1682)"],
            ["1678 vient avant 1684.", "La cour s'installe en 1682, entre les deux.", "Le Vau commence avant Hardouin-Mansart."],
            J("Quelle phrase de la fiche date la galerie des Glaces ?", V4, [V3, V1, V5], pos=0)),
    }
    d["e3-3"] = {
        "mousse": qcm(
            "Réponds à la question, puis vérifie.",
            [("Quel emblème Louis XIV choisit-il ?", ["Le Soleil", "La Lune", "Un lion"], 0, "On l'appelle le Roi-Soleil.")],
            ["Ouvre la fiche " + F + ".", "On voit souvent un visage entouré de rayons.", "Le Soleil éclaire tout."]),
        "lieutenant": vf(
            "Margot a noté cinq phrases sur le Roi-Soleil. Pour chacune, réponds « Vrai » ou « Faux », puis choisis la phrase de la fiche qui explique pourquoi le Soleil est partout.",
            [("Apollon est le dieu grec de la lumière et des arts.", True, "On le voit partout à Versailles."), ("Le bassin d'Apollon est au bout de l'allée royale.", True, "Le dieu est sur son char."), ("Louis XIV choisit la Lune comme emblème.", False, "Le Soleil."),
             ("Versailles est une image du pouvoir du roi.", True, "Une immense image."), ("Le Grand Canal a la forme d'un cercle.", False, "D'une croix.")],
            ["Le Soleil est l'emblème.", "Apollon est le dieu du Soleil.", "Le Grand Canal est en forme de croix."],
            J("Quelle phrase de la fiche explique pourquoi le Soleil est partout ?", V8, [V7, V6, V5], pos=1)),
        "second": qcm(
            carnet("Fiche sur la galerie des Glaces", "(d'après la fiche). Elle est construite de 1678 à 1684 par Hardouin-Mansart. Elle mesure 73 mètres. Ses 357 miroirs font face à 17 fenêtres. Au plafond, trente tableaux de Le Brun racontent les victoires et le gouvernement du roi.")
            + " Réponds aux trois questions, puis choisis la phrase de la fiche qui justifie la question 2.",
            [("Combien d'années dure la construction ?", ["6 ans", "4 ans", "10 ans", "56 ans"], 0, "1684 − 1678 = 6."),
             ("Que racontent les peintures du plafond ?", ["Les victoires et le gouvernement du roi", "La vie des paysans", "L'histoire de la Révolution", "Les voyages de Colbert"], 0, "Trente tableaux de Le Brun."),
             ("Combien de miroirs pour chaque fenêtre, environ ?", ["Environ 21", "Environ 2", "Environ 100", "Environ 1"], 0, "357 ÷ 17 est proche de 21.")],
            ["Soustrais 1678 de 1684.", "Les tableaux de Le Brun.", "Divise 357 par 17."],
            J("Quelle phrase de la fiche justifie ta réponse à la question 2 ?", V5, [V4, V8, V3], pos=1)),
    }
    d["e3-4"] = {
        "lieutenant": lettres(
            "Trouve le mot qui correspond à cette définition : « Grand plan d'eau en forme de croix, au bout des jardins. » Ses lettres sont cachées en couleur dans le texte de Margot, dans le désordre. Clique-les dans l'ordre qui forme le mot (5 lettres). Deux lettres sont des pièges.",
            ["C", "A", "N", "A", "L"],
            marque("Margot raconte : « Ce matin, [l]e soleil se lève sur l'eau. Le [c]hemin est long jusqu'au bout du jardin, mais je suis [a]u travail avec Le Nôtre. Il [n]ote chaque tracé ; je reste [a]ttentive. Et puis [p]etite pause : [s]ur l'herbe, quelques oiseaux. »"),
            ["Le mot a cinq lettres.", "Il commence par C et finit par L.", "Le Grand … est en forme de croix."],
            J("Quelle phrase de la fiche cite ce mot ?", V6, [V7, V4, V3], pos=2)),
        "second": lettres(
            "Trouve le mot qui correspond à cette définition : « Les 357 objets qui reflètent les jardins dans la galerie des Glaces. » Ses lettres sont cachées en couleur dans le texte de Margot, dans le désordre. Clique-les dans l'ordre qui forme le mot (7 lettres). Deux lettres sont des pièges.",
            ["M", "I", "R", "O", "I", "R", "S"],
            marque("Margot raconte : « Dans la galerie, [s]ur un côté, il y a des fenêtres, [r]épétées dix-sept fois. En face, [i]l y a des centaines de reflets. Le roi [o]bserve le jardin. Je [m]arche sans bruit ; [r]ien ne bouge. Je me regarde, [o]ui, j'ai l'[i]nsouciance de mes onze ans. Qu'[a]ffreux ! [p]as un mot. »"),
            ["Le mot a sept lettres.", "Il commence par M et finit par S.", "Ils reflètent les jardins."],
            J("Quelle phrase de la fiche cite ces objets ?", V4, [V5, V8, V2], pos=2)),
    }
    return d
