#!/usr/bin/env node
/* ============================================================
   CONTRÔLE DES enigmes.json AVANT PUBLICATION (amélioration A7)
   ------------------------------------------------------------
   Sans dépendance (Node seul), en une seconde, avant un `git push` :
     node outils-tests/verifier-enigmes.js            → tous les jeux
     node outils-tests/verifier-enigmes.js melanges   → un seul jeu

   Contrôles (✗ = bloquant, ⚠ = à regarder) :
     • JSON lisible, et aucune CLÉ EN DOUBLE (le navigateur garderait
       silencieusement la dernière : une énigme écrasée sans bruit) ;
     • salles numérotées 1, 2, 3… ; identifiants d'énigmes uniques ;
     • chaque énigme : titre, type connu, consigne (CM1 et CM2 si elle
       est différenciée), indices, correction, leçon existante ;
     • les données du type, pour CHAQUE niveau où l'énigme est jouée
       (et pour chaque variante D3) : clés attendues et cohérence
       (bonne réponse dans la liste, rangs 1…n, un seul intrus,
       étiquettes des trous présentes, lettres cachées présentes…) ;
     • CM1 ≤ CM2 : pas plus d'énigmes en CM1 qu'en CM2, par salle ;
     • serrures : un mot-clé par salle, jamais deux fois le même
       (accents et majuscules ignorés, comme au coffre).
   Déclaration et Tour du monde (énigmes écrites dans leur js/) : seules
   les serrures de dialogues.json sont contrôlées.
   Code de sortie 1 s'il y a au moins un ✗ (le crochet pre-push bloque).
   ============================================================ */
const fs = require("fs");
const path = require("path");
const RACINE = path.resolve(__dirname, "..");
const TYPES = ["qcm", "vraifaux", "association", "ordre", "tri", "trous", "lettres", "code", "intrus", "plan", "instrument"];
const NIVEAUX = ["CM1", "CM2"];

/* ---- Détection des clés en double (JSON.parse garde la dernière sans prévenir) ---- */
function clesEnDouble(texte){
  const doublons = []; const pile = []; let i = 0, ligne = 1;
  const lireChaine = () => { let s = ""; i++; while (i < texte.length && texte[i] !== '"') { if (texte[i] === "\\") { s += texte[i] + texte[i + 1]; i += 2; continue; } if (texte[i] === "\n") ligne++; s += texte[i++]; } i++; return s; };
  while (i < texte.length) {
    const c = texte[i];
    if (c === "\n") { ligne++; i++; continue; }
    if (c === "{") { pile.push({ objet: true, cles: new Set(), attendCle: true }); i++; continue; }
    if (c === "[") { pile.push({ objet: false }); i++; continue; }
    if (c === "}" || c === "]") { pile.pop(); i++; continue; }
    if (c === ",") { const h = pile[pile.length - 1]; if (h && h.objet) h.attendCle = true; i++; continue; }
    if (c === '"') {
      const l = ligne, s = lireChaine(), h = pile[pile.length - 1];
      if (h && h.objet && h.attendCle) {
        if (h.cles.has(s)) doublons.push(`« ${s} » (ligne ${l})`);
        h.cles.add(s); h.attendCle = false;
      }
      continue;
    }
    i++;
  }
  return doublons;
}

const norm = s => String(s == null ? "" : s).normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/\s+/g, " ").trim().toUpperCase();
const vide = v => v == null || (typeof v === "string" && !v.trim()) || (Array.isArray(v) && !v.length);
const txt = h => String(h || "").replace(/<[^>]*>/g, "");

function lireJSON(fichier, R){
  const brut = fs.readFileSync(fichier, "utf8").replace(/^﻿/, "");
  let d;
  try { d = JSON.parse(brut); } catch (e) { R.err(`${path.relative(RACINE, fichier)} : JSON illisible — ${e.message}`); return null; }
  const dbl = clesEnDouble(brut);
  if (dbl.length) R.err(`${path.relative(RACINE, fichier)} : clé(s) en double, la première valeur est perdue : ${dbl.slice(0, 6).join(", ")}${dbl.length > 6 ? "…" : ""}`);
  return d;
}

