# -*- coding: utf-8 -*-
"""Génère naissances-animaux/assets/data/lecons.json (5 leçons). Lancer : python gen_lecons.py <dossier data>
Le texte CM2 est fait des phrases de fiches.py (reprises mot pour mot par les justifications des grades)."""
import json, os, sys
from schemas import lecon_fecondation, lecon_milieux, lecon_tableau, lecon_poussin, lecon_gestation, lecon_classe
import fiches as F

BO = "Programme de sciences et technologie, cycle 3 (BO n° 24 du 11 juin 2026), CM1, « Les êtres vivants dans leur environnement » : reproduction, croissance et développement (progression de l'enseignant : année B, période 3)"
LAMAP = "Fondation La main à la pâte, « Biologie animale : fonctions de reproduction »"
MNHN = "Muséum national d'histoire naturelle et INPN (fiches espèces)"


def L(id, salle, titre, objectifs, cm1, cm2, lexique, schema_titre, svg, sources, document=None):
    l = {"id": id, "salle": salle, "icone": str(salle), "titre": titre, "duree": "4 min", "niveau": "CM1-CM2", "objectifs": objectifs,
         "contenu": {"cm1": cm1, "cm2": cm2}, "lexique": [{"mot": m, "def": d} for m, d in lexique],
         "schema": {"titre": schema_titre, "svg": svg}}
    if document:
        l["document"] = document
    l["sources"] = sources
    return l


