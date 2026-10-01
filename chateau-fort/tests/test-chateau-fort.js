/* ============================================================
   TESTS AUTOMATIQUES — Le Secret du donjon (Node + jsdom)
   ------------------------------------------------------------
   Lancement, depuis la racine du dépôt :
       npm install jsdom@26       (une seule fois, hors dépôt ;
                                   la version 30 n'a plus ResourceLoader)
       node chateau-fort/tests/test-chateau-fort.js
   Scénarios (3e argument facultatif, « tous » par défaut) :
       partie-CM1 · partie-CM2 · types · negatifs · verif · verifier
   Moteur d'énigmes v2 (outils-moteur/enigmes.js) : chaque énigme se
   valide par un bouton « Vérifier » ; une erreur n'indique que le
   NOMBRE de réponses justes ; aucune correction après la réussite ;
   10 points du premier coup, 3 après erreur ; coffre final où l'on
   retape les 5 mots-clés.
   Vérifie : partie CM1 sans faute (score = scoreMax() = 185), partie
   CM2 avec une erreur et un coffre raté (235 − 7 − 7), mots-clés
   « Notez ce mot », coffre final (vide, refuse un mot faux, s'ouvre
   avec les bons mots), inscription et herse finale ; pour chacun des
   10 types : message « N … sur M » sans marquage bien/mal, puis
   3 points ; tests négatifs (réponse incomplète non comptée, indice
   −2 points, appariement, lettres et leurres), leçons, mode
   vérification, réglages, impressions, verifier.html.
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

/* ---- Résoudre une énigme par de vrais clics (moteur d'énigmes v2) ----
   Calqué sur le solveur de outils-moteur/tester_parties.py : chaque type se
   valide par le bouton [data-valider]. Avec faux = true, on compose une
   réponse volontairement erronée (une seule pièce mal placée). */
function resoudre(w, e, niv, faux){
  const doc = w.document, d = donnees(e, niv);
  const carte = doc.getElementById("enigme-" + e.id);
  if(!carte) throw new Error("carte absente " + e.id);
  const clic = el => el.dispatchEvent(new w.MouseEvent("click", {bubbles:true}));
  const valider = () => clic(carte.querySelector("[data-valider]"));
  // remise à zéro d'une tentative précédente (comme le ferait un élève)
  carte.querySelectorAll(".slots-lettres .slot.ok").forEach(clic);
  carte.querySelectorAll(".trou[data-pose], .plan-case[data-pose]").forEach(clic);
  switch(e.type){
    case "qcm":
      d.questions.forEach((q,i)=>{
        const j = faux && i === 0 ? (q.bonne + 1) % q.options.length : q.bonne;
        clic(carte.querySelector(`.qcm-question[data-i="${i}"] .qcm-option[data-j="${j}"]`));
      }); valider(); break;
    case "vraifaux":
      d.affirmations.forEach((a,i)=>{
        const v = faux && i === 0 ? !a.vrai : !!a.vrai;
        clic(carte.querySelector(`.vf-ligne[data-i="${i}"] .vf-btn[data-rep="${v?"vrai":"faux"}"]`));
      }); valider(); break;
    case "association": {
      // on apparie gauche → droite (les cartes reçoivent le même numéro), puis Vérifier
      const g = [...carte.querySelectorAll('[data-col="g"] .carte-match')];
      g.forEach((c,i)=>{
        const bon = faux && g.length > 1 ? g[(i + 1) % g.length].dataset.bon : c.dataset.bon;
        clic(c); clic(carte.querySelector(`[data-col="d"] .carte-match[data-id="${bon}"]`));
      }); valider(); break; }
    case "ordre": {
      const liste = carte.querySelector(".liste-ordre");
      for(let r=1; r<=d.items.length; r++){
        const it = liste.querySelector(`.item-ordre[data-rang="${r}"]`);
        while([...liste.children].indexOf(it) > r-1) clic(it.querySelector(".btn-monter"));
      }
      if(faux) clic(liste.children[0].querySelector(".btn-descendre"));
      valider(); break; }
    case "tri": {
      // clic sur une carte, puis sur une colonne
      const cols = [...carte.querySelectorAll(".tri-colonne")];
      [...carte.querySelectorAll(".carte-tri")].forEach((c,i)=>{
        let col = c.dataset.col;
        if(faux && i === 0) col = (cols.find(k=>k.dataset.col !== col) || cols[0]).dataset.col;
        clic(c); clic(carte.querySelector(`.tri-colonne[data-col="${col}"] .tri-zone`));
      }); valider(); break; }
    case "trous": case "plan": {
      const cibles = [...carte.querySelectorAll(e.type==="trous" ? ".trou" : ".plan-case")];
      const reps = cibles.map(c=>c.dataset.rep);
      if(faux && reps.length > 1) [reps[0], reps[1]] = [reps[1], reps[0]];
      cibles.forEach((t,i)=>{
        const et = [...carte.querySelectorAll(".etiquette:not(.posee)")].find(x=>norm(x.dataset.mot)===norm(reps[i]));
        if(!et) throw new Error("étiquette manquante pour " + reps[i] + " dans " + e.id);
        clic(et); clic(t);
      }); valider(); break; }
    case "lettres": {
      // anagramme : les lettres [data-l] cliquées remplissent les cases button.slot
      let cible = d.cible.slice();
      if(faux){
        [cible[0], cible[cible.length-1]] = [cible[cible.length-1], cible[0]];
        if(norm(cible.join("")) === norm(d.cible.join(""))) cible.reverse();
      }
      cible.forEach(l=>{
        const el = [...carte.querySelectorAll("[data-l]:not(.utilisee)")].find(x=>norm(x.dataset.l)===norm(l));
        if(!el) throw new Error("lettre "+l+" absente "+e.id);
        clic(el);
      }); valider(); break; }
    case "code":
      d.champs.forEach((c,i)=>{ carte.querySelector(`#code-${i}`).value = faux && i === 0 ? "faux" : c.valeur; }); valider(); break;
    case "intrus":
      // sélection, puis « C'est l'intrus ! »
      clic(carte.querySelector(`.carte-intrus[data-intrus="${faux?0:1}"]`)); valider(); break;
    default: throw new Error("type inconnu " + e.type);
  }
}
const enigmesNiveau = (s, niv) => s.enigmes.filter(e=>!e.niveaux || e.niveaux.includes(niv));

