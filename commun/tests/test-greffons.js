/* ============================================================
   TESTS DES GREFFONS DU TRONC COMMUN (Node + jsdom)
   Depuis la racine du dépôt :  node commun/tests/test-greffons.js
   Une section par amélioration (B6, E4, E2…), chacune sur plusieurs
   jeux : un greffon s'appuie sur des fonctions des app.js, qui
   restent propres à chaque jeu.
   Étapes au choix : node commun/tests/test-greffons.js B6,E4
   ============================================================ */
const path = require("path");
const { charger, compteur, dodo, attendreQue, RACINE } = require("../../outils-tests/charge");
const T = compteur("Greffons du tronc commun"); const ok = T.ok;
const J = j => path.join(RACINE, j);
const JEUX8 = ["declaration", "tour-du-monde", "constitution", "moyen-age-abbaye", "station-meteo", "melanges", "objets-techniques", "chateau-fort"];
const SECTIONS = {};

/* ---- B6 : transitions entre salles ---- */
SECTIONS.B6 = async () => {
  console.log("\n== B6 : transitions entre salles ==");
  for (const j of ["melanges", "tour-du-monde", "station-meteo"]) {
    const { w, erreurs } = await charger(J(j), "?salle=1&niveau=CM2");
    ok(typeof w.TRANSITIONS === "object", `${j} : greffon chargé`);
    w.afficherSalle(2); await dodo(20);
    const r = w.document.querySelector(".rideau-salle");
    ok(!!r && /2/.test(r.textContent), `${j} : rideau à l'entrée de la salle 2 (« ${r ? r.textContent : "—"} »)`);
    if (j === "tour-du-monde") ok(r && /Escale 2/.test(r.textContent), `${j} : le rideau dit « Escale »`);
    await dodo(1400);
    ok(!w.document.querySelector(".rideau-salle"), `${j} : le rideau disparaît seul`);
    w.document.body.classList.add("calme");
    w.afficherSalle(3); await dodo(20);
    ok(!w.document.querySelector(".rideau-salle"), `${j} : aucun rideau avec « animations réduites »`);
    ok(erreurs.length === 0, `${j} : erreurs JS : ` + erreurs.join(" | "));
  }
  const m = await charger(J("mission-geo"), "");
  ok(typeof m.w.TRANSITIONS === "object" && m.erreurs.length === 0, "mission-geo : greffon chargé sans erreur");
};

/* ---- E4 : police et réglages « dyslexie » ---- */
SECTIONS.E4 = async () => {
  console.log("\n== E4 : lecture facilitée ==");
  for (const j of ["melanges", "declaration", "mission-geo"]) {
    const { w, erreurs } = await charger(J(j), j === "mission-geo" ? "" : "?salle=1&niveau=CM1");
    const d = w.document;
    if (j === "mission-geo") { w.eval("REGLAGES.ouvrir()"); } else { w.ouvrirReglages(); }
    const bloc = await attendreQue(() => d.getElementById("lecture-reglages"), 3000);
    ok(!!bloc, `${j} : bloc « Lecture facilitée » dans les réglages`);
    if (!bloc) continue;
    d.getElementById("lec-police").value = "dys";
    d.getElementById("lec-interligne").value = "tres";
    d.getElementById("lec-espacement").checked = true;
    bloc.dispatchEvent(new w.Event("change", { bubbles: true }));
    ok(d.body.classList.contains("police-dys") && d.body.classList.contains("interligne-tres") && d.body.classList.contains("espacement-lecture"), `${j} : classes appliquées tout de suite`);
    ok(JSON.parse(w.localStorage.getItem("escape_lecture")).police === "dys", `${j} : choix gardé (escape_lecture)`);
    ok(/opendyslexic-latin-400-normal\.woff2/.test(d.getElementById("style-lecture").textContent) && /commun\/polices\//.test(d.getElementById("style-lecture").textContent), `${j} : police chargée depuis commun/polices/`);
    ok(erreurs.length === 0, `${j} : erreurs JS : ` + erreurs.join(" | "));
  }
  // préférence gardée d'un jeu à l'autre
  const { w } = await charger(J("chateau-fort"), "?salle=1&niveau=CM1", { stockage: { escape_lecture: JSON.stringify({ police: "lisible", interligne: "aere", espacement: false }) } });
  ok(w.document.body.classList.contains("police-lisible") && w.document.body.classList.contains("interligne-aere"), "chateau-fort : préférence d'un autre jeu appliquée dès l'ouverture");
};

module.exports = { SECTIONS, charger, ok, dodo, attendreQue, J, JEUX8 };
if (require.main === module) {
  const choix = process.argv[2] ? process.argv[2].split(",") : Object.keys(SECTIONS);
  (async () => {
    try { for (const s of choix) await SECTIONS[s](); } catch (e) { T.exception(e); }
    T.fin();
  })();
}
