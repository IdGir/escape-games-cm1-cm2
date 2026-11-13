"""Salle 3 « La salle de contrôle » : grades mousse, lieutenant, second (fiche : Le schéma électrique)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "electricite", "tests", "donnees"))
from fiches import *

FICHE = "« Le schéma électrique »"


def donnees(svg, bloc=None):
    d = {}
    s3, s5 = svg("e3-2", "matelot"), svg("e3-2", "timonier")
    d["e3-1"] = {
        "mousse": assoc(
            "Relie chaque symbole à l'appareil qu'il représente.",
            [("un grand trait et un petit trait", "la pile"), ("un cercle avec une croix", "la lampe"), ("un cercle avec la lettre M", "le moteur")],
            ["Ouvre la fiche " + FICHE + ".", "M comme moteur.", "La lampe : une croix dans un rond."]),
        "lieutenant": assoc(
            "Hélène veut la légende complète. Relie chaque symbole décrit à ce qu'il représente, puis choisis la phrase de la fiche qui décrit la pile.",
            [("un grand trait et un petit trait parallèles", "la pile"), ("un cercle barré d'une croix", "la lampe"), ("un cercle avec la lettre M", "le moteur"),
             ("un trait levé entre deux points", "l'interrupteur ouvert"), ("un trait couché qui ferme le passage", "l'interrupteur fermé")],
            ["Le grand trait de la pile est la borne +.", "Levé = ouvert ; couché = fermé.", "Pour la justification : cherche « grand trait »."],
            J("Quelle phrase de la fiche décrit la pile ?", S_PILE, [S_LAMPE, S_INTER, S_FILS], pos=1)),
        "second": qcm(
            "Hélène compare le dessin du montage de Nour et le schéma du pupitre. Réponds, puis choisis la phrase de la fiche qui dit ce qu'un schéma garde.",
            [("Qu'est-ce qu'un schéma ne montre pas ?", ["les appareils", "la couleur et la forme réelle des objets", "les liaisons entre les appareils", "le nombre d'appareils"], 1, "Il ne garde que l'essentiel."),
             ("Pourquoi utilise-t-on des symboles normalisés ?", ["parce qu'ils sont plus jolis", "pour que tout le monde les comprenne", "pour cacher le circuit", "parce qu'on ne sait pas dessiner"], 1, "Les mêmes partout dans le monde."),
             ("Comment les fils sont-ils dessinés ?", ["en spirale", "par des traits droits", "en pointillés de couleur", "on ne les dessine pas"], 1, "Des traits droits, souvent en rectangle.")],
            ["Un schéma n'est pas une photo.", "Normalisé : la même règle pour tous.", "Pour la justification : cherche « l'essentiel »."],
            J("Quelle phrase de la fiche dit ce qu'un schéma garde ?", S_DESSIN, [S_SCHEMA, S_POURQUOI, S_FILS], pos=0)),
    }
    d["e3-2"] = {
        "mousse": {"type": "plan", "titre": "Le schéma du pupitre", "colonnes": 3,
                   "cases": [{"libelle": "Repère 1", "reponse": "pile"}, {"libelle": "Repère 2", "reponse": "interrupteur"}, {"libelle": "Repère 3", "reponse": "lampe"}],
                   "etiquettes": ["pile", "interrupteur", "lampe"],
                   "consigne": "Place le nom de chaque appareil sur son repère du schéma." + s3,
                   "indices": ["Ouvre la fiche " + FICHE + ".", "La croix dans le cercle, c'est la lampe.", "Le trait levé, c'est l'interrupteur."]},
        "lieutenant": {"type": "plan", "titre": "Le schéma du pupitre", "colonnes": 2,
                       "cases": [{"libelle": "Repère 1", "reponse": "pile"}, {"libelle": "Repère 2", "reponse": "interrupteur ouvert"}, {"libelle": "Repère 3", "reponse": "lampe"},
                                 {"libelle": "Repère 4", "reponse": "moteur"}, {"libelle": "Repère 5", "reponse": "fil de connexion"}],
                       "etiquettes": ["pile", "interrupteur ouvert", "lampe", "moteur", "fil de connexion", "interrupteur fermé", "prise", "buzzer"],
                       "consigne": "Place chaque étiquette sur son repère (trois sont en trop), puis choisis la phrase de la fiche qui permet de savoir si l'interrupteur est ouvert." + s5,
                       "indices": ["Regarde bien la position du trait de l'interrupteur.", "Le M désigne le moteur.", "Pour la justification : cherche « trait levé »."],
                       "justification": J("Quelle phrase de la fiche permet de le savoir ?", S_INTER, [S_PILE, S_FILS, S_LIRE], pos=2)},
        "second": {"type": "plan", "titre": "Le schéma du pupitre", "colonnes": 2,
                   "cases": [{"libelle": "Repère 1", "reponse": "pile"}, {"libelle": "Repère 2", "reponse": "interrupteur ouvert"}, {"libelle": "Repère 3", "reponse": "lampe"},
                             {"libelle": "Repère 4", "reponse": "moteur"}, {"libelle": "Repère 5", "reponse": "fil de connexion"}],
                   "etiquettes": ["pile", "interrupteur ouvert", "lampe", "moteur", "fil de connexion", "interrupteur fermé", "générateur du secteur", "buzzer"],
                   "consigne": "Place chaque étiquette sur son repère (trois sont en trop), puis choisis la phrase de la fiche qui décrit comment on dessine les fils." + s5,
                   "indices": ["Le repère 2 a un trait levé.", "Le repère 5 est sur un trait droit.", "Pour la justification : cherche « traits droits »."],
                   "justification": J("Quelle phrase de la fiche décrit le dessin des fils ?", S_FILS, [S_REGLE, S_SCHEMA, S_MOTEUR], pos=3)},
    }
    d["e3-3"] = {
        "mousse": vf(
            "Regarde le schéma du pupitre. Vrai ou faux ?" + s3,
            [("L'interrupteur est ouvert.", True, "Le trait est levé."),
             ("La lampe est allumée.", False, "La boucle est coupée."),
             ("Le schéma utilise des symboles.", True, "Pas des dessins ressemblants.")],
            ["Ouvre la fiche " + FICHE + ".", "Un trait levé, c'est ouvert.", "Ouvert : la boucle est coupée."]),
        "lieutenant": vf(
            "Hélène te fait lire le schéma du pupitre. Vrai ou faux ? Puis choisis la phrase de la fiche qui explique l'état du circuit." + s5,
            [("Sur ce schéma, aucun appareil ne fonctionne.", True, "L'interrupteur ouvert coupe la seule boucle."),
             ("Si on ferme l'interrupteur, la lampe et le moteur fonctionneront.", True, "Ils sont dans la même boucle."),
             ("Le moteur a sa propre boucle, indépendante de l'interrupteur.", False, "Il est dans la même boucle."),
             ("Le petit trait de la pile représente la borne +.", False, "C'est le grand trait.")],
            ["Il n'y a qu'un seul chemin.", "Le grand trait est la borne +.", "Pour la justification : cherche « aucun appareil »."],
            J("Quelle phrase de la fiche explique l'état du circuit ?", S_COUPE, [S_INTER, S_LIRE, S_POSITION], pos=0)),
        "second": ordre(
            "Hélène veut que tu transformes le dessin du montage de Nour en schéma. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche qui donne la méthode.",
            ["Repérer chaque appareil sur le dessin.", "Tracer les fils à la règle, en rectangle.", "Placer le symbole de chaque appareil sur un fil.",
             "Vérifier qu'il n'y a aucun trou dans la boucle.", "Suivre le courant de la borne + à la borne −."],
            ["On regarde avant de tracer.", "Les symboles se posent sur les fils.", "Pour la justification : cherche « à la règle »."],
            J("Quelle phrase de la fiche donne la méthode ?", S_REGLE, [S_FILS, S_DESSIN, S_LIRE], pos=2)),
    }
    d["e3-4"] = {
        "lieutenant": ordre(
            "Pose le doigt sur la borne + de la pile du schéma. Range les éléments dans l'ordre où le courant les traverse, puis choisis la phrase de la fiche qui décrit cette méthode." + s5,
            ["la borne + de la pile", "l'interrupteur", "la lampe", "le moteur", "la borne − de la pile"],
            ["La borne + est en haut de la pile.", "On tourne dans le sens des aiguilles d'une montre.", "Pour la justification : cherche « avec le doigt »."],
            J("Quelle phrase de la fiche décrit cette méthode ?", S_LIRE, [S_FILS, S_COUPE, S_PILE], pos=1)),
        "second": vf(
            "Un technicien a redessiné le schéma du pupitre : la lampe est maintenant en bas et le moteur à droite, mais les fils relient les mêmes appareils dans la même boucle. Vrai ou faux ? Puis justifie." + s5,
            [("Le nouveau schéma représente le même circuit.", True, "Les appareils sont reliés de la même façon."),
             ("Dans le nouveau schéma, la lampe et le moteur ne sont plus commandés par l'interrupteur.", False, "Ils sont toujours dans sa boucle."),
             ("Changer la place d'un symbole change forcément le circuit.", False, "Ce qui compte, ce sont les liaisons."),
             ("Si l'interrupteur reste ouvert, rien ne fonctionne dans les deux schémas.", True, "La boucle est coupée.")],
            ["Compare les liaisons, pas les places.", "Il n'y a toujours qu'une boucle.", "Pour la justification : cherche « équivalents »."],
            J("Quelle phrase de la fiche justifie tes réponses ?", S_POSITION, [S_DESSIN, S_LIRE, S_COUPE], pos=3)),
    }
    return d
