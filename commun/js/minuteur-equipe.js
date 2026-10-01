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
   ============================================================ */
(function(){
  if(typeof ETAT === "undefined") return;
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
  if(go) go.addEventListener("click", () => { ETAT.delaiAccordeMin = 0; });

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
