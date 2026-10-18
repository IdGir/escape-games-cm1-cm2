/* ============================================================
   TESTS DES OUTILS COMMUNS DANS LES VARIANTES IMMERSIVES (Node + jsdom)
   Depuis la racine du dépôt :  node commun/tests/test-immersif-greffons.js [étapes]
   Étapes : charge, joker, pouce, alerte, difficulte, correction, progression, mascotte, trophees, prof
   Les variantes immersives (immersifs/<jeu>/) ont leur propre moteur (VML) ; les outils des jeux
   classiques y sont portés par commun/js/immersif/vml-*.js et les modules communs rendus agnostiques.
   ============================================================ */
const fs = require("fs"), path = require("path");
const { charger, compteur, dodo, attendreQue, clic, RACINE } = require("../../outils-tests/charge");
const T = compteur("Outils communs dans les variantes immersives"); const ok = T.ok;
const J = j => path.join(RACINE, "immersifs", j);
const IMM = ["alimentation", "chateau-fort", "constitution", "lumiere", "melanges", "moyen-age-abbaye", "objets-techniques", "renaissance", "station-meteo", "versailles"];
const avant = w => { w.VML_RAPIDE = true; };
const SECTIONS = {};
const donnees = j => JSON.parse(fs.readFileSync(path.join(J(j), "assets/data/enigmes.json"), "utf8"));
const cliquer = (w, el) => el && el.dispatchEvent(new w.MouseEvent("click", { bubbles: true }));

/** Ouvre le jeu en mode vérification sur une énigme, puis le panneau de l'énigme. */
async function ouvrirEnigme(j, escale, grade, num, extra, stockage){
  const q = `?verif=1&escale=${escale}&niveau=${grade}&enigme=${num}${extra || ""}`;
  const r = await charger(J(j), q, { avant, attente: 500, stockage });
  const w = r.w, d = w.document;
  const es = w.VML.escale(escale), e = es.enigmes[num - 1];
  await attendreQue(() => d.querySelector(`#scene-jeu .zone.cible[data-zone="${e.objet_principal}"]`), 4000);
  clic(w, d.querySelector(`.zone[data-zone="${e.objet_principal}"]`));
  await attendreQue(() => d.getElementById("enigme-" + e.id), 3000);
  return Object.assign(r, { e, carte: d.getElementById("enigme-" + e.id) });
}

SECTIONS.charge = async () => {
  console.log("\n== Chargement : les 10 variantes ==");
  for (const j of IMM) {
    const html = fs.readFileSync(path.join(J(j), "index.html"), "utf8");
    const scripts = [...html.matchAll(/<script src="([^"]+)"/g)].map(m => m[1].split("?")[0]);
    const ordre = ["js/app.js", "../../commun/js/immersif/vml-suivi.js", "../../commun/js/immersif/vml-joker.js", "../../commun/js/immersif/vml-pouce.js", "../../commun/js/immersif/vml-difficulte.js", "../../commun/js/immersif/vml-correction.js", "../../commun/js/correction-collective.js", "../../commun/js/mascotte.js"];
    const pos = ordre.map(s => scripts.indexOf(s));
    ok(pos.every((p, i) => p >= 0 && (!i || p > pos[i - 1])), `${j} : outils communs chargés après le moteur, dans l'ordre`);
    const r = await charger(J(j), "", { avant, attente: 600 });
    ok(r.erreurs.length === 0, `${j} : accueil sans erreur JS ${r.erreurs.join(" | ")}`);
    ok(typeof r.w.VML.detailEnigmes === "function" && typeof r.w.VML.coupDePouce === "function" && !!r.w.AIDES_ENIGMES && !!r.w.DIFFICULTE_VML && !!r.w.CORRECTION_ADAPTATEUR && !!r.w.PROGRESSION && !!r.w.MASCOTTE, `${j} : suivi, coup de pouce, difficulté, correction, progression, mascotte présents`);
  }
};

