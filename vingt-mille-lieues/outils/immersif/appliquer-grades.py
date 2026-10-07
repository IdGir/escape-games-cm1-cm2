#!/usr/bin/env python3
"""Complète une variante immersive avec les 5 grades, l'identité du jeu (noms de grades, palette) et les voix.

    python vingt-mille-lieues/outils/immersif/appliquer-grades.py <jeu>

Lit outils/immersif/grades/<jeu>_s1.py … _s5.py (blocs mousse, lieutenant, second de chaque énigme ; fonction donnees(svg, bloc))
et <jeu>_theme.py (NOMS, PALETTE, VOIX, GUIDES), puis :
  - ajoute les blocs mousse / lieutenant / second à immersifs/<jeu>/assets/data/enigmes.json (le dialogue est repris du grade voisin) ;
  - réserve la 4e énigme de chaque salle aux grades timonier, lieutenant, second (mousse et matelot : 15 énigmes) ;
  - un seul personnage guide par salle (il parle pour toutes ses énigmes) ;
  - écrit les noms de grades (enigmes.json, js/jeu-config.js), la palette (css/theme.css) et les voix (personnages.json) ;
  - contrôle : phrases de justification présentes mot pour mot dans la fiche, types jamais identiques deux fois de suite à un grade,
    au moins une manipulation (ordre, plan, tri) par salle et par grade.
Après : python immersifs/<jeu>/outils/embarquer-donnees.py puis node immersifs/<jeu>/tests/test-immersif.js
"""
import importlib, json, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.abspath(os.path.join(ICI, "..", "..", ".."))
sys.path.insert(0, os.path.join(ICI, "grades"))
GRADES = ["mousse", "matelot", "timonier", "lieutenant", "second"]
MANIP = {"ordre", "plan", "tri"}
# Phrase du personnage pour un grade ajouté (neutre : elle ne décrit ni le nombre ni le détail de la tâche).
DIALOGUES = {
    "qcm": "J'ai quelques questions pour vous. Lisez bien le document avant de répondre.",
    "vraifaux": "Voici mes affirmations. À vous de dire lesquelles sont vraies.",
    "ordre": "Mes étapes sont mélangées. Remettez-les dans le bon ordre.",
    "tri": "Il faut tout ranger. Placez chaque carte dans la bonne colonne.",
    "association": "Il faut relier chaque élément à ce qui lui correspond.",
    "trous": "Il manque des mots dans mon carnet. Remettez-les à leur place.",
    "lettres": "Un mot est caché dans mon texte. Retrouvez-le.",
    "code": "Ce cadenas ne s'ouvre qu'avec le bon code. Lisez bien le document.",
    "plan": "Voici mon schéma. Placez chaque étiquette au bon endroit.",
    "intrus": "Un de ces éléments n'est pas comme les autres. Trouvez-le.",
}


def texte(h):
    h = re.sub(r"</?(b|i|em|strong|span|u|sub|sup)(\s[^>]*)?>", "", h or "")          # balises en ligne : pas d'espace ajouté
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()


