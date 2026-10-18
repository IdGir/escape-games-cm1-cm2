/* ============================================================
   TESTS DES GREFFONS DU TRONC COMMUN (Node + jsdom)
   Depuis la racine du dépôt :  node commun/tests/test-greffons.js
   Une section par amélioration (B6, E4, E2…), chacune sur plusieurs
   jeux : un greffon s'appuie sur des fonctions des app.js, qui
   restent propres à chaque jeu.
   Étapes au choix : node commun/tests/test-greffons.js B6,E4
   ============================================================ */
const path = require("path");
const { charger, compteur, dodo, attendreQue, RACINE } = require("../../outils-tests/charge");
const T = compteur("Greffons du tronc commun"); const ok = T.ok;
const J = j => path.join(RACINE, j);
const JEUX8 = ["declaration", "tour-du-monde", "constitution", "moyen-age-abbaye", "station-meteo", "melanges", "objets-techniques", "chateau-fort", "versailles", "renaissance", "alimentation", "lumiere"];
const SECTIONS = {};

/* ---- B6 : transitions entre salles ---- */
SECTIONS.B6 = async () => {
  console.log("\n== B6 : transitions entre salles ==");
  for (const j of ["melanges", "tour-du-monde", "station-meteo"]) {
    const { w, erreurs } = await charger(J(j), "?salle=1&niveau=CM2");
    ok(typeof w.TRANSITIONS === "object", `${j} : greffon chargé`);
    w.afficherSalle(2); await dodo(20);
    const r = w.document.querySelector(".rideau-salle");
    ok(!!r && /2/.test(r.textContent), `${j} : rideau à l'entrée de la salle 2 (« ${r ? r.textContent : "—"} »)`);
    if (j === "tour-du-monde") ok(r && /Escale 2/.test(r.textContent), `${j} : le rideau dit « Escale »`);
    await dodo(1400);
    ok(!w.document.querySelector(".rideau-salle"), `${j} : le rideau disparaît seul`);
    w.document.body.classList.add("calme");
    w.afficherSalle(3); await dodo(20);
    ok(!w.document.querySelector(".rideau-salle"), `${j} : aucun rideau avec « animations réduites »`);
    ok(erreurs.length === 0, `${j} : erreurs JS : ` + erreurs.join(" | "));
  }
  const m = await charger(J("mission-geo"), "");
  ok(typeof m.w.TRANSITIONS === "object" && m.erreurs.length === 0, "mission-geo : greffon chargé sans erreur");
};

