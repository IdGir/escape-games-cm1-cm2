#!/usr/bin/env python3
"""Migrateur « jeu d'origine → modèle immersif » (celui de « Vingt mille lieues sous les mers »).

Principe : NON DESTRUCTIF. Le jeu d'origine n'est jamais modifié ; une variante immersive complète est écrite dans
immersifs/<jeu>/ (moteur copié, données converties, brouillon des zones et des cinématiques, plan de production des médias,
tests, rapport des choses à compléter). L'enseignant compare, complète, puis (s'il le souhaite) remplace le jeu d'origine :
voir GUIDE-IMMERSIF.md (le garde-fou outils-tests/verifier-isolation.sh exige alors --autoriser <jeu>).

Ce qui est converti automatiquement : salles → étapes (« escales »), énigmes, consignes, indices, données de chaque type,
leçons, personnages, dialogues d'introduction et de réussite, mots-clés du coffre, grades (CM1 → matelot, CM2 → timonier par défaut).
Ce qui reste un BROUILLON (listé dans MIGRATION-RAPPORT.md) : zones cliquables des décors, enjeu et réaction du décor de chaque
énigme, phrases des personnages pour les énigmes suivantes, images et vidéos (à produire avec outils/medias/).

Usage :
  python vingt-mille-lieues/outils/immersif/migrer-jeu.py renaissance
  python vingt-mille-lieues/outils/immersif/migrer-jeu.py versailles --theme mon-theme.json --vers immersifs/versailles
  python vingt-mille-lieues/outils/immersif/migrer-jeu.py --lister          (jeux migrables)
Options : --theme <json> (surcharges du thème), --grades cm1:matelot,cm2:timonier,cm1:mousse (correspondances), --force (écrase la sortie).
"""
import argparse, csv, io, json, os, re, shutil, subprocess, sys, unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
MODELE = os.path.dirname(os.path.dirname(ICI))                    # vingt-mille-lieues/ (le moteur sert de modèle)
RACINE = os.path.dirname(MODELE)                                  # racine du dépôt
GRADES_ORDRE = ["mousse", "matelot", "timonier", "lieutenant", "second"]

ZONES = [(6, 14, 26, 34), (37, 10, 26, 34), (68, 14, 26, 34), (37, 48, 26, 26)]   # x, y, w, h (en % de l'image), hors plaque de dialogue
VOIX = [(0.95, 1.0), (1.0, 1.15), (0.9, 0.9), (1.05, 1.2), (0.92, 1.05), (1.0, 0.85)]


def sans_html(t):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", str(t or ""))).strip()


def slug(t):
    t = unicodedata.normalize("NFKD", str(t)).encode("ascii", "ignore").decode()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", t.lower())).strip("-") or "x"


def lire(chemin):
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def ecrire(chemin, d):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")


def par_niveau(v, niv):
    """Champ différencié : chaîne, liste, ou {cm1, cm2, commun}."""
    if isinstance(v, dict) and any(k in v for k in ("cm1", "cm2", "commun")):
        return v.get(niv) or v.get("commun") or v.get("cm2") or v.get("cm1")
    return v


def fusion(base, sur):
    for k, v in (sur or {}).items():
        if isinstance(v, dict) and isinstance(base.get(k), dict):
            fusion(base[k], v)
        else:
            base[k] = v
    return base


def jeux_migrables():
    res = []
    for d in sorted(os.listdir(RACINE)):
        e, dl = (os.path.join(RACINE, d, "assets", "data", f) for f in ("enigmes.json", "dialogues.json"))
        if os.path.isfile(e) and os.path.isfile(dl):
            try:
                if "salles" in lire(e) and "salles" in lire(dl):
                    res.append(d)
            except Exception:
                pass
    return res


