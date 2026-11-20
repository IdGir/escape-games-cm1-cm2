/* ============================================================
   TESTS DU LOT 2 « LA CLASSE EN TROIS GESTES » (Node + jsdom)
   Depuis la racine du dépôt :  node commun/tests/test-seance.js
   Étapes au choix : node commun/tests/test-seance.js A1 B1
   A1 accueil en séance · A2 QR code · A5 fin de séance · B1 portail · B2 pack d'impression · OUTILS calendrier
   Le serveur (routes /api/seance et /api/sante) : python commun/tests/test-seance-serveur.py
   ============================================================ */
const { charger, compteur, dodo, attendreQue, RACINE } = require("../../outils-tests/charge");
const fs = require("fs"), path = require("path");
const T = compteur("Séance du jour (lot 2)"); const ok = T.ok;
const SECTIONS = {};

/** Simule le serveur local : réponses JSON par route /api/… (les autres adresses : fichiers du dépôt). */
const serveur = routes => w => {
  const f = w.fetch;
  w.__appels = [];
  w.fetch = async (url, o) => {
    const u = new URL(String(url), w.location.href);
    const m = u.pathname.match(/\/api\/[a-z]+/);
    if(m && routes[m[0]]){
      w.__appels.push({ route: m[0], methode: (o && o.method) || "GET", corps: o && o.body ? JSON.parse(o.body) : null });
      const r = routes[m[0]]((o && o.method) || "GET", o && o.body ? JSON.parse(o.body) : null);
      return { ok: true, status: 200, json: async () => r, text: async () => JSON.stringify(r) };
    }
    return f(url, o);
  };
};
const avecDate = (d, suite) => w => { w.__dateSeance = new Date(d); w.__ouverts = []; w.open = u => { w.__ouverts.push(u); return {}; }; if(suite) suite(w); };

SECTIONS.OUTILS = async () => {
  console.log("\n== Calendrier : période, année, jeux prévus ==");
  const { w, erreurs } = await charger(RACINE, "", { page: "tableau.html", attente: 200 });
  const S = w.SEANCE, C = w.eval("CATALOGUE");
  ok(S.periodeDe(new Date("2026-11-17")) === "P2" && S.periodeDe(new Date("2027-01-10")) === "P3" && S.periodeDe(new Date("2027-08-20")) === "P1", "périodes : nov. P2, janv. P3, août P1");
  ok(S.anneeDe(new Date("2026-11-17")) === "A" && S.anneeDe(new Date("2027-03-01")) === "A" && S.anneeDe(new Date("2027-10-01")) === "B" && S.anneeDe(new Date("2028-10-01")) === "A", "année A en 2026-2027, B en 2027-2028, puis A");
  const p2 = S.jeuxDeLaPeriode(C, new Date("2026-11-17")).map(j => j.id);
  ok(p2.join(",") === "versailles,alimentation,lumiere", "P2 année A : Versailles, Grand Repas, Phare (" + p2.join(", ") + ")");
  ok(S.lienEleves("https://idgir.github.io/escape-games-cm1-cm2/enseignant.html#x", "lumiere", "matelot") === "https://idgir.github.io/escape-games-cm1-cm2/?jeu=lumiere&grade=matelot", "lien élèves sans serveur : ?jeu=…&grade=…");
  ok(S.cleReglages("moyen-age-abbaye") === "vml_moyen_age_abbaye_reglages", "clé des réglages du jeu immersif");
  // cohérence avec les jeux immersifs : le préfixe de stockage de chaque variante
  const dossiers = fs.readdirSync(path.join(RACINE, "immersifs")).filter(d => fs.existsSync(path.join(RACINE, "immersifs", d, "js", "jeu-config.js")));
  const bons = dossiers.filter(d => fs.readFileSync(path.join(RACINE, "immersifs", d, "js", "jeu-config.js"), "utf8").includes(`"prefixeStockage": "${S.cleReglages(d).replace(/_reglages$/, "")}"`));
  ok(bons.length === dossiers.length, `le grade imposé vise le bon réglage dans les ${dossiers.length} variantes immersives (${bons.length})`);
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
};