async function attendreQue(fn, max=15000){
  const t0 = Date.now();
  while(Date.now()-t0 < max){ const r = fn(); if(r) return r; await attendre(50); }
  return null;
}

/* Constantes du barème (déclarées en const dans app.js : lues par eval). */
const bareme = w => w.eval("({premier:PTS_PREMIER_COUP, apres:PTS_APRES_ERREUR, rapidite:PTS_RAPIDITE, quiz:PTS_QUIZ, nbQuiz:NB_QUIZ, malus:MALUS_INDICE, coffre:PTS_COFFRE_PREMIER, coffreApres:PTS_COFFRE_APRES})");
const texteSansBalises = s => String(s||"").replace(/<[^>]*>/g, " ").replace(/\s+/g, " ").trim();
/* Tous les textes de correction / explication d'une énigme (champ « correction »,
   champs « explication » des questions…). */
function textesCorrection(e){
  const t = [];
  const parcourir = o => { if(o && typeof o === "object") Object.entries(o).forEach(([k,v])=>{
    if(/^(correction|explication)$/.test(k) && typeof v === "string") t.push(texteSansBalises(v));
    else if(/^(correction|explication)$/.test(k) && v && typeof v === "object") Object.values(v).forEach(x=>typeof x === "string" && t.push(texteSansBalises(x)));
    else parcourir(v);
  }); };
  parcourir(e);
  // on écarte les extraits qui figurent aussi dans l'énoncé affiché (même phrase qu'une affirmation…)
  const enonce = texteSansBalises(JSON.stringify(e, (k, v) => /^(correction|explication)$/.test(k) ? undefined : v));
  return t.filter(x => x.length >= 12).map(x => x.slice(0, 40)).filter(x => !enonce.includes(x));
}
/* Après une vérification fausse : seul le NOMBRE de réponses justes est donné. */
function controlerErreur(carte, e, etiquette){
  const fb = carte.querySelector("#fb-" + e.id).textContent;
  ok(!carte.classList.contains("resolue"), `${etiquette} : une réponse fausse ne valide pas`);
  ok(/Pas tout juste/.test(fb) && (e.type === "intrus" ? /Ce n'est pas l'intrus/.test(fb) : /\b\d+ [^.]+ sur \d+\./.test(fb)),
     `${etiquette} : message « N … sur M » (${fb.replace(/\s+/g," ").slice(0,90)})`);
  ok(!carte.querySelector(".bien, .mal, .correct, .incorrect"), `${etiquette} : aucun élément marqué bien/mal`);
}
/* Après la réussite : seulement les points, aucune correction ni explication ni source. */
function controlerReussite(carte, e, pts, etiquette){
  const fb = carte.querySelector("#fb-" + e.id).textContent;
  ok(carte.classList.contains("resolue"), `${etiquette} (${e.type}) résolue`);
  ok(fb.includes("+" + pts + " points") && (pts === 10) === /Tout juste du premier coup/.test(fb), `${etiquette} : « +${pts} points » affiché`);
  const copie = carte.cloneNode(true);
  copie.querySelectorAll(".barre-outils, .consigne").forEach(x=>x.remove());   // la source est affichée dès le début, dans la barre d'outils
  const txt = copie.textContent.replace(/\s+/g, " ");
  const fuite = textesCorrection(e).find(x=>txt.includes(x));
  ok(!carte.querySelector(".correction, .explication") && !fuite && !(e.source && fb.includes(e.source)),
     `${etiquette} : aucune correction affichée après la réussite` + (fuite ? " (trouvé : « " + fuite + " »)" : ""));
}

