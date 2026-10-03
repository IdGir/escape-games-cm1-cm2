# Médias attendus — Le Grand Repas du chef

**Tout est facultatif.** Sans aucun fichier, le jeu est entièrement jouable : décors et personnages sont dessinés
en SVG animé (`js/decors.js`, `js/personnages.js`). Un fichier déposé au bon endroit, avec le bon nom, remplace
automatiquement le dessin (cascade : vidéo → image → dessin). ⚙️ Réglages → « Vérifier les fichiers présents »
et la page [verifier.html](../../verifier.html#alimentation) listent l'état de chaque emplacement.

Règles du projet : **lieux** = photographies réelles ou dessins (licence libre : Wikimedia Commons…) ; **personnages** =
réalistes mais **jamais de personnes réelles** (tous les personnages sont inventés). **Schémas anatomiques** (mâchoire,
appareil digestif, cœur) : **dessinés**, jamais générés par IA — ceux du jeu sont en SVG dans `assets/data/enigmes.json`
(énigmes 3-2 et 4-1) et `assets/data/lecons.json`. Pas de photo d'élève ni de corps réel. Crédits dans
`assets/medias/CREDITS-medias.md`.

## Décors et cinématiques

| Fichier | Où il apparaît | Sans fichier | Contenu suggéré |
|---|---|---|---|
| `videos/intro.mp4` | cinématique au clic sur « Entrer en cuisine » | sautée | une cuisine de restaurant qui s'anime, un coffre à cinq cadenas |
| `videos/salle1.mp4` ou `images/decors/salle1.jpg` | salle 1, la cour du potager et du poulailler | dessin `potager` | un potager et un poulailler (photo libre) |
| `videos/salle2.mp4` ou `images/decors/salle2.jpg` | salle 2, la salle des menus | dessin `menus` | un tableau noir de restaurant, des fiches |
| `videos/salle3.mp4` ou `images/decors/salle3.jpg` | salle 3, la table de dégustation, et l'écran d'accueil | dessin `degustation` | une table nappée : pain, fruits, légumes |
| `videos/salle4.mp4` ou `images/decors/salle4.jpg` | salle 4, le cabinet du Grand Tunnel | dessin `cabinet` | un cabinet médical avec une maquette pédagogique du corps (photo d'objet, sans personne) |
| `videos/salle5.mp4` ou `images/decors/salle5.jpg` | salle 5, la salle d'entraînement | dessin `entrainement` | un vélo de course sur home-trainer |
| `videos/final.mp4` | cinématique de fin (le coffre s'ouvre) | sautée | un livre de recettes qui s'ouvre, un repas servi |
| `videos/bande-annonce.mp4` · `images/affiche.jpg` (+ `affiche-fond.jpg`) | carte du jeu sur l'accueil du site | — | **déjà fournis**, faits à partir des décors dessinés ; à refaire avec `outils-medias/affiches.py` puis `bande-annonce.py` si des photos sont ajoutées |

Format conseillé : vidéo MP4 (H.264) 16/9, 1280 × 720, moins de 20 Mo ; image JPG 1600 × 600 environ, moins de 3 Mo.

## Personnages (tous inventés)

| Clé | Personnage | Image | Vidéo au repos | Vidéo qui parle |
|---|---|---|---|---|
| `rosalie` | Rosalie Bompard, cheffe du Grand Couvert (femme) | `images/personnages/rosalie.png` | `videos/personnages/rosalie.mp4` | `videos/personnages/rosalie-parle.mp4` |
| `nathan` | Nathan, commis : potager et poulailler (garçon, jeune adulte) | `images/personnages/nathan.png` | `videos/personnages/nathan.mp4` | `videos/personnages/nathan-parle.mp4` |
| `ines` | Docteure Inès Morel, médecin de l'équipe cycliste (femme) | `images/personnages/ines.png` | `videos/personnages/ines.mp4` | `videos/personnages/ines-parle.mp4` |
| `basile` | Basile Ndiaye, coureur cycliste (homme) | `images/personnages/basile.png` | `videos/personnages/basile.mp4` | `videos/personnages/basile-parle.mp4` |

Image PNG en pied, fond uni ou transparent, format portrait (environ 600 × 960). Lou, la fille de la cheffe, n'apparaît que
dans les données (toise, pouls) : pas d'image.

## Illustrations d'énigmes (`images/cartes/`) — facultatif

Aucune énigme n'a de bloc `media`. Idées : `e1-1.jpg` un poussin sur une balance de cuisine (photo libre) ; `e5-1.jpg` deux
doigts posés sur un poignet (photo libre, sans visage). Ajouter alors `"media": {"base": "e1-1", "legende": "…", "source": "…"}`
dans `enigmes.json`. Ne pas remplacer les schémas 3-2 et 4-1 par des images.
