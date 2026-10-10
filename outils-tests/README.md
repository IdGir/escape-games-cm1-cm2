# outils-tests — tests automatiques des 9 jeux (Node + jsdom)

Chaque jeu a un dossier `tests/` : une partie complète est jouée **sans navigateur**, comme le ferait
une équipe (clics sur les étiquettes, les cases, les boutons « Vérifier »), en CM1 puis en CM2, avec
des erreurs volontaires. Les tests contrôlent le barème (10 / 3 points), les retours d'erreur (le
**nombre** de bonnes réponses, jamais lesquelles), l'absence de correction après la réussite, les
mots-clés, le coffre final, le mode vérification, les réglages, les leçons, les impressions et le
tableau de bord `prof.html`.

| Fichier | Rôle |
|---|---|
| `charge.js` | ouvre une page d'un jeu dans jsdom, sans réseau (scripts et `fetch` lus sur le disque) |
| `moteur-commun.js` | tests des jeux à moteur commun (constitution, station-meteo, melanges…) : tout est déduit de `enigmes.json` |
| `moteur-ancien.js` | tests de declaration et tour-du-monde (moteur propre, 5 salles à énigme unique) |
| `tous.js` | lance tous les tests, jeu après jeu, et affiche un tableau récapitulatif |
| `<jeu>/tests/test-jeu.js` | le test d'un jeu (quelques lignes : ce qui est propre au jeu) |

## Lancer les tests (Windows)

**Outil : l'Invite de commandes**, avec **Node.js** installé (une seule fois :
https://nodejs.org, version « LTS », options par défaut).

1. Touche **Windows + R**, tapez `cmd`, **Entrée**.
2. Allez dans le dossier du dépôt :
   ```
   E:
   cd "\IDRISS\PROJET ESCAPE GAMES"
   ```
3. **Une seule fois** : installez jsdom dans `outils-tests` (le dossier `node_modules` créé n'est
   pas publié) :
   ```
   cd outils-tests
   npm install
   cd ..
   ```
4. Lancez tous les tests (5 à 8 minutes) :
   ```
   node outils-tests\tous.js
   ```
   ou un seul jeu : `node outils-tests\tous.js melanges`, ou une seule étape d'un jeu :
   `node melanges\tests\test-jeu.js partie` (étapes : `partie`, `types`, `divers`, `prof`).
5. Lisez la dernière ligne : **« Tous les tests passent »**. Sinon, les lignes marquées ✗ disent
   quoi, dans quel jeu.

## Ajouter un jeu

Pour un nouveau jeu à moteur commun, créez `<jeu>/tests/test-jeu.js` :

```js
require("../../outils-tests/moteur-commun").lancer(__dirname + "/..", {
  titre: "Nom du jeu",
  scoresMax: { CM1: 185, CM2: 235 }
});
```

Rien d'autre n'est nécessaire : le nombre d'énigmes, les types, les mots-clés et le barème sont lus
dans les données du jeu. `tous.js` le trouve tout seul.

## Contrôle des énigmes avant publication (A7)

`verifier-enigmes.js` relit en une seconde les `enigmes.json` (et les mots des serrures de
`dialogues.json`) de tous les jeux, **sans navigateur ni jsdom** :

```
node outils-tests\verifier-enigmes.js            (tous les jeux)
node outils-tests\verifier-enigmes.js melanges   (un seul jeu)
```

| Contrôle | Exemple d'erreur attrapée |
|---|---|
| JSON lisible, **aucune clé en double** | deux `"titre"` dans une énigme : le navigateur garderait le second sans prévenir |
| salles numérotées 1, 2, 3… ; identifiants uniques | deux énigmes « 2-3 » |
| titre, type connu, consigne (CM1 **et** CM2 si différenciée), indices, correction, leçon existante | `"lecon": "evaporation"` absente de `lecons.json` |
| clés attendues par type, pour chaque niveau joué et chaque variante (D3) | QCM dont `bonne` dépasse les options ; rangs d'un « ordre » qui ne vont pas de 1 à n ; deux intrus ; réponse d'un texte à trous absente des étiquettes ; lettre du mot non cachée dans le texte |
| **CM1 ≤ CM2** | une salle avec plus d'énigmes en CM1 qu'en CM2 |
| **serrures** : un mot-clé par salle, jamais deux fois le même (accents et majuscules ignorés) | « PESER » en salle 1 et « Peser » en salle 5 |

✗ = bloquant (code de sortie 1), ⚠ = à regarder. Déclaration et Tour du monde écrivent leurs
énigmes dans `js/` : seules leurs serrures sont contrôlées. `vingt-mille-lieues/` et `immersifs/`
ont leur propre format et ne sont pas concernés.

**Avant chaque `git push`, automatiquement** : le crochet `hooks/pre-push` lance ce contrôle et
arrête la publication en cas d'erreur ✗. Il s'active une seule fois par ordinateur :

```
git config core.hooksPath outils-tests/hooks
```

(publier malgré tout, exceptionnellement : `git push --no-verify`). Le test du contrôleur lui-même :
`node commun/tests/test-enigmes-json.js`.
