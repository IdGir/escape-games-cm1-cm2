"""Séance 8 « Niveaux de vie dans le monde » : grades mousse, lieutenant, second (fiche : Les inégalités de niveau de vie)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "mission-geo", "tests", "donnees"))
from fiches import *
import schemas as S

FICHE = "« Les inégalités de niveau de vie »"


def donnees(svg, bloc=None):
    d = {}
    d["e8-1"] = {
        "mousse": {"type": "plan", "titre": "Le planisphère de Nour", "colonnes": 3,
                   "cases": [{"libelle": f"Repère {i + 1}", "reponse": S.PAYS[k][0]} for i, k in enumerate([1, 3, 4])],
                   "etiquettes": [S.PAYS[k][0] for k in (1, 3, 4)],
                   "consigne": "Place chaque pays sur son repère." + S.pays([1, 3, 4]),
                   "indices": ["Ouvre la fiche " + FICHE + ".", "Le Bangladesh est en Asie, où tu te trouves.", "L'Australie est en bas à droite."]},
        "lieutenant": assoc(
            "Nour range ses fiches de pays par continent. Relie chaque pays à son continent, puis choisis la phrase de la fiche qui dit où sont les pays les plus riches.",
            [("les États-Unis", "l'Amérique du Nord"), ("la Norvège", "l'Europe"), ("le Tchad", "l'Afrique"), ("le Bangladesh", "l'Asie"), ("l'Australie", "l'Océanie")],
            ["La Norvège est au nord de l'Europe.", "Le Tchad est au cœur de l'Afrique.", "Pour la justification : cherche « Asie de l'Est »."],
            J("Quelle phrase de la fiche dit où se trouvent les pays les plus riches ?", I_RICHES, [I_PAUVRES, I_NIVEAU, I_INDICATEURS], pos=2)),
        "second": {"type": "plan", "titre": "Le planisphère de Nour", "colonnes": 2,
                   "cases": [{"libelle": f"Repère {i + 1}", "reponse": S.PAYS[i][0]} for i in range(7)],
                   "etiquettes": [p[0] for p in S.PAYS] + ["Le Brésil"],
                   "consigne": "Place les sept pays sur leur repère (une étiquette est en trop), puis choisis la phrase de la fiche qui dit où se trouvent les pays les plus pauvres." + S.pays(range(7)),
                   "indices": ["Le Brésil est en Amérique du Sud : aucun repère n'y est placé.", "Le Mali est à l'ouest du Tchad ; le Japon, tout à l'est de l'Asie.", "Pour la justification : cherche « Asie du Sud »."],
                   "justification": J("Quelle phrase de la fiche dit où se trouvent les pays les plus pauvres ?", I_PAUVRES, [I_RICHES, I_ENFANTS, I_NIVEAU], pos=1)},
    }
    d["e8-2"] = {
        "mousse": tri(
            "Regarde les barres : une longue barre, c'est un pays riche. Range chaque pays." + S.revenus(["la Norvège", "la France", "le Tchad", "le Mali"]),
            [("r", "Pays riches"), ("p", "Pays pauvres")],
            [("la Norvège", "r"), ("la France", "r"), ("le Tchad", "p"), ("le Mali", "p")],
            ["Ouvre la fiche " + FICHE + ".", "Compare la longueur des barres.", "Deux pays riches, deux pays pauvres."]),
        "lieutenant": ordre(
            "Lis le diagramme de Nour, puis range les pays du revenu par habitant le plus élevé au plus faible. Choisis ensuite la phrase de la fiche qui compare la Norvège et le Bangladesh."
            + S.revenus(["la Norvège", "les États-Unis", "la France", "le Bangladesh", "le Tchad"]),
            ["la Norvège", "les États-Unis", "la France", "le Bangladesh", "le Tchad"],
            ["Commence par la plus longue barre.", "Le Tchad a la barre la plus courte.", "Pour la justification : cherche « 13 fois »."],
            J("Quelle phrase de la fiche compare la Norvège et le Bangladesh ?", I_ECART, [I_SEULE, I_PARTAGE, I_INDICATEURS], pos=0)),
        "second": tri(
            "Pour comparer les pays, Nour relève plusieurs mesures. Range chacune selon ce qu'elle mesure, puis choisis la phrase de la fiche qui cite les indicateurs.",
            [("ric", "La richesse"), ("san", "La santé"), ("edu", "L'éducation")],
            [("le revenu par habitant", "ric"), ("le salaire moyen", "ric"), ("l'espérance de vie", "san"), ("le nombre de médecins par habitant", "san"),
             ("la durée de la scolarisation", "edu"), ("la part des enfants qui savent lire", "edu")],
            ["L'espérance de vie dit combien de temps on vit.", "Savoir lire dépend de l'école.", "Pour la justification : cherche « plusieurs indicateurs »."],
            J("Quelle phrase de la fiche cite les indicateurs qui servent à comparer les pays ?", I_INDICATEURS, [I_NIVEAU, I_SEULE, I_ECART], pos=3)),
    }
    d["e8-3"] = {
        "mousse": vf(
            "Nour te raconte ce qu'elle a vu. Pour chaque phrase, choisis vrai ou faux.",
            [("Tout le monde a le même niveau de vie dans le monde.", False, "Il y a des pays riches et des pays pauvres."),
             ("Dans les pays pauvres, des enfants travaillent au lieu d'aller à l'école.", True, "Nour l'a vu à Dhaka."),
             ("Les pays les plus riches sont surtout en Afrique.", False, "Ils sont surtout en Amérique du Nord, en Europe et en Océanie.")],
            ["Ouvre la fiche " + FICHE + ".", "Nour a vu des enfants trier des déchets.", "L'Afrique compte beaucoup de pays pauvres."]),
        "lieutenant": trous(
            "Complète le rapport de Nour (deux mots sont des intrus), puis choisis la phrase de la fiche sur le travail des enfants.",
            "Pour comparer les pays, on utilise le [[revenu]] par habitant, l'[[espérance]] de vie et la durée de la [[scolarisation]]. "
            "En 2024, près de [[138]] millions d'enfants travaillaient dans le monde.",
            ["revenu", "espérance", "scolarisation", "138", "superficie", "13"],
            ["La superficie ne mesure pas le niveau de vie.", "138 millions, selon l'OIT et l'UNICEF.", "Pour la justification : cherche « OIT »."],
            J("Quelle phrase de la fiche parle du nombre d'enfants qui travaillent ?", I_OIT, [I_DROITS, I_ENFANTS, I_PARTAGE], pos=2)),
        "second": qcm(
            "Nour prépare son rapport pour le Professeur Atlas. Réponds à ses questions, puis choisis la phrase de la fiche sur les droits de l'enfant.",
            [("Quelle part du patrimoine mondial possèdent les 10 % les plus riches de la population ?", ["environ les trois quarts", "environ un dixième", "la moitié exactement", "presque rien"], 0,
              "Environ 76 % selon le Rapport sur les inégalités mondiales 2022."),
             ("En quelle année l'ONU a-t-elle adopté la Convention internationale des droits de l'enfant ?", ["1989", "1789", "1945", "2024"], 0, "1789, c'est la Déclaration des droits de l'homme."),
             ("Contre quoi cette convention protège-t-elle les enfants ?", ["le travail qui nuit à leur santé ou à leur éducation", "les devoirs du soir", "les vacances trop longues", "le sport à l'école"], 0,
              "Article 32 de la Convention."),
             ("Pourquoi la pauvreté se transmet-elle souvent d'une génération à l'autre ?", ["un enfant qui ne va pas à l'école trouvera plus difficilement un bon emploi", "les enfants pauvres ne grandissent pas", "l'école coûte toujours très cher", "aucune raison"], 0,
              "L'école est un moyen de sortir de la pauvreté.")],
            ["Les trois quarts, c'est 75 %.", "La Convention date de la fin du XXᵉ siècle.", "Pour la justification : cherche « 1989 »."],
            J("Quelle phrase de la fiche parle des droits de l'enfant ?", I_DROITS, [I_OIT, I_ENFANTS, I_PARTAGE], pos=1)),
    }
    d["e8-4"] = {
        "lieutenant": code(
            "Lis le tableau du PNUD, calcule, puis choisis la phrase de la fiche qui montre que la richesse ne suffit pas."
            + S.tableau_pnud(["la Norvège", "le Koweït", "la Guinée équatoriale", "le Bangladesh"]),
            [("Le revenu d'un habitant de la Norvège est environ combien de fois celui d'un habitant du Bangladesh ? (arrondi à l'unité)", "13", 2),
             ("Combien d'années d'espérance de vie de plus au Bangladesh qu'en Guinée équatoriale ?", "11", 2)],
            ["112 710 ÷ 8 498 : essaie 8 498 × 13.", "74,7 − 63,7.", "Pour la justification : cherche « ne suffit pas »."],
            J("Quelle phrase de la fiche montre que la richesse ne suffit pas à mesurer le développement ?", I_SEULE, [I_ECART, I_INDICATEURS, I_NIVEAU], pos=3)),
        "second": ordre(
            "Chef de mission, reconstitue le raisonnement de Nour devant le tableau du PNUD. Range les étapes dans l'ordre, puis choisis la phrase de la fiche qui le résume.",
            ["Le Bangladesh a un revenu par habitant plus faible que la Guinée équatoriale", "Pourtant, on y vit plus longtemps : 74,7 ans contre 63,7",
             "Le revenu ne dit donc pas tout du développement", "Pour comparer les pays, il faut croiser plusieurs indicateurs"],
            ["On commence par lire le revenu.", "« Pourtant » annonce une surprise.", "Pour la justification : cherche « Guinée équatoriale »."],
            J("Quelle phrase de la fiche résume ce raisonnement ?", I_SEULE, [I_INDICATEURS, I_ECART, I_PAUVRES], pos=0)),
    }
    return d
