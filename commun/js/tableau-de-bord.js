/* ============================================================
   TABLEAU DE BORD DE L'ENSEIGNANT (enseignant.html) — session 2, chantier 3
   ------------------------------------------------------------
   Une seule page d'accueil enseignante, lisible au vidéoprojecteur :
     barre d'état   : les voyants du feu vert (portail-seance.js) reçoivent ici
                      un bouton quand ils sont orange ou rouges ;
     En direct      : QR code des élèves et suivi des équipes (/api/equipes) ;
     Après          : bilan PDF, passeport, résultats, classement, export ;
     Production     : jeux finis / en cours / sensibles, médias et voix
                      manquants, points À VÉRIFIER, médias sans crédit, file
                      « À relire » (/api/production, sinon production.js) ;
     Installations  : PC principal, PC de l'école, copie Nextcloud, site en
                      ligne, Chromebooks, avec version et date ; bouton
                      « Mettre à jour cette installation » (/api/mettre-a-jour).
   Sans serveur (site en ligne) : tout ce qui peut l'être est affiché, le reste
   dit quoi faire. Aucun service externe.
   ============================================================ */
(function(){
  "use strict";
  const $ = id => document.getElementById(id);
  if(!$("tdb")) return;
  const esc = s => String(s == null ? "" : s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const C = window.CATALOGUE || { jeux: [] };
  const SITE = "https://idgir.github.io/escape-games-cm1-cm2/";
  const etat = { serveur: false, info: null, production: null, installations: null, enLigne: null, maj: null };
  window.__tdb = etat;

  async function lireJSON(url, options){
    try{
      const r = await fetch(url, Object.assign({ cache: "no-store" }, options || {}));
      if(!r.ok) return null;
      return await r.json();
    }catch(e){ return null; }
  }
  const titreJeu = id => { const j = (C.jeux || []).find(x => x.id === id || x.dossier === id || (x.immersif || "").split("/").pop() === id); return j ? `${j.icone || ""} ${j.titre}` : id; };
  const dateCourte = iso => { const m = /^(\d{4})-(\d{2})-(\d{2})(?:T(\d{2}):(\d{2}))?/.exec(String(iso || "")); return m ? `${m[3]}/${m[2]}/${m[1]}${m[4] ? " à " + m[4] + " h " + m[5] : ""}` : ""; };
  const texteVersion = v => v && v.numero ? `n° ${v.numero}${v.date ? " du " + dateCourte(v.date).split(" à ")[0] : ""}` : "";

  /* ---------- Mode projection ---------- */
  function projection(actif){
    document.body.classList.toggle("projection", actif);
    $("btn-projection").setAttribute("aria-pressed", String(actif));
    $("btn-projection").textContent = actif ? "📽️ Quitter la projection" : "📽️ Mode projection";
    try{ localStorage.setItem("eg_tdb_projection", actif ? "1" : ""); }catch(e){}
  }
  $("btn-projection").addEventListener("click", () => projection(!document.body.classList.contains("projection")));
  try{ if(localStorage.getItem("eg_tdb_projection") === "1") projection(true); }catch(e){}

  /* ---------- Barre d'état : un bouton pour chaque voyant orange ou rouge ---------- */
  const BOUTONS = {
    version: () => `<button type="button" class="mini" data-action="maj">🔄 Mettre à jour cette installation</button>`,
    medias: () => `<a class="mini" href="verifier.html">🔍 Voir les médias</a>`,
    resultats: () => `<a class="mini" href="#aide-resultats">❓ Comment faire</a>`,
    sauvegarde: () => `<a class="mini" href="#aide-sauvegarde">❓ Comment faire</a>`,
    serveur: () => `<a class="mini" href="#aide-serveur">❓ Lancer le serveur</a>`
  };
  function boutonsFeu(){
    document.querySelectorAll("#feu .voyant.orange, #feu .voyant.rouge").forEach(v => {
      if(v.querySelector(".mini")) return;
      const nom = v.textContent.trim();
      const id = v.dataset.id || (/^Serveur/.test(nom) ? "serveur" : /^Version/.test(nom) ? "version" : /^Médias/.test(nom) ? "medias" :
        /^Dossier des résultats/.test(nom) ? "resultats" : /^Sauvegarde/.test(nom) ? "sauvegarde" : "");
      if(BOUTONS[id]) v.querySelector("span:last-child").insertAdjacentHTML("beforeend", BOUTONS[id]());
    });
  }
  if(window.MutationObserver) new MutationObserver(boutonsFeu).observe($("feu"), { childList: true });
  $("feu").addEventListener("click", e => { if(e.target.closest("[data-action=maj]")){ $("installations").scrollIntoView(); lancerMaj(); } });

  /* ---------- En direct : QR code et équipes ---------- */
  function dessinerQR(texte){
    if(typeof window.qrcode !== "function") return;
    const qr = window.qrcode(0, "M"); qr.addData(texte); qr.make();
    const n = qr.getModuleCount(), m = 2;
    let d = "";
    for(let y = 0; y < n; y++) for(let x = 0; x < n; x++) if(qr.isDark(y, x)) d += `M${x + m},${y + m}h1v1h-1z`;
    $("qr-eleves").innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${n + 2 * m} ${n + 2 * m}" shape-rendering="crispEdges" role="img" aria-label="QR code de l'adresse des élèves"><rect width="100%" height="100%" fill="#fff"/><path d="${d}" fill="#000"/></svg>`;
  }
  const duree = ms => { if(!ms && ms !== 0) return "—"; const s = Math.round(ms / 1000); return `${Math.floor(s / 60)} min ${String(s % 60).padStart(2, "0")}`; };
  function afficherEquipes(liste){
    const z = $("equipes");
    if(!liste.length){ z.innerHTML = `<p class="vide-direct">Aucune équipe connectée pour l'instant. Les équipes apparaissent dès qu'elles jouent depuis l'adresse ci-contre.</p>`; return; }
    liste.sort((a, b) => String(a.jeu).localeCompare(String(b.jeu)) || (b.enigmesReussies || 0) - (a.enigmesReussies || 0) || (b.score || 0) - (a.score || 0));
    z.innerHTML = `<table><thead><tr><th>Équipe</th><th>Jeu</th><th>Progression</th><th>Énigme en cours</th><th>Temps</th><th>Aides</th><th>État</th></tr></thead><tbody>` +
      liste.map(e => {
        const reussies = e.enigmesReussies != null ? e.enigmesReussies : (e.fragments || []).length;
        const aides = (e.indicesTotal || 0) + (e.pouces || 0) + (e.passees || 0);
        const et = e.fini ? `<span class="badge fini">🏁 fini</span>` : e.enPause ? `<span class="badge pause">⏸️ pause</span>` : `<span class="badge jeu">▶ en jeu</span>`;
        return `<tr><td><b>${esc(e.equipe)}</b>${e.niveau ? `<small>${esc(e.niveau)}</small>` : ""}</td><td>${esc(titreJeu(e.jeu))}</td>` +
          `<td>${e.salle != null ? "étape " + esc(e.salle) + " · " : ""}${esc(reussies)} énigme${reussies > 1 ? "s" : ""} réussie${reussies > 1 ? "s" : ""}${e.score != null ? " · " + esc(e.score) + " pts" : ""}</td>` +
          `<td>${e.enigme ? esc(e.enigme) : "—"}</td><td>${duree(e.msEcoules)}</td>` +
          `<td>${aides ? `${esc(e.indicesTotal || 0)} indice(s)${e.pouces ? " · " + esc(e.pouces) + " coup(s) de pouce" : ""}${e.passees ? " · " + esc(e.passees) + " passée(s)" : ""}` : "aucune"}</td><td>${et}</td></tr>`;
      }).join("") + `</tbody></table>`;
  }
  let minuteur = null;
  async function suivre(){
    const r = await lireJSON("/api/equipes");
    if(r && Array.isArray(r.equipes)){ afficherEquipes(r.equipes); etat.equipes = r.equipes.length; majChromebooks(); }
    clearTimeout(minuteur);
    minuteur = setTimeout(suivre, 5000);
  }

  /* ---------- Après la séance ---------- */
  function liensApres(){
    const p = window.__portail || {};
    const jeu = (p.seance && p.seance.jeu) || p.jeu || "";
    if(jeu) $("lien-bilan").href = "resultats.html?fin=" + encodeURIComponent(jeu);
    $("lien-export").hidden = !etat.serveur;
    if(etat.serveur) $("lien-export").href = "/api/export";
  }

  /* ---------- Production et qualité ---------- */
  let filtre = "tous";
  const oui = (v, texte) => v ? `<span class="ok">✔${texte ? " " + texte : ""}</span>` : `<span class="non">✗</span>`;
  function afficherProduction(){
    const P = etat.production;
    if(!P || !P.jeux){ $("production-source").textContent = "État de production indisponible."; return; }
    const t = P.totaux || {};
    $("production-source").innerHTML = P.direct ? `🟢 Calculé à l'instant sur ce PC.` : `Photographie du ${esc(dateCourte(P.genere))} (sans serveur local). Pour l'état exact : ouvrez ce tableau de bord sur le PC principal.`;
    $("production-compteurs").innerHTML = [
      ["fini", t.finis, "jeu(x) fini(s)"], ["en-cours", t.en_cours, "en cours"], ["sensible", t.sensibles, "sensible(s) à relire"],
      ["medias", (t.images || 0) + (t.videos || 0), `médias manquants (${t.images || 0} images, ${t.videos || 0} vidéos)`],
      ["voix", t.sans_voix, "jeu(x) sans voix"], ["verifier", t.a_verifier, "points « À vérifier » ouverts"], ["credit", t.sans_credit, "médias sans crédit"]
    ].map(([c, n, l]) => `<div class="compteur ${c}"><b>${esc(n == null ? "—" : n)}</b><span>${esc(l)}</span></div>`).join("");
    const garder = j => filtre === "tous" || (filtre === "fini" && j.etat === "fini") || (filtre === "en-cours" && j.etat !== "fini") ||
      (filtre === "sensible" && j.sensible) || (filtre === "medias" && j.medias && (j.medias.images || j.medias.videos));
    const lignes = P.jeux.filter(garder).map(j => {
      const m = j.medias;
      const badge = j.etat === "fini" ? `<span class="badge fini">✅ Fini</span>` : `<span class="badge cours">🛠️ En cours</span>`;
      return `<tr data-jeu="${esc(j.id)}"><td class="jeu">${esc(j.icone)} <b>${esc(j.titre)}</b><small>${j.num ? "n° " + esc(j.num) + " · " : ""}${esc(j.matiere)}${j.annee ? " · année " + esc(j.annee) : ""}</small></td>` +
        `<td>${badge}${j.sensible ? `<span class="badge sensible" title="${esc(j.sensible)}">⚠️ À relire</span>` : ""}</td>` +
        `<td>${m ? (m.images || m.videos ? `<span class="non">${m.images ? esc(m.images) + " image(s)" : ""}${m.images && m.videos ? ", " : ""}${m.videos ? esc(m.videos) + " vidéo(s)" : ""}</span>` : oui(true, m.attendus + "/" + m.attendus)) : "—"}</td>` +
        `<td>${j.immersif ? (j.voix ? `<span class="ok">✔ ${esc(j.voix)}</span>` : `<span class="non">✗ aucune</span>`) : "—"}</td>` +
        `<td>${j.lecons ? `<a href="${esc(j.lecons)}">✔ A4</a>` : oui(false)}</td><td>${j.evaluations && /\.html$/.test(j.evaluations) ? `<a href="${esc(j.evaluations)}">✔ Évaluations</a>` : oui(!!j.evaluations)}</td>` +
        `<td>${oui(!!j.affiche, "affiche")} ${oui(!!j.bande_annonce, "bande-annonce")}</td>` +
        `<td>${j.a_verifier == null ? "—" : j.a_verifier ? `<span class="non">${esc(j.a_verifier)}</span>` : oui(true)}</td>` +
        `<td>${j.sans_credit ? `<span class="non">${esc(j.sans_credit)}</span>` : oui(true)}</td>` +
        `<td class="manque">${j.manque && j.manque.length ? esc(j.manque.join(" · ")) : "rien"}</td></tr>`;
    });
    $("production-table").querySelector("tbody").innerHTML = lignes.join("") || `<tr><td colspan="10" class="vide">Aucun jeu dans ce filtre.</td></tr>`;
    $("a-relire").innerHTML = (P.a_relire || []).map(x => `<li class="${x.priorite === 1 ? "prio" : ""}"><b>${esc(x.titre)}</b> — ${esc(x.point)}</li>`).join("") || "<li>Rien à relire.</li>";
  }
  $("production-filtres").addEventListener("click", e => {
    const b = e.target.closest("button[data-filtre]"); if(!b) return;
    filtre = b.dataset.filtre;
    document.querySelectorAll("#production-filtres button").forEach(x => x.setAttribute("aria-pressed", String(x === b)));
    afficherProduction();
  });

  /* ---------- Installations ---------- */
  const NOMS_ROLES = { principal: "PC principal", ecole: "PC de l'école", nextcloud: "Copie Nextcloud", archive: "Copie installée par archive", copie: "Copie des jeux" };
  function ligneInstallation(nom, v, ref, action, ici){
    let etatTxt = `<span class="badge inconnu">inconnue</span>`;
    if(v && v.numero && ref){
      const ecart = ref - v.numero;
      etatTxt = ecart <= 0 ? `<span class="badge fini">✅ à jour</span>` : `<span class="badge retard">⏳ ${esc(ecart)} version${ecart > 1 ? "s" : ""} de retard</span>`;
    }else if(v && v.numero){ etatTxt = `<span class="badge fini">—</span>`; }
    return `<tr${ici ? ' class="ici"' : ""}><td><b>${esc(nom)}</b>${ici ? ` <span class="badge ici">vous êtes ici</span>` : ""}</td><td>${v && v.numero ? esc(texteVersion(v)) : "—"}</td>` +
      `<td>${v && (v.vu || v.copie_du) ? esc(dateCourte(v.vu || v.copie_du)) : v && v.date ? esc(dateCourte(v.date)) : "—"}</td><td>${etatTxt}</td><td class="action">${action}</td></tr>`;
  }
  function majChromebooks(){ const c = $("ligne-chromebooks"); if(c && etat.equipes != null) c.textContent = `${etat.equipes} équipe(s) connectée(s) en ce moment.`; }
  function afficherInstallations(){
    const I = etat.installations, enLigne = (I && I.en_ligne) || etat.enLigne;
    const ici = I && I.ici;
    const fiches = (I && I.fiches) || [];
    const ecole = (ici && ici.ecole) ? ici : fiches.find(f => f.ecole);
    const nc = I && I.nextcloud;
    const ncV = ici && ici.role === "nextcloud" ? ici : nc && nc.existe ? Object.assign({}, nc.version, { copie_du: nc.copie_du }) : null;
    const principal = ici && ici.role === "principal" ? ici : fiches.find(f => f.role === "principal");
    const ref = Math.max(0, ...[principal, ecole, ncV, enLigne].filter(Boolean).map(v => +v.numero || 0)) || 0;
    const r = [];
    r.push(ligneInstallation("PC principal (E:\\IDRISS\\PROJET ESCAPE GAMES)", principal, ref,
      principal ? "Source des jeux : rien à mettre à jour ici." : "Ouvrez ce tableau de bord sur le PC principal (lancer.bat).", ici && ici.role === "principal"));
    r.push(ligneInstallation("PC de l'école", ecole, ref,
      ecole ? "Fermer puis rouvrir la session Windows, ou double-clic sur <code>demarrer-ecole.bat</code>." : "Inconnu ici : sur le PC de l'école, ouvrez ce tableau de bord, ou lancez <code>diagnostic.bat</code>.", !!(ici && ici.ecole)));
    r.push(ligneInstallation("Copie Nextcloud", ncV, ref,
      nc && !nc.existe ? `Dossier introuvable (${esc(nc.dossier)}) : écrivez le bon chemin dans <code>outils-ecole\\dossier-nextcloud.txt</code>.` :
      "Sur le PC principal : bouton « Mettre à jour cette installation », ou double-clic sur <code>mettre-a-jour-nextcloud.bat</code>.", !!(ici && ici.role === "nextcloud")));
    r.push(ligneInstallation("Site en ligne (GitHub Pages)", enLigne, ref,
      `Publier depuis le PC principal (après relecture des jeux sensibles) : <code>git push origin escape-games</code>. <a href="#aide-publier">Pas à pas</a>`, !I && /github\.io$/.test(location.hostname)));
    r.push(`<tr><td><b>Chromebooks des élèves</b></td><td colspan="3">Même version que le PC (ou le site) d'où ils jouent. Application installée : mise à jour à la connexion suivante.</td><td class="action" id="ligne-chromebooks">${etat.serveur ? "" : "Rien à faire."}</td></tr>`);
    $("installations-table").querySelector("tbody").innerHTML = r.join("");
    $("installations-ici").innerHTML = ici ? `Vous êtes sur <b>${esc(NOMS_ROLES[ici.role] || ici.role)}</b> (${esc(ici.machine)}), version <b>${esc(ici.texte || "inconnue")}</b>${ici.commit ? " · commit " + esc(ici.commit.slice(0, 7)) : ""}.`
      : `Serveur local absent : seule la version du site en ligne est connue${enLigne ? " (" + esc(texteVersion(enLigne)) + ")" : ""}. Le bouton de mise à jour marche quand la page est ouverte par <code>lancer.bat</code>.`;
    $("btn-maj").disabled = !I;
    majChromebooks();
  }
  async function lancerMaj(){
    if(!etat.serveur){ $("maj-journal").hidden = false; $("maj-journal").textContent = "Le serveur local n'est pas lancé : double-clic sur lancer.bat, puis rouvrez cette page."; return; }
    const b = $("btn-maj"); b.disabled = true; b.textContent = "⏳ Mise à jour en cours…";
    $("maj-journal").hidden = false; $("maj-journal").textContent = "Démarrage…";
    let r = await lireJSON("/api/mettre-a-jour", { method: "POST", headers: { "Content-Type": "application/json" }, body: "{}" });
    for(let i = 0; r && r.en_cours && i < 2400; i++){
      $("maj-journal").textContent = (r.lignes || []).join("\n") || "…";
      await new Promise(f => setTimeout(f, window.__tdbPas || 1500));
      r = await lireJSON("/api/mettre-a-jour");
    }
    $("maj-journal").textContent = r ? ((r.lignes || []).join("\n") + (r.ok ? "\n✅ Terminé." : "\n⚠️ Terminé avec un problème : lisez les lignes ci-dessus.")) : "Pas de réponse du serveur.";
    b.disabled = false; b.textContent = "🔄 Mettre à jour cette installation";
    etat.maj = r;
    chargerInstallations();
  }
  $("btn-maj").addEventListener("click", lancerMaj);
  async function chargerInstallations(){
    etat.installations = etat.serveur ? await lireJSON("/api/installations") : null;
    if(!(etat.installations && etat.installations.en_ligne))
      etat.enLigne = await lireJSON((/github\.io$/.test(location.hostname) ? "" : SITE) + "version.json?t=" + Date.now());
    afficherInstallations();
  }

  /* ---------- Démarrage ---------- */
  (async function(){
    etat.info = await lireJSON("/api/info");
    etat.serveur = !!(etat.info && etat.info.ip);
    if(etat.serveur){
      const adresse = `http://${etat.info.ip}${+etat.info.port === 80 ? "" : ":" + etat.info.port}/`;
      $("adresse-eleves").innerHTML = `Adresse des élèves : <b>${esc(adresse)}</b>`;
      dessinerQR(adresse);
      $("direct-etat").textContent = "Mise à jour toutes les 5 secondes.";
      suivre();
    }else{
      $("adresse-eleves").innerHTML = `Sans serveur local, les élèves jouent sur le site en ligne : <b>${esc(SITE)}</b>`;
      dessinerQR(SITE);
      $("direct-etat").innerHTML = `Le suivi en direct marche avec le serveur local : double-clic sur <code>lancer.bat</code> sur le PC de la classe. <a href="#aide-serveur">Pas à pas</a>`;
      $("equipes").innerHTML = "";
    }
    const p = etat.serveur ? await lireJSON("/api/production") : null;
    etat.production = p && p.jeux ? p : window.PRODUCTION || null;
    afficherProduction();
    await chargerInstallations();
    liensApres();
    setTimeout(liensApres, 1500);
    boutonsFeu();
    window.__tdbPret = true;
  })();
})();
