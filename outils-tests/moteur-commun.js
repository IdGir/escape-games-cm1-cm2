/* ============================================================
   TESTS DU MOTEUR COMMUN (Node + jsdom)
   ------------------------------------------------------------
   Partie complète, chaque type d'énigme, indices, mode vérification,
   leçons, réglages et impressions, pour les jeux « salles » qui
   partagent le moteur d'énigmes v2 (outils-moteur/enigmes.js) :
   constitution, station-meteo, melanges, objets-techniques,
   moyen-age-abbaye, chateau-fort, versailles, renaissance,
   alimentation.

   Tout est déduit des données du jeu (enigmes.json, dialogues.json) :
   nombre d'énigmes par niveau, mots-clés, barème. Un test de jeu se
   réduit donc à :   require("../../outils-tests/moteur-commun").lancer(__dirname + "/..", {titre:"…"})
   ============================================================ */
const fs = require("fs"), path = require("path");
const { charger, compteur, dodo, attendreQue, testerLeconsA4 } = require("./charge");

function lancer(dossierJeu, cfg = {}){
  const JEU = path.resolve(dossierJeu);
  const NOM = path.basename(JEU);
  const T = compteur(cfg.titre || NOM);
  const ok = T.ok;
  const ENIG = JSON.parse(fs.readFileSync(JEU + "/assets/data/enigmes.json", "utf8"));
  const DIAL = JSON.parse(fs.readFileSync(JEU + "/assets/data/dialogues.json", "utf8"));
  const NB_SALLES = DIAL.salles.length;
  const parNiveau = n => ENIG.salles.map(s => s.enigmes.filter(e => !e.niveaux || e.niveaux.includes(n)));

  /* ---- Résolution d'une énigme par des clics, comme un élève ----
     faux=true : une seule pièce volontairement mal placée. */
  async function resoudre(w, e, d, faux = false){
    const doc = w.document, carte = doc.getElementById("enigme-" + e.id), N = w.normaliser;
    const clic = el => el && el.dispatchEvent(new w.MouseEvent("click", { bubbles: true }));
    carte.querySelectorAll(".slots-lettres .slot.ok").forEach(clic);
    carte.querySelectorAll(".trou[data-pose], .plan-case[data-pose]").forEach(clic);
    switch (e.type) {
      case "qcm": d.questions.forEach((q, i) => clic(carte.querySelector(`.qcm-question[data-i="${i}"] .qcm-option[data-j="${faux && i === 0 ? (q.bonne + 1) % q.options.length : q.bonne}"]`))); break;
      case "vraifaux": d.affirmations.forEach((a, i) => clic(carte.querySelector(`.vf-ligne[data-i="${i}"] [data-rep="${(faux && i === 0 ? !a.vrai : !!a.vrai) ? "vrai" : "faux"}"]`))); break;
      case "association": {
        const g = [...carte.querySelectorAll('[data-col="g"] .carte-match')];
        g.forEach((c, i) => { clic(c); clic(carte.querySelector(`[data-col="d"] [data-id="${faux && g.length > 1 ? g[(i + 1) % g.length].dataset.bon : c.dataset.bon}"]`)); });
        break; }
      case "ordre": {
        const liste = carte.querySelector(".liste-ordre"); const n = d.items.length;
        for (let r = 1; r <= n; r++) { let garde = 0; while (true) { const items = [...liste.querySelectorAll(".item-ordre")]; const idx = items.findIndex(x => +x.dataset.rang === r); if (idx === r - 1 || garde++ > 20) break; clic(items[idx].querySelector(".btn-monter")); } }
        if (faux) clic(liste.children[0].querySelector(".btn-descendre"));
        break; }
      case "tri": {
        const cols = [...carte.querySelectorAll(".tri-colonne")];
        [...carte.querySelectorAll(".carte-tri")].forEach((c, i) => { let col = c.dataset.col; if (faux && i === 0) col = (cols.find(k => k.dataset.col !== col) || cols[0]).dataset.col;
          clic(c); clic(carte.querySelector(`.tri-colonne[data-col="${col}"] .tri-zone`)); });
        break; }
      case "trous": case "plan": {
        const cibles = [...carte.querySelectorAll(e.type === "trous" ? ".trou" : ".plan-case")];
        const reps = cibles.map(t => t.dataset.rep); if (faux && reps.length > 1) [reps[0], reps[1]] = [reps[1], reps[0]];
        cibles.forEach((t, i) => { const et = [...carte.querySelectorAll(".etiquette:not(.posee)")].find(x => N(x.dataset.mot) === N(reps[i])); clic(et); clic(t); });
        break; }
      case "lettres": {
        let cible = d.cible.slice();
        if (faux) { [cible[0], cible[cible.length - 1]] = [cible[cible.length - 1], cible[0]]; if (N(cible.join("")) === N(d.cible.join(""))) cible.reverse(); }
        cible.forEach(l => clic([...carte.querySelectorAll("[data-l]:not(.utilisee)")].find(x => N(x.dataset.l) === N(l))));
        break; }
      case "code": d.champs.forEach((c, i) => { carte.querySelector("#code-" + i).value = faux && i === 0 ? "xxxx" : String(c.valeur).toUpperCase(); }); break;
      case "intrus": clic(carte.querySelector(`[data-intrus="${faux ? 0 : 1}"]`)); break;
      case "instrument":
        carte.querySelectorAll(".instr-item").forEach(it => {
          const item = d.items[+it.dataset.i];
          if (it.dataset.mode === "lire") it.querySelector(".instr-champ").value = faux ? String(item.valeur + 1) : String(item.valeur).replace(".", ",");
          else { const cran = it.querySelector(`.instr-cran[data-v="${item.valeur}"]`);
            if (cran && !faux) clic(cran); else it.dataset.niveau = faux ? item.valeur + 1 : item.valeur; }
        });
        break;
      default: ok(false, `type d'énigme inconnu du test : ${e.type}`);
    }
    clic(carte.querySelector("[data-valider]"));
    await dodo(20);
    return carte.classList.contains("resolue");
  }

  const sansBalises = s => String(s || "").replace(/<[^>]*>/g, " ").replace(/\s+/g, " ").trim();
  function textesCorrection(e){
    const t = [];
    const parcourir = o => { if (o && typeof o === "object") Object.entries(o).forEach(([k, v]) => {
      if (/^(correction|explication)$/.test(k)) [].concat(typeof v === "object" && v ? Object.values(v) : v).forEach(x => typeof x === "string" && t.push(sansBalises(x)));
      else parcourir(v); }); };
    parcourir(e);
    const enonce = sansBalises(JSON.stringify(e, (k, v) => /^(correction|explication)$/.test(k) ? undefined : v));
    return t.filter(x => x.length >= 12).map(x => x.slice(0, 40)).filter(x => !enonce.includes(x));
  }
  function controlerErreur(w, e, etiquette){
    const carte = w.document.getElementById("enigme-" + e.id), fb = w.document.getElementById("fb-" + e.id).textContent;
    ok(!carte.classList.contains("resolue"), `${etiquette} (${e.type}) : mauvaise réponse refusée`);
    ok(/Pas tout juste/.test(fb) && (e.type === "intrus" ? /Ce n'est pas l'intrus/.test(fb) : /\b\d+ [^.]+ sur \d+\./.test(fb)), `${etiquette} (${e.type}) : message « N … sur M » attendu, obtenu « ${fb.replace(/\s+/g, " ").slice(0, 90)} »`);
    ok(!carte.querySelector(".bien, .mal, .correct, .incorrect"), `${etiquette} (${e.type}) : des éléments sont marqués bien/mal`);
  }
  function controlerReussite(w, e, pts, etiquette){
    const carte = w.document.getElementById("enigme-" + e.id), fb = w.document.getElementById("fb-" + e.id).textContent;
    ok(fb.includes("+" + pts + " points") && (pts === 10) === /Tout juste du premier coup/.test(fb), `${etiquette} : « +${pts} points » attendu, obtenu « ${fb.slice(0, 80)} »`);
    const copie = carte.cloneNode(true); copie.querySelectorAll(".barre-outils, .consigne").forEach(x => x.remove());
    const txt = copie.textContent.replace(/\s+/g, " "), fuite = textesCorrection(e).find(x => txt.includes(x));
    ok(!carte.querySelector(".correction, .source-correction, .explication") && !fuite, `${etiquette} : aucune correction affichée après la réussite` + (fuite ? " (trouvé : « " + fuite + " »)" : ""));
  }
  const bareme = w => w.eval("({premier:PTS_PREMIER_COUP, apres:PTS_APRES_ERREUR, rapidite:PTS_RAPIDITE, quiz:PTS_QUIZ, nbQuiz:NB_QUIZ, malus:MALUS_INDICE, coffre:PTS_COFFRE_PREMIER, coffreApres:PTS_COFFRE_APRES})");

  /* ---- Partie complète : avecErreurs = la 1re énigme et le coffre d'abord ratés ---- */
  async function partie(niveau, avecErreurs){
    console.log(`\n== Partie complète ${niveau}${avecErreurs ? " (une erreur, un coffre raté)" : ""} ==`);
    const { w, erreurs } = await charger(JEU);
    const doc = w.document, ETAT = w.ETAT, B = bareme(w), DONNEES = w.eval("DONNEES");
    ETAT.reglages.cinematiques = false; ETAT.reglages.decorsVideo = false;
    doc.querySelector(`.opt-niveau[data-niveau="${niveau}"]`).click();
    const inp = doc.getElementById("input-equipe"); inp.value = "Les Testeurs"; inp.dispatchEvent(new w.Event("input"));
    ok(!doc.getElementById("btn-demarrer").disabled, "bouton démarrer actif");
    doc.getElementById("btn-demarrer").click(); await dodo(200);
    const attendues = parNiveau(niveau);
    let total = 0;
    for (let s = 1; s <= NB_SALLES; s++) {
      ok(ETAT.salle === s, `salle courante ${s}`);
      ok(!!doc.querySelector(".scene"), `décor de la salle ${s}`);
      const liste = w.salleEnigmes(s);
      ok(liste.length === attendues[s - 1].length, `salle ${s} : ${liste.length} énigmes (attendu ${attendues[s - 1].length})`);
      for (let k = 0; k < liste.length; k++) {
        const e = liste[k]; const d = w.donneesNiveau(e);
        ok(!!doc.getElementById("enigme-" + e.id), `énigme ${e.id} affichée`);
        if (e.lecon) ok(!!doc.querySelector(`#enigme-${e.id} [data-fiche="${e.lecon}"]`), `bouton leçon ${e.id}`);
        const avant = ETAT.score, premiere = avecErreurs && total === 0;
        if (premiere) { await resoudre(w, e, d, true); controlerErreur(w, e, e.id); }
        const r = await resoudre(w, e, d); ok(r, `énigme ${e.id} (${e.type}) résolue`);
        const pts = premiere ? B.apres : B.premier;
        controlerReussite(w, e, pts, e.id);
        total++;
        if (k < liste.length - 1) {
          const b = await attendreQue(() => doc.getElementById("btn-enigme-suivante")); ok(!!b, "bouton énigme suivante après " + e.id);
          ok(ETAT.score - avant === pts, `${e.id} : +${pts} points au score (obtenu ${ETAT.score - avant})`);
          b && b.click();
        }
      }
      const id = s < NB_SALLES ? "btn-salle-suivante" : "btn-coffre-final";
      const b = await attendreQue(() => doc.getElementById(id), 2500);
      ok(!!b, `salle ${s} : bouton ${id} tout de suite`);
      ok(ETAT.motsCles.length === s, `mot-clé ${s} obtenu (${ETAT.motsCles.join(",")})`);
      const zone = doc.getElementById("zone-enigme").textContent;
      ok(zone.includes(DONNEES.salles[s - 1].motCle) && /Notez ce mot/.test(zone), `salle ${s} : mot ${DONNEES.salles[s - 1].motCle} affiché avec « Notez ce mot »`);
      if (!b) return w;
      b.click(); await dodo(60);
      if (cfg.apresSalle) await cfg.apresSalle(w, s, T);
      ok(!doc.querySelector(".mot-cle"), `salle ${s} : le mot n'est plus affiché ensuite`);
    }
    const coffre = await attendreQue(() => doc.getElementById("coffre-final"));
    ok(!!coffre, "coffre final affiché");
    if (!coffre) return w;
    const champs = DONNEES.salles.map((x, i) => doc.getElementById("coffre-" + i));
    ok(champs.every(c => c && c.value === ""), "coffre final : les champs sont vides");
    ok(!DONNEES.salles.some(x => coffre.textContent.includes(x.motCle)), "coffre final : aucun mot-clé affiché");
    if (avecErreurs) {
      champs.forEach((c, i) => c.value = i === 0 ? "mot faux" : DONNEES.salles[i].motCle);
      doc.getElementById("btn-coffre").click();
      ok(!ETAT.coffreOuvert && new RegExp(`${NB_SALLES - 1} mots justes sur ${NB_SALLES}`).test(doc.getElementById("fb-coffre").textContent), "coffre final : un mot faux est refusé");
    }
    const avantCoffre = ETAT.score;
    champs.forEach((c, i) => c.value = w.normaliser(DONNEES.salles[i].motCle));
    doc.getElementById("btn-coffre").click();
    ok(ETAT.coffreOuvert, "coffre final : s'ouvre avec les bons mots (accents et casse ignorés)");
    ok(ETAT.score - avantCoffre === (avecErreurs ? B.coffreApres : B.coffre), `coffre final : +${avecErreurs ? B.coffreApres : B.coffre} points`);
    if (cfg.avantFin) await cfg.avantFin(w, T);
    await attendreQue(() => doc.getElementById("ecran-fin").classList.contains("actif"), 6000);
    ok(doc.getElementById("ecran-fin").classList.contains("actif"), "écran de fin");
    ok(ETAT.motsCles.join(" ") === DIAL.salles.map(s => s.motCle).join(" "), "mots-clés dans l'ordre des salles : " + ETAT.motsCles.join(" "));
    const Q = w.quizzCourant();
    Q.forEach((q, i) => doc.querySelector(`#quizz .qcm-question[data-i="${i}"] .qcm-option[data-j="${q.bonne}"]`).click());
    doc.getElementById("btn-voir-score").click(); await dodo(50);
    const max = total * B.premier + B.coffre + NB_SALLES * B.rapidite + B.nbQuiz * B.quiz + (cfg.bonusMax || 0);
    ok(w.scoreMax() === max, `score max ${w.scoreMax()} = ${max}`);
    if (cfg.scoresMax) ok(w.scoreMax() === cfg.scoresMax[niveau], `score max ${niveau} = ${cfg.scoresMax[niveau]} (README)`);
    const attendu = max - (cfg.bonusMax || 0) - (avecErreurs ? (B.premier - B.apres) + (B.coffre - B.coffreApres) : 0);
    ok(ETAT.score === attendu, `score final ${ETAT.score} = ${attendu}`);
    ok(ETAT.enigmesReussies === total, "énigmes réussies " + ETAT.enigmesReussies);
    ok(ETAT.enigmesPremierCoup === total - (avecErreurs ? 1 : 0) && ETAT.erreursTotal === (avecErreurs ? 2 : 0) && ETAT.coffrePremierCoup === !avecErreurs,
       `bilan : ${ETAT.enigmesPremierCoup} du premier coup, ${ETAT.erreursTotal} erreur(s), coffre du premier coup : ${ETAT.coffrePremierCoup}`);
    ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
    return w;
  }

  /* ---- Chaque type d'énigme (mode vérification) : incomplète, fausse, puis juste ---- */
  async function types(){
    console.log("\n== Chaque type : erreur « N … sur M », puis 3 points ==");
    const vus = new Set(); let negatifs = 0;
    const tousTypes = new Set(ENIG.salles.flatMap(s => s.enigmes.filter(e => !e.niveaux || e.niveaux.includes("CM2")).map(e => e.type)));
    for (const s of ENIG.salles) {
      const liste = s.enigmes.filter(e => !e.niveaux || e.niveaux.includes("CM2"));
      for (let k = 0; k < liste.length; k++) {
        const e = liste[k]; if (vus.has(e.type)) continue; vus.add(e.type);
        const { w, erreurs } = await charger(JEU, `?salle=${s.num}&niveau=CM2&enigme=${k + 1}`);
        const carte = w.document.getElementById("enigme-" + e.id);
        if (!carte) { ok(false, "accès direct à " + e.id); continue; }
        const B = bareme(w), d = w.donneesNiveau(e);
        if (e.type !== "ordre") {
          carte.querySelector("[data-valider]").click();
          ok(!carte.classList.contains("resolue") && w.ETAT.erreursTotal === 0, `${e.id} (${e.type}) : une réponse incomplète n'est pas comptée comme erreur`);
        }
        const errAvant = w.ETAT.erreursTotal;
        await resoudre(w, e, d, true); controlerErreur(w, e, e.id); negatifs++;
        ok(w.ETAT.erreursTotal === errAvant + 1, `${e.id} (${e.type}) : une erreur comptée`);
        ok(await resoudre(w, e, d), `${e.id} (${e.type}) résolue après l'erreur`);
        controlerReussite(w, e, B.apres, e.id);
        await dodo(600);
        ok(w.ETAT.score === B.apres, `${e.id} (${e.type}) : ${B.apres} points après une erreur (score ${w.ETAT.score})`);
        ok(erreurs.length === 0, `${e.id} : erreurs JS : ` + erreurs.join(" | "));
      }
    }
    ok(vus.size === tousTypes.size && negatifs === tousTypes.size, `${vus.size} types testés sur ${tousTypes.size}, ${negatifs} réponses fausses refusées`);
  }

  /* ---- Indices, vérification, leçons, réglages, impressions ---- */
  async function divers(){
    console.log("\n== Indices, vérification, réglages, impressions, leçons ==");
    // première énigme CM1 de la salle 3 qui a au moins un indice
    const l3 = parNiveau("CM1")[2]; const k = Math.max(0, l3.findIndex(e => e.indices));
    const e = l3[k];
    const { w, erreurs } = await charger(JEU, `?salle=3&niveau=CM1&enigme=${k + 1}`);
    const doc = w.document;
    ok(w.ETAT.equipe === "Vérification" && w.ETAT.salle === 3 && w.ETAT.niveau === "CM1", "mode vérification salle 3 CM1");
    ok(!!doc.getElementById("enigme-" + e.id), `énigme ${e.id} ciblée par &enigme=${k + 1}`);
    const bandeau = doc.querySelector(`#enigme-${e.id} .bandeau-bareme`);
    ok(bandeau && /10 points/.test(bandeau.textContent) && /3 points/.test(bandeau.textContent), "bandeau du barème : 10 / 3 points");
    const bi = doc.getElementById("indice-" + e.id);
    if (bi) {
      w.ETAT.score = 20;
      bi.click();
      ok(w.ETAT.score === 18, `indice = moins 2 points (20 → ${w.ETAT.score})`);
      const s0 = w.ETAT.score;
      ok(await resoudre(w, e, w.donneesNiveau(e)), `${e.id} résolue après un indice`);
      await dodo(600);
      ok(w.ETAT.score === s0 + 10, `${e.id} : +10 du premier coup malgré l'indice (${s0} → ${w.ETAT.score})`);
    }
    const cle = w.eval("CLE_SAUVEGARDE");
    const sauve = w.localStorage.getItem(cle);
    ok(!sauve || !String(JSON.parse(sauve).equipe || "").includes("Vérification"), "rien de sauvegardé en vérification");
    // leçons
    if (typeof w.ouvrirBiblioLecons === "function") {
      await w.ouvrirBiblioLecons(); await dodo(50);
      const cartes = doc.querySelectorAll("#corps-lecons .carte-lecon, #corps-lecons [data-lecon]");
      ok(cartes.length >= 1, `bibliothèque des leçons : ${cartes.length} leçon(s)`);
    }
    // réglages
    w.ouvrirReglages(); await dodo(50);
    ok(doc.getElementById("overlay-reglages").classList.contains("show"), "réglages ouverts");
    doc.getElementById("reg-taille").value = "1.3"; doc.getElementById("reg-calme").classList.add("actif");
    w.sauverReglages();
    ok(w.ETAT.reglages.tailleTexte === 1.3 && w.ETAT.reglages.animationsReduites === true, "réglages taille et animations");
    ok(doc.body.classList.contains("calme"), "classe calme appliquée");
    if (cfg.reglages) await cfg.reglages(w, T);
    // impressions
    await w.chargerEvaluations();
    for (const t of ["prepa", "qcm", "fermees", "docs", "tout"]) {
      await w.imprimerFiches(t); await dodo(30);
      const z = doc.querySelector(".zone-impression"); const h = z ? z.innerHTML : "";
      ok(h.length > 500 && !/undefined|NaN/.test(h), `impression ${t} (${h.length} car.)`);
    }
    w.imprimerBilan(); await dodo(30);
    ok(!/undefined|NaN/.test(doc.querySelector(".zone-impression").innerHTML), "bilan imprimé");
    if (typeof w.imprimerFicheMission === "function") { w.imprimerFicheMission(); await dodo(30); ok(!/undefined|NaN/.test(doc.querySelector(".zone-impression").innerHTML), "fiche de mission imprimée"); }
    ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
    const f = await charger(JEU, `?salle=${NB_SALLES + 1}&niveau=CM2`); await dodo(300);
    ok(f.w.document.getElementById("ecran-fin").classList.contains("actif"), `vérification : écran de fin (salle=${NB_SALLES + 1})`);
    ok(f.erreurs.length === 0, "erreurs fin : " + f.erreurs.join(" | "));
  }

  /* ---- Tableau de bord enseignant : la page se charge sans erreur ---- */
  async function prof(){
    if (!fs.existsSync(JEU + "/prof.html")) return;
    console.log("\n== Tableau de bord (prof.html) et leçons imprimables A4 ==");
    const p = await charger(JEU, "", { page: "prof.html" });
    ok(p.erreurs.length === 0, "prof.html : erreurs JS : " + p.erreurs.join(" | "));
    await testerLeconsA4(JEU, ok);
  }

  const etapes = (process.argv[2] || "partie,types,divers,prof").split(",");
  (async () => {
    try {
      if (etapes.includes("partie")) { await partie("CM1", false); await partie("CM2", true); }
      if (etapes.includes("types")) await types();
      if (etapes.includes("divers")) await divers();
      if (etapes.includes("prof")) await prof();
      if (cfg.plus) await cfg.plus({ charger: (q, o) => charger(JEU, q, o), ok, resoudre, JEU });
    } catch (e) { T.exception(e); }
    T.fin();
  })();
}

module.exports = { lancer };
