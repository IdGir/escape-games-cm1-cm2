/* ============================================================
   MOTEUR DES ÉNIGMES DU NAUTILUS
   ------------------------------------------------------------
   Le rendu et la correction de chaque type viennent du tronc commun
   (commun/js/enigmes.js : tables CORPS et ACTIVATEURS, non modifié),
   plus le type « circuit » (js/type-circuit.js). Ce fichier ajoute
   ce qui est propre au jeu :
     - l'énigme s'ouvre DEPUIS l'objet du décor (panneau de laiton) ;
     - barème du dépôt : 10 du premier coup, 3 après erreur, −2 par
       indice ; on dit COMBIEN de réponses sont justes, jamais lesquelles ;
       aucun texte de correction après la réussite ;
     - justification (Lieutenant, Second) : choisir la phrase de la
       fiche qui prouve la réponse, comptée comme une réponse ;
     - sas anti-tâtonnement : 3 erreurs en 60 s → verrou 20 s, puis
       40 s, puis 80 s (réglable) ; options remélangées à chaque essai ;
     - bonus « Bien documenté » (+2) : réussite du premier coup après
       avoir ouvert la bonne fiche pendant l'énigme ;
     - aide Mousse : premier indice offert, un choix faux écarté
       (QCM), fiche mise en évidence ;
     - indice proposé (jamais imposé) après inactivité ou 2 erreurs.
   ============================================================ */
var VML = window.VML || (window.VML = {});
var PTS_PREMIER_COUP = 10, PTS_APRES_ERREUR = 3;
/* Délais d'animation (divisés par 20 quand les tests posent window.VML_RAPIDE) */
VML.d = ms => (window.VML_RAPIDE ? Math.round(ms / 20) : ms);

VML.BAREME = { premierCoup: 10, apresErreur: 3, indice: 2, bienDocumente: 2, maitreNageur: 5, rapidite: [ { min: 20, pts: 5 }, { min: 25, pts: 3 } ], coffre: { premierCoup: 20, apresErreur: 6 } };

/** État d'une énigme (persistant dans la partie). */
VML.etatEnigme = function(id){
  const E = VML.ETAT;
  E.enigmes = E.enigmes || {};
  return E.enigmes[id] || (E.enigmes[id] = { erreurs: 0, indices: 0, fiches: [], tsErreurs: [], sasNiveau: 0, sasJusqu: 0, ouverte: 0 });
};

/** Une fiche est ouverte : on le note pour l'énigme en cours (bonus) et pour le journal. */
VML.noterFiche = function(idLecon){
  const E = VML.ETAT;
  E.fichesConsultees = E.fichesConsultees || [];
  if(!E.fichesConsultees.includes(idLecon)) E.fichesConsultees.push(idLecon);
  if(VML.enigmeOuverte){
    const s = VML.etatEnigme(VML.enigmeOuverte);
    if(!s.fiches.includes(idLecon)) s.fiches.push(idLecon);
  }
  if(VML.sauver) VML.sauver();
};

VML.manometreSVG = function(valeur, max){
  const a0 = -225, a1 = 45, ang = v => (a0 + (a1 - a0) * v / max) * Math.PI / 180;
  const cx = 90, cy = 90, r = 70;
  let grad = "";
  for(let v = 0; v <= max; v++){
    const a = ang(v);
    grad += `<line x1="${cx + Math.cos(a) * r * .78}" y1="${cy + Math.sin(a) * r * .78}" x2="${cx + Math.cos(a) * r * .95}" y2="${cy + Math.sin(a) * r * .95}" stroke="#2a1a05" stroke-width="2.5"/>`;
    grad += `<text x="${cx + Math.cos(a) * r * .62}" y="${cy + Math.sin(a) * r * .62 + 5}" text-anchor="middle" font-size="14" font-family="Georgia,serif" fill="#2a1a05">${v}</text>`;
    if(v < max){ const b = ang(v + 0.5); grad += `<line x1="${cx + Math.cos(b) * r * .86}" y1="${cy + Math.sin(b) * r * .86}" x2="${cx + Math.cos(b) * r * .95}" y2="${cy + Math.sin(b) * r * .95}" stroke="#2a1a05" stroke-width="1.2"/>`; }
  }
  const a = ang(valeur);
  return `<svg viewBox="0 0 180 180" class="manometre" role="img" aria-label="Manomètre : l'aiguille indique ${valeur} atmosphères">
    <circle cx="${cx}" cy="${cy}" r="86" fill="#b8892e" stroke="#4a3208" stroke-width="4"/>
    <circle cx="${cx}" cy="${cy}" r="76" fill="#f3ead2"/>${grad}
    <text x="${cx}" y="${cy + 40}" text-anchor="middle" font-size="11" font-family="Georgia,serif" fill="#4a3208">atmosphères</text>
    <line x1="${cx}" y1="${cy}" x2="${cx + Math.cos(a) * r * .8}" y2="${cy + Math.sin(a) * r * .8}" stroke="#8a1c12" stroke-width="4" stroke-linecap="round"/>
    <circle cx="${cx}" cy="${cy}" r="7" fill="#4a3208"/></svg>`;
};

