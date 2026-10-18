/* ============================================================
   SUIVI ÉNIGME PAR ÉNIGME (amélioration N12) — tronc commun
   ------------------------------------------------------------
   Jusqu'ici, le compte-rendu d'une partie ne gardait que des totaux
   (score, erreurs, indices). Ce greffon note, pour CHAQUE énigme jouée :
     id   identifiant de l'énigme (« 2-3 »), ou numéro de salle dans
          Déclaration et Tour du monde (une énigme par salle) ;
     s    numéro de salle ;
     l    identifiant de la leçon liée (sa compétence est dans lecons-a4.json) ;
     ok   résolue ;
     pc   réussie du premier coup (aucune erreur, énigme non passée) ;
     e    nombre d'erreurs (vérifications fausses) ;
     i    nombre d'indices demandés (hors indice offert du palier Découverte) ;
     p    énigme PASSÉE avec le joker (N15) ;
     c    nombre de coups de pouce de l'enseignant reçus (N13).
   Les notes sont gardées avec la partie (ETAT.detail, sauvegardée et reprise
   comme le reste), repartent de zéro à chaque nouvelle partie, et passent
   dans le compte-rendu (champ « detail ») : resultats.html en tire le bilan
   de classe. Aucun effet sur le score ni sur le déroulé du jeu.
   Fonctionne avec les deux moteurs : énigmes JSON (activerEnigme(e, cb)) et
   énigmes écrites en dur (v2Debut / v2Echec / v2Reussite).
   Chargé après app.js, avant les greffons qui s'en servent (joker, coup de pouce).
   ============================================================ */
(function(){
  if(typeof ETAT === "undefined") return;
  let courant = null;       // note de l'énigme affichée

  /** Les notes de la partie en cours (remises à zéro à chaque nouvelle partie, retrouvées à la reprise). */
  function notes(){
    if(!ETAT.detail){
      ETAT.detail = {};
      /* Reprise d'une partie : l'application ne recopie que certains champs de la sauvegarde, on
         retrouve donc les notes dans la sauvegarde elle-même (même équipe, même temps de jeu). */
      try{
        const s = JSON.parse(localStorage.getItem(typeof CLE_SAUVEGARDE !== "undefined" ? CLE_SAUVEGARDE : "") || "null");
        if(s && !s.fini && s.detail && s.equipe === ETAT.equipe && Math.abs((s.msEcoules || 0) - (ETAT.msEcoules || 0)) < 5000) ETAT.detail = s.detail;
      }catch(e){}
    }
    return ETAT.detail;
  }
  /* Nouvelle partie : on repart de zéro (écouteur de capture, avant celui du jeu) */
  const go = document.getElementById("btn-demarrer");
  if(go) go.addEventListener("click", () => { ETAT.detail = {}; }, true);
  function note(id, extra){
    const n = notes();
    id = String(id);
    if(!n[id]) n[id] = { id, s: ETAT.salle || 0, l: "", ok: 0, pc: 0, e: 0, i: 0, p: 0, c: 0 };
    if(extra) Object.assign(n[id], extra);
    return n[id];
  }
  const sauver = () => { if(typeof sauvegarder === "function") sauvegarder(); };

  /* ---- Moteur commun : énigmes de enigmes.json ---- */
  if(typeof window.activerEnigme === "function"){
    const origine = window.activerEnigme;
    window.activerEnigme = function(e, onReussite){
      if(!e || typeof e !== "object") return origine.apply(this, arguments);   // moteur propre : activerEnigme(n)
      const rec = note(e.id, { s: ETAT.salle || 0, l: e.lecon || "" });
      courant = rec;
      const cb = function(en, indices, erreurs){
        rec.ok = 1; rec.e = Math.max(rec.e, erreurs || 0);
        rec.pc = (!rec.e && !rec.p) ? 1 : 0;
        sauver();
        return onReussite.apply(this, arguments);
      };
      return origine.call(this, e, cb);
    };
  }

  /* ---- Moteur propre (Déclaration, Tour du monde) ---- */
  if(typeof window.v2Debut === "function"){
    const debut = window.v2Debut;
    window.v2Debut = function(){
      courant = note("s" + ETAT.salle, { s: ETAT.salle || 0 });
      return debut.apply(this, arguments);
    };
    const echec = window.v2Echec;
    if(typeof echec === "function") window.v2Echec = function(){
      if(courant) courant.e++;
      return echec.apply(this, arguments);
    };
    const reussite = window.v2Reussite;
    if(typeof reussite === "function") window.v2Reussite = function(){
      if(courant){ courant.ok = 1; courant.pc = (!courant.e && !courant.p) ? 1 : 0; sauver(); }
      return reussite.apply(this, arguments);
    };
  }

  /* ---- Erreurs (moteur commun) : le jeu appelle compterErreur() à chaque vérification fausse ---- */
  if(typeof window.compterErreur === "function" && typeof window.activerEnigme === "function"){
    const erreur = window.compterErreur;
    window.compterErreur = function(){
      if(courant && !courant.ok) courant.e++;
      return erreur.apply(this, arguments);
    };
  }

  /* ---- Indices demandés : comptés d'après le total du jeu (l'indice offert du palier Découverte, rendu, ne compte pas) ---- */
  document.addEventListener("click", ev => {
    const b = ev.target && ev.target.closest && ev.target.closest("button");
    if(!b || b.disabled || !(b.id === "btn-indice" || /^indice-/.test(b.id)) || !courant) return;
    const avant = ETAT.indicesTotal || 0, rec = courant;
    setTimeout(() => { if((ETAT.indicesTotal || 0) > avant){ rec.i += (ETAT.indicesTotal - avant); sauver(); } }, 0);
  }, true);

  /** Les notes sous forme compacte pour le compte-rendu (une ligne par énigme jouée). */
  function liste(){
    return Object.values(notes()).filter(n => n.ok || n.p || n.e || n.i || n.c).map(n => ({ ...n }));
  }
  window.SUIVI_ENIGMES = { note, notes, liste, courante: () => courant };
})();
