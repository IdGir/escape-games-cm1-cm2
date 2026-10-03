# -*- coding: utf-8 -*-
# Génère alimentation/README.md à partir des données JSON (solutions toujours à jour).
# Lancement depuis la racine du dépôt : python alimentation/tests/generer-readme.py
import json, sys, re, os
R = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
E = json.load(open(R + "/assets/data/enigmes.json", encoding="utf-8"))
D = json.load(open(R + "/assets/data/dialogues.json", encoding="utf-8"))
URL = "https://idgir.github.io/escape-games-cm1-cm2/alimentation/"

def propre(s):
    return re.sub(r"<[^>]+>", "", s).strip()

def solution(e, niv):
    d = e.get(niv.lower()) or e.get("commun") or {}
    t = e["type"]
    L = []
    if t == "qcm":
        for q in d["questions"]:
            L.append(f"- {propre(q['q'])} → **{propre(q['options'][q['bonne']])}**")
    elif t == "vraifaux":
        for a in d["affirmations"]:
            L.append(f"- {propre(a['txt'])} → **{'Vrai' if a['vrai'] else 'Faux'}**")
    elif t == "association":
        for p in d["paires"]:
            L.append(f"- {p['g']} → **{p['d']}**")
    elif t == "ordre":
        for it in sorted(d["items"], key=lambda x: x["rang"]):
            L.append(f"{it['rang']}. {it['txt']}" + (f" ({it['sous']})" if it.get("sous") else ""))
    elif t == "tri":
        cols = {c["id"]: c["titre"] for c in d["colonnes"]}
        for cid, titre in cols.items():
            L.append(f"- **{titre}** : " + " ; ".join(c["txt"] for c in d["cartes"] if c["col"] == cid))
    elif t == "trous":
        reps = re.findall(r"\[\[(.+?)\]\]", d["texte"])
        L.append("Mots attendus, dans l'ordre : **" + "**, **".join(reps) + "**")
        trop = [x for x in d.get("etiquettes", []) if x not in reps]
        if trop: L.append(f"Étiquettes en trop : {', '.join(trop)}")
    elif t == "lettres":
        L.append("Lettres à cliquer dans l'ordre : **" + " ".join(d["cible"]) + "**")
    elif t == "code":
        for c in d["champs"]:
            L.append(f"- {c['libelle']} → **{c['valeur']}**")
    elif t == "intrus":
        L.append("Intrus : **" + next(c["txt"] for c in d["cartes"] if c["intrus"]) + "**")
    elif t == "plan":
        for c in d["cases"]:
            L.append(f"- {propre(c['libelle'])} → **{c['reponse']}**")
    return "\n".join(L)


COMP = {
 1: "Exploiter des données mettant en évidence le besoin de matière pour la croissance et le développement des êtres vivants.",
 2: "Exploiter des données pour expliquer la variation des besoins alimentaires au cours de la croissance et selon l'activité physique.",
 3: "Identifier et localiser la transformation des aliments dans l'appareil digestif (mastication par les dents, changements de texture lors du trajet).",
 4: "Nommer et localiser les différents organes du système digestif, en les associant à leur fonction ; nutriments utilisables par les organes.",
 5: "Identifier le rôle de la circulation sanguine dans l'approvisionnement des organes en nutriments ; associer l'augmentation de l'activité cardiaque lors d'un effort aux besoins accrus des muscles.",
}
NOTION = {1: "Grandir : le besoin de matière (le poussin Caramel, la toise de Lou)", 2: "Des besoins qui changent (âge, croissance, activité)",
          3: "Mâcher : dents, salive, textures", 4: "Le trajet des aliments : organes et fonctions", 5: "Le sang livre les nutriments ; le pouls"}
BO = ("> 📘 **Référence officielle du programme** (vérifiée sur education.gouv.fr le 1er octobre 2026, affichée aussi sur l'écran d'accueil du jeu) :\n>\n"
      "> - Sciences et technologie, cycles 2 et 3 : [Arrêté du 5 juin 2026 — BO n° 24 du 11 juin 2026](https://www.education.gouv.fr/bo/2026/Hebdo24/MENE2611650A) (NOR MENE2611650A) — en CM1 à la rentrée 2026, en CM2 à la rentrée 2027.\n")
