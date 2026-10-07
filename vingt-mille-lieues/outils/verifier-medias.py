#!/usr/bin/env python3
"""Contrôle qualité des médias du jeu : présents / manquants, dimensions, poids, ratio, noms mal écrits.

Usage : python vingt-mille-lieues/outils/verifier-medias.py
Lit medias.csv (noms attendus). Dimensions des images : Pillow si installé, sinon lecture de l'en-tête PNG/JPEG/WebP.
Avertissements (pas d'erreur) : ratio éloigné de celui attendu, image trop petite, vidéo > 6 Mo, nom inattendu.
"""
import csv, os, struct, sys

ICI = os.path.dirname(os.path.abspath(__file__))
JEU = os.path.dirname(ICI)


def taille_image(p):
    try:
        from PIL import Image
        with Image.open(p) as im:
            return im.size
    except Exception:
        pass
    with open(p, "rb") as f:
        t = f.read(64 * 1024)
    if t[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", t[16:24])
    if t[:4] == b"RIFF" and t[8:12] == b"WEBP":
        if t[12:16] == b"VP8X":
            return (1 + int.from_bytes(t[24:27], "little"), 1 + int.from_bytes(t[27:30], "little"))
        if t[12:16] == b"VP8 ":
            return (struct.unpack("<H", t[26:28])[0] & 0x3FFF, struct.unpack("<H", t[28:30])[0] & 0x3FFF)
    if t[:2] == b"\xff\xd8":
        i = 2
        while i < len(t) - 9:
            if t[i] == 0xFF and t[i + 1] in (0xC0, 0xC2):
                h, w = struct.unpack(">HH", t[i + 5:i + 9]); return (w, h)
            i += 2 + struct.unpack(">H", t[i + 2:i + 4])[0] if t[i] == 0xFF else 1
    return None


def main():
    with open(os.path.join(JEU, "medias.csv"), encoding="utf-8") as f:
        lignes = list(csv.DictReader(f, delimiter=";"))
    attendus, presents, manquants, avert = set(), 0, 0, 0
    for l in lignes:
        base, ext = os.path.splitext(l["fichier"])
        exts = [".webp", ".jpg", ".png"] if l["type"] == "image" else [".mp4", ".webm"]
        for e in exts:
            attendus.add(os.path.normpath(base + e))
        trouve = next((base + e for e in exts if os.path.isfile(os.path.join(JEU, base + e))), None)
        if not trouve:
            manquants += 1
            print(f"·  manquant   {l['fichier']:<45} ({l['statut']})")
            continue
        presents += 1
        p = os.path.join(JEU, trouve)
        ko = os.path.getsize(p) // 1024
        msg = f"✓  présent    {trouve:<45} {ko} Ko"
        if l["type"] == "image":
            dims = taille_image(p)
            if dims:
                w, h = dims
                msg += f", {w}×{h}"
                try:
                    rw, rh = [int(x) for x in l["ratio"].split(":")]
                    if abs(w / h - rw / rh) > 0.05:
                        msg += f"  ⚠️ ratio {w / h:.2f} au lieu de {l['ratio']} (le jeu recadre ; recaler les zones)"; avert += 1
                except ValueError:
                    pass
                if l["ratio"] == "16:9" and w < 1280:
                    msg += "  ⚠️ moins de 1280 px de large (flou sur TBI)"; avert += 1
        elif ko > 6 * 1024:
            msg += "  ⚠️ plus de 6 Mo"; avert += 1
        print(msg)
    for dossier in ("assets/images/decors", "assets/images/personnages", "assets/images/ui", "assets/videos"):
        d = os.path.join(JEU, dossier)
        for n in sorted(os.listdir(d)) if os.path.isdir(d) else []:
            rel = os.path.normpath(os.path.join(dossier, n))
            if rel not in attendus and not n.startswith(".") and n not in ("icone.svg",) and not n.endswith(".vtt"):
                print(f"⚠️ inconnu    {rel} : nom inattendu, le jeu ne le verra pas (minuscules, sans accent ni espace ; voir medias.csv)"); avert += 1
    print(f"\n{presents} présent(s), {manquants} manquant(s) (secours actif), {avert} avertissement(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
