/* ============================================================
   TROPHÉES INTER-JEUX À L'ÉCRAN DE FIN (amélioration N1) — tronc commun
   ------------------------------------------------------------
   Les badges de chaque jeu restent propres au jeu. Les TROPHÉES se
   cumulent d'un jeu à l'autre (règles : commun/donnees/trophees.js),
   pour un même nom d'équipe ou d'élève sur cet appareil.
   À la fin de la partie (après l'enregistrement dans l'historique par
   compte-rendu.js) : les nouveaux trophées sont annoncés, avec le total
   et un lien vers la vitrine trophees.html.
   Rien en mode vérification. Chargé après compte-rendu.js.
   ============================================================ */
(function(){
  if(typeof ETAT === "undefined" || typeof TROPHEES === "undefined" || typeof COMPTE_RENDU === "undefined") return;
  const cat = typeof CATALOGUE !== "undefined" ? CATALOGUE : null;
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  function bloc(){
    const nom = ETAT.equipe;
    const hist = COMPTE_RENDU.historique();
    const cr = COMPTE_RENDU.construire();
    const avant = TROPHEES.obtenus(nom, hist.filter(p => !(p.jeu === cr.jeu && TROPHEES.norm(p.eleve) === TROPHEES.norm(cr.eleve) && (p.partie || p.date) === (cr.partie || cr.date))), cat).map(t => t.id);
    const apres = TROPHEES.obtenus(nom, hist, cat);
    const nouveaux = apres.filter(t => !avant.includes(t.id));
    const d = document.createElement("section");
    d.id = "trophees-fin"; d.className = "trophees-fin";
    d.innerHTML = `<h2>🏅 Trophées de ${esc(nom)}</h2>
      ${nouveaux.length ? `<p class="tr-annonce">${nouveaux.length > 1 ? "Nouveaux trophées" : "Nouveau trophée"} !</p>
        <div class="tr-liste">${nouveaux.map(t => `<div class="tr nouveau"><span class="tr-icone">${t.icone}</span><b>${esc(t.titre)}</b><small>${esc(t.regle)}</small></div>`).join("")}</div>`
        : `<p class="tr-annonce discret">Pas de nouveau trophée cette fois-ci.</p>`}
      <p class="tr-total">${apres.length} trophée${apres.length > 1 ? "s" : ""} sur ${TROPHEES.LISTE.length}, gagnés en jouant aux différents escape games sous le nom « ${esc(nom)} ».
        <a href="../trophees.html?nom=${encodeURIComponent(nom)}">Voir la vitrine des trophées →</a></p>`;
    return d;
  }

  function styles(){
    if(document.getElementById("style-trophees")) return;
    const s = document.createElement("style"); s.id = "style-trophees";
    s.textContent = `
      .trophees-fin{margin:22px 0 8px;padding-top:14px;border-top:2px dotted var(--parchemin-ombre,#e0cfa6);text-align:center}
      .tr-annonce{font-weight:bold;font-size:1.1rem}.tr-annonce.discret{font-weight:normal;opacity:.8;font-size:1rem}
      .tr-liste{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin:8px 0}
      .tr{display:flex;flex-direction:column;align-items:center;gap:2px;width:150px;padding:10px;border-radius:12px;background:#fff8e1;border:2px solid var(--or,#c9a227)}
      .tr .tr-icone{font-size:2rem}.tr small{opacity:.8;font-size:.78rem}
      .tr.nouveau{animation:tr-apparait .6s ease-out both}
      @keyframes tr-apparait{from{transform:scale(.6);opacity:0}to{transform:none;opacity:1}}
      body.calme .tr.nouveau{animation:none}
      .tr-total{font-size:.9rem;opacity:.9}`;
    document.head.appendChild(s);
  }

  if(typeof window.finDuJeu === "function"){
    const origine = window.finDuJeu;
    window.finDuJeu = function(){
      const r = origine.apply(this, arguments);
      if(new URLSearchParams(location.search).get("salle") || !ETAT.equipe) return r;   // mode vérification
      const c = document.getElementById("fin-contenu");
      if(c && !document.getElementById("trophees-fin")){
        styles();
        const ae = document.getElementById("auto-evaluation");
        const rej = c.querySelector("#btn-rejouer"), avant = ae || (rej && rej.closest(".boutons"));
        if(avant && avant.parentNode) avant.parentNode.insertBefore(bloc(), avant); else c.appendChild(bloc());
        // Le quizz final est validé plus tard (« Quizz parfait ») : le bloc est alors recalculé
        const q = document.getElementById("btn-voir-score");
        if(q) q.addEventListener("click", () => setTimeout(() => { const v = document.getElementById("trophees-fin"); if(v) v.replaceWith(bloc()); }, 120));
      }
      return r;
    };
  }
  window.TROPHEES_FIN = { bloc };
})();
