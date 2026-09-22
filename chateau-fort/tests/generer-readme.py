# -*- coding: utf-8 -*-
# Génère chateau-fort/README.md à partir des données JSON (solutions toujours à jour).
# Lancement depuis la racine du dépôt : python chateau-fort/tests/generer-readme.py
import json, sys, re, os
R = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
E = json.load(open(R + "/assets/data/enigmes.json", encoding="utf-8"))
D = json.load(open(R + "/assets/data/dialogues.json", encoding="utf-8"))
URL = "https://idgir.github.io/escape-games-cm1-cm2/chateau-fort/"

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

out = []
w = out.append
w("# Le Secret du donjon\n")
w("**Escape game d'histoire — CM1 / CM2 — le château fort et la vie des paysannes et des paysans au Moyen Âge**  ")
w("60 à 75 minutes · équipes de 3-4 élèves, ou classe entière au TBI · **15 énigmes en CM1, 20 en CM2**.\n")
w("> *Un château fort, un matin d'automne.* Le seigneur est parti rejoindre le roi. Avant de partir, il a confié")
w("> les **cinq clés** de la seigneurie à cinq personnes du domaine. Or un messager du roi arrive avant la nuit :")
w("> si la **herse** reste baissée, il repartira. Les élèves, jeunes pages et jeunes paysans, parcourent le château")
w("> et le village pour retrouver les cinq clés, graver leurs mots dans l'inscription au-dessus de la porte, puis")
w("> relever la herse en répondant aux questions de synthèse.\n")
w("Programme : histoire, CM1 — la vie quotidienne au Moyen Âge. Progression de l'enseignant : **année B, période 1** —")
w("*« Décrire les fonctions d'un château fort (lieu de protection, lieu de vie du seigneur, symbole de la puissance du seigneur).")
w("Raconter la vie quotidienne des paysannes et des paysans. »*\n")
w("| | |\n|---|---|")
w(f"| ▶ **Jouer** | [en ligne]({URL}) · en local : http://127.0.0.1:8000/chateau-fort/ (avec `lancer.bat`) |")
w("| 👨‍🏫 **Tableau de bord** | http://127.0.0.1:8000/chateau-fort/prof.html — mode local uniquement |")
w("| 🔍 **Vérifier** | [page de vérification](https://idgir.github.io/escape-games-cm1-cm2/verifier.html#chateau-fort) : tester chaque énigme, voir les médias |")
w("| 🎞️ **Médias** | [assets/README.md](assets/README.md) : tous les noms de fichiers attendus (tous facultatifs) |")
w("| 📖 **Guide pédagogique** | [GUIDE-PEDAGOGIQUE.md](GUIDE-PEDAGOGIQUE.md) : programme, déroulés, différenciation, évaluation |")
w("| ⚠️ **Points à contrôler** | [A-VERIFIER.md](A-VERIFIER.md) |\n")
w("Liens avec les autres jeux : même période que le jeu n°01 (Moyen Âge, année A : l'Église, l'abbaye) sous un autre angle ;")
w("le calendrier des travaux de la salle 4 prépare le jeu de sciences n°03 (la météo).\n\n---\n")
w("## Les 5 salles\n")
w("| # | Lieu | Notion | Personnage | Mot-clé | Énigmes | Tester |\n|---|---|---|---|---|---|---|")
for s, se in zip(D["salles"], E["salles"]):
    p = D["personnages"][s["dialogue_intro"]["perso"]]["nom"]
    notion = se["titre"].split(" — ", 1)[1]
    w(f"| {s['num']} | {s['titre']} | {notion} | {p} | **{s['motCle']}** | 3 en CM1 · 4 en CM2 | [CM1]({URL}?salle={s['num']}&niveau=CM1) · [CM2]({URL}?salle={s['num']}&niveau=CM2) |")
