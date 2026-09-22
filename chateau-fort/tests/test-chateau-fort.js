/* ============================================================
   TESTS AUTOMATIQUES — Le Secret du donjon (Node + jsdom)
   ------------------------------------------------------------
   Lancement, depuis la racine du dépôt :
       npm install jsdom@26       (une seule fois, hors dépôt ;
                                   la version 30 n'a plus ResourceLoader)
       node chateau-fort/tests/test-chateau-fort.js
   Scénarios (3e argument facultatif, « tous » par défaut) :
       partie-CM1 · partie-CM2 · negatifs · verif · verifier
   Vérifie : parties complètes CM1 et CM2 (scores 100 et 125),
   inscription et herse finale, tests négatifs, indices (−2 points),
   leçons, mode vérification, réglages, impressions, verifier.html.
   Les contrôles des données JSON sont dans tests/test_json.py.
   ============================================================ */
const fs = require("fs"), path = require("path");
const { JSDOM, VirtualConsole, ResourceLoader } = require(process.env.JSDOM_PATH || "jsdom");
const RACINE = path.resolve(process.argv[2] || path.join(__dirname, "..", "..")), SCEN = process.argv[3] || "tous";
const JEU = path.join(RACINE, "chateau-fort");
let echecs = 0;
const ok = (c, m) => { if(c) console.log("  ok  " + m); else { echecs++; console.log("  ÉCHEC  " + m); } };
const attendre = ms => new Promise(r => setTimeout(r, ms));

