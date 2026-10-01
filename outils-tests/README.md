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
