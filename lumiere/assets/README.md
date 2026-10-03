# Médias attendus — Le Phare de l'île Lumière

**Tout est facultatif.** Sans aucun fichier, le jeu est entièrement jouable : décors et personnages sont dessinés
en SVG animé (`js/decors.js`, `js/personnages.js`). Un fichier déposé au bon endroit, avec le bon nom, remplace
automatiquement le dessin (cascade : vidéo → image → dessin). ⚙️ Réglages → « Vérifier les fichiers présents »
et la page [verifier.html](../../verifier.html#lumiere) listent l'état de chaque emplacement.

Règles du projet : **lieux** = photographies réelles ou dessins (licence libre : Wikimedia Commons…) ; **personnages** =
réalistes mais **jamais de personnes réelles** (tous les personnages sont inventés). L'île Lumière est imaginaire : pour
les décors, prendre des photos libres d'un phare et de sa lanterne (par exemple un phare breton), sans nommer un phare
réel comme s'il s'agissait de l'île. **Schémas** (trajet de la lumière, ombres, cour vue de dessus, phases de la Lune) :
**dessinés**, jamais générés par IA — ceux du jeu sont en SVG dans `assets/data/enigmes.json` (énigmes 1-2, 3-1, 4-3, 5-1)
et `assets/data/lecons.json`. Aucune photo du Soleil prise en le regardant. Crédits dans `assets/medias/CREDITS-medias.md`.

## Décors et cinématiques

| Fichier | Où il apparaît | Sans fichier | Contenu suggéré |
|---|---|---|---|
| `videos/intro.mp4` | cinématique au clic sur « Monter dans le phare » | sautée | un phare éteint au crépuscule, un voilier au large |
| `videos/salle1.mp4` ou `images/decors/salle1.jpg` | salle 1, la lanterne du phare | dessin `lanterne` | l'intérieur d'une lanterne de phare : lentille de Fresnel, vitres (photo libre) |
| `videos/salle2.mp4` ou `images/decors/salle2.jpg` | salle 2, l'atelier des vitres | dessin `atelier` | un établi avec plaques de verre, papier calque, planches |
| `videos/salle3.mp4` ou `images/decors/salle3.jpg` | salle 3, la chambre aux ombres | dessin `chambre` | un théâtre d'ombres : drap blanc, lampe, silhouettes (sans visage d'enfant) |
| `videos/salle4.mp4` ou `images/decors/salle4.jpg` | salle 4, la cour du cadran solaire | dessin `cour` | un cadran solaire au sol ou un gnomon et son ombre (photo libre) |
| `videos/salle5.mp4` ou `images/decors/salle5.jpg` | salle 5, la galerie du phare, et l'écran d'accueil | dessin `galerie` | la mer la nuit sous la pleine lune, un voilier au loin |
| `videos/final.mp4` | cinématique de fin (le phare se rallume) | sautée | un faisceau de phare qui balaie la mer |
| `videos/bande-annonce.mp4` · `images/affiche.jpg` (+ `affiche-fond.jpg`) | carte du jeu sur l'accueil du site | — | **déjà fournis**, faits à partir des décors dessinés ; à refaire avec `outils-medias/affiches.py` puis `bande-annonce.py` si des photos sont ajoutées |

Format conseillé : vidéo MP4 (H.264) 16/9, 1280 × 720, moins de 20 Mo ; image JPG 1600 × 600 environ, moins de 3 Mo.

## Personnages (tous inventés)

| Clé | Personnage | Image | Vidéo au repos | Vidéo qui parle |
|---|---|---|---|---|
| `maelle` | Maëlle, gardienne du phare (femme) | `images/personnages/maelle.png` | `videos/personnages/maelle.mp4` | `videos/personnages/maelle-parle.mp4` |
| `salome` | Salomé, ingénieure en signalisation maritime (femme) | `images/personnages/salome.png` | `videos/personnages/salome.mp4` | `videos/personnages/salome-parle.mp4` |
| `nils` | Nils, 9 ans, neveu de la gardienne (garçon) | `images/personnages/nils.png` | `videos/personnages/nils.mp4` | `videos/personnages/nils-parle.mp4` |
| `achille` | Achille, horloger du port (homme âgé) | `images/personnages/achille.png` | `videos/personnages/achille.mp4` | `videos/personnages/achille-parle.mp4` |
| `yasmine` | Capitaine Yasmine, capitaine du voilier *La Mouette* (femme) | `images/personnages/yasmine.png` | `videos/personnages/yasmine.mp4` | `videos/personnages/yasmine-parle.mp4` |

Image PNG en pied, fond uni ou transparent, format portrait (environ 600 × 960).

## Illustrations d'énigmes (`images/cartes/`) — facultatif

Aucune énigme n'a de bloc `media`. Idées : `e2-2.jpg` une lampe derrière une vitre, un papier calque et un carton (photo
libre) ; `e4-1.jpg` un gnomon et son ombre dans une cour (photo libre). Ajouter alors
`"media": {"base": "e2-2", "legende": "…", "source": "…"}` dans `enigmes.json`. Ne pas remplacer les schémas 1-2, 3-1, 4-3
ni les dessins de la Lune (5-1) par des images.