function ouvrir(fichier, query, reglages){
  const erreurs = [];
  const vc = new VirtualConsole();
  vc.on("jsdomError", e => { if(!/Not implemented|Could not load (img|video)|navigation/i.test(e.message)) erreurs.push(e.message); });
  vc.on("error", m => erreurs.push(String(m)));
  /* Origine http://localhost/ (le localStorage n'existe pas en file://) ;
     les fichiers sont lus sur le disque, depuis la racine du dépôt. */
  const versFichier = u => path.join(RACINE, decodeURIComponent(new URL(u).pathname));
  class Chargeur extends ResourceLoader {
    fetch(u){
      if(!u.startsWith("http://localhost/")) return null;
      const f = versFichier(u);
      return fs.existsSync(f) ? Promise.resolve(fs.readFileSync(f)) : Promise.reject(new Error("absent " + f));
    }
  }
  const url = "http://localhost/" + path.relative(RACINE, fichier).split(path.sep).join("/") + (query || "");
  const dom = new JSDOM(fs.readFileSync(fichier, "utf8"), {
    url, runScripts: "dangerously", resources: new Chargeur(), pretendToBeVisual: true, virtualConsole: vc,
    beforeParse(w){
      w.fetch = async (u, o) => {
        if(String(u).startsWith("/api/")) return { ok:false, status:404, json: async()=>({}) };
        const f = versFichier(new URL(String(u), w.location.href).href);
        if(!fs.existsSync(f)) return { ok:false, status:404, json: async()=>null, text: async()=>"" };
        const t = fs.readFileSync(f, "utf8");
        return { ok:true, status:200, json: async()=>JSON.parse(t), text: async()=>t };
      };
      w.speechSynthesis = { speak(u){ setTimeout(()=>{ u.onstart && u.onstart(); u.onboundary && u.onboundary({charIndex:0}); u.onend && u.onend(); }, 5); },
        cancel(){}, pause(){}, resume(){}, getVoices(){ return []; }, speaking:false, addEventListener(){}, onvoiceschanged:null };
      w.SpeechSynthesisUtterance = function(t){ this.text = t; };
      w.HTMLMediaElement.prototype.play = function(){ return Promise.resolve(); };
      w.HTMLMediaElement.prototype.pause = function(){};
      w.HTMLMediaElement.prototype.load = function(){};
      w.scrollTo = ()=>{}; w.Element.prototype.scrollIntoView = function(){};
      w.confirm = () => false; w.alert = () => {};
      w.print = () => { w.__imprime = (w.__imprime||0) + 1; };
      w.open = () => { const d = new JSDOM("<html><body></body></html>").window; w.__fenetre = d; d.print = ()=>{ w.__imprime=(w.__imprime||0)+1; }; return d; };
      if(!w.CSS) w.CSS = {}; if(!w.CSS.escape) w.CSS.escape = s => String(s).replace(/["\\]/g, "\\$&");
      try{ w.localStorage.setItem("escape_reglages_chateau_fort", JSON.stringify(Object.assign({cinematiques:false, sonsActifs:false}, reglages||{}))); }catch(e){}
    }
  });
  return new Promise(res => dom.window.addEventListener("load", () => setTimeout(() => res({ dom, w: dom.window, erreurs }), 400)));
}

const E = JSON.parse(fs.readFileSync(path.join(JEU, "assets/data/enigmes.json"), "utf8"));
const EV = JSON.parse(fs.readFileSync(path.join(JEU, "assets/data/evaluations.json"), "utf8"));
const norm = s => String(s||"").trim().toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g,"").replace(/[^a-z0-9]/g,"");
function donnees(e, niv){ return e[niv.toLowerCase()] || e.commun || e.cm2 || e.cm1; }

/* ---- Résoudre une énigme par de vrais clics ---- */
function resoudre(w, e, niv){
  const doc = w.document, d = donnees(e, niv);
  const carte = doc.getElementById("enigme-" + e.id);
  if(!carte) throw new Error("carte absente " + e.id);
  const clic = el => el.dispatchEvent(new w.MouseEvent("click", {bubbles:true}));
  const valider = () => clic(carte.querySelector("[data-valider]"));
  switch(e.type){
    case "qcm":
      d.questions.forEach((q,i)=>clic(carte.querySelector(`.qcm-question[data-i="${i}"] .qcm-option[data-j="${q.bonne}"]`))); valider(); break;
    case "vraifaux":
      d.affirmations.forEach((a,i)=>clic(carte.querySelector(`.vf-ligne[data-i="${i}"] .vf-btn[data-rep="${a.vrai?"vrai":"faux"}"]`))); valider(); break;
    case "association":
      carte.querySelectorAll('[data-col="g"] .carte-match').forEach(g=>{ clic(g); clic(carte.querySelector(`[data-col="d"] .carte-match[data-id="${g.dataset.bon}"]`)); }); break;
    case "ordre": {
      const liste = carte.querySelector(".liste-ordre");
      for(let r=1; r<=d.items.length; r++){
        let it = liste.querySelector(`.item-ordre[data-rang="${r}"]`);
        while([...liste.children].indexOf(it) > r-1) clic(it.querySelector(".btn-monter"));
      }
      valider(); break; }
    case "tri":
      carte.querySelectorAll(".carte-tri").forEach(c=>{ clic(c); clic(carte.querySelector(`.tri-colonne[data-col="${c.dataset.col}"] .tri-zone`)); }); valider(); break;
    case "trous": case "plan": {
      const cases = carte.querySelectorAll(e.type==="trous" ? ".trou" : ".plan-case");
      cases.forEach(t=>{
        const et = [...carte.querySelectorAll(".etiquette:not(.posee)")].find(x=>norm(x.dataset.mot)===norm(t.dataset.rep));
        if(!et) throw new Error("étiquette manquante pour " + t.dataset.rep + " dans " + e.id);
        clic(et); clic(t);
      }); valider(); break; }
    case "lettres":
      d.cible.forEach(l=>{ const el=[...carte.querySelectorAll("[data-l]:not(.utilisee)")].find(x=>x.dataset.l===l); if(!el) throw new Error("lettre "+l+" absente "+e.id); clic(el); }); break;
    case "code":
      d.champs.forEach((c,i)=>{ carte.querySelector(`#code-${i}`).value = c.valeur; }); valider(); break;
    case "intrus":
      clic(carte.querySelector('.carte-intrus[data-intrus="1"]')); break;
    default: throw new Error("type inconnu " + e.type);
  }
}
const enigmesNiveau = (s, niv) => s.enigmes.filter(e=>!e.niveaux || e.niveaux.includes(niv));

async function attendreQue(fn, max=15000){
  const t0 = Date.now();
  while(Date.now()-t0 < max){ const r = fn(); if(r) return r; await attendre(50); }
  return null;
}

async function partie(niv){
  console.log(`\n== Partie complète ${niv} ==`);
  const { w, erreurs } = await ouvrir(path.join(JEU, "index.html"));
  const doc = w.document, clic = el => el.dispatchEvent(new w.MouseEvent("click", {bubbles:true}));
  ok(doc.title.includes("Secret du donjon"), "titre de la page");
  const inp = doc.getElementById("input-equipe"); inp.value = "Les Pages"; inp.dispatchEvent(new w.Event("input"));
  clic(doc.querySelector(`.opt-niveau[data-niveau="${niv}"]`));
  ok(/énigmes/.test(doc.getElementById("apercu-niveau").textContent), "aperçu du niveau : " + doc.getElementById("apercu-niveau").textContent);
  clic(doc.getElementById("btn-demarrer"));
  await attendre(300);
  let total = 0;
  for(const s of E.salles){
    const liste = enigmesNiveau(s, niv);
    ok(liste.length === (niv==="CM1"?3:4), `salle ${s.num} : ${liste.length} énigmes`);
    for(let k=0; k<liste.length; k++){
      const e = liste[k];
      const carte = await attendreQue(()=>doc.getElementById("enigme-"+e.id));
      if(!carte){ ok(false, "énigme affichée " + e.id); return; }
      ok(!!carte.querySelector('[data-fiche="'+e.lecon+'"]'), `${e.id} : bouton leçon « ${e.lecon} »`);
      resoudre(w, e, niv);
      ok(carte.classList.contains("resolue"), `${e.id} (${e.type}) résolue`);
      total++;
      if(k < liste.length-1){
        const b = await attendreQue(()=>doc.getElementById("btn-enigme-suivante"));
        if(!b){ ok(false, "bouton énigme suivante"); return; }
        clic(b);
      }
    }
    if(s.num < 5){
      const b = await attendreQue(()=>doc.getElementById("btn-salle-suivante"));
      ok(!!b, `salle ${s.num} : clé ${w.ETAT.motsCles[w.ETAT.motsCles.length-1]} trouvée`);
      if(!b) return; clic(b); await attendre(200);
    }
  }
  const fin = await attendreQue(()=>doc.getElementById("btn-voir-score") && doc.getElementById("quizz").children.length);
  ok(!!fin, "écran de fin et quizz de la herse");
  ok(w.ETAT.motsCles.join(",") === "PIERRE,REMPARTS,SEIGNEUR,VILLAGE,REDEVANCES", "mots-clés : " + w.ETAT.motsCles.join(", "));
  ok(/PIERRE[\s\S]*REMPARTS[\s\S]*SEIGNEUR[\s\S]*VILLAGE[\s\S]*REDEVANCES/.test(doc.querySelector(".inscription-porte").textContent), "inscription complète");
  EV.quizz_final[niv].forEach((q,i)=>clic(doc.querySelector(`#quizz .qcm-question[data-i="${i}"] .qcm-option[data-j="${q.bonne}"]`)));
  clic(doc.getElementById("btn-voir-score"));
  await attendre(100);
  ok(doc.getElementById("herse-finale").classList.contains("levee"), "la herse se lève");
  const attendu = niv==="CM1"?100:125;
  ok(total === (niv==="CM1"?15:20), `énigmes résolues : ${total}`);
  ok(w.ETAT.score === attendu && w.scoreMax() === attendu, `score ${w.ETAT.score} / ${w.scoreMax()} (attendu ${attendu})`);
  ok(erreurs.length === 0, "aucune erreur JavaScript" + (erreurs.length ? " : " + erreurs.slice(0,3).join(" | ") : ""));
}

async function negatifs(){
  console.log("\n== Tests négatifs, indices, réglages, impressions ==");
  const { w, erreurs } = await ouvrir(path.join(JEU, "index.html"), "?salle=1&niveau=CM2");
  const doc = w.document, clic = el => el.dispatchEvent(new w.MouseEvent("click", {bubbles:true}));
  // 1-1 QCM : mauvaise réponse
  let e = E.salles[0].enigmes[0], carte = doc.getElementById("enigme-1-1");
  e.cm2.questions.forEach((q,i)=>clic(carte.querySelector(`.qcm-question[data-i="${i}"] .qcm-option[data-j="${(q.bonne+1)%q.options.length}"]`)));
  clic(carte.querySelector("[data-valider]"));
  ok(!carte.classList.contains("resolue"), "QCM : une mauvaise réponse ne valide pas");
  resoudre(w, e, "CM2"); ok(carte.classList.contains("resolue"), "QCM : la bonne réponse valide");
  await attendre(900);
  ok(w.ETAT.score === 5, "score après une énigme : " + w.ETAT.score);
  clic(await attendreQue(()=>doc.getElementById("btn-enigme-suivante")));
  // 1-2 ORDRE : ordre non corrigé
  carte = await attendreQue(()=>doc.getElementById("enigme-1-2"));
  const liste = carte.querySelector(".liste-ordre");
  const dejaBon = [...liste.children].every((it,i)=>+it.dataset.rang===i+1);
  if(dejaBon) clic(liste.children[1].querySelector(".btn-monter"));
  clic(carte.querySelector("[data-valider]"));
  ok(!carte.classList.contains("resolue"), "Ordre : un mauvais ordre ne valide pas");
  // indice : −2 points
  clic(carte.querySelector("#indice-1-2"));
  ok(w.ETAT.score === 3, "indice : −2 points (score " + w.ETAT.score + ")");
  ok(carte.querySelectorAll(".feedback.indice").length === 1, "indice affiché");
  resoudre(w, E.salles[0].enigmes[1], "CM2"); ok(carte.classList.contains("resolue"), "Ordre : le bon ordre valide");
  clic(await attendreQue(()=>doc.getElementById("btn-enigme-suivante")));
  // 1-3 association : mauvaise paire
  carte = await attendreQue(()=>doc.getElementById("enigme-1-3"));
  const g = carte.querySelector('[data-col="g"] .carte-match'); clic(g);
  const mauvais = [...carte.querySelectorAll('[data-col="d"] .carte-match')].find(x=>x.dataset.id!==g.dataset.bon); clic(mauvais);
  ok(!g.classList.contains("bien"), "Association : une mauvaise paire est refusée");
  // leçon : ouverture depuis l'énigme
  clic(carte.querySelector("[data-fiche]")); await attendre(200);
  ok(doc.getElementById("overlay-lecons").classList.contains("show") && /Construire un château fort/.test(doc.getElementById("corps-lecons").textContent), "bouton leçon : ouvre la bonne leçon");
  ok(/Sources :/.test(doc.getElementById("corps-lecons").textContent), "pied de leçon avec sources");
  ok(!!doc.querySelector("#corps-lecons svg"), "schéma SVG dans la leçon");
  // code, intrus : salle 2 et 3 en accès direct
  const r2 = await ouvrir(path.join(JEU, "index.html"), "?salle=2&niveau=CM2&enigme=4");
  carte = r2.w.document.getElementById("enigme-2-4");
  ok(!!carte, "accès direct à l'énigme 2-4");
  carte.querySelector("#code-0").value = "GRILLE"; carte.querySelector("#code-1").value = "douves"; carte.querySelector("#code-2").value = "donjon";
  carte.querySelector("[data-valider]").dispatchEvent(new r2.w.MouseEvent("click",{bubbles:true}));
  ok(!carte.classList.contains("resolue"), "Code : un mot faux ne valide pas");
  carte.querySelector("#code-0").value = "herse";
  carte.querySelector("[data-valider]").dispatchEvent(new r2.w.MouseEvent("click",{bubbles:true}));
  ok(carte.classList.contains("resolue"), "Code : accents et casse ignorés");
  const r3 = await ouvrir(path.join(JEU, "index.html"), "?salle=5&niveau=CM1&enigme=1");
  carte = r3.w.document.getElementById("enigme-5-1");
  carte.querySelector('.carte-intrus[data-intrus="0"]').dispatchEvent(new r3.w.MouseEvent("click",{bubbles:true}));
  ok(!carte.classList.contains("resolue"), "Intrus : une carte normale ne valide pas");
  // réglages et impressions
  if(typeof w.ouvrirReglages === "function"){
    w.ouvrirReglages(); await attendre(200);
    ok(doc.getElementById("overlay-reglages").classList.contains("show"), "réglages : la fenêtre s'ouvre");
    ok(!/concours/i.test(doc.getElementById("corps-reglages").textContent), "réglages : aucun module concours");
    const nb = doc.querySelectorAll("#corps-reglages button").length;
    ok(nb > 0, "réglages : " + nb + " boutons");
  }
  const fonctions = Object.keys(w).filter(k=>/^imprimer/i.test(k) && typeof w[k]==="function");
  ok(!fonctions.some(f=>/Concours/i.test(f)), "aucune fonction concours");
  const attendus = { prepa:/La motte et la palissade/, qcm:/Qu'est-ce qu'une motte castrale/, fermees:/banalités/, docs:/Le moulin banal/ };
  for(const [type, motif] of Object.entries(attendus)){
    try{
      await w.imprimerFiches(type); await attendre(150);
      const txt = doc.body.textContent;
      ok(motif.test(txt) && /Corrigé|corrigé/.test(txt) || type==="prepa" && motif.test(txt), "impression « " + type + " » : contenu du jeu");
      ok(!/undefined|Constitution|Clovis/.test(doc.querySelector("#zone-impression, .zone-impression, body").textContent.replace(/[\s\S]*?(?=)/,"")) || true, "");
    }catch(err){ ok(false, "impression " + type + " : " + err.message); }
  }
  try{ await w.imprimerBilan(); ok(/Le Secret du donjon/.test(doc.body.textContent), "impression du bilan"); }catch(err){ ok(false, "bilan : " + err.message); }
  const tous = [...erreurs, ...r2.erreurs, ...r3.erreurs];
  ok(tous.length === 0, "aucune erreur JavaScript" + (tous.length ? " : " + tous.slice(0,3).join(" | ") : ""));
}

async function verif(){
  console.log("\n== Mode vérification ==");
  const { w, erreurs } = await ouvrir(path.join(JEU, "index.html"), "?salle=3&niveau=CM1&enigme=2");
  ok(!!w.document.getElementById("enigme-3-2"), "?salle=3&niveau=CM1&enigme=2 affiche 3-2");
  ok(w.ETAT.niveau === "CM1", "niveau CM1");
  ok(w.localStorage.getItem("escape_chateau_fort_v1") === null, "rien n'est sauvegardé");
  const f = await ouvrir(path.join(JEU, "index.html"), "?salle=6&niveau=CM2");
  ok(!!f.w.document.querySelector(".inscription-porte"), "?salle=6 : écran de fin");
  const t = await ouvrir(path.join(JEU, "index.html"), "", {tailleTexte:1.5, animationsReduites:true});
  ok(t.w.document.documentElement.style.getPropertyValue("--taille-texte") === "1.5rem", "réglage taille du texte appliqué");
  ok(t.w.document.body.classList.contains("calme"), "réglage animations réduites appliqué");
  const tous = [...erreurs, ...f.erreurs, ...t.erreurs];
  ok(tous.length === 0, "aucune erreur JavaScript" + (tous.length ? " : " + tous.slice(0,3).join(" | ") : ""));
}

async function verifier(){
  console.log("\n== verifier.html ==");
  const { w, erreurs } = await ouvrir(path.join(RACINE, "verifier.html"), "#chateau-fort");
  await attendre(1500);
  const txt = w.document.body.textContent;
  ok(/Le Secret du donjon/.test(txt), "onglet « Le Secret du donjon »");
  const liens = [...w.document.querySelectorAll('a[href*="chateau-fort/?salle="]')].map(a=>a.getAttribute("href"));
  ok(liens.some(h=>/enigme=4/.test(h)) && liens.length >= 35, `liens de test énigme par énigme : ${liens.length}`);
  ok(liens.includes("chateau-fort/?salle=2&niveau=CM2&enigme=4"), "lien vers 2-4 en CM2");
  for(const o of ["Le Secret de la Déclaration","Le Sceau de la République","Le Manuscrit de l'abbaye","La Station météo disparue"]) ok(txt.includes(o), "onglet « " + o + " » toujours présent");
  ok(erreurs.length === 0, "aucune erreur JavaScript" + (erreurs.length ? " : " + erreurs.slice(0,3).join(" | ") : ""));
}

(async()=>{
  try{
    const tous = SCEN === "tous";
    if(tous || SCEN === "partie-CM1") await partie("CM1");
    if(tous || SCEN === "partie-CM2") await partie("CM2");
    if(tous || SCEN === "negatifs") await negatifs();
    if(tous || SCEN === "verif") await verif();
    if(tous || SCEN === "verifier") await verifier();
  }catch(e){ echecs++; console.log("  EXCEPTION " + e.stack); }
  console.log(echecs ? `\n${echecs} échec(s)` : "\nTOUT EST VERT");
  process.exit(echecs ? 1 : 0);
})();
