"""Salle 4 « Le rivage » : grades mousse, lieutenant, second (fiche : Rencontres et conquêtes).
Ton sobre ; les peuples d'Amérique sont présentés pour eux-mêmes (voix d'Itzel), pas seulement comme « découverts »."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "grandes-explorations", "tests", "donnees"))
from fiches import *

FICHE = "« Rencontres et conquêtes »"


def donnees(svg, bloc=None):
    d = {}
    d["e4-1"] = {
        "mousse": tri(
            "Itzel présente trois peuples d'Amérique. Range chaque carte sous le bon peuple.",
            [("azteques", "Aztèques"), ("incas", "Incas"), ("iroquoiens", "Iroquoiens")],
            [("une ville sur un lac", "azteques"), ("les montagnes des Andes", "incas"), ("des maisons longues", "iroquoiens")],
            ["Ouvre la fiche " + FICHE + ".", "Les Andes sont de hautes montagnes.", "Les Iroquoiens vivent près du Saint-Laurent."]),
        "lieutenant": tri(
            "Itzel présente trois peuples d'Amérique vers 1500. Range chaque carte sous le bon peuple, puis choisis la phrase de la fiche qui décrit l'Empire inca.",
            [("azteques", "Aztèques"), ("incas", "Incas"), ("iroquoiens", "Iroquoiens")],
            [("Tenochtitlan, bâtie sur un lac", "azteques"), ("des temples, des marchés et des canaux", "azteques"), ("Cuzco, dans les Andes", "incas"),
             ("un immense réseau de routes", "incas"), ("des villages de maisons longues", "iroquoiens"), ("la culture du maïs le long du Saint-Laurent", "iroquoiens")],
            ["Les canaux sont ceux de la ville sur le lac.", "Cuzco est dans les Andes.", "Pour la justification : cherche « réseau de routes »."],
            J("Quelle phrase de la fiche décrit l'Empire inca ?", R_INCAS, [R_AZTEQUES, R_NORD, R_PEUPLES], pos=1)),
        "second": ordre(
            "Itzel range ses dessins dans l'ordre du temps. Remets les événements du plus ancien au plus récent, puis choisis la phrase de la fiche qui date la chute de Tenochtitlan.",
            ["Colomb atteint une île des Bahamas.", "Cortés et ses alliés amérindiens prennent Tenochtitlan.", "Pizarro capture l'empereur inca Atahualpa.",
             "Cartier rencontre des Iroquoiens à Gaspé.", "Champlain fonde Québec."],
            ["Colomb ouvre la frise, en 1492.", "Tenochtitlan tombe onze ans avant la capture d'Atahualpa.", "Pour la justification : cherche « Cortés »."],
            J("Quelle phrase de la fiche date la chute de Tenochtitlan ?", R_CORTES, [R_PIZARRO, R_TENO, R_ARMES], pos=2)),
    }
    d["e4-2"] = {
        "mousse": qcm(
            "Itzel lit : « Vers 1500, des millions de personnes vivent en Amérique. Les Espagnols arrivent avec des chevaux. Ils apportent aussi des maladies. » Réponds.",
            [("Vers 1500, l'Amérique est...", ["vide", "habitée par des millions de personnes", "une île déserte"], 1, "Des millions de personnes y vivent."),
             ("Quel animal arrive avec les Espagnols ?", ["le cheval", "le lama", "le dindon"], 0, "Il n'existait pas en Amérique à cette époque."),
             ("Qu'apportent aussi les Espagnols, sans le savoir ?", ["des épices", "des livres", "des maladies"], 2, "Comme la variole.")],
            ["Ouvre la fiche " + FICHE + ".", "Relis la première phrase.", "La variole est une maladie."]),
        "lieutenant": qcm(
            "Itzel lit un texte adapté : « En 1521, Cortés et ses alliés amérindiens prennent Tenochtitlan. Les chevaux, l'acier et les armes à feu sont inconnus des Aztèques. La variole tue un très grand nombre d'habitants. » Réponds, puis choisis la phrase de la fiche qui explique l'effondrement de la population.",
            [("Cortés est-il seul face aux Aztèques ?", ["oui, avec quelques soldats", "non, il a des alliés amérindiens", "non, il a l'armée du roi de France", "non, il a les Incas"], 1, "Des peuples ennemis des Aztèques l'aident."),
             ("Qu'est-ce qui est inconnu des Aztèques ?", ["le maïs", "les canaux", "les marchés", "les chevaux et les armes à feu"], 3, "Ils arrivent avec les Espagnols."),
             ("Quelle est la principale cause de mort des Amérindiens ?", ["les maladies venues d'Europe", "les tempêtes", "les volcans", "le froid"], 0, "La variole notamment.")],
            ["Relis qui accompagne Cortés.", "Les Aztèques avaient des canaux et des marchés.", "Pour la justification : cherche « variole »."],
            J("Quelle phrase de la fiche explique l'effondrement de la population ?", R_MALADIES, [R_ARMES, R_CORTES, R_RESIST], pos=3)),
        "second": tri(
            "Pourquoi quelques centaines de conquistadors ont-ils pu l'emporter ? Itzel trie les explications : certaines sont justes, d'autres sont des idées fausses. Range chaque carte, puis choisis la phrase de la fiche qui cite les armes.",
            [("juste", "Explication juste"), ("faux", "Idée fausse")],
            [("des alliés amérindiens, ennemis des Aztèques", "juste"), ("des chevaux et des armes à feu", "juste"), ("des maladies comme la variole", "juste"),
             ("l'Amérique était presque vide", "faux"), ("les Amérindiens n'avaient pas de villes", "faux"), ("aucun peuple n'a résisté", "faux")],
            ["Tenochtitlan était une très grande ville.", "Certains peuples ont résisté longtemps.", "Pour la justification : cherche « acier »."],
            J("Quelle phrase de la fiche cite les armes des conquistadors ?", R_ARMES, [R_MALADIES, R_CORTES, R_RESIST], pos=0)),
    }
    d["e4-3"] = {
        "mousse": vf(
            "Itzel corrige les phrases écrites sur le sable. Vrai ou faux ?",
            [("L'Amérique était vide quand les Européens sont arrivés.", False, "Elle était habitée."),
             ("Le maïs vient d'Amérique.", True, "Il arrive ensuite en Europe."),
             ("Les chevaux existaient déjà en Amérique vers 1500.", False, "Les Espagnols les ont amenés.")],
            ["Ouvre la fiche " + FICHE + ".", "Itzel dit : « Nous étions là ! »", "Les chevaux sont arrivés par bateau."]),
        "lieutenant": vf(
            "Itzel corrige les phrases écrites sur le sable. Vrai ou faux ? Puis choisis la phrase de la fiche qui décrit les échanges.",
            [("On peut dire « arrivée des Européens en Amérique » plutôt que « découverte ».", True, "Car le continent était habité."),
             ("La tomate et le cacao viennent d'Amérique.", True, "Ils arrivent ensuite en Europe."),
             ("Le blé poussait en Amérique avant 1492.", False, "Il arrive avec les Européens."),
             ("Les échanges entre l'Europe et l'Amérique vont dans un seul sens.", False, "Ils vont dans les deux sens."),
             ("Certains peuples ont résisté longtemps aux conquérants.", True, "La conquête dure de nombreuses années.")],
            ["Le blé est cultivé en Europe depuis très longtemps.", "Le cheval va dans un sens, le maïs dans l'autre.", "Pour la justification : cherche « deux sens »."],
            J("Quelle phrase de la fiche décrit les échanges ?", R_ECHANGES, [R_PEUPLES, R_RESIST, R_NORD], pos=2)),
        "second": qcm(
            carnet("Notes d'Itzel", ": « Ma ville s'appelait Tenochtitlan. Les Espagnols l'ont détruite et ont bâti Mexico à sa place. Ils ont aussi donné des noms nouveaux à nos montagnes et à nos rivières. »")
            + "Réponds aux questions, puis choisis la phrase de la fiche qui décrit la ville d'Itzel avant la conquête.",
            [("Quelle ville moderne est bâtie à la place de Tenochtitlan ?", ["Lima", "Québec", "Mexico", "Cuzco"], 2, "Mexico, capitale du Mexique."),
             ("Pourquoi Itzel parle-t-elle de « noms nouveaux » ?", ["parce que les lieux n'avaient pas de nom", "parce que les lieux avaient déjà des noms dans les langues de leurs habitants", "parce que les Aztèques ne parlaient pas", "parce que les cartes étaient fausses"], 1, "Ces lieux avaient déjà des noms."),
             ("Quelle langue parlaient les Aztèques ?", ["le nahuatl", "le quechua", "l'espagnol", "le latin"], 0, "Le quechua est la langue des Incas.")],
            ["Itzel vient de Mexico.", "Relis sa phrase sur les noms.", "Pour la justification : cherche « canaux »."],
            J("Quelle phrase de la fiche décrit la ville d'Itzel avant la conquête ?", R_TENO, [R_AZTEQUES, R_CORTES, R_PEUPLES], pos=1)),
    }
    d["e4-4"] = {
        "lieutenant": intrus(
            "Itzel a rempli un panier de produits venus d'Amérique vers l'Europe. L'un d'eux a fait le chemin inverse : trouve-le, puis choisis la phrase de la fiche qui le confirme.",
            [("le maïs", False), ("la pomme de terre", False), ("la tomate", False), ("le cacao", False), ("le blé", True)],
            ["Cherche une plante cultivée en Europe depuis très longtemps.", "Avec quoi fait-on le pain ?", "Pour la justification : cherche « deux sens »."],
            J("Quelle phrase de la fiche confirme ta réponse ?", R_ECHANGES, [R_NORD, R_AZTEQUES, R_PEUPLES], pos=0)),
        "second": vf(
            "Itzel relit le panneau d'une exposition. Vrai ou faux ? Puis choisis la phrase de la fiche qui situe le début de la conquête de l'Empire inca.",
            [("Pizarro capture l'empereur inca Atahualpa en 1532.", True, "C'est le début de la conquête de l'Empire inca."),
             ("Les Incas vivaient au Mexique.", False, "Ils vivaient dans la cordillère des Andes."),
             ("Les Amérindiens étaient protégés contre la variole.", False, "Ils ne l'étaient pas : la population s'effondre."),
             ("Le cheval, le blé et la vache arrivent en Amérique avec les Européens.", True, "Les échanges vont dans les deux sens."),
             ("Vers 1500, l'Amérique compte des millions d'habitants.", True, "Dans des sociétés très différentes.")],
            ["Les Incas sont dans les Andes, les Aztèques au Mexique.", "La variole était inconnue en Amérique.", "Pour la justification : cherche « Atahualpa »."],
            J("Quelle phrase de la fiche situe le début de la conquête de l'Empire inca ?", R_PIZARRO, [R_INCAS, R_CORTES, R_RESIST], pos=3)),
    }
    return d
