# -*- coding: utf-8 -*-
"""Génère grandes-explorations/assets/data/lecons.json (5 leçons). Lancer : python gen_lecons.py <dossier data>
Le texte CM2 est fait des phrases de fiches.py (reprises mot pour mot par les justifications des grades)."""
import json, os, sys
from schemas import lecon_monde, lecon_caravelle, lecon_routes, lecon_rencontres, lecon_partage
import fiches as F

BO = "Programme d'histoire-géographie du cycle 3, arrêté du 22 avril 2026, BO n° 22 du 28 mai 2026 (thème « Explorations et conquêtes »)"


def L(id, salle, titre, objectifs, cm1, cm2, lexique, schema_titre, svg, sources, document=None):
    l = {"id": id, "salle": salle, "icone": str(salle), "titre": titre, "duree": "4 min", "niveau": "CM1-CM2", "objectifs": objectifs,
         "contenu": {"cm1": cm1, "cm2": cm2}, "lexique": [{"mot": m, "def": d} for m, d in lexique],
         "schema": {"titre": schema_titre, "svg": svg}}
    if document:
        l["document"] = document
    l["sources"] = sources
    return l


LECONS = [
    L("epices", 1, "Pourquoi partir ?",
      ["Savoir ce que les Européens connaissent du monde vers 1450", "Expliquer pourquoi les épices sont recherchées",
       "Citer plusieurs raisons de partir explorer", "CM2 : relier la prise de Constantinople (1453) à la recherche d'une route maritime"],
      "<h4>Le monde connu</h4><p>Vers 1450, les Européens connaissent l'<b>Europe</b>, une partie de l'<b>Afrique</b> et de l'<b>Asie</b>. Ils ne savent pas que les <b>Amériques</b> existent.</p>"
      "<h4>Les épices</h4><p>Le poivre et la cannelle viennent d'Asie. Ils parfument et conservent les aliments. Ils arrivent après un très long voyage : ils coûtent très cher. Les Européens cherchent une <b>route par la mer</b> pour aller les chercher eux-mêmes.</p>"
      "<h4>D'autres raisons</h4><p>Ils veulent aussi trouver de l'<b>or</b>, répandre la <b>religion chrétienne</b>, gagner la gloire et mieux connaître le monde.</p>",
      F.html(F.LECON_EPICES),
      [("épice", "produit venu de plantes (poivre, cannelle) qui parfume les plats"), ("route maritime", "chemin suivi par les navires sur la mer"),
       ("explorer", "partir à la découverte de régions mal connues"), ("Ottomans", "peuple turc qui prend Constantinople en 1453")],
      "Le monde connu des Européens vers 1450", lecon_monde(),
      BO + " ; BnF, exposition « L'âge d'or des cartes marines » ; Lumni, « Les grandes découvertes »."),
    L("techniques", 2, "Les progrès techniques",
      ["Décrire une caravelle et ses voiles", "Dire à quoi servent la boussole, l'astrolabe et les cartes marines",
       "CM2 : expliquer comment le pilote trouve sa latitude"],
      "<h4>La caravelle</h4><p>La <b>caravelle</b> est un navire léger. Ses voiles triangulaires l'aident à avancer même quand le vent n'est pas dans son dos. Le <b>gouvernail</b>, à l'arrière, sert à la diriger.</p>"
      "<h4>Les instruments</h4><p>La <b>boussole</b> indique le nord. L'<b>astrolabe</b> mesure la hauteur du Soleil ou d'une étoile : il aide à savoir où l'on est. Les <b>cartes marines</b> montrent les côtes et les ports.</p>",
      F.html(F.LECON_TECH),
      [("caravelle", "navire léger à voiles latines, utilisé pour les explorations"), ("boussole", "instrument dont l'aiguille aimantée indique le nord"),
       ("astrolabe", "instrument qui mesure la hauteur d'un astre au-dessus de l'horizon"), ("latitude", "position d'un lieu entre le nord et le sud"),
       ("portulan", "carte marine qui dessine les côtes et les ports")],
      "Une caravelle", lecon_caravelle(),
      BO + " ; Musée national de la Marine (instruments de navigation) ; Hérodote, « La vérité sur les bateaux de Colomb » ; BnF, « L'âge d'or des cartes marines »."),
    L("voyages", 3, "Les grands voyages",
      ["Situer sur une frise les voyages de Colomb, de Vasco de Gama, de Magellan et Elcano et de Cartier",
       "Suivre leurs routes sur une carte", "Dire « arrivée des Européens en Amérique », car le continent était habité",
       "CM2 : connaître les dates exactes et le bilan du premier tour du monde"],
      "<h4>Quatre voyages</h4><p>En <b>1492</b>, Christophe Colomb traverse l'Atlantique pour l'Espagne et arrive aux Antilles : il croit être en Asie. En <b>1498</b>, le Portugais Vasco de Gama arrive en Inde en faisant le tour de l'Afrique. De <b>1519 à 1522</b>, l'expédition de Magellan, terminée par Elcano, fait le premier tour du monde. En <b>1534</b>, Jacques Cartier arrive au Canada pour le roi de France.</p>"
      "<h4>Une terre habitée</h4><p>L'Amérique n'était pas vide : des peuples y vivaient depuis des milliers d'années. On parle d'<b>arrivée des Européens</b> en Amérique.</p>",
      F.html(F.LECON_VOYAGES),
      [("expédition", "voyage organisé pour explorer"), ("cap", "pointe de terre qui avance dans la mer"),
       ("tour du monde", "voyage qui revient à son point de départ en faisant le tour de la Terre")],
      "Les routes des grands voyages", lecon_routes(),
      BO + " ; Hérodote, « 20 mai 1498 », « 24 juillet 1534 », « La vérité sur les bateaux de Colomb » ; National Geographic, « Juan Sebastián Elcano » ; BAnQ (Nouvelle-France)."),
    L("rencontres", 4, "Rencontres et conquêtes",
      ["Nommer des peuples d'Amérique : Aztèques, Incas, Iroquoiens", "Expliquer pourquoi quelques centaines de conquistadors l'emportent",
       "Savoir que les maladies venues d'Europe ont tué un très grand nombre d'Amérindiens", "CM2 : dater la prise de Tenochtitlan (1521) et le début de la conquête de l'Empire inca (1532)"],
      "<h4>Les peuples d'Amérique</h4><p>Des millions de personnes vivent en Amérique. Au Mexique, les <b>Aztèques</b> ont une immense capitale, Tenochtitlan. Dans les Andes vivent les <b>Incas</b>. Au Canada, les <b>Iroquoiens</b> cultivent le maïs.</p>"
      "<h4>La conquête</h4><p>Les <b>conquistadors</b> espagnols ont des chevaux et des armes à feu. Ils trouvent des alliés parmi les peuples ennemis des Aztèques. Les <b>maladies</b> apportées d'Europe, comme la variole, tuent un très grand nombre d'Amérindiens.</p>"
      "<h4>Des échanges</h4><p>Le maïs, la pomme de terre, la tomate et le cacao arrivent en Europe ; le cheval et le blé arrivent en Amérique.</p>",
      F.html(F.LECON_RENCONTRES),
      [("conquistador", "soldat espagnol parti conquérir l'Amérique"), ("Amérindiens", "premiers habitants de l'Amérique"),
       ("variole", "maladie contagieuse venue d'Europe"), ("empire", "grand territoire dirigé par un seul souverain")],
      "Trois peuples d'Amérique vers 1500", lecon_rencontres(),
      BO + " ; World History Encyclopedia, « La conquête ibérique des Amériques » ; Schoolmouv, « Siège de Tenochtitlán (1521) » ; Lumni."),
    L("empires", 5, "Les premiers empires coloniaux",
      ["Expliquer le partage de Tordesillas (1494)", "Associer chaque colonie à son pays : Espagne, Portugal, France, Angleterre",
       "Dire ce que l'on exploite dans les colonies", "CM2 : relier l'exploitation des colonies au début de la traite atlantique (jeu « Les Archives du port »)"],
      "<h4>Le partage</h4><p>En <b>1494</b>, au traité de <b>Tordesillas</b>, l'Espagne et le Portugal se partagent les terres à découvrir : l'ouest pour l'Espagne, l'est pour le Portugal.</p>"
      "<h4>Les colonies</h4><p>L'Espagne domine le Mexique et le Pérou, et exploite des mines d'argent. Le Portugal s'installe au Brésil et y cultive la canne à sucre. La France fonde la <b>Nouvelle-France</b> (Québec, 1608) et y fait le commerce des fourrures. L'Angleterre s'installe en Amérique du Nord.</p>"
      "<h4>Le travail forcé</h4><p>Dans les mines et les plantations, les colons font travailler de force des Amérindiens, puis des Africains réduits en esclavage.</p>",
      F.html(F.LECON_EMPIRES),
      [("colonie", "territoire lointain dominé et exploité par un pays"), ("traité", "accord écrit entre des pays"),
       ("empire colonial", "ensemble des colonies d'un pays"), ("Nouvelle-France", "colonie française d'Amérique du Nord")],
      "Le partage de Tordesillas (1494)", lecon_partage(),
      BO + " ; World History Encyclopedia, « Le traité de Tordesillas » ; Hérodote, « 24 juillet 1534 » ; BAnQ, Nouvelle-France.",
      document={"type": "texte", "titre": "Le traité de Tordesillas, expliqué simplement",
                "contenu": "Le 7 juin 1494, les rois d'Espagne et du Portugal signent un accord. Une ligne imaginaire est tracée du nord au sud, à 370 lieues à l'ouest des îles du Cap-Vert. Les terres découvertes à l'ouest de la ligne seront espagnoles ; celles de l'est, portugaises. Les autres pays d'Europe et les peuples d'Amérique ne sont pas consultés.",
                "source": "Reformulation pour le cycle 3, d'après World History Encyclopedia et l'UNESCO (Mémoire du monde)."}),
]


def main(dest):
    json.dump({"lecons": LECONS}, open(os.path.join(dest, "lecons.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
