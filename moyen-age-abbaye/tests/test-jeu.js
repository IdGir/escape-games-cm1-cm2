/* ============================================================
   TESTS AUTOMATIQUES — Le Manuscrit de l'abbaye (Node + jsdom)
   ------------------------------------------------------------
   Lancement, depuis la racine du dépôt :
       npm install jsdom          (une seule fois, hors dépôt)
       node moyen-age-abbaye/tests/test-jeu.js
   Moteur d'énigmes v2 (outils-moteur/enigmes.js) : chaque énigme se
   valide par un bouton « Vérifier » ; une erreur n'indique que le
   NOMBRE de réponses justes, sans marquer bien/mal ; aucune
   correction après la réussite ; 10 points du premier coup, 3 après
   erreur ; coffre final où l'on retape les 5 mots-clés, puis fermoir.
   Vérifie : données JSON, leçons, partie CM1 sans faute (195 points =
   scoreMax()), partie CM2 avec une erreur, un coffre raté et un
   fermoir raté (245 − 21), mots-clés « Notez ce mot », coffre final,
   fermoir, indices (−2 points), chaque énigme en mode vérification
   (erreur puis 3 points), tri, réglages, impressions.
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

/* ---------- Solveurs : résolvent l'énigme affichée par l'interface ----------
   Moteur d'énigmes v2 : chaque type se valide par le bouton [data-valider]
   (calqué sur le solveur de outils-moteur/tester_parties.py). Avec
   faux = true, la réponse composée contient volontairement une erreur. */
