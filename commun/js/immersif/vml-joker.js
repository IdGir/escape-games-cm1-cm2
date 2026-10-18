/* ============================================================
   VARIANTES IMMERSIVES — JOKER D'ÉQUIPE (amélioration N15)
   ------------------------------------------------------------
   Même principe que commun/js/joker.js, adapté au moteur VML : un bouton « 🃏 Joker » dans la barre
   d'outils du panneau d'énigme. L'énigme est PASSÉE : 0 point, aucune erreur comptée, marquée
   « passée » dans le journal, le bilan et le compte-rendu ; la partie continue (réaction du décor,
   énigme suivante, mot de l'escale donné à la fin comme d'habitude). Une escale où un joker a servi
   ne donne ni « Maître-nageur » ni bonus de rapidité.
   Réglage enseignant (⚙️ → 🃏 Joker, même clé que les jeux classiques : escape_joker) :
   désactivé · 1 joker par partie (défaut) · 1 joker par escale ; adresse : ?joker=0|partie|salle.
   Chargé après js/app.js et vml-suivi.js.
   ============================================================ */
(function(){
  const VML = window.VML;
  if(!VML || !VML.ouvrirEnigme) return;
  const CLE = "escape_joker";
  const MODES = { off: "Désactivé", partie: "1 joker par partie (défaut)", salle: "1 joker par escale" };

  function lire(){
    let r = {}; try{ r = JSON.parse(localStorage.getItem(CLE) || "{}") || {}; }catch(e){}
    const p = new URLSearchParams(location.search).get("joker");
    if(p === "0" || p === "off") return "off";
    if(p === "partie" || p === "salle") return p;
    return MODES[r.mode] ? r.mode : "partie";
  }
  const ecrire = m => { try{ localStorage.setItem(CLE, JSON.stringify({ mode: m })); }catch(e){} };
  const idsEscale = n => ((VML.escale(n) || { enigmes: [] }).enigmes || []).map(e => e.id);
  function utilises(){
    const E = VML.ETAT; if(!E) return 0;
    const r = E.resolues || {}, mode = lire();
    const ids = mode === "salle" ? idsEscale(E.escale) : Object.keys(r);
    return ids.filter(id => r[id] && r[id].passee).length;
  }
  const restants = () => lire() === "off" ? 0 : Math.max(0, 1 - utilises());
  const libelle = () => { const r = restants(); return lire() === "off" ? "" : (r > 0 ? `🃏 Joker (${r} restant${r > 1 ? "s" : ""})` : "🃏 Joker utilisé"); };
  const aJokerDansEscale = n => { const r = (VML.ETAT || {}).resolues || {}; return idsEscale(n).some(id => r[id] && r[id].passee); };

  /* ---- Bouton dans le panneau d'énigme ---- */
  const ouvrir = VML.ouvrirEnigme;
  VML.ouvrirEnigme = function(e, o){
    const res = ouvrir.apply(this, arguments);
    try{
      const carte = res && res.carte, barre = carte && carte.querySelector(".barre-outils");
      if(!barre || barre.querySelector(".btn-joker") || lire() === "off") return res;
      const b = document.createElement("button");
      b.type = "button"; b.className = "btn-laiton petit btn-joker";
      b.title = "Passer cette énigme (0 point) pour continuer la partie ; vous la reprendrez avec l'enseignant";
      const maj = () => { b.textContent = libelle(); b.disabled = restants() === 0 || carte.classList.contains("resolue"); };
      maj();
      b.addEventListener("click", () => {
        if(b.disabled || restants() === 0) return;
        if(!window.confirm("🃏 Utiliser le joker ?\n\nL'énigme est passée : elle ne rapporte aucun point. Vous la reprendrez avec l'enseignant.")) return;
        const E = VML.ETAT, s = VML.etatEnigme(e.id);
        E.resolues = E.resolues || {};
        E.resolues[e.id] = { pts: 0, bienDoc: 0, erreurs: s.erreurs, indices: s.indices, fiches: s.fiches.slice(), ms: Date.now() - (s.ouverte || Date.now()), premier: false, passee: true };
        carte.classList.add("resolue");
        carte.querySelectorAll("[data-valider], [data-indice], input, .instr-reglage button").forEach(x => { x.disabled = true; });
        const fb = carte.querySelector("#fb-" + e.id);
        if(fb){ fb.className = "feedback indice show"; fb.innerHTML = "🃏 <b>Joker utilisé : énigme passée</b> (0 point). Notez-la : vous la reprendrez avec l'enseignant."; }
        maj();
        if(VML.majHUD) VML.majHUD();
        if(VML.sauver) VML.sauver();
        setTimeout(() => { res.fermer(); if(o && o.onReussite) o.onReussite(E.resolues[e.id]); }, VML.d ? VML.d(1100) : 1100);
      });
      barre.appendChild(b);
    }catch(err){ console.warn("Joker :", err); }
    return res;
  };

  /* ---- Une escale où un joker a servi : pas de bonus d'escale (ils sont calculés juste avant l'enregistrement du compte-rendu) ---- */
  if(VML.memoriserCompteRendu){
    const memo = VML.memoriserCompteRendu;
    VML.memoriserCompteRendu = function(){
      const E = VML.ETAT;
      if(E && E.escaleTerminee && E.bonus && (E.bonus.maitreNageur || E.bonus.rapidite) && aJokerDansEscale(E.escale)){
        E.score = Math.max(0, (E.score || 0) - (E.bonus.maitreNageur || 0) - (E.bonus.rapidite || 0));
        E.bonus = {};
        if(E.bonusEscales) E.bonusEscales[E.escale] = {};
      }
      return memo.apply(this, arguments);
    };
  }

  /* ---- Réglage dans ⚙️ ---- */
  if(VML.ouvrirReglages){
    const ouvrirReglages = VML.ouvrirReglages;
    VML.ouvrirReglages = function(){
      const r = ouvrirReglages.apply(this, arguments);
      const corps = document.querySelector("#reglages .reglages-corps");
      if(corps && !document.getElementById("reglages-joker")){
        const sec = document.createElement("section");
        sec.id = "reglages-joker";
        sec.innerHTML = `<h4>🃏 Joker d'équipe</h4>
          <label class="reg-ligne" for="reg-joker"><span>Passer une énigme bloquante</span><select id="reg-joker">${Object.entries(MODES).map(([k, v]) => `<option value="${k}" ${k === lire() ? "selected" : ""}>${v}</option>`).join("")}</select></label>
          <p class="note">Le joker passe une énigme (0 point, notée « passée » au bilan) pour ne pas arrêter la partie ; l'équipe la reprend ensuite avec l'enseignant. Gardé sur cet appareil.</p>`;
        sec.querySelector("select").addEventListener("change", ev => ecrire(ev.target.value));
        corps.appendChild(sec);
      }
      return r;
    };
  }
  VML.JOKER = { lire, ecrire, restants, utilises, MODES };
})();
