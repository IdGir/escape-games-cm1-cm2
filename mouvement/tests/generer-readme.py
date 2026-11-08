# -*- coding: utf-8 -*-
# Génère mouvement/README.md à partir des données JSON (solutions toujours à jour).
# Lancement depuis la racine du dépôt : python mouvement/tests/generer-readme.py
import json, sys, re, os
R = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
E = json.load(open(R + "/assets/data/enigmes.json", encoding="utf-8"))
D = json.load(open(R + "/assets/data/dialogues.json", encoding="utf-8"))
URL = "https://idgir.github.io/escape-games-cm1-cm2/mouvement/"

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
 1: "« Mesurer une distance lors du déplacement d'un objet » : repérer un point de départ et un point d'arrivée, choisir un instrument adapté (CM1) ; « effectuer des conversions d'unités de distance » (CM2).",
 2: "« Mesurer une durée, comme intervalle entre deux instants, lors du déplacement d'un objet » ; utiliser un chronomètre (CM1) ; « effectuer des conversions d'unités de […] temps » (CM2).",
 3: "Comparer des déplacements : même distance, durées différentes ; même durée, distances différentes (le programme 2026 place ces constats en sixième, « de manière qualitative, sans aborder la formule » : ici en prolongement, sans formule).",
 4: "« Observer et identifier le mouvement rectiligne ou circulaire d'un objet, en fonction de l'observateur » ; « décrire le mouvement de la Terre par rapport au Soleil et la situer dans le système solaire » (CM2).",
 5: "« Le mouvement d'un objet est toujours décrit par rapport à un observateur » ; « un objet qu'on lâche décrit une droite verticale par rapport à la personne qui le lâche » (CM2) ; classement final par les durées.",
}
NOTION = {1: "Mesurer une distance : instruments, unités, conversions", 2: "Mesurer une durée : instant et durée, chronomètre, conversions",
          3: "Comparer des déplacements (même distance ou même durée)", 4: "Trajectoires rectilignes, circulaires, curvilignes ; la Terre autour du Soleil", 5: "Le mouvement dépend de l'observateur ; classement final"}
BO = ("> 📘 **Référence officielle du programme** (annexe 2 consultée le 8 novembre 2026) :\n>\n"
      "> - Sciences et technologie, cycles 2 et 3 : [Arrêté du 5 juin 2026 — BO n° 24 du 11 juin 2026](https://www.education.gouv.fr/bo/2026/Hebdo24/MENE2611650A) (NOR MENE2611650A) — en CM1 à la rentrée 2026, en CM2 à la rentrée 2027. "
      "Annexe 2, « Différents types de mouvement » : **CM1** mesurer une distance et une durée ; **CM2** mouvement rectiligne ou circulaire en fonction de l'observateur, la Terre autour du Soleil, conversions d'unités ; **sixième** comparaison qualitative des vitesses.\n")