/* ---- Données d'un type, pour un niveau ---- */
function controlerDonnees(type, d, ou, R){
  if (!d || typeof d !== "object") { R.err(`${ou} : aucune donnée (ni cm1/cm2 ni commun)`); return 0; }
  const liste = (cle, min) => {
    const l = d[cle];
    if (!Array.isArray(l)) { R.err(`${ou} : « ${cle} » manquant (liste attendue)`); return []; }
    if (l.length < (min || 1)) R.err(`${ou} : « ${cle} » doit contenir au moins ${min || 1} élément(s)`);
    return l;
  };
  switch (type) {
    case "qcm": { const q = liste("questions");
      q.forEach((x, k) => {
        if (vide(x.q)) R.err(`${ou} : question ${k + 1} sans énoncé (q)`);
        if (!Array.isArray(x.options) || x.options.length < 2) R.err(`${ou} : question ${k + 1} : au moins 2 options`);
        else if (!Number.isInteger(x.bonne) || x.bonne < 0 || x.bonne >= x.options.length) R.err(`${ou} : question ${k + 1} : « bonne » (${x.bonne}) hors des options`);
        else if (new Set(x.options.map(norm)).size !== x.options.length) R.err(`${ou} : question ${k + 1} : deux options identiques`);
      }); return q.length; }
    case "vraifaux": { const a = liste("affirmations");
      a.forEach((x, k) => { if (vide(x.txt)) R.err(`${ou} : affirmation ${k + 1} vide`); if (typeof x.vrai !== "boolean") R.err(`${ou} : affirmation ${k + 1} : « vrai » doit valoir true ou false`); });
      return a.length; }
    case "association": { const p = liste("paires", 2);
      p.forEach((x, k) => { if (vide(x.g) || vide(x.d)) R.err(`${ou} : paire ${k + 1} incomplète (g / d)`); });
      if (new Set(p.map(x => norm(x.g))).size !== p.length) R.err(`${ou} : deux éléments de gauche identiques`);
      if (new Set(p.map(x => norm(x.d))).size !== p.length) R.err(`${ou} : deux éléments de droite identiques (réponse ambiguë)`);
      return p.length; }
    case "ordre": { const it = liste("items", 2);
      const rangs = it.map(x => x.rang).sort((a, b) => a - b);
      if (it.some(x => vide(x.txt))) R.err(`${ou} : un élément sans texte`);
      if (rangs.some((r, k) => r !== k + 1)) R.err(`${ou} : les rangs doivent être 1, 2, … ${it.length} sans trou ni doublon (trouvé : ${rangs.join(", ")})`);
      return it.length; }
    case "tri": { const col = liste("colonnes", 2), ca = liste("cartes", 2);
      const ids = new Set(col.map(c => c.id));
      if (col.some(c => vide(c.id) || vide(c.titre))) R.err(`${ou} : colonne sans id ou sans titre`);
      ca.forEach((x, k) => { if (!ids.has(x.col)) R.err(`${ou} : carte ${k + 1} (« ${txt(x.txt).slice(0, 30)} ») : colonne « ${x.col} » inconnue`); });
      return ca.length; }
    case "trous": {
      if (vide(d.texte)) { R.err(`${ou} : « texte » manquant`); return 0; }
      const rep = [...String(d.texte).matchAll(/\[\[([^\]]+)\]\]/g)].map(m => m[1]);
      if (!rep.length) R.err(`${ou} : aucun trou [[…]] dans le texte`);
      const et = liste("etiquettes").map(norm);
      rep.forEach(r => { if (!et.includes(norm(r))) R.err(`${ou} : la réponse « ${r} » n'est pas dans les étiquettes`); });
      return rep.length; }
    case "lettres": {
      const cible = Array.isArray(d.cible) ? d.cible : String(d.cible || "").split("");
      if (!cible.length) { R.err(`${ou} : « cible » manquante`); return 0; }
      const cachees = [...String(d.texte || "").matchAll(/data-l=['"]([^'"]+)['"]/g)].map(m => norm(m[1]));
      const reste = cachees.slice();
      cible.forEach(l => { const k = reste.indexOf(norm(l)); if (k < 0) R.err(`${ou} : la lettre « ${l} » du mot n'est pas cachée dans le texte (data-l)`); else reste.splice(k, 1); });
      return cible.length; }
    case "code": { const ch = liste("champs");
      ch.forEach((x, k) => { if (vide(x.valeur) && !(Array.isArray(x.valeurs) && x.valeurs.length)) R.err(`${ou} : champ ${k + 1} sans « valeur » attendue`); if (vide(x.libelle)) R.warn(`${ou} : champ ${k + 1} sans libellé`); });
      return ch.length; }
    case "intrus": { const ca = liste("cartes", 3);
      const n = ca.filter(x => x.intrus === true).length;
      if (n !== 1) R.err(`${ou} : il faut exactement un intrus (trouvé : ${n})`);
      return ca.length; }
    case "plan": { const cases = liste("cases");
      cases.forEach((x, k) => { if (vide(x.reponse)) R.err(`${ou} : case ${k + 1} sans « reponse »`); });
      if (Array.isArray(d.etiquettes)) { const et = d.etiquettes.map(norm);
        cases.forEach((x, k) => { if (!vide(x.reponse) && !et.includes(norm(x.reponse))) R.err(`${ou} : case ${k + 1} : réponse « ${x.reponse} » absente des étiquettes`); }); }
      return cases.length; }
    case "instrument": {
      if (vide(d.instrument)) R.err(`${ou} : « instrument » manquant`);
      if (!(typeof d.min === "number" && typeof d.max === "number" && d.min < d.max)) R.err(`${ou} : min / max incohérents`);
      const it = liste("items");
      it.forEach((x, k) => { if (typeof x.valeur !== "number" || x.valeur < d.min || x.valeur > d.max) R.err(`${ou} : relevé ${k + 1} : valeur hors de l'échelle`); });
      return it.length; }
  }
  return 0;
}

