# 🎞️ Médias du jeu — L'Atelier de l'inventeur

**Tout est facultatif.** Sans aucun fichier, le jeu affiche ses décors et ses personnages
dessinés en SVG, animés : c'est le mode par défaut, entièrement jouable. Déposer un fichier
portant exactement le nom attendu le fait apparaître à la place du dessin — **aucun code à
modifier**.

La page de vérification ([verifier.html](../../verifier.html#objets-techniques)) et ⚙️ Réglages →
« 🔍 Vérifier les fichiers présents » affichent, pour chaque emplacement, ce qui est en place
et le nom exact à utiliser.

> Aucun média n'est fourni avec cette version : les emplacements ci-dessous sont prêts à recevoir
> vos photos ou vos vidéos. Pour les photos d'objets réels, préférez vos propres prises de vue
> (objets de la classe) ou des images sous licence libre, en notant l'auteur et la licence.

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

| Emplacement | Nom du fichier | Où il apparaît |
|---|---|---|
| Cinématique d'ouverture | `intro.mp4` | Plein écran au clic sur « Entrer dans l'atelier ». Sautée si absente. |
| Salle 1 — L'entrée de l'atelier | `salle1.mp4` *ou* `salle1.jpg` | Décor de fond de la salle, et fond de l'écran d'accueil |
| Salle 2 — L'établi | `salle2.mp4` *ou* `salle2.jpg` | Décor de fond de la salle |
| Salle 3 — La matériauthèque | `salle3.mp4` *ou* `salle3.jpg` | Décor de fond de la salle |
| Salle 4 — La salle des machines | `salle4.mp4` *ou* `salle4.jpg` | Décor de fond de la salle |
| Salle 5 — Le coin montage | `salle5.mp4` *ou* `salle5.jpg` | Décor de fond de la salle |
| Cinématique de fin | `final.mp4` | Plein écran quand le coffre-fort s'ouvre. Sautée si absente. |

Les vidéos vont dans `assets/videos/`, les images dans `assets/images/decors/`.

## 2. Personnages — `assets/videos/personnages/` et `assets/images/personnages/`

| Personnage | Rôle | Nom du fichier | Variante « parle » |
|---|---|---|---|
| Zoé | Apprentie ingénieure, 11 ans | `zoe.mp4` *ou* `zoe.png` | `zoe-parle.mp4` (facultative) |
| Awa | Ouvrière de l'atelier | `awa.mp4` *ou* `awa.png` | `awa-parle.mp4` (facultative) |
| Monsieur Marcel | Réparateur de vélos | `marcel.mp4` *ou* `marcel.png` | `marcel-parle.mp4` (facultative) |
| Éléonore Marchand | L'inventrice | `eleonore.mp4` *ou* `eleonore.png` | `eleonore-parle.mp4` (facultative) |

Les quatre personnages sont **fictifs** : une image ou une vidéo déposée ne doit ressembler à
aucune personne réelle. Zoé, l'élève, gagne à être rendue en style illustré.

## 3. Illustrations d'énigmes — `assets/images/cartes/`

Chaque illustration est **facultative** : sans fichier, l'énigme reste entièrement jouable et
un encadré discret rappelle le nom attendu. Ces emplacements sont déclarés dans
`assets/data/enigmes.json` (champ `media`).

| Énigme | Nom du fichier | Légende prévue |
|---|---|---|
| 1-1 — Chaque objet répond à un besoin (salle 1) | `e1-1.jpg` | Les cinq objets posés sur la table d'entrée |
| 2-1 — Le schéma de la lampe torche (salle 2) | `e2-1.jpg` | La lampe torche démontée sur l'établi |
| 3-1 — Les casiers de la matériauthèque (salle 3) | `e3-1.jpg` | Les casiers d'échantillons |
| 4-1 — La chaîne d'énergie (salle 4) | `e4-1.jpg` | Le tableau des machines de l'atelier |
| 5-1 — Le montage dans l'ordre (salle 5) | `e5-1.jpg` | La notice de montage |

Idée simple : photographier les objets de la classe (une vraie lampe torche ouverte, des
échantillons de matériaux, une notice de meuble en kit). **Pas d'objet coupant ni dangereux**
sur les photos destinées à une manipulation en classe.

## 4. Leçons

Les cinq leçons sont **rédigées en texte** dans `assets/data/lecons.json`, avec leur schéma
dessiné en SVG : elles n'attendent aucun fichier.
