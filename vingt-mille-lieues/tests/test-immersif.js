/* ============================================================
   TEST GÉNÉRIQUE D'UN JEU AU MODÈLE IMMERSIF (Node + jsdom)
   ------------------------------------------------------------
   Fonctionne pour « Vingt mille lieues » et pour tout jeu issu du migrateur (outils/immersif/migrer-jeu.py) :
   lit js/jeu-config.js (grades, titres) et assets/data/*.json, puis
     · données : grades, types, fiches de leçon, zones, mots, fuites du thème Nautilus (jeux migrés) ;
     · partie  : joue TOUTES les énigmes de TOUS les grades (seulement pour les jeux migrés, ou avec PARTIE=1).
   Usage : node <dossier-du-jeu>/tests/test-immersif.js [donnees|partie]
   ============================================================ */
const path = require("path"), fs = require("fs");
const { charger, compteur, dodo, attendreQue, clic } = require(path.join(process.env.OUTILS_TESTS || path.resolve(__dirname, "../../outils-tests"), "charge"));
const { repondre } = require("./solveurs");
const JEU = path.resolve(__dirname, "..");
const lire = f => JSON.parse(fs.readFileSync(path.join(JEU, "assets", "data", f), "utf8"));
const cfg = (() => { const ctx = {}; new Function("window", fs.readFileSync(path.join(JEU, "js", "jeu-config.js"), "utf8"))(ctx); return ctx.VML_JEU; })();
const { ok, fin, exception } = compteur("Modèle immersif — " + cfg.id);
const etapes = process.argv.slice(2);
const faire = n => !etapes.length || etapes.includes(n);
const NAUTILUS = cfg.id === "vingt-mille-lieues";
const TYPES = ["qcm", "vraifaux", "association", "ordre", "tri", "trous", "lettres", "code", "intrus", "plan", "circuit", "instrument"];
const avant = w => { w.VML_RAPIDE = true; };