# ---------------------------------------------------------------- conversion des données
def convertir(src, theme, correspondances, rapport):
    E, DL = lire(os.path.join(src, "assets/data/enigmes.json")), lire(os.path.join(src, "assets/data/dialogues.json"))
    LC = lire(os.path.join(src, "assets/data/lecons.json")) if os.path.isfile(os.path.join(src, "assets/data/lecons.json")) else {"lecons": []}
    meta = E.get("metadata", {}) or {}
    titre_jeu = meta.get("jeu") or DL.get("metadata", {}).get("jeu") or os.path.basename(src)
    mot_salle = theme["mots"]["escale"]
    persos_src = DL.get("personnages", {}) or {}
    pids = list(persos_src.keys())
    if not pids:
        raise SystemExit("Aucun personnage dans dialogues.json : migration impossible.")
    # grades cibles, dans l'ordre canonique
    cibles = sorted({g for _, g in correspondances}, key=GRADES_ORDRE.index)
    for g in cibles:
        if g in ("lieutenant", "second"):
            rapport["avertissements"].append(f"Le grade « {g} » demande une justification à rédiger pour chaque énigme (non fournie par le jeu d'origine).")

    # --- personnages
    persos = {}
    for i, (pid, p) in enumerate(persos_src.items()):
        rate, pitch = VOIX[i % len(VOIX)]
        nom = p.get("nom", pid)
        persos[pid] = {"nom": nom, "court": nom.split()[-1] if nom.lower().startswith(("maître", "dame", "docteur", "le ", "la ")) else nom.split()[0],
                       "voix": {"rate": rate, "pitch": pitch}, "ton": "à préciser",
                       "fiche": p.get("role") or p.get("fiche") or "personnage du jeu", "portrait": {}}
    # --- escales, énigmes, décors
    escales, fx, lecons_ids = [], {}, set()
    cin, fin_escale = {}, {}
    salles_d = {int(s["num"]): s for s in DL["salles"]}
    for s in E["salles"]:
        n = int(s["num"])
        sd = salles_d.get(n, {})
        decor = slug(sd.get("decor") or f"decor-{n}")
        guide = (sd.get("dialogue_intro") or {}).get("perso") or pids[(n - 1) % len(pids)]
        if guide not in persos:
            guide = pids[(n - 1) % len(pids)]
        enigmes = []
        zones, zid = [], []
        for k, e in enumerate(s["enigmes"], 1):
            x, y, w, h = ZONES[(k - 1) % len(ZONES)]
            z = f"objet-{k}"
            zid.append(z)
            zones.append({"id": z, "libelle": f"À examiner : {sans_html(e['titre'])[:42]}", "x": x, "y": y, "w": w, "h": h,
                          "description": f"Un objet de la {mot_salle} en rapport avec « {sans_html(e['titre'])} »."})
        for k, e in enumerate(s["enigmes"], 1):
            emetteur = guide if k == 1 else pids[(pids.index(guide) + k - 1) % len(pids)]
            new = {
                "id": f"e{n}-{k}", "escale": n, "ordre": k, "titre": sans_html(e["titre"]),
                "decor": decor, "objet_principal": zid[k - 1], "objets_cliquables": list(zid),
                "personnage_emetteur": emetteur,
                "probleme_narratif": sans_html(f"{sd.get('lieu', '')}. {sd.get('description', '')}").strip(". ") + ". À reformuler pour cette énigme.",
                "enjeu": "À préciser : ce qui se passe si l'énigme n'est pas résolue.",
                "episode_du_roman": sans_html(e.get("source", ""))[:140] or meta.get("jeu", titre_jeu),
                "competence_programme": sans_html((next((l for l in LC["lecons"] if l.get("id") == e.get("lecon")), {}) .get("objectifs") or [e["titre"]])[0]),
                "pourquoi_ce_savoir_ici": f"La {mot_salle} « {sans_html(s.get('titre', ''))} » repose sur cette notion.",
                "reaction_du_decor": {"effet": theme["effets_reaction"][(n + k) % len(theme["effets_reaction"])], "description": "À décrire : ce que le décor montre quand l'énigme est résolue."},
                "liberte_ou_anachronisme": "Aucune liberté particulière signalée (jeu migré).",
                "lecon": e.get("lecon", ""), "type": e["type"],
                "niveau_variantes": "Données du jeu d'origine (CM1 / CM2).",
                "correction_origine": e.get("correction", ""),
                "_brouillon": ["zones", "enjeu", "reaction_du_decor", "dialogues", "probleme_narratif"],
            }
            if e.get("niveaux"):
                voulus = sorted({g for old, g in correspondances if old.upper() in [str(x).upper() for x in e["niveaux"]]}, key=GRADES_ORDRE.index)
                new["niveaux"] = voulus
            for old, g in correspondances:
                if new.get("niveaux") and g not in new["niveaux"]:
                    continue
                donnees = e.get(old) or e.get("commun") or e.get("cm2") or e.get("cm1") or {}
                bloc = dict(donnees)
                bloc["consigne"] = par_niveau(e.get("consigne"), old) or ""
                ind = par_niveau(e.get("indices"), old) or []
                bloc["indices"] = list(ind) if isinstance(ind, list) else [str(ind)]
                intro = (sd.get("dialogue_intro") or {}).get("texte", "") if k == 1 else ""
                bloc["dialogue"] = sans_html(intro) or f"Voici la suite : {new['titre']}. Observez bien l'objet qui brille dans la {mot_salle}."
                new[g] = bloc
            enigmes.append(new)
            lecons_ids.add(e.get("lecon"))
        mot = sd.get("motCle") or s.get("motCle") or f"MOT{n}"
        escales.append({
            "numero": n, "id": slug(s.get("titre", f"{mot_salle}-{n}")), "titre": sans_html(sd.get("titre") or s.get("titre") or f"{mot_salle} {n}"),
            "lieu": sans_html(sd.get("lieu", "")), "matiere": "", "periode_conseillee": "",
            "episode": sans_html(sd.get("description", "")), "scenarimage": "", "mot": mot, "mot_origine": f"Le mot-clé de la {mot_salle} {n}.",
            "air": None, "cinematique_ouverture": f"transition-e{n}", "cinematique_fin": f"fin-e{n}", "etats_decor": [], "enigmes": enigmes})
        fx[decor] = {"titre": sans_html(sd.get("lieu") or sd.get("titre") or decor), "reference": None, "ambiance": theme["ambiances"], "kenBurns": {"echelle": 1.05, "duree": 32},
                     "effets": [{"type": "poussiere", "x": 0, "y": 0, "w": 100, "h": 100, "nombre": 24}, {"type": "vignette", "force": 0.5}, {"type": "grain", "force": 0.04}],
                     "zones": zones, "etats": {"normal": {"filtre": "none"}}, "_brouillon": "zones à caler sur l'image (outils/caler-effets.html)"}
        txt_intro = sans_html((sd.get("dialogue_intro") or {}).get("texte", "")) or sans_html(sd.get("description", ""))
        cin[f"transition-e{n}"] = {"titre": f"{mot_salle.capitalize()} {n} — {escales[-1]['titre']}",
                                   "plans": [{"decor": decor, "etat": "normal", "duree": 8, "personnage": guide, "texte": txt_intro[:420], "mouvement": "zoom"}]}
        reussite = sd.get("dialogue_reussite") or sd.get("dialogue_fin") or {}
        cin[f"fin-e{n}"] = {"titre": f"Fin de la {mot_salle} {n}",
                            "plans": [{"decor": decor, "etat": "normal", "duree": 7, "personnage": reussite.get("perso") if reussite.get("perso") in persos else guide,
                                       "texte": sans_html(reussite.get("texte", "")) or f"Bien joué : vous avez trouvé le mot de la {mot_salle}.", "mouvement": "glisse"}]}
        fin_escale[str(n)] = {"personnage": guide, "texte": f"Notez le mot de cette {mot_salle} : il servira à ouvrir le coffre final."}
    derniere = escales[-1]
    cin["fin"] = {"titre": f"Fin de « {titre_jeu} »", "plans": [{"decor": derniere["enigmes"][0]["decor"], "etat": "normal", "duree": 7, "personnage": derniere["enigmes"][0]["personnage_emetteur"],
                                                              "texte": "Le coffre est ouvert : toutes les pages sont rassemblées. Bravo, équipe !", "mouvement": "zoom"}]}
    dialogues = {"_commentaire": "Brouillon généré par le migrateur : reformuler dans le ton de chaque personnage.",
                 "accueil": {"personnage": pids[0], "texte": sans_html(DL.get("intro_accueil", "")) or f"Bienvenue dans « {titre_jeu} »."},
                 "coffre": {"personnage": pids[0], "texte": f"Le coffre ne s'ouvre qu'avec les mots de chaque {mot_salle}, dans l'ordre. Vous les avez notés, j'espère."},
                 "cinematiques": cin, "fin_escale": fin_escale}
    # --- leçons
    rayons = [{"id": "lecons", "titre": "Rayon des leçons", "icone": "📖"}]
    lecons = []
    for i, l in enumerate(LC["lecons"], 1):
        c = l.get("contenu") or {}
        if isinstance(c, str):
            c = {"cm1": c, "cm2": c}
        lex = "".join(f"<tr><td><b>{x.get('mot', '')}</b></td><td>{x.get('def', '')}</td></tr>" for x in (l.get("lexique") or []))
        fr = "".join(f"<tr><td>{x.get('date', '')}</td><td>{x.get('evt', '')}</td></tr>" for x in (l.get("frise") or []))
        doc = l.get("document") or {}
        lecons.append({
            "id": l["id"], "rayon": "lecons", "fiche": i, "icone": "📖", "titre": l.get("titre", l["id"]), "escale": int(l.get("salle") or 1),
            "competence": " ; ".join(l.get("objectifs") or []),
            "essentiel": par_niveau(c, "cm1") or "",
            "approfondi": (par_niveau(c, "cm2") or "") + (f"<table class='tab-lecon'><tr><th>Mot</th><th>Définition</th></tr>{lex}</table>" if lex else "")
                          + (f"<h4>{l.get('frise_titre', 'Frise')}</h4><table class='tab-lecon'>{fr}</table>" if fr else ""),
            "expert": (f"<div class='encadre'><b>{doc.get('titre', '')}</b> — {doc.get('contenu', '')} <i>{doc.get('source', '')}</i></div>" if isinstance(doc, dict) and doc.get("contenu") else ""),
            "dans_le_roman": f"Voir la {mot_salle} {int(l.get('salle') or 1)}."})
    manquantes = sorted(x for x in lecons_ids if x and x not in {l["id"] for l in lecons})
    if manquantes:
        rapport["avertissements"].append("Leçons citées par des énigmes mais absentes de lecons.json : " + ", ".join(manquantes))
    niveaux = [dict(id=g, **theme["noms_grades"][g]) for g in cibles]
    enigmes = {"_commentaire": f"Généré par outils/immersif/migrer-jeu.py depuis « {os.path.basename(src)} ». À compléter : voir MIGRATION-RAPPORT.md.",
               "version": 1, "niveaux": niveaux, "escales": escales}
    return {"titre": titre_jeu, "enigmes": enigmes, "lecons": {"rayons": rayons, "lecons": lecons}, "fx": {"decors": fx}, "dialogues": dialogues,
            "personnages": {"personnages": persos}, "grades": cibles, "meta": meta}


