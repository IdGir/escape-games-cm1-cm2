/* ============================================================
   TESTS AUTOMATIQUES — Le Manuscrit de l'abbaye (Node + jsdom)
   ------------------------------------------------------------
   Lancement, depuis la racine du dépôt :
       npm install jsdom          (une seule fois, hors dépôt)
       node moyen-age-abbaye/tests/test-jeu.js
   Vérifie : données JSON, leçons, parties complètes CM1 et CM2
   (scores 100 et 125), mécanisme final, tests négatifs, indices,
   mode vérification, réglages, impressions.
   ============================================================ */
const fs = require("fs");
const path = require("path");
const { JSDOM, ResourceLoader, VirtualConsole } = require("jsdom");

const JEU = path.resolve(__dirname, "..");
const RACINE = path.resolve(JEU, "..");
let echecs = 0, reussis = 0;
function ok(cond, msg){ if(cond){ reussis++; } else { echecs++; console.error("  ✗ " + msg); } }
const pause = ms => new Promise(r => setTimeout(r, ms));
async function attendre(fn, max = 8000, msg = "condition"){
  const t0 = Date.now();
  while(Date.now() - t0 < max){ try{ if(fn()) return true; }catch(e){} await pause(40); }
  throw new Error("Délai dépassé : " + msg);
}

/* ---------- 1. Données JSON ---------- */
function clesDupliquees(fichier){
  // Parcours manuel : on repère, objet par objet, deux fois la même clé.
  const s = fs.readFileSync(fichier, "utf8");
  const doublons = [];
  const pile = [];
  let i = 0, dansChaine = false, chaine = "", attendCle = false;
  for(i = 0; i < s.length; i++){
    const c = s[i];
    if(dansChaine){
      if(c === "\\"){ chaine += c + s[++i]; continue; }
      if(c === '"'){
        dansChaine = false;
        let j = i + 1; while(/\s/.test(s[j])) j++;
        if(s[j] === ":" && pile.length && pile[pile.length-1].type === "o"){
          const o = pile[pile.length-1];
          if(o.cles.has(chaine)) doublons.push(chaine);
          o.cles.add(chaine);
        }
        continue;
      }
      chaine += c; continue;
    }
    if(c === '"'){ dansChaine = true; chaine = ""; continue; }
    if(c === "{") pile.push({type:"o", cles:new Set()});
    else if(c === "[") pile.push({type:"a"});
    else if(c === "}" || c === "]") pile.pop();
  }
  return doublons;
}

