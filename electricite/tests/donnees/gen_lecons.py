# -*- coding: utf-8 -*-
"""Génère electricite/assets/data/lecons.json (5 leçons). Lancer : python gen_lecons.py <dossier data>
Le texte CM2 est fait des phrases de fiches.py (reprises mot pour mot par les justifications des grades)."""
import json, os, sys
from schemas import lecon_circuit, lecon_conducteurs, lecon_symboles, lecon_securite, lecon_reseau
import fiches as F

BO = "Programme de sciences et technologie, cycle 3 (arrêté du 5 juin 2026, BO n° 24 du 11 juin 2026), CM2, « Signaux » : électricité"
LAMAP = "Fondation La main à la pâte, « L'électricité au cycle 3 »"
RTE = "RTE, Bilan électrique 2025 (repris par Connaissance des énergies, « 95,2 % d'électricité bas carbone en 2025 ») ; Connaissance des énergies, fiche « RTE »"


def L(id, salle, titre, objectifs, cm1, cm2, lexique, schema_titre, svg, sources, document=None):
    l = {"id": id, "salle": salle, "icone": str(salle), "titre": titre, "duree": "4 min", "niveau": "CM1-CM2", "objectifs": objectifs,
         "contenu": {"cm1": cm1, "cm2": cm2}, "lexique": [{"mot": m, "def": d} for m, d in lexique],
         "schema": {"titre": schema_titre, "svg": svg}}
    if document:
        l["document"] = document
    l["sources"] = sources
    return l


