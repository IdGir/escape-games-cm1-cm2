/* ============================================================
   BANQUE D'ÉNIGMES À VARIANTES (amélioration D3) — tronc commun
   ------------------------------------------------------------
   Une énigme de enigmes.json peut proposer des VARIANTES : mêmes
   type, compétence et difficulté, autres données (nombres, exemples,
   documents). Format :
       { "id":"1-3", "type":"code", …énigme d'origine…,
         "variantes":[ { "cm1":{…}, "cm2":{…}, "indices":{…}, "correction":"…" },
                       { … } ] }
   Chaque variante remplace les champs qu'elle contient (les autres
   restent ceux de l'énigme d'origine).
   Quelle version est jouée ? (série 0 = l'énigme d'origine)
     • « automatique » (par défaut) : la série change à chaque ANNÉE
       SCOLAIRE (septembre → août) : même jeu pour toute la classe
       pendant l'année, autres énigmes l'année suivante (frères et
       sœurs, redoublants). 2026-2027 : énigmes d'origine ; 2027-2028 :
       série 1 ; 2028-2029 : série 2…, puis retour à l'origine.
     • une série précise (1, 2…), choisie dans ⚙️ Réglages, pour
       rejouer le jeu avec d'autres énigmes la même année ;
     • « d'origine » : jamais de variante.
   Le choix est le même à la reprise d'une partie, dans les impressions
   (fiches, corrigés) et sur tous les postes réglés de la même façon.
   Adresse de vérification : …?salle=1&niveau=CM1&serie=1
   Chargé après app.js (jeux à moteur commun), sans modifier app.js.
   ============================================================ */
(function(){
  if(typeof window.chargerDonnees !== "function" || typeof JEU === "undefined") return;
  const CLE = "escape_variantes_" + JEU.id;
  const lire = () => { try { return JSON.parse(localStorage.getItem(CLE) || "null") || { mode: "auto" }; } catch(e) { return { mode: "auto" }; } };
  const ecrire = r => { try { localStorage.setItem(CLE, JSON.stringify(r)); } catch(e) {} };
  const ANNEE_DEPART = 2026;   // 2026-2027 : énigmes d'origine ; puis série 1, 2… chaque année
  const anneeScolaire = (d = new Date()) => d.getMonth() >= 7 ? d.getFullYear() : d.getFullYear() - 1;   // à partir d'août

  /** Série demandée : paramètre d'adresse ?serie=N, sinon réglage, sinon année scolaire. */
  function serieDemandee(){
    const p = new URLSearchParams(location.search).get("serie");
    if(p !== null && /^\d+$/.test(p)) return { mode: "serie", serie: +p };
    return lire();
  }
  /** Variante retenue pour une énigme qui en a n : 0 = d'origine, 1..n = variantes. */
  function choix(e, r){
    const n = (e.variantes || []).length;
    if(!n || r.mode === "origine") return 0;
    if(r.mode === "serie") return Math.min(+r.serie || 0, n);
    return ((anneeScolaire() - ANNEE_DEPART) % (n + 1) + (n + 1)) % (n + 1);
  }
  function appliquer(enigmes){
    const r = serieDemandee(); let nb = 0;
    (enigmes && enigmes.salles || []).forEach(s => (s.enigmes || []).forEach(e => {
      if(!e.variantes || e._serie !== undefined) return;
      const k = choix(e, r);
      e._serie = k;
      if(k > 0){ Object.assign(e, e.variantes[k - 1]); nb++; }
    }));
    window.VARIANTES_APPLIQUEES = { mode: r.mode, serie: r.serie, nb };
    return nb;
  }

  const origine = window.chargerDonnees;
  window.chargerDonnees = async function(){
    const res = await origine.apply(this, arguments);
    /* Aperçu depuis l'éditeur d'énigmes (editeur.html, D4) : ?apercu=1 joue la version
       en cours d'édition, gardée dans le navigateur, sans rien enregistrer. */
    if(new URLSearchParams(location.search).get("apercu") === "1"){
      try{
        const a = JSON.parse(localStorage.getItem("escape_apercu_enigmes_" + JEU.id) || "null");
        if(a && Array.isArray(a.salles)){ ENIGMES = a; window.APERCU_EDITEUR = true;
          setTimeout(() => { if(typeof toast === "function") toast("✏️ Aperçu de l'éditeur d'énigmes : rien n'est enregistré"); }, 400); }
      }catch(e){}
    }
    if(typeof ENIGMES !== "undefined" && ENIGMES) appliquer(ENIGMES);
    return res;
  };

  /* Réglage enseignant dans ⚙️ Réglages (si le jeu a au moins une variante) */
  function nbMax(){
    let m = 0;
    if(typeof ENIGMES !== "undefined" && ENIGMES) ENIGMES.salles.forEach(s => (s.enigmes || []).forEach(e => { m = Math.max(m, (e.variantes || []).length); }));
    return m;
  }
  function bloc(){
    const r = lire(), m = nbMax();
    const g = document.createElement("div");
    g.className = "reglages-group"; g.id = "reglages-variantes";
    const opt = (v, t) => `<option value="${v}" ${((r.mode === "serie" ? "s" + r.serie : r.mode) === v) ? "selected" : ""}>${t}</option>`;
    g.innerHTML = `<h4>🎲 Banque d'énigmes</h4>
      <div class="reglage-ligne"><div class="libelle"><b>Série d'énigmes jouée</b><br>
        <span style="font-size:.8rem;opacity:.7">${m} variante(s) au plus par énigme. « Automatique » : la série change à chaque année scolaire.
        Gardé sur cet appareil ; à régler de la même façon sur tous les postes. Recharger la page après un changement.</span></div>
        <div class="controle"><select id="var-serie">
          ${opt("auto", "Automatique (selon l'année)")}${opt("origine", "Énigmes d'origine")}
          ${Array.from({ length: m }, (_, i) => opt("s" + (i + 1), "Série " + (i + 1))).join("")}
        </select></div></div>`;
    g.querySelector("#var-serie").addEventListener("change", ev => {
      const v = ev.target.value;
      ecrire(v[0] === "s" ? { mode: "serie", serie: +v.slice(1) } : { mode: v });
    });
    return g;
  }
  const obs = new MutationObserver(() => {
    const calme = document.getElementById("reg-calme");
    if(calme && !document.getElementById("reglages-variantes") && nbMax() > 0){
      const grp = calme.closest(".reglages-group"); if(grp) grp.parentNode.appendChild(bloc());
    }
  });
  const demarrer = () => obs.observe(document.body, { childList: true, subtree: true });
  if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", demarrer); else demarrer();
  window.VARIANTES = { lire, ecrire, choix, appliquer, anneeScolaire, ANNEE_DEPART };
})();
