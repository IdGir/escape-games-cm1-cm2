# -*- coding: utf-8 -*-
"""Réécrit les énigmes « lettres » : lettres cachées dans le désordre, avec des leurres."""
import json, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def b(l, aff=None):
    return f"<b data-l='{l}'>{aff or l.lower()}</b>"

NOUVEAU = {
 ("melanges", "5-3"): {
  "cible": ["É","V","A","P","O","R","E","R"],
  "texte": ("<p>Chaque matin, Yann fait ent" + b("R") + "er l'eau de mer dans les bassins. Le soleil la chauffe et la fait partir "
            + b("P") + "eu à peu dans l'air ; l" + b("E") + " vent aide aussi. Au bout de quelques jour" + b("S")
            + ", de petits cristaux blancs se f" + b("O") + "rment à la surface : c'est la fleur de sel, récoltée l'" + b("É","é")
            + "té. Yann la " + b("V") + "end au marché, avec " + b("L") + "e gros sel du ma" + b("R") + "ais qu'il r" + b("A")
            + "masse au râteau.</p>"),
  "consigne": {
   "cm1": "Dans le récit de Yann, dix lettres sont en couleur, dans le désordre. Huit forment le nom de la méthode qui sépare le sel de l'eau salée ; deux sont des pièges. Clique les bonnes lettres pour les ranger dans les cases, dans le bon ordre.",
   "cm2": "Des lettres en couleur, dans le désordre, cachent le nom de la méthode qui permet de récupérer un solide dissous dans l'eau. Deux lettres sont des pièges. Range les bonnes dans les cases, dans l'ordre."}},
 ("chateau-fort", "4-4"): {
  "cible": ["V","I","L","L","A","G","E"],
  "texte": ("<p>Au pied du ch" + b("A","â") + "teau, les maisons se serrent autour de l'église. Les femmes et les hommes y travai" + b("L")
            + "lent du lever au coucher du soleil. L" + b("E") + "s champs, les prés et les jardins nourrissent tout le " + b("M")
            + "onde. Le blé est coupé en juillet, puis battu au fléau. En septembre viennent les vendan" + b("G")
            + "es, puis les semailles de l'automne. Le d" + b("I") + "manche, on se repose et l'on se retrouve sur la p" + b("L")
            + "ace, devant l'église, a" + b("V") + "ant de ren" + b("T") + "rer.</p>"),
  "consigne": "Neuf lettres sont cachées dans le texte, dans le désordre, et deux sont des pièges. Range les bonnes dans les cases : elles forment le nom du lieu où vivent la plupart des paysannes et des paysans. C'est le mot de la quatrième clé."},
 ("moyen-age-abbaye", "2-4"): {
  "cible": ["E","M","P","I","R","E"],
  "texte": ("<p>Charlemagne réunit des peuples nombreux : F" + b("R") + "ancs, Saxons, Lombards. Le pap" + b("E")
            + " le couronne à Rome, et Alcu" + b("I") + "n enseigne au palais. Des envoyés, les missi d" + b("O")
            + "minici, parcourent ses terres. Son " + b("P") + "ouvoir s'étend de l'océan jusqu'aux fleuves de l'est, et il fait frapper "
            + b("M") + "on" + b("N") + "aie à son nom. Il meurt à Aix-la-Chapell" + b("E") + " en 814.</p>"),
  "consigne": {"cm2": "Huit lettres ont été écrites à l'encre dorée, dans le désordre ; deux sont des pièges. Range les autres dans les cases : elles forment le nom du territoire immense que gouverne Charlemagne à partir de l'an 800. C'est le mot de la deuxième page."}},
 ("station-meteo", "5-3"): {
  "cible": ["O","U","E","S","T"],
  "texte": ("<p>« Bonjour à tous. Mercredi, le " + b("T") + "hermomètre est monté à 21 °C sous abri. L'anémomètr" + b("E")
            + " a relevé un vent moyen de 24 km/h, force 4. " + b("N","N") + "otre pluviomètre a recueilli 7 mm. Nous prévoyons pour la sortie une matinée "
            + b("S") + "èche, puis des averses en fin de jo" + b("U") + "rnée. Pensez à e" + b("M") + "porter un coupe-vent. Rendez-v" + b("O")
            + "us demain matin pou" + b("R") + " les relevés. »</p>"),
  "consigne": "Dans le bulletin, huit lettres sont en relief, dans le désordre, et trois sont des pièges. Range les bonnes dans les cases pour écrire la direction d'où venait le vent mercredi."},
 ("objets-techniques", "1-4"): {
  "cible": ["B","E","S","O","I","N"],
  "texte": ("<p>Avant d'inventer quoi que ce soit, l'inventrice " + b("N") + "ote ce qu'elle observe. Elle regarde ce qui manque, ce qui est tr"
            + b("O") + "p lourd, ce qui prend " + b("A") + "ssez de temps pour agacer tout le monde. Elle écrit en" + b("S")
            + "uite une phrase très courte dans son carnet : « Il faut un objet qu" + b("I") + "… ». Cette phrase " + b("E")
            + "st sa boussole : elle guide tout le travail, jusqu'au " + b("T") + "out dernier essai de l'o" + b("B") + "jet.</p>"),
  "consigne": "Huit lettres sont cachées en gras dans le texte, dans le désordre ; deux sont des pièges. Range les bonnes dans les cases : elles forment ce qui fait naître un objet technique. C'est le mot de la première serrure."},
 ("constitution", "1-4"): {
  "cible": ["R","È","G","L","E","S"],
  "texte": ("<p>Une Constitution rassemble " + b("L") + "es principes les plus importants d'un pays. Ell" + b("E")
            + " dit qui gouverne, c" + b("O") + "mment on vote et quels droit" + b("S") + " sont protégés. Son but est tr" + b("È","è")
            + "s clair : permettre à tous de vivre ensemble. Elle or" + b("G") + "anise les trois pouvoirs e" + b("T")
            + " se place au-dessus de toutes les lois : c'est le texte le plus impo" + b("R") + "tant de la République.</p>"),
  "consigne": "Huit lettres sont cliquables, dans le désordre ; deux sont des pièges. Range les bonnes dans les cases pour écrire ce qu'une Constitution fixe pour tout un pays. C'est le mot de la première serrure."},
}

for (jeu, eid), n in NOUVEAU.items():
    if jeu == "moyen-age-abbaye":
        continue   # fichier au format compact : modifié à la main (même contenu que ci-dessus)
    p = os.path.join(R, jeu, "assets", "data", "enigmes.json")
    s = open(p, encoding="utf-8").read()
    d = json.loads(s)
    for sal in d["salles"]:
        for e in sal["enigmes"]:
            if e["id"] != eid:
                continue
            bloc = "commun" if "commun" in e else ("cm2" if "cm2" in e else "cm1")
            # contrôle : les lettres du mot sont toutes dans le texte, et au moins une lettre en trop
            import re
            lettres = re.findall(r"data-l='([^']+)'", n["texte"])
            reste = lettres[:]
            for L in n["cible"]:
                reste.remove(L)
            assert reste, (jeu, "pas de leurre")
            assert lettres != n["cible"], (jeu, "lettres dans l'ordre")
            e[bloc]["cible"] = n["cible"]
            e[bloc]["texte"] = n["texte"]
            e["consigne"] = n["consigne"]
    out = json.dumps(d, ensure_ascii=False, indent=2) + ("\n" if s.endswith("\n") else "")
    open(p, "w", encoding="utf-8", newline="").write(out)
    print("lettres :", jeu, eid)
