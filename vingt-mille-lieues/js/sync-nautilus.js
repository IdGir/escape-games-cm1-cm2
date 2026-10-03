/* ============================================================
   SYNCHRONISATION avec le tableau de bord (serveur.py, mode local)
   ------------------------------------------------------------
   Même API que commun/js/sync.js (/api/info, /api/etat, commandes),
   sans modifier le serveur : les détails propres au jeu (énigme en
   cours, erreurs, fiches consultées, sas, énigmes résolues) voyagent
   dans le champ « enigme », que serveur.py garde tel quel.
   Commandes reconnues : pause, message, indice, delaiMin, niveau.
   Sans serveur (en ligne, double-clic) : rien n'est envoyé.
   ============================================================ */
var VML = window.VML || (window.VML = {});
VML.SYNC = { actif: false, serveurOk: null, derniere: null };

VML.demarrerSync = function(){
  if(VML.SYNC.actif || VML.modeVerif || location.protocol === "file:") return;
  fetch("/api/info", { cache: "no-store" }).then(r => r.ok ? r.json() : null).then(d => {
    VML.SYNC.serveurOk = !!(d && d.serveur);
    if(!VML.SYNC.serveurOk) return;
    VML.SYNC.actif = true;
    VML.SYNC.id = setInterval(VML.envoyerEtat, 3000);
    VML.envoyerEtat();
  }).catch(() => { VML.SYNC.serveurOk = false; });
};

VML.payloadEtat = function(){
  const E = VML.ETAT, es = VML.escale(E.escale) || { enigmes: [] };
  const e = es.enigmes[E.indexEnigme || 0] || null;
  const s = e ? ((E.enigmes || {})[e.id] || {}) : {};
  return {
    jeu: "vingt-mille-lieues", equipe: E.equipe, niveau: E.niveau, salle: E.escale,
    enigme: {
      id: e ? e.id : null, titre: e ? e.titre : null, ordre: e ? e.ordre : null, total: es.enigmes.length,
      competence: e ? e.competence_programme : null,
      erreurs: s.erreurs || 0, indices: s.indices || 0, fiches: s.fiches || [],
      depuisMs: s.ouverte ? Date.now() - s.ouverte : 0, sas: !!(s.sasJusqu && s.sasJusqu > Date.now()),
      resolues: E.resolues || {}, fichesConsultees: E.fichesConsultees || [], air: Math.round(E.air || 0),
      grade: VML.infoGrade(E.niveau).nom
    },
    score: E.score, fragments: E.mots || [], enigmesReussies: Object.keys(E.resolues || {}).length,
    indicesTotal: E.indicesTotal || 0, msEcoules: E.msEcoules || 0, enPause: !!E.enPause,
    fini: !!E.escaleTerminee, palier: E.niveau, delaiMin: E.delaiAccordeMin || 0
  };
};

VML.envoyerEtat = function(){
  if(!VML.SYNC.actif || !VML.ETAT.equipe) return;
  fetch("/api/etat", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(VML.payloadEtat()) })
    .then(r => r.json()).then(d => { if(d && d.commande) VML.traiterCommande(d.commande); }).catch(() => {});
};

VML.traiterCommande = function(cmd){
  if(!cmd || JSON.stringify(cmd) === JSON.stringify(VML.SYNC.derniere)) return;
  VML.SYNC.derniere = cmd;
  if(cmd.pause === true && VML.mettreEnPause) VML.mettreEnPause(true, "enseignant");
  if(cmd.pause === false && VML.mettreEnPause) VML.mettreEnPause(false, "enseignant");
  if(cmd.message && VML.toast) VML.toast("📣 " + cmd.message, 9000);
  if(cmd.indice && VML.toast) VML.toast("💡 Message de l'enseignant : " + cmd.indice, 12000);
  if(cmd.delaiMin){ VML.ETAT.delaiAccordeMin = (VML.ETAT.delaiAccordeMin || 0) + (+cmd.delaiMin || 0); if(VML.toast) VML.toast(`⏱️ L'enseignant vous accorde ${cmd.delaiMin} minute${cmd.delaiMin > 1 ? "s" : ""}.`); if(VML.sauver) VML.sauver(); }
  if(cmd.niveau && VML.gradeValide(cmd.niveau) && VML.changerGrade) VML.changerGrade(cmd.niveau, true);
};
