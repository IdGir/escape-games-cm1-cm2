/* ============================================================
   TRANSITIONS ENTRE SALLES (amélioration B6) — tronc commun
   ------------------------------------------------------------
   Avant : une coupure nette d'une salle à l'autre. Désormais :
     • chaque changement d'écran (accueil → salle, salle → fin…) se
       fait en fondu court (0,45 s) ;
     • l'entrée dans une NOUVELLE salle affiche un court « rideau »
       (numéro et titre de la salle) qui s'efface en 1,2 s, sans
       bloquer le jeu ni le chrono.
   Désactivé automatiquement par le réglage « animations réduites »
   (classe body.calme, ou body.animations-reduites pour Mission
   géographique) et par le réglage du système « réduire les
   animations » (prefers-reduced-motion).
   Chargé APRÈS app.js : il complète afficherSalle() sans la modifier.
   ============================================================ */
(function(){
  const reduit = () => document.body.classList.contains("calme")
    || document.body.classList.contains("animations-reduites")
    || !!(window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches);

  const style = document.createElement("style");
  style.id = "style-transitions";
  style.textContent = `
    .ecran.tr-ecran{animation:tr-fondu .45s ease-out both}
    @keyframes tr-fondu{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
    .rideau-salle{position:fixed;inset:0;z-index:9000;display:flex;flex-direction:column;align-items:center;justify-content:center;
      gap:6px;pointer-events:none;background:rgba(15,20,35,.82);color:#fff;text-align:center;
      animation:tr-rideau 1.2s ease-in-out both}
    .rideau-salle .num{font-size:1rem;letter-spacing:.25em;text-transform:uppercase;opacity:.85}
    .rideau-salle .titre{font-size:clamp(1.4rem,4vw,2.4rem);font-weight:700;max-width:90vw}
    @keyframes tr-rideau{0%{opacity:0}18%{opacity:1}62%{opacity:1}100%{opacity:0}}
    body.calme .rideau-salle, body.animations-reduites .rideau-salle{display:none}
    body.calme .ecran.tr-ecran, body.animations-reduites .ecran.tr-ecran{animation:none}
    @media (prefers-reduced-motion: reduce){ .rideau-salle{display:none} .ecran.tr-ecran{animation:none} }
  `;
  document.head.appendChild(style);

  /* 1. Fondu à chaque écran qui devient actif */
  const obs = new MutationObserver(muts => {
    for(const m of muts){
      const el = m.target;
      if(el.classList.contains("actif") && !/\bactif\b/.test(m.oldValue || "") && !reduit()){
        el.classList.remove("tr-ecran"); void el.offsetWidth; el.classList.add("tr-ecran");
        setTimeout(() => el.classList.remove("tr-ecran"), 600);
      }
    }
  });
  const brancher = () => document.querySelectorAll(".ecran").forEach(e =>
    obs.observe(e, { attributes: true, attributeFilter: ["class"], attributeOldValue: true }));
  if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", brancher); else brancher();

  /* 2. Rideau à l'entrée d'une nouvelle salle (jeux « salles ») */
  function rideau(n){
    const donnees = (typeof DONNEES !== "undefined" && DONNEES && DONNEES.salles) ? DONNEES.salles[n - 1] : null;
    const mot = (typeof JEU !== "undefined" && JEU.motSalle) || "Salle";
    const r = document.createElement("div");
    r.className = "rideau-salle";
    r.setAttribute("aria-hidden", "true");
    r.innerHTML = `<div class="num">${mot} ${n}</div>` + (donnees && donnees.titre ? `<div class="titre"></div>` : "");
    if(donnees && donnees.titre) r.querySelector(".titre").textContent = donnees.titre;
    document.body.appendChild(r);
    setTimeout(() => r.remove(), 1300);
  }
  if(typeof window.afficherSalle === "function"){
    const origine = window.afficherSalle;
    let derniere = null;
    window.afficherSalle = function(n){
      const resultat = origine.apply(this, arguments);
      if(derniere !== null && n !== derniere && !reduit()) rideau(n);
      derniere = n;
      return resultat;
    };
  }
  window.TRANSITIONS = { rideau, reduit };
})();