const D = path.join(JEU, "assets", "data");
const fichiers = ["enigmes.json", "dialogues.json", "lecons.json", "evaluations.json"];
console.log("1. Données JSON");
const data = {};
for(const f of fichiers){
  const p = path.join(D, f);
  try{ data[f] = JSON.parse(fs.readFileSync(p, "utf8")); ok(true, f); }
  catch(e){ ok(false, f + " invalide : " + e.message); }
  const dup = clesDupliquees(p);
  ok(dup.length === 0, f + " : clés dupliquées " + dup.join(", "));
}
const E = data["enigmes.json"], L = data["lecons.json"], DI = data["dialogues.json"], EV = data["evaluations.json"];
const idsLecons = new Set(L.lecons.map(l => l.id));
const citees = new Set([E.final.lecon]);
const TYPES = new Set();
for(const niv of ["CM1", "CM2"]){
  let total = 0;
  for(const s of E.salles){
    const es = s.enigmes.filter(e => !e.niveaux || e.niveaux.includes(niv));
    total += es.length;
    ok(es.length === (niv === "CM1" ? 3 : 4), `salle ${s.num} ${niv} : ${es.length} énigmes`);
    for(let k = 1; k < es.length; k++) ok(es[k].type !== es[k-1].type, `salle ${s.num} ${niv} : deux « ${es[k].type} » consécutifs`);
    ok(es.some(e => ["ordre","tri","plan"].includes(e.type)), `salle ${s.num} ${niv} : aucune manipulation`);
    for(const e of es){
      TYPES.add(e.type);
      ok(idsLecons.has(e.lecon), `${e.id} : leçon « ${e.lecon} » introuvable`);
      citees.add(e.lecon);
      const ind = (e.indices[niv.toLowerCase()] || e.indices.commun || []);
      ok(ind.length === 3, `${e.id} ${niv} : ${ind.length} indices au lieu de 3`);
      ok(e.source && e.correction && e.consigne, `${e.id} : source, correction ou consigne manquante`);
      ok(e[niv.toLowerCase()] || e.commun, `${e.id} : pas de données pour ${niv}`);
    }
  }
  ok(total === (niv === "CM1" ? 15 : 20), `${niv} : ${total} énigmes`);
}
ok(TYPES.size >= 7, `types d'énigmes : ${TYPES.size}`);
for(const id of idsLecons) ok(citees.has(id), `leçon « ${id} » citée par aucune énigme`);
for(const l of L.lecons){
  ok(l.contenu && l.contenu.cm1 && l.contenu.cm2, `leçon ${l.id} : contenu cm1 / cm2`);
  ok(l.objectifs && l.objectifs.length, `leçon ${l.id} : objectifs`);
  ok(l.lexique && l.lexique.length >= 3, `leçon ${l.id} : lexique`);
  ok(l.sources && l.sources.length, `leçon ${l.id} : sources`);
  const mots = (l.contenu.cm2.replace(/<[^>]+>/g, " ").match(/\S+/g) || []).length;
  ok(mots >= 200 && mots <= 650, `leçon ${l.id} : ${mots} mots en CM2 (3 à 4 min de lecture visées)`);
}
ok(DI.salles.length === 5 && DI.salles.every(s => s.motCle), "5 salles avec mot-clé");
ok(DI.salles.every(s => DI.incipit.includes(s.motCle)), "l'incipit contient les 5 mots-clés");
ok(EV.quizz_final.CM1.length === 5 && EV.quizz_final.CM2.length === 5, "quizz final : 5 questions par niveau");
ok(EV.qcm.CM1.length === 10 && EV.qcm.CM2.length === 12, "QCM imprimables 10 / 12");
/* Pas d'emoji dans les énoncés, dialogues, leçons et corrections */
const EMOJI = /[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}]/u;
const textes = [];
E.salles.forEach(s => s.enigmes.forEach(e => {
  textes.push([e.id, JSON.stringify(e.consigne) + JSON.stringify(e.correction) + JSON.stringify(e.cm1||"") + JSON.stringify(e.cm2||"") + JSON.stringify(e.commun||"") + JSON.stringify(e.indices)]);
}));
DI.salles.forEach(s => textes.push(["dialogue " + s.num, JSON.stringify(s.dialogue_intro) + JSON.stringify(s.dialogue_reussite||s.dialogue_fin) + s.description]));
L.lecons.forEach(l => textes.push(["leçon " + l.id, JSON.stringify(l.contenu) + JSON.stringify(l.lexique)]));
for(const [nom, t] of textes) ok(!EMOJI.test(t.replace(/📚/g, "")), `${nom} : emoji dans le texte`);

