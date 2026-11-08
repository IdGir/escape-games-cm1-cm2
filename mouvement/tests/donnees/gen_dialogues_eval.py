# -*- coding: utf-8 -*-
"""Génère dialogues.json et evaluations.json. Lancer : python gen_dialogues_eval.py <dossier data>"""
import json, os, sys

MOTS = ["DISTANCE", "DURÉE", "VITESSE", "TRAJECTOIRE", "OBSERVATEUR"]

DIALOGUES = {
    "metadata": {"jeu": "Le Grand Prix de l'observatoire",
                 "sujet": "Mesurer une distance et une durée lors d'un déplacement, comparer des déplacements, différents types de mouvement (rectiligne, circulaire), le mouvement de la Terre autour du Soleil et le rôle de l'observateur — sciences, cycle 3",
                 "niveaux": ["CM1", "CM2"],
                 "lien_autres_jeux": "Prépare le jeu n°14 « La Centrale en panne » et le jeu n°18 « Le Robot de l'atelier » ; se relie au « Tour du monde » (échelles, durées de trajet) et à « L'Atelier de l'inventeur » (n°04 : transmission du mouvement).",
                 "sources": "Programme de sciences et technologie, cycle 3 (BO n° 24 du 11 juin 2026) ; Eduscol ; La main à la pâte ; Vikidia. Détail : README.md, section Sources."},
    "personnages": {"margaux": {"nom": "Margaux", "role": "Commissaire de course du Grand Prix"},
                    "yanis": {"nom": "Yanis", "role": "Pilote de caisse à savon"},
                    "salome": {"nom": "Salomé", "role": "Cycliste, responsable du tableau des temps"},
                    "leonie": {"nom": "Léonie", "role": "Astronome de l'observatoire"},
                    "hugo": {"nom": "Hugo", "role": "Contrôleur du petit train"}},
    "intro_accueil": "Bonjour, et bienvenue au Grand Prix de l'observatoire ! Je suis Margaux, la commissaire de course. Chaque année, les véhicules de l'école descendent la piste du plateau, au pied de la coupole. Mais cette nuit, le vent a renversé les plots et dispersé nos feuilles de mesure, et le chronomètre officiel s'est verrouillé. Les résultats doivent être validés avant midi. Vous êtes mes commissaires : dans chacun des cinq postes, retrouvez un mot, notez-le bien, et le Grand Prix pourra avoir lieu.",
    "salles": [
        {"num": 1, "titre": "La ligne de départ", "decor": "depart", "motCle": MOTS[0], "lieu": "La ligne de départ, sur le plateau de l'observatoire",
         "description": "Une large piste descend du plateau. Les plots orange sont renversés, un décamètre jaune traîne dans l'herbe et une banderole « Départ » flotte au vent. Au loin, la coupole blanche de l'observatoire.",
         "sens": ["À voir : les plots renversés et le décamètre jaune", "À entendre : la banderole qui claque au vent", "À sentir : l'herbe fraîche du matin"],
         "dialogue_intro": {"perso": "margaux", "nom": "Margaux", "texte": "Merci d'être là ! Le vent a déplacé tous mes plots : je ne sais plus où sont les lignes de départ et d'arrivée. Avant midi, il faut tout remesurer. Prenez les bons instruments, et n'oubliez jamais l'unité !"},
         "dialogue_reussite": {"perso": "margaux", "nom": "Margaux", "texte": "Bravo ! Le premier mot est <b>DISTANCE</b> : de la ligne de départ à la ligne d'arrivée, et toujours avec son unité. Filez au stand des chronométreurs : Yanis vous attend."}},
        {"num": 2, "titre": "Le stand des chronométreurs", "decor": "stand", "motCle": MOTS[1], "lieu": "Le stand des chronométreurs, au bord de la piste",
         "description": "Une tente rayée, une grande horloge, une table couverte de chronomètres et de sabliers. Une caisse à savon rouge attend, prête pour la descente.",
         "sens": ["À voir : la grande horloge et les chronomètres", "À entendre : le bip d'un chronomètre", "À sentir : l'odeur du bois verni de la caisse à savon"],
         "dialogue_intro": {"perso": "yanis", "nom": "Yanis", "texte": "Salut ! Je suis Yanis, pilote de la caisse à savon rouge. Mes temps d'essai ont été mélangés par le vent. Sans eux, je ne peux pas prendre le départ. Vous savez ce qu'est une durée ?"},
         "dialogue_reussite": {"perso": "yanis", "nom": "Yanis", "texte": "Super ! Le deuxième mot est <b>DURÉE</b> : le temps entre deux instants, le départ et l'arrivée. Salomé a besoin de vous au tableau des temps."}},
        {"num": 3, "titre": "Le tableau des temps", "decor": "tableau", "motCle": MOTS[2], "lieu": "Le tableau des temps, près des tribunes",
         "description": "Un grand panneau noir où l'on écrit les résultats à la craie. Des vélos sont appuyés contre la barrière ; une petite tribune attend le public.",
         "sens": ["À voir : le grand panneau des résultats", "À entendre : le cliquetis des roues de vélo", "À sentir : la poussière de craie"],
         "dialogue_intro": {"perso": "salome", "nom": "Salomé", "texte": "Bonjour ! Je suis Salomé, cycliste et gardienne du tableau des temps. Tout le monde me demande qui est le plus rapide. Pour comparer, il faut une règle : aidez-moi à la retrouver."},
         "dialogue_reussite": {"perso": "salome", "nom": "Salomé", "texte": "Voilà ! Le troisième mot est <b>VITESSE</b> : à distance égale, le plus rapide met le moins de temps. Montez à la coupole : Léonie observe tout le circuit."}},
        {"num": 4, "titre": "La coupole de l'observatoire", "decor": "coupole", "motCle": MOTS[3], "lieu": "La coupole de l'observatoire, au sommet du plateau",
         "description": "Une salle ronde sous un toit qui s'ouvre. Au centre, une grande lunette. Par la fente du toit, on voit le circuit, le manège et la grande roue de la fête.",
         "sens": ["À voir : la grande lunette et le circuit tout en bas", "À entendre : le grincement du toit qui tourne", "À sentir : l'air frais qui entre par la fente"],
         "dialogue_intro": {"perso": "leonie", "nom": "Léonie", "texte": "Bienvenue sous ma coupole ! Je suis Léonie, l'astronome. D'ici, je regarde les étoiles la nuit et, le jour, le circuit du Grand Prix. Chaque objet dessine un chemin : une droite, un cercle, une courbe. Sauriez-vous les reconnaître ?"},
         "dialogue_reussite": {"perso": "leonie", "nom": "Léonie", "texte": "Parfait ! Le quatrième mot est <b>TRAJECTOIRE</b> : le chemin que dessine un objet qui se déplace. Descendez au quai : Hugo va vous faire monter dans le petit train."}},
        {"num": 5, "titre": "Le quai du petit train", "decor": "quai", "motCle": MOTS[4], "lieu": "Le quai du petit train, au pied du plateau",
         "description": "Un petit quai de bois, une locomotive verte et trois wagons ouverts. Sur le quai, un pupitre porte le chronomètre officiel, verrouillé par un code.",
         "sens": ["À voir : la locomotive verte et le chronomètre officiel", "À entendre : le sifflet du contrôleur", "À sentir : l'odeur de l'huile des rails"],
         "dialogue_intro": {"perso": "hugo", "nom": "Hugo", "texte": "En voiture ! Je suis Hugo, le contrôleur du petit train. Dans mon wagon, les voyageurs se disputent : l'un dit qu'il ne bouge pas, l'autre qu'il avance. Qui a raison ? Montez, on va voir ça ensemble."},
         "dialogue_fin": {"perso": "margaux", "nom": "Margaux", "texte": "Le dernier mot est <b>OBSERVATEUR</b> : un mouvement se décrit toujours par rapport à quelqu'un. Vous avez les cinq mots : ouvrons le coffre du Grand Prix !"}},
    ]}


