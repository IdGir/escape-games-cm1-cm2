/* Tests jsdom — Le Laboratoire de Madame Mélange
   Usage : node test-melanges.js <racine du dépôt>
   Vérifie : données, partie complète CM1 et CM2 (scores 100 / 125),
   tests négatifs, indices, mode vérification, réglages, impressions,
   leçons, et page verifier.html. */
const fs = require("fs"), path = require("path");
const { JSDOM, VirtualConsole } = require("jsdom");

const RACINE = path.resolve(process.argv[2] || ".");
const JEU = path.join(RACINE, "melanges");
let ECHECS = 0, OK = 0;
const ok = (cond, msg) => { if(cond){ OK++; } else { ECHECS++; console.log("  ÉCHEC : " + msg); } };
const sleep = ms => new Promise(r => setTimeout(r, ms));

/* ---------------- 1. Données ---------------- */
function jsonSansDoublon(fichier){
  const txt = fs.readFileSync(fichier, "utf8");
  // Détection de clés dupliquées : reviver sur le texte brut, objet par objet
  const pile = [];
  const re = /"((?:[^"\\]|\\.)*)"\s*:|[{}\[\]]/g;
  let m, doublons = [];
  // on ignore le contenu des chaînes de valeur : on repère les clés seulement
  const sansChaines = txt.replace(/"(?:[^"\\]|\\.)*"(?!\s*:)/g, '""');
  while((m = re.exec(sansChaines))){
    const t = m[0];
    if(t === "{") pile.push(new Set());
    else if(t === "}") pile.pop();
    else if(t === "[" || t === "]") { if(t === "[") pile.push(null); else pile.pop(); }
    else { const top = pile[pile.length-1]; if(top){ if(top.has(m[1])) doublons.push(m[1]); top.add(m[1]); } }
  }
  return { data: JSON.parse(txt), doublons };
}

