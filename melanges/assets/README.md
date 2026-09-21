# 🎞️ Médias du jeu — Le Laboratoire de Madame Mélange

**Tout est facultatif.** Sans aucun fichier, le jeu affiche ses décors et ses personnages
dessinés en SVG, animés : c'est le mode par défaut, entièrement jouable. Déposer un fichier
portant exactement le nom attendu le fait apparaître à la place du dessin — **aucun code à
modifier**.

Aucun média n'est fourni avec cette première version : ce fichier liste seulement les
emplacements prévus.

La page de vérification ([verifier.html](../../verifier.html#melanges)) et ⚙️ Réglages →
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
| Illustrations d'énigmes | `.jpg` (ou `.png` / `.webp`) |

---

## 1. Décors et cinématiques — `assets/videos/` et `assets/images/decors/`

| Emplacement | Nom du fichier | Où il apparaît | Ce que l'image doit montrer |
|---|---|---|---|
| Cinématique d'ouverture | `intro.mp4` | Plein écran au clic sur « Entrer dans le laboratoire ». Sautée si absente. | Des fioles qui tombent d'une étagère, puis la page effacée du testament |
| Salle 1 — La salle des balances | `salle1.mp4` *ou* `salle1.jpg` | Décor de la salle, et fond de l'écran d'accueil | Balance à plateaux, balance électronique, masses marquées |
| Salle 2 — La cuisine d'essai | `salle2.mp4` *ou* `salle2.jpg` | Décor de fond de la salle | Plan de travail, cafetière, sucrier, balance de cuisine |
| Salle 3 — La salle des fioles | `salle3.mp4` *ou* `salle3.jpg` | Décor de fond de la salle | Étagères de fioles : liquides clairs, à deux couches, troubles |
| Salle 4 — L'atelier de tri | `salle4.mp4` *ou* `salle4.jpg` | Décor de fond de la salle | Tamis, aimant en fer à cheval, bacs de sable et de gravier, bassine d'eau |
| Salle 5 — La saline | `salle5.mp4` *ou* `salle5.jpg` | Décor de fond de la salle | Montage de filtration, coupelle au soleil, marais salants par la fenêtre |
| Cinématique de fin | `final.mp4` | Plein écran quand le testament est complet. Sautée si absente. | Les cristaux de sel au fond de la coupelle, la limaille sur l'aimant |

Les vidéos vont dans `assets/videos/`, les images dans `assets/images/decors/`.

**Sécurité à l'image** : aucune personne qui goûte ou qui sent un produit.

## 2. Personnages — `assets/videos/personnages/` et `assets/images/personnages/`

| Personnage | Rôle | Salles | Nom du fichier | Variante « parle » |
|---|---|---|---|---|
| Lila | Apprentie chimiste, 11 ans | accueil, 1, 3 | `lila.mp4` *ou* `lila.png` | `lila-parle.mp4` (facultative) |
| Marius | Cuisinier de la cuisine d'essai | 2 | `marius.mp4` *ou* `marius.png` | `marius-parle.mp4` (facultative) |
| Nadia | Laborantine de l'atelier de tri | 4 | `nadia.mp4` *ou* `nadia.png` | `nadia-parle.mp4` (facultative) |
| Yann | Paludier, ramasseur de sel de mer | 5 | `yann.mp4` *ou* `yann.png` | `yann-parle.mp4` (facultative) |
| Madame Mélange | Chimiste, directrice du laboratoire | fin | `melange.mp4` *ou* `melange.png` | `melange-parle.mp4` (facultative) |

La variante `-parle` est jouée pendant que le personnage parle ; sans elle, la vidéo au repos
est conservée.

## 3. Illustrations d'énigmes — `assets/images/cartes/`

Chaque illustration est **facultative** : sans fichier, l'énigme reste entièrement jouable et
un encadré discret rappelle le nom attendu. Ces emplacements sont déclarés dans
`assets/data/enigmes.json` (champ `media`).

| Énigme | Nom du fichier | Légende prévue |
|---|---|---|
| 1-1 — Du plus léger au plus lourd (salle 1) | `e1-1.jpg` | Les fioles posées sur la balance électronique |
| 2-2 — Le cahier taché de Marius (salle 2) | `e2-2.jpg` | L'expérience de Marius : eau, sucre, balance |
| 3-1 — Homogène ou hétérogène ? (salle 3) | `e3-1.jpg` | Les fioles de l'étagère de Madame Mélange |
| 4-2 — Pas à pas (salle 4) | `e4-2.jpg` | Le tamis et la bassine de l'atelier |
| 5-1 — Filtrer, décanter, évaporer (salle 5) | `e5-1.jpg` | Les marais salants |
| 5-4 — Le testament de Madame Mélange (salle 5) | `e5-4.jpg` | Le testament de Madame Mélange |

Pour qu'une illustration soit une **vidéo**, ajoutez `"type": "video"` dans le bloc `media` de
l'énigme et déposez `<nom>.mp4` dans `assets/videos/`.

> Attention : une illustration ne doit pas donner la réponse (par exemple, pas de fioles
> étiquetées « homogène » pour l'énigme 3-1).

## 4. Leçons

Les cinq leçons sont **rédigées** dans `assets/data/lecons.json` (texte CM1 et CM2, lexique,
schéma SVG, source). Elles ne demandent aucun fichier. Le dossier `assets/images/documents/`
n'est pas utilisé.

## 5. Où trouver des images libres de droits

- **Wikimedia Commons** : balances, marais salants, matériel de laboratoire — vérifiez la licence de chaque fichier.
- **Photos de classe** : les manipulations des activités décrochées (sans visage d'élève, ou avec les autorisations nécessaires).

Vérifiez toujours les droits avant de publier le dépôt en ligne : les fichiers déposés ici
sont accessibles publiquement.