w(f"| 🏁 | Fin : inscription, herse, quizz | | Dame Aliénor | | 5 questions | [CM1]({URL}?salle=6&niveau=CM1) · [CM2]({URL}?salle=6&niveau=CM2) |\n")
w("Les cinq mots se gravent dans l'inscription au-dessus de la porte :  ")
w("**« Sur la PIERRE s'élèvent les REMPARTS. Le SEIGNEUR protège le VILLAGE ; le village paie les REDEVANCES. »**  ")
w("La herse se relève ensuite quand l'équipe a répondu aux **5 questions de synthèse** (quizz final).\n")
w("Les liens « Tester » ouvrent la salle directement, sans nom d'équipe ; **rien n'est sauvegardé**.")
w("On peut aussi viser une énigme précise : `chateau-fort/?salle=2&niveau=CM2&enigme=4`.\n\n---\n")
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
        w(f"*Correction affichée :* {propre(e['correction'])}  \n*Source :* {e['source']} · *Leçon :* `{e['lecon']}`\n")
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
w("énigme fait manipuler (ordonner, placer sur un plan, trier) : 1-2, 2-1, 3-1, 4-1, 5-3 (et 5-4 en CM2).\n\n---\n")
w("## Score\n")
w("| | CM1 | CM2 |\n|---|---|---|")
w("| Énigmes résolues (5 pts) | 15 × 5 = 75 | 20 × 5 = 100 |")
w("| Bonus de rapidité (3 pts par salle) | 15 | 15 |")
w("| Quizz final de la herse (2 pts × 5) | 10 | 10 |")
w("| **Total maximal** | **100** | **125** |\n")
w("Un indice consulté retire **2 points**. Le bonus de rapidité tombe à 2 points si la salle a demandé un indice, et à 0")
w("au-delà de 8 minutes (CM1) ou 10 minutes (CM2) par salle.\n")
w("**Mentions** : 90 % → Gardien du donjon · 75 % → Chevalier du domaine · 55 % → Écuyer · en dessous → Page en formation.  ")
w("**Badges** : Équipe rapide (une salle en moins de 6 min) · Œil de sentinelle (salle 2 sans indice) · Ami du village")
w("(salle 4 sans indice) · Gardien du donjon (3 indices au maximum sur la partie).\n\n---\n")
w("## Les leçons (bouton « Leçons »)\n")
w("Cinq leçons rédigées, une par salle, de 3 à 4 minutes de lecture, avec un texte CM1 et un texte CM2, des objectifs, un")
w("lexique, un schéma ou une frise, un document et leurs sources en pied de leçon. Chaque énigme ouvre sa leçon par le bouton")
w("« Leçon » (champ `lecon` de `enigmes.json`). L'enseignant peut interdire la consultation (⚙️ Réglages → Séance).\n")
w("| Salle | Leçon (`id`) | Schéma ou frise |\n|---|---|---|")
L = json.load(open(R + "/assets/data/lecons.json", encoding="utf-8"))["lecons"]
for l in L:
    extra = " + ".join(x for x in [("schéma SVG" if l.get("schema") else ""), ("frise" if l.get("frise") else "")] if x)
    w(f"| {l['salle']} | {l['titre']} (`{l['id']}`) | {extra} |")
