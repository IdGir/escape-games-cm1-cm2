# -*- coding: utf-8 -*-
"""Génère vivant-ecosystemes/assets/data/enigmes.json (L'Expédition biodiversité). Lancer : python gen_enigmes.py <dossier data>
Programme : BO n° 24 du 11 juin 2026, annexe 2. Vocabulaire du programme (milieu de vie, êtres vivants, réseau alimentaire) ;
pas de groupe « invertébrés » (on ne classe pas sur une absence) ; ton non alarmiste. Réserve et personnages inventés."""
import json, os, sys
from schemas import oiseau, cle, mare, reseau, strates

BO = "Programme de sciences et technologie, cycle 3 (BO n° 24 du 11 juin 2026, annexe 2) : « Unité et diversité du vivant » et « Les écosystèmes » (progression de l'enseignant : année A, période 4)"
MNHN = "Muséum national d'histoire naturelle et INPN (inpn.mnhn.fr)"
LAMAP = "Fondation La main à la pâte, « Classification du vivant » et « Écosystèmes »"
TEMPS = "Académie de Martinique, « Marche des temps géologiques », dossier pédagogique (2024)"
CRISE = "Espace des sciences, Sciences Ouest n° 413, « Disparition des dinosaures : que s'est-il passé ? »"
EEE = "Centre de ressources Espèces exotiques envahissantes (OFB, UICN France), fiche « Écrevisse de Louisiane »"
FRELON = "MNHN, Villemant et al. (2011), « Bilan de l'invasion de Vespa velutina en France »"
OFB = "Office français de la biodiversité (OFB)"


def E(id, titre, type_, consigne, source, correction, indices, cm1=None, cm2=None, commun=None, lecon="", cm2_seul=False):
    e = {"id": id, "titre": titre, "type": type_}
    if cm2_seul:
        e["niveaux"] = ["CM2"]
    e["consigne"] = consigne
    e["source"] = source
    e["correction"] = correction
    e["indices"] = indices
    if cm1 is not None: e["cm1"] = cm1
    if cm2 is not None: e["cm2"] = cm2
    if commun is not None: e["commun"] = commun
    e["lecon"] = lecon
    return e


def tri(cols, cartes):
    return {"colonnes": [{"id": i, "titre": t} for i, t in cols], "cartes": [{"txt": t, "col": c} for t, c in cartes]}


def qcm(qs):
    return {"questions": [{"q": q, "options": o, "bonne": b, "explication": x} for q, o, b, x in qs]}


def vf(affs):
    return {"affirmations": [{"txt": t, "vrai": v, "explication": x} for t, v, x in affs]}


def ordre(items):
    out = []
    for i, t in enumerate(items):
        d = {"txt": t[0] if isinstance(t, tuple) else t, "rang": i + 1}
        if isinstance(t, tuple):
            d["sous"] = t[1]
        out.append(d)
    return {"items": out}


def assoc(paires):
    return {"paires": [{"g": g, "d": d} for g, d in paires]}


def code(champs):
    return {"champs": [{"libelle": l, "valeur": v, "longueur": len(v)} for l, v in champs]}


def intrus(cartes):
    return {"cartes": [{"txt": t, "intrus": i} for t, i in cartes]}


def plan(titre, col, cases, etiq):
    return {"titre": titre, "colonnes": col, "cases": [{"libelle": f"Repère {i + 1}", "reponse": r} for i, r in enumerate(cases)], "etiquettes": etiq}


def tableau(titre, entetes, lignes):
    h = "".join(f"<th>{x}</th>" for x in entetes)
    c = "".join("<tr>" + "".join(f"<td>{x}</td>" for x in l) + "</tr>" for l in lignes)
    return f"<div class='doc-titre'><i>{titre}</i></div><table class='tableau-releves'><tr>{h}</tr>{c}</table>"


CARNET5 = tableau("Le carnet d'Élio : les espèces de l'étang, numérotées",
                  ["N°", "Espèce", "Elle mange…"],
                  [["1", "algues", "(fabriquent leur matière avec la lumière)"], ["2", "héron cendré", "des perches et des grenouilles"],
                   ["3", "perche", "des têtards et des larves de libellule"], ["4", "têtard", "des algues"],
                   ["5", "larve de libellule", "des têtards"], ["6", "grenouille verte", "des insectes, dont les libellules adultes"]])

