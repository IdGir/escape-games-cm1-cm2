/* ============================================================
   JOKER D'ÉQUIPE (amélioration N15) — tronc commun
   ------------------------------------------------------------
   Les énigmes d'une salle s'enchaînent : une seule énigme bloquante arrête
   toute l'équipe, même avec les indices (E3) et le palier Découverte (E2).
   Le joker permet de CONTINUER la partie et de reprendre l'énigme ensuite
   avec l'enseignant :
     • bouton « 🃏 Joker » à côté de « 💡 Indice », avec demande de
       confirmation ; l'énigme est PASSÉE : 0 point, aucune erreur comptée,
       marquée « passée » dans le bilan et le compte-rendu (suivi N12) ;
     • la salle continue normalement (énigme suivante, puis mot de la serrure
       donné à la fin de la salle comme d'habitude) ; une salle où un joker
       a servi ne donne pas le bonus de rapidité ;
     • Déclaration et Tour du monde (une énigme par salle) : la salle est
       validée sans point et le fragment du mot est donné, pour continuer.
   Réglage enseignant (⚙️ Réglages → 🃏 Joker, gardé sur l'appareil) :
     désactivé · 1 joker par partie (défaut) · 1 joker par salle.
     Adresse : …?joker=0 (désactivé), ?joker=partie, ?joker=salle.
   En mode duel (N4) : un joker PAR ÉQUIPE (par partie ou par salle).
   Le nombre de jokers utilisés se déduit des notes du suivi, gardées avec la
   partie : il survit à la reprise d'une partie. Chargé après suivi-enigmes.js.
   ============================================================ */
