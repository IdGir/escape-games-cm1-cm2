/* ============================================================
   DIFFICULTÉ ÉNIGME PAR ÉNIGME (amélioration N20) — tronc commun
   ------------------------------------------------------------
   Les trois paliers (Découverte, CM1, CM2 — E2) valent pour toute la salle.
   Mais, pour une classe donnée, certaines énigmes sont systématiquement plus
   dures ou plus faciles que les autres. Un réglage FIN, énigme par énigme,
   s'AJOUTE au palier choisi au départ (il ne le remplace pas) :

     échelle des positions :  0 aide renforcée · 1 données du CM1 · 2 données du CM2 · 3 défi
     départ : Découverte = 0 · CM1 = 1 · CM2 = 2 ;   position = départ + réglage (de −2 à +2),
     limitée à 0…3.

     0  aide renforcée (comme le palier Découverte, pour cette énigme seulement) :
        données du CM1, premier indice offert, un choix faux écarté, leçon mise en avant ;
     1  les données du CM1 ;           2  les données du CM2 ;
     3  défi : données du CM2, et chaque indice coûte 2 points de plus.

   D'où vient le réglage de chaque énigme (le premier trouvé) :
     1. l'adresse : …/?dif=1-2:-1,2-3:+1  (identifiant de l'énigme : réglage) ;
     2. les réglages de la classe posés par l'enseignant dans prof.html
        (« 🎚️ Difficulté par énigme ») : serveur local, sinon cet appareil ;
     3. le champ facultatif « difficulte » (de −2 à +2) de l'énigme dans
        enigmes.json, contrôlé avant publication (verifier-enigmes.js).
   Sans réglage, rien ne change : la position de départ est jouée.
   Aucun effet sur les règles de score (10 / 3 points, indices −2 chacun,
   hors « défi »). Une pastille 🎚️ prévient l'équipe quand l'énigme est réglée.
   Chargé après palier-decouverte.js et suivi-enigmes.js.
   ============================================================ */