def main(jeu):
    dest = os.path.join(RACINE, "immersifs", jeu)
    data = os.path.join(dest, "assets", "data")
    lire = lambda n: json.load(open(os.path.join(data, n), encoding="utf-8"))
    E, L, P, DL = lire("enigmes.json"), lire("lecons.json"), lire("personnages.json"), lire("dialogues.json")
    mod = jeu.replace("-", "_")
    theme = importlib.import_module(mod + "_theme")
    fiches = {l["id"]: texte(" ".join(str(l.get(k, "")) for k in ("essentiel", "approfondi", "expert"))) for l in L["lecons"]}
    par_id = {e["id"]: e for s in E["escales"] for e in s["enigmes"]}
    svg = lambda qid, g: __import__("aide").svg_de(par_id[qid], g)
    bloc = lambda qid, g: par_id[qid][g]

    nouveaux = {}
    n = 1
    while True:
        try:
            m = importlib.import_module(f"{mod}_s{n}")
        except ModuleNotFoundError:
            break
        nouveaux.update(m.donnees(svg, bloc))
        n += 1
    erreurs = []
    # --- 1. blocs de grade
    for s in E["escales"]:
        guide = theme.GUIDES[s["numero"]]
        for e in s["enigmes"]:
            e["personnage_emetteur"] = guide
            nv = nouveaux.get(e["id"])
            if not nv:
                erreurs.append(f"{e['id']} : aucun grade écrit")
                continue
            for g, b in nv.items():
                voisin = {"mousse": "matelot", "lieutenant": "timonier", "second": "timonier"}[g]
                base = e.get(voisin) or e.get("timonier") or e.get("matelot")
                b["dialogue"] = base["dialogue"] if e["ordre"] == 1 else DIALOGUES[b["type"]]
                e[g] = b
                if b["type"] == "lettres":
                    marq = re.findall(r"data-l='(.)'", b["texte"])
                    reste = list(marq)
                    for c in b["cible"]:
                        if c in reste:
                            reste.remove(c)
                        else:
                            erreurs.append(f"{e['id']} {g} : la lettre {c} n'est pas cachée dans le texte")
                    if len(reste) < 2:
                        erreurs.append(f"{e['id']} {g} : au moins deux lettres pièges sont nécessaires (il y en a {len(reste)})")
                    if "".join(marq[:len(b["cible"])]) == "".join(b["cible"]):
                        erreurs.append(f"{e['id']} {g} : les lettres sont dans l'ordre du mot (elles doivent être dans le désordre)")
                j = b.get("justification")
                if j:
                    ok = j["options"][j["bonne"]]
                    if texte(ok) not in fiches[e["lecon"]]:
                        erreurs.append(f"{e['id']} {g} : la phrase de justification n'est pas dans la fiche « {e['lecon']} » : {ok[:70]}")
                    if len(set(j["options"])) != len(j["options"]):
                        erreurs.append(f"{e['id']} {g} : options de justification en double")
            extra = e.get("niveaux") in (["timonier"], ["timonier", "lieutenant", "second"])      # énigme réservée au CM2 dans le jeu d'origine
            if extra:
                e["niveaux"] = ["timonier", "lieutenant", "second"]
                for g in ("mousse", "matelot"):
                    e.pop(g, None)
            else:
                e.pop("niveaux", None)
            if e["id"] in nouveaux and not extra:
                missing = [g for g in GRADES if g not in e]
                if missing:
                    erreurs.append(f"{e['id']} : grades manquants {missing}")
            ty = {g: (e[g].get("type") or e["type"]) for g in GRADES if g in e}
            e["niveau_variantes"] = " ; ".join(f"{theme.NOMS[g]['nom']} ({ty[g]})" for g in GRADES if g in ty) + ". Mousse : indices renvoyant à la fiche, énoncés courts ; lieutenant et second : justification par une phrase de la fiche."
        # contrôles de variété, par grade
        for g in GRADES:
            es = [e for e in s["enigmes"] if g in e and (not e.get("niveaux") or g in e["niveaux"])]
            types = [e[g].get("type") or e["type"] for e in es]
            if any(a == b for a, b in zip(types, types[1:])):
                erreurs.append(f"salle {s['numero']} {g} : deux types identiques de suite {types}")
            if not MANIP & set(types):
                erreurs.append(f"salle {s['numero']} {g} : aucune manipulation (ordre, plan, tri) {types}")
            if len(es) < 3:
                erreurs.append(f"salle {s['numero']} {g} : moins de 3 énigmes")
    # --- 2. grades, noms
    E["niveaux"] = [dict(id=g, **theme.NOMS[g]) for g in GRADES]
    E.pop("_commentaire", None)
    # --- 3. voix et guides
    for pid, v in theme.VOIX.items():
        if pid not in P["personnages"]:
            erreurs.append(f"personnage inconnu pour la voix : {pid}")
        else:
            P["personnages"][pid]["voix"] = v
    for pid, q in getattr(theme, "PORTRAITS", {}).items():
        if pid in P["personnages"]:
            P["personnages"][pid]["portrait"] = q
    manque = [k for k in P["personnages"] if not P["personnages"][k].get("voix", {}).get("edge")]
    if manque:
        erreurs.append(f"personnages sans voix Edge : {manque}")
    if len({v['edge'] for v in theme.VOIX.values()}) != len(theme.VOIX):
        erreurs.append("deux personnages ont la même voix")
    for k, c in DL["cinematiques"].items():
        num = int(re.search(r"e(\d+)$", k).group(1)) if re.search(r"e(\d+)$", k) else None
        if num:
            for p in c["plans"]:
                if p.get("personnage"):
                    p["personnage"] = theme.GUIDES[num]
    for k, f in DL["fin_escale"].items():
        f["personnage"] = theme.GUIDES[int(k)]
    if erreurs:
        print("\n".join("✖ " + x for x in erreurs))
        sys.exit(1)
    # --- 4. écriture
    ecr = lambda n, o: json.dump(o, open(os.path.join(data, n), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    ecr("enigmes.json", E); ecr("personnages.json", P); ecr("dialogues.json", DL)
    cfg_p = os.path.join(dest, "js", "jeu-config.js")
    s = open(cfg_p, encoding="utf-8").read()
    m = re.search(r"window\.VML_JEU = (\{[\s\S]*\});", s)
    cfg = json.loads(m.group(1))
    cfg["grades"] = list(GRADES)
    open(cfg_p, "w", encoding="utf-8", newline="\n").write(s[:m.start(1)] + json.dumps(cfg, ensure_ascii=False, indent=2) + s[m.end(1):])
    css = "/* Charte graphique du jeu (surcharge les variables de css/nautilus.css) — générée par outils/immersif/appliquer-grades.py. */\n:root{\n" + \
          "".join(f"  {k}: {v};\n" for k, v in theme.PALETTE.items()) + "}\n"
    open(os.path.join(dest, "css", "theme.css"), "w", encoding="utf-8", newline="\n").write(css)
    nb = {g: sum(1 for s_ in E["escales"] for e in s_["enigmes"] if g in e) for g in GRADES}
    print(f"{jeu} : grades écrits ; énigmes par grade {nb} ; noms : " + ", ".join(theme.NOMS[g]["nom"] for g in GRADES))


if __name__ == "__main__":
    main(sys.argv[1])
