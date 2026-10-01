/* Tests automatiques — Le Laboratoire de Madame Mélange (Node + jsdom)
   Depuis la racine du dépôt :  node melanges/tests/test-jeu.js
   (jsdom requis : voir outils-tests/README.md). Étapes au choix :
   node melanges/tests/test-jeu.js partie   (ou types, divers, prof) */
require("../../outils-tests/moteur-commun").lancer(__dirname + "/..", {
  titre: "Le Laboratoire de Madame Mélange",
  scoresMax: { CM1: 185, CM2: 235 },
});
