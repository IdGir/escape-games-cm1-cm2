/* ============================================================
   PORTAIL À TROIS BOUTONS (B1) — espace enseignant
   ------------------------------------------------------------
   En haut d'enseignant.html : le feu vert (A4), le jeu prévu pour la
   période (calendrier du catalogue ; Année A en 2026-2027), puis :
     1 · Préparer  → revérifie le feu vert, ouvre le pack d'impression (B2) ;
     2 · Lancer    → fixe la séance du jour (A1, serveur local) et ouvre
                     la page à projeter avec le QR code (A2) ; sans
                     serveur : fabrique le lien « ?jeu=… » des élèves ;
     3 · Terminer  → bilan de séance imprimable + passeport (A5,
                     resultats.html?fin=<jeu>) et fin de la séance.
   Les 24 tuiles d'avant restent, repliées sous « Tout le reste ».
   ============================================================ */
(function(){
  "use strict";
  const S = window.SEANCE, C = window.CATALOGUE, $ = id => document.getElementById(id);
  if(!S || !C || !$("seance")) return;
  const esc = s => String(s == null ? "" : s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const maintenant = window.__dateSeance && typeof window.__dateSeance.getMonth === "function" ? window.__dateSeance : new Date();
  const P = S.periodeDe(maintenant), A = S.anneeDe(maintenant);
  const prevus = S.jeuxDeLaPeriode(C, maintenant);
  const tous = C.jeux.filter(S.jouable);
  const etat = { jeu: "", grade: "", serveur: false, local: false, seance: null };
  const memo = S.choixLocal() || {};

  /* ---- Tout le reste : replié, mais s'ouvre pour un lien #ancre ou l'impression ---- */
  const reste = $("tout-le-reste");
  const ouvrirSiAncre = () => { const h = location.hash && document.getElementById(location.hash.slice(1)); if(h && reste && reste.contains(h)){ reste.open = true; setTimeout(() => h.scrollIntoView(), 30); } };
  window.addEventListener("hashchange", ouvrirSiAncre); ouvrirSiAncre();
  window.addEventListener("beforeprint", () => { if(reste) reste.open = true; });

  /* ---- Choix du jeu ---- */
  $("periode").textContent = `Période ${P.slice(1)} (${S.NOMS_PERIODES[P]}) · Année ${A} — ${prevus.length ? (prevus.length > 1 ? "jeux prévus" : "jeu prévu") + " au calendrier :" : "aucun jeu prévu au calendrier pour cette période : choisissez-en un."}`;
  $("choix-jeux").innerHTML = prevus.map(j => `<button type="button" data-jeu="${esc(S.idDe(j))}" aria-pressed="false" style="--c:${esc((j.couleurs || [])[0] || "#1d3a8a")}">${esc(j.icone || "")} ${esc(j.titre)}</button>`).join("");
  $("autre-jeu").innerHTML = `<option value="">—</option>` + tous.map(j => `<option value="${esc(S.idDe(j))}">${esc(j.icone || "")} ${esc(j.titre)} (${esc(j.matiere || "")}${j.annee && j.periodes && j.periodes.length ? ", " + esc(j.annee) + " " + esc(j.periodes.join("-")) : ""})</option>`).join("");
  async function grades(id){
    const j = S.infoJeu(C, id);
    try{
      if(j && j.immersif){ const r = await fetch(j.immersif + "/assets/data/enigmes.json", { cache: "no-store" }); if(r.ok) return ((await r.json()).niveaux || []); }
    }catch(e){}
    return [];
  }
  async function choisir(id, grade){
    etat.jeu = id;
    document.querySelectorAll("#choix-jeux button").forEach(b => b.setAttribute("aria-pressed", String(b.dataset.jeu === id)));
    $("autre-jeu").value = prevus.some(j => S.idDe(j) === id) ? "" : id;
    const gs = await grades(id), sel = $("choix-grade");
    sel.innerHTML = `<option value="">au choix des équipes</option>` + gs.map(g => `<option value="${esc(g.id)}">${esc(g.icone || "")} ${esc(g.nom)} (${esc(g.equivalent || "")})</option>`).join("");
    sel.disabled = !gs.length;
    sel.value = gs.some(g => g.id === grade) ? grade : "";
    etat.grade = sel.value;
    S.choixLocal({ jeu: etat.jeu, grade: etat.grade });
    afficherEtat();
  }
  $("choix-jeux").addEventListener("click", e => { const b = e.target.closest("button[data-jeu]"); if(b) choisir(b.dataset.jeu, etat.grade); });
  $("autre-jeu").addEventListener("change", e => { if(e.target.value) choisir(e.target.value, etat.grade); else if(prevus[0]) choisir(S.idDe(prevus[0]), etat.grade); });
  $("choix-grade").addEventListener("change", e => { etat.grade = e.target.value; S.choixLocal({ jeu: etat.jeu, grade: etat.grade }); });

  /* ---- État de la séance ---- */
  const titre = id => (S.infoJeu(C, id) || {}).titre || id;
  function afficherEtat(){
    const s = etat.seance, p = $("etat-seance");
    if(s && s.jeu) p.innerHTML = `🟢 <b>Séance en cours</b> : ${esc(titre(s.jeu))}${s.grade ? " · grade imposé" : ""}${s.depuis ? " · depuis " + esc(String(s.depuis).slice(11, 16).replace(":", " h ")) : ""}. Les élèves ne voient qu'un bouton « Jouer ». <a href="tableau.html" target="_blank" rel="noopener">QR code à projeter</a>`;
    else if(etat.serveur) p.innerHTML = `⚪ Aucune séance lancée : l'accueil des élèves montre tous les jeux.`;
    else p.innerHTML = `ℹ️ Serveur local non lancé : « Lancer » fabrique un lien pour les élèves (site en ligne). Pour enregistrer les résultats sur ce PC, double-clic sur <code>lancer.bat</code>.`;
  }

  /* ---- Feu vert (A4) ---- */
  function voyant(v){
    return `<div class="voyant ${esc(v.etat)}" tabindex="0" title="${esc(v.message)}"><span class="pastille" aria-hidden="true"></span><span><b>${esc(v.nom)} — ${({ vert: "OK", orange: "à regarder", rouge: "bloquant" })[v.etat] || ""}</b><span class="msg">${esc(v.message)}</span>${v.action ? `<span class="action">➜ ${esc(v.action)}</span>` : ""}</span></div>`;
  }
  async function feuVert(){
    const z = $("feu");
    const r = await S.sante("");
    if(r && r.voyants){ z.innerHTML = r.voyants.map(voyant).join(""); z.dataset.etat = r.etat; return r; }
    const i = await S.info("");
    const v = i ? [{ nom: "Serveur", etat: "orange", message: "Le serveur répond, mais le feu vert n'est lisible que sur le PC qui fait tourner le serveur.", action: "Ouvrez http://127.0.0.1:8000/enseignant.html sur ce PC." }]
      : [{ nom: "Serveur", etat: "orange", message: "Serveur local non lancé (ou page ouverte depuis le site en ligne) : les résultats restent dans les Chromebooks.",
           action: "Sur le PC de la classe : double-clic sur lancer.bat (ou installer-ecole.bat une fois pour qu'il démarre tout seul)." }];
    z.innerHTML = v.map(voyant).join(""); z.dataset.etat = "orange";
    return null;
  }

  /* ---- Les trois boutons ---- */
  const ouvrir = url => { const w = window.open(url, "_blank"); if(!w) location.href = url; };
  $("btn-preparer").addEventListener("click", async () => {
    if(!etat.jeu) return;
    ouvrir(`pack-impression.html?jeu=${encodeURIComponent(etat.jeu)}${etat.grade ? "&grade=" + encodeURIComponent(etat.grade) : ""}`);
    feuVert();
  });
  $("btn-lancer").addEventListener("click", async () => {
    if(!etat.jeu) return;
    const b = $("btn-lancer"); b.disabled = true;
    S.choixLocal({ jeu: etat.jeu, grade: etat.grade });
    const r = etat.serveur ? await S.fixer(etat.jeu, etat.grade, titre(etat.jeu), "") : null;
    b.disabled = false;
    const lien = $("lien-eleves");
    if(r && r.ok){
      etat.seance = r.seance; afficherEtat(); feuVert();
      lien.hidden = true;
      ouvrir("tableau.html");
    }else{
      const url = S.lienEleves(/^https?:$/.test(location.protocol) ? location.href : S.URL_EN_LIGNE, etat.jeu, etat.grade);
      lien.hidden = false;
      lien.innerHTML = `🔗 Lien à donner aux élèves (ou à mettre en favori) : <a href="${esc(url)}" target="_blank" rel="noopener">${esc(url)}</a> <button type="button" id="copier-lien">📋 Copier</button>`;
      $("copier-lien").addEventListener("click", async () => { try{ await navigator.clipboard.writeText(url); $("copier-lien").textContent = "✅ Copié"; }catch(e){} });
      ouvrir(`tableau.html?jeu=${encodeURIComponent(etat.jeu)}${etat.grade ? "&grade=" + encodeURIComponent(etat.grade) : ""}`);
    }
    window.__lance = { jeu: etat.jeu, grade: etat.grade, serveur: !!(r && r.ok) };
  });
  $("btn-terminer").addEventListener("click", async () => {
    const jeu = (etat.seance && etat.seance.jeu) || etat.jeu;
    if(!jeu) return;
    if(etat.serveur){ await S.terminer(""); etat.seance = null; afficherEtat(); }
    ouvrir(`resultats.html?fin=${encodeURIComponent(jeu)}`);
    window.__termine = { jeu };
  });

  /* ---- Démarrage : séance déjà lancée ? sinon le jeu prévu (ou le dernier choisi) ---- */
  (async function(){
    const s = await S.lire("");
    etat.serveur = !!(s.source === "serveur" || s.serveur);
    etat.local = !!s.local;
    etat.seance = s.source === "serveur" ? s : null;
    const depart = (etat.seance && etat.seance.jeu) || (memo.jeu && S.infoJeu(C, memo.jeu) ? memo.jeu : "") || (prevus[0] ? S.idDe(prevus[0]) : S.idDe(tous[0]));
    await choisir(depart, (etat.seance && etat.seance.grade) || memo.grade || "");
    await feuVert();
    window.__portail = etat;
  })();
})();
