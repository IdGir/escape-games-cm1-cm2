#!/usr/bin/env node
/* ============================================================
   CONTRÔLE DES LIENS INTERNES (amélioration N10)
   ------------------------------------------------------------
   Sans dépendance (Node seul), en une seconde, avant un `git push` :
     node outils-tests/verifier-liens-internes.js            → tout le dépôt
     node outils-tests/verifier-liens-internes.js melanges   → un seul jeu (+ pages communes)

   Pages parcourues : l'accueil et toutes les pages communes de la racine
   (annee, passeport, trophées, FAQ, adopter…), puis, dans chaque jeu,
   index.html, prof.html, lecons-imprimables.html et les autres pages .html.

   Contrôles (✗ = bloquant, ⚠ = à regarder) :
     • chaque lien <a href>, <link href>, <script src>, <iframe src> relatif
       mène à un fichier existant (un dossier doit contenir index.html) ;
     • les liens d'un document média (affiche, bande-annonce, .vtt) sont
       signalés ⚠ seulement : ils peuvent attendre le dépôt du fichier ;
     • une ancre #id vers une autre page ou la même page : ⚠ si l'id n'y est pas ;
     • les liens FABRIQUÉS PAR LE CODE, que le HTML ne contient pas :
         – « Et ensuite ? » (C4, jeu-suivant.js) : chaque dossier du catalogue,
           chaque « suite » / « precedent » mène à un jeu publié, et l'id de
           js/jeu.js de chaque jeu est celui du catalogue (sinon l'encart
           n'apparaît jamais) ;
         – la vitrine des trophées (trophees.js) : trophees.html existe ;
         – les pages que les modules communs ouvrent depuis un jeu
           (resultats.html, passeport.html, classement.html, verifier.html…).
   Les liens externes (https://…) relèvent du contrôle F3, pas de celui-ci.
   Code de sortie 1 s'il y a au moins un ✗ (le crochet pre-push bloque).
   ============================================================ */
const fs = require("fs");
const path = require("path");
const RACINE = path.resolve(__dirname, "..");
const IGNORES = new Set(["node_modules", ".git", "archives-hors-ligne", "_a-supprimer", "Claude outputs", "Michel strogoff", "Constitution 1958", "outils-lecons", "outils-docs", "__pycache__", "references", "sources", "captures", "scenarimages"]);
const MEDIAS = /\.(jpe?g|png|gif|webp|svg|mp4|webm|vtt|mp3|ogg|wav|woff2?|pdf|zip|json)$/i;
const filtre = process.argv[2] || "";

const R = { erreurs: [], alertes: [], pages: 0, liens: 0 };
const rel = f => path.relative(RACINE, f).replace(/\\/g, "/");
const err = (page, lien, msg) => R.erreurs.push({ page, lien, msg });
const alerte = (page, lien, msg) => R.alertes.push({ page, lien, msg });
const lire = f => { try { return fs.readFileSync(f, "utf8"); } catch (e) { return null; } };
const existe = f => { try { return fs.statSync(f); } catch (e) { return null; } };

/* ---- Pages à parcourir ---- */
function pagesHtml(dossier, profondeur){
  const out = [];
  let noms = []; try { noms = fs.readdirSync(dossier, { withFileTypes: true }); } catch (e) { return out; }
  for (const n of noms) {
    if (IGNORES.has(n.name)) continue;
    const p = path.join(dossier, n.name);
    if (n.isDirectory()) { if (profondeur < 3 && n.name !== "assets" && n.name !== "css" && n.name !== "js" && n.name !== "tests") out.push(...pagesHtml(p, profondeur + 1)); }
    else if (/\.html$/i.test(n.name)) out.push(p);
  }
  return out;
}
function pagesDuDepot(){
  const racine = fs.readdirSync(RACINE, { withFileTypes: true });
  const out = [];
  for (const n of racine) {
    if (n.isFile() && /\.html$/i.test(n.name)) out.push(path.join(RACINE, n.name));
  }
  for (const n of racine) {
    if (!n.isDirectory() || IGNORES.has(n.name) || n.name === "commun") continue;
    if (filtre && n.name !== filtre) continue;
    out.push(...pagesHtml(path.join(RACINE, n.name), 1));
  }
  return out;
}