function testerDonnees(){
  console.log("1. Données JSON");
  const D = {};
  for(const f of ["enigmes", "dialogues", "lecons", "evaluations"]){
    let r;
    try{ r = jsonSansDoublon(path.join(JEU, "assets/data", f + ".json")); }
    catch(e){ ok(false, f + ".json invalide : " + e.message); continue; }
    ok(r.doublons.length === 0, f + ".json : clés dupliquées " + r.doublons.join(", "));
    D[f] = r.data;
  }
  const E = D.enigmes, L = D.lecons.lecons, DL = D.dialogues, EV = D.evaluations;
  const ids = new Set(L.map(l => l.id)), cites = new Set();
  const types = { CM1: new Set(), CM2: new Set() };
  for(const niv of ["CM1", "CM2"]){
    let total = 0;
    E.salles.forEach(s => {
      const liste = s.enigmes.filter(e => !e.niveaux || e.niveaux.includes(niv));
      total += liste.length;
      ok(liste.length === (niv === "CM1" ? 3 : 4), `salle ${s.num} ${niv} : ${liste.length} énigmes`);
      for(let i = 1; i < liste.length; i++) ok(liste[i].type !== liste[i-1].type, `salle ${s.num} ${niv} : deux « ${liste[i].type} » consécutifs`);
      const manip = liste.some(e => ["ordre", "plan", "tri", "trous", "association"].includes(e.type));
      ok(manip, `salle ${s.num} ${niv} : aucune manipulation`);
      liste.forEach(e => types[niv].add(e.type));
    });
    ok(total === (niv === "CM1" ? 15 : 20), niv + " : total " + total);
  }
  ok(types.CM2.size >= 7 && types.CM1.size >= 7, "moins de 7 types d'énigmes");
  E.salles.forEach(s => s.enigmes.forEach(e => {
    ok(ids.has(e.lecon), `${e.id} : leçon « ${e.lecon} » absente`); cites.add(e.lecon);
    ok(!!e.consigne && !!e.correction && !!e.source, `${e.id} : consigne/correction/source manquante`);
    const ind = e.indices || {};
    (e.niveaux || ["CM1", "CM2"]).forEach(n => {
      const arr = ind[n.toLowerCase()] || ind.commun;
      ok(Array.isArray(arr) && arr.length === 3, `${e.id} ${n} : il faut 3 indices`);
      const bloc = e[n.toLowerCase()] || e.commun;
      ok(!!bloc, `${e.id} ${n} : pas de données`);
    });
    // Cohérence interne de chaque type
    for(const n of ["cm1", "cm2", "commun"]){
      const b = e[n]; if(!b) continue;
      if(e.type === "qcm") b.questions.forEach(q => ok(q.bonne >= 0 && q.bonne < q.options.length, e.id + " bonne hors limites"));
      if(e.type === "ordre"){ const r = b.items.map(i => i.rang).sort((a,b)=>a-b); ok(r.every((v,i)=>v===i+1), e.id + " rangs"); }
      if(e.type === "tri"){ const c = new Set(b.colonnes.map(c => c.id)); b.cartes.forEach(k => ok(c.has(k.col), e.id + " colonne inconnue")); }
      if(e.type === "intrus") ok(b.cartes.filter(c => c.intrus).length === 1, e.id + " : un seul intrus");
      if(e.type === "trous"){ const reps = [...b.texte.matchAll(/\[\[(.+?)\]\]/g)].map(m=>m[1]); reps.forEach(r => ok(b.etiquettes.includes(r), e.id + " étiquette manquante " + r)); }
      if(e.type === "plan"){ b.cases.forEach(c => ok(b.etiquettes.includes(c.reponse), e.id + " étiquette manquante " + c.reponse));
        const norm = s => s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g,"").replace(/[^a-z0-9]/g,"");
        ok(new Set(b.etiquettes.map(norm)).size === b.etiquettes.length, e.id + " : étiquettes ambiguës"); }
      if(e.type === "lettres"){ const dom = new JSDOM(b.texte); const ls = [...dom.window.document.querySelectorAll("[data-l]")].map(x=>x.dataset.l);
        ok(ls.join("") === b.cible.join(""), e.id + " : lettres cachées ≠ cible"); }
    }
  }));
  L.forEach(l => {
    ok(cites.has(l.id), `leçon « ${l.id} » jamais citée`);
    ok(l.contenu && l.contenu.cm1 && l.contenu.cm2 && l.lexique && l.lexique.length && l.source && l.objectifs, `leçon ${l.id} incomplète`);
  });
  // Mots-clés = protocole
  const mots = DL.salles.map(s => s.motCle).sort().join();
  ok(mots === [...DL.protocole].sort().join(), "mots-clés ≠ protocole");
  const s54 = E.salles[4].enigmes.find(e => e.id === "5-4");
  ok(s54.cm1.items.sort((a,b)=>a.rang-b.rang).map(i=>i.txt).join() === DL.protocole.join(), "5-4 ≠ protocole (CM1)");
  ok(s54.cm2.items.sort((a,b)=>a.rang-b.rang).map(i=>i.txt).join() === DL.protocole.join(), "5-4 ≠ protocole (CM2)");
  // Évaluations
  ok(EV.qcm.CM1.length === 10 && EV.qcm.CM2.length === 12, "QCM 10/12");
  ok(EV.quizz_final.CM1.length === 5 && EV.quizz_final.CM2.length === 5, "quizz 5/5");
  ok(EV.fiches_preparatoires.length === 5, "5 fiches préparatoires");
  // Pas d'emoji dans les contenus
  const emoji = /[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}\u{1F000}-\u{1F2FF}]/u;
  const textes = [];
  const collecte = (o, cle) => { if(typeof o === "string"){ if(!["schema"].includes(cle)) textes.push([cle, o]); }
    else if(Array.isArray(o)) o.forEach(x => collecte(x, cle)); else if(o && typeof o === "object") Object.entries(o).forEach(([k,v]) => collecte(v, k)); };
  collecte(E); collecte(L); collecte(DL); collecte(EV);
  const avecEmoji = textes.filter(([k, t]) => emoji.test(t));
  ok(avecEmoji.length === 0, "emoji dans les contenus : " + avecEmoji.slice(0,3).map(x=>x[1].slice(0,50)).join(" | "));
  // Termes du collège sans définition
  const college = textes.filter(([k, t]) => /\b(solvant|soluté|miscible)\b/i.test(t) || /\bsolution\b/i.test(t));
  ok(college.length === 0, "termes du collège : " + college.map(x=>x[1].slice(0,60)).join(" | "));
  return D;
}

