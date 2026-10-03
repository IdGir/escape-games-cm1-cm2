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
  ok(d.querySelectorAll(".jeu.avenir").length === 2, "P2 Année B : 2 jeux à venir");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
};

SECTIONS.C3 = async () => {
  console.log("\n== C3 : passeport de compétences (passeport.html) ==");
  const hist = JSON.stringify([{ type: "escape-game-compte-rendu", jeu: "melanges", eleve: "Léa B.", termine: true, score: 200, scoreMax: 235 }]);
  const { w, erreurs } = await charger(RACINE, "", { page: "passeport.html", attente: 1200, stockage: { escape_resultats: hist } });
  const d = w.document, P = w.PASSEPORT;
  ok(P.COMPETENCES.length === 5 * 10 + 8 + 6 + 16, `compétences des 13 jeux publiés, une par leçon (${P.COMPETENCES.length})`);
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
  ok(D.jeux.length === 13 && D.jeux.every(j => fs.existsSync(path.join(RACINE, j.dossier, "index.html"))), "un extrait pour chacun des 13 jeux publiés");
  ok(D.jeux.every(j => /[?&](salle|seance)=/.test(D.EXTRAITS[j.dossier])), "extraits en mode vérification (rien n'est enregistré)");
  await dodo(2700);
  ok(D.etat.i === 0 && /\/\?/.test(w.document.getElementById("cadre").getAttribute("src")), "premier extrait lancé : " + w.document.getElementById("cadre").getAttribute("src"));
  ok(/1 \/ 13/.test(w.document.getElementById("titre").textContent), "bandeau : 1 / 13");
  w.document.getElementById("b-suivant").click();
  ok(D.etat.i === 1, "⏭ extrait suivant");
  w.document.getElementById("b-pause").click(); const avant = D.etat.i; await dodo(400);
  ok(D.etat.pause && D.etat.i === avant, "⏸ pause");
  D.montrer(12); D.montrer(D.etat.i + 1);
  ok(D.etat.i === 0, "la boucle repart au premier jeu");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
};

SECTIONS.D4 = async () => {
  console.log("\n== D4 : éditeur d'énigmes (editeur.html) ==");
  const path = require("path");
  for (const j of ["melanges", "objets-techniques", "station-meteo", "chateau-fort", "moyen-age-abbaye", "constitution", "versailles", "renaissance", "alimentation", "lumiere"]) {
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
  const jeux = C.jeux.filter(j => j.dossier).map(j => j.dossier);
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

module.exports = { SECTIONS, avecEquipes };
if (require.main === module) {
  const choix = process.argv[2] ? process.argv[2].split(",") : Object.keys(SECTIONS);
  (async () => { try { for (const s of choix) await SECTIONS[s](); } catch (e) { T.exception(e); } T.fin(); })();
}