SECTIONS.A1 = async () => {
  console.log("\n== A1 : accueil en séance (un seul bouton « Jouer ») ==");
  let r = await charger(RACINE, "?jeu=lumiere&grade=matelot", { page: "index.html", attente: 500 });
  let d = r.w.document, a = d.querySelector("#seance-eleves a.jouer-seance");
  ok(a && a.getAttribute("href") === "immersifs/lumiere/" && /Jouer/.test(a.textContent), "lien ?jeu= : un grand bouton « Jouer » vers la version immersive");
  ok(d.documentElement.classList.contains("seance-eleves") && /Phare/.test(d.querySelector("#seance-eleves h1").textContent), "le reste de l'accueil est caché ; titre du jeu du jour");
  await attendreQue(() => !d.querySelector("#seance-eleves .grade").hidden, 1500);
  ok(/Veilleur/.test(d.querySelector("#seance-eleves .grade").textContent), "nom du grade propre au jeu (Veilleur)");
  a.click();
  ok(JSON.parse(r.w.localStorage.getItem("vml_lumiere_reglages")).niveauImpose === "matelot", "clic sur Jouer : grade imposé dans le jeu immersif");
  ok(r.erreurs.length === 0, "erreurs JS : " + r.erreurs.join(" | "));

  r = await charger(RACINE, "", { page: "index.html", attente: 500, avant: serveur({ "/api/seance": () => ({ ok: true, local: false, seance: { jeu: "versailles", grade: "", adresse: "immersifs/versailles/" } }) }) });
  d = r.w.document;
  ok(d.querySelector("#seance-eleves a.jouer-seance") && d.querySelector("#seance-eleves a.jouer-seance").getAttribute("href") === "immersifs/versailles/", "séance fixée par le serveur : Chromebook d'élève → un seul bouton");
  r.w.document.querySelector("#seance-eleves a.jouer-seance").click();
  ok(JSON.parse(r.w.localStorage.getItem("vml_versailles_reglages")).niveauImpose === null, "sans grade : au choix des équipes");

  r = await charger(RACINE, "", { page: "index.html", attente: 500, avant: serveur({ "/api/seance": () => ({ ok: true, local: true, seance: { jeu: "versailles", grade: "", adresse: "immersifs/versailles/" } }) }) });
  d = r.w.document;
  ok(!d.getElementById("seance-eleves") && d.querySelector(".bandeau-seance-prof") && d.querySelectorAll("article.jeu").length > 10, "ordinateur de l'enseignant : tous les jeux, et un bandeau qui rappelle la séance");
  ok(!d.documentElement.classList.contains("seance-attente"), "rien n'est caché");

  r = await charger(RACINE, "?jeu=lumiere&tous=1", { page: "index.html", attente: 400 });
  ok(!r.w.document.getElementById("seance-eleves"), "?tous=1 : accueil complet (enseignant sur un Chromebook)");
  r = await charger(RACINE, "", { page: "index.html", attente: 400, avant: serveur({ "/api/seance": () => ({ ok: true, local: false, seance: null }) }) });
  ok(!r.w.document.getElementById("seance-eleves") && !r.w.document.documentElement.classList.contains("seance-attente"), "sans séance : accueil inchangé");
  ok(r.erreurs.length === 0, "erreurs JS : " + r.erreurs.join(" | "));
};

