# 🎞️ Médias du jeu — Le Sceau de la République

**Tout est facultatif.** Sans aucun fichier, le jeu affiche ses décors et ses personnages
dessinés en SVG, animés : c'est le mode par défaut, entièrement jouable. Déposer un fichier
portant exactement le nom attendu le fait apparaître à la place du dessin — **aucun code à
modifier**.

La page de vérification ([verifier.html](../../verifier.html#constitution)) et ⚙️ Réglages →
« 🔍 Vérifier les fichiers présents » affichent, pour chaque emplacement, ce qui est en place
et le nom exact à utiliser.

## Règles de nommage

- Noms **en minuscules, sans espace ni accent** : `salle1.jpg`, jamais `Salle 1.JPG`.
- Vidéo **et** image du même nom : la vidéo s'affiche, l'image lui sert d'affiche.
- Un fichier `.vtt` du même nom qu'une vidéo est chargé automatiquement comme sous-titres.
- Les décors filmés sont joués **muets** (un bouton 🔇 permet d'activer le son).
- Supprimer un fichier ramène le dessin par défaut.

| | Formats acceptés |
|---|---|
| Décors et cinématiques | `.mp4` (H.264) ou `.webm`, 16:9, 15 à 30 s en boucle, < 20 Mo — ou `.jpg` / `.png` / `.webp` 16:9 |
| Personnages | `.mp4` en boucle, cadrage portrait vertical — ou `.png` carré à fond transparent (`.gif` animé accepté) |
| Illustrations d'énigmes et documents | `.jpg` (ou `.png` / `.webp`) |

---

## 1. Décors et cinématiques — `assets/videos/` et `assets/images/decors/`

| Emplacement | Nom du fichier | Où il apparaît |
|---|---|---|
| Cinématique d'ouverture | `intro.mp4` | Plein écran au clic sur « Ouvrir le coffre ». Sautée si absente. |
| Salle 1 — La cour du Palais-Royal | `salle1.mp4` *ou* `salle1.jpg` | Décor de fond de la salle, et fond de l'écran d'accueil |
| Salle 2 — La salle des Textes | `salle2.mp4` *ou* `salle2.jpg` | Décor de fond de la salle |
| Salle 3 — L'hémicycle | `salle3.mp4` *ou* `salle3.jpg` | Décor de fond de la salle |
| Salle 4 — La navette parlementaire | `salle4.mp4` *ou* `salle4.jpg` | Décor de fond de la salle |
| Salle 5 — La salle des séances du Conseil constitutionnel | `salle5.mp4` *ou* `salle5.jpg` | Décor de fond de la salle |
| Cinématique de fin | `final.mp4` | Plein écran quand le coffre s'ouvre. Sautée si absente. |

Les vidéos vont dans `assets/videos/`, les images dans `assets/images/decors/`.

## 2. Personnages — `assets/videos/personnages/` et `assets/images/personnages/`

| Personnage | Rôle | Nom du fichier | Variante « parle » |
|---|---|---|---|
| Monsieur Berthier | Gardien-archiviste du Palais-Royal | `berthier.mp4` *ou* `berthier.png` | `berthier-parle.mp4` (facultative) |
| Nour | Déléguée de classe, 10 ans | `nour.mp4` *ou* `nour.png` | `nour-parle.mp4` (facultative) |
| Madame Ferrand | Députée à l'Assemblée nationale | `ferrand.mp4` *ou* `ferrand.png` | `ferrand-parle.mp4` (facultative) |
| Maître Sylla | Juriste au Conseil constitutionnel | `sylla.mp4` *ou* `sylla.png` | `sylla-parle.mp4` (facultative) |

La variante `-parle` est jouée pendant que le personnage parle ; sans elle, la vidéo au repos
est conservée.

## 3. Illustrations d'énigmes — `assets/images/cartes/`

Chaque illustration est **facultative** : sans fichier, l'énigme reste entièrement jouable et
un encadré discret rappelle le nom attendu. Ces emplacements sont déclarés dans
`assets/data/enigmes.json` (champ `media`) : en ajouter un ne demande aucune modification de code.

| Énigme | Nom du fichier | Légende prévue |
|---|---|---|
| 1-1 — La règle du jeu (salle 1) | `e1-1.jpg` | Le coffre scellé le 4 octobre 1958 |
| 1-3 — Les trois pouvoirs (salle 1) | `e1-3.jpg` | La séparation des pouvoirs |
| 2-1 — Les quatre textes, dans l'ordre (salle 2) | `e2-1.jpg` | Le bloc de constitutionnalité |
| 3-1 — Qui fait quoi dans la République ? (salle 3) | `e3-1.jpg` | L'organisation des pouvoirs |
| 4-2 — Le parcours d'une loi (salle 4) | `e4-2.jpg` | Le parcours d'une loi, étape par étape |
| 5-1 — Les articles 1 et 2 (salle 5) | `e5-1.jpg` | Les symboles de la République |
| 5-3 — La Constitution dans ton quotidien (salle 5) | `e5-3.jpg` | La Constitution dans ton quotidien |

Pour qu'une illustration soit une **vidéo**, ajoutez `"type": "video"` dans le bloc `media` de
l'énigme et déposez `<nom>.mp4` dans `assets/videos/`.

## 4. Documents des leçons — `assets/images/documents/`

Les leçons de la bibliothèque 📚 utilisent pour l'instant des **documents-textes** (citations
sourcées) : aucun fichier image n'est attendu. Pour remplacer un document-texte par une image,
passez son `type` à `"image"` dans `assets/data/lecons.json` et déposez `<id-de-la-leçon>.jpg`
dans `assets/images/documents/`.

## 5. Où trouver des images libres de droits

- **Conseil constitutionnel** — photographies du Palais-Royal et de la salle des séances.
- **Assemblée nationale** et **Sénat** — visuels de l'hémicycle et du palais du Luxembourg.
- **Wikimedia Commons** — vérifiez la licence de chaque fichier avant de le publier.

Vérifiez toujours les droits avant de publier le dépôt en ligne : les fichiers déposés ici
sont accessibles publiquement.
