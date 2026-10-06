/* ============================================================
   TEST DU MIGRATEUR (outils/immersif/migrer-jeu.py)
   ------------------------------------------------------------
   · le jeu d'origine n'est JAMAIS modifié (empreintes avant/après) ;
   · la variante est complète : moteur, données converties, rapport, plan de médias, lanceur ;
   · aucune fuite du thème « Vingt mille lieues » ; grades et vocabulaire du thème ;
   · refus des cas dangereux (sortie = source, structure inconnue, sortie existante) ;
   · la variante se joue de bout en bout (test-immersif.js).
   Usage : node vingt-mille-lieues/tests/test-migration.js [jeu]   (défaut : renaissance)
   ============================================================ */
const path = require("path"), fs = require("fs"), os = require("os"), crypto = require("crypto");
const { spawnSync } = require("child_process");
const OUTILS = path.resolve(__dirname, "../../outils-tests");
const { compteur } = require(path.join(OUTILS, "charge"));
const { ok, fin } = compteur("Migrateur de jeux");
const RACINE = path.resolve(__dirname, "../..");
const MIGRER = path.join(RACINE, "vingt-mille-lieues", "outils", "immersif", "migrer-jeu.py");
const py = ["python3", "python"].find(p => spawnSync(p, ["--version"]).status === 0);
const jeu = process.argv[2] || "renaissance";

const empreinte = dossier => {
  const h = crypto.createHash("sha1");
  const marche = d => fs.readdirSync(d, { withFileTypes: true }).sort((a, b) => a.name.localeCompare(b.name)).forEach(e => {
    const p = path.join(d, e.name);
    if(e.isDirectory()){ if(e.name !== "node_modules") marche(p); } else { h.update(path.relative(dossier, p)); h.update(fs.readFileSync(p)); }
  });
  marche(dossier);
  return h.digest("hex");
};
const lancer = (...args) => spawnSync(py, [MIGRER, ...args], { encoding: "utf8" });

