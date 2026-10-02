# Médias attendus — L'Atelier de Léonard à Amboise

**Tout est facultatif.** Sans aucun fichier, le jeu est entièrement jouable : décors et personnages sont dessinés
en SVG animé (`js/decors.js`, `js/personnages.js`). Un fichier déposé au bon endroit, avec le bon nom, remplace
automatiquement le dessin (cascade : vidéo → image → dessin). ⚙️ Réglages → « Vérifier les fichiers présents »
et la page [verifier.html](../../verifier.html#renaissance) listent l'état de chaque emplacement.

Règles du projet : **lieux réels** = photographies réelles (domaine public ou licence libre : Wikimedia Commons…),
jamais d'image inventée d'un lieu existant (château d'Amboise, Clos Lucé, Chambord, Blois) ; **personnages** =
réalistes mais **jamais de personnes réelles** (pas de portrait de Léonard ou de François Ier généré par IA : utiliser
plutôt une œuvre d'époque du domaine public, avec son crédit). Crédits dans `assets/medias/CREDITS-medias.md`.

## Décors et cinématiques

| Fichier | Où il apparaît | Sans fichier | Contenu suggéré |
|---|---|---|---|
| `videos/intro.mp4` | cinématique au clic sur « Chercher les pages » | sautée | des pages de carnet emportées par le vent au-dessus de la Loire |
| `videos/salle1.mp4` ou `images/decors/salle1.jpg` | salle 1, l'imprimerie | dessin `imprimerie` | une presse à bras ancienne (photo de musée) |
| `videos/salle2.mp4` ou `images/decors/salle2.jpg` | salle 2, la grande salle d'Amboise | dessin `salle` | photo réelle : une salle du château royal d'Amboise |
| `videos/salle3.mp4` ou `images/decors/salle3.jpg` | salle 3, l'atelier du Cloux, et l'écran d'accueil | dessin `atelier` | photo réelle : le Clos Lucé |
| `videos/salle4.mp4` ou `images/decors/salle4.jpg` | salle 4, le cabinet des plans | dessin `plans` | photo réelle : Chambord ou l'escalier François Ier de Blois |
| `videos/salle5.mp4` ou `images/decors/salle5.jpg` | salle 5, la galerie des tableaux | dessin `galerie` | une galerie de château ou de musée |
| `videos/final.mp4` | cinématique de fin (le carnet est complet) | sautée | un carnet relié qui se referme, une salamandre |
| `videos/bande-annonce.mp4` · `images/affiche.jpg` (+ `affiche-fond.jpg`) | carte du jeu sur l'accueil du site | — | **déjà fournis**, faits à partir des décors dessinés ; à refaire avec `outils-medias/affiches.py` puis `bande-annonce.py` si des photos sont ajoutées |

Format conseillé : vidéo MP4 (H.264) 16/9, 1280 × 720, moins de 20 Mo ; image JPG 1600 × 600 environ, moins de 3 Mo.

## Personnages (tous inventés)

| Clé | Personnage | Image | Vidéo au repos | Vidéo qui parle |
|---|---|---|---|---|
| `tommaso` | Tommaso, apprenti de Léonard (garçon, 12 ans) | `images/personnages/tommaso.png` | `videos/personnages/tommaso.mp4` | `videos/personnages/tommaso-parle.mp4` |
| `jacquet` | Maître Jacquet, imprimeur | `images/personnages/jacquet.png` | `videos/personnages/jacquet.mp4` | `videos/personnages/jacquet-parle.mp4` |
| `helene` | Dame Hélène, dame de la cour | `images/personnages/helene.png` | `videos/personnages/helene.mp4` | `videos/personnages/helene-parle.mp4` |
| `colombe` | Colombe, fille du maître maçon (fille, 11 ans) | `images/personnages/colombe.png` | `videos/personnages/colombe.mp4` | `videos/personnages/colombe-parle.mp4` |
| `bastien` | Bastien, jeune peintre de la cour | `images/personnages/bastien.png` | `videos/personnages/bastien.mp4` | `videos/personnages/bastien-parle.mp4` |

Image PNG en pied, fond uni ou transparent, format portrait (environ 600 × 960). Costumes : vers 1515-1520.

## Illustrations d'énigmes (`images/cartes/`) — facultatif

Aucune énigme n'a de bloc `media`. Idées : `e3-1.jpg` une page de carnet de Léonard (domaine public) ; `e4-1.jpg`
l'escalier à double révolution de Chambord (photo libre) ; `e5-1.jpg` un tableau italien construit en perspective
(domaine public). Ajouter alors `"media": {"base": "e3-1", "legende": "…", "source": "…"}` dans `enigmes.json`.
