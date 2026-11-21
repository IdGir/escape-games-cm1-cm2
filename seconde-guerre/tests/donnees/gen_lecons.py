# -*- coding: utf-8 -*-
"""Génère seconde-guerre/assets/data/lecons.json (5 leçons). Lancer : python gen_lecons.py <dossier data>
Le texte CM2 est fait des phrases de fiches.py (reprises mot pour mot par les justifications des grades).
Leçon 3 : les persécutions et la Shoah sont enseignées avec sobriété, sans image ; aucune énigme notée n'en dépend."""
import json, os, sys
from schemas import carte_1940, carte_1944, frise, resistance
import fiches as F

BO = "Programme d'histoire du cycle 3 (BO n° 22 du 28 mai 2026), Seconde Guerre mondiale ; progression de l'enseignant : thème 6, année A, période 5"
CDM = "Ministère des Armées, Chemins de mémoire"


def L(id, salle, titre, objectifs, cm1, cm2, lexique, schema_titre, svg, sources, document=None):
    l = {"id": id, "salle": salle, "icone": str(salle), "titre": titre, "duree": "4 min", "niveau": "CM1-CM2", "objectifs": objectifs,
         "contenu": {"cm1": cm1, "cm2": cm2}, "lexique": [{"mot": m, "def": d} for m, d in lexique],
         "schema": {"titre": schema_titre, "svg": svg}}
    if document:
        l["document"] = document
    l["sources"] = sources
    return l


FRISE = frise([(1922.8, "Mussolini"), (1929.8, "crise"), (1933.1, "Hitler"), (1939.67, "guerre"), (1940.47, "défaite, appel"),
               (1943.1, "STO"), (1944.43, "Jour J"), (1945.35, "8 mai 1945")])

