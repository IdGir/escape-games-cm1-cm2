/* ============================================================
   SERVICE WORKER du jeu « renaissance » (hors connexion)
   ------------------------------------------------------------
   Portée : immersifs/renaissance/ uniquement ; cache propre (« vml-… »),
   jamais partagé avec les autres jeux. Le code et les données sont
   mis en cache à l'installation ; les médias déposés (images, vidéos)
   le sont au premier affichage. Réseau d'abord pour les JSON (une
   correction est vue tout de suite), cache d'abord pour le reste.
   Changer VERSION à chaque publication (le test le contrôle).
   ============================================================ */
const VERSION = "vml-renaissance-1";
const FICHIERS = [
  "./", "index.html", "prof.html", "medias.html", "lecons-imprimables.html", "manifest.webmanifest", "css/nautilus.css", "css/enigmes-nautilus.css", "css/theme.css", "js/jeu-config.js", "js/donnees-embarquees.js", "js/donnees.js", "js/niveaux.js", "js/sons.js", "js/decors-secours.js", "js/scene.js", "js/personnages.js", "js/voix.js", "js/type-circuit.js", "js/solutions.js", "js/moteur.js", "js/bibliotheque.js", "js/journal.js", "js/reglages.js", "js/sync-nautilus.js", "js/app.js", "assets/data/enigmes.json", "assets/data/lecons.json", "assets/data/decors-fx.json", "assets/data/dialogues.json", "assets/data/personnages.json", "assets/images/ui/icone.svg", "../../commun/js/enigmes.js", "../../commun/polices/atkinson-hyperlegible-latin-400-normal.woff2", "../../commun/polices/atkinson-hyperlegible-latin-700-normal.woff2", "../../commun/polices/opendyslexic-latin-400-normal.woff2", "../../commun/polices/opendyslexic-latin-700-normal.woff2"
];
self.FICHIERS_NAUTILUS = FICHIERS;

self.addEventListener("install", ev => {
  ev.waitUntil(caches.open(VERSION).then(c => Promise.all(FICHIERS.map(f => c.add(new Request(f, { cache: "reload" })).catch(() => null)))).then(() => self.skipWaiting()));
});
self.addEventListener("activate", ev => {
  ev.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k.startsWith("vml-renaissance-") && k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener("fetch", ev => {
  const req = ev.request;
  if(req.method !== "GET") return;
  const url = new URL(req.url);
  if(url.pathname.includes("/api/")) return;
  const json = url.pathname.endsWith(".json");
  if(json){
    ev.respondWith(fetch(req).then(r => { if(r.ok){ const c = r.clone(); caches.open(VERSION).then(k => k.put(req, c)); } return r; }).catch(() => caches.match(req, { ignoreSearch: true })));
    return;
  }
  ev.respondWith(caches.match(req, { ignoreSearch: true }).then(hit => hit || fetch(req).then(r => {
    if(r.ok && url.origin === location.origin && /\/assets\/(images|videos)\//.test(url.pathname)){ const c = r.clone(); caches.open(VERSION).then(k => k.put(req, c)); }
    return r;
  })));
});
