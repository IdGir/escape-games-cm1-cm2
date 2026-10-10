# commun/ — le tronc commun du moteur

Avant octobre 2026, chaque jeu avait **sa propre copie** du moteur (`media.js`, `audio.js`,
`enigmes.js`…) : un correctif devait être recopié à la main dans huit dossiers. Désormais, tout ce qui
est commun n'existe **qu'une fois**, ici, et chaque jeu le charge avec `../commun/js/…`.

## Ce qui est dans le tronc commun

| Fichier | Rôle | Jeux qui le chargent |
|---|---|---|
| `js/media.js` | vidéos, images et décors dessinés (cascade), cinématiques | les 12 jeux « salles » |
| `js/audio.js` | sons et ambiances synthétisés (aucun fichier audio) | les 12 |
| `js/narration.js` | personnages qui parlent (voix du navigateur), sous-titres | les 12 |
| `js/api.js` | assistant IA facultatif (Albert, DeepSeek) | les 12 |
| `js/sync.js` | envoi de l'état de l'équipe au tableau de bord `prof.html` | les 12 |
| `js/fiche-mission.js` | fiche de mission A4 | les 12 |
| `js/enigmes.js` | moteur des 11 types d'énigmes (v2) | les 10 jeux à moteur commun* |
| `js/impression.js` | bilan, fiches préparatoires, QCM, corrigés | les 10 jeux à moteur commun* |
| `js/lecons-a4.js` · `css/lecons-a4.css` | leçons imprimables A4 | les 13 jeux (dont Mission géographique) |
| `css/animations.css` · `css/personnages.css` · `css/video.css` | animations, portraits, vidéos | les 12 |

### Greffons (chargés après `app.js`)

Ils ajoutent une fonction à tous les jeux **sans modifier** leurs `app.js` : ils complètent les
fonctions existantes (`afficherSalle`, `ouvrirReglages`…) et lisent l'état du jeu (`ETAT`).

