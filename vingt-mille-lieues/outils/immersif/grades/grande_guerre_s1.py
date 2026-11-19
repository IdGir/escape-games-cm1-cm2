"""Lettre 1 « La place du village » (août 1914) : grades mousse, lieutenant, second (fiche : 1914, l'entrée en guerre)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "grande-guerre", "tests", "donnees"))
from fiches import *

FICHE = "« 1914 : l'entrée en guerre »"


def donnees(svg, bloc=None):
    d = {}
    d["e1-1"] = {
        "mousse": ordre(
            "Les événements de l'été 1914 sont mélangés. Remets-les dans l'ordre, du premier au dernier.",
            [("l'attentat de Sarajevo", "en juin"), ("l'affiche de la mobilisation", "début août"), ("le départ de Louis", "début août")],
            ["Ouvre la fiche " + FICHE + ".", "Tout commence par un attentat.", "Louis part après l'affiche."]),
        "lieutenant": ordre(
            "Jeanne a recopié des dates dans son cahier, dans le désordre. Remets-les dans l'ordre chronologique, puis choisis la phrase de la fiche qui explique comment la crise s'étend.",
            [("l'attentat de Sarajevo", "28 juin 1914"), ("l'Autriche-Hongrie déclare la guerre à la Serbie", "28 juillet 1914"),
             ("l'affiche de la mobilisation générale", "1er août 1914"), ("le premier jour de la mobilisation", "2 août 1914"),
             ("l'Allemagne déclare la guerre à la France", "3 août 1914")],
            ["Un mois sépare Sarajevo de la déclaration de guerre à la Serbie.", "L'affiche est collée la veille du premier jour.", "Pour la justification : cherche « les uns après les autres »."],
            J("Quelle phrase de la fiche explique comment une crise locale devient une guerre mondiale ?", C_ENGRE, [C_RIVAL, C_SARA, C_COURTE], pos=1)),
        "second": ordre(
            "Remets dans l'ordre ces étapes, des causes lointaines jusqu'à l'entrée en guerre de la France, puis choisis la phrase de la fiche sur l'Alsace et la Moselle.",
            [("la guerre de 1870 : l'Alsace et la Moselle deviennent allemandes", "1871"), ("les deux alliances se forment", "fin du XIXe et début du XXe siècle"),
             ("l'attentat de Sarajevo", "28 juin 1914"), ("la mobilisation générale en France", "1er-2 août 1914"), ("l'Allemagne déclare la guerre à la France", "3 août 1914")],
            ["La cause la plus ancienne remonte à 1870.", "Les alliances existent avant l'attentat.", "Pour la justification : cherche « 1870 »."],
            J("Quelle phrase de la fiche parle d'une cause ancienne de rivalité entre la France et l'Allemagne ?", C_ALSACE, [C_ALLI, C_RIVAL, C_DECLA], pos=0)),
    }
    d["e1-2"] = {
        "mousse": qcm(
            "Jeanne lit l'affiche de la mairie. Réponds à ses questions.",
            [("Que demande l'affiche ?", ["de rejoindre l'armée", "d'aller à l'école", "de fêter un mariage"], 0, "C'est la mobilisation générale."),
             ("Les grands pensent que la guerre sera…", ["courte", "très longue", "joyeuse"], 0, "Elle durera plus de quatre ans.")],
            ["Ouvre la fiche " + FICHE + ".", "Mobiliser, c'est appeler les soldats.", "Tout le monde pense rentrer vite."]),
        "lieutenant": qcm(
            "Jeanne compare l'affiche avec ce que disent les grands. Réponds, puis choisis la phrase de la fiche qui donne le nombre de mobilisés.",
            [("Le premier jour de la mobilisation est…", ["le 1er août 1914", "le 2 août 1914", "le 3 août 1914", "le 28 juin 1914"], 1, "L'affiche est collée la veille, le 1er août."),
             ("Combien de Français sont mobilisés pendant toute la guerre ?", ["800 000", "3,6 millions", "8,7 millions", "40 millions"], 2, "8,7 millions de 1914 à 1918."),
             ("Qui déclare la guerre à la France le 3 août 1914 ?", ["la Russie", "le Royaume-Uni", "l'Allemagne", "la Serbie"], 2, "L'Allemagne."),
             ("Pourquoi le Royaume-Uni entre-t-il en guerre ?", ["parce que l'armée allemande traverse la Belgique, pays neutre", "parce que la Serbie l'attaque", "pour prendre l'Alsace", "parce que la Russie l'attaque"], 0, "La Belgique était neutre.")],
            ["Le premier jour : un dimanche.", "8,7 millions sur toute la guerre.", "Pour la justification : cherche « 8,7 millions »."],
            J("Quelle phrase de la fiche donne le nombre de Français mobilisés ?", C_NOMBRE, [C_MOBIL, C_DECLA, C_COURTE], pos=2)),
        "second": assoc(
            "Jeanne a mélangé les dates et les événements de l'été 1914. Relie chaque date à son événement, puis choisis la phrase de la fiche sur l'entrée en guerre du Royaume-Uni.",
            [("28 juin 1914", "l'attentat de Sarajevo"), ("28 juillet 1914", "l'Autriche-Hongrie déclare la guerre à la Serbie"), ("1er août 1914", "l'affiche de la mobilisation est collée"),
             ("2 août 1914", "le premier jour de la mobilisation"), ("3 août 1914", "l'Allemagne déclare la guerre à la France")],
            ["Sarajevo et la Serbie : à un mois d'écart.", "Affiche la veille, mobilisation le lendemain.", "Pour la justification : cherche « Belgique »."],
            J("Quelle phrase de la fiche explique l'entrée en guerre du Royaume-Uni ?", C_BELGIQUE, [C_ENGRE, C_ALLI, C_SERBIE], pos=3)),
    }
    d["e1-3"] = {
        "mousse": tri(
            "Range chaque pays dans son camp.",
            [("entente", "Avec la France"), ("allem", "Avec l'Allemagne")],
            [("le Royaume-Uni", "entente"), ("la Russie", "entente"), ("l'Autriche-Hongrie", "allem")],
            ["Ouvre la fiche " + FICHE + ".", "La France a deux grands alliés.", "L'Autriche-Hongrie est avec l'Allemagne."]),
        "lieutenant": tri(
            "Louis a noté pourquoi chaque pays entre en guerre. Range chaque pays dans son camp, puis choisis la phrase de la fiche qui décrit les alliances.",
            [("entente", "Le camp de la France"), ("allem", "Le camp de l'Allemagne")],
            [("la Russie, alliée de la Serbie", "entente"), ("le Royaume-Uni, après l'invasion de la Belgique", "entente"), ("la Serbie, attaquée en juillet 1914", "entente"),
             ("l'Autriche-Hongrie, après Sarajevo", "allem"), ("l'Empire ottoman, à l'automne 1914", "allem"), ("l'Allemagne, alliée de l'Autriche-Hongrie", "allem")],
            ["La Russie soutient la Serbie.", "L'Allemagne soutient l'Autriche-Hongrie.", "Pour la justification : cherche « Triple-Entente »."],
            J("Quelle phrase de la fiche décrit les deux alliances ?", C_ALLI, [C_RIVAL, C_ENGRE, C_ALSACE], pos=0)),
        "second": qcm(
            "Louis cherche à comprendre l'enchaînement de 1914. Réponds, puis choisis la phrase de la fiche sur les rivalités.",
            [("Pourquoi un attentat à Sarajevo entraîne-t-il la France dans la guerre ?", ["parce que la France est alliée de la Serbie", "à cause du jeu des alliances qui entraîne les pays les uns après les autres", "parce que l'attentat a lieu en France", "parce que la France le décide seule"], 1, "La Russie soutient la Serbie, la France est alliée de la Russie."),
             ("Que se disputent les grandes puissances avant 1914 ?", ["des territoires, des colonies et des marchés", "des équipes de football", "des écoles", "rien du tout"], 0, "Ce sont des rivalités."),
             ("Qui commet l'attentat de Sarajevo ?", ["un soldat français", "un jeune nationaliste serbe", "un espion russe", "l'empereur d'Allemagne"], 1, "L'archiduc François-Ferdinand est assassiné."),
             ("Après la mobilisation, combien d'hommes compte l'armée française en 1914 ?", ["800 000", "près de 3,6 millions", "8,7 millions", "1,4 million"], 1, "Elle passe de 800 000 à près de 3,6 millions.")],
            ["Les alliances sont comme des dominos.", "Territoires, colonies, marchés.", "Pour la justification : cherche « rivales »."],
            J("Quelle phrase de la fiche décrit les rivalités entre puissances ?", C_RIVAL, [C_ALLI, C_ALSACE, C_ENGRE], pos=1)),
    }
    d["e1-4"] = {
        "lieutenant": vf(
            "Une carte postale de 1914 montre des soldats souriants. Légende ou réalité ? Choisis vrai ou faux, puis la phrase de la fiche qui répond.",
            [("La plupart des soldats partent avec résignation et sens du devoir.", True, "Pas dans la joie."),
             ("Les cartes postales montrent toujours la réalité.", False, "Elles embellissent : c'est de la propagande."),
             ("En 1914, on pense que la guerre sera courte.", True, "Elle durera plus de quatre ans."),
             ("La guerre est finie avant Noël 1914.", False, "Elle dure jusqu'en novembre 1918."),
             ("Beaucoup de Français veulent retrouver l'Alsace et la Moselle.", True, "Perdues après 1870.")],
            ["Une image peut mentir.", "Résignation : on accepte sans joie.", "Pour la justification : cherche « légende »."],
            J("Quelle phrase de la fiche dit si « la fleur au fusil » est vraie ?", C_FLEUR, [C_COURTE, C_MOBIL, C_NOMBRE], pos=0)),
        "second": tri(
            "Range chaque idée sur le départ des soldats en 1914 : légende de la propagande, ou réalité vérifiée par les historiens. Puis choisis la phrase de la fiche sur la durée attendue de la guerre.",
            [("legende", "Légende"), ("realite", "Réalité")],
            [("tous partent en chantant de joie", "legende"), ("la fleur au fusil", "legende"), ("la guerre durera quelques semaines", "legende"),
             ("ils partent avec résignation et sens du devoir", "realite"), ("l'armée passe à près de 3,6 millions d'hommes", "realite"), ("la guerre durera plus de quatre ans", "realite")],
            ["La propagande embellit.", "Ce qu'on croyait n'est pas ce qui est arrivé.", "Pour la justification : cherche « quatre ans »."],
            J("Quelle phrase de la fiche compare la durée attendue et la durée réelle ?", C_COURTE, [C_FLEUR, C_NOMBRE, C_DECLA], pos=2)),
    }
    return d