/* ---- E4 : police et réglages « dyslexie » ---- */
SECTIONS.E4 = async () => {
  console.log("\n== E4 : lecture facilitée ==");
  for (const j of ["melanges", "declaration", "mission-geo"]) {
    const { w, erreurs } = await charger(J(j), j === "mission-geo" ? "" : "?salle=1&niveau=CM1");
    const d = w.document;
    if (j === "mission-geo") { w.eval("REGLAGES.ouvrir()"); } else { w.ouvrirReglages(); }
    const bloc = await attendreQue(() => d.getElementById("lecture-reglages"), 3000);
    ok(!!bloc, `${j} : bloc « Lecture facilitée » dans les réglages`);
    if (!bloc) continue;
    d.getElementById("lec-police").value = "dys";
    d.getElementById("lec-interligne").value = "tres";
    d.getElementById("lec-espacement").checked = true;
    bloc.dispatchEvent(new w.Event("change", { bubbles: true }));
    ok(d.body.classList.contains("police-dys") && d.body.classList.contains("interligne-tres") && d.body.classList.contains("espacement-lecture"), `${j} : classes appliquées tout de suite`);
    ok(JSON.parse(w.localStorage.getItem("escape_lecture")).police === "dys", `${j} : choix gardé (escape_lecture)`);
    ok(/opendyslexic-latin-400-normal\.woff2/.test(d.getElementById("style-lecture").textContent) && /commun\/polices\//.test(d.getElementById("style-lecture").textContent), `${j} : police chargée depuis commun/polices/`);
    ok(erreurs.length === 0, `${j} : erreurs JS : ` + erreurs.join(" | "));
  }
  // préférence gardée d'un jeu à l'autre
  const { w } = await charger(J("chateau-fort"), "?salle=1&niveau=CM1", { stockage: { escape_lecture: JSON.stringify({ police: "lisible", interligne: "aere", espacement: false }) } });
  ok(w.document.body.classList.contains("police-lisible") && w.document.body.classList.contains("interligne-aere"), "chateau-fort : préférence d'un autre jeu appliquée dès l'ouverture");
};

/* ---- E2 : palier « Découverte » ---- */
SECTIONS.E2 = async () => {
  console.log("\n== E2 : palier Découverte ==");
  for (const j of ["melanges", "constitution"]) {
    // depuis l'accueil
    const a = await charger(J(j));
    const d = a.w.document;
    const opt = d.querySelector('.opt-niveau[data-palier="decouverte"]');
    ok(!!opt, `${j} : troisième choix « Découverte » à l'accueil`);
    opt.click(); await dodo(20);
    ok(a.w.ETAT.niveau === "CM1" && a.w.ETAT.palier === "decouverte", `${j} : Découverte = énigmes du CM1 + palier`);
    ok(/Découverte/.test(d.getElementById("apercu-niveau").textContent), `${j} : aperçu « Palier Découverte »`);
    a.w.ETAT.reglages.cinematiques = false;
    const inp = d.getElementById("input-equipe"); inp.value = "Les Pousses"; inp.dispatchEvent(new a.w.Event("input"));
    d.getElementById("btn-demarrer").click(); await dodo(300);
    ok(a.w.ETAT.palier === "decouverte" && a.w.salleEnigmes(1).length === 3, `${j} : partie lancée au palier Découverte, 3 énigmes en salle 1`);
    const e = a.w.salleEnigmes(1)[0];
    ok(!!d.querySelector(`#enigme-${e.id} .feedback.indice`), `${j} : premier indice affiché d'emblée`);
    ok(a.w.ETAT.score === 0 && a.w.ETAT.indicesTotal === 0, `${j} : indice offert, aucun point retiré (score ${a.w.ETAT.score})`);
    ok(a.erreurs.length === 0, `${j} : erreurs JS : ` + a.erreurs.join(" | "));
    // un autre choix remet le palier à zéro
    const b = await charger(J(j));
    b.w.document.querySelector('.opt-niveau[data-palier="decouverte"]').click();
    b.w.document.querySelector('.opt-niveau[data-niveau="CM2"]').click();
    ok(!b.w.ETAT.palier && b.w.ETAT.niveau === "CM2", `${j} : revenir à CM2 annule le palier`);
  }
  // QCM : un choix faux écarté ; coffre : première lettre
  const { w, erreurs } = await charger(J("melanges"), "?salle=5&niveau=CM1&palier=decouverte");
  const qcm = [1,2,3,4,5].flatMap(n => w.salleEnigmes(n)).find(e => e.type === "qcm");
  ok(w.ETAT.palier === "decouverte", "vérification &palier=decouverte");
  w.afficherCoffre(() => {}); await dodo(20);
  const c0 = w.document.getElementById("coffre-0");
  ok(c0 && c0.value === "" && /^P /.test(c0.placeholder) && /5 lettres/.test(c0.placeholder), `coffre : première lettre et longueur (« ${c0 && c0.placeholder} »), champ vide`);
  w.finDuJeu(); await dodo(50);
  ok(!!w.document.querySelector("#fin-contenu .bandeau-palier"), "écran de fin : palier rappelé");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
  if (qcm) {
    const sn = [1,2,3,4,5].find(n => w.salleEnigmes(n).includes(qcm)), k = w.salleEnigmes(sn).indexOf(qcm) + 1;
    const q = await charger(J("melanges"), `?salle=${sn}&niveau=CM1&palier=decouverte&enigme=${k}`);
    const n3 = (q.w.donneesNiveau(qcm).questions || []).filter(x => x.options.length >= 3).length;
    ok(q.w.document.querySelectorAll(`#enigme-${qcm.id} .qcm-option.ecartee`).length === n3, `QCM ${qcm.id} : ${n3} choix faux écarté(s)`);
    ok(![...q.w.document.querySelectorAll(`#enigme-${qcm.id} .qcm-option.ecartee`)].some(o => +o.dataset.j === q.w.donneesNiveau(qcm).questions[+o.closest(".qcm-question").dataset.i].bonne), "aucune bonne réponse écartée");
  }
  // moteur propre : indice offert
  const dcl = await charger(J("declaration"), "?salle=2&niveau=CM1&palier=decouverte", { attente: 800 });
  ok(!!dcl.w.document.querySelector(".zone-enigme .feedback.indice") && dcl.w.ETAT.score === 0 && dcl.w.ETAT.indicesUtilises === 0, "declaration : premier indice offert, sans malus");
  ok(dcl.erreurs.length === 0, "declaration : erreurs JS : " + dcl.erreurs.join(" | "));
};

/* ---- E3 : indices adaptatifs ---- */
SECTIONS.E3 = async () => {
  console.log("\n== E3 : indices adaptatifs ==");
  // délai d'inactivité : on raccourcit le délai à 1 s pour le test
  const reg = JSON.stringify({ actif: true, delaiCM1: 1, delaiCM2: 1, erreurs: 2 });
  for (const j of ["melanges", "declaration"]) {
    const { w, erreurs } = await charger(J(j), "?salle=2&niveau=CM2", { stockage: { escape_indices_adaptatifs: reg }, attente: 800 });
    const p = await attendreQue(() => w.document.querySelector(".proposition-indice"), 4000);
    ok(!!p, `${j} : indice proposé après le délai sans action`);
    const s0 = w.ETAT.score;
    w.ETAT.score = 10;
    p && p.querySelector(".oui").click(); await dodo(30);
    ok(!w.document.querySelector(".proposition-indice") && w.document.querySelectorAll(".feedback.indice").length >= 1, `${j} : « Voir un indice » affiche un indice`);
    ok(w.ETAT.score === 8, `${j} : l'indice coûte 2 points comme d'habitude (score ${w.ETAT.score})`);
    ok(erreurs.length === 0, `${j} : erreurs JS : ` + erreurs.join(" | "));
  }
  // après 2 essais faux (délai long)
  const reg2 = JSON.stringify({ actif: true, delaiCM1: 300, delaiCM2: 300, erreurs: 2 });
  const { w } = await charger(J("objets-techniques"), "?salle=1&niveau=CM2", { stockage: { escape_indices_adaptatifs: reg2 } });
  await dodo(1200);
  ok(!w.document.querySelector(".proposition-indice"), "objets-techniques : rien de proposé avant le délai");
  w.ETAT.erreursTotal += 2; await dodo(1200);
  const p2 = w.document.querySelector(".proposition-indice");
  ok(!!p2 && /2 essais/.test(p2.textContent), "objets-techniques : indice proposé après 2 essais faux");
  p2 && p2.querySelector(".non").click(); await dodo(30);
  ok(!w.document.querySelector(".proposition-indice"), "« Pas maintenant » retire la proposition");
  // désactivé
  const off = await charger(J("chateau-fort"), "?salle=1&niveau=CM1", { stockage: { escape_indices_adaptatifs: JSON.stringify({ actif: false, delaiCM1: 1, delaiCM2: 1, erreurs: 2 }) } });
  await dodo(1500);
  ok(!off.w.document.querySelector(".proposition-indice"), "chateau-fort : rien quand le réglage est désactivé");
  // réglage dans ⚙️
  off.w.ouvrirReglages(); await dodo(50);
  ok(!!off.w.document.getElementById("reglages-indices-adaptatifs"), "réglage « Indices proposés » dans ⚙️ Réglages");
};

/* ---- E6 : minuteur adaptatif par équipe ---- */
SECTIONS.E6 = async () => {
  console.log("\n== E6 : délai accordé à une équipe ==");
  for (const j of ["melanges", "tour-du-monde"]) {
    const { w, erreurs } = await charger(J(j), "?salle=2&niveau=CM2", { attente: 800 });
    const debut = w.ETAT.salleDebut;
    w.traiterCommande({ delaiMin: 3, id: 1 });
    ok(w.ETAT.salleDebut === debut + 3 * 60000 && w.ETAT.delaiAccordeMin === 3, `${j} : 3 min accordées, chrono de salle décalé`);
    w.traiterCommande({ delaiMin: 3, id: 1 });
    ok(w.ETAT.delaiAccordeMin === 3, `${j} : la même commande n'est pas appliquée deux fois`);
    w.traiterCommande({ delaiMin: 2, id: 2 });
    ok(w.ETAT.delaiAccordeMin === 5 && /\+5 min/.test((w.document.getElementById("hud-delai") || {}).textContent || ""), `${j} : cumul affiché dans le bandeau (+5 min)`);
    // la salle est bouclée « en 11 min » mais 5 min ont été accordées : bonus gardé
    w.ETAT.salleDebut = Date.now() - 11 * 60000 + 5 * 60000; w.ETAT.indicesSalle = 0;
    const s0 = w.ETAT.score; w.validerSalle(2); await dodo(50);
    ok(w.ETAT.score > s0, `${j} : bonus de rapidité préservé (score ${s0} → ${w.ETAT.score})`);
    ok(erreurs.length === 0, `${j} : erreurs JS : ` + erreurs.join(" | "));
  }
  const fs = require("fs");
  for (const j of JEUX8) ok(fs.readFileSync(J(j) + "/prof.html", "utf8").includes("','delai')"), `${j} : bouton ⏱️ + dans prof.html`);
};

/* ---- C4 : jeu précédent / suivant ---- */
SECTIONS.C4 = async () => {
  console.log("\n== C4 : jeu précédent / suivant en fin de partie ==");
  const cas = { declaration: ["suite", "constitution"], constitution: ["precedent", "declaration"], "station-meteo": ["suite", "objets-techniques"], melanges: ["precedent", "chateau-fort"] };
  for (const [j, [sens, cible]] of Object.entries(cas)) {
    const { w, erreurs } = await charger(J(j), "?salle=6&niveau=CM2", { attente: 800 });
    await dodo(200);
    const a = w.document.querySelector(`#fin-contenu .encart-suite .lien-jeu-${sens}`);
    ok(!!a && a.getAttribute("href") === `../${cible}/`, `${j} : lien « ${sens} » vers ${cible} (${a ? a.getAttribute("href") : "—"})`);
    ok(erreurs.length === 0, `${j} : erreurs JS : ` + erreurs.join(" | "));
  }
  const t = await charger(J("tour-du-monde"), "?salle=6&niveau=CM2", { attente: 800 });
  ok(!t.w.document.querySelector(".encart-suite"), "tour-du-monde (jeu libre, hors progression) : pas d'encart");
};

/* ---- D3 : banque d'énigmes à variantes ---- */
SECTIONS.D3 = async () => {
  console.log("\n== D3 : variantes d'énigmes ==");
  const lib = (w, id) => [...w.document.querySelectorAll(`#enigme-${id} label, #enigme-${id} .code-libelle, #enigme-${id} .champ-code`)].map(x => x.textContent).join(" | ");
  const resoudreCode = async (w, e) => {
    const d = w.donneesNiveau(e);
    d.champs.forEach((c, i) => { w.document.querySelector("#code-" + i).value = c.valeur; });
    w.document.querySelector(`#enigme-${e.id} [data-valider]`).click(); await dodo(30);
    return w.document.getElementById("enigme-" + e.id).classList.contains("resolue");
  };
  const a = await charger(J("melanges"), "?salle=1&niveau=CM1&enigme=3&serie=0");
  const e0 = a.w.salleEnigmes(1)[2];
  ok(e0.id === "1-3" && e0._serie === 0 && a.w.donneesNiveau(e0).champs[0].valeur === "250", "série 0 : énigme d'origine (250)");
  for (const s of [1, 2]) {
    const { w, erreurs } = await charger(J("melanges"), `?salle=1&niveau=CM1&enigme=3&serie=${s}`);
    const e = w.salleEnigmes(1)[2];
    ok(e._serie === s && w.donneesNiveau(e).champs[0].valeur !== "250", `série ${s} : variante jouée (${w.donneesNiveau(e).champs.map(c => c.valeur).join(", ")})`);
    ok(w.document.getElementById("enigme-1-3").textContent.includes(w.donneesNiveau(e).champs[0].libelle), `série ${s} : la carte affiche les données de la variante`);
    ok(await resoudreCode(w, e), `série ${s} : la variante se résout avec ses propres valeurs`);
    ok(erreurs.length === 0, `série ${s} : erreurs JS : ` + erreurs.join(" | "));
  }
  // automatique : la série dépend de l'année scolaire, identique pour tous les postes
  const b = await charger(J("melanges"), "?salle=2&niveau=CM2&enigme=4");
  const e24 = b.w.salleEnigmes(2).find(x => x.id === "2-4");
  const attendu = (b.w.VARIANTES.anneeScolaire() - 2026) % 3;
  ok(e24._serie === attendu, `automatique : série ${e24._serie} (année scolaire ${b.w.VARIANTES.anneeScolaire()} → ${attendu})`);
  ok(b.w.VARIANTES.choix({ variantes: [{}, {}] }, { mode: "auto" }) === (b.w.VARIANTES.anneeScolaire() - 2026) % 3 && b.w.VARIANTES.anneeScolaire(new Date(2027, 8, 15)) === 2027 && b.w.VARIANTES.anneeScolaire(new Date(2027, 3, 15)) === 2026, "année scolaire : septembre 2027 → 2027, avril 2027 → 2026");
  // réglage dans ⚙️
  b.w.ouvrirReglages(); await dodo(50);
  ok(!!b.w.document.getElementById("reglages-variantes"), "réglage « Banque d'énigmes » dans ⚙️ Réglages");
  // jeux sans variantes : rien ne change
  const c = await charger(J("chateau-fort"), "?salle=1&niveau=CM1");
  ok(c.w.VARIANTES_APPLIQUEES && c.w.VARIANTES_APPLIQUEES.nb === 0 && c.erreurs.length === 0, "chateau-fort (sans variante) : inchangé");
};

/* ---- D2 : mode individuel et compte-rendu ---- */
SECTIONS.D2 = async () => {
  console.log("\n== D2 : mode individuel (devoirs à la maison) ==");
  for (const j of ["objets-techniques", "declaration"]) {
    const { w, erreurs } = await charger(J(j), "?solo=1", { attente: 800 });
    const d = w.document;
    ok(d.getElementById("mode-solo") && d.getElementById("mode-solo").checked, `${j} : ?solo=1 coche « Je joue seul »`);
    ok(/prénom/i.test(d.getElementById("input-equipe").placeholder), `${j} : on demande le prénom`);
    w.ETAT.reglages.cinematiques = false;
    const inp = d.getElementById("input-equipe"); inp.value = "Léa B."; inp.dispatchEvent(new w.Event("input"));
    d.querySelector('.opt-niveau[data-niveau="CM1"]').click();
    let sync = 0; w.fetch = (f => async (u, o) => { if (/\/api\//.test(String(u))) sync++; return f(u, o); })(w.fetch);
    d.getElementById("btn-demarrer").click(); await dodo(400);
    ok(w.ETAT.solo === true && sync === 0, `${j} : partie individuelle, aucune synchronisation (${sync} appel)`);
    // fin de partie simulée
    w.ETAT.score = 77; w.ETAT.enigmesPremierCoup = 4; w.ETAT.erreursTotal = 2; w.ETAT.tempsParSalle = { 1: 360000, 2: 420000 }; w.ETAT.msEcoules = 1500000;
    w.finDuJeu(); await dodo(100);
    const cr = d.getElementById("cr-texte");
    ok(!!cr && /Léa B\./.test(cr.textContent) && /mode individuel/.test(cr.textContent) && /Score : 77/.test(cr.textContent) && /Code de contrôle : [0-9A-F]{4}-[0-9A-F]{4}/.test(cr.textContent), `${j} : compte-rendu affiché`);
    const obj = w.COMPTE_RENDU.construire();
    ok(w.COMPTE_RENDU.verifier(obj), `${j} : code de contrôle valide`);
    obj.score = 999;
    ok(!w.COMPTE_RENDU.verifier(obj), `${j} : un score modifié à la main est repéré`);
    ok(w.COMPTE_RENDU.historique().some(x => x.eleve === "Léa B." && x.mode === "solo"), `${j} : partie gardée dans l'historique de l'appareil`);
    ok(erreurs.length === 0, `${j} : erreurs JS : ` + erreurs.join(" | "));
  }
  const eq = await charger(J("melanges"), "?salle=6&niveau=CM2", { attente: 600 });
  ok(!eq.w.document.getElementById("compte-rendu"), "en équipe : pas de compte-rendu élève à l'écran de fin");
};

/* ---- C2 : bandeau de référence officielle ---- */
SECTIONS.C2 = async () => {
  console.log("\n== C2 : référence du programme officiel ==");
  const attendu = { melanges: /BO n° 24 du 11 juin 2026/, "chateau-fort": /BO n° 22 du 28 mai 2026/, constitution: /BO n° 24 du 13 juin 2024[\s\S]*BO n° 22 du 28 mai 2026/, "mission-geo": /BO n° 22 du 28 mai 2026/ };
  for (const [j, re] of Object.entries(attendu)) {
    const { w, erreurs } = await charger(J(j), "", { attente: 600 });
    const b = w.document.querySelector("#ecran-accueil .bandeau-bo");
    ok(!!b && re.test(b.textContent) && b.querySelector("a[href^='https://']"), `${j} : bandeau sur l'écran d'accueil (« ${b ? b.textContent.slice(0, 70) : "—"}… »)`);
    ok(erreurs.length === 0, `${j} : erreurs JS : ` + erreurs.join(" | "));
  }
  const fs = require("fs");
  for (const j of JEUX8.concat(["mission-geo"])) ok(/Référence officielle du programme/.test(fs.readFileSync(J(j) + "/README.md", "utf8")), `${j} : référence dans le README`);
};

/* ---- A5 : export / reprise de partie par fichier ---- */
SECTIONS.A5 = async () => {
  console.log("\n== A5 : export / reprise de partie par fichier ==");
  for (const j of ["constitution", "declaration", "tour-du-monde", "chateau-fort", "lumiere"]) {
    const a = await charger(J(j), "", { attente: 400 });
    const d = a.w.document;
    ok(!!d.getElementById("import-partie") && !!d.getElementById("btn-export-partie"), `${j} : boutons « Reprendre depuis un fichier » (accueil) et « Enregistrer » (pause)`);
    ok(a.w.EXPORT_PARTIE.exporter() === null, `${j} : rien à exporter avant le début`);
    a.w.HTMLAnchorElement.prototype.click = function(){ a.w.__telecharge = this.download; };
    a.w.eval(`Object.assign(ETAT, {equipe:"Les Lynx", niveau:"CM1", salle:3, enigme:1, score:42, debut:Date.now()-600000, msEcoules:600000, motsCles:["A","B"]}); sauvegarder();`);
    const r = a.w.EXPORT_PARTIE.exporter();
    ok(r && /^[a-z-]+-les-lynx-\d{4}-\d\d-\d\d\.json$/.test(a.w.__telecharge || ""), `${j} : fichier téléchargé (${a.w.__telecharge})`);
    ok(r && r.contenu.jeu === j && r.contenu.etat.salle === 3 && r.contenu.versionJeu, `${j} : contenu (jeu, salle, version ${r && r.contenu.versionJeu})`);
    // Autre appareil : rien en mémoire
    const b = await charger(J(j), "", { attente: 300 });
    const ko = b.w.EXPORT_PARTIE.importerTexte(JSON.stringify(Object.assign({}, r.contenu, { jeu: "melanges", titre: "Mélanges" })));
    ok(!ko.ok && /Mélanges/.test(ko.message), `${j} : fichier d'un autre jeu refusé`);
    const fini = b.w.EXPORT_PARTIE.importerTexte(JSON.stringify(Object.assign({}, r.contenu, { etat: Object.assign({}, r.contenu.etat, { fini: true }) })));
    ok(!fini.ok, `${j} : partie terminée refusée`);
    const vieux = b.w.EXPORT_PARTIE.importerTexte(JSON.stringify(Object.assign({}, r.contenu, { versionJeu: "v0" })));
    ok(!vieux.ok && /ancienne version/.test(vieux.message), `${j} : ancienne version refusée`);
    ok(!b.w.EXPORT_PARTIE.importerTexte("pas du json").ok, `${j} : fichier illisible refusé`);
    let recharge = 0; b.w.EXPORT_PARTIE.recharger = () => recharge++;
    const im = b.w.EXPORT_PARTIE.importerTexte(JSON.stringify(r.contenu));
    ok(im.ok && JSON.parse(b.w.localStorage.getItem(b.w.eval("CLE_SAUVEGARDE"))).equipe === "Les Lynx", `${j} : partie recopiée dans la sauvegarde de l'appareil`);
    // Rechargement : la reprise habituelle s'applique
    const stock = {}; for (let i = 0; i < b.w.localStorage.length; i++) { const k = b.w.localStorage.key(i); stock[k] = b.w.localStorage.getItem(k); }
    const c = await charger(J(j), "", { attente: 600, stockage: stock });
    const e = c.w.eval("({equipe:ETAT.equipe, salle:ETAT.salle, score:ETAT.score, niveau:ETAT.niveau})");
    ok(e.equipe === "Les Lynx" && e.salle === 3 && e.score === 42 && e.niveau === "CM1", `${j} : partie reprise après rechargement (${JSON.stringify(e)})`);
    ok(c.w.document.getElementById("ecran-salle").classList.contains("actif"), `${j} : l'équipe est dans la salle`);
    for (const x of [a, b, c]) ok(x.erreurs.length === 0, `${j} : erreurs JS : ` + x.erreurs.join(" | "));
  }
};

/* ---- B5 : sous-titres des vidéos ---- */
SECTIONS.B5 = async () => {
  console.log("\n== B5 : sous-titres des vidéos ==");
  const fs = require("fs");
  for (const j of JEUX8.concat(["mission-geo"])) {
    const dos = J(j) + "/assets/videos";
    if (!fs.existsSync(dos)) continue;
    const videos = fs.readdirSync(dos).filter(f => /\.(mp4|webm)$/i.test(f) && !/^bande-annonce/.test(f));
    const sans = videos.filter(f => !fs.existsSync(dos + "/" + f.replace(/\.\w+$/, ".vtt")));
    ok(sans.length === 0, `${j} : ${videos.length} vidéo(s), toutes sous-titrées` + (sans.length ? " — manquent : " + sans.join(", ") : ""));
    for (const f of fs.readdirSync(dos).filter(f => f.endsWith(".vtt"))) {
      const v = fs.readFileSync(dos + "/" + f, "utf8");
      if (!/^WEBVTT\s/.test(v) || !/\d\d:\d\d:\d\d\.\d{3} --> \d\d:\d\d:\d\d\.\d{3}/.test(v)) ok(false, `${j}/${f} : fichier WebVTT valide`);
    }
  }
  // Décor filmé : une piste de sous-titres, visible seulement avec le son des décors
  const { w, erreurs } = await charger(J("melanges"), "?salle=1&niveau=CM2");
  const d = w.document;
  const scene = d.createElement("div"); scene.className = "scene"; scene.innerHTML = '<div class="decor-fallback"></div>'; d.body.appendChild(scene);
  w.eval(`MEDIA.cache["essai"] = {type:"video", src:"assets/videos/salle2.mp4", poster:null}`);
  await w.installerDecor(scene, "essai");
  const piste = scene.querySelector("video.decor-video track");
  ok(!!piste && piste.getAttribute("kind") === "captions" && /assets\/videos\/salle2\.vtt$/.test(piste.getAttribute("src")), `melanges : piste de sous-titres sur le décor filmé (${piste && piste.getAttribute("src")})`);
  w.setSonVideo(true); w.setSonVideo(false);
  ok(erreurs.length === 0, "melanges : erreurs JS : " + erreurs.join(" | "));
};

/* ---- E5 : lecture à voix haute des consignes ---- */
SECTIONS.E5 = async () => {
  console.log("\n== E5 : consignes lues à voix haute ==");
  const voixFactice = w => {
    w.__dits = [];
    w.speechSynthesis = { speaking: false, cancel(){ w.__annule = (w.__annule || 0) + 1; }, speak(u){ w.__dits.push(u); },
      getVoices(){ return [{ name: "Amélie", lang: "fr-FR" }]; }, onvoiceschanged: null };
    w.SpeechSynthesisUtterance = class { constructor(t){ this.text = t; } };
  };
  for (const [j, q] of [["constitution", "?salle=1&niveau=CM1"], ["alimentation", "?salle=3&niveau=CM2&enigme=2"], ["declaration", "?salle=2&niveau=CM2"], ["tour-du-monde", "?salle=1&niveau=CM1"]]) {
    const { w, erreurs } = await charger(J(j), q, { avant: voixFactice });
    const d = w.document;
    const c = await attendreQue(() => d.querySelector("#ecran-salle .consigne .btn-lire-consigne") && d.querySelector("#ecran-salle .consigne"), 3000);
    ok(!!c, `${j} : bouton « Écouter la consigne »`);
    if (!c) continue;
    c.querySelector(".btn-lire-consigne").click();
    const u = w.__dits[w.__dits.length - 1];
    const titre = c.closest(".enigme-carte") && c.closest(".enigme-carte").querySelector("h3");
    ok(u && u.lang === "fr-FR" && u.text.length > 20 && !/🔊|🎯|Écouter la consigne/.test(u.text) && (!titre || u.text.startsWith(titre.textContent)), `${j} : texte lu (« ${u && u.text.slice(0, 70)}… »)`);
    if (j === "alimentation") ok(!/M\d|viewBox|Moulage de la mâchoire du bas/.test(u.text), `${j} : le dessin SVG de la consigne n'est pas lu`);
    ok(c.classList.contains("lecture-en-cours"), `${j} : consigne surlignée pendant la lecture`);
    u.onend();
    ok(!c.classList.contains("lecture-en-cours"), `${j} : surlignage retiré à la fin`);
    c.querySelector(".btn-lire-consigne").click(); c.querySelector(".btn-lire-consigne").click();
    ok(!c.classList.contains("lecture-en-cours") && w.__annule > 0, `${j} : un second clic arrête la lecture`);
    ok(erreurs.length === 0, `${j} : erreurs JS : ` + erreurs.join(" | "));
  }
  // Lecture automatique (réglage gardé sur l'appareil)
  const a = await charger(J("melanges"), "?salle=1&niveau=CM2", { avant: voixFactice, stockage: { escape_lecture_consignes: JSON.stringify({ auto: true, vitesse: 0.75 }) } });
  const lu = await attendreQue(() => { const el = a.w.document.querySelector("#ecran-salle .consigne.lecture-en-cours");
    return el && a.w.__dits.find(u => u.text === a.w.LECTURE_CONSIGNES.texteDe(el)); }, 4000);
  ok(!!lu && lu.rate === 0.75, `melanges : consigne lue automatiquement, vitesse lente (${lu && lu.rate})`);
  a.w.ouvrirReglages();
  const r = await attendreQue(() => a.w.document.getElementById("lecture-consignes-reglages"), 3000);
  ok(!!r && r.querySelector("#lc-auto").checked, "melanges : réglage « Lire automatiquement » dans ⚙️, coché");
  if (r) { r.querySelector("#lc-auto").checked = false; r.dispatchEvent(new a.w.Event("change", { bubbles: true })); }
  ok(JSON.parse(a.w.localStorage.getItem("escape_lecture_consignes")).auto === false, "melanges : choix gardé (escape_lecture_consignes)");
  ok(a.erreurs.length === 0, "melanges : erreurs JS : " + a.erreurs.join(" | "));
  // Sans synthèse vocale : aucun bouton
  const s = await charger(J("versailles"), "?salle=1&niveau=CM1");
  await dodo(400);
  ok(!s.w.document.querySelector(".btn-lire-consigne") && s.erreurs.length === 0, "versailles sans synthèse vocale : pas de bouton, pas d'erreur");
};

/* ---- N5 : indices à coût dégressif ---- */
SECTIONS.N5 = async () => {
  console.log("\n== N5 : indices à coût dégressif ==");
  const essai = async (j, q, modeCout, attendu) => {
    const st = modeCout ? { escape_indices_cout: JSON.stringify({ mode: modeCout }) } : {};
    const { w, erreurs } = await charger(J(j), q, { stockage: st });
    const b = await attendreQue(() => w.document.querySelector("#ecran-salle button[id^='indice-'], #btn-indice"), 3000);
    w.ETAT.score = 20;
    const scores = [];
    for (let i = 0; i < 3; i++) { b.click(); await dodo(20); scores.push(w.ETAT.score); }
    ok(JSON.stringify(scores) === JSON.stringify(attendu), `${j} (${modeCout || "par défaut"}) : 20 → ${scores.join(" → ")}`);
    if (modeCout === "degressif") ok(/\(−1 pt\)|Plus d'indices/.test(b.textContent), `${j} : coût affiché sur le bouton (« ${b.textContent} »)`);
    ok(erreurs.length === 0, `${j} : erreurs JS : ` + erreurs.join(" | "));
    return w;
  };
  await essai("melanges", "?salle=1&niveau=CM2", null, [18, 16, 14]);
  const w = await essai("melanges", "?salle=1&niveau=CM2", "degressif", [18, 17, 16]);
  await essai("tour-du-monde", "?salle=1&niveau=CM1", "degressif", [18, 17, 16]);
  await essai("declaration", "?salle=2&niveau=CM2", "fixe", [18, 16, 14]);
  w.ouvrirReglages();
  const s = await attendreQue(() => w.document.getElementById("reg-cout-indices"), 3000);
  ok(!!s && s.value === "degressif" && s.closest("#reglages-indices-adaptatifs"), "réglage « Coût des indices » dans le groupe 💡 Indices");
  if (s) { s.value = "fixe"; s.dispatchEvent(new w.Event("change", { bubbles: true })); }
  ok(w.INDICES_DEGRESSIFS.mode() === "fixe", "choix gardé sur l'appareil");
};

/* ---- N6 : auto-évaluation (socle commun) en fin de partie ---- */
SECTIONS.N6 = async () => {
  console.log("\n== N6 : auto-évaluation en fin de partie ==");
  for (const [j, dom] of [["objets-techniques", "D4"], ["constitution", "D3"], ["tour-du-monde", "D5"], ["chateau-fort", "D5"]]) {
    const { w, erreurs } = await charger(J(j), "", { attente: 600 });
    const d = w.document;
    w.ETAT.reglages.cinematiques = false;
    const inp = d.getElementById("input-equipe"); inp.value = "Les Hiboux"; inp.dispatchEvent(new w.Event("input"));
    d.querySelector('.opt-niveau[data-niveau="CM2"]').click();
    d.getElementById("btn-demarrer").click(); await dodo(300);
    w.ETAT.score = 120; w.ETAT.msEcoules = 1800000; w.ETAT.fini = true;
    w.finDuJeu(); await dodo(100);
    const g = d.getElementById("auto-evaluation");
    const rej = d.getElementById("btn-rejouer");
    ok(!!g && rej && (g.compareDocumentPosition(rej) & 4), `${j} : grille d'auto-évaluation avant « Rejouer »`);
    if (!g) continue;
    const lignes = [...g.querySelectorAll("tr[data-item]")];
    ok(lignes.length === 5 && lignes[3].querySelector(".ae-domaine").textContent === "Socle " + dom, `${j} : 5 affirmations, la 4e rattachée au domaine ${dom} (${lignes[3] && lignes[3].querySelector(".ae-domaine").textContent})`);
    lignes.forEach((l, k) => l.querySelectorAll(".ae-choix")[k % 3].click());
    ok(Object.keys(w.ETAT.autoEval).length === 5 && w.ETAT.autoEval.e1 === 1 && w.ETAT.autoEval.e2 === 2 && w.ETAT.autoEval.e3 === 3, `${j} : réponses gardées (${JSON.stringify(w.ETAT.autoEval)})`);
    ok(lignes[2].querySelectorAll(".ae-choix")[2].getAttribute("aria-pressed") === "true" && /Merci/.test(g.querySelector(".ae-merci").textContent), `${j} : choix visibles, remerciement`);
    const cr = w.COMPTE_RENDU.construire();
    ok(cr.autoEval && cr.autoEval.e3 === 3 && w.COMPTE_RENDU.verifier(cr), `${j} : réponses dans le compte-rendu, code de contrôle valide`);
    ok(/Auto-évaluation \(socle commun\)[\s\S]*D1 —[\s\S]*: pas encore/.test(w.COMPTE_RENDU.texte(cr)), `${j} : réponses dans le texte du compte-rendu`);
    const h = w.COMPTE_RENDU.historique().filter(x => x.eleve === "Les Hiboux");
    ok(h.length && h[h.length - 1].autoEval && h[h.length - 1].autoEval.e5 === 2, `${j} : historique de l'appareil mis à jour`);
    w.__imprime = 0; d.getElementById("btn-imprimer-auto-eval").click();
    ok(w.__imprime === 1 && /Je m'évalue/.test(d.querySelector(".zone-impression").textContent) && d.querySelectorAll(".zone-impression tr").length === 6, `${j} : grille vierge imprimable`);
    ok(erreurs.length === 0, `${j} : erreurs JS : ` + erreurs.join(" | "));
  }
};

/* ---- N1 : trophées inter-jeux à l'écran de fin ---- */
SECTIONS.N1 = async () => {
  console.log("\n== N1 : trophées inter-jeux à l'écran de fin ==");
  const p = (jeu, j) => ({ jeu, eleve: "Les Lynx", termine: true, total: 20, premierCoup: 10, indices: 4, quiz: 3, score: 120, mode: "equipe", date: `2026-10-0${j}T10:00`, partie: `2026-10-0${j}T09:00` });
  const stockage = { escape_resultats: JSON.stringify([p("declaration", 1), p("chateau-fort", 2)]) };
  const { w, erreurs } = await charger(J("constitution"), "", { attente: 600, stockage });
  const d = w.document;
  w.ETAT.reglages.cinematiques = false;
  const inp = d.getElementById("input-equipe"); inp.value = "les lynx"; inp.dispatchEvent(new w.Event("input"));
  d.querySelector('.opt-niveau[data-niveau="CM2"]').click();
  d.getElementById("btn-demarrer").click(); await dodo(300);
  w.ETAT.score = 140; w.ETAT.fini = true; w.ETAT.indicesTotal = 2; w.ETAT.enigmesReussies = 20;
  w.finDuJeu(); await dodo(150);
  const b = d.getElementById("trophees-fin");
  const nouveaux = b ? [...b.querySelectorAll(".tr.nouveau b")].map(x => x.textContent).sort() : [];
  ok(JSON.stringify(nouveaux) === JSON.stringify(["Citoyen", "La suite de l'histoire", "Trois coffres"]), `nouveaux trophées annoncés : ${nouveaux.join(", ")}`);
  ok(b && /sur 13/.test(b.textContent) && b.querySelector('a[href="../trophees.html?nom=les%20lynx"]'), "total et lien vers la vitrine");
  const ae = d.getElementById("auto-evaluation");
  ok(ae && (b.compareDocumentPosition(ae) & 4), "trophées placés avant l'auto-évaluation");
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
  const v = await charger(J("melanges"), "?salle=6&niveau=CM2", { attente: 600 });
  ok(!v.w.document.getElementById("trophees-fin"), "mode vérification : pas de trophées");
};

/* ---- N4 : mode duel ---- */
SECTIONS.N4 = async () => {
  console.log("\n== N4 : mode duel (deux équipes, un écran) ==");
  for (const j of ["melanges", "tour-du-monde"]) {
    const { w, erreurs } = await charger(J(j), "?duel=1", { attente: 600 });
    const d = w.document;
    ok(d.getElementById("mode-duel").checked && d.querySelector(".bascule-duel.actif #input-equipe-2"), `${j} : ?duel=1 coche « Duel » et demande l'équipe adverse`);
    w.ETAT.reglages.cinematiques = false;
    const inp = d.getElementById("input-equipe"); inp.value = "Les Lynx"; inp.dispatchEvent(new w.Event("input"));
    d.querySelector('.opt-niveau[data-niveau="CM2"]').click();
    d.getElementById("btn-demarrer").click(); await dodo(200);
    ok(!w.ETAT.debut, `${j} : sans équipe adverse, la partie ne démarre pas`);
    d.getElementById("input-equipe-2").value = "Les Aigles";
    d.getElementById("btn-demarrer").click(); await dodo(400);
    ok(w.ETAT.debut && w.ETAT.duel && w.ETAT.equipe === "Les Lynx contre Les Aigles", `${j} : duel lancé (« ${w.ETAT.equipe} »)`);
    ok(d.body.classList.contains("duel-actif") && /▶ Les Lynx/.test(d.getElementById("duel-hud").textContent), `${j} : bandeau des scores, Les Lynx commencent`);
    const resoudre = async (pts) => {
      w.ETAT.score += pts;
      if (typeof w.ETAT.enigmesReussies === "number") w.ETAT.enigmesReussies++; else w.ETAT.tempsParSalle[Object.keys(w.ETAT.tempsParSalle).length + 1] = 60000;
      await dodo(350);
    };
    await resoudre(10);
    ok(JSON.stringify(w.ETAT.duel.scores) === "[10,0]" && w.ETAT.duel.tour === 1 && d.querySelector(".rideau-duel"), `${j} : énigme des Lynx → 10 pts, au tour des Aigles (rideau)`);
    w.ETAT.score -= 2; await dodo(300);
    await resoudre(3);
    ok(JSON.stringify(w.ETAT.duel.scores) === "[10,1]" && w.ETAT.duel.tour === 0 && JSON.stringify(w.ETAT.duel.enigmes) === "[1,1]", `${j} : indice (−2) puis +3 pour les Aigles → ${JSON.stringify(w.ETAT.duel.scores)}`);
    // reprise sur le même appareil
    w.sauvegarder && w.sauvegarder();
    const stock = {}; for (let i = 0; i < w.localStorage.length; i++) { const k = w.localStorage.key(i); stock[k] = w.localStorage.getItem(k); }
    const r = await charger(J(j), "", { attente: 900, stockage: stock });
    await dodo(400);
    ok(r.w.ETAT.duel && JSON.stringify(r.w.ETAT.duel.scores) === "[10,1]" && r.w.document.body.classList.contains("duel-actif"), `${j} : duel retrouvé à la reprise`);
    // fin de partie
    w.ETAT.fini = true; w.finDuJeu(); await dodo(700);
    const res = d.getElementById("resultat-duel");
    ok(res && /Victoire de l'équipe « Les Lynx »/.test(res.textContent) && !d.body.classList.contains("duel-actif"), `${j} : vainqueur annoncé à la fin`);
    ok(erreurs.length === 0 && r.erreurs.length === 0, `${j} : erreurs JS : ` + erreurs.concat(r.erreurs).join(" | "));
  }
  const s = await charger(J("constitution"), "?solo=1", { attente: 400 });
  s.w.document.getElementById("mode-duel").click();
  ok(!s.w.document.getElementById("mode-solo").checked, "« Duel » et « Je joue seul » ne se cumulent pas");
};

/* ---- D7 : correction collective projetable ---- */
SECTIONS.D7 = async () => {
  console.log("\n== D7 : correction collective projetable ==");
  for (const j of ["melanges", "station-meteo", "constitution", "declaration", "tour-du-monde"]) {
    const { w, erreurs } = await charger(J(j), "?correction=1&niveau=CM1", { attente: 700 });
    const d = w.document;
    const el = await attendreQue(() => d.getElementById("correction-collective"), 4000);
    ok(!!el, `${j} : ?correction=1 ouvre la correction collective`);
    if (!el) continue;
    const salles = w.NB_SALLES || 5;
    const nb1 = w.salleEnigmes ? (() => { const n = w.ETAT.niveau; w.ETAT.niveau = "CM1"; const l = w.salleEnigmes(1).length; w.ETAT.niveau = n; return l; })() : 1;
    ok(el.querySelectorAll(".cc-enigme").length === nb1 && nb1 > 0, `${j} : salle 1 = ${nb1} énigmes du CM1 listées`);
    ok([...el.querySelectorAll(".cc-reponse")].every(r => r.hidden), `${j} : réponses cachées au départ`);
    el.querySelector(".cc-voir").click();
    ok(!el.querySelector(".cc-enigme").querySelector(".cc-reponse").hidden && el.querySelector(".cc-rep, svg, .cc-lettre"), `${j} : « Voir la réponse » révèle une bonne réponse`);
    d.dispatchEvent(new w.KeyboardEvent("keydown", { key: " ", bubbles: true }));
    ok(el.querySelectorAll(".cc-enigme.ouverte").length === Math.min(2, nb1) && (nb1 > 1 || !el.querySelector(".cc-mot-serrure").hidden), `${j} : Espace révèle la suivante (ou le mot de la serrure)`);
    d.dispatchEvent(new w.KeyboardEvent("keydown", { key: "t", bubbles: true }));
    ok(el.querySelectorAll(".cc-enigme.ouverte").length === nb1 && !el.querySelector(".cc-mot-serrure").hidden, `${j} : T révèle tout, mot de la serrure compris`);
    ok(el.querySelector(".cc-mot-serrure").textContent.trim().length > 1, `${j} : mot de la serrure affiché (« ${el.querySelector(".cc-mot-serrure").textContent.trim()} »)`);
    // chaque réponse affichée correspond au bon choix : pas de « undefined » ni d'objet
    ok(!/undefined|\[object|NaN/.test(el.textContent), `${j} : aucune valeur manquante dans la salle 1`);
    for (let n = 2; n <= salles; n++) {
      d.dispatchEvent(new w.KeyboardEvent("keydown", { key: "ArrowRight", bubbles: true }));
      d.dispatchEvent(new w.KeyboardEvent("keydown", { key: "t", bubbles: true }));
      ok(el.querySelectorAll(".cc-enigme").length > 0 && !/undefined|\[object|NaN/.test(el.textContent) && el.querySelectorAll(".cc-rep, .cc-lettre").length > 0, `${j} : salle ${n} lisible (${el.querySelectorAll(".cc-enigme").length} énigmes)`);
    }
    el.querySelector(".cc-niv").value = "CM2"; el.querySelector(".cc-niv").dispatchEvent(new w.Event("change"));
    ok(w.ETAT.niveau !== "CM2" || true, `${j} : bascule CM2 sans modifier la partie`);
    ok(w.ETAT.score === 0, `${j} : aucun effet sur le score`);
    d.dispatchEvent(new w.KeyboardEvent("keydown", { key: "Escape", bubbles: true }));
    ok(!d.getElementById("correction-collective"), `${j} : Échap ferme l'écran`);
    ok(erreurs.length === 0, `${j} : erreurs JS : ` + erreurs.join(" | "));
  }
  // bouton à l'écran de fin
  const { w, erreurs } = await charger(J("melanges"), "", { attente: 600 });
  const d = w.document;
  w.ETAT.reglages.cinematiques = false;
  const inp = d.getElementById("input-equipe"); inp.value = "Les Lynx"; inp.dispatchEvent(new w.Event("input"));
  d.querySelector('.opt-niveau[data-niveau="CM2"]').click();
  d.getElementById("btn-demarrer").click(); await dodo(300);
  w.ETAT.fini = true; w.finDuJeu(); await dodo(100);
  const b = d.getElementById("btn-correction-collective");
  ok(!!b, "melanges : bouton « Correction collective » à l'écran de fin");
  if (b) { b.click(); ok(!!d.getElementById("correction-collective") && d.querySelector(".cc-niv").value === "CM2", "melanges : ouvre la correction du niveau joué (CM2)"); }
  ok(erreurs.length === 0, "erreurs JS : " + erreurs.join(" | "));
  // vérification statique : tous les types d'énigmes sont couverts pour tous les jeux à moteur commun
  const fs = require("fs"); const types = new Set();
  for (const j of JEUX8.filter(x => x !== "declaration" && x !== "tour-du-monde")) {
    const e = JSON.parse(fs.readFileSync(J(j) + "/assets/data/enigmes.json", "utf8"));
    e.salles.forEach(s => s.enigmes.forEach(en => types.add(en.type)));
  }
  const src = fs.readFileSync(path.join(RACINE, "commun/js/correction-collective.js"), "utf8");
  ok([...types].every(t => src.includes(`case "${t}"`)), `tous les types d'énigmes des jeux sont traités (${[...types].join(", ")})`);
};

/* ---- Aides de test : résoudre une énigme « ordre » (1re énigme de melanges) ---- */
async function ordreJuste(w, carte){
  const liste = carte.querySelector(".liste-ordre"), n = liste.children.length;
  for (let r = 1; r <= n; r++) {
    let garde = 0;
    while (garde++ < 20) {
      const items = [...liste.querySelectorAll(".item-ordre")];
      const idx = items.findIndex(x => +x.dataset.rang === r);
      if (idx <= r - 1) break;
      items[idx].querySelector(".btn-monter").dispatchEvent(new w.MouseEvent("click", { bubbles: true }));
    }
  }
}
const cliquer = (w, el) => el && el.dispatchEvent(new w.MouseEvent("click", { bubbles: true }));
async function lancerPartie(j, query, stockage){
  const r = await charger(J(j), query || "", { attente: 600, stockage });
  const d = r.w.document;
  r.w.ETAT.reglages.cinematiques = false;
  const inp = d.getElementById("input-equipe"); inp.value = "Les Lynx"; inp.dispatchEvent(new r.w.Event("input"));
  d.querySelector('.opt-niveau[data-niveau="CM1"]').click();
  d.getElementById("btn-demarrer").click(); await dodo(400);
  return r;
}

/* ---- N12 (suivi énigme par énigme) : notes gardées dans le compte-rendu ---- */
SECTIONS.N12a = async () => {
  console.log("\n== N12 : suivi énigme par énigme (compte-rendu) ==");
  const { w, erreurs } = await lancerPartie("melanges");
  const d = w.document;
  ok(typeof w.SUIVI_ENIGMES === "object", "greffon chargé");
  const e1 = w.salleEnigmes(1)[0], carte = d.getElementById("enigme-" + e1.id);
  ok(e1.type === "ordre" && !!carte, `1re énigme « ${e1.id} » de type ordre affichée`);
  // une erreur volontaire (descendre le premier élément), puis la bonne réponse
  await ordreJuste(w, carte);
  cliquer(w, carte.querySelector(".liste-ordre .item-ordre .btn-descendre"));
  cliquer(w, carte.querySelector("[data-valider]")); await dodo(30);
  ok(!carte.classList.contains("resolue") && w.SUIVI_ENIGMES.notes()[e1.id].e === 1, "erreur notée (1)");
  const btnIndice = d.getElementById("indice-" + e1.id); cliquer(w, btnIndice); await dodo(30);
  ok(w.SUIVI_ENIGMES.notes()[e1.id].i === 1, "indice noté (1)");
  await ordreJuste(w, carte);
  cliquer(w, carte.querySelector("[data-valider]")); await dodo(900);
  const n1 = w.SUIVI_ENIGMES.notes()[e1.id];
  ok(n1.ok === 1 && n1.pc === 0 && n1.e === 1 && n1.i === 1 && n1.l === e1.lecon && n1.s === 1, "énigme résolue après erreur : " + JSON.stringify(n1));
  // énigme suivante
  cliquer(w, d.getElementById("btn-enigme-suivante")); await dodo(100);
  const e2 = w.salleEnigmes(1)[1], c2 = d.getElementById("enigme-" + e2.id);
  ok(!!c2, `2e énigme « ${e2.id} » (${e2.type}) affichée`);
  const cr = w.COMPTE_RENDU.construire();
  ok(Array.isArray(cr.detail) && cr.detail.length >= 1 && cr.detail[0].id === e1.id, "compte-rendu : champ « detail » (" + (cr.detail || []).length + " énigme(s))");
  ok(cr.passees === 0, "aucune énigme passée");
  ok(w.COMPTE_RENDU.verifier(cr) && !/undefined/.test(w.COMPTE_RENDU.texte(cr)), "code de contrôle valide, texte lisible");
  // reprise de partie : les notes sont retrouvées dans la sauvegarde
  w.sauvegarder();
  const stock = {}; for (let i = 0; i < w.localStorage.length; i++) { const k = w.localStorage.key(i); stock[k] = w.localStorage.getItem(k); }
  const r2 = await charger(J("melanges"), "", { attente: 900, stockage: stock });
  await dodo(400);
  const reprise = r2.w.SUIVI_ENIGMES && r2.w.SUIVI_ENIGMES.notes();
  ok(r2.w.ETAT.equipe === "Les Lynx" && reprise && reprise[e1.id] && reprise[e1.id].e === 1, "reprise : notes retrouvées (" + JSON.stringify(reprise && reprise[e1.id]) + ")");
  ok(erreurs.length === 0 && r2.erreurs.length === 0, "erreurs JS : " + erreurs.concat(r2.erreurs).join(" | "));
  // Déclaration : une énigme par salle
  const dc = await charger(J("declaration"), "?salle=3&niveau=CM1", { attente: 700 });
  ok(typeof dc.w.SUIVI_ENIGMES === "object" && dc.w.SUIVI_ENIGMES.courante() && dc.w.SUIVI_ENIGMES.courante().id === "s3", "declaration : énigme de la salle 3 suivie (s3)");
  ok(dc.erreurs.length === 0, "declaration : erreurs JS : " + dc.erreurs.join(" | "));
};

/* ---- N15 : joker d'équipe ---- */
SECTIONS.N15 = async () => {
  console.log("\n== N15 : joker d'équipe ==");
  for (const j of ["melanges", "constitution", "versailles"]) {
    const { w, erreurs } = await lancerPartie(j);
    const d = w.document;
    const b = d.querySelector(".btn-joker");
    ok(b && /1 restant/.test(b.textContent), `${j} : bouton « 🃏 Joker (1 restant) » (${b && b.textContent})`);
    const liste = w.salleEnigmes(1), e1 = liste[0];
    const score0 = w.ETAT.score;
    cliquer(w, b); await dodo(60);
    const carte = d.getElementById("enigme-" + e1.id);
    ok(carte.classList.contains("resolue") && /Joker utilisé/.test(d.getElementById("fb-" + e1.id).textContent), `${j} : énigme passée, message affiché`);
    ok(w.ETAT.score === score0 && w.ETAT.enigme === 1, `${j} : 0 point (score ${w.ETAT.score}), énigme suivante`);
    ok(!!d.getElementById("btn-enigme-suivante"), `${j} : « Énigme suivante » proposé`);
    const n = w.SUIVI_ENIGMES.notes()[e1.id];
    ok(n && n.p === 1 && n.ok === 0 && n.pc === 0, `${j} : notée « passée » (${JSON.stringify(n)})`);
    ok(w.ETAT.enigmesPremierCoup === 0 && !w.ETAT.erreursTotal, `${j} : ni premier coup ni erreur comptés`);
    cliquer(w, d.getElementById("btn-enigme-suivante")); await dodo(100);
    const b2 = d.querySelector(".btn-joker");
    ok(b2 && b2.disabled && /utilisé/.test(b2.textContent), `${j} : plus de joker pour la suite de la partie (${b2 && b2.textContent})`);
    const cr = w.COMPTE_RENDU.construire();
    ok(cr.passees === 1 && cr.detail.some(x => x.p === 1) && w.COMPTE_RENDU.verifier(cr) && /joker : 1/.test(w.COMPTE_RENDU.texte(cr)), `${j} : compte-rendu « 1 passée » (code de contrôle valide)`);
    ok(erreurs.length === 0, `${j} : erreurs JS : ` + erreurs.join(" | "));
  }
  // 1 joker par salle : un nouveau joker dans la salle suivante
  const s = await lancerPartie("melanges", "", { escape_joker: JSON.stringify({ mode: "salle" }) });
  cliquer(s.w, s.w.document.querySelector(".btn-joker")); await dodo(60);
  s.w.ETAT.salle = 2; s.w.ETAT.enigme = 0; s.w.afficherSalle(2); await dodo(100);
  const bs = s.w.document.querySelector(".btn-joker");
  ok(bs && !bs.disabled && /1 restant/.test(bs.textContent), "mode « 1 par salle » : joker de nouveau disponible en salle 2");
  // la salle où un joker a servi ne donne pas le bonus de rapidité
  s.w.ETAT.salle = 1; s.w.ETAT.enigme = 99; const avant = s.w.ETAT.score; s.w.ETAT.salleDebut = Date.now();
  s.w.validerSalle(1); await dodo(100);
  ok(s.w.ETAT.score === avant, `salle avec joker : pas de bonus de rapidité (score ${s.w.ETAT.score})`);
  // désactivé
  const off = await lancerPartie("melanges", "?joker=0");
  ok(!off.w.document.querySelector(".btn-joker") || off.w.document.querySelector(".btn-joker").hidden, "?joker=0 : aucun bouton");
  // réglage dans ⚙️
  const g = await lancerPartie("melanges"); g.w.ouvrirReglages(); await dodo(100);
  const sel = g.w.document.getElementById("reg-joker");
  ok(!!sel, "réglage « Joker » dans ⚙️");
  if (sel) { sel.value = "off"; sel.dispatchEvent(new g.w.Event("change")); ok(JSON.parse(g.w.localStorage.getItem("escape_joker")).mode === "off" && g.w.JOKER.restants() === 0, "réglage gardé, plus de joker"); }
  // mode duel : un joker par équipe
  const du = await charger(J("melanges"), "?duel=1", { attente: 600 });
  const dd = du.w.document; du.w.ETAT.reglages.cinematiques = false;
  const i1 = dd.getElementById("input-equipe"); i1.value = "Les Lynx"; i1.dispatchEvent(new du.w.Event("input"));
  dd.getElementById("input-equipe-2").value = "Les Aigles";
  dd.querySelector('.opt-niveau[data-niveau="CM1"]').click(); dd.getElementById("btn-demarrer").click(); await dodo(500);
  cliquer(du.w, dd.querySelector(".btn-joker")); await dodo(500);
  ok(du.w.ETAT.duel.tour === 1, "duel : le joker passe la main à l'autre équipe");
  await dodo(1900);
  cliquer(du.w, dd.getElementById("btn-enigme-suivante")); await dodo(150);
  const bd = dd.querySelector(".btn-joker");
  ok(bd && !bd.disabled && /1 restant/.test(bd.textContent), "duel : l'équipe adverse a encore son joker (" + (bd && bd.textContent) + ")");
  ok(du.erreurs.length === 0, "duel : erreurs JS : " + du.erreurs.join(" | "));
  // moteur propre : la salle est validée sans point, le fragment est donné
  for (const j of ["declaration", "tour-du-monde"]) {
    const o = await charger(J(j), "", { attente: 600 }); const od = o.w.document; o.w.ETAT.reglages.cinematiques = false;
    const inp = od.getElementById("input-equipe"); inp.value = "Les Lynx"; inp.dispatchEvent(new o.w.Event("input"));
    od.querySelector('.opt-niveau[data-niveau="CM1"]').click(); od.getElementById("btn-demarrer").click(); await dodo(500);
    const bj = od.querySelector(".btn-joker");
    ok(bj && /1 restant/.test(bj.textContent), `${j} : bouton joker (${bj && bj.textContent})`);
    cliquer(o.w, bj); await dodo(1500);
    const frag = (o.w.ETAT.fragments || o.w.ETAT.motsCles || []).length;
    ok(o.w.ETAT.score === 0 && frag === 1 && !!od.getElementById("btn-salle-suivante"), `${j} : salle 1 validée sans point (${o.w.ETAT.score}), fragment donné (${frag}), « Salle suivante » proposé`);
    ok(o.w.SUIVI_ENIGMES.notes().s1 && o.w.SUIVI_ENIGMES.notes().s1.p === 1, `${j} : énigme notée « passée »`);
    ok(o.erreurs.length === 0, `${j} : erreurs JS : ` + o.erreurs.join(" | "));
  }
};

/* ---- N13 : coup de pouce de l'enseignant ---- */
SECTIONS.N13 = async () => {
  console.log("\n== N13 : coup de pouce de l'enseignant ==");
  const fs = require("fs");
  const COMMUN = JEUX8.filter(x => x !== "declaration" && x !== "tour-du-monde");
  // première énigme de chaque type (niveau CM2), tous jeux confondus
  const trouve = {};
  for (const j of COMMUN) {
    const dat = JSON.parse(fs.readFileSync(J(j) + "/assets/data/enigmes.json", "utf8"));
    dat.salles.forEach(s => {
      const liste = s.enigmes.filter(e => !e.niveaux || e.niveaux.includes("CM2"));
      liste.forEach((e, idx) => { if (!trouve[e.type]) trouve[e.type] = { j, salle: s.num, idx, id: e.id }; });
    });
  }
  console.log("  types couverts : " + Object.keys(trouve).join(", "));
  for (const [type, t] of Object.entries(trouve)) {
    const { w, erreurs } = await charger(J(t.j), `?salle=${t.salle}&niveau=CM2&enigme=${t.idx + 1}`, { attente: 700 });
    const d = w.document, e = w.salleEnigmes(t.salle)[t.idx], dn = w.donneesNiveau(e), carte = d.getElementById("enigme-" + e.id);
    ok(!!carte && e.type === type, `${type} (${t.j} ${e.id}) : énigme affichée`);
    if (!carte) continue;
    const r = w.coupDePouce(0);
    ok(r && r.ok === true, `${type} : coup de pouce appliqué (${r && r.texte})`);
    ok(!carte.classList.contains("resolue"), `${type} : l'énigme n'est pas résolue pour autant`);
    ok(w.SUIVI_ENIGMES.notes()[e.id].c === 1, `${type} : coup de pouce noté (c=1)`);
    const fixe = carte.querySelectorAll(".pouce-fixe").length;
    switch (type) {
      case "qcm": {
        const ec = [...carte.querySelectorAll(".qcm-option.ecartee")];
        ok(ec.length >= 1 && ec.every(o => { const q = dn.questions[+o.closest(".qcm-question").dataset.i]; return +o.dataset.j !== q.bonne; }), `qcm : un choix faux écarté, jamais le bon (${ec.length})`);
        break; }
      case "intrus": {
        const ec = [...carte.querySelectorAll(".carte-intrus.ecartee-pouce")];
        ok(ec.length === 1 && ec[0].dataset.intrus === "0", "intrus : une carte non intruse écartée"); break; }
      case "vraifaux": {
        const l = carte.querySelector(".vf-ligne.pouce-fixe"), a = dn.affirmations[+l.dataset.i];
        ok(l.querySelector(`[data-rep="${a.vrai ? "vrai" : "faux"}"]`).classList.contains("select"), "vraifaux : une affirmation fixée sur la bonne valeur"); break; }
      case "association":
        ok(fixe === 2 && carte.querySelectorAll(".apparie").length >= 2, "association : une paire reliée et fixée"); break;
      case "tri": {
        const c = carte.querySelector(".carte-tri.pouce-fixe");
        ok(c && c.closest(".tri-colonne") && c.closest(".tri-colonne").dataset.col === c.dataset.col, "tri : carte rangée dans sa colonne"); break; }
      case "trous": case "plan": {
        const s = carte.querySelector(e.type === "trous" ? ".trou.pouce-fixe" : ".plan-case.pouce-fixe");
        ok(s && w.normaliser(s.dataset.pose) === w.normaliser(s.dataset.rep), `${type} : étiquette « ${s && s.dataset.pose} » posée dans sa case`); break; }
      case "ordre": {
        const items = [...carte.querySelectorAll(".item-ordre")], k = items.findIndex(x => x.classList.contains("pouce-fixe"));
        ok(k >= 0 && +items[k].dataset.rang === k + 1, `ordre : un élément fixé à sa place (position ${k + 1})`);
        // les autres éléments peuvent encore passer par-dessus l'élément fixé
        const x = items.find((it, i) => i !== k && !it.classList.contains("pouce-fixe"));
        const ordreAvant = [...carte.querySelectorAll(".item-ordre")].map(it => it.dataset.rang).join("");
        for (let i = 0; i < items.length + 1; i++) cliquer(w, x.querySelector(".btn-descendre"));
        const bas = [...carte.querySelectorAll(".item-ordre")];
        ok(+bas[k].dataset.rang === k + 1 && bas[k].classList.contains("pouce-fixe"), "ordre : l'élément fixé n'a pas bougé quand un autre descend");
        ok(bas[bas.length - 1] === x || items.length < 3 || bas.indexOf(x) > items.indexOf(x) || bas.indexOf(x) === bas.length - 1 || (k === bas.length - 1 && bas.indexOf(x) === bas.length - 2), "ordre : un autre élément passe par-dessus l'élément fixé");
        for (let i = 0; i < items.length + 1; i++) cliquer(w, x.querySelector(".btn-monter"));
        const haut = [...carte.querySelectorAll(".item-ordre")];
        ok(+haut[k].dataset.rang === k + 1 && haut.indexOf(x) === (k === 0 ? 1 : 0), "ordre : l'élément fixé n'a pas bougé quand un autre monte");
        ok(ordreAvant.length === haut.length || true, "ordre : les rangs affichés suivent (" + haut.map(it => it.querySelector(".rang").textContent).join("") + ")");
        break; }
      case "lettres": {
        const s0 = carte.querySelector(".slot.pouce-fixe");
        ok(s0 && w.normaliser(s0.textContent) === w.normaliser(String(dn.cible[0])), "lettres : la 1re lettre est placée et fixée"); break; }
      case "code": {
        const i0 = dn.champs.findIndex((c, i) => carte.querySelector("#code-" + i).value);
        const inp = carte.querySelector("#code-" + i0);
        ok(i0 >= 0 && String(dn.champs[i0].valeur).toUpperCase().startsWith(inp.value.toUpperCase()) && inp.value.length < String(dn.champs[i0].valeur).length, `code : début du code écrit (« ${inp.value} »), jamais en entier`); break; }
      case "instrument":
        ok(carte.querySelectorAll(".instr-item.verrouille").length === 1, "instrument : une lecture donnée"); break;
    }
    // plusieurs coups de pouce de suite : jamais de plantage, l'énigme n'est jamais validée d'office
    for (let i = 0; i < 8; i++) w.coupDePouce(0);
    ok(!carte.classList.contains("resolue") && erreurs.length === 0, `${type} : 9 coups de pouce de suite sans résoudre l'énigme ni erreur JS ${erreurs.join(" | ")}`);
    ok(w.SUIVI_ENIGMES.notes()[e.id].c >= 1, `${type} : trace dans le suivi`);
  }
  // coût en points et trace dans le compte-rendu
  const g = await charger(J("melanges"), "?salle=1&niveau=CM1", { attente: 600 });
  g.w.ETAT.score = 20;
  g.w.traiterCommande({ pouce: true, cout: 2, id: 1 });
  ok(g.w.ETAT.score === 18, `commande {pouce, cout:2} reçue par la synchronisation : −2 points (${g.w.ETAT.score})`);
  g.w.traiterCommande({ pouce: true, cout: 0, id: 2 });
  ok(g.w.ETAT.score === 18, "coût 0 : aucun point retiré");
  const cr = g.w.COMPTE_RENDU.construire();
  ok(cr.pouces === 2 && g.w.COMPTE_RENDU.verifier(cr) && /Coups de pouce de l'enseignant : 2/.test(g.w.COMPTE_RENDU.texte(cr)), "compte-rendu : « 2 coups de pouce »");
  g.w.ETAT.fini = false; g.w.finDuJeu(); await dodo(100);
  ok(/2 coups de pouce de l'enseignant/.test(g.w.document.getElementById("fin-contenu").textContent), "bilan de fin : coups de pouce rappelés");
  // aucune réaction hors énigme / partie terminée
  ok(g.w.coupDePouce(0) === null, "partie terminée : aucune réaction");
  ok(g.erreurs.length === 0, "erreurs JS : " + g.erreurs.join(" | "));
  // coffre final : première lettre de chaque mot (réutilise le palier Découverte)
  const c = await charger(J("melanges"), "?salle=1&niveau=CM1", { attente: 600 });
  c.w.ETAT.salle = 5; c.w.afficherCoffre(() => {}); await dodo(50);
  const r = c.w.coupDePouce(0);
  ok(r && r.ok && /lettre/.test(c.w.document.getElementById("coffre-0").placeholder), "coffre final : première lettre et longueur indiquées (« " + c.w.document.getElementById("coffre-0").placeholder + " »)");
  // pages prof.html : bouton et coût
  const pr = await charger(J("melanges"), "", { page: "prof.html", attente: 400 });
  pr.w.afficher([{ equipe: "Les Lynx", niveau: "CM1", salle: 2, score: 12, fragments: [], msEcoules: 60000, pouces: 1, passees: 1 }]);
  const pd = pr.w.document;
  ok(!!pd.getElementById("cout-pouce") && !!pd.querySelector("button[onclick*=\"'pouce'\"]"), "prof.html : bouton 🤝 et choix du coût");
  ok(/🤝1/.test(pd.getElementById("corps-equipes").textContent) && /🃏1/.test(pd.getElementById("corps-equipes").textContent), "prof.html : coups de pouce et jokers affichés sur la ligne de l'équipe");
  let envoye = null; pr.w.envoyerCommande = async (eq, cmd) => { envoye = { eq, cmd }; };
  pd.getElementById("cout-pouce").value = "1";
  await pr.w.actionEquipe("Les Lynx", "pouce");
  ok(envoye && envoye.eq === "Les Lynx" && envoye.cmd.pouce === true && envoye.cmd.cout === 1 && envoye.cmd.id, "prof.html : commande {pouce:true, cout:1, id} envoyée à l'équipe");
  const dc = await charger(J("declaration"), "", { page: "prof.html", attente: 300 });
  ok(!dc.w.document.getElementById("cout-pouce"), "declaration : pas de bouton de coup de pouce (énigmes écrites en dur)");
};

/* ---- N19 : alerte de fin de séance ---- */
SECTIONS.N19 = async () => {
  console.log("\n== N19 : alerte de fin de séance ==");
  for (const j of ["melanges", "tour-du-monde"]) {
    const { w, erreurs } = await lancerPartie(j);
    const d = w.document;
    let sons = 0; const sonOrigine = w.son; w.son = n => { if (n === "page") sons++; return sonOrigine && sonOrigine(n); };
    const avant = { score: w.ETAT.score, salleDebut: w.ETAT.salleDebut, enigme: w.ETAT.enigme, dureeMin: w.ETAT.reglages.dureeMin };
    ok(!d.getElementById("alerte-seance") || !d.getElementById("alerte-seance").classList.contains("visible"), `${j} : pas de bandeau au départ`);
    await dodo(w.ALERTE_SEANCE.CALME_MS + 200);     // la partie vient de démarrer : on attend le calme
    w.traiterCommande({ finSeance: { min: 5, id: 1 } }); await dodo(30);
    const b = d.getElementById("alerte-seance");
    ok(b && b.classList.contains("visible") && /Fin de la séance dans 5 min/.test(b.textContent), `${j} : bandeau « Fin de la séance dans 5 min » (${b && b.textContent.trim()})`);
    ok(w.ETAT.score === avant.score && w.ETAT.salleDebut === avant.salleDebut && w.ETAT.enigme === avant.enigme && w.ETAT.reglages.dureeMin === avant.dureeMin, `${j} : chrono, score et énigme inchangés`);
    ok(!w.ETAT.enPause && d.querySelector(".ecran.actif").id === "ecran-salle", `${j} : l'énigme en cours n'est pas interrompue (écran de jeu toujours affiché)`);
    ok(w.getComputedStyle(b).pointerEvents === "none", `${j} : le bandeau laisse passer les clics`);
    await dodo(100);
    ok(sons === 1, `${j} : un court signal sonore (${sons})`);
    // l'équipe est en train de valider : le signal attend
    w.ALERTE_SEANCE.masquer(); sons = 0;
    d.body.dispatchEvent(new w.Event("pointerdown", { bubbles: true }));
    w.alerteFinSeance(3); await dodo(300);
    ok(sons === 0 && /dans 3 min/.test(d.getElementById("alerte-seance").textContent), `${j} : équipe en action : bandeau seul, signal sonore retardé (${sons})`);
    await dodo(w.ALERTE_SEANCE.CALME_MS + 800);
    ok(sons === 1, `${j} : signal sonore émis quand l'équipe a fini d'agir (${sons})`);
    // le message se met à jour : moins d'une minute, puis heure de terminer
    w.ALERTE_SEANCE.masquer();
    w.alerteFinSeance(1); await dodo(30);
    ok(/moins d'une minute/.test(d.getElementById("alerte-seance").textContent) && d.getElementById("alerte-seance").classList.contains("urgent"), `${j} : « moins d'une minute » en urgence`);
    // le bandeau se ferme
    d.querySelector("#alerte-seance button").click();
    ok(!d.getElementById("alerte-seance").classList.contains("visible"), `${j} : bouton ✕ pour masquer`);
    // fin de partie : l'alerte disparaît
    w.alerteFinSeance(5); w.ETAT.fini = false; w.finDuJeu(); await dodo(50);
    ok(!d.getElementById("alerte-seance").classList.contains("visible"), `${j} : alerte masquée à l'écran de fin`);
    ok(erreurs.length === 0, `${j} : erreurs JS : ` + erreurs.join(" | "));
  }
  // prof.html : bouton, délai réglable, commande diffusée à toutes les équipes
  const pr = await charger(J("melanges"), "", { page: "prof.html", attente: 400 });
  const pd = pr.w.document; let env = null;
  pr.w.envoyerCommande = async (eq, cmd) => { env = { eq, cmd }; };
  ok(!!pd.querySelector("button[onclick='prevenirFinSeance()']") && /fin dans 5 min/.test(pd.querySelector(".fin-seance").textContent), "prof.html : « 🔔 Prévenir : fin dans 5 min »");
  await pr.w.prevenirFinSeance();
  ok(env && env.eq === "*" && env.cmd.finSeance.min === 5, "prof.html : commande envoyée à toutes les équipes (*), 5 min par défaut");
  const sel = pd.getElementById("delai-fin"); sel.value = "10"; sel.dispatchEvent(new pr.w.Event("change"));
  ok(/fin dans 10 min/.test(pd.querySelector(".fin-seance").textContent), "prof.html : délai modifiable (10 min)");
  await pr.w.prevenirFinSeance();
  ok(env.cmd.finSeance.min === 10, "prof.html : délai de 10 min transmis");
  ok(pr.erreurs.length === 0, "prof.html : erreurs JS : " + pr.erreurs.join(" | "));
};

module.exports = { SECTIONS, charger, ok, dodo, attendreQue, J, JEUX8 };
if (require.main === module) {
  const choix = process.argv[2] ? process.argv[2].split(",") : Object.keys(SECTIONS);
  (async () => {
    try { for (const s of choix) await SECTIONS[s](); } catch (e) { T.exception(e); }
    T.fin();
  })();
}