/**
 * Ouvre une énigme dans le panneau.
 * @param {object} e   énigme (enigmes.json)
 * @param {object} o   { numero, total, origine:{x,y}, onReussite(bilan), onFermer() }
 */
VML.ouvrirEnigme = function(e, o = {}){
  const g = VML.ETAT.niveau;
  const v = VML.vueEnigme(e, g);
  const s = VML.etatEnigme(e.id);
  if(!s.ouverte) s.ouverte = Date.now();
  VML.enigmeOuverte = e.id;
  const overlay = document.getElementById("panneau-enigme");
  const perso = VML.perso(e.personnage_emetteur) || {};
  const reglages = VML.reglage ? VML.reglage() : {};
  const mousse = VML.aideRenforcee(g);
  const corpsFn = (typeof CORPS !== "undefined" && CORPS[v.type]) || (() => `<p class="feedback erreur show">Type inconnu : ${v.type}</p>`);
  /* Le moteur commun lit e.type et e[niveau] : on lui passe une vue au bon type */
  const ee = Object.assign({}, e, { type: v.type });
  const indicesDispo = reglages.indices !== false;

  overlay.innerHTML = `
    <div class="panneau" role="dialog" aria-modal="true" aria-labelledby="titre-${e.id}">
      <div class="panneau-rivets" aria-hidden="true"></div>
      <div class="enigme-carte" id="enigme-${e.id}" data-type="${v.type}">
        <div class="panneau-tete">
          <span class="enigme-num">Énigme ${o.numero || 1}/${o.total || 1}</span>
          <h3 id="titre-${e.id}">${e.titre}</h3>
          <button class="fermer-panneau" aria-label="Revenir au décor" title="Revenir au décor">✕</button>
        </div>
        <div class="panneau-emetteur">
          ${VML.htmlPortrait(e.personnage_emetteur, "mini")}
          <div><b>${perso.court || perso.nom || ""}</b> — <span class="emetteur-texte">${v.dialogue}</span>
            <div class="episode">📖 ${e.episode_du_roman.split(":")[0]}</div></div>
        </div>
        <div class="bandeau-bareme">🎯 Tout juste du premier coup : <b>${VML.BAREME.premierCoup} points</b> · après une erreur : ${VML.BAREME.apresErreur} points · indice : −${VML.BAREME.indice}</div>
        ${v.consigne ? `<div class="consigne">${v.consigne}</div>` : ""}
        <div class="enigme-corps">${corpsFn(v.donnees, ee)}</div>
        <div class="sas-voile" hidden><div class="sas-boite"><div class="sas-titre">🔒 Sas de sécurité</div><p class="sas-message"></p><div class="sas-compte"></div></div></div>
        <div class="feedback" id="fb-${e.id}" role="status"></div>
        <div class="barre-outils">
          ${indicesDispo ? `<button class="btn-laiton petit" data-indice>💡 ${mousse && s.indices === 0 ? "Indice offert" : "Indice (−" + VML.BAREME.indice + ")"}</button>` : ""}
          ${e.lecon ? `<button class="btn-laiton petit ${mousse ? "mise-en-evidence" : ""}" data-fiche="${e.lecon}">📚 Voir : ${VML.referenceFiche(e.lecon)}</button>` : ""}
        </div>
        <div class="indices-donnes"></div>
      </div>
    </div>`;
  const panneau = overlay.querySelector(".panneau");
  if(o.origine) panneau.style.transformOrigin = `${o.origine.x}px ${o.origine.y}px`;
  overlay.classList.add("ouvert");
  overlay.setAttribute("aria-hidden", "false");
  const carte = overlay.querySelector(".enigme-carte");
  VML.installerPortrait(carte.querySelector(".portrait-ovale"));
  carte.querySelectorAll(".doc-manometre").forEach(m => m.innerHTML = VML.manometreSVG(+m.dataset.valeur, +m.dataset.max || 8));
  const fb = carte.querySelector("#fb-" + e.id);

  /* ---- Justification (Lieutenant, Second) ---- */
  let justifChoix = null;
  if(v.justification){
    const j = v.justification;
    const bloc = document.createElement("div");
    bloc.className = "justif";
    bloc.innerHTML = `<div class="justif-q">🔎 <b>Justification</b> — ${j.question}</div>` +
      melanger(j.options.map((t, i) => ({ t, i }))).map(x => `<label class="justif-option" data-j="${x.i}" tabindex="0">${x.t}</label>`).join("");
    const valider = carte.querySelector("[data-valider]");
    const ancre = valider ? (valider.closest(".center") || valider) : null;
    if(ancre && ancre.parentNode) ancre.parentNode.insertBefore(bloc, ancre); else carte.querySelector(".enigme-corps").appendChild(bloc);
    bloc.addEventListener("click", ev => {
      const opt = ev.target.closest(".justif-option"); if(!opt || carte.classList.contains("resolue")) return;
      bloc.querySelectorAll(".justif-option").forEach(x => x.classList.remove("select"));
      opt.classList.add("select"); justifChoix = +opt.dataset.j;
    });
    bloc.addEventListener("keydown", ev => { if((ev.key === "Enter" || ev.key === " ") && ev.target.classList.contains("justif-option")){ ev.preventDefault(); ev.target.click(); } });
  }

  /* ---- Aide Mousse : un choix faux écarté dans les QCM ---- */
  if(mousse && v.type === "qcm"){
    carte.querySelectorAll(".qcm-question").forEach(q => {
      const bonne = ((v.donnees.questions || [])[+q.dataset.i] || {}).bonne;
      const faux = [...q.querySelectorAll(".qcm-option")].filter(x => +x.dataset.j !== bonne);
      if(faux.length) faux[0].classList.add("ecartee");
    });
    carte.addEventListener("click", ev => { if(ev.target.closest(".ecartee")){ ev.stopPropagation(); ev.preventDefault(); } }, true);
  }

  const montrer = (classe, html, duree) => {
    fb.className = "feedback " + classe + " show"; fb.innerHTML = html;
    clearTimeout(fb._t); if(duree) fb._t = setTimeout(() => fb.classList.remove("show"), duree);
  };
  const remelanger = () => {
    carte.querySelectorAll(".qcm-question").forEach(q => { melanger([...q.querySelectorAll(".qcm-option")]).forEach(x => q.appendChild(x)); });
    carte.querySelectorAll(".justif").forEach(b => { melanger([...b.querySelectorAll(".justif-option")]).forEach(x => b.appendChild(x)); });
    carte.querySelectorAll(".grille-intrus").forEach(gr => { melanger([...gr.children]).forEach(x => gr.appendChild(x)); });
  };

  /* ---- Sas de sécurité ---- */
  const voile = carte.querySelector(".sas-voile");
  const majSas = () => {
    const reste = Math.ceil((s.sasJusqu - Date.now()) / 1000);
    if(reste > 0){
      voile.hidden = false; carte.classList.add("sas-verrouille");
      voile.querySelector(".sas-compte").textContent = reste + " s";
      clearTimeout(voile._t); voile._t = setTimeout(majSas, 250);
    }else{ voile.hidden = true; carte.classList.remove("sas-verrouille"); }
  };
  const declencherSas = () => {
    if(reglages.antiTatonnement === false) return;
    const durees = [20, 40, 80];
    const d = durees[Math.min(s.sasNiveau, durees.length - 1)];
    s.sasNiveau++; s.tsErreurs = [];
    s.sasJusqu = Date.now() + d * 1000;
    VML.ETAT.sasDeclenches = (VML.ETAT.sasDeclenches || 0) + 1;
    const msgs = ((VML.D.dialogues || {}).sas) || ["Sas verrouillé : relisez la fiche."];
    voile.querySelector(".sas-message").textContent = msgs[(s.sasNiveau - 1) % msgs.length];
    if(VML.son) VML.son("sas");
    majSas();
    if(VML.sauver) VML.sauver();
  };
  majSas();

  /* ---- Indice proposé après inactivité ---- */
  const delaiProposition = (reglages.delaiIndiceMin || (["mousse", "matelot"].includes(g) ? 2 : 3)) * 60000;
  let minuteur = null, proposeDeja = false;
  const proposer = () => {
    if(proposeDeja || carte.classList.contains("resolue") || !indicesDispo) return;
    if(s.indices >= v.indices.length) return;
    proposeDeja = true;
    const t = document.createElement("div");
    t.className = "proposition-indice";
    t.innerHTML = `💡 Besoin d'un coup de main ? <button class="btn-laiton petit" data-oui>Voir un indice${mousse && s.indices === 0 ? " (offert)" : " (−" + VML.BAREME.indice + ")"}</button> <button class="btn-laiton petit gris" data-non>Non merci</button>`;
    carte.querySelector(".barre-outils").after(t);
    t.querySelector("[data-oui]").addEventListener("click", () => { t.remove(); donnerIndice(); });
    t.querySelector("[data-non]").addEventListener("click", () => t.remove());
  };
  const relancerMinuteur = () => { clearTimeout(minuteur); if(!carte.classList.contains("resolue")) minuteur = setTimeout(proposer, delaiProposition); };
  carte.addEventListener("click", () => { VML.taire(); relancerMinuteur(); });
  carte.addEventListener("keydown", relancerMinuteur);
  relancerMinuteur();

  /* ---- Indices ---- */
  const zoneIndices = carte.querySelector(".indices-donnes");
  const afficherIndices = () => {
    zoneIndices.innerHTML = v.indices.slice(0, s.indices).map(t => `<div class="feedback indice show">💡 ${t}</div>`).join("");
  };
  afficherIndices();
  const btnIndice = carte.querySelector("[data-indice]");
  const majBoutonIndice = () => {
    if(!btnIndice) return;
    if(s.indices >= v.indices.length){ btnIndice.textContent = "💡 Plus d'indice"; btnIndice.disabled = true; }
    else btnIndice.textContent = "💡 " + (mousse && s.indices === 0 ? "Indice offert" : "Indice (−" + VML.BAREME.indice + ")");
  };
  const donnerIndice = () => {
    if(s.indices >= v.indices.length || carte.classList.contains("resolue")) return;
    const gratuit = mousse && s.indices === 0;
    s.indices++;
    if(!gratuit){
      VML.ETAT.score = Math.max(0, (VML.ETAT.score || 0) - VML.BAREME.indice);
      VML.ETAT.indicesTotal = (VML.ETAT.indicesTotal || 0) + 1;
      VML.ETAT.indicesEscale = (VML.ETAT.indicesEscale || 0) + 1;
      if(VML.perteAir) VML.perteAir("indice");
    }else s.indiceOffert = true;
    if(VML.son) VML.son("indice");
    afficherIndices(); majBoutonIndice();
    if(VML.majHUD) VML.majHUD();
    if(VML.sauver) VML.sauver();
  };
  if(btnIndice) btnIndice.addEventListener("click", donnerIndice);
  majBoutonIndice();

  const btnFiche = carte.querySelector("[data-fiche]");
  if(btnFiche) btnFiche.addEventListener("click", () => VML.ouvrirBibliotheque(btnFiche.dataset.fiche));

  const fermer = () => {
    clearTimeout(minuteur); clearTimeout(voile._t);
    overlay.classList.remove("ouvert"); overlay.setAttribute("aria-hidden", "true");
    overlay.innerHTML = ""; VML.enigmeOuverte = null;
    document.removeEventListener("keydown", echap);
  };
  const echap = ev => { if(ev.key === "Escape" && !document.querySelector(".biblio.ouverte")){ fermer(); if(o.onFermer) o.onFermer(); } };
  document.addEventListener("keydown", echap);
  carte.querySelector(".fermer-panneau").addEventListener("click", () => { fermer(); if(o.onFermer) o.onFermer(); });

  /* ---- API de correction passée à l'activateur ---- */
  let resolu = false;
  const justifOk = () => !v.justification || justifChoix === v.justification.bonne;
  const api = {
    incomplet(msg){ if(!resolu) montrer("indice", "✋ " + msg, 2600); },
    erreur(justes, total, unites, message){
      if(resolu) return;
      if(Date.now() < s.sasJusqu) return;
      if(v.justification && justifChoix === null){ api.incomplet("Choisis aussi la phrase qui justifie ta réponse."); return; }
      let detail;
      if(v.justification){
        justes = (justes || 0) + (justifOk() ? 1 : 0); total = (total || 1) + 1;
        detail = `${justes} réponse${justes > 1 ? "s" : ""} juste${justes > 1 ? "s" : ""} sur ${total} (la justification compte pour une).`;
      }else detail = message || (unites ? `${justes} ${justes > 1 ? unites[1] : unites[0]} sur ${total}.` : "");
      s.erreurs++;
      VML.ETAT.erreursTotal = (VML.ETAT.erreursTotal || 0) + 1;
      const now = Date.now();
      s.tsErreurs = (s.tsErreurs || []).filter(t => now - t < 60000); s.tsErreurs.push(now);
      if(VML.son) VML.son("erreur");
      carte.classList.remove("secoue"); void carte.offsetWidth; carte.classList.add("secoue");
      const perte = s.erreurs === 1 ? `<div class="perte-bonus">Le bonus du premier coup est perdu : cette énigme ne rapportera plus que ${VML.BAREME.apresErreur} points. Vérifie dans la fiche avant de revalider.</div>` : "";
      montrer("erreur", `✗ <b>Pas tout juste.</b> ${detail}${perte}`, 0);
      remelanger();
      if(s.tsErreurs.length >= 3) declencherSas();
      if(s.erreurs === 2) setTimeout(proposer, 1200);
      if(VML.sauver) VML.sauver();
    },
    reussir(){
      if(resolu) return;
      if(Date.now() < s.sasJusqu) return;
      if(v.justification && justifChoix === null){ api.incomplet("Choisis aussi la phrase qui justifie ta réponse."); return; }
      if(!justifOk()){ api.erreur(null, null, null); return; }
      resolu = true;
      clearTimeout(minuteur);
      const premier = s.erreurs === 0;
      const pts = premier ? VML.BAREME.premierCoup : VML.BAREME.apresErreur;
      const bienDoc = premier && e.lecon && s.fiches.includes(e.lecon) ? VML.BAREME.bienDocumente : 0;
      VML.ETAT.score = (VML.ETAT.score || 0) + pts + bienDoc;
      VML.ETAT.resolues = VML.ETAT.resolues || {};
      VML.ETAT.resolues[e.id] = { pts, bienDoc, erreurs: s.erreurs, indices: s.indices, fiches: s.fiches.slice(), ms: Date.now() - s.ouverte, premier };
      if(VML.son) VML.son("succes");
      carte.classList.add("resolue");
      carte.querySelectorAll("[data-valider], [data-indice]").forEach(b => b.disabled = true);
      montrer(premier ? "succes premier-coup" : "succes",
        (premier ? `🎯 <b>Tout juste du premier coup !</b> <b>+${pts} points</b>` : `✔ Résolue : <b>+${pts} points</b>.`) +
        (bienDoc ? ` <span class="badge-doc">📚 Bien documenté +${bienDoc}</span>` : ""), 0);
      if(VML.majHUD) VML.majHUD();
      if(VML.sauver) VML.sauver();
      setTimeout(() => { fermer(); if(o.onReussite) o.onReussite(VML.ETAT.resolues[e.id]); }, VML.d(1300));
    }
  };
  VML._apiCourante = api;      // pour les tests
  const act = (typeof ACTIVATEURS !== "undefined" && ACTIVATEURS[v.type]) || (() => {});
  act(ee, v.donnees, api);
  setTimeout(() => { const f = carte.querySelector("button, [tabindex]"); if(f && f.focus) f.focus(); }, 50);
  return { carte, fermer, api };
};
