/* ============================================================
   TESTS — tronc commun (commun/) et onglet « Cohérence du moteur »
   Depuis la racine du dépôt :  node commun/tests/test-coherence.js
   1. Sur le disque : aucun jeu ne garde de copie d'un module commun,
      chaque index.html charge js/jeu.js en premier puis ../commun/js/…
   2. verifier.html#coherence : bilan vert sur le dépôt réel, puis
      détection d'une copie locale simulée (index.html modifié en mémoire).
   ============================================================ */
const fs = require("fs"), path = require("path");
const { charger, compteur, dodo, attendreQue, RACINE } = require("../../outils-tests/charge");
const T = compteur("Tronc commun et cohérence du moteur"); const ok = T.ok;
const JEUX8 = ["declaration", "tour-du-monde", "constitution", "moyen-age-abbaye", "station-meteo", "melanges", "objets-techniques", "chateau-fort"];
const COMMUNS = fs.readdirSync(path.join(RACINE, "commun", "js")).filter(f => f.endsWith(".js"));

function disque(){
  console.log("\n== Tronc commun sur le disque ==");
  for (const j of JEUX8.concat(["mission-geo"])) {
    const locaux = COMMUNS.filter(f => fs.existsSync(path.join(RACINE, j, "js", f))
      && !(["enigmes.js", "impression.js"].includes(f) && ["declaration", "tour-du-monde"].includes(j))
      && !(j === "mission-geo" && f !== "lecons-a4.js"));
    ok(!locaux.length, `${j} : pas de copie locale d'un module commun (${locaux.join(", ")})`);
    if (j === "mission-geo") continue;
    const html = fs.readFileSync(path.join(RACINE, j, "index.html"), "utf8");
    const scripts = [...html.matchAll(/<script src="([^"]+)"/g)].map(m => m[1]);
    ok(/^js\/jeu\.js/.test(scripts[0] || ""), `${j} : js/jeu.js chargé en premier`);
    for (const s of scripts.filter(s => s.startsWith("../commun/"))) ok(fs.existsSync(path.join(RACINE, j, s.split("?")[0])), `${j} : ${s} existe`);
  }
}

async function onglet(){
  console.log("\n== verifier.html : onglet Cohérence du moteur ==");
  const { w, erreurs } = await charger(RACINE, "#coherence", { page: "verifier.html", attente: 500 });
  const bilan = await attendreQue(() => w.document.querySelector(".bilan-coh"), 15000);
  ok(!!bilan, "onglet affiché");
  ok(bilan && bilan.classList.contains("ok"), "bilan vert sur le dépôt : " + (bilan ? bilan.textContent : "—"));
  ok(w.document.querySelectorAll(".tab-coh td.ko").length === 0, "aucune case rouge");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
  // Régression simulée : melanges recharge sa propre copie de media.js
  const fetchVrai = w.fetch;
  w.fetch = async (url, o) => {
    const r = await fetchVrai(url, o);
    if (/melanges\/index\.html/.test(String(url))) {
      const t = (await r.text()).replace("../commun/js/media.js?c1", "js/media.js?v1");
      return { ok: true, status: 200, text: async () => t, json: async () => ({}), headers: { get: () => null } };
    }
    return r;
  };
  w.eval("COHERENCE = null; rendre();");
  const b2 = await attendreQue(() => { const b = w.document.querySelector(".bilan-coh"); return b && b.classList.contains("ko") ? b : null; }, 15000);
  ok(!!b2, "copie locale simulée : bilan rouge");
  const cases = [...w.document.querySelectorAll(".tab-coh td.ko")].map(td => td.textContent);
  ok(cases.includes("copie locale"), "copie locale simulée : case « copie locale » signalée");
}

(async () => {
  try { disque(); await onglet(); } catch (e) { T.exception(e); }
  T.fin();
})();
