#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les évaluations imprimables de « La Caravelle du capitaine » (jeu n°13, grandes explorations).

    python grandes-explorations/outils/generer-evaluations.py

Écrit grandes-explorations/assets/data/evaluations.json (format commun des jeux) et
grandes-explorations/assets/data/evaluations-embarquees.js (copie lue en double-clic, file://).
Page d'impression : grandes-explorations/evaluations-imprimables.html.
Tous les faits viennent des leçons du jeu (assets/data/lecons.json). Les documents marqués
« inventé pour le jeu » sont des résumés de leçon, pas des sources d'époque.
"""
import json, os
ICI = os.path.dirname(os.path.abspath(__file__))
JEU = os.path.dirname(ICI)

def q(texte, options, bonne): return {"q": texte, "options": options, "bonne": bonne, "pts": 1}
def vf(texte, rep): return {"q": texte, "type": "vf", "bonne": rep, "pts": 1}
def court(texte, rep): return {"q": texte, "type": "court", "rep": rep, "pts": 1}

EVAL = {
 "metadata": {
  "sujet": "Les raisons des explorations, les progrès techniques, les grands voyages, la rencontre avec les peuples d'Amérique et la conquête, les premiers empires coloniaux",
  "niveaux": ["CM1", "CM2"],
  "programme": "Histoire, cycle 3 — thème « Explorations et conquêtes » (programme 2026). Progression de l'enseignant : année B, période 3. Repères en CM1, dates exactes en CM2.",
  "sources": "Leçons du jeu (assets/data/lecons.json) ; voir README.md et A-VERIFIER.md du jeu."
 },
 "quizz_final": {
  "CM1": [
   q("Vers 1450, les Européens cherchent une route par la mer pour aller chercher...", ["les épices d'Asie", "le maïs d'Amérique", "le sucre du Brésil"], 0),
   q("Quel instrument indique le nord ?", ["l'astrolabe", "la boussole", "le sablier"], 1),
   q("En quelle année Christophe Colomb arrive-t-il aux Antilles ?", ["1453", "1534", "1492"], 2),
   q("Qui vivait au Mexique à l'arrivée des Espagnols ?", ["les Aztèques", "les Incas", "les Iroquoiens"], 0),
   q("Au traité de Tordesillas (1494), les terres sont partagées entre...", ["la France et l'Angleterre", "l'Espagne et le Portugal", "l'Espagne et la France"], 1)],
  "CM2": [
   q("En 1453, Constantinople est prise par...", ["les Portugais", "les Espagnols", "les Turcs ottomans"], 2),
   q("Avec l'astrolabe, le pilote trouve...", ["sa latitude", "l'heure exacte", "la profondeur de l'eau"], 0),
   q("Qui ramène la Victoria en Espagne le 6 septembre 1522 ?", ["Magellan", "Elcano", "Vasco de Gama"], 1),
   q("En 1521, Cortés et ses alliés amérindiens prennent...", ["Cuzco", "Québec", "Tenochtitlan"], 2),
   q("Qui fonde Québec en 1608 ?", ["Samuel de Champlain", "Jacques Cartier", "Pedro Cabral"], 0)]
 },
 "fiches_preparatoires": [
  {"salle": 1, "titre": "La cale aux épices — Pourquoi partir ?",
   "objectifs": ["Savoir ce que les Européens connaissent du monde vers 1450", "Citer plusieurs raisons de partir explorer"],
   "vocabulaire": [{"mot": "épice", "def": "produit venu de plantes (poivre, cannelle) qui parfume les plats"}, {"mot": "route maritime", "def": "chemin suivi par les navires sur la mer"}, {"mot": "explorer", "def": "partir à la découverte de régions mal connues"}],
   "contexte": "Les épices viennent d'Asie et coûtent très cher : les Européens cherchent une route par la mer pour aller les chercher eux-mêmes."},
  {"salle": 2, "titre": "Le pont de la caravelle — Les progrès techniques",
   "objectifs": ["Décrire une caravelle", "Dire à quoi servent la boussole, l'astrolabe et les cartes marines"],
   "vocabulaire": [{"mot": "caravelle", "def": "navire léger aux voiles triangulaires"}, {"mot": "boussole", "def": "instrument dont l'aiguille indique le nord"}, {"mot": "astrolabe", "def": "instrument qui mesure la hauteur du Soleil ou d'une étoile"}],
   "contexte": "Grâce à de nouveaux navires et instruments, les marins osent s'éloigner des côtes."},
  {"salle": 3, "titre": "La chambre des cartes — Les grands voyages",
   "objectifs": ["Placer sur une frise les voyages de 1492, 1498, 1519-1522 et 1534", "Suivre leurs routes sur une carte"],
   "vocabulaire": [{"mot": "expédition", "def": "voyage organisé pour explorer"}, {"mot": "cap", "def": "pointe de terre qui avance dans la mer"}, {"mot": "tour du monde", "def": "voyage qui revient à son point de départ en faisant le tour de la Terre"}],
   "contexte": "Colomb vers l'ouest, Vasco de Gama vers l'est, Magellan et Elcano autour du monde, Cartier au nord. L'Amérique était déjà habitée."},
  {"salle": 4, "titre": "Le rivage — Rencontres et conquêtes",
   "objectifs": ["Nommer des peuples d'Amérique", "Expliquer le rôle des maladies dans la conquête"],
   "vocabulaire": [{"mot": "conquistador", "def": "conquérant espagnol en Amérique"}, {"mot": "Amérindiens", "def": "premiers habitants de l'Amérique"}, {"mot": "variole", "def": "maladie contagieuse apportée d'Europe"}],
   "contexte": "Aztèques au Mexique, Incas dans les Andes, Iroquoiens au Canada. Les maladies venues d'Europe tuent un très grand nombre d'Amérindiens."},
  {"salle": 5, "titre": "Le cabinet du cartographe — Les premiers empires coloniaux",
   "objectifs": ["Expliquer le partage de Tordesillas", "Associer chaque colonie à son pays"],
   "vocabulaire": [{"mot": "colonie", "def": "territoire lointain dominé et exploité par un pays"}, {"mot": "traité", "def": "accord écrit entre des pays"}, {"mot": "empire colonial", "def": "ensemble des colonies d'un pays"}],
   "contexte": "Espagne : Mexique et Pérou ; Portugal : Brésil ; France : Nouvelle-France ; Angleterre : Amérique du Nord. Le travail forcé conduit au début de la traite atlantique."}
 ],
 "qcm": {
  "CM1": [
   q("Vers 1450, quel continent les Européens ne connaissent-ils pas ?", ["l'Afrique", "l'Amérique", "l'Asie"], 1),
   q("Les épices servent à...", ["parfumer et conserver les aliments", "construire des navires", "fabriquer des cartes"], 0),
   q("Pourquoi les épices coûtent-elles très cher ?", ["elles sont rares en Asie", "elles pèsent lourd", "elles arrivent après un très long voyage"], 2),
   q("Les voiles triangulaires de la caravelle l'aident à avancer...", ["même quand le vent n'est pas dans son dos", "seulement par temps calme", "sans aucun vent"], 0),
   q("Le gouvernail sert à...", ["mesurer la vitesse", "diriger le navire", "indiquer le nord"], 1),
   q("En 1498, Vasco de Gama arrive...", ["au Canada", "aux Antilles", "en Inde"], 2),
   q("Le premier tour du monde a lieu de...", ["1519 à 1522", "1492 à 1498", "1534 à 1608"], 0),
   q("Pour quel roi Jacques Cartier part-il au Canada ?", ["le roi d'Espagne", "le roi de France", "le roi du Portugal"], 1),
   q("Les conquistadors ont des chevaux et...", ["des avions", "des boussoles seulement", "des armes à feu"], 2),
   q("Le Portugal cultive au Brésil...", ["la canne à sucre", "le blé", "les épices"], 0)],
  "CM2": [
   q("Vers 1450, les savants européens savent déjà que la Terre est...", ["plate", "ronde", "immobile au centre de l'Univers"], 1),
   q("Quels pays lancent les premières grandes expéditions ?", ["la France et l'Angleterre", "Venise et Gênes", "le Portugal et l'Espagne"], 2),
   q("La boussole a été inventée...", ["en Chine", "au Portugal", "en Amérique"], 0),
   q("Les portulans sont...", ["des marins", "des cartes marines", "des voiles"], 1),
   q("Colomb quitte Palos le...", ["12 octobre 1492", "20 mai 1498", "3 août 1492"], 2),
   q("Vasco de Gama passe par...", ["le cap de Bonne-Espérance", "le détroit de Magellan", "l'océan Pacifique"], 0),
   q("Combien d'hommes reviennent sur la Victoria en 1522 ?", ["250", "18", "5"], 1),
   q("En 1532, Pizarro capture l'empereur inca...", ["Moctezuma", "Cortés", "Atahualpa"], 2),
   q("La ligne de Tordesillas passe à 370 lieues à l'ouest...", ["des îles du Cap-Vert", "de Lisbonne", "des Antilles"], 0),
   q("Le Portugais Cabral arrive au Brésil en...", ["1494", "1500", "1534"], 1),
   q("L'Espagne s'enrichit surtout grâce...", ["aux fourrures", "au sucre", "à l'argent des mines"], 2),
   q("La Virginie, première colonie anglaise, est fondée en...", ["1607", "1608", "1492"], 0)]
 },
 "questions_fermees": {
  "CM1": [
   vf("Vers 1450, les Européens connaissent déjà l'Amérique.", "faux"),
   vf("L'astrolabe mesure la hauteur du Soleil ou d'une étoile.", "vrai"),
   vf("Christophe Colomb croit être arrivé en Asie.", "vrai"),
   vf("L'Amérique était vide quand les Européens sont arrivés.", "faux"),
   vf("La France fonde la Nouvelle-France.", "vrai"),
   court("Cite deux raisons qui poussent les Européens à explorer.", "les épices, l'or, la religion chrétienne, la gloire ou le savoir (deux au choix)"),
   court("Cite un produit venu d'Amérique et un produit venu d'Europe.", "Amérique : maïs, pomme de terre, tomate ou cacao ; Europe : cheval ou blé"),
   court("Pourquoi beaucoup d'Amérindiens meurent-ils après l'arrivée des Européens ?", "à cause des maladies venues d'Europe, comme la variole")],
  "CM2": [
   vf("En 1453, les Turcs ottomans prennent Constantinople.", "vrai"),
   vf("Magellan rentre lui-même en Espagne en 1522.", "faux"),
   vf("Les Iroquoiens vivent le long du fleuve Saint-Laurent.", "vrai"),
   vf("La France et l'Angleterre acceptent le partage de Tordesillas.", "faux"),
   court("Explique ce qu'est la latitude.", "la position d'un lieu entre le nord et le sud"),
   court("Pourquoi dit-on « arrivée des Européens en Amérique » plutôt que « découverte » ?", "parce que l'Amérique était habitée depuis des milliers d'années"),
   court("Donne deux raisons pour lesquelles quelques centaines de conquistadors l'emportent.", "chevaux, armes en acier et armes à feu, alliés amérindiens, maladies (deux au choix)"),
   court("Qu'est-ce qu'un empire colonial ?", "l'ensemble des territoires lointains dominés et exploités par un pays")]
 },
 "etudes_documents": {
  "CM1": [
   {"titre": "Le carnet de route de la Rose des vents", "document": {"contenu": "1492 : Colomb arrive aux Antilles pour l'Espagne. 1498 : Vasco de Gama arrive en Inde. 1519-1522 : l'expédition de Magellan et Elcano fait le tour du monde. 1534 : Cartier arrive au Canada.", "source": "Résumé de la leçon 3 du jeu (inventé pour le jeu)."},
    "questions": [court("Quel voyage est le plus ancien ?", "celui de Colomb, en 1492"),
                  court("Combien d'années dure le premier tour du monde ?", "environ 3 ans (1519-1522)"),
                  court("Quel explorateur part pour le roi de France ?", "Jacques Cartier")]},
   {"titre": "Le tableau des colonies", "document": {"contenu": "Espagne : Mexique et Pérou, mines d'argent. Portugal : Brésil, canne à sucre. France : Nouvelle-France, fourrures. Angleterre : Amérique du Nord.", "source": "Résumé de la leçon 5 du jeu."},
    "questions": [court("Quel pays exploite des mines d'argent ?", "l'Espagne"),
                  court("Quelle est la colonie du Portugal ?", "le Brésil"),
                  court("Que fait-on en Nouvelle-France ?", "le commerce des fourrures")]}],
  "CM2": [
   {"titre": "Le traité de Tordesillas, expliqué simplement", "document": {"contenu": "Le 7 juin 1494, les rois d'Espagne et du Portugal signent un accord. Une ligne imaginaire est tracée du nord au sud, à 370 lieues à l'ouest des îles du Cap-Vert. Les terres découvertes à l'ouest de la ligne seront espagnoles ; celles de l'est, portugaises.", "source": "Reformulation pour le cycle 3 (document de la leçon 5 du jeu)."},
    "questions": [court("Quels pays signent ce traité ?", "l'Espagne et le Portugal"),
                  court("À qui reviennent les terres à l'ouest de la ligne ?", "à l'Espagne"),
                  court("Pourquoi le Brésil devient-il portugais ?", "parce qu'il dépasse la ligne vers l'est")]},
   {"titre": "Le dernier navire", "document": {"contenu": "En 1519, cinq navires et environ 250 hommes partent d'Espagne avec Magellan pour atteindre l'Asie par l'ouest. Magellan est tué aux Philippines en 1521. Le 6 septembre 1522, Elcano ramène en Espagne le dernier navire, la Victoria, avec 18 hommes.", "source": "Résumé de la leçon 3 du jeu."},
    "questions": [court("Combien de navires reviennent ?", "un seul, la Victoria"),
                  court("Qui termine l'expédition ?", "Juan Sebastián Elcano"),
                  court("Que prouve ce voyage ?", "qu'on peut faire le tour de la Terre par la mer")]}]
 }
}

with open(os.path.join(JEU, "assets", "data", "evaluations.json"), "w", encoding="utf-8", newline="\n") as f:
    json.dump(EVAL, f, ensure_ascii=False, indent=1); f.write("\n")
with open(os.path.join(JEU, "assets", "data", "evaluations-embarquees.js"), "w", encoding="utf-8", newline="\n") as f:
    f.write("/* FICHIER GÉNÉRÉ par grandes-explorations/outils/generer-evaluations.py — ne pas modifier à la main. */\n")
    f.write("window.EVAL_EMBARQUEES = "); json.dump(EVAL, f, ensure_ascii=False, separators=(",", ":")); f.write(";\n")
n = {k: {niv: len(v[niv]) for niv in v} for k, v in EVAL.items() if k in ("qcm", "questions_fermees", "etudes_documents")}
print("évaluations écrites :", n)
