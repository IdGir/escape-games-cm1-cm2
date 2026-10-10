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

module.exports = { SECTIONS, charger, ok, dodo, attendreQue, J, JEUX8 };
if (require.main === module) {
  const choix = process.argv[2] ? process.argv[2].split(",") : Object.keys(SECTIONS);
  (async () => {
    try { for (const s of choix) await SECTIONS[s](); } catch (e) { T.exception(e); }
    T.fin();
  })();
}
