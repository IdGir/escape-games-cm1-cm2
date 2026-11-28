# -*- coding: utf-8 -*-
"""Génère napoleon-republique/assets/data/lecons.json (5 leçons). Lancer : python gen_lecons.py <dossier data>
Le texte CM2 est fait des phrases de fiches.py (reprises mot pour mot par les justifications des grades)."""
import json, os, sys
from schemas import carte_europe, sacre, paris, place, frise
import fiches as F

BO = "Programme d'histoire du cycle 3 (BO n° 22 du 28 mai 2026), le temps de la Révolution et de l'Empire ; progression de l'enseignant : thème 4, année B, période 4"
FN = "Fondation Napoléon (napoleon.org)"


def L(id, salle, titre, objectifs, cm1, cm2, lexique, schema_titre, svg, sources, document=None):
    l = {"id": id, "salle": salle, "icone": str(salle), "titre": titre, "duree": "4 min", "niveau": "CM1-CM2", "objectifs": objectifs,
         "contenu": {"cm1": cm1, "cm2": cm2}, "lexique": [{"mot": m, "def": d} for m, d in lexique],
         "schema": {"titre": schema_titre, "svg": svg}}
    if document:
        l["document"] = document
    l["sources"] = sources
    return l


FRISE = frise([(1769.6, "naissance"), (1793.97, "Toulon"), (1799.85, "18 brumaire"), (1804.92, "sacre"), (1805.92, "Austerlitz"),
               (1812.7, "Moscou"), (1815.46, "Waterloo"), (1821.35, "mort")])

