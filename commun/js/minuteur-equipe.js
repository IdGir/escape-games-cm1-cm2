/* ============================================================
   MINUTEUR ADAPTATIF PAR ÉQUIPE (amélioration E6) — tronc commun
   ------------------------------------------------------------
   Le bonus de rapidité d'une salle est accordé si l'équipe la boucle
   en moins de 8 min (CM1) ou 10 min (CM2). Depuis le tableau de bord
   prof.html (bouton ⏱️ +), l'enseignant peut accorder à UNE équipe
   précise quelques minutes de plus : le chrono de la salle en cours
   est décalé d'autant, l'équipe garde donc son bonus, et l'alerte de
   fin de séance est repoussée. Le chrono total affiché reste vrai.
   La commande arrive par sync.js ({delaiMin, id}) ; le délai accordé
   est renvoyé au tableau de bord et noté au bilan.
   Chargé après app.js, sans modifier app.js.

   TEMPS MAJORÉ INDIVIDUALISÉ (amélioration N26) — PAP / PPS
   ------------------------------------------------------------
   Un élève bénéficiaire d'un aménagement de temps (tiers-temps…) joue à son rythme sans que
   rien ne le signale à ses camarades. Réglage unique, dans le passeport (passeport.html,
   « ⏱️ Temps majoré ») : un COEFFICIENT par élève (aucun par défaut : 1 ; 1,25 · 1,33 · 1,5 · 2)
   et, au besoin, la COMPOSITION de chaque équipe. Quand une équipe démarre, le coefficient
   retenu est le plus grand de ses membres (un élève qui joue seul, mode individuel D2, est
   reconnu par son prénom). Il s'applique à l'allure attendue d'une salle : le bonus de rapidité
   est jugé sur le temps réel divisé par le coefficient (une salle bouclée en 12 min avec ×1,5
   compte comme 8 min), et l'alerte de durée de séance est repoussée d'autant. Le chrono total
   affiché et le temps réel des salles (bilan, compte-rendu) restent vrais.
   DISCRÉTION : aucun message, aucune icône, aucune mention dans le HUD ni à l'écran de fin ;
   la trace n'est lisible que dans le passeport de l'enseignant. Les données vivent sous leur
   propre clé « escape_amenagements » : elles ne sont PAS dans les exports « Ma progression »
   (N16), les comptes-rendus, ni le serveur de classe.
   Fonctions (sans dépendre d'un jeu) : AMENAGEMENTS.lire/ecrire/coefPour/tracer.
   ============================================================ */
