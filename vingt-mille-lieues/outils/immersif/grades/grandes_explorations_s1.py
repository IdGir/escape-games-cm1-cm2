"""Salle 1 « La cale aux épices » : grades mousse, lieutenant, second (fiche : Pourquoi partir ?)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "grandes-explorations", "tests", "donnees"))
from fiches import *

FICHE = "« Pourquoi partir ? »"


def donnees(svg, bloc=None):
    d = {}
    carte = svg("e1-1", "timonier")
    d["e1-1"] = {
        "mousse": {"type": "plan", "titre": "La carte d'Amaury", "colonnes": 3,
                   "cases": [{"libelle": "Repère 1", "reponse": "Europe"}, {"libelle": "Repère 2", "reponse": "Afrique"}, {"libelle": "Repère 3", "reponse": "Asie"}],
                   "etiquettes": ["Europe", "Afrique", "Asie"],
                   "consigne": "Amaury déroule sa carte. Place le nom de chaque continent sur son repère. Les repères 4 et 5 ne comptent pas ici." + carte,
                   "indices": ["Ouvre la fiche " + FICHE + ".", "L'Europe est en haut, au milieu.", "L'Asie est la grande terre à droite."]},
        "lieutenant": {"type": "plan", "titre": "La carte d'Amaury", "colonnes": 2,
                       "cases": [{"libelle": "Repère 1", "reponse": "Europe"}, {"libelle": "Repère 2", "reponse": "Afrique"}, {"libelle": "Repère 3", "reponse": "Asie"},
                                 {"libelle": "Repère 4", "reponse": "mer Méditerranée"}, {"libelle": "Repère 5", "reponse": "route des épices"}],
                       "etiquettes": ["Europe", "Afrique", "Asie", "mer Méditerranée", "route des épices", "Amériques", "océan Pacifique", "route de la soie maritime"],
                       "consigne": "Place chaque étiquette sur son repère (trois sont en trop), puis choisis la phrase de la fiche qui explique pourquoi les Amériques sont en pointillés." + carte,
                       "indices": ["Les terres en pointillés sont inconnues des Européens.", "La ligne marron arrive d'Asie par la terre.", "Pour la justification : cherche le mot « ignorent »."],
                       "justification": J("Quelle phrase de la fiche explique les pointillés ?", E_MONDE, [E_RONDE, E_MER, E_COTES], pos=1)},
        "second": tri(
            "Sur la carte d'Amaury, certaines terres sont dessinées, d'autres en pointillés. Range chaque élément : connu ou inconnu des Européens vers 1450 ? Puis choisis la phrase de la fiche qui parle de la forme de la Terre." + carte,
            [("connu", "Connu des Européens vers 1450"), ("inconnu", "Inconnu des Européens vers 1450")],
            [("la mer Méditerranée", "connu"), ("le nord de l'Afrique", "connu"), ("une partie de l'Asie", "connu"), ("la forme ronde de la Terre", "connu"),
             ("les Amériques", "inconnu"), ("l'océan Pacifique", "inconnu"), ("la vraie taille de la Terre", "inconnu")],
            ["Les pointillés montrent ce qui est inconnu.", "Les savants savent que la Terre est ronde, mais pas sa vraie taille.", "Pour la justification : cherche « plus petite »."],
            J("Quelle phrase de la fiche parle de la forme de la Terre ?", E_RONDE, [E_MONDE, E_INTERM, E_GLOIRE], pos=2)),
    }
    d["e1-2"] = {
        "mousse": assoc(
            "Relie chaque produit de la cale à ce qu'on en fait.",
            [("le poivre", "parfume les plats"), ("l'or", "sert à faire des pièces"), ("la soie", "est un tissu précieux")],
            ["Ouvre la fiche " + FICHE + ".", "Le poivre se met dans la nourriture.", "La soie est douce comme un foulard."]),
        "lieutenant": qcm(
            "Amaury interroge ses visiteurs sur le prix des épices. Réponds aux questions, puis choisis la phrase de la fiche qui explique ce prix.",
            [("D'où viennent le poivre et la cannelle ?", ["d'Amérique", "d'Asie", "d'Europe du Nord", "d'Australie"], 1, "Ils viennent d'Asie."),
             ("À quoi servent les épices ?", ["à parfumer et à conserver les aliments", "à fabriquer des voiles", "à soigner le bois des navires", "à teindre le cuir"], 0, "Elles parfument et conservent."),
             ("Pourquoi coûtent-elles si cher en Europe ?", ["parce qu'elles sont lourdes", "parce que le roi les interdit", "parce qu'elles passent par de nombreux marchands", "parce qu'elles pourrissent vite"], 2, "Chaque marchand prend sa part.")],
            ["Le poivre pousse très loin de l'Europe.", "On met les épices dans les plats.", "Pour la justification : cherche « augmentent leur prix »."],
            J("Quelle phrase de la fiche explique le prix des épices ?", E_INTERM, [E_EPICES, E_MER, E_OR], pos=0)),
        "second": vf(
            "Amaury a entendu des visiteurs expliquer les voyages. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui explique le choix de la mer.",
            [("En 1453, les Turcs ottomans prennent Constantinople.", True, "Ils contrôlent une partie des routes vers l'Asie."),
             ("La prise de Constantinople rend les routes de terre vers l'Asie plus faciles pour les Européens.", False, "Au contraire : une partie de ces routes leur échappe."),
             ("Les Européens cherchent une route par la mer pour aller chercher les épices eux-mêmes.", True, "Sans tous les intermédiaires."),
             ("Le Portugal et l'Espagne sont tournés vers l'océan Atlantique.", True, "Ils lancent les premières grandes expéditions."),
             ("Les épices servaient seulement à décorer les tables.", False, "Elles parfument et conservent les aliments.")],
            ["Les Ottomans contrôlent une partie des routes.", "Relis le rôle des épices.", "Pour la justification : cherche « par la mer »."],
            J("Quelle phrase de la fiche dit ce que cherchent les Européens ?", E_MER, [E_1453, E_PORTU, E_EPICES], pos=3)),
    }
    d["e1-3"] = {
        "mousse": vf(
            "Amaury te raconte des histoires. Vrai ou faux ?",
            [("Le poivre venait de très loin, d'Asie.", True, "Il coûtait très cher."),
             ("Vers 1450, les Européens connaissaient déjà l'Amérique.", False, "Ils ne la connaissaient pas."),
             ("Les savants savaient que la Terre est ronde.", True, "La Terre plate est une légende.")],
            ["Ouvre la fiche " + FICHE + ".", "Les Amériques sont en pointillés sur la carte.", "Les savants avaient étudié le ciel."]),
        "lieutenant": vf(
            "Amaury trie les histoires du port : certaines sont des légendes. Vrai ou faux ? Puis choisis la phrase de la fiche qui corrige la légende de la Terre plate.",
            [("Les savants de 1450 pensaient que la Terre était plate.", False, "Ils savaient qu'elle est ronde."),
             ("Les savants croyaient la Terre plus petite qu'elle ne l'est.", True, "C'est pourquoi Colomb pensait atteindre vite l'Asie."),
             ("Au XVe siècle, les marins portugais longent les côtes d'Afrique.", True, "Ils cherchent un passage vers l'Asie."),
             ("Vers 1450, les Amériques figurent sur les cartes européennes.", False, "Elles sont inconnues des Européens.")],
            ["La Terre plate est une légende.", "Ronde, mais plus petite qu'on ne le croyait.", "Pour la justification : cherche « ronde »."],
            J("Quelle phrase de la fiche corrige la légende ?", E_RONDE, [E_MONDE, E_COTES, E_PORTU], pos=1)),
        "second": qcm(
            carnet("Note d'Amaury", ": « Un marchand achète du poivre en Asie et le revend. D'autres marchands l'achètent et le revendent à leur tour, jusqu'à Venise. »") + "Réponds aux questions, puis choisis la phrase de la fiche qui résume l'idée des Européens.",
            [("Que se passe-t-il à chaque revente ?", ["le prix baisse", "le prix augmente", "le poivre change de goût", "rien ne change"], 1, "Chaque marchand gagne sa part."),
             ("Quel événement de 1453 complique ces routes ?", ["la prise de Constantinople par les Ottomans", "le voyage de Colomb", "la fondation de Québec", "le traité de Tordesillas"], 0, "Les Ottomans contrôlent une partie des routes."),
             ("Quels pays lancent les premières grandes expéditions ?", ["la France et l'Angleterre", "la Pologne et la Suède", "le Portugal et l'Espagne", "l'Italie et la Grèce"], 2, "Ils sont tournés vers l'Atlantique.")],
            ["Plus il y a d'intermédiaires, plus c'est cher.", "1453 : Constantinople.", "Pour la justification : cherche « directement »."],
            J("Quelle phrase de la fiche résume l'idée des Européens ?", E_MER, [E_INTERM, E_1453, E_OR], pos=2)),
    }
    d["e1-4"] = {
        "lieutenant": tri(
            "Amaury range ses caisses selon la raison du voyage. Place chaque carte, puis choisis la phrase de la fiche qui parle de religion.",
            [("richesse", "Richesse"), ("religion", "Religion"), ("savoir", "Savoir et gloire")],
            [("acheter le poivre moins cher", "richesse"), ("trouver de l'or et de l'argent", "richesse"), ("répandre la religion chrétienne", "religion"),
             ("baptiser les peuples rencontrés", "religion"), ("mieux connaître le monde", "savoir"), ("recevoir des titres du roi", "savoir")],
            ["Tout ce qui rapporte de l'argent : richesse.", "Les titres sont une récompense : gloire.", "Pour la justification : cherche « catholiques »."],
            J("Quelle phrase de la fiche parle de religion ?", E_FOI, [E_GLOIRE, E_OR, E_MER], pos=0)),
        "second": ordre(
            "Amaury retrace l'enchaînement qui pousse les Européens vers la mer. Remets les étapes dans l'ordre, puis choisis la phrase de la fiche qui décrit l'avance portugaise.",
            ["Les épices d'Asie sont très recherchées en Europe.", "Elles passent par de nombreux marchands : leur prix augmente.",
             "En 1453, les Ottomans prennent Constantinople.", "Les Européens cherchent une route par la mer.",
             "Les marins portugais descendent le long des côtes d'Afrique."],
            ["Commence par le produit recherché.", "La prise de Constantinople est un événement daté.", "Pour la justification : cherche « peu à peu »."],
            J("Quelle phrase de la fiche décrit l'avance portugaise ?", E_COTES, [E_PORTU, E_MER, E_1453], pos=3)),
    }
    return d