# ---------------------------------------------------------------- copie du moteur
EXCLURE_DOSSIERS = {"assets", "references", "captures", "sources", "scenarimages", "outils", "tests", "node_modules", "medias-proposes"}
EXCLURE_FICHIERS = {"medias.csv", "PRODUCTION-MEDIAS.md", "ISOLATION-SORTIE.txt", "README.md", "GUIDE-PEDAGOGIQUE.md", "COHERENCE.md", "A-VERIFIER.md",
                    "CHANGELOG.md", "PLAN.md", "BASELINE-TESTS.md", "INTEGRATION.md", "ESSAYER.md", "GUIDE-IMMERSIF.md", "GUIDE-MEDIAS.md", "lancer-nautilus.bat"}
EXCLURE_JS = {"donnees-embarquees.js", "decors-secours.js", "jeu-config.js"}


def profondeur_de(dest):
    """Nombre de dossiers entre la racine du dépôt et la sortie (immersifs/<jeu> → 2) : les liens vers commun/ en dépendent."""
    rel = os.path.relpath(os.path.abspath(dest), RACINE)
    return 2 if rel.startswith("..") else len(rel.split(os.sep))


def copier_moteur(dest, slug_jeu):
    prof = profondeur_de(dest)
    for racine, dossiers, fichiers in os.walk(MODELE):
        rel = os.path.relpath(racine, MODELE)
        top = rel.split(os.sep)[0]
        if top in EXCLURE_DOSSIERS:
            dossiers[:] = []
            continue
        for f in fichiers:
            if f in EXCLURE_FICHIERS or (rel == "js" and f in EXCLURE_JS):
                continue
            cible = os.path.join(dest, rel, f) if rel != "." else os.path.join(dest, f)
            os.makedirs(os.path.dirname(cible), exist_ok=True)
            shutil.copy2(os.path.join(racine, f), cible)
    # chemins vers commun/ : un dossier plus profond
    for rel in ("index.html", "prof.html", "medias.html", "lecons-imprimables.html", "sw.js"):
        p = os.path.join(dest, rel)
        s = open(p, encoding="utf-8").read().replace("../commun/", "../" * prof + "commun/")
        open(p, "w", encoding="utf-8", newline="\n").write(s)
    for f in os.listdir(os.path.join(dest, "css")):
        if f.endswith(".css"):
            p = os.path.join(dest, "css", f)
            s = open(p, encoding="utf-8").read().replace("../../commun/", "../" * (prof + 1) + "commun/")
            open(p, "w", encoding="utf-8", newline="\n").write(s)
    # fichiers statiques propres au jeu
    os.makedirs(os.path.join(dest, "assets/images/ui"), exist_ok=True)
    if os.path.isfile(os.path.join(MODELE, "assets/images/ui/icone.svg")):
        shutil.copy2(os.path.join(MODELE, "assets/images/ui/icone.svg"), os.path.join(dest, "assets/images/ui/icone.svg"))
    for d in ("images/decors", "images/personnages", "videos", "medias-depart", "data"):
        os.makedirs(os.path.join(dest, "assets", d), exist_ok=True)
    open(os.path.join(dest, "js/decors-secours.js"), "w", encoding="utf-8").write(
        "/* Décors dessinés de secours : aucun pour ce jeu (le moteur dessine un décor générique, VML.svgGenerique, tant qu'aucune image n'est déposée\n"
        "   dans assets/images/decors/<id>.webp). Ajouter ici des SVG propres au jeu si besoin : VML.SVG_DECORS.<id> = () => `<svg…>`. */\n"
        "var VML = window.VML || (window.VML = {});\nVML.SVG_DECORS = VML.SVG_DECORS || {};\n")
    # outils embarqués
    os.makedirs(os.path.join(dest, "outils"), exist_ok=True)
    for f in ("embarquer-donnees.py", "caler-effets.html", "choisir-medias.html"):
        if os.path.isfile(os.path.join(MODELE, "outils", f)):
            shutil.copy2(os.path.join(MODELE, "outils", f), os.path.join(dest, "outils", f))
    if os.path.isdir(os.path.join(MODELE, "outils", "medias")):
        shutil.copytree(os.path.join(MODELE, "outils", "medias"), os.path.join(dest, "outils", "medias"), dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    os.makedirs(os.path.join(dest, "tests"), exist_ok=True)
    for f in ("test-immersif.js", "solveurs.js"):
        if os.path.isfile(os.path.join(MODELE, "tests", f)):
            s = open(os.path.join(MODELE, "tests", f), encoding="utf-8").read()
            s = s.replace('path.resolve(__dirname, "../../outils-tests")', 'path.resolve(__dirname, "' + "../" * (prof + 1) + 'outils-tests")').replace('"../../outils-tests/charge"', '"' + "../" * (prof + 1) + 'outils-tests/charge"')
            open(os.path.join(dest, "tests", f), "w", encoding="utf-8", newline="\n").write(s)


def ecrire_sw(dest, slug_jeu):
    """Service worker : cache propre à ce jeu, liste réduite aux fichiers existants (à appeler en DERNIER)."""
    p = os.path.join(dest, "sw.js")
    s = open(p, encoding="utf-8").read()
    s = re.sub(r'"vml-[a-z0-9-]*"', f'"vml-{slug_jeu}-1"', s, count=1).replace('startsWith("vml-")', f'startsWith("vml-{slug_jeu}-")')
    s = s.replace("« Le Journal du Nautilus »", f"« {slug_jeu} »").replace("vingt-mille-lieues/ uniquement", f"immersifs/{slug_jeu}/ uniquement")
    m = re.search(r"const FICHIERS = \[([\s\S]*?)\];", s)
    liste = json.loads("[" + m.group(1).replace("'", '"') + "]")
    liste = [f for f in liste if f == "./" or f.startswith("../") or os.path.exists(os.path.join(dest, f))]
    liste = [f if not f.startswith("../") or os.path.exists(os.path.normpath(os.path.join(dest, f))) else None for f in liste]
    liste = [f for f in liste if f]
    s = s[:m.start(1)] + "\n  " + ", ".join(json.dumps(f) for f in liste) + "\n" + s[m.end(1):]
    open(p, "w", encoding="utf-8", newline="\n").write(s)




def adapter_html(dest, textes, titre):
    """Remplace les titres « Nautilus » en dur des pages statiques par ceux du jeu (le moteur les relit aussi au chargement)."""
    par_defaut = {"Le Journal du Nautilus": textes["journal"], "La Bibliothèque du Nautilus": textes["bibliotheque"], "Bibliothèque du Nautilus": textes["bibliotheque"].replace("La ", "", 1),
                  "Le Nautilus est stoppé": textes["pause"].replace("⏸ ", ""), "Vingt mille lieues sous les mers": textes["titre"], "Jules Verne": textes["auteur"]}
    for f in ("index.html", "prof.html", "medias.html", "lecons-imprimables.html"):
        p = os.path.join(dest, f)
        h = open(p, encoding="utf-8").read()
        h = re.sub(r'(data-t="([A-Za-z]+)"[^>]*>)([^<]*)(<)', lambda m: m.group(1) + (textes.get(m.group(2)) or m.group(3)) + m.group(4), h)
        for a, b in par_defaut.items():
            h = h.replace(a, b)
        h = h.replace("⚓ ", "").replace("d'après Jules Verne", "")
        open(p, "w", encoding="utf-8", newline="\n").write(h)
    p = os.path.join(dest, "manifest.webmanifest")
    if os.path.isfile(p):
        h = open(p, encoding="utf-8").read().replace("Le Journal du Nautilus — Vingt mille lieues sous les mers", titre)
        open(p, "w", encoding="utf-8", newline="\n").write(h)


def ecrire_theme(dest, theme):
    pal = theme.get("palette") or {}
    css = "/* Thème généré par le migrateur (outils/immersif/theme-defaut.json → \"palette\"). */\n"
    if pal:
        css += ":root{ " + " ".join(f"--{k.lstrip('-')}: {v};" for k, v in pal.items()) + " }\n"
    open(os.path.join(dest, "css/theme.css"), "w", encoding="utf-8", newline="\n").write(css)


def ecrire_manifeste(dest, titre, slug_jeu):
    p = os.path.join(dest, "manifest.webmanifest")
    if os.path.isfile(p):
        d = json.load(open(p, encoding="utf-8"))
        d["name"], d["short_name"] = titre, titre[:12]
        for k in ("start_url", "scope", "id"):
            if k in d:
                d[k] = "./" if k != "id" else f"/immersifs/{slug_jeu}/"
        ecrire(p, d)
    ecrire_meta(dest, titre)


def ecrire_meta(dest, titre):
    p = os.path.join(dest, "index.html")
    s = open(p, encoding="utf-8").read()
    s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{titre} : escape game immersif de cycle 3, version immersive du jeu de la collection.">', s, count=1)
    open(p, "w", encoding="utf-8", newline="\n").write(s)


def plan_medias(dest, jeu, theme):
    """medias.csv : prompts de production des décors, portraits et vidéos (lus par outils/medias/produire.py)."""
    en_tete = ["id", "type", "fichier", "dimensions", "duree", "ratio", "escale", "reference_ou_depart", "statut", "zones", "effets_moteur", "prompt_fr", "prompt_en", "negatif"]
    lignes = []
    mot = theme["mots"]["escale"]
    style = theme["style_visuel"]
    for es in jeu["enigmes"]["escales"]:
        decor = es["enigmes"][0]["decor"]
        d = jeu["fx"]["decors"][decor]
        zones = "; ".join(f"{z['id']} ({z['x']},{z['y']},{z['w']},{z['h']})" for z in d["zones"])
        prompt = (f"Décor en plan large, 16:9 : {es['lieu'] or es['titre']}. {es['episode']} Composition lisible avec {len(d['zones'])} objets distincts bien séparés "
                  f"(un par énigme), espace sombre et dégagé en bas de l'image pour la plaque de dialogue. {style}. Aucun texte lisible, aucun personnage au premier plan.")
        lignes.append({"id": f"decor-{decor}", "type": "image", "fichier": f"assets/images/decors/{decor}.webp", "dimensions": "1920×1080", "duree": "", "ratio": "16:9",
                       "escale": str(es["numero"]), "reference_ou_depart": "", "statut": "à produire", "zones": zones, "effets_moteur": "poussière, vignette, grain",
                       "prompt_fr": prompt, "prompt_en": "", "negatif": theme["negatif"]})
        lignes.append({"id": f"video-transition-e{es['numero']}", "type": "vidéo", "fichier": f"assets/videos/transition-e{es['numero']}.mp4", "dimensions": "1280×720", "duree": "8 s",
                       "ratio": "16:9", "escale": str(es["numero"]), "reference_ou_depart": f"assets/medias-depart/transition-e{es['numero']}.jpg", "statut": "à produire", "zones": "",
                       "effets_moteur": "voix et sous-titres dans le code", "prompt_fr": f"Image de départ : le décor de la {mot} {es['numero']}. Lent travelling avant ; l'ambiance vit (poussière, lumière qui vacille, objets qui bougent légèrement). Aucun texte, aucune lettre.",
                       "prompt_en": "", "negatif": theme["negatif"]})
    for pid, p in jeu["personnages"]["personnages"].items():
        lignes.append({"id": f"portrait-{pid}", "type": "image", "fichier": f"assets/images/personnages/{pid}.webp", "dimensions": "1200×1600", "duree": "", "ratio": "3:4",
                       "escale": "toutes", "reference_ou_depart": "", "statut": "secours actif (portrait dessiné)", "zones": "", "effets_moteur": "respiration, clignement, bouche animée (moteur)",
                       "prompt_fr": f"Portrait de référence, plan taille, cadrage vertical, fond flou. {p['nom']} : {p['fiche']}. Personnage inventé, visage non réel. {style}.",
                       "prompt_en": "", "negatif": theme["negatif"]})
    with open(os.path.join(dest, "medias.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=en_tete, delimiter=";")
        w.writeheader()
        w.writerows(lignes)
    return len(lignes)


def ecrire_rapport(dest, jeu, src_nom, rapport, theme, correspondances):
    esc = jeu["enigmes"]["escales"]
    nb = sum(len(e["enigmes"]) for e in esc)
    mot = theme["mots"]["escale"]
    L = [f"# Rapport de migration — {jeu['titre']}", "",
         f"Jeu d'origine : `{src_nom}/` (**non modifié**). Variante immersive : `immersifs/{os.path.basename(dest)}/`.", "",
         f"- {len(esc)} {theme['mots']['escales']}, {nb} énigmes ; grades : " + ", ".join(f"{a.upper()} → {b}" for a, b in correspondances) + ".",
         "- Le moteur est une copie de celui de « Vingt mille lieues » ; seuls `js/jeu-config.js`, `css/theme.css` et `assets/data/*.json` sont propres à ce jeu.", "",
         "## Ce qui est converti tel quel", "",
         "Énigmes (types, données, consignes, indices), leçons (Bibliothèque), personnages, mots-clés du coffre, dialogues d'introduction et de réussite.", "",
         "## Ce qu'il reste à faire (brouillons)", "",
         f"1. **Zones des décors** ({len(esc)} décors) : 3 à 4 zones à positions standard. Déposer l'image du décor, puis caler avec `outils/caler-effets.html` et nommer chaque objet.",
         f"2. **Enjeu et réaction du décor** de chacune des {nb} énigmes : rédiger (champs `enjeu`, `reaction_du_decor`, `probleme_narratif`).",
         "3. **Phrases des personnages** pour les énigmes 2 à 4 de chaque " + mot + " : écrire ce que dit l'émetteur (champ `dialogue` de chaque grade).",
         "4. **Médias** : `medias.csv` contient les prompts des décors, portraits et vidéos → `python outils/medias/produire.py --source <fournisseur>` (voir GUIDE-IMMERSIF.md).",
         "5. **Grades supplémentaires** (mousse, lieutenant, second) : à écrire si souhaité (le moteur les prend en charge).", ""]
    if rapport["avertissements"]:
        L += ["## Avertissements", ""] + [f"- {a}" for a in rapport["avertissements"]] + [""]
    L += ["## Vérifier", "", "```", f"node immersifs/{os.path.basename(dest)}/tests/test-immersif.js", "```", "",
          "Le test joue toutes les énigmes de tous les grades. Ouvrir ensuite le jeu avec `lancer-nautilus.bat` (adresse : `/immersifs/" + os.path.basename(dest) + "/`).", ""]
    open(os.path.join(dest, "MIGRATION-RAPPORT.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L))


def lanceur(dest, slug_jeu):
    prof = profondeur_de(dest)
    adresse = os.path.relpath(os.path.abspath(dest), RACINE).replace(os.sep, "/")
    s = ("@echo off\r\nchcp 65001 >nul\r\ntitle Serveur local - " + slug_jeu + "\r\ncd /d \"%~dp0" + "..\\" * prof + "\"\r\ncls\r\nset CMD=\r\npython --version >nul 2>&1 && set CMD=python\r\n"
         "if not defined CMD py --version >nul 2>&1 && set CMD=py\r\nif not defined CMD goto :sanspython\r\n"
         f"echo  Jeu : http://127.0.0.1:8000/{adresse}/\r\necho  Fermez cette fenetre pour arreter le serveur.\r\n"
         f"start \"\" cmd /c \"timeout /t 2 /nobreak >nul & start http://127.0.0.1:8000/{adresse}/\"\r\n"
         "if exist serveur.py (%CMD% serveur.py 8000) else (%CMD% -m http.server 8000)\r\npause\r\nexit /b 0\r\n\r\n:sanspython\r\n"
         "echo  [ERREUR] Python n'est pas installe ou pas dans le PATH.\r\npause\r\nexit /b 1\r\n")
    open(os.path.join(dest, "lancer.bat"), "w", encoding="ascii", newline="").write(s)


A_GARDER = ("assets/", "js/jeu-config.js", "js/donnees-embarquees.js", "js/decors-secours.js", "css/theme.css", "medias.csv", "MIGRATION-RAPPORT.md", "lancer.bat",
            "manifest.webmanifest", ".gitignore", "GUIDE-")


def maj_moteur(dest):
    """Remplace les fichiers du moteur par ceux du modèle ; le travail propre au jeu (données, médias, thème, config) est conservé."""
    dest = os.path.abspath(dest)
    cfg = os.path.join(dest, "js", "jeu-config.js")
    if not os.path.isfile(cfg):
        sys.exit(f"{dest} n'est pas une variante migrée (js/jeu-config.js introuvable).")
    slug_jeu = os.path.basename(dest)
    temp = dest + ".maj-tmp"
    if os.path.exists(temp):
        shutil.rmtree(temp)
    try:
        copier_moteur(temp, slug_jeu)
        # les pages statiques gardent leurs titres : on ne remplace que ce qui n'est pas du texte du jeu
        textes = {}
        m = re.search(r"window\.VML_JEU = (\{[\s\S]*\});", open(cfg, encoding="utf-8").read())
        textes = json.loads(m.group(1))["textes"] if m else {}
        adapter_html(temp, {**{"journal": "", "bibliotheque": "La Bibliothèque", "pause": "⏸ Pause", "titre": "", "auteur": ""}, **textes}, textes.get("titre", slug_jeu))
        ecrire_meta(temp, textes.get("titre", slug_jeu))
        for f in ("js/jeu-config.js", "js/donnees-embarquees.js", "js/decors-secours.js", "css/theme.css"):   # fichiers propres au jeu : nécessaires à la liste hors ligne
            if os.path.isfile(os.path.join(dest, f)):
                shutil.copy2(os.path.join(dest, f), os.path.join(temp, f))
        ecrire_sw(temp, slug_jeu)
        n = 0
        for racine, _, fichiers in os.walk(temp):
            for f in fichiers:
                rel = os.path.relpath(os.path.join(racine, f), temp).replace(os.sep, "/")
                if any(rel == g or rel.startswith(g) for g in A_GARDER):
                    continue
                cible = os.path.join(dest, rel)
                os.makedirs(os.path.dirname(cible), exist_ok=True)
                if not os.path.exists(cible) or open(cible, "rb").read() != open(os.path.join(racine, f), "rb").read():
                    shutil.copy2(os.path.join(racine, f), cible)
                    n += 1
        subprocess.run([sys.executable, os.path.join(dest, "outils", "embarquer-donnees.py")], check=True, stdout=subprocess.DEVNULL)
    finally:
        shutil.rmtree(temp, ignore_errors=True)
    print(f"✔ moteur de {os.path.relpath(dest, RACINE)} mis à jour : {n} fichier(s) changé(s) ; données, médias, thème et config conservés.")


def main():
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("jeu", nargs="?", help="dossier du jeu d'origine (ex. renaissance)")
    a.add_argument("--vers", help="dossier de sortie (défaut : immersifs/<jeu>)")
    a.add_argument("--theme", help="JSON de thème (surcharges de outils/immersif/theme-defaut.json)")
    a.add_argument("--grades", help="correspondances ancien:nouveau, ex. cm1:matelot,cm2:timonier,cm1:mousse")
    a.add_argument("--force", action="store_true", help="écrase la sortie si elle existe")
    a.add_argument("--lister", action="store_true", help="liste les jeux migrables et quitte")
    a.add_argument("--tous", action="store_true", help="migre tous les jeux migrables (dans immersifs/<jeu>)")
    a.add_argument("--maj-moteur", metavar="DOSSIER", help="met à jour le MOTEUR d'une variante déjà migrée (js, css, pages, tests, outils médias) sans toucher à ses données, ses médias, sa config ni son thème")
    o = a.parse_args()
    if o.lister:
        for j in jeux_migrables():
            print(j)
        return
    if o.maj_moteur:
        return maj_moteur(o.maj_moteur if os.path.isdir(o.maj_moteur) else os.path.join(RACINE, o.maj_moteur))
    if o.tous:
        for j in jeux_migrables():
            cmd = [sys.executable, os.path.abspath(__file__), j] + (["--force"] if o.force else []) + (["--theme", o.theme] if o.theme else []) + (["--grades", o.grades] if o.grades else [])
            subprocess.run(cmd, check=False)
        return
    if not o.jeu:
        a.error("indiquez le dossier du jeu à migrer (ou --lister, ou --tous)")
    src = o.jeu if os.path.isdir(o.jeu) else os.path.join(RACINE, o.jeu)
    if not os.path.isdir(src):
        sys.exit(f"Dossier introuvable : {o.jeu}")
    nom = os.path.basename(os.path.normpath(src))
    try:
        if "salles" not in lire(os.path.join(src, "assets/data/enigmes.json")):
            raise KeyError
    except Exception:
        sys.exit(f"« {nom} » n'a pas la structure attendue (assets/data/enigmes.json avec « salles » + dialogues.json). "
                 "Jeux migrables : " + ", ".join(jeux_migrables()) + ". Les autres (structure plus ancienne) se refont avec la skill, voir GUIDE-IMMERSIF.md.")
    dest = o.vers or os.path.join(RACINE, "immersifs", nom)
    if os.path.abspath(dest) == os.path.abspath(src):
        sys.exit("La sortie ne peut pas être le jeu d'origine : la migration est non destructive.")
    if os.path.exists(dest):
        if not o.force:
            sys.exit(f"{dest} existe déjà (--force pour l'écraser).")
        shutil.rmtree(dest)
    theme = fusion(lire(os.path.join(ICI, "theme-defaut.json")), lire(o.theme) if o.theme else {})
    if o.grades:
        correspondances = [tuple(x.split(":")) for x in o.grades.split(",")]
    else:
        correspondances = [(old, g) for old, gs in theme["grades"].items() for g in gs]
    rapport = {"avertissements": []}
    jeu = convertir(src, theme, correspondances, rapport)
    slug_jeu = slug(nom)
    # texte du thème : substitution {titre}, {auteur}
    auteur = (jeu["meta"].get("auteur") or "").strip() or "Escape game · cycle 3"
    textes = {k: v.replace("{titre}", jeu["titre"]).replace("{auteur}", auteur) for k, v in theme["textes"].items()}
    textes["fichierExport"] = slug_jeu
    textes["escale"] = theme["mots"]["escale"].capitalize()
    copier_moteur(dest, slug_jeu)
    for k in ("enigmes", "lecons", "dialogues", "personnages"):
        ecrire(os.path.join(dest, "assets/data", ("decors-fx" if k == "fx" else k) + ".json"), jeu[k])
    ecrire(os.path.join(dest, "assets/data/decors-fx.json"), jeu["fx"])
    cfg = {"id": slug_jeu, "decorAccueil": jeu["enigmes"]["escales"][0]["enigmes"][0]["decor"], "prefixeStockage": "vml_" + slug_jeu.replace("-", "_"), "grades": jeu["grades"], "textes": textes, "mots": theme["mots"]}
    open(os.path.join(dest, "js/jeu-config.js"), "w", encoding="utf-8", newline="\n").write(
        "/* Configuration du jeu — GÉNÉRÉ par outils/immersif/migrer-jeu.py ; modifiable à la main (titres, grades, vocabulaire). */\nwindow.VML_JEU = "
        + json.dumps(cfg, ensure_ascii=False, indent=2) + ";\n")
    ecrire_theme(dest, theme)
    ecrire_manifeste(dest, jeu["titre"], slug_jeu)
    adapter_html(dest, textes, jeu["titre"])
    lanceur(dest, slug_jeu)
    n_med = plan_medias(dest, jeu, theme)
    subprocess.run([sys.executable, os.path.join(dest, "outils", "embarquer-donnees.py")], check=True, stdout=subprocess.DEVNULL)
    ecrire_sw(dest, slug_jeu)
    ecrire_rapport(dest, jeu, nom, rapport, theme, correspondances)
    rel = os.path.relpath(dest, RACINE)
    print(f"✔ {nom} → {rel} : {len(jeu['enigmes']['escales'])} {theme['mots']['escales']}, "
          f"{sum(len(e['enigmes']) for e in jeu['enigmes']['escales'])} énigmes, {n_med} médias à produire.")
    print(f"  Rapport : {rel}/MIGRATION-RAPPORT.md   ·   Test : node {rel}/tests/test-immersif.js")


if __name__ == "__main__":
    main()
