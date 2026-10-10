/* ============================================================
   LECTURE À VOIX HAUTE DES CONSIGNES (amélioration E5) — tronc commun
   ------------------------------------------------------------
   La voix du navigateur faisait déjà parler les personnages ; elle lit
   maintenant aussi les CONSIGNES des énigmes, pour les lecteurs fragiles.
     • un bouton « 🔊 Écouter la consigne » sur chaque consigne
       (un second clic arrête la lecture) ; le texte lu est surligné ;
     • ⚙️ Réglages → Accessibilité : « Lire automatiquement chaque
       nouvelle consigne » (gardé sur l'appareil, pour tous les jeux ;
       sans effet si l'enseignant a coupé les voix).
   Le titre de l'énigme est lu avant la consigne ; les tableaux sont lus,
   les dessins (SVG) sont ignorés. Rien ne se passe sur un navigateur sans
   synthèse vocale (le bouton n'apparaît pas). Chargé après app.js.
   ============================================================ */
(function(){
  const CLE = "escape_lecture_consignes";
  const API = { lire, arreter, texteDe, reglage, actif: () => "speechSynthesis" in window && typeof SpeechSynthesisUtterance !== "undefined" };
  window.LECTURE_CONSIGNES = API;
  if(!API.actif()) return;

  function reglage(n){
    try{
      if(n) localStorage.setItem(CLE, JSON.stringify(n));
      return Object.assign({auto:false, vitesse:0.9}, JSON.parse(localStorage.getItem(CLE) || "{}"));
    }catch(e){ return {auto:false, vitesse:0.9}; }
  }

  let enCours = null;   // élément .consigne en cours de lecture
  const dejaLues = new Set();   // consignes déjà lues automatiquement

  /** Texte à prononcer : titre de l'énigme + consigne, sans dessins ni émojis */
  function texteDe(el){
    const copie = el.cloneNode(true);
    copie.querySelectorAll("svg, script, style, .btn-lire-consigne, [aria-hidden='true']").forEach(n => n.remove());
    copie.querySelectorAll("td, th").forEach(n => n.append(". "));
    copie.querySelectorAll("p, div, li, tr, br").forEach(n => n.append(" "));
    let t = copie.textContent || "";
    const carte = el.closest(".enigme-carte");
    const titre = carte && carte.querySelector(".enigme-tete h3");
    if(titre) t = titre.textContent + ". " + t;
    return t.replace(/[\u{1F000}-\u{1FFFF}\u{2600}-\u{27BF}\u{FE0F}]/gu, "")
            .replace(/\s*\.\s*(\.\s*)+/g, ". ").replace(/\s+/g, " ").trim();
  }

  function voix(){
    if(typeof NARRATION !== "undefined" && NARRATION.voixFR && NARRATION.voixFR.length) return NARRATION.voixFR[0];
    try{ return speechSynthesis.getVoices().find(v => /^fr/i.test(v.lang)) || null; }catch(e){ return null; }
  }

  function marquer(el, oui){
    if(!el) return;
    el.classList.toggle("lecture-en-cours", oui);
    const b = el.querySelector(".btn-lire-consigne");
    if(b){ b.textContent = oui ? "⏹ Arrêter" : "🔊 Écouter la consigne"; b.setAttribute("aria-pressed", oui ? "true" : "false"); }
  }

  function arreter(){
    try{ speechSynthesis.cancel(); }catch(e){}
    marquer(enCours, false); enCours = null;
  }

  function lire(el){
    if(!el) return null;
    if(enCours === el){ arreter(); return null; }
    arreter();
    const u = new SpeechSynthesisUtterance(texteDe(el));
    u.lang = "fr-FR";
    const v = voix(); if(v) u.voice = v;
    u.rate = reglage().vitesse;
    u.volume = (typeof NARRATION !== "undefined" && NARRATION.volume != null) ? NARRATION.volume : 1;
    const fin = () => { if(enCours === el){ marquer(el, false); enCours = null; } };
    u.onend = fin; u.onerror = fin;
    enCours = el; marquer(el, true);
    speechSynthesis.speak(u);
    return u;
  }

  /* ---- Bouton sur chaque consigne ---- */
  function equiper(el){
    if(el.dataset.lecture) return;
    el.dataset.lecture = "1";
    const b = document.createElement("button");
    b.type = "button"; b.className = "btn-lire-consigne";
    b.textContent = "🔊 Écouter la consigne";
    b.title = "La consigne est lue à voix haute (un second clic arrête)";
    b.setAttribute("aria-pressed", "false");
    b.addEventListener("click", ev => { ev.preventDefault(); ev.stopPropagation(); lire(el); });
    el.insertBefore(b, el.firstChild);
    // Lecture automatique : seulement pour une énigme qui vient d'apparaître, voix non coupées
    // (une fois par consigne : une carte redessinée n'est pas relue)
    const voixCoupees = typeof ETAT !== "undefined" && ETAT.reglages && ETAT.reglages.narrationActive === false;
    const cle = texteDe(el);
    if(reglage().auto && !voixCoupees && el.closest("#ecran-salle") && !dejaLues.has(cle)){
      dejaLues.add(cle); attendrePuisLire(el, 0);
    }
  }
  function attendrePuisLire(el, essais){
    // On laisse d'abord finir un personnage qui parle (dialogue d'entrée de salle)
    setTimeout(() => {
      if(!el.isConnected || enCours) return;
      let parle = false; try{ parle = speechSynthesis.speaking; }catch(e){}
      if(parle && essais < 40) return attendrePuisLire(el, essais + 1);
      lire(el);
    }, essais ? 500 : 400);
  }

  function balayer(racine){
    (racine.querySelectorAll ? racine : document).querySelectorAll(".consigne").forEach(equiper);
    if(enCours && !enCours.isConnected) arreter();   // énigme changée : on se tait
  }

  /* ---- Réglage dans ⚙️ (sous « Lecture facilitée » ou « Animations réduites ») ---- */
  function insererReglage(){
    if(document.getElementById("lecture-consignes-reglages")) return;
    const apres = document.getElementById("lecture-reglages")
      || (document.getElementById("reg-calme") && (document.getElementById("reg-calme").closest(".reglage-ligne") || document.getElementById("reg-calme").parentNode));
    if(!apres) return;
    const r = reglage();
    const d = document.createElement("div");
    d.id = "lecture-consignes-reglages"; d.className = "lecture-reglages";
    d.innerHTML = `<b>🔊 Consignes lues à voix haute</b> <span style="font-size:.8rem;opacity:.75">(gardé sur cet appareil, pour tous les jeux)</span>
      <div class="ligne-lecture"><label><input type="checkbox" id="lc-auto"> Lire automatiquement chaque nouvelle consigne</label></div>
      <div class="ligne-lecture"><label for="lc-vitesse">Vitesse</label>
        <select id="lc-vitesse"><option value="0.75">Lente</option><option value="0.9">Normale</option><option value="1.05">Rapide</option></select></div>
      <div style="font-size:.85rem;opacity:.8">Sans cette case, chaque consigne garde son bouton « 🔊 Écouter la consigne ».</div>`;
    d.querySelector("#lc-auto").checked = !!r.auto;
    d.querySelector("#lc-vitesse").value = String(r.vitesse);
    if(d.querySelector("#lc-vitesse").selectedIndex < 0) d.querySelector("#lc-vitesse").value = "0.9";
    d.addEventListener("change", () => reglage({ auto: d.querySelector("#lc-auto").checked, vitesse: parseFloat(d.querySelector("#lc-vitesse").value) || 0.9 }));
    apres.after(d);
  }

  function styles(){
    if(document.getElementById("style-lecture-consignes")) return;
    const s = document.createElement("style"); s.id = "style-lecture-consignes";
    s.textContent = `
      .btn-lire-consigne{float:right;margin:0 0 6px 10px;font:inherit;font-size:.8rem;font-weight:bold;cursor:pointer;
        padding:4px 10px;border-radius:16px;border:1px solid rgba(0,0,0,.25);background:rgba(255,255,255,.75);color:inherit}
      .btn-lire-consigne:hover,.btn-lire-consigne:focus-visible{background:#fff;outline:2px solid var(--or,#c9a227)}
      .consigne.lecture-en-cours{outline:3px solid var(--or,#c9a227);outline-offset:3px;border-radius:6px}
      @media print{.btn-lire-consigne{display:none}}`;
    document.head.appendChild(s);
  }

  const obs = new MutationObserver(() => { balayer(document); insererReglage(); });
  const demarrer = () => { styles(); balayer(document); obs.observe(document.body, {childList:true, subtree:true}); };
  if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", demarrer); else demarrer();
})();
