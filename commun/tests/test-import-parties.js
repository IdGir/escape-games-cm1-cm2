/* ============================================================
   TESTS — IMPORT DES PARTIES DE MISSION GÉO (session 4) — Node + jsdom
   Depuis la racine du dépôt :  node commun/tests/test-import-parties.js
   Étapes au choix : CONVERTIR PAGE APPLI SECOURS
   CONVERTIR : commun/js/mission-geo-import.js (ancien format, script de secours, fusion sans perte)
   PAGE      : importer-parties.html (aperçu, fusion, remplacement, erreurs lisibles)
   APPLI     : mission-geo/ copie la partie sur le PC de la classe et la reprend depuis le PC
   SECOURS   : mission-geo/secours-export.html (ancienne version des Chromebooks)
   Le serveur (/api/parties) : python commun/tests/test-parties-serveur.py
   ============================================================ */
const { charger, compteur, dodo, attendreQue, RACINE } = require("../../outils-tests/charge");
const path = require("path");
const T = compteur("Import des parties (Mission géo)"); const ok = T.ok;
const I = require(path.join(RACINE, "commun/js/mission-geo-import.js"));
const SECTIONS = {};

/** Une sauvegarde telle que l'application l'écrit depuis septembre (clé mission_geo_annee_a_v1). */
const ancienne = () => ({
  version: 1, equipe: "Les Lynx de Léa", niveau: "CM1", palier: "decouverte", debut: "2026-09-08T09:00:00.000Z", erreurs: 4,
  sessions: {
    s01: { reussie: true, points: 18, maximum: 20, duree: 2400, date: "2026-09-15T10:00:00.000Z", resultats: [{ reussi: true, essais: 1, points: 4 }] },
    s02: { reussie: true, points: 15, maximum: 22, duree: 2600, date: "2026-09-29T10:00:00.000Z" },
    s03: { reussie: false, points: 6, date: "2026-10-13T10:00:00.000Z" }
  },
  indices: [
    { session: "s01", numero: 1, seance: "Le grand départ", type: "nombre", symbole: "etoile", valeur: 5, libelle: "Nombre de lettres de la ville de rendez-vous" },
    { session: "s02", numero: 2, seance: "Direction Dijon !", type: "nombre", symbole: "cercle", valeur: 7, libelle: "Nombre de continents" }
  ],
  final: { pays: null, colonne: null, ligne: null, code: null, resolu: false },
  reglages: { tailleTexte: 1.2, videosActives: false }, profil: { commune: "Clamecy" }, recompense: { active: false, titre: "", texte: "", media: "" }
});

