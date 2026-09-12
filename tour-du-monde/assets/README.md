# 🎞️ Médias — Le Tour du Monde en 80 minutes

Tous les médias du jeu sont dans ce dossier, `tour-du-monde/assets/`.
**Aucun n'est obligatoire** : sans fichier, le jeu affiche son dessin.

👉 Ce qui est déjà en place, avec aperçu :
[page de vérification](https://idgir.github.io/escape-games-cm1-cm2/verifier.html#tour-du-monde)
(en local : http://127.0.0.1:8000/verifier.html).
Comment déposer un fichier : [README principal, § 3](../../README.md#3-ajouter-ou-remplacer-une-image-ou-une-vidéo).

---

## Décors et cinématiques

| Emplacement | Vidéo → `videos/` | Image → `images/decors/` |
|---|---|---|
| Cinématique d'ouverture — le pari (au clic sur « Lever l'ancre ») | `intro.mp4` | `intro.jpg` |
| Escale 1 — Le Reform Club, Londres *(aussi l'écran d'accueil)* | `etape1.mp4` | `etape1.jpg` |
| Escale 2 — L'isthme de Suez | `etape2.mp4` | `etape2.jpg` |
| Escale 3 — La jungle de l'Inde | `etape3.mp4` | `etape3.jpg` |
| Escale 4 — La mer de Chine | `etape4.mp4` | `etape4.jpg` |
| Escale 5 — L'observatoire de Greenwich | `etape5.mp4` | `etape5.jpg` |
| Cinématique de fin — le jour gagné (après l'escale 5) | `final.mp4` | `final.jpg` |

- Vidéo : `.mp4` ou `.webm`, 16:9, 15 à 30 s en boucle, moins de 20 Mo, jouée muette.
- Image : `.jpg`, `.png` ou `.webp`, 16:9. Elle sert d'affiche à la vidéo, et de
  décor fixe si la vidéo manque.
- Une cinématique absente est simplement sautée.

## Personnages

| Personnage | Vidéo → `videos/personnages/` | Image → `images/personnages/` |
|---|---|---|
| Phileas Fogg | `fogg.mp4` | `fogg.png` |
| Jean Passepartout | `passepartout.mp4` | `passepartout.png` |
| Mrs Aouda | `aouda.mp4` | `aouda.png` |
| L'inspecteur Fix | `fix.mp4` | `fix.png` |

- Vidéo : boucle muette, cadre **170 × 262 px** (portrait vertical, plein corps).
  Variante facultative `fogg-parle.mp4` (etc.) : jouée pendant que le personnage parle.
- Image : `.png` à fond transparent de préférence ; `.gif` animé, `.webp`, `.jpg` acceptés.

## Cartes et paysages → `images/cartes/`

**Dans les énigmes** (`.jpg`, `.png` ou `.webp`) :

| Fichier | Où il apparaît |
|---|---|
| `planisphere.jpg` | Escale 1 : fond de carte, **sous** les zones cliquables (proportions 2:1) |
| `paysage-desert.jpg` | Escale 3 : vignette du désert |
| `paysage-jungle.jpg` | Escale 3 : vignette de la jungle |
| `paysage-montagne.jpg` | Escale 3 : vignette de l'Himalaya |
| `paysage-campagne.jpg` | Escale 3 : vignette de la campagne anglaise |
| `paysage-banquise.jpg` | Escale 3 : vignette de la banquise (CM2) |
| `paysage-savane.jpg` | Escale 3 : vignette de la savane (CM2) |

**Dans la bibliothèque de leçons 📚** (`.jpg` uniquement) :

| Fichier | Leçon | Contenu suggéré |
|---|---|---|
| `planisphere.jpg` | Les continents et les océans | *(le même que ci-dessus)* |
| `rose-des-vents.jpg` | S'orienter : les points cardinaux | Rose des vents à 8 directions |
| `carte-exemple-echelle.jpg` | Lire une carte : légende et échelle | Carte avec titre, légende, flèche du nord et échelle |
| `carte-climats-monde.jpg` | Les climats et les paysages du monde | Planisphère des grandes zones climatiques |
| `carte-canaux-detroits.jpg` | Se déplacer dans le monde | Canaux de Suez et de Panama, détroits de Gibraltar et de Malacca |
| `carte-fuseaux-horaires.jpg` | Méridiens, parallèles et fuseaux horaires | Carte des fuseaux horaires |

Ces noms viennent de la clé `"carte"` de chaque leçon dans `data/lecons.json`.
Des cartes libres de droits existent sur Wikimedia Commons.

## Documents et vidéos de leçon (facultatif)

Une leçon de `data/lecons.json` peut aussi déclarer :
- un document image : `"document": {"type": "image", "fichier": "extrait-verne", …}`
  → fichier `images/documents/extrait-verne.jpg` ;
- une vidéo : `"video": {"base": "lecon-fuseaux", …}` → fichier `videos/lecon-fuseaux.mp4`.

Aucune leçon n'en déclare pour l'instant. La page de vérification les listera
dès qu'elles seront ajoutées.

## Textes du jeu → `data/`

`dialogues.json`, `lecons.json`, `evaluations.json` : ce ne sont pas des médias,
ne les renommez pas.

---

## Remplacer, changer de format, supprimer

- **Remplacer** : déposez un fichier du même nom, il écrase l'ancien.
- **Changer de format** (`intro.png` → `intro.jpg`) : supprimez l'ancien fichier,
  pour qu'il ne reste qu'un fichier par emplacement.
- **Supprimer** : le jeu revient à son dessin.
- Noms **en minuscules**, sans espace ni accent : `etape1.mp4`, pas `Etape1.mp4`.
