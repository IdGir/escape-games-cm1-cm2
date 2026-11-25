/* ============================================================
   TESTS DU TABLEAU DE BORD DE L'ENSEIGNANT (session 2, chantier 3) — Node + jsdom
   Depuis la racine du dépôt :  node commun/tests/test-tableau-de-bord.js
   Étapes au choix : node commun/tests/test-tableau-de-bord.js SANS SERVEUR
   SANS    : page ouverte depuis le site en ligne (aucun serveur local)
   SERVEUR : serveur local simulé (équipes en direct, production, installations, mise à jour)
   Le serveur réel (/api/production, /api/installations, /api/mettre-a-jour) :
   python commun/tests/test-tableau-serveur.py
   ============================================================ */
const { charger, compteur, dodo, attendreQue, RACINE } = require("../../outils-tests/charge");
const fs = require("fs"), path = require("path"), vm = require("vm");
const T = compteur("Tableau de bord de l'enseignant"); const ok = T.ok;
const SECTIONS = {};

const serveur = routes => w => {
  const f = w.fetch;
  w.__appels = []; w.__tdbPas = 20; w.__ouverts = []; w.open = u => { w.__ouverts.push(u); return {}; };
  w.fetch = async (url, o) => {
    const u = new URL(String(url), w.location.href);
    const m = u.host === "localhost" && u.pathname.match(/^\/api\/[a-z-]+/);
    if(m && routes[m[0]]){
      const methode = (o && o.method) || "GET";
      w.__appels.push({ route: m[0], methode });
      const r = routes[m[0]](methode, o && o.body ? JSON.parse(o.body) : null);
      return { ok: true, status: 200, json: async () => r, text: async () => JSON.stringify(r) };
    }
    return f(url, o);
  };
};

function production(){
  const ctx = {}; vm.createContext(ctx);
  vm.runInContext(fs.readFileSync(path.join(RACINE, "commun/donnees/production.js"), "utf8"), ctx);
  return ctx.PRODUCTION;
}