S = []
# =================================================================== SALLE 1 — la tente-laboratoire (Lina)
S.append({"num": 1, "titre": "La tente-laboratoire — Observer le vivant, l'espèce", "enigmes": [
    E("1-1", "La mésange du carnet", "plan",
      {"cm1": "Lina a dessiné une mésange dans son carnet de terrain, mais l'eau a effacé les étiquettes. Place chaque mot sur son repère : clique sur une étiquette, puis sur la case du repère." + oiseau(3),
       "cm2": "Lina a dessiné une mésange dans son carnet de terrain. Place chaque attribut sur son repère. Attention : il y a des étiquettes en trop." + oiseau(5)},
      BO + " ; " + MNHN,
      "Sur le dessin, le repère 1 montre le bec, le repère 2 l'œil et le repère 3 les plumes de l'aile. En CM2, le repère 4 montre la patte et le repère 5 la queue ; les poils et la coquille ne sont pas des attributs de la mésange.",
      {"cm1": ["Le bec est tout au bout de la tête.", "L'œil est le rond noir.", "L'aile est couverte de plumes."],
       "cm2": ["Un oiseau n'a pas de poils.", "Les pattes touchent la branche.", "La queue est à l'opposé du bec."]},
      cm1=plan("Le carnet de Lina", 3, ["le bec", "l'œil", "les plumes"], ["le bec", "l'œil", "les plumes"]),
      cm2=plan("Le carnet de Lina", 2, ["le bec", "l'œil", "les plumes", "la patte", "la queue"],
               ["le bec", "l'œil", "les plumes", "la patte", "la queue", "les poils", "la coquille"]),
      lecon="espece"),
    E("1-2", "Les notes mouillées", "vraifaux",
      {"cm1": "Les notes de Lina sont tombées dans la mare et certaines phrases ont été mal recopiées. Pour chaque phrase, choisis vrai ou faux.",
       "cm2": "Lina relit les notes recopiées par un stagiaire. Pour chaque phrase, choisis vrai ou faux."},
      BO + " ; " + MNHN + " ; " + LAMAP,
      "Une espèce réunit des êtres vivants qui se ressemblent et peuvent avoir ensemble des petits, qui auront à leur tour des petits. Un caniche et un berger allemand sont de la même espèce, le chien. En CM2 : le mulet ne peut pas avoir de petits, donc l'âne et le cheval sont deux espèces ; un attribut se voit sur l'être vivant ; ce qu'il mange n'en est pas un.",
      {"cm1": ["Une espèce : des êtres vivants qui ont des petits ensemble.", "Le caniche et le berger allemand sont des chiens.", "Une poule n'a pas de poils."],
       "cm2": ["Le mulet n'a pas de petits.", "Un attribut se voit.", "Le nom scientifique a deux mots."]},
      cm1=vf([("Les êtres vivants d'une même espèce se ressemblent et peuvent avoir des petits ensemble.", True, "C'est la définition de l'espèce."),
              ("Un caniche et un berger allemand sont deux espèces différentes.", False, "Ce sont deux races de la même espèce : le chien."),
              ("Les plumes sont un attribut des oiseaux.", True, "On les voit sur l'animal.")]),
      cm2=vf([("Un âne et une jument peuvent avoir un mulet, mais le mulet ne peut pas avoir de petits.", True, "L'âne et le cheval sont donc deux espèces."),
              ("Ce qu'un animal mange est un de ses attributs.", False, "Un attribut se voit sur l'être vivant."),
              ("Chaque espèce a un nom scientifique en deux mots, le même dans tous les pays.", True, "Le héron cendré : Ardea cinerea."),
              ("Faire l'inventaire d'un lieu, c'est noter toutes les espèces qu'on y trouve.", True, "On mesure ainsi sa biodiversité."),
              ("Deux chiens très différents ne peuvent pas avoir de petits ensemble.", False, "Ils sont de la même espèce.")]),
      lecon="espece"),
    E("1-3", "Les boîtes d'observation", "association",
      {"cm1": "Dans les boîtes d'observation, chaque animal attend sa fiche. Relie chaque animal à un attribut que Lina a vu sur lui.",
       "cm2": "Dans les boîtes d'observation, chaque être vivant attend sa fiche. Relie chacun à ce que Lina a observé sur lui."},
      BO + " ; " + MNHN,
      "L'escargot a une coquille enroulée, la libellule six pattes et quatre ailes, le renard des poils. En CM2 : le héron a des plumes et un long bec, la grenouille une peau nue et quatre membres, l'araignée huit pattes, et la fougère des feuilles mais pas de fleurs.",
      {"cm1": ["Qui porte sa maison sur le dos ?", "Les insectes ont six pattes.", "Le renard a un pelage."],
       "cm2": ["La grenouille n'a ni poils ni plumes.", "Compte les pattes de l'araignée.", "La fougère n'a pas de fleurs."]},
      cm1=assoc([("l'escargot", "une coquille enroulée"), ("la libellule", "six pattes et quatre ailes"), ("le renard", "des poils")]),
      cm2=assoc([("le héron cendré", "des plumes et un long bec"), ("la grenouille verte", "une peau nue et quatre membres"), ("l'araignée", "huit pattes"),
                 ("la libellule", "six pattes et quatre ailes"), ("la fougère", "des feuilles, mais pas de fleurs")]),
      lecon="espece"),
    E("1-4", "Même espèce ?", "tri",
      "Lina reçoit des questions des visiteurs : « Ces deux-là sont-ils de la même espèce ? » Range chaque paire dans la bonne colonne.",
      BO + " ; " + MNHN,
      "Le caniche et le berger allemand, le chat roux et le chat noir, le coq et la poule sont de la même espèce : leurs petits peuvent avoir des petits. L'âne et le cheval donnent des mulets qui n'ont pas de petits ; le chat et le tigre, la mésange et le moineau ne se reproduisent pas ensemble : ce sont des espèces différentes.",
      {"cm2": ["Le coq et la poule : un mâle et une femelle de la même espèce.", "Pense au mulet.", "Se ressembler un peu ne suffit pas."]},
      commun=tri([("meme", "Même espèce"), ("diff", "Deux espèces différentes")],
                 [("un caniche et un berger allemand", "meme"), ("un chat roux et un chat noir", "meme"), ("un coq et une poule", "meme"),
                  ("un âne et un cheval", "diff"), ("un chat et un tigre", "diff"), ("une mésange et un moineau", "diff")]),
      lecon="espece", cm2_seul=True),
]})

