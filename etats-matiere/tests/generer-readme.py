# -*- coding: utf-8 -*-
# Génère etats-matiere/README.md à partir des données JSON (solutions toujours à jour).
# Lancement depuis la racine du dépôt : python etats-matiere/tests/generer-readme.py
import json, sys, re, os
R = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
E = json.load(open(R + "/assets/data/enigmes.json", encoding="utf-8"))
D = json.load(open(R + "/assets/data/dialogues.json", encoding="utf-8"))
URL = "https://idgir.github.io/escape-games-cm1-cm2/etats-matiere/"

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
            sous = it.get("sous") or ""
            L.append(f"{it['rang']}. {it['txt']}" + (f" ({sous})" if sous and not sous.startswith("<svg") else ""))
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
    elif t == "instrument":
        for it in d["items"]:
            L.append(f"- {it['libelle']} ({'à lire' if it['mode']=='lire' else 'à régler'}) → **{str(it['valeur']).replace('-', '−')} {d.get('unite','')}**")
    elif t == "plan":
        for c in d["cases"]:
            L.append(f"- {propre(c['libelle'])} → **{c['reponse']}**")
    return "\n".join(L)


COMP = {
 1: "« Identifier les états physiques de la matière » à partir de critères observables (forme, volume, écoulement, compressibilité) ; un solide divisé (sable, farine, sucre) reste un solide (« États et constitution de la matière à l'échelle macroscopique »).",
 2: "Mettre en évidence que l'air est de la matière : il occupe un volume, il est compressible, il a une masse (« décrire un échantillon de matière avec la grandeur masse » ; prolongement des activités sur l'air).",
 3: "« Observer des changements d'état physique et leur réversibilité » : fusion, solidification, vaporisation (évaporation, ébullition), liquéfaction ; températures repères de l'eau (0 °C, 100 °C).",
 4: "Comparer avant et après un changement d'état : la masse se conserve, le volume peut changer (l'eau qui gèle) ; calculs simples de masses et de volumes.",
 5: "« Utiliser les propriétés physiques des matériaux pour les classer » (flotter, conduire la chaleur, se dissoudre) ; « identifier les états physiques de la matière dans la nature, en particulier ceux de l'eau » : le cycle de l'eau.",
}
NOTION = {1: "Solide, liquide, gaz : critères observables", 2: "L'air est de la matière : volume, compression, masse",
          3: "Changements d'état de l'eau ; 0 °C et 100 °C ; évaporation et ébullition", 4: "La masse se conserve, le volume peut changer", 5: "Propriétés de la matière ; le cycle de l'eau"}
BO = ("> 📘 **Référence officielle du programme** (arrêté vérifié le 5 novembre 2026 ; libellés à contrôler sur l'annexe, voir A-VERIFIER.md) :\n>\n"
      "> - Sciences et technologie, cycles 2 et 3 : [Arrêté du 5 juin 2026 — BO n° 24 du 11 juin 2026](https://www.education.gouv.fr/bo/2026/Hebdo24/MENE2611650A) (NOR MENE2611650A) — en CM1 à la rentrée 2026, en CM2 à la rentrée 2027. "
      "Annexe 2, thème « La matière, les mouvements et les signaux » : les **états physiques et les changements d'état** sont au **CM2** (rentrée 2027) ; mélanges, masse et propriétés de la matière au CM1.\n")