function clic(el){ el.dispatchEvent(new el.ownerDocument.defaultView.MouseEvent("click", { bubbles:true })); }
const norm = s => String(s||"").trim().toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g,"").replace(/[^a-z0-9]/g,"");
function donneesNiv(w, e){ const n = w.ETAT.niveau.toLowerCase(); return e[n] || e.commun || e.cm2 || e.cm1; }
function resoudre(w, e, carte, faux = false){
  const d = donneesNiv(w, e), q = s => carte.querySelector(s), qa = s => [...carte.querySelectorAll(s)];
  // remise à zéro d'une tentative précédente (comme le ferait un élève)
  qa(".slots-lettres .slot.ok").forEach(clic);
  qa(".trou[data-pose], .plan-case[data-pose]").forEach(clic);
  switch(e.type){
    case "qcm":
      d.questions.forEach((x, i) => clic(q(`.qcm-question[data-i="${i}"] .qcm-option[data-j="${faux && i === 0 ? (x.bonne + 1) % x.options.length : x.bonne}"]`)));
      break;
    case "vraifaux":
      d.affirmations.forEach((a, i) => clic(q(`.vf-ligne[data-i="${i}"] .vf-btn[data-rep="${(faux && i === 0 ? !a.vrai : !!a.vrai) ? "vrai" : "faux"}"]`)));
      break;
    case "association": {
      // on apparie gauche → droite (même numéro de paire), rien n'est corrigé avant « Vérifier »
      const g = qa('[data-col="g"] .carte-match');
      g.forEach((c, i) => { clic(c); clic(q(`[data-col="d"] .carte-match[data-id="${faux && g.length > 1 ? g[(i + 1) % g.length].dataset.bon : c.dataset.bon}"]`)); });
      break;
    }
    case "ordre": {
      const liste = q(".liste-ordre");
      for(let r = 1; r <= d.items.length; r++){
        const it = liste.querySelector(`.item-ordre[data-rang="${r}"]`);
        while([...liste.children].indexOf(it) > r - 1) clic(it.querySelector(".btn-monter"));
      }
      if(faux) clic(liste.children[0].querySelector(".btn-descendre"));
      break;
    }
    case "tri": {
      // clic sur une carte, puis sur une colonne
      const cols = qa(".tri-colonne");
      qa(".carte-tri").forEach((c, i) => {
        let col = c.dataset.col;
        if(faux && i === 0) col = (cols.find(k => k.dataset.col !== col) || cols[0]).dataset.col;
        clic(c); clic(q(`.tri-colonne[data-col="${col}"] .tri-zone`));
      });
      break;
    }
    case "trous": case "plan": {
      const cibles = qa(e.type === "trous" ? ".trou" : ".plan-case");
      const reps = cibles.map(c => c.dataset.rep);
      if(faux && reps.length > 1) [reps[0], reps[1]] = [reps[1], reps[0]];
      cibles.forEach((c, i) => { clic(qa(".etiquette:not(.posee)").find(x => norm(x.dataset.mot) === norm(reps[i]))); clic(c); });
      break;
    }
    case "lettres": {
      // anagramme : les lettres [data-l] cliquées remplissent les cases (des leurres existent)
      let cible = d.cible.slice();
      if(faux){
        [cible[0], cible[cible.length - 1]] = [cible[cible.length - 1], cible[0]];
        if(norm(cible.join("")) === norm(d.cible.join(""))) cible.reverse();
      }
      cible.forEach(l => clic(qa("[data-l]:not(.utilisee)").find(x => norm(x.dataset.l) === norm(l))));
      break;
    }
    case "code":
      d.champs.forEach((c, i) => { q(`#code-${i}`).value = faux && i === 0 ? "0" : c.valeur; });
      break;
    case "intrus":
      // sélection, puis « C'est l'intrus ! »
      clic(q(`.carte-intrus[data-intrus="${faux ? 0 : 1}"]`));
      break;
    default: throw new Error("type inconnu " + e.type);
  }
  clic(q("[data-valider]"));
}
const texteSansBalises = s => String(s||"").replace(/<[^>]*>/g, " ").replace(/\s+/g, " ").trim();
/* Débuts des textes de correction / explication d'une énigme. */
function textesCorrection(e){
  const t = [];
  const parcourir = o => { if(o && typeof o === "object") Object.entries(o).forEach(([k, v]) => {
    if(/^(correction|explication)$/.test(k)) [].concat(typeof v === "object" && v ? Object.values(v) : v).forEach(x => typeof x === "string" && t.push(texteSansBalises(x)));
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
  ok(!carte.classList.contains("resolue"), `${etiquette} (${e.type}) : mauvaise réponse refusée`);
  ok(/Pas tout juste/.test(fb) && (e.type === "intrus" ? /Ce n'est pas l'intrus/.test(fb) : /\b\d+ [^.]+ sur \d+\./.test(fb)),
     `${etiquette} (${e.type}) : message « N … sur M » attendu, obtenu « ${fb.replace(/\s+/g, " ").slice(0, 90)} »`);
  ok(!carte.querySelector(".bien, .mal, .correct, .incorrect"), `${etiquette} (${e.type}) : des éléments sont marqués bien/mal`);
}
/* Après la réussite : les points, et aucune correction, explication ni source. */
function controlerReussite(carte, e, pts, etiquette){
  const fb = carte.querySelector("#fb-" + e.id).textContent;
  ok(fb.includes("+" + pts + " points") && (pts === 10) === /Tout juste du premier coup/.test(fb), `${etiquette} : « +${pts} points » attendu, obtenu « ${fb.slice(0, 80)} »`);
  const copie = carte.cloneNode(true);
  copie.querySelectorAll(".barre-outils, .consigne").forEach(x => x.remove());   // la source figure dès le début dans la barre d'outils
  const txt = copie.textContent.replace(/\s+/g, " ");
  const fuite = textesCorrection(e).find(x => txt.includes(x));
  ok(!carte.querySelector(".correction, .source-correction, .explication") && !fuite && !(e.source && fb.includes(e.source)),
     `${etiquette} : aucune correction affichée après la réussite` + (fuite ? " (trouvé : « " + fuite + " »)" : ""));
}
const bareme = w => w.eval("({premier:PTS_PREMIER_COUP, apres:PTS_APRES_ERREUR, rapidite:PTS_RAPIDITE, quiz:PTS_QUIZ, nbQuiz:NB_QUIZ, malus:MALUS_INDICE, coffre:PTS_COFFRE_PREMIER, coffreApres:PTS_COFFRE_APRES})");

/* ---------- 3. Partie complète ----------
   avecErreurs : la première énigme, le coffre final et le fermoir sont
   d'abord ratés (3 points au lieu de 10 pour chacun). */
async function partie(niveau, { indiceSalle = 0, avecErreurs = false } = {}){
  const { w, erreurs } = await ouvrir("", { escape_reglages_moyenage: REGLAGES_TEST });
  const doc = w.document;
  clic(doc.querySelector(`.opt-niveau[data-niveau="${niveau}"]`));
  const inp = doc.getElementById("input-equipe");
  inp.value = "Les Testeurs"; inp.dispatchEvent(new w.Event("input"));
  ok(!doc.getElementById("btn-demarrer").disabled, "bouton de départ actif");
  clic(doc.getElementById("btn-demarrer"));
  const B = bareme(w);
  let indicesPris = 0, total = 0;
  for(let s = 1; s <= 5; s++){
    await attendre(() => w.ETAT.salle === s && doc.querySelector("#zone-enigme .enigme-carte"), 8000, `salle ${s}`);
    const liste = w.salleEnigmes(s);
    for(let k = 0; k < liste.length; k++){
      const e = liste[k];
      await attendre(() => doc.getElementById("enigme-" + e.id), 8000, "énigme " + e.id);
      const c2 = doc.getElementById("enigme-" + e.id);
      if(indiceSalle === s && k === 0){
        const avant = w.ETAT.score;
        clic(c2.querySelector("#indice-" + e.id));
        ok(w.ETAT.score === Math.max(0, avant - 2), "un indice retire 2 points");
        ok(c2.querySelector(".feedback.indice"), "l'indice s'affiche");
        indicesPris++;
      }
      const avant = w.ETAT.score, premiere = avecErreurs && total === 0;
      if(premiere){ resoudre(w, e, c2, true); controlerErreur(c2, e, e.id); }
      resoudre(w, e, c2);
      await attendre(() => c2.classList.contains("resolue"), 3000, "résolution " + e.id);
      const pts = premiere ? B.apres : B.premier;
      controlerReussite(c2, e, pts, e.id);
      total++;
      if(k < liste.length - 1){
        await attendre(() => doc.getElementById("btn-enigme-suivante"), 4000, "bouton énigme suivante");
        ok(w.ETAT.score - avant === pts, `${e.id} : +${pts} points au score (obtenu ${w.ETAT.score - avant})`);
        clic(doc.getElementById("btn-enigme-suivante"));
      }
    }
    // fin de page : plus de dialogue de réussite, le bouton suivant apparaît tout de suite
    const id = s < 5 ? "btn-salle-suivante" : "btn-coffre-final";
    await attendre(() => doc.getElementById(id), 2500, "bouton " + id + " après la page " + s);
    const zone = doc.getElementById("zone-enigme").textContent;
    ok(w.ETAT.motsCles.includes(DI.salles[s-1].motCle) && zone.includes(DI.salles[s-1].motCle) && /Notez ce mot/.test(zone), `mot-clé ${DI.salles[s-1].motCle} affiché avec « Notez ce mot »`);
    clic(doc.getElementById(id));
    await pause(100);
    ok(!doc.querySelector(".mot-cle"), `page ${s} : le mot-clé n'est plus affiché ensuite`);
  }
  /* Coffre final : les 5 mots sont à retaper, rien n'est prérempli */
  await attendre(() => doc.getElementById("coffre-final"), 4000, "coffre final");
  const champs = DI.salles.map((x, i) => doc.getElementById("coffre-" + i));
  ok(champs.every(c => c && c.value === ""), "coffre final : les 5 champs sont vides");
  ok(!DI.salles.some(x => doc.getElementById("coffre-final").textContent.includes(x.motCle)), "coffre final : aucun mot-clé affiché");
  if(avecErreurs){
    champs.forEach((c, i) => c.value = i === 0 ? "gaulois" : DI.salles[i].motCle);
    clic(doc.getElementById("btn-coffre"));
    ok(!w.ETAT.coffreOuvert && /4 mots justes sur 5/.test(doc.getElementById("fb-coffre").textContent), "coffre final : un mot faux est refusé (« 4 mots justes sur 5 »)");
  }
  const avantCoffre = w.ETAT.score;
  champs.forEach((c, i) => c.value = norm(DI.salles[i].motCle));   // minuscules, sans accent (CHARITÉ → charite)
  clic(doc.getElementById("btn-coffre"));
  ok(w.ETAT.coffreOuvert, "coffre final : s'ouvre avec les bons mots (accents et casse ignorés)");
  ok(w.ETAT.score - avantCoffre === (avecErreurs ? B.coffreApres : B.coffre), `coffre final : +${avecErreurs ? B.coffreApres : B.coffre} points`);
  /* Mécanisme final : le fermoir (frise) */
  await attendre(() => doc.getElementById("enigme-final"), 8000, "fermoir");
  ok(w.ETAT.motsCles.length === 5, "5 mots-clés");
  ok(doc.querySelectorAll(".incipit .mot-incipit").length === 5, "l'incipit affiche les 5 mots");
  const fin = w.ENIGMES().final, cf = doc.getElementById("enigme-final");
  const avantFermoir = w.ETAT.score;
  if(avecErreurs){ resoudre(w, fin, cf, true); controlerErreur(cf, fin, "fermoir"); }
  resoudre(w, fin, cf);
  await attendre(() => cf.classList.contains("resolue"), 3000, "résolution du fermoir");
  controlerReussite(cf, fin, avecErreurs ? B.apres : B.premier, "fermoir");
  await attendre(() => doc.querySelector("#quizz .qcm-question"), 8000, "écran de fin");
  ok(w.ETAT.fermoir === true, "fermoir ouvert");
  ok(w.ETAT.score - avantFermoir === (avecErreurs ? B.apres : B.premier), `fermoir : +${avecErreurs ? B.apres : B.premier} points`);
  /* Quizz final */
  const quizz = w.quizzCourant();
  quizz.forEach((x, i) => clic(doc.querySelector(`#quizz .qcm-question[data-i="${i}"] .qcm-option[data-j="${x.bonne}"]`)));
  clic(doc.getElementById("btn-voir-score"));
  await pause(50);
  // barème v2 : énigmes × 10 + coffre 10 + fermoir 10 + 5 salles × 3 + quizz 5 × 2
  const max = total * B.premier + B.coffre + B.premier + 5 * B.rapidite + B.nbQuiz * B.quiz;
  ok(w.scoreMax() === max && max === (niveau === "CM1" ? 195 : 245), `score maximal ${niveau} = ${w.scoreMax()} (attendu ${max})`);
  const attendu = max - 2*indicesPris - (indicesPris ? 1 : 0)   // indice : −2, et bonus de rapidité 3 → 2
    - (avecErreurs ? (B.premier - B.apres) * 2 + (B.coffre - B.coffreApres) : 0);
  ok(w.ETAT.score === attendu, `score final ${niveau} : ${w.ETAT.score} (attendu ${attendu})`);
  ok(w.ETAT.erreursTotal === (avecErreurs ? 3 : 0) && w.ETAT.enigmesPremierCoup === total - (avecErreurs ? 1 : 0),
     `bilan : ${w.ETAT.erreursTotal} erreur(s), ${w.ETAT.enigmesPremierCoup} énigme(s) du premier coup`);
  ok(doc.getElementById("score-recap").textContent.includes(String(attendu)), "bilan affiché");
  /* Impression du bilan */
  clic(doc.getElementById("btn-imprimer-bilan"));
  ok(w.__imprime >= 1, "impression du bilan");
  ok(erreurs.length === 0, "erreurs JavaScript : " + erreurs.join(" | "));
  w.close();
}

/* Étapes : node test-jeu.js [cm1|cm2|indice|tri|verif|reglages] — sans argument, tout est lancé. */
const ETAPE = process.argv[2] || "tout";
const faire = e => ETAPE === "tout" || ETAPE === e;
(async () => {
  try{
    if(faire("cm1")){ console.log("2. Partie complète CM1");  await partie("CM1"); }
    if(faire("cm2")){ console.log("3. Partie complète CM2 (une erreur, coffre et fermoir ratés une fois)");  await partie("CM2", { avecErreurs: true }); }
    if(faire("indice")){ console.log("4. Indice en salle 2 (CM2)"); await partie("CM2", { indiceSalle: 2 }); }
    if(faire("verif")){
    console.log("5. Chaque énigme en mode vérification : erreur « N … sur M », puis résolution à 3 points");
    for(const s of E.salles) for(const e of s.enigmes){
      const niv = (!e.niveaux || e.niveaux.includes("CM1")) ? "CM1" : "CM2";
      const { w, erreurs } = await ouvrir(`?salle=${s.num}&niveau=${niv}&enigme=${w_rang(e, s, niv)}`, { escape_reglages_moyenage: REGLAGES_TEST });
      await attendre(() => w.document.getElementById("enigme-" + e.id), 6000, "vérif " + e.id);
      const carte = w.document.getElementById("enigme-" + e.id);
      const B = bareme(w);
      // une réponse incomplète n'est pas une erreur (l'ordre, lui, est toujours complet : on ne le valide pas au hasard)
      if(e.type !== "ordre"){
        clic(carte.querySelector("[data-valider]"));
        ok(!carte.classList.contains("resolue") && w.ETAT.erreursTotal === 0, `${e.id} (${e.type}) : une réponse incomplète ne compte pas comme erreur`);
      }
      const errAvant = w.ETAT.erreursTotal;
      resoudre(w, e, carte, true);
      await pause(30);
      controlerErreur(carte, e, e.id);
      ok(w.ETAT.erreursTotal === errAvant + 1, `${e.id} (${e.type}) : une erreur comptée`);
      resoudre(w, e, carte);
      await attendre(() => carte.classList.contains("resolue"), 3000, "résolution " + e.id);
      controlerReussite(carte, e, B.apres, e.id);
      await attendre(() => w.ETAT.enigmesReussies === 1, 2000, "points de " + e.id);
      ok(w.ETAT.score === B.apres, `${e.id} : ${B.apres} points après une erreur (score ${w.ETAT.score})`);
      ok(w.localStorage.getItem("escape_moyenage_v1") === null, `${e.id} : le mode vérification ne sauvegarde rien`);
      ok(erreurs.length === 0, `${e.id} : erreurs JavaScript : ` + erreurs.join(" | "));
      w.close();
    }
    }
    if(faire("tri")){
      console.log("5 bis. Tri : déposer dans une colonne déjà remplie");
      const { w } = await ouvrir("?salle=5&niveau=CM1&enigme=3", { escape_reglages_moyenage: REGLAGES_TEST });
      await attendre(() => w.document.getElementById("enigme-5-3"), 6000, "énigme 5-3");
      const carte = w.document.getElementById("enigme-5-3");
      const q = s => carte.querySelector(s), qa = s => [...carte.querySelectorAll(s)];
      const colRoman = qa(".tri-colonne").find(c => c.dataset.col === "roman");
      const premiere = qa(".tri-reserve .carte-tri")[0];
      clic(premiere); clic(colRoman.querySelector(".tri-titre"));      // clic sur le titre de la colonne
      ok(colRoman.querySelector(".tri-zone").contains(premiere), "un clic sur le titre de la colonne dépose la carte");
      const seconde = qa(".tri-reserve .carte-tri")[0];
      clic(seconde); clic(premiere);                                   // clic sur une carte déjà posée
      ok(colRoman.querySelector(".tri-zone").contains(seconde), "on peut déposer sur une colonne déjà remplie");
      ok(qa(".tri-reserve .carte-tri").length === qa(".carte-tri").length - 2, "les deux cartes ont quitté la réserve");
      clic(premiere);                                                  // rien de choisi : on la reprend
      clic(q(".tri-reserve"));
      ok(q(".tri-reserve").contains(premiere), "on peut renvoyer une carte dans la réserve");
      w.close();
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