(function(){
  if(typeof ETAT === "undefined" || !window.SUIVI_ENIGMES) return;
  const CLE = "escape_joker";
  const SUIVI = window.SUIVI_ENIGMES;
  const MODES = { off: "Désactivé", partie: "1 joker par partie (défaut)", salle: "1 joker par salle" };

  /* ---- Réglage ---- */
  function lire(){
    let r = {}; try{ r = JSON.parse(localStorage.getItem(CLE) || "{}") || {}; }catch(e){}
    const p = new URLSearchParams(location.search).get("joker");
    if(p === "0" || p === "off") return "off";
    if(p === "partie" || p === "salle") return p;
    return MODES[r.mode] ? r.mode : "partie";
  }
  function ecrire(mode){ try{ localStorage.setItem(CLE, JSON.stringify({ mode })); }catch(e){} majBoutons(); }

  /* ---- Combien de jokers a déjà utilisé l'équipe qui joue ? ---- */
  const equipeQuiJoue = () => (ETAT.duel && typeof ETAT.duel.tour === "number") ? ETAT.duel.tour : 0;
  function utilises(){
    const mode = lire();
    return Object.values(SUIVI.notes()).filter(n => n.p && (n.t || 0) === equipeQuiJoue() && (mode !== "salle" || n.s === ETAT.salle)).length;
  }
  const restants = () => { const m = lire(); return m === "off" ? 0 : Math.max(0, 1 - utilises()); };

  /* ---- Pas de point, pas de confettis pour une énigme passée ---- */
  let muetJusqua = 0;
  const muet = ms => { muetJusqua = Math.max(muetJusqua, Date.now() + ms); };
  const enMuet = () => Date.now() < muetJusqua;
  if(typeof window.ajouterScore === "function"){
    const o = window.ajouterScore;
    window.ajouterScore = function(){ return enMuet() ? undefined : o.apply(this, arguments); };
  }
  if(typeof window.confettis === "function"){
    const o = window.confettis;
    window.confettis = function(){ return enMuet() ? undefined : o.apply(this, arguments); };
  }
  /* Une salle où un joker a servi ne donne pas le bonus de rapidité */
  if(typeof window.validerSalle === "function"){
    const o = window.validerSalle;
    window.validerSalle = function(n){
      if(Object.values(SUIVI.notes()).some(x => x.p && x.s === n)) muet(1800);
      return o.apply(this, arguments);
    };
  }

  /* ---- Bouton ---- */
  const libelle = () => { const r = restants(); return lire() === "off" ? "" : (r > 0 ? `🃏 Joker (${r} restant${r > 1 ? "s" : ""})` : "🃏 Joker utilisé"); };
  function majBoutons(){
    document.querySelectorAll(".btn-joker").forEach(b => {
      const carteResolue = b.closest(".enigme-carte.resolue, .zone-enigme.resolue");
      const l = libelle();
      b.hidden = !l; b.textContent = l;
      b.disabled = restants() === 0 || !!carteResolue;
    });
  }
  function creerBouton(onClic){
    const b = document.createElement("button");
    b.type = "button"; b.className = "btn gris petit btn-joker";
    b.title = "Passer cette énigme (0 point) pour continuer la partie ; vous la reprendrez avec l'enseignant";
    b.addEventListener("click", () => {
      if(b.disabled || restants() === 0) return;
      if(!window.confirm("🃏 Utiliser le joker ?\n\nL'énigme est passée : elle ne rapporte aucun point. Vous la reprendrez avec l'enseignant.")) return;
      onClic();
    });
    return b;
  }
  function marquer(id, salle){
    const n = SUIVI.note(id, { s: salle != null ? salle : ETAT.salle, p: 1, ok: 0, pc: 0, t: equipeQuiJoue() });
    n.p = 1; n.ok = 0; n.pc = 0;
    if(typeof sauvegarder === "function") sauvegarder();
  }
  const message = "🃏 <b>Joker utilisé : énigme passée</b> (0 point). Notez-la : vous la reprendrez avec l'enseignant.";

  /* ---- Moteur commun : une carte d'énigme, un callback de réussite ---- */
  if(typeof window.activerEnigme === "function"){
    const origine = window.activerEnigme;
    window.activerEnigme = function(e, onReussite){
      const r = origine.apply(this, arguments);
      if(!e || typeof e !== "object") return r;                       // moteur propre : voir plus bas
      const carte = document.getElementById("enigme-" + e.id);
      const barre = carte && carte.querySelector(".barre-outils");
      if(barre && !barre.querySelector(".btn-joker")){
        const b = creerBouton(() => {
          marquer(e.id);
          carte.classList.add("resolue");
          carte.querySelectorAll("[data-valider], input, .instr-reglage button").forEach(x => { x.disabled = true; });
          const bi = carte.querySelector("#indice-" + e.id); if(bi) bi.disabled = true;
          const fb = carte.querySelector("#fb-" + e.id);
          if(fb){ fb.className = "feedback indice show"; fb.innerHTML = message; }
          muet(300);
          b.disabled = true;
          setTimeout(() => { onReussite(e, 0, 1); majBoutons(); }, 0);
        });
        barre.appendChild(b);
        majBoutons();
      }
      return r;
    };
  }

  /* ---- Moteur propre (Déclaration, Tour du monde) : une énigme par salle ---- */
  if(typeof window.v2Debut === "function" && typeof window.validerSalle === "function"){
    const debut = window.v2Debut;
    window.v2Debut = function(){
      const r = debut.apply(this, arguments);
      setTimeout(() => {
        const zone = document.querySelector("#salle-contenu .zone-enigme");
        const barre = zone && zone.querySelector(".barre-outils");
        if(!barre || barre.querySelector(".btn-joker")) return;
        const salle = ETAT.salle;
        const b = creerBouton(() => {
          marquer("s" + salle, salle);
          zone.classList.add("resolue");
          zone.querySelectorAll("button, select, input").forEach(x => { if(!x.closest(".barre-outils")) x.disabled = true; });
          b.disabled = true;
          const fb = zone.querySelector(".feedback");
          if(fb){ fb.className = "feedback indice show"; fb.innerHTML = message; }
          muet(2500);
          setTimeout(() => { window.validerSalle(salle, 1); majBoutons(); }, 900);
        });
        barre.appendChild(b);
        majBoutons();
      }, 0);
      return r;
    };
  }

  /* ---- Réglage dans ⚙️ ---- */
  function bloc(){
    const g = document.createElement("div");
    g.className = "reglages-group"; g.id = "reglages-joker";
    const m = lire();
    g.innerHTML = `<h4>🃏 Joker d'équipe</h4>
      <div class="reglage-ligne"><div class="libelle"><b>Passer une énigme bloquante</b><br>
        <span style="font-size:.8rem;opacity:.7">Le joker passe une énigme (0 point, notée « passée » au bilan) pour ne pas arrêter la partie ; l'équipe la reprend ensuite avec l'enseignant.
        En mode duel : un joker par équipe. Gardé sur cet appareil.</span></div>
        <div class="controle"><select id="reg-joker">${Object.entries(MODES).map(([k, v]) => `<option value="${k}" ${k === m ? "selected" : ""}>${v}</option>`).join("")}</select></div></div>`;
    g.querySelector("select").addEventListener("change", ev => ecrire(ev.target.value));
    return g;
  }
  const obs = new MutationObserver(() => {
    const calme = document.getElementById("reg-calme");
    if(calme && !document.getElementById("reglages-joker")){
      const grp = calme.closest(".reglages-group"); if(grp) grp.parentNode.appendChild(bloc());
    }
  });
  const demarrer = () => obs.observe(document.body, { childList: true, subtree: true });
  if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", demarrer); else demarrer();

  window.JOKER = { lire, ecrire, restants, utilises, MODES };
})();
