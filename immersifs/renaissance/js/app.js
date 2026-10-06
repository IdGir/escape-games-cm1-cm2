/* ============================================================
   APP — déroulé du jeu « Le Journal du Nautilus »
   ------------------------------------------------------------
   Accueil (équipe, grade) → cinématique d'escale → énigmes jouées
   dans les décors (on clique l'objet du décor) → réaction du décor →
   fin d'escale (fragment affiché une seule fois, bonus, journal de
   bord, « plonger plus profond »).
   Adresse de vérification (rien n'est enregistré) :
     ?verif=1&escale=2&niveau=lieutenant&enigme=3   (&secours=1 : décors dessinés)
   ============================================================ */
var VML = window.VML || (window.VML = {});
var ETAT = null;               // lu par commun/js/enigmes.js (donneesNiveau)
VML.CLE_PARTIE = ((window.VML_JEU || {}).prefixeStockage || "vml") + "_partie";

(function(){
  const $ = s => document.querySelector(s);
  let scene = null, tic = null, dernierTic = 0, insiste = null;

  /* Escales jouables : celles des données, filtrées par le réglage enseignant, dans l'ordre du roman */
  VML.escalesJouables = function(){
    const toutes = ((VML.D.enigmes || {}).escales || []).map(x => x.numero).sort((a, b) => a - b);
    const choix = VML.reglage ? VML.reglage("escales") : null;
    const f = Array.isArray(choix) && choix.length ? toutes.filter(n => choix.includes(n)) : toutes;
    return f.length ? f : toutes;
  };
  VML.escaleSuivante = function(n){ const l = VML.escalesJouables(); const i = l.indexOf(n); return i >= 0 && i < l.length - 1 ? l[i + 1] : null; };

  const nouvelEtat = (equipe, niveau, escale) => ({
    version: 2, equipe, niveau, escale: escale || VML.escalesJouables()[0], indexEnigme: 0, score: 0, resolues: {}, enigmes: {},
    fichesConsultees: [], indicesTotal: 0, indicesEscale: 0, erreursTotal: 0, msEcoules: 0, msTotal: 0,
    debut: Date.now(), enPause: false, escaleTerminee: false, mots: [], motVu: false, bonus: {}, bonusEscales: {},
    escalesFaites: [], air: 100, introVue: false, delaiAccordeMin: 0, coffreOuvert: false, final: false
  });

  VML.sauver = function(){
    if(VML.modeVerif || !VML.ETAT) return;
    try{ localStorage.setItem(VML.CLE_PARTIE, JSON.stringify(VML.ETAT)); }catch(e){}
  };
  const charger = () => { try{ return JSON.parse(localStorage.getItem(VML.CLE_PARTIE) || "null"); }catch(e){ return null; } };

  VML.aller = function(id){
    document.querySelectorAll(".ecran").forEach(e => e.classList.toggle("actif", e.id === id));
    document.body.dataset.ecran = id;
  };

  VML.toast = function(msg, ms){
    const t = document.createElement("div");
    t.className = "toast"; t.setAttribute("role", "status"); t.innerHTML = msg;
    $("#toasts").appendChild(t);
    setTimeout(() => t.classList.add("part"), (ms || 4500));
    setTimeout(() => t.remove(), (ms || 4500) + 600);
  };

  /* ---------------- HUD ---------------- */
  VML.majHUD = function(){
    const E = VML.ETAT; if(!E) return;
    const g = VML.infoGrade(E.niveau);
    $("#hud-equipe").textContent = E.equipe || "—";
    $("#hud-grade").textContent = g.icone + " " + g.nom;
    const s = Math.floor((E.msEcoules || 0) / 1000);
    $("#hud-temps").textContent = String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0");
    $("#hud-score").textContent = E.score || 0;
    $("#hud-fragments").textContent = (E.mots || []).length + "/11";
    const air = Math.max(0, Math.min(100, E.air == null ? 100 : E.air));
    const jauge = $("#jauge-air");
    jauge.style.setProperty("--air", air);
    jauge.setAttribute("aria-valuenow", Math.round(air));
    jauge.classList.toggle("basse", air < 40);
    $("#jauge-air-val").textContent = Math.round(air) + " %";
  };

  /* Jauge d'air : décor narratif, ne retire aucun point */
  VML.perteAir = function(cause){
    const es = VML.escale(VML.ETAT.escale) || {}; const a = es.air || {};
    if(cause === "indice") VML.ETAT.air = Math.max(a.plancher || 25, (VML.ETAT.air || 100) - (a.perte_par_indice || 3));
    VML.majHUD();
  };
  const airEscale = () => (VML.escale(VML.ETAT.escale) || {}).air || null;
  /* l'air baisse tant que la « pompe » n'est pas réparée ; avec « debut », seulement après cette énigme-là */
  const pompeEnMarche = () => { const a = airEscale(), r = VML.ETAT.resolues || {}; return !a || !a.pompe || !!r[a.pompe] || (!!a.debut && !r[a.debut]); };

  function demarrerChrono(){
    clearInterval(tic); dernierTic = Date.now();
    tic = setInterval(() => {
      const E = VML.ETAT, now = Date.now(), dt = now - dernierTic; dernierTic = now;
      if(!E || E.enPause || E.escaleTerminee || document.body.dataset.ecran !== "ecran-jeu") return;
      E.msEcoules = (E.msEcoules || 0) + dt;
      E.msTotal = (E.msTotal || 0) + dt;
      const es = VML.escale(E.escale) || {}; const a = es.air || {};
      if(E.introVue && !pompeEnMarche()) E.air = Math.max(a.plancher || 25, (E.air || 100) - (a.perte_par_minute || 1) * dt / 60000);
      VML.majHUD();
      if(Math.round(E.msEcoules / 1000) % 10 === 0) VML.sauver();
    }, 1000);
  }

  VML.mettreEnPause = function(oui, par){
    const E = VML.ETAT; if(!E) return;
    E.enPause = !!oui;
    if(oui){ VML.taire(); VML.aller("ecran-pause"); $("#pause-par").textContent = par === "enseignant" ? "Pause demandée par l'enseignant." : "Le temps est suspendu."; }
    else { VML.aller("ecran-jeu"); dernierTic = Date.now(); }
    VML.sauver();
  };

  VML.changerGrade = function(g, parEnseignant){
    if(!VML.gradeValide(g) || !VML.ETAT) return;
    VML.ETAT.niveau = g; ETAT = VML.ETAT;
    if(parEnseignant) VML.toast("🎚️ L'enseignant a réglé votre grade : " + VML.infoGrade(g).icone + " " + VML.infoGrade(g).nom);
    VML.majHUD(); VML.sauver();
    if(document.body.dataset.ecran === "ecran-jeu" && !VML.ETAT.escaleTerminee){
      const o = document.getElementById("panneau-enigme"); o.classList.remove("ouvert"); o.innerHTML = "";
      entrerEnigme();
    }
  };

  /* ---------------- Accueil ---------------- */
  function accueil(){
    VML.aller("ecran-accueil");
    const sc = new VML.Scene($("#scene-accueil"));
    sc.afficher("salon", { etat: "normal", actives: [] });
    const grades = (VML.D.enigmes || {}).niveaux || [];
    const impose = VML.reglage("niveauImpose");
    $("#choix-grade").innerHTML = grades.map(g => `
      <button class="carte-grade ${impose && impose !== g.id ? "indisponible" : ""}" data-grade="${g.id}" ${impose && impose !== g.id ? "disabled" : ""} aria-pressed="false">
        <span class="g-icone">${g.icone}</span><span class="g-nom">${g.nom}</span>
        <span class="g-desc">${({ mousse: "Énigmes courtes, aides renforcées", matelot: "L'équipage au complet", timonier: "Plus d'éléments, vocabulaire précis", lieutenant: "Documents à croiser, justification", second: "Données chiffrées, pièges, justification" })[g.id] || ""}</span>
      </button>`).join("");
    let choisi = impose || null;
    const maj = () => {
      document.querySelectorAll(".carte-grade").forEach(b => { const s = b.dataset.grade === choisi; b.classList.toggle("choisie", s); b.setAttribute("aria-pressed", s); });
      $("#btn-embarquer").disabled = !(choisi && $("#nom-equipe").value.trim());
    };
    document.querySelectorAll(".carte-grade").forEach(b => b.addEventListener("click", () => { choisi = b.dataset.grade; maj(); }));
    $("#nom-equipe").addEventListener("input", maj);
    maj();
    const sauvee = charger();
    if(sauvee && sauvee.equipe && sauvee.niveau){
      $("#reprise").hidden = false;
      $("#reprise-texte").textContent = `Équipe « ${sauvee.equipe} » · ${VML.infoGrade(sauvee.niveau).icone} ${VML.infoGrade(sauvee.niveau).nom} · escale ${sauvee.escale}, ${sauvee.escaleTerminee ? "terminée" : "énigme " + ((sauvee.indexEnigme || 0) + 1)}`;
      $("#btn-reprendre-partie").onclick = () => { sc.detruire(); lancer(sauvee); };
    }
    $("#btn-embarquer").onclick = () => {
      const nom = $("#nom-equipe").value.trim().slice(0, 24);
      if(!nom || !choisi) return;
      sc.detruire();
      lancer(nouvelEtat(nom, choisi));
    };
    /* Bande-annonce : le bouton n'apparaît que si assets/videos/bande-annonce.mp4 existe */
    VML.sonderVideo("bande-annonce").then(url => {
      if(!url) return;
      const bb = $("#btn-bande-annonce"); bb.hidden = false;
      bb.onclick = () => {
        const ov = $("#cinematique"); VML.aller("ecran-cine");
        ov.innerHTML = `<video class="cine-video" playsinline controls autoplay></video><button class="btn-laiton cine-passer">⏭ Fermer</button>`;
        const v = ov.querySelector("video"), retour = () => { v.pause(); ov.innerHTML = ""; VML.aller("ecran-accueil"); };
        v.src = url; v.onended = retour; ov.querySelector(".cine-passer").onclick = retour;
        v.play().catch(() => {});
      };
    });
    const d = (VML.D.dialogues || {}).accueil;
    if(d){
      $("#accueil-portrait").innerHTML = VML.htmlPortrait(d.personnage, "accueil");
      VML.installerPortrait($("#accueil-portrait .portrait-ovale"));
      VML.ecrire($("#accueil-texte"), d.texte);
      $("#btn-ecouter-accueil").onclick = () => VML.dire(d.personnage, d.texte, $("#accueil-portrait .portrait-ovale"));
    }
  }

  function lancer(etat){
    VML.ETAT = ETAT = etat;
    VML.sauver();
    VML.demarrerSync();
    demarrerChrono();
    if(etat.final){ VML.ouvrirCoffre(); return; }
    if(etat.escaleTerminee){ finEscale(true); return; }
    const es = VML.escale(etat.escale) || {};
    if(!etat.introVue){
      etat.air = (es.air || {}).depart || 100;
      VML.jouerCinematique(es.cinematique_ouverture || ("transition-e" + etat.escale)).then(() => { VML.ETAT.introVue = true; VML.sauver(); entrerEnigme(); });
    }
    else entrerEnigme();
  }

  /* ---------------- Cinématiques ---------------- */
  VML.sonderVideo = async function(base){
    if(location.protocol === "file:" || VML.parametre("secours") === "1") return null;
    for(const ext of [".mp4", ".webm"]){
      const url = "assets/videos/" + base + ext;
      try{ const r = await fetch(url, { method: "HEAD", cache: "no-cache" }); if(r.ok) return url; }catch(e){}
    }
    return null;
  };

  VML.jouerCinematique = async function(id){
    const c = ((VML.D.dialogues || {}).cinematiques || {})[id];
    const ov = $("#cinematique");
    if(!c || VML.modeVerif){ if(c) appliquerEffetsCine(c); return; }
    VML.aller("ecran-cine");
    ov.innerHTML = `<div class="cine-scene"></div><video class="cine-video" playsinline hidden></video>
      <div class="cine-titre">${c.titre || ""}</div>
      <div class="cine-soustitre" aria-live="polite"></div>
      <button class="btn-laiton cine-passer">⏭ Passer</button>`;
    let passe = false;
    const fin = new Promise(res => { ov.querySelector(".cine-passer").onclick = () => { passe = true; VML.taire(); res(); }; });
    const st = ov.querySelector(".cine-soustitre");
    const video = c.video ? await VML.sonderVideo(c.video) : null;
    const jouer = async () => {
      if(video){
        const v = ov.querySelector(".cine-video"); v.hidden = false; v.src = video; v.muted = false;
        let k = 0;
        const total = c.plans.reduce((s, p) => s + p.duree, 0);
        v.ontimeupdate = () => { let acc = 0; for(let j = 0; j < c.plans.length; j++){ acc += c.plans[j].duree * (v.duration || total) / total; if(v.currentTime < acc){ if(j !== k || !st.innerHTML){ k = j; st.innerHTML = sousTitre(c.plans[j]); } break; } } };
        try{ await v.play(); }catch(e){}
        await new Promise(r => { v.onended = r; v.onerror = r; });
        return;
      }
      const sc = new VML.Scene(ov.querySelector(".cine-scene"));
      for(const p of c.plans){
        if(passe) break;
        await sc.afficher(p.decor, { etat: p.etat, actives: [] });
        const hote = ov.querySelector(".cine-scene");
        /* Plan filmé (vidéo déposée) : il se pose au-dessus du décor ; sans fichier, le décor animé reste */
        const anc = ov.querySelector(".cine-plan-video"); if(anc) anc.remove();
        const urlPlan = p.video ? await VML.sonderVideo(p.video) : null;
        if(urlPlan){
          const v = document.createElement("video");
          v.className = "cine-plan-video"; v.muted = true; v.playsInline = true; v.src = urlPlan;
          /* Si le fichier ne se lit pas (codec, fichier abîmé), la vidéo disparaît et le décor animé reste : la cinématique ne dépend jamais d'elle */
          v.onerror = () => v.remove();
          ov.querySelector(".cine-scene").after(v);
          try{ const pr = v.play(); if(pr && pr.catch) pr.catch(() => v.remove()); }catch(e){ v.remove(); }
        }
        hote.classList.remove("mvt-zoom", "mvt-glisse", "mvt-secousse"); void hote.offsetWidth;
        hote.classList.add("mvt-" + (p.mouvement || "zoom"));
        if(p.effet === "coupure" || p.effet === "alarme"){ if(p.effet === "coupure") hote.classList.add("coupure"); if(VML.son) VML.son("alarme"); const a = (VML.escale(VML.ETAT.escale) || {}).air || {}; if(a.apres_avarie) VML.ETAT.air = a.apres_avarie; VML.majHUD(); }
        st.innerHTML = sousTitre(p);
        const portrait = st.querySelector(".portrait-ovale"); if(portrait) VML.installerPortrait(portrait);
        await Promise.race([
          Promise.all([p.personnage ? VML.dire(p.personnage, p.texte, portrait) : Promise.resolve(), new Promise(r => setTimeout(r, p.duree * 1000))]),
          fin
        ]);
      }
      sc.detruire();
      const pv = ov.querySelector(".cine-plan-video"); if(pv) pv.remove();
    };
    await Promise.race([jouer(), fin]);
    appliquerEffetsCine(c);
    /* Sortie en fondu au noir : le voile couvre l'écran, la cinématique est retirée, l'écran suivant se met en place
       dessous, puis le voile se lève. « Passer » fait le même fondu, en plus court. */
    await VML.fonduNoir(passe ? 350 : 900);
    ov.innerHTML = "";
    VML.leverVoileNoir(700);
  };
  VML.fonduNoir = function(ms){
    return new Promise(res => {
      let v = document.getElementById("voile-noir");
      if(!v){ v = document.createElement("div"); v.id = "voile-noir"; v.setAttribute("aria-hidden", "true"); document.body.appendChild(v); }
      v.style.transition = "none"; v.style.opacity = "0"; void v.offsetWidth;
      const d = (VML.animationsReduites && VML.animationsReduites()) ? 250 : ms;
      v.style.transition = `opacity ${d}ms ease`; v.style.opacity = "1";
      setTimeout(res, VML.d(d) + 30);
    });
  };
  VML.leverVoileNoir = function(ms){
    setTimeout(() => {
      const v = document.getElementById("voile-noir"); if(!v) return;
      v.style.transition = `opacity ${ms}ms ease`; v.style.opacity = "0";
      setTimeout(() => { if(v.style.opacity === "0") v.remove(); }, VML.d(ms) + 60);
    }, VML.d(80));
  };
  function sousTitre(p){
    const pe = p.personnage ? VML.perso(p.personnage) : null;
    return (p.personnage ? VML.htmlPortrait(p.personnage, "cine") : "") + `<div><b>${pe ? pe.court || pe.nom : ""}</b> ${pe ? "— " : ""}<span>${p.texte}</span></div>`;
  }
  function appliquerEffetsCine(c){
    const a = VML.ETAT ? ((VML.escale(VML.ETAT.escale) || {}).air || {}) : {};
    if(c.plans.some(p => p.effet === "coupure" || p.effet === "alarme") && VML.ETAT && !VML.ETAT.introVue && a.apres_avarie){
      VML.ETAT.air = a.apres_avarie;
    }
  }

  /* ---------------- Escale ---------------- */
  /* États des décors (panne, alarme, victoire…) : règles « etats_decor » de l'escale.
     { decor, etat, jusqua: idEnigme } vaut tant que l'énigme n'est pas résolue ;
     { decor, etat, apres: idEnigme } vaut une fois l'énigme résolue (la dernière règle qui s'applique gagne). */
  function etatDecor(decor){
    const r = VML.ETAT.resolues || {}, es = VML.escale(VML.ETAT.escale) || {};
    let etat = "normal";
    (es.etats_decor || []).forEach(g => {
      if(g.decor !== decor) return;
      if(g.jusqua && !r[g.jusqua]) etat = g.etat;
      if(g.apres && r[g.apres]) etat = g.etat;
      if(!g.jusqua && !g.apres) etat = g.etat;
    });
    return etat;
  }
  VML.etatDecor = etatDecor;

  function entrerEnigme(){
    const E = VML.ETAT, es = VML.escale(E.escale);
    const e = es.enigmes[E.indexEnigme];
    if(!e){ finEscale(); return; }
    VML.aller("ecran-jeu");
    VML.majHUD();
    if(!scene) scene = new VML.Scene($("#scene-jeu"));
    const ouvrir = (zoneId) => {
      const r = scene.rectZone(zoneId) || { x: innerWidth / 2, y: innerHeight / 2, w: 0, h: 0 };
      VML.masquerPlaque($("#plaque"));
      clearTimeout(insiste); scene.hote.classList.remove("insiste");
      VML.ouvrirEnigme(e, {
        numero: E.indexEnigme + 1, total: es.enigmes.length, origine: { x: r.x + r.w / 2, y: r.y + r.h / 2 },
        onFermer: () => presenter(false),
        onReussite: () => reussite(e)
      });
    };
    VML.ouvrirEnigmeCourante = () => ouvrir(e.objet_principal);
    scene.afficher(e.decor, {
      etat: etatDecor(e.decor), cible: e.objet_principal, actives: e.objets_cliquables,
      onZone: (id, z) => {
        if(id === e.objet_principal) ouvrir(id);
        else examiner(z);
      }
    }).then(() => { if(typeof document !== "undefined" && document && scene.hote.isConnected) $("#lieu").textContent = (VML.decor(e.decor) || {}).titre || ""; });
    const presenter = (parler) => {
      const v = VML.vueEnigme(e, E.niveau);
      const z = (VML.decor(e.decor) || { zones: [] }).zones.find(x => x.id === e.objet_principal) || {};
      const p = VML.plaque($("#plaque"), {
        perso: e.personnage_emetteur, texte: v.dialogue,
        source: "📖 " + e.episode_du_roman.split(":")[0],
        boutons: [{ libelle: "🔍 Examiner : " + (z.libelle || "l'objet"), classe: "principal", action: () => ouvrir(e.objet_principal) }]
      });
      if(!parler) VML.taire();
      clearTimeout(insiste);
      insiste = setTimeout(() => scene.hote.classList.add("insiste"), 45000);
      return p;
    };
    presenter(true);
    VML.sauver();
    if(VML.envoyerEtat) VML.envoyerEtat();
  }

  function examiner(z){
    if(!z) return;
    const b = $("#bulle-examen");
    const r = scene.rectZone(z.id);
    b.innerHTML = `<b>${z.libelle}</b><br>${z.description || ""}`;
    b.style.left = Math.max(12, Math.min(innerWidth - 300, (r ? r.x + r.w / 2 : innerWidth / 2) - 140)) + "px";
    b.style.top = Math.max(70, (r ? r.y + r.h + 8 : innerHeight / 2)) + "px";
    b.classList.add("visible");
    if(VML.son) VML.son("clic");
    clearTimeout(b._t); b._t = setTimeout(() => b.classList.remove("visible"), 4200);
  }

  function reussite(e){
    const E = VML.ETAT;
    const re = e.reaction_du_decor || {};
    const a = airEscale();
    if(a && a.plein === e.id) E.air = 100;
    scene.reaction(re.effet, e.objet_principal);
    VML.masquerPlaque($("#plaque"));
    E.indexEnigme++;
    VML.sauver();
    VML.majHUD();
    setTimeout(() => {
      scene.viderReactions();
      if(E.indexEnigme >= VML.escale(E.escale).enigmes.length){
        const es = VML.escale(E.escale) || {};
        VML.jouerCinematique(es.cinematique_fin || ("fin-e" + E.escale)).then(() => finEscale());
      }else{
        const hote = $("#scene-jeu");
        hote.classList.add("fondu");
        setTimeout(() => { hote.classList.remove("fondu"); entrerEnigme(); }, VML.d(650));
      }
    }, VML.d(re.effet === "hublots" ? 3200 : 2400));
  }

  /* ---------------- Fin d'escale ---------------- */
  function finEscale(reprise){
    const E = VML.ETAT, es = VML.escale(E.escale);
    if(!E.escaleTerminee){
      E.escaleTerminee = true;
      E.air = 100;
      const B = VML.BAREME;
      E.bonus = {};
      if((E.indicesEscale || 0) === 0) E.bonus.maitreNageur = B.maitreNageur;
      const ref = (VML.reglage("dureeEscaleMin") || 25) + (E.delaiAccordeMin || 0);
      const min = (E.msEcoules || 0) / 60000;
      const rap = min <= ref - 5 ? B.rapidite[0].pts : min <= ref ? B.rapidite[1].pts : 0;
      if(rap) E.bonus.rapidite = rap;
      E.bonusEscales = E.bonusEscales || {};
      E.bonusEscales[E.escale] = Object.assign({}, E.bonus);
      E.score = (E.score || 0) + (E.bonus.maitreNageur || 0) + (E.bonus.rapidite || 0);
      if(!(E.mots || []).includes(es.mot)) E.mots = (E.mots || []).concat([es.mot]);
      E.escalesFaites = [...new Set((E.escalesFaites || []).concat([E.escale]))];
      VML.sauver();
      VML.memoriserCompteRendu();
      if(VML.envoyerEtat) VML.envoyerEtat();
    }
    VML.aller("ecran-fin");
    VML.majHUD();
    const f = $("#fin-contenu");
    const d = ((VML.D.dialogues || {}).fin_escale || {})[E.escale];
    const g = VML.gradeSuivant(E.niveau);
    const suivante = VML.escaleSuivante(E.escale);
    const esS = suivante ? VML.escale(suivante) : null;
    const fragment = !E.motVu
      ? `<div class="fragment" id="fragment">
          <div class="fragment-titre">Fragment du journal de bord — escale ${E.escale}</div>
          <div class="fragment-mot" aria-label="Mot de l'escale">${es.mot}</div>
          <p>Ce mot n'apparaîtra <b>qu'une seule fois</b>. Recopiez-le maintenant sur votre fiche de mission, case « Escale ${E.escale} ».</p>
          <button class="btn-laiton principal" id="btn-mot-note">✅ Nous l'avons noté</button>
        </div>`
      : `<div class="fragment ferme"><div class="fragment-titre">Fragment de l'escale ${E.escale} : déjà noté sur la fiche de mission.</div></div>`;
    f.innerHTML = `
      <div class="fin-plaque" id="fin-plaque"></div>
      ${fragment}
      <div class="bilan" ${E.motVu ? "" : "hidden"} id="bilan">
        <h2>⚓ Escale ${E.escale} accomplie</h2>
        <p class="bilan-score">Escale : <b>${VML.scoreEscale(E.escale)}</b> / ${VML.scoreMaxEscale(E.escale)} · total du voyage : <b>${E.score}</b></p>
        <p>${E.bonus && E.bonus.maitreNageur ? "🏊 <b>Maître-nageur</b> : escale sans indice, +" + E.bonus.maitreNageur + " · " : ""}${E.bonus && E.bonus.rapidite ? "⏱️ <b>Rapidité</b> +" + E.bonus.rapidite + " · " : ""}📚 Bien documenté : ${es.enigmes.filter(x => (E.resolues[x.id] || {}).bienDoc).length} fois</p>
        ${VML.htmlJournal()}
        <div class="boutons-fin">
          ${esS ? `<button class="btn-laiton principal" id="btn-escale-suivante">🗺️ Escale ${suivante} : ${esS.titre}</button>`
                : `<button class="btn-laiton principal" id="btn-coffre">🔐 Ouvrir le coffre du capitaine</button>`}
          ${g ? `<button class="btn-laiton" id="btn-plonger">🌊 Plonger plus profond : rejouer cette escale en ${VML.infoGrade(g).icone} ${VML.infoGrade(g).nom}</button>` : ""}
          <button class="btn-laiton" id="btn-imprimer-journal">🖨️ Imprimer le journal de bord</button>
        </div>
      </div>`;
    if(d && !reprise) VML.plaque($("#fin-plaque"), { perso: d.personnage, texte: d.texte });
    else if(d) $("#fin-plaque").innerHTML = "";
    const bm = $("#btn-mot-note");
    if(bm) bm.onclick = () => {
      E.motVu = true; VML.sauver();
      const fr = $("#fragment"); fr.classList.add("ferme"); fr.innerHTML = `<div class="fragment-titre">Fragment de l'escale ${E.escale} : noté sur la fiche de mission.</div>`;
      $("#bilan").hidden = false;
      if(VML.son) VML.son("fragment");
    };
    if(!E.motVu && VML.son) VML.son("orgue");
    const bp = $("#btn-plonger");
    if(bp) bp.onclick = () => { VML.taire(); rejouerEscale(g); };
    const bs = $("#btn-escale-suivante");
    if(bs) bs.onclick = () => { VML.taire(); passerEscale(suivante); };
    const bc = $("#btn-coffre");
    if(bc) bc.onclick = () => { VML.taire(); E.final = true; VML.sauver(); VML.ouvrirCoffre(); };
    $("#btn-imprimer-journal").onclick = () => VML.imprimer(VML.htmlJournal(), "Journal de bord");
  }

  function reinitialiserEscale(E){
    Object.assign(E, { indexEnigme: 0, escaleTerminee: false, indicesEscale: 0, msEcoules: 0, motVu: false, introVue: false, bonus: {}, delaiAccordeMin: 0 });
  }
  function passerEscale(n){
    const E = VML.ETAT;
    E.escale = n; reinitialiserEscale(E);
    VML.sauver(); lancer(E);
  }
  /* « Plonger plus profond » : la même escale au grade supérieur ; ses points sont remplacés */
  function rejouerEscale(g){
    const E = VML.ETAT, es = VML.escale(E.escale);
    E.score = Math.max(0, (E.score || 0) - VML.scoreEscale(E.escale));
    es.enigmes.forEach(x => { delete E.resolues[x.id]; delete E.enigmes[x.id]; });
    delete (E.bonusEscales || {})[E.escale];
    E.niveau = g; ETAT = E;
    reinitialiserEscale(E);
    E.motVu = true; E.introVue = true;
    VML.sauver(); lancer(E);
  }

  /* ---------------- Coffre du capitaine (final) ---------------- */
  VML.ouvrirCoffre = function(){
    const E = VML.ETAT;
    VML.aller("ecran-fin");
    const l = VML.escalesJouables().filter(n => (E.escalesFaites || []).includes(n));
    const C = (VML.D.dialogues || {}).coffre || {};
    E.coffre = E.coffre || { erreurs: 0 };
    $("#fin-contenu").innerHTML = `
      <div class="fin-plaque" id="coffre-plaque"></div>
      <div class="coffre ${E.coffreOuvert ? "ouvert" : ""}">
        <h2>${VML.T("coffre")}</h2>
        <p>Retapez, case par case, les fragments du journal de bord notés sur votre fiche de mission.</p>
        <div class="coffre-cases">${l.map(n => `<label class="coffre-case">Escale ${n}<input type="text" data-escale="${n}" autocomplete="off" maxlength="16" ${E.coffreOuvert ? "disabled" : ""}></label>`).join("")}</div>
        <div class="feedback" id="fb-coffre" role="status"></div>
        <div class="boutons-fin">${E.coffreOuvert ? "" : `<button class="btn-laiton principal" id="btn-ouvrir-coffre">🔓 Ouvrir</button>`}
          <button class="btn-laiton" id="btn-journal-final">🖨️ Journal de bord complet</button></div>
      </div>`;
    if(C.personnage && !E.coffreOuvert) VML.plaque($("#coffre-plaque"), { perso: C.personnage, texte: C.texte });
    $("#btn-journal-final").onclick = () => VML.imprimer(VML.htmlJournal(true), "Journal de bord complet");
    const bo = $("#btn-ouvrir-coffre");
    if(bo) bo.onclick = () => {
      const champs = [...document.querySelectorAll(".coffre-case input")];
      if(champs.some(c => !c.value.trim())){ const fb = $("#fb-coffre"); fb.className = "feedback indice show"; fb.textContent = "✋ Toutes les cases ne sont pas remplies."; return; }
      const justes = champs.filter(c => normaliser(c.value) === normaliser((VML.escale(+c.dataset.escale) || {}).mot)).length;
      const fb = $("#fb-coffre");
      if(justes === champs.length){
        const pts = E.coffre.erreurs ? VML.BAREME.coffre.apresErreur : VML.BAREME.coffre.premierCoup;
        E.score += pts; E.coffreOuvert = true; E.fini = true;
        fb.className = "feedback succes show"; fb.innerHTML = `🔓 <b>Le coffre s'ouvre.</b> +${pts} points`;
        if(VML.son) VML.son("fragment");
        VML.sauver(); VML.memoriserCompteRendu();
        setTimeout(() => VML.jouerCinematique("fin").then(() => VML.ouvrirCoffre()), VML.d(1600));
      }else{
        E.coffre.erreurs++;
        if(VML.son) VML.son("erreur");
        fb.className = "feedback erreur show"; fb.innerHTML = `✗ <b>Le coffre reste fermé.</b> ${justes} fragment${justes > 1 ? "s" : ""} juste${justes > 1 ? "s" : ""} sur ${champs.length}. Relisez votre fiche de mission.`;
        VML.sauver();
      }
    };
  };

  /* ---------------- Démarrage ---------------- */
  VML.demarrer = async function(){
    await VML.chargerDonnees();
    VML.appliquerReglages();
    $("#btn-biblio").onclick = () => VML.ouvrirBibliotheque();
    $("#btn-reglages").onclick = () => VML.ouvrirReglages();
    $("#btn-reglages-accueil").onclick = () => VML.ouvrirReglages();
    $("#btn-pause").onclick = () => VML.mettreEnPause(true, "equipe");
    $("#btn-reprendre").onclick = () => VML.mettreEnPause(false);
    const verif = VML.parametre("verif") === "1";
    VML.modeVerif = verif;
    if(verif){
      const g = VML.gradeValide(VML.parametre("niveau")) || "matelot";
      const n = nouvelEtat("Vérification", g, +(VML.parametre("escale") || VML.escalesJouables()[0]));
      n.indexEnigme = Math.max(0, (+(VML.parametre("enigme") || 1)) - 1);
      n.introVue = true; n.air = ((VML.escale(n.escale) || {}).air || {}).apres_avarie || 100;
      const es = VML.escale(n.escale);
      if(es) es.enigmes.slice(0, n.indexEnigme).forEach(e => n.resolues[e.id] = { pts: 0, bienDoc: 0, erreurs: 0, indices: 0, fiches: [], ms: 0, premier: false, verif: true });
      document.body.classList.add("mode-verif");
      VML.ETAT = ETAT = n;
      demarrerChrono();
      if(VML.parametre("coffre") === "1"){
        n.escalesFaites = VML.escalesJouables(); n.mots = n.escalesFaites.map(x => VML.escale(x).mot); n.final = true; VML.ouvrirCoffre();
      }
      else if(VML.parametre("fin") === "1"){ n.indexEnigme = es.enigmes.length; finEscale(); }
      else entrerEnigme();
      return;
    }
    accueil();
  };

  if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", VML.demarrer);
  else VML.demarrer();
})();
