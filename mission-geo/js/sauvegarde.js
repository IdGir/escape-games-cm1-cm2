/* =========================================================
   SAUVEGARDE — état de la mission, conservé d'une séance
   à l'autre pendant toute l'année scolaire.
   ---------------------------------------------------------
   La mission s'étale sur 16 séances réparties sur l'année :
   la progression DOIT survivre à la fermeture du navigateur.
   Tout est conservé dans le localStorage du poste, et peut
   être exporté / réimporté en un fichier (changement de
   poste, sauvegarde de sécurité, passage en salle informatique).
   ========================================================= */

const SAUVEGARDE = (function(){

  const CLE = "mission_geo_annee_a_v1";

  const REGLAGES_DEFAUT = {
    tailleTexte: 1,
    animationsReduites: false,
    videosActives: true,
    sonVideo: false,
    imagesActives: true,
    lecturePermanente: true,   /* la lecon reste consultable pendant l'enigme */
    ordreLibre: false,         /* true : toutes les seances ouvertes d'emblee */
    dureeSeance: 45            /* minutes indicatives */
  };

  /* Repere local de la classe : personnalise les seances 1 et 2.
     Valeurs par defaut = celles du livret papier. */
  const PROFIL_DEFAUT = {
    commune: "Dijon",
    typeCommune: "ville",
    departement: "Côte-d'Or",
    numeroDepartement: "21",
    region: "Bourgogne-Franche-Comté",
    numeroRegion: 8,
    pays: "France",
    continent: "Europe"
  };

  const RECOMPENSE_DEFAUT = {
    active: false,
    titre: "",
    texte: "",
    media: ""     /* nom de base d'un fichier depose dans assets/ */
  };

  function neuf(){
    return {
      version: 1,
      equipe: "",
      niveau: "CM2",
      palier: "",            /* "decouverte" : palier Découverte (contenu CM1 + coups de pouce offerts) */
      debut: null,
      sessions: {},          /* id -> {reussie, points, essais, duree, date, reponses} */
      indices: [],           /* indices debloques, dans l'ordre d'obtention */
      final: { pays:null, colonne:null, ligne:null, code:null, resolu:false },
      reglages: Object.assign({}, REGLAGES_DEFAUT),
      profil:   Object.assign({}, PROFIL_DEFAUT),
      recompense: Object.assign({}, RECOMPENSE_DEFAUT)
    };
  }

  let etat = neuf();

  /* Mode vérification (enseignant) : index.html?seance=5 ouvre la séance 5
     sur un carnet vierge, en ordre libre, et n'écrit RIEN : la progression
     annuelle de la classe reste intacte sur ce poste. Les réglages, repères
     locaux et récompense déjà saisis sont relus pour un rendu fidèle. */
  const VERIF = new URLSearchParams(location.search).has("seance");

  function charger(){
    if(VERIF){
      etat = neuf();
      try{
        const lu = JSON.parse(localStorage.getItem(CLE) || "null");
        if(lu){
          Object.assign(etat.reglages, lu.reglages || {});
          Object.assign(etat.profil, lu.profil || {});
          Object.assign(etat.recompense, lu.recompense || {});
        }
      }catch(e){}
      etat.equipe = "Vérification";
      etat.reglages.ordreLibre = true;
      return etat;
    }
    try{
      const brut = localStorage.getItem(CLE);
      if(brut){
        const lu = JSON.parse(brut);
        etat = Object.assign(neuf(), lu);
        etat.reglages   = Object.assign({}, REGLAGES_DEFAUT,   lu.reglages   || {});
        etat.profil     = Object.assign({}, PROFIL_DEFAUT,     lu.profil     || {});
        etat.recompense = Object.assign({}, RECOMPENSE_DEFAUT, lu.recompense || {});
      }
    }catch(e){
      console.warn("Sauvegarde illisible, on repart d'un carnet vierge.", e);
      etat = neuf();
    }
    /* Dès l'ouverture : une partie commencée avant cette version arrive aussi sur le PC de la classe. */
    if(Object.keys(etat.sessions || {}).length) setTimeout(() => envoyerAuPC(true), 1500);
    return etat;
  }

  function enregistrer(){
    if(VERIF) return;
    try{ localStorage.setItem(CLE, JSON.stringify(etat)); }
    catch(e){ console.warn("Impossible d'enregistrer la progression.", e); }
    envoyerAuPC();
  }

  /* Copie de la partie sur le PC de la classe (serveur local, /api/parties), quelques secondes après
     chaque enregistrement : si le Chromebook est réinitialisé, ou pour la future version immersive,
     l'équipe reprend sa mission depuis le PC (⚙️ → Progression → « Reprendre depuis le PC »).
     Jamais depuis le site en ligne ni en double-clic : rien ne sort de l'école. */
  const SURPC = /^https?:$/.test(location.protocol) && !/github\.io$/.test(location.hostname);
  let minuteurEnvoi = null;
  function envoyerAuPC(immediat){
    if(VERIF || !SURPC || typeof MISSION_GEO_IMPORT === "undefined" || !etat.equipe) return;
    clearTimeout(minuteurEnvoi);
    minuteurEnvoi = setTimeout(() => {
      const c = MISSION_GEO_IMPORT.convertir(etat);
      if(!c.ok || !c.partie.equipe) return;
      try{
        fetch("/api/parties?jeu=mission-geo", { method: "POST", headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ jeu: "mission-geo", partie: c.partie }) })
          .then(r => { etat.__envoi = r.ok ? new Date().toISOString() : null; }).catch(() => {});
      }catch(e){}
    }, immediat ? 0 : 3000);
  }

  /* Liste des parties gardées sur le PC de la classe (null : pas de serveur local). */
  function partiesDuPC(){
    if(!SURPC) return Promise.resolve(null);
    return fetch("/api/parties?jeu=mission-geo", { cache: "no-store" }).then(r => r.ok ? r.json() : null).then(r => r && r.parties || null).catch(() => null);
  }

  /* Reprend la partie d'une équipe gardée sur le PC (fusion : rien de ce poste n'est perdu). */
  function reprendreDuPC(slug){
    return fetch("/api/parties?jeu=mission-geo&equipe=" + encodeURIComponent(slug), { cache: "no-store" })
      .then(r => r.json()).then(r => {
        if(!r || !r.ok || !r.partie) throw new Error("absente");
        const ici = MISSION_GEO_IMPORT.convertir(etat).partie;
        const p = (ici && ici.equipe && MISSION_GEO_IMPORT.slug(ici.equipe) === slug) ? MISSION_GEO_IMPORT.fusionner(r.partie, ici) : r.partie;
        etat = Object.assign(neuf(), MISSION_GEO_IMPORT.versAncien(p, { reglages: etat.reglages, profil: etat.profil, recompense: etat.recompense }));
        etat.reglages = Object.assign({}, REGLAGES_DEFAUT, etat.reglages || {});
        etat.profil = Object.assign({}, PROFIL_DEFAUT, etat.profil || {});
        etat.recompense = Object.assign({}, RECOMPENSE_DEFAUT, etat.recompense || {});
        enregistrer();
        return etat;
      });
  }

  /* ---- Acces ---- */
  const lire = () => etat;

  function majSession(id, donnees){
    etat.sessions[id] = Object.assign({}, etat.sessions[id], donnees);
    enregistrer();
  }

  function ajouterIndice(indice){
    if(etat.indices.some(i => i.session === indice.session)) return false;
    etat.indices.push(indice);
    enregistrer();
    return true;
  }

  /* v2 : vérification fausse (compteur pour le bilan enseignant) */
  function compterErreur(){
    etat.erreurs = (etat.erreurs || 0) + 1;
    enregistrer();
  }

  function reussies(){
    return Object.values(etat.sessions).filter(s => s.reussie).length;
  }

  function estReussie(id){
    return !!(etat.sessions[id] && etat.sessions[id].reussie);
  }

  function pointsTotaux(){
    return Object.values(etat.sessions).reduce((t, s) => t + (s.points || 0), 0);
  }

  function reinitialiser(garderReglages){
    const r = etat.reglages, p = etat.profil, rec = etat.recompense;
    etat = neuf();
    if(garderReglages){ etat.reglages = r; etat.profil = p; etat.recompense = rec; }
    enregistrer();
  }

  /* ---- Export / import fichier ---- */
  function exporter(){
    const blob = new Blob([JSON.stringify(etat, null, 2)], {type:"application/json"});
    const a = document.createElement("a");
    const jour = new Date().toISOString().slice(0, 10);
    a.href = URL.createObjectURL(blob);
    a.download = "mission-geo-" + (etat.equipe || "classe").replace(/\W+/g, "-") + "-" + jour + ".json";
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(() => URL.revokeObjectURL(a.href), 2000);
  }

  function importer(fichier){
    return new Promise((resolve, reject) => {
      const fr = new FileReader();
      fr.onload = () => {
        try{
          let lu = JSON.parse(fr.result);
          /* Fichier du script de secours ou partie au format commun : convertis d'abord. */
          if(lu && typeof MISSION_GEO_IMPORT !== "undefined" && !("sessions" in lu)){
            const c = MISSION_GEO_IMPORT.convertir(lu);
            if(!c.ok) throw new Error("format");
            lu = MISSION_GEO_IMPORT.versAncien(c.partie, { reglages: etat.reglages, profil: etat.profil, recompense: etat.recompense });
          }
          if(!lu || typeof lu !== "object" || !("sessions" in lu)) throw new Error("format");
          etat = Object.assign(neuf(), lu);
          enregistrer();
          resolve(etat);
        }catch(e){ reject(e); }
      };
      fr.onerror = () => reject(fr.error);
      fr.readAsText(fichier);
    });
  }

  return {
    charger, enregistrer, lire, majSession, ajouterIndice, compterErreur,
    reussies, estReussie, pointsTotaux, reinitialiser,
    exporter, importer, envoyerAuPC, partiesDuPC, reprendreDuPC, REGLAGES_DEFAUT, PROFIL_DEFAUT
  };
})();
