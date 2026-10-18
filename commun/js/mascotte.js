/* ============================================================
   MASCOTTE COMMUNE « NOA » (amélioration N11) — tronc commun
   ------------------------------------------------------------
   Chaque jeu a ses personnages, liés à son époque ou à son lieu ; rien ne
   relie les jeux entre eux pour l'élève. Noa, guide de la collection, est
   le même personnage dans tous les jeux — avec trois rôles seulement :
     1. ACCUEILLIR la classe : sur l'accueil de la collection (index.html)
        et sur l'écran d'accueil de chaque jeu ;
     2. expliquer les règles communes (« ❓ Comment jouer ? » : barème, coffre,
        indices), ouvertes d'office au PREMIER lancement ;
     3. ANNONCER les trophées gagnés (N1) à l'écran de fin.
   Elle ne parle JAMAIS pendant les énigmes : elle n'apparaît que sur les écrans
   d'accueil et de fin, et sa voix s'arrête dès que la partie démarre.
   Portrait : personnage ORIGINAL (ni personnage existant, ni personne réelle),
   viewBox 200 × 320, même squelette que les personnages des jeux (charte B1 :
   .tete .yeux .paupiere .bouche .sourcils .buste .bras-g/-d .avant-g/-d
   .main-g/-d .jambes), carnation « hâlée » de la palette ; animé au repos
   (respiration, clignement) et quand elle parle (bouche, salut de la main).
   Voix : synthèse vocale du navigateur (comme narration.js, dont elle respecte
   « narration active » et le volume) ; sous-titres : le texte reste affiché.
   Réglage : ⚙️ Réglages → 🧑‍🎓 Mascotte (activée avec voix · sans voix · désactivée),
   ou ✕ sur Noa ; gardé sur l'appareil. AUCUN effet sur le score ni sur le jeu.
   Textes : commun/donnees/mascotte.js. Chargé après app.js, trophees.js.
   ============================================================ */