/* ---------- 2. Chargement du jeu dans jsdom ---------- */
class ChargeurLocal extends ResourceLoader {
  fetch(url){
    const u = new URL(url);
    const f = path.join(RACINE, decodeURIComponent(u.pathname));
    if(fs.existsSync(f) && fs.statSync(f).isFile() && /\.(js|css)$/.test(f)) return Promise.resolve(fs.readFileSync(f));
    return null;   // médias absents : comme en classe sans fichier
  }
}
function installerFetch(window){
  window.fetch = async (url) => {
    const u = new URL(url, window.location.href);
    const f = path.join(RACINE, decodeURIComponent(u.pathname));
    const existe = fs.existsSync(f) && fs.statSync(f).isFile();
    const corps = existe ? fs.readFileSync(f, "utf8") : "";
    return { ok: existe, status: existe ? 200 : 404,
      json: async () => JSON.parse(corps), text: async () => corps,
      headers: { get: () => null } };
  };
}
async function ouvrir(recherche = "", stockage = {}){
  const erreurs = [];
  const vc = new VirtualConsole();
  vc.on("jsdomError", e => { if(!/Could not load|Not implemented/.test(e.message)) erreurs.push(e.message); });
  vc.on("error", m => erreurs.push(String(m)));
  const html = fs.readFileSync(path.join(JEU, "index.html"), "utf8");
  const dom = new JSDOM(html, {
    url: "http://localhost/moyen-age-abbaye/index.html" + recherche,
    runScripts: "dangerously", resources: new ChargeurLocal(), pretendToBeVisual: true, virtualConsole: vc,
    beforeParse(w){
      installerFetch(w);
      for(const [k, v] of Object.entries(stockage)) w.localStorage.setItem(k, v);
      w.confirm = () => false; w.alert = () => {}; w.print = () => { w.__imprime = (w.__imprime||0) + 1; };
      w.HTMLElement.prototype.scrollIntoView = function(){};
      w.scrollTo = () => {};
      w.HTMLMediaElement.prototype.play = function(){ return Promise.reject(new Error("pas de média")); };
      w.HTMLMediaElement.prototype.pause = function(){};
      w.HTMLMediaElement.prototype.load = function(){};
      if(!w.CSS) w.CSS = {};
      w.CSS.escape = s => String(s).replace(/["\\]/g, "\\$&");
      w.matchMedia = () => ({ matches: false, addListener(){}, removeListener(){}, addEventListener(){} });
    }
  });
  const w = dom.window;
  await attendre(() => w.document.readyState === "complete", 8000, "chargement");
  await attendre(() => typeof w.ENIGMES === "function" && w.ENIGMES() && w.ENIGMES().salles, 8000, "données");
  return { w, erreurs };
}
const REGLAGES_TEST = JSON.stringify({ cinematiques:false, narrationActive:false, sonsActifs:false, decorsVideo:false });

/* ---------- Solveurs : résolvent l'énigme affichée par l'interface ---------- */
function clic(el){ el.dispatchEvent(new el.ownerDocument.defaultView.MouseEvent("click", { bubbles:true })); }
function donneesNiv(w, e){ const n = w.ETAT.niveau.toLowerCase(); return e[n] || e.commun || e.cm2 || e.cm1; }
function resoudre(w, e, carte){
  const d = donneesNiv(w, e), q = s => carte.querySelector(s), qa = s => [...carte.querySelectorAll(s)];
  switch(e.type){
    case "qcm":
      d.questions.forEach((x, i) => clic(q(`.qcm-question[data-i="${i}"] .qcm-option[data-j="${x.bonne}"]`)));
      clic(q("[data-valider]")); break;
    case "vraifaux":
      d.affirmations.forEach((a, i) => clic(q(`.vf-ligne[data-i="${i}"] .vf-btn[data-rep="${a.vrai ? "vrai" : "faux"}"]`)));
      clic(q("[data-valider]")); break;
    case "association":
      qa('[data-col="g"] .carte-match').forEach(g => { clic(g); clic(q(`[data-col="d"] .carte-match[data-id="${g.dataset.bon}"]`)); });
      break;
    case "ordre": {
      const liste = q(".liste-ordre");
      for(let r = 1; r <= d.items.length; r++){
        let it = liste.querySelector(`.item-ordre[data-rang="${r}"]`);
        while([...liste.children].indexOf(it) > r - 1) clic(it.querySelector(".btn-monter"));
      }
      clic(q("[data-valider]")); break;
    }
    case "tri":
      qa(".carte-tri").forEach(c => { clic(c); clic(q(`.tri-colonne[data-col="${c.dataset.col}"] .tri-zone`)); });
      clic(q("[data-valider]")); break;
    case "trous":
      qa(".trou").forEach(t => { clic(qa(".etiquette:not(.posee)").find(x => x.dataset.mot === t.dataset.rep)); clic(t); });
      clic(q("[data-valider]")); break;
    case "plan":
      qa(".plan-case").forEach(c => { clic(qa(".etiquette:not(.posee)").find(x => x.dataset.mot === c.dataset.rep)); clic(c); });
      clic(q("[data-valider]")); break;
    case "lettres":
      d.cible.forEach(l => clic(qa(`[data-l="${l}"]:not(.utilisee)`)[0]));
      break;
    case "code":
      d.champs.forEach((c, i) => { q(`#code-${i}`).value = c.valeur; });
      clic(q("[data-valider]")); break;
    case "intrus":
      clic(q('.carte-intrus[data-intrus="1"]')); break;
    default: throw new Error("type inconnu " + e.type);
  }
}
/* Mauvaise réponse volontaire : l'énigme ne doit pas être validée */
function seTromper(w, e, carte){
  const d = donneesNiv(w, e), q = s => carte.querySelector(s), qa = s => [...carte.querySelectorAll(s)];
  switch(e.type){
    case "qcm":
      d.questions.forEach((x, i) => clic(q(`.qcm-question[data-i="${i}"] .qcm-option[data-j="${(x.bonne + 1) % x.options.length}"]`)));
      clic(q("[data-valider]")); return true;
    case "vraifaux":
      d.affirmations.forEach((a, i) => clic(q(`.vf-ligne[data-i="${i}"] .vf-btn[data-rep="${a.vrai ? "faux" : "vrai"}"]`)));
      clic(q("[data-valider]")); return true;
    case "code":
      d.champs.forEach((c, i) => { q(`#code-${i}`).value = "0"; });
      clic(q("[data-valider]")); return true;
    case "intrus":
      clic(q('.carte-intrus[data-intrus="0"]')); return true;
    case "association": {
      const g = qa('[data-col="g"] .carte-match')[0];
      clic(g); clic(qa('[data-col="d"] .carte-match').find(x => x.dataset.id !== g.dataset.bon)); return true;
    }
    case "tri": case "trous": case "plan": case "ordre":
      clic(q("[data-valider]")); return e.type !== "ordre";   // incomplet → refusé (l'ordre peut être juste par hasard)
    default: return false;
  }
}

/* ---------- 3. Partie complète ---------- */
async function partie(niveau, { indiceSalle = 0 } = {}){
  const { w, erreurs } = await ouvrir("", { escape_reglages_moyenage: REGLAGES_TEST });
  const doc = w.document;
  clic(doc.querySelector(`.opt-niveau[data-niveau="${niveau}"]`));
  const inp = doc.getElementById("input-equipe");
  inp.value = "Les Testeurs"; inp.dispatchEvent(new w.Event("input"));
  ok(!doc.getElementById("btn-demarrer").disabled, "bouton de départ actif");
  clic(doc.getElementById("btn-demarrer"));
  let indicesPris = 0;
  for(let s = 1; s <= 5; s++){
    await attendre(() => w.ETAT.salle === s && doc.querySelector("#zone-enigme .enigme-carte"), 8000, `salle ${s}`);
    const liste = w.salleEnigmes(s);
    for(let k = 0; k < liste.length; k++){
      const e = liste[k];
      await attendre(() => doc.getElementById("enigme-" + e.id), 8000, "énigme " + e.id);
      const carte = doc.getElementById("enigme-" + e.id);
      const c2 = carte;
      if(indiceSalle === s && k === 0){
        const avant = w.ETAT.score;
        clic(c2.querySelector("#indice-" + e.id));
        ok(w.ETAT.score === Math.max(0, avant - 2), "un indice retire 2 points");
        ok(c2.querySelector(".feedback.indice"), "l'indice s'affiche");
        indicesPris++;
      }
      resoudre(w, e, c2);
      await attendre(() => c2.classList.contains("resolue"), 3000, "résolution " + e.id);
      ok(c2.querySelector(".correction") && c2.querySelector(".source-correction"), `${e.id} : correction et source affichées`);
      if(k < liste.length - 1){
        await attendre(() => doc.getElementById("btn-enigme-suivante"), 4000, "bouton énigme suivante");
        clic(doc.getElementById("btn-enigme-suivante"));
      }
    }
    if(s < 5){
      await attendre(() => doc.getElementById("btn-salle-suivante"), 15000, "bouton page suivante " + s);
      ok(w.ETAT.motsCles.includes(DI.salles[s-1].motCle), `mot-clé ${DI.salles[s-1].motCle}`);
      clic(doc.getElementById("btn-salle-suivante"));
    }
  }
  /* Mécanisme final : le fermoir (frise) */
  await attendre(() => doc.getElementById("enigme-final"), 8000, "fermoir");
  ok(w.ETAT.motsCles.length === 5, "5 mots-clés");
  ok(doc.querySelectorAll(".incipit .mot-incipit").length === 5, "l'incipit affiche les 5 mots");
  const fin = w.ENIGMES().final, cf = doc.getElementById("enigme-final");
  clic(cf.querySelector("[data-valider]"));   // ordre de départ mélangé : on essaie, puis on résout
  resoudre(w, fin, cf);
  await attendre(() => doc.querySelector("#quizz .qcm-question"), 8000, "écran de fin");
  ok(w.ETAT.fermoir === true, "fermoir ouvert");
  /* Quizz final */
  const quizz = w.quizzCourant();
  quizz.forEach((x, i) => clic(doc.querySelector(`#quizz .qcm-question[data-i="${i}"] .qcm-option[data-j="${x.bonne}"]`)));
  clic(doc.getElementById("btn-voir-score"));
  await pause(50);
  const max = niveau === "CM1" ? 100 : 125;
  ok(w.scoreMax() === max, `score maximal ${niveau} = ${w.scoreMax()}`);
  const attendu = max - 2*indicesPris - (indicesPris ? 1 : 0);   // indice : −2, et bonus de rapidité 3 → 2
  ok(w.ETAT.score === attendu, `score final ${niveau} : ${w.ETAT.score} (attendu ${attendu})`);
  ok(doc.getElementById("score-recap").textContent.includes(String(attendu)), "bilan affiché");
  /* Impression du bilan */
  clic(doc.getElementById("btn-imprimer-bilan"));
  ok(w.__imprime >= 1, "impression du bilan");
  ok(erreurs.length === 0, "erreurs JavaScript : " + erreurs.join(" | "));
  w.close();
}

/* Étapes : node test-jeu.js [cm1|cm2|indice|verif|reglages] — sans argument, tout est lancé. */
const ETAPE = process.argv[2] || "tout";
const faire = e => ETAPE === "tout" || ETAPE === e;
(async () => {
  try{
    if(faire("cm1")){ console.log("2. Partie complète CM1");  await partie("CM1"); }
    if(faire("cm2")){ console.log("3. Partie complète CM2");  await partie("CM2"); }
    if(faire("indice")){ console.log("4. Indice en salle 2 (CM2)"); await partie("CM2", { indiceSalle: 2 }); }
    if(faire("verif")){
    console.log("5. Chaque énigme en mode vérification : mauvaise réponse refusée, puis résolution");
    for(const s of E.salles) for(const e of s.enigmes){
      const niv = (!e.niveaux || e.niveaux.includes("CM1")) ? "CM1" : "CM2";
      const { w } = await ouvrir(`?salle=${s.num}&niveau=${niv}&enigme=${w_rang(e, s, niv)}`, { escape_reglages_moyenage: REGLAGES_TEST });
      await attendre(() => w.document.getElementById("enigme-" + e.id), 6000, "vérif " + e.id);
      const carte = w.document.getElementById("enigme-" + e.id);
      const teste = seTromper(w, e, carte);
      await pause(30);
      if(teste) ok(!carte.classList.contains("resolue"), `${e.id} (${e.type}) : mauvaise réponse refusée`);
      resoudre(w, e, carte);
      await attendre(() => carte.classList.contains("resolue"), 3000, "résolution " + e.id);
      ok(w.localStorage.getItem("escape_moyenage_v1") === null, `${e.id} : le mode vérification ne sauvegarde rien`);
      w.close();
    }
    }
    if(faire("verif")){
    console.log("6. Mode vérification : fin de partie");
    {
      const { w } = await ouvrir("?salle=6&niveau=CM2", { escape_reglages_moyenage: REGLAGES_TEST });
      await attendre(() => w.document.getElementById("enigme-final"), 6000, "fermoir en vérification");
      ok(true, "salle=6 ouvre le fermoir");
      w.close();
    }
    }
    if(faire("reglages")){
      console.log("7. Réglages et leçons");
      const { w, erreurs } = await ouvrir("", { escape_reglages_moyenage: REGLAGES_TEST });
      const doc = w.document;
      w.ouvrirReglages();
      ok(doc.getElementById("overlay-reglages").classList.contains("show"), "réglages ouverts");
      doc.getElementById("reg-taille").value = "1.3";
      const calme = doc.getElementById("reg-calme"); if(!calme.classList.contains("actif")) clic(calme);
      w.sauverReglages();
      const r = JSON.parse(w.localStorage.getItem("escape_reglages_moyenage"));
      ok(r.tailleTexte === 1.3 && r.animationsReduites === true, "réglages sauvegardés");
      ok(doc.documentElement.style.getPropertyValue("--taille-texte") === "1.3rem", "taille du texte appliquée");
      ok(doc.body.classList.contains("calme"), "animations réduites appliquées");
      await w.ouvrirBiblioLecons();
      ok(doc.querySelectorAll(".carte-lecon").length === 5, "5 leçons dans la bibliothèque");
      for(const l of L.lecons){
        w.afficherLecon(l.id);
        const corps = doc.getElementById("corps-lecons");
        ok(corps.querySelector(".lecon-lexique") && corps.querySelector(".lecon-sources"), `leçon ${l.id} : lexique et sources affichés`);
        if(l.schema) ok(corps.querySelector(".lecon-schema svg"), `leçon ${l.id} : schéma SVG`);
      }
      console.log("8. Impressions");
      for(const niv of ["CM1", "CM2"]){
        w.ETAT.niveau = niv;
        await w.imprimerFiches("tout");
        const z = doc.querySelector(".zone-impression");
        ok(z && z.textContent.includes("CORRIGÉS"), `impression ${niv} : corrigés séparés`);
        ok(z.querySelectorAll(".impr-fiche-prepa").length === 5, `impression ${niv} : 5 fiches préparatoires`);
        ok(!/undefined|Constitution/.test(z.textContent), `impression ${niv} : texte propre`);
      }
      ok(erreurs.length === 0, "erreurs JavaScript : " + erreurs.join(" | "));
      w.close();
    }
  }catch(e){ echecs++; console.error("  ✗ " + e.stack); }
  console.log(`\n${reussis} vérifications réussies, ${echecs} échec(s).`);
  process.exit(echecs ? 1 : 0);
})();

function w_rang(e, s, niv){
  return s.enigmes.filter(x => !x.niveaux || x.niveaux.includes(niv)).findIndex(x => x.id === e.id) + 1;
}
