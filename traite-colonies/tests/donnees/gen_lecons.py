# -*- coding: utf-8 -*-
"""Génère traite-colonies/assets/data/lecons.json (5 leçons). Lancer : python gen_lecons.py <dossier data>"""
import json, os, sys
from schemas import lecon_triangle, lecon_traite, lecon_habitation, lecon_produits, lecon_abolitions

BO = "Programme d'histoire-géographie du cycle 3, arrêté du 22 avril 2026, BO n° 22 du 28 mai 2026 (thème « Explorations et conquêtes »)"
BNF = "BnF, France-Amériques, « La traite négrière » (C. Vidal, 2021, d'après Slave Voyages)"


def L(id, salle, icone, titre, objectifs, cm1, cm2, lexique, schema_titre, svg, sources, document=None):
    l = {"id": id, "salle": salle, "icone": icone, "titre": titre, "duree": "4 min", "niveau": "CM1-CM2", "objectifs": objectifs,
         "contenu": {"cm1": cm1, "cm2": cm2}, "lexique": [{"mot": m, "def": d} for m, d in lexique],
         "schema": {"titre": schema_titre, "svg": svg}}
    if document:
        l["document"] = document
    l["sources"] = sources
    return l


LECONS = [
    L("triangle", 1, "1", "Le commerce triangulaire",
      ["Situer l'Europe, l'Afrique et les Amériques autour de l'océan Atlantique", "Décrire les trois trajets d'un navire négrier",
       "Nommer les marchandises transportées à chaque trajet", "CM2 : connaître le rôle de l'armateur et la principale destination des navires français"],
      "<h4>Trois continents</h4><p>Du XVIIe au XIXe siècle, des navires partent des ports d'<b>Europe</b>, vont en <b>Afrique</b>, traversent l'océan <b>Atlantique</b> vers les <b>Amériques</b>, puis reviennent en Europe. Sur une carte, ce voyage dessine un triangle : on parle de <b>commerce triangulaire</b>.</p>"
      "<h4>Trois trajets</h4><p>Au premier trajet, le navire emporte des tissus, des armes et de l'alcool vers l'Afrique. Ces marchandises sont échangées contre des captifs africains. Au deuxième trajet, les captifs sont emmenés de force vers les Amériques, où ils sont vendus comme esclaves. Au troisième trajet, le navire revient en Europe avec du sucre, du café ou du coton.</p>",
      "<h4>Un voyage en triangle</h4><p>Du XVIIe au XIXe siècle, des négociants européens organisent un commerce qui relie trois continents autour de l'océan Atlantique. Sur une carte, les trois trajets du navire dessinent un triangle : on parle de commerce triangulaire. Les historiens parlent aussi de traite atlantique.</p>"
      "<h4>L'armateur et son navire</h4><p>L'armateur est le négociant qui finance le navire, recrute l'équipage et achète la cargaison. Le navire quitte un port français chargé de tissus, de fusils, de poudre et d'eau-de-vie.</p>"
      "<h4>Les trois trajets</h4><p>Sur les côtes d'Afrique, ces marchandises sont échangées contre des captifs. La traversée de l'Atlantique avec les captifs dure en moyenne environ deux mois. Aux Antilles, les captifs sont vendus comme esclaves à des propriétaires de plantations. Le navire revient en Europe chargé de sucre, de café, de coton ou d'indigo, vendus très cher.</p>"
      "<h4>Saint-Domingue</h4><p>À partir de 1715, Saint-Domingue, l'actuelle Haïti, devient la principale destination des navires français : elle reçoit environ les trois quarts des expéditions. Neuf voyages français sur dix vont aux Antilles ou en Guyane.</p><h4>Un commerce autorisé par le roi</h4><p>Les plantations des colonies d'Amérique réclament toujours plus de travailleurs : les colons y font travailler de force des Africains réduits en esclavage. Le roi autorise la traite et la confie d'abord à des compagnies, comme la Compagnie des Indes occidentales, créée en 1664. Entre 1713 et 1721, d'autres ports, dont Bordeaux, obtiennent le droit d'y participer.</p>",
      [("commerce triangulaire", "commerce entre l'Europe, l'Afrique et les Amériques, dont les trois trajets dessinent un triangle"),
       ("captif", "personne capturée et privée de liberté"), ("armateur", "négociant qui finance et équipe un navire"),
       ("cargaison", "ensemble des marchandises transportées par un navire")],
      "Les trois trajets du commerce triangulaire", lecon_triangle(),
      BO + " ; " + BNF + " ; Académie de Bordeaux, « Bordeaux et le commerce triangulaire » (d'après le musée d'Aquitaine)."),
    L("traite", 2, "2", "La traite atlantique",
      ["Savoir ce qu'est la traite négrière", "Connaître l'ampleur de la traite atlantique (des millions de personnes déportées)",
       "Citer des ports français de la traite", "CM2 : connaître des chiffres sourcés (part de la France, de Nantes, durée de la traversée)"],
      "<h4>Qu'est-ce que la traite ?</h4><p>La <b>traite négrière</b> est le commerce de captifs achetés en Afrique et vendus comme esclaves en Amérique. Des <b>millions</b> de personnes ont ainsi été arrachées à leur famille et à leur pays.</p>"
      "<h4>Le navire négrier</h4><p>Des navires partent de ports français comme Nantes, La Rochelle ou Le Havre. Les captifs sont enchaînés et entassés dans le navire. La traversée de l'océan dure environ deux mois. Beaucoup meurent en route.</p>",
      "<h4>Plus de trois siècles</h4><p>La traite atlantique a duré du XVIe au XIXe siècle. Plus de 12,5 millions de personnes ont été déportées d'Afrique vers les Amériques. Les captifs ne partaient pas de leur plein gré : ils étaient achetés sur les côtes d'Afrique, comme le Sénégal, le golfe du Bénin ou la côte de Loango, puis transportés de force.</p>"
      "<h4>La part de la France</h4><p>Les navires français ont transporté environ 11 % des captifs de la traite atlantique, soit plus de 1,3 million de personnes. Nantes, premier port négrier français, a armé 44 % des expéditions françaises ; d'autres partaient du Havre, de La Rochelle, de Saint-Malo, d'Honfleur ou de Bordeaux.</p>"
      "<h4>La traversée</h4><p>En moyenne, un navire français transportait environ 320 captifs. La traversée durait environ deux mois. Environ 13 % des captifs mouraient pendant la traversée, et environ 27 % des captifs étaient des enfants. Les captifs ne passaient pas par la France : ils étaient conduits directement d'Afrique aux Amériques.</p><h4>Comment le sait-on ?</h4><p>À bord, les captifs sont séparés de leurs proches, entassés, dans des conditions d'hygiène terribles. Des révoltes éclatent parfois à bord, et l'équipage les réprime avec violence. Les historiens reconstituent cette histoire grâce aux registres des navires, aux journaux de bord et aux archives des ports. La base de données Slave Voyages rassemble les informations connues sur des dizaines de milliers de voyages.</p>",
      [("traite négrière", "commerce de captifs africains vendus comme esclaves"), ("navire négrier", "navire qui transporte des captifs"),
       ("déporter", "emmener de force loin de son pays"), ("esclave", "personne privée de liberté, qui appartient à un maître")],
      "La traite atlantique : plus de trois siècles", lecon_traite(),
      BO + " ; " + BNF + " ; Musée d'histoire de Nantes (château des ducs de Bretagne)."),
    L("plantations", 3, "3", "La vie dans les plantations",
      ["Décrire le travail forcé des esclaves dans une plantation de canne à sucre", "Savoir ce qu'est le Code noir (1685)",
       "Connaître des formes de résistance, dont le marronnage", "CM2 : distinguer petit et grand marronnage"],
      "<h4>Le travail forcé</h4><p>Aux Antilles, les esclaves travaillent de force, sans salaire, dans les plantations de canne à sucre. Ils coupent la canne, la portent au <b>moulin</b> qui la broie, puis le jus est transformé en sucre dans la <b>sucrerie</b>.</p>"
      "<h4>Le Code noir</h4><p>En 1685, le roi Louis XIV signe le <b>Code noir</b>. Cette loi fixe les règles de l'esclavage dans les colonies. Elle considère l'esclave comme un bien que l'on peut vendre.</p>"
      "<h4>Résister</h4><p>Les esclaves n'acceptent pas leur sort. Certains s'enfuient : ce sont les <b>marrons</b>. D'autres se révoltent. Tous gardent des chants, des contes et des croyances venus d'Afrique.</p>",
      "<h4>L'habitation sucrière</h4><p>Aux Antilles, la plantation s'appelle une habitation. Pendant la récolte, de janvier à juin environ, les esclaves coupent la canne, enlèvent les feuilles et la mettent en paquets. Au moulin, la canne est broyée pour récolter le vesou, le jus de canne. Le vesou est transformé en sucre dans la sucrerie, puis le sucre passe par la purgerie. Pendant la récolte, la journée de travail pouvait dépasser 18 heures.</p>"
      "<h4>Le Code noir</h4><p>Le Code noir est un édit du roi Louis XIV, signé en mars 1685. Il donne un cadre légal à l'esclavage dans les colonies. Il considère les esclaves comme des « biens meubles », privés de tout droit. Il prévoit des punitions très sévères. En 2026, une loi l'a officiellement abrogé.</p>"
      "<h4>Les résistances</h4><p>Le marronnage est la fuite des esclaves hors de la plantation. Le petit marronnage est une fuite de quelques jours. Le grand marronnage est une fuite sans retour : les marrons forment des groupes qui vivent dans la forêt ou les montagnes. Le mot marron vient de l'espagnol cimarrón, qui veut dire « fuir ». Les révoltes sont une autre forme de résistance.</p><h4>Une société très inégale</h4><p>Sur l'habitation, la grande majorité des esclaves travaillent dans les champs. Certains sont affectés au moulin, d'autres servent dans la maison du maître. Un économe organise le travail des ateliers. Les journées épuisantes, la mauvaise nourriture et le manque d'hygiène provoquent de nombreux décès.</p>",
      [("habitation", "nom de la plantation aux Antilles"), ("vesou", "jus de la canne à sucre"), ("édit", "loi signée par le roi"),
       ("marron", "esclave qui s'est enfui"), ("affranchi", "esclave devenu libre")],
      "Une habitation sucrière aux Antilles (plan simplifié)", lecon_habitation(),
      BO + " ; Académie de Martinique, « Le travail à l'habitation-sucrerie » (M. Descas-Ravoteur) ; Académie de Guyane, livret « Le marronnage » ; Sénat, rapport sur l'abrogation du Code noir (2026).",
      document={"type": "texte", "titre": "Le Code noir, expliqué simplement",
                "contenu": "Le Code noir est un édit du roi Louis XIV, signé en mars 1685. Il donne un cadre légal à l'esclavage dans les colonies. Il traite l'esclave comme un objet que l'on possède, et non comme une personne.",
                "source": "Reformulation pour le cycle 3, d'après le rapport du Sénat sur l'abrogation du Code noir (2026)."}),
    L("ports", 4, "4", "Les échanges avec les colonies",
      ["Nommer les produits venus des colonies d'Amérique", "Nommer les marchandises chargées en France pour l'Afrique",
       "Situer des ports français de l'Atlantique et de la Manche", "CM2 : expliquer l'enrichissement de certains ports, sans généraliser à toute la France"],
      "<h4>Ce qui part, ce qui revient</h4><p>Pour l'Afrique, les navires emportent des tissus, des fusils et de l'eau-de-vie. Des colonies d'Amérique, ils rapportent du <b>sucre</b>, du <b>café</b> et du <b>coton</b>.</p>"
      "<h4>Les ports</h4><p>Nantes, La Rochelle, Le Havre et Bordeaux sont des ports de l'Atlantique ou de la Manche. Le commerce avec les colonies a enrichi ces villes. Une ville loin de la mer, comme Dijon, n'armait pas de navires.</p>",
      "<h4>Les produits des colonies</h4><p>Dans les colonies d'Amérique, les esclaves cultivent des produits vendus très cher en Europe : le sucre de canne, le café, le cacao qui donne le chocolat, le coton qui sert à tisser des étoffes, l'indigo qui donne une teinture bleue.</p>"
      "<h4>Les cargaisons</h4><p>Pour acheter des captifs, les navires emportent des toiles et des draperies, des fusils et de la poudre, de l'eau-de-vie et du vin, du fer en barre. En janvier 1787, La Licorne quitte Bordeaux avec une telle cargaison. Le même navire transporte donc, à chaque trajet, une cargaison différente : des marchandises, puis des captifs, puis des denrées coloniales.</p>"
      "<h4>Des ports enrichis</h4><p>Au XVIIIe siècle, Nantes est le premier port négrier français et devient un grand port colonial : la ville s'enrichit visiblement. Bordeaux s'enrichit aussi du commerce des produits coloniaux. Ces richesses viennent du travail forcé des esclaves. Chaque port a son histoire : on ne généralise pas l'histoire d'un port à toute la France.</p><h4>Les traces dans les villes</h4><p>Aujourd'hui, des musées racontent cette histoire. À Nantes, le musée d'histoire, installé au château des ducs de Bretagne, y consacre en tout ou en partie quatorze salles. À Bordeaux, le musée d'Aquitaine présente le commerce atlantique et l'esclavage. Ces lieux montrent aussi les personnes réduites en esclavage, leurs résistances et les combats pour l'abolition.</p>",
      [("colonie", "territoire dominé et exploité par un pays lointain"), ("denrée coloniale", "produit venu des colonies : sucre, café, cacao"),
       ("indigo", "plante qui donne une teinture bleue"), ("port négrier", "port d'où partent des navires de la traite")],
      "Ce qui part des ports, ce qui y revient", lecon_produits(),
      BO + " ; Académie de Bordeaux, « Bordeaux et le commerce triangulaire » (d'après le musée d'Aquitaine) ; Musée d'histoire de Nantes ; " + BNF + "."),
    L("abolitions", 5, "5", "Résistances et abolitions",
      ["Connaître la révolte de Saint-Domingue et Toussaint Louverture", "Situer les abolitions de 1794 et de 1848 sur une frise",
       "Savoir pourquoi le 10 mai est une journée de mémoire", "CM2 : connaître le rétablissement de 1802, l'indépendance d'Haïti (1804) et la loi du 21 mai 2001"],
      "<h4>La révolte de Saint-Domingue</h4><p>En 1791, les esclaves de Saint-Domingue se révoltent. <b>Toussaint Louverture</b>, né esclave, devient l'un de leurs chefs.</p>"
      "<h4>Deux abolitions</h4><p>En 1794, l'esclavage est aboli une première fois. En 1802, Napoléon Bonaparte le rétablit. En 1848, il est aboli définitivement, grâce au travail de <b>Victor Schœlcher</b>.</p>"
      "<h4>Se souvenir</h4><p>Chaque <b>10 mai</b>, la France se souvient de la traite, de l'esclavage et de leurs abolitions.</p>",
      "<h4>Saint-Domingue et Haïti</h4><p>En août 1791, une insurrection d'esclaves éclate dans la plaine du nord de Saint-Domingue. Toussaint Louverture, né esclave vers 1740, devient l'un de ses chefs, puis gouverneur de la colonie en 1798. Il meurt prisonnier en France. Le 1er janvier 1804, Saint-Domingue devient Haïti, un pays indépendant fondé par d'anciens esclaves.</p>"
      "<h4>Abolir, rétablir, abolir</h4><p>Le 4 février 1794, la Convention abolit l'esclavage dans les colonies françaises. Le 20 mai 1802, Napoléon Bonaparte, Premier consul, rétablit l'esclavage et la traite. Le décret du 27 avril 1848 abolit définitivement l'esclavage dans toutes les colonies françaises. Victor Schœlcher a présidé la commission qui l'a préparé. L'abolition prend effet dans chaque colonie deux mois après la promulgation du décret dans cette colonie.</p>"
      "<h4>La mémoire</h4><p>La loi du 21 mai 2001 reconnaît la traite et l'esclavage comme un crime contre l'humanité. Depuis 2006, le 10 mai est la journée nationale des mémoires de la traite, de l'esclavage et de leurs abolitions.</p><h4>Les combats pour la liberté</h4><p>Les révoltes des esclaves, comme celle de Saint-Domingue, ont pesé sur les décisions prises à Paris. En France, des abolitionnistes ont milité pendant des années, comme Victor Schœlcher. En 2026, une loi a officiellement abrogé le Code noir. Ce texte n'avait plus d'effet depuis 1848, mais son abrogation rappelle que l'esclavage a été inscrit dans la loi.</p>",
      [("abolir", "supprimer par une loi"), ("insurrection", "révolte d'un grand nombre de personnes"),
       ("crime contre l'humanité", "crime si grave qu'il concerne toute l'humanité et ne peut pas être oublié"), ("mémoire", "souvenir que l'on garde et que l'on transmet")],
      "Résistances et abolitions", lecon_abolitions(),
      BO + " ; " + BNF + " ; BnF, France-Amériques, « Toussaint Louverture » ; Hérodote, « 1er janvier 1804 » ; décret du 27 avril 1848 ; ministère de la Culture (loi n° 2001-434 du 21 mai 2001, décret n° 2006-388).",
      document={"type": "texte", "titre": "Article 1er du décret du 27 avril 1848",
                "contenu": "« L'esclavage sera entièrement aboli dans toutes les colonies et possessions françaises, deux mois après la promulgation du présent décret dans chacune d'elles. »",
                "source": "Décret du gouvernement provisoire du 27 avril 1848 (texte : mjp.univ-perp.fr)."}),
]


def main(dest):
    json.dump({"lecons": LECONS}, open(os.path.join(dest, "lecons.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
