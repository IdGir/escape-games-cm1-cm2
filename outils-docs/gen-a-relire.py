#!/usr/bin/env python3
"""Génère a-relire.html : la page « À relire » de l'espace enseignant.

    python outils-docs/gen-a-relire.py

Lit les <jeu>/A-VERIFIER.md (un point = une ligne numérotée ou une puce), y associe
des liens directs (jeu, leçons, guide, ligne exacte du fichier) et des sources officielles,
et écrit a-relire.html (autonome, données incluses).
Les validations sont gardées par le serveur (relectures-validees.json, dossier de données)
et par le navigateur ; un point dont le texte change redevient « à relire » (identifiant = jeu + n° + empreinte du texte).
Pour ajouter une source : compléter SOURCES puis REGLES (mots-clés) ou NOTES (un point précis).
"""
import hashlib, html, json, os, re, subprocess, sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GITHUB = "https://github.com/IdGir/escape-games-cm1-cm2/blob/escape-games/"
SENSIBLES = ["traite-colonies", "grande-guerre", "seconde-guerre", "etats-matiere"]
HISTOIRE = {"chateau-fort", "grande-guerre", "grandes-explorations", "moyen-age-abbaye", "renaissance", "seconde-guerre",
            "traite-colonies", "versailles", "constitution"}
IGNORER_SECTIONS = re.compile(r"contr[oô]les faits|v[ée]rifications faites", re.I)
DM = "https://www.defense.gouv.fr/chemins-memoire/histoire-memoires/"

# cle : (libellé, url, précise = vérifiée par une recherche le 25/11/2026)
SOURCES = {
    "bo22": ("BO n° 22 du 28 mai 2026 — histoire-géographie, cycle 3", "https://www.education.gouv.fr/bo/2026/Hebdo22/MENE2608631A"),
    "bo24": ("BO n° 24 du 11 juin 2026 — sciences et technologie, cycles 2 et 3", "https://www.education.gouv.fr/bo/2026/Hebdo24/MENE2611650A"),
    "eduscol": ("Éduscol — ressources cycle 3", "https://eduscol.education.gouv.fr/"),
    "lumni": ("Lumni (service public)", "https://www.lumni.fr/"),
    "gallica": ("Gallica (BnF)", "https://gallica.bnf.fr/"),
    "legifrance_noir": ("Légifrance — loi n° 2026-1015 du 2 novembre 2026 (abrogation du « code noir »)", "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000055047268"),
    "vp_noir": ("vie-publique.fr — Abrogation du code noir, loi du 2 novembre 2026", "https://www.vie-publique.fr/loi/303397-abrogation-du-code-noir-loi-du-2-novembre-2026-mathiasin"),
    "an_noir": ("Assemblée nationale — rapport sur l'abrogation du Code noir (histoire du texte)", "https://www.assemblee-nationale.fr/dyn/opendata/RAPPANR5L17B2810.html"),
    "bnf_traite": ("BnF — La traite (ports autorisés 1713-1721)", "https://heritage.bnf.fr/france-ameriques/en/slave-trade-1"),
    "bnf_esclavage": ("BnF — La réalité historique de l'esclavage, ressources en ligne", "https://www.bnf.fr/fr/la-realite-historique-de-lesclavage-ressources-en-ligne"),
    "fa_rochelle": ("FranceArchives — Le commerce triangulaire et la traite négrière rochelaise", "https://francearchives.gouv.fr/article/540820424"),
    "nantes_guide": ("Mémorial de l'abolition de l'esclavage (Nantes) — guide enseignants", "https://pedagogie.ac-nantes.fr/medias/fichier/memorial_guide_enseignants_1334846808143.pdf"),
    "anses": ("ANSES — Nutrition des enfants : repères", "https://www.anses.fr/fr/content/nutrition-des-enfants-des-personnes-agees-et-des-femmes-enceintes-ou-allaitantes-lanses"),
    "cdm_verdun": ("Chemins de mémoire — 1916, Verdun et la Somme", DM + "ressources-historiques/premiere-guerre-mondiale/combattre-combats/fronts-32"),
    "cdm_11nov": ("Chemins de mémoire — 11 novembre, journée nationale de commémoration", DM + "journees-nationales-commemoratives/11-novembre-journee-nationale-commemoration"),
    "cdm_1918": ("Chemins de mémoire — 1918, sortir de la guerre", DM + "ressources-historiques/premiere-guerre-mondiale/sorties-guerre/celebrer-4"),
    "cdm_rafles": ("Chemins de mémoire — Les grandes rafles de Juifs en France", DM + "ressources-historiques/seconde-guerre-mondiale/sort-juifs-tsiganes-0"),
    "vp_vel": ("vie-publique.fr — La rafle du Vél' d'Hiv' de juillet 1942", "https://www.vie-publique.fr/parole-dexpert/285291-il-y-80-ans-la-rafle-du-vel-dhiv-de-juillet-1942"),
    "ushmm_vel": ("USHMM — La rafle du Vél' d'Hiv'", "https://encyclopedia.ushmm.org/content/fr/article/the-velodrome-dhiver-vel-dhiv-roundup"),
    "mer_fresnel": ("mer.gouv.fr — Bicentenaire de la lentille de Fresnel", "https://www.mer.gouv.fr/bicentenaire-de-linvention-de-la-lentille-de-fresnel"),
    "eco_fresnel": ("Ministère de la Transition écologique — Dossier de presse Fresnel", "https://www.ecologie.gouv.fr/sites/default/files/DPFresnel.pdf"),
    "pop_cordouan": ("POP (ministère de la Culture) — Phare de Cordouan", "https://pop.culture.gouv.fr/notice/merimee/PA00083858"),
    "ipgp_soufriere": ("IPGP — Rapport de mission à la Soufrière, juillet 1976", "https://www.ipgp.fr/~beaudu/soufriere/doc/19760723_rapport_Tazieff_retranscription.pdf"),
    "sdes_volcans": ("SDES (ministère de la Transition écologique) — Éruptions volcaniques, chiffres clés", "https://www.statistiques.developpement-durable.gouv.fr/edition-numerique/chiffres-cles-risques-naturels/26-eruptions-volcaniques"),
    "code_route": ("Légifrance — Code de la route (art. R413-3 : 50 km/h en agglomération)", "https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006074228/"),
}
# Pistes générales : utiles mais non précises (pas de page exacte vérifiée pour le point).
GENERALES_HISTOIRE = ["bo22", "eduscol", "gallica"]
GENERALES_SCIENCES = ["bo24", "eduscol", "lumni"]

