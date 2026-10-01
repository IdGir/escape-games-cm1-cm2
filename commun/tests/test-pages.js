/* ============================================================
   TESTS DES PAGES COMMUNES (Node + jsdom)
   Depuis la racine du dépôt :  node commun/tests/test-pages.js
   classement.html (D1) et les pages publiques ajoutées ensuite.
   Étapes au choix : node commun/tests/test-pages.js D1
   ============================================================ */
const { charger, compteur, dodo, attendreQue, RACINE } = require("../../outils-tests/charge");
const T = compteur("Pages communes"); const ok = T.ok;
const SECTIONS = {};

/** Simule le serveur local : /api/equipes renvoie les équipes données. */
const avecEquipes = equipes => w => {
  const f = w.fetch;
  w.fetch = async (url, o) => /\/api\/equipes/.test(String(url))
    ? { ok: true, status: 200, json: async () => ({ equipes }), text: async () => "" } : f(url, o);
};

SECTIONS.D1 = async () => {
  console.log("\n== D1 : écran de classement ==");
  const equipes = [
    { equipe: "Les Lynx", jeu: "melanges", niveau: "CM2", salle: 3, enigme: 1, score: 60, msEcoules: 900000 },
    { equipe: "Les Hiboux", jeu: "melanges", niveau: "CM1", salle: 4, enigme: 0, score: 40, msEcoules: 800000, palier: "decouverte" },
    { equipe: "Les Renards", jeu: "melanges", niveau: "CM2", salle: 5, score: 150, fini: true, msEcoules: 1800000 },
    { equipe: "Autre jeu", jeu: "declaration", niveau: "CM2", salle: 2, score: 20 }
  ];
  const { w, erreurs } = await charger(RACINE, "?jeu=melanges", { page: "classement.html", avant: avecEquipes(equipes), attente: 400 });
  await attendreQue(() => w.document.querySelectorAll("#liste li").length, 3000);
  const noms = [...w.document.querySelectorAll("#liste li .nom")].map(n => n.firstChild.textContent);
  ok(noms.length === 3, `seulement les équipes du jeu choisi (${noms.length})`);
  ok(noms.join(",") === "Les Renards,Les Hiboux,Les Lynx", "classé par progression : " + noms.join(", "));
  ok(!/⭐/.test(w.document.getElementById("liste").textContent), "affichage par défaut : progression, sans les scores");
  ok(/🌱/.test(w.document.getElementById("liste").textContent), "palier Découverte signalé");
  const a = w.document.getElementById("choix-affichage"); a.value = "score"; a.dispatchEvent(new w.Event("change"));
  await dodo(100);
  const noms2 = [...w.document.querySelectorAll("#liste li .nom")].map(n => n.firstChild.textContent);
  ok(noms2.join(",") === "Les Renards,Les Lynx,Les Hiboux" && /⭐/.test(w.document.getElementById("liste").textContent), "classé par score : " + noms2.join(", "));
  ok(!w.document.querySelector("button[onclick], .actions"), "aucune commande de pilotage sur l'écran de projection");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
  const sans = await charger(RACINE, "", { page: "classement.html", attente: 400 });
  ok(/lancer\.bat/.test(sans.w.document.getElementById("vide").textContent), "sans serveur : message explicatif");
};

