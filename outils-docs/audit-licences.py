#!/usr/bin/env python3
"""Audit des crédits et licences des images et vidéos (amélioration N14).

    python outils-docs/audit-licences.py            écrit diffusion/AUDIT-MEDIAS.md et résume
    python outils-docs/audit-licences.py --stdout   n'écrit rien, affiche seulement

Pour chaque jeu (et chaque variante immersive), compare les fichiers de assets/images et assets/videos avec le
tableau de <jeu>/assets/medias/CREDITS-medias.md, et classe chaque média :
  - « crédité »          une ligne du tableau cite le fichier (auteur, licence, source) ;
  - « dérivé »            affiche, bande-annonce, vidéos animées : montage d'autres médias du jeu ;
  - « généré (IA) »       personnages, scènes et vidéos créés avec Agnes AI (déclaration générale dans CREDITS) ;
  - « dessin du dépôt »   SVG / dessin écrit pour le jeu ;
  - « SANS CRÉDIT »       aucun des cas ci-dessus : à vérifier avant diffusion.
Puis relève les licences citées et ce qu'elles impliquent pour une diffusion (attribution, partage dans les mêmes
conditions, licence propre d'un site comme Pixabay). Ce n'est pas un avis juridique : c'est l'inventaire qui permet
à l'auteur de décider.
"""
import os, re, sys, collections

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXT_IMG = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg"}
EXT_VID = {".mp4", ".webm"}
DOSSIERS_IGNORES = {"node_modules", ".git", "archives-hors-ligne", "_a-supprimer", "Claude outputs", "Michel strogoff", "Constitution 1958", "outils-tests", "__pycache__"}

def jeux():
    res = []
    for n in sorted(os.listdir(RACINE)):
        if n in DOSSIERS_IGNORES: continue
        if os.path.isfile(os.path.join(RACINE, n, "assets", "medias", "CREDITS-medias.md")):
            res.append(n)
    imm = os.path.join(RACINE, "immersifs")
    if os.path.isdir(imm):
        for n in sorted(os.listdir(imm)):
            if os.path.isfile(os.path.join(imm, n, "assets", "medias", "CREDITS-medias.md")):
                res.append("immersifs/" + n)
    return res

def lire_credits(chemin):
    t = open(chemin, encoding="utf-8").read()
    lignes = {}
    for l in t.splitlines():
        if not l.startswith("|"): continue
        cel = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cel) < 5 or cel[0].startswith("---") or cel[0].lower() == "fichier": continue
        f = cel[0].strip("`")
        lignes[f] = {"sujet": cel[1], "source": cel[2], "auteur": cel[3], "licence": cel[4]}
    # format « liste » des variantes immersives : - `fichier` · source · licence/droits · date
    for l in t.splitlines():
        m = re.match(r"^- `([^`]+)` · (.+?) · (.+?) · ", l)
        if m: lignes[m.group(1)] = {"sujet": "", "source": m.group(2), "auteur": m.group(2), "licence": m.group(3)}
    return t, lignes

def classer(jeu, f, credits_txt, lignes):
    rel = f.replace("\\", "/")
    if rel in lignes:
        lic = lignes[rel]["licence"]
        return ("droits à préciser" if re.match(r"à préciser", lic, re.I) else "crédité"), lic
    if rel.endswith("affiche.jpg") or "bande-annonce" in rel or "/miniatures/" in rel: return "dérivé", ""
    if os.path.splitext(rel)[1] == ".svg": return "dessin du dépôt", ""
    if re.search(r"dessin[ée]s? \(SVG|capture du d[ée]cor dessin", credits_txt, re.I) and ("/decors/" in rel or "/personnages/" in rel or "/cartes/" in rel or "/documents/" in rel or rel.startswith("assets/images/affiche")): return "dessin du dépôt", ""
    if "/personnages/" in rel or "/decors/" in rel or rel.startswith("assets/videos/") or "/videos/" in rel:
        if re.search(r"Agnes AI|Google Flow|cr[ée]{1,2}[ée]?s? avec", credits_txt, re.I): return "généré (IA)", ""
    return "SANS CRÉDIT", ""

def auditer():
    sortie = {}
    for jeu in jeux():
        base = os.path.join(RACINE, jeu)
        credits_txt, lignes = lire_credits(os.path.join(base, "assets", "medias", "CREDITS-medias.md"))
        cat = collections.Counter(); licences = collections.Counter(); sans = []; total = 0
        for racine, _, noms in os.walk(os.path.join(base, "assets")):
            if os.sep + "medias" in racine: continue
            for n in noms:
                ext = os.path.splitext(n)[1].lower()
                if ext not in EXT_IMG | EXT_VID: continue
                total += 1
                rel = os.path.relpath(os.path.join(racine, n), base)
                c, lic = classer(jeu, rel, credits_txt, lignes)
                cat[c] += 1
                if lic: licences[re.sub(r"\s+", " ", lic)] += 1
                if c == "SANS CRÉDIT": sans.append(rel.replace("\\", "/"))
        manquants = [f for f in lignes if not os.path.exists(os.path.join(base, f))]
        sortie[jeu] = {"total": total, "cat": cat, "licences": licences, "sans": sans, "lignes": len(lignes), "manquants": manquants}
    return sortie

