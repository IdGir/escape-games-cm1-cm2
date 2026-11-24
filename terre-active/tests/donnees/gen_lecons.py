# -*- coding: utf-8 -*-
"""Génère terre-active/assets/data/lecons.json (5 leçons). Lancer : python gen_lecons.py <dossier data>
Le texte CM2 est fait des phrases de fiches.py (reprises mot pour mot par les justifications des grades)."""
import json, os, sys
from schemas import lecon_terre, lecon_plaques, lecon_volcan, lecon_seisme, carte_risques
import fiches as F

BO = "Programme de sciences et technologie, cycle 3 (BO n° 24 du 11 juin 2026, annexe 2) : « La Terre, une planète active », CM2 « L'activité terrestre » (progression de l'enseignant : année A, période 5)"


def L(id, salle, titre, objectifs, cm1, cm2, lexique, schema_titre, svg, sources, document=None):
    l = {"id": id, "salle": salle, "icone": str(salle), "titre": titre, "duree": "4 min", "niveau": "CM1-CM2", "objectifs": objectifs,
         "contenu": {"cm1": cm1, "cm2": cm2}, "lexique": [{"mot": m, "def": d} for m, d in lexique],
         "schema": {"titre": schema_titre, "svg": svg}}
    if document:
        l["document"] = document
    l["sources"] = sources
    return l


