/* ============================================================
   ALERTE DE FIN DE SÉANCE COMMUNE (amélioration N19) — tronc commun
   ------------------------------------------------------------
   Chaque équipe a son propre chrono, qui suit le rythme de sa partie. Mais
   la fin de la SÉANCE de classe est la même pour tout le monde : au lieu de
   l'annoncer à voix haute en interrompant tout le monde, l'enseignant clique
   sur « 🔔 Prévenir : fin dans 5 min » dans prof.html (comme pour un
   indice 💡 ou un délai ⏱️) ; le délai se règle dans la page (1 à 15 min).
   Chez chaque équipe, sans toucher à son chrono ni à son score :
     • un petit bandeau discret en haut à droite de l'écran de jeu
       (« 🔔 Fin de la séance dans 5 min »), qui se met à jour chaque
       minute puis annonce « c'est l'heure de terminer » ;
     • le même court signal sonore que les indices (« page ») ;
     • RIEN n'est interrompu : le bandeau ne prend pas de place dans la page
       et laisse passer les clics (sauf son bouton ✕) ; le signal sonore
       attend que l'équipe ait fini de taper ou de valider (2,5 s sans action).
   Le bandeau survit à un rechargement de la page (sessionStorage).
   La commande arrive par sync.js ({finSeance:{min, id}}) ; chargé après app.js.
   ============================================================ */
(function(){
  if(typeof ETAT === "undefined") return;
  const CLE = "escape_fin_seance";
  const CALME_MS = 2500;          // silence d'action demandé avant le signal sonore
  const ATTENTE_MAX_MS = 15000;   // on ne retarde jamais le signal plus longtemps
  let fin = 0, minuteur = null, derniereAction = 0, jeton = 0;

  const style = document.createElement("style");
  style.textContent = `
    #alerte-seance{position:fixed;top:6px;right:8px;z-index:880;display:none;align-items:center;gap:8px;max-width:min(92vw,360px);
      padding:5px 12px;border-radius:999px;background:rgba(255,248,225,.96);color:#5a3a00;border:2px solid #c9a227;
      font:600 .9rem/1.25 system-ui,sans-serif;box-shadow:0 3px 10px rgba(0,0,0,.2);pointer-events:none}
    #alerte-seance.visible{display:flex}
    #alerte-seance.urgent{background:rgba(255,235,230,.97);color:#7a1d10;border-color:#b3261e}
    #alerte-seance button{pointer-events:auto;border:0;background:transparent;color:inherit;font:inherit;font-size:1rem;cursor:pointer;padding:0 2px;opacity:.7}
    body.calme #alerte-seance{box-shadow:none}`;
  document.head.appendChild(style);

  function barre(){
    let b = document.getElementById("alerte-seance");
    if(!b){
      b = document.createElement("div");
      b.id = "alerte-seance"; b.setAttribute("role", "status"); b.setAttribute("aria-live", "polite");
      b.innerHTML = `<span class="texte"></span><button type="button" aria-label="Masquer l'alerte de fin de séance" title="Masquer">✕</button>`;
      b.querySelector("button").addEventListener("click", masquer);
      document.body.appendChild(b);
    }
    return b;
  }
  function texte(){
    const reste = fin - Date.now();
    if(reste <= 0) return { t: "🔔 C'est l'heure de terminer : finissez l'énigme en cours.", urgent: true };
    const min = Math.ceil(reste / 60000);
    return min <= 1 ? { t: "🔔 Fin de la séance dans moins d'une minute.", urgent: true }
                    : { t: `🔔 Fin de la séance dans ${min} min.`, urgent: false };
  }
  function afficher(){
    if(!fin || ETAT.fini){ masquer(); return; }
    const b = barre(), x = texte();
    b.querySelector(".texte").textContent = x.t;
    b.classList.toggle("urgent", x.urgent);
    b.classList.add("visible");
  }
  function masquer(){
    const b = document.getElementById("alerte-seance"); if(b) b.classList.remove("visible");
    if(minuteur){ clearInterval(minuteur); minuteur = null; }
    try{ sessionStorage.removeItem(CLE); }catch(e){}
    fin = 0; jeton++;                 // un signal sonore en attente est annulé
  }

  /* Le signal sonore attend que l'équipe ait fini de taper ou de valider */
  ["input", "keydown", "pointerdown"].forEach(t => document.addEventListener(t, () => { derniereAction = Date.now(); }, true));
  function signalSonore(depuis, moi){
    if(moi !== jeton) return;
    const occupe = Date.now() - derniereAction < CALME_MS;
    if(occupe && Date.now() - depuis < ATTENTE_MAX_MS){ setTimeout(() => signalSonore(depuis, moi), 500); return; }
    if(typeof son === "function" && !(ETAT.reglages && ETAT.reglages.sonsActifs === false)) son("page");
  }

  /** Prévenir l'équipe : fin de la séance dans « min » minutes (appelé par la commande de prof.html). */
  function alerteFinSeance(min){
    min = Math.max(1, Math.min(60, Math.round(+min || 5)));
    if(ETAT.fini) return false;
    fin = Date.now() + min * 60000;
    try{ sessionStorage.setItem(CLE, String(fin)); }catch(e){}
    afficher();
    if(minuteur) clearInterval(minuteur);
    minuteur = setInterval(afficher, 15000);
    signalSonore(Date.now(), ++jeton);
    return true;
  }
  window.alerteFinSeance = alerteFinSeance;

  /* Rechargement de la page pendant l'alerte : le bandeau revient */
  try{
    const f = +sessionStorage.getItem(CLE);
    if(f && f > Date.now() - 600000 && !new URLSearchParams(location.search).get("salle")){
      fin = f; minuteur = setInterval(afficher, 15000);
      const attendre = setInterval(() => { if(ETAT.debut){ clearInterval(attendre); afficher(); } }, 500);
      setTimeout(() => clearInterval(attendre), 60000);
    }
  }catch(e){}

  /* Fin de partie : l'alerte disparaît */
  if(typeof window.finDuJeu === "function"){
    const origine = window.finDuJeu;
    window.finDuJeu = function(){ const r = origine.apply(this, arguments); masquer(); return r; };
  }
  window.ALERTE_SEANCE = { alerteFinSeance, masquer, texte, CALME_MS };
})();