# =================================================================== SALLE 2 — la cabane du garde (Hugo)
S.append({"num": 2, "titre": "La cabane du garde — Classer le vivant", "enigmes": [
    E("2-1", "Les caisses du garde", "tri",
      {"cm1": "Hugo range les fiches des animaux de la réserve dans ses caisses. Place chaque animal dans la caisse qui correspond à ce qu'il possède.",
       "cm2": "Hugo range les fiches dans des groupes emboîtés. Place chaque animal dans le plus petit groupe qui lui convient."},
      BO + " ; " + LAMAP + " ; " + MNHN,
      "Le renard et le hérisson ont des poils ; le héron et le canard ont des plumes ; la libellule et la fourmi ont six pattes. En CM2 : la chauve-souris a des poils (elle vole, mais ce n'est pas un oiseau) ; la grenouille et le lézard ont quatre membres sans poils ni plumes ; la truite a un squelette interne et des nageoires.",
      {"cm1": ["Regarde ce que l'animal possède.", "Le hérisson a des piquants, qui sont des poils durs.", "Les insectes ont six pattes."],
       "cm2": ["La chauve-souris a des poils.", "La grenouille a quatre membres.", "La truite a des nageoires, pas de membres."]},
      cm1=tri([("poils", "A des poils"), ("plumes", "A des plumes"), ("six", "A six pattes")],
              [("le renard", "poils"), ("le hérisson", "poils"), ("le héron", "plumes"), ("le canard", "plumes"), ("la libellule", "six"), ("la fourmi", "six")]),
      cm2=tri([("poils", "Poils"), ("plumes", "Plumes"), ("membres", "Quatre membres, ni poils ni plumes"), ("squel", "Squelette interne, sans membres")],
              [("le renard", "poils"), ("la chauve-souris", "poils"), ("le héron", "plumes"), ("la mésange", "plumes"),
               ("la grenouille", "membres"), ("le lézard", "membres"), ("la truite", "squel"), ("la perche", "squel")]),
      lecon="classer"),
    E("2-2", "Les règles du classement", "qcm",
      {"cm1": "Hugo veut vérifier que vous savez classer. Réponds à ses questions.",
       "cm2": "Hugo interroge les naturalistes sur les règles du classement. Choisis la bonne réponse."},
      BO + " ; " + LAMAP,
      "On classe les êtres vivants selon les attributs qu'ils possèdent en commun, pas selon l'endroit où ils vivent ni ce qu'ils mangent. La chauve-souris a des poils : elle est rangée avec le renard. En CM2 : on ne fait jamais de groupe avec une absence ; les groupes sont emboîtés ; le dauphin est rangé avec les animaux qui allaitent leurs petits.",
      {"cm1": ["On regarde ce que l'animal possède.", "La chauve-souris a des poils.", "Où il vit ne compte pas."],
       "cm2": ["« Sans pattes » décrit une absence.", "Des boîtes dans des boîtes.", "Le dauphin allaite ses petits."]},
      cm1=qcm([("Pour classer les animaux, on regarde…", ["où ils vivent", "ce qu'ils possèdent", "leur couleur préférée", "ce qu'ils mangent"], 1, "On compare leurs attributs."),
               ("Avec qui range-t-on la chauve-souris ?", ["avec les oiseaux", "avec le renard, car elle a des poils", "avec les insectes", "avec les poissons"], 1, "Elle vole, mais elle a des poils."),
               ("La grenouille vit dans l'eau et sur terre. Pour la classer, cela compte-t-il ?", ["oui, toujours", "non, on regarde ses attributs", "seulement l'hiver", "seulement pour les têtards"], 1, "Le lieu de vie ne sert pas à classer.")]),
      cm2=qcm([("Pourquoi « les animaux sans pattes » n'est-il pas un groupe de classification ?", ["parce qu'il est trop grand", "parce qu'on ne classe pas avec ce qui manque", "parce que les serpents ont des pattes", "parce qu'il n'existe pas d'animaux sans pattes"], 1, "On classe avec ce que l'on possède."),
               ("Que veut dire « groupes emboîtés » ?", ["des groupes rangés les uns dans les autres", "des groupes de même taille", "des groupes tirés au sort", "des groupes rangés par couleur"], 0, "Comme des boîtes dans des boîtes."),
               ("Le dauphin vit dans la mer. Avec qui le range-t-on ?", ["avec les poissons", "avec les animaux qui allaitent leurs petits", "avec les algues", "avec les crabes"], 1, "Il respire avec des poumons et allaite ses petits."),
               ("Le renard est plus proche parent…", ["du hérisson", "du loup", "de la mésange", "de la truite"], 1, "Ils partagent plus d'attributs.")]),
      lecon="classer"),
    E("2-3", "La clé des petites bêtes", "plan",
      {"cm1": "Sous les feuilles mortes, Hugo a trouvé des petites bêtes. Suis sa clé de détermination et place chaque nom dans sa case." + cle(3),
       "cm2": "Sous les feuilles mortes, Hugo a trouvé des petites bêtes. Suis la clé de détermination et place chaque nom dans sa case. Attention : il y a des étiquettes en trop." + cle(5)},
      BO + " ; " + LAMAP + " ; " + MNHN,
      "La clé se lit de haut en bas : l'escargot n'a pas de pattes (case 1) ; la fourmi, un insecte, a six pattes (case 2) ; l'araignée en a huit (case 3). En CM2 : le cloporte a quatorze pattes (case 4) et le mille-pattes plus de trente (case 5). La libellule et le scarabée sont des insectes : ils iraient dans la case des six pattes, déjà occupée par la fourmi.",
      {"cm1": ["L'escargot n'a pas de pattes.", "Les insectes ont six pattes.", "L'araignée a huit pattes."],
       "cm2": ["Commence par la question du haut.", "Le cloporte : quatorze pattes.", "Les insectes ont six pattes : une seule case."]},
      cm1=plan("La clé d'Hugo", 3, ["l'escargot", "la fourmi", "l'araignée"], ["l'escargot", "la fourmi", "l'araignée"]),
      cm2=plan("La clé d'Hugo", 2, ["l'escargot", "la fourmi", "l'araignée", "le cloporte", "le mille-pattes"],
               ["l'escargot", "la fourmi", "l'araignée", "le cloporte", "le mille-pattes", "la libellule", "le scarabée"]),
      lecon="classer"),
    E("2-4", "La caisse des poils", "intrus",
      "Dans la caisse « A des poils », un apprenti a glissé une fiche qui n'a rien à faire là. Trouve l'intrus.",
      BO + " ; " + LAMAP,
      "Le renard, le hérisson, la chauve-souris et le ragondin ont des poils. Le lézard a des écailles, sans poils : il n'a rien à faire dans cette caisse, même s'il a quatre membres comme eux.",
      {"cm2": ["Les piquants du hérisson sont des poils.", "La chauve-souris a un pelage.", "Écailles ou poils ?"]},
      commun=intrus([("le renard", False), ("le hérisson", False), ("la chauve-souris", False), ("le ragondin", False), ("le lézard", True)]),
      lecon="classer", cm2_seul=True),
]})