LECONS = [
    L("montee", 1, "La montée des dictatures (1919-1939)",
      ["Comprendre les effets de la crise de 1929", "Savoir ce qu'est une dictature et un régime totalitaire",
       "Situer le fascisme (Italie), le nazisme (Allemagne) et le communisme soviétique (URSS)", "CM2 : expliquer pourquoi la démocratie est menacée"],
      "<h4>La crise</h4><p>En <b>1929</b>, une grave <b>crise économique</b> commence aux États-Unis et touche le monde entier. Des usines ferment, beaucoup de gens perdent leur travail.</p>"
      "<h4>Des dictateurs</h4><p>Dans plusieurs pays, des chefs prennent tout le pouvoir : <b>Mussolini</b> en Italie, <b>Hitler</b> en Allemagne, <b>Staline</b> en Union soviétique. Ce sont des <b>dictatures</b> : un seul parti, pas d'élections libres, pas de liberté. Hitler et les nazis sont racistes et haïssent les Juifs.</p>"
      "<h4>La démocratie menacée</h4><p>La France et le Royaume-Uni restent des <b>démocraties</b>. Mais Hitler veut agrandir l'Allemagne par la force : la paix est en danger.</p>",
      F.html(F.LECON_MONTEE),
      [("crise économique", "période où les usines ferment et où beaucoup de gens perdent leur travail"), ("dictature", "régime où un chef ou un parti a tous les pouvoirs, sans liberté"),
       ("totalitaire", "se dit d'une dictature qui veut contrôler toute la vie des habitants"), ("démocratie", "régime où les citoyens choisissent librement leurs dirigeants"),
       ("antisémitisme", "haine des Juifs"), ("propagande", "images et textes qui cherchent à imposer des idées")],
      "Frise de 1919 à 1945", FRISE, BO + " ; " + CDM + " ; Lumni et Eduscol."),
    L("defaite", 2, "1939-1940 : la guerre, la défaite et Vichy",
      ["Dater le début de la guerre (septembre 1939) et la défaite (juin 1940)", "Connaître l'appel du 18 juin 1940",
       "Comprendre l'armistice et la France coupée en deux", "CM2 : définir le régime de Vichy et la collaboration"],
      "<h4>La guerre commence</h4><p>En <b>septembre 1939</b>, l'Allemagne envahit la Pologne : la France et le Royaume-Uni lui déclarent la guerre.</p>"
      "<h4>La défaite</h4><p>Au printemps <b>1940</b>, l'armée allemande attaque et bat l'armée française en quelques semaines. Des millions de Français fuient sur les routes : c'est l'<b>exode</b>. Le maréchal <b>Pétain</b> demande l'arrêt des combats. Le <b>18 juin 1940</b>, depuis Londres, le général <b>de Gaulle</b> appelle à la radio à continuer le combat.</p>"
      "<h4>Vichy</h4><p>L'<b>armistice</b> coupe la France en deux : une zone occupée par l'armée allemande et une zone non occupée. Pétain gouverne depuis <b>Vichy</b> ; il supprime la République et choisit de <b>collaborer</b> avec l'Allemagne nazie.</p>",
      F.html(F.LECON_DEFAITE),
      [("exode", "fuite de millions de personnes sur les routes en mai et juin 1940"), ("armistice", "accord qui arrête les combats"),
       ("ligne de démarcation", "frontière intérieure entre la zone occupée et la zone non occupée"), ("occupation", "présence et domination d'une armée étrangère dans un pays"),
       ("collaboration", "politique qui consiste à aider l'Allemagne nazie"), ("appel du 18 Juin", "discours radio du général de Gaulle appelant à continuer le combat")],
      "La France coupée en deux (1940)", carte_1940(5, avec_noms=True), BO + " ; " + CDM + " ; Ordre de la Libération."),
    L("occupation", 3, "Vivre sous l'Occupation",
      ["Décrire la vie quotidienne : rationnement, tickets, queues, ersatz", "Savoir ce qu'est le STO (1943)",
       "Connaître les persécutions contre les Juifs, la Shoah, et le courage des Justes", "Employer le vocabulaire exact : génocide des Juifs, Shoah"],
      "<h4>Le manque de tout</h4><p>Pendant l'Occupation, la nourriture, le charbon et les vêtements manquent. Chacun reçoit des <b>tickets de rationnement</b> : sans ticket, pas de pain ni de sucre. On fait la queue pendant des heures et on invente des <b>ersatz</b>.</p>"
      "<h4>Le travail forcé</h4><p>À partir de <b>1943</b>, des jeunes Français doivent partir travailler en Allemagne : c'est le <b>STO</b>. Beaucoup refusent et se cachent.</p>"
      "<h4>Les persécutions</h4><p>Les nazis et le régime de Vichy persécutent les <b>Juifs</b>. Des dizaines de milliers de Juifs de France, dont des enfants, sont arrêtés, déportés et assassinés : c'est la <b>Shoah</b>, le génocide des Juifs d'Europe. Des Français cachent et sauvent des Juifs en risquant leur vie : ce sont les <b>Justes</b>.</p>",
      F.html(F.LECON_OCCUPATION),
      [("rationnement", "limitation de ce que chacun a le droit d'acheter"), ("ersatz", "produit qui en remplace un autre qui manque"),
       ("marché noir", "commerce caché, à des prix très élevés"), ("STO", "Service du travail obligatoire : travail forcé en Allemagne, créé en 1943"),
       ("persécution", "traitement injuste et violent infligé à un groupe de personnes"), ("Shoah", "génocide des Juifs d'Europe par les nazis"),
       ("génocide", "crime qui veut faire disparaître tout un peuple"), ("Juste parmi les Nations", "titre donné à une personne qui a sauvé des Juifs au péril de sa vie")],
      "Frise de 1919 à 1945", FRISE, BO + " ; " + CDM + " ; USHMM, Encyclopédie de la Shoah, « France » ; ministère des Armées, « Hommage national aux Justes » ; Encyclopædia Universalis, « STO ».",
      document={"type": "texte", "titre": "Repères chiffrés (sources officielles)",
                "contenu": "Rafle du Vél d'Hiv, Paris : 16 et 17 juillet 1942, environ 13 000 Juifs arrêtés. Juifs déportés de France : 75 721 ; survivants comptés à la libération des camps : 2 566. STO : loi du 16 février 1943.",
                "source": "USHMM, Encyclopédie de la Shoah, « France » ; ministère des Armées, « Hommage national aux Justes » (2026) ; Encyclopædia Universalis, « STO »."}),
    L("resistance", 4, "La Résistance",
      ["Savoir ce que veut dire résister", "Connaître les formes de la Résistance : journaux, réseaux, maquis, Radio Londres",
       "Connaître le rôle de Jean Moulin et du Conseil national de la Résistance (1943)", "CM2 : savoir que les résistants sont une minorité courageuse"],
      "<h4>Dire non</h4><p>Des Français refusent la défaite et l'occupation : ce sont les <b>résistants</b>. Depuis Londres, le général de Gaulle dirige la <b>France libre</b>.</p>"
      "<h4>Agir en cachette</h4><p>Les résistants impriment des <b>journaux clandestins</b>, transmettent des informations aux Alliés, cachent des personnes recherchées. Le soir, ils écoutent <b>Radio Londres</b>, qui envoie des messages codés. Des jeunes qui refusent le STO forment des <b>maquis</b> dans les forêts, comme dans le Morvan.</p>"
      "<h4>S'unir</h4><p>En <b>1943</b>, <b>Jean Moulin</b> réunit les mouvements de résistance dans le <b>Conseil national de la Résistance</b>. Les résistants risquent leur vie.</p>",
      F.html(F.LECON_RESISTANCE),
      [("résistant", "personne qui lutte contre l'occupant et la collaboration"), ("clandestin", "fait en cachette, interdit par l'occupant"),
       ("maquis", "groupe de résistants cachés dans la forêt ou la montagne"), ("réseau", "groupe organisé de résistants qui recueille des renseignements"),
       ("agent de liaison", "résistant qui transporte des messages entre les groupes"), ("CNR", "Conseil national de la Résistance, réuni pour la première fois le 27 mai 1943")],
      "Comment la Résistance s'organise", resistance(), BO + " ; Fondation de la Résistance ; Ordre de la Libération ; Musée de la Résistance en Morvan."),
    L("liberation", 5, "La Libération et la victoire des Alliés",
      ["Dater le débarquement de Normandie (6 juin 1944) et la libération de Paris (25 août 1944)", "Dater la capitulation de l'Allemagne (8 mai 1945)",
       "Savoir que la République est rétablie et que les femmes votent", "CM2 : comprendre le bilan de la guerre et le « plus jamais ça »"],
      "<h4>Les débarquements</h4><p>Le <b>6 juin 1944</b>, les Alliés débarquent en <b>Normandie</b>. En août 1944, d'autres troupes débarquent en Provence.</p>"
      "<h4>La Libération</h4><p>Le <b>25 août 1944</b>, <b>Paris</b> est libéré. Les résistants aident les Alliés à libérer le pays. La <b>République</b> est rétablie et les femmes obtiennent le <b>droit de vote</b>.</p>"
      "<h4>La victoire</h4><p>Le <b>8 mai 1945</b>, l'Allemagne nazie capitule : la guerre est finie en Europe. Elle a fait des dizaines de millions de morts. Pour que cela ne recommence jamais, des pays décident de construire la paix ensemble.</p>",
      F.html(F.LECON_LIBERATION),
      [("débarquement", "arrivée d'une armée par la mer sur une côte"), ("Alliés", "pays unis contre l'Allemagne nazie : Royaume-Uni, URSS, États-Unis, France libre…"),
       ("Libération", "fin de l'occupation allemande en France, en 1944"), ("capitulation", "reddition sans condition d'une armée vaincue"),
       ("droit de vote", "droit de choisir ses représentants ; les Françaises l'obtiennent en 1944"), ("ONU", "Organisation des Nations unies, créée en 1945 pour maintenir la paix")],
      "La Libération de la France (1944)", carte_1944(5, avec_noms=True), BO + " ; Mémorial de Caen ; " + CDM + "."),
]


def main(dest):
    json.dump({"lecons": LECONS}, open(os.path.join(dest, "lecons.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
