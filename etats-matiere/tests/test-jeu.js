/* Tests automatiques — La Fabrique des états (Node + jsdom)
   Depuis la racine du dépôt :  node etats-matiere/tests/test-jeu.js
   (jsdom requis : voir outils-tests/README.md). Étapes au choix :
   node etats-matiere/tests/test-jeu.js partie   (ou types, divers, prof) */
require("../../outils-tests/moteur-commun").lancer(__dirname + "/..", {
  titre: "La Fabrique des états",
  scoresMax: { CM1: 185, CM2: 235 },
});
