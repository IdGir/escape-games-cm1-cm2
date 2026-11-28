# -*- coding: utf-8 -*-
"""Génère README.md et GUIDE-PEDAGOGIQUE.md de napoleon-republique/ depuis assets/data (solutions et compétences toujours à jour).
Lancer depuis napoleon-republique/ : python tests/donnees/gen_docs.py"""
import json, re

E = json.load(open("assets/data/enigmes.json", encoding="utf-8"))
D = json.load(open("assets/data/dialogues.json", encoding="utf-8"))
COMP = {1: "Napoléon Bonaparte, du général à l'empereur : raconter comment un jeune général (Toulon, Italie, Égypte) prend le pouvoir par le coup d'État du 18 brumaire (1799) et dirige le Consulat",
        2: "Napoléon Bonaparte, du général à l'empereur : la naissance de l'Empire (1804), le sacre à Notre-Dame, la lecture du tableau de David et les symboles impériaux",
        3: "Napoléon Bonaparte, du général à l'empereur : les conquêtes (Austerlitz, Iéna, Wagram), la campagne de Russie, Waterloo (1815) et l'exil à Sainte-Hélène ; le coût humain des guerres",
        4: "Napoléon Bonaparte, du général à l'empereur : les monuments de l'Empire et les institutions qui durent (Code civil, préfets, Banque de France, lycées, Légion d'honneur) ; un bilan nuancé (autoritarisme, rétablissement de l'esclavage en 1802)",
        5: "Lieux, symboles et rites de la République (Marianne, drapeau, devise, Marseillaise, 14 juillet, mairie, école, vote, cérémonies) ; lois protectrices des droits et des libertés (renvoi aux jeux « Déclaration » et « Constitution »)"}
txt = lambda h: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()
pers = D["personnages"]
NUANCE = ("**Bilan nuancé.** Le jeu ne fait ni l'éloge ni la caricature de Napoléon : il montre les réformes qui durent (Code civil, préfets, lycées…), "
          "mais aussi les guerres et leurs centaines de milliers de morts, la censure et l'arrestation des opposants, et le rétablissement de l'esclavage dans les colonies en 1802 "
          "(lien avec le jeu n°12 « Les Archives du port »). Aucune scène de combat ; personnages inventés ; les personnes réelles (Napoléon, Joséphine, le pape) ne parlent jamais.")

r = ["# Le Testament de l'Empereur — escape game d'histoire (cycle 3, jeu n°16)", "",
     "Histoire, programme 2026 (arrêté du 22 avril 2026, BO n° 22 du 28 mai 2026 ; niveau exact à confirmer, cf. `A-VERIFIER.md`) ; progression de l'enseignant : thème 4, année B, période 4 :",
     "*Le temps de la Révolution et l'Empire. Napoléon Bonaparte, du général à l'empereur : naissance de l'empire, conquêtes, monuments de l'empire. Lieux, symboles et rites de la République. Lois protectrices des droits et des libertés.*",
     "Ce jeu fait suite au « Secret de la Déclaration » (Révolution). Les lois protectrices des droits et des libertés sont traitées dans « Le Secret de la Déclaration » et « Le Sceau de la République » : la salle 5 y renvoie.", "",
     "**Jouer** : version immersive `../immersifs/napoleon-republique/` (5 grades : Jeune visiteur ≈ CE2, Guide du musée ≈ CM1, Enquêteur d'histoire ≈ CM2, Archiviste ≈ 6ᵉ, Conservateur ≈ 5ᵉ).",
     "Ce dossier contient les **données sources** (format des jeux classiques) d'où la variante immersive est générée ; la version classique (pages `index.html`, `prof.html`) n'est pas écrite.", "",
     "## Points de vigilance", "", NUANCE, "",
     "## Fil narratif", "",
     "Dans les réserves du musée de l'Armée, aux Invalides, Hugo, conservateur, ouvre un vieux coffre de voyage : il contient une copie scellée du testament de l'Empereur et cinq objets. Chaque objet ouvre un souvenir, du jeune général Bonaparte à la République d'aujourd'hui ; les élèves rassemblent cinq mots qui brisent le sceau :",
     "> " + D["metadata"]["phrase_bilan"], "",
     "| Salle | Lieu | Personnage (inventé) | Mot |", "|---|---|---|---|"]
for s in D["salles"]:
    p = s["dialogue_intro"]["perso"]
    r.append(f"| {s['num']} | {s['lieu']} | {pers[p]['nom']}, {pers[p]['role'][0].lower() + pers[p]['role'][1:]} | {s['motCle']} |")
