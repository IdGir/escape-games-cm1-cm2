# Médias attendus — Le Grand Prix de l'observatoire

**Tout est facultatif.** Sans aucun fichier, le jeu est entièrement jouable : décors et personnages sont dessinés
en SVG animé (`js/decors.js`, `js/personnages.js`). Un fichier déposé au bon endroit, avec le bon nom, remplace
automatiquement le dessin (cascade : vidéo → image → dessin). ⚙️ Réglages → « Vérifier les fichiers présents »
et la page [verifier.html](../../verifier.html#mouvement) listent l'état de chaque emplacement.

Règles du projet : **lieux** = photographies réelles ou dessins (licence libre : Wikimedia Commons…) ; **personnages** =
réalistes mais **jamais de personnes réelles** (tous les personnages sont inventés). **Schémas** (ruban gradué, reports du
décamètre, circuit, Soleil et planètes) : **dessinés**, jamais générés par IA. Aucun média n'a été produit : la production
se fait seulement avec l'accord de l'enseignant. Crédits dans `assets/medias/CREDITS-medias.md`.

## Décors et cinématiques

| Fichier | Où il apparaît | Sans fichier | Contenu suggéré |
|---|---|---|---|
| `videos/intro.mp4` | cinématique au clic sur « Rejoindre le Grand Prix » | sautée | un plateau au matin, une coupole blanche, des plots renversés |
| `videos/salle1.mp4` ou `images/decors/salle1.jpg` | salle 1, la ligne de départ, et l'écran d'accueil | dessin `depart` | une piste en pente sur un plateau herbeux, des plots, une banderole (photo libre) |
| `videos/salle2.mp4` ou `images/decors/salle2.jpg` | salle 2, le stand des chronométreurs | dessin `stand` | une tente de course, une horloge, des chronomètres |
| `videos/salle3.mp4` ou `images/decors/salle3.jpg` | salle 3, le tableau des temps | dessin `tableau` | un panneau d'affichage, une petite tribune, des vélos |
| `videos/salle4.mp4` ou `images/decors/salle4.jpg` | salle 4, la coupole de l'observatoire | dessin `coupole` | l'intérieur d'une coupole d'observatoire avec sa lunette (photo libre d'un observatoire réel, sans le nommer comme lieu du jeu) |
| `videos/salle5.mp4` ou `images/decors/salle5.jpg` | salle 5, le quai du petit train | dessin `quai` | un petit train touristique à quai |
| `videos/final.mp4` | cinématique de fin | sautée | un podium, des drapeaux à damier |

Format conseillé : vidéo MP4 (H.264) 16/9, 1280 × 720, moins de 20 Mo ; image JPG 1600 × 600 environ, moins de 3 Mo.

## Personnages (tous inventés)

| Clé | Personnage | Image | Vidéo au repos | Vidéo qui parle |
|---|---|---|---|---|
| `margaux` | Margaux, commissaire de course (femme, casquette rouge, gilet jaune, drapeau à damier) | `images/personnages/margaux.png` | `videos/personnages/margaux.mp4` | `videos/personnages/margaux-parle.mp4` |
| `yanis` | Yanis, pilote de caisse à savon (garçon ou jeune homme, combinaison rouge, casque blanc) | `images/personnages/yanis.png` | `videos/personnages/yanis.mp4` | `videos/personnages/yanis-parle.mp4` |
| `salome` | Salomé, cycliste (femme, maillot vert et jaune, casque de vélo) | `images/personnages/salome.png` | `videos/personnages/salome.mp4` | `videos/personnages/salome-parle.mp4` |
| `leonie` | Léonie, astronome (femme rousse, lunettes, veste bleu nuit) | `images/personnages/leonie.png` | `videos/personnages/leonie.mp4` | `videos/personnages/leonie-parle.mp4` |
| `hugo` | Hugo, contrôleur du petit train (homme, veste bleu marine, casquette, sifflet) | `images/personnages/hugo.png` | `videos/personnages/hugo.mp4` | `videos/personnages/hugo-parle.mp4` |

Image PNG en pied, fond uni ou transparent, format portrait (environ 600 × 960).

## Illustrations d'énigmes (`images/cartes/`) — facultatif

Aucune énigme n'a de bloc `media`. Idées : `e1-1.jpg` un décamètre et un mètre ruban (photo libre) ; `e4-1.jpg` une grande
roue (photo libre). Ne pas remplacer les schémas 1-3 et 4-2 par des images.
