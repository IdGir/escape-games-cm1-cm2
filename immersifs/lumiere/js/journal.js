/* ============================================================
   JOURNAL DE BORD — compte rendu de l'équipe
   ------------------------------------------------------------
   Réussites du premier coup, fiches consultées, notions à revoir,
   bonus. Imprimable, exportable (JSON), et enregistré au même format
   que le tronc commun (commun/js/compte-rendu.js : clé
   « escape_resultats », empreinte FNV-1a, POST /api/resultat avec
   serveur.py) : resultats.html le lit sans modification.
   ============================================================ */
var VML = window.VML || (window.VML = {});

(function(){
  function empreinte(texte){
    let h = 0x811c9dc5;
    for(const c of String(texte)){ h ^= c.codePointAt(0); h = Math.imul(h, 0x01000193) >>> 0; }
    const x = h.toString(16).toUpperCase().padStart(8, "0");
    return x.slice(0, 4) + "-" + x.slice(4);
  }
  const canon = cr => JSON.stringify(Object.keys(cr).filter(k => k !== "code").sort().reduce((o, k) => (o[k] = cr[k], o), {}));

  VML.scoreMaxEscale = function(num){
    const es = VML.escale(num); if(!es) return 0;
    const B = VML.BAREME;
    return es.enigmes.length * (B.premierCoup + B.bienDocumente) + B.maitreNageur + B.rapidite[0].pts;
  };

  /** Points obtenus sur une escale (énigmes, bonus « Bien documenté », bonus d'escale) */
  VML.scoreEscale = function(num){
    const E = VML.ETAT, es = VML.escale(num); if(!es || !E) return 0;
    const r = E.resolues || {}, b = (E.bonusEscales || {})[num] || {};
    return es.enigmes.reduce((t, e) => t + (r[e.id] ? (r[e.id].pts || 0) + (r[e.id].bienDoc || 0) : 0), 0) + (b.maitreNageur || 0) + (b.rapidite || 0);
  };
  VML.scoreMaxCampagne = function(){
    return (VML.escalesJouables ? VML.escalesJouables() : []).reduce((t, n) => t + VML.scoreMaxEscale(n), 0) + VML.BAREME.coffre.premierCoup;
  };

  VML.compteRendu = function(){
    const E = VML.ETAT, es = VML.escale(E.escale) || { enigmes: [] };
    const res = E.resolues || {};
    const ids = es.enigmes.map(e => e.id);
    const cr = {
      type: "escape-game-compte-rendu", version: 1,
      jeu: VML.JEU.id, titre: VML.T("titre") + " — " + VML.T("sousTitre"),
      eleve: E.equipe || "", mode: E.solo ? "solo" : "equipe",
      niveau: VML.infoGrade(E.niveau).nom, palier: E.niveau,
      date: new Date().toISOString().slice(0, 16),
      partie: E.debut ? new Date(E.debut).toISOString().slice(0, 16) : "",
      termine: !!E.escaleTerminee, dureeMin: Math.round((E.msTotal || E.msEcoules || 0) / 6000) / 10,
      score: E.score || 0, scoreMax: VML.scoreMaxCampagne(),
      enigmes: Object.keys(res).length, total: (VML.escalesJouables ? VML.escalesJouables() : [E.escale]).reduce((t, n) => t + ((VML.escale(n) || { enigmes: [] }).enigmes.length), 0),
      premierCoup: Object.values(res).filter(r => r.premier).length,
      erreurs: E.erreursTotal || 0, indices: E.indicesTotal || 0,
      motsCles: (E.mots || []).length, quiz: null,
      salles: (E.escalesFaites || [E.escale]).reduce((o, n) => (o["Escale " + n] = VML.scoreEscale(n) + " pts", o), {}),
      coffre: !!E.coffreOuvert,
      delaiAccordeMin: E.delaiAccordeMin || 0,
      fiches: (E.fichesConsultees || []).slice(),
      bonus: Object.assign({}, E.bonus || {})
    };
    cr.code = empreinte(canon(cr));
    return cr;
  };

  VML.memoriserCompteRendu = function(){
    if(VML.modeVerif) return;
    const cr = VML.compteRendu();
    try{
      const h = JSON.parse(localStorage.getItem("escape_resultats") || "[]").filter(x => !(x.jeu === cr.jeu && x.eleve === cr.eleve && (x.partie || x.date) === (cr.partie || cr.date)));
      h.push(cr);
      localStorage.setItem("escape_resultats", JSON.stringify(h.slice(-100)));
    }catch(e){}
    if(VML.SYNC && VML.SYNC.serveurOk) fetch("/api/resultat", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(cr) }).catch(() => {});
    return cr;
  };

  /** HTML du journal (écran de fin d'escale et impression) */
  VML.htmlJournal = function(complet){
    const E = VML.ETAT;
    const g = VML.infoGrade(E.niveau);
    const nums = complet ? (E.escalesFaites || []).slice().sort((a, b) => a - b) : [E.escale];
    const res = E.resolues || {};
    const blocs = nums.map(n => {
      const es = VML.escale(n) || { enigmes: [] }, b = (E.bonusEscales || {})[n] || (n === E.escale ? E.bonus : {}) || {};
      const lignes = es.enigmes.map(e => {
        const r = res[e.id], s = (E.enigmes || {})[e.id] || {};
        const etat = !r ? "⏳ non résolue" : r.premier ? "🎯 du premier coup" : `✔ après ${r.erreurs} erreur${r.erreurs > 1 ? "s" : ""}`;
        return `<tr><td>${e.titre}</td><td>${e.competence_programme}</td><td>${etat}</td><td>${r ? r.pts + (r.bienDoc ? " + " + r.bienDoc + " 📚" : "") : "—"}</td><td>${s.indices || 0}</td><td>${(s.fiches || []).map(f => (VML.lecon(f) || {}).titre || f).join(", ") || "—"}</td></tr>`;
      }).join("");
      const aRevoir = es.enigmes.filter(e => !res[e.id] || !res[e.id].premier).map(e => `<li>${e.competence_programme} <i>(${VML.referenceFiche(e.lecon)})</i></li>`).join("");
      return `<h4>Escale ${n} — ${es.titre} · ${VML.scoreEscale(n)} / ${VML.scoreMaxEscale(n)} points</h4>
        <table class="tab-journal"><tr><th>Énigme</th><th>Compétence</th><th>Résultat</th><th>Points</th><th>Indices</th><th>Fiches consultées</th></tr>${lignes}</table>
        <p>Bonus : ${b.maitreNageur ? "🏊 Maître-nageur +" + b.maitreNageur + " · " : ""}${b.rapidite ? "⏱️ Rapidité +" + b.rapidite + " · " : ""}📚 Bien documenté : ${es.enigmes.filter(e => (res[e.id] || {}).bienDoc).length} fois</p>
        ${aRevoir ? `<p><b>Notions à revoir</b> :</p><ul>${aRevoir}</ul>` : "<p><b>Aucune notion à revoir</b> sur cette escale.</p>"}`;
    }).join("");
    return `<div class="journal">
      <h3>📔 Journal de bord — équipe « ${VML.echapper(E.equipe || "")} » · ${g.icone} ${g.nom}</h3>
      <p>Durée de l'escale ${Math.round((E.msEcoules || 0) / 60000)} min · total du voyage : <b>${E.score || 0}</b> points${E.coffreOuvert ? " · 🔓 coffre ouvert" : ""}</p>
      ${blocs}
      <p>Fiches consultées pendant le voyage : ${(E.fichesConsultees || []).map(f => (VML.lecon(f) || {}).titre || f).join(", ") || "aucune"}</p>
    </div>`;
  };

  VML.echapper = s => String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

  VML.imprimer = function(html, titre){
    let z = document.getElementById("zone-impression");
    if(!z){ z = document.createElement("div"); z.id = "zone-impression"; document.body.appendChild(z); }
    z.innerHTML = `<div class="impression-tete">⚓ Vingt mille lieues sous les mers — ${titre || ""}</div>${html}`;
    document.body.classList.add("imprime");
    setTimeout(() => { window.print(); setTimeout(() => document.body.classList.remove("imprime"), 500); }, 50);
  };

  VML.telecharger = function(nom, contenu, type){
    try{
      const a = document.createElement("a");
      a.href = URL.createObjectURL(new Blob([contenu], { type: type || "application/json" }));
      a.download = nom; document.body.appendChild(a); a.click(); a.remove();
    }catch(e){}
  };
})();
