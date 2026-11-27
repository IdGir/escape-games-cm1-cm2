"""Séance 9 « Les pratiques alimentaires » : grades mousse, lieutenant, second (fiche : Se nourrir ici et ailleurs)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "mission-geo", "tests", "donnees"))
from fiches import *
import schemas as S

FICHE = "« Se nourrir ici et ailleurs »"
PRIX_LOCAUX = tableau("Prix au kilo des produits locaux du marché de Bamako (en euros)", ["Gombo", "Millet", "Arachides", "Riz", "Haricots", "Mangue"],
                      [["1,22", "0,76", "1,52", "0,91", "1,37", "1,06"]])
PRIX_IMPORT = tableau("Prix au marché de Bamako (en euros)", ["Produit", "Prix"],
                      [["Millet (1 kg)", "0,76"], ["Pâtes importées (1 kg)", "3,81"], ["Fromage importé (100 g)", "2,29"], ["Yaourt importé (1 pot)", "1,22"]])


def donnees(svg, bloc=None):
    d = {}
    d["e9-1"] = {
        "mousse": tri(
            "Aminata a mélangé le contenu de deux frigos. Range chaque aliment dans le bon frigo.",
            [("fr", "Le frigo en France"), ("ml", "Le frigo au Mali")],
            [("Pain de mie", "fr"), ("Fromage", "fr"), ("Yaourt", "fr"), ("Millet", "ml"), ("Arachides", "ml"), ("Mangue", "ml")],
            ["Ouvre la fiche " + FICHE + ".", "Au Mali, on mange ce qui est produit sur place.", "Le fromage et le yaourt sont importés au Mali : ils sont rares et chers."]),
        "lieutenant": ordre(
            "Aminata relève les prix au kilo des produits locaux du marché de Bamako. Range-les du moins cher au plus cher, puis choisis la phrase de la fiche qui dit ce que l'on mange surtout au Mali." + PRIX_LOCAUX,
            ["le millet", "le riz", "la mangue", "le gombo", "les haricots", "les arachides"],
            ["Le millet coûte le moins : 0,76 €.", "Les arachides coûtent le plus : 1,52 €.", "Pour la justification : cherche « produit sur place »."],
            J("Quelle phrase de la fiche dit ce que l'on mange surtout au Mali ?", P_MALI, [P_IMPORT, P_FRIGO, P_BUDGET], pos=1)),
        "second": tri(
            "Aminata classe les causes de ce que tu vois au marché. Range chaque cause selon son origine, puis choisis la phrase de la fiche sur le réfrigérateur.",
            [("geo", "La géographie et le climat"), ("rev", "Les revenus"), ("con", "La conservation des aliments")],
            [("Pas d'accès à la mer", "geo"), ("Saison des pluies courte", "geo"), ("Climat chaud et sec", "geo"), ("Les produits importés coûtent très cher", "rev"),
             ("Un budget de moins de 10 € pour la semaine", "rev"), ("Peu de familles ont un réfrigérateur", "con"), ("La viande et le poisson se gâtent vite", "con")],
            ["Le Mali est enclavé : il n'a pas de côte.", "Le prix des produits importés relève des revenus.", "Pour la justification : cherche « réfrigérateur »."],
            J("Quelle phrase de la fiche parle du réfrigérateur ?", P_FRIGO, [P_MALI, P_BUDGET, P_ENCLAVE], pos=2)),
    }
    d["e9-2"] = {
        "mousse": vf(
            "Aminata te raconte ce qu'elle a vu au marché. Pour chaque phrase, choisis vrai ou faux.",
            [("Au Mali, on mange surtout ce qui est produit sur place.", True, "Le millet, le riz et la mangue poussent là-bas."),
             ("Les pâtes importées coûtent moins cher que le millet.", False, "Un kilo de pâtes importées vaut environ cinq fois le prix d'un kilo de millet."),
             ("Au Mali, presque toutes les familles ont un réfrigérateur.", False, "Peu de familles en possèdent un.")],
            ["Ouvre la fiche " + FICHE + ".", "Ce qui vient de loin coûte plus cher.", "Sans réfrigérateur, la viande ne se garde pas."]),
        "lieutenant": trous(
            "Complète le carnet d'Aminata (deux mots sont des intrus), puis choisis la phrase de la fiche qui dit de quoi dépendent les pratiques alimentaires.",
            "Au Mali, on mange surtout ce qui est [[produit]] sur place : le [[millet]], le riz, les [[arachides]]. Les aliments [[importés]] coûtent très cher.",
            ["produit", "millet", "arachides", "importés", "congelés", "gratuits"],
            ["Les produits importés viennent d'un autre pays.", "Le millet et les arachides poussent sur place.", "Pour la justification : cherche « surtout des revenus »."],
            J("Quelle phrase de la fiche dit de quoi dépendent les pratiques alimentaires ?", P_PRATIQUES, [P_SOUS, P_BUDGET, P_FRIGO], pos=2)),
        "second": qcm(
            "Aminata prépare son rapport. Réponds à ses questions, puis choisis la phrase de la fiche qui cite les pays touchés par la sous-alimentation.",
            [("Qu'est-ce que la sous-alimentation ?", ["ne pas manger assez pour couvrir ses besoins", "manger trop de sucre", "ne manger que des produits importés", "manger uniquement du poisson"], 0,
              "C'est manger trop peu pour couvrir ses besoins."),
             ("Quelle région du monde est surtout touchée par la sous-alimentation ?", ["l'Afrique subsaharienne", "l'Europe de l'Ouest", "l'Océanie", "le Japon"], 0, "Comme le Tchad, le Soudan et Madagascar."),
             ("Quelle part de la population française est sous-alimentée ?", ["moins de 2,5 %", "environ 25 %", "la moitié", "un tiers"], 0, "Moins de 2,5 %, comme aux États-Unis."),
             ("Que montre la comparaison des budgets (25 € en France, moins de 10 € au Mali) ?", ["les revenus influencent beaucoup ce que l'on mange", "tout le monde mange la même chose", "le Mali est plus riche que la France", "le prix n'a aucun effet"], 0,
              "Les pratiques alimentaires dépendent surtout des revenus.")],
            ["La sous-alimentation, c'est manger trop peu.", "Le Tchad et Madagascar sont en Afrique.", "Pour la justification : cherche « Soudan »."],
            J("Quelle phrase de la fiche cite les pays touchés par la sous-alimentation ?", P_ZONES, [P_SOUS, P_FRANCE, P_PRATIQUES], pos=3)),
    }
    d["e9-3"] = {
        "mousse": qcm(
            "Aminata compare des prix. Un kilo de pâtes importées coûte 3,81 € et un kilo de millet 0,76 €.",
            [("Quel produit coûte le moins cher ?", ["le millet", "les pâtes importées", "le même prix"], 0, "0,76 € est plus petit que 3,81 €."),
             ("La famille A (France) a 25 € et la famille C (Mali) a 8 €. Quelle famille a le plus d'argent ?", ["la famille A", "la famille C", "la même somme"], 0, "25 € est plus grand que 8 €.")],
            ["Ouvre la fiche " + FICHE + ".", "Compare 3,81 et 0,76.", "Compare 25 et 8."]),
        "lieutenant": code(
            "La famille C (8 €) achète 1 kg de pâtes importées, 100 g de fromage importé et 1 yaourt importé. Calcule en centimes (1 € = 100 centimes), puis choisis la phrase de la fiche qui compare les pâtes importées et le millet." + PRIX_IMPORT,
            [("Dépense de la famille C (centimes)", "732", 3), ("Il lui reste sur 8 € (centimes)", "68", 2), ("Kilos de millet pour 8 € (nombre entier)", "10", 2)],
            ["381 + 229 + 122.", "800 moins la dépense.", "800 ÷ 76, en gardant les kilos entiers. Pour la justification : cherche « cinq fois »."],
            J("Quelle phrase de la fiche compare le prix des pâtes importées et celui du millet ?", P_IMPORT, [P_MALI, P_BUDGET, P_SOUS], pos=2)),
        "second": code(
            "Un kilo de pâtes importées (3,81 €), 100 g de fromage importé (2,29 €) et un yaourt importé (1,22 €) : calcule en centimes ce que dépense la famille C (8 €), puis compare avec la famille A (25 €). "
            "Choisis ensuite la phrase de la fiche qui parle de ces budgets.",
            [("Dépense de la famille C (centimes)", "732", 3), ("Il lui reste sur 8 € (centimes)", "68", 2), ("Euros de plus pour la famille A que pour la famille C", "17", 2),
             ("La famille A est environ … fois plus riche (arrondi à l'unité)", "3", 1)],
            ["381 + 229 + 122.", "25 − 8.", "25 ÷ 8 donne un peu plus de 3. Pour la justification : cherche « 25 € »."],
            J("Quelle phrase de la fiche compare les budgets de la France et du Mali ?", P_BUDGET, [P_IMPORT, P_FRIGO, P_MALI], pos=0)),
    }
    d["e9-4"] = {
        "lieutenant": tri(
            "Aminata te donne des pays. Range chacun selon la part de sa population qui ne mange pas assez, puis choisis la phrase de la fiche sur la France et les États-Unis.",
            [("fa", "Moins de 2,5 % de la population"), ("fo", "Beaucoup plus de personnes touchées")],
            [("la France", "fa"), ("les États-Unis", "fa"), ("le Tchad", "fo"), ("Madagascar", "fo"), ("Haïti", "fo"), ("le Soudan", "fo")],
            ["Deux pays riches, quatre pays où la sous-alimentation est forte.", "Haïti est une île des Caraïbes.", "Pour la justification : cherche « moins de 2,5 % »."],
            J("Quelle phrase de la fiche parle de la France et des États-Unis ?", P_FRANCE, [P_ZONES, P_SOUS, P_BUDGET], pos=1)),
        "second": {"type": "plan", "titre": "Le planisphère d'Aminata", "colonnes": 2,
                   "cases": [{"libelle": f"Repère {i + 1}", "reponse": S.PAYS9[i][0]} for i in range(5)],
                   "etiquettes": [p[0] for p in S.PAYS9] + ["L'Inde"],
                   "consigne": "Place les cinq pays sur leur repère (une étiquette est en trop), puis choisis la phrase de la fiche qui cite des pays où la sous-alimentation est forte." + S.pays9(range(5)),
                   "indices": ["L'Inde est en Asie : aucun repère n'y est placé.", "Haïti est une île, à l'est de l'Amérique centrale.", "Pour la justification : cherche « Madagascar »."],
                   "justification": J("Quelle phrase de la fiche cite des pays où la sous-alimentation est forte ?", P_ZONES, [P_FRANCE, P_SOUS, P_MALI], pos=2)},
    }
    return d
