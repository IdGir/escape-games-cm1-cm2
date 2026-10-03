/* ============================================================
   TESTS DU JEU « Le Journal du Nautilus » (Node + jsdom)
   ------------------------------------------------------------
   node vingt-mille-lieues/tests/test-jeu.js        (jsdom : cd outils-tests && npm install)
   Étapes : donnees · circuit · partie (5 grades) · erreurs · aides ·
            reglages · pages. Une étape seule : … test-jeu.js partie
   Réutilise outils-tests/charge.js (lecture seule).
   ============================================================ */
const path = require("path"), fs = require("fs");
const { charger, compteur, dodo, attendreQue, clic } = require("../../outils-tests/charge");
const JEU = path.resolve(__dirname, "..");
const { ok, fin, exception } = compteur("Le Journal du Nautilus");
const etapes = process.argv.slice(2);
const faire = n => !etapes.length || etapes.includes(n);
const GRADES = ["mousse", "matelot", "timonier", "lieutenant", "second"];
const lire = f => JSON.parse(fs.readFileSync(path.join(JEU, "assets", "data", f), "utf8"));
const D = { enigmes: lire("enigmes.json"), lecons: lire("lecons.json"), fx: lire("decors-fx.json"), dialogues: lire("dialogues.json"), persos: lire("personnages.json") };
const avant = w => { w.VML_RAPIDE = true; };

/* Solutions justes d'un circuit, par grade (fils à poser, interrupteurs à fermer, fils à retirer) */
const CIRCUITS = {
  mousse: { fils: [["L1b", "P-"]], fermes: {} },
  matelot: { fils: [["P+", "K1a"], ["K1b", "L1a"], ["L1b", "Ma"], ["Mb", "P-"]], fermes: { K1: true } },
  timonier: { fils: [["P+", "L1a"], ["L1b", "P-"], ["P+", "L2a"], ["L2b", "P-"]], fermes: {} },
  lieutenant: { fils: [["P+", "L1a"], ["L1b", "P-"], ["P+", "L2a"], ["L2b", "P-"], ["P+", "K2a"], ["K2b", "Ma"], ["Mb", "P-"]], fermes: { K2: true } },
  second: { retirer: true, fils: [["P+", "L1a"], ["L1b", "P-"], ["P+", "L2a"], ["L2b", "P-"], ["P+", "K2a"], ["K2b", "Ma"], ["Mb", "P-"]], fermes: { K2: true } }
};

/** Répond juste à l'énigme ouverte (ou faux si « faux » est vrai). */
async function repondre(w, e, grade, faux){
  const d = w.document, b = e[grade], type = b.type || e.type;
  const carte = d.getElementById("enigme-" + e.id);
  if(!carte) throw new Error("carte absente " + e.id);
  if(type === "tri"){
    const cartes = [...carte.querySelectorAll(".carte-tri")];
    cartes.forEach((c, i) => {
      clic(w, c);
      let col = c.dataset.col;
      if(faux && i === 0) col = (b.colonnes.find(x => x.id !== col) || {}).id;
      clic(w, carte.querySelector(`.tri-colonne[data-col="${col}"]`));
    });
  }else if(type === "association"){
    const g = [...carte.querySelectorAll('[data-col="g"] .carte-match')];
    g.forEach((c, i) => {
      clic(w, c);
      let cible = c.dataset.bon;
      if(faux && i < 2) cible = g[1 - i].dataset.bon;
      clic(w, carte.querySelector(`[data-col="d"] [data-id="${cible}"]`));
    });
  }else if(type === "ordre"){
    const liste = carte.querySelector(".liste-ordre");
    const items = [...liste.querySelectorAll(".item-ordre")].sort((a, c) => a.dataset.rang - c.dataset.rang);
    if(faux) [items[0], items[1]] = [items[1], items[0]];
    items.forEach(it => liste.appendChild(it));
  }else if(type === "trous"){
    const trous = [...carte.querySelectorAll(".trou")];
    trous.forEach((t, i) => {
      let mot = t.dataset.rep;
      if(faux && i === 0) mot = b.etiquettes.find(x => !String(b.texte).includes("[[" + x + "]]"));
      clic(w, carte.querySelector(`.etiquette[data-mot="${mot}"]:not(.posee)`));
      clic(w, t);
    });
  }else if(type === "qcm"){
    carte.querySelectorAll(".qcm-question").forEach((q, i) => {
      let j = b.questions[+q.dataset.i].bonne;
      if(faux && i === 0) j = (j + 1) % b.questions[+q.dataset.i].options.length;
      clic(w, q.querySelector(`.qcm-option[data-j="${j}"]`));
    });
  }else if(type === "circuit"){
    const s = CIRCUITS[grade];
    const c = carte._circuit;
    if(s.retirer) c.fils.splice(0, c.fils.length, ...c.fils.filter(f => f.fixe));
    (faux ? s.fils.slice(0, s.fils.length - 1) : s.fils).forEach(([de, a]) => c.fils.push({ de, a }));
    Object.assign(c.fermes, s.fermes);
  }
  if(b.justification && (grade === "lieutenant" || grade === "second")){
    clic(w, carte.querySelector(`.justif-option[data-j="${b.justification.bonne}"]`));
  }
  clic(w, carte.querySelector("[data-valider]"));
  await dodo(30);
}

