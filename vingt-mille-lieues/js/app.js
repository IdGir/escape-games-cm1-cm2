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
VML.CLE_PARTIE = "vml_partie";

(function(){
  const $ = s => document.querySelector(s);
  let scene = null, tic = null, dernierTic = 0, insiste = null;

  const nouvelEtat = (equipe, niveau) => ({
    version: 1, equipe, niveau, escale: 2, indexEnigme: 0, score: 0, resolues: {}, enigmes: {},
    fichesConsultees: [], indicesTotal: 0, indicesEscale: 0, erreursTotal: 0, msEcoules: 0,
    debut: Date.now(), enPause: false, escaleTerminee: false, mots: [], motVu: false, bonus: {},
    air: 100, introVue: false, delaiAccordeMin: 0
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
  const pompeEnMarche = () => !!(VML.ETAT.resolues || {})["e2-2"];

  function demarrerChrono(){
    clearInterval(tic); dernierTic = Date.now();
    tic = setInterval(() => {
      const E = VML.ETAT, now = Date.now(), dt = now - dernierTic; dernierTic = now;
      if(!E || E.enPause || E.escaleTerminee || document.body.dataset.ecran !== "ecran-jeu") return;
      E.msEcoules = (E.msEcoules || 0) + dt;
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
    if(etat.escaleTerminee){ finEscale(true); return; }
    if(!etat.introVue){ VML.jouerCinematique("transition-e2").then(() => { VML.ETAT.introVue = true; VML.sauver(); entrerEnigme(); }); }
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
        hote.classList.remove("mvt-zoom", "mvt-glisse", "mvt-secousse"); void hote.offsetWidth;
        hote.classList.add("mvt-" + (p.mouvement || "zoom"));
        if(p.effet === "coupure"){ hote.classList.add("coupure"); if(VML.son) VML.son("alarme"); VML.ETAT.air = ((VML.escale(VML.ETAT.escale) || {}).air || {}).apres_avarie || 62; VML.majHUD(); }
        st.innerHTML = sousTitre(p);
        const portrait = st.querySelector(".portrait-ovale"); if(portrait) VML.installerPortrait(portrait);
        await Promise.race([
          Promise.all([p.personnage ? VML.dire(p.personnage, p.texte, portrait) : Promise.resolve(), new Promise(r => setTimeout(r, p.duree * 1000))]),
          fin
        ]);
      }
      sc.detruire();
    };
    await Promise.race([jouer(), fin]);
    appliquerEffetsCine(c);
    ov.innerHTML = "";
  };
  function sousTitre(p){
    const pe = p.personnage ? VML.perso(p.personnage) : null;
    return (p.personnage ? VML.htmlPortrait(p.personnage, "cine") : "") + `<div><b>${pe ? pe.court || pe.nom : ""}</b> ${pe ? "— " : ""}<span>${p.texte}</span></div>`;
  }
  function appliquerEffetsCine(c){
    if(c.plans.some(p => p.effet === "coupure") && VML.ETAT && !VML.ETAT.introVue){
      VML.ETAT.air = ((VML.escale(VML.ETAT.escale) || {}).air || {}).apres_avarie || 62;
    }
  }

  /* ---------------- Escale ---------------- */
  function etatDecor(decor){
    const r = VML.ETAT.resolues || {};
    if(decor === "carre") return r["e2-1"] ? "normal" : "panne";
    if(decor === "machines" || decor === "salon") return r["e2-2"] ? (r["e2-4"] ? "victoire" : "normal") : "panne";
    return "normal";
  }

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
    if(re.effet === "lumiere" || re.effet === "hublots") E.air = re.effet === "hublots" ? 100 : E.air;
    scene.reaction(re.effet, e.objet_principal);
    VML.masquerPlaque($("#plaque"));
    E.indexEnigme++;
    VML.sauver();
    VML.majHUD();
    setTimeout(() => {
      scene.viderReactions();
      if(E.indexEnigme >= VML.escale(E.escale).enigmes.length){
        VML.jouerCinematique("fin-e2").then(() => finEscale());
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
      E.bonus = E.bonus || {};
      if((E.indicesEscale || 0) === 0) E.bonus.maitreNageur = B.maitreNageur;
      const ref = (VML.reglage("dureeEscaleMin") || 25) + (E.delaiAccordeMin || 0);
      const min = (E.msEcoules || 0) / 60000;
      const rap = min <= ref - 5 ? B.rapidite[0].pts : min <= ref ? B.rapidite[1].pts : 0;
      if(rap) E.bonus.rapidite = rap;
      E.score = (E.score || 0) + (E.bonus.maitreNageur || 0) + (E.bonus.rapidite || 0);
      if(!(E.mots || []).includes(es.mot)) E.mots = (E.mots || []).concat([es.mot]);
      VML.sauver();
      VML.memoriserCompteRendu();
      if(VML.envoyerEtat) VML.envoyerEtat();
    }
    VML.aller("ecran-fin");
    VML.majHUD();
    const f = $("#fin-contenu");
    const d = ((VML.D.dialogues || {}).fin_escale || {})[E.escale];
    const g = VML.gradeSuivant(E.niveau);
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
        <p class="bilan-score">Score : <b>${E.score}</b> / ${VML.scoreMaxEscale(E.escale)}</p>
        <p>${E.bonus && E.bonus.maitreNageur ? "🏊 <b>Maître-nageur</b> : escale sans indice, +" + E.bonus.maitreNageur + " · " : ""}${E.bonus && E.bonus.rapidite ? "⏱️ <b>Rapidité</b> +" + E.bonus.rapidite + " · " : ""}📚 Bien documenté : ${Object.values(E.resolues || {}).filter(r => r.bienDoc).length} fois</p>
        ${VML.htmlJournal()}
        <div class="boutons-fin">
          ${g ? `<button class="btn-laiton" id="btn-plonger">🌊 Plonger plus profond : rejouer en ${VML.infoGrade(g).icone} ${VML.infoGrade(g).nom}</button>` : ""}
          <button class="btn-laiton" id="btn-imprimer-journal">🖨️ Imprimer le journal de bord</button>
          <button class="btn-laiton gris" disabled title="Les autres escales seront produites après validation de l'escale pilote">🗺️ Escale 3 — en préparation</button>
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
    if(bp) bp.onclick = () => {
      const n = nouvelEtat(E.equipe, g);
      n.mots = E.mots.slice(); n.motVu = true; n.introVue = true; n.air = 62;
      lancer(n);
    };
    $("#btn-imprimer-journal").onclick = () => VML.imprimer(VML.htmlJournal(), "Journal de bord");
  }

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
      const n = nouvelEtat("Vérification", g);
      n.escale = +(VML.parametre("escale") || 2);
      n.indexEnigme = Math.max(0, (+(VML.parametre("enigme") || 1)) - 1);
      n.introVue = true; n.air = 62;
      const es = VML.escale(n.escale);
      if(es) es.enigmes.slice(0, n.indexEnigme).forEach(e => n.resolues[e.id] = { pts: 0, bienDoc: 0, erreurs: 0, indices: 0, fiches: [], ms: 0, premier: false, verif: true });
      document.body.classList.add("mode-verif");
      VML.ETAT = ETAT = n;
      demarrerChrono();
      if(VML.parametre("fin") === "1"){ n.indexEnigme = es.enigmes.length; finEscale(); }
      else entrerEnigme();
      return;
    }
    accueil();
  };

  if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", VML.demarrer);
  else VML.demarrer();
})();