# =================================================================== SALLE 3 — l'ancienne carrière (Amara)
S.append({"num": 3, "titre": "L'ancienne carrière — La biodiversité passée", "enigmes": [
    E("3-1", "La frise de la carrière", "ordre",
      {"cm1": "Amara veut afficher l'histoire du vivant sur une grande frise. Remets les étapes dans l'ordre, de la plus ancienne à la plus récente.",
       "cm2": "Amara prépare la frise du temps géologique. Remets les étapes dans l'ordre, de la plus ancienne à la plus récente."},
      BO + " ; " + TEMPS,
      "D'abord la formation de la Terre, puis les premières traces de vie, puis les trilobites dans la mer, puis la disparition des dinosaures, et enfin l'apparition de notre espèce. En CM2 : il y a environ 4,6 milliards d'années, 3,8 milliards d'années, 540 millions d'années, 66 millions d'années et 300 000 ans.",
      {"cm1": ["La Terre est arrivée en premier.", "Les dinosaures ont disparu bien avant les humains.", "Les humains sont les plus récents."],
       "cm2": ["Un milliard, c'est mille millions.", "540 millions est plus ancien que 66 millions.", "300 000 ans, c'est très récent."]},
      cm1=ordre(["La Terre se forme.", "Les premiers êtres vivants apparaissent dans la mer.", "Les dinosaures disparaissent.", "Les premiers humains de notre espèce apparaissent."]),
      cm2=ordre([("La Terre se forme.", "il y a environ 4,6 milliards d'années"), ("Premières traces de vie.", "il y a environ 3,8 milliards d'années"),
                 ("Les trilobites vivent dans la mer.", "il y a 540 millions d'années"), ("Les dinosaures disparaissent.", "il y a environ 66 millions d'années"),
                 ("Homo sapiens apparaît en Afrique.", "il y a environ 300 000 ans")]),
      lecon="fossiles"),
    E("3-2", "Le tiroir des fossiles", "association",
      {"cm1": "Dans le tiroir d'Amara, chaque fossile a perdu son étiquette. Relie chaque fossile à ce qu'il était.",
       "cm2": "Dans le tiroir d'Amara, chaque fossile a perdu son étiquette. Relie chaque fossile à ce qu'il nous apprend."},
      BO + " ; " + TEMPS + " ; " + MNHN,
      "Une ammonite était un animal marin à coquille enroulée, un trilobite un animal marin à carapace, une empreinte de fougère la trace d'une plante. En CM2 : une dent de requin trouvée dans un champ montre qu'une mer recouvrait autrefois ce lieu ; un os de dinosaure, que de grands reptiles vivaient sur la terre ferme ; les ammonites ont disparu il y a 66 millions d'années, les trilobites il y a 252 millions d'années.",
      {"cm1": ["L'ammonite a une coquille en spirale.", "Une empreinte de feuille vient d'une plante.", "Le trilobite a une carapace."],
       "cm2": ["Une dent de requin : il y avait la mer.", "Les trilobites sont plus anciens.", "Un os vient d'un animal à squelette."]},
      cm1=assoc([("l'ammonite", "un animal marin à coquille enroulée"), ("le trilobite", "un animal marin à carapace"), ("l'empreinte de fougère", "la trace d'une plante")]),
      cm2=assoc([("l'ammonite", "disparue il y a 66 millions d'années"), ("le trilobite", "disparu il y a 252 millions d'années"),
                 ("la dent de requin trouvée dans un champ", "une mer recouvrait ce lieu"), ("l'os de dinosaure", "de grands reptiles vivaient sur la terre ferme"),
                 ("l'empreinte de fougère", "une plante qui vivait dans un lieu humide")]),
      lecon="fossiles"),
    E("3-3", "Le panneau de la crise", "vraifaux",
      {"cm1": "Amara écrit le panneau sur la disparition des dinosaures. Pour chaque phrase, choisis vrai ou faux.",
       "cm2": "Amara relit le panneau sur l'extinction de la fin du Crétacé. Pour chaque phrase, choisis vrai ou faux."},
      BO + " ; " + CRISE + " ; " + TEMPS,
      "Les dinosaures ont disparu il y a très longtemps, bien avant l'apparition des humains : aucun humain n'en a vu vivant. Un fossile est un reste ou une trace d'être vivant conservé dans une roche. En CM2 : il y a environ 66 millions d'années, une extinction massive a fait disparaître un très grand nombre d'espèces ; les causes étudiées sont une météorite géante au Mexique et d'énormes éruptions en Inde ; les oiseaux descendent de petits dinosaures à plumes ; ensuite, les mammifères se sont diversifiés.",
      {"cm1": ["Les humains sont arrivés très tard.", "Un fossile est dans une roche.", "Les oiseaux sont-ils des cousins des dinosaures ?"],
       "cm2": ["66 millions contre 300 000.", "Deux causes sont étudiées.", "Après la crise, de nouvelles espèces apparaissent."]},
      cm1=vf([("Des hommes préhistoriques ont chassé des dinosaures.", False, "Les dinosaures avaient disparu depuis des millions d'années."),
              ("Un fossile est une trace d'un être vivant ancien, conservée dans une roche.", True, "Une coquille, un os, une empreinte."),
              ("Les oiseaux descendent de petits dinosaures à plumes.", True, "Ce sont les seuls dinosaures qui n'ont pas disparu.")]),
      cm2=vf([("Il y a environ 66 millions d'années, un très grand nombre d'espèces a disparu en peu de temps.", True, "C'est une extinction massive."),
              ("Les scientifiques savent avec certitude qu'une seule cause explique cette crise.", False, "Ils étudient une météorite et des éruptions volcaniques."),
              ("Après la crise, de nouvelles espèces de mammifères sont apparues rapidement.", True, "La biodiversité s'est reconstruite."),
              ("Homo sapiens est apparu il y a environ 300 000 ans.", True, "Bien après les dinosaures."),
              ("Les ammonites vivent encore aujourd'hui dans la mer.", False, "Elles ont disparu avec les dinosaures.")]),
      lecon="fossiles"),
    E("3-4", "Le cadenas des millions", "code",
      "La vitrine des fossiles est fermée par un cadenas à deux nombres. Calcule-les avec le panneau d'Amara." + strates("La carrière d'Amara") +
      tableau("Le panneau d'Amara", ["Fossile", "Disparu il y a…"], [["trilobite", "252 millions d'années"], ["ammonite", "66 millions d'années"]]),
      BO + " ; " + TEMPS,
      "Les trilobites ont disparu 252 − 66 = 186 millions d'années avant les ammonites. Les ammonites ont disparu il y a environ 66 millions d'années : c'est le second nombre.",
      {"cm2": ["Fais une soustraction.", "252 − 66 = ?", "Le second nombre est écrit dans le panneau."]},
      commun=code([("Millions d'années entre la disparition des trilobites et celle des ammonites", "186"),
                   ("Millions d'années depuis la disparition des ammonites", "66")]),
      lecon="fossiles", cm2_seul=True),
]})

