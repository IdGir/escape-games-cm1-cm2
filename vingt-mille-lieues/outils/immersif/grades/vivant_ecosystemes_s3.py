"""Salle 3 « L'ancienne carrière » : grades mousse, lieutenant, second (fiche : La biodiversité passée)."""
import os, sys
from aide import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "vivant-ecosystemes", "tests", "donnees"))
from fiches import *
from schemas import strates, frise

FICHE = "« La biodiversité passée »"


def donnees(svg, bloc=None):
    d = {}
    d["e3-1"] = {
        "mousse": ordre(
            "Remets ces étapes dans l'ordre, de la plus ancienne à la plus récente.",
            ["Les dinosaures vivent sur la Terre.", "Les dinosaures disparaissent.", "Les premiers humains apparaissent."],
            ["Ouvre la fiche " + FICHE + ".", "Il faut que les dinosaures vivent avant de disparaître.", "Les humains sont arrivés bien après."]),
        "lieutenant": ordre(
            "Amara prépare la frise. Remets les six étapes dans l'ordre, de la plus ancienne à la plus récente, puis choisis la phrase de la fiche qui compare les deux façons de compter le temps.",
            [("La Terre se forme.", "environ 4,6 milliards d'années"), ("Premières traces de vie.", "environ 3,8 milliards d'années"),
             ("Les trilobites vivent dans la mer.", "540 millions d'années"), ("Les trilobites disparaissent.", "252 millions d'années"),
             ("Les dinosaures et les ammonites disparaissent.", "environ 66 millions d'années"), ("Homo sapiens apparaît.", "environ 300 000 ans")],
            ["Un milliard = mille millions.", "Les trilobites disparaissent avant les dinosaures.", "Pour la justification : cherche « siècles »."],
            J("Quelle phrase de la fiche compare le temps géologique et l'histoire des humains ?", P_ECHELLE, [P_TERRE, P_CHANGE, P_SAPIENS], pos=2)),
        "second": tri(
            "Amara a trouvé ces fossiles dans les couches de la carrière. Range chacun : sous la couche de la crise (avant), ou au-dessus (après). Puis choisis la phrase de la fiche qui résume ce que montrent les fossiles." + strates(),
            [("avant", "Avant la crise d'il y a 66 millions d'années"), ("apres", "Après la crise")],
            [("une ammonite", "avant"), ("un trilobite", "avant"), ("un os de dinosaure à long cou", "avant"),
             ("un os de mammifère", "apres"), ("une coquille d'escargot actuel", "apres")],
            ["Les ammonites disparaissent pendant la crise.", "Les mammifères se diversifient ensuite.", "Pour la justification : cherche « au cours du temps »."],
            J("Quelle phrase de la fiche résume ce que montrent les fossiles ?", P_CHANGE, [P_FOSSILE, P_ROCHE, P_CRISE], pos=1)),
    }
    d["e3-2"] = {
        "mousse": assoc(
            "Relie chaque fossile à ce qu'il était.",
            [("l'ammonite", "un animal à coquille enroulée"), ("l'os de dinosaure", "un grand reptile disparu"), ("l'empreinte de feuille", "une plante")],
            ["Ouvre la fiche " + FICHE + ".", "L'ammonite a une spirale.", "Une empreinte de feuille vient d'une plante."]),
        "lieutenant": assoc(
            "Relie chaque fossile à ce qu'il nous apprend, puis choisis la phrase de la fiche qui définit un fossile.",
            [("une coquille dans un calcaire", "un animal marin vivait là, au fond de l'eau"), ("une empreinte de fougère", "une plante, et non un animal"),
             ("une dent de requin dans un champ", "une mer recouvrait autrefois ce lieu"), ("un trilobite", "un animal marin à carapace, très ancien"),
             ("une trace de pas dans la roche", "un animal qui marchait sur un sol mou")],
            ["Une trace de pas est aussi un fossile.", "Les fossiles se forment surtout au fond de l'eau.", "Pour la justification : cherche « reste ou une trace »."],
            J("Quelle phrase de la fiche définit un fossile ?", P_FOSSILE, [P_ROCHE, P_CHANGE, P_TRILO], pos=0)),
        "second": qcm(
            "Amara interroge les naturalistes sur la crise de la fin du Crétacé. Choisis la bonne réponse, puis la phrase de la fiche sur les causes.",
            [("Qu'appelle-t-on une extinction massive ?", ["la disparition d'une seule espèce", "la disparition d'un très grand nombre d'espèces en peu de temps", "la naissance de nouvelles espèces", "un tremblement de terre"], 1, "C'est une crise de la biodiversité."),
             ("Quelles causes les scientifiques étudient-ils ?", ["une météorite géante et d'énormes éruptions volcaniques", "les chasseurs préhistoriques", "un hiver très froid d'un an", "une maladie des plantes"], 0, "Le débat n'est pas tranché."),
             ("Que se passe-t-il après la crise ?", ["plus rien ne vit", "de nouvelles espèces apparaissent rapidement", "les dinosaures reviennent", "les trilobites réapparaissent"], 1, "Les mammifères se diversifient."),
             ("Quels dinosaures n'ont pas disparu ?", ["les grands herbivores", "les oiseaux", "les ammonites", "aucun"], 1, "Ils descendent de petits dinosaures à plumes.")],
            ["Une extinction massive touche beaucoup d'espèces.", "Deux causes sont étudiées.", "Pour la justification : cherche « météorite »."],
            J("Quelle phrase de la fiche présente les causes étudiées ?", P_CAUSES, [P_CRISE, P_REMPLACE, P_DINOS], pos=2)),
    }
    d["e3-3"] = {
        "mousse": vf(
            "Amara a écrit trois phrases. Pour chacune, choisis vrai ou faux.",
            [("Un fossile se trouve dans une roche.", True, "C'est une trace d'un être vivant ancien."),
             ("Des humains ont vu des dinosaures vivants.", False, "Les dinosaures avaient disparu depuis très longtemps."),
             ("Les dinosaures ont disparu.", True, "Sauf les oiseaux, qui en descendent.")],
            ["Ouvre la fiche " + FICHE + ".", "Les fossiles sont dans la pierre.", "Les humains sont arrivés bien plus tard."]),
        "lieutenant": vf(
            "Amara relit le panneau de la crise. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche qui dit ce qui s'est passé après.",
            [("Après la crise, les mammifères se sont diversifiés.", True, "De nouvelles espèces sont apparues."),
             ("Les ammonites ont disparu en même temps que les dinosaures.", True, "Il y a environ 66 millions d'années."),
             ("La biodiversité ne change jamais.", False, "Des espèces apparaissent, d'autres disparaissent."),
             ("La plupart des fossiles se forment au fond de l'eau.", True, "Recouverts de sable ou de boue."),
             ("Les trilobites ont disparu pendant la crise de la fin du Crétacé.", False, "Bien avant : il y a 252 millions d'années.")],
            ["252 millions, c'est avant 66 millions.", "Les fossiles naissent sous l'eau.", "Pour la justification : cherche « rapidement »."],
            J("Quelle phrase de la fiche dit ce qui s'est passé après la crise ?", P_REMPLACE, [P_CRISE, P_CHANGE, P_OISEAUX], pos=3)),
        "second": vf(
            "Amara prépare une conférence. Pour chaque phrase, choisis vrai ou faux, puis la phrase de la fiche sur les oiseaux.",
            [("La mésange de la réserve est une descendante des dinosaures.", True, "Les oiseaux descendent de petits dinosaures à plumes."),
             ("Les dinosaures ont vécu moins d'un million d'années.", False, "Plus de 150 millions d'années."),
             ("Les premières traces de vie sont plus anciennes que les trilobites.", True, "3,8 milliards contre 540 millions d'années."),
             ("Homo sapiens est apparu en Europe.", False, "En Afrique."),
             ("Le temps géologique se compte en millions d'années.", True, "Et même en milliards.")],
            ["Les oiseaux ont des plumes, comme certains petits dinosaures.", "Homo sapiens : en Afrique.", "Pour la justification : cherche « oiseaux »."],
            J("Quelle phrase de la fiche parle des oiseaux ?", P_OISEAUX, [P_DINOS, P_REMPLACE, P_CHANGE], pos=1)),
    }
    d["e3-4"] = {
        "lieutenant": code(
            "La vitrine d'Amara a un cadenas à deux nombres. Calcule-les avec la frise, puis choisis la phrase de la fiche sur l'âge de la Terre." + frise(),
            [("Millions d'années entre la formation de la Terre et les premières traces de vie", "800", 3, True),
             ("Millions d'années entre la disparition des trilobites et celle des ammonites", "186", 3, True)],
            ["4,6 milliards = 4 600 millions ; 3,8 milliards = 3 800 millions.", "252 − 66 = ?", "Pour la justification : cherche « 4,6 milliards »."],
            J("Quelle phrase de la fiche donne l'âge de la Terre ?", P_TERRE, [P_ECHELLE, P_TRILO, P_SAPIENS], pos=0)),
        "second": code(
            "Le dernier cadenas d'Amara demande deux nombres. Calcule-les avec la fiche, puis choisis la phrase qui donne les dates des trilobites.",
            [("Pendant combien de millions d'années les trilobites ont-ils vécu au moins (de 540 à 252) ?", "288", 3, True),
             ("Combien de milliers d'années depuis l'apparition d'Homo sapiens ?", "300", 3, True)],
            ["540 − 252 = ?", "300 000 ans = 300 milliers d'années.", "Pour la justification : cherche « carapace »."],
            J("Quelle phrase de la fiche donne les dates des trilobites ?", P_TRILO, [P_DINOS, P_TERRE, P_SAPIENS], pos=2)),
    }
    return d