function niveauxDe(e){ return Array.isArray(e.niveaux) && e.niveaux.length ? e.niveaux : NIVEAUX; }
function donneesNiveau(e, niv){ const n = niv.toLowerCase(); return e[n] || e.commun || e.cm2 || e.cm1; }

function controlerEnigme(e, ou, R, lecons){
  if (vide(e.titre)) R.err(`${ou} : titre manquant`);
  if (!TYPES.includes(e.type)) { R.err(`${ou} : type « ${e.type} » inconnu (types : ${TYPES.join(", ")})`); return {}; }
  const nivs = niveauxDe(e);
  if (nivs.some(n => !NIVEAUX.includes(n))) R.err(`${ou} : niveaux ${JSON.stringify(e.niveaux)} (attendu : "CM1", "CM2")`);
  const c = e.consigne;
  if (vide(c) || (typeof c === "object" && nivs.some(n => vide(c[n.toLowerCase()] || c.commun)))) R.err(`${ou} : consigne manquante pour ${nivs.join("/")}`);
  for (const n of nivs) {   // indices : une liste, ou {cm1, cm2, commun} (comme le moteur)
    const src = e.indices || {};
    const l = Array.isArray(src) ? src : (src[n.toLowerCase()] || src.commun || src.cm2 || src.cm1 || []);
    if (!l.length || l.some(vide)) R.err(`${ou} [${n}] : indices manquants ou vides`);
    else if (l.length < 3) R.warn(`${ou} [${n}] : ${l.length} indice(s) seulement (3 prévus)`);
  }
  if (vide(e.correction) || (typeof e.correction === "object" && !Object.values(e.correction).some(v => !vide(v)))) R.err(`${ou} : correction manquante (corrigé enseignant)`);
  if (vide(e.lecon)) R.warn(`${ou} : aucune leçon associée`);
  else if (lecons && !lecons.has(e.lecon)) R.err(`${ou} : leçon « ${e.lecon} » introuvable dans lecons.json`);
  const tailles = {};
  for (const n of nivs) tailles[n] = controlerDonnees(e.type, donneesNiveau(e, n), `${ou} [${n}]`, R);
  if (nivs.length === 2 && e.cm1 && e.cm2 && tailles.CM1 > tailles.CM2)
    R.warn(`${ou} : plus d'éléments en CM1 (${tailles.CM1}) qu'en CM2 (${tailles.CM2})`);
  (e.variantes || []).forEach((v, k) => {
    const ev = Object.assign({}, e, v); delete ev.variantes;
    for (const n of nivs) controlerDonnees(e.type, donneesNiveau(ev, n), `${ou} variante ${k + 1} [${n}]`, R);
  });
  return tailles;
}

function controlerSerrures(salles, cle, ou, R){
  const vus = new Map();
  salles.forEach(s => {
    const m = s[cle];
    if (vide(m)) return;
    const k = norm(m);
    if (vus.has(k)) R.err(`${ou} : mot de serrure « ${m} » en double (salles ${vus.get(k)} et ${s.num})`);
    else vus.set(k, s.num);
  });
  return vus.size;
}

