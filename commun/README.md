# commun/ — le tronc commun du moteur

Avant octobre 2026, chaque jeu avait **sa propre copie** du moteur (`media.js`, `audio.js`,
`enigmes.js`…) : un correctif devait être recopié à la main dans huit dossiers. Désormais, tout ce qui
est commun n'existe **qu'une fois**, ici, et chaque jeu le charge avec `../commun/js/…`.

## Ce qui est dans le tronc commun

| Fichier | Rôle | Jeux qui le chargent |
|---|---|---|
| `js/media.js` | vidéos, images et décors dessinés (cascade), cinématiques | les 8 jeux « salles » |
| `js/audio.js` | sons et ambiances synthétisés (aucun fichier audio) | les 8 |
| `js/narration.js` | personnages qui parlent (voix du navigateur), sous-titres | les 8 |
| `js/api.js` | assistant IA facultatif (Albert, DeepSeek) | les 8 |
| `js/sync.js` | envoi de l'état de l'équipe au tableau de bord `prof.html` | les 8 |
| `js/fiche-mission.js` | fiche de mission A4 | les 8 |
| `js/enigmes.js` | moteur des 11 types d'énigmes (v2) | les 6 jeux à moteur commun* |
| `js/impression.js` | bilan, fiches préparatoires, QCM, corrigés | les 6 jeux à moteur commun* |
| `js/lecons-a4.js` · `css/lecons-a4.css` | leçons imprimables A4 | les 9 jeux (dont Mission géographique) |
| `css/animations.css` · `css/personnages.css` · `css/video.css` | animations, portraits, vidéos | les 8 |

### Greffons (chargés après `app.js`)

Ils ajoutent une fonction à tous les jeux **sans modifier** leurs `app.js` : ils complètent les
fonctions existantes (`afficherSalle`, `ouvrirReglages`…) et lisent l'état du jeu (`ETAT`).

| Fichier | Amélioration | Jeux |
|---|---|---|
| `js/transitions.js` | B6 — fondu entre écrans, « rideau » à l'entrée d'une salle (désactivé par « animations réduites ») | les 8 + Mission géographique |

\* constitution, station-meteo, melanges, objets-techniques, moyen-age-abbaye, chateau-fort.
`declaration` et `tour-du-monde` gardent leur moteur d'énigmes et leurs impressions propres
(énigme unique par salle) ; `mission-geo` a son propre moteur (16 séances).

## Ce qui reste dans chaque jeu

- **`js/jeu.js`** — *tout* ce qui est propre au jeu pour les modules communs : identifiant, titre,
  voix des personnages, ambiance sonore de chaque décor, textes de l'assistant IA, textes des
  impressions. Il est chargé **en premier** par `index.html` (objet `JEU`).
- `js/app.js`, `js/reglages.js` — le déroulé du jeu (salles, coffre, badges, quizz) et le volet
  enseignant, qui contiennent beaucoup de textes propres au jeu ;
- `js/decors.js`, `js/personnages.js`, `js/lecons.js` — le contenu (décors dessinés, portraits,
  leçons) ;
- `assets/data/*.json` — les énigmes, dialogues, leçons et évaluations.

## Corriger le moteur

1. Modifiez le fichier dans `commun/js/` — **une seule fois**.
2. Si la modification change le comportement, augmentez le numéro après `?c` dans les balises
   `<script src="../commun/js/…?c1">` des `index.html` (le navigateur rechargera le fichier au lieu
   de garder l'ancien en mémoire).
3. Lancez les tests des 9 jeux : `node outils-tests/tous.js` (voir `outils-tests/README.md`).
4. L'onglet **🧬 Cohérence du moteur** de `verifier.html` contrôle qu'aucun jeu n'a gardé une copie
   locale d'un fichier du tronc commun.

Un nouveau texte propre à un jeu ne s'écrit jamais dans `commun/` : on ajoute un champ dans `JEU`
(avec une valeur par défaut dans le module commun) et on le remplit dans chaque `js/jeu.js`.