ENTETE = "_Sciences et technologie, cycle 3 — Année B, période 2 — « Mesure une distance et une durée lors du déplacement d'un objet. Différents types de mouvement. » (programme 2026 : « Différents types de mouvement »)._\n"
out = []
w = out.append
w("# Le Grand Prix de l'observatoire\n")
w("**Escape game n°11 de sciences — CM1 / CM2 — mesurer une distance et une durée, comparer des déplacements, trajectoires, la Terre autour du Soleil, le rôle de l'observateur**  ")
w("60 à 75 minutes · équipes de 3-4 élèves, ou classe entière au TBI · **15 énigmes en CM1, 20 en CM2** · 10 types d'énigmes.\n")
w("> *Sur un plateau au pied d'un petit observatoire, le matin du Grand Prix des véhicules de l'école.* Cette nuit, le vent a renversé")
w("> les plots et dispersé les feuilles de mesure de Margaux, la commissaire de course ; le chronomètre officiel est verrouillé et les")
w("> résultats doivent être validés avant midi. Les élèves, commissaires, passent par la ligne de départ, le stand des chronométreurs,")
w("> le tableau des temps, la coupole de l'observatoire et le quai du petit train. Le classement de la descente ouvre le chronomètre officiel ;")
w("> les cinq mots ouvrent le coffre du Grand Prix.\n")
w("Programme : sciences et technologie, cycle 3 (programme 2026) — « Différents types de mouvement ». Progression de l'enseignant :")
w("**année B, période 2** (« Mesure une distance et une durée lors du déplacement d'un objet. Différents types de mouvement. »).")
w("La vitesse reste une comparaison (même distance ou même durée), **sans formule**, comme le demande le programme.\n")
w("| | |\n|---|---|")
w(f"| ▶ **Jouer** | [en ligne]({URL}) · en local : http://127.0.0.1:8000/mouvement/ (avec `lancer.bat`) · [version immersive](../immersifs/mouvement/) |")
w(f"| 📖 **Leçons A4** | [à imprimer, CM1 ou CM2]({URL}lecons-imprimables.html) — aussi depuis ⚙️ Réglages dans le jeu : une page illustrée par leçon |")
w("| 👨‍🏫 **Tableau de bord** | http://127.0.0.1:8000/mouvement/prof.html — mode local uniquement |")
w("| 🔍 **Vérifier** | [page de vérification](https://idgir.github.io/escape-games-cm1-cm2/verifier.html#mouvement) : tester chaque énigme, voir les médias |")
w("| 🎞️ **Médias** | [assets/README.md](assets/README.md) : tous les noms de fichiers attendus (tous facultatifs) |")
w("| 📖 **Guide pédagogique** | [GUIDE-PEDAGOGIQUE.md](GUIDE-PEDAGOGIQUE.md) : programme, déroulés, différenciation, évaluation |")
w("| ⚠️ **Points à contrôler** | [A-VERIFIER.md](A-VERIFIER.md) |\n")
w("**Sécurité** (à dire en classe) : on ne mesure ni ne chronomètre jamais au bord d'une route ou d'une voie ferrée ; les essais de")
w("petites voitures se font dans la cour ou le préau.\n")
w("Liens avec les autres jeux : prépare « La Centrale en panne » (n°14) et « Le Robot de l'atelier » (n°18) ; se relie à « L'Atelier")
w("de l'inventeur » (n°04 : transmission du mouvement) et au « Tour du monde » (échelles, durées de trajet).\n\n---\n")
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
w(f"| 🏁 | Fin : coffre du Grand Prix, tableau d'honneur, quizz | | Margaux | | 5 questions | [CM1]({URL}?salle=6&niveau=CM1) · [CM2]({URL}?salle=6&niveau=CM2) |\n")
w("Les cinq mots, retapés dans le coffre, valident le Grand Prix ; le tableau d'honneur affiche :  ")
w("**« On mesure une DISTANCE et une DURÉE ; on compare la VITESSE ; on décrit la TRAJECTOIRE, toujours par rapport à un OBSERVATEUR. »**  ")
w("Le tableau d'honneur rappelle ensuite le classement officiel de la descente (code 47925). Pendant les **5 questions de synthèse** (quizz final), chaque bonne réponse fait tomber un drapeau à damier au-dessus du podium.\n")
w("Les liens « Tester » ouvrent la salle directement, sans nom d'équipe ; **rien n'est sauvegardé**.")
w("On peut aussi viser une énigme précise : `mouvement/?salle=2&niveau=CM2&enigme=4`.\n\n---\n")
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
w("## Types d'énigmes utilisés (10 sur 11)\n")
w("| Type | Énigmes |\n|---|---|")
from collections import defaultdict
T = defaultdict(list)
for se in E["salles"]:
    for e in se["enigmes"]:
        T[e["type"]].append(e["id"] + ("*" if e.get("niveaux") else ""))
for t in E["metadata"]["types"]:
    w(f"| `{t}` | {', '.join(T[t])} |")
w("\n\\* énigme réservée au CM2. Dans chaque salle, deux énigmes consécutives ne sont jamais du même type, et au moins une")
w("énigme fait manipuler (ordonner, trier, placer sur un schéma) : 1-1, 2-1, 2-4, 3-2, 4-1, 4-2, 5-2. Le type `instrument` (thermomètre, pluviomètre) n'a pas d'équivalent pour une règle ou un chronomètre : les lectures se font sur des schémas (1-3) et des tableaux (2-3, 5-3).\n\n---\n")
w(open(os.path.join(R, "tests", "readme-suite.md"), encoding="utf-8").read())
print_ = None
open(os.path.join(R, "README.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("README.md écrit :", sum(len(x) for x in out), "caractères")
