#!/usr/bin/env node
/* ============================================================
   CONTRÔLE DE L'AFFICHAGE SUR TABLETTE ET SMARTPHONE (amélioration N17)
   ------------------------------------------------------------
   Les jeux sont conçus et testés surtout pour ordinateur et TBI, mais ils se
   jouent aussi sur les tablettes de la classe et, en mode individuel (D2), sur
   smartphone. Les contrôles A6 (cohérence du moteur) et B1 (charte) ne regardent
   pas la mise en page : ce script ouvre chaque jeu dans un VRAI navigateur
   (Chrome ou Edge, pilotés sans fenêtre) à trois largeurs types et vérifie, avant
   un `git push`, qu'aucun bouton essentiel ne sort de l'écran.

       node outils-tests/verifier-responsive.js                 tous les jeux, 4 écrans, captures
       node outils-tests/verifier-responsive.js melanges        un seul jeu
       node outils-tests/verifier-responsive.js --rapide        2 écrans par jeu, captures des seuls défauts
                                                                (c'est ce que lance le crochet pre-push)
   Options : --captures=aucune|defauts|toutes · --largeurs=tablette10,tablette7,smartphone

   Formats : tablette 10″ (1280 × 800), tablette 7″ (600 × 960), smartphone (390 × 844).
   Écrans : accueil du jeu · une énigme (salle 1, CM2) · le coffre final · l'écran de fin.
   Pour chaque écran et chaque format :
     ✗ bloquant   un bouton essentiel (démarrer, valider, indice, coffre, pause, réglages…) est
                  hors de l'écran (à gauche ou à droite), ou recouvert par un autre élément
                  une fois amené à l'écran par défilement (on peut défiler vers le bas, pas sur le côté) ;
     ⚠ à regarder la page défile horizontalement, ou un élément dépasse du bord de l'écran
                  (texte coupé, image trop large).
   Les captures sont rangées dans outils-tests/captures-responsive/ (non publié) :
   <jeu>-<format>-<écran>.png. Il faut un navigateur Chrome ou Edge installé
   (ou la variable CHROME_PATH) et, une fois, « npm install » dans outils-tests
   (puppeteer-core ne télécharge aucun navigateur). Sans navigateur : le contrôle est sauté (⚠).
   Code de sortie 1 s'il y a au moins un ✗ (le crochet pre-push bloque).
   ============================================================ */
const fs = require("fs");
const path = require("path");
const http = require("http");
const RACINE = path.resolve(__dirname, "..");

const FORMATS = {
  tablette10: { nom: "tablette 10″", width: 1280, height: 800, mobile: false },
  tablette7: { nom: "tablette 7″", width: 600, height: 960, mobile: true },
  smartphone: { nom: "smartphone", width: 390, height: 844, mobile: true }
};
const IMMERSIFS = ["alimentation", "chateau-fort", "constitution", "lumiere", "melanges", "moyen-age-abbaye", "objets-techniques", "renaissance", "station-meteo", "versailles"].map(j => "immersifs/" + j);
const JEUX_SALLES = ["declaration", "tour-du-monde", "constitution", "moyen-age-abbaye", "station-meteo", "melanges", "objets-techniques", "chateau-fort", "versailles", "renaissance", "alimentation", "lumiere"];
const VALIDER = '[data-valider], [id^="btn-verif"]';
const INDICE = '#btn-indice, [id^="indice-"]';
/* Variantes immersives (jouées par défaut) : accueil, énigme ouverte depuis l'objet du décor, coffre, fin d'escale */
const OUVRIR_ENIGME = "(function(){ var z = document.querySelector('.zone.cible'); if(z) z.dispatchEvent(new MouseEvent('click', { bubbles: true })); })()";
const ECRANS_IMMERSIFS = {
  accueil: { query: "", attend: "#btn-embarquer", essentiels: [["#btn-embarquer"], ["#nom-equipe"]] },
  decor: { query: "?verif=1&escale=1&niveau=matelot&enigme=1", attend: ".zone.cible", essentiels: [["#btn-pause"], ["#btn-reglages"]] },
  /* le panneau d'énigme est modal : seuls ses propres boutons doivent rester accessibles (pause et réglages sont derrière) */
  enigme: { query: "?verif=1&escale=1&niveau=matelot&enigme=1", attend: ".zone.cible", avant: OUVRIR_ENIGME, attendApres: ".enigme-carte .barre-outils",
            essentiels: [[VALIDER], ["[data-indice]"], [".fermer-panneau"]] }
};
const ecransDe = jeu => /^immersifs\//.test(jeu) ? ECRANS_IMMERSIFS : ECRANS;

