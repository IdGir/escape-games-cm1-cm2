# -*- coding: utf-8 -*-
"""Génère traite-colonies/assets/medias/medias.json (manifeste lu par outils-medias/produire-medias.ps1).
Lancer : python gen_medias.py <dossier assets/medias>
Sujet sensible : aucune image de personnes réduites en esclavage, de chaînes, de violence ou de navire chargé de captifs.
Décors : archives imaginaires (IA, sans personne). Documents réels : photos Wikimedia Commons (crédits automatiques).
Cartes et schémas : jamais par IA (dessinés en SVG)."""
import json, os, sys

DEC = ("Photorealistic cinematic wide shot for a children's educational history game, 16:9 composition, soft natural autumn light, "
       "rich detail, calm and respectful atmosphere, no people at all. No text, no lettering, no readable writing, no signage, no watermark. Scene: ")
POR = ("Realistic digital painting portrait for a children's educational game. Completely fictional person, not resembling any real or public figure. "
       "Waist-up, three-quarter view, kind and serious expression, soft warm key light from the left, plain deep black background, vertical portrait framing, "
       "sharp focus on the eyes. No text, no lettering, no logo, no watermark. Subject: ")
REPOS = "Subtle idle animation of the portrait: slow natural breathing, occasional gentle blinking, very slight head movement. Static camera, unchanged framing, black background stays black. Calm, loopable, no speech."
PARLE = "The person speaks calmly to the camera: natural mouth movement, small head nods, gentle serious expression, occasional blinking. Static camera, unchanged framing, black background stays black."
PUSH = "Slow cinematic push-in, gentle steady camera move forward, soft light and floating dust, no people appearing, nothing new invented, photorealistic, calm. No text appears."

DECORS = [
    ("salle1", "Salle 1, la salle des cartes", "an old archive map room with tall wooden plan chests with wide flat drawers, a reading table with a green banker's lamp and a magnifying glass, a large antique map of the Atlantic Ocean framed on the wall, parquet floor."),
    ("salle2", "Salle 2, le cabinet des registres", "an archive study lined with shelves of old leather-bound ledgers, a wooden lectern with an open handwritten logbook, a model of an 18th-century merchant sailing ship under a glass case, a wall clock."),
    ("salle3", "Salle 3, le fonds des colonies", "a quiet archive reading room on a rainy day, rain on tall windows, a wooden table with an old map-like plan of a sugar estate and an old law book under a glass case, a green lamp."),
    ("salle4", "Salle 4, le musée du port", "a small harbour history museum gallery, lit display cases with sugar, coffee beans, cocoa pods, cotton and indigo, wooden barrels and burlap sacks, a framed map of a coastline on the wall, parquet floor."),
    ("salle5", "Salle 5, la salle de lecture", "a large bright archive reading hall with tall arched windows, long wooden tables with green lamps, a wooden easel holding a blank timeline board, a closed old ledger with a brass clasp on the table."),
]
PERSOS = [
    ("ines", "Inès, archiviste", "a French woman archivist in her forties, long dark hair, round glasses, grey archivist's coat over a red scarf, holding a cardboard archive folder."),
    ("malik", "Malik, historien venu de Dakar", "a Senegalese man historian in his fifties, short black hair and short beard, brown jacket over a white shirt, holding a dark blue notebook."),
    ("celia", "Célia, historienne venue de Guadeloupe", "a Black woman historian from Guadeloupe in her thirties, curly black hair, green dress with a small golden pendant, holding an open book."),
    ("margot", "Margot, conservatrice du musée du port", "a French woman museum curator in her thirties, auburn hair in a bun, slate-blue suit, white cotton museum gloves."),
    ("theo", "Théo, élève de l'atelier d'enquête", "a 10-year-old French schoolboy with short ginger hair, red sweatshirt, small backpack straps, holding a paper worksheet, eager and serious."),
]