/* ---- Partie complète ----
   avecErreurs = false : tout est juste du premier coup, score = scoreMax().
   avecErreurs = true  : la première énigme et le coffre sont d'abord ratés
   (3 points au lieu de 10 pour chacun). */
async function partie(niv, avecErreurs){
  console.log(`\n== Partie complète ${niv}${avecErreurs ? " (avec une erreur et un coffre raté)" : ""} ==`);
  const { w, erreurs } = await ouvrir(path.join(JEU, "index.html"));
  const doc = w.document, clic = el => el.dispatchEvent(new w.MouseEvent("click", {bubbles:true}));
  ok(doc.title.includes("Secret du donjon"), "titre de la page");
  const inp = doc.getElementById("input-equipe"); inp.value = "Les Pages"; inp.dispatchEvent(new w.Event("input"));
  clic(doc.querySelector(`.opt-niveau[data-niveau="${niv}"]`));
  ok(/énigmes/.test(doc.getElementById("apercu-niveau").textContent), "aperçu du niveau : " + doc.getElementById("apercu-niveau").textContent);
  clic(doc.getElementById("btn-demarrer"));
  await attendre(300);
  const B = bareme(w), DONNEES = w.eval("DONNEES");
  let total = 0;
  for(const s of E.salles){
    const liste = enigmesNiveau(s, niv);
    ok(liste.length === (niv==="CM1"?3:4), `salle ${s.num} : ${liste.length} énigmes`);
    for(let k=0; k<liste.length; k++){
      const e = liste[k];
      const carte = await attendreQue(()=>doc.getElementById("enigme-"+e.id));
      if(!carte){ ok(false, "énigme affichée " + e.id); return; }
      ok(!!carte.querySelector('[data-fiche="'+e.lecon+'"]'), `${e.id} : bouton leçon « ${e.lecon} »`);
      const avant = w.ETAT.score, premiere = avecErreurs && total === 0;
      if(premiere){ resoudre(w, e, niv, true); controlerErreur(carte, e, e.id); }
      resoudre(w, e, niv);
      const pts = premiere ? B.apres : B.premier;
      controlerReussite(carte, e, pts, e.id);
      total++;
      if(k < liste.length-1){
        const b = await attendreQue(()=>doc.getElementById("btn-enigme-suivante"));
        if(!b){ ok(false, "bouton énigme suivante après " + e.id); return; }
        ok(w.ETAT.score - avant === pts, `${e.id} : +${pts} points au score (${w.ETAT.score - avant})`);
        clic(b);
      }else{
        // fin de salle : pas de dialogue de réussite, le bouton suivant est là tout de suite
        const id = s.num < 5 ? "btn-salle-suivante" : "btn-coffre-final";
        const t0 = Date.now();
        const b = await attendreQue(()=>doc.getElementById(id), 3000);
        ok(!!b, `salle ${s.num} : bouton « ${s.num < 5 ? "Lieu suivant" : "Aller au coffre final"} » tout de suite (${Date.now()-t0} ms)`);
        if(!b) return;
        ok(w.ETAT.score - avant === pts + B.rapidite, `${e.id} : +${pts} points et +${B.rapidite} de rapidité (${w.ETAT.score - avant})`);
        const zone = doc.getElementById("zone-enigme").textContent;
        ok(zone.includes(s.motCle || DONNEES.salles[s.num-1].motCle) && /Notez ce mot/.test(zone), `salle ${s.num} : mot ${w.ETAT.motsCles[w.ETAT.motsCles.length-1]} affiché avec « Notez ce mot »`);
        clic(b); await attendre(200);
        ok(!doc.querySelector(".mot-cle"), `salle ${s.num} : le mot n'est plus affiché ensuite`);
      }
    }
  }
  // coffre final : les 5 mots sont à retaper, rien n'est prérempli
  const coffre = await attendreQue(()=>doc.getElementById("coffre-final"));
  ok(!!coffre, "coffre final affiché");
  if(!coffre) return;
  const champs = DONNEES.salles.map((s,i)=>doc.getElementById("coffre-"+i));
  ok(champs.length === 5 && champs.every(c=>c && c.value === ""), "coffre final : les 5 champs sont vides (non préremplis)");
  ok(!/PIERRE|REMPARTS|SEIGNEUR|REDEVANCES/.test(coffre.textContent), "coffre final : aucun mot-clé affiché");
  clic(doc.getElementById("btn-coffre"));
  ok(!w.ETAT.coffreOuvert && /manque/.test(doc.getElementById("fb-coffre").textContent) && w.ETAT.erreursTotal === (avecErreurs?1:0), "coffre final : champs vides refusés sans compter d'erreur");
  if(avecErreurs){
    champs.forEach((c,i)=>c.value = i === 2 ? "chevalier" : DONNEES.salles[i].motCle);
    clic(doc.getElementById("btn-coffre"));
    ok(!w.ETAT.coffreOuvert, "coffre final : un mot faux est refusé");
    ok(/4 mots justes sur 5/.test(doc.getElementById("fb-coffre").textContent), "coffre final : « 4 mots justes sur 5 »");
  }
  const avantCoffre = w.ETAT.score;
  champs.forEach((c,i)=>c.value = DONNEES.salles[i].motCle.toLowerCase());
  clic(doc.getElementById("btn-coffre"));
  ok(w.ETAT.coffreOuvert, "coffre final : s'ouvre avec les bons mots (casse ignorée)");
  ok(w.ETAT.score - avantCoffre === (avecErreurs ? B.coffreApres : B.coffre), `coffre final : +${avecErreurs ? B.coffreApres : B.coffre} points`);
  const fin = await attendreQue(()=>doc.getElementById("btn-voir-score") && doc.getElementById("quizz").children.length);
  ok(!!fin, "écran de fin et quizz de la herse");
  ok(w.ETAT.motsCles.join(",") === "PIERRE,REMPARTS,SEIGNEUR,VILLAGE,REDEVANCES", "mots-clés : " + w.ETAT.motsCles.join(", "));
  ok(/PIERRE[\s\S]*REMPARTS[\s\S]*SEIGNEUR[\s\S]*VILLAGE[\s\S]*REDEVANCES/.test(doc.querySelector(".inscription-porte").textContent), "inscription complète");
  EV.quizz_final[niv].forEach((q,i)=>clic(doc.querySelector(`#quizz .qcm-question[data-i="${i}"] .qcm-option[data-j="${q.bonne}"]`)));
  clic(doc.getElementById("btn-voir-score"));
  await attendre(100);
  ok(doc.getElementById("herse-finale").classList.contains("levee"), "la herse se lève");
  ok(total === (niv==="CM1"?15:20), `énigmes résolues : ${total}`);
  // barème v2 : nbEnigmes × 10 + 10 (coffre) + 5 salles × 3 (rapidité) + 5 questions × 2 (quizz)
  const max = total*B.premier + B.coffre + 5*B.rapidite + B.nbQuiz*B.quiz;
  ok(w.scoreMax() === max && max === (niv==="CM1"?185:235), `score maximum ${w.scoreMax()} (attendu ${max})`);
  const attendu = max - (avecErreurs ? (B.premier - B.apres) + (B.coffre - B.coffreApres) : 0);
  ok(w.ETAT.score === attendu, `score ${w.ETAT.score} / ${w.scoreMax()} (attendu ${attendu})`);
  ok(w.ETAT.enigmesPremierCoup === total - (avecErreurs?1:0) && w.ETAT.erreursTotal === (avecErreurs?2:0) && w.ETAT.coffrePremierCoup === !avecErreurs,
     `bilan : ${w.ETAT.enigmesPremierCoup} du premier coup, ${w.ETAT.erreursTotal} erreur(s), coffre du premier coup : ${w.ETAT.coffrePremierCoup}`);
  ok(erreurs.length === 0, "aucune erreur JavaScript" + (erreurs.length ? " : " + erreurs.slice(0,3).join(" | ") : ""));
}

