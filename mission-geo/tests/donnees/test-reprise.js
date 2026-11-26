/* Vérifie la reprise des parties dans la version immersive (bloc ajouté à immersifs/mission-geo/js/jeu-config.js).
   node mission-geo/tests/donnees/test-reprise.js */
const fs = require("fs"), path = require("path"), vm = require("vm"), assert = require("assert");
const RACINE = path.resolve(__dirname, "../../..");
const cfg = fs.readFileSync(path.join(RACINE, "immersifs/mission-geo/js/jeu-config.js"), "utf8");
const debut = cfg.indexOf("(function(){"), fin = cfg.lastIndexOf("window.VML_JEU =");
const mod = { exports: {} };
vm.runInNewContext(cfg.slice(debut, fin), { module: mod, console });
const R = mod.exports;
const IMPORT = require(path.join(RACINE, "commun/js/mission-geo-import.js"));
let n = 0; const ok = (c, m) => { assert.ok(c, m); n++; };

// 1. Sauvegarde de la version classique : séances 1 et 2 réussies, 3 commencée
const classique = { version: 1, equipe: "Les Boussoles", niveau: "CM1", palier: "", erreurs: 2,
  sessions: { s01: { reussie: true, points: 15 }, s02: { reussie: true, points: 20 }, s03: { reussie: false, points: 4 } },
  indices: [{ session: "s01", type: "nombre", symbole: "etoile", valeur: 5 }], final: {} };
const p = R.depuisClassique(classique);
ok(p && p.equipe === "Les Boussoles" && p.seances[1].reussie && !p.seances[3].reussie, "conversion de la sauvegarde classique");
const E = R.versEtat(p);
ok(E.niveau === "matelot", "CM1 → matelot");
ok(E.escale === 3 && !E.escaleTerminee && E.indexEnigme === 0, "reprise à la séance 3");
ok(JSON.stringify(E.escalesFaites) === "[1,2]" && E.mots.join(" ") === "COMMUNE EMBOÎTÉS", "escales faites et mots du coffre");
ok(E.score === 35 && E.resolues["e1-1"].pts === 15 && E.resolues["e1-2"].pts === 0 && E.resolues["e2-4"], "points repris tels quels, sans bonus, toutes les énigmes résolues");
ok(E.carnetMissionGeo.length === 1, "carnet d'indices conservé");

// 2. Partie du PC de la classe (format commun v2, produite par commun/js/mission-geo-import.js)
const v2 = IMPORT.convertir({ version: 1, equipe: "Atlas 2", niveau: "CM2", palier: "decouverte",
  sessions: { s01: { reussie: true, points: 10 }, s02: { reussie: true, points: 9 }, s03: { reussie: true, points: 8 }, s04: { reussie: true, points: 7 }, s05: { reussie: true, points: 6 }, s06: { reussie: true, points: 5 } } }).partie;
const E2 = R.versEtat(v2);
ok(E2.niveau === "mousse", "Découverte → mousse");
ok(E2.escaleTerminee && E2.escale === 5 && E2.escalesFaites.length === 5, "toutes les séances jouables faites : fin de la séance 5 (la séance 6 attend la période 2)");
ok(R.versEtat(Object.assign({}, v2, { grade: "lieutenant" })).niveau === "lieutenant", "grade imposé à l'import");

// 3. Copie vers le PC : format accepté par le serveur (mission-geo-partie, séances 1 à 16)
const P = R.versPartie(Object.assign({}, E, { escalesFaites: [1, 2], niveau: "timonier" }));
ok(P.format === "mission-geo-partie" && P.seances[1].id === "s01" && P.seances[2].reussie && P.niveau === "CM2" && P.grade === "timonier", "partie envoyée au PC");
ok(P.indices.length === 2 && P.indices[0].valeur === 5 && P.indices[1].valeur === 7, "indices du carnet envoyés");
const ancien = IMPORT.versAncien(IMPORT.convertir(P).partie);
ok(ancien.sessions.s01.reussie && ancien.sessions.s02.reussie, "relisible par la version classique");

// 4. Dans la page (jsdom) : reprise d'office de la partie classique ; proposition « Reprendre la mission de mon équipe »
(async () => {
  const { charger, attendreQue, clic } = require(path.join(RACINE, "outils-tests/charge.js"));
  const dossier = path.join(RACINE, "immersifs/mission-geo");
  let r = await charger(dossier, "", { stockage: { mission_geo_annee_a_v1: JSON.stringify(classique) }, attente: 900 });
  const sauvee = JSON.parse(r.w.localStorage.getItem("vml_mission_geo_partie") || "null");
  ok(sauvee && sauvee.equipe === "Les Boussoles" && sauvee.escale === 3, "page : partie classique reprise d'office");
  ok(await attendreQue(() => !r.w.document.getElementById("reprise").hidden && /Boussoles/.test(r.w.document.getElementById("reprise-texte").textContent)), "page : bouton « Reprendre » proposé");
  ok(r.erreurs.length === 0, "page : aucune erreur JS (" + r.erreurs.join(" | ") + ")");
  r.dom.window.close();
  const partiePC = IMPORT.convertir({ version: 1, equipe: "Les Cartographes", niveau: "CM2", sessions: { s01: { reussie: true, points: 12 } } }).partie;
  let recharge = 0;
  r = await charger(dossier, "", { attente: 900, avant: w => {
    const f = w.fetch;
    w.fetch = async (u, o) => {
      const s = String(u);
      if (/\/api\/parties\?jeu=mission-geo&equipe=/.test(s)) return { ok: true, json: async () => ({ ok: true, partie: partiePC }) };
      if (/\/api\/parties\?jeu=mission-geo/.test(s)) return { ok: true, json: async () => ({ ok: true, parties: [{ equipe: "Les Cartographes", slug: "les-cartographes", reussies: [1] }] }) };
      return f(u, o);
    };
    try { Object.defineProperty(w.location, "reload", { value: () => { recharge++; } }); } catch (e) { w.__pasDeReload = true; }
  } });
  const btn = await attendreQue(() => r.w.document.getElementById("reprise-pc-btn"));
  ok(btn, "page : « Reprendre la mission de mon équipe » proposé par le PC de la classe");
  if (btn) { clic(r.w, btn); await attendreQue(() => r.w.localStorage.getItem("vml_mission_geo_partie")); }
  const pc = JSON.parse(r.w.localStorage.getItem("vml_mission_geo_partie") || "null");
  ok(pc && pc.equipe === "Les Cartographes" && pc.escale === 2 && pc.niveau === "timonier", "page : partie du PC convertie et enregistrée");
  ok(r.erreurs.length === 0, "page (PC) : aucune erreur JS (" + r.erreurs.join(" | ") + ")");
  r.dom.window.close();
  console.log(`Reprise mission-geo (immersif) : ${n} vérifications réussies.`);
})().catch(e => { console.error(e); process.exit(1); });
