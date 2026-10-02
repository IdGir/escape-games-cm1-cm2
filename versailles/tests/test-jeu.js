/* Tests automatiques — De l'édit de Nantes à Versailles (Node + jsdom)
   Depuis la racine du dépôt :  node versailles/tests/test-jeu.js
   (jsdom requis : voir outils-tests/README.md). Étapes au choix :
   node versailles/tests/test-jeu.js partie   (ou types, divers, prof) */
require("../../outils-tests/moteur-commun").lancer(__dirname + "/..", {
  titre: "De l'édit de Nantes à Versailles",
  scoresMax: { CM1: 185, CM2: 235 },
});