# Mots-clés (dans le texte du point) -> sources précises
REGLES = [
    (r"code noir|abrog", ["legifrance_noir", "vp_noir", "an_noir"]),
    (r"traite|bordeaux|nantes|le havre|la rochelle|saint-malo|honfleur|esclav|habitation|toussaint|ha[iï]ti", ["bnf_traite", "bnf_esclavage", "fa_rochelle", "nantes_guide"]),
    (r"kcal|[ée]nergie.*enfant|anses|besoins en [ée]nergie", ["anses"]),
    (r"verdun|bataille de la somme|poilu|mobilisation|monument aux morts|fleur au fusil", ["cdm_verdun", "cdm_11nov"]),
    (r"armistice|11 novembre|soldat inconnu|1922", ["cdm_11nov", "cdm_1918"]),
    (r"v[ée]l.?d.?hiv|rafle|d[ée]port|juif|juifs", ["cdm_rafles", "vp_vel", "ushmm_vel"]),
    (r"fresnel|cordouan|phare", ["mer_fresnel", "eco_fresnel", "pop_cordouan"]),
    (r"soufri[èe]re|pel[ée]e|volcan|[ée]ruption", ["ipgp_soufriere", "sdes_volcans"]),
    (r"r ?413|agglom[ée]ration|50 km/h|code de la route", ["code_route"]),
]
# Notes de vérification déjà établies (dossier, n° du point) -> texte
NOTES = {
    ("traite-colonies", 1): "Source trouvée le 25/11/2026 : la loi n° 2026-1015 du 2 novembre 2026 portant abrogation du « code noir » a été promulguée le 2 novembre et publiée au Journal officiel du 3 novembre 2026. La phrase du jeu (« En 2026, une loi l'a officiellement abrogé ») est exacte. Reste à décider si vous voulez citer le numéro de la loi.",
    ("traite-colonies", 3): "La BnF liste les ports autorisés à la traite entre 1713 et 1721 : Nantes, Rouen, La Rochelle, Bordeaux, Saint-Malo, Honfleur, Le Havre et Marseille. Cela confirme la formulation du jeu.",
    ("traite-colonies", 4): "La BnF cite bien ces ports parmi les ports autorisés (1713-1721). Pour un classement : les sources pédagogiques parlent de Nantes en tête, puis La Rochelle, Le Havre, Bordeaux (le jeu ne donne aucun rang, c'est prudent).",
    ("lumiere", 7): "Sources officielles concordantes : lentille testée sur le phare de Cordouan en juillet 1823 (mer.gouv.fr, dossier de presse du ministère). Attention : les pages officielles donnent des jours différents (25 juillet, 25 août) : ne pas écrire de jour précis. Cordouan éclaire depuis 1611 (dossier de presse du syndicat mixte de l'estuaire).",
    ("seconde-guerre", 2): "Vél' d'Hiv : 12 884 personnes arrêtées les 16 et 17 juillet 1942 (vie-publique.fr, Mémorial de la Shoah, ville de Paris). « Environ 13 000 » est correct. Au total, environ 33 000 Juifs déportés depuis la France en 1942 d'après vie-publique.fr (à comparer avec le chiffre du jeu).",
    ("terre-active", 1): "Les sources divergent : 28 000 victimes (Futura, Global Chance) et 30 000 habitants de Saint-Pierre (Larousse). « Près de 28 000 » ou « environ 30 000 » sont défendables ; garder « environ ».",
    ("terre-active", 6): "IPGP : plus de 70 000 personnes vivent sur les flancs de la Soufrière (ordre de grandeur de la population concernée par une évacuation) ; ce n'est pas un nombre d'évacués confirmé en 1976. « Des dizaines de milliers » reste la formule prudente.",
    ("mouvement", 7): "Confirmé : art. R413-3 du Code de la route, 50 km/h en agglomération (version en vigueur depuis le 10 janvier 2014), le maire pouvant fixer une limite plus basse (30 km/h).",
}

