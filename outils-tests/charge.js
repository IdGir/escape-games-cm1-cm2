/* ============================================================
   CHARGEUR COMMUN DES TESTS (Node + jsdom)
   ------------------------------------------------------------
   Ouvre une page d'un jeu (index.html, prof.html…) dans jsdom, sans
   réseau ni serveur : les <script src> sont lus sur le disque, fetch()
   est simulé à partir des fichiers du dépôt. Les chemins relatifs
   (« js/app.js », « ../commun/js/media.js ») sont résolus comme le
   ferait le navigateur, à partir de la racine du dépôt.
   ============================================================ */
const fs = require("fs"), path = require("path");
let JSDOM;
try { ({ JSDOM } = require("jsdom")); }
catch (e) {
  console.error("jsdom est introuvable. Installez-le une fois, hors du dépôt :\n" +
    "  npm install jsdom   (dans un dossier parent), ou définissez NODE_PATH.");
  process.exit(2);
}
const RACINE = path.resolve(__dirname, "..");

/** Convertit une adresse http://localhost/... en chemin de fichier du dépôt. */
function fichierDe(url){
  const u = new URL(url);
  if (u.hostname !== "localhost") return null;
  return path.join(RACINE, decodeURIComponent(u.pathname));
}

/**
 * @param {string} dossierJeu  chemin absolu du dossier du jeu
 * @param {string} query       « ?salle=3&niveau=CM1 », par exemple
 * @param {object} options     { page:"index.html", stockage:{cle:valeur}, avant:(w)=>{} }
 */
async function charger(dossierJeu, query = "", options = {}){
  const page = options.page || "index.html";
  const nomJeu = path.relative(RACINE, dossierJeu).split(path.sep).join("/");
  const urlPage = `http://localhost/${nomJeu}/${page}${query}`;
  const html = fs.readFileSync(path.join(dossierJeu, page), "utf8");
  const scripts = [...html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/g)].map(m => {
    const src = (m[1].match(/\bsrc="([^"]+)"/) || [])[1];
    return { src, code: m[2] };
  });
  const sansScripts = html.replace(/<script\b[\s\S]*?<\/script>/g, "");
  const erreurs = [];
  const dom = new JSDOM(sansScripts, { url: urlPage, runScripts: "dangerously", pretendToBeVisual: true });
  const w = dom.window;
  if (options.stockage) for (const [k, v] of Object.entries(options.stockage)) w.localStorage.setItem(k, v);
  w.fetch = async (url) => {
    const f = fichierDe(new URL(String(url), w.location.href).href);
    const ok = !!f && fs.existsSync(f) && fs.statSync(f).isFile();
    const lire = () => fs.readFileSync(f, "utf8");
    return { ok, status: ok ? 200 : 404, json: async () => JSON.parse(lire()), text: async () => lire(),
             headers: { get: () => null } };
  };
  w.print = () => { w.__imprime = (w.__imprime || 0) + 1; };
  w.scrollTo = () => {}; w.confirm = () => true; w.alert = () => {};
  w.open = () => null;
  w.HTMLElement.prototype.scrollIntoView = function(){};
  w.HTMLMediaElement.prototype.play = function(){ return Promise.resolve(); };
  w.HTMLMediaElement.prototype.pause = function(){};
  w.HTMLMediaElement.prototype.load = function(){};
  w.Image = class { set src(v){ setTimeout(() => this.onerror && this.onerror(), 0); } };
  if (!w.CSS) w.CSS = {};
  if (!w.CSS.escape) w.CSS.escape = s => String(s).replace(/["\\]/g, "\\$&");
  if (!w.matchMedia) w.matchMedia = () => ({ matches: false, addEventListener(){}, removeEventListener(){}, addListener(){}, removeListener(){} });
  w.addEventListener("error", e => erreurs.push("JS: " + e.message));
  w.console.error = (...a) => erreurs.push(a.join(" "));
  if (options.silencieux !== false) { w.console.warn = () => {}; w.console.info = () => {}; w.console.log = () => {}; }
  if (options.avant) options.avant(w);
  const injecter = (code, nom) => {
    const el = w.document.createElement("script");
    el.textContent = code + (nom ? `\n//# sourceURL=${nom}` : "");
    w.document.body.appendChild(el);
  };
  for (const s of scripts) {
    if (s.src) {
      const f = fichierDe(new URL(s.src, urlPage).href);
      if (f && fs.existsSync(f)) injecter(fs.readFileSync(f, "utf8"), s.src);
      else erreurs.push("script introuvable : " + s.src);
    } else if (s.code.trim()) injecter(s.code);
  }
  w.document.dispatchEvent(new w.Event("DOMContentLoaded"));
  w.dispatchEvent(new w.Event("load"));
  await new Promise(r => setTimeout(r, options.attente || 300));
  return { dom, w, erreurs };
}

/* ---- Petits outils partagés par tous les tests ---- */
function compteur(titre){
  let echecs = 0, oks = 0;
  const ok = (c, m) => { if (c) oks++; else { echecs++; console.log("  ✗ " + m); } };
  const fin = () => {
    console.log(`\n${titre} : ${oks} vérifications réussies, ${echecs} échec(s).`);
    process.exit(echecs ? 1 : 0);
  };
  const exception = e => { echecs++; console.log("  ✗ EXCEPTION " + (e && e.stack || e)); };
  return { ok, fin, exception, get echecs(){ return echecs; } };
}
const dodo = ms => new Promise(r => setTimeout(r, ms));
async function attendreQue(fn, max = 6000){
  const t0 = Date.now();
  while (Date.now() - t0 < max) { const r = fn(); if (r) return r; await dodo(40); }
  return null;
}
const clic = (w, el) => el && el.dispatchEvent(new w.MouseEvent("click", { bubbles: true }));

module.exports = { charger, compteur, dodo, attendreQue, clic, RACINE };