(function(){
  if(typeof ETAT === "undefined" || typeof window.enigmeHTML !== "function" || typeof window.activerEnigme !== "function" || !window.PALIER) return;
  const JEU_ID = (typeof JEU !== "undefined" && JEU.id) || "jeu";
  const CLE = "escape_difficulte_" + JEU_ID;
  const SURCOUT_DEFI = 2;
  let serveur = null;          // réglages reçus du serveur local (prof.html)
  let reel = null;             // niveau réel de la partie, pendant qu'on joue une énigme à un autre niveau
  const NIV = {};              // énigme → niveau des données affichées
  const borne = (n, a, b) => Math.max(a, Math.min(b, n));
  const niveauReel = () => reel || ETAT.niveau;
  const avecNiveau = (niv, fn) => {
    const avant = ETAT.niveau, r = reel;
    if(!reel) reel = avant;
    ETAT.niveau = niv;
    try{ return fn(); } finally { ETAT.niveau = avant; reel = r; }
  };

  /* ---- Les réglages ---- */
  function lireAdresse(){
    const p = new URLSearchParams(location.search).get("dif");
    if(p === null) return null;
    const o = {};
    p.split(",").forEach(x => { const m = x.trim().match(/^([^:]+):\s*([+-]?\d)$/); if(m) o[m[1]] = +m[2]; });
    return o;
  }
  function lireLocal(){ try{ return JSON.parse(localStorage.getItem(CLE) || "{}") || {}; }catch(e){ return {}; } }
  const reglagesClasse = () => lireAdresse() || serveur || lireLocal();
  function reglage(e){
    const r = reglagesClasse(), v = r[e.id] !== undefined ? +r[e.id] : (+e.difficulte || 0);
    return Number.isFinite(v) ? borne(Math.round(v), -2, 2) : 0;
  }
  const depart = () => ETAT.palier === "decouverte" ? 0 : (niveauReel() === "CM1" ? 1 : 2);
  const position = e => borne(depart() + reglage(e), 0, 3);
  const niveauDonnees = e => position(e) <= 1 ? "CM1" : "CM2";
  const aideRenforcee = e => position(e) === 0;

  /* Réglages du serveur local (en classe, avec lancer.bat) */
  try{
    fetch("/api/difficulte?jeu=" + encodeURIComponent(JEU_ID), { cache: "no-store" })
      .then(r => r.ok ? r.json() : null).then(d => { if(d && d.valeurs && typeof d.valeurs === "object") serveur = d.valeurs; }).catch(() => {});
  }catch(e){}

  const style = document.createElement("style");
  style.textContent = `.badge-difficulte{display:inline-block;margin-left:8px;padding:1px 9px;border-radius:999px;font-size:.78rem;font-weight:bold;vertical-align:middle;background:#ede7f6;color:#4a2c8a;border:1px solid #b39ddb}
    .badge-difficulte.facile{background:#e5f5ea;color:#14532d;border-color:#9bd3a6}.badge-difficulte.defi{background:#fff3e0;color:#7a3d00;border-color:#f0b36a}`;
  document.head.appendChild(style);

  /* ---- Les données affichées sont celles du niveau de la position ---- */
  const dn = window.donneesNiveau;
  if(typeof dn === "function"){
    window.donneesNiveau = function(e){
      const n = e && NIV[e.id];
      return n && n !== ETAT.niveau ? avecNiveau(n, () => dn.call(this, e)) : dn.apply(this, arguments);
    };
  }
  const html = window.enigmeHTML;
  window.enigmeHTML = function(e){
    const args = arguments, n = niveauDonnees(e);
    NIV[e.id] = n;
    return avecNiveau(n, () => html.apply(this, args));
  };

  const origine = window.activerEnigme;
  window.activerEnigme = function(e, onReussite){
    if(!e || typeof e !== "object") return origine.apply(this, arguments);
    const args = arguments, p = position(e), n = niveauDonnees(e);
    NIV[e.id] = n;
    const r = avecNiveau(n, () => origine.apply(this, args));
    const carte = document.getElementById("enigme-" + e.id);
    if(carte){
      const base = depart();
      carte.dataset.difficulte = String(p - base);
      carte.dataset.position = String(p);
      const tete = carte.querySelector(".enigme-tete");
      if(tete && p !== base && !tete.querySelector(".badge-difficulte")){
        const b = document.createElement("span");
        b.className = "badge-difficulte " + (p < base ? "facile" : "defi");
        b.textContent = p === 3 ? "🏆 Défi" : p === 0 ? "🎚️ Aide renforcée" : (p < base ? "🎚️ Réglée plus facile" : "🎚️ Réglée plus difficile");
        b.title = p === 3 ? "Données du CM2 ; chaque indice coûte 2 points de plus" : p === 0 ? "Données du CM1, premier indice offert, un choix faux écarté"
          : `Réglage de l'enseignant pour cette énigme : données du ${n}`;
        tete.appendChild(b);
      }
      /* Position 0 hors palier Découverte : la même aide renforcée, pour cette énigme seulement */
      if(p === 0 && !window.PALIER.actif()){
        window.PALIER.indiceOffert(carte.querySelector("#indice-" + e.id), "énigme réglée au plus facile");
        window.PALIER.ecarterChoixFaux(carte, e, 0);
        const lecon = carte.querySelector("[data-fiche]"); if(lecon) lecon.classList.add("palier-conseil");
      }
    }
    return r;
  };

  /* Position 3 : défi, chaque indice coûte 2 points de plus (le clic passe d'abord ici, en phase de capture) */
  document.addEventListener("click", ev => {
    const b = ev.target && ev.target.closest && ev.target.closest("button[id^='indice-']");
    const carte = b && b.closest(".enigme-carte");
    if(!b || b.disabled || !carte || carte.dataset.position !== "3") return;
    const avant = ETAT.indicesTotal || 0;
    setTimeout(() => {
      if((ETAT.indicesTotal || 0) > avant){
        ETAT.score = Math.max(0, ETAT.score - SURCOUT_DEFI);
        if(typeof majHUD === "function") majHUD();
        if(typeof sauvegarder === "function") sauvegarder();
      }
    }, 0);
  }, true);

  window.DIFFICULTE = { position, niveauDonnees, aideRenforcee, reglage, reglagesClasse, depart, CLE, SURCOUT_DEFI };
})();