r += ["", "## 🎯 Compétences du programme (vue d'ensemble)", "", "| Salle | Compétence du programme |", "|---|---|"]
r += [f"| {n} | {c} |" for n, c in COMP.items()]
r += ["", "CM1 : 3 énigmes par salle (15) ; CM2 : 4 énigmes par salle (20). Repères en CM1 (ordre des événements, années) ; dates exactes en CM2 (15 août 1769, décembre 1793, 21 juillet 1798, 9 novembre 1799, 15 juillet 1801, 18 mai et 2 décembre 1804, 2 décembre 1805, 14 octobre 1806, 18 juin 1815, 5 mai 1821 ; 18 janvier 1800, 17 février 1800, 1er et 19 mai 1802, 21 mars 1804 ; Constitution de 1958, article 2).", "",
      "## Solutions (générées depuis `assets/data/enigmes.json`)", ""]
for s, d in zip(E["salles"], D["salles"]):
    r.append(f"### {s['titre']} (mot : **{d['motCle']}**)")
    r.append("")
    for e in s["enigmes"]:
        r.append(f"<details><summary><b>{e['id']} {e['titre']}</b> ({e['type']}{', CM2' if e.get('niveaux') == ['CM2'] else ''})</summary>\n\n{txt(e['correction'])}\n\n</details>\n")
    r.append("")
r += ["## Sources", ""] + [f"- {x.strip()}" for x in E["metadata"]["sources"].split(" ; ")] + [
      "", "## Fichiers", "",
      "- `assets/data/` : `enigmes.json`, `lecons.json`, `dialogues.json`, générés par `tests/donnees/gen_enigmes.py`, `gen_lecons.py`, `gen_dialogues.py` ; phrases des fiches dans `tests/donnees/fiches.py` (reprises mot pour mot par les justifications des grades) ; carte, frise, schéma du Sacre, plan de Paris et place de la commune en SVG dans `tests/donnees/schemas.py`.",
      "- Variante immersive : `python vingt-mille-lieues/outils/immersif/migrer-jeu.py napoleon-republique --theme napoleon-republique/tests/donnees/theme-immersif.json --force`, puis `appliquer-narration.py napoleon-republique` et `finir-jeu.py napoleon-republique`.",
      "- Prompts des médias : `python napoleon-republique/tests/donnees/gen_medias.py` après chaque migration (le migrateur réécrit `medias.csv`), puis `prompts-flow.py napoleon-republique`.",
      "- Grades : `vingt-mille-lieues/outils/immersif/grades/napoleon_republique_s1..s5.py` et `napoleon_republique_theme.py` ; narration : `vingt-mille-lieues/outils/immersif/narration/napoleon-republique.json`.", ""]
open("README.md", "w", encoding="utf-8").write("\n".join(r))

g = ["# Guide pédagogique — Le Testament de l'Empereur (jeu n°16)", "", "## Points de vigilance", "", NUANCE, "",
     "## 1. Place dans les programmes", "",
     "Histoire, cycle 3 (arrêté du 22 avril 2026, BO n° 22 du 28 mai 2026 ; niveau à confirmer). La progression de l'enseignant place ce thème en année B, période 4 (thème 4 « Le temps de la Révolution et l'Empire »), après la Révolution. Le jeu couvre :",
     "- **du général au Premier consul** : Toulon, Italie, Égypte, 18 brumaire, Consulat, Concordat ;",
     "- **la naissance de l'Empire** : proclamation et sacre (1804), lecture du tableau de David, symboles impériaux ;",
     "- **les conquêtes et la chute** : Austerlitz, Iéna, Wagram, Russie, Waterloo, Sainte-Hélène, coût humain ;",
     "- **ce qui reste de l'Empire** : monuments (Arc de triomphe, colonne Vendôme, Invalides), institutions (Code civil, préfets, Banque de France, lycées, Légion d'honneur), part d'ombre ;",
     "- **lieux, symboles et rites de la République** : Marianne, drapeau, devise, Marseillaise, 14 juillet, mairie, école, vote, cérémonies ; renvoi aux jeux « Déclaration » et « Constitution » pour les lois protectrices des droits.", "",
     "## 🎯 Compétences du programme, énigme par énigme", "", "| Salle | Énigme | Type | Compétence du programme |", "|---|---|---|---|"]