SECTIONS.joker = async () => {
  console.log("\n== N15 : joker (immersif) ==");
  for (const j of ["renaissance", "melanges"]) {
    const { w, erreurs, e, carte } = await ouvrirEnigme(j, 1, "matelot", 1);
    const d = w.document, E = w.VML.ETAT;
    const b = carte.querySelector(".btn-joker");
    ok(b && /1 restant/.test(b.textContent), `${j} : bouton « 🃏 Joker (1 restant) » dans le panneau (${b && b.textContent})`);
    const score = E.score;
    cliquer(w, b); await dodo(250);
    const r = E.resolues[e.id];
    ok(r && r.passee === true && r.pts === 0 && r.premier === false, `${j} : énigme passée, 0 point, pas du premier coup`);
    ok(E.score === score, `${j} : score inchangé (${E.score})`);
    ok(/Joker utilisé/.test(carte.querySelector("#fb-" + e.id).textContent) || !d.getElementById("enigme-" + e.id), `${j} : message de joker`);
    await attendreQue(() => !d.getElementById("panneau-enigme").classList.contains("ouvert"), 3000);
    const det = w.VML.detailEnigmes().find(n => n.id === e.id);
    ok(det && det.p === 1 && det.ok === 0 && det.pc === 0, `${j} : détail « passée » (${JSON.stringify(det)})`);
    const cr = w.VML.compteRendu();
    ok(cr.passees === 1 && Array.isArray(cr.detail) && /^[0-9A-F]{4}-[0-9A-F]{4}$/.test(cr.code), `${j} : compte-rendu « 1 passée », code de contrôle`);
    // l'énigme suivante : plus de joker
    await attendreQue(() => w.VML.ETAT.indexEnigme === 1, 4000);
    const es = w.VML.escale(1), e2 = es.enigmes[1];
    await attendreQue(() => d.querySelector(`#scene-jeu .zone.cible[data-zone="${e2.objet_principal}"]`), 5000);
    clic(w, d.querySelector(`.zone[data-zone="${e2.objet_principal}"]`));
    await attendreQue(() => d.getElementById("enigme-" + e2.id), 3000);
    const b2 = d.getElementById("enigme-" + e2.id).querySelector(".btn-joker");
    ok(b2 && b2.disabled && /utilisé/.test(b2.textContent), `${j} : plus de joker pour la suite (${b2 && b2.textContent})`);
    ok(erreurs.length === 0, `${j} : erreurs JS ${erreurs.join(" | ")}`);
  }
  // désactivé, par escale, réglage ⚙️
  const off = await ouvrirEnigme("melanges", 1, "matelot", 1, "&joker=0");
  ok(!off.carte.querySelector(".btn-joker"), "?joker=0 : aucun bouton");
  const r = await charger(J("melanges"), "?verif=1&escale=1&niveau=matelot&enigme=1", { avant, attente: 500 });
  r.w.VML.ouvrirReglages(); await dodo(100);
  const sel = r.w.document.getElementById("reg-joker");
  ok(!!sel, "réglage « 🃏 Joker » dans ⚙️ (volet enseignant)");
  if (sel) { sel.value = "salle"; sel.dispatchEvent(new r.w.Event("change")); ok(JSON.parse(r.w.localStorage.getItem("escape_joker")).mode === "salle", "réglage « 1 par escale » gardé"); }
  // une escale avec joker : pas de bonus d'escale
  const f = await ouvrirEnigme("melanges", 1, "matelot", 1);
  const E = f.w.VML.ETAT, es = f.w.VML.escale(1);
  cliquer(f.w, f.carte.querySelector(".btn-joker")); await dodo(200);
  es.enigmes.slice(1).forEach(x => { E.resolues[x.id] = { pts: 10, bienDoc: 0, erreurs: 0, indices: 0, fiches: [], ms: 1000, premier: true }; });
  E.score = 30; E.indicesEscale = 0; E.msEcoules = 60000; E.indexEnigme = es.enigmes.length;
  f.w.VML.modeVerif = false;
  E.escaleTerminee = true; E.bonus = { maitreNageur: 5, rapidite: 5 }; E.bonusEscales = { 1: { maitreNageur: 5, rapidite: 5 } }; E.score += 10;
  f.w.VML.memoriserCompteRendu();
  ok(E.score === 30 && !E.bonus.maitreNageur && !E.bonus.rapidite, `escale avec joker : bonus d'escale retirés (score ${E.score})`);
};

