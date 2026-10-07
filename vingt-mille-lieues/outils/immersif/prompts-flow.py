#!/usr/bin/env python3
"""Écrit PROMPTS-GOOGLE-FLOW.md : les prompts d'images (Google Flow) d'une variante immersive.

    python vingt-mille-lieues/outils/immersif/prompts-flow.py <jeu>      (ou --tous)

Pour chaque salle : un décor 16:9 dont les quatre objets des énigmes sont placés là où le moteur attend les zones cliquables
et dont le bas reste calme (plaque de dialogue). Pour chaque personnage : un portrait 3:4. Les images servent aussi de points
de départ aux vidéos (Agnes) : une section donne le prompt de mouvement de chaque vidéo.
Sources : assets/data/decors-fx.json (objets et positions), enigmes.json, personnages.json, css/theme.css (palette), js/jeu-config.js.
"""
import json, os, re, sys

RACINE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))

STYLE = ("Peinture numérique semi-réaliste de cinéma, éclairage dramatique (lumière chaude contre ombres froides), matières crédibles, "
         "nombreux détails narratifs lisibles, grain fin, profondeur de champ.")
NEGATIF = ("texte, lettres, chiffres, logo, filigrane, signature, interface, cadre, mains déformées, doigts en trop, visage déformé, flou, "
           "personne réelle ou célébrité, style dessin animé, violence, sang")


def place(x, y, w, h):
    """Position en mots d'une zone (pourcentages de l'image)."""
    cx, cy = x + w / 2, y + h / 2
    h_ = "à gauche" if cx < 36 else ("à droite" if cx > 64 else "au centre")
    v_ = "en haut" if cy < 40 else ("au milieu" if cy < 62 else "en bas")
    return f"{v_} {h_}" if not (h_ == "au centre" and v_ == "au milieu") else "au centre"


def lire(chemin):
    return json.load(open(chemin, encoding="utf-8"))


def palette_texte(dest):
    p = os.path.join(dest, "css", "theme.css")
    if not os.path.isfile(p):
        return ""
    v = dict(re.findall(r"(--[\w-]+):\s*([^;]+);", open(p, encoding="utf-8").read()))
    if not v:
        return ""
    return (f"Dominantes de couleur du jeu (à respecter pour que les images aillent avec l'interface) : fond {v.get('--abysse', '')} et {v.get('--ocean', '')}, "
            f"lumières et accents {v.get('--laiton', '')}, {v.get('--ambre', '')}, touches {v.get('--cyan', '')}.")


def decrire_perso(p):
    q = p.get("portrait") or {}
    bits = [p.get("fiche", "")]
    if q.get("genre"):
        bits.append(f"genre : {q['genre']}")
    if q.get("coiffure"):
        bits.append("cheveux " + {"longue": "longs", "courte": "courts", "chauve": "absents"}.get(q["coiffure"], q["coiffure"]))
    if q.get("lunettes"):
        bits.append("porte des lunettes")
    if p.get("ton"):
        bits.append("expression : " + p["ton"].lower())
    return ", ".join(b for b in bits if b)


def direction(jeu):
    """STYLE_VISUEL et EPOQUE du module grades/<jeu>_theme.py (direction artistique propre au jeu), sinon la charte commune."""
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "grades"))
        m = __import__(jeu.replace("-", "_") + "_theme")
        return getattr(m, "STYLE_VISUEL", STYLE), getattr(m, "EPOQUE", "")
    except Exception:
        return STYLE, ""