function controlerJeu(jeu){
  const R = { erreurs: [], alertes: [], err(m){ this.erreurs.push(m); }, warn(m){ this.alertes.push(m); } };
  const dos = path.join(path.isAbsolute(jeu) ? jeu : path.join(RACINE, jeu), "assets", "data");
  const fE = path.join(dos, "enigmes.json"), fD = path.join(dos, "dialogues.json"), fL = path.join(dos, "lecons.json");
  const enig = fs.existsSync(fE) ? lireJSON(fE, R) : null;
  const dial = fs.existsSync(fD) ? lireJSON(fD, R) : null;
  const lec = fs.existsSync(fL) ? lireJSON(fL, R) : null;
  let lecons = null;
  if (lec) { const l = lec.lecons || lec; lecons = new Set(Array.isArray(l) ? l.map(x => x.id) : Object.keys(l)); }
  const bilan = { CM1: 0, CM2: 0, serrures: 0 };
  if (enig) {
    const salles = enig.salles || [];
    if (!salles.length) R.err("enigmes.json : aucune salle");
    const ids = new Set();
    salles.forEach((s, k) => {
      if (s.num !== k + 1) R.err(`enigmes.json : salle n° ${s.num} à la position ${k + 1} (attendu ${k + 1})`);
      const parNiv = { CM1: 0, CM2: 0 };
      (s.enigmes || []).forEach(e => {
        const ou = `salle ${s.num}, énigme ${e.id || "?"}`;
        if (vide(e.id)) R.err(`${ou} : identifiant manquant`);
        else if (ids.has(e.id)) R.err(`${ou} : identifiant « ${e.id} » en double`);
        ids.add(e.id);
        controlerEnigme(e, ou, R, lecons);
        niveauxDe(e).forEach(n => { if (parNiv[n] != null) parNiv[n]++; });
      });
      if (!parNiv.CM1 || !parNiv.CM2) R.err(`salle ${s.num} : aucune énigme en ${!parNiv.CM1 ? "CM1" : "CM2"}`);
      if (parNiv.CM1 > parNiv.CM2) R.err(`salle ${s.num} : plus d'énigmes en CM1 (${parNiv.CM1}) qu'en CM2 (${parNiv.CM2})`);
      bilan.CM1 += parNiv.CM1; bilan.CM2 += parNiv.CM2;
    });
    if (enig.final) controlerEnigme(enig.final, "énigme finale", R, null);
    if (dial && Array.isArray(dial.salles)) {
      if (dial.salles.length !== salles.length) R.err(`dialogues.json : ${dial.salles.length} salles, enigmes.json : ${salles.length}`);
      dial.salles.forEach(s => { if (vide(s.motCle)) R.err(`dialogues.json, salle ${s.num} : mot de serrure (motCle) manquant`); });
      bilan.serrures = controlerSerrures(dial.salles, "motCle", "dialogues.json", R);
    }
  } else if (dial && Array.isArray(dial.salles)) {
    // Déclaration, Tour du monde : énigmes dans js/, fragments du coffre dans dialogues.json
    bilan.serrures = controlerSerrures(dial.salles, dial.salles.some(s => s.motCle) ? "motCle" : "fragment", "dialogues.json", R);
  }
  return { jeu, R, bilan, enigmes: !!enig };
}

function jeuxDuDepot(){
  return fs.readdirSync(RACINE, { withFileTypes: true })
    .filter(d => d.isDirectory() && fs.existsSync(path.join(RACINE, d.name, "index.html")) && fs.existsSync(path.join(RACINE, d.name, "assets", "data", "dialogues.json")))
    .map(d => d.name)
    .filter(j => { // format « salles » seulement (vingt-mille-lieues et immersifs/ ont leur propre format)
      const f = path.join(RACINE, j, "assets", "data", "enigmes.json");
      if (!fs.existsSync(f)) return true;
      try { return Array.isArray(JSON.parse(fs.readFileSync(f, "utf8")).salles); } catch (e) { return true; }
    }).sort();
}

function lancer(choix){
  const jeux = choix.length ? choix : jeuxDuDepot();
  let nErr = 0, nWarn = 0;
  console.log("Contrôle des énigmes avant publication (A7)\n");
  for (const j of jeux) {
    if (!fs.existsSync(path.join(RACINE, j))) { console.log(`✗ ${j} : dossier introuvable`); nErr++; continue; }
    const { R, bilan, enigmes } = controlerJeu(j);
    const etat = R.erreurs.length ? "✗" : (R.alertes.length ? "⚠" : "✓");
    const resume = enigmes ? `${bilan.CM1} énigmes CM1 · ${bilan.CM2} CM2 · ${bilan.serrures} serrures` : `${bilan.serrures} serrures (énigmes dans js/)`;
    console.log(`${etat} ${j.padEnd(20)} ${resume}`);
    R.erreurs.forEach(m => console.log("    ✗ " + m));
    R.alertes.forEach(m => console.log("    ⚠ " + m));
    nErr += R.erreurs.length; nWarn += R.alertes.length;
  }
  console.log(`\n${jeux.length} jeu(x) : ${nErr} erreur(s) bloquante(s), ${nWarn} alerte(s).`);
  return nErr;
}

module.exports = { controlerJeu, controlerDonnees, clesEnDouble, jeuxDuDepot, lancer };
if (require.main === module) process.exitCode = lancer(process.argv.slice(2)) ? 1 : 0;