(async () => {
  try{
    const E = lire("enigmes.json"), L = lire("lecons.json"), F = lire("decors-fx.json"), DL = lire("dialogues.json"), P = lire("personnages.json").personnages;
    const GRADES = cfg.grades;

    if(faire("donnees")){
      console.log("== Données ==");
      ok(GRADES.length >= 1 && GRADES.every(g => ["mousse", "matelot", "timonier", "lieutenant", "second"].includes(g)), `grades de la config : ${GRADES.join(", ")}`);
      ok(E.niveaux.map(n => n.id).join() === GRADES.join(), "assets/data/enigmes.json : les grades correspondent à la config (même ordre)");
      ok(cfg.prefixeStockage && cfg.textes.titre && cfg.textes.journal, "js/jeu-config.js : identité, clé de sauvegarde et titres renseignés");
      const ids = E.escales.flatMap(x => x.enigmes.map(e => e.id));
      ok(new Set(ids).size === ids.length, "identifiants d'énigmes uniques");
      ok(new Set(E.escales.map(x => x.mot)).size === E.escales.length, "un mot différent par étape (coffre final)");
      ok(E.escales.map(x => x.numero).every((n, i, t) => !i || n > t[i - 1]), "étapes rangées dans l'ordre");
      for(const es of E.escales){
        const dec = (F.decors || F)[es.enigmes[0].decor];
        ok(!!dec && dec.zones && dec.zones.length >= 1, `étape ${es.numero} : décor « ${es.enigmes[0].decor} » décrit (zones)`);
        ok(!!(DL.cinematiques[es.cinematique_ouverture] && DL.cinematiques[es.cinematique_fin]), `étape ${es.numero} : cinématiques d'ouverture et de fin`);
        for(const e of es.enigmes){
          const d = (F.decors || F)[e.decor];
          ok(!!d && d.zones.some(z => z.id === e.objet_principal) && e.objets_cliquables.includes(e.objet_principal), `${e.id} : objet principal présent dans les zones du décor`);
          ok(!!P[e.personnage_emetteur], `${e.id} : personnage émetteur connu`);
          ok(L.lecons.some(l => l.id === e.lecon), `${e.id} : fiche de leçon « ${e.lecon} » existante`);
          const grades = e.niveaux && e.niveaux.length ? e.niveaux : GRADES;
          ok(grades.every(g => GRADES.includes(g)), `${e.id} : "niveaux" ne cite que des grades du jeu`);
          for(const g of grades){
            const b = e[g]; if(!b){ ok(false, `${e.id} : bloc ${g} absent`); continue; }
            const type = b.type || e.type;
            ok(TYPES.includes(type) && b.consigne && b.indices && b.indices.length >= 1, `${e.id} ${g} : type, consigne, indice(s)`);
            if(type === "qcm") b.questions.forEach((q, i) => ok(q.bonne >= 0 && q.bonne < q.options.length, `${e.id} ${g} Q${i + 1} : bonne réponse valide`));
            if(type === "trous") ok([...b.texte.matchAll(/\[\[(.+?)\]\]/g)].every(x => b.etiquettes.includes(x[1])), `${e.id} ${g} : chaque trou a son étiquette`);
            if(type === "tri") ok(b.cartes.every(c => b.colonnes.some(x => x.id === c.col)), `${e.id} ${g} : chaque carte a sa colonne`);
          }
        }
      }
      const emb = fs.readFileSync(path.join(JEU, "js", "donnees-embarquees.js"), "utf8");
      const m = emb.match(/window\.VML_DONNEES_EMBARQUEES = ([\s\S]*);\s*$/);
      const EMB = m ? JSON.parse(m[1]) : {};
      ok(JSON.stringify(EMB.enigmes) === JSON.stringify(E) && JSON.stringify(EMB.lecons) === JSON.stringify(L) && JSON.stringify(EMB.dialogues) === JSON.stringify(DL),
        "js/donnees-embarquees.js à jour (sinon : python outils/embarquer-donnees.py)");
      const sw = fs.readFileSync(path.join(JEU, "sw.js"), "utf8");
      const liste = JSON.parse("[" + sw.match(/const FICHIERS = \[([\s\S]*?)\];/)[1].replace(/'/g, '"') + "]");
      ok(liste.filter(f => f !== "./").every(f => fs.existsSync(path.join(JEU, f))), "sw.js : tous les fichiers listés existent");
      ok(fs.readdirSync(path.join(JEU, "js")).every(f => liste.includes("js/" + f)), "sw.js : tous les fichiers js/ sont listés (hors connexion)");
      const donneesTexte = JSON.stringify([E, L, F, DL, P]) + JSON.stringify(cfg);
      ok(!/[A-Za-z0-9_-]{24,}\.(?:apihub)|(?:API_KEY|api_key)["']?\s*[:=]\s*["'][A-Za-z0-9]{12,}|Bearer\s+[A-Za-z0-9]{12,}/.test(donneesTexte), "aucune clé d'API dans les données");
      if(!NAUTILUS){
        ok(!/Nautilus|Nemo|Aronnax|Ned Land|Conseil le|vingt mille lieues|Jules Verne/i.test(donneesTexte), "aucune fuite du thème « Vingt mille lieues » dans les données du jeu");
        for(const f of ["index.html", "prof.html", "manifest.webmanifest"]){
          ok(!/Journal du Nautilus|Nemo/.test(fs.readFileSync(path.join(JEU, f), "utf8").replace(/data-t="[^"]*">[^<]*</g, "><")), `${f} : aucun titre « Nautilus » en dur (lu depuis js/jeu-config.js)`);
        }
      }
    }

    if(faire("partie") && (!NAUTILUS || process.env.PARTIE === "1")){
      console.log("== Partie complète, toutes étapes, tous grades ==");
      for(const es of E.escales) for(const g of GRADES){
        const attendues = es.enigmes.filter(e => !(e.niveaux && e.niveaux.length) || e.niveaux.includes(g));
        const { w, erreurs } = await charger(JEU, `?verif=1&escale=${es.numero}&niveau=${g}&enigme=1`, { avant });
        const d = w.document;
        const vue = w.VML.escale(es.numero);
        ok(vue.enigmes.length === attendues.length, `étape ${es.numero} ${g} : ${attendues.length} énigme(s) pour ce grade`);
        ok(await attendreQue(() => d.querySelector("#scene-jeu .zone.cible")), `${g} : décor et objet cible affichés`);
        for(const e of attendues){
          await attendreQue(() => d.querySelector(`#scene-jeu[data-decor="${e.decor}"] .zone.cible[data-zone="${e.objet_principal}"]`), 4000);
          clic(w, d.querySelector(`.zone[data-zone="${e.objet_principal}"]`));
          ok(await attendreQue(() => d.getElementById("enigme-" + e.id)), `${g} ${e.id} : l'énigme s'ouvre depuis l'objet du décor`);
          await repondre(w, e, g);
          ok(await attendreQue(() => w.VML.ETAT.resolues[e.id]), `${g} ${e.id} : résolue`);
          await attendreQue(() => !d.getElementById("panneau-enigme").classList.contains("ouvert"));
          await dodo(150);
        }
        ok(await attendreQue(() => d.body.dataset.ecran === "ecran-fin", 4000), `étape ${es.numero} ${g} : écran de fin d'étape`);
        ok(d.querySelector(".fragment-mot") && d.querySelector(".fragment-mot").textContent === es.mot, `étape ${es.numero} ${g} : le mot « ${es.mot} » s'affiche`);
        ok(erreurs.length === 0, `étape ${es.numero} ${g} : aucune erreur JS (${erreurs.join(" | ")})`);
        w.close();
      }
    }
  }catch(e){ exception(e); }
  fin();
})();
