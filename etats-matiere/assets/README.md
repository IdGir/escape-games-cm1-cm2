# Médias attendus — La Fabrique des états

**Tout est facultatif.** Sans aucun fichier, le jeu est entièrement jouable : décors et personnages sont dessinés
en SVG animé (`js/decors.js`, `js/personnages.js`). Un fichier déposé au bon endroit, avec le bon nom, remplace
automatiquement le dessin (cascade : vidéo → image → dessin). ⚙️ Réglages → « Vérifier les fichiers présents »
et la page [verifier.html](../../verifier.html#etats-matiere) listent l'état de chaque emplacement.

Règles du projet : **lieux** = photographies réelles ou dessins (licence libre : Wikimedia Commons…) ; **personnages** =
réalistes mais **jamais de personnes réelles** (tous les personnages sont inventés). La Fabrique des états est imaginaire :
pour les décors, prendre des photos libres d'une halle industrielle en brique, d'un toit avec abri météo, d'une cuisine
collective, d'un château d'eau, sans nommer un lieu réel comme s'il s'agissait de la Fabrique. **Schémas** (bouteille avant
et après le congélateur, changements d'état, cycle de l'eau) : **dessinés**, jamais générés par IA — ceux du jeu sont en
SVG dans `assets/data/enigmes.json` (énigme 4-3) et `assets/data/lecons.json`. Une image générée ne doit jamais montrer
la vapeur d'eau comme un nuage blanc en l'appelant « vapeur ». Crédits dans `assets/medias/CREDITS-medias.md`.

## Décors et cinématiques

| Fichier | Où il apparaît | Sans fichier | Contenu suggéré |
|---|---|---|---|
| `videos/intro.mp4` | cinématique au clic sur « Entrer dans la Fabrique » | sautée | une usine de brique au bord d'un lac, après l'orage |
| `videos/salle1.mp4` ou `images/decors/salle1.jpg` | salle 1, le hall des cuves, et l'écran d'accueil | dessin `hall` | une halle de brique avec des cuves, des tuyaux, un pupitre |
| `videos/salle2.mp4` ou `images/decors/salle2.jpg` | salle 2, la terrasse du ballon-sonde | dessin `terrasse` | un abri météo, une girouette, un ballon-sonde (photo libre) |
| `videos/salle3.mp4` ou `images/decors/salle3.jpg` | salle 3, la glacerie de Paolo | dessin `glacerie` | un congélateur givré, une casserole sur une plaque, des thermomètres |
| `videos/salle4.mp4` ou `images/decors/salle4.jpg` | salle 4, la cuisine de Fatou | dessin `cuisine` | une cuisine collective avec une balance de cuisine |
| `videos/salle5.mp4` ou `images/decors/salle5.jpg` | salle 5, le château d'eau de Ninon | dessin `tour` | un lac, une rivière, des nuages vus de haut (photo libre) |
| `videos/final.mp4` | cinématique de fin (la Fabrique redémarre) | sautée | des fenêtres d'usine qui s'allument, un ciel qui se dégage |
| `videos/bande-annonce.mp4` · `images/affiche.jpg` (+ `affiche-fond.jpg`) | carte du jeu sur l'accueil du site | — | à faire avec `outils-medias/affiches.py` puis `bande-annonce.py` (captures des décors dessinés) |

Format conseillé : vidéo MP4 (H.264) 16/9, 1280 × 720, moins de 20 Mo ; image JPG 1600 × 600 environ, moins de 3 Mo.

## Personnages (tous inventés)

| Clé | Personnage | Image | Vidéo au repos | Vidéo qui parle |
|---|---|---|---|---|
| `ines` | Inès, ingénieure de la Fabrique (femme, casque blanc, gilet orange) | `images/personnages/ines.png` | `videos/personnages/ines.mp4` | `videos/personnages/ines-parle.mp4` |
| `bastien` | Bastien, agent météo (homme, parka bleue, anémomètre) | `images/personnages/bastien.png` | `videos/personnages/bastien.mp4` | `videos/personnages/bastien-parle.mp4` |
| `paolo` | Paolo, glacier (homme, veste et calot blancs) | `images/personnages/paolo.png` | `videos/personnages/paolo.mp4` | `videos/personnages/paolo-parle.mp4` |
| `fatou` | Fatou, cuisinière (femme, tablier vert, foulard) | `images/personnages/fatou.png` | `videos/personnages/fatou.mp4` | `videos/personnages/fatou-parle.mp4` |
| `ninon` | Ninon, gardienne du château d'eau (femme âgée, veste verte, lunettes) | `images/personnages/ninon.png` | `videos/personnages/ninon.mp4` | `videos/personnages/ninon-parle.mp4` |

Image PNG en pied, fond uni ou transparent, format portrait (environ 600 × 960).

## Illustrations d'énigmes (`images/cartes/`) — facultatif

Aucune énigme n'a de bloc `media`. Idées : `e2-3.jpg` un verre retourné enfoncé dans une bassine (photo libre) ;
`e5-1.jpg` des objets qui flottent ou coulent dans un bac d'eau (photo libre). Ajouter alors
`"media": {"base": "e2-3", "legende": "…", "source": "…"}` dans `enigmes.json`. Ne pas remplacer le schéma 4-3 ni les
thermomètres (3-2, dessinés par le moteur) par des images.