SECTIONS.SANS = async () => {
  console.log("\n== Sans serveur (site en ligne) ==");
  const P = production();
  ok(P && P.jeux.length >= 20 && P.totaux && Array.isArray(P.a_relire), `production.js : ${P && P.jeux.length} jeux, totaux et file « À relire »`);
  ok(P.jeux.every(j => j.id && j.titre && ["fini", "en-cours"].includes(j.etat) && Array.isArray(j.manque)), "chaque jeu : identifiant, titre, état fini / en cours, reste à faire");
  ok(["traite-colonies", "grande-guerre", "seconde-guerre"].every(id => (P.jeux.find(j => j.id === id) || {}).sensible), "jeux sensibles n°12, 19, 20 marqués « À relire »");
  const r = await charger(RACINE, "", { page: "enseignant.html", attente: 900 });
  const d = r.w.document;
  await attendreQue(() => r.w.__tdbPret, 3000);
  ok(/Mon tableau de bord/.test(d.querySelector("h1").textContent) && /Tableau de bord/.test(d.title), "titre : tableau de bord de l'enseignant");
  const onglets = [...d.querySelectorAll(".onglets a")].map(a => a.getAttribute("href"));
  ok(onglets.join(" ") === "#seance #direct #apres-seance a-relire.html #production #installations #aide-actions #tout-le-reste", "rubriques : " + onglets.join(" "));
  ok(onglets.filter(h => h[0] === "#").every(h => d.getElementById(h.slice(1))), "chaque rubrique existe dans la page");
  ok(d.getElementById("seance").firstElementChild === d.getElementById("feu"), "barre d'état (voyants) tout en haut de la séance");
  const ordre = ["seance", "direct", "apres-seance", "production", "installations", "aide-actions", "tout-le-reste"].map(id => d.getElementById(id));
  ok(ordre.every((x, i) => i === 0 || (ordre[i - 1].compareDocumentPosition(x) & 4)), "ordre : barre d'état, séance, en direct, après, production, installations, aide, tout le reste");
  ok(d.querySelector("#qr-eleves svg path") && /idgir\.github\.io/.test(d.getElementById("adresse-eleves").textContent), "QR code du site en ligne dessiné dans la page");
  ok(/lancer\.bat/.test(d.getElementById("direct-etat").textContent) && !d.querySelector("#equipes table"), "en direct : sans serveur, la page dit quoi faire");
  ok(d.querySelectorAll(".gros-boutons a.gros:not([hidden])").length === 5 && d.getElementById("lien-export").hidden, "après la séance : bilan, passeport, résultats, classement, trophées (export seulement avec le serveur)");
  await attendreQue(() => /resultats\.html\?fin=/.test(d.getElementById("lien-bilan").getAttribute("href")), 2500);
  ok(/resultats\.html\?fin=[a-z-]+/.test(d.getElementById("lien-bilan").getAttribute("href")), "bilan : celui du jeu de la séance (" + d.getElementById("lien-bilan").getAttribute("href") + ")");
  ok(/Photographie du/.test(d.getElementById("production-source").textContent), "production : photographie de production.js (sans serveur)");
  ok(d.querySelectorAll("#production-compteurs .compteur").length === 7, "production : 7 compteurs");
  ok(d.querySelectorAll("#production-table tbody tr").length === P.jeux.length, "production : une ligne par jeu (" + d.querySelectorAll("#production-table tbody tr").length + ")");
  d.querySelector("#production-filtres [data-filtre=sensible]").click(); await dodo(30);
  const sens = d.querySelectorAll("#production-table tbody tr");
  ok(sens.length === P.totaux.sensibles && [...sens].every(tr => tr.querySelector(".badge.sensible")), `filtre « Sensibles » : ${sens.length} jeu(x), tous marqués`);
  d.querySelector("#production-filtres [data-filtre=tous]").click(); await dodo(30);
  ok(d.querySelectorAll("#a-relire li").length >= 4 && d.querySelector("#a-relire li").classList.contains("prio"), "file « À relire » : jeux sensibles en tête");
  const lignes = d.querySelectorAll("#installations-table tbody tr");
  ok(lignes.length === 5 && /PC principal/.test(lignes[0].textContent) && /PC de l'école/.test(lignes[1].textContent) && /Nextcloud/.test(lignes[2].textContent) && /GitHub Pages/.test(lignes[3].textContent) && /Chromebooks/.test(lignes[4].textContent),
     "mes installations : PC principal, PC de l'école, Nextcloud, site en ligne, Chromebooks");
  ok(d.getElementById("btn-maj").disabled && /lancer\.bat/.test(d.getElementById("installations-ici").textContent), "sans serveur : bouton de mise à jour inactif, la page dit pourquoi");
  const aides = d.querySelectorAll("#aide-actions details");
  ok(aides.length === 9 && [...aides].every(x => x.querySelectorAll("ol li").length >= 2), `aide : ${aides.length} pas-à-pas numérotés`);
  ok([...aides].filter(x => /Outil :/.test(x.textContent)).length >= 7, "chaque pas-à-pas dit quel outil ouvrir");
  d.getElementById("btn-projection").click(); await dodo(20);
  ok(d.body.classList.contains("projection") && d.getElementById("btn-projection").getAttribute("aria-pressed") === "true", "mode projection : activé en un clic");
  ok(r.w.localStorage.getItem("eg_tdb_projection") === "1", "mode projection : retenu sur ce navigateur");
  d.getElementById("btn-projection").click(); await dodo(20);
  ok(!d.body.classList.contains("projection"), "mode projection : désactivé");
  ok(d.querySelector("#tout-le-reste .carte") && d.querySelectorAll("#tout-le-reste .carte").length === 24, "les 24 ressources restent dans « Tout le reste »");
  ok(r.erreurs.length === 0, "erreurs JS : " + r.erreurs.join(" | "));
};