SECTIONS.CONVERTIR = async () => {
  console.log("\n== Convertisseur (commun/js/mission-geo-import.js) ==");
  let c = I.convertir(JSON.stringify(ancienne()), { fichier: "mission-geo-lynx.json" });
  const p = c.partie;
  ok(c.ok && p.format === "mission-geo-partie" && p.version === 2, "ancienne sauvegarde lue, format commun v2");
  ok(p.equipe === "Les Lynx de Léa" && p.niveau === "CM1" && p.grade === "mousse", "équipe, niveau, palier Découverte → grade « mousse »");
  ok(Object.keys(p.seances).join(",") === "1,2,3" && p.seances[1].id === "s01" && p.seances[1].points === 18 && p.seances[3].reussie === false, "séances 1 à 3 : numéros, points, réussite gardés");
  ok(p.indices.length === 2 && p.indices[0].valeur === 5 && p.indices[1].symbole === "cercle", "indices du carnet gardés (nombre, symbole)");
  ok(p.debut === "2026-09-08T09:00:00.000Z" && p.derniere === "2026-10-13T10:00:00.000Z" && p.erreurs === 4, "dates de début et de dernière séance, erreurs");
  ok(p.profil.commune === "Clamecy" && p.source.format === I.CLE_ANCIENNE && p.source.fichier === "mission-geo-lynx.json", "repères de la classe et origine du fichier gardés");
  const r = I.resume(p);
  ok(r.nbReussies === 2 && r.reussies.join() === "1,2" && r.points === 39, "résumé : 2 séances réussies, 39 points");
  c = I.convertir({ cle: I.CLE_ANCIENNE, valeur: JSON.stringify(ancienne()), exporte_le: "2026-11-26T08:00:00Z" });
  ok(c.ok && c.partie.seances[2].reussie && c.partie.source.exporte_le === "2026-11-26T08:00:00.000Z", "fichier du script de secours lu (date d'export gardée)");
  c = I.convertir(I.convertir(ancienne()).partie);
  ok(c.ok && c.partie.seances[1].points === 18 && c.partie.grade === "mousse", "une partie déjà convertie se relit à l'identique");
  c = I.convertir(ancienne(), { grade: "timonier", equipe: "Équipe 3", classe: "CM1-CM2" });
  ok(c.partie.grade === "timonier" && c.partie.equipe === "Équipe 3" && c.partie.classe === "CM1-CM2", "l'enseignante peut imposer grade, nom d'équipe et classe");
  ok(!I.convertir("pas du json").ok && /illisible/.test(I.convertir("pas du json").erreurs[0]), "fichier illisible : erreur en français");
  ok(!I.convertir({ autre: 1 }).ok && /séances/.test(I.convertir({ autre: 1 }).erreurs[0]), "autre fichier JSON : erreur lisible");
  const bizarre = ancienne(); bizarre.sessions.s99 = { reussie: true }; bizarre.sessions.s04 = "abîmé"; bizarre.equipe = "";
  c = I.convertir(bizarre);
  ok(c.ok && !c.partie.seances[99] && c.alertes.some(a => /inconnue/.test(a)) && c.alertes.some(a => /Séance 4 illisible/.test(a)) && c.alertes.some(a => /Nom d'équipe absent/.test(a)), "séances inconnues ou abîmées ignorées, avec une alerte ; nom d'équipe manquant signalé");
  // fusion sans perte
  const a = I.convertir(ancienne()).partie;
  const b2 = ancienne(); b2.sessions.s01 = { reussie: true, points: 10, date: "2026-11-20T10:00:00Z" }; b2.sessions.s03 = { reussie: true, points: 14, date: "2026-11-24T10:00:00Z" };
  b2.indices.push({ session: "s03", numero: 3, type: "nombre", symbole: "nuage", valeur: 7 });
  const b = I.convertir(b2).partie;
  ok(I.nouveautes(a, b).join() === "3", "aperçu : la séance 3 est nouvelle");
  const f = I.fusionner(a, b);
  ok(f.seances[1].points === 18 && f.seances[1].reussie && f.seances[3].reussie && f.seances[3].points === 14 && f.indices.length === 3, "fusion : meilleur score gardé, séance 3 ajoutée, indices réunis");
  const g = I.fusionner(b, I.convertir(Object.assign(ancienne(), { sessions: { s01: { reussie: false, points: 0 } } })).partie);
  ok(g.seances[1].reussie && g.seances[3].reussie, "fusion : une séance réussie ne redevient jamais « non réussie »");
  const v = I.versAncien(f, { reglages: { tailleTexte: 1.4 } });
  ok(v.version === 1 && v.sessions.s03.reussie && v.sessions.s01.points === 18 && v.indices.length === 3 && v.reglages.tailleTexte === 1.4 && v.palier === "decouverte", "retour au format de l'application (reprise sur un autre poste)");
  ok(I.slug("Les Lynx de Léa !") === "les-lynx-de-lea" && I.SEANCES.length === 16 && I.SEANCES[15].id === "s16", "nom de fichier sûr ; 16 séances connues");
};

/** Serveur simulé : /api/parties (liste, lecture, écriture avec fusion comme serveur.py). */
function serveurParties(w, depart){
  const store = Object.assign({}, depart || {});
  w.__store = store; w.__posts = [];
  const f = w.fetch;
  w.fetch = async (url, o) => {
    const u = new URL(String(url), w.location.href);
    if(u.pathname !== "/api/parties") return f(url, o);
    const rep = (c, s) => ({ ok: s === undefined || s < 400, status: s || 200, json: async () => c });
    if(o && o.method === "POST"){
      const b = JSON.parse(o.body); w.__posts.push(b);
      if(!b.partie || !b.partie.equipe) return rep({ ok: false, message: "partie illisible" }, 400);
      const s = I.slug(b.partie.equipe), avant = store[s];
      store[s] = b.mode === "remplacer" || !avant ? b.partie : I.fusionner(avant, b.partie);
      return rep({ ok: true, message: "enregistrée", ajoutees: I.nouveautes(avant, b.partie), resume: I.resume(store[s]) });
    }
    if(u.searchParams.get("equipe")){ const p = store[u.searchParams.get("equipe")]; return p ? rep({ ok: true, partie: p }) : rep({ ok: false }, 404); }
    return rep({ ok: true, local: true, parties: Object.entries(store).map(([slug, p]) => Object.assign({ slug, classe: p.classe || "" }, I.resume(p))) });
  };
}

SECTIONS.PAGE = async () => {
  console.log("\n== Page « Importer des parties » ==");
  const lynx = I.convertir(ancienne()).partie;
  const r = await charger(RACINE, "", { page: "importer-parties.html", attente: 400, avant: w => serveurParties(w, { "les-lynx-de-lea": lynx }) });
  const d = r.w.document, E = r.w.__import;
  await E.pret;
  ok(/Serveur local/.test(d.getElementById("etat-serveur").textContent) && d.querySelectorAll("#pc tr").length === 1, "serveur trouvé ; 1 partie déjà gardée sur le PC");
  const plus = ancienne(); plus.sessions.s03 = { reussie: true, points: 12, date: "2026-11-24T10:00:00Z" };
  const autre = ancienne(); autre.equipe = "Les Hiboux"; autre.palier = ""; autre.niveau = "CM2";
  const sansNom = ancienne(); sansNom.equipe = "";
  const F = (t, n) => new r.w.File([typeof t === "string" ? t : JSON.stringify(t)], n, { type: "application/json" });
  await E.lire([F(plus, "lynx.json"), F({ cle: I.CLE_ANCIENNE, valeur: JSON.stringify(autre) }, "hiboux-secours.json"), F(sansNom, "sans-nom.json"), F("n'importe quoi", "photo.json"),
                F({ format: "lot-parties", parties: [I.convertir(Object.assign(ancienne(), { equipe: "Les Renards" })).partie] }, "lot.json")]);
  await dodo(50);
  const L = [...d.querySelectorAll("#apercu tr")];
  ok(L.length === 5, "aperçu : une ligne par partie (lot compris) : " + L.length);
  ok(/Déjà là : fusion/.test(L[0].textContent) && /\+1 séance/.test(L[0].textContent), "équipe déjà sur le PC : fusion, +1 séance annoncée");
  ok(/Nouvelle équipe/.test(L[1].textContent) && /CM2/.test(L[1].textContent), "fichier de secours : nouvelle équipe, grade CM2");
  ok(/Nom d'équipe à saisir/.test(L[2].textContent) && L[2].querySelector("[data-choix]").disabled, "sans nom d'équipe : à saisir, non sélectionnée");
  ok(/Erreur/.test(L[3].textContent) && /illisible/.test(L[3].textContent), "fichier illisible : erreur lisible, rien d'importé");
  ok(/lot\.json #1/.test(L[4].textContent) && /Les Renards/.test(L[4].querySelector("[data-equipe]").value), "lot converti réimportable");
  const champ = L[2].querySelector("[data-equipe]"); champ.value = "Les Loutres"; champ.dispatchEvent(new r.w.Event("change", { bubbles: true })); await dodo(30);
  ok(!d.querySelectorAll("#apercu tr")[2].querySelector("[data-choix]").disabled, "nom saisi : la partie peut être importée");
  d.getElementById("btn-importer").click();
  await attendreQue(() => !d.getElementById("rapport").hidden, 2000); await dodo(50);
  ok(r.w.__posts.length === 4 && r.w.__posts.every(p => p.mode === "fusion"), "import : 4 parties envoyées, en fusion");
  ok(r.w.__store["les-lynx-de-lea"].seances[3].reussie && r.w.__store["les-lynx-de-lea"].seances[1].points === 18, "fusion : séance 3 ajoutée, rien de perdu");
  ok(/4 partie\(s\) importée\(s\) sur 4/.test(d.getElementById("rapport").textContent) && /\+ séance\(s\) 3/.test(d.getElementById("rapport").textContent), "rapport lisible (séances ajoutées)");
  ok(d.querySelectorAll("#pc tr").length === 4, "liste du PC relue : 4 équipes");
  ok(r.erreurs.length === 0, "erreurs JS : " + r.erreurs.join(" | "));
};

SECTIONS.APPLI = async () => {
  console.log("\n== Application mission-geo : copie sur le PC et reprise ==");
  const stockage = { [I.CLE_ANCIENNE]: JSON.stringify(ancienne()) };
  const r = await charger(path.join(RACINE, "mission-geo"), "", { page: "index.html", attente: 2200, stockage, avant: w => serveurParties(w) });
  ok(r.w.__posts.length >= 1 && r.w.__posts[0].partie.equipe === "Les Lynx de Léa" && r.w.__posts[0].partie.seances[2].reussie, "à l'ouverture, une partie commencée est copiée sur le PC de la classe");
  const pc = I.convertir(ancienne()).partie;
  pc.seances[4] = { id: "s04", numero: 4, titre: "Besançon", reussie: true, points: 17, date: "2026-11-20T10:00:00.000Z" };
  pc.indices.push({ session: "s04", numero: 4, type: "fait", texte: "Le pays est en Amérique", libelle: "Continent" });
  r.w.__store["les-lynx-de-lea"] = pc;
  const S = r.w.eval("SAUVEGARDE");
  const liste = await S.partiesDuPC();
  ok(liste && liste.length === 1 && liste[0].reussies.join() === "1,2,4", "« Reprendre depuis le PC » : la liste des équipes vient du PC");
  await S.reprendreDuPC("les-lynx-de-lea");
  const e = JSON.parse(r.w.localStorage.getItem(I.CLE_ANCIENNE));
  ok(e.sessions.s04.reussie && e.sessions.s01.points === 18 && e.indices.length === 3 && e.equipe === "Les Lynx de Léa", "reprise : séance 4 ajoutée, rien de perdu sur ce poste");
  ok(e.reglages.tailleTexte === 1.2 && e.profil.commune === "Clamecy", "reprise : réglages et repères du poste gardés");
  const avant = r.w.__posts.length;
  S.majSession("s05", { reussie: true, points: 9, date: new Date().toISOString() });
  await attendreQue(() => r.w.__posts.length > avant, 4500);
  ok(r.w.__posts.length > avant && r.w.__posts[r.w.__posts.length - 1].partie.seances[5].reussie, "après une séance réussie, la copie du PC est mise à jour");
  ok(r.erreurs.length === 0, "erreurs JS : " + r.erreurs.join(" | "));
  const v = await charger(path.join(RACINE, "mission-geo"), "?seance=3", { page: "index.html", attente: 1800, stockage, avant: w => serveurParties(w) });
  ok(v.w.__posts.length === 0, "mode vérification (?seance=3) : rien n'est envoyé au PC");
};

SECTIONS.SECOURS = async () => {
  console.log("\n== Page de secours (ancienne version des Chromebooks) ==");
  const r = await charger(path.join(RACINE, "mission-geo"), "", { page: "secours-export.html", attente: 300, stockage: { [I.CLE_ANCIENNE]: JSON.stringify(ancienne()) }, avant: w => serveurParties(w) });
  await attendreQue(() => r.w.__secours && r.w.__secours.pc !== undefined, 2000);
  const d = r.w.document;
  ok(r.w.__secours.trouve && r.w.__secours.resume.nbReussies === 2 && /Les Lynx de Léa/.test(d.getElementById("etat").textContent), "mission trouvée sur ce Chromebook (équipe, séances)");
  ok(r.w.__secours.pc === true && r.w.__store["les-lynx-de-lea"], "copiée sur le PC de la classe");
  ok(!d.getElementById("btn-sauver").hidden && /localStorage\.getItem\("mission_geo_annee_a_v1"\)/.test(d.getElementById("ligne-console").textContent), "bouton de téléchargement et ligne de console de secours");
  const vide = await charger(path.join(RACINE, "mission-geo"), "", { page: "secours-export.html", attente: 200 });
  ok(!vide.w.__secours.trouve && /Aucune mission/.test(vide.w.document.getElementById("etat").textContent), "rien sur ce poste : message clair");
  ok(r.erreurs.length === 0 && vide.erreurs.length === 0, "erreurs JS : " + r.erreurs.concat(vide.erreurs).join(" | "));
};

(async () => {
  const demandees = process.argv.slice(2).map(x => x.toUpperCase());
  for(const [nom, f] of Object.entries(SECTIONS)){
    if(demandees.length && !demandees.includes(nom)) continue;
    try{ await f(); }catch(e){ T.exception(e); }
  }
  T.fin();
})();