/* ---------------- 2. Chargement du jeu dans jsdom ---------------- */
async function chargerJeu(query, reglages){
  const html = fs.readFileSync(path.join(JEU, "index.html"), "utf8");
  const scripts = [...html.matchAll(/<script src="([^"?]+)(?:\?[^"]*)?"><\/script>/g)].map(m => m[1]);
  const inline = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
  const sansScripts = html.replace(/<script[\s\S]*?<\/script>/g, "");
  const erreurs = [];
  const vc = new VirtualConsole();
  vc.on("jsdomError", e => erreurs.push(String(e && (e.stack || e.message) || e)));
  vc.on("error", e => erreurs.push("console.error " + e));
  const dom = new JSDOM(sansScripts, { url: "http://localhost/melanges/" + (query || ""), runScripts: "outside-only", pretendToBeVisual: true, virtualConsole: vc });
  const w = dom.window;
  w.fetch = async (url, opts) => {
    const u = new URL(url, w.location.href);
    let p = decodeURIComponent(u.pathname);
    if(p.startsWith("/api/")) throw new Error("pas de serveur");
    const f = path.join(RACINE, p);
    if(fs.existsSync(f) && fs.statSync(f).isFile()){
      const txt = fs.readFileSync(f, "utf8");
      return { ok: true, status: 200, json: async () => JSON.parse(txt), text: async () => txt, headers: { get: () => null } };
    }
    return { ok: false, status: 404, json: async () => ({}), text: async () => "", headers: { get: () => null } };
  };
  w.confirm = () => false; w.alert = () => {}; w.print = () => { w.__imprime = (w.__imprime||0) + 1; };
  w.scrollTo = () => {}; w.HTMLElement.prototype.scrollIntoView = function(){};
  w.HTMLMediaElement.prototype.play = function(){ return Promise.resolve(); };
  w.HTMLMediaElement.prototype.pause = function(){};
  w.HTMLMediaElement.prototype.load = function(){};
  if(reglages) w.localStorage.setItem("escape_reglages_melanges", JSON.stringify(reglages));
  for(const s of scripts){
    const code = fs.readFileSync(path.join(JEU, s), "utf8");
    try{ w.eval(code + "\n//# sourceURL=" + s); }catch(e){ erreurs.push(s + " : " + e.message); }
  }
  inline.forEach(c => { try{ w.eval(c); }catch(e){ erreurs.push("inline : " + e.message); } });
  w.document.dispatchEvent(new w.Event("DOMContentLoaded"));
  await sleep(300);
  return { dom, w, doc: w.document, erreurs };
}
const REGLAGES_TEST = { cinematiques: false, decorsVideo: false, narrationActive: false, sonsActifs: false };

/* ---------------- 3. Résolution automatique d'une énigme ---------------- */
function resoudre(w, e, niveau){
  const doc = w.document;
  const carte = doc.getElementById("enigme-" + e.id);
  if(!carte) throw new Error("carte absente " + e.id);
  const d = e[niveau.toLowerCase()] || e.commun;
  const clic = el => el.dispatchEvent(new w.MouseEvent("click", { bubbles: true }));
  switch(e.type){
    case "qcm":
      d.questions.forEach((q, i) => clic(carte.querySelector(`.qcm-question[data-i="${i}"] .qcm-option[data-j="${q.bonne}"]`)));
      break;
    case "vraifaux":
      d.affirmations.forEach((a, i) => clic(carte.querySelector(`.vf-ligne[data-i="${i}"] .vf-btn[data-rep="${a.vrai ? "vrai" : "faux"}"]`)));
      break;
    case "association":
      carte.querySelectorAll('[data-col="g"] .carte-match').forEach(g => {
        clic(g); clic(carte.querySelector(`[data-col="d"] .carte-match[data-id="${g.dataset.bon}"]`));
      });
      return;
    case "ordre": {
      const liste = carte.querySelector(".liste-ordre");
      [...liste.querySelectorAll(".item-ordre")].sort((a, b) => a.dataset.rang - b.dataset.rang).forEach(it => liste.appendChild(it));
      break;
    }
    case "tri":
      [...carte.querySelectorAll(".carte-tri")].forEach(c => { clic(c); clic(carte.querySelector(`.tri-colonne[data-col="${c.dataset.col}"] .tri-zone`)); });
      break;
    case "trous":
      carte.querySelectorAll(".trou").forEach(t => {
        const et = [...carte.querySelectorAll(".etiquette:not(.posee)")].find(x => x.dataset.mot === t.dataset.rep);
        clic(et); clic(t);
      });
      break;
    case "plan":
      carte.querySelectorAll(".plan-case").forEach(c => {
        const et = [...carte.querySelectorAll(".etiquette:not(.posee)")].find(x => x.dataset.mot === c.dataset.rep);
        clic(et); clic(c);
      });
      break;
    case "lettres":
      d.cible.forEach(l => clic([...carte.querySelectorAll("[data-l]:not(.utilisee)")].find(x => x.dataset.l === l)));
      return;
    case "code":
      d.champs.forEach((c, i) => { carte.querySelector("#code-" + i).value = c.valeur; });
      break;
    case "intrus":
      clic(carte.querySelector('.carte-intrus[data-intrus="1"]'));
      return;
  }
  clic(carte.querySelector("[data-valider]"));
}

