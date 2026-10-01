/* ============================================================
   PALIER « DÉCOUVERTE » (amélioration E2) — tronc commun
   ------------------------------------------------------------
   Un troisième choix à côté de CM1 et CM2, pour les classes à triple
   niveau ou les élèves très en difficulté. Même mécanisme de bascule :
   le palier Découverte joue les énigmes du CM1 (ETAT.niveau = "CM1"),
   avec une ASSISTANCE RENFORCÉE :
     • le premier indice de chaque énigme est affiché d'emblée, sans
       retirer de points ;
     • dans les QCM à trois choix ou plus, un choix faux est écarté
       (grisé, impossible à sélectionner) ;
     • le bouton de leçon de l'énigme est mis en évidence ;
     • au coffre final, chaque case indique la première lettre et le
       nombre de lettres du mot à retrouver.
   Les règles du jeu ne changent pas : en cas d'erreur, le jeu dit
   toujours COMBIEN de réponses sont justes, jamais lesquelles.
   Adresse de vérification : index.html?salle=2&niveau=CM1&palier=decouverte
   Chargé après app.js, sans modifier app.js.
   ============================================================ */
(function(){
  if(typeof ETAT === "undefined" || !document.querySelector(".choix-niveau")) return;
  const DEC = "decouverte";
  const actif = () => ETAT.palier === DEC;

  const style = document.createElement("style");
  style.textContent = `
    .opt-niveau[data-palier="decouverte"] .gros{color:#15803d}
    .qcm-option.ecartee{opacity:.35;text-decoration:line-through;pointer-events:none;cursor:not-allowed}
    .palier-conseil{outline:3px solid #15803d;outline-offset:2px;animation:palier-pulse 1.6s ease-in-out 3}
    @keyframes palier-pulse{50%{outline-color:rgba(21,128,61,.25)}}
    body.calme .palier-conseil{animation:none}
    .bandeau-palier{margin:8px auto;max-width:640px;padding:6px 12px;border-radius:10px;background:#e5f5ea;color:#14532d;
      font-size:.9rem;text-align:center}
  `;
  document.head.appendChild(style);

  /* ---- 1. Le troisième choix, sur l'écran d'accueil ---- */
  const choix = document.querySelector(".choix-niveau");
  const opt = document.createElement("div");
  opt.className = "opt-niveau";
  opt.dataset.niveau = "CM1";
  opt.dataset.palier = DEC;
  opt.innerHTML = `<div class="gros">Découverte</div>
    <div class="petit">Énigmes du CM1 avec une aide renforcée : premier indice offert, un choix faux écarté,
      première lettre des mots au coffre. Pour les classes à triple niveau ou les élèves en difficulté.</div>`;
  choix.appendChild(opt);
  const apercu = () => {
    const el = document.getElementById("apercu-niveau");
    if(el && actif() && !/Découverte/.test(el.textContent)) el.textContent = "Palier Découverte · " + el.textContent;
  };
  choix.querySelectorAll(".opt-niveau").forEach(o => o.addEventListener("click", () => {
    ETAT.palier = o.dataset.palier || null;
    setTimeout(apercu, 0);
  }));
  // Au démarrage, le palier suit le choix affiché (et non une partie précédente)
  const go = document.getElementById("btn-demarrer");
  if(go) go.addEventListener("click", () => {
    const c = choix.querySelector(".opt-niveau.choisi");
    ETAT.palier = c && c.dataset.palier || null;
  });
  // Mode vérification (&palier=decouverte) ou reprise d'une partie en palier Découverte
  const p = new URLSearchParams(location.search);
  if(p.get("palier") === DEC) ETAT.palier = DEC;
  else if(!p.get("salle")){
    try{
      const s = JSON.parse(localStorage.getItem(typeof CLE_SAUVEGARDE !== "undefined" ? CLE_SAUVEGARDE : "") || "null");
      if(s && s.palier === DEC && !s.fini) ETAT.palier = DEC;
    }catch(e){}
  }

  /* Indice offert : on « clique » le bouton puis on rend les points retirés */
  function indiceOffert(btn){
    if(!btn || btn.disabled) return;
    const avant = { score: ETAT.score, s: ETAT.indicesSalle, t: ETAT.indicesTotal, u: ETAT.indicesUtilises };
    const deja = new Set(document.querySelectorAll(".feedback.indice"));
    btn.click();
    ETAT.score = avant.score;
    if(avant.s !== undefined) ETAT.indicesSalle = avant.s;
    if(avant.t !== undefined) ETAT.indicesTotal = avant.t;
    if(avant.u !== undefined) ETAT.indicesUtilises = avant.u;
    if(typeof majHUD === "function") majHUD();
    const bulle = [...document.querySelectorAll(".feedback.indice")].find(b => !deja.has(b));
    if(bulle && !/offert/.test(bulle.innerHTML)) bulle.insertAdjacentHTML("beforeend", ` <small>(indice offert : palier Découverte)</small>`);
  }

  /* ---- 2. Énigmes du moteur commun ---- */
  if(typeof window.activerEnigme === "function"){
    const origine = window.activerEnigme;
    window.activerEnigme = function(e, onReussite){
      const r = origine.apply(this, arguments);
      if(actif()){
        const carte = document.getElementById("enigme-" + e.id);
        if(carte){
          indiceOffert(carte.querySelector("#indice-" + e.id));
          if(e.type === "qcm" && typeof donneesNiveau === "function"){
            const d = donneesNiveau(e);
            (d.questions || []).forEach((q, i) => {
              if(!q.options || q.options.length < 3) return;
              const faux = q.options.map((_, j) => j).filter(j => j !== q.bonne);
              const j = faux[(i + e.id.length) % faux.length];
              const o = carte.querySelector(`.qcm-question[data-i="${i}"] .qcm-option[data-j="${j}"]`);
              if(o){ o.classList.add("ecartee"); o.setAttribute("aria-disabled", "true"); o.title = "Choix écarté (palier Découverte)"; }
            });
          }
          const lecon = carte.querySelector("[data-fiche]");
          if(lecon) lecon.classList.add("palier-conseil");
        }
      }
      return r;
    };
  }

  /* ---- 3. Jeux à moteur propre (Déclaration, Tour du monde) ---- */
  if(typeof window.activerBoutonIndice === "function"){
    const origine = window.activerBoutonIndice;
    window.activerBoutonIndice = function(){
      const r = origine.apply(this, arguments);
      if(actif()) indiceOffert(document.getElementById("btn-indice"));
      return r;
    };
  }

  /* ---- 4. Coffre final : première lettre et longueur de chaque mot ---- */
  if(typeof window.afficherCoffre === "function"){
    const origine = window.afficherCoffre;
    window.afficherCoffre = function(){
      const r = origine.apply(this, arguments);
      if(actif() && typeof DONNEES !== "undefined" && DONNEES.salles){
        const mots = DONNEES.salles.filter(s => s.motCle || s.fragment).map(s => s.motCle || s.fragment);
        mots.forEach((m, i) => {
          const c = document.getElementById("coffre-" + i);
          if(c){ const n = [...String(m).replace(/\s/g, "")].length; c.placeholder = String(m)[0] + " " + "_ ".repeat(Math.max(0, n - 1)).trim() + ` (${n} lettres)`; }
        });
      }
      return r;
    };
  }

  /* ---- 5. Écran de fin : le palier est rappelé ---- */
  if(typeof window.finDuJeu === "function"){
    const origine = window.finDuJeu;
    window.finDuJeu = function(){
      const r = origine.apply(this, arguments);
      const c = document.getElementById("fin-contenu");
      if(actif() && c && !c.querySelector(".bandeau-palier"))
        c.insertAdjacentHTML("afterbegin", `<div class="bandeau-palier">🌱 Partie jouée au <b>palier Découverte</b> : énigmes du CM1, aide renforcée.</div>`);
      return r;
    };
  }
  window.PALIER = { actif, DEC };
})();
