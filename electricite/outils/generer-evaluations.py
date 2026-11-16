#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les évaluations imprimables de « La Centrale en panne » (jeu n°14, électricité).

    python electricite/outils/generer-evaluations.py

Écrit electricite/assets/data/evaluations.json (format commun des jeux) et
electricite/assets/data/evaluations-embarquees.js (copie lue en double-clic, file://).
Page d'impression : electricite/evaluations-imprimables.html.
Tous les faits viennent des leçons du jeu (assets/data/lecons.json) ; chiffres RTE, Bilan électrique 2025.
"""
import json, os
ICI = os.path.dirname(os.path.abspath(__file__))
JEU = os.path.dirname(ICI)

def q(texte, options, bonne): return {"q": texte, "options": options, "bonne": bonne, "pts": 1}
def vf(texte, rep): return {"q": texte, "type": "vf", "bonne": rep, "pts": 1}
def court(texte, rep): return {"q": texte, "type": "court", "rep": rep, "pts": 1}

EVAL = {
 "metadata": {
  "sujet": "Le circuit électrique, conducteurs et isolants, le schéma normalisé, la sécurité électrique, produire et transporter l'électricité",
  "niveaux": ["CM1", "CM2"],
  "programme": "Sciences et technologie, cycle 3 — « Signaux » : l'électricité (BO n° 24 du 11 juin 2026), CM2. Progression de l'enseignant : année A, période 3 (« L'électricité »). En CM1, on reste sur le circuit à une boucle, les matériaux et la sécurité.",
  "sources": "Leçons du jeu (assets/data/lecons.json) ; RTE, Bilan électrique 2025. Voir README.md du jeu, section Sources."
 },
 "quizz_final": {
  "CM1": [
   q("Pour que la lampe brille, le circuit doit être...", ["ouvert", "fermé", "coupé"], 1),
   q("Lequel de ces matériaux est conducteur ?", ["le cuivre", "le plastique", "le bois"], 0),
   q("Sur un schéma, un cercle avec une croix représente...", ["la pile", "le moteur", "la lampe"], 2),
   q("La pile de la classe (4,5 V) est...", ["sans danger", "dangereuse", "interdite"], 0),
   q("Quelle source d'énergie est renouvelable ?", ["le charbon", "le vent", "l'uranium"], 1)],
  "CM2": [
   q("Deux lampes sont dans la même boucle. On dévisse l'une : l'autre...", ["reste allumée", "brille plus fort", "s'éteint"], 2),
   q("La mine d'un crayon à papier (graphite)...", ["conduit le courant", "est un isolant", "est un métal"], 0),
   q("Pour lire un schéma, on suit le courant...", ["de la lampe à l'interrupteur", "de la borne + à la borne − de la pile", "au hasard"], 1),
   q("Une personne est électrisée. On commence par...", ["la tirer par le bras", "lui jeter de l'eau", "couper le courant au disjoncteur"], 2),
   q("En 2025, la plus grande partie de l'électricité française vient...", ["du nucléaire", "du solaire", "du gaz"], 0)]
 },
 "fiches_preparatoires": [
  {"salle": 1, "titre": "L'atelier du club sciences — le circuit électrique",
   "objectifs": ["Nommer les éléments d'un circuit : pile, lampe, interrupteur, fils", "Distinguer circuit ouvert et circuit fermé"],
   "vocabulaire": [{"mot": "circuit", "def": "chemin fermé que suit le courant électrique"}, {"mot": "borne", "def": "point où l'on branche un fil sur une pile ou une lampe"}, {"mot": "interrupteur", "def": "dispositif qui ouvre ou ferme le circuit"}],
   "contexte": "La lampe ne brille que si le courant fait une boucle complète, d'une borne de la pile à l'autre."},
  {"salle": 2, "titre": "Le magasin de matériel — conducteurs et isolants",
   "objectifs": ["Trier des matériaux conducteurs et isolants", "Utiliser un circuit testeur"],
   "vocabulaire": [{"mot": "conducteur", "def": "matériau qui laisse passer le courant"}, {"mot": "isolant", "def": "matériau qui ne laisse pas passer le courant"}, {"mot": "gaine", "def": "enveloppe isolante autour d'un fil"}],
   "contexte": "On place l'objet dans la boucle du circuit testeur : si la lampe s'allume, l'objet est conducteur."},
  {"salle": 3, "titre": "La salle de contrôle — le schéma électrique",
   "objectifs": ["Reconnaître les symboles normalisés", "Passer du dessin au schéma"],
   "vocabulaire": [{"mot": "schéma", "def": "dessin simplifié qui utilise des symboles"}, {"mot": "symbole", "def": "signe qui représente un objet"}, {"mot": "normalisé", "def": "fait selon une règle commune à tous"}],
   "contexte": "Pile : un grand trait et un petit trait. Lampe : un cercle avec une croix. Moteur : un cercle avec un M. Interrupteur ouvert : un trait levé."},
  {"salle": 4, "titre": "La maison témoin — la sécurité électrique",
   "objectifs": ["Distinguer la pile, sans danger, et le secteur, dangereux", "Connaître les gestes de sécurité et d'économie"],
   "vocabulaire": [{"mot": "secteur", "def": "courant électrique des prises de la maison"}, {"mot": "disjoncteur", "def": "appareil qui coupe le courant de la maison"}, {"mot": "veille", "def": "appareil éteint mais encore branché, qui consomme un peu"}],
   "contexte": "On ne fait jamais d'expérience avec une prise : le courant du secteur (230 volts) peut tuer."},
  {"salle": 5, "titre": "Le poste de conduite du réseau — produire et transporter l'électricité",
   "objectifs": ["Nommer des centrales électriques", "Décrire le trajet de l'électricité jusqu'à la prise"],
   "vocabulaire": [{"mot": "centrale", "def": "usine qui produit de l'électricité"}, {"mot": "renouvelable", "def": "qui ne s'épuise pas : vent, eau, Soleil"}, {"mot": "pylône", "def": "grand support métallique des lignes électriques"}],
   "contexte": "Centrale, transformateur, lignes à très haute tension, poste, réseau de la ville, compteur, prise."}
 ],
 "qcm": {
  "CM1": [
   q("Dans un circuit, la pile a...", ["une seule borne", "deux bornes : + et −", "trois bornes"], 1),
   q("Un fil est débranché : le circuit est...", ["ouvert", "fermé", "plus puissant"], 0),
   q("L'interrupteur sert à...", ["faire briller la lampe plus fort", "user la pile", "ouvrir ou fermer le circuit"], 2),
   q("Lequel de ces objets est isolant ?", ["une clé en fer", "une règle en plastique", "un trombone"], 1),
   q("Le cœur d'un fil électrique est en...", ["cuivre", "verre", "bois"], 0),
   q("Sur un schéma, le moteur est représenté par...", ["un cercle avec une croix", "un trait levé", "un cercle avec un M"], 2),
   q("Les fils d'un schéma sont dessinés...", ["en traits droits", "en vagues", "en pointillés"], 0),
   q("Le courant des prises de la maison est...", ["sans danger", "dangereux", "le même que celui d'une pile"], 1),
   q("Pour débrancher un appareil, on tire sur...", ["le fil", "l'appareil", "la fiche"], 2),
   q("Dans une éolienne, ce qui fait tourner les pales, c'est...", ["le vent", "l'eau", "la vapeur"], 0)],
  "CM2": [
   q("Une pile, une lampe et des fils : la pile est...", ["un récepteur", "le générateur", "un isolant"], 1),
   q("On relie directement les deux bornes de la pile par un fil. C'est...", ["un circuit en dérivation", "un interrupteur", "un court-circuit"], 2),
   q("Ce qui s'use peu à peu dans un circuit, c'est...", ["la pile", "le courant", "la lampe"], 0),
   q("Lequel de ces matériaux conduit le courant ?", ["le verre", "le caoutchouc", "l'aluminium"], 2),
   q("Quand l'interrupteur est ouvert, ce qui coupe la boucle, c'est...", ["du plastique", "une couche d'air", "du cuivre"], 1),
   q("Sur le symbole de la pile, le grand trait représente...", ["la borne +", "la borne −", "l'interrupteur"], 0),
   q("Deux schémas sont équivalents si...", ["les appareils sont dessinés à la même place", "ils ont la même couleur", "les appareils sont reliés de la même façon"], 2),
   q("La tension du secteur en France est de...", ["4,5 volts", "230 volts", "12 volts"], 1),
   q("Une lampe à LED, comparée à une ancienne lampe à incandescence...", ["consomme beaucoup moins", "consomme plus", "n'éclaire pas"], 0),
   q("Dans une centrale nucléaire, la chaleur sert à...", ["faire de la vapeur qui fait tourner la turbine", "charger des piles", "chauffer les maisons"], 0),
   q("Les panneaux solaires photovoltaïques...", ["font tourner une turbine", "transforment directement la lumière en électricité", "brûlent du gaz"], 1),
   q("Près des villes, les postes de transformation...", ["produisent l'électricité", "stockent l'électricité", "abaissent la tension"], 2)]
 },
 "questions_fermees": {
  "CM1": [
   vf("Une lampe peut briller avec un seul fil branché à la pile.", "faux"),
   vf("Les métaux sont conducteurs.", "vrai"),
   vf("Le bois sec laisse passer le courant.", "faux"),
   vf("Sur un schéma, on remplace les objets par des symboles.", "vrai"),
   vf("On peut faire des expériences avec une prise de courant.", "faux"),
   court("Cite les trois éléments d'un circuit simple.", "une pile, une lampe (ou un moteur) et des fils"),
   court("Que faire si une personne est électrisée ?", "ne pas la toucher, couper le courant, appeler le 18 ou le 112"),
   court("Cite une source d'énergie renouvelable.", "l'eau, le vent ou le Soleil")],
  "CM2": [
   vf("En dérivation, chaque lampe a sa propre boucle reliée à la pile.", "vrai"),
   vf("Le courant s'use en traversant la lampe.", "faux"),
   vf("L'eau du robinet conduit le courant du secteur.", "vrai"),
   vf("L'électricité se stocke très facilement.", "faux"),
   court("Pourquoi la gaine d'un fil électrique est-elle en plastique ?", "parce que le plastique est isolant : il protège les personnes"),
   court("Explique la différence entre électrisation et électrocution.", "l'électrisation est le passage du courant dans le corps ; l'électrocution est une électrisation mortelle"),
   court("Quelle machine produit le courant quand une turbine la fait tourner ?", "l'alternateur"),
   court("Donne deux gestes pour économiser l'électricité.", "éteindre la lumière en quittant une pièce ; ne pas laisser les appareils en veille (ou utiliser des lampes à LED)")]
 },
 "etudes_documents": {
  "CM1": [
   {"titre": "Le cahier de tests de Maëlle", "document": {"contenu": "Objets placés dans le circuit testeur. Clé en fer : la lampe s'allume. Gomme : la lampe reste éteinte. Cuillère en métal : la lampe s'allume. Cuillère en bois : la lampe reste éteinte.", "source": "Résultats inventés pour le jeu, conformes à la leçon 2."},
    "questions": [court("Quels objets sont conducteurs ?", "la clé en fer et la cuillère en métal"),
                  court("Quels objets sont isolants ?", "la gomme et la cuillère en bois"),
                  court("Que montrent les deux cuillères ?", "un même objet peut être conducteur ou isolant selon son matériau")]},
   {"titre": "L'affiche de la maison témoin", "document": {"contenu": "Ne jamais mettre un objet dans une prise. Ne jamais toucher un appareil avec les mains mouillées. Tirer sur la fiche, pas sur le fil. Ne pas jouer près des lignes électriques.", "source": "Règles de la leçon 4 du jeu."},
    "questions": [court("Pourquoi ne faut-il pas toucher un appareil avec les mains mouillées ?", "parce que l'eau conduit le courant du secteur, qui est dangereux"),
                  court("Combien de volts y a-t-il dans une prise de la maison ?", "230 volts"),
                  court("Ajoute une règle de sécurité à l'affiche.", "par exemple : ne jamais grimper sur un pylône")]}],
  "CM2": [
   {"titre": "La production d'électricité en France en 2025", "document": {"contenu": "Production totale : 547,5 milliards de kilowattheures (TWh). Nucléaire : 373 TWh (68 %). Hydraulique : 62,4 TWh (11 %). Éolien : 49,6 TWh (9 %). Solaire : 32,9 TWh (6 %). Gaz : environ 3 %.", "source": "RTE, Bilan électrique 2025, d'après Connaissance des énergies."},
    "questions": [court("Quelle source produit le plus d'électricité en France ?", "le nucléaire (68 %)"),
                  court("Additionne les parts de l'hydraulique, de l'éolien et du solaire.", "11 + 9 + 6 = 26 %"),
                  court("Ces trois sources sont-elles renouvelables ? Pourquoi ?", "oui : l'eau, le vent et le Soleil ne s'épuisent pas")]},
   {"titre": "Le schéma d'Hélène", "document": {"contenu": "Un rectangle de fils. Sur le côté gauche, une pile. En haut, une lampe. À droite, un interrupteur dessiné par un trait levé. En bas, un moteur.", "source": "Description d'un schéma inventé pour le jeu."},
    "questions": [court("La lampe brille-t-elle ? Pourquoi ?", "non : l'interrupteur est ouvert, la boucle est coupée"),
                  court("Le moteur tourne-t-il ?", "non, il est dans la même boucle"),
                  court("Que faut-il faire pour que la lampe et le moteur fonctionnent ?", "fermer l'interrupteur (trait couché)")]}]
 }
}

with open(os.path.join(JEU, "assets", "data", "evaluations.json"), "w", encoding="utf-8", newline="\n") as f:
    json.dump(EVAL, f, ensure_ascii=False, indent=1); f.write("\n")
with open(os.path.join(JEU, "assets", "data", "evaluations-embarquees.js"), "w", encoding="utf-8", newline="\n") as f:
    f.write("/* FICHIER GÉNÉRÉ par electricite/outils/generer-evaluations.py — ne pas modifier à la main. */\n")
    f.write("window.EVAL_EMBARQUEES = "); json.dump(EVAL, f, ensure_ascii=False, separators=(",", ":")); f.write(";\n")
n = {k: {niv: len(v[niv]) for niv in v} for k, v in EVAL.items() if k in ("qcm", "questions_fermees", "etudes_documents")}
print("évaluations écrites :", n)
