# -*- coding: utf-8 -*-
"""Génère vivant-ecosystemes/assets/data/lecons.json (5 leçons). Lancer : python gen_lecons.py <dossier data>
Le texte CM2 est fait des phrases de fiches.py (reprises mot pour mot par les justifications des grades)."""
import json, os, sys
from schemas import lecon_oiseau, emboitement, frise, lecon_mare, reseau
import fiches as F

BO = "Programme de sciences et technologie, cycle 3 (BO n° 24 du 11 juin 2026, annexe 2) : « Unité et diversité du vivant » et « Les écosystèmes » (progression de l'enseignant : année A, période 4)"
MNHN = "Muséum national d'histoire naturelle et INPN"
LAMAP = "Fondation La main à la pâte"


def L(id, salle, titre, objectifs, cm1, cm2, lexique, schema_titre, svg, sources, document=None):
    l = {"id": id, "salle": salle, "icone": str(salle), "titre": titre, "duree": "4 min", "niveau": "CM1-CM2", "objectifs": objectifs,
         "contenu": {"cm1": cm1, "cm2": cm2}, "lexique": [{"mot": m, "def": d} for m, d in lexique],
         "schema": {"titre": schema_titre, "svg": svg}}
    if document:
        l["document"] = document
    l["sources"] = sources
    return l


