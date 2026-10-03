/* Tests automatiques — Le Phare de l'île Lumière (Node + jsdom)
   Depuis la racine du dépôt :  node lumiere/tests/test-jeu.js
   (jsdom requis : voir outils-tests/README.md). Étapes au choix :
   node lumiere/tests/test-jeu.js partie   (ou types, divers, prof) */
require("../../outils-tests/moteur-commun").lancer(__dirname + "/..", {
  titre: "Le Phare de l'île Lumière",
  scoresMax: { CM1: 185, CM2: 235 },
});
