# Lire un échec de l'intégration continue (N28)

À chaque `git push` et à chaque pull request, GitHub relance les contrôles automatiques du dépôt
(workflow `.github/workflows/verifications.yml`). Rien à installer : tout se lit sur github.com.

## Où voir le résultat

| Où | Ce qu'on voit |
|---|---|
| Page du dépôt → liste des commits | à droite de chaque commit : ✓ vert (tout passe), ✗ rouge (échec), ● orange (en cours) |
| Pull request | bloc « Checks » en bas de la discussion |
| Onglet **Actions** du dépôt | une ligne par push, « Vérifications (N28) » |

## Lire un échec, pas à pas

1. Sur github.com, ouvrez le dépôt `IdGir/escape-games-cm1-cm2`, onglet **Actions**.
2. Cliquez sur la ligne rouge ✗ « Vérifications (N28) » correspondant à votre push.
3. Cliquez sur le travail **Contrôles automatiques** (colonne de gauche).
4. Repérez l'**étape rouge** (✗) : chacune est un contrôle distinct, les autres étapes tournent quand même.
5. Cliquez sur cette étape pour déplier son journal, puis cherchez les lignes marquées **✗** : elles disent
   quel jeu, quel fichier, quel problème (même texte qu'en local).
6. Corrigez, commitez, repoussez : la CI se relance toute seule.

## Que veut dire chaque étape

| Étape | Script | Si elle échoue |
|---|---|---|
| Énigmes de tous les jeux (A7) | `verifier-enigmes.js` | un `enigmes.json` est invalide (clé en double, bonne réponse hors liste, deux serrures identiques…) ; la ligne ✗ donne le jeu et l'énigme |
| Liens internes de navigation (N10) | `verifier-liens-internes.js` | un lien interne mène à un fichier qui n'existe plus ; la ligne ✗ donne la page et le lien |
| Charte graphique (B1) | `verifier-charte.js` | un jeu s'écarte des couleurs de `CHARTE-GRAPHIQUE.md` |
| Affichage tablette et smartphone (N17) | `verifier-responsive.js --rapide` | un bouton essentiel sort de l'écran à une largeur type ; en cas d'échec, les captures sont téléchargeables en bas de la page du run, rubrique **Artifacts** → `captures-responsive` |
| Vérifier que Chrome est disponible | — | problème du serveur GitHub, pas du dépôt : relancer (« Re-run jobs ») |

⚠ (alerte) n'est pas bloquant et ne fait pas échouer l'étape ; seuls les ✗ le font.

## Refaire le même contrôle chez soi

Depuis la racine du dépôt (Node.js installé) : `node outils-tests/verifier-enigmes.js`, puis
`node outils-tests/verifier-liens-internes.js`, `node outils-tests/verifier-charte.js` et
`node outils-tests/verifier-responsive.js --rapide` (ce dernier demande Chrome ou Edge et un
`npm install` dans `outils-tests`). Le crochet `pre-push` (voir `README.md`) lance les trois premiers
contrôles + l'affichage automatiquement avant chaque `git push`.

## Relancer ou lancer à la main

Onglet Actions → « Vérifications (N28) » → **Run workflow** (choisir la branche), ou, sur un run échoué,
**Re-run failed jobs** (utile si l'échec vient d'un souci passager du serveur).