SECTIONS.A2 = async () => {
  console.log("\n== A2 : page à projeter (QR code) ==");
  let r = await charger(RACINE, "?jeu=lumiere&grade=timonier", { page: "tableau.html", attente: 400 });
  let d = r.w.document;
  ok(d.querySelector("#qr svg path") && /^http:\/\/localhost\/\?jeu=lumiere&grade=timonier$/.test(r.w.__qrTexte || ""), "sans serveur : QR code de l'adresse du site avec ?jeu= (" + r.w.__qrTexte + ")");
  ok(/Phare/.test(d.getElementById("jeu").textContent), "jeu du jour rappelé");
  r = await charger(RACINE, "", { page: "tableau.html", attente: 400, avant: serveur({ "/api/info": () => ({ ip: "192.168.1.23", port: 8000, local: true }), "/api/seance": () => ({ ok: true, local: true, seance: { jeu: "versailles" } }) }) });
  d = r.w.document;
  ok(r.w.__qrTexte === "http://192.168.1.23:8000/" && d.getElementById("adresse").textContent === "192.168.1.23:8000", "avec le serveur : adresse courte du PC (192.168.1.23:8000)");
  ok(/Versailles|Nantes/.test(d.getElementById("jeu").textContent), "jeu du jour lu sur le serveur");
  ok(fs.readFileSync(path.join(RACINE, "commun/js/qrcode.js"), "utf8").includes("MIT"), "bibliothèque QR libre (MIT), embarquée : aucun service externe");
  ok(!/https?:\/\/(?!idgir)[^"' ]*qr/i.test(fs.readFileSync(path.join(RACINE, "tableau.html"), "utf8")), "aucun service de QR en ligne appelé");
  ok(r.erreurs.length === 0, "erreurs JS : " + r.erreurs.join(" | "));
};

SECTIONS.B1 = async () => {
  console.log("\n== B1 : portail à trois boutons (enseignant.html) ==");
  let r = await charger(RACINE, "", { page: "enseignant.html", attente: 700, avant: avecDate("2026-11-17T10:00:00") });
  let d = r.w.document;
  const boutons = ["btn-preparer", "btn-lancer", "btn-terminer"].map(id => d.getElementById(id));
  ok(boutons.every(Boolean) && /Préparer/.test(boutons[0].textContent) && /Lancer/.test(boutons[1].textContent) && /Terminer/.test(boutons[2].textContent), "trois boutons : Préparer, Lancer, Terminer");
  ok(d.getElementById("seance").compareDocumentPosition(d.getElementById("tout-le-reste")) & 4, "la séance est en haut, avant « Tout le reste »");
  const reste = d.getElementById("tout-le-reste");
  ok(reste.tagName === "DETAILS" && !reste.open && reste.querySelectorAll(".carte").length === 24, `les 24 tuiles restent, repliées sous « Tout le reste » (${reste.querySelectorAll(".carte").length})`);
  ok(reste.querySelector("table tbody tr") && reste.querySelector("#filtre"), "le tableau jeu par jeu est toujours là");
  ok(/Période 2 .*Année A/.test(d.getElementById("periode").textContent), "période 2, année A (2026-2027)");
  const puces = [...d.querySelectorAll("#choix-jeux button")];
  ok(puces.length === 3 && puces[0].getAttribute("aria-pressed") === "true", "jeux prévus au calendrier, le premier choisi (" + puces.map(b => b.textContent.trim()).join(" / ") + ")");
  await attendreQue(() => d.querySelectorAll("#choix-grade option").length > 1, 2000);
  ok(d.querySelectorAll("#choix-grade option").length === 6, "niveau : au choix des équipes + 5 grades");
  ok(/non lancé/.test(d.getElementById("feu").textContent) && d.querySelector("#feu .voyant.orange .action"), "sans serveur : feu orange avec l'action à faire");
  puces[2].click(); await dodo(150);
  ok(r.w.__portail.jeu === "lumiere", "choix d'un autre jeu prévu en un clic");
  const g = d.getElementById("choix-grade"); g.value = "matelot"; g.dispatchEvent(new r.w.Event("change"));
  d.getElementById("btn-lancer").click(); await dodo(150);
  ok(!d.getElementById("lien-eleves").hidden && /\?jeu=lumiere&grade=matelot/.test(d.getElementById("lien-eleves").textContent), "Lancer sans serveur : lien ?jeu= pour les élèves");
  r.w.location.hash = "#apres"; r.w.dispatchEvent(new r.w.HashChangeEvent("hashchange")); await dodo(60);
  ok(reste.open, "un lien vers une ressource (#apres) ouvre « Tout le reste »");
  ok(r.erreurs.length === 0, "erreurs JS : " + r.erreurs.join(" | "));

  console.log("   … avec le serveur local");
  let seance = null;
  const routes = {
    "/api/seance": (m, b) => { if(m === "POST"){ seance = b.fin ? null : Object.assign({ depuis: "2026-11-17T09:05:00", adresse: "immersifs/" + b.jeu + "/" }, b); return { ok: true, seance }; } return { ok: true, local: true, seance }; },
    "/api/sante": () => ({ ok: true, etat: "orange", voyants: [
      { id: "serveur", nom: "Serveur", etat: "vert", message: "Le serveur répond.", action: "" },
      { id: "version", nom: "Version", etat: "orange", message: "Une version plus récente existe.", action: "Fermez la session." },
      { id: "medias", nom: "Médias du jeu du jour", etat: "vert", message: "Tous les médias sont là.", action: "" },
      { id: "resultats", nom: "Dossier des résultats", etat: "rouge", message: "Impossible d'écrire.", action: "Vérifiez dossier-donnees.txt." }] }),
    "/api/info": () => ({ ip: "192.168.1.23", port: 8000, local: true })
  };
  r = await charger(RACINE, "", { page: "enseignant.html", attente: 700, avant: avecDate("2026-11-17T10:00:00", serveur(routes)) });
  d = r.w.document;
  await attendreQue(() => d.querySelectorAll("#feu .voyant").length === 4, 2000);
  ok(d.querySelectorAll("#feu .voyant.vert").length === 2 && d.querySelectorAll("#feu .voyant.orange").length === 1 && d.querySelectorAll("#feu .voyant.rouge").length === 1, "feu vert : 4 voyants (vert, orange, rouge)");
  ok(/Fermez la session/.test(d.querySelector("#feu .voyant.orange").textContent) && /dossier-donnees/.test(d.querySelector("#feu .voyant.rouge").textContent), "chaque orange ou rouge dit quoi faire");
  ok(/Aucune séance lancée/.test(d.getElementById("etat-seance").textContent), "pas encore de séance");
  d.getElementById("btn-lancer").click(); await dodo(200);
  const post = r.w.__appels.find(x => x.route === "/api/seance" && x.methode === "POST");
  ok(post && post.corps.jeu === "versailles", "Lancer : séance du jour fixée sur le serveur (" + (post && post.corps.jeu) + ")");
  ok(/Séance en cours/.test(d.getElementById("etat-seance").textContent) && d.getElementById("lien-eleves").hidden, "séance en cours affichée");
  d.getElementById("btn-terminer").click(); await dodo(200);
  ok(r.w.__appels.some(x => x.route === "/api/seance" && x.corps && x.corps.fin) && r.w.__termine.jeu === "versailles" && seance === null && r.w.__ouverts.includes("resultats.html?fin=versailles"), "Terminer : fin de la séance (bilan ouvert dans resultats.html?fin=)");
  d.getElementById("btn-preparer").click(); await dodo(100);
  ok(r.w.__appels.filter(x => x.route === "/api/sante").length >= 2 && r.w.__ouverts.some(u => /^pack-impression\.html\?jeu=versailles/.test(u)), "Préparer : feu vert revérifié (et pack d'impression ouvert)");
  ok(r.erreurs.length === 0, "erreurs JS : " + r.erreurs.join(" | "));
};

SECTIONS.B2 = async () => {
  console.log("\n== B2 : pack d'impression ==");
  const r = await charger(RACINE, "?jeu=lumiere&grade=matelot", { page: "pack-impression.html", attente: 900 });
  const d = r.w.document;
  await attendreQue(() => r.w.__pack, 2000);
  ok(d.querySelectorAll("#documents .feuille.fiche").length === 6 && d.querySelectorAll(".feuille.fiche")[0].querySelectorAll(".case").length === 5, "fiche de mission : 6 exemplaires, 5 étapes");
  ok(r.w.__pack.niveau === "CM1" && /lumiere\/lecons-imprimables\.html\?niveau=CM1/.test(r.w.__pack.lecons), "leçons A4 du niveau choisi (Veilleur → CM1)");
  ok(d.querySelector(".feuille.eval") && d.querySelectorAll(".feuille.eval ol.qcm li").length >= 10 && /Niveau CM1/.test(d.querySelector(".feuille.eval").textContent), "évaluation CM1 fabriquée à partir de evaluations.json");
  ok(d.querySelector(".feuille.corrige-prof"), "corrigé à part (jamais imprimé pour les élèves)");
  ok(d.querySelectorAll("#docs li").length === 3 && d.querySelectorAll("#docs li").length === [...d.querySelectorAll("#docs li")].filter(li => /✅/.test(li.textContent)).length, "les trois documents sont prêts");
  d.getElementById("tout-imprimer").click(); await dodo(150);
  ok(r.w.__imprime >= 1 && (r.w.__cadres || []).some(u => /lecons-imprimables/.test(u)), "un bouton : fiche + évaluation imprimées, puis les leçons");
  const g = d.getElementById("choix-grade"); g.value = "second"; g.dispatchEvent(new r.w.Event("change")); await dodo(400);
  ok(r.w.__pack.niveau === "CM2" && /niveau=CM2/.test(r.w.__pack.lecons) && /Niveau CM2/.test(d.querySelector(".feuille.eval").textContent), "grade Second → leçons et évaluation CM2");
  const j = d.getElementById("choix-jeu"); j.value = "grande-guerre"; j.dispatchEvent(new r.w.Event("change")); await dodo(500);
  ok(/immersifs\/grande-guerre\/lecons-imprimables\.html/.test(r.w.__pack.lecons) && /⚠️/.test(d.getElementById("docs").textContent), "jeu sans leçons A4 classiques : fiches de la variante immersive ; évaluation absente signalée");
  ok(r.erreurs.length === 0, "erreurs JS : " + r.erreurs.join(" | "));
};

SECTIONS.A5 = async () => {
  console.log("\n== A5 : fin de séance en un clic (bilan + passeport) ==");
  const page = await charger(RACINE, "", { page: "tableau.html", attente: 100 });
  // règles de mise à jour du passeport (module seul)
  const code = fs.readFileSync(path.join(RACINE, "commun/js/fin-seance.js"), "utf8");
  page.w.eval(code);
  const F = page.w.FIN_SEANCE;
  ok(F.elevesDe("Les Lynx", ["Léa B.", "Tom R."], { "les lynx": ["Léa B.", "Tom R."] }).length === 2, "équipe : composition connue");
  ok(F.elevesDe("Léa et Tom", ["Léa B.", "Tom R.", "Inès M."], {}).join(",") === "Léa B.,Tom R.", "équipe nommée par les prénoms (« Léa et Tom »)");
  const comps = [{ cle: "melanges|1", lecon: "L1" }, { cle: "melanges|2", lecon: "L2" }, { cle: "melanges|3", lecon: "L3" }];
  const partie = { jeu: "melanges", eleve: "Les Lynx", mode: "equipe", termine: true, date: "2026-11-17T10:00", score: 90, scoreMax: 100,
    detail: [{ id: "a", l: "L1", pc: 1 }, { id: "b", l: "L1", pc: 1 }, { id: "c", l: "L2", pc: 1 }, { id: "d", l: "L2", pc: 0 }, { id: "e", l: "L2", pc: 0 }] };
  const res = F.majPasseport({ parties: [partie], jeu: "melanges", competences: comps, compositions: { "Les Lynx": ["Léa B.", "Tom R."] },
    passeport: { eleves: ["Léa B.", "Tom R."], notes: { "Tom R.": { "melanges|1": { v: "N", date: "2026-11-01" } } } }, jour: "2026-11-17" });
  const n = res.passeport.notes;
  ok(n["Léa B."]["melanges|1"].v === "A" && n["Léa B."]["melanges|2"].v === "N" && !n["Léa B."]["melanges|3"], "par leçon : 100 % → Acquis, 33 % → Non acquis, leçon non jouée → rien");
  ok(n["Tom R."]["melanges|1"].v === "N" && !n["Tom R."]["melanges|1"].src && res.gardees === 1, "une note posée à la main n'est jamais remplacée");
  ok(n["Léa B."]["melanges|1"].src === "seance" && res.ajoutees === 3, "notes proposées repérables (src « seance »)");
  const res2 = F.majPasseport({ parties: [Object.assign({}, partie, { detail: null, score: 50 })], jeu: "melanges", competences: comps, compositions: {},
    passeport: { eleves: ["Les Lynx"], notes: {} } });
  ok(Object.values(res2.passeport.notes["Les Lynx"]).every(x => x.v === "E") && res2.ajoutees === 3, "sans détail : score global (50 % → En cours)");

  // page complète : resultats.html?fin=<jeu>
  const jour = new Date().toISOString().slice(0, 10);
  const parties = [
    { type: "escape-game-compte-rendu", jeu: "melanges", titre: "Le Laboratoire", eleve: "Léa B.", mode: "equipe", niveau: "CM2", date: jour + "T09:10", partie: jour + "T09:10", termine: true, dureeMin: 40, score: 200, scoreMax: 235, enigmes: 20, total: 20, premierCoup: 17, erreurs: 3, indices: 1 },
    { type: "escape-game-compte-rendu", jeu: "melanges", titre: "Le Laboratoire", eleve: "Les Fioles", mode: "equipe", niveau: "CM1", date: jour + "T09:12", partie: jour + "T09:12", termine: false, dureeMin: 35, score: 60, scoreMax: 175, enigmes: 8, total: 15, premierCoup: 5, erreurs: 6, indices: 2 }
  ];
  const r = await charger(RACINE, "?fin=melanges", { page: "resultats.html", attente: 1500, stockage: {
    escape_resultats: JSON.stringify(parties), escape_passeport: JSON.stringify({ eleves: ["Léa B.", "Tom R."], notes: {} }) } });
  await attendreQue(() => r.w.__finSeance, 4000);
  const f = r.w.__finSeance || {};
  ok(f.ok && /^rapport-seance-\d{4}-\d\d-\d\d-.*\.pdf$/.test(f.pdf || ""), "bilan de séance : PDF fabriqué (" + f.pdf + ")");
  ok(!r.w.document.getElementById("fin-seance").hidden && /2 équipe\(s\), 1 terminée\(s\), 1 interrompue/.test(r.w.document.getElementById("fin-contenu").textContent), "résumé de la séance affiché");
  const pass = JSON.parse(r.w.localStorage.getItem("escape_passeport"));
  ok(Object.keys(pass.notes["Léa B."] || {}).length === 5 && Object.values(pass.notes["Léa B."]).every(x => x.v === "A"), "passeport mis à jour : 5 compétences de Léa (85 % → Acquis)");
  ok(f.passeport && f.passeport.equipesSansEleve.join(",") === "Les Fioles", "équipe non reconnue signalée");
  ok(r.erreurs.length === 0, "erreurs JS : " + r.erreurs.join(" | "));
};

(async () => {
  const demandees = process.argv.slice(2).map(x => x.toUpperCase());
  for(const [nom, f] of Object.entries(SECTIONS)){
    if(demandees.length && !demandees.includes(nom)) continue;
    try{ await f(); }catch(e){ T.exception(e); }
  }
  T.fin();
})();