/* Une mauvaise réponse ne doit pas valider */
function mauvaiseReponse(w, e, niveau){
  const carte = w.document.getElementById("enigme-" + e.id);
  const d = e[niveau.toLowerCase()] || e.commun;
  const clic = el => el && el.dispatchEvent(new w.MouseEvent("click", { bubbles: true }));
  switch(e.type){
    case "qcm": d.questions.forEach((q, i) => clic(carte.querySelector(`.qcm-question[data-i="${i}"] .qcm-option[data-j="${(q.bonne+1) % q.options.length}"]`))); break;
    case "vraifaux": d.affirmations.forEach((a, i) => clic(carte.querySelector(`.vf-ligne[data-i="${i}"] .vf-btn[data-rep="${a.vrai ? "faux" : "vrai"}"]`))); break;
    case "code": d.champs.forEach((c, i) => { carte.querySelector("#code-" + i).value = "999"; }); break;
    case "intrus": clic(carte.querySelector('.carte-intrus[data-intrus="0"]')); return;
    case "ordre": { const liste = carte.querySelector(".liste-ordre");
      [...liste.querySelectorAll(".item-ordre")].sort((a, b) => b.dataset.rang - a.dataset.rang).forEach(it => liste.appendChild(it)); break; }
    case "tri": [...carte.querySelectorAll(".carte-tri")].forEach(c => { clic(c); clic(carte.querySelector(".tri-colonne:not([data-col='" + c.dataset.col + "']) .tri-zone")); }); break;
    case "lettres": { const l = [...carte.querySelectorAll("[data-l]")].find(x => x.dataset.l !== d.cible[0]); clic(l); return; }
    case "association": { const g = carte.querySelector('[data-col="g"] .carte-match'); clic(g);
      clic([...carte.querySelectorAll('[data-col="d"] .carte-match')].find(x => x.dataset.id !== g.dataset.bon)); return; }
    case "trous": case "plan": {
      const cibles = [...carte.querySelectorAll(e.type === "trous" ? ".trou" : ".plan-case")];
      const ets = [...carte.querySelectorAll(".etiquette")];
      cibles.forEach((c, i) => { const et = ets.filter(x => !x.classList.contains("posee")).find(x => x.dataset.mot !== c.dataset.rep); clic(et); clic(c); });
      break; }
  }
  clic(carte.querySelector("[data-valider]"));
}

