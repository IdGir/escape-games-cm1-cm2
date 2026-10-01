/* =========================================================
   APP — moteur principal de la mission
   Enchaîne : accueil → carnet → séance (intro, énigmes,
   leçon, dénouement, indice) → carnet → piste finale.
   ========================================================= */

const APP = (function(){

  const $  = (t, c, x) => { const e = document.createElement(t); if(c) e.className = c;
                            if(x !== undefined) e.textContent = x; return e; };
  const id = s => document.getElementById(s);

  let courant = null;      /* séance en cours */
  let minuterie = null;

  /* ---------------------------------------------------------
     Substitution des repères locaux : {{profil.commune}}, etc.
     --------------------------------------------------------- */
  function substituer(valeur, profil){
    if(typeof valeur === "string"){
      return valeur.replace(/\{\{profil\.(\w+)\}\}/g, (t, cle) =>
        (profil[cle] !== undefined ? profil[cle] : t));
    }
    if(Array.isArray(valeur)) return valeur.map(v => substituer(v, profil));
    if(valeur && typeof valeur === "object"){
      const sortie = {};
      for(const k of Object.keys(valeur)) sortie[k] = substituer(valeur[k], profil);
      return sortie;
    }
    return valeur;
  }

  /* ---------------------------------------------------------
     Écrans, messages, modale
     --------------------------------------------------------- */
  function afficherEcran(nom){
    document.querySelectorAll(".ecran").forEach(e => e.classList.remove("actif"));
    const cible = id("ecran-" + nom);
    if(cible) cible.classList.add("actif");
    id("barre").hidden = (nom === "accueil");
    if(nom === "carnet"){ CARNET.dessinerHub(); majBarre("Carnet de mission", ""); }
    window.scrollTo({ top: 0, behavior: "instant" in window ? "instant" : "auto" });
  }

  function majBarre(titre, sousTitre){
    id("barre-session").textContent = titre;
    id("barre-element").textContent = sousTitre || "";
  }

  let horlogeMessage = null;
  function message(texte, type){
    const b = id("bandeau-message");
    b.textContent = texte;
    b.className = "bandeau" + (type ? " " + type : "");
    b.hidden = false;
    clearTimeout(horlogeMessage);
    horlogeMessage = setTimeout(() => { b.hidden = true; }, 4200);
  }

  function modale(html, apres){
    id("modale-contenu").innerHTML = html;
    id("modale").hidden = false;
    if(apres) apres();
  }
  function fermerModale(){ id("modale").hidden = true; id("modale-contenu").innerHTML = ""; }

  /* ---------------------------------------------------------
     Chronomètre de séance
     --------------------------------------------------------- */
  function demarrerChrono(){
    arreterChrono();
    const depart = Date.now();
    minuterie = setInterval(() => {
      const s = Math.floor((Date.now() - depart) / 1000);
      id("barre-chrono").querySelector("b").textContent =
        String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0");
    }, 1000);
    return depart;
  }
  function arreterChrono(){ if(minuterie){ clearInterval(minuterie); minuterie = null; } }

  function majScore(){
    const pts = courant ? courant.points : 0;
    id("barre-score").querySelector("b").textContent =
      pts + (courant ? " / " + courant.maximum : "");
  }

  /* ---------------------------------------------------------
     Ouverture d'une séance
     --------------------------------------------------------- */
  /* Niveau joué (A2) : CM1 (version guidée), CM2 (livret + « pour aller plus loin »),
     DEC (palier Découverte : CM1 + coups de pouce offerts). ?niveau=… en vérification. */
  function niveauCourant(){
    const p = new URLSearchParams(location.search).get("niveau");
    if(p) return MISSION.niveauDe(p);
    const e = SAUVEGARDE.lire();
    return e.palier === "decouverte" ? "DEC" : MISSION.niveauDe(e.niveau);
  }

  function ouvrirSession(idSession){
    const brut = MISSION.parId(idSession);
    if(!brut) return;
    if(!CARNET.estOuverte(brut) && !SAUVEGARDE.estReussie(idSession)){
      message("Cette séance est encore verrouillée : termine d'abord les précédentes.", "erreur");
      return;
    }
    const profil = SAUVEGARDE.lire().profil;
    const s = MISSION.adapter(substituer(JSON.parse(JSON.stringify(brut)), profil), niveauCourant());

    courant = {
      s,
      etape: 0,                                   /* 0 = intro, 1..n = activités, n+1 = fin */
      points: 0,
      maximum: s.activites.length * PTS_PREMIER_COUP,     /* v2 : 10 points par énigme juste du premier coup */
      resultats: [],
      debut: demarrerChrono()
    };
    majScore();
    majBarre("Séance " + s.numero + " — " + s.titre, s.element);
    afficherEcran("session");
    dessinerEtape();
  }

  /* ---------------------------------------------------------
     Rendu d'une étape de séance
     --------------------------------------------------------- */
  function dessinerEtape(){
    const { s, etape } = courant;
    const hote = id("session-scene");
    hote.innerHTML = "";
    const scene = $("div", "scene");

    scene.appendChild($("h2", null, s.titre));
    const fil = $("p", "fil");
    fil.innerHTML = "📍 " + s.lieu + " · " + s.theme +
      '<span class="badge-livret">livret p. ' + s.livret + "</span>";
    scene.appendChild(fil);

    /* points de progression */
    const points = $("div", "etapes");
    for(let i = 0; i <= s.activites.length + 1; i++){
      const p = $("span");
      if(i < etape) p.classList.add("faite");
      if(i === etape) p.classList.add("active");
      points.appendChild(p);
    }
    scene.appendChild(points);

    if(etape === 0)                       dessinerIntro(scene);
    else if(etape <= s.activites.length)  dessinerActivite(scene);
    else                                  dessinerDenouement(scene);

    hote.appendChild(scene);
    window.scrollTo({ top: 0 });
  }

  function dessinerIntro(scene){
    const { s } = courant;
    if(s.intro && s.intro.media) scene.appendChild(MEDIAS.bloc(s.intro.media));
    const n = $("div", "narration");
    n.innerHTML = s.intro ? s.intro.texte : "";
    scene.appendChild(n);

    const encart = $("div", "avertissement");
    encart.innerHTML = "<b>Objectif de la séance :</b> " + s.element +
      "<br><b>Durée conseillée :</b> environ " + s.duree + " minutes." +
      "<br><b>Nombre d'énigmes :</b> " + s.activites.length + "." +
      "<br><b>🎯 Barème :</b> tout juste du premier coup = " + PTS_PREMIER_COUP + " points ; après une erreur = " +
      PTS_APRES_ERREUR + " points seulement. Lisez la leçon avant de répondre !";
    scene.appendChild(encart);

    const pied = $("div", "pied-scene");
    const retour = $("button", "bouton-second", "← Carnet");
    retour.type = "button";
    retour.addEventListener("click", quitterSession);
    const lecon = $("button", "bouton-second", "📚 Lire la leçon d'abord");
    lecon.type = "button";
    lecon.addEventListener("click", () => LECONS.ouvrir(s.lecon));
    const go = $("button", "bouton-principal", "Commencer la mission →");
    go.type = "button";
    go.addEventListener("click", () => { courant.etape = 1; dessinerEtape(); });
    pied.appendChild(retour); pied.appendChild(lecon); pied.appendChild(go);
    scene.appendChild(pied);
  }

  function dessinerActivite(scene){
    const { s, etape } = courant;
    const act = s.activites[etape - 1];

    const compteur = $("p", "fil", "Énigme " + etape + " sur " + s.activites.length);
    scene.appendChild(compteur);

    if(etape === 1 && s.mediaCoeur) scene.appendChild(MEDIAS.bloc(s.mediaCoeur));

    const zone = $("div");
    scene.appendChild(zone);

    const pied = $("div", "pied-scene");
    const retour = $("button", "bouton-second", "← Énigme précédente");
    retour.type = "button";
    retour.disabled = etape === 1;
    retour.addEventListener("click", () => { courant.etape--; dessinerEtape(); });
    const suite = $("button", "bouton-principal", "Énigme suivante →");
    suite.type = "button";
    suite.disabled = true;
    suite.addEventListener("click", () => { courant.etape++; dessinerEtape(); });
    pied.appendChild(retour); pied.appendChild(suite);
    scene.appendChild(pied);

    ACTIVITES.rendre(act, zone, {
      onFini: r => {
        courant.points += r.points || 0;
        courant.resultats[etape - 1] = {
          type: act.type, reussi: r.reussi, points: r.points,
          essais: r.essais, aide: r.aideUtilisee, detail: r.detail || null
        };
        majScore();
        suite.disabled = false;
        suite.textContent = (etape === s.activites.length)
          ? "Terminer la séance →" : "Énigme suivante →";
        if(r.reussi) message("Énigme résolue ! +" + r.points + " points", "reussite");
      }
    });

    /* si l'activité a déjà été jouée dans cette séance, on ne rejoue pas les points */
    if(courant.resultats[etape - 1]){
      suite.disabled = false;
    }
  }

  /* v2 (octobre 2026) : aucun texte après la résolution. Le dénouement
     n'affiche plus que le bilan chiffré et l'indice, qui n'est montré
     QU'UNE FOIS : les élèves le notent sur leur fiche de mission et
     s'en servent dans la piste finale (le carnet n'en garde que la trace). */
  function dessinerDenouement(scene){
    const { s } = courant;
    arreterChrono();
    const duree = Math.round((Date.now() - courant.debut) / 1000);

    /* enregistrement */
    const dejaReussie = SAUVEGARDE.estReussie(s.id);
    SAUVEGARDE.majSession(s.id, {
      reussie: true,
      points: Math.max(courant.points, (SAUVEGARDE.lire().sessions[s.id] || {}).points || 0),
      maximum: courant.maximum,
      duree,
      date: new Date().toISOString(),
      resultats: courant.resultats
    });

    const nouveau = SAUVEGARDE.ajouterIndice(Object.assign(
      { session: s.id, numero: s.numero, seance: s.titre }, s.indice));

    /* bilan */
    const premiers = courant.resultats.filter(r => r && r.reussi && r.essais === 1).length;
    const bilan = $("div", "avertissement");
    bilan.innerHTML =
      "<b>Bilan de la séance :</b> " + courant.points + " points sur " + courant.maximum +
      " · 🎯 justes du premier coup : " + premiers + "/" + s.activites.length +
      " · durée " + Math.floor(duree / 60) + " min " + (duree % 60) + " s.";
    scene.appendChild(bilan);

    /* indice, affiché une seule fois */
    const F = MISSION.final;
    const carteIndice = $("div", "recompense");
    carteIndice.appendChild($("h2", null, "🔎 Indice de la séance " + s.numero));
    if(s.indice.type === "nombre"){
      const g = (F.symboles[s.indice.symbole] || {}).glyphe || "◇";
      const p = $("p");
      p.innerHTML = '<span style="font-size:2.6rem">' + g + '</span> <b style="font-size:1.8rem"> = ' +
        s.indice.valeur + "</b>";
      carteIndice.appendChild(p);
    } else {
      carteIndice.appendChild($("p", "indice-fait", "« " + s.indice.texte + " »"));
    }
    carteIndice.appendChild($("p", "a-noter",
      "✍️ Recopie cet indice sur ta fiche de mission : il ne sera plus affiché ! Tu en auras besoin pour la piste finale."));
    if(!nouveau && dejaReussie)
      carteIndice.appendChild($("p", "aide-panneau", "(séance déjà réussie : cet indice était déjà noté)"));
    scene.appendChild(carteIndice);

    const pied = $("div", "pied-scene");
    const retour = $("button", "bouton-principal", "Retourner au carnet de mission →");
    retour.type = "button";
    retour.addEventListener("click", quitterSession);
    pied.appendChild(retour);
    scene.appendChild(pied);
  }

  function quitterSession(){
    arreterChrono();
    courant = null;
    id("barre-score").querySelector("b").textContent = "0";
    id("barre-chrono").querySelector("b").textContent = "00:00";
    afficherEcran("carnet");
  }

  /* ---------------------------------------------------------
     Réglages appliqués à la page
     --------------------------------------------------------- */
  function appliquerReglages(){
    const r = SAUVEGARDE.lire().reglages;
    document.documentElement.style.setProperty("--echelle", r.tailleTexte);
    document.body.classList.toggle("animations-reduites", !!r.animationsReduites);
    if(typeof MEDIAS !== "undefined"){
      MEDIAS.configurer({
        videosActives: r.videosActives,
        sonVideo: r.sonVideo,
        imagesActives: r.imagesActives
      });
    }
  }

  /* ---------------------------------------------------------
     Démarrage
     --------------------------------------------------------- */
  function init(){
    SAUVEGARDE.charger();
    appliquerReglages();

    /* Emplacements média déclarés directement dans la page (écran d'accueil) */
    document.querySelectorAll(".media-slot[data-media]").forEach(slot =>
      MEDIAS.remplir(slot, { base: slot.dataset.media, legende: slot.dataset.legende || "" }));

    const etat = SAUVEGARDE.lire();
    if(etat.equipe){
      id("champ-equipe").value = etat.equipe;
      const radio = document.querySelector('input[name="niveau"][value="' + (etat.palier === "decouverte" ? "DEC" : etat.niveau) + '"]');
      if(radio) radio.checked = true;
    }

    id("form-depart").addEventListener("submit", e => {
      e.preventDefault();
      const nom = id("champ-equipe").value.trim();
      if(!nom){ message("Indique d'abord un nom d'équipe.", "erreur"); return; }
      const et = SAUVEGARDE.lire();
      et.equipe = nom;
      const choix = document.querySelector('input[name="niveau"]:checked').value;
      et.niveau = choix === "DEC" ? "CM1" : choix;          // Découverte = contenu CM1 + aide (A2, E2)
      et.palier = choix === "DEC" ? "decouverte" : "";
      if(!et.debut) et.debut = new Date().toISOString();
      SAUVEGARDE.enregistrer();
      afficherEcran("carnet");
    });

    id("btn-carnet").addEventListener("click", () => {
      if(courant && !confirm("Quitter la séance en cours ? Les énigmes déjà validées sont conservées."))
        return;
      quitterSession();
    });
    id("btn-lecon").addEventListener("click", () => {
      if(courant) LECONS.ouvrir(courant.s.lecon);
      else LECONS.bibliotheque();
    });
    id("btn-aide").addEventListener("click", coupDePouce);
    id("btn-reglages").addEventListener("click", () => REGLAGES.ouvrir());
    id("btn-reglages-accueil").addEventListener("click", () => REGLAGES.ouvrir());
    id("btn-valise").addEventListener("click", () => {
      afficherEcran("final");
      CARNET.ouvrirFinal();
      majBarre("La piste finale", "Retrouver la valise");
    });
    id("modale-fermer").addEventListener("click", fermerModale);
    id("modale").addEventListener("click", e => { if(e.target.id === "modale") fermerModale(); });
    document.addEventListener("keydown", e => { if(e.key === "Escape") fermerModale(); });

    /* Mode vérification : ?seance=5 (ou s05) ouvre la séance directement,
       ?seance=final ouvre la piste finale. Voir sauvegarde.js. */
    const verif = new URLSearchParams(location.search).get("seance");
    if(verif){
      afficherEcran("carnet");
      if(verif === "final") id("btn-valise").click();
      else ouvrirSession(/^\d+$/.test(verif) ? "s" + verif.padStart(2, "0") : verif);
      message("🔍 Mode vérification : rien n'est enregistré sur ce poste.");
      return;
    }

    afficherEcran(etat.equipe ? "carnet" : "accueil");
  }

  function coupDePouce(){
    if(!courant){
      modale("<h2>💡 Coup de pouce</h2><p>Choisis une séance dans ton carnet de mission. " +
             "Les séances se débloquent l'une après l'autre — sauf si ton enseignant a " +
             "activé l'ordre libre dans l'espace enseignant.</p>");
      return;
    }
    const act = courant.s.activites[courant.etape - 1];
    if(act && act.aide) modale("<h2>💡 Coup de pouce</h2><p>" + act.aide + "</p>");
    else modale("<h2>💡 Coup de pouce</h2><p>Relis la leçon (icône 📚) : la réponse s'y trouve. " +
                "Tu peux aussi revenir sur une énigme précédente.</p>");
  }

  document.addEventListener("DOMContentLoaded", init);

  return { afficherEcran, ouvrirSession, message, modale, fermerModale, niveauCourant,
           appliquerReglages, majBarre, get courant(){ return courant; } };
})();