for s in E["salles"]:
    for e in s["enigmes"]:
        g.append(f"| {s['num']} | {e['id']} {e['titre']} ({'CM2' if e.get('niveaux') == ['CM2'] else 'CM1-CM2'}) | {e['type']} | {COMP[s['num']]} |")
g += ["", "## 2. Prérequis", "",
      "- Avoir étudié la Révolution française (jeu « Le Secret de la Déclaration ») : 1789, fin de la monarchie absolue, Déclaration des droits de l'homme.",
      "- Lire une frise, une carte simple et un tableau d'histoire.", "",
      "## 3. Déroulés possibles", "",
      "- **Une séance de 60 à 75 min** : équipes de 3 ou 4 ; tableau de bord enseignant `immersifs/napoleon-republique/prof.html`.",
      "- **Cinq séances de 25 min** : une salle par séance, la fiche lue en fin de séance (bouton « Leçons A4 » des réglages). La séance 4 se termine par un débat « héritage ou part d'ombre ? ».",
      "- **Avec une sortie ou un projet** : la mairie de la commune (salle des mariages, devise au fronton, buste de Marianne), le monument aux morts, une cérémonie du 11 Novembre ; à Paris, les Invalides et l'Arc de triomphe.", "",
      "## 4. Différenciation (grades)", "",
      "- **Jeune visiteur (≈ CE2)** : 15 énigmes courtes, vocabulaire simple, premier indice offert.",
      "- **Guide du musée (≈ CM1)** et **Enquêteur d'histoire (≈ CM2)** : les énigmes des niveaux CM1 et CM2 ci-dessus.",
      "- **Archiviste (≈ 6ᵉ)** et **Conservateur (≈ 5ᵉ)** : 20 énigmes avec justification par une phrase de la fiche ; propagande, héritage et part d'ombre, calculs de durées.", "",
      "## 5. Gestion de classe et pistes de discussion", "",
      "- « Napoléon est-il un héros ? » : faire lister ce qu'il a construit et ce qu'il a détruit (tri de la salle 4) ; conclure qu'un personnage historique se juge avec des faits.",
      "- « Pourquoi Napoléon fait-il peindre ses victoires et son sacre ? » : la propagande (salles 1 et 2).",
      "- « Qu'est-ce qui distingue un empereur d'un président de la République ? » : héréditaire / élu (salle 5).",
      "- Le rétablissement de l'esclavage en 1802 : à relier au jeu n°12 et à la Journée nationale des mémoires de la traite, de l'esclavage et de leurs abolitions (10 mai).", "",
      "## 6. Lexique", "",
      "général, coup d'État, Consulat, Premier consul, Concordat, plébiscite, empereur, sacre, héréditaire, emblème, sceptre, Grande Armée, campagne, retraite, abdiquer, exil, Cent-Jours, Code civil, préfet, lycée, Légion d'honneur, censure, esclavage, République, devise, hymne, Marianne, rite, Constitution.", "",
      "## 7. Évaluation", "",
      "- Fin de jeu : la phrase des cinq mots à expliquer à l'oral.", "- Trace écrite : une frise 1769-1821 avec six repères ; un tableau « héritage / part d'ombre » ; les cinq symboles de la République.",
      "- Évaluations imprimables (QCM, vrai/faux, études de documents) : à produire avec les leçons A4.", "",
      "## 8. Points de vigilance notionnels", "",
      "- Bonaparte devient « Napoléon » à partir de 1804 (Napoléon Ier) : avant, on dit « Bonaparte » ou « le Premier consul ».",
      "- Le Consulat n'est pas une démocratie : le Premier consul a presque tous les pouvoirs ; le plébiscite n'est pas une élection libre entre plusieurs candidats.",
      "- Le drapeau tricolore est né pendant la Révolution et a été utilisé sous l'Empire : il n'est donc pas un critère pour distinguer Empire et République (énigme 5-1).",
      "- L'esclavage, aboli en 1794, est rétabli en 1802 ; il n'est aboli définitivement qu'en 1848.",
      "- Le tableau de David est une œuvre de propagande : David a choisi de peindre le couronnement de Joséphine.", "",
      "## 9. Sources", ""] + [f"- {x.strip()}" for x in E["metadata"]["sources"].split(" ; ")] + [""]
open("GUIDE-PEDAGOGIQUE.md", "w", encoding="utf-8").write("\n".join(g))
print("README.md et GUIDE-PEDAGOGIQUE.md écrits")
