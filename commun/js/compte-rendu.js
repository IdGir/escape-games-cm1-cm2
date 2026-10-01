/* ============================================================
   COMPTE-RENDU DE PARTIE — tronc commun (D2 mode individuel, D5 export)
   ------------------------------------------------------------
   Construit le compte-rendu d'une partie terminée (ou en cours) à
   partir de l'état du jeu (ETAT), quel que soit le moteur :
     { type:"escape-game-compte-rendu", version:1, jeu, titre, eleve
       (ou équipe), mode:"equipe"|"solo", niveau, palier, date, dureeMin,
       score, scoreMax, enigmes, total, premierCoup, erreurs, indices,
       salles:{n:minutes}, delaiAccordeMin, quiz, code }
   « code » est un code de contrôle (empreinte du contenu) : la page
   resultats.html le recalcule pour repérer un compte-rendu modifié à
   la main. Ce n'est pas une signature infalsifiable, juste un garde-fou.
   Chaque partie terminée est aussi gardée sur l'appareil (historique,
   100 dernières parties) : resultats.html peut tout exporter.
   ============================================================ */
(function(){
  /** Empreinte FNV-1a 32 bits, affichée « XXXX-XXXX ». */
  function empreinte(texte){
    let h = 0x811c9dc5;
    for(const c of String(texte)){ h ^= c.codePointAt(0); h = Math.imul(h, 0x01000193) >>> 0; }
    const x = h.toString(16).toUpperCase().padStart(8, "0");
    return x.slice(0, 4) + "-" + x.slice(4);
  }
  const canon = cr => JSON.stringify(Object.keys(cr).filter(k => k !== "code").sort().reduce((o, k) => (o[k] = cr[k], o), {}));
  const signer = cr => (cr.code = empreinte(canon(cr)), cr);
  const verifier = cr => !!cr && cr.code === empreinte(canon(cr));

  function construire(){
    if(typeof ETAT === "undefined") return null;
    const J = (typeof JEU !== "undefined") ? JEU : {};
    const total = typeof nbEnigmesTotal === "function" ? nbEnigmesTotal() : 5;
    const max = typeof scoreMax === "function" ? scoreMax() : (typeof SCORE_MAX === "number" ? SCORE_MAX : null);
    const salles = {};
    Object.entries(ETAT.tempsParSalle || {}).forEach(([n, ms]) => { salles[n] = Math.round(ms / 6000) / 10; });
    const reussies = ETAT.enigmesReussies != null ? ETAT.enigmesReussies
      : (ETAT.fini ? total : Object.keys(ETAT.tempsParSalle || {}).length);
    const cr = {
      type: "escape-game-compte-rendu", version: 1,
      jeu: J.id || "", titre: J.titre || document.title,
      eleve: ETAT.equipe || "", mode: ETAT.solo ? "solo" : "equipe",
      niveau: ETAT.niveau || "", palier: ETAT.palier || "",
      date: new Date().toISOString().slice(0, 16),
      termine: !!ETAT.fini, dureeMin: Math.round((ETAT.msEcoules || 0) / 6000) / 10,
      score: ETAT.score || 0, scoreMax: max,
      enigmes: reussies, total, premierCoup: ETAT.enigmesPremierCoup || 0,
      erreurs: ETAT.erreursTotal || 0, indices: ETAT.indicesTotal != null ? ETAT.indicesTotal : (ETAT.indicesUtilises || 0),
      motsCles: (ETAT.motsCles || ETAT.fragments || []).length, coffre: !!ETAT.coffreOuvert,
      quiz: ETAT.quiz && ETAT.quiz.repondu ? ETAT.quiz.score : null,
      salles, delaiAccordeMin: ETAT.delaiAccordeMin || 0
    };
    return signer(cr);
  }

  function texte(cr){
    const d = new Date(cr.date);
    const quand = isNaN(d) ? cr.date : d.toLocaleDateString("fr-FR") + " " + d.toLocaleTimeString("fr-FR", { hour: "2-digit", minute: "2-digit" });
    const salles = Object.entries(cr.salles || {}).map(([n, m]) => `${n} (${m} min)`).join(" · ");
    return [
      `Compte-rendu — ${cr.titre} (escape game)`,
      `${cr.mode === "solo" ? "Élève" : "Équipe"} : ${cr.eleve} · ${cr.niveau}${cr.palier === "decouverte" ? " (palier Découverte)" : ""} · ${cr.mode === "solo" ? "mode individuel" : "en équipe"}`,
      `Date : ${quand} · Durée : ${cr.dureeMin} min${cr.termine ? "" : " · partie NON terminée"}`,
      `Score : ${cr.score}${cr.scoreMax ? " / " + cr.scoreMax : ""} · Énigmes : ${cr.enigmes}/${cr.total} (${cr.premierCoup} du premier coup) · Erreurs : ${cr.erreurs} · Indices : ${cr.indices}`,
      cr.quiz != null ? `Quizz final : ${cr.quiz}/5` : "",
      salles ? `Salles : ${salles}` : "",
      cr.delaiAccordeMin ? `Temps accordé par l'enseignant : ${cr.delaiAccordeMin} min` : "",
      `Code de contrôle : ${cr.code}`
    ].filter(Boolean).join("\n");
  }

  /* ---- Historique des parties terminées, sur cet appareil (pour D5) ---- */
  const CLE_HIST = "escape_resultats";
  function historique(){ try { return JSON.parse(localStorage.getItem(CLE_HIST) || "[]"); } catch(e) { return []; } }
  function memoriser(cr){
    if(!cr || !cr.eleve || /^Vérification$/.test(cr.eleve)) return;
    try{
      const h = historique().filter(x => !(x.jeu === cr.jeu && x.eleve === cr.eleve && x.date.slice(0, 10) === cr.date.slice(0, 10) && x.mode === cr.mode));
      h.push(cr);
      localStorage.setItem(CLE_HIST, JSON.stringify(h.slice(-100)));
    }catch(e){}
  }

  /* Fin de partie : mémorisée ; mise à jour quand le quizz est validé */
  if(typeof window.finDuJeu === "function"){
    const origine = window.finDuJeu;
    window.finDuJeu = function(){
      const r = origine.apply(this, arguments);
      const verif = new URLSearchParams(location.search).get("salle");
      if(!verif){
        memoriser(construire());
        const b = document.getElementById("btn-voir-score");
        if(b) b.addEventListener("click", () => setTimeout(() => memoriser(construire()), 50));
      }
      return r;
    };
  }
  window.COMPTE_RENDU = { construire, texte, empreinte, signer, verifier, historique, memoriser, CLE_HIST };
})();