ENTETE = "_Sciences et technologie, cycle 3 — Année A, période 2 — Thème « Le corps humain et la santé » : Alimentation humaine — Besoins alimentaires et nutrition humaine (programme 2026)._\n"
out = []
w = out.append
w("# Le Grand Repas du chef\n")
w("**Escape game n°08 de sciences — CM1 / CM2 — l'alimentation humaine : besoins alimentaires et nutrition humaine**  ")
w("60 à 75 minutes · équipes de 3-4 élèves, ou classe entière au TBI · **15 énigmes en CM1, 20 en CM2** · les 10 types du moteur.\n")
w("> *Au restaurant Le Grand Couvert, la veille d'une étape de montagne.* La cheffe Rosalie prépare le repas de Basile,")
w("> coureur cycliste. Mais son carnet de recettes, *Le Livre des cinq services*, est enfermé dans un coffre à cinq cadenas.")
w("> Les élèves, ses commis, parcourent la cour du potager et du poulailler, la salle des menus, la table de dégustation, le")
w("> cabinet du Grand Tunnel et la salle d'entraînement. Les cinq mots retrouvés ouvrent le coffre, puis le livre révèle sa")
w("> première page et le menu du repas.\n")
w("Programme : sciences et technologie, cycle 3 — « Le corps humain et la santé », **Alimentation humaine — Besoins alimentaires")
w("et nutrition humaine** (programme 2026). Progression de l'enseignant : **année A, période 2**. L'ancien libellé « production")
w("et conservation des aliments » (programme 2020) ne figure plus dans le programme 2026 : le jeu suit le nouveau libellé.\n")
w("| | |\n|---|---|")
w(f"| ▶ **Jouer** | [en ligne]({URL}) · en local : http://127.0.0.1:8000/alimentation/ (avec `lancer.bat`) |")
w(f"| 📖 **Leçons A4** | [à imprimer, CM1 ou CM2]({URL}lecons-imprimables.html) — aussi depuis ⚙️ Réglages dans le jeu : une page illustrée par leçon (courbe, toise, barres, mâchoire, tube digestif, pouls, compétence du programme) |")
w("| 👨‍🏫 **Tableau de bord** | http://127.0.0.1:8000/alimentation/prof.html — mode local uniquement |")
w("| 🔍 **Vérifier** | [page de vérification](https://idgir.github.io/escape-games-cm1-cm2/verifier.html#alimentation) : tester chaque énigme, voir les médias |")
w("| 🎞️ **Médias** | [assets/README.md](assets/README.md) : tous les noms de fichiers attendus (tous facultatifs) |")
w("| 📖 **Guide pédagogique** | [GUIDE-PEDAGOGIQUE.md](GUIDE-PEDAGOGIQUE.md) : programme, déroulés, différenciation, évaluation |")
w("| ⚠️ **Points à contrôler** | [A-VERIFIER.md](A-VERIFIER.md) |\n")
w("Liens avec les autres jeux : prolonge les séances 9 à 12 de la géographie (`mission-geo/` : pratiques alimentaires, chaîne du")
w("yaourt) ; prépare le jeu n°15 (le développement des animaux).\n\n---\n")
w("## 🎯 Compétences du programme (vue d'ensemble)\n")
w(ENTETE + "\n" + BO)
w("| Salle | Compétence du programme |\n|---|---|")
for s in D["salles"]:
    w(f"| **{s['num']}.** {s['titre']} | {COMP[s['num']]} |")
w("\nDétail énigme par énigme : voir [GUIDE-PEDAGOGIQUE.md](GUIDE-PEDAGOGIQUE.md).\n\n")
w("## Les 5 salles\n")
w("| # | Lieu | Notion | Personnage | Mot-clé | Énigmes | Tester |\n|---|---|---|---|---|---|---|")
for s in D["salles"]:
    p = s["dialogue_intro"]["nom"]
    w(f"| {s['num']} | {s['titre']} | {NOTION[s['num']]} | {p} | **{s['motCle']}** | 3 en CM1 · 4 en CM2 | [CM1]({URL}?salle={s['num']}&niveau=CM1) · [CM2]({URL}?salle={s['num']}&niveau=CM2) |")
w(f"| 🏁 | Fin : coffre, Livre des cinq services, quizz | | Rosalie | | 5 questions | [CM1]({URL}?salle=6&niveau=CM1) · [CM2]({URL}?salle=6&niveau=CM2) |\n")
w("Les cinq mots ouvrent le coffre final, puis le livre révèle sa première page :  ")
w("**« Pour GRANDIR et BOUGER, il faut MÂCHER et DIGÉRER : le SANG livre le reste. »**  ")
w("Puis le menu du repas de Basile : entrée (carottes râpées), plat (pâtes, poulet et haricots verts), fromage, dessert (une pomme), boisson (de l'eau) —")
w("à adapter à la classe (allergies, régimes, pratiques des familles). Les cadenas du livre sautent pendant les **5 questions de synthèse** (quizz final).\n")
w("Les liens « Tester » ouvrent la salle directement, sans nom d'équipe ; **rien n'est sauvegardé**.")
w("On peut aussi viser une énigme précise : `alimentation/?salle=2&niveau=CM2&enigme=4`.\n\n---\n")
w("## Énigmes et solutions\n")
w("<details>\n<summary>⚠️ Solutions — à ne pas projeter en classe</summary>\n")
for se in E["salles"]:
    w(f"### Salle {se['num']} — {se['titre']}\n")
    for e in se["enigmes"]:
        nivs = e.get("niveaux") or ["CM1", "CM2"]
        w(f"#### {e['id']} · {e['titre']} — type `{e['type']}` — {' et '.join(nivs)}\n")
        if len(nivs) == 2 and ("cm1" in e) and ("cm2" in e):
            w("**CM1**\n\n" + solution(e, "CM1") + "\n\n**CM2**\n\n" + solution(e, "CM2") + "\n")
        else:
            w(solution(e, nivs[0]) + "\n")
        w(f"*Correction (documents enseignant) :* {propre(e['correction'])}  \n*Source :* {e['source']} · *Leçon :* `{e['lecon']}`\n")
w("</details>\n\n---\n")
w("## Types d'énigmes utilisés (10 sur 10)\n")
w("| Type | Énigmes |\n|---|---|")
from collections import defaultdict
T = defaultdict(list)
for se in E["salles"]:
    for e in se["enigmes"]:
        T[e["type"]].append(e["id"] + ("*" if e.get("niveaux") else ""))
for t in E["metadata"]["types"]:
    w(f"| `{t}` | {', '.join(T[t])} |")
w("\n\\* énigme réservée au CM2. Dans chaque salle, deux énigmes consécutives ne sont jamais du même type, et au moins une")
w("énigme fait manipuler (ordonner, trier, placer sur un schéma) : 1-3, 2-1, 2-2, 3-2, 3-4, 4-1, 5-3.\n\n---\n")
w(open(os.path.join(R, "tests", "readme-suite.md"), encoding="utf-8").read())
print_ = None
open(os.path.join(R, "README.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("README.md écrit :", sum(len(x) for x in out), "caractères")