/* ---- Chaque type d'énigme : une réponse fausse, puis la bonne ----
   Accès direct (mode vérification) à la première énigme CM2 de chaque type. */
async function types(){
  console.log("\n== Chaque type : erreur « N … sur M », puis réussite à 3 points ==");
  const vus = new Set(), tous = [];
  for(const s of E.salles){
    enigmesNiveau(s, "CM2").forEach((e, k)=>{
      if(vus.has(e.type)) return; vus.add(e.type);
      tous.push({ s, e, k });
    });
  }
  ok(vus.size === 10, `${vus.size} types d'énigmes rencontrés`);
  const errs = [];
  for(const { s, e, k } of tous){
    const r = await ouvrir(path.join(JEU, "index.html"), `?salle=${s.num}&niveau=CM2&enigme=${k+1}`);
    const carte = r.w.document.getElementById("enigme-" + e.id);
    if(!carte){ ok(false, `accès direct à ${e.id}`); continue; }
    const B = bareme(r.w);
    resoudre(r.w, e, "CM2", true);
    controlerErreur(carte, e, `${e.type} ${e.id}`);
    ok(r.w.ETAT.erreursTotal === 1, `${e.type} ${e.id} : une erreur comptée`);
    resoudre(r.w, e, "CM2");
    controlerReussite(carte, e, B.apres, `${e.type} ${e.id}`);
    await attendre(700);
    ok(r.w.ETAT.score === B.apres, `${e.type} ${e.id} : ${B.apres} points après une erreur (score ${r.w.ETAT.score})`);
    errs.push(...r.erreurs);
  }
  ok(errs.length === 0, "aucune erreur JavaScript" + (errs.length ? " : " + errs.slice(0,3).join(" | ") : ""));
}

