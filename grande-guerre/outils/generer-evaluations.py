#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les évaluations imprimables des « Lettres du poilu » (jeu n°19, Première Guerre mondiale).
JEU SENSIBLE : relecture obligatoire avant la classe.

    python grande-guerre/outils/generer-evaluations.py

Écrit grande-guerre/assets/data/evaluations.json (format commun des jeux) et
grande-guerre/assets/data/evaluations-embarquees.js (copie lue en double-clic, file://).
Page d'impression : grande-guerre/evaluations-imprimables.html.
Tous les faits et chiffres viennent des leçons du jeu (assets/data/lecons.json, chiffres officiels
du ministère des Armées). Les lettres marquées « inventée pour le jeu » sont celles des personnages
fictifs du village de Vaux-les-Tilleuls. Aucune question sur la violence des combats.
"""
import json, os
ICI = os.path.dirname(os.path.abspath(__file__))
JEU = os.path.dirname(ICI)

def q(texte, options, bonne): return {"q": texte, "options": options, "bonne": bonne, "pts": 1}
def vf(texte, rep): return {"q": texte, "type": "vf", "bonne": rep, "pts": 1}
def court(texte, rep): return {"q": texte, "type": "court", "rep": rep, "pts": 1}

EVAL = {
 "metadata": {
  "sujet": "La Première Guerre mondiale : l'entrée en guerre, le front et les tranchées, l'arrière, l'armistice et la paix, la mémoire et une paix fragile",
  "niveaux": ["CM1", "CM2"],
  "programme": "Histoire, cycle 3 — la Première Guerre mondiale (programme 2026, BO n° 22 du 28 mai 2026). Progression de l'enseignant : thème 6, année A, période 5. Repères en CM1, dates exactes et chiffres officiels en CM2.",
  "sources": "Leçons du jeu (assets/data/lecons.json) ; ministère des Armées (Chemins de mémoire), musée de l'Armée ; voir README.md et A-VERIFIER.md du jeu."
 },
 "quizz_final": {
  "CM1": [
   q("En quelle année commence la Première Guerre mondiale ?", ["1914", "1918", "1870"], 0),
   q("Comment appelle-t-on les soldats français de la Grande Guerre ?", ["les mousquetaires", "les poilus", "les tirailleurs du roi"], 1),
   q("Les ouvrières qui fabriquent des obus s'appellent...", ["les infirmières", "les factrices", "les munitionnettes"], 2),
   q("Quel jour l'armistice est-il signé ?", ["le 14 juillet 1918", "le 11 novembre 1918", "le 1er août 1914"], 1),
   q("Sur le monument aux morts, on grave...", ["les noms des soldats de la commune morts pour la France", "les noms des maires", "les dates des fêtes du village"], 0)],
  "CM2": [
   q("Où l'archiduc François-Ferdinand est-il assassiné le 28 juin 1914 ?", ["à Verdun", "à Sarajevo", "à Versailles"], 1),
   q("La bataille de Verdun a lieu en...", ["1914", "1918", "1916"], 2),
   q("En 1918, environ combien de femmes travaillent dans les usines d'armement ?", ["430 000", "4 300", "43 millions"], 0),
   q("Le traité de Versailles est signé le...", ["11 novembre 1918", "3 août 1914", "28 juin 1919"], 2),
   q("En 1922, en Italie, Mussolini...", ["prend le pouvoir et supprime peu à peu les libertés", "signe l'armistice", "devient roi de France"], 0)]
 },
 "fiches_preparatoires": [
  {"salle": 1, "titre": "Lettre n°1, août 1914 — La place du village : l'entrée en guerre",
   "objectifs": ["Expliquer pourquoi les pays d'Europe entrent en guerre", "Situer l'attentat de Sarajevo et la mobilisation générale"],
   "vocabulaire": [{"mot": "alliance", "def": "accord entre des pays qui promettent de s'aider en cas de guerre"}, {"mot": "mobilisation", "def": "appel des hommes en âge de combattre pour qu'ils rejoignent l'armée"}, {"mot": "propagande", "def": "images et textes qui cherchent à influencer l'opinion"}],
   "contexte": "En 1914, deux alliances se font face. Après l'attentat de Sarajevo, les pays entrent en guerre les uns après les autres ; l'affiche de la mobilisation générale est collée dans chaque commune."},
  {"salle": 2, "titre": "Lettre n°2, 1916 — L'abri de tranchée : le front",
   "objectifs": ["Décrire une tranchée et la vie des poilus", "Situer les batailles de Verdun et de la Somme"],
   "vocabulaire": [{"mot": "tranchée", "def": "fossé creusé pour se protéger, où vivent les soldats du front"}, {"mot": "front", "def": "ligne où les armées se font face et combattent"}, {"mot": "censure", "def": "contrôle des lettres et des journaux par les autorités"}],
   "contexte": "De la mer du Nord à la Suisse, les armées vivent dans les tranchées. Les poilus tiennent grâce aux lettres, aux colis et à la camaraderie. En 1916 : Verdun et la Somme."},
  {"salle": 3, "titre": "Lettre n°3, 1917 — L'usine d'obus : l'arrière",
   "objectifs": ["Expliquer ce qu'est l'arrière et l'économie de guerre", "Décrire le rôle des femmes et des enfants"],
   "vocabulaire": [{"mot": "arrière", "def": "partie du pays éloignée des combats"}, {"mot": "munitionnette", "def": "ouvrière qui fabrique des obus"}, {"mot": "économie de guerre", "def": "économie où les usines produisent surtout pour l'armée"}],
   "contexte": "Les femmes remplacent les hommes partis, aux champs comme à l'usine. Les élèves écrivent aux soldats. Des travailleurs venus des colonies et d'autres pays travaillent en France."},
  {"salle": 4, "titre": "Lettre n°4, 11 novembre 1918 — L'école-hôpital : l'armistice",
   "objectifs": ["Dater l'armistice et le traité de Versailles", "Distinguer armistice et paix ; connaître le bilan humain"],
   "vocabulaire": [{"mot": "armistice", "def": "accord qui arrête les combats, avant la signature de la paix"}, {"mot": "traité", "def": "accord écrit et signé entre des pays"}, {"mot": "veuve", "def": "femme dont le mari est mort"}],
   "contexte": "Le 11 novembre 1918, les combats s'arrêtent. La paix est signée en 1919 à Versailles. La France compte près de 1,4 million de soldats morts."},
  {"salle": 5, "titre": "Lettre n°5, 1922 — Le monument aux morts : la mémoire",
   "objectifs": ["Expliquer à quoi sert un monument aux morts et le 11 novembre", "Comprendre pourquoi la paix reste fragile"],
   "vocabulaire": [{"mot": "monument aux morts", "def": "monument qui porte les noms des soldats d'une commune morts à la guerre"}, {"mot": "commémorer", "def": "se rassembler pour se souvenir ensemble"}, {"mot": "régime autoritaire", "def": "pouvoir qui supprime les libertés et ne tolère pas d'opposition"}],
   "contexte": "Chaque commune grave les noms de ses morts. Le 11 novembre, on se souvient ensemble. Après la guerre, la colère et la crise profitent aux extrémistes."}
 ],
 "qcm": {
  "CM1": [
   q("En 1914, la France est alliée...", ["au Royaume-Uni et à la Russie", "à l'Allemagne", "à l'Autriche-Hongrie"], 0),
   q("Que fait l'affiche de la mobilisation générale ?", ["elle annonce la paix", "elle appelle les hommes à rejoindre l'armée", "elle annonce une fête"], 1),
   q("Au début de la guerre, presque tout le monde croit...", ["qu'elle durera dix ans", "qu'il n'y aura pas de guerre", "qu'elle sera courte"], 2),
   q("Le front va...", ["de la mer du Nord à la Suisse", "de Paris à Marseille", "de Brest à Lyon"], 0),
   q("Qu'est-ce qui aide les poilus à tenir ?", ["les vacances", "les lettres, les colis et l'amitié entre camarades", "la télévision"], 1),
   q("L'arrière, c'est...", ["la dernière ligne de tranchées", "le dos du soldat", "le pays loin du front"], 2),
   q("Qui fait les moissons à la place des hommes partis ?", ["les femmes, les enfants et les anciens", "les soldats en permission", "personne"], 0),
   q("Quel pays entre en guerre en 1917 aux côtés de la France ?", ["l'Allemagne", "les États-Unis", "l'Italie de Mussolini"], 1),
   q("Que devient le 11 novembre ?", ["un jour d'école", "le jour de la fête nationale", "un jour férié pour se souvenir"], 2),
   q("Où repose le Soldat inconnu ?", ["sous l'Arc de Triomphe, à Paris", "à Versailles", "à Sarajevo"], 0)],
  "CM2": [
   q("Depuis la guerre de 1870, l'Alsace et la Moselle appartiennent...", ["à la Belgique", "à l'Allemagne", "au Royaume-Uni"], 1),
   q("La Triple-Entente réunit...", ["l'Allemagne et l'Autriche-Hongrie", "la France, l'Italie et l'Espagne", "la France, le Royaume-Uni et la Russie"], 2),
   q("Le 3 août 1914...", ["l'Allemagne déclare la guerre à la France", "l'armistice est signé", "les États-Unis entrent en guerre"], 0),
   q("Pourquoi le Royaume-Uni entre-t-il en guerre ?", ["parce que Paris est attaqué", "parce que l'armée allemande traverse la Belgique, un pays neutre", "à cause de la crise de 1929"], 1),
   q("Le no man's land, c'est...", ["un abri sous terre", "un boyau vers l'arrière", "l'espace entre les tranchées ennemies"], 2),
   q("La bataille de Verdun dure...", ["du 21 février au 18 décembre 1916", "du 1er juillet au 18 novembre 1916", "quelques jours"], 0),
   q("Les gaz de combat sont employés à partir de...", ["1914", "1915", "1918"], 1),
   q("Combien de soldats venus des colonies combattent dans l'armée française ?", ["environ 6 000", "environ 6 millions", "environ 600 000"], 2),
   q("Environ 40 000 ouvriers chinois travaillent en France, par exemple...", ["dans les usines du Creusot", "dans les tranchées de Verdun", "à Versailles"], 0),
   q("L'armistice est signé à 5 h 15 le 11 novembre 1918...", ["dans la galerie des Glaces", "à Rethondes, en forêt de Compiègne", "à Sarajevo"], 1),
   q("Les Françaises obtiennent le droit de vote en...", ["1918", "1922", "1944"], 2),
   q("Depuis quelle loi le 11 novembre est-il un jour férié ?", ["la loi du 24 octobre 1922", "le traité de Versailles", "la loi de 2012"], 0)]
 },
 "questions_fermees": {
  "CM1": [
   vf("En 1914, les grands pays d'Europe forment deux alliances.", "vrai"),
   vf("Les soldats partent tous joyeux, « la fleur au fusil ».", "faux"),
   vf("Pendant la guerre, des femmes conduisent les tramways.", "vrai"),
   vf("L'armistice du 11 novembre 1918, c'est déjà la paix signée.", "faux"),
   vf("Presque chaque commune de France a construit un monument aux morts.", "vrai"),
   court("Qu'est-ce qu'une tranchée ?", "un fossé creusé pour se protéger, où vivent les soldats du front"),
   court("Cite deux armes nouvelles de cette guerre.", "par exemple : les mitrailleuses, les gaz, les avions, les chars"),
   court("Que redeviennent l'Alsace et la Moselle après la guerre ?", "françaises")],
  "CM2": [
   vf("Le 1er août 1914, l'affiche de la mobilisation générale est collée dans toutes les communes de France.", "vrai"),
   vf("La bataille de la Somme est menée par les Français seuls.", "faux"),
   vf("Le courrier des soldats est surveillé par la censure.", "vrai"),
   vf("Le traité de Versailles est signé le 11 novembre 1918.", "faux"),
   court("Quelle est la différence entre un armistice et un traité de paix ?", "l'armistice arrête les combats ; le traité, signé plus tard, fait la paix"),
   court("Pourquoi parle-t-on d'économie de guerre ?", "parce que les usines produisent surtout pour l'armée (obus, canons, uniformes)"),
   court("Que doit faire l'Allemagne d'après le traité de Versailles ? Donne deux exemples.", "rendre l'Alsace et la Moselle, payer des réparations, réduire son armée"),
   court("Pourquoi dit-on que la paix est fragile après 1918 ?", "colère, dettes, chômage puis crise de 1929 ; des extrémistes prennent le pouvoir, comme Mussolini en Italie en 1922")]
 },
 "etudes_documents": {
  "CM1": [
   {"titre": "La lettre de Louis", "document": {"contenu": "Ma chère Jeanne, je t'écris de notre abri, au fond de la tranchée. Il pleut depuis trois jours et la boue colle à nos chaussures. Ton colis est bien arrivé : le chocolat et les chaussettes de laine ont fait le bonheur de toute l'escouade. Je ne peux pas te dire où nous sommes. Embrasse papa et maman pour moi. Ton grand frère, Louis.", "source": "Lettre inventée pour le jeu, d'après la leçon 2."},
    "questions": [court("Où Louis écrit-il sa lettre ?", "dans un abri, au fond de la tranchée"),
                  court("Qu'est-ce qui l'aide à tenir ? Donne un exemple.", "le colis de sa famille (chocolat, chaussettes), les lettres, ses camarades"),
                  court("Pourquoi Louis ne peut-il pas dire où il est ?", "parce que le courrier est surveillé : c'est la censure")]},
   {"titre": "Les repères de la guerre", "document": {"contenu": "Août 1914 : mobilisation générale. 1916 : batailles de Verdun et de la Somme. 1917 : les États-Unis entrent en guerre. 11 novembre 1918 : armistice. 1919 : traité de Versailles.", "source": "D'après la frise de la leçon 4 du jeu."},
    "questions": [court("En quelle année commence la guerre ?", "en 1914"),
                  court("Quel événement a lieu le 11 novembre 1918 ?", "l'armistice : les combats s'arrêtent"),
                  court("Combien d'années la guerre a-t-elle duré environ ?", "plus de quatre ans (de 1914 à 1918)")]}],
  "CM2": [
   {"titre": "Repères chiffrés (chiffres officiels)", "document": {"contenu": "Français mobilisés de 1914 à 1918 : 8,7 millions. Soldats français morts : près de 1,4 million. Veuves de guerre en France : près de 600 000. Armistice : 11 novembre 1918, signé à 5 h 15 à Rethondes ; fin des combats à 11 heures. Traité de Versailles : 28 juin 1919.", "source": "Document de la leçon 4 du jeu (ministère des Armées, Chemins de mémoire ; musée de l'Armée)."},
    "questions": [court("Combien de Français sont mobilisés pendant la guerre ?", "8,7 millions"),
                  court("Combien de temps sépare la signature de l'armistice de la fin des combats ?", "5 h 45 (de 5 h 15 à 11 heures)"),
                  court("Que montre le chiffre de 600 000 veuves ?", "que beaucoup de familles ont perdu un mari, un père : le deuil touche tout le pays")]},
   {"titre": "La lettre de Marcelle", "document": {"contenu": "Chère Jeanne, à l'usine, nous sommes des centaines de femmes à fabriquer des obus, du matin jusqu'au soir. Mon frère est au front, mon mari aussi. À la campagne, ma mère et les enfants ont fait les vendanges. Le soir, je lis les nouvelles du front dans le journal. Je pense souvent que nous, les femmes, faisons tourner le pays, et pourtant nous ne votons pas. Marcelle.", "source": "Lettre inventée pour le jeu, d'après la leçon 3."},
    "questions": [court("Comment appelle-t-on les ouvrières comme Marcelle ?", "les munitionnettes"),
                  court("Qui fait les vendanges ? Pourquoi ?", "les femmes, les enfants et les anciens, parce que les hommes sont partis au front"),
                  court("En quelle année les Françaises obtiendront-elles le droit de vote ?", "en 1944")]}]
 }
}

with open(os.path.join(JEU, "assets", "data", "evaluations.json"), "w", encoding="utf-8", newline="\n") as f:
    json.dump(EVAL, f, ensure_ascii=False, indent=1); f.write("\n")
with open(os.path.join(JEU, "assets", "data", "evaluations-embarquees.js"), "w", encoding="utf-8", newline="\n") as f:
    f.write("/* FICHIER GÉNÉRÉ par grande-guerre/outils/generer-evaluations.py — ne pas modifier à la main. */\n")
    f.write("window.EVAL_EMBARQUEES = "); json.dump(EVAL, f, ensure_ascii=False, separators=(",", ":")); f.write(";\n")
n = {k: {niv: len(v[niv]) for niv in v} for k, v in EVAL.items() if k in ("qcm", "questions_fermees", "etudes_documents")}
print("évaluations écrites :", n)
