#!/usr/bin/env python3
"""Génère les fichiers de voix (mp3) d'un jeu immersif avec les voix gratuites d'Edge (module `edge-tts`).

    pip install edge-tts                      (hors dépôt ; Internet nécessaire à la génération seulement)
    python outils/voix/generer-voix.py --liste-voix                 # voix françaises disponibles
    python outils/voix/generer-voix.py --essai                      # répliques et voix, sans rien générer
    python outils/voix/generer-voix.py                              # génère ce qui manque ou a changé
    python outils/voix/generer-voix.py --perso maelle --forcer      # refait un personnage

Une voix par personnage, la même tout au long du jeu : `assets/data/personnages.json`,
    "voix": {"edge": "fr-FR-DeniseNeural", "nom": "Denise", "rate": 0.95, "pitch": 1.0}
  - edge  : identifiant de la voix Edge (génération des mp3) ;
  - nom   : mot du nom de la voix du navigateur (repli sans mp3, Edge la propose en ligne) ;
  - rate, pitch : débit et hauteur (1 = neutre), appliqués aussi à la voix du navigateur.

Fichiers : assets/audio/voix/<personnage>/<clé>.mp3, clé = FNV-1a 32 bits du texte de la réplique (voir js/voix.js,
VML.cleReplique) ; suivi dans assets/audio/voix/index.json (personnage, voix, réglages, texte).
Répliques lues : accueil, cinématiques, fin de salle, coffre, dialogue de chaque énigme à chaque grade.
Aucune voix réelle n'est clonée ; ne rien écrire de plus que le texte du jeu.
"""
import argparse, asyncio, json, os, re, sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))   # dossier du jeu
DATA = os.path.join(RACINE, "assets", "data")
SORTIE = os.path.join(RACINE, "assets", "audio", "voix")
GRADES = ["mousse", "matelot", "timonier", "lieutenant", "second"]


def texte_replique(t):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", str(t or ""))).strip()


def cle_replique(texte):
    h = 0x811C9DC5
    for o in texte_replique(texte).encode("utf-8"):
        h = ((h ^ o) * 0x01000193) & 0xFFFFFFFF
    return format(h, "08x")


def lire(n):
    return json.load(open(os.path.join(DATA, n), encoding="utf-8"))


def repliques():
    """Liste de (personnage, texte) dans l'ordre du jeu, sans doublon."""
    d, e = lire("dialogues.json"), lire("enigmes.json")
    vus, sortie = set(), []

    def ajouter(perso, texte):
        t = texte_replique(texte)
        if perso and t and (perso, t) not in vus:
            vus.add((perso, t)); sortie.append((perso, t))

    a = d.get("accueil") or {}
    ajouter(a.get("personnage"), a.get("texte"))
    for c in (d.get("cinematiques") or {}).values():
        for p in c.get("plans", []):
            ajouter(p.get("personnage"), p.get("texte"))
    for f in (d.get("fin_escale") or {}).values():
        ajouter(f.get("personnage"), f.get("texte"))
    c = d.get("coffre") or {}
    ajouter(c.get("personnage"), c.get("texte"))
    for s in e["escales"]:
        for q in s["enigmes"]:
            for g in GRADES:
                if g in q:
                    ajouter(q.get("personnage_emetteur"), q[g].get("dialogue"))
    return sortie


def reglages(v):
    rate, pitch = float(v.get("rate", 1)), float(v.get("pitch", 1))
    return "%+d%%" % round((rate - 1) * 100), "%+dHz" % round((pitch - 1) * 50)


async def generer(travaux, index):
    import edge_tts
    for perso, texte, voix, chemin, rate, pitch in travaux:
        os.makedirs(os.path.dirname(chemin), exist_ok=True)
        for essai in range(3):
            try:
                await edge_tts.Communicate(texte, voix, rate=rate, pitch=pitch).save(chemin)
                break
            except Exception as ex:                           # réseau, file d'attente : on réessaie
                if essai == 2:
                    print("  ✖", perso, texte[:40], "->", ex)
                    chemin = None
                else:
                    await asyncio.sleep(2 * (essai + 1))
        if chemin:
            print("  ✔", perso, cle_replique(texte), texte[:50])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--liste-voix", action="store_true")
    ap.add_argument("--essai", action="store_true")
    ap.add_argument("--perso")
    ap.add_argument("--forcer", action="store_true")
    o = ap.parse_args()
    if o.liste_voix:
        import edge_tts
        for v in asyncio.run(edge_tts.list_voices()):
            if v["Locale"].lower().startswith("fr-"):
                print(f'{v["ShortName"]:38} {v["Gender"]:7} {v["Locale"]}')
        return
    persos = lire("personnages.json")["personnages"]
    idx_chemin = os.path.join(SORTIE, "index.json")
    index = json.load(open(idx_chemin, encoding="utf-8")) if os.path.isfile(idx_chemin) else {}
    sans, travaux, prises = [], [], {}
    for perso, texte in repliques():
        if o.perso and perso != o.perso:
            continue
        v = (persos.get(perso) or {}).get("voix") or {}
        if not v.get("edge"):
            sans.append(perso); continue
        prises.setdefault(v["edge"], set()).add(perso)
        rate, pitch = reglages(v)
        cle = cle_replique(texte)
        chemin = os.path.join(SORTIE, perso, cle + ".mp3")
        empreinte = [v["edge"], rate, pitch, texte]
        if not o.forcer and os.path.isfile(chemin) and index.get(perso + "/" + cle) == empreinte:
            continue
        travaux.append((perso, texte, v["edge"], chemin, rate, pitch))
        index[perso + "/" + cle] = empreinte
    for p in sorted(set(sans)):
        print("⚠ pas de voix Edge pour", p, '(personnages.json : "voix": {"edge": "fr-FR-…Neural"})')
    for voix, qui in prises.items():
        if len(qui) > 1:
            print("⚠ la voix", voix, "est partagée par", ", ".join(sorted(qui)), ": une voix par personnage")
    print(f"{len(repliques())} répliques ; {len(travaux)} à générer.")
    if o.essai or not travaux:
        return
    asyncio.run(generer(travaux, index))
    os.makedirs(SORTIE, exist_ok=True)
    json.dump(index, open(idx_chemin, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