# =================================================================== SALLE 4 — la mare et le pré (Rose)
S.append({"num": 4, "titre": "La mare et le pré fleuri — L'écosystème", "enigmes": [
    E("4-1", "La coupe de la mare", "plan",
      {"cm1": "Rose a dessiné la mare de la réserve pour les visiteurs. Place chaque mot sur son repère." + mare(3),
       "cm2": "Rose a dessiné la mare de la réserve. Place chaque mot sur son repère. Attention : il y a des étiquettes en trop." + mare(5)},
      BO + " ; " + LAMAP + " ; " + OFB,
      "Le repère 1 montre la lumière du soleil, le repère 2 l'eau de la mare, le repère 3 un roseau. En CM2, le repère 4 montre une grenouille et le repère 5 la vase du fond. La lumière, l'eau et la vase font partie du milieu de vie ; le roseau et la grenouille sont des êtres vivants.",
      {"cm1": ["Le soleil est en haut.", "L'eau est bleue.", "Le roseau pousse sur la berge."],
       "cm2": ["La grenouille est au bord de l'eau.", "La vase est au fond.", "Il n'y a pas de neige sur ce dessin."]},
      cm1=plan("La mare de Rose", 3, ["la lumière", "l'eau", "un roseau"], ["la lumière", "l'eau", "un roseau"]),
      cm2=plan("La mare de Rose", 2, ["la lumière", "l'eau", "un roseau", "une grenouille", "la vase"],
               ["la lumière", "l'eau", "un roseau", "une grenouille", "la vase", "la neige", "un sapin"]),
      lecon="ecosysteme"),
    E("4-2", "Les relevés de Rose", "tri",
      {"cm1": "Rose a noté tout ce qu'elle a observé autour de la mare. Range chaque observation : est-ce un élément du milieu de vie ou un être vivant ?",
       "cm2": "Rose a noté tout ce qu'elle a observé autour de la mare. Range chaque observation : caractéristique du milieu de vie ou être vivant ?"},
      BO + " ; " + LAMAP,
      "La lumière, la température de l'eau et la pluie décrivent le milieu de vie ; le nénuphar, la libellule et le champignon sont des êtres vivants. En CM2 : l'humidité de l'air et la profondeur de l'eau décrivent aussi le milieu ; la mousse et la paramécie, minuscule, sont des êtres vivants.",
      {"cm1": ["Un être vivant naît, grandit et meurt.", "La pluie n'est pas vivante.", "Le champignon est vivant."],
       "cm2": ["Ce qui se mesure avec un instrument décrit le milieu.", "La paramécie se voit au microscope.", "La mousse est une plante."]},
      cm1=tri([("milieu", "Milieu de vie"), ("vivant", "Être vivant")],
              [("la lumière", "milieu"), ("la température de l'eau", "milieu"), ("la pluie", "milieu"),
               ("le nénuphar", "vivant"), ("la libellule", "vivant"), ("le champignon", "vivant")]),
      cm2=tri([("milieu", "Caractéristique du milieu de vie"), ("vivant", "Être vivant")],
              [("la lumière", "milieu"), ("la température de l'eau", "milieu"), ("l'humidité de l'air", "milieu"), ("la profondeur de l'eau", "milieu"),
               ("le nénuphar", "vivant"), ("la mousse", "vivant"), ("la paramécie", "vivant"), ("le héron cendré", "vivant")]),
      lecon="ecosysteme"),
    E("4-3", "Les questions de l'apicultrice", "qcm",
      {"cm1": "Rose s'occupe des ruches du pré, à côté de la mare. Réponds à ses questions.",
       "cm2": "Rose interroge les naturalistes sur les relations entre les êtres vivants. Choisis la bonne réponse."},
      BO + " ; " + LAMAP + " ; " + MNHN,
      "Le héron qui attrape une grenouille est un prédateur et la grenouille sa proie : c'est la prédation. L'abeille boit le nectar et transporte le pollen d'une fleur à l'autre : chacun gagne, c'est une coopération. En CM2 : un écosystème réunit un milieu de vie, des êtres vivants et leurs relations ; la grenouille a besoin de l'eau de la mare pour pondre ; les nénuphars ont besoin d'une eau calme et ensoleillée.",
      {"cm1": ["Qui mange qui ?", "L'abeille et la fleur gagnent toutes les deux.", "Les œufs de grenouille sont dans l'eau."],
       "cm2": ["Trois choses forment un écosystème.", "Prédateur et proie.", "Le nénuphar flotte au soleil."]},
      cm1=qcm([("Le héron attrape une grenouille. Comment appelle-t-on cette relation ?", ["une coopération", "une prédation", "une pollinisation", "une amitié"], 1, "Le héron est le prédateur."),
               ("L'abeille boit le nectar et transporte le pollen de la fleur. Qui y gagne ?", ["seulement l'abeille", "seulement la fleur", "les deux", "personne"], 2, "C'est une coopération."),
               ("Pourquoi la grenouille vit-elle près de la mare ?", ["pour pondre ses œufs dans l'eau", "pour manger les nénuphars", "pour se cacher du soleil", "pour boire du nectar"], 0, "Ses œufs se développent dans l'eau.")]),
      cm2=qcm([("Qu'est-ce qu'un écosystème ?", ["seulement les animaux d'un lieu", "un milieu de vie, les êtres vivants qui l'habitent et leurs relations", "seulement les plantes d'un lieu", "une réserve naturelle"], 1, "Les trois ensemble."),
               ("Dans la prédation du héron sur la grenouille, la grenouille est…", ["le prédateur", "la proie", "la coopératrice", "le milieu"], 1, "Elle est mangée."),
               ("Pourquoi trouve-t-on des nénuphars au milieu de la mare et pas sous les arbres ?", ["ils ont besoin d'une eau calme et ensoleillée", "ils fuient les grenouilles", "ils aiment l'ombre", "le vent les y pousse"], 0, "Leur présence dépend du milieu."),
               ("Quelle relation est une coopération ?", ["le héron et la perche", "l'abeille et la fleur", "le renard et le mulot", "l'épervier et la mésange"], 1, "Chacun y gagne.")]),
      lecon="ecosysteme"),
    E("4-4", "Qui vit où ?", "association",
      "Rose explique aux visiteurs pourquoi chaque être vivant se trouve à cet endroit de la réserve. Relie chaque être vivant à ce dont il a besoin dans son milieu.",
      BO + " ; " + LAMAP + " ; " + MNHN,
      "Le nénuphar a besoin d'une eau calme et ensoleillée ; la mousse d'un endroit humide et ombragé ; la grenouille d'eau pour pondre ; l'abeille de fleurs pour son nectar ; le héron d'une eau peu profonde où il pêche à pied.",
      {"cm2": ["La mousse aime l'ombre.", "Le héron marche dans l'eau.", "L'abeille butine."]},
      commun=assoc([("le nénuphar", "une eau calme et ensoleillée"), ("la mousse", "un endroit humide et ombragé"), ("la grenouille", "de l'eau pour pondre ses œufs"),
                    ("l'abeille", "des fleurs pour boire leur nectar"), ("le héron cendré", "une eau peu profonde pour pêcher")]),
      lecon="ecosysteme", cm2_seul=True),
]})