def q(qq, opts, b, pts=1):
    return {"q": qq, "options": opts, "bonne": b, "pts": pts}


EVAL = {
    "metadata": {"sujet": "Mesurer une distance et une durée, comparer des déplacements, trajectoires, la Terre autour du Soleil, le rôle de l'observateur",
                 "niveaux": ["CM1", "CM2"],
                 "programme": "Sciences et technologie, cycle 3 — « Différents types de mouvement » (BO n° 24 du 11 juin 2026). Progression de l'enseignant : année B, période 2 (« Mesure une distance et une durée lors du déplacement d'un objet. Différents types de mouvement. »).",
                 "sources": "Voir README.md du jeu, section Sources."},
    "quizz_final": {
        "CM1": [{"q": "Pour mesurer une piste de 50 m, on prend...", "options": ["une règle", "un décamètre", "un sablier"], "bonne": 1},
                {"q": "Une durée, c'est...", "options": ["le temps entre deux instants", "une heure précise", "une longueur"], "bonne": 0},
                {"q": "Sur la même distance, le plus rapide est celui qui...", "options": ["part le dernier", "met le plus de temps", "met le moins de temps"], "bonne": 2},
                {"q": "La nacelle de la grande roue se déplace...", "options": ["en cercle", "en ligne droite", "elle ne bouge pas"], "bonne": 0},
                {"q": "Dans le train qui roule, pour son voisin assis, le voyageur est...", "options": ["en mouvement", "immobile", "dehors"], "bonne": 1}],
        "CM2": [{"q": "2 km et 300 m, cela fait...", "options": ["230 m", "2 300 m", "23 000 m"], "bonne": 1},
                {"q": "2 min 30 s, cela fait...", "options": ["230 s", "130 s", "150 s"], "bonne": 2},
                {"q": "Pendant une même durée, le plus rapide est celui qui...", "options": ["va le plus loin", "s'arrête le premier", "va le moins loin"], "bonne": 0},
                {"q": "La Terre fait le tour du Soleil en environ...", "options": ["un jour", "un an", "un mois"], "bonne": 1},
                {"q": "Un mouvement se décrit toujours...", "options": ["en kilomètres", "avec un chronomètre", "par rapport à un observateur"], "bonne": 2}]},
    "fiches_preparatoires": [
        {"salle": 1, "titre": "La ligne de départ — mesurer une distance", "objectifs": ["Repérer un départ et une arrivée", "Choisir un instrument de mesure adapté"],
         "vocabulaire": [{"mot": "distance parcourue", "def": "longueur du départ à l'arrivée"}, {"mot": "décamètre", "def": "ruban gradué d'au moins 10 m"}, {"mot": "unité", "def": "m, cm, km..."}],
         "contexte": "Une mesure s'écrit toujours avec son unité. Si le départ n'est pas au zéro, on soustrait les deux graduations."},
        {"salle": 2, "titre": "Le stand des chronométreurs — mesurer une durée", "objectifs": ["Distinguer un instant et une durée", "Utiliser un chronomètre"],
         "vocabulaire": [{"mot": "instant", "def": "moment précis"}, {"mot": "durée", "def": "temps entre deux instants"}, {"mot": "chronomètre", "def": "instrument qui mesure une durée"}],
         "contexte": "1 h = 60 min ; 1 min = 60 s. Pour calculer une durée, on peut passer par une heure ronde."},
        {"salle": 3, "titre": "Le tableau des temps — comparer des déplacements", "objectifs": ["Comparer sur une même distance", "Comparer pendant une même durée"],
         "vocabulaire": [{"mot": "plus rapide", "def": "moins de temps pour la même distance"}, {"mot": "km/h", "def": "kilomètres par heure, une unité de vitesse"}],
         "contexte": "Pour comparer, on garde une grandeur identique : la distance ou la durée."},
        {"salle": 4, "titre": "La coupole de l'observatoire — trajectoires", "objectifs": ["Reconnaître un mouvement rectiligne ou circulaire", "Situer la Terre dans le système solaire"],
         "vocabulaire": [{"mot": "trajectoire", "def": "chemin dessiné par l'objet"}, {"mot": "rectiligne", "def": "en ligne droite"}, {"mot": "circulaire", "def": "en cercle"}],
         "contexte": "La Terre est la troisième planète à partir du Soleil ; elle en fait le tour en environ un an."},
        {"salle": 5, "titre": "Le quai du petit train — l'observateur", "objectifs": ["Dire si un objet est immobile ou en mouvement pour un observateur", "Classer des durées"],
         "vocabulaire": [{"mot": "observateur", "def": "celui qui regarde"}, {"mot": "immobile", "def": "qui ne change pas de place pour l'observateur"}],
         "contexte": "Le même voyageur est immobile pour son voisin assis et en mouvement pour la personne sur le quai."}],
    "qcm": {
        "CM1": [q("Pour mesurer la longueur d'un crayon, on utilise...", ["un décamètre", "une règle graduée", "un chronomètre"], 1),
                q("La distance parcourue se mesure entre...", ["le départ et l'arrivée", "le pilote et le public", "deux chronomètres"], 0),
                q("1 m, c'est...", ["10 cm", "1 000 cm", "100 cm"], 2),
                q("« 10 h 15 » est...", ["un instant", "une durée", "une distance"], 0),
                q("Pour chronométrer, on déclenche le chronomètre...", ["à l'arrivée", "au départ", "n'importe quand"], 1),
                q("De 10 h 15 à 10 h 40, il s'écoule...", ["15 min", "40 min", "25 min"], 2),
                q("Sur 100 m, Léa met 30 s et Tom 45 s. Le plus rapide est...", ["Léa", "Tom", "ils vont aussi vite"], 0),
                q("Le cheval de bois du manège a une trajectoire...", ["droite", "en cercle", "en zigzag"], 1),
                q("Une bille lâchée tombe...", ["en cercle", "en zigzag", "en ligne droite"], 2),
                q("Pour le voyageur assis dans le train, la gare...", ["défile", "est immobile", "tourne en rond"], 0)],
        "CM2": [q("3 km, cela fait...", ["300 m", "3 000 m", "30 000 m"], 1),
                q("Quelle longueur est la plus grande ?", ["1 km et 20 m", "1 010 m", "950 m"], 0),
                q("1 dam, c'est...", ["100 m", "1 m", "10 m"], 2),
                q("1 h 15 min, cela fait...", ["75 min", "115 min", "65 min"], 0),
                q("Un chronomètre affiche 01:30. La durée est de...", ["130 s", "90 s", "13 s"], 1),
                q("Pendant 10 s, A parcourt 40 m et B 30 m. Le plus rapide est...", ["B", "on ne peut pas savoir", "A"], 2),
                q("Un cycliste en ville roule en moyenne à environ...", ["15 km/h", "150 km/h", "1 km/h"], 0),
                q("Un ballon lancé vers le panier a une trajectoire...", ["rectiligne", "curviligne", "circulaire"], 1),
                q("La Terre est la ... planète à partir du Soleil.", ["première", "cinquième", "troisième"], 2),
                q("La caisse à savon freine avant l'arrivée : son mouvement est...", ["ralenti", "accéléré", "circulaire"], 0),
                q("Pour Margaux sur le quai, le voyageur assis dans le train est...", ["immobile", "en mouvement", "invisible"], 1),
                q("Hugo lâche son stylo dans le train qui roule tout droit. Pour Hugo, le stylo tombe...", ["en cercle", "en arrière", "en ligne droite verticale"], 2)]},
    "questions_fermees": {
        "CM1": [{"q": "Une mesure doit toujours être écrite avec son unité.", "type": "vf", "bonne": "vrai", "pts": 1},
                {"q": "Un sablier donne l'heure qu'il est.", "type": "vf", "bonne": "faux", "pts": 1},
                {"q": "Sur la même distance, le plus rapide met le plus de temps.", "type": "vf", "bonne": "faux", "pts": 1},
                {"q": "Un même objet peut être immobile pour une personne et en mouvement pour une autre.", "type": "vf", "bonne": "vrai", "pts": 1},
                {"q": "Cite un instrument pour mesurer une distance.", "type": "court", "rep": "une règle graduée, un mètre ruban ou un décamètre", "pts": 1},
                {"q": "Cite un instrument pour mesurer une durée.", "type": "court", "rep": "un chronomètre ou un sablier", "pts": 1},
                {"q": "Comment appelle-t-on un mouvement en ligne droite ?", "type": "court", "rep": "un mouvement rectiligne", "pts": 1},
                {"q": "Comment appelle-t-on celui qui regarde un mouvement ?", "type": "court", "rep": "l'observateur", "pts": 1}],
        "CM2": [{"q": "1 km = 100 m.", "type": "vf", "bonne": "faux", "pts": 1},
                {"q": "Une minute vaut 60 secondes.", "type": "vf", "bonne": "vrai", "pts": 1},
                {"q": "La Terre tourne autour du Soleil en environ un an.", "type": "vf", "bonne": "vrai", "pts": 1},
                {"q": "Le quai est immobile pour tous les observateurs.", "type": "vf", "bonne": "faux", "pts": 1},
                {"q": "Convertis 4 m en centimètres.", "type": "court", "rep": "400 cm", "pts": 1},
                {"q": "Convertis 3 min 20 s en secondes.", "type": "court", "rep": "200 s", "pts": 1},
                {"q": "Cite un objet qui a un mouvement circulaire.", "type": "court", "rep": "la nacelle d'une grande roue, un manège, l'aiguille d'une horloge...", "pts": 1},
                {"q": "Pourquoi faut-il préciser l'observateur pour décrire un mouvement ?", "type": "court", "rep": "parce qu'un objet peut être immobile pour l'un et en mouvement pour l'autre", "pts": 1}]},
    "etudes_documents": {
        "CM1": [{"titre": "Le carnet de Margaux", "document": {"contenu": "Ruban posé le long de la piste. Ligne de départ : graduation 5 m. Ligne d'arrivée : graduation 17 m.", "source": "Mesures inventées pour le jeu."},
                 "questions": [{"q": "Quelle distance la petite voiture a-t-elle parcourue ?", "type": "court", "rep": "17 − 5 = 12 m", "pts": 1},
                               {"q": "Quel instrument Margaux a-t-elle utilisé ?", "type": "court", "rep": "un décamètre (un ruban gradué)", "pts": 1},
                               {"q": "Pourquoi écrit-elle « m » après les nombres ?", "type": "court", "rep": "c'est l'unité : les mètres", "pts": 1}]},
                {"title_": "", "titre": "Le petit train", "document": {"contenu": "Dans le wagon, Lou est assise à côté de son frère. Sur le quai, leur grand-mère leur fait signe pendant que le train part.", "source": "Texte inventé pour le jeu."},
                 "questions": [{"q": "Pour son frère, Lou est-elle immobile ou en mouvement ?", "type": "court", "rep": "immobile", "pts": 1},
                               {"q": "Pour la grand-mère, Lou est-elle immobile ou en mouvement ?", "type": "court", "rep": "en mouvement", "pts": 1},
                               {"q": "Pour Lou, la grand-mère est-elle immobile ou en mouvement ?", "type": "court", "rep": "en mouvement : elle s'éloigne", "pts": 1}]}],
        "CM2": [{"titre": "Le relevé de Salomé", "document": {"contenu": "Course de 300 m. Salomé : 1 min 05 s. Yanis : 58 s. Léo : 1 min 20 s. Mila : 3 min 10 s.", "source": "Durées inventées pour le jeu."},
                 "questions": [{"q": "Convertis toutes les durées en secondes.", "type": "court", "rep": "65 s ; 58 s ; 80 s ; 190 s", "pts": 1},
                               {"q": "Classe les concurrents du plus rapide au plus lent.", "type": "court", "rep": "Yanis, Salomé, Léo, Mila", "pts": 1},
                               {"q": "Quel est l'écart entre le premier et le dernier ?", "type": "court", "rep": "190 − 58 = 132 s", "pts": 1}]},
                {"titre": "Le schéma de Léonie", "document": {"contenu": "Au centre, le Soleil. Autour, trois cercles : Mercure sur le plus petit, Vénus sur le deuxième, la Terre sur le troisième.", "source": "Description d'un schéma ; tailles et distances non respectées."},
                 "questions": [{"q": "Quelle est la place de la Terre à partir du Soleil ?", "type": "court", "rep": "la troisième", "pts": 1},
                               {"q": "Quelle est la forme de la trajectoire de la Terre ?", "type": "court", "rep": "presque un cercle", "pts": 1},
                               {"q": "Combien de temps dure un tour complet ?", "type": "court", "rep": "environ un an (365 jours)", "pts": 1}]}]},
}
del EVAL["etudes_documents"]["CM1"][1]["title_"]


def main(dest):
    json.dump(DIALOGUES, open(os.path.join(dest, "dialogues.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(EVAL, open(os.path.join(dest, "evaluations.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
