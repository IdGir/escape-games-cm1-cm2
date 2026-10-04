# Essayer et vérifier « Le Journal du Nautilus »

## 1. Récupérer et lancer le jeu (Windows)

1. Sur GitHub, ouvrez la branche `claude/tender-shannon-aq897z` du dépôt, puis **Code → Download ZIP** (ou `git checkout claude/tender-shannon-aq897z` si vous avez le dépôt).
2. Dézippez, puis double-cliquez sur **`lancer.bat`** à la racine (Python est requis). Une fenêtre noire reste ouverte : c'est le serveur local, ne la fermez pas.
3. Ouvrez dans Chrome : **http://127.0.0.1:8000/vingt-mille-lieues/**
   (Il faut passer par ce serveur : en double-cliquant sur `index.html`, les vidéos et le chargement des données sont désactivés.)
   Sur Mac : `lancer-mac.command`.

## 2. Parcours d'essai conseillé (15 minutes)

| Étape | Quoi faire | À regarder |
|---|---|---|
| Accueil | Cliquez sur **🎬 Bande-annonce** (21 s). Saisissez un nom d'équipe, choisissez un grade, **Embarquer**. | Le bouton n'apparaît que si `assets/videos/bande-annonce.mp4` existe. |
| Ouverture | Regardez la cinématique de l'escale 1 (vidéo d'intro, voix, sous-titres). **⏭ Passer** pour la sauter. | Voix et sous-titres sont dans le jeu ; la vidéo se pose derrière. |
| Énigme | Ouvrez la **Bibliothèque** (fiches), faites volontairement une erreur, demandez un indice. | Options remélangées à chaque erreur ; sas de sécurité après 3 erreurs en 60 s. |
| Fin d'escale | Notez le mot, passez à l'escale suivante, ou **Plonger plus profond** (même escale, grade supérieur). | Score, bonus, bouton **Imprimer le journal**. |
| Coffre | Après la dernière escale, saisissez les 11 mots (voir `README.md`, section solutions). | NARVAL, MOBILIS, CRESPO, ASTROLABE, PERLE, ISTHME, ATLANTIS, SARGASSES, BANQUISE, POULPE, MAELSTROM. |

## 3. Aller directement à un endroit (sans rien enregistrer)

Ajoutez ces paramètres à l'adresse, après `index.html` :

- `?verif=1&escale=7&niveau=lieutenant&enigme=2` : une énigme précise (escale 1 à 11, grades `mousse`, `matelot`, `timonier`, `lieutenant`, `second`).
- `&fin=1` : l'écran de fin d'escale. `?verif=1&coffre=1` : le coffre final.
- `&secours=1` : décors dessinés en code (sans les images ni les vidéos). `&reference=0` : ignore l'image de référence de l'enseignant.

Exemple : `http://127.0.0.1:8000/vingt-mille-lieues/index.html?verif=1&escale=9&niveau=timonier&enigme=3`

## 4. Pages pour l'enseignant

- **`prof.html`** : tableau de bord (équipes, progression, envoi d'un message ou d'un indice).
- **⚙️ Enseignant** (accueil) : choisir les escales jouées, imposer un grade, imprimer les corrigés.
- **`lecons-imprimables.html`** : toutes les fiches de leçon en A4.
- **`medias.html`** : état de chaque image et vidéo (déposée ou de secours), avec aperçu.

## 5. Qu'est-ce qu'il faut vérifier, vous ?

1. **Programme** : `PLAN.md` § 4 (matrice escales × programmation 2026). Manque-t-il une notion ?
2. **Faits** : `A-VERIFIER.md` (chiffres, dates, chapitres du roman à confirmer).
3. **Cohérence avec le roman** : `COHERENCE.md` § 4 et 5, et les scénarimages (`scenarimages/escale-NN.md`, une page par escale).
4. **Solutions** : `README.md` donne les réponses de chaque énigme à chaque grade ; `GUIDE-PEDAGOGIQUE.md` les fiches d'ancrage.
5. **Médias** : regardez les vidéos et les décors. Pour en remplacer un, déposez un fichier du même nom (`assets/videos/transition-eN.mp4`, `assets/images/decors/<décor>.webp`). Le moteur le prend aussitôt ; supprimez-le pour revenir au précédent.

## 6. Vérifications automatiques

Depuis la racine du dépôt (Node.js requis, une fois `npm install` fait dans `outils-tests`) :

```
bash outils-tests/verifier-isolation.sh                        # doit afficher « OK » : aucun jeu existant modifié
node vingt-mille-lieues/tests/test-jeu.js                      # toutes les escales, tous les grades (≈ 1 min)
node vingt-mille-lieues/tests/test-coherence-narrative.js
node vingt-mille-lieues/tests/test-medias.js
node outils-tests/tous.js                                      # tous les jeux du dépôt (≈ 13 min)
```

Un seul échec est attendu dans `tous.js`, et il date d'avant ce travail : `commun/test-hors-ligne` (voir `BASELINE-TESTS.md`).

## 7. Si quelque chose ne marche pas

- **Pas de vidéo / décor dessiné à la place de l'image** : vous avez ouvert `index.html` directement (protocole `file:`) ou ajouté `&secours=1`. Passez par `lancer.bat`.
- **Vieille version affichée** : l'application se met en cache. Rechargez avec Ctrl + Maj + R, ou videz les données du site dans Chrome.
- **Pas de son** : cliquez une fois dans la page (Chrome bloque le son avant le premier clic) ; vérifiez le réglage du son dans ⚙️.