LECONS = [
    L("circuit", 1, "Le circuit électrique",
      ["Nommer les éléments d'un circuit : pile, lampe, interrupteur, fils", "Savoir qu'une lampe ne brille que dans une boucle complète",
       "Distinguer circuit ouvert et circuit fermé", "CM2 : expliquer qu'une lampe dévissée éteint les autres lampes de la même boucle"],
      "<h4>Les éléments</h4><p>Un circuit électrique comprend une <b>pile</b>, une <b>lampe</b> (ou un moteur) et des <b>fils</b>. La pile a deux bornes : la borne + et la borne −.</p>"
      "<h4>Une boucle complète</h4><p>La lampe ne s'allume que si le courant peut faire une <b>boucle</b> sans interruption, d'une borne de la pile à l'autre. Le circuit est alors <b>fermé</b>. Si un fil est débranché, le circuit est <b>ouvert</b> : la lampe s'éteint.</p>"
      "<h4>L'interrupteur</h4><p>L'<b>interrupteur</b> ouvre ou ferme le circuit sans débrancher les fils.</p>",
      F.html(F.LECON_CIRCUIT),
      [("circuit", "chemin fermé que suit le courant électrique"), ("borne", "point où l'on branche un fil sur une pile ou une lampe"),
       ("récepteur", "appareil qui utilise le courant : lampe, moteur"), ("générateur", "appareil qui fournit le courant : la pile"),
       ("interrupteur", "dispositif qui ouvre ou ferme le circuit")],
      "Un circuit fermé", lecon_circuit(), BO + " ; " + LAMAP + " ; Lumni, « Le circuit électrique »."),
    L("conducteurs", 2, "Conducteurs et isolants",
      ["Trier des matériaux conducteurs et isolants", "Savoir que les métaux conduisent le courant",
       "Utiliser un circuit testeur", "CM2 : expliquer la composition d'un fil électrique"],
      "<h4>Conducteur ou isolant ?</h4><p>Un <b>conducteur</b> laisse passer le courant : les <b>métaux</b> (fer, cuivre, aluminium). Un <b>isolant</b> ne le laisse pas passer : le <b>plastique</b>, le <b>bois</b>, le <b>verre</b>, le <b>papier</b>, le <b>caoutchouc</b>.</p>"
      "<h4>Le circuit testeur</h4><p>On place l'objet dans la boucle d'un circuit. Si la lampe s'allume, l'objet est conducteur.</p>"
      "<h4>Le fil électrique</h4><p>Le cœur du fil est en <b>cuivre</b> (conducteur) ; la gaine est en <b>plastique</b> (isolant).</p>",
      F.html(F.LECON_COND),
      [("conducteur", "matériau qui laisse passer le courant électrique"), ("isolant", "matériau qui ne laisse pas passer le courant"),
       ("gaine", "enveloppe isolante autour d'un fil"), ("graphite", "matière noire de la mine du crayon, qui conduit le courant")],
      "Le circuit testeur", lecon_conducteurs(), BO + " ; " + LAMAP + " ; Lumni, « Conducteurs et isolants »."),
    L("schema", 3, "Le schéma électrique",
      ["Reconnaître les symboles de la pile, de la lampe, du moteur et de l'interrupteur", "Lire un schéma normalisé",
       "Passer du dessin au schéma", "CM2 : suivre le trajet du courant de la borne + à la borne −"],
      "<h4>Les symboles</h4><p>Sur un <b>schéma</b>, on remplace les objets par des <b>symboles</b>, les mêmes pour tout le monde. La pile : un grand trait et un petit trait. La lampe : un cercle avec une croix. Le moteur : un cercle avec un M. L'interrupteur ouvert : un trait levé.</p>"
      "<h4>Les fils</h4><p>Les fils sont des traits droits. Le circuit forme souvent un rectangle.</p>",
      F.html(F.LECON_SCHEMA),
      [("schéma", "dessin simplifié qui utilise des symboles"), ("symbole", "signe qui représente un objet"),
       ("normalisé", "fait selon une règle commune à tous")],
      "Les symboles normalisés", lecon_symboles(), BO + " ; " + LAMAP + " ; Eduscol, ressources d'accompagnement du programme de sciences et technologie au cycle 3."),
    L("securite", 4, "La sécurité électrique",
      ["Savoir que la pile de la classe est sans danger et que le secteur est dangereux", "Connaître les règles de sécurité à la maison et dehors",
       "Savoir quoi faire en cas d'accident", "Citer des gestes pour économiser l'électricité"],
      "<h4>Pile ou secteur ?</h4><p>La <b>pile</b> de la classe (4,5 volts) est sans danger. Le courant des <b>prises</b> (230 volts) est <b>dangereux</b> : il peut brûler et tuer. On ne fait <b>jamais</b> d'expérience avec une prise.</p>"
      "<h4>Les règles</h4><p>Ne jamais mettre un objet dans une prise. Ne jamais toucher un appareil avec les mains mouillées. Tirer sur la fiche, pas sur le fil. Ne jamais jouer près des lignes électriques ni grimper sur un pylône.</p>"
      "<h4>En cas d'accident</h4><p>Ne pas toucher la personne : couper le courant, puis appeler le <b>18</b> ou le <b>112</b>.</p>"
      "<h4>Économiser</h4><p>Éteindre la lumière en quittant une pièce, ne pas laisser les appareils en veille.</p>",
      F.html(F.LECON_SECU),
      [("secteur", "courant électrique des prises de la maison"), ("électrisation", "passage du courant dans le corps"),
       ("disjoncteur", "appareil qui coupe le courant de la maison"), ("veille", "appareil éteint mais encore branché, qui consomme un peu")],
      "Pile ou secteur ?", lecon_securite(), BO + " (règles de sécurité électrique) ; " + LAMAP + " ; Enedis, conseils de prévention des accidents électriques."),
    L("production", 5, "Produire et transporter l'électricité",
      ["Nommer des centrales : nucléaire, hydraulique, éolienne, solaire, thermique", "Distinguer sources renouvelables et non renouvelables",
       "Décrire le trajet de l'électricité, de la centrale à la prise", "CM2 : lire les chiffres de la production française en 2025"],
      "<h4>Les centrales</h4><p>L'électricité des prises est produite dans des <b>centrales</b>. Dans une centrale <b>nucléaire</b> ou <b>thermique</b>, de la vapeur fait tourner une turbine. Dans une centrale <b>hydraulique</b>, c'est l'eau d'un barrage. Dans une <b>éolienne</b>, c'est le vent. Les panneaux <b>solaires</b> transforment la lumière en électricité.</p>"
      "<h4>Renouvelable ou non ?</h4><p>L'eau, le vent et le Soleil se renouvellent. L'uranium, le gaz et le charbon ne se renouvellent pas. En France, la plus grande partie de l'électricité vient des centrales nucléaires.</p>"
      "<h4>Le voyage de l'électricité</h4><p>Centrale, transformateur, lignes à très haute tension sur des pylônes, poste, puis réseau de la ville jusqu'au compteur et aux prises.</p>",
      F.html(F.LECON_PROD),
      [("centrale", "usine qui produit de l'électricité"), ("turbine", "roue à pales que l'on fait tourner"),
       ("alternateur", "machine qui produit le courant quand on la fait tourner"), ("renouvelable", "qui ne s'épuise pas : vent, eau, Soleil"),
       ("pylône", "grand support métallique des lignes électriques")],
      "De la centrale à la prise", lecon_reseau(), BO + " ; " + RTE + " ; Lumni, « Comment produit-on de l'électricité ? ».",
      document={"type": "texte", "titre": "La production d'électricité en France en 2025",
                "contenu": "Production totale : 547,5 milliards de kilowattheures (TWh). Nucléaire : 373 TWh (68 %). Hydraulique : 62,4 TWh (11 %). Éolien : 49,6 TWh (9 %). Solaire : 32,9 TWh (6 %). Gaz, charbon et fioul : environ 18,7 TWh (3 % pour le gaz). Plus de 95 % de cette électricité est produite sans rejeter beaucoup de gaz carbonique.",
                "source": "RTE, Bilan électrique 2025, d'après Connaissance des énergies."}),
]


def main(dest):
    json.dump({"lecons": LECONS}, open(os.path.join(dest, "lecons.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
