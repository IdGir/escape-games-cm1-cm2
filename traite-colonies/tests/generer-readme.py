# -*- coding: utf-8 -*-
# Génère traite-colonies/README.md à partir des données JSON (solutions toujours à jour).
# Lancement depuis la racine du dépôt : python traite-colonies/tests/generer-readme.py
import json, sys, re, os
R = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
E = json.load(open(R + "/assets/data/enigmes.json", encoding="utf-8"))
D = json.load(open(R + "/assets/data/dialogues.json", encoding="utf-8"))
URL = "https://idgir.github.io/escape-games-cm1-cm2/traite-colonies/"

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
 1: "« La traite des esclaves entre l'Afrique et l'Amérique » : situer l'Europe, l'Afrique et les Amériques ; décrire les trois trajets du commerce triangulaire et les marchandises échangées.",
 2: "« La traite des esclaves entre l'Afrique et l'Amérique » : ampleur de la traite atlantique, ports français, navire négrier et traversée (chiffres sourcés en CM2).",
 3: "« La vie des esclaves dans les plantations » : travail forcé dans l'habitation sucrière, le Code noir (1685), les formes de résistance dont le marronnage.",
 4: "« Les échanges commerciaux avec les colonies » : produits des colonies, cargaisons des navires, ports de l'Atlantique et de la Manche, enrichissement de certains ports.",
 5: "Résistances et abolitions (prolongement du thème) : révolte de Saint-Domingue, Toussaint Louverture, 1794, 1802, 1804, 1848 (Victor Schœlcher), loi du 21 mai 2001, journée du 10 mai.",
}
NOTION = {1: "Le commerce triangulaire : continents, trajets, marchandises", 2: "La traite atlantique : ampleur, ports, traversée",
          3: "Les plantations : travail forcé, Code noir, résistances", 4: "Les échanges avec les colonies : produits, ports", 5: "Résistances et abolitions ; mémoire"}
BO = ("> 📘 **Référence officielle du programme** :\n>\n"
      "> - Histoire-géographie, cycle 3 : [Arrêté du 22 avril 2026 — BO n° 22 du 28 mai 2026](https://www.education.gouv.fr/bo/2026/Hebdo22/MENE2608631A) (NOR MENE2608631A) — en CM1 à la rentrée 2026, en CM2 à la rentrée 2027. "
      "Thème « Explorations et conquêtes ».\n")
ENTETE = "_Histoire, cycle 3 — Année A, période 3 — Thème 3 : « Explorations et conquêtes. La traite des esclaves entre l'Afrique et l'Amérique et la vie des esclaves dans les plantations. Les échanges commerciaux avec les colonies. »_\n"
out = []
w = out.append
w("# Les Archives du port\n")
w("**Escape game n°12 d'histoire — CM1 / CM2 — la traite des esclaves entre l'Afrique et l'Amérique, la vie dans les plantations, les échanges avec les colonies, les résistances et les abolitions**  ")
w("60 à 75 minutes · équipes de 3-4 élèves, ou classe entière au TBI · **15 énigmes en CM1, 20 en CM2** · 10 types d'énigmes.\n")
w("> *Dans les Archives d'un port imaginaire de la façade atlantique.* Cette nuit, l'humidité a décollé les pages d'un registre de navire,")
w("> qui se sont mélangées dans cinq salles. Les élèves, enquêtrices et enquêteurs d'archives, passent par la salle des cartes, le cabinet")
w("> des registres, le fonds des colonies, le musée du port et la salle de lecture, avec Inès (archiviste), Malik (historien venu de Dakar),")
w("> Célia (historienne venue de Guadeloupe), Margot (conservatrice) et Théo (élève de l'atelier d'enquête). Les cinq mots referment le registre reconstitué.\n")
w("⚠️ **Sujet sensible.** Les élèves restent des enquêteurs : aucun jeu de rôle d'esclave, aucune image de violence, aucun point « gagné »")
w("grâce au profit de la traite. Vocabulaire : personnes réduites en esclavage, captifs, traite négrière. Le jeu montre aussi les")
w("résistances et les abolitions. Lire le [guide pédagogique](GUIDE-PEDAGOGIQUE.md) (consignes de discussion en classe) avant la séance.\n")
w("| | |\n|---|---|")
w(f"| ▶ **Jouer** | [en ligne]({URL}) · en local : http://127.0.0.1:8000/traite-colonies/ (avec `lancer.bat`) · [version immersive](../immersifs/traite-colonies/) |")
w("| 👨‍🏫 **Tableau de bord** | http://127.0.0.1:8000/traite-colonies/prof.html — mode local uniquement |")
w("| 🎞️ **Médias** | [assets/README.md](assets/README.md) : tous les noms de fichiers attendus (tous facultatifs) |")
w("| 📖 **Guide pédagogique** | [GUIDE-PEDAGOGIQUE.md](GUIDE-PEDAGOGIQUE.md) : programme, déroulés, différenciation, discussion, évaluation |")
w("| ⚠️ **Points à contrôler** | [A-VERIFIER.md](A-VERIFIER.md) |\n")
w("Liens avec les autres jeux : prépare « La Caravelle du capitaine » (n°13) et « Le Testament de l'Empereur » (n°16 : Napoléon rétablit")
w("l'esclavage en 1802) ; se relie à « De l'édit de Nantes à Versailles » (Louis XIV signe le Code noir en 1685).\n\n---\n")
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
w(f"| 📜 | Fin : coffre du registre, dernière page, quizz | | Inès | | 5 questions | [CM1]({URL}?salle=6&niveau=CM1) · [CM2]({URL}?salle=6&niveau=CM2) |\n")
w("Les cinq mots, retapés dans le coffre, referment le registre ; la dernière page affiche :  ")
w("**« Le commerce en TRIANGLE a déporté des millions de CAPTIFS vers les PLANTATIONS et enrichi des PORTS ; par leurs résistances et par la loi, les personnes réduites en esclavage ont obtenu la LIBERTÉ. »**  ")
w("La dernière page rappelle cinq repères (1685, 1791, 1794, 1802, 1848). Pendant les **5 questions de synthèse** (quizz final), chaque bonne réponse appose un sceau sur le registre.\n")
w("Les liens « Tester » ouvrent la salle directement, sans nom d'équipe ; **rien n'est sauvegardé**.")
w("On peut aussi viser une énigme précise : `traite-colonies/?salle=2&niveau=CM2&enigme=4`.\n\n---\n")
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
w("énigme fait manipuler (ordonner, trier, placer sur une carte) : 1-1, 1-3, 2-2, 3-1, 3-3, 4-3, 4-4, 5-1. Le type `instrument` (thermomètre, pluviomètre) n'a pas d'usage en histoire.\n\n---\n")
w(open(os.path.join(R, "tests", "readme-suite.md"), encoding="utf-8").read())
print_ = None
open(os.path.join(R, "README.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("README.md écrit :", sum(len(x) for x in out), "caractères")