w("\n---\n")
w("## Modifier le contenu\n")
w("| Pour changer… | Fichier |\n|---|---|")
w("| les énigmes : questions, réponses, indices, corrections | `assets/data/enigmes.json` |")
w("| les dialogues, les lieux, les mots-clés | `assets/data/dialogues.json` |")
w("| les leçons | `assets/data/lecons.json` |")
w("| les évaluations imprimables et le quizz final | `assets/data/evaluations.json` |")
w("| les décors dessinés | `js/decors.js` |")
w("| les personnages dessinés | `js/personnages.js` |\n")
w("**Aucune énigme n'est écrite en dur** : le moteur `js/enigmes.js` est celui de `constitution/`, dans la version déjà reprise par `moyen-age-abbaye/` (bouton « Leçon », source affichée dans la correction) ; aucun type d'énigme n'a été ajouté.")
w("Après une modification d'un fichier `js/` ou `css/`, augmentez son numéro de version dans `index.html` (`app.js?v1` → `app.js?v2`).\n")
w("```\nchateau-fort/\n├── index.html · prof.html\n├── README.md · GUIDE-PEDAGOGIQUE.md · A-VERIFIER.md\n├── assets/\n│   ├── data/      enigmes.json, dialogues.json, lecons.json, evaluations.json\n│   ├── videos/    décors et cinématiques (+ personnages/) — facultatif\n│   └── images/    decors/, personnages/, cartes/, documents/ — facultatif\n├── css/           style, enigmes, video, animations, personnages, impression\n└── js/            app, enigmes (les 10 types), decors, personnages, media,\n                   narration, audio, lecons, impression, api, sync, reglages\n```\n\n---\n")
w("## Tests automatiques\n")
w("Depuis la racine du dépôt (Invite de commandes) :\n")
w("```\npython chateau-fort/tests/test_json.py\nnpm install jsdom@26\nnode chateau-fort/tests/test-chateau-fort.js\n```\n")
w("`test_json.py` contrôle les données (JSON valides, clés uniques, liens énigme → leçon, règles du cahier des charges, absence d'emoji).")
w("`test-chateau-fort.js` joue les parties complètes CM1 et CM2 (scores 100 et 125), teste les mauvaises réponses, les indices, les leçons,")
w("le mode vérification, les réglages, les impressions et `verifier.html`. `generer-readme.py` régénère ce README à partir des données.\n\n---\n")
w("## Sources\n")
w("- Programme d'histoire-géographie du cycle 3, publié au Bulletin officiel du 28 mai 2026, en vigueur en CM1 à la rentrée 2026 — [Eduscol, cycle 3](https://eduscol.education.gouv.fr/4356/enseigner-au-cycle-3) ; projet du CSP, juin 2025 : [education.gouv.fr](https://www.education.gouv.fr/media/228384/download).")
w("- Progression de l'enseignant : `programmation histoire-géo sciences 2026.pdf` (racine du dépôt), année B, période 1.")
w("- Académie de Nice, fiche « Le château fort » (définitions et datations des éléments du château) : [pedagogie.ac-nice.fr](https://www.pedagogie.ac-nice.fr/dsden06/eac/wp-content/uploads/sites/5/2018/04/Le-chateau-fort.pdf).")
w("- Chantier médiéval de Guédelon (Treigny, Yonne), commencé en 1997, château d'inspiration « philippienne » du XIIIe siècle : [guedelon.fr](https://www.guedelon.fr/) ; [Décoder les églises et les châteaux](https://decoder-eglises-chateaux.fr/guedelon-batir-chateau-fort-xxie-siecle/).")
w("- Cité de l'architecture et du patrimoine : [citedelarchitecture.fr](https://www.citedelarchitecture.fr/).")
w("- *Les Très Riches Heures du duc de Berry*, commencées vers 1411 par les frères Limbourg, conservées au château de Chantilly (musée Condé, Ms 65) — et non à la BnF : [bibliotheque-conde.fr](https://www.bibliotheque-conde.fr/les-tres-riches-heures) ; calendrier mois par mois : [Wikipédia](https://fr.wikipedia.org/wiki/Les_Tr%C3%A8s_Riches_Heures_du_duc_de_Berry).")
w("- Larousse, article « donjon » (étymologie *dominus*) : [larousse.fr](https://www.larousse.fr/encyclopedie/divers/donjon/44419).")
w("- Vikidia, « Vie des paysans au Moyen Âge » et « Banalité (droit seigneurial) » : [fr.vikidia.org](https://fr.vikidia.org/wiki/Vie_des_paysans_au_Moyen_%C3%82ge).")
w("- Lumni (vidéos et dossiers « château fort », « paysans au Moyen Âge ») : [lumni.fr](https://www.lumni.fr/) ; L'Histoire par l'image : [histoire-image.org](https://histoire-image.org/).")
open(R + "/README.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("README OK", len(out))
