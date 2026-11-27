"""Séance 12 « L heure du ravitaillement » : grades mousse, lieutenant, second (fiche : Les kilomètres alimentaires)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "mission-geo", "tests", "donnees"))
from fiches import *
import schemas as S

FICHE = "« Les kilomètres alimentaires »"
KM = tableau("Distance jusqu'en France (en kilomètres)", ["Chili", "Grèce", "Espagne", "Turquie", "Maroc"], [["11 702", "2 585", "1 013", "3 422", "2 292"]])


def donnees(svg, bloc=None):
    d = {}
    d["e12-1"] = {
        "mousse": tri(
            "Yanis te montre les étiquettes du marché. Range chaque produit selon le continent d'où il vient.",
            [("eu", "Europe"), ("af", "Afrique"), ("as", "Amérique du Sud")],
            [("Fraises (Espagne)", "eu"), ("Feta (Grèce)", "eu"), ("Bananes (Cameroun)", "af"), ("Tomates (Maroc)", "af"), ("Poires (Chili)", "as"), ("Mangues (Brésil)", "as")],
            ["Ouvre la fiche " + FICHE + ".", "L'Espagne et la Grèce sont en Europe.", "Le Chili et le Brésil sont en Amérique du Sud."]),
        "lieutenant": ordre(
            "Yanis veut savoir quel ingrédient de sa salade vient de plus près. Range-les du plus proche au plus lointain, puis choisis la phrase de la fiche qui définit les kilomètres alimentaires." + KM,
            ["la salade d'Espagne", "les tomates du Maroc", "la feta de Grèce", "les noisettes de Turquie", "la poire du Chili"],
            ["Compare les nombres de kilomètres.", "L'Espagne est le pays le plus proche.", "Pour la justification : cherche « distance totale parcourue »."],
            J("Quelle phrase de la fiche définit les kilomètres alimentaires ?", K_KM, [K_CO2, K_ORIGINES, K_CIRCUIT], pos=1)),
        "second": assoc(
            "Yanis lit les étiquettes d'origine. Relie chaque produit à son pays d'origine, puis choisis la phrase de la fiche qui les cite.",
            [("les kiwis", "la Nouvelle-Zélande"), ("les bananes", "le Cameroun"), ("les poires", "le Chili"), ("les noisettes", "la Turquie"), ("la feta", "la Grèce"), ("les mangues", "le Brésil")],
            ["Les kiwis viennent de l'autre bout du monde.", "Les mangues poussent en Amérique du Sud.", "Pour la justification : cherche « origines très variées »."],
            J("Quelle phrase de la fiche cite des produits et leurs pays d'origine ?", K_ORIGINES, [K_KM, K_CIRCUIT, K_LOCAL], pos=0)),
    }
    d["e12-2"] = {
        "mousse": code(
            "Yanis a additionné les kilomètres alimentaires de sa salade fraîcheur : 21 014 km. Lis bien ce nombre.",
            [("Chiffre des unités de 21 014", "4", 1), ("Chiffre des milliers de 21 014", "1", 1)],
            ["Ouvre la fiche " + FICHE + ".", "Le chiffre des unités est le dernier chiffre.", "Le chiffre des milliers est le deuxième en partant de la gauche."]),
        "lieutenant": qcm(
            "Yanis cherche comment réduire les kilomètres alimentaires. Réponds, puis choisis la phrase de la fiche sur le circuit court.",
            [("Que veut dire « circuit court » ?", ["une vente directe, ou avec un seul intermédiaire, entre le producteur et le consommateur", "un trajet de moins d'un kilomètre", "un petit supermarché", "un camion plus rapide"], 0,
              "Moins d'intermédiaires, moins de transport."),
             ("Pourquoi les kilomètres alimentaires posent-ils un problème ?", ["le transport rejette du CO₂", "les aliments perdent leur couleur", "les étiquettes deviennent illisibles", "les camions sont trop lents"], 0, "Le CO₂ contribue au réchauffement climatique."),
             ("Lequel de ces gestes n'a aucun effet sur les kilomètres alimentaires ?", ["manger moins salé", "acheter local", "choisir des produits de saison", "acheter en circuit court"], 0, "Le sel n'a aucun rapport avec la distance.")],
            ["Un seul intermédiaire au plus.", "Le transport rejette du gaz.", "Pour la justification : cherche « directement au producteur »."],
            J("Quelle phrase de la fiche parle du circuit court ?", K_CIRCUIT, [K_LOCAL, K_SANS, K_CO2], pos=0)),
        "second": vf(
            "Yanis te présente des idées reçues. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui dit ce qui n'a aucun effet.",
            [("Acheter en circuit court réduit les kilomètres alimentaires.", True, "Moins d'intermédiaires, moins de transport."),
             ("Ne pas laver ses fruits réduit les kilomètres alimentaires.", False, "Cela n'a aucun effet sur la distance parcourue."),
             ("Manger moins salé n'a aucun effet sur les kilomètres alimentaires.", True, "Le sel n'a aucun rapport avec la distance."),
             ("Plus la distance est grande, moins le transport rejette de CO₂.", False, "Plus la distance est grande, plus il y a de CO₂."),
             ("Choisir des fruits de saison peut réduire les kilomètres alimentaires.", True, "Un produit de saison vient plus souvent de près.")],
            ["Le sel et le lavage n'ont aucun rapport avec la distance.", "Plus on va loin, plus on pollue.", "Pour la justification : cherche « aucun effet »."],
            J("Quelle phrase de la fiche dit ce qui n'a aucun effet sur les kilomètres alimentaires ?", K_SANS, [K_CIRCUIT, K_LOCAL, K_CO2], pos=3)),
    }
    d["e12-3"] = {
        "mousse": vf(
            "Yanis te pose trois questions. Pour chaque phrase, choisis vrai ou faux.",
            [("Un aliment qui vient de loin a parcouru beaucoup de kilomètres.", True, "On parle de kilomètres alimentaires."),
             ("Le transport des aliments rejette du CO₂.", True, "Ce gaz contribue au réchauffement climatique."),
             ("Ne pas laver ses fruits réduit les kilomètres alimentaires.", False, "Cela n'a aucun effet.")],
            ["Ouvre la fiche " + FICHE + ".", "Loin, ça veut dire beaucoup de kilomètres.", "Laver un fruit ne change pas la distance."]),
        "lieutenant": tri(
            "Yanis classe les produits du marché par continent. Range-les, puis choisis la phrase de la fiche qui cite les origines des produits.",
            [("eu", "Europe"), ("af", "Afrique"), ("as", "Amérique du Sud"), ("asie", "Asie"), ("oc", "Océanie")],
            [("Fraises (Espagne)", "eu"), ("Feta (Grèce)", "eu"), ("Bananes (Cameroun)", "af"), ("Oranges (Afrique du Sud)", "af"), ("Citrons (Argentine)", "as"), ("Poires (Chili)", "as"),
             ("Noisettes (Turquie)", "asie"), ("Kiwis (Nouvelle-Zélande)", "oc")],
            ["La Turquie se trouve surtout en Asie.", "La Nouvelle-Zélande est en Océanie.", "Pour la justification : cherche « myrtilles du Portugal »."],
            J("Quelle phrase de la fiche cite les origines des produits d'un supermarché ?", K_ORIGINES, [K_KM, K_CIRCUIT, K_LOCAL], pos=3)),
        "second": tri(
            "Yanis te propose des gestes. Range chacun selon son effet sur les kilomètres alimentaires, puis choisis la phrase de la fiche qui cite les gestes efficaces.",
            [("oui", "Réduit les kilomètres alimentaires"), ("non", "N'a aucun effet")],
            [("Acheter en circuit court", "oui"), ("Choisir des produits locaux", "oui"), ("Choisir des fruits et des légumes de saison", "oui"), ("Manger moins de viande", "oui"),
             ("Manger moins salé", "non"), ("Ne pas laver ses fruits", "non")],
            ["Le sel et le lavage n'ont aucun effet.", "Local et de saison : moins de transport.", "Pour la justification : cherche « manger moins de viande »."],
            J("Quelle phrase de la fiche cite des gestes qui réduisent les kilomètres ?", K_LOCAL, [K_CIRCUIT, K_SANS, K_CO2], pos=1)),
    }
    d["e12-4"] = {
        "lieutenant": code(
            "Yanis prépare une autre salade : 1 poire (Chili), 100 g de feta (Grèce) et 200 g de tomates (Maroc). Calcule, puis choisis la phrase de la fiche qui explique pourquoi la distance compte." + KM,
            [("Total des kilomètres alimentaires de cette salade", "16579", 5), ("Chiffre des dizaines de ce total", "7", 1)],
            ["11 702 + 2 585 + 2 292.", "Le chiffre des dizaines est l'avant-dernier chiffre.", "Pour la justification : cherche « rejette de CO₂ »."],
            J("Quelle phrase de la fiche explique pourquoi la distance compte ?", K_CO2, [K_KM, K_LOCAL, K_SANS], pos=2)),
        "second": code(
            "Imagine que Yanis remplace la poire du Chili de la salade fraîcheur (1 poire du Chili, 100 g de feta de Grèce, 1 salade d'Espagne, 100 g de noisettes de Turquie, 200 g de tomates du Maroc) "
            "par une pomme de saison produite à 300 km. Calcule, puis choisis la phrase de la fiche qui recommande les produits locaux." + KM,
            [("Total initial des kilomètres alimentaires", "21014", 5), ("Kilomètres économisés", "11402", 5), ("Nouveau total", "9612", 4)],
            ["11 702 + 2 585 + 1 013 + 3 422 + 2 292.", "11 702 − 300.", "Le total initial moins les kilomètres économisés. Pour la justification : cherche « produits locaux »."],
            J("Quelle phrase de la fiche recommande les produits locaux ?", K_LOCAL, [K_KM, K_CIRCUIT, K_CO2], pos=0)),
    }
    return d
