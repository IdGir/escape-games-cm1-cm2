# -*- coding: utf-8 -*-
# Génère renaissance/README.md à partir des données JSON (solutions toujours à jour).
# Lancement depuis la racine du dépôt : python renaissance/tests/generer-readme.py
import json, sys, re, os
R = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
E = json.load(open(R + "/assets/data/enigmes.json", encoding="utf-8"))
D = json.load(open(R + "/assets/data/dialogues.json", encoding="utf-8"))
URL = "https://idgir.github.io/escape-games-cm1-cm2/renaissance/"

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
 1: "François Ier, un protecteur des arts et des lettres à la Renaissance (la Renaissance venue d'Italie, l'humanisme, l'imprimerie).",
 2: "François Ier, un protecteur des arts et des lettres à la Renaissance (le roi mécène : les arts, les lettres, la langue française).",
 3: "François Ier, un protecteur des arts et des lettres à la Renaissance, grâce à l'aide de Léonard de Vinci (peintre, ingénieur, observateur).",
 4: "François Ier, un protecteur des arts et des lettres à la Renaissance (les châteaux : Amboise, Blois, Chambord ; la salamandre).",
 5: "François Ier, un protecteur des arts et des lettres à la Renaissance, grâce à l'aide de Léonard de Vinci (l'art : perspective, proportions, portrait).",
}
NOTION = {1: "La Renaissance, l'humanisme, l'imprimerie", 2: "François Ier, roi mécène", 3: "Léonard de Vinci, l'artiste invité",
          4: "Les châteaux de la Renaissance", 5: "L'art de la Renaissance"}
BO = ("> 📘 **Référence officielle du programme** (vérifiée sur education.gouv.fr le 1er octobre 2026, affichée aussi sur l'écran d'accueil du jeu) :\n>\n"
      "> - Histoire-géographie, cycle 3 : [Arrêté du 22 avril 2026 — BO n° 22 du 28 mai 2026](https://www.education.gouv.fr/bo/2026/Hebdo22/MENE2608631A) (NOR MENE2608631A) — en CM1 à la rentrée 2026, en CM2 à la rentrée 2027.\n")
ENTETE = "_Histoire, cycle 3 — Année B, période 2 — Thème 2 : « La monarchie en France » : François Ier, un protecteur des arts et des lettres à la Renaissance, grâce à l'aide de Léonard de Vinci (programme d'histoire-géographie du cycle 3, BO 2026)._\n"
out = []
w = out.append
w("# L'Atelier de Léonard à Amboise\n")
w("**Escape game d'histoire — CM1 / CM2 — la Renaissance : François Ier, protecteur des arts et des lettres, et Léonard de Vinci**  ")
w("60 à 75 minutes · équipes de 3-4 élèves, ou classe entière au TBI · **15 énigmes en CM1, 20 en CM2**.\n")
w("> *Amboise, au printemps 1518.* Le roi François Ier prépare une grande fête au château. Un coup de vent a dispersé cinq pages")
w("> du carnet de Léonard de Vinci, son invité. Tommaso, l'apprenti (personnage inventé), demande aux élèves de les retrouver : chez")
w("> l'imprimeur, dans la grande salle du château, à l'atelier du Cloux, au cabinet des plans et dans la galerie des tableaux.")
w("> Les cinq mots retrouvés ouvrent le coffre final, puis le carnet, qui révèle sa page de garde et la devise du roi.\n")
w("Programme : histoire, cycle 3 — thème « La monarchie en France ». Progression de l'enseignant : **année B, période 2** —")
w("*« François Ier, un protecteur des arts et des lettres à la Renaissance, grâce à l'aide de Léonard de Vinci. »*\n")
w("| | |\n|---|---|")
w(f"| ▶ **Jouer** | [en ligne]({URL}) · en local : http://127.0.0.1:8000/renaissance/ (avec `lancer.bat`) |")
w(f"| 📖 **Leçons A4** | [à imprimer, CM1 ou CM2]({URL}lecons-imprimables.html) — aussi depuis ⚙️ Réglages dans le jeu : une page illustrée par leçon (plan, schéma, frise, compétence du programme) |")
w("| 👨‍🏫 **Tableau de bord** | http://127.0.0.1:8000/renaissance/prof.html — mode local uniquement |")
w("| 🔍 **Vérifier** | [page de vérification](https://idgir.github.io/escape-games-cm1-cm2/verifier.html#renaissance) : tester chaque énigme, voir les médias |")
w("| 🎞️ **Médias** | [assets/README.md](assets/README.md) : tous les noms de fichiers attendus (tous facultatifs) |")
w("| 📖 **Guide pédagogique** | [GUIDE-PEDAGOGIQUE.md](GUIDE-PEDAGOGIQUE.md) : programme, déroulés, différenciation, évaluation |")
w("| ⚠️ **Points à contrôler** | [A-VERIFIER.md](A-VERIFIER.md) |\n")
w("Liens avec les autres jeux : voisin du jeu n°06 (Henri IV et Louis XIV, année A) ; les châteaux de la Loire prolongent le jeu n°02")
w("(le château fort) : l'architecture passe de la défense au prestige.\n\n---\n")
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
w(f"| 🏁 | Fin : coffre, carnet complet, quizz | | Dame Hélène | | 5 questions | [CM1]({URL}?salle=6&niveau=CM1) · [CM2]({URL}?salle=6&niveau=CM2) |\n")
w("Les cinq mots ouvrent le coffre final, puis le carnet révèle sa page de garde :  ")
w("**« En imitant l'ANTIQUITÉ, la Renaissance trouve en François Ier un MÉCÈNE. Léonard apprend à OBSERVER la nature ; la SALAMANDRE du roi orne ses châteaux et la PERSPECTIVE ouvre les tableaux. »**  ")
w("Sous la page de garde : la salamandre et la devise du roi, « Nutrisco et extinguo ». Les pages se tournent pendant les **5 questions de synthèse** (quizz final).\n")
w("Les liens « Tester » ouvrent la salle directement, sans nom d'équipe ; **rien n'est sauvegardé**.")
w("On peut aussi viser une énigme précise : `renaissance/?salle=2&niveau=CM2&enigme=4`.\n\n---\n")
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
w("énigme fait manipuler (ordonner, trier, placer sur un plan) : 1-1, 2-2, 2-3, 3-2, 4-1, 4-2, 5-1.\n\n---\n")
w(open(os.path.join(R, "tests", "readme-suite.md"), encoding="utf-8").read())
print_ = None
open(os.path.join(R, "README.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("README.md écrit :", sum(len(x) for x in out), "caractères")