# =================================================================== SALLE 5 — le ponton de l'étang (Élio)
S.append({"num": 5, "titre": "Le ponton de l'étang — Le réseau alimentaire", "enigmes": [
    E("5-1", "Qui mange qui ?", "ordre",
      {"cm1": "Élio, le pêcheur de l'étang, montre une chaîne « est mangé par ». Remets les êtres vivants dans l'ordre, en commençant par celui qui est mangé en premier.",
       "cm2": "Élio montre une chaîne « est mangé par » de l'étang. Remets les êtres vivants dans l'ordre, du premier mangé au dernier mangeur."},
      BO + " ; " + LAMAP + " ; " + MNHN,
      "Les algues sont mangées par les têtards, les têtards par les larves de libellule, puis par les perches. En CM2 : la chaîne continue jusqu'au héron cendré, qui mange les perches. Chaque chaîne commence par une plante ou une algue.",
      {"cm1": ["On commence par une algue.", "Le têtard mange des algues.", "La perche est un poisson qui mange les petits animaux."],
       "cm2": ["Au début, une algue.", "La larve de libellule chasse les têtards.", "Le héron pêche les poissons."]},
      cm1=ordre(["les algues", "le têtard", "la larve de libellule", "la perche"]),
      cm2=ordre(["les algues", "le têtard", "la larve de libellule", "la perche", "le héron cendré"]),
      lecon="reseau"),
    E("5-2", "Les flèches d'Élio", "vraifaux",
      {"cm1": "Élio dessine des flèches dans son carnet. Pour chaque phrase, choisis vrai ou faux.",
       "cm2": "Élio vérifie les règles du réseau alimentaire. Pour chaque phrase, choisis vrai ou faux."},
      BO + " ; " + LAMAP,
      "La flèche va de celui qui est mangé vers celui qui le mange : algues → têtard veut dire « les algues sont mangées par le têtard ». Les animaux mangent d'autres êtres vivants pour grandir. En CM2 : les chaînes se croisent et forment un réseau ; si une espèce change beaucoup en nombre, tout le réseau est touché ; au départ de chaque chaîne il y a une plante ou une algue.",
      {"cm1": ["La flèche veut dire « est mangé par ».", "Le têtard mange les algues.", "Un animal mange pour grandir."],
       "cm2": ["Les chaînes se croisent.", "Une espèce en moins touche les autres.", "Au départ : une plante ou une algue."]},
      cm1=vf([("Dans « algues → têtard », la flèche veut dire « les algues sont mangées par le têtard ».", True, "La flèche va vers celui qui mange."),
              ("La flèche va toujours du mangeur vers ce qu'il mange.", False, "C'est l'inverse."),
              ("Les animaux mangent d'autres êtres vivants pour grandir.", True, "Plantes ou animaux.")]),
      cm2=vf([("Les chaînes « est mangé par » d'un étang se croisent et forment un réseau.", True, "La perche mange des têtards et des larves."),
              ("Si les perches disparaissent, seul le héron est touché.", False, "Les larves de libellule deviennent aussi trop nombreuses."),
              ("Au départ de chaque chaîne, on trouve une plante ou une algue.", True, "Elles fabriquent leur matière avec la lumière."),
              ("Le héron peut manger des perches et des grenouilles.", True, "Deux flèches arrivent au héron."),
              ("Dans « perche → héron », c'est la perche qui mange le héron.", False, "La perche est mangée par le héron.")]),
      lecon="reseau"),
    E("5-3", "L'intruse venue d'Amérique", "trous",
      {"cm1": "Une affiche de la réserve a été déchirée. Complète-la avec les bonnes étiquettes.",
       "cm2": "Une affiche de la réserve a été déchirée. Complète-la. Attention : il y a des étiquettes en trop."},
      BO + " ; " + EEE + " ; " + FRELON + " ; " + OFB,
      "L'écrevisse de Louisiane vient d'Amérique ; relâchée dans la nature, elle détruit les plantes de l'eau et mange les petits animaux de la mare. Il ne faut jamais relâcher un animal exotique dans la nature. En CM2 : elle a été introduite en France en 1976 ; le frelon asiatique, observé en France depuis 2004, chasse surtout les abeilles ; on peut aider la mare en ne relâchant aucun animal et en gardant des haies.",
      {"cm1": ["Elle vient d'un autre continent.", "Elle mange les plantes de l'eau.", "Il ne faut jamais relâcher un animal exotique."],
       "cm2": ["1976 : son arrivée en France.", "Le frelon chasse près des ruches.", "Les haies abritent les êtres vivants."]},
      cm1={"texte": "<p>L'écrevisse de Louisiane vient d'[[Amérique]]. Dans la mare, elle détruit les [[plantes]] de l'eau et mange les petits animaux. Il ne faut jamais [[relâcher]] un animal exotique dans la nature.</p>",
           "etiquettes": ["Amérique", "plantes", "relâcher"]},
      cm2={"texte": "<p>L'écrevisse de Louisiane, venue d'[[Amérique]], a été introduite en France en [[1976]]. Elle détruit les [[plantes]] de l'eau et mange les petits animaux de la mare : tout le [[réseau]] alimentaire est touché. Le frelon asiatique, observé en France depuis [[2004]], chasse surtout les [[abeilles]]. Pour protéger la mare, on ne relâche jamais un animal exotique et on garde les [[haies]].</p>",
           "etiquettes": ["Amérique", "1976", "plantes", "réseau", "2004", "abeilles", "haies", "Afrique", "1789", "renards"]},
      lecon="reseau"),
    E("5-4", "Le maillon manquant", "code",
      "Pour finir la carte du vivant, il manque trois maillons du réseau de l'étang. Trouve le numéro de chaque espèce manquante dans le carnet d'Élio." +
      reseau(3, "Les trois maillons manquants", ("têtard", "perche", "héron")) + CARNET5,
      BO + " ; " + LAMAP + " ; " + MNHN,
      "Le maillon 1 mange les algues et est mangé par la larve de libellule : c'est le têtard (n° 4). Le maillon 2 mange les têtards et les larves de libellule : c'est la perche (n° 3). Le maillon 3 mange les perches et les grenouilles : c'est le héron cendré (n° 2). Le code est 4, 3, 2.",
      {"cm2": ["Suis les flèches qui arrivent sur chaque case.", "Qui mange les algues ?", "Qui mange les perches et les grenouilles ?"]},
      commun=code([("Maillon 1", "4"), ("Maillon 2", "3"), ("Maillon 3", "2")]),
      lecon="reseau", cm2_seul=True),
]})


def main(dest):
    meta = {"jeu": "L'Expédition biodiversité", "version": 1,
            "differenciation": "CM1 : 3 énigmes par salle (15 au total). CM2 : 4 énigmes par salle (20 au total). Le champ \"niveaux\" limite une énigme à un niveau ; les blocs \"cm1\" / \"cm2\" / \"commun\" portent les données.",
            "types": sorted({e["type"] for s in S for e in s["enigmes"]}),
            "sources": " ; ".join([BO, MNHN, LAMAP, TEMPS, CRISE, EEE, FRELON, OFB]) + ". Détail : README.md, section Sources.",
            "media": "Chaque énigme accepte un bloc \"media\" : {\"base\":\"e3-1\",\"legende\":\"…\",\"source\":\"…\"}. Les schémas (mésange, clé, frise, mare, réseau) sont dessinés en SVG par script : ne jamais les remplacer par des images générées par IA. Fossiles réels : photos Wikimedia Commons."}
    json.dump({"metadata": meta, "salles": S}, open(os.path.join(dest, "enigmes.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