/* ---------------- 4. Partie complète ---------------- */
async function partieComplete(niveau, D){
  console.log(`\n2. Partie complète ${niveau}`);
  const { w, doc, erreurs } = await chargerJeu("", REGLAGES_TEST);
  const E = D.enigmes;
  const inp = doc.getElementById("input-equipe");
  inp.value = "Les Fioles " + niveau; inp.dispatchEvent(new w.Event("input"));
  doc.querySelector(`.opt-niveau[data-niveau="${niveau}"]`).click();
  ok(!doc.getElementById("btn-demarrer").disabled, "bouton démarrer inactif");
  doc.getElementById("btn-demarrer").click();
  await sleep(200);
  const ETAT = w.ETAT;
  ok(doc.getElementById("ecran-salle").classList.contains("actif"), "écran salle non affiché");
  let negatifFait = false, indiceTeste = false;
  for(const s of E.salles){
    ok(ETAT.salle === s.num, `salle attendue ${s.num}, obtenue ${ETAT.salle}`);
    ok(doc.querySelector("#salle-contenu .decor-fallback svg"), `salle ${s.num} : décor SVG absent`);
    const portrait = doc.querySelector("#salle-contenu .personnage-scene .portrait");
    ok(portrait && portrait.querySelector("svg") && portrait.dataset.perso === D.dialogues.salles[s.num-1].dialogue_intro.perso, `salle ${s.num} : personnage SVG absent`);
    const liste = s.enigmes.filter(e => !e.niveaux || e.niveaux.includes(niveau));
    for(const [k, e] of liste.entries()){
      ok(doc.getElementById("enigme-" + e.id), `énigme ${e.id} non affichée`);
      if(!negatifFait || s.num === 3){
        // tests négatifs sur plusieurs types
        const avant = ETAT.enigmesReussies;
        mauvaiseReponse(w, e, niveau);
        await sleep(20);
        ok(ETAT.enigmesReussies === avant && !doc.getElementById("enigme-" + e.id).classList.contains("resolue"), `${e.id} (${e.type}) : une mauvaise réponse a validé`);
        negatifFait = true;
        // on recharge l'énigme proprement pour la résoudre
        w.eval("afficherEnigmeCourante()");
      }
      if(niveau === "CM2" && s.num === 2 && k === 0 && !indiceTeste){
        const sc = ETAT.score;
        doc.getElementById("indice-" + e.id).click();
        ok(ETAT.score === Math.max(0, sc - 2) && ETAT.indicesTotal === 1, "indice : moins 2 points");
        indiceTeste = true;
        ETAT.score += 2; ETAT.indicesTotal = 0; ETAT.indicesSalle = 0; // on neutralise pour viser le score maximal
      }
      resoudre(w, e, niveau);
      await sleep(760);
      ok(doc.getElementById("enigme-" + e.id).classList.contains("resolue"), `${e.id} (${e.type}) non résolue`);
      const src = doc.querySelector(`#fb-${CSS_ID(e.id)} .source-correction`);
      ok(!!src, `${e.id} : source absente de la correction`);
      if(k < liste.length - 1){
        const b = doc.getElementById("btn-enigme-suivante");
        ok(!!b, `${e.id} : pas de bouton suivant`); if(b) b.click();
        await sleep(20);
      }
    }
    await sleep(950);
    ok(ETAT.motsCles.includes(D.dialogues.salles[s.num - 1].motCle), `salle ${s.num} : mot-clé non obtenu`);
    if(s.num < 5){
      // Le bouton « Salle suivante » apparaît en fin de dialogue (ou après 12 s) : on simule le clic
      w.eval("ETAT.salle++; ETAT.enigme = 0; afficherSalle(ETAT.salle);");
      await sleep(50);
    }
  }
  await sleep(1800);
  ok(doc.getElementById("ecran-fin").classList.contains("actif"), "écran de fin non affiché");
  const fin = doc.getElementById("fin-contenu").textContent;
  ok(/PESER[\s\S]*OBSERVER[\s\S]*AIMANTER[\s\S]*ÉVAPORER[\s\S]*COMPARER/.test(doc.querySelector(".protocole-final").textContent), "protocole final dans le désordre");
  ok(ETAT.motsCles.length === 5, "5 mots-clés");
  ok(ETAT.enigmesReussies === (niveau === "CM1" ? 15 : 20), "énigmes réussies " + ETAT.enigmesReussies);
  // Quizz
  const Q = w.quizzCourant();
  doc.querySelectorAll("#quizz .qcm-question").forEach((qi, i) => qi.querySelector(`.qcm-option[data-j="${Q[i].bonne}"]`).click());
  doc.getElementById("btn-voir-score").click();
  await sleep(20);
  const attendu = niveau === "CM1" ? 100 : 125;
  ok(w.scoreMax() === attendu, `score max ${w.scoreMax()} ≠ ${attendu}`);
  ok(ETAT.score === attendu, `score final ${ETAT.score} ≠ ${attendu}`);
  ok(/Grand chimiste/.test(doc.getElementById("score-recap").textContent), "mention absente");
  ok(!/undefined|NaN/.test(doc.getElementById("fin-contenu").innerHTML), "undefined/NaN à l'écran de fin");
  // Impression du bilan
  w.imprimerBilan();
  ok(w.__imprime >= 1, "bilan non imprimé");
  const sauve = JSON.parse(w.localStorage.getItem("escape_melanges_v1") || "{}");
  ok(sauve.fini === true && sauve.score === attendu, "sauvegarde finale incorrecte");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.slice(0, 3).join(" | "));
  console.log(`   ${niveau} : score ${ETAT.score}/${w.scoreMax()}, ${ETAT.enigmesReussies} énigmes, mots ${ETAT.motsCles.join(" ")}`);
}
const CSS_ID = id => id.replace(/([^a-zA-Z0-9_-])/g, "\\$1");