| Fichier | Amélioration | Jeux |
|---|---|---|
| `js/transitions.js` | B6 — fondu entre écrans, « rideau » à l'entrée d'une salle (désactivé par « animations réduites ») | les 12 jeux « salles » + Mission géographique |
| `js/accessibilite.js` + `polices/` | E4 — lecture facilitée : police très lisible ou OpenDyslexic, interlignage, espacement (⚙️ Réglages → Accessibilité ; gardé sur l'appareil pour tous les jeux) | les 13 |
| `js/lecture-consignes.js` | E5 — « 🔊 Écouter la consigne » sur chaque consigne (titre + consigne, tableaux lus, dessins ignorés, texte surligné ; second clic = arrêt) ; ⚙️ → Accessibilité : lecture automatique de chaque nouvelle consigne et vitesse (gardé sur l'appareil, pour tous les jeux) | les 12 jeux « salles » |
| `js/palier-decouverte.js` | E2 — troisième palier « Découverte » (énigmes CM1 + aide renforcée) | les 12 jeux « salles » |
| `js/indices-adaptatifs.js` | E3 — un indice est proposé (jamais imposé) après un temps sans action ou 2 essais faux ; réglable dans ⚙️ | les 12 jeux « salles » |
| `js/indices-degressifs.js` | N5 — option ⚙️ → 💡 Indices « Coût des indices » : fixe (−2 chacun, par défaut) ou dégressif (−2, puis −1, puis −1 par énigme) ; coût du prochain indice écrit sur le bouton | les 12 jeux « salles » |
| `js/minuteur-equipe.js` | E6 — depuis `prof.html` (bouton ⏱️ +), quelques minutes accordées à une équipe : le chrono de la salle est décalé, le bonus de rapidité préservé | les 12 jeux « salles » |
| `js/jeu-suivant.js` | C4 — « Et ensuite ? » à l'écran de fin : suite directe (Déclaration → Constitution) ou jeu précédent/suivant de la progression | les 12 jeux « salles » |
| `js/variantes.js` | D3 — banque d'énigmes : une énigme peut avoir des `variantes` dans `enigmes.json` ; la série jouée change à chaque année scolaire (ou se choisit dans ⚙️) | les 10 jeux à moteur commun |
| `js/compte-rendu.js` | compte-rendu d'une partie (score, énigmes, erreurs, indices, temps, code de contrôle) ; historique des parties de l'appareil (pour `resultats.html`) | les 12 jeux « salles » |
| `js/trophees.js` + `donnees/trophees.js` | N1 — trophées cumulés d'un jeu à l'autre (même nom d'équipe ou d'élève, parties terminées de l'appareil) : nouveaux trophées annoncés à l'écran de fin, total, lien vers `trophees.html` (vitrine, diplôme). 13 trophées, règles dans `donnees/trophees.js` | les 12 jeux « salles » + `trophees.html` |
| `js/auto-evaluation.js` | N6 — écran de fin : « 🪞 On s'évalue » (« Je m'évalue » en mode individuel), 5 affirmations rattachées au socle commun (D1, D2 ×2, D3, et D4 sciences / D5 histoire-géographie / D3 EMC), 3 réponses ; gardées avec le compte-rendu (historique, `resultats.html`, CSV) ; grille vierge imprimable, une par élève | les 12 jeux « salles » |
| `js/mode-solo.js` | D2 — « 🏠 Je joue seul » (`?solo=1`) : prénom, pas de synchronisation, compte-rendu à copier, télécharger ou imprimer pour l'enseignant | les 12 jeux « salles » |
| `js/export-partie.js` | A5 — écran Pause : « 💾 Enregistrer la partie dans un fichier » (`<jeu>-<équipe>-<date>.json`) ; accueil : « 📂 Reprendre une partie depuis un fichier » (contrôle du jeu, de la version et de la partie, puis reprise habituelle) | les 12 jeux « salles » |
| `js/mode-duel.js` | N4 — « ⚔️ Duel » (`?duel=1`) : deux équipes sur un même écran, à tour de rôle (une énigme chacune ; une salle chacune dans Déclaration et Tour du monde), points de chaque tour à l'équipe qui joue, bandeau des scores, rideau à chaque changement, vainqueur à la fin ; gardé pour la reprise | les 12 jeux « salles » |
| `js/pwa.js` | A4 — enregistre le service worker `sw.js` (application installable, hors connexion ; voir `outils-pwa/README.md`) | les 13 jeux et l'accueil |

\* constitution, station-meteo, melanges, objets-techniques, moyen-age-abbaye, chateau-fort, versailles, renaissance, alimentation, lumiere.
`declaration` et `tour-du-monde` gardent leur moteur d'énigmes et leurs impressions propres
(énigme unique par salle) ; `mission-geo` a son propre moteur (16 séances).

### Données communes

| Fichier | Contenu |
|---|---|
| `icones/` | icônes de l'application installable (dessinées par `outils-pwa/icones.py`) |
| `donnees/catalogue.js` | les 26 jeux de la progression et les 4 jeux hors liste : matière, année A/B, période, points du programme, dossier publié, liens « suite directe ». Source : `prompts-opus/00-ORDRE-DE-PRODUCTION.md`. **Un jeu publié : renseigner son `dossier`.** |

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

## Écrire des variantes d'une énigme (banque d'énigmes, D3)

Dans `assets/data/enigmes.json`, ajouter à l'énigme un tableau `variantes`. Chaque variante ne contient
que les champs qui changent (`cm1`, `cm2`, `commun`, `consigne`, `indices`, `correction`…) ; le type, la
compétence et la leçon restent ceux de l'énigme. Exemple : `melanges`, énigmes 1-3 et 2-4 (calculs de
masses). Règles : même difficulté, faits vérifiés comme pour l'énigme d'origine, corrigé à jour.
Tester une série : `…/?salle=1&niveau=CM1&enigme=3&serie=1`. Les corrigés imprimés suivent la série jouée.