(function(){
  const T = window.MASCOTTE_TEXTES;
  if(!T) return;
  const CLE = "escape_mascotte";
  const MODES = { voix: "Activée, avec la voix", muette: "Activée, sans la voix", off: "Désactivée" };
  const esc = s => String(s == null ? "" : s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  /* jeu classique (ETAT, #input-equipe) ou variante immersive (VML, #nom-equipe) */
  const immersif = !!window.VML && !!document.getElementById("nom-equipe");
  const champEquipe = () => document.getElementById("input-equipe") || document.getElementById("nom-equipe");
  const estJeu = (typeof ETAT !== "undefined" || immersif) && !!champEquipe();
  const verification = () => { const q = new URLSearchParams(location.search); return !!(q.get("salle") || q.get("verif")); };

  /* ---------------- Réglage (gardé sur l'appareil) ---------------- */
  const lire = () => { try{ const r = JSON.parse(localStorage.getItem(CLE) || "{}") || {}; return { mode: MODES[r.mode] ? r.mode : "voix", vu: !!r.vu }; }catch(e){ return { mode: "voix", vu: false }; } };
  const ecrire = r => { try{ localStorage.setItem(CLE, JSON.stringify(r)); }catch(e){} };
  const mode = () => lire().mode;
  const regler = m => { const r = lire(); r.mode = MODES[m] ? m : "voix"; ecrire(r); rafraichir(); };
  const marquerVu = () => { const r = lire(); if(!r.vu){ r.vu = true; ecrire(r); } };
  const voixPossible = () => mode() === "voix" && "speechSynthesis" in window && !(estJeu && window.NARRATION && window.NARRATION.parlerActif === false) && !(immersif && window.VML.reglage && window.VML.reglage("voix") === false);
  function bareme(){
    const b = Object.assign({}, T.bareme);
    try{
      if(typeof PTS_PREMIER_COUP !== "undefined") b.premier = PTS_PREMIER_COUP;
      if(typeof PTS_APRES_ERREUR !== "undefined") b.apres = PTS_APRES_ERREUR;
      if(typeof MALUS_INDICE !== "undefined") b.indice = MALUS_INDICE;
      if(typeof PTS_COFFRE_PREMIER !== "undefined") b.coffre = PTS_COFFRE_PREMIER;
      if(window.VML && window.VML.BAREME){ const B = window.VML.BAREME; b.premier = B.premierCoup; b.apres = B.apresErreur; b.indice = B.indice; b.coffre = B.coffre.premierCoup; }
    }catch(e){}
    return b;
  }

  /* ---------------- Le portrait : SVG 200 × 320, squelette commun ---------------- */
  const PEAU_HALE = ["#e2b183", "#c48f5e"];                 // carnation « hale » de la charte
  function svgNoa(){
    const P = PEAU_HALE;
    return `<svg class="mascotte-svg perso-plein" viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMax meet" aria-hidden="true" focusable="false">
  <defs>
    <radialGradient id="noaFond" cx="50%" cy="32%" r="78%"><stop offset="0%" stop-color="#3a5c9a"/><stop offset="100%" stop-color="#101a38"/></radialGradient>
    <linearGradient id="noaPeau" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="${P[0]}"/><stop offset="100%" stop-color="${P[1]}"/></linearGradient>
    <linearGradient id="noaGilet" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#2f7f86"/><stop offset="100%" stop-color="#1d5560"/></linearGradient>
    <linearGradient id="noaPantalon" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#c9a46a"/><stop offset="100%" stop-color="#9a7a45"/></linearGradient>
  </defs>
  <rect width="200" height="320" fill="url(#noaFond)"/>
  <ellipse cx="100" cy="308" rx="50" ry="9" fill="#000" opacity=".35"/>
  <g class="perso-corps">
    <g class="jambes">
      <path d="M76 212 L70 292 L90 292 L94 212 Z" fill="url(#noaPantalon)"/>
      <path d="M106 212 L110 292 L130 292 L124 212 Z" fill="url(#noaPantalon)"/>
      <path d="M68 270 L92 270 L92 292 L68 292 Z" fill="#5a3a22"/><path d="M108 270 L132 270 L132 292 L108 292 Z" fill="#5a3a22"/>
      <ellipse cx="80" cy="298" rx="16" ry="7" fill="#5a3a22"/><ellipse cx="120" cy="298" rx="16" ry="7" fill="#5a3a22"/>
    </g>
    <g class="bras bras-g">
      <path d="M70 152 Q58 180 54 206" stroke="url(#noaGilet)" stroke-width="15" fill="none" stroke-linecap="round"/>
      <g class="avant-g">
        <path d="M54 206 Q52 222 56 236" stroke="#fff4dc" stroke-width="13" fill="none" stroke-linecap="round"/>
        <circle class="main-g" cx="57" cy="242" r="9" fill="url(#noaPeau)"/>
      </g>
    </g>
    <g class="buste">
      <path d="M70 148 Q68 134 80 128 L120 128 Q132 134 130 148 L134 214 Q100 222 66 214 Z" fill="url(#noaGilet)"/>
      <path d="M88 126 L100 150 L112 126 Z" fill="#fff4dc"/>
      <path d="M90 126 L100 140 L110 126 Z" fill="url(#noaPeau)"/>
      <path d="M76 134 L124 208" stroke="#7a4b24" stroke-width="7" stroke-linecap="round"/>
      <rect x="110" y="190" width="32" height="26" rx="4" fill="#8a5a2b" stroke="#5a3a22" stroke-width="2"/><circle cx="126" cy="200" r="3.2" fill="#c9a227"/>
      <circle cx="94" cy="166" r="2.6" fill="#c9a227"/><circle cx="94" cy="182" r="2.6" fill="#c9a227"/><circle cx="94" cy="198" r="2.6" fill="#c9a227"/>
    </g>
    <g class="bras bras-d">
      <path d="M130 152 Q142 180 146 206" stroke="url(#noaGilet)" stroke-width="15" fill="none" stroke-linecap="round"/>
      <g class="avant-d">
        <path d="M146 206 Q148 222 144 236" stroke="#fff4dc" stroke-width="13" fill="none" stroke-linecap="round"/>
        <circle class="main-d" cx="143" cy="242" r="9" fill="url(#noaPeau)"/>
        <g transform="translate(146,232) rotate(-18)"><circle cx="0" cy="-13" r="6.5" fill="none" stroke="#e6c757" stroke-width="3.2"/><rect x="-1.6" y="-7" width="3.2" height="22" fill="#e6c757"/><rect x="1.6" y="7" width="6" height="3.2" fill="#e6c757"/><rect x="1.6" y="12" width="4" height="3" fill="#e6c757"/></g>
      </g>
    </g>
    <g class="tete">
      <rect x="92" y="112" width="16" height="18" fill="url(#noaPeau)"/>
      <path d="M67 90 Q62 56 100 48 Q138 56 133 90 Q130 66 100 62 Q70 66 67 90 Z" fill="#3b2a1e"/>
      <ellipse cx="69" cy="88" rx="5" ry="8" fill="url(#noaPeau)"/><ellipse cx="131" cy="88" rx="5" ry="8" fill="url(#noaPeau)"/>
      <ellipse cx="100" cy="86" rx="31" ry="36" fill="url(#noaPeau)"/>
      <ellipse cx="82" cy="97" rx="8" ry="5" fill="#e79a97" opacity=".35"/><ellipse cx="118" cy="97" rx="8" ry="5" fill="#e79a97" opacity=".35"/>
      <g class="sourcils">
        <path d="M82 74 Q88 70 94 74" stroke="#3a2a1a" stroke-width="2.4" fill="none" stroke-linecap="round"/>
        <path d="M106 74 Q112 70 118 74" stroke="#3a2a1a" stroke-width="2.4" fill="none" stroke-linecap="round"/>
      </g>
      <g class="yeux">
        <ellipse cx="88" cy="83" rx="6" ry="4.6" fill="#fff"/><ellipse cx="112" cy="83" rx="6" ry="4.6" fill="#fff"/>
        <circle cx="88" cy="83" r="3" fill="#3a2a1a"/><circle cx="112" cy="83" r="3" fill="#3a2a1a"/>
        <circle cx="89.2" cy="81.8" r="1.1" fill="#fff"/><circle cx="113.2" cy="81.8" r="1.1" fill="#fff"/>
        <ellipse class="paupiere" cx="88" cy="83" rx="6.3" ry="4.9" fill="url(#noaPeau)"/><ellipse class="paupiere" cx="112" cy="83" rx="6.3" ry="4.9" fill="url(#noaPeau)"/>
      </g>
      <path d="M100 88 Q97 95 101 97" stroke="#c89a70" stroke-width="2" fill="none" stroke-linecap="round"/>
      <ellipse class="bouche bouche-ouverte" cx="100" cy="107" rx="7" ry="4" fill="#a8434a"/>
      <path class="bouche-fermee" d="M93 106 Q100 111 107 106" stroke="#8d3a40" stroke-width="2" fill="none" stroke-linecap="round"/>
      <path d="M66 70 Q70 44 100 42 Q130 44 134 70 Q100 60 66 70 Z" fill="#1f3b73"/>
      <path d="M96 68 Q124 62 146 74 Q124 80 96 76 Z" fill="#162c58"/>
      <circle cx="100" cy="53" r="5.5" fill="#e6c757"/><circle cx="100" cy="53" r="2.2" fill="#1f3b73"/>
    </g>
  </g>
</svg>`;
  }

  /* ---------------- Voix et bouche animée ---------------- */
  let parole = null, timerBouche = null, portraitParlant = null;
  function arreterBouche(){
    if(timerBouche){ clearInterval(timerBouche); timerBouche = null; }
    if(portraitParlant){ portraitParlant.classList.remove("parle", "bouche-on"); portraitParlant = null; }
  }
  function silence(){
    if(parole){ try{ speechSynthesis.cancel(); }catch(e){} parole = null; }
    arreterBouche();
  }
  function choisirVoix(){
    let voix = [];
    try{ voix = speechSynthesis.getVoices().filter(v => /^fr/i.test(v.lang) || /fran/i.test(v.name)); }catch(e){}
    const f = voix.find(v => /am[ée]lie|julie|marie|virginie|google fran[çc]ais|female|femme/i.test(v.name));
    return f || voix[0] || null;
  }
  /** Lit un texte à voix haute (si la voix est activée) ; le portrait « parle ». Renvoie true si la lecture démarre. */
  function parler(texte, portrait){
    if(!voixPossible()) return false;
    silence();
    const u = new SpeechSynthesisUtterance(String(texte).replace(/\s+/g, " ").trim());
    u.lang = "fr-FR"; u.rate = 0.97; u.pitch = 1.12;
    u.volume = (window.NARRATION && typeof window.NARRATION.volume === "number") ? window.NARRATION.volume : 1;
    const v = choisirVoix(); if(v) u.voice = v;
    const fin = () => { if(parole === u){ parole = null; arreterBouche(); } };
    u.onstart = () => {
      portraitParlant = portrait; portrait.classList.add("parle");
      timerBouche = setInterval(() => portrait.classList.toggle("bouche-on"), 140);
    };
    u.onend = fin; u.onerror = fin;
    parole = u;
    try{ speechSynthesis.speak(u); }catch(e){ parole = null; return false; }
    return true;
  }

  /* ---------------- Styles ---------------- */
  function styles(){
    if(document.getElementById("style-mascotte")) return;
    const s = document.createElement("style"); s.id = "style-mascotte";
    s.textContent = `
      .mascotte-bloc{display:flex;gap:14px;align-items:flex-end;max-width:760px;margin:16px auto;text-align:left}
      .mascotte-portrait{flex:0 0 auto;width:96px;height:154px;border-radius:12px 12px 8px 8px;overflow:hidden;border:3px solid #c9a227;background:#101a38;box-shadow:0 6px 16px rgba(0,0,0,.35)}
      .mascotte-portrait .mascotte-svg{display:block;width:100%;height:100%}
      .mascotte-bulle{position:relative;flex:1;min-width:0;background:#fffdf6;color:#2b1d10;border:2px solid #c9a227;border-radius:14px;padding:10px 14px;font-size:.98rem;line-height:1.45}
      .mascotte-bulle::before{content:"";position:absolute;left:-10px;bottom:22px;width:16px;height:16px;background:#fffdf6;border-left:2px solid #c9a227;border-bottom:2px solid #c9a227;transform:rotate(45deg)}
      .mascotte-nom{font-weight:bold;color:#1d3a8a}.mascotte-nom small{font-weight:normal;opacity:.75;margin-left:6px}
      .mascotte-texte{margin:4px 0 8px}
      .mascotte-actions{display:flex;flex-wrap:wrap;gap:6px}
      .mascotte-actions button,.mascotte-rappel,.mascotte-lire-regles{font:inherit;font-size:.85rem;border:2px solid #c9a227;background:#fff8e1;color:#2b1d10;border-radius:999px;padding:3px 12px;cursor:pointer}
      .mascotte-actions .mascotte-masquer{border-color:#bbb;background:#f3f3f3;padding:3px 9px}
      .mascotte-rappel{display:block;margin:10px auto}
      .mascotte-regles{margin-top:8px;border-top:1px dashed #c9a227;padding-top:6px}
      .mascotte-regles ul{list-style:none;margin:0 0 6px;padding:0}.mascotte-regles li{margin:5px 0}
      .mascotte-regles li b{color:#1d3a8a}
      .mascotte-trophee{display:flex;gap:10px;align-items:flex-end;margin:10px auto;max-width:620px;text-align:left}
      .mascotte-trophee .mascotte-portrait{width:64px;height:102px}
      .mascotte-trophee .mascotte-bulle{font-size:.95rem}
      /* animation : respiration, clignement, parole (tout s'arrête avec « animations réduites ») */
      .mascotte-svg .tete,.mascotte-svg .buste,.mascotte-svg .bras,.mascotte-svg .avant-g,.mascotte-svg .avant-d,.mascotte-svg .perso-corps{transform-box:fill-box}
      .mascotte-svg .buste{transform-origin:50% 100%;animation:mascotte-respire 4.2s ease-in-out infinite}
      .mascotte-svg .tete{transform-origin:50% 92%}
      .mascotte-svg .bras{transform-origin:50% 6%}.mascotte-svg .avant-d{transform-origin:50% 8%}
      .mascotte-svg .yeux .paupiere{transform-box:fill-box;transform-origin:50% 0%;transform:scaleY(0);animation:mascotte-cligne 5.2s infinite ease-in-out}
      .mascotte-svg .bouche-ouverte{opacity:0}.mascotte-svg .bouche-fermee{opacity:1}
      .mascotte-portrait.parle.bouche-on .bouche-ouverte{opacity:1}.mascotte-portrait.parle.bouche-on .bouche-fermee{opacity:0}
      .mascotte-portrait.parle .tete{animation:mascotte-tete 2s ease-in-out infinite}
      .mascotte-portrait.parle .bras-d{animation:mascotte-salue 1.6s ease-in-out infinite}
      @keyframes mascotte-respire{0%,100%{transform:scaleY(1) translateY(0)}50%{transform:scaleY(1.018) translateY(-1.2px)}}
      @keyframes mascotte-cligne{0%,41%,100%{transform:scaleY(0)}43%,44%{transform:scaleY(1)}46%,88%{transform:scaleY(0)}90%,91%{transform:scaleY(1)}93%{transform:scaleY(0)}}
      @keyframes mascotte-tete{0%,100%{transform:rotate(0)}30%{transform:rotate(1.6deg)}65%{transform:rotate(-1.2deg)}}
      @keyframes mascotte-salue{0%,100%{transform:rotate(0)}25%{transform:rotate(-34deg)}50%{transform:rotate(-20deg)}75%{transform:rotate(-34deg)}}
      body.calme .mascotte-svg *,body.calme .mascotte-portrait *,body.anim-reduites .mascotte-svg *,body.anim-reduites .mascotte-portrait *{animation:none!important}
      @media (max-width:520px){.mascotte-bloc{flex-direction:column;align-items:center}.mascotte-bulle::before{display:none}.mascotte-portrait{width:84px;height:134px}}`;
    document.head.appendChild(s);
  }

  /* ---------------- Le bloc d'accueil ---------------- */
  function reglesHTML(){
    return `<ul>${T.regles(bareme()).map(r => `<li>${r.icone} <b>${esc(r.titre)}</b> — ${esc(r.texte)}</li>`).join("")}</ul>
      ${voixPossible() ? `<button type="button" class="mascotte-lire-regles">🔊 Lire les règles</button>` : ""}`;
  }
  function bloc(texte, ouvrirRegles){
    const el = document.createElement("aside");
    el.className = "mascotte-bloc"; el.id = "mascotte-bloc";
    el.setAttribute("aria-label", T.nom + ", " + T.role.toLowerCase());
    el.innerHTML = `<div class="mascotte-portrait">${svgNoa()}</div>
      <div class="mascotte-bulle">
        <div class="mascotte-nom">${esc(T.nom)} <small>${esc(T.role)}</small></div>
        <p class="mascotte-texte">${esc(texte)}</p>
        <div class="mascotte-actions">
          ${voixPossible() ? `<button type="button" class="mascotte-ecouter">🔊 Écouter</button>` : ""}
          <button type="button" class="mascotte-regles-btn" aria-expanded="${!!ouvrirRegles}">❓ Comment jouer ?</button>
          <button type="button" class="mascotte-masquer" title="Masquer Noa (à remettre dans ⚙️ Réglages ou avec le bouton « Réafficher Noa »)" aria-label="Masquer Noa">✕</button>
        </div>
        <div class="mascotte-regles" ${ouvrirRegles ? "" : "hidden"}>${reglesHTML()}</div>
      </div>`;
    const portrait = el.querySelector(".mascotte-portrait");
    const e = el.querySelector(".mascotte-ecouter");
    if(e) e.addEventListener("click", () => { if(!parler(texte, portrait)) silence(); });
    el.querySelector(".mascotte-regles-btn").addEventListener("click", ev => {
      const r = el.querySelector(".mascotte-regles"), ouvert = r.hidden;
      r.hidden = !ouvert; ev.currentTarget.setAttribute("aria-expanded", String(ouvert));
      if(ouvert) marquerVu();
      if(!ouvert) silence();
    });
    el.addEventListener("click", ev => {
      const l = ev.target.closest(".mascotte-lire-regles");
      if(l && !parler(T.lectureRegles(bareme()), portrait)) silence();
    });
    el.querySelector(".mascotte-masquer").addEventListener("click", () => { silence(); regler("off"); });
    return el;
  }
  const rappel = () => {
    const b = document.createElement("button");
    b.type = "button"; b.className = "mascotte-rappel"; b.id = "mascotte-rappel";
    b.textContent = "🧑‍🎓 Réafficher Noa, le guide de la collection";
    b.addEventListener("click", () => regler("voix"));
    return b;
  };

  /** Place (ou remplace) Noa sur l'écran d'accueil, selon le réglage. */
  function rafraichir(){
    document.querySelectorAll("#mascotte-bloc, #mascotte-rappel").forEach(x => x.remove());
    silence();
    let point = null, texte = "", ouvrir = false;
    const m = mode(), vu = lire().vu;
    if(estJeu){
      const inp = champEquipe();
      const h = inp && inp.previousElementSibling && /^(H[1-6]|LABEL)$/.test(inp.previousElementSibling.tagName) ? inp.previousElementSibling : inp;
      point = h; texte = vu ? T.retour : T.accueilJeu; ouvrir = !vu;
    }else{
      point = document.getElementById("mascotte-accueil");
      const n = (typeof CATALOGUE !== "undefined" && CATALOGUE.jeux) ? CATALOGUE.jeux.filter(j => j.dossier).length : 0;
      texte = T.accueilCollection(n); ouvrir = !vu;
    }
    if(!point) return;
    styles();
    if(m === "off"){ if(estJeu) point.before(rappel()); else point.appendChild(rappel()); return; }
    const b = bloc(texte, ouvrir);
    if(estJeu) point.before(b); else point.appendChild(b);
  }

  /* ---------------- Fin de partie : annonce des trophées ---------------- */
  function annoncerTrophees(){
    if(mode() === "off" || verification()) return;
    const sec = document.getElementById("trophees-fin"); if(!sec) return;
    const noms = [...sec.querySelectorAll(".tr.nouveau b")].map(b => b.textContent.trim());
    const ancien = sec.querySelector(".mascotte-trophee");
    if(!noms.length){ if(ancien) ancien.remove(); return; }
    const texte = T.trophees(noms);
    if(ancien && ancien.dataset.texte === texte) return;
    if(ancien) ancien.remove();
    styles();
    const el = document.createElement("div");
    el.className = "mascotte-trophee"; el.dataset.texte = texte;
    el.innerHTML = `<div class="mascotte-portrait">${svgNoa()}</div>
      <div class="mascotte-bulle"><div class="mascotte-nom">${esc(T.nom)}</div><p class="mascotte-texte" style="margin-bottom:4px">${esc(texte)}</p>
        ${voixPossible() ? `<div class="mascotte-actions"><button type="button" class="mascotte-ecouter">🔊 Écouter</button></div>` : ""}</div>`;
    const b = el.querySelector(".mascotte-ecouter");
    if(b) b.addEventListener("click", () => { if(!parler(texte, el.querySelector(".mascotte-portrait"))) silence(); });
    const t = sec.querySelector("h2");
    if(t) t.after(el); else sec.prepend(el);
  }
  if(estJeu && typeof window.finDuJeu === "function"){
    const origine = window.finDuJeu;
    window.finDuJeu = function(){
      const r = origine.apply(this, arguments);
      silence();
      annoncerTrophees();
      const c = document.getElementById("fin-contenu");
      if(c && window.MutationObserver) new MutationObserver(() => annoncerTrophees()).observe(c, { childList: true, subtree: true });   // le quizz final recalcule les trophées
      return r;
    };
  }
  /* Elle se tait dès que la partie démarre ou qu'une salle s'affiche : jamais pendant les énigmes */
  if(estJeu){
    const go = document.getElementById("btn-demarrer") || document.getElementById("btn-embarquer");
    if(go) go.addEventListener("click", () => { silence(); marquerVu(); document.querySelectorAll("#mascotte-bloc").forEach(x => x.remove()); }, true);
    if(typeof window.afficherSalle === "function"){
      const o = window.afficherSalle;
      window.afficherSalle = function(){ silence(); return o.apply(this, arguments); };
    }
  }

  /* ---------------- Réglage dans ⚙️ ---------------- */
  function groupeReglage(){
    const g = document.createElement("div");
    g.className = "reglages-group"; g.id = "reglages-mascotte";
    g.innerHTML = `<h4>🧑‍🎓 Mascotte</h4>
      <div class="reglage-ligne"><div class="libelle"><b>Noa, le guide de la collection</b><br>
        <span style="font-size:.8rem;opacity:.7">Elle accueille la classe, explique les règles communes et annonce les trophées ; elle ne parle jamais pendant les énigmes et n'a aucun effet sur le score. Gardé sur cet appareil.</span></div>
        <div class="controle"><select id="reg-mascotte">${Object.entries(MODES).map(([k, v]) => `<option value="${k}" ${k === mode() ? "selected" : ""}>${v}</option>`).join("")}</select></div></div>`;
    g.querySelector("select").addEventListener("change", ev => regler(ev.target.value));
    return g;
  }
  function sectionImmersive(){
    const sec = document.createElement("section");
    sec.id = "reglages-mascotte";
    sec.innerHTML = `<h4>🧑‍🎓 Mascotte</h4>
      <label class="reg-ligne" for="reg-mascotte"><span>Noa, le guide de la collection</span><select id="reg-mascotte">${Object.entries(MODES).map(([k, v]) => `<option value="${k}" ${k === mode() ? "selected" : ""}>${v}</option>`).join("")}</select></label>
      <p class="note">Elle accueille la classe, explique les règles communes et annonce les trophées ; elle ne parle jamais pendant les énigmes et n'a aucun effet sur le score.</p>`;
    sec.querySelector("select").addEventListener("change", ev => regler(ev.target.value));
    return sec;
  }
  if(estJeu){
    new MutationObserver(() => {
      if(!window.document || !window.document.getElementById) return;
      if(document.getElementById("reglages-mascotte")) return;
      const calme = document.getElementById("reg-calme");
      if(calme){ const grp = calme.closest(".reglages-group"); if(grp) grp.parentNode.appendChild(groupeReglage()); return; }
      const corps = document.querySelector("#reglages .reglages-corps");
      if(corps) corps.appendChild(sectionImmersive());
    }).observe(document.body, { childList: true, subtree: true });
  }

  const demarrer = () => rafraichir();
  if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", demarrer); else demarrer();
  window.MASCOTTE = { mode, regler, lire, silence, parler, svg: svgNoa, annoncerTrophees, rafraichir, MODES, bareme };
})();
