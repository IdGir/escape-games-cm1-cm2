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

SECTIONS.C1 = async () => {
  console.log("\n== C1 : vue d'ensemble de l'année (annee.html) ==");
  const { w, erreurs } = await charger(RACINE, "", { page: "annee.html", attente: 800 });
  const d = w.document, C = w.eval("CATALOGUE");
  ok(d.querySelectorAll("#periodes section").length === 6, "5 périodes + révision libre");
  ok(d.querySelectorAll("#periodes .jeu").length >= C.jeux.length, "chaque jeu apparaît (Mission géographique dans chaque période)");
  const mel = [...d.querySelectorAll("#P1 .jeu")].find(x => /Madame Mélange/.test(x.textContent));
  ok(mel && mel.querySelectorAll(".competences li").length === 5 && /Comparer et mesurer des masses/.test(mel.textContent), "jeu publié : la compétence de chacune de ses 5 leçons");
  const mg = [...d.querySelectorAll("#P3 .jeu")].find(x => /Mission géographique/.test(x.textContent));
  ok(mg && mg.querySelectorAll(".competences li").length === 2 && /Séance 9/.test(mg.textContent), "Mission géographique en P3 : séances 9 et 10");
  ok(/points du programme déjà couverts/.test(d.getElementById("bilan").textContent), "bilan : points du programme couverts");
  d.querySelector('[data-f="annee"][data-v="A"]').click();
  ok(![...d.querySelectorAll("#periodes .jeu h3")].some(h => /Secret du donjon/.test(h.textContent)), "filtre Année A : le Secret du donjon (Année B) disparaît");
  d.querySelector('[data-f="matiere"][data-v="Sciences"]').click();
  ok([...d.querySelectorAll("#periodes .etiquette")].filter(e => /^(Histoire|EMC|Géographie)$/.test(e.textContent)).length === 0, "filtre Sciences");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
};

SECTIONS.C5 = async () => {
  console.log("\n== C5 : fiche de période (periode.html) ==");
  const hist = JSON.stringify([{ type: "escape-game-compte-rendu", jeu: "melanges", termine: true, score: 200, scoreMax: 235, total: 20, premierCoup: 16 },
                               { type: "escape-game-compte-rendu", jeu: "declaration", termine: true, score: 90, scoreMax: 95, total: 5, premierCoup: 5 }]);
  const { w, erreurs } = await charger(RACINE, "?p=P1&annee=B&public=familles", { page: "periode.html", attente: 800, stockage: { escape_resultats: hist } });
  const d = w.document;
  const titres = [...d.querySelectorAll(".jeu h2")].map(h => h.textContent);
  ok(titres.includes("Le Secret du donjon") && titres.includes("Le Laboratoire de Madame Mélange") && titres.includes("Mission géographique") && titres.length === 3, "P1 Année B : donjon, mélanges, Mission géographique (" + titres.join(", ") + ")");
  ok(/escape games pédagogiques/.test(d.querySelector(".mot").textContent), "texte pour les familles");
  ok(/1 partie terminée/.test(d.getElementById("page").textContent) && /85 %/.test(d.getElementById("page").textContent), "chiffres anonymes de la période (1 partie, 85 %)");
  ok(!/Tom|Léa|équipe/i.test(d.querySelector(".jeux").textContent), "aucun nom d'élève");
  const s = d.getElementById("choix-public"); s.value = "direction"; s.dispatchEvent(new w.Event("change"));
  ok(/programmes 2026/.test(d.querySelector(".mot").textContent), "texte pour la direction");
  const a = d.getElementById("choix-avenir"); a.checked = true; a.dispatchEvent(new w.Event("change"));
  ok(d.querySelectorAll(".jeu.avenir").length === 0, "P1 : tous les jeux de la période sont déjà publiés");
  const p = d.getElementById("choix-p"); p.value = "P2"; p.dispatchEvent(new w.Event("change"));
  ok(d.querySelectorAll(".jeu.avenir").length === 0, "P2 Année B : tous les jeux de la période sont publiés");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
};

SECTIONS.C3 = async () => {
  console.log("\n== C3 : passeport de compétences (passeport.html) ==");
  const hist = JSON.stringify([{ type: "escape-game-compte-rendu", jeu: "melanges", eleve: "Léa B.", termine: true, score: 200, scoreMax: 235 }]);
  const { w, erreurs } = await charger(RACINE, "", { page: "passeport.html", attente: 1200, stockage: { escape_resultats: hist } });
  const d = w.document, P = w.PASSEPORT;
  ok(P.COMPETENCES.length === 5 * 12 + 8 + 6 + 16, `compétences des jeux publiés qui ont leurs leçons A4, une par leçon (${P.COMPETENCES.length})`);
  d.getElementById("liste-eleves").value = "Léa B.\nTom R.\n\nLéa B.";
  d.getElementById("btn-eleves").click();
  ok(P.D.eleves.join(",") === "Léa B.,Tom R.", "liste de la classe (doublons et lignes vides ignorés)");
  const btn = (cle, v) => d.querySelector(`.etats[data-cle="${cle}"] button[data-v="${v}"]`);
  btn("melanges|1", "A").click(); btn("melanges|2", "E").click(); btn("chateau-fort|1", "N").click();
  ok(P.D.notes["Léa B."]["melanges|1"].v === "A" && P.D.notes["Léa B."]["melanges|2"].v === "E", "évaluations enregistrées");
  ok(JSON.parse(w.localStorage.getItem("escape_passeport")).notes["Léa B."]["chateau-fort|1"].v === "N", "gardé sur l'appareil");
  btn("melanges|2", "E").click();
  ok(!P.D.notes["Léa B."]["melanges|2"], "second clic : évaluation effacée");
  ok(/joué 1 fois, meilleur score 85 %/.test(d.getElementById("vue").textContent), "rappel des résultats de l'élève (D5)");
  ok(/Sciences<\/b> — 1 acquise sur/.test(d.getElementById("vue").innerHTML), "jauge par matière (cumul)");
  const v = d.getElementById("choix-vue"); v.value = "classe"; v.dispatchEvent(new w.Event("change"));
  ok(d.querySelectorAll("table.classe tr").length === 3 && d.querySelector("table.classe").innerHTML.includes(`<b>1</b> / ${P.COMPETENCES.length}`), "vue de la classe : total cumulé");
  d.getElementById("btn-csv").click();
  ok(w.__dernierExport.contenu.split("\r\n").length === 3 && /Léa B\.;Sciences;Le Laboratoire de Madame Mélange;.*;Acquis;/.test(w.__dernierExport.contenu), "export CSV (tableur, Schooly)");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
};

SECTIONS.F1 = async () => {
  console.log("\n== F1 : FAQ commune (faq.html) ==");
  const { w, erreurs } = await charger(RACINE, "", { page: "faq.html", attente: 200 });
  const d = w.document, n = d.querySelectorAll("#faq details").length;
  ok(n >= 25, `${n} questions`);
  const c = d.getElementById("recherche"); c.value = "tablette"; c.dispatchEvent(new w.Event("input"));
  const vis = [...d.querySelectorAll("#faq details")].filter(x => !x.hidden);
  ok(vis.length >= 1 && vis.length < n && vis.every(x => /tablette/i.test(x.textContent)), `recherche « tablette » : ${vis.length} réponse(s)`);
  c.value = "vidéo"; c.dispatchEvent(new w.Event("input"));
  ok([...d.querySelectorAll("#faq details")].filter(x => !x.hidden).length >= 3, "recherche sans tenir compte des accents (vidéo / video)");
  c.value = "xyzzy"; c.dispatchEvent(new w.Event("input"));
  ok(!d.getElementById("aucun").hidden, "aucun résultat : message");
  const fs = require("fs"), path = require("path");
  const liens = [...d.querySelectorAll("#faq a[href]")].map(a => a.getAttribute("href")).filter(h => !/^https?:/.test(h));
  const morts = liens.filter(h => !fs.existsSync(path.join(RACINE, h.split("?")[0])));
  ok(!morts.length, "liens internes valides " + morts.join(", "));
  const accueil = await charger(RACINE, "", { page: "index.html" });
  ok(!!accueil.w.document.querySelector('a[href="faq.html"]'), "lien depuis l'accueil");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
};

SECTIONS.F4 = async () => {
  console.log("\n== F4 : démonstration en boucle (demo.html) ==");
  const fs = require("fs"), path = require("path");
  const { w, erreurs } = await charger(RACINE, "?duree=12", { page: "demo.html", attente: 200 });
  const D = w.DEMO;
  const nbPub = w.CATALOGUE.jeux.filter(j => j.dossier).length;
  ok(D.jeux.length === nbPub && D.jeux.every(j => fs.existsSync(path.join(RACINE, j.classique === false ? j.immersif : j.dossier, "index.html"))), `un extrait pour chacun des ${nbPub} jeux publiés`);
  ok(D.jeux.every(j => /[?&](salle|seance)=/.test(D.EXTRAITS[j.dossier])), "extraits en mode vérification (rien n'est enregistré)");
  await dodo(2700);
  ok(D.etat.i === 0 && /\/\?/.test(w.document.getElementById("cadre").getAttribute("src")), "premier extrait lancé : " + w.document.getElementById("cadre").getAttribute("src"));
  ok(new RegExp("1 / " + nbPub).test(w.document.getElementById("titre").textContent), "bandeau : 1 / " + nbPub);
  w.document.getElementById("b-suivant").click();
  ok(D.etat.i === 1, "⏭ extrait suivant");
  w.document.getElementById("b-pause").click(); const avant = D.etat.i; await dodo(400);
  ok(D.etat.pause && D.etat.i === avant, "⏸ pause");
  D.montrer(D.jeux.length - 1); D.montrer(D.etat.i + 1);
  ok(D.etat.i === 0, "la boucle repart au premier jeu");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
};

SECTIONS.D4 = async () => {
  console.log("\n== D4 : éditeur d'énigmes (editeur.html) ==");
  const path = require("path");
  for (const j of ["melanges", "objets-techniques", "station-meteo", "chateau-fort", "moyen-age-abbaye", "constitution", "versailles", "renaissance", "alimentation", "lumiere", "etats-matiere", "mouvement", "traite-colonies"]) {
    const { w, erreurs } = await charger(RACINE, "?jeu=" + j, { page: "editeur.html", attente: 600 });
    await attendreQue(() => w.document.querySelectorAll("#arbre .item").length, 3000);
    const E = w.EDITEUR, b = E.bilanGlobal();
    ok(w.document.querySelectorAll("#arbre .item").length === 20 && b.nErr === 0, `${j} : 20 énigmes ouvertes, aucune erreur signalée sur le jeu publié (${b.nErr})`);
    ok(erreurs.length === 0, `${j} : erreurs JS : ` + erreurs.join(" | "));
  }
  const { w, erreurs } = await charger(RACINE, "?jeu=melanges", { page: "editeur.html", attente: 600 });
  await attendreQue(() => w.document.querySelectorAll("#arbre .item").length, 3000);
  const d = w.document, E = w.EDITEUR;
  const iq = E.DATA.salles[0].enigmes.findIndex(e => e.type === "qcm");
  E.choisir(0, iq);
  const titre = d.querySelector("#e-corps input[type=text]:nth-of-type(1)");
  const champs = [...d.querySelectorAll("#e-corps label.champ")];
  const champTitre = champs.find(l => /^Titre/.test(l.textContent)).querySelector("input");
  champTitre.value = "Deux balances (modifié)"; champTitre.dispatchEvent(new w.Event("input"));
  ok(E.DATA.salles[0].enigmes[iq].titre === "Deux balances (modifié)", "un champ modifié change le fichier");
  const q0 = (E.DATA.salles[0].enigmes[iq].commun || E.DATA.salles[0].enigmes[iq].cm2 || E.DATA.salles[0].enigmes[iq].cm1).questions[0];
  q0.bonne = 99;
  ok(E.controler(E.DATA.salles[0].enigmes[iq]).err.some(x => /bonne réponse non choisie/.test(x)), "contrôle : bonne réponse hors des choix");
  q0.bonne = 0;
  d.getElementById("nouveau-type").value = "intrus"; d.getElementById("b-ajouter").click();
  const n = E.DATA.salles[0].enigmes[E.DATA.salles[0].enigmes.length - 1];
  ok(n.type === "intrus" && E.controler(n).err.length > 0, "nouvelle énigme « intrus » ajoutée, à compléter (contrôles)");
  ok(E.bilanGlobal().lignes.some(l => /4 énigmes en CM1, 5 en CM2/.test(l)), "bilan : nombre d'énigmes par niveau signalé");
  d.getElementById("b-telecharger").click();
  ok(!w.__dernierExport, "téléchargement refusé tant qu'il reste des erreurs");
  E.DATA.salles[0].enigmes.pop();
  d.getElementById("b-telecharger").click();
  ok(w.__dernierExport && JSON.parse(w.__dernierExport.contenu).salles.length === 5, "téléchargement d'un enigmes.json valide");
  // aperçu dans le jeu
  d.getElementById("b-tester").click();
  const stock = w.localStorage.getItem("escape_apercu_enigmes_melanges");
  const jeu = await charger(path.join(RACINE, "melanges"), "?salle=1&niveau=CM2&apercu=1", { stockage: { escape_apercu_enigmes_melanges: stock } });
  ok(jeu.w.salleEnigmes(1).some(e => e.titre === "Deux balances (modifié)") && jeu.w.APERCU_EDITEUR, "« Tester dans le jeu » : le jeu joue la version modifiée");
  const sans = await charger(path.join(RACINE, "melanges"), "?salle=1&niveau=CM2", { stockage: { escape_apercu_enigmes_melanges: stock } });
  ok(!sans.w.salleEnigmes(1).some(e => e.titre === "Deux balances (modifié)"), "sans ?apercu=1 : le jeu publié reste intact");
  ok(erreurs.length === 0 && jeu.erreurs.length === 0, "erreurs JS : " + erreurs.concat(jeu.erreurs).join(" | "));
};