/* ---------------- 5. Mode vérification, réglages, impressions, leçons ---------------- */
async function autresTests(D){
  console.log("\n3. Mode vérification");
  let { w, doc, erreurs } = await chargerJeu("?salle=3&niveau=CM1&enigme=2", REGLAGES_TEST);
  ok(w.ETAT.salle === 3 && w.ETAT.niveau === "CM1", "vérif : mauvaise salle");
  ok(!!doc.getElementById("enigme-3-2"), "vérif : énigme 3-2 non affichée");
  ok(w.localStorage.getItem("escape_melanges_v1") === null, "vérif : sauvegarde écrite");
  ok(erreurs.length === 0, "erreurs JS (vérif) : " + erreurs.join(" | "));
  for(const q of ["?salle=5&niveau=CM2&enigme=4", "?salle=6&niveau=CM2", "?salle=6&niveau=CM1"]){
    const r = await chargerJeu(q, REGLAGES_TEST);
    if(q.includes("enigme=4")) ok(!!r.doc.getElementById("enigme-5-4"), "vérif : 5-4 absente");
    if(q.includes("salle=6")) ok(r.doc.getElementById("ecran-fin").classList.contains("actif") && r.doc.querySelector(".protocole-final"), "vérif : fin absente " + q);
    ok(r.erreurs.length === 0, "erreurs JS " + q + " : " + r.erreurs.join(" | "));
  }

  console.log("4. Réglages, leçons, impressions");
  ({ w, doc, erreurs } = await chargerJeu("?salle=1&niveau=CM2", REGLAGES_TEST));
  w.ouvrirReglages();
  ok(doc.getElementById("overlay-reglages").classList.contains("show"), "réglages non ouverts");
  ok(!doc.getElementById("reg-concours"), "module concours encore présent");
  doc.getElementById("reg-taille").value = "1.3";
  doc.getElementById("reg-calme").click();
  doc.getElementById("btn-sauver-reglages").click();
  const R = JSON.parse(w.localStorage.getItem("escape_reglages_melanges"));
  ok(R.tailleTexte === 1.3 && R.animationsReduites === true, "réglages non sauvegardés");
  ok(doc.body.classList.contains("calme"), "animations réduites non appliquées");
  ok(doc.documentElement.style.getPropertyValue("--taille-texte") === "1.3rem", "taille du texte non appliquée");
  // Leçons
  await w.ouvrirBiblioLecons();
  ok(doc.querySelectorAll("#corps-lecons .carte-lecon").length === 5, "5 leçons dans la bibliothèque");
  for(const l of D.lecons.lecons){
    w.afficherLecon(l.id);
    const c = doc.getElementById("corps-lecons");
    ok(c.querySelector(".lecon-schema svg") && c.querySelector(".lecon-lexique") && c.querySelector(".lecon-source"), `leçon ${l.id} : schéma/lexique/source`);
  }
  // Bouton « Leçon » d'une énigme
  const bf = doc.querySelector("[data-fiche]");
  ok(bf && bf.dataset.fiche === "masses", "bouton Leçon de l'énigme");
  // Impressions
  w.__imprime = 0;
  for(const t of ["prepa", "qcm", "fermees", "docs", "tout"]){
    await w.imprimerFiches(t);
    await sleep(20);
    const z = doc.getElementById("zone-impression") || doc.querySelector(".zone-impression, #impression");
    const html = z ? z.innerHTML : doc.body.innerHTML;
    ok(!/undefined|NaN|\[object Object\]/.test(html), "impression " + t + " : undefined");
  }
  ok(w.__imprime >= 5, "impressions lancées : " + w.__imprime);
  const zoneTxt = (doc.getElementById("zone-impression") || doc.body).textContent;
  ok(/Madame Mélange/.test(zoneTxt) && !/Constitution|Sceau/.test(zoneTxt), "impression : titres du jeu");
  ok(erreurs.length === 0, "erreurs JS (réglages) : " + erreurs.join(" | "));
}