LECONS = [
    L("espece", 1, "Observer le vivant, l'espèce",
      ["Décrire un être vivant par ses attributs (ce qu'il possède)", "Savoir ce qu'est une espèce",
       "CM2 : savoir pourquoi l'âne et le cheval sont deux espèces", "Pour aller plus loin (6e) : la cellule, unité du vivant"],
      "<h4>Observer</h4><p>Pour décrire un être vivant, on regarde ce qu'il <b>possède</b> : des plumes, des poils, une coquille, des pattes, des ailes. Ce sont ses <b>attributs</b>. On compte avec précision : six pattes, huit pattes, quatre ailes.</p>"
      "<h4>L'espèce</h4><p>Les êtres vivants d'une même <b>espèce</b> se ressemblent et peuvent avoir des petits ensemble ; leurs petits pourront eux aussi avoir des petits. Un caniche et un berger allemand sont très différents, mais ce sont deux chiens : ils sont de la même espèce.</p>"
      "<h4>L'inventaire</h4><p>Noter toutes les espèces d'un lieu, c'est faire son <b>inventaire</b>. Plus il y a d'espèces, plus la biodiversité est grande.</p>",
      F.html(F.LECON_ESPECE),
      [("attribut", "ce que possède un être vivant et que l'on peut observer"), ("espèce", "êtres vivants qui se ressemblent et peuvent avoir ensemble des petits, eux-mêmes capables d'avoir des petits"),
       ("biodiversité", "la diversité des êtres vivants : des espèces, et des individus dans chaque espèce"), ("inventaire", "liste des espèces observées dans un lieu"),
       ("cellule", "plus petit élément vivant ; tous les êtres vivants en sont faits (6e)")],
      "Observer les attributs", lecon_oiseau(), BO + " ; " + MNHN + " ; " + LAMAP + "."),
    L("classer", 2, "Classer et identifier",
      ["Ranger des êtres vivants dans des groupes emboîtés selon leurs attributs", "Savoir qu'on ne classe ni sur une absence ni sur le lieu de vie",
       "Utiliser une clé de détermination pour identifier", "CM2 : distinguer identifier et classer ; parler de parenté"],
      "<h4>Classer</h4><p>On range les êtres vivants dans des <b>groupes</b> selon ce qu'ils <b>possèdent en commun</b> : des poils, des plumes, six pattes. Les groupes sont <b>emboîtés</b>, comme des boîtes dans des boîtes. Le lieu de vie et la nourriture ne servent pas à classer : la chauve-souris vole, mais elle a des poils.</p>"
      "<h4>Identifier</h4><p>Pour trouver le nom d'une petite bête, on suit une <b>clé de détermination</b> : on répond à des questions simples (a-t-elle des pattes ? combien ?) jusqu'à son nom. Les insectes ont six pattes, les araignées huit.</p>",
      F.html(F.LECON_CLASSER),
      [("classer", "ranger dans des groupes selon des attributs communs"), ("groupes emboîtés", "groupes rangés les uns dans les autres"),
       ("clé de détermination", "suite de questions qui permet de trouver le nom d'un être vivant"), ("parenté", "lien entre des espèces qui partagent beaucoup d'attributs"),
       ("ancêtre commun", "espèce disparue dont descendent plusieurs espèces actuelles (6e)")],
      "Des groupes emboîtés", emboitement(), BO + " ; " + LAMAP + " ; " + MNHN + "."),
    L("fossiles", 3, "La biodiversité passée",
      ["Savoir ce qu'est un fossile", "Placer quelques repères sur l'échelle des temps géologiques",
       "CM2 : manipuler des millions et des milliards d'années", "CM2 : décrire l'extinction massive d'il y a 66 millions d'années et ce qui a suivi"],
      "<h4>Les fossiles</h4><p>Un <b>fossile</b> est le reste ou la trace d'un être vivant très ancien, conservé dans une roche : une coquille, un os, une dent, une empreinte de feuille.</p>"
      "<h4>Une très longue histoire</h4><p>La Terre est très ancienne. La vie est apparue d'abord dans la mer. Les <b>dinosaures</b> ont vécu pendant très longtemps, puis ont disparu, bien avant l'arrivée des humains : aucun humain n'a vu de dinosaure vivant.</p>"
      "<h4>Des espèces apparaissent, d'autres disparaissent</h4><p>Les fossiles montrent que la biodiversité <b>change</b> au cours du temps. Les oiseaux descendent de petits dinosaures à plumes.</p>",
      F.html(F.LECON_FOSSILES),
      [("fossile", "reste ou trace d'un être vivant ancien conservé dans une roche"), ("temps géologique", "temps de l'histoire de la Terre, compté en millions d'années"),
       ("extinction massive", "disparition d'un très grand nombre d'espèces en peu de temps"), ("ammonite", "animal marin à coquille enroulée, disparu il y a 66 millions d'années"),
       ("trilobite", "animal marin à carapace, disparu il y a 252 millions d'années")],
      "Quelques repères du temps géologique", frise(), BO + " ; académie de Martinique, « Marche des temps géologiques » ; Espace des sciences, Sciences Ouest n° 413.",
      document={"type": "texte", "titre": "Repères chiffrés",
                "contenu": "Formation de la Terre : environ 4,6 milliards d'années. Premières traces de vie : environ 3,8 milliards d'années. Trilobites : il y a 540 millions d'années, disparus il y a 252 millions d'années. Disparition des dinosaures et des ammonites : il y a environ 66 millions d'années. Homo sapiens : environ 300 000 ans.",
                "source": "Académie de Martinique, « Marche des temps géologiques » (2024) ; Espace des sciences, Sciences Ouest n° 413."}),
    L("ecosysteme", 4, "L'écosystème",
      ["Définir un écosystème : un milieu de vie, des êtres vivants et leurs relations", "Décrire un milieu par ses caractéristiques physiques",
       "Relier la présence d'un être vivant aux caractéristiques du milieu", "Reconnaître une prédation et une coopération"],
      "<h4>Un milieu et des êtres vivants</h4><p>Une mare, une forêt, une prairie sont des <b>écosystèmes</b> : un <b>milieu de vie</b> (l'eau, la lumière, la température, l'humidité) et les <b>êtres vivants</b> qui l'habitent. Chaque être vivant vit là où le milieu lui convient : le nénuphar dans une eau calme et ensoleillée.</p>"
      "<h4>Des relations</h4><p>Le héron attrape les grenouilles : c'est une <b>prédation</b>. L'abeille boit le nectar de la fleur et transporte son pollen : chacun y gagne, c'est une <b>coopération</b>.</p>",
      F.html(F.LECON_ECO),
      [("écosystème", "un milieu de vie, les êtres vivants qui l'habitent et leurs relations"), ("milieu de vie", "lieu décrit par sa température, sa lumière, son humidité…"),
       ("prédation", "relation où un prédateur mange sa proie"), ("coopération", "relation où chacun gagne"), ("pollen", "poudre des fleurs nécessaire à la formation des graines")],
      "La mare : un milieu de vie et des êtres vivants", lecon_mare(), BO + " ; " + LAMAP + " ; " + MNHN + " ; Office français de la biodiversité."),
    L("reseau", 5, "Le réseau alimentaire",
      ["Représenter « est mangé par » par une flèche de la proie vers celui qui la mange", "Construire une chaîne, puis un réseau alimentaire",
       "Prévoir l'effet d'une forte variation du nombre d'individus d'une espèce", "Connaître des actions humaines qui perturbent ou protègent un écosystème"],
      "<h4>Qui mange qui ?</h4><p>Les animaux mangent d'autres êtres vivants pour grandir. On dessine une <b>flèche</b> qui va de celui qui est mangé vers celui qui le mange : algues → têtard → larve de libellule → perche → héron. Les chaînes se croisent : elles forment un <b>réseau alimentaire</b>.</p>"
      "<h4>Quand une espèce change</h4><p>Si une espèce devient trop nombreuse ou disparaît, tout le réseau est touché. Un animal venu d'ailleurs, comme l'<b>écrevisse de Louisiane</b>, peut tout déséquilibrer : on ne relâche jamais un animal exotique dans la nature. Creuser une mare ou garder des haies aide les êtres vivants.</p>",
      F.html(F.LECON_RESEAU),
      [("réseau alimentaire", "ensemble des chaînes « est mangé par » d'un écosystème"), ("proie", "être vivant mangé par un autre"), ("prédateur", "animal qui mange d'autres animaux"),
       ("espèce exotique envahissante", "espèce venue d'ailleurs qui se multiplie et perturbe l'écosystème"), ("décomposition", "transformation des restes d'êtres vivants en matière du sol (6e)")],
      "Le réseau alimentaire de l'étang", reseau(), BO + " ; " + LAMAP + " ; Centre de ressources Espèces exotiques envahissantes (OFB, UICN) ; MNHN, inventaire du frelon asiatique."),
]


def main(dest):
    json.dump({"lecons": LECONS}, open(os.path.join(dest, "lecons.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