def jeu_md(jeu):
    STYLE, EPOQUE = direction(jeu)
    dest = os.path.join(RACINE, "immersifs", jeu)
    data = os.path.join(dest, "assets", "data")
    E, P, FX = lire(os.path.join(data, "enigmes.json")), lire(os.path.join(data, "personnages.json")), lire(os.path.join(data, "decors-fx.json"))
    cfg = json.loads(re.search(r"window\.VML_JEU = (\{[\s\S]*\});", open(os.path.join(dest, "js", "jeu-config.js"), encoding="utf-8").read()).group(1))
    titre = cfg["textes"]["titre"]
    pal = palette_texte(dest)
    L = [f"# Prompts Google Flow — {titre}", "",
         "Ces prompts produisent les images du jeu `immersifs/" + jeu + "/`. Les décors servent aussi de **premières images des vidéos** (Agnes).", "",
         "## Mode d'emploi", "",
         "1. Dans Google Flow, choisir **Images** (Imagen), format **16:9** pour les décors et **3:4** (ou 9:16 recadré) pour les portraits ; 4 variantes par prompt, choisir la meilleure.",
         "2. Commencer par la **charte** ci-dessous : l'ajouter à la fin de chaque prompt (ou la coller dans les ingrédients de style).",
         "3. Les prompts sont en français. Si le rendu est faible, les traduire en anglais en gardant la structure.",
         "4. Vérifier chaque image : **les quatre objets numérotés sont bien visibles et séparés**, le **bas de l'image est calme** (la plaque de dialogue le recouvre), **aucun texte** dans l'image, **aucune personne réelle**.",
         "5. Déposer les fichiers : `python outils/medias/importer-image.py <fichier> --decor <id>` (ou `--portrait <id>`) ; ajouter `--depart <vidéo>` pour qu'un décor serve aussi de départ de vidéo.",
         "6. Renseigner la source (« Google Flow, Imagen ») et la licence dans les crédits : `--source \"Google Flow\" --licence \"…\"`.", "",
         "## Charte (à ajouter à chaque prompt)", "",
         "> " + STYLE + (" " + EPOQUE if EPOQUE else "") + (" " + pal if pal else ""), ">",
         "> Éviter : " + NEGATIF + ".", "",
         "Règles de composition communes aux décors : plan large 16:9 ; **aucun personnage au premier plan** ; les quatre objets d'énigme sont éclairés et bien lisibles, "
         "placés aux endroits indiqués (zones du moteur : repères en pourcentage de l'image) ; le **quart inférieur** reste sombre ou dégagé pour la plaque de dialogue ; "
         "pas de texte lisible (les livres, cartes et écrans montrent des motifs, pas de mots).", ""]
    # ---- décors
    L += ["## Décors (16:9, 1920 × 1080)", ""]
    vus = set()
    for s in E["escales"]:
        decor = s["enigmes"][0]["decor"]
        if decor in vus:
            continue
        vus.add(decor)
        fx = FX["decors"].get(decor, {})
        zones = {z["id"]: z for z in fx.get("zones", [])}
        L += [f"### {s['numero']}. {s['titre']} — `{decor}`", "",
              f"**Lieu** : {s.get('lieu', '')}. {re.sub(r'<[^>]+>', '', s.get('episode', '')).strip()}", "", "**Les objets des énigmes** (un par énigme, bien séparés) :", ""]
        objets = []
        for e in s["enigmes"]:
            z = zones.get(e["objet_principal"])
            if not z:
                continue
            pos = place(z["x"], z["y"], z["w"], z["h"])
            objets.append((pos, z["libelle"], z.get("description", ""), e["id"]))
            L.append(f"- {pos} : **{z['libelle']}** — {z.get('description', '')} (énigme {e['id']})")
        phrase = "; ".join(f"{o[1]} ({o[0]})" for o in objets)
        L += ["", "**Prompt**", "",
              "```",
              f"Décor d'escape game pour enfants, plan large 16:9 : {s.get('lieu', '')}. {re.sub(r'<[^>]+>', '', s.get('episode', '')).strip()} "
              f"Quatre objets bien éclairés, nettement séparés et lisibles : {phrase}. "
              "Aucun personnage au premier plan. Le tiers inférieur de l'image est sombre et dégagé. Aucun texte lisible. "
              + STYLE + (" " + pal if pal else ""),
              "```", ""]
    # ---- portraits
    L += ["## Portraits (3:4, 1200 × 1600)", "",
          "Un portrait par personnage, **personnage inventé, jamais une personne réelle**. Buste, regard vers le spectateur, fond sobre dans les couleurs du jeu, éclairage doux. "
          "Une fois le portrait choisi, le **réutiliser comme image de départ** de la vidéo du personnage (« au repos » puis « parle »).", ""]
    for pid, p in P["personnages"].items():
        L += [f"### {p['nom']} — `{pid}`", "", "```",
              f"Portrait en buste d'un personnage de fiction, format 3:4, fond sobre légèrement flou, éclairage doux et chaleureux, regard vers l'objectif, expression bienveillante : "
              f"{decrire_perso(p)}. Tenue en rapport avec son rôle ({p.get('fiche', '')}). " + STYLE,
              "```", ""]
    # ---- vidéos
    L += ["## Vidéos (Agnes, à partir des images)", "",
          "Image de départ = le décor correspondant (importé avec `--depart`). Ordre : lancer `produire.py --types video --id <vidéo> --max-videos 1 --depart-decor <décor>`. "
          "Prompt de mouvement (court, calme, sans texte) :", ""]
    for s in E["escales"]:
        decor = s["enigmes"][0]["decor"]
        L += [f"- `transition-e{s['numero']}` (départ : `{decor}`) : « Lent travelling avant dans {s.get('lieu', 'la pièce')}. L'ambiance vit : lumière qui vacille, poussière en suspension, objets qui bougent à peine. Pas de texte, pas de personnage. »"]
    L += ["- `fin-e<N>` : même départ que `transition-e<N>`, mouvement plus lumineux (« la lumière s'intensifie, tout s'apaise »).",
          "- `intro` et `fin` : plan d'ensemble du lieu principal ; « lent mouvement de caméra vers le lieu clé, lumière du début de l'histoire » ; pour `fin`, la lumière revient.",
          "- Portraits « parle » : départ = première image de la vidéo au repos ; « le personnage parle calmement, léger mouvement de tête, clignement des yeux ». Durée 5 s, 24 images/s.", ""]
    out = os.path.join(dest, "PROMPTS-GOOGLE-FLOW.md")
    open(out, "w", encoding="utf-8", newline="\n").write("\n".join(L))
    return out


if __name__ == "__main__":
    jeux = sorted(d for d in os.listdir(os.path.join(RACINE, "immersifs")) if os.path.isfile(os.path.join(RACINE, "immersifs", d, "assets", "data", "enigmes.json"))) if sys.argv[1] == "--tous" else [sys.argv[1]]
    for j in jeux:
        print(os.path.relpath(jeu_md(j), RACINE))
