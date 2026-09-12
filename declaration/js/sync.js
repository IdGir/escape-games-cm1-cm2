/* ============================================================
   SYNC — Synchronisation élève ↔ serveur prof
   Envoie l'état toutes les 3 s + écoute les commandes prof.
   Fallback gracieux : si le serveur n'est pas joignable,
   l'app fonctionne en mode autonome (100% hors-ligne).
   ============================================================ */

const SYNC = {
  actif: false,
  intervalId: null,
  serveurOk: null,
  derniereCommande: null,
};

function detecterServeur(){
  // On essaie /api/info ; si ça répond, le serveur prof tourne
  return fetch("/api/info", {cache:"no-store"})
    .then(r=>r.ok ? r.json() : null)
    .then(d=>{ SYNC.serveurOk = !!(d && d.serveur); return SYNC.serveurOk; })
    .catch(()=>{ SYNC.serveurOk = false; return false; });
}

function demarrerSync(){
  if(SYNC.actif) return;
  detecterServeur().then(ok=>{
    if(!ok){
      console.info("Serveur prof non détecté — mode autonome.");
      return;
    }
    SYNC.actif = true;
    console.info("Serveur prof détecté — synchronisation active.");
    // Envoi périodique de l'état
    SYNC.intervalId = setInterval(envoyerEtat, 3000);
    envoyerEtat();
  });
}

function envoyerEtat(){
  if(!SYNC.actif || !ETAT.equipe) return;
  const payload = {
    equipe: ETAT.equipe,
    niveau: ETAT.niveau,
    salle: ETAT.salle,
    score: ETAT.score,
    fragments: ETAT.fragments,
    msEcoules: ETAT.msEcoules,
    enPause: ETAT.enPause,
    fini: ETAT.fini
  };
  fetch("/api/etat", {
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body: JSON.stringify(payload)
  })
  .then(r=>r.json())
  .then(data=>{
    if(data && data.commande){
      traiterCommande(data.commande);
    }
  })
  .catch(()=>{ /* serveur injoignable : on ignore */ });
}

function traiterCommande(cmd){
  if(!cmd || JSON.stringify(cmd)===JSON.stringify(SYNC.derniereCommande)) return;
  SYNC.derniereCommande = cmd;
  if(cmd.pause===true && !ETAT.enPause){
    ETAT.enPause = true;
    aller("ecran-pause");
    toast("⏸ Pause demandée par l'enseignant");
  }
  if(cmd.pause===false && ETAT.enPause){
    ETAT.enPause = false;
    aller("ecran-salle");
    toast("▶️ Reprise demandée par l'enseignant");
  }
  if(cmd.indice){
    toast("💡 Message de l'enseignant : " + cmd.indice);
  }
  if(cmd.message){
    toast("📣 " + cmd.message);
  }
}

// Démarrer la synchro dès qu'une partie commence
window.demarrerSync = demarrerSync;
