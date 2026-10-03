/* Tests automatiques — Le Grand Repas du chef (Node + jsdom)
   Depuis la racine du dépôt :  node alimentation/tests/test-jeu.js
   (jsdom requis : voir outils-tests/README.md). Étapes au choix :
   node alimentation/tests/test-jeu.js partie   (ou types, divers, prof) */
require("../../outils-tests/moteur-commun").lancer(__dirname + "/..", {
  titre: "Le Grand Repas du chef",
  scoresMax: { CM1: 185, CM2: 235 },
});