def main(dest):
    images, videos = [], []
    for cle, nom, scene in DECORS:
        images.append({"cle": cle, "nom": nom + " (archives imaginaires)", "cible": f"assets/images/decors/{cle}.jpg", "prompt": DEC + scene, "taille": "1344x768"})
        videos.append({"cle": cle + "-video", "nom": nom + " (vidéo)", "cible": f"assets/videos/{cle}.mp4", "depuis": cle, "prompt": PUSH, "largeur": 1152, "hauteur": 768})
    images.append({"cle": "cine-intro", "nom": "Cinématique d'ouverture (image de départ)", "cible": "assets/images/decors/intro.jpg",
                   "prompt": DEC + "the stone facade of an old archive building on a harbour quay at dawn, mist over the water, a few moored small modern boats, warm lights behind the windows.", "taille": "1344x768"})
    images.append({"cle": "cine-final", "nom": "Cinématique de fin (image de départ)", "cible": "assets/images/decors/final.jpg",
                   "prompt": DEC + "close-up of an old leather ledger being closed on a wooden table, a brass clasp, a green lamp, soft golden light.", "taille": "1344x768"})
    images.append({"cle": "affiche-fond", "nom": "Affiche du jeu : fond sans texte", "cible": "assets/images/affiche-fond.jpg",
                   "prompt": DEC + "Keep the left third of the image calm and slightly darker, to leave room for a title. An old archive room with shelves of leather ledgers, an antique Atlantic map and a green lamp on a table, golden dust in the light.", "taille": "1344x768"})
    for cle, nom, sujet in PERSOS:
        images.append({"cle": cle, "nom": nom, "cible": f"assets/images/personnages/{cle}.png", "prompt": POR + sujet, "taille": "768x1024"})
        videos.append({"cle": cle + "-repos", "nom": nom + " (au repos)", "cible": f"assets/videos/personnages/{cle}.mp4", "depuis": cle, "prompt": REPOS, "largeur": 768, "hauteur": 1152})
        videos.append({"cle": cle + "-parle", "nom": nom + " (parle)", "cible": f"assets/videos/personnages/{cle}-parle.mp4", "depuis": cle, "prompt": PARLE, "largeur": 768, "hauteur": 1152})
    videos.append({"cle": "intro", "nom": "Cinématique d'ouverture", "cible": "assets/videos/intro.mp4", "depuis": "cine-intro",
                   "prompt": "Slow cinematic push-in towards the archive building, mist drifting over the water, light slowly rising, no people appearing, photorealistic, calm. No text appears.", "largeur": 1152, "hauteur": 768})
    videos.append({"cle": "final", "nom": "Cinématique de fin", "cible": "assets/videos/final.mp4", "depuis": "cine-final",
                   "prompt": "The ledger closes slowly and the brass clasp shuts, the lamp light glows softly, static camera, photorealistic, calm. No text appears.", "largeur": 1152, "hauteur": 768})
    videos.append({"cle": "bande-annonce-ouverture", "nom": "Bande-annonce : plan d'ouverture", "cible": "assets/videos/bande-annonce-ouverture.mp4", "depuis": "affiche-fond",
                   "prompt": PUSH, "largeur": 1152, "hauteur": 768})
    photos = [
        {"cle": "e3-2", "cible": "assets/images/cartes/e3-2.jpg", "recherche": "Code noir 1685 edit page titre", "lieu": "Le Code noir, page de titre d'une édition ancienne (document)", "paysage": False, "rang": 1},
        {"cle": "e5-2", "cible": "assets/images/cartes/e5-2.jpg", "recherche": "Toussaint Louverture portrait gravure", "lieu": "Toussaint Louverture, gravure ancienne (document)", "paysage": False, "rang": 1},
    ]
    m = {"_commentaire": "Manifeste des médias du jeu Les Archives du port. Sujet sensible : aucune image de personnes réduites en esclavage, de chaînes, de violence ni de navire chargé de captifs. Décors : archives imaginaires générées par l'API Agnes, sans personne. Personnages inventés (Agnes). Documents réels : Wikimedia Commons. Cartes et schémas jamais générés par IA. Généré par tests/donnees/gen_medias.py.",
         "jeu": "traite-colonies", "titre": "Les Archives du port",
         "api": {"nom": "Agnes AI", "base": "https://apihub.agnes-ai.com", "modele_image": "agnes-image-2.1-flash", "modele_video": "agnes-video-v2.0"},
         "negatif": "text, letters, words, watermark, logo, signature, distorted hands, extra fingers, deformed face, blurry, low quality, violence, chains, shackles, blood, slaves, captives, slave ship, caricature, celebrity likeness",
         "photos": photos, "images": images, "videos": videos}
    os.makedirs(dest, exist_ok=True)
    json.dump(m, open(os.path.join(dest, "medias.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"medias.json : {len(photos)} photos, {len(images)} images, {len(videos)} vidéos")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