def catalogue():
    js = ("const t=require('fs').readFileSync('commun/donnees/catalogue.js','utf8');"
          "console.log(JSON.stringify(new Function(t+';return CATALOGUE')().jeux))")
    try:
        out = subprocess.run(["node", "-e", js], cwd=RACINE, capture_output=True, encoding="utf-8", check=True).stdout
        return [j for j in json.loads(out) if j.get("dossier")]
    except Exception:
        return []

def existe(*p):
    return os.path.exists(os.path.join(RACINE, *p))

def md_html(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"(https?://[^\s<>)]+)", r'<a href="\1" target="_blank" rel="noopener">\1</a>', t)
    return t

def lire_points(dossier):
    chemin = os.path.join(RACINE, dossier, "A-VERIFIER.md")
    lignes = open(chemin, encoding="utf-8").read().splitlines()
    points, section, cur = [], "", None
    def clore():
        nonlocal cur
        if cur and not IGNORER_SECTIONS.search(cur["section"]) and not re.match(
                r"^(Histoire-g[ée]ographie|Sciences et technologie)[^:]*:\s*Arr[êe]t[ée]", cur["texte"]):
            points.append(cur)
        cur = None
    for i, l in enumerate(lignes, 1):
        if l.startswith("#"):
            clore(); section = l.lstrip("# ").strip(); continue
        m = re.match(r"^(\d+)\.\s+(.*)", l)
        b = re.match(r"^[-*]\s+(.*)", l)
        if m or b:
            clore()
            cur = {"ligne": i, "section": section, "texte": (m.group(2) if m else b.group(1)).strip(), "num": int(m.group(1)) if m else None}
        elif cur and l.strip() and l.startswith(" "):
            cur["texte"] += " " + l.strip()
        elif not l.strip():
            clore()
    clore()
    for n, p in enumerate(points, 1):
        p["ordre"] = n
    return points