LECONS = [
    L("activite", 1, "Une planète active",
      ["Repérer des manifestations de l'activité interne ou externe de la Terre", "Nommer les trois grandes enveloppes de la Terre : croûte, manteau, noyau",
       "CM2 : donner quelques profondeurs (30 km, 2 900 km, 6 400 km)", "Pour aller plus loin (cycle 4) : la chaleur interne"],
      "<h4>Une planète active</h4><p>La surface de la Terre <b>change</b>. Les <b>volcans</b> et les <b>séismes</b> viennent de l'intérieur de la Terre : c'est l'<b>activité interne</b>. Les tempêtes, les inondations et les vagues qui rongent les falaises viennent de l'air et de l'eau : c'est l'<b>activité externe</b>.</p>"
      "<h4>Sous nos pieds</h4><p>Si l'on coupait la Terre en deux, on verrait trois grandes enveloppes : la <b>croûte</b>, très fine, où nous vivons ; le <b>manteau</b>, très épais et très chaud ; le <b>noyau</b>, au centre. Personne n'y est jamais allé : les scientifiques l'étudient grâce aux séismes.</p>",
      F.html(F.LECON_ACTIVE),
      [("activité interne", "phénomènes dont la cause est à l'intérieur de la Terre : volcans, séismes"), ("activité externe", "phénomènes venus de l'air et de l'eau : tempêtes, inondations, érosion"),
       ("croûte", "enveloppe la plus fine de la Terre, sur laquelle nous vivons"), ("manteau", "enveloppe épaisse de roches très chaudes, sous la croûte"),
       ("noyau", "partie centrale de la Terre")],
      "Les enveloppes de la Terre", lecon_terre(), BO + " ; Futura-Sciences, « Structure de la Terre »."),
    L("plaques", 2, "Les plaques",
      ["Savoir que la surface de la Terre est découpée en plaques qui bougent lentement", "Relier volcans et séismes aux frontières des plaques",
       "Comprendre à quoi sert une maquette (modéliser)", "CM2 : expliquer pourquoi les Antilles ont des volcans et des séismes"],
      "<h4>Un puzzle qui bouge</h4><p>La surface de la Terre est découpée en grandes <b>plaques</b>, comme un puzzle. Elles bougent <b>très lentement</b> : on ne le sent pas. La plupart des volcans et des séismes sont près des <b>frontières</b> entre les plaques.</p>"
      "<h4>Modéliser</h4><p>Ce mouvement est trop lent pour être vu. On fabrique une <b>maquette</b> : deux plaques de polystyrène posées sur une pâte molle, que l'on pousse doucement. La pâte se plisse, comme une montagne.</p>",
      F.html(F.LECON_PLAQUES),
      [("plaque", "grand morceau de la surface de la Terre, qui bouge lentement"), ("frontière de plaques", "zone où deux plaques se touchent, s'écartent ou se rapprochent"),
       ("maquette", "modèle qui aide à comprendre un phénomène"), ("modéliser", "représenter un phénomène par un modèle plus simple"),
       ("faille", "cassure dans les roches")],
      "Deux plaques qui se rapprochent", lecon_plaques(), BO + " ; SDES, Chiffres clés des risques naturels (2023)."),
    L("volcans", 3, "Les volcans",
      ["Nommer les parties d'un volcan : chambre magmatique, cheminée, cratère", "Décrire une éruption et ses produits : lave, cendres, gaz",
       "Connaître des volcans français", "CM2 : distinguer éruption effusive et éruption explosive"],
      "<h4>Comment fonctionne un volcan</h4><p>Sous le volcan, une roche fondue très chaude, le <b>magma</b>, s'accumule dans la <b>chambre magmatique</b>. Lors d'une <b>éruption</b>, il monte par la <b>cheminée</b> et sort par le <b>cratère</b>. Le volcan rejette de la <b>lave</b>, des <b>cendres</b> et des <b>gaz</b>.</p>"
      "<h4>Des volcans en France</h4><p>Le <b>Piton de la Fournaise</b>, à La Réunion, entre souvent en éruption. Aux Antilles, la <b>montagne Pelée</b> (Martinique) et la <b>Soufrière</b> (Guadeloupe) sont surveillées. En Auvergne, les volcans de la <b>Chaîne des Puys</b> sont endormis depuis des milliers d'années.</p>",
      F.html(F.LECON_VOLCANS),
      [("magma", "roche fondue très chaude sous le volcan"), ("lave", "magma sorti du volcan, qui coule puis durcit"),
       ("cratère", "ouverture au sommet du volcan"), ("éruption", "sortie de lave, de cendres ou de gaz par le volcan"),
       ("nuée ardente", "nuage brûlant de gaz et de cendres qui dévale la pente d'un volcan")],
      "Un volcan en coupe", lecon_volcan(), BO + " ; Espace des sciences, Sciences Ouest n° 416 ; Futura-Sciences ; IPGP ; ministère de la Culture (2018).",
      document={"type": "texte", "titre": "Repères",
                "contenu": "Montagne Pelée (Martinique) : 8 mai 1902, la ville de Saint-Pierre est détruite par une nuée ardente. Soufrière (Guadeloupe) : 1976, des dizaines de milliers d'habitants évacués. Chaîne des Puys (Auvergne) : 80 volcans endormis depuis au moins 8 000 ans, patrimoine mondial de l'Unesco depuis 2018.",
                "source": "Espace des sciences (2024) ; Futura-Sciences (2022) ; IPGP (2026) ; ministère de la Culture (2018)."}),
    L("seismes", 4, "Les séismes",
      ["Expliquer ce qu'est un séisme : une cassure brusque des roches le long d'une faille", "Nommer le foyer, l'épicentre, les ondes sismiques",
       "Savoir qu'un sismographe enregistre les séismes et que la magnitude mesure leur énergie", "Savoir qu'on ne peut pas prévoir le jour d'un séisme"],
      "<h4>Quand la Terre tremble</h4><p>Poussées par le mouvement des plaques, les roches finissent par <b>casser d'un coup</b> le long d'une <b>faille</b> : c'est un <b>séisme</b>. L'endroit où la roche casse est le <b>foyer</b> ; juste au-dessus, à la surface, c'est l'<b>épicentre</b>. Des <b>ondes</b> partent du foyer et font vibrer le sol.</p>"
      "<h4>Mesurer et surveiller</h4><p>Le <b>sismographe</b> enregistre les vibrations. Les scientifiques savent <b>où</b> les séismes sont probables, par exemple aux Antilles, mais personne ne sait prévoir le <b>jour</b> d'un séisme.</p>",
      F.html(F.LECON_SEISMES),
      [("séisme", "secousse du sol causée par une cassure brusque des roches"), ("foyer", "endroit sous terre où la roche casse"),
       ("épicentre", "point de la surface situé juste au-dessus du foyer"), ("sismographe", "appareil qui enregistre les vibrations du sol"),
       ("magnitude", "nombre qui mesure l'énergie libérée par un séisme")],
      "Un séisme en coupe", lecon_seisme(), BO + " ; SDES, Chiffres clés des risques naturels (2023) ; préfecture du Puy-de-Dôme, « Les bons réflexes en cas de séisme »."),
    L("prevention", 5, "Prévenir et se protéger",
      ["Définir la notion de risque naturel", "Identifier des mesures de prévention et de protection",
       "Connaître les bons réflexes avant, pendant et après un séisme", "CM2 : lire une carte des risques"],
      "<h4>Le risque naturel</h4><p>Il y a un <b>risque</b> quand un séisme ou une éruption peut toucher des personnes, des maisons ou des routes. Pour s'y préparer, on <b>surveille</b> (observatoires), on <b>informe</b> (cartes des risques), on <b>construit solidement</b> et on <b>s'entraîne</b> : c'est la <b>prévention</b>.</p>"
      "<h4>Les bons réflexes</h4><p>Pendant les secousses, je reste où je suis : je m'abrite sous une table solide, je protège ma tête avec mes bras, je m'éloigne des fenêtres. Après, je sors calmement par l'escalier, sans ascenseur, et j'écoute les adultes. Les risques existent, mais on sait s'y préparer.</p>",
      F.html(F.LECON_PREVENTION),
      [("risque naturel", "possibilité qu'un phénomène naturel touche des personnes ou des biens"), ("prévention", "ce que l'on fait avant pour limiter les dégâts"),
       ("protection", "ce qui met les personnes à l'abri pendant et après le phénomène"), ("observatoire", "lieu où des scientifiques surveillent volcans et séismes"),
       ("évacuer", "quitter un lieu dangereux sur ordre des autorités")],
      "Une carte des risques (village inventé)", carte_risques(), BO + " ; préfectures du Puy-de-Dôme et de la Nièvre (consignes séisme) ; ministère de l'Europe et des Affaires étrangères (2026) ; Géorisques."),
]


def main(dest):
    json.dump({"lecons": LECONS}, open(os.path.join(dest, "lecons.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
