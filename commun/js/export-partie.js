/* ============================================================
   EXPORT / REPRISE DE PARTIE PAR FICHIER (amélioration A5) — tronc commun
   ------------------------------------------------------------
   Chaque jeu « salles » garde déjà la partie en cours sur l'appareil
   (localStorage) et propose de la reprendre au retour. Ce greffon la
   rend PORTABLE : utile pour le déroulé en plusieurs séances quand
   l'équipe ne retrouve pas la même tablette ou le même navigateur.

     • écran Pause : « 💾 Enregistrer la partie dans un fichier »
       → <jeu>-<équipe>-<date>.json (rien n'est envoyé sur internet) ;
     • écran d'accueil : « 📂 Reprendre une partie depuis un fichier »
       → le fichier est contrôlé (bon jeu, même version, partie non
         terminée), recopié dans la sauvegarde de l'appareil, puis la
         page se recharge : la question habituelle « Voulez-vous la
         reprendre ? » apparaît.

   S'appuie sur CLE_SAUVEGARDE, ETAT, sauvegarder() et toast() des app.js,
   sans les modifier. Chargé après app.js.
   ============================================================ */
(function(){
  if(typeof ETAT === "undefined" || typeof CLE_SAUVEGARDE === "undefined") return;
  const JEU_ID = (typeof JEU !== "undefined" && JEU.id) || "jeu";
  const TITRE = (typeof JEU !== "undefined" && JEU.titre) || document.title;

  /* Clé où chaque app.js range son numéro de version de sauvegarde
     (une sauvegarde d'une autre version est effacée au démarrage). */
  const CLES_VERSION = {
    "declaration": "escape_app_version",
    "tour-du-monde": "escape_tdm_version",
    "chateau-fort": "escape_app_version_chateau_fort",
    "moyen-age-abbaye": "escape_app_version_moyenage",
    "station-meteo": "escape_app_version_meteo",
    "objets-techniques": "escape_app_version_objets_techniques"
  };
  const CLE_VERSION = (typeof JEU !== "undefined" && JEU.cleVersionSauvegarde)
    || CLES_VERSION[JEU_ID] || ("escape_app_version_" + JEU_ID);
  const FORMAT = "escape-game-partie";

  const lireLS = c => { try{ return localStorage.getItem(c); }catch(e){ return null; } };
  const ecrireLS = (c, v) => { try{ localStorage.setItem(c, v); return true; }catch(e){ return false; } };
  const dire = m => { if(typeof toast === "function") toast(m); else alert(m); };
  const slug = s => String(s || "equipe").normalize("NFD").replace(/[̀-ͯ]/g, "")
    .replace(/[^A-Za-z0-9]+/g, "-").replace(/^-|-$/g, "").toLowerCase() || "equipe";

  /* ---- Export ---- */
  function etatCourant(){
    if(typeof sauvegarder === "function") sauvegarder();
    let e = null;
    try{ e = JSON.parse(lireLS(CLE_SAUVEGARDE) || "null"); }catch(err){}
    if(!e || !e.debut) e = JSON.parse(JSON.stringify(ETAT));   // mode vérification : rien n'est sauvegardé
    return e;
  }
  function contenuExport(){
    const etat = etatCourant();
    if(!etat || !etat.debut || !etat.equipe || etat.fini) return null;
    return {
      format: FORMAT, versionFormat: 1,
      jeu: JEU_ID, titre: TITRE,
      exporteLe: new Date().toISOString(),
      equipe: etat.equipe, niveau: etat.niveau, salle: etat.salle,
      cleSauvegarde: CLE_SAUVEGARDE,
      cleVersion: CLE_VERSION, versionJeu: lireLS(CLE_VERSION),
      etat
    };
  }
  function nomFichier(c){
    const j = new Date(), z = n => String(n).padStart(2, "0");
    return `${JEU_ID}-${slug(c.equipe)}-${j.getFullYear()}-${z(j.getMonth()+1)}-${z(j.getDate())}.json`;
  }
  function exporter(){
    const c = contenuExport();
    if(!c){ dire("Aucune partie en cours à enregistrer."); return null; }
    const texte = JSON.stringify(c, null, 1), nom = nomFichier(c);
    try{
      const a = document.createElement("a");
      a.href = (window.URL && URL.createObjectURL)
        ? URL.createObjectURL(new Blob([texte], {type: "application/json"}))
        : "data:application/json;charset=utf-8," + encodeURIComponent(texte);
      a.download = nom; document.body.appendChild(a); a.click(); a.remove();
    }catch(e){}
    dire(`💾 Partie enregistrée : ${nom} (salle ${c.salle}). Gardez ce fichier pour la prochaine séance.`);
    return {nom, contenu: c};
  }

  /* ---- Import ---- */
  /** Contrôle un contenu de fichier ; renvoie un message d'erreur ou "" */
  function controler(c){
    if(!c || c.format !== FORMAT || !c.etat) return "Ce fichier n'est pas une partie enregistrée par un escape game.";
    if(c.jeu !== JEU_ID) return `Ce fichier est une partie du jeu « ${c.titre || c.jeu} » : ouvrez ce jeu-là pour la reprendre.`;
    const e = c.etat;
    if(e.fini) return "Cette partie est terminée : il n'y a rien à reprendre.";
    if(!e.equipe || !e.debut || !(e.salle >= 1)) return "Le fichier est incomplet (équipe ou salle manquante).";
    if(typeof NB_SALLES !== "undefined" && e.salle > NB_SALLES) return "Le fichier est incohérent (numéro de salle).";
    const v = lireLS(CLE_VERSION);
    if(c.versionJeu && v && c.versionJeu !== v)
      return "Ce fichier vient d'une ancienne version du jeu (le barème a changé) : la partie ne peut pas être reprise.";
    return "";
  }
  function importerTexte(texte){
    let c = null;
    try{ c = JSON.parse(texte); }catch(e){ return {ok:false, message:"Fichier illisible (ce n'est pas un fichier .json valide)."}; }
    const err = controler(c);
    if(err) return {ok:false, message:err};
    let enCours = null;
    try{ enCours = JSON.parse(lireLS(CLE_SAUVEGARDE) || "null"); }catch(e){}
    if(enCours && enCours.debut && !enCours.fini && enCours.equipe !== c.etat.equipe
       && !API.confirmer(`Une partie de l'équipe « ${enCours.equipe} » est déjà en cours sur cet appareil.\nLa remplacer par celle de « ${c.etat.equipe} » ?`))
      return {ok:false, message:"Import annulé."};
    if(!ecrireLS(CLE_SAUVEGARDE, JSON.stringify(c.etat))) return {ok:false, message:"Impossible d'écrire sur cet appareil (navigation privée ?)."};
    if(c.versionJeu) ecrireLS(CLE_VERSION, c.versionJeu);
    return {ok:true, message:`📂 Partie de l'équipe « ${c.etat.equipe} » chargée (salle ${c.etat.salle}).`, contenu:c};
  }
  function importerFichier(f){
    if(!f) return;
    const fr = new FileReader();
    fr.onload = () => {
      const r = importerTexte(String(fr.result || ""));
      dire(r.message);
      if(r.ok) setTimeout(() => API.recharger(), 900);
    };
    fr.readAsText(f);
  }

  /* ---- Interface ---- */
  function ajouterBoutons(){
    const pause = document.querySelector("#ecran-pause .boutons");
    if(pause && !document.getElementById("btn-export-partie")){
      pause.insertAdjacentHTML("beforeend",
        `<button class="btn gris" id="btn-export-partie" type="button" title="Pour reprendre la partie sur un autre appareil">💾 Enregistrer la partie dans un fichier</button>`);
      pause.insertAdjacentHTML("afterend",
        `<p class="note-export" style="font-size:.85rem;opacity:.75;text-align:center">Changement de tablette à la prochaine séance ? Enregistrez la partie, puis sur l'autre appareil : accueil du jeu → « 📂 Reprendre une partie depuis un fichier ».</p>`);
      document.getElementById("btn-export-partie").addEventListener("click", exporter);
    }
    const go = document.getElementById("btn-demarrer");
    const zone = go && (go.closest(".boutons") || go.parentNode);
    if(zone && !document.getElementById("import-partie")){
      zone.insertAdjacentHTML("afterend",
        `<p class="import-partie" style="text-align:center;margin:.4rem 0 0">
           <label class="btn gris petit" for="import-partie" style="cursor:pointer" title="Fichier .json enregistré depuis l'écran Pause">📂 Reprendre une partie depuis un fichier</label>
           <input type="file" id="import-partie" accept=".json,application/json" hidden>
         </p>`);
      document.getElementById("import-partie").addEventListener("change", ev => {
        importerFichier(ev.target.files && ev.target.files[0]); ev.target.value = "";
      });
    }
  }
  if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", ajouterBoutons);
  else ajouterBoutons();

  const API = {
    exporter, contenuExport, importerTexte, controler, cleVersion: CLE_VERSION,
    confirmer: m => window.confirm(m),
    recharger: () => location.reload()
  };
  window.EXPORT_PARTIE = API;
})();
