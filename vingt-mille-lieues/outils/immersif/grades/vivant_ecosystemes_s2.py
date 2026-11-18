"""Salle 2 « La cabane du garde » : grades mousse, lieutenant, second (fiche : Classer et identifier)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "vivant-ecosystemes", "tests", "donnees"))
from fiches import *
from schemas import cle, arbre

FICHE = "« Classer et identifier »"


def _plan_cle(n, cases, etiq, consigne, indices, j=None):
    b = {"type": "plan", "titre": "La clé d'Hugo", "colonnes": 2 if n > 3 else 3,
         "cases": [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(cases)], "etiquettes": etiq,
         "consigne": consigne + cle(n), "indices": indices}
    if j:
        b["justification"] = j
    return b


def donnees(svg, bloc=None):
    d = {}
    d["e2-1"] = {
        "mousse": tri(
            "Hugo range ses fiches. Place chaque animal dans la bonne caisse.",
            [("poils", "A des poils"), ("plumes", "A des plumes")],
            [("le renard", "poils"), ("le lapin", "poils"), ("le héron", "plumes"), ("le canard", "plumes")],
            ["Ouvre la fiche " + FICHE + ".", "Les oiseaux ont des plumes.", "Le lapin a un pelage doux."]),
        "lieutenant": tri(
            "Hugo range les fiches dans les groupes emboîtés de son affiche. Place chaque animal dans le plus petit groupe qui lui convient, puis choisis la phrase de la fiche qui explique l'emboîtement.",
            [("poils", "Poils"), ("plumes", "Plumes"), ("membres", "Quatre membres, ni poils ni plumes"), ("six", "Six pattes"), ("huit", "Huit pattes")],
            [("la chauve-souris", "poils"), ("le hérisson", "poils"), ("le canard", "plumes"), ("le lézard", "membres"), ("la salamandre", "membres"),
             ("la libellule", "six"), ("le scarabée", "six"), ("l'araignée", "huit")],
            ["La salamandre a une peau nue et quatre membres.", "Les insectes ont six pattes.", "Pour la justification : cherche « rangé dans »."],
            J("Quelle phrase de la fiche explique ce que sont des groupes emboîtés ?", C_EMBOITE, [C_CLASSER, C_PARENTE, C_PAS_MILIEU], pos=1)),
        "second": ordre(
            "Hugo montre un arbre de parenté. Range ces animaux du plus proche parent du loup au plus éloigné, puis choisis la phrase de la fiche qui explique comment lire l'arbre." + arbre(),
            [("le renard", "même point de séparation que le loup, tout en haut"), "le lézard", "la grenouille", ("la truite", "séparée la première")],
            ["Le renard partage l'ancêtre commun le plus récent.", "La truite s'est séparée la première.", "Pour la justification : cherche « séparées tard »."],
            J("Quelle phrase de la fiche explique comment lire un arbre de parenté ?", C_ARBRE, [C_ANCETRE, C_PARENTE, C_EMBOITE], pos=2)),
    }
    d["e2-2"] = {
        "mousse": qcm(
            "Hugo pose deux questions. Choisis la bonne réponse.",
            [("Pour ranger les animaux, on regarde…", ["ce qu'ils possèdent", "leur couleur préférée", "leur prénom", "leur âge"], 0, "Des poils, des plumes, des pattes."),
             ("La chauve-souris a des poils. Avec qui la range-t-on ?", ["avec le renard", "avec le héron", "avec la libellule", "avec la truite"], 0, "Elle a des poils, comme le renard.")],
            ["Ouvre la fiche " + FICHE + ".", "On regarde l'animal.", "Poils avec poils."]),
        "lieutenant": qcm(
            "Hugo montre son arbre de parenté. Réponds à ses questions, puis choisis la phrase de la fiche qui définit l'ancêtre commun." + arbre(),
            [("Quel animal est le plus proche parent du loup ?", ["la truite", "le renard", "le lézard", "la grenouille"], 1, "Ils partagent l'ancêtre commun le plus récent."),
             ("Le lézard est-il plus proche du renard ou de la truite ?", ["du renard", "de la truite", "des deux autant", "d'aucun"], 0, "Il s'est séparé plus tard de la lignée du renard."),
             ("Le point rouge de l'arbre représente…", ["un animal actuel", "un ancêtre commun disparu", "un fossile de trilobite", "une erreur"], 1, "Une espèce disparue."),
             ("Un arbre de parenté sert à…", ["trouver le nom d'une bête", "montrer les liens de parenté", "compter les pattes", "dessiner une forêt"], 1, "Identifier, c'est la clé.")],
            ["Plus haut est le point de séparation, plus les espèces sont proches.", "L'ancêtre commun a disparu.", "Pour la justification : cherche « dont descendent »."],
            J("Quelle phrase de la fiche définit l'ancêtre commun ?", C_ANCETRE, [C_ARBRE, C_PARENTE, C_CLE], pos=2)),
        "second": vf(
            "Une visiteuse a photographié une petite bête avec une application. Hugo vérifie. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur les applications.",
            [("Une application d'identification peut se tromper.", True, "On vérifie avec une clé."),
             ("La clé donne le nom d'une espèce ; la classification montre sa parenté.", True, "Identifier n'est pas classer."),
             ("« Les animaux qui vivent dans l'eau » est un groupe de classification.", False, "Le lieu de vie ne sert pas à classer."),
             ("Le dauphin est rangé avec les poissons, car il nage.", False, "Il respire avec des poumons et allaite ses petits."),
             ("Le cloporte a quatorze pattes : ce n'est pas un insecte.", True, "Les insectes ont six pattes.")],
            ["Une photo peut être floue.", "Le lieu de vie ne compte pas.", "Pour la justification : cherche « intelligence artificielle »."],
            J("Quelle phrase de la fiche parle des applications d'identification ?", C_APPLI, [C_CLE, C_CLE_PAS, C_PATTES], pos=1)),
    }
    d["e2-3"] = {
        "mousse": _plan_cle(3, ["l'escargot", "la fourmi", "l'araignée"], ["l'escargot", "la fourmi", "l'araignée"],
                            "Suis la clé d'Hugo et place chaque nom dans sa case.",
                            ["Ouvre la fiche " + FICHE + ".", "L'escargot n'a pas de pattes.", "L'araignée a huit pattes."]),
        "lieutenant": _plan_cle(5, ["l'escargot", "la fourmi", "l'araignée", "le cloporte", "le mille-pattes"],
                                ["l'escargot", "la fourmi", "l'araignée", "le cloporte", "le mille-pattes", "le ver de terre", "la coccinelle"],
                                "Suis la clé d'Hugo et place chaque nom dans sa case (deux sont en trop), puis choisis la phrase de la fiche qui distingue identifier et classer.",
                                ["Le ver de terre n'a pas de pattes, mais la case est déjà prise.", "La coccinelle est un insecte.", "Pour la justification : cherche « n'est pas classer »."],
                                J("Quelle phrase de la fiche distingue identifier et classer ?", C_CLE_PAS, [C_CLE, C_CLASSER, C_APPLI], pos=3)),
        "second": _plan_cle(5, ["l'escargot", "la fourmi", "l'araignée", "le cloporte", "le mille-pattes"],
                            ["l'escargot", "la fourmi", "l'araignée", "le cloporte", "le mille-pattes", "la limace", "le moustique", "l'opilion"],
                            "Hugo a trouvé cinq bêtes dans le bac, mais ses étiquettes en proposent huit. Place les bonnes, puis choisis la phrase de la fiche qui donne le nombre de pattes.",
                            ["Le moustique est un insecte : six pattes.", "L'opilion a huit pattes, mais la case est déjà prise par l'araignée.", "Pour la justification : cherche « quatorze »."],
                            J("Quelle phrase de la fiche donne le nombre de pattes de ces animaux ?", C_PATTES, [C_CLE, C_APPLI, C_EMBOITE], pos=0)),
    }
    d["e2-4"] = {
        "lieutenant": intrus(
            "Un apprenti a écrit des noms de groupes sur les caisses. Un seul n'est pas un groupe de classification. Trouve-le, puis choisis la phrase de la fiche qui l'explique.",
            [("A des plumes", False), ("A des poils", False), ("A six pattes", False), ("A un squelette interne", False), ("N'a pas de pattes", True)],
            ["On classe avec ce que l'on possède.", "« N'a pas » décrit une absence.", "Pour la justification : cherche « ne possède pas »."],
            J("Quelle phrase de la fiche explique pourquoi ce n'est pas un groupe ?", C_PAS_ABSENCE, [C_CLASSER, C_PAS_MILIEU, C_EMBOITE], pos=0)),
        "second": qcm(
            "Hugo pose ses questions les plus difficiles. Choisis la bonne réponse, puis la phrase de la fiche sur le lieu de vie.",
            [("Le dauphin et la truite vivent dans l'eau. Avec qui range-t-on le dauphin ?", ["avec la truite", "avec la vache et le renard", "avec les algues", "avec la libellule"], 1, "Il respire avec des poumons et allaite."),
             ("Pourquoi le renard est-il plus proche du loup que du hérisson ?", ["ils ont la même couleur", "ils partagent plus d'attributs", "ils vivent dans la même forêt", "ils mangent des lapins"], 1, "La parenté se lit dans les attributs."),
             ("Un ancêtre commun est…", ["une espèce actuelle", "une espèce disparue dont descendent plusieurs espèces actuelles", "le plus vieil animal du zoo", "un fossile de plante"], 1, "Il a disparu."),
             ("Qu'apporte une clé de détermination ?", ["le nom d'un être vivant", "sa date de naissance", "ses parents", "son poids"], 0, "Elle identifie.")],
            ["Le lieu de vie ne compte pas pour classer.", "Les attributs partagés montrent la parenté.", "Pour la justification : cherche « dauphin »."],
            J("Quelle phrase de la fiche dit que le lieu de vie ne sert pas à classer ?", C_PAS_MILIEU, [C_PAS_ABSENCE, C_PARENTE, C_CLASSER], pos=3)),
    }
    return d