/* Écrans : adresse, attente, action préalable, boutons essentiels (au moins un de chaque groupe doit exister) */
const ECRANS = {
  accueil: { query: "", attend: "#btn-demarrer", essentiels: [["#btn-demarrer"]] },
  enigme: { query: "?salle=1&niveau=CM2", attend: ".zone-enigme .barre-outils, #zone-enigme .barre-outils", essentiels: [[VALIDER], [INDICE], ["#btn-pause"], ["#btn-reglages"]] },
  coffre: { query: "?salle=1&niveau=CM2", attend: ".zone-enigme .barre-outils, #zone-enigme .barre-outils", avant: "afficherCoffre(function(){})", essentiels: [["#btn-coffre"], ["#btn-pause"]] },
  fin: { query: "?salle=6&niveau=CM2", attend: "#fin-contenu button", essentiels: [["#fin-contenu button"]], tous: "#fin-contenu button" }
};

/* ---------------- Navigateur et serveur statique ---------------- */
function trouverNavigateur(){
  const c = [process.env.CHROME_PATH,
    "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
    "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe", "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/usr/bin/google-chrome", "/usr/bin/google-chrome-stable", "/usr/bin/chromium", "/usr/bin/chromium-browser", "/usr/bin/microsoft-edge"].filter(Boolean);
  return c.find(f => { try{ return fs.statSync(f).isFile(); }catch(e){ return false; } }) || null;
}
const TYPES = { ".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8", ".css": "text/css; charset=utf-8", ".json": "application/json; charset=utf-8", ".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp", ".mp4": "video/mp4", ".woff2": "font/woff2", ".vtt": "text/vtt", ".webmanifest": "application/manifest+json" };
function serveur(){
  return new Promise(ok => {
    const s = http.createServer((req, res) => {
      let chemin = decodeURIComponent(req.url.split("?")[0]);
      if(chemin.startsWith("/api/")){ res.writeHead(404); res.end(); return; }
      let f = path.join(RACINE, chemin);
      if(!f.startsWith(RACINE)){ res.writeHead(403); res.end(); return; }
      try{ if(fs.statSync(f).isDirectory()) f = path.join(f, "index.html"); }catch(e){}
      fs.readFile(f, (err, data) => {
        if(err){ res.writeHead(404); res.end(); return; }
        res.writeHead(200, { "Content-Type": TYPES[path.extname(f).toLowerCase()] || "application/octet-stream", "Cache-Control": "no-store" });
        res.end(data);
      });
    });
    s.listen(0, "127.0.0.1", () => ok({ s, port: s.address().port }));
  });
}

/* ---------------- Mesures dans la page ---------------- */
function mesurer(ecran, formats){
  /* Exécutée dans le navigateur */
  return function(config){
    const vw = window.innerWidth, vh = window.innerHeight;
    const visible = el => { const r = el.getBoundingClientRect(), cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && cs.visibility !== "hidden" && cs.display !== "none" && cs.opacity !== "0"; };
    const nom = el => (el.id ? "#" + el.id : el.tagName.toLowerCase() + (el.className && typeof el.className === "string" ? "." + el.className.trim().split(/\s+/).slice(0, 2).join(".") : "")) + (el.textContent ? ` « ${el.textContent.trim().replace(/\s+/g, " ").slice(0, 30)} »` : "");
    const resultat = { vw, vh, essentiels: [], depassements: [], defileX: Math.max(document.documentElement.scrollWidth, document.body ? document.body.scrollWidth : 0) - document.documentElement.clientWidth };   // le body masque parfois le débordement (overflow-x:hidden) : le texte est alors coupé
    const verifier = el => {
      el.scrollIntoView({ block: "center", inline: "nearest" });
      for(let a = el; a; a = a.parentElement) a.scrollLeft = 0;      // on défile vers le bas, jamais sur le côté (même si le body cache le débordement) :
      window.scrollTo(0, window.scrollY);                            // un bouton poussé hors de l'écran à droite reste hors de l'écran
      const r = el.getBoundingClientRect();
      const x = Math.min(vw - 1, Math.max(0, r.left + r.width / 2)), y = Math.min(vh - 1, Math.max(0, r.top + r.height / 2));
      const hit = document.elementFromPoint(x, y);
      return { nom: nom(el), horsEcran: r.left < -1 || r.right > vw + 1, gauche: Math.round(r.left), droite: Math.round(r.right), recouvert: !(hit && (el === hit || el.contains(hit))), par: hit && !el.contains(hit) ? nom(hit) : "" };
    };
    config.essentiels.forEach(groupe => {
      const trouves = [...new Set(groupe.flatMap(sel => [...document.querySelectorAll(sel)]))].filter(visible);
      if(!trouves.length){ resultat.essentiels.push({ groupe: groupe.join(" | "), absent: true }); return; }
      (config.tous ? trouves : trouves.slice(0, 1)).forEach(el => resultat.essentiels.push(Object.assign({ groupe: groupe.join(" | ") }, verifier(el))));
    });
    window.scrollTo(0, 0);
    /* éléments qui dépassent du bord de l'écran (hors zones qui défilent volontairement) */
    const dedans = el => { for(let p = el.parentElement; p; p = p.parentElement){ const o = getComputedStyle(p).overflowX; if((o === "auto" || o === "scroll") && p.scrollWidth > p.clientWidth) return true; } return false; };
    /* coupé par un conteneur qui rogne (décor d'une scène, lien d'évitement hors champ) : rien ne déborde réellement */
    const rogne = el => { for(let p = el.parentElement; p && p !== document.body; p = p.parentElement){ const cs = getComputedStyle(p); if(cs.overflowX === "hidden" || cs.overflowX === "clip"){ const r = p.getBoundingClientRect(); if(r.left >= -2 && r.right <= vw + 2) return true; } } return false; };
    const vus = new Set();
    document.querySelectorAll("body *").forEach(el => {
      if(resultat.depassements.length >= 5 || !visible(el) || dedans(el) || rogne(el) || el.classList.contains("evitement")) return;
      const cs = getComputedStyle(el);
      if(cs.position === "fixed" || cs.position === "sticky") return;
      if(["svg", "path", "g", "circle", "rect", "line", "ellipse", "polygon", "text", "tspan", "use", "defs", "image", "video", "source", "script", "style"].includes(el.tagName.toLowerCase())) return;
      if(el.closest("svg, #fiche-mission, .impression, .zone-impression, [hidden]")) return;
      const r = el.getBoundingClientRect();
      if((r.right > vw + 2 || r.left < -2) && r.width < vw * 3){
        const parent = el.parentElement && [...vus].some(v => v.contains(el));
        if(!parent){ vus.add(el); resultat.depassements.push({ nom: nom(el), gauche: Math.round(r.left), droite: Math.round(r.right) }); }
      }
    });
    return resultat;
  };
}

