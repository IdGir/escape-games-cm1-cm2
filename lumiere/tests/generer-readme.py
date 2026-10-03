# -*- coding: utf-8 -*-
# Génère lumiere/README.md à partir des données JSON (solutions toujours à jour).
# Lancement depuis la racine du dépôt : python lumiere/tests/generer-readme.py
import json, sys, re, os
R = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
E = json.load(open(R + "/assets/data/enigmes.json", encoding="utf-8"))
D = json.load(open(R + "/assets/data/dialogues.json", encoding="utf-8"))
URL = "https://idgir.github.io/escape-games-cm1-cm2/lumiere/"

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
    elif t == "plan":
        for c in d["cases"]:
            L.append(f"- {propre(c['libelle'])} → **{c['reponse']}**")
    return "\n".join(L)


COMP = {
 1: "Signaux — la lumière : identifier une source lumineuse et des objets éclairés ; la lumière se propage en ligne droite jusqu'à l'œil ; la lumière porte un signal (prérequis de « produire une ombre […] associée à une source » ; progression : « Matière, mouvement, énergie et information »).",
 2: "« Observer et classer des matériaux selon qu'ils sont transparents, opaques à la lumière ou translucides » ; justifier un tri.",
 3: "« Produire expérimentalement une ombre (déficit de lumière associé à une source) à l'aide d'un objet opaque et distinguer ombre propre et ombre portée » ; « associer leurs positions et leurs tailles à celles de la source lumineuse et de l'objet opaque ».",
 4: "« Observer la position de l'ombre d'un bâton sur le sol au cours d'une journée ensoleillée et l'associer au déplacement du Soleil dans le ciel du point de vue de la cour de récréation ».",
 5: "« Observer, schématiser et nommer les phases de la Lune » ; constater l'existence d'un cycle (la lunaison) ; décoder un signal lumineux (Morse).",
}
NOTION = {1: "Sources de lumière, objets éclairés, trajet de la lumière, signaux", 2: "Transparent, translucide, opaque ; le miroir",
          3: "Ombre propre, ombre portée : position et taille", 4: "L'ombre d'un bâton au fil de la journée ; le midi solaire", 5: "Les phases de la Lune ; le message Morse"}
BO = ("> 📘 **Référence officielle du programme** (vérifiée sur education.gouv.fr le 3 octobre 2026, affichée aussi sur l'écran d'accueil du jeu) :\n>\n"
      "> - Sciences et technologie, cycles 2 et 3 : [Arrêté du 5 juin 2026 — BO n° 24 du 11 juin 2026](https://www.education.gouv.fr/bo/2026/Hebdo24/MENE2611650A) (NOR MENE2611650A) — en CM1 à la rentrée 2026, en CM2 à la rentrée 2027. "
      "Annexe 2, cours moyen première année, thème « La matière, les mouvements et les signaux », sous-thème **Signaux — Lumière**.\n")
ENTETE = "_Sciences et technologie, cycle 3 — Année A, période 2 — « Matière, mouvement, énergie et information » : la lumière (programme 2026 : « La matière, les mouvements et les signaux », Signaux — Lumière)._\n"
out = []
w = out.append
w("# Le Phare de l'île Lumière\n")
w("**Escape game n°09 de sciences — CM1 / CM2 — la lumière : sources, matériaux, ombres, Soleil et Lune, signaux lumineux**  ")
w("60 à 75 minutes · équipes de 3-4 élèves, ou classe entière au TBI · **15 énigmes en CM1, 20 en CM2** · les 10 types du moteur.\n")
w("> *Sur l'île Lumière, île imaginaire, à la tombée de la nuit.* Le phare de Maëlle, la gardienne, ne s'allume plus, et")
w("> *La Mouette*, le voilier de la capitaine Yasmine, approche des rochers. Le tableau de commande est verrouillé par un code")
w("> de cinq mots. Les élèves, apprentis gardiens, parcourent la lanterne, l'atelier des vitres, la chambre aux ombres, la cour")
w("> du cadran solaire et la galerie du phare. Les cinq mots rallument le phare ; *La Mouette* répond en Morse.\n")
w("Programme : sciences et technologie, cycle 3 (programme 2026) — « La matière, les mouvements et les signaux », **Signaux —")
w("Lumière** (cours moyen première année). Progression de l'enseignant : **année A, période 2** (« Matière, mouvement, énergie")
w("et information. La lumière. »). En classe à double niveau, les CM2 révisent et approfondissent (distances, relevés, 6 phases).\n")
w("| | |\n|---|---|")
w(f"| ▶ **Jouer** | [en ligne]({URL}) · en local : http://127.0.0.1:8000/lumiere/ (avec `lancer.bat`) |")
w(f"| 📖 **Leçons A4** | [à imprimer, CM1 ou CM2]({URL}lecons-imprimables.html) — aussi depuis ⚙️ Réglages dans le jeu : une page illustrée par leçon (schémas, tableau du Morse, relevé d'ombres, phases de la Lune, compétence du programme) |")
w("| 👨‍🏫 **Tableau de bord** | http://127.0.0.1:8000/lumiere/prof.html — mode local uniquement |")
w("| 🔍 **Vérifier** | [page de vérification](https://idgir.github.io/escape-games-cm1-cm2/verifier.html#lumiere) : tester chaque énigme, voir les médias |")
w("| 🎞️ **Médias** | [assets/README.md](assets/README.md) : tous les noms de fichiers attendus (tous facultatifs) |")
w("| 📖 **Guide pédagogique** | [GUIDE-PEDAGOGIQUE.md](GUIDE-PEDAGOGIQUE.md) : programme, déroulés, différenciation, évaluation |")
w("| ⚠️ **Points à contrôler** | [A-VERIFIER.md](A-VERIFIER.md) |\n")
w("**Sécurité** (à dire en classe, rappelée dans les leçons) : ne jamais regarder le Soleil directement, même avec des lunettes")
w("de soleil ; ne jamais diriger un pointeur laser vers les yeux.\n")
w("Liens avec les autres jeux : prolonge « La Station météo disparue » (n°03, mesures dans la cour) ; prépare le jeu n°14")
w("(l'électricité : la lampe).\n\n---\n")
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
w(f"| 🏁 | Fin : tableau de commande, registre du phare, quizz | | Maëlle | | 5 questions | [CM1]({URL}?salle=6&niveau=CM1) · [CM2]({URL}?salle=6&niveau=CM2) |\n")
w("Les cinq mots, retapés sur le tableau de commande, rallument le phare ; la première page du registre affiche :  ")
w("**« Une SOURCE envoie sa lumière en ligne droite ; un objet OPAQUE l'arrête et fait naître une OMBRE. L'ombre tourne avec le SOLEIL, qui éclaire aussi la LUNE. »**  ")
w("*La Mouette* répond au phare en Morse : MERCI (—— • •—• —•—• ••). Pendant les **5 questions de synthèse** (quizz final), chaque bonne réponse chasse un nuage devant le phare.\n")
w("Les liens « Tester » ouvrent la salle directement, sans nom d'équipe ; **rien n'est sauvegardé**.")
w("On peut aussi viser une énigme précise : `lumiere/?salle=2&niveau=CM2&enigme=4`.\n\n---\n")
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
w("énigme fait manipuler (ordonner, trier, placer sur un schéma) : 1-1, 1-2, 2-2, 3-1, 3-3, 4-1, 4-3, 5-1.\n\n---\n")
w(open(os.path.join(R, "tests", "readme-suite.md"), encoding="utf-8").read())
print_ = None
open(os.path.join(R, "README.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("README.md écrit :", sum(len(x) for x in out), "caractères")