/* ---------------- 6. verifier.html ---------------- */
async function testerVerifier(){
  console.log("5. verifier.html");
  const html = fs.readFileSync(path.join(RACINE, "verifier.html"), "utf8");
  const erreurs = [];
  const vc = new VirtualConsole();
  vc.on("jsdomError", e => erreurs.push(String(e.message || e)));
  const dom = new JSDOM(html.replace(/<script[\s\S]*?<\/script>/g, ""), { url: "http://localhost/verifier.html#melanges", runScripts: "outside-only", virtualConsole: vc });
  const w = dom.window;
  w.fetch = async url => {
    const u = new URL(url, w.location.href); const p = decodeURIComponent(u.pathname);
    if(p === "/api/fichiers") return { ok: true, status: 200, json: async () => ({ fichiers: {} }) };
    const f = path.join(RACINE, p);
    if(fs.existsSync(f) && fs.statSync(f).isFile()){ const t = fs.readFileSync(f, "utf8"); return { ok: true, status: 200, json: async () => JSON.parse(t), text: async () => t }; }
    return { ok: false, status: 404, json: async () => ({}), text: async () => "" };
  };
  const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
  try{ w.eval(scripts.join("\n;\n") + "\n;window.__T = {ONGLETS, CONSTRUCTEURS, construireMelanges, construireDeclaration, construireTour, construireConstitution};"); }catch(e){ erreurs.push(e.message); }
  w.document.dispatchEvent(new w.Event("DOMContentLoaded"));
  await sleep(600);
  let jeu;
  try{ jeu = await w.__T.construireMelanges(); }catch(e){ erreurs.push("construireMelanges : " + e.message); }
  ok(!!jeu, "construireMelanges a échoué");
  if(jeu){
    const cm1 = jeu.tests[0], cm2 = jeu.tests[1];
    ok(/15 énigmes/.test(cm1.titre) && /20 énigmes/.test(cm2.titre), "compteurs d'énigmes : " + cm1.titre + " / " + cm2.titre);
    ok(cm2.liens.some(l => /salle=5&niveau=CM2&enigme=4/.test(l.url)), "lien vers 5-4 CM2");
    ok(jeu.familles[1].slots.length === 5, "5 personnages");
    ok(jeu.familles[2].slots.length === 6, "6 illustrations");
  }
  ok(w.__T.ONGLETS.some(o => o.id === "melanges") && typeof w.__T.CONSTRUCTEURS.melanges === "function", "onglet melanges");
  // les autres jeux se construisent toujours
  for(const f of ["construireDeclaration", "construireTour", "construireConstitution"]){
    try{ const j = await w.__T[f](); ok(!!j && j.tests, f); }catch(e){ ok(false, f + " : " + e.message); }
  }
  ok(erreurs.length === 0, "erreurs JS verifier : " + erreurs.join(" | "));
}

(async () => {
  const D = testerDonnees();
  await partieComplete("CM1", D);
  await partieComplete("CM2", D);
  await autresTests(D);
  await testerVerifier();
  console.log(`\nRésultat : ${OK} vérifications réussies, ${ECHECS} échec(s).`);
  process.exit(ECHECS ? 1 : 0);
})().catch(e => { console.error("ERREUR", e); process.exit(2); });
