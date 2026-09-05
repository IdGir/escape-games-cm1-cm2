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

  function charger(){
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
    return etat;
  }

  function enregistrer(){
    try{ localStorage.setItem(CLE, JSON.stringify(etat)); }
    catch(e){ console.warn("Impossible d'enregistrer la progression.", e); }
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
          const lu = JSON.parse(fr.result);
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
    charger, enregistrer, lire, majSession, ajouterIndice,
    reussies, estReussie, pointsTotaux, reinitialiser,
    exporter, importer, REGLAGES_DEFAUT, PROFIL_DEFAUT
  };
})();