ENTETE = "_Sciences et technologie, cycle 3 — Année B, période 2 — « États et constitution de la matière à l'échelle macroscopique. Propriétés de la matière. » (programme 2026 : « La matière, les mouvements et les signaux »)._\n"
out = []
w = out.append
w("# La Fabrique des états\n")
w("**Escape game n°10 de sciences — CM1 / CM2 — les états de la matière, l'air, les changements d'état de l'eau, la masse et le volume, le cycle de l'eau**  ")
w("60 à 75 minutes · équipes de 3-4 élèves, ou classe entière au TBI · **15 énigmes en CM1, 20 en CM2** · 11 types d'énigmes.\n")
w("> *Dans la Fabrique des états, une usine imaginaire au bord d'un lac, au lendemain d'un orage.* Inès, l'ingénieure, ne peut")
w("> plus faire tourner ses machines : le grand pupitre est verrouillé par un code de cinq mots. Les élèves, ingénieurs stagiaires,")
w("> parcourent le hall des cuves, la terrasse du ballon-sonde, la glacerie de Paolo, la cuisine de Fatou et le château d'eau de")
w("> Ninon. Les cinq mots redémarrent la Fabrique ; le registre retrace le cycle de l'eau.\n")
w("Programme : sciences et technologie, cycle 3 (programme 2026) — « La matière, les mouvements et les signaux ». Progression de")
w("l'enseignant : **année B, période 2** (« États et constitution de la matière à l'échelle macroscopique. Propriétés de la matière. »).")
w("Dans le programme 2026, les états et changements d'état sont placés au CM2 : les CM1 les abordent par l'observation et le vocabulaire courant.\n")
w("| | |\n|---|---|")
w(f"| ▶ **Jouer** | [en ligne]({URL}) · en local : http://127.0.0.1:8000/etats-matiere/ (avec `lancer.bat`) · [version immersive](../immersifs/etats-matiere/) |")
w(f"| 📖 **Leçons A4** | [à imprimer, CM1 ou CM2]({URL}lecons-imprimables.html) — aussi depuis ⚙️ Réglages dans le jeu : une page illustrée par leçon |")
w("| 👨‍🏫 **Tableau de bord** | http://127.0.0.1:8000/etats-matiere/prof.html — mode local uniquement |")
w("| 🔍 **Vérifier** | [page de vérification](https://idgir.github.io/escape-games-cm1-cm2/verifier.html#etats-matiere) : tester chaque énigme, voir les médias |")
w("| 🎞️ **Médias** | [assets/README.md](assets/README.md) : tous les noms de fichiers attendus (tous facultatifs) |")
w("| 📖 **Guide pédagogique** | [GUIDE-PEDAGOGIQUE.md](GUIDE-PEDAGOGIQUE.md) : programme, déroulés, différenciation, évaluation |")
w("| ⚠️ **Points à contrôler** | [A-VERIFIER.md](A-VERIFIER.md) |\n")
w("**Sécurité** (à dire en classe, rappelée dans les leçons) : l'eau qui bout et la vapeur brûlent ; les expériences avec une")
w("source de chaleur se font avec un adulte ; jamais de bouteille en verre pleine au congélateur.\n")
w("Liens avec les autres jeux : prolonge « Le Laboratoire de Madame Mélange » (n°05 : masses, dissolution) ; se relie à « La Station")
w("météo disparue » (n°03 : thermomètre, pluie) ; prépare le jeu n°26 « Mission Climat ».\n\n---\n")
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
w(f"| 🏁 | Fin : pupitre, registre de la Fabrique, quizz | | Inès | | 5 questions | [CM1]({URL}?salle=6&niveau=CM1) · [CM2]({URL}?salle=6&niveau=CM2) |\n")
w("Les cinq mots, retapés sur le pupitre, redémarrent la Fabrique ; la première page du registre affiche :  ")
w("**« La glace est SOLIDE, l'AIR est un gaz qui a une masse ; quand l'eau devient VAPEUR, sa MASSE se conserve, puis elle redevient gouttelettes dans le NUAGE. »**  ")
w("Le registre rappelle ensuite le cycle de l'eau (évaporation, liquéfaction, précipitations, ruissellement). Pendant les **5 questions de synthèse** (quizz final), chaque bonne réponse chasse un nuage d'orage au-dessus de la Fabrique.\n")
w("Les liens « Tester » ouvrent la salle directement, sans nom d'équipe ; **rien n'est sauvegardé**.")
w("On peut aussi viser une énigme précise : `etats-matiere/?salle=2&niveau=CM2&enigme=4`.\n\n---\n")
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
w("## Types d'énigmes utilisés (11 sur 11)\n")
w("| Type | Énigmes |\n|---|---|")
from collections import defaultdict
T = defaultdict(list)
for se in E["salles"]:
    for e in se["enigmes"]:
        T[e["type"]].append(e["id"] + ("*" if e.get("niveaux") else ""))
for t in E["metadata"]["types"]:
    w(f"| `{t}` | {', '.join(T[t])} |")
w("\n\\* énigme réservée au CM2. Dans chaque salle, deux énigmes consécutives ne sont jamais du même type, et au moins une")
w("énigme fait manipuler (ordonner, trier, placer sur un schéma) : 1-1, 2-2, 3-3, 4-3, 4-4, 5-1, 5-3.\n\n---\n")
w(open(os.path.join(R, "tests", "readme-suite.md"), encoding="utf-8").read())
print_ = None
open(os.path.join(R, "README.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("README.md écrit :", sum(len(x) for x in out), "caractères")