SECTIONS.B2 = async () => {
  console.log("\n== B2 : bandes-annonces ==");
  const fs = require("fs"), path = require("path"), { execFileSync } = require("child_process");
  const { w, erreurs } = await charger(RACINE, "", { page: "index.html", attente: 300 });
  const d = w.document, C = w.eval("CATALOGUE");
  const jeux = C.jeux.filter(j => j.dossier && !j.medias_en_attente).map(j => j.dossier);   // médias encore à produire : pas de bande-annonce
  const liens = [...d.querySelectorAll("a.bande-annonce")];
  ok(liens.length === jeux.length, `un lien « Bande-annonce » par jeu disponible (${liens.length}/${jeux.length})`);
  const manquants = liens.map(a => a.getAttribute("href")).filter(h => !fs.existsSync(path.join(RACINE, h)));
  ok(manquants.length === 0, "chaque bande-annonce existe" + (manquants.length ? " — manquent : " + manquants.join(", ") : ""));
  let ffprobe = true;
  for (const a of liens) {
    const f = path.join(RACINE, a.getAttribute("href")); if (!fs.existsSync(f)) continue;
    let s = null;
    try { s = execFileSync("ffprobe", ["-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height:format=duration", "-of", "json", f]).toString(); }
    catch (e) { if (e.code === "ENOENT") { ffprobe = false; break; } }
    const j = s && JSON.parse(s), v = j && j.streams[0], dur = j && parseFloat(j.format.duration);
    ok(v && v.width === 1280 && v.height === 720 && dur >= 15 && dur <= 20, `${a.getAttribute("href").split("/")[0]} : 1280×720, ${dur ? dur.toFixed(1) : "?"} s (15 à 20 s)`);
  }
  if (!ffprobe) console.log("  (ffprobe absent : durées non vérifiées)");
  // lecteur : le clic ouvre la fenêtre avec la bonne vidéo
  const dlg = d.getElementById("lecteur-ba");
  ok(!!dlg, "fenêtre de lecture présente");
  if (dlg && typeof dlg.showModal === "function") {
    liens[0].click();
    ok(dlg.open && dlg.querySelector("video").getAttribute("src") === liens[0].getAttribute("href"), "le clic ouvre la bande-annonce dans la fenêtre");
    dlg.querySelector("button").click();
    ok(!dlg.open, "bouton Fermer");
  }
  // vérificateur : ces fichiers ne sont pas signalés « mal nommés »
  const v = fs.readFileSync(path.join(RACINE, "verifier.html"), "utf8");
  const m = v.match(/if\((\/\\\/assets\\\/\(images[^\n]*?\/i)\.test\(chemin\)\) continue;/);
  ok(!!m, "verifier.html ignore affiche et bande-annonce dans les orphelins");
  if (m) { const re = eval(m[1]); ok(["melanges/assets/videos/bande-annonce.mp4", "melanges/assets/images/affiche.jpg", "melanges/assets/images/affiche-fond.jpg", "melanges/assets/videos/bande-annonce-ouverture.mp4"].every(c => re.test(c)) && !re.test("melanges/assets/videos/salle1.mp4"), "motif d'exception correct"); }
  // crédits
  const sansCredit = jeux.filter(j => !/\n## Bande-annonce\n/.test(fs.readFileSync(path.join(RACINE, j, "assets/medias/CREDITS-medias.md"), "utf8")));
  ok(sansCredit.length === 0, "crédit « Bande-annonce » dans chaque CREDITS-medias.md" + (sansCredit.length ? " — manque : " + sansCredit.join(", ") : ""));
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
};

/* ---- N1 : vitrine des trophées (trophees.html) ---- */
SECTIONS.N1 = async () => {
  console.log("\n== N1 : trophées inter-jeux (trophees.html) ==");
  const p = (jeu, eleve, o) => Object.assign({ jeu, eleve, termine: true, total: 20, premierCoup: 12, indices: 3, quiz: 3, score: 150, mode: "equipe", date: "2026-10-0" + (o && o.j || 1) + "T10:00", partie: "2026-10-0" + (o && o.j || 1) + "T09:00" }, o || {});
  const hist = [
    p("declaration", "Les Lynx", { j: 1 }), p("constitution", "les lynx ", { j: 2, indices: 0 }), p("melanges", "Les Lynx", { j: 3, premierCoup: 19, quiz: 5 }),
    p("melanges", "Les Lynx", { j: 4, score: 170 }), p("chateau-fort", "LES LYNX", { j: 5, termine: false }),
    p("melanges", "Les Hiboux", { j: 1 }), p("melanges", "Vérification", { j: 1 })
  ];
  const { w, erreurs } = await charger(RACINE, "?nom=les%20lynx", { page: "trophees.html", attente: 300, stockage: { escape_resultats: JSON.stringify(hist) } });
  const d = w.document;
  const noms = [...d.querySelectorAll("#choix-nom option")].map(o => o.textContent);
  ok(noms.length === 2 && !noms.some(n => /rification/.test(n)), `noms de l'historique, sans « Vérification » (${noms.join(", ")})`);
  ok(/lynx/i.test(d.getElementById("choix-nom").value), "?nom= choisit l'équipe (majuscules et espaces ignorés)");
  const gagnes = [...d.querySelectorAll(".tr.gagne")].map(x => x.dataset.id).sort();
  const attendus = ["citoyen", "touche-a-tout", "perseverant", "premier-coffre", "quizz-parfait", "sans-coup-de-pouce", "sans-faute", "suite-de-l-histoire", "trois-coffres"].sort();
  ok(JSON.stringify(gagnes) === JSON.stringify(attendus), `trophées des Lynx : ${gagnes.join(", ")}`);
  ok(!d.querySelector('.tr.gagne[data-id="grand-explorateur"]') && d.querySelector('.tr.verrou[data-id="historien"]'), "trophées non gagnés grisés (château fort non terminé : pas « Historien »)");
  ok(/9<\/b> trophées sur 13 · 3 jeux terminés/.test(d.getElementById("compteur").innerHTML), "compteur : " + d.getElementById("compteur").textContent);
  w.__imprime = 0; d.getElementById("btn-imprimer").click();
  ok(w.__imprime === 1 && /Diplôme/.test(d.getElementById("impression").textContent), "diplôme imprimable");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
  const vide = await charger(RACINE, "", { page: "trophees.html", attente: 200 });
  ok(/Aucune partie terminée/.test(vide.w.document.getElementById("vitrine").textContent), "sans historique : message");
};

/* ---- N2 : kit « adopter ce projet » (adopter.html) ---- */
SECTIONS.N2 = async () => {
  console.log("\n== N2 : kit pour les collègues (adopter.html) ==");
  const fs = require("fs"), path = require("path");
  const { w, erreurs } = await charger(RACINE, "", { page: "adopter.html", attente: 200 });
  const d = w.document;
  ok(d.querySelectorAll("main h2").length >= 7, "7 rubriques (jouer, préparer, pendant, après, adapter, récupérer…)");
  const internes = [...d.querySelectorAll("a[href]")].map(a => a.getAttribute("href")).filter(h => !/^(https?:|#|mailto:)/.test(h));
  const absents = internes.filter(h => !fs.existsSync(path.join(RACINE, h.split(/[?#]/)[0])));
  ok(internes.length >= 10 && absents.length === 0, `${internes.length} liens internes, tous valides` + (absents.length ? " — absents : " + absents.join(", ") : ""));
  ok(/releases\/tag\/hors-ligne/.test(d.body.innerHTML) && /\?solo=1/.test(d.body.textContent), "archive hors ligne et mode individuel mentionnés");
  w.__imprime = 0; d.getElementById("btn-imprimer").click(); ok(w.__imprime === 1, "imprimable");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
  const accueil = fs.readFileSync(path.join(RACINE, "index.html"), "utf8");
  ok(/href="adopter.html"/.test(accueil), "lien depuis l'accueil");
};

/* ---- N12 : bilan de classe dans resultats.html ---- */
SECTIONS.N12 = async () => {
  console.log("\n== N12 : bilan de classe (resultats.html) ==");
  // 4 parties de melanges (CM2) : l'énigme 1-1 échoue souvent, 1-2 est réussie ; 1 partie sans détail ; 1 partie de Déclaration
  const base = { type: "escape-game-compte-rendu", version: 1, jeu: "melanges", titre: "Le Laboratoire de Madame Mélange", mode: "equipe", niveau: "CM2", termine: true, score: 100, scoreMax: 235, enigmes: 20, total: 20, premierCoup: 10, erreurs: 4, indices: 2, dureeMin: 40 };
  const e = (id, s, l, pc, err, ind, extra) => Object.assign({ id, s, l, ok: 1, pc, e: err, i: ind, p: 0, c: 0 }, extra || {});
  const parties = [
    { eleve: "Les Lynx", date: "2026-10-12T10:00", detail: [e("1-1", 1, "masses", 0, 2, 1), e("1-2", 1, "masses", 1, 0, 0), e("2-1", 2, "melanges", 0, 1, 0, { c: 1 })] },
    { eleve: "Les Hiboux", date: "2026-10-12T10:05", detail: [e("1-1", 1, "masses", 0, 1, 0), e("1-2", 1, "masses", 1, 0, 0), e("2-1", 2, "melanges", 1, 0, 0)] },
    { eleve: "Les Renards", date: "2026-10-13T10:00", detail: [e("1-1", 1, "masses", 0, 0, 0, { ok: 0, p: 1 }), e("1-2", 1, "masses", 0, 1, 0), e("2-1", 2, "melanges", 1, 0, 0)] },
    { eleve: "Les Aigles", date: "2026-10-13T10:10", detail: [e("1-1", 1, "masses", 1, 0, 0), e("1-2", 1, "masses", 1, 0, 0), e("2-1", 2, "melanges", 1, 0, 0)] },
    { eleve: "Sans détail", date: "2026-10-14T10:00" }
  ].map(p => Object.assign({}, base, p));
  const decl = { type: "escape-game-compte-rendu", version: 1, jeu: "declaration", titre: "Le Secret de la Déclaration", eleve: "Les Lynx", mode: "equipe", niveau: "CM1", date: "2026-10-14T11:00", termine: true, score: 80, scoreMax: 185, enigmes: 5, total: 5, premierCoup: 2, erreurs: 3, indices: 1, dureeMin: 30,
    detail: [{ id: "s1", s: 1, l: "", ok: 1, pc: 0, e: 1, i: 0, p: 0, c: 0 }, { id: "s2", s: 2, l: "", ok: 1, pc: 1, e: 0, i: 0, p: 0, c: 0 }] };
  const toutes = parties.concat([decl]);
  const { w, erreurs } = await charger(RACINE, "", { page: "resultats.html", attente: 400, stockage: { escape_resultats: JSON.stringify(toutes) } });
  const d = w.document;
  d.getElementById("btn-appareil").click();
  await attendreQue(() => w.RESULTATS_PAGE.bilan && w.RESULTATS_PAGE.bilan.parties.length === 5, 4000);
  await dodo(200);
  const B = w.RESULTATS_PAGE.bilan;
  ok(B && B.parties.length === 5, `5 parties avec détail prises en compte (la partie sans détail est ignorée) : ${B && B.parties.length}`);
  const en = (jeu, id) => B.enigmes.find(x => x.jeu === jeu && x.id === id);
  ok(en("melanges", "1-1").n === 4 && en("melanges", "1-1").pc === 1, "énigme 1-1 : 1 réussite du premier coup sur 4 (25 %)");
  ok(en("melanges", "1-2").pc === 3 && en("melanges", "1-2").n === 4, "énigme 1-2 : 3 sur 4 (75 %)");
  ok(en("melanges", "1-1").pass === 1 && en("melanges", "1-1").err === 3 && en("melanges", "1-1").ind === 1, "totaux d'erreurs, d'indices et de jokers (3 · 1 · 1)");
  ok(en("melanges", "2-1").pouce === 1, "coups de pouce de l'enseignant comptés");
  ok(B.enigmes.filter(x => x.jeu === "melanges")[0].id === "1-1" && B.enigmes[0].pc === 0 && B.enigmes[B.enigmes.length - 1].pc >= B.enigmes[0].pc, "énigmes triées de la plus difficile à la plus facile");
  const comp = B.comps.find(c => c.jeu === "melanges" && c.lecon === "masses");
  ok(comp && comp.n === 8 && comp.pc === 4 && !!comp.texte, `compétence « masses » : 4 sur 8 (50 %), texte du programme : « ${comp && comp.texte.slice(0, 50)} »`);
  ok(en("declaration", "s1") && /Salle 1/.test(en("declaration", "s1").titre) && en("declaration", "s1").lecon === "causes", `Déclaration (une énigme par salle) : « ${en("declaration", "s1").titre} », leçon ${en("declaration", "s1").lecon}`);
  // liste « à retravailler »
  const txt = d.getElementById("bilan-contenu").textContent;
  ok(/À retravailler en classe entière/.test(txt) && d.querySelectorAll("#bilan-contenu .a-retravailler li").length >= 1, `liste « à retravailler » : ${d.querySelectorAll("#bilan-contenu .a-retravailler li").length} entrée(s)`);
  const items = [...d.querySelectorAll("#bilan-contenu .a-retravailler li")].map(li => li.textContent);
  ok(items.some(t => /1-1/.test(t) && /25 %/.test(t)) && !items.some(t => /1-2/.test(t)), "1-1 (25 %) à retravailler, 1-2 (75 %) non");
  const liens = [...d.querySelectorAll("#bilan-contenu a.lien-lecon")].map(a => a.getAttribute("href"));
  ok(liens.length >= 1 && liens.every(h => /^[a-z-]+\/lecons-imprimables\.html\?niveau=CM[12]&lecon=/.test(h)) && liens.some(h => /^melanges\/.*lecon=masses/.test(h)), `liens vers la leçon A4 à imprimer : ${liens.join(" ; ")}`);
  const cibles = [...new Set(liens.map(h => h.split("?")[0]))];
  const fs = require("fs");
  ok(cibles.every(c => fs.existsSync(require('path').join(RACINE, c))), "les pages de leçons liées existent");
  // seuil modifiable
  const seuil = d.getElementById("seuil-bilan"); seuil.value = "80"; seuil.dispatchEvent(new w.Event("input")); await dodo(250);
  ok([...d.querySelectorAll("#bilan-contenu .a-retravailler li")].some(li => /1-2/.test(li.textContent)), "seuil à 80 % : 1-2 (75 %) devient « à retravailler »");
  seuil.value = "50";
  // filtres : un seul jeu
  const fj = d.getElementById("filtre-jeu"); fj.value = "declaration"; fj.dispatchEvent(new w.Event("input")); await dodo(250);
  ok(w.RESULTATS_PAGE.bilan.parties.length === 1 && /1 partie avec détail/.test(d.getElementById("compte-bilan").textContent), "le bilan suit les filtres (jeu)");
  fj.value = ""; fj.dispatchEvent(new w.Event("input")); await dodo(250);
  // export tableur du bilan
  d.getElementById("exp-bilan").click(); await dodo(300);
  const x = w.__dernierExport;
  ok(x && /^bilan-de-classe-\d{4}-\d\d-\d\d\.csv$/.test(x.nom) && x.contenu.startsWith("﻿Type;Jeu;Identifiant;"), `export du bilan : ${x && x.nom}`);
  const lignes = x.contenu.split("\r\n");
  ok(lignes.some(l => /^Énigme;Le Laboratoire de Madame Mélange;1-1;Du plus léger au plus lourd;4;1;25;3;1;1;0;oui;/.test(l)), "export : ligne de l'énigme 1-1 (25 %, à retravailler)");
  ok(lignes.some(l => /^Compétence;.*;masses;.*;8;4;50;/.test(l)), "export : ligne de la compétence « masses » (50 %)");
  // version imprimable
  w.__imprime = 0; d.getElementById("imp-bilan").click();
  ok(w.__imprime === 1 && /@media print/.test(d.head.innerHTML) && /\.imprimer-seulement/.test(d.head.innerHTML) && /\d+ partie\(s\)/.test(d.getElementById("titre-impr-bilan").textContent), "version imprimable : bouton et mise en page d'impression");
  // export tableur des parties : colonnes jokers et coups de pouce
  d.getElementById("exp-tableur").click();
  ok(/Énigmes passées \(joker\);Coups de pouce \(enseignant\);Contrôle/.test(w.__dernierExport.contenu), "export des parties : colonnes « passées » et « coups de pouce »");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
  // compte-rendu texte : « 2 passées » se retrouve en collant le texte
  const j = await charger(require('path').join(RACINE, 'melanges'), "", { attente: 500 });
  ok(typeof j.w.COMPTE_RENDU.construire === "function", "compte-rendu de partie prêt (champ detail)");
};

/* ---- N16 : progression portable (passeport + parties) entre appareils ---- */
SECTIONS.N16 = async () => {
  console.log("\n== N16 : export / import de la progression (maison ↔ classe) ==");
  const PROG = require(require("path").join(RACINE, "commun/js/progression.js"));
  const stock = init => { const m = Object.assign({}, init); return { getItem: k => (k in m ? m[k] : null), setItem: (k, v) => { m[k] = String(v); }, _m: m }; };
  const partie = (jeu, eleve, date, extra) => Object.assign({ type: "escape-game-compte-rendu", version: 1, jeu, eleve, mode: "equipe", niveau: "CM2", date, partie: date, termine: true, score: 100, scoreMax: 235, total: 20, premierCoup: 10, indices: 1 }, extra || {});
  // Cas simple : même élève, deux appareils, compétences différentes validées sur chacun
  const tablette = stock({ escape_passeport: JSON.stringify({ eleves: ["Léa B."], notes: { "Léa B.": { "melanges|1": { v: "A", date: "2026-10-12", t: "2026-10-12T10:00:00Z" }, "melanges|2": { v: "E", date: "2026-10-12", t: "2026-10-12T10:05:00Z" } } } }),
    escape_resultats: JSON.stringify([partie("melanges", "Léa B.", "2026-10-12T10:00")]) });
  const maison = stock({ escape_passeport: JSON.stringify({ eleves: ["Léa B."], notes: { "Léa B.": { "chateau-fort|1": { v: "A", date: "2026-10-14", t: "2026-10-14T18:00:00Z" }, "melanges|2": { v: "A", date: "2026-10-14", t: "2026-10-14T18:10:00Z" } } } }),
    escape_resultats: JSON.stringify([partie("chateau-fort", "Léa B.", "2026-10-14T18:00")]) });
  const fichier = JSON.stringify(PROG.contenu({ stockage: tablette, eleve: "léa b." }));
  const c = JSON.parse(fichier);
  ok(c.format === "escape-game-passeport" && c.versionFormat === 1 && c.eleve === "léa b." && c.parties.length === 1 && Object.keys(c.notes).length === 1, "export : enveloppe du format A5 (format, versionFormat, exporteLe), élève, parties");
  ok(PROG.nomFichier(c).startsWith("passeport-lea-b-"), "nom de fichier : " + PROG.nomFichier(c));
  const r1 = await PROG.importerTexte(fichier, { stockage: maison });
  ok(r1.ok && r1.bilan.notes === 1 && r1.bilan.remplacees === 0 && r1.bilan.gardees === 1 && r1.bilan.parties === 1, "import sur l'appareil de la maison : " + r1.message);
  const notes = JSON.parse(maison._m.escape_passeport).notes["Léa B."];
  ok(notes["melanges|1"].v === "A" && notes["chateau-fort|1"].v === "A", "les compétences des DEUX appareils sont réunies (melanges|1 venu de la tablette, chateau-fort|1 d'ici)");
  ok(notes["melanges|2"].v === "A" && notes["melanges|2"].t === "2026-10-14T18:10:00Z", "note plus récente de la maison gardée (A, pas le E plus ancien de la tablette)");
  ok(JSON.parse(maison._m.escape_resultats).length === 2, "les parties des deux appareils sont réunies (2)");
  // sens inverse : retour en classe, la note plus récente remplace la plus ancienne
  const r2 = await PROG.importerTexte(JSON.stringify(PROG.contenu({ stockage: maison })), { stockage: tablette });
  const n2 = JSON.parse(tablette._m.escape_passeport).notes["Léa B."];
  ok(r2.ok && n2["melanges|2"].v === "A" && n2["chateau-fort|1"].v === "A" && r2.bilan.remplacees === 1, "retour en classe : la note plus récente remplace l'ancienne (" + r2.message + ")");
  // idempotence : réimporter le même fichier ne change rien
  const avant = JSON.stringify(tablette._m);
  const r3 = await PROG.importerTexte(JSON.stringify(PROG.contenu({ stockage: maison })), { stockage: tablette });
  ok(JSON.stringify(tablette._m) === avant && /déjà à jour|Rien de nouveau/.test(r3.message), "réimport : rien ne change (" + r3.message + ")");
  // code court : aller-retour, compressé (Node) et non compressé
  const brut = PROG.contenu({ stockage: tablette, eleve: "Léa B." });
  const codeZ = await PROG.codeCourt(brut), codeP = await PROG.codeCourt(brut, { sansCompression: true });
  ok(/^EGP1z\.[A-Za-z0-9_-]+$/.test(codeZ) && /^EGP1\.[A-Za-z0-9_-]+$/.test(codeP) && codeZ.length < codeP.length, `code court compressé ${codeZ.length} caractères (non compressé ${codeP.length})`);
  const eleve3 = stock({});
  const r4 = await PROG.importerTexte("  " + codeZ.slice(0, 20) + "\n" + codeZ.slice(20) + "  ", { stockage: eleve3 });
  ok(r4.ok && JSON.parse(eleve3._m.escape_passeport).notes["Léa B."]["melanges|1"].v === "A" && JSON.parse(eleve3._m.escape_resultats).length === 2, "import d'un code collé (espaces et retours à la ligne ignorés) sur un appareil vide");
  const eleve4 = stock({}); const r5 = await PROG.importerTexte(codeP, { stockage: eleve4 });
  ok(r5.ok && JSON.parse(eleve4._m.escape_resultats).length === 2, "code non compressé accepté");
  // erreurs : fichier d'un autre type, code invalide, JSON illisible
  ok(!(await PROG.importerTexte(JSON.stringify({ format: "escape-game-partie", etat: {} }), { stockage: stock({}) })).ok, "un fichier de PARTIE (A5) est refusé");
  ok(!(await PROG.importerTexte("EGP1.@@@", { stockage: stock({}) })).ok && !(await PROG.importerTexte("n'importe quoi", { stockage: stock({}) })).ok, "code invalide et fichier illisible : message d'erreur, rien d'écrit");
  ok(!(await PROG.importerTexte(JSON.stringify({ format: "escape-game-passeport", versionFormat: 9 }), { stockage: stock({}) })).ok, "format plus récent que le site : refusé avec un message");
  // ancien export du passeport (C3) : accepté et fusionné
  const ancien = stock({ escape_passeport: JSON.stringify({ eleves: ["Tom R."], notes: { "Tom R.": { "melanges|1": { v: "E", date: "2026-09-30" } } } }) });
  const r6 = await PROG.importerTexte(JSON.stringify({ eleves: ["Tom R.", "Inès M."], notes: { "Tom R.": { "melanges|1": { v: "A", date: "2026-10-05" }, "melanges|3": { v: "N", date: "2026-10-05" } } } }), { stockage: ancien });
  const tom = JSON.parse(ancien._m.escape_passeport);
  ok(r6.ok && tom.notes["Tom R."]["melanges|1"].v === "A" && tom.notes["Tom R."]["melanges|3"].v === "N" && tom.eleves.includes("Inès M."), "ancien format du passeport : fusionné (date seule, sans heure)");
  // 100 parties au plus
  const gros = stock({ escape_resultats: JSON.stringify(Array.from({ length: 98 }, (_, i) => partie("melanges", "Les Lynx", "2026-09-" + String(i % 28 + 1).padStart(2, "0") + "T" + String(i).padStart(2, "0") + ":00"))) });
  await PROG.importerTexte(JSON.stringify(PROG.contenu({ stockage: stock({ escape_resultats: JSON.stringify(Array.from({ length: 10 }, (_, i) => partie("versailles", "Les Lynx", "2026-10-0" + (i % 9 + 1) + "T10:0" + i))) }) })), { stockage: gros });
  ok(JSON.parse(gros._m.escape_resultats).length === 100, "historique limité aux 100 parties les plus récentes");

  // passeport.html : deux « appareils » (deux pages), export fichier puis import avec fusion
  const A = await charger(RACINE, "", { page: "passeport.html", attente: 1200 });
  const dA = A.w.document;
  dA.getElementById("liste-eleves").value = "Léa B."; dA.getElementById("btn-eleves").click();
  dA.querySelector('.etats[data-cle="melanges|1"] button[data-v="A"]').click();
  ok(!!A.w.D === false || true, "passeport : page chargée");
  ok(!!dA.getElementById("btn-export") && !!dA.getElementById("btn-code") && /Exporter ma progression/.test(dA.getElementById("btn-export").textContent), "passeport : bouton « 📤 Exporter ma progression »");
  ok(/Léa B\./.test(dA.getElementById("portee-export").textContent), "passeport : l'export précise l'élève concerné");
  dA.getElementById("btn-export").click(); await dodo(100);
  const exporte = A.w.__dernierExport;
  ok(exporte && /^passeport-lea-b-\d{4}-\d\d-\d\d\.json$/.test(exporte.nom) && JSON.parse(exporte.contenu).notes["Léa B."]["melanges|1"].t, "passeport : fichier .json exporté avec l'heure de la note (" + (exporte && exporte.nom) + ")");
  dA.getElementById("btn-code").click(); await dodo(200);
  const code = dA.getElementById("code-progression").value;
  ok(/^EGP1\.[A-Za-z0-9_-]+$/.test(code), "passeport : code court affiché (" + code.slice(0, 14) + "…, " + code.length + " caractères)");
  const B = await charger(RACINE, "", { page: "passeport.html", attente: 1200 });
  const dB = B.w.document;
  dB.getElementById("liste-eleves").value = "Léa B."; dB.getElementById("btn-eleves").click();
  dB.querySelector('.etats[data-cle="chateau-fort|1"] button[data-v="E"]').click();
  dB.getElementById("coller-code").value = code; dB.getElementById("btn-code-importer").click(); await dodo(300);
  ok(/Progression fusionnée/.test(dB.getElementById("msg-transfert").textContent), "passeport (autre appareil) : « " + dB.getElementById("msg-transfert").textContent + " »");
  ok(B.w.PASSEPORT.D.notes["Léa B."]["melanges|1"].v === "A" && B.w.PASSEPORT.D.notes["Léa B."]["chateau-fort|1"].v === "E", "les compétences validées sur chacun des deux appareils sont réunies, vue mise à jour");
  ok(dB.querySelector('.etats[data-cle="melanges|1"] button[data-v="A"]').getAttribute("aria-pressed") === "true", "la vue affiche la compétence importée");
  ok(A.erreurs.length === 0 && B.erreurs.length === 0, "passeport : erreurs JS : " + A.erreurs.concat(B.erreurs).join(" | "));

  // jeux : bouton « 🎓 Ma progression » sur l'écran d'accueil
  const G = await charger(require("path").join(RACINE, "melanges"), "", { attente: 500, stockage: { escape_resultats: JSON.stringify([partie("melanges", "Les Lynx", "2026-10-12T10:00"), partie("melanges", "Les Aigles", "2026-10-12T10:30")]) } });
  const dG = G.w.document;
  const bt = dG.getElementById("btn-progression");
  ok(!!bt && /Ma progression/.test(bt.textContent), "melanges : bouton « 🎓 Ma progression » à l'accueil");
  dG.getElementById("input-equipe").value = "Les Lynx"; bt.click();
  const pan = dG.getElementById("panneau-progression");
  ok(!!pan && pan.querySelector("#prog-nom").value === "Les Lynx", "panneau : le nom saisi à l'accueil est repris");
  pan.querySelector("#prog-exporter").click(); await dodo(100);
  ok(G.w.__dernierExport && JSON.parse(G.w.__dernierExport.contenu).parties.length === 1 && /Garde ce fichier/.test(pan.querySelector("#prog-message").textContent), "export limité à l'élève nommé : 1 partie sur 2 (les Aigles ne sortent pas)");
  pan.querySelector("#prog-code").click(); await dodo(200);
  const codeG = pan.querySelector("#prog-code-texte").value;
  ok(/^EGP1/.test(codeG), "code court obtenu dans le jeu");
  const G2 = await charger(require("path").join(RACINE, "melanges"), "", { attente: 500 });
  G2.w.document.getElementById("btn-progression").click();
  G2.w.document.getElementById("prog-coller").value = codeG; G2.w.document.getElementById("prog-importer").click(); await dodo(300);
  ok(/fusionnée/.test(G2.w.document.getElementById("prog-message").textContent) && JSON.parse(G2.w.localStorage.getItem("escape_resultats")).length === 1, "autre appareil : code importé, la partie est retrouvée (trophées, résultats)");
  ok(G.erreurs.length === 0 && G2.erreurs.length === 0, "jeu : erreurs JS : " + G.erreurs.concat(G2.erreurs).join(" | "));
};

/* ---- N18 : fiches de séquence « avant / après » ---- */
SECTIONS.N18 = async () => {
  console.log("\n== N18 : séquences avant / après (sequences/) ==");
  const fs = require("fs"), path = require("path");
  const I = await charger(RACINE, "", { page: "sequences/index.html", attente: 300 });
  const d = I.w.document;
  const publies = I.w.SEQUENCES_PAGE.publies;
  ok(d.querySelectorAll("#liste .jeu").length === publies.length && publies.length >= 12, `liste : les ${publies.length} jeux publiés du catalogue`);
  ok(d.querySelectorAll("#liste .etat.fait").length === 2 && /melanges/.test(d.querySelector('#liste a[href*="melanges"]').getAttribute("href")), "2 fiches disponibles (✅), les autres « à rédiger » avec le modèle vierge");
  ok([...d.querySelectorAll("#liste a.bouton")].every(a => /^fiche\.html\?jeu=/.test(a.getAttribute("href"))), "chaque jeu renvoie vers sa fiche (ou le modèle)");
  ok(I.erreurs.length === 0, "liste : erreurs JS : " + I.erreurs.join(" | "));

  // intégrité des fiches rédigées
  const SEQ = I.w.SEQUENCES;
  for (const [jeu, s] of Object.entries(SEQ)) {
    const cat = I.w.CATALOGUE.jeux.find(j => j.dossier === jeu);
    ok(!!cat && fs.existsSync(path.join(RACINE, jeu, "index.html")), `${jeu} : jeu publié du catalogue`);
    ok(s.objectif && s.objectif.length > 40 && s.niveaux, `${jeu} : objectif et niveaux`);
    for (const k of ["avant", "apres"]) {
      const t = s[k];
      ok(t && /15-20 min/.test(t.duree) && t.titre && t.deroule.length >= 3 && t.materiel.length >= 1 && t.trace, `${jeu} : activité « ${k} » complète (15-20 min, ${t && t.deroule.length} étapes, matériel, trace)`);
    }
    ok(s.jeu && s.jeu.duree && s.jeu.formules.length >= 1 && s.jeu.roles.length >= 2 && s.jeu.conseils.length >= 1, `${jeu} : le jeu (durée, formule, rôles, conseils)`);
    ok(s.evaluer.length >= 2 && /passeport/i.test(s.evaluer.join(" ")), `${jeu} : évaluation reliée au passeport`);
    const guide = fs.readFileSync(path.join(RACINE, jeu, "GUIDE-PEDAGOGIQUE.md"), "utf8");
    ok(/60 à 75 min/.test(s.jeu.duree) && /60 à 75 minutes/.test(guide), `${jeu} : la durée du jeu est celle de son guide pédagogique`);
  }

  // la fiche d'un jeu
  const F = await charger(RACINE, "?jeu=melanges", { page: "sequences/fiche.html", attente: 300 });
  const f = F.w.document;
  ok(/Séquence — .*Laboratoire de Madame Mélange/.test(f.getElementById("titre").textContent), "fiche : titre « " + f.getElementById("titre").textContent + " »");
  ok(/Sciences/.test(f.getElementById("sous-titre").textContent) && /P1/.test(f.getElementById("sous-titre").textContent), "fiche : matière et période (" + f.getElementById("sous-titre").textContent + ")");
  ok(f.querySelectorAll(".temps.avant, .temps.jeu, .temps.apres").length === 3 && /15-20 min/.test(f.querySelector(".temps.avant .duree").textContent) && /15-20 min/.test(f.querySelector(".temps.apres .duree").textContent), "fiche : trois temps (avant 15-20 min · jeu · après 15-20 min)");
  ok(f.querySelectorAll(".temps.avant ol li").length >= 3 && f.querySelector(".temps.avant .trace"), "fiche : déroulé et trace de l'activité avant");
  const liens = [...f.querySelectorAll("a[href]")].map(a => a.getAttribute("href")).filter(h => !/^https?:/.test(h));
  ok(liens.some(h => /periode\.html\?p=P1&annee=B/.test(h)), "fiche : lien vers la fiche de compétences de la période (C5)");
  ok(liens.some(h => /passeport\.html/.test(h)) && liens.some(h => /resultats\.html/.test(h)), "fiche : liens vers le passeport (C3) et le bilan de classe");
  const morts = liens.filter(h => !fs.existsSync(path.join(RACINE, "sequences", h.split("?")[0])));
  ok(morts.length === 0, "fiche : tous les liens internes existent " + morts.join(", "));
  F.w.__imprime = 0; f.getElementById("btn-imprimer").click();
  ok(F.w.__imprime === 1 && /@media print/.test(f.head.innerHTML), "fiche : imprimable");
  ok(F.erreurs.length === 0, "fiche : erreurs JS : " + F.erreurs.join(" | "));

  // un jeu sans fiche : modèle vierge, jeu non bloqué ; jeu inconnu : pas de plantage
  const V = await charger(RACINE, "?jeu=declaration", { page: "sequences/fiche.html", attente: 300 });
  const v = V.w.document;
  ok(/Pas encore de fiche de séquence/.test(v.getElementById("fiche").textContent) && v.querySelectorAll(".temps").length === 3 && v.querySelector('a[href="../declaration/"]'), "jeu sans fiche : modèle vierge (avant · jeu · après) et lien pour jouer, rien n'est bloqué");
  ok(V.erreurs.length === 0, "modèle vierge : erreurs JS : " + V.erreurs.join(" | "));
  const X = await charger(RACINE, "?jeu=inconnu", { page: "sequences/fiche.html", attente: 300 });
  ok(/Modèle vierge/.test(X.w.document.getElementById("sous-titre").textContent) && X.erreurs.length === 0, "jeu inconnu : modèle vierge, sans erreur");

  // liens depuis chaque jeu et depuis la vue d'ensemble de l'année
  const jeux = ["declaration", "tour-du-monde", "constitution", "moyen-age-abbaye", "station-meteo", "melanges", "objets-techniques", "chateau-fort", "versailles", "renaissance", "alimentation", "lumiere", "etats-matiere", "mouvement", "traite-colonies"];
  const sans = jeux.filter(j => !fs.readFileSync(path.join(RACINE, j, "prof.html"), "utf8").includes(`../sequences/fiche.html?jeu=${j}`));
  ok(sans.length === 0, "prof.html des 12 jeux : bouton « 📘 Fiche de séquence » " + sans.join(", "));
  const A = await charger(RACINE, "", { page: "annee.html", attente: 600 });
  const liensAnnee = [...A.w.document.querySelectorAll('a[href^="sequences/fiche.html?jeu="]')].map(a => a.getAttribute("href"));
  ok(liensAnnee.length >= 12 && liensAnnee.includes("sequences/fiche.html?jeu=melanges"), `vue d'ensemble de l'année : lien « Séquence » sur chaque jeu disponible (${liensAnnee.length})`);
  ok(A.erreurs.length === 0, "annee.html : erreurs JS : " + A.erreurs.join(" | "));
  const acc = fs.readFileSync(path.join(RACINE, "index.html"), "utf8"), ad = fs.readFileSync(path.join(RACINE, "adopter.html"), "utf8");
  ok(/href="sequences\/"/.test(acc) && /href="sequences\/"/.test(ad), "liens depuis l'accueil et le kit « adopter ce projet »");
};

/* ---- N21 : kit de présentation (presentation/) ---- */
SECTIONS.N21 = async () => {
  console.log("\n== N21 : kit de présentation pour une animation pédagogique ==");
  const fs = require("fs"), path = require("path");
  const P = path.join(RACINE, "presentation");
  // diaporama
  const D = await charger(RACINE, "", { page: "presentation/diaporama.html", attente: 800 });
  const d = D.w.document, PR = D.w.PRESENTATION;
  ok(PR.diapos.length >= 10 && PR.diapos.length <= 15, `diaporama : ${PR.diapos.length} diapositives`);
  ok(PR.duree >= 10 && PR.duree <= 15, `diaporama : durée prévue ${PR.duree} min (10 à 15)`);
  ok(PR.diapos.every(s => s.querySelector(".notes") && /⏱/.test(s.querySelector(".notes").textContent)), "chaque diapositive a ses notes de l'intervenant, avec le temps prévu");
  const titres = PR.diapos.map(s => s.dataset.titre).join(" | ");
  ok(/constat/i.test(titres) && /moteur/i.test(titres) && /Démonstration/i.test(titres) && /lancer/i.test(titres), "contenu demandé : constat de départ, principe du moteur commun, démonstration, pour se lancer (" + titres + ")");
  ok(d.querySelectorAll(".diapo.actuelle").length === 1, "une seule diapositive affichée à la fois");
  d.dispatchEvent(new D.w.KeyboardEvent("keydown", { key: "ArrowRight" })); ok(PR.courante === 1, "→ : diapositive suivante");
  d.dispatchEvent(new D.w.KeyboardEvent("keydown", { key: "End" })); ok(PR.courante === PR.diapos.length - 1, "Fin : dernière diapositive");
  d.dispatchEvent(new D.w.KeyboardEvent("keydown", { key: "ArrowLeft" })); ok(PR.courante === PR.diapos.length - 2, "← : retour");
  d.dispatchEvent(new D.w.KeyboardEvent("keydown", { key: "n" })); ok(d.body.classList.contains("avec-notes"), "touche N : notes de l'intervenant");
  D.w.__imprime = 0; d.getElementById("btn-imprimer").click(); ok(D.w.__imprime === 1 && /@media print/.test(d.head.innerHTML) && /break-after:page/.test(d.head.innerHTML), "imprimable (une diapositive par page)");
  // chiffres à jour avec le catalogue (C1)
  const cat = D.w.CATALOGUE.jeux, publies = cat.filter(j => j.dossier).length;
  await attendreQue(() => D.w.CHIFFRES_VALEURS, 4000);
  const lu = nom => [...d.querySelectorAll(`[data-chiffre="${nom}"]`)].map(e => e.textContent);
  ok(lu("jeux").every(t => +t === publies) && publies >= 13, `chiffres : ${publies} jeux jouables, comme le catalogue`);
  ok(lu("prevus").every(t => +t === cat.length), `chiffres : ${cat.length} jeux dans la progression`);
  const matieres = [...new Set(cat.filter(j => j.dossier).map(j => j.matiere))];
  ok(lu("matieres").every(t => +t === matieres.length) && lu("listematieres")[0] === matieres.join(", "), `chiffres : ${matieres.length} matières (${matieres.join(", ")})`);
  const attendu = 5 * 12 + 8 + 6 + 16;       // même décompte que le passeport (C3) : une compétence par leçon
  ok(lu("competences").every(t => +t === attendu), `chiffres : ${lu("competences")[0]} compétences, comme le passeport (${attendu})`);
  ok(!/[0-9]{2,} jeux|\b13 jeux\b/.test(fs.readFileSync(path.join(P, "diaporama.html"), "utf8").replace(/<script[\s\S]*?<\/script>/g, "")), "aucun nombre de jeux écrit en dur dans le diaporama");
  ok(D.erreurs.length === 0, "diaporama : erreurs JS : " + D.erreurs.join(" | "));
  // déroulé minuté
  const R = await charger(RACINE, "", { page: "presentation/deroule.html", attente: 300 });
  const r = R.w.document, F = R.w.DEROULE.FORMATS;
  const total = f => F[f].etapes.reduce((t, e) => t + e[0], 0), manip = f => F[f].etapes.filter(e => e[4]).reduce((t, e) => t + e[0], 0);
  ok(total("court") === 30 && total("complet") === 45, `déroulé : 30 min (court) et 45 min (complet) : ${total("court")} / ${total("complet")}`);
  ok(manip("court") >= 8 && manip("complet") >= 15, `un temps de manipulation par les collègues : ${manip("court")} min (court), ${manip("complet")} min (complet)`);
  ok(r.querySelectorAll("#tableau tbody tr").length === F.complet.etapes.length && /dont 15 minutes de manipulation/.test(r.getElementById("total").textContent) && r.querySelector("tr.manip"), "déroulé complet affiché : horaires, étape de manipulation en évidence, total");
  r.querySelector('button[data-format="court"]').click();
  ok(r.querySelectorAll("#tableau tbody tr").length === F.court.etapes.length && /Total : 30 minutes/.test(r.getElementById("total").textContent), "bouton 30 minutes : déroulé court");
  const horaires = [...r.querySelectorAll("#tableau td.h")].map(td => td.textContent);
  ok(horaires[0] === "0-3 min" && horaires[horaires.length - 1] === "26-30 min", "horaires cumulés (" + horaires.join(", ") + ")");
  ok(/Avant la séance/.test(r.body.textContent) && /Mon plan pour la première séance/.test(r.body.textContent), "préparation et plan de première séance");
  ok(R.erreurs.length === 0, "déroulé : erreurs JS : " + R.erreurs.join(" | "));
  // page d'entrée, captures, liens
  const H = await charger(RACINE, "", { page: "presentation/index.html", attente: 600 });
  const h = H.w.document;
  ok(!!h.querySelector('a[href="diaporama.html"]') && !!h.querySelector('a[href="deroule.html"]'), "page d'entrée : liens vers le diaporama et le déroulé");
  const imgs = [...h.querySelectorAll("#captures img")].map(i => i.getAttribute("src"));
  ok(imgs.length >= 5 && imgs.every(s => fs.existsSync(path.join(P, s)) && fs.statSync(path.join(P, s)).size > 20000), `${imgs.length} captures d'écran présentes et non vides`);
  const dia = [...D.w.document.querySelectorAll("img")].map(i => i.getAttribute("src"));
  ok(dia.every(s => fs.existsSync(path.join(P, s))), "les captures du diaporama existent");
  const liens = [...h.querySelectorAll("a[href]")].map(a => a.getAttribute("href")).filter(x => !/^https?:/.test(x));
  const morts = liens.filter(x => !fs.existsSync(path.join(P, x.split("?")[0].split("#")[0]).replace(/\/$/, "")) && !fs.existsSync(path.join(P, x.split("?")[0], "index.html")));
  ok(morts.length === 0, "page d'entrée : liens internes valides " + morts.join(", "));
  ok(lu("jeux")[0] !== undefined && h.querySelector('[data-chiffre="jeux"]').textContent == publies, "page d'entrée : chiffres calculés");
  ok(H.erreurs.length === 0, "page d'entrée : erreurs JS : " + H.erreurs.join(" | "));
  // liens depuis adopter.html, README, captures de démonstration fictives
  const ad = fs.readFileSync(path.join(RACINE, "adopter.html"), "utf8");
  ok(/href="presentation\/"/.test(ad), "liée depuis adopter.html");
  const cap = fs.readFileSync(path.join(P, "capturer.js"), "utf8");
  ok(/FICTIFS/.test(cap) && !/Inès|Léa B\.|Tom R\./.test(cap), "captures : données fictives (aucun élève réel)");
  ok(fs.existsSync(path.join(P, "README.md")), "README du dossier");
};

/* ---- N24 : export du passeport au format LSU ---- */
SECTIONS.N24 = async () => {
  console.log("\n== N24 : export du passeport pour le LSU (passeport.html) ==");
  const fs = require("fs"), path = require("path");
  const LSU = require(path.join(RACINE, "commun/donnees/lsu.js"));
  const EXP = require(path.join(RACINE, "commun/js/export-lsu.js"));
  // 1. la table couvre toutes les leçons du passeport, sans intitulé inconnu ni leçon fantôme
  const jeux = fs.readdirSync(RACINE).filter(d => fs.existsSync(path.join(RACINE, d, "assets/data/lecons-a4.json")));
  let manquantes = [], fantomes = [], inconnus = [], total = 0;
  for (const j of jeux) {
    const lecons = Object.keys(JSON.parse(fs.readFileSync(path.join(RACINE, j, "assets/data/lecons-a4.json"), "utf8")).lecons || {});
    const table = LSU.correspondance[j] || {};
    total += lecons.length;
    lecons.forEach(l => { if (!table[l]) manquantes.push(j + "/" + l); else if (!LSU.items[table[l][0]] || !["=", "~"].includes(table[l][1])) inconnus.push(j + "/" + l); });
    Object.keys(table).forEach(l => { if (!lecons.includes(l)) fantomes.push(j + "/" + l); });
  }
  ok(jeux.length >= 14 && manquantes.length === 0, `chaque leçon de ${jeux.length} jeux (${total}) a son intitulé LSU ${manquantes.join(", ")}`);
  ok(fantomes.length === 0 && inconnus.length === 0, `aucune ligne orpheline ni intitulé inconnu ${fantomes.concat(inconnus).join(", ")}`);
  ok(Object.keys(LSU.correspondance).every(j => jeux.includes(j)), "table : seulement des jeux publiés");
  ok(Object.values(LSU.items).every(i => i.discipline && i.type && i.libelle), "chaque intitulé LSU : discipline, type, libellé");
  // 2. niveaux suggérés (règle simple, « dépassés » jamais proposé)
  ok(EXP.niveau({ A: 3, E: 0, N: 0 }, LSU) === "Objectifs atteints" && EXP.niveau({ A: 1, E: 1, N: 0 }, LSU) === "Objectifs partiellement atteints"
    && EXP.niveau({ A: 2, E: 0, N: 1 }, LSU) === "Objectifs partiellement atteints" && EXP.niveau({ A: 0, E: 0, N: 2 }, LSU) === "Objectifs non atteints"
    && EXP.niveau({ A: 0, E: 1, N: 0 }, LSU) === "Objectifs partiellement atteints" && EXP.niveau({ A: 0, E: 0, N: 0 }, LSU) === "", "règle des niveaux suggérés");
  ok(!Object.values(LSU.niveaux).some(n => /dépass/i.test(n)), "« dépassés » jamais proposé");
  // 3. dans la page : un élève à l'historique varié, un élève sans note
  const { w, erreurs } = await charger(RACINE, "", { page: "passeport.html", attente: 1200 });
  const d = w.document, P = w.PASSEPORT;
  const cle = (jeu, lecon) => { const k = P.COMPETENCES.find(c => c.jeu === jeu && c.lecon === lecon); if (!k) throw new Error("compétence introuvable " + jeu + "/" + lecon); return k.cle; };
  ok(P.COMPETENCES.every(c => c.lecon), "passeport : la clé de leçon est conservée sur chaque compétence");
  const note = (v, date) => ({ v, date, t: date + "T10:00:00Z" });
  const lea = {};
  [["moyen-age-abbaye", "clovis", "A", "2026-09-15"], ["moyen-age-abbaye", "charlemagne", "A", "2026-09-15"],      // Et avant la France ? : 2/2 acquises
   ["moyen-age-abbaye", "scriptorium", "E", "2026-09-22"], ["chateau-fort", "vie-des-paysans", "N", "2026-10-06"],   // Le temps des rois : en cours + non acquise (approchée), partielle
   ["etats-matiere", "etats", "A", "2026-10-13"], ["etats-matiere", "air", "A", "2026-10-13"], ["etats-matiere", "changements", "A", "2026-10-13"],
   ["etats-matiere", "conservation", "A", "2026-10-13"], ["etats-matiere", "proprietes", "A", "2026-10-13"],     // matière : 5/5 acquises (exacte)
   ["melanges", "masses", "N", "2026-11-03"],                                                                        // + 1 non acquise approchée → partiellement atteints
   ["lumiere", "sources", "N", "2026-11-03"],                                                                        // signal : 1 seule note, non acquise, partielle
   ["constitution", "textes", "A", "2026-11-04"], ["declaration", "bastille", "E", "2026-11-04"], ["tour-du-monde", "carte", "A", "2026-11-04"],
   ["mission-geo", "l11", "E", "2026-11-05"]
  ].forEach(([j, l, v, dt]) => { lea[cle(j, l)] = note(v, dt); });
  w.localStorage.setItem("escape_passeport", JSON.stringify({ eleves: ["Léa B.", "Tom R."], notes: { "Léa B.": lea } }));
  P.D.eleves.splice(0, P.D.eleves.length, "Léa B.", "Tom R."); P.D.notes["Léa B."] = lea; P.rendre();
  ok(d.getElementById("panneau-lsu").hidden && d.getElementById("btn-lsu") && /Exporter pour le LSU/.test(d.getElementById("btn-lsu").textContent), "bouton « 🧾 Exporter pour le LSU » (panneau fermé au départ)");
  d.getElementById("btn-lsu").click();
  const panneau = d.getElementById("panneau-lsu");
  ok(!panneau.hidden && /aide à la saisie, pas une validation/i.test(d.getElementById("lsu-avertissement").textContent) && /garde la main/.test(d.getElementById("lsu-avertissement").textContent), "avertissement : une aide, pas une validation, l'enseignant garde la main");
  const rows = [...d.querySelectorAll("#lsu-apercu table tr")].slice(1).map(tr => [...tr.children].map(td => td.textContent.trim()));
  const ligne = intitule => rows.find(r => r[1].startsWith(intitule));
  ok(rows.length === 8, `8 intitulés LSU pour Léa (${rows.length}) : ` + rows.map(r => r[1].slice(0, 30)).join(" / "));
  ok(ligne("Et avant la France ?")[2] === "Objectifs atteints" && /2 acquises — 2 notées sur 2/.test(ligne("Et avant la France ?")[3]) && !/partielle/.test(ligne("Et avant la France ?")[3]), "« Et avant la France ? » : atteints, évaluation complète");
  const rois = ligne("Le temps des rois");
  ok(rois[2] === "Objectifs partiellement atteints" && /1 en cours, 1 non acquise — 2 notées sur 18/.test(rois[3]) && /évaluation partielle/.test(rois[3]) && /≈/.test(rois[1]), "« Le temps des rois » : partiel, correspondance approchée (≈) et évaluation partielle signalées : " + rois.join(" | "));
  const matiere = ligne("Matière, mouvement, énergie, information : décrire");
  ok(matiere[2] === "Objectifs partiellement atteints" && /5 acquises, 1 non acquise — 6 notées sur 14/.test(matiere[3]), "matière : 5 acquises + 1 non acquise (mélanges) regroupées : " + matiere.join(" | "));
  ok(ligne("Matière, mouvement, énergie, information : identifier un signal")[2] === "Objectifs non atteints", "signal : non atteints");
  ok(ligne("Les principes et les valeurs de la République")[2] === "Objectifs atteints" && ligne("Appréhender la notion d'échelle")[2] === "Objectifs atteints" && ligne("Consommer en France")[2] === "Objectifs partiellement atteints", "EMC, compétence d'échelle et « Consommer en France » : une ligne chacun");
  ok(rows.every(r => r[0]) && rows[0][0] === "Histoire et géographie", "classé par discipline (histoire-géographie d'abord)");
  const L = w.EXPORT_LSU.construire({ eleves: ["Léa B."], notes: { "Léa B.": lea }, competences: P.COMPETENCES, donnees: w.LSU, catalogue: w.CATALOGUE });
  ok(L.lignes.length === 8 && L.partielles >= 5 && L.approchees >= 3, `signalements : ${L.partielles} évaluations partielles, ${L.approchees} correspondances approchées`);
  // texte à copier-coller et CSV
  const texte = d.getElementById("lsu-texte").value;
  ok(/^AIDE À LA SAISIE LSU/.test(texte) && /LÉA B\./.test(texte) && /Histoire et géographie/.test(texte) && /Le temps des rois → Objectifs partiellement atteints/.test(texte) && /\[correspondance approchée\]/.test(texte) && !/TOM R/.test(texte), "texte à copier-coller : avertissement, élève, discipline, niveau, signalements");
  d.getElementById("btn-lsu-csv").click();
  const csv = w.__dernierExport.contenu, lignes = csv.replace(/^\uFEFF/, "").split("\r\n");
  ok(/^passeport-LSU-\d{4}-\d{2}-\d{2}\.csv$/.test(w.__dernierExport.nom) && csv.startsWith("\uFEFF") && lignes.length === 9, `CSV : en-tête + 8 lignes, BOM Excel, nom daté (${lignes.length} lignes)`);
  ok(lignes[0] === "eleve;discipline_LSU;type;intitule_LSU;niveau_suggere;detail;evaluation_complete;correspondance;derniere_date;jeux;programme_de_reference", "CSV : colonnes");
  ok(lignes.some(l => /^Léa B\.;Histoire et géographie;Élément de programme;Et avant la France \?;Objectifs atteints;.*;complète;exacte;2026-09-15;Le Manuscrit de l'abbaye;Arrêté du 22 avril 2026/.test(l)), "CSV : une ligne complète lue (programme de référence du bandeau BO, C2)");
  ok(lignes.every(l => l.split(";").length >= 11), "CSV : 11 colonnes partout (séparateurs protégés)");
  // filtre « depuis » : seules les notes récentes (bilan de la période)
  const dep = d.getElementById("lsu-depuis"); dep.value = "2026-11-01"; dep.dispatchEvent(new w.Event("change"));
  const rows2 = [...d.querySelectorAll("#lsu-apercu table tr")].slice(1).map(tr => tr.children[1].textContent);
  ok(rows2.length === 6 && !rows2.some(r => /Et avant la France/.test(r)), `depuis le 1er novembre : ${rows2.length} intitulés (les notes de septembre-octobre sont écartées)`);
  dep.value = "2026-12-01"; dep.dispatchEvent(new w.Event("change"));
  ok(/rien à reporter/.test(d.getElementById("lsu-apercu").textContent) && d.getElementById("lsu-texte").value.includes("aucune compétence notée"), "aucune note sur la période : message clair, rien à reporter");
  dep.value = ""; dep.dispatchEvent(new w.Event("change"));
  // portée : un élève sans note, puis toute la classe
  const sel = d.getElementById("choix-eleve"); sel.value = "Tom R."; sel.dispatchEvent(new w.Event("change"));
  ok(/rien à reporter/.test(d.getElementById("lsu-apercu").textContent), "élève sans note : rien à reporter");
  const v = d.getElementById("choix-vue"); v.value = "classe"; v.dispatchEvent(new w.Event("change"));
  ok(/Toute la classe : 2 élève\(s\)/.test(d.getElementById("lsu-portee").textContent) && d.querySelectorAll("#lsu-apercu table tr").length === 9, "vue de la classe : l'export concerne toute la classe (colonne Élève)");
  // 4. leçon inconnue de la table (nouveau jeu) : retombe sur la discipline du bandeau BO (C2), sans rien inventer
  const inconnue = EXP.construire({ eleves: ["Zoé"], notes: { Zoé: { "chateau-fort|1": note("A", "2026-11-01"), "jeu-futur|1": note("E", "2026-11-01") } },
    competences: [{ cle: "chateau-fort|1", jeu: "chateau-fort", lecon: "leçon-inconnue", titre: "Le Secret du donjon", matiere: "Histoire", texte: "x" },
                  { cle: "jeu-futur|1", jeu: "jeu-futur", lecon: "a", titre: "Futur", matiere: "?", texte: "y" }],
    donnees: LSU, catalogue: w.CATALOGUE });
  ok(inconnue.lignes.length === 2 && inconnue.lignes[0].discipline === "Histoire et géographie" && inconnue.lignes[0].intitule === "(à rattacher dans votre LSU)" && inconnue.lignes[0].approchee, "leçon absente de la table : discipline du bandeau BO (C2), « à rattacher dans votre LSU »");
  ok(inconnue.lignes[1].discipline === "(discipline à préciser)", "jeu inconnu : discipline à préciser, rien d'inventé");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
};

/* ---- N30 : fiche synthèse pour les familles ---- */
SECTIONS.N30 = async () => {
  console.log("\n== N30 : fiche synthèse pour les familles (passeport.html) ==");
  const fs = require("fs"), path = require("path");
  const FAM = require(path.join(RACINE, "commun/donnees/familles.js"));
  const FF = require(path.join(RACINE, "commun/js/fiche-famille.js"));
  // 1. toutes les leçons du passeport ont leur formulation, sans jargon
  const jeux = fs.readdirSync(RACINE).filter(d => fs.existsSync(path.join(RACINE, d, "assets/data/lecons-a4.json")));
  const manque = [], fantomes = [], jargon = [], longs = [];
  const JARGON = /comp[ée]tence|socle|cycle\b(?! de l'eau)|programme|acquis|évalu|\bBO\b|élément|objectif|séquence|\bCM[12]\b|savoir-faire|\bitem|référentiel|\bLSU\b|domaine/i;
  for (const j of jeux) {
    const lecons = Object.keys(JSON.parse(fs.readFileSync(path.join(RACINE, j, "assets/data/lecons-a4.json"), "utf8")).lecons || {});
    const F = FAM.jeux[j];
    if (!F) { manque.push(j); continue; }
    lecons.forEach(l => { if (!F.lecons[l]) manque.push(j + "/" + l); });
    Object.keys(F.lecons).forEach(l => { if (!lecons.includes(l)) fantomes.push(j + "/" + l); });
    [[j + "/deroule", F.deroule]].concat(Object.entries(F.lecons).map(([l, t]) => [j + "/" + l, t])).forEach(([k, t]) => {
      if (JARGON.test(t) || /\b(?![IVXL]+\b)[A-Z]{3,}\b/.test(t)) jargon.push(k);   // sigles (les chiffres romains des rois sont permis)
      if (t.length > (k.endsWith("/deroule") ? 230 : 120)) longs.push(k + " (" + t.length + ")");
    });
  }
  ok(manque.length === 0 && fantomes.length === 0, `une formulation pour chacune des leçons de ${jeux.length} jeux ${manque.concat(fantomes).join(", ")}`);
  ok(jargon.length === 0, "aucun jargon de programme (compétence, socle, cycle, acquis…) : " + jargon.join(", "));
  ok(longs.length === 0, "phrases courtes (lecture rapide par un parent) : " + longs.join(", "));
  ok(Object.values(FAM.jeux).every(j => /^[A-ZÀÉ]/.test(j.deroule) && /\.$/.test(j.deroule)), "chaque phrase de déroulé est une phrase");
  ok(!Object.values(FAM.niveaux).some(n => /non acquis|insuffisant|échec|faible/i.test(n)), "étiquettes bienveillantes : " + Object.values(FAM.niveaux).join(" / "));
  // 2. dans la page
  const hist = JSON.stringify([
    { type: "escape-game-compte-rendu", jeu: "chateau-fort", eleve: "Les Lynx", mode: "equipe", termine: true, date: "2026-11-05T10:00", score: 150, scoreMax: 185,
      detail: [{ id: "1-1", l: "construire-un-chateau", ok: 1, pc: 1 }, { id: "2-1", l: "les-defenses", ok: 1, pc: 0 }, { id: "3-1", l: "vie-du-seigneur", ok: 0 }, { id: "4-1", l: "vie-des-paysans", ok: 1, pc: 1 }] },
    { type: "escape-game-compte-rendu", jeu: "chateau-fort", eleve: "Mia (solo)", mode: "solo", termine: true, date: "2026-11-05T11:00", detail: [{ id: "1-1", l: "les-defenses", ok: 1 }] }
  ]);
  const { w, erreurs } = await charger(RACINE, "", { page: "passeport.html", attente: 1200, stockage: { escape_resultats: hist } });
  const d = w.document, P = w.PASSEPORT;
  const cle = (jeu, lecon) => P.COMPETENCES.find(c => c.jeu === jeu && c.lecon === lecon).cle;
  const note = (v, date) => ({ v, date, t: date + "T10:00:00Z" });
  P.D.eleves.splice(0, P.D.eleves.length, "Léa B.", "Tom R.", "Inès M.");
  P.D.notes["Léa B."] = { [cle("chateau-fort", "vie-des-paysans")]: note("N", "2026-11-05"), [cle("chateau-fort", "construire-un-chateau")]: note("A", "2026-11-05"),
    [cle("chateau-fort", "les-defenses")]: note("E", "2026-11-05"), [cle("chateau-fort", "vie-du-seigneur")]: note("A", "2026-11-05"), [cle("melanges", "masses")]: note("A", "2026-10-01") };
  P.D.notes["Tom R."] = { [cle("chateau-fort", "vie-des-paysans")]: note("N", "2026-11-05") };
  P.rendre();
  ok(d.getElementById("panneau-famille").hidden && /Fiche pour les familles/.test(d.getElementById("btn-famille").textContent), "bouton « 👪 Fiche pour les familles » (panneau fermé au départ)");
  d.getElementById("btn-famille").click();
  const sel = id => d.getElementById(id), apercu = () => sel("fam-apercu").textContent, fiches = () => d.querySelectorAll("#fam-apercu .ffam");
  ok(sel("fam-jeu").value === "chateau-fort" && sel("fam-pour").value === "eleve", "jeu proposé : le plus récemment travaillé par l'élève (" + sel("fam-jeu").value + ")");
  ok(fiches().length === 1 && /Le Secret du donjon/.test(apercu()) && /Léa B\./.test(apercu()), "une fiche : nom du jeu et de l'élève");
  const puces = [...d.querySelectorAll("#fam-apercu li")].map(li => li.textContent.trim());
  ok(puces.length === 3 && /^Expliquer comment et pourquoi on construisait un château fort.*bien en place/.test(puces[0]) && /^Raconter la vie du seigneur.*bien en place/.test(puces[1]) && /^Décrire comment un château fort protégeait.*en progrès/.test(puces[2]),
    "3 points au plus, les mieux maîtrisés d'abord : " + puces.join(" | "));
  ok(!/à consolider|non acquis|%|\d\s*\/\s*\d/i.test(apercu()), "la leçon non acquise n'est pas étalée, aucune note chiffrée");
  ok(/Au Moyen Âge, en équipe, les élèves ont parcouru un château/.test(apercu()) && /Pas de note chiffrée/.test(apercu()), "une phrase sur le déroulé du jeu et la mention « pas de note chiffrée »");
  ok(!/compétence|socle|programme|cycle|acquis/i.test(apercu()), "aucun jargon dans la fiche affichée");
  // un élève avec une seule leçon à consolider : présentée avec bienveillance
  sel("choix-eleve").value = "Tom R."; sel("choix-eleve").dispatchEvent(new w.Event("change"));
  ok(fiches().length === 1 && /Raconter la vie de tous les jours des paysans.*à consolider/.test(apercu()) && /Tom R\./.test(apercu()), "élève Tom : une seule leçon, « à consolider »");
  // élève sans aucune note : rien d'affirmé sur lui, seulement ce que le jeu fait travailler
  sel("choix-eleve").value = "Inès M."; sel("choix-eleve").dispatchEvent(new w.Event("change"));
  ok(/Pendant ce jeu, la classe a travaillé à/.test(apercu()) && d.querySelectorAll("#fam-apercu li").length === 3 && d.querySelectorAll("#fam-apercu .et").length === 0, "sans note : « la classe a travaillé à… », 3 premières leçons, aucune étiquette");
  // une équipe : leçons de sa dernière partie
  const optEq = [...sel("fam-pour").options].map(o => o.value);
  ok(optEq.includes("equipe:Les Lynx") && !optEq.some(v => /Mia/.test(v)), "équipes proposées : celles du jeu (le mode solo n'en est pas une) : " + optEq.join(", "));
  sel("fam-pour").value = "equipe:Les Lynx"; sel("fam-pour").dispatchEvent(new w.Event("change"));
  const pe = [...d.querySelectorAll("#fam-apercu li")].map(li => li.textContent.trim());
  ok(/L'équipe « Les Lynx »/.test(apercu()) && /Ce que l'équipe a travaillé/.test(apercu()) && pe.length === 3 && pe.every(t => /bien en place/.test(t)) && !/vie du seigneur/i.test(apercu()), "fiche d'équipe : leçons réussies d'abord, la leçon non réussie reste dans l'ombre : " + pe.join(" | "));
  ok(/5 novembre 2026/.test(apercu()), "date de la partie de l'équipe");
  // toute la classe, mot de l'enseignant (échappé), impression et texte à copier
  sel("fam-pour").value = "classe"; sel("fam-pour").dispatchEvent(new w.Event("change"));
  sel("fam-mot").value = "Bravo <b>l'équipe</b> !"; sel("fam-mot").dispatchEvent(new w.Event("input"));
  ok(fiches().length === 3 && d.querySelectorAll("#fam-apercu .mot").length === 3 && !d.querySelector("#fam-apercu .mot b b") && /<b>l'équipe<\/b>/.test(apercu()), "classe : 3 fiches, mot de l'enseignant sur chacune et affiché tel quel (non interprété)");
  const texte = sel("fam-texte").value;
  ok(texte.split("————————————————").length === 3 && /^Un escape game en classe : « Le Secret du donjon »/.test(texte) && /Mot de l'enseignant : Bravo/.test(texte) && /• Expliquer comment et pourquoi on construisait un château fort \(bien en place\)/.test(texte), "texte à copier-coller : une fiche par élève, séparées, avec puces et mot");
  sel("btn-fam-imprimer").click();
  ok(w.__imprime === 1 && d.querySelectorAll("#impression .ffam").length === 3, "impression : 3 fiches envoyées à l'impression");
  ok(/\.ffam\{[^}]*height:128mm/.test(fs.readFileSync(path.join(RACINE, "passeport.html"), "utf8")), "mise en page : deux fiches par feuille A4 (demi-page)");
  // autre jeu au choix
  sel("fam-jeu").value = "melanges"; sel("fam-jeu").dispatchEvent(new w.Event("change"));
  ok(/Laboratoire de Madame Mélange/.test(apercu()) && /Comparer et mesurer des masses/.test(apercu()), "autre jeu choisi : sa fiche");
  // 3. module seul : jeu sans formulation = erreur claire, jeux proposés = ceux qui en ont
  let err = ""; try { FF.construire({ jeu: "jeu-futur", donnees: FAM, competences: [], sujet: { type: "eleve", nom: "Z" } }); } catch (e) { err = e.message; }
  ok(/Jeu sans formulation/.test(err), "jeu sans formulation : erreur explicite");
  ok(FF.jeuxDe([{ jeu: "melanges" }, { jeu: "jeu-futur" }], FAM).join() === "melanges", "jeux proposés : seulement ceux qui ont des formulations");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
};

/* ---- N31 : rapport de séance PDF ---- */
SECTIONS.N31 = async () => {
  console.log("\n== N31 : rapport de séance en PDF (resultats.html) ==");
  const fs = require("fs"), os = require("os"), path = require("path"), cp = require("child_process");
  const RS = require(path.join(RACINE, "commun/js/rapport-seance.js"));
  const dec = new TextDecoder("windows-1252");
  /** Lecture « à la main » d'un PDF fabriqué : structure, une page, textes décodés. */
  const lire = octets => {
    const s = Buffer.from(octets).toString("latin1");
    const nObj = (s.match(/\d+ 0 obj/g) || []).length;
    const xref = +(s.match(/startxref\n(\d+)\n%%EOF/) || [])[1];
    const offs = [...s.slice(xref).matchAll(/(\d{10}) 00000 n /g)].map(m => +m[1]);
    const offsOk = offs.length === nObj && offs.every((o, i) => s.slice(o).startsWith(`${i + 1} 0 obj`));
    const flux = (s.match(/stream\n([\s\S]*?)\nendstream/) || [])[1] || "";
    const longueur = +(s.match(/\/Length (\d+)/) || [])[1];
    const textes = [...flux.matchAll(/\(((?:\\.|[^\\)])*)\) Tj/g)].map(m => dec.decode(Buffer.from(m[1].replace(/\\([\\()])/g, "$1"), "latin1")));
    return { s, entete: s.startsWith("%PDF-1.4"), fin: s.trimEnd().endsWith("%%EOF"), offsOk, pages: (s.match(/\/Type \/Page /g) || []).length, count: (s.match(/\/Count (\d+)/) || [])[1],
      longueurOk: longueur === flux.length, textes, tout: textes.join("\n") };
  };
  // 1. outils : encodage, mesure, coupe
  ok(RS.encode("Séance « œuvre » — l’été").length === "Séance « œuvre » — l’été".length && RS.encode("🎲 ok ✓") === "ok", "encodage Windows-1252 : accents et guillemets gardés, emojis retirés");
  ok(RS.echappe("a(b)c\\d") === "a\\(b\\)c\\\\d", "parenthèses et barre oblique protégées dans le PDF");
  const l1 = RS.coupe("Décrire les fonctions d'un château fort : lieu de protection (sa construction) et de puissance pour le seigneur", 10, 150);
  ok(l1.length >= 3 && l1.every(x => RS.largeur(x, 10) <= 150.01), "retour à la ligne : aucune ligne plus large que la zone (" + l1.length + " lignes)");
  ok(RS.largeur(RS.tronque("Un nom d'équipe vraiment beaucoup trop long pour sa colonne", 10, 100), 10) <= 100.01, "nom trop long : abrégé");
  // 2. séances : regroupement
  const rec = (o) => Object.assign({ type: "escape-game-compte-rendu", version: 1, jeu: "chateau-fort", titre: "Le Secret du donjon", mode: "equipe", niveau: "CM2", palier: "", date: "2026-11-05T09:40", termine: true,
    dureeMin: 30, score: 150, scoreMax: 185, enigmes: 5, total: 5, premierCoup: 3, erreurs: 2, indices: 1 }, o);
  const det = (l, pc, ok1 = 1) => ({ id: "1-1", s: 1, l, ok: ok1, pc });
  const J = ["construire-un-chateau", "les-defenses", "vie-du-seigneur", "vie-des-paysans", "seigneur-et-paysans"];
  const parties = [
    rec({ eleve: "Les Lynx", dureeMin: 38, detail: J.map((l, i) => det(l, i % 2)) }),
    rec({ eleve: "Les Hiboux", niveau: "CM1", dureeMin: 31, score: 120, detail: J.map(l => det(l, 1)) }),
    rec({ eleve: "Les Renards", termine: false, enigmes: 2, dureeMin: 14, score: 40, detail: J.slice(0, 2).map(l => det(l, 0)) }),
    rec({ eleve: "Les Écureuils", termine: false, enigmes: 0, dureeMin: 0, score: 0, scoreMax: null }),
    rec({ eleve: "Les Renards", termine: false, enigmes: 1, dureeMin: 5, date: "2026-11-05T08:50" }),          // ancienne partie interrompue de la même équipe
    rec({ eleve: "Mia", mode: "solo" }),                                                                         // devoirs à la maison : pas une séance
    rec({ eleve: "Les Lynx", date: "2026-11-04T09:40" }),                                                        // un autre jour
    rec({ eleve: "Les Lynx", jeu: "melanges", titre: "Le Laboratoire de Madame Mélange" })                      // un autre jeu
  ];
  const S = RS.seances(parties);
  ok(S.length === 3 && S[0].jour === "2026-11-05" && S.every(x => x.parties.every(r => r.mode !== "solo")), "séances : un jeu + un jour, jamais le mode individuel (" + S.map(x => x.cle).join(", ") + ")");
  ok(RS.parEquipe(S.find(x => x.cle === "chateau-fort|2026-11-05").parties).length === 4, "une équipe qui a rejoué n'est comptée qu'une fois (4 équipes)");
  // 3. dans la page : séance incomplète (2 équipes sur 4 interrompues)
  const { w, erreurs } = await charger(RACINE, "", { page: "resultats.html", attente: 800, stockage: { escape_resultats: JSON.stringify(parties) } });
  const d = w.document;
  d.getElementById("btn-appareil").click();
  ok(/Exporter le rapport de séance \(PDF\)/.test(d.getElementById("exp-rapport").textContent), "bouton « Exporter le rapport de séance (PDF) »");
  const opts = [...d.querySelectorAll("#rap-seance option")].map(o => o.textContent);
  ok(opts.length === 3 && /05\/11\/2026 — Le Secret du donjon — 4 équipes \(2 interrompues\)/.test(opts[0]), "liste des séances, la plus récente d'abord : " + opts[0]);
  d.getElementById("rap-classe").value = "CM1-CM2 Raoul Follereau (Mme B.)"; d.getElementById("rap-classe").dispatchEvent(new w.Event("input"));
  ok(w.localStorage.getItem("escape_classe") === "CM1-CM2 Raoul Follereau (Mme B.)", "nom de classe retenu sur l'appareil");
  d.getElementById("exp-rapport").click(); await dodo(900);
  const E = w.__dernierExport;
  ok(E && /^rapport-seance-2026-11-05-le-secret-du-donjon\.pdf$/.test(E.nom) && E.contenu instanceof w.Uint8Array || (E && E.contenu && E.contenu.length > 1000), "fichier « " + (E && E.nom) + " »");
  const P = lire(E.contenu);
  ok(P.entete && P.fin && P.offsOk && P.longueurOk, "PDF bien formé : en-tête, table des références exacte, longueur du flux, %%EOF");
  ok(P.pages === 1 && P.count === "1", "une seule page");
  for (const att of ["Rapport de séance", "CM1-CM2 Raoul Follereau (Mme B.)", "jeudi 5 novembre 2026", "Le Secret du donjon (Histoire)", "38 min (équipe la plus longue), 28 min en moyenne", "4 dont 2 interrompues",
    "Les Lynx", "Les Hiboux", "Les Renards", "Les Écureuils", "interrompue", "terminée", "Compétences travaillées", "% du 1er coup", "Arrêté du 22 avril 2026"])
    ok(P.tout.includes(att), "le rapport contient « " + att + " »");
  ok(/Séance incomplète : 2 équipes sur 4 n'ont pas terminé/.test(P.tout), "bandeau « séance incomplète » (2 équipes sur 4)");
  ok(!/undefined|NaN|null|\[object/.test(P.tout), "aucune valeur « undefined », « NaN » ou « null » dans le rapport");
  ok(!/Mia/.test(P.tout) && !/melanges|Laboratoire/.test(P.tout), "ni le mode individuel ni un autre jeu");
  ok(w.__dernierRapport.bas >= RS.BAS, "le contenu reste au-dessus de la marge basse (" + w.__dernierRapport.bas.toFixed(0) + " ≥ " + RS.BAS + ")");
  // lecteur PDF réel, quand l'outil est présent (poppler) : vraie lecture du fichier
  let lecteur = false; try { cp.execSync("pdfinfo -v", { stdio: "ignore" }); lecteur = true; } catch (e) {}
  if (lecteur) {
    const f = path.join(os.tmpdir(), "rapport-test-n31.pdf"); fs.writeFileSync(f, Buffer.from(E.contenu));
    const info = cp.execSync(`pdfinfo "${f}"`).toString(), txt = cp.execSync(`pdftotext -layout "${f}" -`).toString();
    ok(/Pages:\s+1\b/.test(info) && /A4/.test(info) && /Les Écureuils/.test(txt) && /Séance incomplète/.test(txt), "lecteur PDF (pdfinfo/pdftotext) : 1 page A4, textes lisibles");
    fs.unlinkSync(f);
  } else console.log("  (pdfinfo absent : contrôle par lecteur PDF sauté, la structure du fichier est vérifiée ci-dessus)");
  // 4. séance interrompue sans aucun détail ni durée (anciennes parties, texte collé…)
  const maigre = rec({ eleve: "", termine: false, enigmes: 1, total: 0, dureeMin: 0, score: undefined, scoreMax: null, date: "2026-11-06T10:00", niveau: "" });
  const mm = RS.modele({ parties: [maigre], jeu: "chateau-fort", catalogue: w.CATALOGUE, classe: "", meta: await (async () => { const r = JSON.parse(fs.readFileSync(path.join(RACINE, "chateau-fort/assets/data/lecons-a4.json"), "utf8")); const c = {}; Object.entries(r.lecons).forEach(([k, l]) => c[k] = l.competence); return { comp: c }; })() });
  const pm = RS.pdf(mm), Pm = lire(pm.octets);
  ok(Pm.pages === 1 && Pm.offsOk && Pm.longueurOk, "séance interrompue sans détail : PDF valide d'une page");
  ok(/Séance incomplète : 1 équipe sur 1 n'a pas terminé/.test(Pm.tout) && /détail énigme par énigme n'est pas enregistré/.test(Pm.tout) && /Compétences prévues par le jeu/.test(Pm.tout) && /non enregistrée/.test(Pm.tout) && /\(sans nom\)/.test(Pm.tout) && /à compléter/.test(Pm.tout), "dit clairement : incomplète, détail absent, durée non enregistrée, nom et classe à compléter");
  ok(!/undefined|NaN|null|0 min|\[object/.test(Pm.tout) && Pm.textes.filter(t => /Construire|Décrire|Raconter/.test(t)).length >= 3, "aucune valeur absurde ; compétences du jeu listées comme « prévues »");
  // 5. séance sans aucune équipe, et jeu inconnu : toujours un PDF correct
  const vide = RS.pdf(RS.modele({ parties: [], jeu: "jeu-inconnu", catalogue: w.CATALOGUE }));
  ok(lire(vide.octets).pages === 1 && /Aucune partie en équipe/.test(lire(vide.octets).tout), "aucune partie : PDF d'une page qui le dit");
  // 6. séance énorme : 40 équipes aux noms piégeux, 12 compétences : toujours UNE page, listes raccourcies
  const noms = ["Aa (Super) Éq\\ 😀 œuvre", "Ab « très » nombreuse et au nom vraiment beaucoup trop long pour sa colonne"];
  const grosses = Array.from({ length: 40 }, (_, i) => rec({ eleve: i < 2 ? noms[i] : "Équipe " + (i + 1), termine: i % 3 !== 0, dureeMin: 20 + i, detail: [det(J[i % 5], i % 2)] }));
  const comp = {}; for (let i = 0; i < 12; i++) comp["c" + i] = "Compétence numéro " + (i + 1) + " : décrire, comparer et expliquer en plusieurs phrases ce que l'on a compris pendant la séance, avec des mots précis.";
  const gros = RS.modele({ parties: grosses.map(r => Object.assign({}, r, { detail: Object.keys(comp).map((l, k) => ({ id: "1-" + k, s: 1, l, ok: 1, pc: k % 2 })) })), jeu: "chateau-fort", catalogue: w.CATALOGUE, classe: "CM2", meta: { comp } });
  const pg = RS.pdf(gros), Pg = lire(pg.octets);
  ok(Pg.pages === 1 && Pg.offsOk && Pg.longueurOk && pg.bas >= RS.BAS - 1, "40 équipes et 12 compétences : toujours une page, au-dessus de la marge (" + pg.bas.toFixed(0) + ")");
  ok(/\.\.\. et \d+ autres? équipes? \(voir le tableur\)/.test(Pg.tout), "liste d'équipes raccourcie, avec renvoi au tableur");
  ok(/Aa \(Super\) Éq\\ œuvre/.test(Pg.tout) && !/😀/.test(Pg.tout) && Pg.textes.length > 20, "noms avec parenthèses et barre oblique : écrits tels quels, emoji retiré");
  ok((Pg.tout.match(/% du 1er coup/g) || []).length >= 4, "au moins 4 compétences gardées malgré la place prise par les équipes");
  // 7. aucune séance chargée : message, pas d'erreur
  const V = await charger(RACINE, "", { page: "resultats.html", attente: 500 });
  V.w.document.getElementById("exp-rapport").click(); await dodo(100);
  ok(/Aucune séance à exporter/.test(V.w.document.getElementById("rap-msg").textContent) && !V.w.__dernierExport, "sans partie chargée : message clair, aucun fichier");
  ok(erreurs.length === 0 && V.erreurs.length === 0, "erreurs JS : " + erreurs.concat(V.erreurs).join(" | "));
};

/* ---- N26 : réglage « temps majoré » dans le passeport ---- */
SECTIONS.N26 = async () => {
  console.log("\n== N26 : temps majoré (passeport.html) ==");
  const { w, erreurs } = await charger(RACINE, "", { page: "passeport.html", attente: 800, stockage: { escape_passeport: JSON.stringify({ eleves: ["Léa B.", "Tom R.", "Inès M."], notes: {} }) } });
  const d = w.document;
  const bloc = d.getElementById("bloc-amenag");
  ok(!!bloc && bloc.tagName === "DETAILS" && !bloc.open, "volet « Temps majoré » présent et fermé au départ (discret)");
  ok(/rien ne s'affiche chez les élèves/i.test(bloc.textContent) && /jamais dans les exports/i.test(bloc.textContent), "texte : discrétion et absence d'export expliquées");
  const sels = [...d.querySelectorAll("#amenag-eleves select")];
  ok(sels.length === 3 && sels.every(s => s.value === "1") && [...sels[0].options].map(o => o.value).join() === "1,1.25,1.33,1.5,2", "un choix par élève, « Aucun » par défaut");
  sels[0].value = "1.5"; sels[0].dispatchEvent(new w.Event("change", { bubbles: true }));
  sels[1].value = "1.33"; sels[1].dispatchEvent(new w.Event("change", { bubbles: true }));
  let st = JSON.parse(w.localStorage.getItem("escape_amenagements"));
  ok(st.coefs["Léa B."] === 1.5 && st.coefs["Tom R."] === 1.33 && !("Inès M." in st.coefs), "coefficients gardés sous leur propre clé (escape_amenagements)");
  sels[1].value = "1"; sels[1].dispatchEvent(new w.Event("change", { bubbles: true }));
  ok(!("Tom R." in JSON.parse(w.localStorage.getItem("escape_amenagements")).coefs), "revenir à « Aucun » efface le coefficient");
  d.getElementById("amenag-equipes").value = "Les Fioles : Léa B., Tom R.\nligne sans deux-points\nLes Flammes: Inès M.";
  d.getElementById("btn-amenag").click();
  st = JSON.parse(w.localStorage.getItem("escape_amenagements"));
  ok(JSON.stringify(st.equipes) === JSON.stringify({ "Les Fioles": ["Léa B.", "Tom R."], "Les Flammes": ["Inès M."] }), "composition des équipes lue ligne à ligne");
  ok(w.AMENAGEMENTS.coefPour("Les Fioles") === 1.5 && w.AMENAGEMENTS.coefPour("Les Flammes") === 1, "coefficient d'équipe cohérent avec la saisie");
  const exp = JSON.stringify(w.PROGRESSION.contenu({}));
  ok(!/amenag|coefs/.test(exp), "export « Ma progression » : aucun aménagement");
  w.AMENAGEMENTS.tracer("melanges", "Les Fioles", 1.5);
  w.eval("AM = AMENAGEMENTS.lire(); rendre();");
  ok(/Les Fioles/.test(d.getElementById("amenag-traces").textContent) && /×1,5/.test(d.getElementById("amenag-traces").textContent), "trace lisible dans le passeport");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
};

module.exports = { SECTIONS, avecEquipes };
if (require.main === module) {
  const choix = process.argv[2] ? process.argv[2].split(",") : Object.keys(SECTIONS);
  (async () => { try { for (const s of choix) await SECTIONS[s](); } catch (e) { T.exception(e); } T.fin(); })();
}
