# 🎞️ Médias — Le Secret de la Déclaration

Tous les médias du jeu sont dans ce dossier, `declaration/assets/`.
**Aucun n'est obligatoire** : sans fichier, le jeu affiche son dessin.

👉 Ce qui est déjà en place, avec aperçu :
[page de vérification](https://idgir.github.io/escape-games-cm1-cm2/verifier.html#declaration)
(en local : http://127.0.0.1:8000/verifier.html).
Comment déposer un fichier : [README principal, § 3](../../README.md#3-ajouter-ou-remplacer-une-image-ou-une-vidéo).

---

## Décors et cinématiques

| Emplacement | Vidéo → `videos/` | Image → `images/decors/` |
|---|---|---|
| Cinématique d'ouverture (au clic sur « Commencer ») | `intro.mp4` | `intro.jpg` |
| Salle 1 — La cour du Palais-Royal *(aussi l'écran d'accueil)* | `salle1.mp4` | `salle1.jpg` |
| Salle 2 — L'imprimerie clandestine | `salle2.mp4` | `salle2.jpg` |
| Salle 3 — Le jardin des Tuileries | `salle3.mp4` | `salle3.jpg` |
| Salle 4 — La place de la Bastille | `salle4.mp4` | `salle4.png` |
| Salle 5 — La salle de l'Assemblée nationale | `salle5.mp4` | `salle5.jpg` |
| Cinématique de fin (après la salle 5) | `final.mp4` | `final.jpg` |

- Vidéo : `.mp4` ou `.webm`, 16:9, 15 à 30 s en boucle, moins de 20 Mo, jouée muette.
- Image : `.jpg`, `.png` ou `.webp`, 16:9. Elle sert d'affiche à la vidéo, et de
  décor fixe si la vidéo manque.
- Une cinématique absente est simplement sautée.

## Personnages

| Personnage | Vidéo → `videos/personnages/` | Image → `images/personnages/` |
|---|---|---|
| Louise | `louise.mp4` | `louise.png` |
| Maître Gutenberg | `gutenberg.mp4` | `gutenberg.png` |
| Le Marquis de Montclair | `marquis.mp4` | `marquis.png` |
| Maximilien | `maximilien.mp4` | `maximilien.png` |

- Vidéo : boucle muette, cadre portrait vertical (la voix vient de la synthèse vocale).
  Variante facultative `louise-parle.mp4` (etc.) : jouée pendant que le personnage parle.
- Image : carrée, `.png` à fond transparent de préférence ; `.gif` animé, `.webp`, `.jpg` acceptés.

## Documents des leçons (📚) → `images/documents/`

| Leçon | Fichier (`.jpg` uniquement) |
|---|---|
| Les États généraux et le serment du Jeu de paume | `etats-generaux.jpg` |
| La prise de la Bastille | `bastille.jpg` |
| La Déclaration des droits de l'homme et du citoyen | `declaration.jpg` |
| Carte et lieux de Paris en 1789 | `paris.jpg` |

Le nom vient de la clé `"fichier"` du document dans `data/lecons.json` (à défaut,
l'identifiant de la leçon). Sans fichier, la leçon affiche un encadré avec un
lien Wikimedia.

## Textes du jeu → `data/`

`dialogues.json`, `lecons.json`, `evaluations.json` : ce ne sont pas des médias,
ne les renommez pas.

---

## Remplacer, changer de format, supprimer

- **Remplacer** : déposez un fichier du même nom, il écrase l'ancien.
- **Changer de format** (`salle4.png` → `salle4.jpg`) : supprimez l'ancien fichier,
  pour qu'il ne reste qu'un fichier par emplacement.
- **Supprimer** : le jeu revient à son dessin.
- Noms **en minuscules**, sans espace ni accent.