def sources_du_point(dossier, texte):
    bas = texte.lower()
    precises = []
    for motif, cles in REGLES:
        if re.search(motif, bas):
            for c in cles:
                if c not in precises:
                    precises.append(c)
    programme = re.search(r"programme|bo n|annexe|libell[ée]|niveau|cm1|cm2|attendu", bas)
    gen = GENERALES_HISTOIRE if dossier in HISTOIRE else GENERALES_SCIENCES
    if programme:
        prog = gen[0]
        if prog not in precises:
            precises.insert(0, prog)
    return precises[:5], ([] if precises else gen)

def main():
    cat = {j["dossier"]: j for j in catalogue()}
    ordre = [d for d in SENSIBLES] + sorted(d for d in os.listdir(RACINE)
             if d not in SENSIBLES and os.path.isfile(os.path.join(RACINE, d, "A-VERIFIER.md")) and d not in ("prompts-opus", "_a-supprimer"))
    jeux, total = [], 0
    for d in ordre:
        if not existe(d, "A-VERIFIER.md"):
            continue
        j = cat.get(d, {})
        imm = j.get("immersif") or ("immersifs/" + d if existe("immersifs", d, "index.html") else "")
        liens = []
        if imm and existe(imm, "index.html"): liens.append(["Jouer (immersif)", imm + "/"])
        if existe(d, "index.html"): liens.append(["Jouer (classique)", d + "/"])
        for base in (imm, d):
            if base and existe(base, "lecons-imprimables.html"):
                liens.append(["Leçons A4", base + "/lecons-imprimables.html"]); break
        if existe(d, "prof.html"): liens.append(["Tableau de bord", d + "/prof.html"])
        if existe(d, "GUIDE-PEDAGOGIQUE.md"): liens.append(["Guide pédagogique", GITHUB + d + "/GUIDE-PEDAGOGIQUE.md"])
        if existe(d, "README.md"): liens.append(["Solutions (README)", GITHUB + d + "/README.md"])
        points = []
        for p in lire_points(d):
            precises, generales = sources_du_point(d, p["texte"])
            h = hashlib.sha1(p["texte"].encode("utf-8")).hexdigest()[:6]
            ou = sorted(set(re.findall(r"(?:[ée]nigmes?|salle|le[çc]on|ch\.)\s*[\dIVX]+(?:-\d+)?", p["texte"], re.I)))[:4]
            points.append({
                "id": f"{d}:{p['ordre']}:{h}", "n": p["num"] or p["ordre"], "section": p["section"],
                "html": md_html(p["texte"]), "texte": p["texte"], "ligne": p["ligne"], "ou": ou,
                "note": NOTES.get((d, p["num"])) if p["num"] else None,
                "src": precises, "gen": generales,
            })
        if not points:
            continue
        total += len(points)
        jeux.append({"d": d, "titre": j.get("titre") or d, "icone": j.get("icone", ""), "matiere": j.get("matiere", ""),
                     "sensible": d in SENSIBLES, "md": GITHUB + d + "/A-VERIFIER.md", "liens": liens, "points": points})
    donnees = {"jeux": jeux, "sources": {k: [v[0], v[1]] for k, v in SOURCES.items()},
               "programme": {"histoire": "bo22", "sciences": "bo24"}, "histoire": sorted(HISTOIRE), "total": total}
    modele = open(os.path.join(RACINE, "outils-docs", "modele-a-relire.html"), encoding="utf-8").read()
    js = json.dumps(donnees, ensure_ascii=False).replace("</", "<\\/")
    sortie = modele.replace("/*DONNEES*/null", js)
    with open(os.path.join(RACINE, "a-relire.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(sortie)
    print(f"a-relire.html : {len(jeux)} jeux, {total} points.")

if __name__ == "__main__":
    main()
