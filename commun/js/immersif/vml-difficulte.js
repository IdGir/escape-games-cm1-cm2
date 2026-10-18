/* ============================================================
   VARIANTES IMMERSIVES — DIFFICULTÉ ÉNIGME PAR ÉNIGME (amélioration N20)
   ------------------------------------------------------------
   Les cinq grades (Dessinateur… Humaniste, en interne mousse…second) s'appliquent à toute la partie.
   Mais certaines énigmes sont plus dures ou plus faciles que les autres pour une classe donnée. Un
   réglage de −2 à +2 par énigme DÉCALE son grade : +1 = données, consigne, indices et justification
   du grade au-dessus ; −1 = du grade au-dessous (le grade le plus bas donne l'aide renforcée :
   premier indice offert, un choix faux écarté). Il s'AJOUTE au grade de l'équipe, plafonné aux
   extrémités ; si l'énigme n'existe pas dans le grade visé, le plus proche disponible est joué.
   D'où vient le réglage (le premier trouvé) :
     1. l'adresse : …/?dif=e1-1:-1,e2-3:+1 ;
     2. les réglages de la classe posés par l'enseignant dans prof.html (« 🎚️ Difficulté par énigme » :
        serveur local, sinon cet appareil) — clé « immersif-<jeu> », distincte de la version classique ;
     3. le champ facultatif « difficulte » de l'énigme dans enigmes.json.
   Une pastille 🎚️ prévient l'équipe. Aucun effet sur le barème. Chargé après js/app.js.
   ============================================================ */
(function(){
  const VML = window.VML;
  if(!VML || !VML.ouvrirEnigme || !VML.vueEnigme) return;
  const JEU_ID = "immersif-" + ((VML.JEU && VML.JEU.id) || (window.VML_JEU || {}).id || "jeu");
  const CLE = "escape_difficulte_" + JEU_ID;
  let serveur = null;
  const borne = (n, a, b) => Math.max(a, Math.min(b, n));

  function lireAdresse(){
    const p = new URLSearchParams(location.search).get("dif");
    if(p === null) return null;
    const o = {};
    p.split(",").forEach(x => { const m = x.trim().match(/^([^:]+):\s*([+-]?\d)$/); if(m) o[m[1]] = +m[2]; });
    return o;
  }
  const lireLocal = () => { try{ return JSON.parse(localStorage.getItem(CLE) || "{}") || {}; }catch(e){ return {}; } };
  const reglagesClasse = () => lireAdresse() || serveur || lireLocal();
  function reglage(e){
    const r = reglagesClasse(), v = r[e.id] !== undefined ? +r[e.id] : (+e.difficulte || 0);
    return Number.isFinite(v) ? borne(Math.round(v), -2, 2) : 0;
  }
  /** Le grade réellement joué pour cette énigme (null = celui de l'équipe). */
  function gradeEffectif(e, grade){
    const G = VML.GRADES, i = G.indexOf(grade);
    if(i < 0) return grade;
    let j = borne(i + reglage(e), 0, G.length - 1);
    const dispo = g => !!e[g] && (!e.niveaux || !e.niveaux.length || e.niveaux.includes(g));
    while(j !== i && !dispo(G[j])) j += j > i ? -1 : 1;     // plus proche grade disponible, vers le grade de l'équipe
    return G[j];
  }

  try{
    fetch("/api/difficulte?jeu=" + encodeURIComponent(JEU_ID), { cache: "no-store" })
      .then(r => r.ok ? r.json() : null).then(d => { if(d && d.valeurs && typeof d.valeurs === "object") serveur = d.valeurs; }).catch(() => {});
  }catch(e){}

  const style = document.createElement("style");
  style.textContent = `.badge-difficulte{display:inline-block;margin-left:8px;padding:1px 9px;border-radius:999px;font-size:.78rem;font-weight:bold;vertical-align:middle;background:#ede7f6;color:#4a2c8a;border:1px solid #b39ddb}
    .badge-difficulte.facile{background:#e5f5ea;color:#14532d;border-color:#9bd3a6}`;
  document.head.appendChild(style);

  const ouvrir = VML.ouvrirEnigme;
  VML.ouvrirEnigme = function(e, o){
    const E = VML.ETAT, propre = E.niveau, eff = gradeEffectif(e, propre);
    let res;
    if(eff === propre) res = ouvrir.apply(this, arguments);
    else{
      E.niveau = eff;                                       // le moteur lit le grade de l'équipe : on le décale le temps d'ouvrir le panneau
      try{ res = ouvrir.apply(this, arguments); } finally { E.niveau = propre; }
    }
    try{
      const carte = res && res.carte;
      if(carte){
        carte.dataset.gradeEnigme = eff; carte.dataset.decalage = String(VML.GRADES.indexOf(eff) - VML.GRADES.indexOf(propre));
        const tete = carte.querySelector(".panneau-tete");
        if(tete && eff !== propre && !tete.querySelector(".badge-difficulte")){
          const plus = VML.GRADES.indexOf(eff) > VML.GRADES.indexOf(propre);
          const b = document.createElement("span");
          b.className = "badge-difficulte" + (plus ? "" : " facile");
          b.textContent = plus ? "🎚️ Réglée plus difficile" : (VML.aideRenforcee && VML.aideRenforcee(eff) ? "🎚️ Aide renforcée" : "🎚️ Réglée plus facile");
          b.title = `Réglage de l'enseignant pour cette énigme : jouée au grade ${VML.infoGrade(eff).nom}`;
          tete.appendChild(b);
        }
      }
    }catch(err){ console.warn("Difficulté :", err); }
    return res;
  };

  window.DIFFICULTE_VML = { reglage, gradeEffectif, reglagesClasse, CLE, JEU_ID };
})();