(function(){
  /* ---------- Aménagements : lecture, composition des équipes, coefficient ---------- */
  const CLE_AMENAGEMENTS = "escape_amenagements";
  const COEFFICIENTS = [1, 1.25, 1.33, 1.5, 2];
  const norm = s => String(s == null ? "" : s).normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/\s+/g, " ").trim().toLowerCase();
  const vide = () => ({ coefs: {}, equipes: {}, traces: [] });
  const stockage = () => { try{ return window.localStorage; }catch(e){ return null; } };
  function lire(stock){
    stock = stock || stockage();
    let d = null;
    try{ d = JSON.parse(stock.getItem(CLE_AMENAGEMENTS) || "null"); }catch(e){}
    d = d && typeof d === "object" ? d : {};
    return { coefs: d.coefs && typeof d.coefs === "object" ? d.coefs : {}, equipes: d.equipes && typeof d.equipes === "object" ? d.equipes : {},
             traces: Array.isArray(d.traces) ? d.traces : [] };
  }
  function ecrire(d, stock){ stock = stock || stockage(); try{ stock.setItem(CLE_AMENAGEMENTS, JSON.stringify(d)); return true; }catch(e){ return false; } }
  const coefDe = (d, eleve) => { const k = Object.keys(d.coefs).find(x => norm(x) === norm(eleve)); const c = k ? +d.coefs[k] : 1; return c > 1 && c <= 3 ? c : 1; };
  /** Coefficient d'une équipe (ou d'un élève qui joue seul) : le plus grand de ses membres, 1 par défaut. */
  function coefPour(nom, d){
    d = d || lire();
    const cle = Object.keys(d.equipes).find(x => norm(x) === norm(nom));
    if(cle) return Math.max(1, ...(d.equipes[cle] || []).map(e => coefDe(d, e)));
    return coefDe(d, nom);
  }
  /** Garde une trace (lisible dans le passeport seulement) : jeu, équipe, jour, coefficient. 200 traces au plus. */
  function tracer(jeu, equipe, coef, d, stock){
    d = d || lire(stock);
    d.traces.push({ jeu, equipe, coef, date: new Date().toISOString().slice(0, 16) });
    d.traces = d.traces.slice(-200);
    ecrire(d, stock);
    return d;
  }
  const AMENAGEMENTS = { CLE: CLE_AMENAGEMENTS, COEFFICIENTS, lire, ecrire, coefPour, coefDe, tracer, norm, vide };
  if(typeof window !== "undefined") window.AMENAGEMENTS = AMENAGEMENTS;
  if(typeof module !== "undefined") module.exports = AMENAGEMENTS;

  if(typeof ETAT === "undefined") return;

  /* ---------- N26 : application dans le jeu (aucun affichage) ---------- */
  function appliquerMajoration(){
    if(!ETAT.reglages) return;
    // « durée de séance » réglée avant toute majoration (gardée avec la partie : pas de double majoration après un rechargement)
    const dureeOrigine = ETAT.reglages.dureeMinBase || (ETAT.reglages.dureeMinBase = ETAT.reglages.dureeMin || 60);
    let coef = 1;
    try{ coef = coefPour(ETAT.equipe); }catch(e){}
    ETAT.coefTemps = coef > 1 ? coef : 0;
    ETAT.reglages.dureeMin = Math.round(dureeOrigine * (coef > 1 ? coef : 1));
    if(coef > 1){
      const jeu = (typeof JEU !== "undefined" && JEU.id) || (location.pathname.split("/").filter(Boolean).slice(-2, -1)[0]) || "";
      tracer(jeu, ETAT.equipe, coef);
    }
  }
  /* Le bonus de rapidité se juge sur le temps réel divisé par le coefficient : pendant validerSalle, on recule
     l'heure de début de salle ; le temps réel est rétabli juste après (bilan et compte-rendu restent vrais). */
  if(typeof window.validerSalle === "function"){
    const valider = window.validerSalle;
    window.validerSalle = function(n){
      const k = ETAT.coefTemps;
      if(!(k > 1) || !ETAT.salleDebut) return valider.apply(this, arguments);
      const debut = ETAT.salleDebut, maintenant = Date.now(), reel = maintenant - debut;
      ETAT.salleDebut = maintenant - reel / k;
      const dejaVue = ETAT.tempsParSalle && ETAT.tempsParSalle[n] !== undefined;
      try{ return valider.apply(this, arguments); }
      finally{
        ETAT.salleDebut = debut;
        if(ETAT.tempsParSalle && !dejaVue && ETAT.tempsParSalle[n] !== undefined) ETAT.tempsParSalle[n] = reel;
      }
    };
  }
  function accorderDelai(min){
    min = Math.max(1, Math.min(30, Math.round(+min || 0)));
    if(!min || ETAT.fini) return false;
    if(ETAT.salleDebut) ETAT.salleDebut += min * 60000;
    ETAT.delaiAccordeMin = (ETAT.delaiAccordeMin || 0) + min;
    if(ETAT.reglages) ETAT.reglages.dureeMin = (ETAT.reglages.dureeMin || 60) + min;
    if(typeof majHUD === "function") majHUD();
    if(typeof sauvegarder === "function") sauvegarder();
    if(typeof toast === "function") toast(`⏱️ L'enseignant vous accorde ${min} min de plus : le bonus de rapidité est préservé.`);
    const h = document.getElementById("hud-temps");
    if(h){
      let b = document.getElementById("hud-delai");
      if(!b){ b = document.createElement("span"); b.id = "hud-delai"; b.style.cssText = "margin-left:6px;font-size:.8em;opacity:.85"; h.appendChild(b); }
      b.textContent = `(+${ETAT.delaiAccordeMin} min)`;
      b.title = "Temps supplémentaire accordé par l'enseignant";
    }
    return true;
  }
  window.accorderDelai = accorderDelai;

  /* Le délai accordé est remis à zéro au début d'une nouvelle partie */
  const go = document.getElementById("btn-demarrer");
  if(go) go.addEventListener("click", () => { ETAT.delaiAccordeMin = 0; appliquerMajoration(); });

  /* Bilan de fin : le délai est rappelé (transparence avec l'équipe) */
  if(typeof window.finDuJeu === "function"){
    const origine = window.finDuJeu;
    window.finDuJeu = function(){
      const r = origine.apply(this, arguments);
      const c = document.getElementById("fin-contenu");
      if(c && ETAT.delaiAccordeMin && !c.querySelector(".note-delai"))
        c.insertAdjacentHTML("beforeend", `<p class="note-delai" style="text-align:center;opacity:.8;font-size:.9rem">⏱️ Temps supplémentaire accordé par l'enseignant : ${ETAT.delaiAccordeMin} min.</p>`);
      return r;
    };
  }
})();