async function negatifs(){
  console.log("\n== Tests négatifs, barème, indices, réglages, impressions ==");
  const { w, erreurs } = await ouvrir(path.join(JEU, "index.html"), "?salle=1&niveau=CM2");
  const doc = w.document, clic = el => el.dispatchEvent(new w.MouseEvent("click", {bubbles:true}));
  const B = bareme(w);
  ok(B.premier === 10 && B.apres === 3 && B.malus === 2, `barème : ${B.premier} pts du premier coup, ${B.apres} après erreur, indice −${B.malus}`);
  // 1-1 QCM : incomplet, puis faux deux fois, puis juste → 3 points
  let e = E.salles[0].enigmes[0], carte = doc.getElementById("enigme-1-1");
  ok(/10 points/.test(carte.querySelector(".bandeau-bareme").textContent) && /3 points/.test(carte.querySelector(".bandeau-bareme").textContent), "bandeau du barème : 10 / 3 points");
  clic(carte.querySelector("[data-valider]"));
  ok(!carte.classList.contains("resolue") && /Il reste/.test(doc.getElementById("fb-1-1").textContent) && w.ETAT.erreursTotal === 0, "QCM : une réponse incomplète n'est pas comptée comme erreur");
  e.cm2.questions.forEach((q,i)=>clic(carte.querySelector(`.qcm-question[data-i="${i}"] .qcm-option[data-j="${(q.bonne+1)%q.options.length}"]`)));
  clic(carte.querySelector("[data-valider]"));
  controlerErreur(carte, e, "QCM");
  ok(new RegExp("0 bonne réponse sur " + e.cm2.questions.length).test(doc.getElementById("fb-1-1").textContent), "QCM : « 0 bonne réponse sur " + e.cm2.questions.length + " »");
  ok(!!carte.querySelector(".perte-bonus") && w.ETAT.erreursTotal === 1, "QCM : bonus du premier coup perdu, une erreur comptée");
  clic(carte.querySelector("[data-valider]"));
  ok(w.ETAT.erreursTotal === 2 && !carte.querySelector(".perte-bonus"), "QCM : deuxième erreur comptée (avertissement non répété)");
  resoudre(w, e, "CM2");
  controlerReussite(carte, e, B.apres, "QCM");
  await attendre(900);
  ok(w.ETAT.score === 3 && w.ETAT.enigmesPremierCoup === 0, "score après une énigme réussie après erreurs : " + w.ETAT.score + " (attendu 3)");
  clic(await attendreQue(()=>doc.getElementById("btn-enigme-suivante")));
  // 1-2 ORDRE : un indice (−2), puis juste du premier coup → 10 points
  carte = await attendreQue(()=>doc.getElementById("enigme-1-2"));
  clic(carte.querySelector("#indice-1-2"));
  ok(w.ETAT.score === 1, "indice : −2 points (score " + w.ETAT.score + ")");
  ok(carte.querySelectorAll(".feedback.indice").length === 1, "indice affiché");
  resoudre(w, E.salles[0].enigmes[1], "CM2");
  controlerReussite(carte, E.salles[0].enigmes[1], B.premier, "Ordre");
  ok(carte.querySelector("#indice-1-2").disabled, "Ordre : bouton indice désactivé après la réussite");
  await attendre(900);
  ok(w.ETAT.score === 11 && w.ETAT.enigmesPremierCoup === 1, "Ordre : +10 du premier coup (l'indice n'annule pas le bonus) : score " + w.ETAT.score);
  clic(await attendreQue(()=>doc.getElementById("btn-enigme-suivante")));
  // 1-3 association : appariement par numéros, rien n'est corrigé avant « Vérifier »
  carte = await attendreQue(()=>doc.getElementById("enigme-1-3"));
  clic(carte.querySelector("[data-valider]"));
  ok(/Il reste/.test(doc.getElementById("fb-1-3").textContent) && w.ETAT.erreursTotal === 2, "Association : rien de relié → incomplet, aucune erreur comptée");
  const g = carte.querySelector('[data-col="g"] .carte-match'); clic(g);
  const mauvais = [...carte.querySelectorAll('[data-col="d"] .carte-match')].find(x=>x.dataset.id!==g.dataset.bon); clic(mauvais);
  ok(mauvais.classList.contains("apparie") && mauvais.querySelector(".num-paire").textContent === g.dataset.num, "Association : la paire reçoit le numéro " + g.dataset.num);
  ok(!carte.querySelector(".bien, .mal") && w.ETAT.erreursTotal === 2, "Association : une mauvaise paire n'est ni marquée ni comptée avant « Vérifier »");
  clic(mauvais);
  ok(!mauvais.classList.contains("apparie") && !g.classList.contains("apparie"), "Association : un clic sur la paire la défait");
  // leçon : ouverture depuis l'énigme
  clic(carte.querySelector("[data-fiche]")); await attendre(200);
  ok(doc.getElementById("overlay-lecons").classList.contains("show") && /Construire un château fort/.test(doc.getElementById("corps-lecons").textContent), "bouton leçon : ouvre la bonne leçon");
  ok(/Sources :/.test(doc.getElementById("corps-lecons").textContent), "pied de leçon avec sources");
  ok(!!doc.querySelector("#corps-lecons svg"), "schéma SVG dans la leçon");
  // code, intrus, lettres : accès direct
  const r2 = await ouvrir(path.join(JEU, "index.html"), "?salle=2&niveau=CM2&enigme=4");
  carte = r2.w.document.getElementById("enigme-2-4");
  ok(!!carte, "accès direct à l'énigme 2-4");
  carte.querySelector("#code-0").value = "GRILLE"; carte.querySelector("#code-1").value = "douves"; carte.querySelector("#code-2").value = "donjon";
  carte.querySelector("[data-valider]").dispatchEvent(new r2.w.MouseEvent("click",{bubbles:true}));
  ok(!carte.classList.contains("resolue"), "Code : un mot faux ne valide pas");
  ok(/2 cases justes sur 3/.test(carte.querySelector(".feedback").textContent), "Code : « 2 cases justes sur 3 »");
  carte.querySelector("#code-0").value = "hérse";
  carte.querySelector("[data-valider]").dispatchEvent(new r2.w.MouseEvent("click",{bubbles:true}));
  ok(carte.classList.contains("resolue"), "Code : accents et casse ignorés");
  const r3 = await ouvrir(path.join(JEU, "index.html"), "?salle=5&niveau=CM1&enigme=1");
  carte = r3.w.document.getElementById("enigme-5-1");
  const clic3 = el => el.dispatchEvent(new r3.w.MouseEvent("click",{bubbles:true}));
  clic3(carte.querySelector('.carte-intrus[data-intrus="0"]'));
  ok(!carte.classList.contains("resolue") && r3.w.ETAT.erreursTotal === 0, "Intrus : choisir une carte ne valide rien tout seul");
  clic3(carte.querySelector("[data-valider]"));
  ok(!carte.classList.contains("resolue") && /Ce n'est pas l'intrus/.test(carte.querySelector(".feedback").textContent), "Intrus : « C'est l'intrus ! » sur une carte normale est refusé");
  clic3(carte.querySelector('.carte-intrus[data-intrus="1"]')); clic3(carte.querySelector("[data-valider]"));
  ok(carte.classList.contains("resolue"), "Intrus : sélection de l'intrus puis « C'est l'intrus ! » valide");
  const r4 = await ouvrir(path.join(JEU, "index.html"), "?salle=4&niveau=CM2&enigme=4");
  carte = r4.w.document.getElementById("enigme-4-4");
  const clic4 = el => el.dispatchEvent(new r4.w.MouseEvent("click",{bubbles:true}));
  const e44 = E.salles[3].enigmes[3], lettres = carte.querySelectorAll("[data-l]"), slots = carte.querySelectorAll("button.slot");
  ok(slots.length === e44.commun.cible.length && lettres.length > slots.length, `Lettres : ${slots.length} cases, ${lettres.length} lettres dont ${lettres.length - slots.length} leurres`);
  clic4(lettres[0]);
  ok(slots[0].textContent === lettres[0].dataset.l && lettres[0].classList.contains("utilisee"), "Lettres : la lettre cliquée remplit la première case");
  clic4(slots[0]);
  ok(slots[0].textContent === "" && slots[0].classList.contains("vide") && !lettres[0].classList.contains("utilisee"), "Lettres : un clic sur la case la vide");
  clic4(carte.querySelector("[data-valider]"));
  ok(!carte.classList.contains("resolue") && /pas complet/.test(carte.querySelector(".feedback").textContent) && r4.w.ETAT.erreursTotal === 0, "Lettres : mot incomplet refusé sans erreur comptée");
  resoudre(r4.w, e44, "CM2");
  ok(carte.classList.contains("resolue"), "Lettres : l'anagramme VILLAGE valide");
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
    }catch(err){ ok(false, "impression " + type + " : " + err.message); }
  }
  try{ await w.imprimerBilan(); ok(/Le Secret du donjon/.test(doc.body.textContent), "impression du bilan"); }catch(err){ ok(false, "bilan : " + err.message); }
  const tous = [...erreurs, ...r2.erreurs, ...r3.erreurs, ...r4.erreurs];
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
    if(tous || SCEN === "partie-CM1") await partie("CM1", false);
    if(tous || SCEN === "partie-CM2") await partie("CM2", true);
    if(tous || SCEN === "types") await types();
    if(tous || SCEN === "negatifs") await negatifs();
    if(tous || SCEN === "verif") await verif();
    if(tous || SCEN === "verifier") await verifier();
  }catch(e){ echecs++; console.log("  EXCEPTION " + e.stack); }
  console.log(echecs ? `\n${echecs} échec(s)` : "\nTOUT EST VERT");
  process.exit(echecs ? 1 : 0);
})();
