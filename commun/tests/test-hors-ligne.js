/* ============================================================
   TESTS — application installable, hors connexion (A4)
   Depuis la racine du dépôt :  node commun/tests/test-hors-ligne.js
   1. sw-fichiers.js est à jour : tous les fichiers listés existent, et
      tout ce que chargent les pages (scripts, styles, données) y figure.
   2. sw.js simulé dans Node : installation (fichiers gardés), puis
      réponses HORS CONNEXION depuis le cache (pages, scripts « ?c1 »,
      navigation vers un dossier), images gardées à la demande,
      vidéos et /api/ jamais interceptées.
   ============================================================ */
const fs = require("fs"), path = require("path"), vm = require("vm");
const { compteur, RACINE } = require("../../outils-tests/charge");
const T = compteur("Hors connexion (PWA)"); const ok = T.ok;
const BASE = "https://idgir.github.io/escape-games-cm1-cm2/";

function liste(){
  const ctx = { self: {} }; vm.createContext(ctx);
  vm.runInContext(fs.readFileSync(path.join(RACINE, "sw-fichiers.js"), "utf8"), ctx);
  return ctx.self;
}

function controleListe(L){
  console.log("\n== sw-fichiers.js ==");
  ok(/^[0-9a-f]{10}$/.test(L.VERSION_HORS_LIGNE), "numéro de version");
  // même calcul que outils-pwa/maj-hors-ligne.py : la version suit le contenu des fichiers
  const crypto = require("crypto"), h = crypto.createHash("sha1");
  for (const f of L.FICHIERS_CODE.concat(...Object.values(L.IMAGES_JEUX))) {
    if (!fs.existsSync(path.join(RACINE, f))) continue;
    h.update(Buffer.from(f, "utf8")); h.update(crypto.createHash("sha1").update(fs.readFileSync(path.join(RACINE, f))).digest());
  }
  ok(h.digest("hex").slice(0, 10) === L.VERSION_HORS_LIGNE, "version à jour (sinon : python outils-pwa/maj-hors-ligne.py avant de publier)");
  const absents = L.FICHIERS_CODE.filter(f => !fs.existsSync(path.join(RACINE, f)));
  ok(!absents.length, "fichiers listés présents sur le disque " + absents.slice(0, 5).join(", "));
  const pages = ["index.html", "classement.html", "resultats.html"].concat(
    ["chateau-fort", "constitution", "declaration", "melanges", "mission-geo", "moyen-age-abbaye", "objets-techniques", "station-meteo", "tour-du-monde"]
      .flatMap(j => [j + "/index.html", j + "/lecons-imprimables.html"]));
  const manquants = [];
  for (const p of pages) {
    ok(L.FICHIERS_CODE.includes(p), `${p} gardé hors connexion`);
    const h = fs.readFileSync(path.join(RACINE, p), "utf8");
    for (const m of h.matchAll(/(?:src|href)="([^"#:]+\.(?:js|css|webmanifest)(?:\?[^"]*)?)"/g)) {
      const f = path.posix.normalize(path.posix.join(path.posix.dirname(p), m[1].split("?")[0]));
      if (!L.FICHIERS_CODE.includes(f)) manquants.push(p + " → " + f);
    }
  }
  ok(!manquants.length, "tout ce que chargent les pages est gardé (sinon : python outils-pwa/maj-hors-ligne.py) " + manquants.slice(0, 5).join(" ; "));
  ok(["melanges/assets/data/enigmes.json", "commun/polices/opendyslexic-latin-400-normal.woff2", "commun/donnees/catalogue.js"].every(f => L.FICHIERS_CODE.includes(f)), "données, polices et catalogue gardés");
  ok(!L.FICHIERS_CODE.some(f => /\.(mp4|webm)$/.test(f)) && !L.FICHIERS_CODE.some(f => /^outils-|\/tests\//.test(f)), "ni vidéos, ni outils, ni tests");
}

/* Mini-environnement de service worker */
function environnement(){
  const caches = new Map();
  const cle = (u, ign) => { const x = new URL(typeof u === "string" ? u : u.url); if (ign) x.search = ""; return x.href; };
  const cacheAPI = {
    open: async n => { if (!caches.has(n)) caches.set(n, new Map()); const m = caches.get(n);
      return { put: async (u, r) => { m.set(cle(u), await r.clone().text()); },
               match: async (u, o = {}) => { for (const [k, v] of m) if (cle(k, o.ignoreSearch) === cle(u, o.ignoreSearch)) return new Response(v, { status: 200 }); return undefined; },
               keys: async () => [...m.keys()].map(k => ({ url: k })) }; },
    keys: async () => [...caches.keys()], delete: async n => caches.delete(n)
  };
  let enLigne = true; const appels = [];
  const fetchDisque = async u => {
    const url = typeof u === "string" ? u : u.url; appels.push(url);
    if (!enLigne) throw new TypeError("Failed to fetch");
    const rel = decodeURIComponent(new URL(url).pathname.replace("/escape-games-cm1-cm2/", "")) || "index.html";
    const f = path.join(RACINE, rel.endsWith("/") || rel === "" ? rel + "index.html" : rel);
    return fs.existsSync(f) && fs.statSync(f).isFile() ? new Response(fs.readFileSync(f)) : new Response("", { status: 404 });
  };
  const ecouteurs = {};
  const self = { location: new URL(BASE + "sw.js"), addEventListener: (t, f) => (ecouteurs[t] = f), skipWaiting: async () => {}, clients: { claim: async () => {} } };
  const ctx = { self, caches: cacheAPI, fetch: fetchDisque, Response, Request, URL, setTimeout, Promise, console,
    importScripts: f => vm.runInContext(fs.readFileSync(path.join(RACINE, f), "utf8"), ctx) };
  vm.createContext(ctx);
  vm.runInContext(fs.readFileSync(path.join(RACINE, "sw.js"), "utf8"), ctx);
  const evenement = async (type, extra = {}) => { let p = null, rep = null;
    const ev = Object.assign({ waitUntil: x => (p = x), respondWith: x => (rep = x) }, extra);
    ecouteurs[type](ev); if (p) await p; return rep ? await rep : null; };
  const requete = (u, o = {}) => new Request(u, o);
  return { evenement, caches, setEnLigne: v => (enLigne = v), appels, requete };
}

async function simulation(L){
  console.log("\n== sw.js simulé ==");
  const E = environnement();
  await E.evenement("install");
  const code = E.caches.get("eg-code-" + L.VERSION_HORS_LIGNE);
  ok(code && code.size === L.FICHIERS_CODE.length + 1, `installation : ${code ? code.size : 0} fichiers gardés (attendu ${L.FICHIERS_CODE.length + 1})`);
  await E.evenement("activate");
  E.setEnLigne(false);
  const lire = async (u, o) => { const r = await E.evenement("fetch", { request: E.requete(u, o) }); return r ? { status: r.status, texte: await r.text() } : null; };
  const a = await lire(BASE + "melanges/js/jeu.js?c1");
  ok(a && a.status === 200 && /var JEU = \{/.test(a.texte), "hors connexion : melanges/js/jeu.js?c1 servi depuis le cache");
  const b = await lire(BASE + "commun/js/enigmes.js?c9");
  ok(b && b.status === 200 && /activerEnigme/.test(b.texte), "hors connexion : autre numéro de version (?c9) → même fichier");
  const c = await lire(BASE + "chateau-fort/", { mode: "same-origin" });
  ok(c && c.status === 200 && /<html/i.test(c.texte), "hors connexion : chateau-fort/ → sa page index.html");
  const d = await lire(BASE + "station-meteo/assets/data/enigmes.json");
  ok(d && d.status === 200 && JSON.parse(d.texte).salles, "hors connexion : données JSON des énigmes");
  const v = await E.evenement("fetch", { request: E.requete(BASE + "melanges/assets/videos/salle1.mp4") });
  ok(v === null, "vidéos : jamais interceptées (le jeu retombe sur l'image ou le dessin)");
  const api = await E.evenement("fetch", { request: E.requete(BASE + "api/equipes") });
  ok(api === null, "/api/… : jamais intercepté");
  // images à la demande
  E.setEnLigne(true);
  const jeu = Object.keys(L.IMAGES_JEUX)[0];
  let reponse = null;
  await E.evenement("message", { data: { type: "preparer-images", jeu }, source: { postMessage: m => (reponse = m) } });
  ok(reponse && reponse.ok === L.IMAGES_JEUX[jeu].length, `images de ${jeu} gardées à la demande (${reponse && reponse.ok}/${L.IMAGES_JEUX[jeu].length})`);
  E.setEnLigne(false);
  const img = await lire(BASE + encodeURI(L.IMAGES_JEUX[jeu][0]));
  ok(img && img.status === 200 && img.texte.length > 100, "hors connexion : image gardée servie");
  const absente = await lire(BASE + "melanges/assets/images/decors/inexistant.jpg");
  ok(absente && absente.status === 404, "image jamais vue, hors connexion : 404 (le jeu affiche son dessin)");
  let etat = null;
  await E.evenement("message", { data: { type: "etat" }, source: { postMessage: m => (etat = m) } });
  ok(etat && etat.code === L.FICHIERS_CODE.length + 1 && etat.images[jeu].gardees === L.IMAGES_JEUX[jeu].length, "message « etat » : fichiers et images gardés");
}

(async () => {
  try { const L = liste(); controleListe(L); await simulation(L); } catch (e) { T.exception(e); }
  T.fin();
})();
