# -*- coding: utf-8 -*-
"""Génère reproduction/assets/data/lecons.json (5 leçons). Lancer : python gen_lecons.py <dossier data>
Le texte CM2 est fait des phrases de fiches.py (reprises mot pour mot par les justifications des grades)."""
import json, os, sys
from schemas import lecon_fleur, fleur_fruit, cycle_plante, fecondation, oeuf, cycle_grenouille
import fiches as F

BO = "Programme de sciences et technologie, cycle 3 (BO n° 24 du 11 juin 2026, annexe 2) : « Les êtres vivants dans leur environnement » (progression de l'enseignant : année A, période 5)"


def L(id, salle, titre, objectifs, cm1, cm2, lexique, schema_titre, svg, sources, document=None):
    l = {"id": id, "salle": salle, "icone": str(salle), "titre": titre, "duree": "4 min", "niveau": "CM1-CM2", "objectifs": objectifs,
         "contenu": {"cm1": cm1, "cm2": cm2}, "lexique": [{"mot": m, "def": d} for m, d in lexique],
         "schema": {"titre": schema_titre, "svg": svg}}
    if document:
        l["document"] = document
    l["sources"] = sources
    return l


LECONS = [
    L("fleur", 1, "La fleur",
      ["Savoir que la fleur est l'organe de la reproduction des plantes à fleurs", "Nommer les pièces d'une fleur : sépales, pétales, étamines, pistil",
       "Distinguer les organes mâles (étamines, pollen) et femelles (pistil, ovaire, ovules)", "CM2 : savoir disséquer une fleur (programme de 6e)"],
      "<h4>Une fleur pour se reproduire</h4><p>La <b>fleur</b> sert à la <b>reproduction</b> de la plante. Les <b>sépales</b>, verts, protègent le bouton. Les <b>pétales</b>, colorés, attirent les insectes.</p>"
      "<h4>Mâle et femelle</h4><p>Les <b>étamines</b> sont les organes <b>mâles</b> : elles fabriquent le <b>pollen</b>, une poudre jaune. Le <b>pistil</b>, au centre, est l'organe <b>femelle</b> : il contient les <b>ovules</b>.</p>",
      F.html(F.LECON_FLEUR),
      [("étamine", "organe mâle de la fleur, qui fabrique le pollen"), ("pollen", "poudre fabriquée par les étamines"),
       ("pistil", "organe femelle de la fleur, au centre"), ("ovaire", "partie renflée du pistil, qui contient les ovules"),
       ("stigmate", "haut du pistil, collant, où se dépose le pollen")],
      "Les organes d'une fleur", lecon_fleur(), BO + " ; Encyclopædia Universalis, « Fleur »."),
    L("pollen", 2, "Pollinisation et fécondation",
      ["Définir la pollinisation : le transport du pollen des étamines au pistil", "Savoir que les insectes et le vent transportent le pollen",
       "Savoir que la fleur devient fruit et que les ovules deviennent graines", "CM2 : la pollinisation, une coopération ; protéger les pollinisateurs (programme de 6e)"],
      "<h4>Le voyage du pollen</h4><p>Pour faire des graines, le <b>pollen</b> doit aller des étamines jusqu'au <b>pistil</b> d'une autre fleur de la même espèce : c'est la <b>pollinisation</b>. Les <b>abeilles</b>, les bourdons et les papillons le transportent en venant boire le <b>nectar</b>. Le <b>vent</b> transporte aussi le pollen de certaines plantes, comme le maïs.</p>"
      "<h4>De la fleur au fruit</h4><p>Ensuite, les ovules sont <b>fécondés</b>. Les pétales fanent, l'ovaire grossit et devient le <b>fruit</b>, et les ovules deviennent les <b>graines</b>.</p>",
      F.html(F.LECON_POLLEN),
      [("pollinisation", "transport du pollen des étamines au pistil"), ("nectar", "liquide sucré produit par la fleur"),
       ("pollinisateur", "animal qui transporte le pollen, comme l'abeille"), ("fécondation", "union du pollen et de l'ovule, qui permet de former une graine"),
       ("fruit", "ovaire transformé, qui contient les graines")],
      "De la fleur au fruit", fleur_fruit(), BO + " ; MNHN et OFB, « Les pollinisateurs » ; La main à la pâte, « Le cycle de vie des végétaux »."),
    L("graines", 3, "Graines, dispersion et germination",
      ["Savoir ce que contient une graine", "Connaître des modes de dispersion des graines : vent, animaux, eau",
       "Connaître les besoins de la germination : eau, air, température douce", "Ordonner le cycle de vie d'une plante à fleurs (rappel du cycle 2)"],
      "<h4>Le voyage des graines</h4><p>Une <b>graine</b> contient une future plante et des réserves. Les graines s'éloignent de la plante : c'est la <b>dispersion</b>. Le <b>vent</b> emporte les graines du pissenlit, les <b>animaux</b> transportent les fruits de la bardane ou les glands, l'<b>eau</b> emporte la noix de coco.</p>"
      "<h4>La germination</h4><p>Pour <b>germer</b>, la graine a besoin d'<b>eau</b>, d'<b>air</b> et d'une <b>température douce</b>. Elle germe même dans le noir. Ensuite, la jeune plante a besoin de <b>lumière</b> pour grandir, puis elle fleurit et fait de nouvelles graines.</p>",
      F.html(F.LECON_GRAINES),
      [("graine", "partie de la plante qui contient une future plante et des réserves"), ("dispersion", "transport des graines loin de la plante mère"),
       ("germination", "moment où la graine se réveille et où la jeune plante sort"), ("embryon", "future plante, ou futur animal, au tout début de son développement"),
       ("cycle de vie", "suite des étapes de la vie d'un être vivant, qui recommence")],
      "Le cycle de vie d'une plante à fleurs", cycle_plante(), BO + " ; programme du cycle 2 (CE2) ; La main à la pâte, « De quoi a besoin une graine pour germer ? »."),
    L("fecondation", 4, "La fécondation chez les animaux",
      ["Savoir qu'il faut en général un mâle et une femelle de la même espèce", "Définir la fécondation : rencontre d'une cellule reproductrice mâle et d'une cellule reproductrice femelle",
       "Distinguer la fécondation interne et la fécondation externe", "CM2 : expliquer pourquoi la fécondation externe se fait dans l'eau"],
      "<h4>Un mâle et une femelle</h4><p>Pour avoir des petits, il faut en général un <b>mâle</b> et une <b>femelle</b> de la même espèce. La <b>fécondation</b> est la rencontre d'une cellule reproductrice mâle et d'une cellule reproductrice femelle : c'est le début d'un nouvel être vivant.</p>"
      "<h4>Dedans ou dehors</h4><p>Chez les oiseaux et les mammifères (poule, vache, lapin), la fécondation a lieu dans le corps de la femelle : elle est <b>interne</b>. Chez la grenouille et la truite, elle a lieu dans l'eau : elle est <b>externe</b>.</p>",
      F.html(F.LECON_FECONDATION),
      [("mâle", "individu qui produit les cellules reproductrices mâles"), ("femelle", "individu qui produit les cellules reproductrices femelles"),
       ("gamète", "cellule reproductrice"), ("fécondation interne", "fécondation dans le corps de la femelle"),
       ("fécondation externe", "fécondation hors du corps, dans l'eau")],
      "Deux façons de féconder", fecondation(), BO + " ; Lumni, « La reproduction des animaux »."),
    L("naitre", 5, "Naître ou éclore",
      ["Décrire les étapes du développement d'un animal, de la fécondation à la naissance ou à l'éclosion", "Distinguer les animaux ovipares et vivipares",
       "Relier le type de fécondation au mode de reproduction", "Définir une espèce ; savoir que les petits ressemblent à leurs parents sans être identiques"],
      "<h4>Dans un œuf ou dans le ventre</h4><p>Après la fécondation, l'<b>embryon</b> se développe. Chez les <b>ovipares</b> (poule, tortue, grenouille), il grandit dans un <b>œuf</b> pondu, puis le petit sort : c'est l'<b>éclosion</b>. Chez les <b>vivipares</b> (vache, brebis, lapine), il grandit dans le <b>ventre de sa mère</b>, puis le petit <b>naît</b>. Le têtard est une <b>larve</b> qui deviendra grenouille.</p>"
      "<h4>La même espèce</h4><p>Un petit appartient toujours à la même <b>espèce</b> que ses parents. Il leur ressemble, mais il n'est pas identique : chaque individu est unique.</p>",
      F.html(F.LECON_NAITRE),
      [("ovipare", "animal dont le petit se développe dans un œuf pondu"), ("vivipare", "animal dont le petit se développe dans le ventre de sa mère"),
       ("éclosion", "sortie du petit hors de l'œuf"), ("larve", "jeune animal très différent de l'adulte, comme le têtard"),
       ("espèce", "ensemble d'êtres vivants qui peuvent se reproduire entre eux")],
      "Un œuf de poule fécondé, en coupe", oeuf(), BO + " ; FAO, « Incubation naturelle » ; Lumni, « La reproduction des animaux ».",
      document={"type": "texte", "titre": "Le développement de la grenouille",
                "contenu": "Fécondation externe dans l'eau, puis un très grand nombre d'œufs dans la mare ; l'embryon se développe dans l'œuf ; le têtard (larve) éclot ; des pattes lui poussent et sa queue raccourcit ; la jeune grenouille quitte l'eau et grandit jusqu'à l'âge adulte.",
                "source": "La main à la pâte ; Lumni."}),
]


def main(dest):
    json.dump({"lecons": LECONS}, open(os.path.join(dest, "lecons.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
