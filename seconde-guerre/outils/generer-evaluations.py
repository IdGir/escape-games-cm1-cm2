#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les évaluations imprimables de « Radio Londres » (jeu n°20, Seconde Guerre mondiale).
JEU TRÈS SENSIBLE : relecture obligatoire avant la classe.

    python seconde-guerre/outils/generer-evaluations.py

Écrit seconde-guerre/assets/data/evaluations.json (format commun des jeux) et
seconde-guerre/assets/data/evaluations-embarquees.js (copie lue en double-clic, file://).
Page d'impression : seconde-guerre/evaluations-imprimables.html.
Tous les faits et chiffres viennent des leçons du jeu (assets/data/lecons.json). Comme dans le jeu,
AUCUNE question notée ne porte sur les persécutions ni sur la Shoah : la fiche préparatoire 3 renvoie
à la leçon et à la discussion en classe. Aucun personnage réel ne parle ; aucun texte historique n'est
cité (les documents sont des repères tirés des leçons).
"""
import json, os
ICI = os.path.dirname(os.path.abspath(__file__))
JEU = os.path.dirname(ICI)

def q(texte, options, bonne): return {"q": texte, "options": options, "bonne": bonne, "pts": 1}
def vf(texte, rep): return {"q": texte, "type": "vf", "bonne": rep, "pts": 1}
def court(texte, rep): return {"q": texte, "type": "court", "rep": rep, "pts": 1}

EVAL = {
 "metadata": {
  "sujet": "La Seconde Guerre mondiale : la montée des dictatures, la défaite de 1940 et Vichy, la vie sous l'Occupation, la Résistance, la Libération et la victoire",
  "niveaux": ["CM1", "CM2"],
  "programme": "Histoire, cycle 3 — la Seconde Guerre mondiale (programme 2026, BO n° 22 du 28 mai 2026). Progression de l'enseignant : thème 6, année A, période 5. Repères en CM1, dates exactes en CM2.",
  "sources": "Leçons du jeu (assets/data/lecons.json) ; ministère des Armées (Chemins de mémoire), Ordre de la Libération, Fondation de la Résistance, Mémorial de Caen ; voir README.md et A-VERIFIER.md du jeu."
 },
 "quizz_final": {
  "CM1": [
   q("En quelle année commence une grave crise économique mondiale ?", ["1929", "1945", "1914"], 0),
   q("Le 18 juin 1940, depuis Londres, le général de Gaulle...", ["signe l'armistice", "appelle à continuer le combat", "devient chef du gouvernement de Vichy"], 1),
   q("Sous l'Occupation, pour acheter du pain, il faut...", ["une carte d'électeur", "un billet de train", "des tickets de rationnement"], 2),
   q("Qui réunit les mouvements de résistance en 1943 ?", ["Jean Moulin", "le maréchal Pétain", "Mussolini"], 0),
   q("Le 8 mai 1945...", ["les Alliés débarquent en Normandie", "l'Allemagne nazie capitule", "Paris est occupé"], 1)],
  "CM2": [
   q("Hitler devient chancelier de l'Allemagne le...", ["30 janvier 1933", "1er septembre 1939", "22 juin 1940"], 0),
   q("L'armistice de 1940 est signé le 22 juin à...", ["Vichy", "Londres", "Rethondes"], 2),
   q("La loi qui crée le STO date du...", ["10 juillet 1940", "16 février 1943", "6 juin 1944"], 1),
   q("Le Conseil national de la Résistance se réunit pour la première fois le...", ["27 mai 1943", "25 août 1944", "18 juin 1940"], 0),
   q("Paris est libéré le...", ["6 juin 1944", "8 mai 1945", "25 août 1944"], 2)]
 },
 "fiches_preparatoires": [
  {"salle": 1, "titre": "Fréquence 1, 1938 — La classe de Bastien : la montée des dictatures",
   "objectifs": ["Expliquer les effets de la crise de 1929", "Distinguer une démocratie d'une dictature"],
   "vocabulaire": [{"mot": "crise économique", "def": "période où les usines ferment et où beaucoup de gens perdent leur travail"}, {"mot": "dictature", "def": "régime où un chef ou un parti a tous les pouvoirs, sans liberté"}, {"mot": "démocratie", "def": "régime où les citoyens choisissent librement leurs dirigeants"}],
   "contexte": "Après la crise de 1929, des dictateurs prennent tout le pouvoir : Mussolini en Italie, Hitler en Allemagne, Staline en URSS. La France et le Royaume-Uni restent des démocraties, mais la paix est menacée."},
  {"salle": 2, "titre": "Fréquence 2, juin 1940 — La gare de Paul : la défaite et Vichy",
   "objectifs": ["Dater le début de la guerre et la défaite de 1940", "Expliquer l'appel du 18 juin, l'armistice et le régime de Vichy"],
   "vocabulaire": [{"mot": "exode", "def": "fuite de millions de personnes sur les routes en mai et juin 1940"}, {"mot": "armistice", "def": "accord qui arrête les combats"}, {"mot": "collaboration", "def": "politique qui consiste à aider l'Allemagne nazie"}],
   "contexte": "En 1940, l'armée française est battue. Le 18 juin, le général de Gaulle appelle à continuer le combat. L'armistice coupe la France en deux ; à Vichy, Pétain supprime la République et collabore avec l'Allemagne nazie."},
  {"salle": 3, "titre": "Fréquence 3, 1942-1943 — L'épicerie de Madeleine : vivre sous l'Occupation",
   "objectifs": ["Décrire la vie quotidienne : rationnement, tickets, queues, ersatz", "Savoir ce qu'est le STO"],
   "vocabulaire": [{"mot": "rationnement", "def": "limitation de ce que chacun a le droit d'acheter"}, {"mot": "ersatz", "def": "produit qui en remplace un autre qui manque"}, {"mot": "STO", "def": "Service du travail obligatoire : travail forcé en Allemagne, créé en 1943"}],
   "contexte": "La nourriture, le charbon et les vêtements manquent : il faut des tickets pour acheter. À partir de 1943, des jeunes doivent partir travailler en Allemagne. La leçon parle aussi des persécutions contre les Juifs, de la Shoah et des Justes : on en parle ensemble en classe, sans question notée."},
  {"salle": 4, "titre": "Fréquence 4, 1944 — Le maquis de Marc : la Résistance",
   "objectifs": ["Expliquer ce que veut dire résister", "Citer des formes de la Résistance et le rôle de Jean Moulin"],
   "vocabulaire": [{"mot": "résistant", "def": "personne qui lutte contre l'occupant et la collaboration"}, {"mot": "clandestin", "def": "fait en cachette, interdit par l'occupant"}, {"mot": "maquis", "def": "groupe de résistants cachés dans la forêt ou la montagne"}],
   "contexte": "Des Français refusent la défaite : journaux clandestins, réseaux, messages de Radio Londres, maquis comme dans le Morvan. En 1943, Jean Moulin réunit les mouvements dans le Conseil national de la Résistance."},
  {"salle": 5, "titre": "Fréquence 5, 8 mai 1945 — La place de la mairie de Lucie : la Libération",
   "objectifs": ["Dater les débarquements, la libération de Paris et la victoire", "Expliquer le retour de la République et le vote des femmes"],
   "vocabulaire": [{"mot": "débarquement", "def": "arrivée d'une armée par la mer sur une côte"}, {"mot": "Libération", "def": "fin de l'occupation allemande en France, en 1944"}, {"mot": "capitulation", "def": "reddition sans condition d'une armée vaincue"}],
   "contexte": "Le 6 juin 1944, les Alliés débarquent en Normandie ; Paris est libéré le 25 août 1944. Le 8 mai 1945, l'Allemagne nazie capitule. La République est rétablie et les femmes votent."}
 ],
 "qcm": {
  "CM1": [
   q("Où commence la crise économique de 1929 ?", ["aux États-Unis", "en France", "en Italie"], 0),
   q("Qui dirige l'Allemagne nazie ?", ["Mussolini", "Hitler", "Staline"], 1),
   q("Dans une dictature...", ["on vote librement", "les journaux sont libres", "il n'y a pas de liberté"], 2),
   q("En septembre 1939, l'Allemagne envahit...", ["la Pologne", "l'Angleterre", "l'Espagne"], 0),
   q("La fuite de millions de Français sur les routes en 1940 s'appelle...", ["la Libération", "l'exode", "la mobilisation"], 1),
   q("Après l'armistice de 1940, Pétain gouverne depuis...", ["Londres", "Paris", "Vichy"], 2),
   q("Un ersatz, c'est...", ["un produit qui en remplace un autre qui manque", "un ticket de rationnement", "un soldat allemand"], 0),
   q("Que font les jeunes qui refusent le STO et se cachent dans les forêts ?", ["ils partent en vacances", "ils forment des maquis", "ils deviennent policiers"], 1),
   q("Le soir, les résistants écoutent des messages codés sur...", ["la télévision", "le téléphone", "Radio Londres"], 2),
   q("Le 6 juin 1944, les Alliés débarquent en...", ["Normandie", "Bourgogne", "Provence"], 0)],
  "CM2": [
   q("En octobre 1929...", ["la Bourse de New York s'effondre", "Hitler devient chancelier", "la guerre commence"], 0),
   q("Un régime totalitaire, c'est une dictature qui...", ["organise des élections libres", "veut contrôler toute la vie des habitants", "laisse les journaux libres"], 1),
   q("Mussolini, chef du parti fasciste, prend le pouvoir en Italie en...", ["1933", "1938", "1922"], 2),
   q("Le 3 septembre 1939, le Royaume-Uni et la France...", ["déclarent la guerre à l'Allemagne", "signent l'armistice", "débarquent en Normandie"], 0),
   q("Pendant les huit mois de la « drôle de guerre »...", ["Paris est occupé", "il y a peu de combats à l'ouest", "les Alliés débarquent"], 1),
   q("L'armée allemande entre dans Paris le...", ["18 juin 1940", "22 juin 1940", "14 juin 1940"], 2),
   q("Le 10 juillet 1940, les députés et les sénateurs...", ["donnent les pleins pouvoirs à Pétain", "votent la guerre", "rétablissent la République"], 0),
   q("La devise du régime de Vichy est...", ["« Liberté, Égalité, Fraternité »", "« Travail, Famille, Patrie »", "« Les Français parlent aux Français »"], 1),
   q("Les résistants sont...", ["la majorité des Français dès 1940", "des soldats allemands", "une minorité courageuse, qui grandit à partir de 1943"], 2),
   q("Jean Moulin est arrêté près de Lyon le...", ["21 juin 1943", "27 mai 1943", "6 juin 1944"], 0),
   q("Le 15 août 1944, des troupes alliées, dont l'armée française, débarquent en...", ["Normandie", "Provence", "Bretagne"], 1),
   q("La guerre se termine dans le monde le 2 septembre 1945, avec la capitulation...", ["de l'Italie", "de l'Allemagne", "du Japon"], 2)]
 },
 "questions_fermees": {
  "CM1": [
   vf("La France et le Royaume-Uni restent des démocraties avant la guerre.", "vrai"),
   vf("Le général de Gaulle lance son appel depuis Vichy.", "faux"),
   vf("Après l'armistice, la France est coupée en deux.", "vrai"),
   vf("Sous l'Occupation, on trouve de tout dans les magasins.", "faux"),
   vf("Les résistants risquent leur vie.", "vrai"),
   court("Que veut dire « collaborer » avec l'Allemagne nazie ?", "aider l'Allemagne nazie"),
   court("Cite deux actions des résistants.", "par exemple : imprimer des journaux clandestins, transmettre des informations aux Alliés, cacher des personnes recherchées, écouter Radio Londres"),
   court("Quel droit les femmes obtiennent-elles à la Libération ?", "le droit de vote")],
  "CM2": [
   vf("Le régime de Vichy est une dictature : il n'y a plus d'élections.", "vrai"),
   vf("L'armistice est signé le 18 juin 1940.", "faux"),
   vf("En France, écouter Radio Londres est interdit.", "vrai"),
   vf("Dijon est libérée le même jour que Paris.", "faux"),
   court("Qu'est-ce que la ligne de démarcation ?", "la frontière intérieure entre la zone occupée et la zone non occupée"),
   court("Qu'est-ce que le marché noir ?", "un commerce caché, à des prix très élevés"),
   court("À quoi servent les messages personnels de Radio Londres ?", "ce sont des ordres codés pour les résistants"),
   court("Pourquoi les pays vainqueurs créent-ils l'ONU en 1945 ?", "pour maintenir la paix, pour que la guerre ne recommence pas")]
 },
 "etudes_documents": {
  "CM1": [
   {"titre": "Radio Londres", "document": {"contenu": "Chaque soir, la radio de Londres, la BBC, diffuse l'émission « Les Français parlent aux Français ». Après les nouvelles viennent les messages personnels : des phrases étranges, qui sont des ordres codés pour les résistants. En France, écouter Radio Londres est interdit.", "source": "D'après la leçon 4 du jeu."},
    "questions": [court("Depuis quelle ville parle Radio Londres ?", "depuis Londres"),
                  court("Pourquoi les messages personnels ont-ils l'air étranges ?", "parce que ce sont des ordres codés pour les résistants"),
                  court("Écouter Radio Londres est-il permis en France occupée ?", "non, c'est interdit")]},
   {"titre": "Les repères de la guerre", "document": {"contenu": "1929 : début d'une grave crise économique. Septembre 1939 : début de la guerre. Juin 1940 : défaite de la France et appel du général de Gaulle. 1943 : STO ; Jean Moulin réunit la Résistance. 6 juin 1944 : débarquement de Normandie. 25 août 1944 : libération de Paris. 8 mai 1945 : capitulation de l'Allemagne nazie.", "source": "D'après les leçons du jeu."},
    "questions": [court("En quelle année commence la Seconde Guerre mondiale ?", "en 1939"),
                  court("Qu'arrive-t-il le 6 juin 1944 ?", "les Alliés débarquent en Normandie"),
                  court("Combien d'années la guerre a-t-elle duré environ en Europe ?", "près de six ans (de 1939 à 1945)")]}],
  "CM2": [
   {"titre": "Juin 1940, jour après jour", "document": {"contenu": "10 mai 1940 : l'armée allemande attaque à l'ouest. 14 juin : l'armée allemande entre dans Paris. 17 juin : le maréchal Pétain annonce à la radio qu'il faut cesser le combat. 18 juin : depuis Londres, le général de Gaulle appelle à la radio de la BBC à continuer le combat. 22 juin : armistice signé à Rethondes. 10 juillet : les députés et les sénateurs donnent les pleins pouvoirs à Pétain.", "source": "D'après la leçon 2 du jeu."},
    "questions": [court("Combien de jours séparent l'annonce de Pétain et l'appel du général de Gaulle ?", "un jour (17 et 18 juin 1940)"),
                  court("Pétain et de Gaulle font-ils le même choix ? Explique.", "non : Pétain veut cesser le combat, de Gaulle veut le continuer"),
                  court("Que devient la République après le 10 juillet 1940 ?", "elle est remplacée par l'État français de Vichy, une dictature")]},
   {"titre": "La Libération", "document": {"contenu": "Les jours qui précèdent le 6 juin 1944, Radio Londres diffuse des vers de Verlaine pour prévenir les résistants. 6 juin 1944 : débarquement de Normandie, le Jour J. 15 août 1944 : débarquement de Provence. 25 août 1944 : Paris est libéré par la 2e division blindée du général Leclerc, les Alliés et les résistants. 11 septembre 1944 : Dijon est libérée. 8 mai 1945 : l'Allemagne nazie capitule.", "source": "D'après la leçon 5 du jeu."},
    "questions": [court("Pourquoi Radio Londres diffuse-t-elle des vers de Verlaine avant le 6 juin 1944 ?", "pour prévenir les résistants que le débarquement approche"),
                  court("Qui libère Paris ? Cite deux acteurs.", "la 2e division blindée du général Leclerc, les Alliés, les résistants"),
                  court("Combien de temps sépare le débarquement de Normandie de la capitulation de l'Allemagne ?", "environ onze mois (du 6 juin 1944 au 8 mai 1945)")]}]
 }
}

with open(os.path.join(JEU, "assets", "data", "evaluations.json"), "w", encoding="utf-8", newline="\n") as f:
    json.dump(EVAL, f, ensure_ascii=False, indent=1); f.write("\n")
with open(os.path.join(JEU, "assets", "data", "evaluations-embarquees.js"), "w", encoding="utf-8", newline="\n") as f:
    f.write("/* FICHIER GÉNÉRÉ par seconde-guerre/outils/generer-evaluations.py — ne pas modifier à la main. */\n")
    f.write("window.EVAL_EMBARQUEES = "); json.dump(EVAL, f, ensure_ascii=False, separators=(",", ":")); f.write(";\n")
n = {k: {niv: len(v[niv]) for niv in v} for k, v in EVAL.items() if k in ("qcm", "questions_fermees", "etudes_documents")}
print("évaluations écrites :", n)
