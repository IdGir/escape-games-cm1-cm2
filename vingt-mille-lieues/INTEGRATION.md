# INTÉGRATION AU SITE — à appliquer par l'enseignant dans une SECONDE PR (après validation)

Cette PR n'ajoute que des fichiers (contrôle : `bash outils-tests/verifier-isolation.sh`). Les modifications ci-dessous
touchent des fichiers existants : elles ne sont **pas** appliquées ici. Le jeu fonctionne déjà par son adresse directe.

## 1. `commun/donnees/catalogue.js` — nouvelle entrée hors liste (dans le tableau `jeux`, après « tour-du-monde »)
```js
  {
   "num": "N",
   "id": "vingt-mille-lieues",
   "titre": "Vingt mille lieues sous les mers — Le Journal du Nautilus",
   "matiere": "Sciences",
   "annee": "AB",
   "periodes": ["P1", "P2", "P3", "P4", "P5"],
   "competences": "Campagne de 11 escales d'après Jules Verne. Escale 2 : électricité (conducteurs, circuits, série/dérivation), objets techniques (instruments), chaîne d'énergie.",
   "dossier": "vingt-mille-lieues",
   "icone": "⚓",
   "couleurs": ["#0b2230", "#c9a24a"],
   "resume": "Recueillis à bord du Nautilus après une avarie, les mousses de l'Abraham Lincoln reconstituent le journal de bord, escale après escale.",
   "prompt": "vingt-mille-lieues.md",
   "programme": ["st2026", "hg2026"]
  },
```
(Vérifier que `annee: "AB"` et le `num` « N » sont acceptés par l'accueil, la frise et `commun/tests/test-pages.js` ; sinon
reprendre la forme de l'entrée « tour-du-monde ».)

## 2. `index.html` (accueil) et `annee.html`
Rien à coder si ces pages lisent le catalogue ; sinon ajouter une carte « ⚓ Le Journal du Nautilus » vers `vingt-mille-lieues/`.

## 3. Hors connexion : `sw-fichiers.js`
Le jeu a son propre service worker (`vingt-mille-lieues/sw.js`, portée limitée au dossier). Pour l'inclure aussi dans l'application
installable globale : ajouter les fichiers listés dans `FICHIERS` de `vingt-mille-lieues/sw.js` (préfixés `vingt-mille-lieues/`)
à `FICHIERS_CODE`, puis lancer `python outils-pwa/maj-hors-ligne.py` (qui corrige aussi l'échec préexistant « version à jour » de
`commun/tests/test-hors-ligne.js`, voir BASELINE-TESTS.md).

## 4. `outils-tests/tous.js`
Aucune modification nécessaire : il découvre `vingt-mille-lieues/tests/` tout seul (test-jeu, test-coherence-narrative,
test-medias).

## 5. `serveur.py` (facultatif)
- `/api/fichiers` : ajouter `"vingt-mille-lieues"` au tuple des jeux pour que `verifier.html` voie ses médias.
- `/api/enigmes` (éditeur) : non compatible (format à 5 grades) — ne pas ajouter.
Le tableau de bord fonctionne sans changer le serveur (les détails voyagent dans le champ `enigme`).

## 6. `verifier.html`, `editeur.html`
`verifier.html` : un onglet pointant vers `vingt-mille-lieues/medias.html` et les adresses `?verif=1&escale=2&niveau=…&enigme=…`.
`editeur.html` : non compatible pour l'instant (5 grades, fiches d'ancrage).

## 7. Outils de médias
Le cahier des charges les plaçait dans `outils-medias/` ; le script d'isolation n'y autorise pas d'ajout. Ils sont dans
`vingt-mille-lieues/outils/` : `verifier-medias.py`, `caler-effets.html`, `choisir-medias.html`, `generer-medias.py`. Les déplacer
est facultatif (adapter alors les chemins relatifs `../`).

## 8. `README.md` (racine)
- Phrase d'ouverture : « Douze escape games » → « Treize escape games ».
- Ligne à ajouter au tableau des jeux :
```
| ⚓ | **Vingt mille lieues sous les mers — Le Journal du Nautilus** — Sciences, histoire, géographie (campagne de 11 escales, 5 grades) | [▶ en ligne](https://idgir.github.io/escape-games-cm1-cm2/vingt-mille-lieues/) | [vingt-mille-lieues/README.md](vingt-mille-lieues/README.md) | [liste](vingt-mille-lieues/assets/README.md) |
```
- Tableau des adresses de test : `vingt-mille-lieues/?verif=1&escale=2&niveau=timonier&enigme=K` — K de 1 à 4 ; `&fin=1` : fin d'escale.
- § 4 « Organisation du dépôt » : ajouter le dossier `vingt-mille-lieues/` (même organisation que `alimentation/`, plus
  `outils/`, `scenarimages/`, `references/`).