SECTIONS.pouce = async () => {
  console.log("\n== N13 : coup de pouce (immersif) ==");
  // première énigme de chaque type, tous jeux et grades confondus
  const trouve = {};
  for (const j of IMM) {
    const D = donnees(j);
    D.escales.forEach(es => es.enigmes.forEach((e, k) => ["timonier", "matelot"].forEach(g => {
      const b = e[g]; if (!b) return;
      const t = b.type || e.type;
      if (!trouve[t]) trouve[t] = { j, escale: es.numero, num: k + 1, g, id: e.id };
    })));
  }
  console.log("  types couverts : " + Object.keys(trouve).join(", "));
  for (const [type, t] of Object.entries(trouve)) {
    if (type === "circuit") continue;                      // type propre aux variantes : repli sur un indice offert, testé plus bas
    const { w, erreurs, e, carte } = await ouvrirEnigme(t.j, t.escale, t.g, t.num);
    ok(!!carte, `${type} (${t.j} ${t.id}) : énigme ouverte`);
    if (!carte) continue;
    const res = w.VML.coupDePouce(0);
    ok(res && res.ok === true, `${type} : coup de pouce appliqué (${res && res.texte})`);
    ok(!carte.classList.contains("resolue"), `${type} : l'énigme n'est pas résolue pour autant`);
    ok(w.VML.etatEnigme(e.id).pouces === 1, `${type} : trace (pouces = 1)`);
    for (let i = 0; i < 6; i++) w.VML.coupDePouce(0);
    ok(!carte.classList.contains("resolue") && erreurs.length === 0, `${type} : plusieurs coups de pouce de suite sans résoudre ni erreur JS ${erreurs.join(" | ")}`);
  }
  // coût, trace dans le détail et le compte-rendu, commande de la synchronisation
  const { w, e, carte } = await ouvrirEnigme("renaissance", 1, "timonier", 1);
  w.VML.ETAT.score = 20;
  w.VML.traiterCommande({ pouce: true, cout: 2, id: 1 });
  ok(w.VML.ETAT.score === 18, `commande {pouce, cout:2} reçue : −2 points (${w.VML.ETAT.score})`);
  const cr = w.VML.compteRendu();
  ok(cr.pouces >= 1 && cr.detail.find(n => n.id === e.id).c >= 1, "compte-rendu : coups de pouce notés");
  ok(w.VML.payloadEtat().pouces >= 1, "prof.html : « pouces » dans l'état envoyé");
  // en attente : aucune énigme ouverte
  const r = await charger(J("renaissance"), "?verif=1&escale=1&niveau=timonier&enigme=1", { avant, attente: 500 });
  const rr = r.w.VML.coupDePouce(0);
  ok(rr && rr.attente === true && !!r.w.VML.ETAT.poucePending, "aucune énigme ouverte : le coup de pouce attend");
  const es = r.w.VML.escale(1), e1 = es.enigmes[0];
  await attendreQue(() => r.w.document.querySelector(`#scene-jeu .zone.cible[data-zone="${e1.objet_principal}"]`), 4000);
  clic(r.w, r.w.document.querySelector(`.zone[data-zone="${e1.objet_principal}"]`));
  await dodo(700);
  ok(!r.w.VML.ETAT.poucePending && r.w.VML.etatEnigme(e1.id).pouces >= 1, "à l'ouverture de l'énigme, le coup de pouce en attente s'applique");
  // coffre : première lettre
  const c = await charger(J("renaissance"), "?verif=1&coffre=1&niveau=timonier", { avant, attente: 600 });
  const rc = c.w.VML.coupDePouce(0);
  const inp = c.w.document.querySelector(".coffre-case input");
  ok(rc && rc.ok && inp && /\(\d+ lettres\)/.test(inp.placeholder), `coffre final : première lettre et longueur (« ${inp && inp.placeholder} »)`);
};

SECTIONS.alerte = async () => {
  console.log("\n== N19 : alerte de fin de séance (immersif) ==");
  const { w, erreurs } = await ouvrirEnigme("melanges", 1, "matelot", 1);
  const E = w.VML.ETAT, avantEtat = { score: E.score, idx: E.indexEnigme, ms: E.msEcoules };
  w.VML.traiterCommande({ finSeance: { min: 5, id: 1 } }); await dodo(60);
  const b = w.document.getElementById("alerte-seance");
  ok(b && b.classList.contains("visible") && /Fin de la séance dans 5 min/.test(b.textContent), "bandeau « Fin de la séance dans 5 min »");
  ok(E.score === avantEtat.score && E.indexEnigme === avantEtat.idx && !E.enPause, "score, énigme et chrono intacts, énigme non interrompue");
  ok(w.document.getElementById("panneau-enigme").classList.contains("ouvert"), "le panneau de l'énigme reste ouvert");
  w.VML.traiterCommande({ message: "coucou", t: 5 });
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
};