SECTIONS.SERVEUR = async () => {
  console.log("\n== Avec le serveur local (simulé) ==");
  let majFaite = 0;
  const routes = {
    "/api/info": () => ({ ip: "192.168.1.23", port: 8000, local: true }),
    "/api/seance": () => ({ ok: true, local: true, seance: { jeu: "lumiere", grade: "", depuis: "2026-11-24T09:05:00", adresse: "immersifs/lumiere/" } }),
    "/api/sante": () => ({ ok: true, etat: "orange", voyants: [
      { id: "serveur", nom: "Serveur", etat: "vert", message: "Le serveur répond.", action: "" },
      { id: "version", nom: "Version", etat: "orange", message: "Une version plus récente existe.", action: "Fermez la session." },
      { id: "medias", nom: "Médias du jeu du jour", etat: "orange", message: "3 médias manquent.", action: "Rien d'obligatoire." },
      { id: "resultats", nom: "Dossier des résultats", etat: "vert", message: "OK", action: "" },
      { id: "sauvegarde", nom: "Sauvegarde", etat: "orange", message: "Dernière sauvegarde il y a 12 jours.", action: "Laissez le PC allumé." }] }),
    "/api/equipes": () => ({ equipes: [
      { equipe: "Les Lynx", jeu: "lumiere", niveau: "matelot", salle: 3, score: 120, enigmesReussies: 9, enigme: "3-2", msEcoules: 754000, indicesTotal: 2, pouces: 1, fini: false },
      { equipe: "Les Hiboux", jeu: "lumiere", niveau: "matelot", salle: 5, score: 190, enigmesReussies: 15, enigme: "", msEcoules: 1500000, indicesTotal: 0, fini: true }] }),
    "/api/production": () => ({ ok: true, direct: true, genere: "2026-11-24T10:00", totaux: { jeux: 2, finis: 1, en_cours: 1, sensibles: 1, images: 2, videos: 1, sans_voix: 0, a_verifier: 3, sans_credit: 0 },
      jeux: [{ id: "lumiere", titre: "Le Phare", icone: "🔦", num: 5, matiere: "Sciences", etat: "fini", sensible: "", manque: [], medias: { attendus: 15, images: 0, videos: 0 }, voix: 57, immersif: "immersifs/lumiere", lecons: "lumiere/lecons-imprimables.html", evaluations: "lumiere/evaluations-imprimables.html", affiche: "x", bande_annonce: "y", a_verifier: 0, sans_credit: 0 },
             { id: "seconde-guerre", titre: "Radio Londres", icone: "📻", num: 20, matiere: "Histoire", etat: "en-cours", sensible: "RELECTURE OBLIGATOIRE", manque: ["2 images", "1 vidéo"], medias: { attendus: 15, images: 2, videos: 1 }, voix: 0, immersif: "immersifs/seconde-guerre", lecons: "", evaluations: "", affiche: "", bande_annonce: "", a_verifier: 3, sans_credit: 0 }],
      a_relire: [{ jeu: "seconde-guerre", titre: "Radio Londres", point: "RELECTURE OBLIGATOIRE", priorite: 1 }] }),
    "/api/installations": () => ({ ok: true, ici: { role: "principal", machine: "DESKTOP-P8GEI81", numero: 260, date: "2026-11-24T21:00:00+0100", texte: "n° 260 du 24/11/2026", commit: "abcdef123456", vu: "2026-11-24T21:05" },
      fiches: [{ machine: "PC-ECOLE", role: "nextcloud", ecole: true, numero: 255, vu: "2026-11-23T08:30", via: "nextcloud" }],
      nextcloud: { dossier: "C:\\Users\\x\\Nextcloud\\copie", existe: true, version: { numero: 258, date: "2026-11-24T08:00:00+0100" }, copie_du: "2026-11-24T08:01:00" },
      en_ligne: { numero: 250, date: "2026-11-20T10:00:00+0100" } }),
    "/api/mettre-a-jour": m => { if(m === "POST"){ majFaite = 1; return { en_cours: true, lignes: ["PC principal : je mets à jour la copie Nextcloud."] }; }
      majFaite++; return majFaite < 3 ? { en_cours: true, lignes: ["PC principal : je mets à jour la copie Nextcloud.", "copié : index.html"] }
        : { en_cours: false, ok: true, lignes: ["PC principal : je mets à jour la copie Nextcloud.", "Copie Nextcloud : 3 fichier(s) copié(s)."] }; }
  };
  const r = await charger(RACINE, "", { page: "enseignant.html", attente: 900, avant: serveur(routes) });
  const d = r.w.document;
  await attendreQue(() => r.w.__tdbPret && d.querySelectorAll("#feu .voyant").length === 5, 3000);
  ok(/192\.168\.1\.23:8000/.test(d.getElementById("adresse-eleves").textContent) && d.querySelector("#qr-eleves svg"), "QR code : adresse du PC de la classe");
  await attendreQue(() => d.querySelectorAll("#equipes tbody tr").length === 2, 2000);
  const eq = d.querySelectorAll("#equipes tbody tr");
  ok(eq.length === 2 && /Les Hiboux/.test(eq[0].textContent), "en direct : 2 équipes, la plus avancée en tête");
  ok(/étape 3/.test(eq[1].textContent) && /3-2/.test(eq[1].textContent) && /12 min 34/.test(eq[1].textContent) && /2 indice\(s\) · 1 coup\(s\) de pouce/.test(eq[1].textContent), "progression, énigme en cours, temps, aides");
  ok(/fini/.test(eq[0].textContent) && /en jeu/.test(eq[1].textContent), "état de chaque équipe (fini, en jeu)");
  ok(!d.getElementById("lien-export").hidden && d.getElementById("lien-export").getAttribute("href") === "/api/export", "export des équipes (CSV) visible avec le serveur");
  const fv = d.querySelector('#feu .voyant[data-id="version"]');
  ok(fv && fv.querySelector("[data-action=maj]"), "barre d'état : la version en orange propose « Mettre à jour »");
  ok(d.querySelector('#feu .voyant[data-id="medias"] a[href="verifier.html"]') && d.querySelector('#feu .voyant[data-id="sauvegarde"] a[href="#aide-sauvegarde"]'), "barre d'état : médias et sauvegarde ont leur bouton");
  ok(!d.querySelector('#feu .voyant[data-id="serveur"] .mini'), "un voyant vert n'a pas de bouton");
  ok(/Calculé à l'instant/.test(d.getElementById("production-source").textContent) && d.querySelectorAll("#production-table tbody tr").length === 2, "production : calculée en direct par le serveur");
  ok(/2 image\(s\), 1 vidéo\(s\)/.test(d.querySelector('#production-table tr[data-jeu="seconde-guerre"]').textContent) && /✗ aucune/.test(d.querySelector('#production-table tr[data-jeu="seconde-guerre"]').textContent), "médias et voix manquants signalés");
  const L = [...d.querySelectorAll("#installations-table tbody tr")].map(tr => tr.textContent);
  ok(/vous êtes ici/.test(L[0]) && /n° 260/.test(L[0]) && /à jour/.test(L[0]), "PC principal : vous êtes ici, n° 260, à jour");
  ok(/n° 255/.test(L[1]) && /5 versions de retard/.test(L[1]), "PC de l'école (fiche remontée par Nextcloud) : 5 versions de retard");
  ok(/n° 258/.test(L[2]) && /2 versions de retard/.test(L[2]), "copie Nextcloud : 2 versions de retard");
  ok(/n° 250/.test(L[3]) && /10 versions de retard/.test(L[3]), "site en ligne : 10 versions de retard (à publier)");
  ok(/2 équipe\(s\) connectée\(s\)/.test(L[4]), "Chromebooks : équipes connectées en ce moment");
  ok(!d.getElementById("btn-maj").disabled && /PC principal/.test(d.getElementById("installations-ici").textContent), "bouton « Mettre à jour cette installation » actif sur le PC");
  d.getElementById("btn-maj").click();
  await attendreQue(() => /Terminé/.test(d.getElementById("maj-journal").textContent), 3000);
  ok(r.w.__appels.some(a => a.route === "/api/mettre-a-jour" && a.methode === "POST") && /3 fichier\(s\) copié\(s\)/.test(d.getElementById("maj-journal").textContent) && /✅ Terminé/.test(d.getElementById("maj-journal").textContent),
     "mise à jour : lancée, suivie, journal lisible jusqu'à « Terminé »");
  ok(r.w.__appels.filter(a => a.route === "/api/installations").length >= 2, "après la mise à jour : le tableau des installations est relu");
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