SECTIONS.D5 = async () => {
  console.log("\n== D5 : résultats de la classe (resultats.html) ==");
  const path = require("path");
  // deux comptes-rendus fabriqués par un vrai jeu
  const jeu = await charger(path.join(RACINE, "objets-techniques"), "?salle=6&niveau=CM2", { attente: 600 });
  Object.assign(jeu.w.ETAT, { equipe: "Les Engrenages", score: 180, enigmesPremierCoup: 17, erreursTotal: 3, debut: Date.now() - 2400000, msEcoules: 2400000 });
  const cr1 = jeu.w.COMPTE_RENDU.construire();
  Object.assign(jeu.w.ETAT, { equipe: "Tom R.", solo: true, score: 150, debut: Date.now() - 3000000 });
  const cr2 = jeu.w.COMPTE_RENDU.construire();
  const triche = Object.assign({}, cr2, { eleve: "Zoé K.", score: 235 });     // modifié à la main
  const texte = jeu.w.COMPTE_RENDU.texte(Object.assign({}, cr2, { eleve: "Inès M." }));
  const { w, erreurs } = await charger(RACINE, "", { page: "resultats.html", stockage: { escape_resultats: JSON.stringify([cr1, cr2, triche]) } });
  const d = w.document;
  d.getElementById("btn-appareil").click(); await dodo(50);
  ok(d.querySelectorAll("#corps tr").length === 3, `3 parties de cet appareil (${d.querySelectorAll("#corps tr").length})`);
  ok(d.querySelectorAll("#corps .ok").length === 2 && d.querySelectorAll("#corps .ko").length === 1, "codes de contrôle : 2 vérifiés, 1 modifié repéré");
  d.getElementById("colle").value = "Bonjour maîtresse,\n" + texte + "\nMerci";
  d.getElementById("btn-colle").click(); await dodo(30);
  ok(w.RESULTATS_PAGE.liste.some(r => r.eleve === "Inès M." && r.score === 150 && r.mode === "solo" && r.niveau === "CM2"), "texte collé depuis un message : compte-rendu reconnu");
  const f = d.getElementById("filtre-mode"); f.value = "solo"; f.dispatchEvent(new w.Event("input"));
  ok(d.querySelectorAll("#corps tr").length === 3, "filtre « individuel » : 3 parties");
  d.getElementById("exp-tableur").click();
  const e1 = w.__dernierExport;
  ok(e1 && e1.contenu.startsWith("\ufeffDate;Élève / équipe;") && e1.contenu.split("\r\n").length === 4, "export tableur : CSV point-virgule, 3 lignes (filtre appliqué)");
  d.getElementById("exp-schooly").click();
  ok(w.__dernierExport.contenu.startsWith("\ufeffeleve;date;matiere;activite;niveau;note;note_max;pourcentage;observation") && /Tom R\.;\d{4}-\d\d-\d\d;Sciences;Escape game : L'Atelier de l'inventeur;CM2;150;235;64;/.test(w.__dernierExport.contenu), "export Schooly : une ligne par élève et par partie");
  ok(erreurs.length === 0 && jeu.erreurs.length === 0, "erreurs JS : " + erreurs.concat(jeu.erreurs).join(" | "));
  const fs = require("fs");
  ok(/resultats-classe\.jsonl/.test(fs.readFileSync(path.join(RACINE, ".gitignore"), "utf8")), "resultats-classe.jsonl jamais publié (.gitignore)");
};

SECTIONS.B3 = async () => {
  console.log("\n== B3 : frise de l'année sur l'accueil ==");
  const { w, erreurs } = await charger(RACINE, "", { page: "index.html", attente: 300 });
  const d = w.document, C = w.eval("CATALOGUE");
  const puces = d.querySelectorAll("#frise .frise-jeu");
  ok(puces.length === C.jeux.length, `les ${C.jeux.length} jeux du catalogue sont sur la frise (${puces.length})`);
  const liens = [...d.querySelectorAll("#frise a.frise-jeu")].map(a => a.getAttribute("href"));
  ok(liens.length === C.jeux.filter(j => j.dossier).length && liens.every(h => require("fs").existsSync(require("path").join(RACINE, h, "index.html"))), `jeux disponibles en lien vers leur dossier (${liens.length})`);
  ok(d.querySelectorAll("#frise .frise-jeu.avenir").length === C.jeux.filter(j => !j.dossier).length, "jeux à venir en grisé");
  const a01 = d.querySelector('#frise [data-jeu="moyen-age-abbaye"]');
  ok(a01 && a01.closest(".frise-case").dataset.periode === "P1 · Année A", "Le Manuscrit de l'abbaye : P1, Année A");
  d.querySelector('.choix-annee[data-annee="B"]').click();
  ok(!d.querySelector('#frise [data-jeu="moyen-age-abbaye"]') && !!d.querySelector('#frise [data-jeu="chateau-fort"]'), "filtre Année B");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
};

module.exports = { SECTIONS, avecEquipes };
if (require.main === module) {
  const choix = process.argv[2] ? process.argv[2].split(",") : Object.keys(SECTIONS);
  (async () => { try { for (const s of choix) await SECTIONS[s](); } catch (e) { T.exception(e); } T.fin(); })();
}