SECTIONS.difficulte = async () => {
  console.log("\n== N20 : difficulté énigme par énigme (immersif) ==");
  const D = donnees("renaissance"), e11 = D.escales[0].enigmes[0], G = D.niveaux.map(n => n.id);
  const nb = g => JSON.stringify(e11[g]).length;
  let r = await ouvrirEnigme("renaissance", 1, "timonier", 1);
  ok(r.carte.dataset.gradeEnigme === "timonier" && !r.carte.querySelector(".badge-difficulte"), "sans réglage : grade de l'équipe, pas de pastille");
  r = await ouvrirEnigme("renaissance", 1, "timonier", 1, `&dif=${e11.id}:+1`);
  ok(r.carte.dataset.gradeEnigme === "lieutenant" && r.w.VML.ETAT.niveau === "timonier", `timonier + 1 : énigme jouée au grade lieutenant, grade de l'équipe inchangé (${r.carte.dataset.gradeEnigme})`);
  ok(/plus difficile/.test(r.carte.querySelector(".badge-difficulte").textContent), "pastille « Réglée plus difficile »");
  ok(!!r.carte.querySelector(".justif"), "grade lieutenant : la justification est demandée");
  r = await ouvrirEnigme("renaissance", 1, "timonier", 1, `&dif=${e11.id}:-2`);
  ok(r.carte.dataset.gradeEnigme === "mousse" && /Aide renforcée/.test(r.carte.querySelector(".badge-difficulte").textContent), "timonier − 2 : grade mousse, pastille « Aide renforcée »");
  const bi = r.carte.querySelector("[data-indice]");
  ok(bi && /offert/.test(bi.textContent), "aide renforcée : « Indice offert » sur le bouton");
  r.w.VML.ETAT.score = 10; cliquer(r.w, bi); await dodo(50);
  ok(!!r.carte.querySelector(".indices-donnes .feedback.indice") && r.w.VML.ETAT.score === 10 && r.w.VML.ETAT.indicesTotal === 0, "premier indice offert : aucun point retiré");
  r = await ouvrirEnigme("renaissance", 1, "second", 1, `&dif=${e11.id}:+2`);
  ok(r.carte.dataset.gradeEnigme === "second", "plafond : le grade le plus haut ne dépasse pas");
  r = await ouvrirEnigme("renaissance", 1, "mousse", 1, `&dif=${e11.id}:-2`);
  ok(r.carte.dataset.gradeEnigme === "mousse", "plancher : le grade le plus bas ne descend pas");
  // réglage de l'enseignant sur l'appareil (clé propre à la variante immersive)
  r = await ouvrirEnigme("renaissance", 1, "timonier", 1, "", { escape_difficulte_immersif_renaissance: "{}", "escape_difficulte_immersif-renaissance": JSON.stringify({ [e11.id]: -1 }) });
  ok(r.carte.dataset.gradeEnigme === "matelot", "réglage de l'enseignant (appareil) : pris en compte");
  // la clé n'est pas celle de la version classique
  r = await ouvrirEnigme("renaissance", 1, "timonier", 1, "", { escape_difficulte_renaissance: JSON.stringify({ [e11.id]: 2 }) });
  ok(r.carte.dataset.gradeEnigme === "timonier", "les réglages de la version classique ne s'appliquent pas à la variante immersive");
  ok(r.erreurs.length === 0, "erreurs JS : " + r.erreurs.join(" | "));
};

