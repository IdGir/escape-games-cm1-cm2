/* ============================================================
   VARIANTES IMMERSIVES — TROPHÉES D'UN JEU À L'AUTRE (amélioration N1, portée aux variantes)
   ------------------------------------------------------------
   Même règles et même bloc que commun/js/trophees.js (commun/donnees/trophees.js, historique
   « escape_resultats »), à l'ÉCRAN DU COFFRE OUVERT : un jeu n'est « terminé » que coffre ouvert (une
   escale finie ne compte pas). Les nouveaux trophées sont annoncés, avec le total et un lien vers
   trophees.html ; la mascotte (mascotte.js) les annonce à voix haute. Rien en mode vérification.
   Chargé après js/app.js, js/journal.js et commun/donnees/trophees.js.
   ============================================================ */
(function(){
  const VML = window.VML;
  if(!VML || !VML.ouvrirCoffre || typeof TROPHEES === "undefined") return;
  const cat = typeof CATALOGUE !== "undefined" ? CATALOGUE : null;
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const historique = () => { try{ return JSON.parse(localStorage.getItem("escape_resultats") || "[]"); }catch(e){ return []; } };

  function bloc(){
    const nom = VML.ETAT.equipe, hist = historique(), cr = VML.compteRendu();
    const memePartie = p => p.jeu === cr.jeu && TROPHEES.norm(p.eleve) === TROPHEES.norm(cr.eleve) && (p.partie || p.date) === (cr.partie || cr.date);
    const avant = TROPHEES.obtenus(nom, hist.filter(p => !memePartie(p)), cat).map(t => t.id);
    const apres = TROPHEES.obtenus(nom, hist, cat);
    const nouveaux = apres.filter(t => !avant.includes(t.id));
    const d = document.createElement("section");
    d.id = "trophees-fin"; d.className = "trophees-fin";
    d.innerHTML = `<h2>🏅 Trophées de ${esc(nom)}</h2>
      ${nouveaux.length ? `<p class="tr-annonce">${nouveaux.length > 1 ? "Nouveaux trophées" : "Nouveau trophée"} !</p>
        <div class="tr-liste">${nouveaux.map(t => `<div class="tr nouveau"><span class="tr-icone">${t.icone}</span><b>${esc(t.titre)}</b><small>${esc(t.regle)}</small></div>`).join("")}</div>`
        : `<p class="tr-annonce discret">Pas de nouveau trophée cette fois-ci.</p>`}
      <p class="tr-total">${apres.length} trophée${apres.length > 1 ? "s" : ""} sur ${TROPHEES.LISTE.length}, gagnés en jouant aux différents escape games sous le nom « ${esc(nom)} ».
        <a href="../../trophees.html?nom=${encodeURIComponent(nom)}">Voir la vitrine des trophées →</a></p>`;
    return d;
  }
  function styles(){
    if(document.getElementById("style-trophees")) return;
    const s = document.createElement("style"); s.id = "style-trophees";
    s.textContent = `.trophees-fin{margin:22px 0 8px;padding:14px;border-top:2px dotted #c9a227;text-align:center;background:rgba(255,248,225,.9);color:#2b1d10;border-radius:12px}
      .tr-annonce{font-weight:bold;font-size:1.1rem}.tr-annonce.discret{font-weight:normal;opacity:.8;font-size:1rem}
      .tr-liste{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin:8px 0}
      .tr{display:flex;flex-direction:column;align-items:center;gap:2px;width:150px;padding:10px;border-radius:12px;background:#fff8e1;border:2px solid #c9a227}
      .tr .tr-icone{font-size:2rem}.tr small{opacity:.8;font-size:.78rem}
      .tr.nouveau{animation:tr-apparait .6s ease-out both}
      @keyframes tr-apparait{from{transform:scale(.6);opacity:0}to{transform:none;opacity:1}}
      body.anim-reduites .tr.nouveau{animation:none}
      .tr-total{font-size:.9rem;opacity:.9}.tr-total a{color:#1d3a8a}`;
    document.head.appendChild(s);
  }

  const ouvrirCoffre = VML.ouvrirCoffre;
  VML.ouvrirCoffre = function(){
    const r = ouvrirCoffre.apply(this, arguments);
    const E = VML.ETAT, c = document.getElementById("fin-contenu");
    if(E && E.coffreOuvert && !VML.modeVerif && E.equipe && c && !document.getElementById("trophees-fin")){
      styles();
      const zone = c.querySelector(".coffre");
      const b = bloc();
      if(zone) zone.after(b); else c.appendChild(b);
      if(window.MASCOTTE && window.MASCOTTE.annoncerTrophees) window.MASCOTTE.annoncerTrophees();
    }
    return r;
  };
})();
