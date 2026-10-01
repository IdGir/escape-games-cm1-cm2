/* ============================================================
   SERVICE WORKER — application installable, hors connexion (amélioration A4)
   ------------------------------------------------------------
   Une fois le site ouvert une fois avec internet (et, si l'on veut,
   « installé » sur la tablette), les jeux fonctionnent SANS RÉSEAU et
   sans lancer serveur.py :
     • pages, scripts, styles, polices et données des 9 jeux sont gardés
       dès la première visite (liste : sw-fichiers.js, ~4 Mo) ;
     • les images d'un jeu sont gardées quand on les voit, ou toutes
       d'un coup avec le bouton « Préparer pour le hors-ligne » de l'accueil ;
     • les vidéos ne sont pas gardées : hors connexion, le jeu montre
       l'image ou le décor dessiné à la place (comme sans fichier) ;
     • le tableau de bord en direct (/api/…) reste réservé au mode local.
   Avec internet, la version en ligne est toujours prise en priorité :
   les mises à jour arrivent d'elles-mêmes.
   ============================================================ */
importScripts("sw-fichiers.js");
const CACHE_CODE = "eg-code-" + self.VERSION_HORS_LIGNE;
const CACHE_IMAGES = "eg-images";
const BASE = new URL("./", self.location).href;      // racine du site (GitHub Pages ou serveur local)
const VIDEO = /\.(mp4|webm|m4v|ogv)$/i, IMAGE = /\.(jpe?g|png|webp|gif|svg|pdf)$/i;

self.addEventListener("install", ev => {
  ev.waitUntil((async () => {
    const c = await caches.open(CACHE_CODE);
    // fichier par fichier : un fichier manquant n'empêche pas l'installation
    await Promise.all([BASE, ...self.FICHIERS_CODE.map(f => BASE + encodeURI(f))].map(u =>
      fetch(u, { cache: "no-cache" }).then(r => r.ok ? c.put(u, r) : null).catch(() => null)));
    await self.skipWaiting();
  })());
});

self.addEventListener("activate", ev => {
  ev.waitUntil((async () => {
    for(const k of await caches.keys()) if(k.startsWith("eg-code-") && k !== CACHE_CODE) await caches.delete(k);
    await self.clients.claim();
  })());
});

/* Réseau d'abord (avec un délai court), puis la copie gardée */
async function reseauPuisCache(req){
  const c = await caches.open(CACHE_CODE);
  try{
    const r = await Promise.race([fetch(req), new Promise((_, ko) => setTimeout(() => ko(new Error("délai")), 4000))]);
    if(r && r.ok && req.method === "GET") c.put(req, r.clone());
    return r;
  }catch(e){
    const url = new URL(req.url); url.search = "";            // « app.js?c2 » → « app.js »
    return (await c.match(req, { ignoreSearch: true })) || (await c.match(url.href))
      || (url.pathname.endsWith("/") ? await c.match(url.href + "index.html") : null)
      || (req.mode === "navigate" ? await c.match(BASE) : null)
      || new Response("Hors connexion : ce fichier n'a pas encore été gardé sur cet appareil.", { status: 503, headers: { "Content-Type": "text/plain; charset=utf-8" } });
  }
}
/* Images : la copie gardée d'abord, sinon le réseau (et on la garde) */
async function cachePuisReseau(req){
  const c = await caches.open(CACHE_IMAGES);
  const gardee = await c.match(req, { ignoreSearch: true });
  if(gardee) return gardee;
  try{
    const r = await fetch(req);
    if(r && r.ok) c.put(req, r.clone());
    return r;
  }catch(e){ return new Response("", { status: 404 }); }    // le jeu retombe sur son dessin
}

self.addEventListener("fetch", ev => {
  const req = ev.request, url = new URL(req.url);
  if(req.method !== "GET" || url.origin !== self.location.origin) return;     // API GitHub, IA… : pas touché
  if(url.pathname.includes("/api/") || req.headers.has("range") || VIDEO.test(url.pathname)) return;
  ev.respondWith(IMAGE.test(url.pathname) ? cachePuisReseau(req) : reseauPuisCache(req));
});

/* Messages de l'accueil : état, et préparation des images d'un jeu */
self.addEventListener("message", ev => {
  const m = ev.data || {};
  const repondre = x => ev.source && ev.source.postMessage(Object.assign({ demande: m.type }, x));
  if(m.type === "etat"){
    ev.waitUntil((async () => {
      const c = await caches.open(CACHE_CODE), ci = await caches.open(CACHE_IMAGES);
      const gardes = (await c.keys()).length, images = (await ci.keys()).map(r => r.url);
      const parJeu = {};
      for(const [jeu, l] of Object.entries(self.IMAGES_JEUX)) parJeu[jeu] = { total: l.length, gardees: l.filter(f => images.includes(BASE + encodeURI(f))).length };
      repondre({ version: self.VERSION_HORS_LIGNE, code: gardes, codeTotal: self.FICHIERS_CODE.length + 1, images: parJeu });
    })());
  }
  if(m.type === "preparer-images" && self.IMAGES_JEUX[m.jeu]){
    ev.waitUntil((async () => {
      const ci = await caches.open(CACHE_IMAGES); let ok = 0;
      for(const f of self.IMAGES_JEUX[m.jeu]){
        try{ const r = await fetch(BASE + encodeURI(f)); if(r.ok){ await ci.put(BASE + encodeURI(f), r); ok++; } }catch(e){}
      }
      repondre({ jeu: m.jeu, ok, total: self.IMAGES_JEUX[m.jeu].length });
    })());
  }
});
