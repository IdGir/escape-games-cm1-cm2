/* ============================================================
   TESTS DES PAGES COMMUNES (Node + jsdom)
   Depuis la racine du dépôt :  node commun/tests/test-pages.js
   classement.html (D1) et les pages publiques ajoutées ensuite.
   Étapes au choix : node commun/tests/test-pages.js D1
   ============================================================ */
const { charger, compteur, dodo, attendreQue, RACINE } = require("../../outils-tests/charge");
const T = compteur("Pages communes"); const ok = T.ok;
const SECTIONS = {};

/** Simule le serveur local : /api/equipes renvoie les équipes données. */
const avecEquipes = equipes => w => {
  const f = w.fetch;
  w.fetch = async (url, o) => /\/api\/equipes/.test(String(url))
    ? { ok: true, status: 200, json: async () => ({ equipes }), text: async () => "" } : f(url, o);
};

SECTIONS.D1 = async () => {
  console.log("\n== D1 : écran de classement ==");
  const equipes = [
    { equipe: "Les Lynx", jeu: "melanges", niveau: "CM2", salle: 3, enigme: 1, score: 60, msEcoules: 900000 },
    { equipe: "Les Hiboux", jeu: "melanges", niveau: "CM1", salle: 4, enigme: 0, score: 40, msEcoules: 800000, palier: "decouverte" },
    { equipe: "Les Renards", jeu: "melanges", niveau: "CM2", salle: 5, score: 150, fini: true, msEcoules: 1800000 },
    { equipe: "Autre jeu", jeu: "declaration", niveau: "CM2", salle: 2, score: 20 }
  ];
  const { w, erreurs } = await charger(RACINE, "?jeu=melanges", { page: "classement.html", avant: avecEquipes(equipes), attente: 400 });
  await attendreQue(() => w.document.querySelectorAll("#liste li").length, 3000);
  const noms = [...w.document.querySelectorAll("#liste li .nom")].map(n => n.firstChild.textContent);
  ok(noms.length === 3, `seulement les équipes du jeu choisi (${noms.length})`);
  ok(noms.join(",") === "Les Renards,Les Hiboux,Les Lynx", "classé par progression : " + noms.join(", "));
  ok(!/⭐/.test(w.document.getElementById("liste").textContent), "affichage par défaut : progression, sans les scores");
  ok(/🌱/.test(w.document.getElementById("liste").textContent), "palier Découverte signalé");
  const a = w.document.getElementById("choix-affichage"); a.value = "score"; a.dispatchEvent(new w.Event("change"));
  await dodo(100);
  const noms2 = [...w.document.querySelectorAll("#liste li .nom")].map(n => n.firstChild.textContent);
  ok(noms2.join(",") === "Les Renards,Les Lynx,Les Hiboux" && /⭐/.test(w.document.getElementById("liste").textContent), "classé par score : " + noms2.join(", "));
  ok(!w.document.querySelector("button[onclick], .actions"), "aucune commande de pilotage sur l'écran de projection");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
  const sans = await charger(RACINE, "", { page: "classement.html", attente: 400 });
  ok(/lancer\.bat/.test(sans.w.document.getElementById("vide").textContent), "sans serveur : message explicatif");
};

module.exports = { SECTIONS, avecEquipes };
if (require.main === module) {
  const choix = process.argv[2] ? process.argv[2].split(",") : Object.keys(SECTIONS);
  (async () => { try { for (const s of choix) await SECTIONS[s](); } catch (e) { T.exception(e); } T.fin(); })();
}
