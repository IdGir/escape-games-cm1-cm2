# Base de référence des tests (avant toute modification)

Relevé le 3 octobre 2026, branche `claude/tender-shannon-aq897z` (commit `eab998a`), après
`cd outils-tests && npm install` (jsdom, non publié), commande : `node outils-tests/tous.js`.

| Jeu | Test | Résultat | Vérifications | Échecs |
|---|---|---|---|---|
| alimentation | test-jeu.js | ok | 451 | 0 |
| alimentation | test-verifier.js | ok | 16 | 0 |
| chateau-fort | test-chateau-fort.js | ok | ? | ? |
| commun | test-coherence.js | ok | 255 | 0 |
| commun | test-greffons.js | ok | 150 | 0 |
| commun | **test-hors-ligne.js** | **ÉCHEC** | 43 | **1** |
| commun | test-pages.js | ok | 109 | 0 |
| constitution | test-jeu.js | ok | 454 | 0 |
| declaration | test-jeu.js | ok | 90 | 0 |
| melanges | test-jeu.js | ok | 451 | 0 |
| mission-geo | test-jeu.js | ok | 985 | 0 |
| moyen-age-abbaye | test-jeu.js | ok | 722 | 0 |
| moyen-age-abbaye | test-verifier.js | ok | 20 | 0 |
| objets-techniques | test-jeu.js | ok | 451 | 0 |
| objets-techniques | test-verifier.js | ok | ? | ? |
| renaissance | test-jeu.js | ok | 451 | 0 |
| renaissance | test-verifier.js | ok | 16 | 0 |
| station-meteo | test-jeu.js | ok | 462 | 0 |
| tour-du-monde | test-jeu.js | ok | 90 | 0 |
| versailles | test-jeu.js | ok | 451 | 0 |
| versailles | test-verifier.js | ok | 16 | 0 |

**Échec préexistant (non causé par ce travail)** : `commun/tests/test-hors-ligne.js` →
« ✗ version à jour (sinon : python outils-pwa/maj-hors-ligne.py avant de publier) ». Le numéro
`VERSION_HORS_LIGNE` de `sw-fichiers.js` ne correspond plus au contenu des fichiers listés. Ce calcul ne
porte que sur les fichiers listés dans `sw-fichiers.js` : les fichiers ajoutés dans `vingt-mille-lieues/` ne
le changent pas. Correction (hors de cette PR, car elle modifie un fichier existant) :
`python outils-pwa/maj-hors-ligne.py`.

Critère de non-régression : après chaque série de commits, même tableau (20 ok + cet échec), plus les
lignes nouvelles de `vingt-mille-lieues/tests/` qui doivent être vertes.