IMPLICATIONS = [
    (r"CC BY-SA", "Attribution + partage dans les mêmes conditions : le média ET ses adaptations (vidéo animée à partir de la photo, affiche) restent sous CC BY-SA ; l'auteur et la licence doivent rester affichés."),
    (r"CC BY(?!-)", "Attribution : citer l'auteur, la licence et la source (déjà fait dans CREDITS-medias.md)."),
    (r"CC0|domaine public|Public domain", "Aucune condition (domaine public) ; citer la source par courtoisie."),
    (r"Pixabay", "Licence propre à Pixabay (pas une licence Creative Commons) : usage libre, mais redistribuer le fichier seul, comme banque d'images, est interdit ; il ne peut pas être placé sous une licence libre choisie par l'auteur du dépôt."),
    (r"Agnes|IA|Flow", "Images et vidéos générées par IA : conditions d'usage de l'outil (Agnes AI, Google Flow) et statut de droit d'auteur incertain à vérifier avant d'apposer une licence ; scènes et personnages fictifs, jamais de personne réelle."),
]

def rapport():
    S = auditer()
    L = []
    L.append("# Audit des crédits et licences des médias (N14)\n")
    L.append("Généré par `python outils-docs/audit-licences.py` — inventaire des images et vidéos de chaque jeu, comparé au tableau "
             "`assets/medias/CREDITS-medias.md`. Ce n'est pas un avis juridique : c'est l'état des lieux qui permet de choisir une licence.\n")
    tot = sum(s["total"] for s in S.values())
    cat = collections.Counter()
    lic = collections.Counter()
    for s in S.values():
        cat.update(s["cat"]); lic.update(s["licences"])
    L.append(f"**{tot} médias** dans {len(S)} jeux et variantes : " + ", ".join(f"{n} {k}" for k, n in cat.most_common()) + ".\n")
    L.append("## Licences citées dans les crédits\n")
    L.append("| Licence | Médias |\n|---|---|")
    for k, n in lic.most_common(): L.append(f"| {k} | {n} |")
    L.append("\n## Ce que cela implique pour la diffusion\n")
    for motif, texte in IMPLICATIONS:
        if any(re.search(motif, k, re.I) for k in lic) or (motif.startswith("Agnes") and cat.get("généré (IA)")):
            L.append(f"- **{motif.split('|')[0].replace('(?!-)','')}** — {texte}")
    L.append("\n## Par jeu\n")
    L.append("| Jeu | Médias | Crédités | Dérivés | Générés (IA) | Dessins | Sans crédit | Lignes de crédit sans fichier |\n|---|---|---|---|---|---|---|---|")
    for j, s in S.items():
        c = s["cat"]
        L.append(f"| {j} | {s['total']} | {c['crédité']} | {c['dérivé']} | {c['généré (IA)']} | {c['dessin du dépôt']} | {c['SANS CRÉDIT']} | {len(s['manquants'])} |")
    sans = [(j, f) for j, s in S.items() for f in s["sans"]]
    L.append("\n## Médias sans crédit (à vérifier avant diffusion)\n")
    if not sans: L.append("Aucun.")
    else:
        for j, f in sans[:80]: L.append(f"- `{j}/{f}`")
        if len(sans) > 80: L.append(f"- … et {len(sans) - 80} autres")
    manq = [(j, f) for j, s in S.items() for f in s["manquants"]]
    L.append("\n## Lignes de crédit dont le fichier n'est plus dans le dépôt\n")
    if not manq: L.append("Aucune.")
    else:
        for j, f in manq[:40]: L.append(f"- `{j}/{f}`")
        if len(manq) > 40: L.append(f"- … et {len(manq) - 40} autres")
    return "\n".join(L) + "\n", S

if __name__ == "__main__":
    texte, S = rapport()
    if "--stdout" in sys.argv:
        sys.stdout.reconfigure(encoding="utf-8"); print(texte)
    else:
        os.makedirs(os.path.join(RACINE, "diffusion"), exist_ok=True)
        with open(os.path.join(RACINE, "diffusion", "AUDIT-MEDIAS.md"), "w", encoding="utf-8", newline="\n") as f: f.write(texte)
        sys.stdout.reconfigure(encoding="utf-8")
        print(texte[:3500])