/* ---- Extraction des liens d'une page ---- */
function liensDe(html){
  const sansCommentaires = html.replace(/<!--[\s\S]*?-->/g, "");
  const out = []; let m;
  const re = /<(a|link|script|iframe)\b[^>]*?\b(href|src)\s*=\s*("([^"]*)"|'([^']*)')/gi;
  while ((m = re.exec(sansCommentaires))) {
    const url = (m[4] !== undefined ? m[4] : m[5]).trim();
    out.push({ balise: m[1].toLowerCase(), url });
  }
  return out;
}
const ids = new Map();
function idsDe(fichier){
  if (ids.has(fichier)) return ids.get(fichier);
  const t = lire(fichier) || "";
  const s = new Set(); let m; const re = /\b(?:id|name)\s*=\s*["']([^"']+)["']/g;
  while ((m = re.exec(t))) s.add(m[1]);
  ids.set(fichier, s); return s;
}

function verifierLien(page, balise, url){
  if (!url || /^(https?:|mailto:|tel:|data:|javascript:|blob:|about:|\/\/)/i.test(url) || /[()\[\]^*|]/.test(url)) return;
  if (/\$\{|\{\{|<%|'\s*\+|\+\s*'/.test(url)) return;           // lien construit par le code : voir plus bas
  R.liens++;
  const [sansAncre, ancre] = url.split("#");
  const sansRequete = sansAncre.split("?")[0];
  const dir = path.dirname(page);
  if (!sansRequete) {                                            // ancre sur la même page
    if (ancre && !idsDe(page).has(ancre) && !/^(top|haut)$/i.test(ancre)) alerte(rel(page), url, "ancre absente de la page");
    return;
  }
  let cible = path.resolve(dir, decodeURIComponent(sansRequete));
  if (!cible.startsWith(RACINE)) { err(rel(page), url, "sort du dépôt"); return; }
  const st = existe(cible);
  if (!st) {
    (MEDIAS.test(sansRequete) ? alerte : err)(rel(page), url, "cible manquante : " + rel(cible));
    return;
  }
  if (st.isDirectory()) {
    const index = path.join(cible, "index.html");
    if (!existe(index)) { err(rel(page), url, "dossier sans index.html : " + rel(cible)); return; }
    cible = index;
  }
  if (ancre && /\.html$/i.test(cible) && !idsDe(cible).has(ancre)) alerte(rel(page), url, `ancre « #${ancre} » absente de ${rel(cible)}`);
}

/* ---- Liens fabriqués par le code ---- */
function chargerCatalogue(){
  const t = lire(path.join(RACINE, "commun/donnees/catalogue.js"));
  if (!t) { err("commun/donnees/catalogue.js", "—", "fichier introuvable"); return null; }
  try { return new Function(t + "; return CATALOGUE;")(); } catch (e) { err("commun/donnees/catalogue.js", "—", "illisible : " + e.message); return null; }
}
function liensFabriques(){
  const cat = chargerCatalogue();
  const jeuxHtml = fs.readdirSync(RACINE, { withFileTypes: true }).filter(n => n.isDirectory() && existe(path.join(RACINE, n.name, "js/jeu.js"))).map(n => n.name);
  if (cat) {
    const parId = id => cat.jeux.find(j => j.id === id || j.dossier === id);
    for (const j of cat.jeux) {
      const nom = `catalogue : ${j.id}`;
      if (j.dossier) {
        if (filtre && j.dossier !== filtre) continue;
        R.liens++;
        /* jeu immersif seul (« classique »: false) : la page à vérifier est celle de la variante immersive */
        const cibleIndex = j.classique === false && j.immersif ? j.immersif.replace(/^\.?\/?/, "").replace(/\/$/, "") : j.dossier;
        if (!existe(path.join(RACINE, cibleIndex, "index.html"))) err("commun/donnees/catalogue.js", `../${cibleIndex}/`, `${nom} : dossier publié sans index.html`);
      }
      for (const champ of ["precedent", "suite"]) {
        if (!j[champ]) continue;
        R.liens++;
        const autre = parId(j[champ]);
        if (!autre) err("commun/donnees/catalogue.js", j[champ], `${nom} : « ${champ} » inconnu dans le catalogue`);
        else if (!autre.dossier) alerte("commun/donnees/catalogue.js", j[champ], `${nom} : « ${champ} » pas encore publié (lien non affiché)`);
        else if (!existe(path.join(RACINE, autre.classique === false && autre.immersif ? autre.immersif.replace(/^\.?\/?/, "").replace(/\/$/, "") : autre.dossier, "index.html"))) err("commun/donnees/catalogue.js", `../${autre.dossier}/`, `${nom} : « ${champ} » sans index.html`);
      }
    }
    /* chaque jeu à moteur commun doit être reconnu par jeu-suivant.js (JEU.id = dossier ou id du catalogue) */
    for (const d of jeuxHtml) {
      if (filtre && d !== filtre) continue;
      const jeuJs = lire(path.join(RACINE, d, "js/jeu.js")) || "";
      const m = jeuJs.match(/\bid\s*:\s*["']([^"']+)["']/);
      const idJeu = m ? m[1] : null;
      R.liens++;
      if (!idJeu) { alerte(`${d}/js/jeu.js`, "JEU.id", "identifiant introuvable"); continue; }
      if (!cat.jeux.find(j => j.dossier === idJeu || j.id === idJeu)) err(`${d}/js/jeu.js`, "JEU.id = " + idJeu, "absent du catalogue : l'encart « Et ensuite ? » (C4) et le passeport (C3) ne le reconnaîtront pas");
      if (idJeu !== d) alerte(`${d}/js/jeu.js`, "JEU.id = " + idJeu, `l'identifiant diffère du dossier « ${d} »`);
    }
  }
  /* pages que les modules communs ouvrent depuis un jeu */
  const cibles = [
    ["commun/js/trophees.js", "../trophees.html"],
    ["commun/js/jeu-suivant.js", "../"],
    ["commun/js/compte-rendu.js", "../resultats.html"],
    ["commun/js/mode-solo.js", "../index.html"]
  ];
  for (const [source, cible] of cibles) {
    const t = lire(path.join(RACINE, source));
    if (t === null) continue;
    const nom = cible.replace(/^\.\.\//, "").replace(/\?.*/, "");
    if (!t.includes(nom) && nom !== "" && cible !== "../") continue;     // le module ne cite pas ce lien : rien à contrôler
    R.liens++;
    const f = nom ? path.join(RACINE, nom) : path.join(RACINE, "index.html");
    if (!existe(f)) err(source, cible, "cible manquante : " + rel(f));
  }
  /* pages communes de la racine toujours attendues par les jeux */
  for (const p of ["index.html", "trophees.html", "passeport.html", "resultats.html", "classement.html", "annee.html", "faq.html", "adopter.html", "enseignant.html", "verifier.html"]) {
    R.liens++;
    if (!existe(path.join(RACINE, p))) err("racine", p, "page commune attendue absente");
  }
}

/* ---- Lancement ---- */
for (const page of pagesDuDepot()) {
  const html = lire(page); if (html === null) continue;
  R.pages++;
  for (const l of liensDe(html)) verifierLien(page, l.balise, l.url);
}
liensFabriques();

const ligne = e => `   ${e.page}\n      lien  : ${e.lien}\n      motif : ${e.msg}`;
console.log(`\nLiens internes${filtre ? " (" + filtre + ")" : ""} : ${R.pages} pages, ${R.liens} liens contrôlés.`);
if (R.alertes.length) {
  console.log(`\n⚠ ${R.alertes.length} alerte${R.alertes.length > 1 ? "s" : ""} (à regarder, non bloquant) :`);
  R.alertes.slice(0, 40).forEach(e => console.log(ligne(e)));
  if (R.alertes.length > 40) console.log(`   … et ${R.alertes.length - 40} autres`);
}
if (R.erreurs.length) {
  console.log(`\n✗ ${R.erreurs.length} lien${R.erreurs.length > 1 ? "s" : ""} cassé${R.erreurs.length > 1 ? "s" : ""} :`);
  R.erreurs.forEach(e => console.log(ligne(e)));
  process.exit(1);
}
console.log("\n✓ Tous les liens internes mènent à un fichier existant.");
