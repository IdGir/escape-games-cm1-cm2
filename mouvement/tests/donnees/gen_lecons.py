# -*- coding: utf-8 -*-
"""Génère mouvement/assets/data/lecons.json (5 leçons). Lancer : python gen_lecons.py <dossier data>"""
import json, os, sys
from schemas import lecon_distance, lecon_duree, lecon_comparer, lecon_trajectoires, lecon_observateur

BO = "Programme de sciences et technologie, cycle 3, arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026 (CM1 et CM2 : « Différents types de mouvement »)"


def L(id, salle, icone, titre, objectifs, cm1, cm2, lexique, schema_titre, svg, sources, document=None):
    l = {"id": id, "salle": salle, "icone": icone, "titre": titre, "duree": "3 min", "niveau": "CM1-CM2", "objectifs": objectifs,
         "contenu": {"cm1": cm1, "cm2": cm2}, "lexique": [{"mot": m, "def": d} for m, d in lexique],
         "schema": {"titre": schema_titre, "svg": svg}}
    if document:
        l["document"] = document
    l["sources"] = sources
    return l


LECONS = [
    L("distance", 1, "D", "Mesurer une distance",
      ["Repérer un point de départ et un point d'arrivée", "Choisir un instrument adapté à la longueur", "Lire une graduation et écrire l'unité",
       "CM2 : convertir des unités de longueur (km, m, cm, mm)"],
      "<h4>Du départ à l'arrivée</h4><p>Quand un objet se déplace, il part d'un <b>point de départ</b> et arrive à un <b>point d'arrivée</b>. La longueur entre ces deux points est la <b>distance parcourue</b>.</p>"
      "<h4>Le bon instrument</h4><p>Pour mesurer une petite longueur, on utilise une <b>règle graduée</b>. Pour quelques mètres, on prend un <b>mètre ruban</b>. Pour une piste de plusieurs dizaines de mètres, on déroule un <b>décamètre</b>, un long ruban d'au moins 10 m.</p>"
      "<h4>Lire et écrire une mesure</h4><p>Si le départ n'est pas au zéro du ruban, on fait une soustraction : la graduation de l'arrivée moins celle du départ. Une mesure s'écrit toujours avec son <b>unité</b> : 15 m, 30 cm.</p>",
      "<h4>Distance parcourue</h4><p>Pour décrire un déplacement, on repère d'abord un point de départ et un point d'arrivée. La distance parcourue est la longueur entre ces deux points, mesurée le long du trajet.</p>"
      "<h4>Choisir l'instrument</h4><p>On choisit l'instrument selon la longueur à mesurer : la règle graduée pour quelques centimètres, le mètre ruban pour quelques mètres, le décamètre pour quelques dizaines de mètres. Pour une très longue distance, on pousse une roue de mesure qui compte les mètres en roulant. Quand la longueur dépasse celle du ruban, on le reporte plusieurs fois bout à bout, puis on additionne.</p>"
      "<h4>Lire une graduation</h4><p>Si le départ n'est pas au zéro du ruban, la distance parcourue est égale à la graduation de l'arrivée moins la graduation du départ. Une mesure s'écrit toujours avec son unité : un nombre seul ne veut rien dire.</p>"
      "<h4>Convertir</h4><p>Le mètre (m) est l'unité de longueur. On utilise aussi le kilomètre (1 km = 1 000 m), le décamètre (1 dam = 10 m), le centimètre (1 m = 100 cm) et le millimètre (1 cm = 10 mm). Pour comparer deux longueurs, on les écrit d'abord dans la même unité : 1 km et 20 m, c'est 1 020 m.</p>",
      [("distance parcourue", "longueur entre le point de départ et le point d'arrivée"), ("décamètre", "ruban gradué d'au moins 10 m ; aussi l'unité qui vaut 10 m"),
       ("graduation", "trait numéroté sur un instrument de mesure"), ("unité", "ce qui suit le nombre d'une mesure : m, cm, km")],
      "Lire une distance sur un ruban gradué", lecon_distance(),
      BO + " (CM1 : « mesurer une distance lors du déplacement d'un objet » ; CM2 : « effectuer des conversions d'unités de distance ») ; La main à la pâte, ressources « Mouvement » ; Eduscol, ressources d'accompagnement « Matière, mouvement, énergie, information »."),
    L("duree", 2, "T", "Mesurer une durée",
      ["Distinguer un instant et une durée", "Mesurer une durée avec un chronomètre", "Calculer une durée entre deux instants",
       "CM2 : convertir des unités de temps (h, min, s)"],
      "<h4>Instant et durée</h4><p>Un <b>instant</b> est un moment précis, que l'on lit sur une horloge : 10 h 15. Une <b>durée</b> est le temps qui passe entre deux instants : entre le départ et l'arrivée d'une course.</p>"
      "<h4>Les instruments</h4><p>Le <b>chronomètre</b> mesure une durée : on le remet à zéro, on le déclenche au départ et on l'arrête à l'arrivée. Le <b>sablier</b> mesure toujours la même durée.</p>"
      "<h4>Calculer une durée</h4><p>De 10 h 15 à 10 h 40, il s'est écoulé 25 minutes. On écrit toujours l'unité : h pour les heures, min pour les minutes, s pour les secondes.</p>",
      "<h4>Un intervalle entre deux instants</h4><p>Un instant est un moment précis, comme l'heure du départ. Une durée est l'intervalle entre deux instants : pour la connaître, il faut l'instant du départ et l'instant de l'arrivée. L'horloge donne des instants ; le chronomètre et le sablier mesurent des durées.</p>"
      "<h4>Chronométrer</h4><p>On remet le chronomètre à zéro, on le déclenche au moment exact du départ et on l'arrête quand l'objet franchit la ligne d'arrivée. On lit la durée et on la note avec son unité. Refaire la mesure permet de vérifier : un chronométreur qui réagit en retard fausse le résultat.</p>"
      "<h4>Calculer et convertir</h4><p>Pour calculer une durée, on peut passer par une heure ronde : de 10 h 50 à 11 h 05, il y a 10 minutes puis 5 minutes, soit 15 minutes. Une heure vaut 60 minutes et une minute vaut 60 secondes : 2 min 30 s font 150 s, et 1 h 15 min font 75 min. Sur l'écran d'un chronomètre, 01:30 se lit une minute et trente secondes.</p><h4>Toujours l'unité</h4><p>Comme pour une distance, une durée s'écrit toujours avec son unité : « 25 » ne veut rien dire, alors que « 25 min » ou « 25 s » désignent deux durées très différentes. Pour comparer deux durées, on les convertit d'abord dans la même unité.</p>",
      [("instant", "moment précis, lu sur une horloge"), ("durée", "temps écoulé entre deux instants"),
       ("chronomètre", "instrument qui mesure une durée"), ("sablier", "instrument qui mesure toujours la même durée")],
      "Une durée entre deux instants", lecon_duree(),
      BO + " (CM1 : « mesurer une durée, comme intervalle entre deux instants » ; CM2 : conversions d'unités de temps) ; La main à la pâte, ressources « Mouvement »."),
    L("comparer", 3, "V", "Comparer des déplacements",
      ["Comparer des déplacements sur une même distance", "Comparer des déplacements pendant une même durée", "Classer du plus rapide au plus lent",
       "CM2 : connaître des ordres de grandeur de vitesses (km/h)"],
      "<h4>Même distance</h4><p>Sur une même distance, le plus rapide est celui qui met <b>le moins de temps</b>. Sur 100 m, Salomé à vélo met 20 s et Mila à pied 70 s : Salomé est la plus rapide.</p>"
      "<h4>Même durée</h4><p>Pendant une même durée, le plus rapide est celui qui va <b>le plus loin</b>.</p>"
      "<h4>Pour comparer</h4><p>On garde toujours une grandeur identique pour tous : la distance ou la durée. Puis on range les concurrents du plus rapide au plus lent.</p>",
      "<h4>Deux façons de comparer</h4><p>Pour comparer deux déplacements, on garde une grandeur identique. Sur une même distance, le plus rapide met la durée la plus courte. Pendant une même durée, le plus rapide parcourt la plus grande distance. Si la distance et la durée changent toutes les deux, on ne peut pas conclure tout de suite : il faut d'abord ramener les deux déplacements à une même distance ou à une même durée.</p>"
      "<h4>Classer</h4><p>Pour classer des concurrents sur une même distance, on écrit toutes les durées dans la même unité, puis on les range de la plus courte à la plus longue : 38 s, 52 s, puis 1 min 05 s, c'est-à-dire 65 s.</p>"
      "<h4>La vitesse</h4><p>La vitesse dit si un objet va vite ou lentement. On peut l'exprimer en kilomètres par heure (km/h) : c'est la distance qui serait parcourue en une heure. Quelques ordres de grandeur : un piéton marche à environ 4 km/h, un cycliste en ville roule en moyenne à 15 km/h, une voiture ne doit pas dépasser 50 km/h en ville, un TGV roule jusqu'à 320 km/h. Le guépard peut dépasser 100 km/h, mais seulement sur quelques centaines de mètres.</p>",
      [("plus rapide", "qui met moins de temps pour la même distance, ou va plus loin pendant la même durée"),
       ("ordre de grandeur", "valeur approchée, pour se faire une idée"), ("km/h", "kilomètres par heure : une unité de vitesse")],
      "Même distance, durées différentes", lecon_comparer(),
      "Programme de sciences et technologie, cycle 3, BO n° 24 du 11 juin 2026 (la comparaison de vitesses est un objectif de sixième, « de manière qualitative, sans aborder la formule ») ; La main à la pâte ; Vikidia, « TGV » et « Vitesse des animaux » ; Fédération française de randonnée ; Club des villes et territoires cyclables ; Code de la route, article R413-3 (50 km/h en agglomération)."),
    L("trajectoires", 4, "C", "Trajectoires : droite, cercle ou courbe",
      ["Reconnaître un mouvement rectiligne ou circulaire", "CM2 : reconnaître un mouvement curviligne", "CM2 : décrire le mouvement de la Terre autour du Soleil",
       "CM2 : reconnaître un mouvement accéléré ou ralenti"],
      "<h4>La trajectoire</h4><p>La <b>trajectoire</b> est le chemin que dessine un objet qui se déplace.</p>"
      "<h4>En ligne droite</h4><p>Une bille lâchée tombe tout droit, l'ascenseur monte tout droit : leur trajectoire est une droite. On dit que le mouvement est <b>rectiligne</b>.</p>"
      "<h4>En cercle</h4><p>La nacelle de la grande roue, le cheval de bois du manège, le bout de l'aiguille d'une horloge tournent autour d'un centre : leur trajectoire est un cercle. Le mouvement est <b>circulaire</b>.</p>",
      "<h4>Droite, cercle ou courbe</h4><p>La trajectoire est l'ensemble des positions occupées par un objet au cours de son déplacement. Si c'est une droite, le mouvement est rectiligne : la bille qui tombe, l'ascenseur, le train sur une voie droite. Si c'est un cercle, le mouvement est circulaire : la grande roue, le manège, la pale d'une éolienne. Si c'est une courbe qui n'est pas un cercle, le mouvement est curviligne : un ballon lancé vers le panier, une voiture dans un virage en S.</p>"
      "<h4>La Terre autour du Soleil</h4><p>La Terre est la troisième planète du système solaire à partir du Soleil, après Mercure et Vénus. Elle tourne autour du Soleil en environ un an, à peu près 365 jours ; sa trajectoire est presque un cercle.</p>"
      "<h4>Vitesse qui change</h4><p>Un mouvement peut aussi changer de vitesse. Quand la caisse à savon va de plus en plus vite dans la descente, son mouvement est accéléré. Quand elle freine, sa vitesse diminue : le mouvement est ralenti. Si sa vitesse ne change pas, on dit que le mouvement est uniforme.</p><h4>Observer avant de nommer</h4><p>Pour reconnaître une trajectoire, on imagine le trait que laisserait l'objet derrière lui, ou on le photographie plusieurs fois de suite. La forme du trait dépend de la personne qui regarde : on précise toujours l'observateur.</p>",
      [("trajectoire", "chemin dessiné par un objet en mouvement"), ("rectiligne", "en ligne droite"), ("circulaire", "en cercle"),
       ("curviligne", "en ligne courbe")],
      "Trois formes de trajectoire", lecon_trajectoires(),
      BO + " (CM2 : « observer et identifier le mouvement rectiligne ou circulaire d'un objet, en fonction de l'observateur » ; « décrire le mouvement de la Terre par rapport au Soleil et la situer dans le système solaire ») ; Vikidia, « Terre » ; Eduscol, ressources d'accompagnement « Matière, mouvement, énergie, information »."),
    L("observateur", 5, "O", "Tout dépend de l'observateur",
      ["Savoir qu'un mouvement se décrit par rapport à un observateur", "Dire si un objet est immobile ou en mouvement pour un observateur donné",
       "Classer des durées pour établir un classement", "CM2 : savoir qu'un objet lâché tombe en ligne droite pour celui qui le lâche"],
      "<h4>Immobile ou en mouvement ?</h4><p>Dans le petit train qui roule, Hugo est assis en face d'un voyageur. Pour Hugo, le voyageur ne bouge pas : il est <b>immobile</b>. Pour Margaux, restée sur le quai, le même voyageur s'éloigne : il est <b>en mouvement</b>.</p>"
      "<h4>L'observateur</h4><p>On ne peut pas dire qu'un objet bouge sans dire <b>qui le regarde</b>. Celui qui regarde s'appelle l'<b>observateur</b>.</p>"
      "<h4>Par la fenêtre</h4><p>Pour Hugo, ce qui roule avec lui est immobile ; les arbres et la gare défilent.</p>",
      "<h4>Un mouvement « par rapport à »</h4><p>Le mouvement d'un objet est toujours décrit par rapport à un observateur. Le même voyageur peut être immobile pour son voisin assis dans le wagon et en mouvement pour la personne restée sur le quai. Pour les voyageurs, c'est le quai qui défile. Avant de dire qu'un objet bouge, on choisit donc toujours qui le regarde.</p>"
      "<h4>La forme de la trajectoire dépend aussi de l'observateur</h4><p>Dans un train qui roule tout droit à vitesse constante, un objet qu'on lâche décrit une droite verticale par rapport à la personne qui le lâche. Pour la personne sur le quai, il avance en même temps que le train pendant sa chute. De la même façon, on décrit le mouvement de la Terre autour du Soleil comme si on regardait le système solaire depuis l'espace.</p>"
      "<h4>Le classement du Grand Prix</h4><p>Pour classer des concurrents sur une même distance, on convertit leurs durées dans la même unité et on les range de la plus courte à la plus longue. L'écart entre deux concurrents est la différence de leurs durées.</p>",
      [("observateur", "personne qui regarde et par rapport à qui on décrit le mouvement"), ("immobile", "qui ne change pas de place pour un observateur"),
       ("en mouvement", "qui change de place pour un observateur")],
      "Le même voyageur, vu par deux observateurs", lecon_observateur(),
      BO + " (CM2 : « le mouvement d'un objet est toujours décrit par rapport à un observateur » ; « un objet qu'on lâche décrit une droite verticale par rapport à la personne qui le lâche ») ; Eduscol, ressources d'accompagnement « Matière, mouvement, énergie, information ».",
      document={"type": "texte", "titre": "Le carnet d'Hugo", "contenu": "Ce matin, dans le wagon, mon voisin lisait sans bouger, et pourtant Margaux, sur le quai, l'a vu partir avec le train. Quand j'ai lâché mon stylo, il est tombé tout droit à mes pieds.", "source": "Texte inventé pour le jeu."}),
]


def main(dest):
    json.dump({"lecons": LECONS}, open(os.path.join(dest, "lecons.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