if(!py){ ok(true, "Python absent : étape ignorée"); fin(); process.exit(0); }
const tmp = path.join(RACINE, "immersifs", "_test-migration-" + process.pid);   // dans le dépôt : les liens vers commun/ doivent exister
const sortie = path.join(tmp, jeu);
fs.mkdirSync(tmp, { recursive: true });
try{
  const avant = empreinte(path.join(RACINE, jeu));
  const l = lancer("--lister");
  ok(l.status === 0 && l.stdout.split("\n").includes(jeu), `--lister : « ${jeu} » est migrable`);
  const r = lancer(jeu, "--vers", sortie);
  ok(r.status === 0, "migration réussie : " + (r.stdout || r.stderr).split("\n")[0]);
  ok(empreinte(path.join(RACINE, jeu)) === avant, `le jeu d'origine « ${jeu} » est strictement inchangé`);
  for(const f of ["index.html", "prof.html", "medias.html", "lecons-imprimables.html", "sw.js", "manifest.webmanifest", "lancer.bat", "medias.csv", "MIGRATION-RAPPORT.md",
                  "js/jeu-config.js", "js/app.js", "js/scene.js", "css/nautilus.css", "css/theme.css", "assets/data/enigmes.json", "assets/data/lecons.json", "assets/data/dialogues.json",
                  "assets/data/decors-fx.json", "assets/data/personnages.json", "outils/medias/produire.py", "outils/medias/importer-image.py", "outils/medias/sources-medias.json",
                  "outils/embarquer-donnees.py", "tests/test-immersif.js", "tests/solveurs.js"])
    ok(fs.existsSync(path.join(sortie, f)), `variante : ${f} présent`);
  ok(!fs.existsSync(path.join(sortie, "assets/images/decors/salon.webp")) && !fs.existsSync(path.join(sortie, "references")), "aucune image ni référence du jeu Nautilus copiée");
  const E = JSON.parse(fs.readFileSync(path.join(sortie, "assets/data/enigmes.json"), "utf8"));
  const cfg = (() => { const c = {}; new Function("window", fs.readFileSync(path.join(sortie, "js/jeu-config.js"), "utf8"))(c); return c.VML_JEU; })();
  const ancien = JSON.parse(fs.readFileSync(path.join(RACINE, jeu, "assets/data/enigmes.json"), "utf8"));
  ok(E.escales.length === ancien.salles.length, `${E.escales.length} étapes = ${ancien.salles.length} salles du jeu d'origine`);
  ok(E.escales.reduce((t, e) => t + e.enigmes.length, 0) === ancien.salles.reduce((t, s) => t + s.enigmes.length, 0), "toutes les énigmes sont reprises");
  ok(cfg.grades.join() === "matelot,timonier" && E.niveaux.map(n => n.id).join() === "matelot,timonier", "grades : CM1 → matelot, CM2 → timonier");
  ok(cfg.id === jeu && cfg.prefixeStockage !== "vml" && cfg.textes.titre === ancien.metadata.jeu, "identité propre : clé de sauvegarde distincte de celle de Nautilus, titre du jeu d'origine");
  ok(cfg.mots.escale === "salle", "vocabulaire du thème : « salle » à la place d'« escale »");
  const cm2seul = E.escales.flatMap(e => e.enigmes).filter(e => e.niveaux && e.niveaux.join() === "timonier");
  ok(cm2seul.length >= 1 && cm2seul.every(e => !e.matelot && e.timonier), "énigmes réservées au CM2 : un seul bloc (timonier), filtrées au grade matelot");
  const csv = fs.readFileSync(path.join(sortie, "medias.csv"), "utf8").split("\n").filter(Boolean);
  ok(csv.length > 10 && /decor-/.test(csv.join("\n")) && /portrait-/.test(csv.join("\n")) && /video-transition-e1/.test(csv.join("\n")), `medias.csv : ${csv.length - 1} médias à produire (décors, portraits, vidéos)`);
  const rapport = fs.readFileSync(path.join(sortie, "MIGRATION-RAPPORT.md"), "utf8");
  ok(/Zones des décors/.test(rapport) && /Enjeu et réaction/.test(rapport) && /produire\.py/.test(rapport), "rapport : liste ce qu'il reste à faire");
  /* mise à jour du moteur seul : le travail de l'enseignant est conservé */
  fs.appendFileSync(path.join(sortie, "js/moteur.js"), "\n// modification locale du moteur\n");
  const dl = path.join(sortie, "assets/data/dialogues.json");
  const dd = JSON.parse(fs.readFileSync(dl, "utf8")); dd.accueil.texte = "TEXTE RÉÉCRIT PAR L'ENSEIGNANT"; fs.writeFileSync(dl, JSON.stringify(dd, null, 2));
  const maj = lancer("--maj-moteur", sortie);
  ok(maj.status === 0 && /mis à jour/.test(maj.stdout), "--maj-moteur : " + (maj.stdout || maj.stderr).trim().slice(0, 90));
  ok(!/modification locale du moteur/.test(fs.readFileSync(path.join(sortie, "js/moteur.js"), "utf8")), "--maj-moteur : le moteur est remis à l'état du modèle");
  ok(JSON.parse(fs.readFileSync(dl, "utf8")).accueil.texte === "TEXTE RÉÉCRIT PAR L'ENSEIGNANT", "--maj-moteur : les données de l'enseignant sont conservées");
  ok(fs.readFileSync(path.join(sortie, "js/donnees-embarquees.js"), "utf8").includes("TEXTE RÉÉCRIT PAR L'ENSEIGNANT"), "--maj-moteur : la copie embarquée des données est régénérée");
  /* refus des cas dangereux */
  const memeSortie = lancer(jeu, "--vers", path.join(RACINE, jeu));
  ok(memeSortie.status !== 0 && /non destructive/.test(memeSortie.stderr), "refuse d'écrire dans le jeu d'origine");
  const existe = lancer(jeu, "--vers", sortie);
  ok(existe.status !== 0 && /--force/.test(existe.stderr), "refuse d'écraser une sortie existante sans --force");
  const inconnu = lancer("declaration");
  ok(inconnu.status !== 0 && /structure attendue/.test(inconnu.stderr), "jeu à structure ancienne : message clair, rien d'écrit");
  ok(!fs.existsSync(path.join(RACINE, "immersifs", "declaration")), "aucun dossier créé pour un jeu non migrable");
  /* la variante se joue */
  const t = spawnSync("node", [path.join(sortie, "tests", "test-immersif.js")], { encoding: "utf8", env: Object.assign({}, process.env, { OUTILS_TESTS: OUTILS }), timeout: 280000 });
  const m = (t.stdout || "").match(/(\d+) vérifications réussies, (\d+) échec/);
  ok(!!m && +m[2] === 0, `la variante se joue de bout en bout : ${m ? m[1] + " vérifications, " + m[2] + " échec(s)" : (t.stdout || t.stderr).slice(-300)}`);
}catch(e){ ok(false, "EXCEPTION " + e.message); }
finally{ fs.rmSync(tmp, { recursive: true, force: true }); try{ if(!fs.readdirSync(path.join(RACINE, "immersifs")).length) fs.rmdirSync(path.join(RACINE, "immersifs")); }catch(e){} }
fin();