LECONS = [
    L("fecondation", 1, "La fécondation",
      ["Savoir qu'un petit commence par la rencontre d'une cellule du mâle et d'une cellule de la femelle", "Définir la fécondation et l'œuf",
       "CM2 : nommer les gamètes (spermatozoïde, ovule) et les organes qui les produisent", "CM2 : savoir que la cellule-œuf devient un embryon"],
      "<h4>Deux cellules</h4><p>Chez la plupart des animaux, un petit naît de la rencontre de <b>deux cellules</b> : une cellule du <b>mâle</b>, minuscule, qui nage, et une cellule de la <b>femelle</b>, grosse et ronde. On ne les voit qu'au microscope.</p>"
      "<h4>La fécondation</h4><p>Quand ces deux cellules se rencontrent et s'unissent, c'est la <b>fécondation</b>. Elle donne un <b>œuf</b> : la toute première cellule du petit. Cet œuf va grandir.</p>"
      "<h4>Sans fécondation, pas de petit</h4><p>Il faut un mâle et une femelle. Un œuf de poule acheté au magasin n'a pas été fécondé : il ne donnera jamais de poussin.</p>",
      F.html(F.LECON_FECOND),
      [("cellule", "plus petit élément vivant ; un animal en a des milliards"), ("fécondation", "rencontre et union de la cellule du mâle et de celle de la femelle"),
       ("gamète", "cellule reproductrice : spermatozoïde ou ovule"), ("cellule-œuf", "première cellule du futur animal, née de la fécondation"),
       ("embryon", "petit en train de se former, avant la naissance")],
      "La fécondation", lecon_fecondation(), BO + " ; " + LAMAP + " ; Lumni, « La reproduction des animaux »."),
    L("externe", 2, "Fécondation externe et interne",
      ["Savoir que la fécondation peut avoir lieu dans l'eau ou dans le corps de la femelle", "Donner des exemples d'animaux à fécondation externe et interne",
       "CM2 : expliquer pourquoi les pontes sont nombreuses en fécondation externe", "CM2 : savoir que vivre dans l'eau ne suffit pas pour avoir une fécondation externe"],
      "<h4>Dans l'eau</h4><p>Chez la <b>grenouille</b> et la <b>truite</b>, la femelle pond ses cellules dans l'eau et le mâle y libère les siennes. Elles se rencontrent dans l'eau : c'est une fécondation <b>externe</b>.</p>"
      "<h4>Dans le corps</h4><p>Chez les <b>oiseaux</b>, les <b>reptiles</b> et les <b>mammifères</b>, le mâle et la femelle s'accouplent : les cellules se rencontrent dans le corps de la femelle. C'est une fécondation <b>interne</b>.</p>"
      "<h4>Attention</h4><p>La tortue marine et le dauphin vivent dans la mer, mais leur fécondation est interne.</p>",
      F.html(F.LECON_EXT),
      [("externe", "à l'extérieur, hors du corps"), ("interne", "à l'intérieur du corps"), ("ponte", "action de pondre des œufs"),
       ("accouplement", "union du mâle et de la femelle avant une fécondation interne")],
      "Où se rencontrent les gamètes ?", lecon_milieux(), BO + " ; " + LAMAP + " ; " + MNHN + "."),
    L("ovipares", 3, "Ovipares et vivipares",
      ["Distinguer un animal ovipare d'un animal vivipare", "Donner des exemples d'ovipares et de vivipares",
       "Mettre en relation le type de fécondation et le mode de reproduction", "Connaître quelques exceptions : ornithorynque, vipère aspic, requins"],
      "<h4>Pondre</h4><p>Un animal <b>ovipare</b> pond des œufs. Le petit grandit dans l'œuf, hors du corps de sa mère : la poule, le crocodile, la grenouille, le papillon.</p>"
      "<h4>Naître vivant</h4><p>Un animal <b>vivipare</b> ne pond pas. Le petit grandit dans le ventre de sa mère et naît vivant : le chat, la vache, le lapin. Presque tous les mammifères sont vivipares.</p>"
      "<h4>Des exceptions</h4><p>L'<b>ornithorynque</b> est un mammifère qui pond des œufs. Certains <b>requins</b> pondent, d'autres donnent naissance à des petits vivants. Ce sont des exceptions.</p>",
      F.html(F.LECON_OVI),
      [("ovipare", "animal qui pond des œufs"), ("vivipare", "animal dont le petit se développe dans le ventre de la mère et naît vivant"),
       ("ovovivipare", "animal dont les œufs éclosent dans le ventre de la mère"), ("placenta", "organe qui relie le petit à sa mère avant la naissance"),
       ("exception", "cas qui ne suit pas la règle générale")],
      "Fécondation et mode de reproduction", lecon_tableau(), BO + " ; " + LAMAP + " ; " + MNHN + " ; Futura Sciences, « Pourquoi certains requins pondent-ils des œufs ? »."),
    L("developpement", 4, "Le développement avant la naissance",
      ["Décrire les grandes étapes du développement du poussin dans l'œuf", "Nommer les parties d'un œuf de poule",
       "Savoir ce qu'est la gestation", "CM2 : comparer des durées de gestation"],
      "<h4>Dans l'œuf</h4><p>Dans l'œuf fécondé, l'<b>embryon</b> grandit. Le <b>jaune</b> le nourrit, le <b>blanc</b> le protège, la <b>coquille</b> l'abrite. La poule couve ses œufs pendant <b>21 jours</b> : sa chaleur permet au poussin de se former. Le cœur bat très tôt, puis on reconnaît la forme du poussin, puis viennent les plumes. Le poussin perce enfin la coquille.</p>"
      "<h4>Dans le ventre</h4><p>Chez les mammifères, le petit grandit dans le ventre de sa mère : c'est la <b>gestation</b>. Elle dure environ 1 mois chez la lapine, 9 mois chez la vache, presque 2 ans chez l'éléphante.</p>",
      F.html(F.LECON_DEV),
      [("couvaison", "temps où l'oiseau tient ses œufs au chaud"), ("éclosion", "sortie du petit hors de l'œuf"), ("diamant", "petite pointe au bout du bec du poussin, qui perce la coquille"),
       ("gestation", "temps où le petit se développe dans le ventre de sa mère"), ("utérus", "organe de la femelle où grandit le petit d'un mammifère")],
      "21 jours de couvaison", lecon_poussin(), BO + " ; Écolothèque de Montpellier Méditerranée Métropole, « Naissance d'un poussin » ; Techno-Science, glossaire « Gestation ».",
      document={"type": "texte", "titre": "Durées moyennes avant la naissance",
                "contenu": "Poule (couvaison) : 21 jours. Lapine : environ 31 jours. Chatte : 63 à 65 jours. Vache : environ 280 jours (9 mois). Jument : environ 336 jours (11 mois). Éléphante : 600 à 660 jours (20 à 22 mois).",
                "source": "Techno-Science, glossaire « Gestation » ; Écolothèque de Montpellier, « Naissance d'un poussin »."}),
    L("classification", 5, "Classer les animaux du zoo",
      ["Pour un animal, dire son type de fécondation et son mode de reproduction", "Remplir un tableau à deux entrées",
       "Savoir qu'une fécondation externe donne un animal ovipare", "CM2 : comprendre qu'une exception ne change pas la règle"],
      "<h4>Deux questions</h4><p>Pour décrire comment naît un animal, on se pose deux questions : <b>où</b> se rencontrent les cellules (dans l'eau ou dans le corps de la femelle) ? <b>comment</b> naît le petit (il sort d'un œuf ou il naît vivant) ?</p>"
      "<h4>Trois cas</h4><p>Dans l'eau, puis ponte : la grenouille, la truite. Dans le corps, puis ponte : la poule, la tortue. Dans le corps, petit vivant : la girafe, le dauphin.</p>",
      F.html(F.LECON_CLASSE),
      [("tableau à deux entrées", "tableau qui croise deux questions, l'une en ligne, l'autre en colonne"), ("classer", "ranger selon des points communs"),
       ("mammifère", "animal dont la femelle allaite ses petits")],
      "Le carnet de naissance du zoo", lecon_classe(), BO + " ; " + LAMAP + " ; " + MNHN + "."),
]


def main(dest):
    json.dump({"lecons": LECONS}, open(os.path.join(dest, "lecons.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