SECTIONS.correction = async () => {
  console.log("\n== D7 : correction collective (immersif) ==");
  for (const j of ["renaissance", "melanges"]) {
    const { w, erreurs } = await charger(J(j), "?correction=1&niveau=timonier", { avant, attente: 700 });
    const d = w.document;
    const el = await attendreQue(() => d.getElementById("correction-collective"), 5000);
    ok(!!el, `${j} : ?correction=1 ouvre la correction collective`);
    if (!el) continue;
    const D = donnees(j), es1 = D.escales[0];
    ok(el.querySelectorAll(".cc-enigme").length === es1.enigmes.length, `${j} : escale 1, ${es1.enigmes.length} énigmes listées`);
    ok([...el.querySelectorAll(".cc-reponse")].every(x => x.hidden), `${j} : réponses cachées au départ`);
    d.dispatchEvent(new w.KeyboardEvent("keydown", { key: "t", bubbles: true }));
    ok(!/undefined|\[object|NaN/.test(el.textContent) && el.querySelectorAll(".cc-rep, .cc-lettre").length > 0, `${j} : réponses lisibles`);
    ok(el.querySelector(".cc-mot-serrure").textContent.trim() === es1.mot, `${j} : mot de l'escale affiché (« ${es1.mot} »)`);
    ok([...el.querySelectorAll(".cc-niv option")].map(o => o.value).join() === D.niveaux.map(n => n.id).join(), `${j} : les cinq grades proposés`);
    for (let n = 2; n <= D.escales.length; n++) {
      d.dispatchEvent(new w.KeyboardEvent("keydown", { key: "ArrowRight", bubbles: true }));
      d.dispatchEvent(new w.KeyboardEvent("keydown", { key: "t", bubbles: true }));
      ok(el.querySelectorAll(".cc-enigme").length > 0 && !/undefined|\[object|NaN/.test(el.textContent), `${j} : escale ${n} lisible`);
    }
    const sel = el.querySelector(".cc-niv"); sel.value = "lieutenant"; sel.dispatchEvent(new w.Event("change"));
    d.dispatchEvent(new w.KeyboardEvent("keydown", { key: "t", bubbles: true }));
    ok(/Justification/.test(el.textContent), `${j} : grade lieutenant : justification affichée`);
    ok(erreurs.length === 0, `${j} : erreurs JS ${erreurs.join(" | ")}`);
  }
  // bouton à l'écran de fin d'escale
  const { w } = await charger(J("melanges"), "?verif=1&escale=1&niveau=timonier&enigme=1&fin=1", { avant, attente: 700 });
  await dodo(200);
  ok(!!w.document.getElementById("btn-correction-collective"), "écran de fin d'escale : bouton « Correction collective »");
};

SECTIONS.progression = async () => {
  console.log("\n== N16 : progression (immersif) ==");
  const parties = JSON.stringify([{ type: "escape-game-compte-rendu", jeu: "melanges", eleve: "Les Lynx", mode: "equipe", date: "2026-10-12T10:00", partie: "2026-10-12T09:00", termine: true, score: 100, scoreMax: 235, total: 20, premierCoup: 9, indices: 1 }]);
  const { w, erreurs } = await charger(J("melanges"), "", { avant, attente: 700, stockage: { escape_resultats: parties } });
  const d = w.document;
  const b = d.getElementById("btn-progression");
  ok(!!b && /Ma progression/.test(b.textContent), "accueil : bouton « 🎓 Ma progression »");
  d.getElementById("nom-equipe").value = "Les Lynx"; b.click();
  const pan = d.getElementById("panneau-progression");
  ok(!!pan && pan.querySelector("#prog-nom").value === "Les Lynx", "panneau : nom d'équipe repris");
  pan.querySelector("#prog-code").click(); await dodo(200);
  const code = pan.querySelector("#prog-code-texte").value;
  ok(/^EGP1/.test(code), "code court obtenu");
  const r2 = await charger(J("renaissance"), "", { avant, attente: 600 });
  r2.w.document.getElementById("btn-progression").click();
  r2.w.document.getElementById("prog-coller").value = code; r2.w.document.getElementById("prog-importer").click(); await dodo(300);
  ok(JSON.parse(r2.w.localStorage.getItem("escape_resultats")).length === 1, "autre appareil : partie retrouvée par le code");
  ok(erreurs.length === 0 && r2.erreurs.length === 0, "erreurs JS " + erreurs.concat(r2.erreurs).join(" | "));
};

SECTIONS.mascotte = async () => {
  console.log("\n== N11 : mascotte (immersif) ==");
  const parole = w => { avant(w); w.__dit = []; w.speechSynthesis = { speak(u){ w.__dit.push(u.text); w.__u = u; }, cancel(){ w.__annule = (w.__annule || 0) + 1; }, getVoices(){ return []; } }; w.SpeechSynthesisUtterance = function(t){ this.text = t; }; };
  const { w, erreurs } = await charger(J("melanges"), "", { avant: parole, attente: 800 });
  const d = w.document;
  const bl = d.getElementById("mascotte-bloc");
  ok(!!bl && /Noa/.test(bl.textContent), "accueil : Noa accueille l'équipe");
  ok(bl.compareDocumentPosition(d.getElementById("nom-equipe")) & 4, "placée avant le nom d'équipe");
  const regles = bl.querySelector(".mascotte-regles");
  ok(!regles.hidden && /10 points/.test(regles.textContent) && /20 points/.test(regles.textContent), "premier lancement : règles ouvertes, barème du moteur immersif (10 points, coffre 20 points)");
  ok(bl.querySelector("svg").getAttribute("viewBox") === "0 0 200 320", "portrait 200 × 320");
  bl.querySelector(".mascotte-ecouter").click();
  ok(w.__dit.length === 1, "elle parle sur l'accueil");
  // elle se tait au départ et n'est pas dans le jeu
  d.getElementById("nom-equipe").value = "Les Lynx"; d.getElementById("nom-equipe").dispatchEvent(new w.Event("input"));
  d.querySelector(".carte-grade").click();
  const annul = w.__annule || 0;
  d.getElementById("btn-embarquer").click(); await dodo(300);
  ok(!d.getElementById("mascotte-bloc") && (w.__annule || 0) > annul, "au départ : Noa disparaît, sa voix est coupée");
  ok(JSON.parse(w.localStorage.getItem("escape_mascotte")).vu === true, "premier lancement noté");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
  // réglage ⚙️
  const r = await charger(J("melanges"), "", { avant: parole, attente: 700, stockage: { escape_mascotte: JSON.stringify({ mode: "voix", vu: true }) } });
  ok(/Content de vous revoir/.test(r.w.document.getElementById("mascotte-bloc").textContent), "deuxième visite : texte de retour");
  r.w.VML.ouvrirReglages(); await dodo(100);
  const sel = r.w.document.getElementById("reg-mascotte");
  ok(!!sel, "réglage « 🧑‍🎓 Mascotte » dans ⚙️");
  if (sel) { sel.value = "off"; sel.dispatchEvent(new r.w.Event("change")); ok(!r.w.document.getElementById("mascotte-bloc") && JSON.parse(r.w.localStorage.getItem("escape_mascotte")).mode === "off", "désactivable : Noa masquée, réglage gardé"); }
};

SECTIONS.trophees = async () => {
  console.log("\n== N1 : trophées (immersif) ==");
  const p = (jeu, k) => ({ type: "escape-game-compte-rendu", jeu, eleve: "Les Lynx", termine: true, total: 20, premierCoup: 10, indices: 4, quiz: 3, score: 120, mode: "equipe", date: `2026-10-0${k}T10:00`, partie: `2026-10-0${k}T09:00` });
  const parole = w => { avant(w); w.__dit = []; w.speechSynthesis = { speak(u){ w.__dit.push(u.text); }, cancel(){}, getVoices(){ return []; } }; w.SpeechSynthesisUtterance = function(t){ this.text = t; }; };
  const { w, erreurs } = await charger(J("constitution"), "", { avant: parole, attente: 800, stockage: { escape_resultats: JSON.stringify([p("declaration", 1), p("chateau-fort", 2)]), escape_mascotte: JSON.stringify({ mode: "voix", vu: true }) } });
  const d = w.document;
  d.getElementById("nom-equipe").value = "les lynx"; d.getElementById("nom-equipe").dispatchEvent(new w.Event("input"));
  d.querySelector(".carte-grade").click(); d.getElementById("btn-embarquer").click(); await dodo(500);
  const E = w.VML.ETAT;
  // une escale terminée ne suffit pas à « terminer le jeu »
  E.escaleTerminee = true; E.escalesFaites = [1]; E.mots = ["X"]; w.VML.memoriserCompteRendu();
  const h1 = JSON.parse(w.localStorage.getItem("escape_resultats")).find(x => x.jeu === "constitution");
  ok(h1 && h1.termine === true && h1.coffre === false, "escale terminée : compte-rendu « termine » mais coffre fermé");
  ok(!w.TROPHEES.obtenus("les lynx", JSON.parse(w.localStorage.getItem("escape_resultats")), w.CATALOGUE).some(t => t.id === "citoyen"), "une escale finie ne donne pas encore le trophée « Citoyen »");
  // coffre ouvert : le jeu est terminé
  w.VML.escalesJouables().forEach(n => { if(!E.escalesFaites.includes(n)) E.escalesFaites.push(n); });
  E.coffreOuvert = true; E.fini = true; E.coffre = { erreurs: 0 }; E.score = 140;
  w.VML.memoriserCompteRendu();
  w.VML.ouvrirCoffre(); await dodo(200);
  const bloc = d.getElementById("trophees-fin");
  const nouveaux = bloc ? [...bloc.querySelectorAll(".tr.nouveau b")].map(x => x.textContent).sort() : [];
  ok(nouveaux.includes("Citoyen") && nouveaux.includes("Trois coffres"), `trophées annoncés au coffre ouvert : ${nouveaux.join(", ")}`);
  ok(bloc && bloc.querySelector('a[href="../../trophees.html?nom=les%20lynx"]'), "lien vers la vitrine (../../trophees.html)");
  const m = bloc && bloc.querySelector(".mascotte-trophee");
  ok(!!m && /Bravo ! Vous avez gagné/.test(m.textContent), "la mascotte annonce les trophées");
  m.querySelector(".mascotte-ecouter").click();
  ok(/nouveaux trophées/.test(w.__dit[w.__dit.length - 1]), "annonce lue à voix haute");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
};

SECTIONS.prof = async () => {
  console.log("\n== prof.html des variantes immersives ==");
  for (const j of ["renaissance", "melanges"]) {
    const pr = await charger(J(j), "", { page: "prof.html", attente: 700 });
    const d = pr.w.document;
    pr.w.PROF.equipes = [{ equipe: "Les Lynx", jeu: j, niveau: "timonier", salle: 1, score: 40, enigme: { id: "x", titre: "T", ordre: 1, total: 4, resolues: {} }, pouces: 1, passees: 1, msEcoules: 60000 }];
    pr.w.PROF.dessiner();
    ok(/1 · 1/.test(d.querySelector(".eq").textContent) && /Jokers/.test(d.querySelector(".eq").textContent), `${j} : jokers et coups de pouce affichés sur la carte de l'équipe`);
    ok(!!d.querySelector('.eq [data-c="pouce"]') && !!d.getElementById("cout-pouce") && !!d.getElementById("tout-fin"), `${j} : boutons 🤝, coût, 🔔 fin de séance`);
    ok(!!d.querySelector('a[href="index.html?correction=1"]') && /sequences\/fiche\.html\?jeu=/.test(d.getElementById("lien-sequence").getAttribute("href")), `${j} : correction collective et fiche de séquence`);
    ok(!!d.querySelector(".btn-prof-difficulte"), `${j} : bouton « 🎚️ Difficulté par énigme »`);
    const envoyes = []; const f0 = pr.w.fetch; pr.w.fetch = async (u, o) => { if (o && o.method === "POST" && /api\/commande/.test(u)) { envoyes.push(JSON.parse(o.body)); return { ok: true, json: async () => ({}) }; } return f0(u, o); };
    d.getElementById("cout-pouce").value = "1";
    cliquer(pr.w, d.querySelector('.eq [data-c="pouce"]')); await dodo(50);
    ok(envoyes.length === 1 && envoyes[0].equipe === "Les Lynx" && envoyes[0].commande.pouce === true && envoyes[0].commande.cout === 1, `${j} : commande {pouce, cout:1} envoyée à l'équipe`);
    cliquer(pr.w, d.getElementById("tout-fin")); await dodo(50);
    ok(envoyes.length === 2 && envoyes[1].equipe === "*" && envoyes[1].commande.finSeance.min === 5, `${j} : « fin dans 5 min » envoyé à toutes les équipes`);
    await pr.w.PROF_DIFFICULTE.ouvrir();
    const lignes = d.querySelectorAll("#prof-difficulte tr[data-id]");
    const total = donnees(j).escales.reduce((t, es) => t + es.enigmes.length, 0);
    ok(lignes.length === total && /grade/.test(d.querySelector("#prof-difficulte .pd-corps").textContent), `${j} : ${lignes.length} énigmes listées, légende en grades`);
    ok(pr.w.PROF_DIFFICULTE.JEU_ID === "immersif-" + j, `${j} : réglages enregistrés sous la clé « immersif-${j} »`);
    ok(pr.erreurs.length === 0, `${j} : erreurs JS ${pr.erreurs.join(" | ")}`);
    // les équipes de CE jeu s'affichent (et non celles de « vingt-mille-lieues »)
    const pr2 = await charger(J(j), "", { page: "prof.html", attente: 300, avant: w => { const f = w.fetch; w.fetch = async (u, o) => /api\/equipes/.test(String(u)) ? { ok: true, json: async () => ({ equipes: [{ equipe: "Les Lynx", jeu: j, niveau: "timonier", salle: 1, enigme: { resolues: {}, total: 4 }, score: 5 }, { equipe: "Autres", jeu: "vingt-mille-lieues", niveau: "matelot", salle: 1, enigme: { resolues: {}, total: 4 }, score: 5 }] }) } : f(u, o); } });
    await dodo(500);
    ok(pr2.w.document.querySelectorAll(".eq").length === 1, `${j} : seules les équipes de ce jeu sont listées`);
  }
};

SECTIONS.defaut = async () => {
  console.log("\n== Immersif par défaut, classique en option ==");
  const C = new Function(fs.readFileSync(path.join(RACINE, "commun/donnees/catalogue.js"), "utf8") + "; return { CATALOGUE, CATALOGUE_JEU };")();
  const avecImm = C.CATALOGUE.jeux.filter(j => j.immersif);
  ok(avecImm.length === IMM.length && IMM.every(j => avecImm.some(x => x.dossier === j && x.immersif === "immersifs/" + j)), `catalogue : champ « immersif » pour les ${IMM.length} jeux qui ont une variante`);
  ok(avecImm.every(j => fs.existsSync(path.join(RACINE, j.immersif, "index.html"))), "catalogue : chaque variante existe");
  ok(C.CATALOGUE_JEU.adresse(avecImm[0]) === avecImm[0].immersif && C.CATALOGUE_JEU.classique(avecImm[0]) === avecImm[0].dossier, "CATALOGUE_JEU.adresse = immersif, classique = dossier");
  const sans = C.CATALOGUE.jeux.filter(j => j.dossier && !j.immersif).map(j => j.dossier).sort().join();
  ok(sans === "declaration,mission-geo,tour-du-monde", `sans variante immersive : ${sans} (restent à l'adresse classique)`);
  // accueil de la collection : « Jouer » mène à l'immersif, la version classique est proposée
  const A = await charger(RACINE, "", { page: "index.html", attente: 500 });
  const d = A.w.document;
  for (const j of IMM) {
    const carte = [...d.querySelectorAll("article")].find(a => a.querySelector(`a.jouer[href="immersifs/${j}/"]`));
    ok(!!carte && !!carte.querySelector(`a.classique[href="${j}/"]`) && !!carte.querySelector(`a.prof[href="immersifs/${j}/prof.html"]`), `accueil : ${j} → immersif par défaut, lien « version classique » et tableau de bord`);
  }
  ok(!!d.querySelector('a.jouer[href="declaration/"]') && !!d.querySelector('a.jouer[href="mission-geo/"]'), "accueil : les jeux sans variante gardent leur adresse");
  ok(/version immersive/.test(d.body.textContent), "accueil : la version immersive est annoncée");
  const frise = [...d.querySelectorAll("#frise a.frise-jeu")].map(a => a.getAttribute("href"));
  ok(IMM.every(j => frise.includes(`immersifs/${j}/`)) && frise.includes("declaration/"), "frise de l'année : variantes immersives par défaut");
  ok(A.erreurs.length === 0, "accueil : erreurs JS " + A.erreurs.join(" | "));
  // vue d'ensemble de l'année
  const Y = await charger(RACINE, "", { page: "annee.html", attente: 800 });
  const liens = [...Y.w.document.querySelectorAll(".liens a")].map(a => a.getAttribute("href"));
  ok(IMM.every(j => liens.includes(`immersifs/${j}/`) && liens.includes(`${j}/`)), "année : « Jouer (immersif) » et « Version classique » pour chaque jeu");
  // liens réciproques
  for (const j of IMM) {
    const I = await charger(J(j), "", { avant, attente: 400 });
    ok(I.w.document.getElementById("lien-classique").getAttribute("href") === `../../${j}/`, `${j} immersif : lien « Version classique »`);
    const html = fs.readFileSync(path.join(RACINE, j, "index.html"), "utf8");
    ok(html.includes(`href="../immersifs/${j}/"`) && /lien-immersif/.test(html), `${j} classique : lien « version immersive »`);
  }
  // « Et ensuite ? » à l'écran du coffre ouvert : mène à l'immersif du jeu suivant, depuis la variante immersive
  const parole = w => { avant(w); };
  const { w } = await charger(J("constitution"), "", { avant: parole, attente: 800 });
  const dd = w.document;
  dd.getElementById("nom-equipe").value = "Les Lynx"; dd.getElementById("nom-equipe").dispatchEvent(new w.Event("input"));
  dd.querySelector(".carte-grade").click(); dd.getElementById("btn-embarquer").click(); await dodo(500);
  const E = w.VML.ETAT; E.escalesFaites = w.VML.escalesJouables(); E.coffreOuvert = true; E.fini = true; E.coffre = { erreurs: 0 };
  w.VML.ouvrirCoffre(); await dodo(100);
  const suite = dd.querySelector("#fin-contenu .encart-suite");
  ok(!!suite, "variante immersive : encart « Et ensuite ? » au coffre ouvert");
  const lienSuite = suite && [...suite.querySelectorAll("a")].map(a => a.getAttribute("href"));
  ok(lienSuite && lienSuite.every(h => /^\.\.\/\.\.\//.test(h)), "…avec des liens relatifs à la variante (../../…) : " + (lienSuite || []).join(" "));
  ok(lienSuite.some(h => h === "../../immersifs/versailles/" || h === "../../immersifs/declaration/" || /^\.\.\/\.\.\/(immersifs\/)?[a-z-]+\/$/.test(h)), "…vers la variante immersive par défaut quand elle existe");
};

SECTIONS.bilan = async () => {
  console.log("\n== N12 : bilan de classe avec des parties immersives ==");
  const e = (id, s, l, pc, err, ind) => ({ id, s, l, ok: 1, pc, e: err, i: ind, p: 0, c: 0 });
  const base = { type: "escape-game-compte-rendu", version: 1, jeu: "renaissance", titre: "L'Atelier de Léonard à Amboise — Carnet de mission", mode: "equipe", niveau: "Peintre", palier: "timonier", termine: true, score: 100, scoreMax: 400, enigmes: 20, total: 20, premierCoup: 8, erreurs: 5, indices: 2, dureeMin: 40 };
  const D = donnees("renaissance"), e1 = D.escales[0].enigmes[0], e2 = D.escales[0].enigmes[1];
  const parties = [["Les Lynx", 0], ["Les Hiboux", 0], ["Les Renards", 1]].map(([nom, pc], k) => Object.assign({}, base, { eleve: nom, date: `2026-10-1${k}T10:00`, partie: `2026-10-1${k}T09:00`, detail: [e(e1.id, 1, e1.lecon, pc, pc ? 0 : 2, pc ? 0 : 1), e(e2.id, 1, e2.lecon, 1, 0, 0)] }));
  const { w, erreurs } = await charger(RACINE, "", { page: "resultats.html", attente: 400, stockage: { escape_resultats: JSON.stringify(parties) } });
  const d = w.document;
  d.getElementById("btn-appareil").click();
  await attendreQue(() => w.RESULTATS_PAGE.bilan && w.RESULTATS_PAGE.bilan.parties.length === 3, 4000); await dodo(200);
  const B = w.RESULTATS_PAGE.bilan;
  const en = B.enigmes.find(x => x.id === e1.id);
  ok(en && en.imm === true && en.titre === e1.titre && en.n === 3 && en.pc === 1, `énigme immersive « ${en && en.titre} » : titre trouvé dans la variante, 1 réussite du premier coup sur 3`);
  const comp = B.comps.find(c => c.lecon === e1.lecon);
  ok(comp && comp.texte.length > 20, `compétence du programme retrouvée pour la leçon « ${e1.lecon} » : « ${comp && comp.texte.slice(0, 60)}… »`);
  const liens = [...d.querySelectorAll("#bilan-contenu a.lien-lecon")].map(a => a.getAttribute("href"));
  ok(liens.length >= 1 && liens.every(h => /^immersifs\/renaissance\/lecons-imprimables\.html\?niveau=timonier&lecon=/.test(h)), "liens vers les leçons à imprimer de la variante, au bon grade : " + liens.join(" ; "));
  ok(liens.every(h => fs.existsSync(path.join(RACINE, h.split("?")[0]))), "les pages de leçons liées existent");
  ok(erreurs.length === 0, "erreurs JS " + erreurs.join(" | "));
};

module.exports = { SECTIONS };
if (require.main === module) {
  const choix = process.argv[2] ? process.argv[2].split(",") : Object.keys(SECTIONS);
  (async () => { try { for (const s of choix) await SECTIONS[s](); } catch (e) { T.exception(e); } T.fin(); })();
}