(async () => {
  try{
    /* ================= Données ================= */
    if(faire("donnees")){
      console.log("== Données ==");
      const es = D.enigmes.escales.find(x => x.numero === 2);
      ok(es && es.enigmes.length >= 3 && es.enigmes.length <= 4, "escale 2 : 3 à 4 énigmes");
      ok(D.enigmes.niveaux.map(n => n.id).join() === GRADES.join(), "5 grades dans l'ordre");
      const emb = fs.readFileSync(path.join(JEU, "js", "donnees-embarquees.js"), "utf8");
      const m = emb.match(/window\.VML_DONNEES_EMBARQUEES = ([\s\S]*);\s*$/);
      const E = m ? JSON.parse(m[1]) : {};
      ok(JSON.stringify(E.enigmes) === JSON.stringify(D.enigmes) && JSON.stringify(E.lecons) === JSON.stringify(D.lecons) && JSON.stringify(E["decors-fx"]) === JSON.stringify(D.fx) && JSON.stringify(E.dialogues) === JSON.stringify(D.dialogues) && JSON.stringify(E.personnages) === JSON.stringify(D.persos),
        "js/donnees-embarquees.js à jour (sinon : python vingt-mille-lieues/outils/embarquer-donnees.py)");
      const solutions = (() => { const ctx = {}; new Function("globalThis", fs.readFileSync(path.join(JEU, "js", "solutions.js"), "utf8").replace("typeof window !== \"undefined\" ? window : globalThis", "globalThis"))(ctx); return ctx.VML.solutionTexte; })();
      for(const e of es.enigmes){
        for(const g of GRADES){
          const b = e[g];
          ok(!!b, `${e.id} : bloc ${g}`); if(!b) continue;
          ok(b.dialogue && b.consigne && b.indices && b.indices.length >= 2, `${e.id} ${g} : dialogue, consigne, 2 indices`);
          const type = b.type || e.type;
          if(type === "qcm") b.questions.forEach((q, i) => ok(q.bonne >= 0 && q.bonne < q.options.length && new Set(q.options).size === q.options.length, `${e.id} ${g} Q${i + 1} : bonne réponse valide, options distinctes`));
          if(type === "tri") ok(b.cartes.every(c => b.colonnes.some(x => x.id === c.col)), `${e.id} ${g} : chaque carte a une colonne`);
          if(type === "trous") ok([...b.texte.matchAll(/\[\[(.+?)\]\]/g)].every(x => b.etiquettes.includes(x[1])), `${e.id} ${g} : chaque trou a son étiquette`);
          if(type === "circuit"){ const ids = b.composants.map(c => c.id); const a = b.attendu; ok([...(a.allumes || []), ...(a.fermes || []), ...(a.independants || []), ...Object.keys(a.commande || {})].every(x => ids.includes(x)), `${e.id} ${g} : composants attendus existent`); }
          if(g === "lieutenant" || g === "second") ok(b.justification && b.justification.options[b.justification.bonne], `${e.id} ${g} : justification présente`);
        }
        const sol = GRADES.map(g => solutions(e, g).join(" | "));
        ok(sol.every(s => s.length > 5), `${e.id} : corrigé non vide à chaque grade`);
        ok(sol.every((s, i) => i === 0 || s !== sol[i - 1]), `${e.id} : réponses différentes d'un grade au suivant (pas de réponse recopiable)`);
      }
      for(const g of GRADES){
        const types = es.enigmes.map(e => e[g].type || e.type);
        ok(types.every((t, i) => i === 0 || t !== types[i - 1]), `${g} : jamais deux énigmes de même type d'affilée (${types.join(", ")})`);
      }
      ok(es.enigmes.every(e => D.lecons.lecons.some(l => l.id === e.lecon)), "chaque énigme renvoie à une fiche existante");
      const textes = JSON.stringify(D);
      ok(!/CE2|CM1|CM2|6e|5e/.test(JSON.stringify(D.enigmes.escales)), "aucune étiquette scolaire dans les énigmes affichées");
      ok(!/[A-Za-z0-9_-]{20,}\.(?:apihub)|AGNES_API_KEY\s*=|Bearer\s+[A-Za-z0-9]/.test(textes), "aucune clé d'API dans les données");
      const sw = fs.readFileSync(path.join(JEU, "sw.js"), "utf8");
      const liste = JSON.parse("[" + sw.match(/const FICHIERS = \[([\s\S]*?)\];/)[1].replace(/'/g, '"') + "]");
      ok(liste.filter(f => f !== "./").every(f => fs.existsSync(path.join(JEU, f))), "sw.js : tous les fichiers listés existent");
      const js = fs.readdirSync(path.join(JEU, "js")).map(f => "js/" + f);
      ok(js.every(f => liste.includes(f)), "sw.js : tous les fichiers js/ sont listés (hors connexion)");
    }

    /* ================= Simulation du circuit ================= */
    if(faire("circuit")){
      console.log("== Circuit ==");
      const { w } = await charger(JEU, "?verif=1&escale=2&niveau=timonier&enigme=2", { avant });
      const V = w.VML;
      const comps = [{ id: "P", type: "pile" }, { id: "L1", type: "lampe" }, { id: "L2", type: "lampe" }, { id: "K", type: "interrupteur" }];
      const f = (...p) => p.map(([de, a]) => ({ de, a }));
      let r = V.simulerCircuit(comps, f(["P+", "L1a"], ["L1b", "L2a"], ["L2b", "P-"]), {});
      ok(r.tension.L1 > 0.15 && r.tension.L2 > 0.15 && !r.cc, "série : les deux lampes brillent");
      r = V.simulerCircuit(comps, f(["P+", "L1a"], ["L1b", "L2a"], ["L2b", "P-"]), {}, ["L1"]);
      ok(r.tension.L2 < 0.15, "série : une lampe retirée, l'autre s'éteint");
      r = V.simulerCircuit(comps, f(["P+", "L1a"], ["L1b", "P-"], ["P+", "L2a"], ["L2b", "P-"]), {}, ["L1"]);
      ok(r.tension.L2 > 0.15, "dérivation : une lampe retirée, l'autre reste allumée");
      r = V.simulerCircuit(comps, f(["P+", "P-"], ["P+", "L1a"], ["L1b", "P-"]), {});
      ok(r.cc && !(r.tension.L1 > 0.15), "court-circuit détecté, rien ne brille");
      r = V.simulerCircuit(comps, f(["P+", "Ka"], ["Kb", "L1a"], ["L1b", "P-"]), { K: false });
      ok(!(r.tension.L1 > 0.15), "interrupteur ouvert : circuit ouvert");
      r = V.simulerCircuit(comps, f(["P+", "L1a"], ["L1b", "P-"], ["L1a", "L1b"]), {});
      ok(!(r.tension.L1 > 0.15), "lampe court-circuitée par un fil : éteinte");
      const e = D.enigmes.escales[0].enigmes[1];
      for(const g of GRADES){
        const s = CIRCUITS[g];
        let fils = (e[g].fils || []).filter(x => !s.retirer || x.fixe).concat(s.fils.map(([de, a]) => ({ de, a })));
        const fermes = Object.assign({}, s.fermes);
        const v = V.verifierCircuit(e[g], fils, fermes);
        ok(v.liste.every(x => x.ok), `${g} : la solution de référence est acceptée`);
        const v2 = V.verifierCircuit(e[g], fils.slice(0, -1), fermes);
        ok(!v2.liste.every(x => x.ok), `${g} : un fil manquant est refusé`);
      }
      const serie = V.verifierCircuit(e.timonier, f(["P+", "L1a"], ["L1b", "L2a"], ["L2b", "P-"]), {});
      ok(!serie.liste.every(x => x.ok) && serie.liste.filter(x => x.ok).length >= 3, "timonier : le montage en série est refusé (lampes non indépendantes)");
      const derivMatelot = V.verifierCircuit(e.matelot, f(["P+", "K1a"], ["K1b", "L1a"], ["L1b", "P-"], ["K1b", "Ma"], ["Mb", "P-"]), { K1: true });
      ok(!derivMatelot.liste.every(x => x.ok), "matelot : une dérivation est refusée (la consigne exige une seule boucle)");
      const sansRetrait = V.verifierCircuit(e.second, e.second.fils.concat(CIRCUITS.second.fils.map(([de, a]) => ({ de, a }))), { K2: true });
      ok(!sansRetrait.liste.every(x => x.ok), "second : garder le fil de secours (court-circuit) est refusé");
    }

    /* ================= Partie complète aux 5 grades ================= */
    if(faire("partie")){
      console.log("== Partie complète, 5 grades ==");
      const es = D.enigmes.escales[0];
      for(const g of GRADES){
        const { w, erreurs } = await charger(JEU, `?verif=1&escale=2&niveau=${g}&enigme=1`, { avant });
        const d = w.document;
        ok(await attendreQue(() => d.querySelector("#scene-jeu .zone.cible")), `${g} : décor et objet cible affichés`);
        ok(d.querySelector("#scene-jeu").dataset.source === "secours", `${g} : décor de secours (aucune image dans jsdom)`);
        ok(/plaque-dialogue/.test(d.getElementById("plaque").innerHTML), `${g} : le personnage émetteur pose le problème`);
        for(const e of es.enigmes){
          await attendreQue(() => d.querySelector(`#scene-jeu[data-decor="${e.decor}"] .zone[data-zone="${e.objet_principal}"]`));
          ok(d.querySelector("#scene-jeu").dataset.decor === e.decor, `${g} ${e.id} : décor « ${e.decor} »`);
          e.objets_cliquables.filter(z => z !== e.objet_principal).forEach(z => {
            clic(w, d.querySelector(`.zone[data-zone="${z}"]`));
          });
          ok(!d.getElementById("panneau-enigme").classList.contains("ouvert"), `${g} ${e.id} : examiner un autre objet n'ouvre pas l'énigme`);
          clic(w, d.querySelector(`.zone[data-zone="${e.objet_principal}"]`));
          ok(await attendreQue(() => d.getElementById("enigme-" + e.id)), `${g} ${e.id} : l'énigme s'ouvre depuis l'objet du décor`);
          if(e.id === "e2-1") clic(w, d.querySelector("[data-fiche]"));
          const score0 = w.VML.ETAT.score;
          await repondre(w, e, g);
          ok(await attendreQue(() => w.VML.ETAT.resolues[e.id]), `${g} ${e.id} : résolue du premier coup`);
          const attendu = 10 + (e.id === "e2-1" ? 2 : 0);
          ok(w.VML.ETAT.score - score0 === attendu, `${g} ${e.id} : +${attendu} points (obtenu ${w.VML.ETAT.score - score0})`);
          if(e.id === "e2-1") ok(/Bien documenté/.test(d.getElementById("fb-" + e.id).innerHTML), `${g} : bonus « Bien documenté » affiché`);
          ok(!/Bravo|correction|La bonne réponse/i.test(d.getElementById("fb-" + e.id).textContent), `${g} ${e.id} : aucun texte de correction après la réussite`);
          await attendreQue(() => !d.getElementById("panneau-enigme").classList.contains("ouvert"));
          ok(d.querySelector(`.reaction-${e.reaction_du_decor.effet}`) || d.querySelector("#scene-jeu").classList.contains("flash-lumiere") || e.reaction_du_decor.effet === "hublots" || e.reaction_du_decor.effet === "lumiere", `${g} ${e.id} : le décor réagit (${e.reaction_du_decor.effet})`);
          ok(!d.getElementById("plaque").classList.contains("visible"), `${g} ${e.id} : personnage muet après la réussite`);
          await dodo(200);
        }
        ok(await attendreQue(() => d.body.dataset.ecran === "ecran-fin", 4000), `${g} : écran de fin d'escale`);
        ok(d.querySelector(".fragment-mot") && d.querySelector(".fragment-mot").textContent === es.mot, `${g} : le fragment ${es.mot} s'affiche`);
        ok(d.getElementById("bilan").hidden, `${g} : bilan caché tant que le mot n'est pas noté`);
        clic(w, d.getElementById("btn-mot-note"));
        ok(!d.querySelector(".fragment-mot") && !d.getElementById("bilan").hidden, `${g} : le mot disparaît une fois noté, le bilan apparaît`);
        const max = es.enigmes.length * 12 + 10;
        ok(w.VML.ETAT.score === 40 + 2 + 5 + 5 && d.querySelector(".bilan-score").textContent.includes("/ " + max), `${g} : score ${w.VML.ETAT.score} (40 + 2 documenté + 5 maître-nageur + 5 rapidité) sur ${max}`);
        ok((g === "second") === !d.getElementById("btn-plonger"), `${g} : « plonger plus profond » proposé sauf au dernier grade`);
        ok(erreurs.length === 0, `${g} : aucune erreur JS (${erreurs.join(" | ")})`);
        w.close();
      }
    }

    /* ================= Erreurs, sas, barème après erreur ================= */
    if(faire("erreurs")){
      console.log("== Erreurs et sas de sécurité ==");
      const es = D.enigmes.escales[0];
      for(const [g, k] of [["matelot", 0], ["timonier", 2], ["lieutenant", 3], ["second", 1]]){
        const e = es.enigmes[k];
        const { w, erreurs } = await charger(JEU, `?verif=1&escale=2&niveau=${g}&enigme=${k + 1}`, { avant });
        const d = w.document;
        await attendreQue(() => w.VML.ouvrirEnigmeCourante);
        w.VML.ouvrirEnigmeCourante();
        await attendreQue(() => d.getElementById("enigme-" + e.id));
        await repondre(w, e, g, true);
        const fb = d.getElementById("fb-" + e.id).textContent;
        ok(/Pas tout juste/.test(fb) && /sur \d+/.test(fb), `${g} ${e.id} : l'erreur dit combien de réponses sont justes (« ${fb.slice(0, 70)}… »)`);
        ok(/ne rapportera plus que 3 points/.test(fb), `${g} ${e.id} : perte du bonus annoncée`);
        ok(!d.querySelector(".bien, .mal, .juste, .fausse"), `${g} ${e.id} : aucune réponse marquée juste ou fausse`);
        /* Rouvrir l'énigme (réponses remises à zéro), répondre juste : 3 points */
        const score0 = w.VML.ETAT.score;
        w.VML.ouvrirEnigmeCourante();
        await attendreQue(() => d.getElementById("enigme-" + e.id));
        await repondre(w, e, g);
        ok(await attendreQue(() => w.VML.ETAT.resolues[e.id]) && w.VML.ETAT.score - score0 === 3, `${g} ${e.id} : 3 points après une erreur`);
        ok(erreurs.length === 0, `${g} : aucune erreur JS (${erreurs.join(" | ")})`);
        w.close();
      }
      /* Sas : 3 erreurs en moins de 60 s */
      const e = es.enigmes[0];
      const { w } = await charger(JEU, `?verif=1&escale=2&niveau=matelot&enigme=1`, { avant });
      const d = w.document;
      await attendreQue(() => w.VML.ouvrirEnigmeCourante); w.VML.ouvrirEnigmeCourante();
      await attendreQue(() => d.getElementById("enigme-" + e.id));
      for(let i = 0; i < 3; i++) clic(w, d.querySelector("#enigme-e2-1 [data-valider]"));
      ok(w.VML.etatEnigme("e2-1").erreurs === 0, "valider un tri incomplet ne compte pas d'erreur");
      await repondre(w, e, "matelot", true);
      clic(w, d.querySelector("#enigme-e2-1 [data-valider]"));
      clic(w, d.querySelector("#enigme-e2-1 [data-valider]"));
      ok(w.VML.etatEnigme("e2-1").erreurs === 3, "trois erreurs comptées");
      ok(!d.querySelector(".sas-voile").hidden && d.querySelector(".enigme-carte").classList.contains("sas-verrouille"), "sas de sécurité verrouillé après 3 erreurs en 60 s");
      ok(/20 s|19 s/.test(d.querySelector(".sas-compte").textContent), "premier verrou : 20 s");
      clic(w, d.querySelector("#enigme-e2-1 [data-valider]"));
      ok(w.VML.etatEnigme("e2-1").erreurs === 3, "pendant le verrou, une validation n'est pas comptée");
      ok(!d.querySelector("[data-fiche]").disabled, "la fiche reste consultable pendant le verrou");
      w.VML.etatEnigme("e2-1").sasJusqu = Date.now() - 1;
      w.VML.ouvrirEnigmeCourante(); await attendreQue(() => d.getElementById("enigme-e2-1"));
      ok(d.querySelector(".sas-voile").hidden, "le sas se rouvre à la fin du délai");
      w.close();
    }

    /* ================= Aides : indices, Mousse, justification, mélange ================= */
    if(faire("aides")){
      console.log("== Aides ==");
      const es = D.enigmes.escales[0];
      let { w } = await charger(JEU, `?verif=1&escale=2&niveau=mousse&enigme=3`, { avant });
      let d = w.document;
      await attendreQue(() => w.VML.ouvrirEnigmeCourante); w.VML.ouvrirEnigmeCourante();
      await attendreQue(() => d.getElementById("enigme-e2-3"));
      ok(d.querySelector("[data-fiche]").classList.contains("mise-en-evidence"), "Mousse : fiche mise en évidence");
      ok(/offert/.test(d.querySelector("[data-indice]").textContent), "Mousse : premier indice offert");
      clic(w, d.querySelector("[data-indice]"));
      ok(w.VML.ETAT.score === 0 && w.VML.ETAT.indicesTotal === 0 && d.querySelectorAll(".indices-donnes .indice").length === 1, "Mousse : le premier indice ne coûte rien");
      w.VML.ETAT.score = 10;
      clic(w, d.querySelector("[data-indice]"));
      ok(w.VML.ETAT.score === 8 && w.VML.ETAT.indicesTotal === 1, "deuxième indice : −2 points");
      ok(d.querySelector("[data-indice]").disabled, "plus d'indice disponible ensuite");
      w.close();
      /* Justification obligatoire et comptée comme une réponse */
      ({ w } = await charger(JEU, `?verif=1&escale=2&niveau=lieutenant&enigme=4`, { avant }));
      d = w.document;
      await attendreQue(() => w.VML.ouvrirEnigmeCourante); w.VML.ouvrirEnigmeCourante();
      await attendreQue(() => d.getElementById("enigme-e2-4"));
      const e = es.enigmes[3], b = e.lieutenant;
      const carte = d.getElementById("enigme-e2-4");
      [...carte.querySelectorAll(".trou")].forEach(t => { clic(w, carte.querySelector(`.etiquette[data-mot="${t.dataset.rep}"]:not(.posee)`)); clic(w, t); });
      clic(w, carte.querySelector("[data-valider]"));
      ok(w.VML.etatEnigme("e2-4").erreurs === 0 && /justifie/.test(d.getElementById("fb-e2-4").textContent), "Lieutenant : sans justification, rien n'est compté (message)");
      const mauvaise = (b.justification.bonne + 1) % b.justification.options.length;
      clic(w, carte.querySelector(`.justif-option[data-j="${mauvaise}"]`));
      const ordre1 = [...carte.querySelectorAll(".justif-option")].map(x => x.dataset.j).join();
      clic(w, carte.querySelector("[data-valider]"));
      ok(w.VML.etatEnigme("e2-4").erreurs === 1, "Lieutenant : mauvaise justification = une erreur");
      let ordreChange = false;
      for(let i = 0; i < 6 && !ordreChange; i++){
        clic(w, carte.querySelector(`.justif-option[data-j="${mauvaise}"]`));
        w.VML.etatEnigme("e2-4").tsErreurs = [];
        clic(w, carte.querySelector("[data-valider]"));
        ordreChange = [...carte.querySelectorAll(".justif-option")].map(x => x.dataset.j).join() !== ordre1;
      }
      ok(ordreChange, "les options sont remélangées après une erreur");
      w.close();
    }

    /* ================= Partie normale : accueil, sauvegarde, réglages, impressions ================= */
    if(faire("reglages")){
      console.log("== Accueil, sauvegarde, réglages ==");
      let { w, erreurs } = await charger(JEU, "", { avant });
      let d = w.document;
      ok(d.querySelectorAll(".carte-grade").length === 5, "accueil : 5 grades");
      ok(!/CE2|CM1|CM2|6ᵉ|5ᵉ/.test(d.getElementById("ecran-accueil").textContent), "accueil : aucune étiquette scolaire visible");
      ok(d.getElementById("btn-embarquer").disabled, "embarquer : désactivé sans nom ni grade");
      d.getElementById("nom-equipe").value = "Les Hublots"; d.getElementById("nom-equipe").dispatchEvent(new w.Event("input"));
      clic(w, d.querySelector('[data-grade="timonier"]'));
      ok(!d.getElementById("btn-embarquer").disabled, "embarquer : actif avec nom et grade");
      clic(w, d.getElementById("btn-embarquer"));
      ok(await attendreQue(() => d.body.dataset.ecran === "ecran-cine"), "cinématique d'escale lancée");
      clic(w, d.querySelector(".cine-passer"));
      ok(await attendreQue(() => d.body.dataset.ecran === "ecran-jeu"), "cinématique passée : la scène s'ouvre");
      ok(w.VML.ETAT.air < 100, "jauge d'air entamée par l'avarie (décor)");
      const sauve = JSON.parse(w.localStorage.getItem("vml_partie"));
      ok(sauve && sauve.equipe === "Les Hublots" && sauve.niveau === "timonier" && sauve.introVue, "partie sauvegardée");
      clic(w, d.getElementById("btn-reglages"));
      ok(d.getElementById("reglages").classList.contains("ouverte"), "⚙️ réglages ouverts");
      ok(/≈ CM2/.test(d.getElementById("reglages").textContent), "réglages : équivalences visibles pour l'enseignant");
      w.__imprime = 0;
      clic(w, d.querySelector('[data-act="fiche"]')); await dodo(80);
      ok(w.__imprime === 1 && /Escale 11/.test(d.getElementById("zone-impression").textContent), "fiche de mission : 11 cases");
      clic(w, d.querySelector('[data-act="corriges"]')); await dodo(80);
      const cor = d.getElementById("zone-impression").textContent;
      ok(w.__imprime === 2 && /MOBILIS/.test(cor) && GRADES.every(g => cor.includes(w.VML.infoGrade(g).nom)), "corrigés : 5 grades et mot de l'escale");
      clic(w, d.querySelector('[data-act="journal"]')); await dodo(80);
      ok(w.__imprime === 3 && /Journal de bord/.test(d.getElementById("zone-impression").textContent), "journal de bord imprimable");
      const cb = d.querySelector('[data-cle="antiTatonnement"]'); cb.checked = false; cb.dispatchEvent(new w.Event("change"));
      ok(JSON.parse(w.localStorage.getItem("vml_reglages")).antiTatonnement === false, "réglage gardé sur l'appareil");
      w.VML.traiterCommande({ delaiMin: 2, t: 1 });
      ok(w.VML.ETAT.delaiAccordeMin === 2, "commande enseignant : +2 min accordées");
      w.VML.traiterCommande({ niveau: "second", t: 2 });
      ok(w.VML.ETAT.niveau === "second", "commande enseignant : grade changé à distance");
      w.VML.traiterCommande({ pause: true, t: 3 });
      ok(d.body.dataset.ecran === "ecran-pause", "commande enseignant : pause");
      w.VML.traiterCommande({ pause: false, t: 4 });
      ok(d.body.dataset.ecran === "ecran-jeu", "commande enseignant : reprise");
      const p = w.VML.payloadEtat();
      ok(p.jeu === "vingt-mille-lieues" && p.enigme && Array.isArray(p.enigme.fiches) && "sas" in p.enigme, "état envoyé au tableau de bord : énigme, fiches, sas");
      ok(erreurs.length === 0, "aucune erreur JS (" + erreurs.join(" | ") + ")");
      const stock = { vml_partie: w.localStorage.getItem("vml_partie") };
      w.close();
      ({ w, erreurs } = await charger(JEU, "", { avant, stockage: stock }));
      d = w.document;
      ok(!d.getElementById("reprise").hidden && /Les Hublots/.test(d.getElementById("reprise-texte").textContent), "reprise de la partie proposée à l'accueil");
      clic(w, d.getElementById("btn-reprendre-partie"));
      ok(await attendreQue(() => d.body.dataset.ecran === "ecran-jeu"), "reprise : retour dans la scène sans cinématique");
      w.close();
    }

    /* ================= Autres pages ================= */
    if(faire("pages")){
      console.log("== Pages annexes ==");
      for(const [page, test] of [
        ["prof.html", d => /Tableau de bord/.test(d.body.textContent) && d.getElementById("synthese").textContent.includes("Le câble brûlé du carré")],
        ["lecons-imprimables.html", d => d.querySelectorAll(".page").length === D.lecons.lecons.length],
        ["medias.html", d => d.querySelectorAll("#decors .m").length === Object.keys(D.fx.decors).length]
      ]){
        const { w, erreurs } = await charger(JEU, "", { page, avant, attente: 1200 });
        ok(test(w.document), `${page} : construite`);
        ok(erreurs.length === 0, `${page} : aucune erreur JS (${erreurs.join(" | ")})`);
        if(page === "prof.html"){
          w.PROF.equipes = [{ equipe: "Les Hublots", jeu: "vingt-mille-lieues", niveau: "lieutenant", salle: 2, score: 22, msEcoules: 420000, indicesTotal: 1, fini: false, timestamp: Date.now() / 1000,
            enigme: { id: "e2-3", titre: "Le mur des instruments", ordre: 3, total: 4, erreurs: 5, indices: 1, fiches: ["instruments"], depuisMs: 400000, sas: true, resolues: { "e2-1": { premier: true, bienDoc: 2 }, "e2-2": { premier: false } }, fichesConsultees: ["circuit"], air: 70 } }];
          w.PROF.dessiner();
          const c = w.document.querySelector(".eq");
          ok(c && c.classList.contains("alerte") && /sas/.test(c.textContent) && /bloquée/.test(c.textContent), "prof.html : carte d'équipe avec alertes (sas, erreurs, bloquée)");
          ok(/≈ 6ᵉ/.test(c.textContent) && /Le circuit électrique/.test(c.textContent), "prof.html : grade et fiches consultées");
        }
        w.close();
      }
    }
  }catch(e){ exception(e); }
  fin();
})();
