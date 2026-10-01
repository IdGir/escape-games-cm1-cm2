/* Tests automatiques — Le Sceau de la République (Node + jsdom)
   Depuis la racine du dépôt :  node constitution/tests/test-jeu.js
   (jsdom requis : voir outils-tests/README.md). Étapes au choix :
   node constitution/tests/test-jeu.js partie   (ou types, divers, prof) */
require("../../outils-tests/moteur-commun").lancer(__dirname + "/..", {
  titre: "Le Sceau de la République",
  scoresMax: { CM1: 185, CM2: 235 },
  /* Propre à ce jeu : le concours (concours.json) */
  plus: async ({ charger, ok }) => {
    console.log("\n== Concours (encart de fin de partie) ==");
    const { w, erreurs } = await charger("?salle=6&niveau=CM2");
    await new Promise(r => setTimeout(r, 300));
    const c = w.donneesConcours();
    ok(c && c.nom && Array.isArray(c.liens) && c.liens.length >= 1, "concours.json : nom et liens");
    const zone = w.document.getElementById("zone-concours");
    if (zone) { w.afficherConcours(); ok(zone.textContent.includes(c.nom) && !/undefined/.test(zone.innerHTML), "encart du concours affiché sans valeur manquante"); }
    ok(erreurs.length === 0, "concours : erreurs JS : " + erreurs.join(" | "));
  }
});