async function controlerEcran(page, base, jeu, ecran, format){
  const cfg = ecransDe(jeu)[ecran];
  const url = `${base}/${jeu}/index.html${cfg.query}`;
  const erreurs = [];
  const ecoute = e => erreurs.push(e.message);
  page.on("pageerror", ecoute);
  await page.goto(url, { waitUntil: "load", timeout: 20000 });
  try{ await page.waitForSelector(cfg.attend, { visible: true, timeout: 6000 }); }catch(e){ /* l'absence est signalée par les essentiels */ }
  if(cfg.avant){ try{ await page.evaluate(cfg.avant); await new Promise(r => setTimeout(r, 300)); }catch(e){} }
  if(cfg.attendApres){ try{ await page.waitForSelector(cfg.attendApres, { visible: true, timeout: 6000 }); }catch(e){} }
  await new Promise(r => setTimeout(r, 150));
  await page.evaluate(() => { document.querySelectorAll(".toast, .rideau-salle, .rideau-duel, #cine, .cinematique, .ecran-cine").forEach(x => x.remove()); });
  const m = await page.evaluate(mesurer(ecran, format), { essentiels: cfg.essentiels, tous: !!cfg.tous });
  page.off("pageerror", ecoute);
  return { m, erreurs };
}

/* ---------------- Programme principal ---------------- */
async function lancer(args){
  const rapide = args.includes("--rapide");
  const opt = n => { const a = args.find(x => x.startsWith("--" + n + "=")); return a ? a.split("=")[1] : null; };
  const captures = opt("captures") || (rapide ? "defauts" : "toutes");
  const fmts = (opt("largeurs") || Object.keys(FORMATS).join(",")).split(",").filter(f => FORMATS[f]);
  const choix = args.filter(a => !a.startsWith("--"));
  const jeux = choix.length ? choix : JEUX_SALLES.concat(IMMERSIFS);
  const ecransPour = jeu => { const tous = Object.keys(ecransDe(jeu)); return rapide ? tous.filter(e => e === "accueil" || e === "enigme") : tous; };

  let puppeteer = null;
  try{ puppeteer = require("puppeteer-core"); }catch(e){}
  const navigateur = trouverNavigateur();
  if(!puppeteer || !navigateur){
    console.log(`⚠ Contrôle de l'affichage (N17) sauté : ${!puppeteer ? "puppeteer-core absent (faire « npm install » dans outils-tests)" : "aucun navigateur Chrome ou Edge trouvé (variable CHROME_PATH)"}.`);
    return 0;
  }
  const { s, port } = await serveur();
  const base = `http://127.0.0.1:${port}`;
  const dossierCaptures = path.join(__dirname, "captures-responsive");
  if(captures !== "aucune") fs.mkdirSync(dossierCaptures, { recursive: true });
  const browser = await puppeteer.launch({ executablePath: navigateur, headless: true, args: ["--no-sandbox", "--hide-scrollbars", "--autoplay-policy=no-user-gesture-required", "--mute-audio"] });
  const R = { erreurs: [], alertes: [], ok: 0, total: 0, captures: 0 };
  const t0 = Date.now();
  try{
    const sorties = {};
    const controlerJeu = async jeu => {
      if(!fs.existsSync(path.join(RACINE, jeu, "index.html"))){ sorties[jeu] = `⚠ ${jeu} : pas de index.html`; return; }
      const lignes = [];
      for(const f of fmts){
        const F = FORMATS[f];
        const page = await browser.newPage();
        await page.setViewport({ width: F.width, height: F.height, deviceScaleFactor: 1, isMobile: F.mobile, hasTouch: F.mobile });
        for(const e of ecransPour(jeu)){
          R.total++;
          let res;
          try{ res = await controlerEcran(page, base, jeu, e, F); }
          catch(err){ R.erreurs.push({ jeu, f: F.nom, e, msg: "ouverture impossible : " + err.message }); lignes.push("✗"); continue; }
          const m = res.m, defauts = [], notes = [];
          m.essentiels.forEach(x => {
            if(x.absent){ if(!(e === "fin" || (e === "coffre" && /pause/.test(x.groupe)))) notes.push(`bouton introuvable : ${x.groupe}`); return; }
            if(x.horsEcran) defauts.push(`« ${x.nom} » sort de l'écran (${x.gauche} → ${x.droite} px sur ${m.vw})`);
            else if(x.recouvert) defauts.push(`« ${x.nom} » est recouvert par ${x.par || "un autre élément"}`);
          });
          if(m.essentiels.every(x => x.absent) && ["accueil", "enigme", "coffre"].includes(e)) defauts.push(`écran « ${e} » introuvable (aucun bouton essentiel affiché)`);
          if(m.defileX > 2) notes.push(`la page défile horizontalement (${m.defileX} px de trop)`);
          m.depassements.forEach(d => notes.push(`dépasse du bord : ${d.nom} (${d.gauche} → ${d.droite} px)`));
          defauts.forEach(d => R.erreurs.push({ jeu, f: F.nom, e, msg: d }));
          notes.forEach(n => R.alertes.push({ jeu, f: F.nom, e, msg: n }));
          if(!defauts.length) R.ok++;
          if(captures === "toutes" || (captures === "defauts" && (defauts.length || notes.length))){
            try{ await page.screenshot({ path: path.join(dossierCaptures, `${jeu.replace(/\//g, "-")}-${f}-${e}.png`) }); R.captures++; }catch(err){}
          }
          lignes.push(defauts.length ? "✗" : notes.length ? "⚠" : "✓");
        }
        await page.close();
      }
      sorties[jeu] = `${lignes.includes("✗") ? "✗" : lignes.includes("⚠") ? "⚠" : "✓"} ${jeu.padEnd(18)} ${lignes.join("")}  (${fmts.map(f => FORMATS[f].nom).join(" · ")} × ${ecransPour(jeu).join(", ")})`;
    };
    const file = jeux.slice();
    await Promise.all(Array.from({ length: Math.min(4, file.length) }, async () => { while(file.length) await controlerJeu(file.shift()); }));
    jeux.forEach(j => console.log(sorties[j]));
  } finally {
    await browser.close(); s.close();
  }
  console.log(`\nAffichage tablette et smartphone : ${R.total} écrans contrôlés en ${Math.round((Date.now() - t0) / 1000)} s, ${R.captures} capture(s) dans outils-tests/captures-responsive/.`);
  const ligne = e => `   ${e.jeu} · ${e.f} · écran « ${e.e} »\n      ${e.msg}`;
  if(R.alertes.length){
    console.log(`\n⚠ ${R.alertes.length} point(s) à regarder (non bloquants) :`);
    R.alertes.slice(0, 30).forEach(e => console.log(ligne(e)));
    if(R.alertes.length > 30) console.log(`   … et ${R.alertes.length - 30} autres`);
  }
  if(R.erreurs.length){
    console.log(`\n✗ ${R.erreurs.length} bouton(s) essentiel(s) inaccessible(s) :`);
    R.erreurs.forEach(e => console.log(ligne(e)));
    return 1;
  }
  console.log("\n✓ Aucun bouton essentiel ne sort de l'écran.");
  return 0;
}

if(require.main === module) lancer(process.argv.slice(2)).then(c => process.exit(c), e => { console.error(e); process.exit(1); });
module.exports = { IMMERSIFS, ECRANS_IMMERSIFS, chargerPuppeteer: () => { try{ return require("puppeteer-core"); }catch(e){ return null; } }, lancer, FORMATS, ECRANS, trouverNavigateur, serveur, controlerEcran, mesurerPage: () => mesurer() };
