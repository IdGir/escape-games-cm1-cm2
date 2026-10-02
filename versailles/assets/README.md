# Médias attendus — De l'édit de Nantes à Versailles

**Tout est facultatif.** Sans aucun fichier, le jeu est entièrement jouable : décors et personnages sont dessinés
en SVG animé (`js/decors.js`, `js/personnages.js`). Un fichier déposé au bon endroit, avec le bon nom, remplace
automatiquement le dessin (cascade : vidéo → image → dessin). ⚙️ Réglages → « Vérifier les fichiers présents »
et la page [verifier.html](../../verifier.html#versailles) listent l'état de chaque emplacement.

Aucune photo ni vidéo n'est fournie avec ce jeu. Règles du projet : **lieux réels** = photographies réelles (domaine
public ou licence libre : Wikimedia Commons, château de Versailles en libre accès…), jamais d'image inventée d'un lieu
existant ; **personnages** = réalistes mais **jamais de personnes réelles** (pas de portrait de Louis XIV ou d'Henri IV
généré par IA : utiliser plutôt une œuvre d'époque du domaine public, avec son crédit). Le crédit va dans la légende
(`enigmes.json`, bloc `media`, champ `source`) et dans `assets/medias/CREDITS-medias.md`.

## Décors et cinématiques

| Fichier | Où il apparaît | Sans fichier | Contenu suggéré |
|---|---|---|---|
| `videos/intro.mp4` | cinématique plein écran au clic sur « Suivre le pli » | sautée | un pli scellé de cire rouge sur une table, à la lumière d'une bougie |
| `videos/salle1.mp4` ou `images/decors/salle1.jpg` | salle 1, l'imprimerie de Suzanne | dessin `imprimerie` | un atelier d'imprimerie du XVIe siècle (presse à bras) — photo d'une presse ancienne de musée |
| `videos/salle2.mp4` ou `images/decors/salle2.jpg` | salle 2, la rue des deux voisins | dessin `rue` | une rue à maisons à pans de bois d'une ville française |
| `videos/salle3.mp4` ou `images/decors/salle3.jpg` | salle 3, les jardins de Versailles, et l'écran d'accueil | dessin `jardins` | photo réelle : le parterre d'eau ou le bassin d'Apollon, château au fond |
| `videos/salle4.mp4` ou `images/decors/salle4.jpg` | salle 4, la chambre du roi | dessin `chambre` | photo réelle : la chambre du roi au château de Versailles |
| `videos/salle5.mp4` ou `images/decors/salle5.jpg` | salle 5, le cabinet du Conseil | dessin `conseil` | photo réelle : le cabinet du Conseil au château de Versailles |
| `videos/final.mp4` | cinématique plein écran à la fin (les sceaux se lèvent) | sautée | les sceaux de cire qui se brisent, le pli qui s'ouvre |
| `videos/bande-annonce.mp4` · `images/affiche.jpg` (+ `affiche-fond.jpg`) | carte du jeu sur l'accueil du site | — | **déjà fournis**, faits à partir des décors dessinés ; à refaire avec `outils-medias/affiches.py` puis `bande-annonce.py` si des photos ou vidéos sont ajoutées |

Format conseillé : vidéo MP4 (H.264) 16/9, 1280 × 720, moins de 20 Mo, boucle de 8 à 15 s sans son indispensable ;
image JPG 1600 × 600 environ, moins de 3 Mo (`.png` et `.webm` sont aussi acceptés).

## Personnages

| Clé | Personnage | Image | Vidéo au repos | Vidéo qui parle |
|---|---|---|---|---|
| `gabriel` | Gabriel, apprenti secrétaire du roi (garçon, 12 ans, 1682) | `images/personnages/gabriel.png` | `videos/personnages/gabriel.mp4` | `videos/personnages/gabriel-parle.mp4` |
| `suzanne` | Suzanne, imprimeuse protestante (1598) | `images/personnages/suzanne.png` | `videos/personnages/suzanne.mp4` | `videos/personnages/suzanne-parle.mp4` |
| `mathurin` | Mathurin, boulanger catholique (1598) | `images/personnages/mathurin.png` | `videos/personnages/mathurin.mp4` | `videos/personnages/mathurin-parle.mp4` |
| `margot` | Margot, aide-jardinière (fille, 11 ans, 1682) | `images/personnages/margot.png` | `videos/personnages/margot.mp4` | `videos/personnages/margot-parle.mp4` |
| `isabeau` | Dame Isabeau, dame de la cour (1682) | `images/personnages/isabeau.png` | `videos/personnages/isabeau.mp4` | `videos/personnages/isabeau-parle.mp4` |

Image PNG en pied, fond uni ou transparent, format portrait (environ 600 × 960). Costumes : fin du XVIe siècle pour
Suzanne et Mathurin (vêtements de travail simples), années 1680 pour Gabriel, Margot et Dame Isabeau ; aucun signe
religieux caricatural.

## Illustrations d'énigmes (`images/cartes/`) — facultatif

Aucune énigme n'a de bloc `media` pour l'instant. Pour en ajouter une, écrire dans `enigmes.json` :
`"media": {"base": "e3-1", "legende": "…", "source": "…"}` puis déposer `images/cartes/e3-1.jpg`. Idées :

| Fichier | Énigme | Contenu suggéré |
|---|---|---|
| `e2-1.jpg` | 2-1 Le texte du roi | la première page de l'édit de Nantes (Archives nationales, domaine public) |
| `e3-1.jpg` | 3-1 Le plan du domaine | un plan ancien des jardins de Versailles (domaine public) |
| `e3-3.jpg` | 3-3 Pourquoi le Soleil ? | la galerie des Glaces (photo libre) |

## Documents des leçons (`images/documents/`, format `.jpg` uniquement)

Les leçons utilisent des documents texte : aucune image n'est attendue. Pour ajouter une image à une leçon,
remplacer son bloc `document` par `{"type": "image", "fichier": "<nom>", "titre": "…", "source": "…"}` dans `lecons.json`.
