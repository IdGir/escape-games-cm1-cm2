/* ============================================================
   VARIANTES IMMERSIVES — SUIVI ÉNIGME PAR ÉNIGME ET COMMANDES (N12, N13, N15, N19)
   ------------------------------------------------------------
   Greffon des variantes immersives (immersifs/<jeu>/, moteur VML), chargé après js/app.js,
   sans modifier le moteur (copié dans chaque variante) :
     • VML.detailEnigmes() : une ligne par énigme jouée {id, s (étape), l (leçon), ok, pc (premier
       coup), e (erreurs), i (indices payés), p (passée avec le joker), c (coups de pouce)}, lue dans
       l'état de la partie (VML.ETAT.enigmes / resolues) ; même format que commun/js/suivi-enigmes.js ;
     • le compte-rendu (VML.compteRendu) reçoit « detail », « passees » et « pouces », et son code de
       contrôle est recalculé : resultats.html en tire le bilan de classe (N12) ;
     • l'état envoyé au tableau de bord (VML.payloadEtat) reçoit « pouces » et « passees » ;
     • les commandes du tableau de bord {finSeance:{min}} (N19) et {pouce:true, cout} (N13) sont
       transmises à window.alerteFinSeance et VML.coupDePouce (greffons vml-pouce.js, alerte-seance.js).
   ============================================================ */
(function(){
  const VML = window.VML;
  if(!VML || !VML.compteRendu || !VML.traiterCommande) return;

  /* ---- Détail énigme par énigme ---- */
  VML.detailEnigmes = function(){
    const E = VML.ETAT; if(!E) return [];
    const out = [];
    (((VML.D || {}).enigmes || {}).escales || []).forEach(es => (es.enigmes || []).forEach(e => {
      const s = (E.enigmes || {})[e.id], r = (E.resolues || {})[e.id];
      if(!s && !r) return;
      if(r && r.verif) return;                                  // mode vérification : rien à noter
      const passee = !!(r && r.passee);
      const offerts = s ? (s.indicesOfferts || 0) + (s.indiceOffert ? 1 : 0) : 0;
      const n = { id: e.id, s: es.numero, l: e.lecon || "", ok: r && !passee ? 1 : 0, pc: r && r.premier && !passee ? 1 : 0,
        e: s ? s.erreurs || 0 : 0, i: s ? Math.max(0, (s.indices || 0) - offerts) : 0, p: passee ? 1 : 0, c: s ? s.pouces || 0 : 0 };
      if(n.ok || n.p || n.e || n.i || n.c) out.push(n);
    }));
    return out;
  };

  /* ---- Compte-rendu : même empreinte que journal.js ---- */
  const empreinte = texte => {
    let h = 0x811c9dc5;
    for(const c of String(texte)){ h ^= c.codePointAt(0); h = Math.imul(h, 0x01000193) >>> 0; }
    const x = h.toString(16).toUpperCase().padStart(8, "0");
    return x.slice(0, 4) + "-" + x.slice(4);
  };
  const canon = cr => JSON.stringify(Object.keys(cr).filter(k => k !== "code").sort().reduce((o, k) => (o[k] = cr[k], o), {}));
  const compteRendu = VML.compteRendu;
  VML.compteRendu = function(){
    const cr = compteRendu.apply(this, arguments);
    const detail = VML.detailEnigmes();
    if(detail.length){
      cr.detail = detail;
      cr.passees = detail.filter(n => n.p).length;
      cr.pouces = detail.reduce((t, n) => t + (n.c || 0), 0);
      cr.code = empreinte(canon(cr));
    }
    return cr;
  };

  /* ---- État envoyé au tableau de bord ---- */
  if(VML.payloadEtat){
    const payload = VML.payloadEtat;
    VML.payloadEtat = function(){
      const p = payload.apply(this, arguments), d = VML.detailEnigmes();
      p.pouces = d.reduce((t, n) => t + (n.c || 0), 0);
      p.passees = d.filter(n => n.p).length;
      return p;
    };
  }

  /* ---- Commandes du tableau de bord ---- */
  const traiter = VML.traiterCommande;
  let derniere = null;
  VML.traiterCommande = function(cmd){
    const cle = cmd ? JSON.stringify(cmd) : null;
    const nouveau = !!cmd && (cmd.finSeance || cmd.pouce) && cle !== derniere;
    const r = traiter.apply(this, arguments);
    if(nouveau){
      derniere = cle;
      if(cmd.finSeance && typeof window.alerteFinSeance === "function") window.alerteFinSeance(cmd.finSeance.min);
      if(cmd.pouce && typeof VML.coupDePouce === "function") VML.coupDePouce(cmd.cout);
    }
    return r;
  };
})();