LECONS = [
    L("general", 1, "Du général au Premier consul (1769-1802)",
      ["Situer la naissance de Bonaparte (1769, Corse) et ses premières victoires", "Savoir comment il prend le pouvoir : le coup d'État de 1799",
       "Comprendre ce qu'est le Consulat", "CM2 : dater Toulon, les Pyramides, le 18 brumaire, le Concordat"],
      "<h4>Un jeune officier</h4><p>Napoléon Bonaparte naît en <b>1769</b> en <b>Corse</b>. Il devient officier. En <b>1793</b>, il aide l'armée de la République à reprendre le port de <b>Toulon</b> : il devient général.</p>"
      "<h4>Un général célèbre</h4><p>Il gagne de nombreuses batailles en <b>Italie</b>, puis part en <b>Égypte</b> avec une armée et des savants. Les journaux et les tableaux racontent ses victoires : il devient très populaire.</p>"
      "<h4>Le Premier consul</h4><p>En <b>1799</b>, il prend le pouvoir par un <b>coup d'État</b>. Trois consuls gouvernent, mais Bonaparte, le <b>Premier consul</b>, décide de presque tout.</p>",
      F.html(F.LECON_GENERAL),
      [("général", "officier qui commande une grande partie de l'armée"), ("coup d'État", "prise du pouvoir par la force"),
       ("Consulat", "régime de 1799 à 1804, dirigé par trois consuls"), ("Premier consul", "le consul qui a presque tous les pouvoirs : Bonaparte"),
       ("Concordat", "accord signé avec le pape en 1801"), ("brumaire", "deuxième mois du calendrier républicain (octobre-novembre)")],
      "La vie de Napoléon Bonaparte", FRISE, BO + " ; " + FN + " ; Histoire par l'image."),
    L("sacre", 2, "Le sacre et la naissance de l'Empire (1804)",
      ["Dater la naissance de l'Empire (1804)", "Décrire le sacre à Notre-Dame et lire le tableau de David",
       "Reconnaître les symboles de l'Empire : aigle, abeilles, couronne de lauriers", "CM2 : savoir que l'Empire est héréditaire"],
      "<h4>Un empereur</h4><p>En <b>1804</b>, Bonaparte devient <b>empereur des Français</b> : il s'appelle désormais <b>Napoléon Ier</b>. Le pouvoir doit passer à son fils, comme pour un roi.</p>"
      "<h4>Le sacre</h4><p>Le <b>2 décembre 1804</b>, il est sacré dans la cathédrale <b>Notre-Dame de Paris</b>, en présence du <b>pape</b>. Il pose lui-même la couronne sur sa tête, puis il couronne l'impératrice <b>Joséphine</b>. Le peintre <b>David</b> a peint cette scène dans un immense tableau.</p>"
      "<h4>Les symboles</h4><p>L'<b>aigle</b>, les <b>abeilles d'or</b> et la <b>couronne de lauriers</b> deviennent les symboles de l'Empire.</p>",
      F.html(F.LECON_SACRE),
      [("empereur", "souverain qui dirige un empire"), ("sacre", "cérémonie religieuse qui consacre un souverain"),
       ("héréditaire", "qui passe des parents aux enfants"), ("plébiscite", "vote où l'on répond par oui ou par non"),
       ("emblème", "objet ou animal qui représente un pays ou un régime"), ("sceptre", "bâton, symbole du pouvoir du souverain")],
      "Lire le tableau du Sacre", sacre(5, avec_noms=True), BO + " ; " + FN + " ; Musée du Louvre."),
    L("conquetes", 3, "Les conquêtes et la chute (1805-1821)",
      ["Connaître quelques grandes batailles : Austerlitz (1805), la campagne de Russie (1812), Waterloo (1815)", "Situer ces lieux sur une carte de l'Europe",
       "Savoir que Napoléon finit sa vie en exil à Sainte-Hélène", "CM2 : mesurer le coût humain des guerres de l'Empire"],
      "<h4>Les victoires</h4><p>Napoléon fait la guerre à plusieurs pays d'Europe. Il gagne de grandes batailles, comme à <b>Austerlitz</b> en <b>1805</b>. Vers 1811, l'Empire domine une grande partie de l'Europe.</p>"
      "<h4>La Russie</h4><p>En <b>1812</b>, il envahit la <b>Russie</b> et entre dans <b>Moscou</b>. Mais pendant la retraite, le froid et la faim font disparaître la plus grande partie de son armée.</p>"
      "<h4>La chute</h4><p>Les pays d'Europe s'unissent contre lui. Il est battu à <b>Waterloo</b>, en Belgique, en <b>1815</b>, et exilé sur l'île de <b>Sainte-Hélène</b>, où il meurt en <b>1821</b>. Ses guerres ont fait des centaines de milliers de morts.</p>",
      F.html(F.LECON_CONQUETES),
      [("Grande Armée", "l'armée de Napoléon, avec des soldats de toute l'Europe"), ("campagne", "longue expédition militaire"),
       ("retraite", "mouvement d'une armée qui recule"), ("abdiquer", "renoncer au pouvoir"),
       ("exil", "obligation de vivre loin de son pays"), ("Cent-Jours", "retour de Napoléon au pouvoir en 1815, environ cent jours")],
      "L'Europe de Napoléon", carte_europe(5, avec_noms=True), BO + " ; " + FN + " ; Musée de l'Armée."),
    L("heritage", 4, "Ce qui reste de l'Empire",
      ["Connaître les institutions créées par Bonaparte : Code civil, préfets, lycées, Banque de France, Légion d'honneur",
       "Reconnaître les monuments de l'Empire à Paris", "Comprendre la part d'ombre : guerres, censure, rétablissement de l'esclavage",
       "CM2 : dater les principales créations (1800-1804)"],
      "<h4>Des créations qui durent</h4><p>Bonaparte organise la France. Il crée les <b>préfets</b>, la <b>Banque de France</b>, les <b>lycées</b> et la <b>Légion d'honneur</b>. En <b>1804</b>, le <b>Code civil</b> réunit les lois dans un seul livre : tous les hommes sont égaux devant la loi. Tout cela existe encore aujourd'hui.</p>"
      "<h4>Une part d'ombre</h4><p>Mais l'Empire n'est pas une démocratie : les journaux sont censurés et les opposants arrêtés. Les femmes mariées doivent obéir à leur mari. En <b>1802</b>, Bonaparte rétablit l'<b>esclavage</b> dans les colonies.</p>"
      "<h4>Des monuments</h4><p>À Paris, l'<b>Arc de triomphe</b> et la <b>colonne Vendôme</b> célèbrent les victoires. Le tombeau de Napoléon est sous le dôme des <b>Invalides</b>.</p>",
      F.html(F.LECON_HERITAGE),
      [("Code civil", "livre qui réunit les lois sur les personnes, la famille et les biens (1804)"), ("préfet", "représentant du gouvernement dans un département"),
       ("lycée", "établissement créé en 1802 pour former les futurs cadres du pays"), ("Légion d'honneur", "décoration qui récompense les mérites"),
       ("censure", "contrôle et interdiction de ce qui est publié"), ("esclavage", "situation d'une personne privée de liberté et traitée comme un objet")],
      "Paris : les monuments de l'Empire", paris(), BO + " ; " + FN + " ; Banque de France ; Musée de l'Armée.",
      document={"type": "texte", "titre": "Les « masses de granit » (dates officielles)",
                "contenu": "Banque de France : 18 janvier 1800. Préfets : 17 février 1800. Lycées : 1er mai 1802. Légion d'honneur : 19 mai 1802. Code civil : 21 mars 1804. Rétablissement de l'esclavage : 1802 ; abolition définitive : 1848.",
                "source": "Fondation Napoléon, « Masses de granit » ; Banque de France."}),
    L("republique", 5, "Lieux, symboles et rites de la République",
      ["Connaître les symboles de la République : drapeau, devise, Marseillaise, Marianne, 14 juillet", "Nommer des lieux de la République : mairie, école, monument aux morts",
       "Connaître quelques rites : le vote, le mariage à la mairie, les cérémonies", "CM2 : savoir que l'article 2 de la Constitution de 1958 fixe les symboles"],
      "<h4>Les symboles</h4><p>La République a ses symboles : le <b>drapeau tricolore</b> bleu, blanc, rouge ; la <b>devise</b> « Liberté, Égalité, Fraternité » ; l'hymne national, la <b>Marseillaise</b> ; <b>Marianne</b>, qui la représente ; la fête nationale du <b>14 juillet</b>.</p>"
      "<h4>Les lieux et les rites</h4><p>La <b>mairie</b> et l'<b>école</b> sont des lieux de la République. À la mairie, on se marie et on <b>vote</b>. Devant le <b>monument aux morts</b>, on se souvient des victimes des guerres, le 8 Mai et le 11 Novembre.</p>"
      "<h4>Des droits protégés</h4><p>Nos droits et nos libertés sont protégés par la Déclaration des droits de l'homme et du citoyen et par la Constitution.</p>",
      F.html(F.LECON_REPUBLIQUE),
      [("République", "régime où le pouvoir appartient au peuple, qui élit ses représentants"), ("devise", "courte phrase qui exprime un idéal"),
       ("hymne", "chant officiel d'un pays"), ("Marianne", "figure de femme qui représente la République"),
       ("rite", "geste ou cérémonie répétés qui ont un sens pour tous"), ("Constitution", "texte qui fixe les règles de fonctionnement de l'État")],
      "La place de la commune", place(5, avec_noms=True), BO + " ; Constitution de 1958, article 2 ; Présidence de la République ; vie-publique.fr."),
]


def main(dest):
    json.dump({"lecons": LECONS}, open(os.path.join(dest, "lecons.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
