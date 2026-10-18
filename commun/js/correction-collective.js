/* ============================================================
   MODE CORRECTION COLLECTIVE PROJETABLE (amélioration D7) — tronc commun
   ------------------------------------------------------------
   Après la partie, pour l'institutionnalisation en grand groupe : un
   écran à projeter qui présente, SALLE PAR SALLE, toutes les énigmes
   avec leur bonne réponse (sans rouvrir chaque énigme une par une).
   Pour chaque salle : la liste des énigmes (consigne, réponse, rappel
   de la leçon), puis le mot de la serrure. Les réponses sont d'abord
   cachées : l'enseignant interroge la classe, puis révèle (clic sur
   « Voir la réponse », ou touche Espace pour la suivante).
   Où le trouver :
     • écran de fin de partie : bouton « 🖥️ Correction collective » ;
     • tableau de bord prof.html : « 🖥️ Correction collective » ;
     • adresse : index.html?correction=1[&niveau=CM1|CM2] (sans jouer).
   Clavier : ← → changent de salle, Espace révèle la réponse suivante,
   T révèle tout, Échap ferme, + − agrandissent le texte.
   Lit les énigmes réellement jouées (série de la banque D3 comprise),
   ne modifie ni app.js ni le score. Chargé après app.js.
   Jeux à moteur propre (Déclaration, Tour du monde : énigmes écrites dans
   leur enigmes.js) : les réponses sont listées dans leur js/correction.js
   (objet CORRECTION_JEU) ; à tenir à jour si une énigme change.
   ============================================================ */
(function(){
  if(typeof ETAT === "undefined") return;
  const esc = s => String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  const donnees = () => (typeof window.DONNEES === "function" ? window.DONNEES() : window.DONNEES) || null;
  const enigmesJson = () => (typeof window.ENIGMES === "function" ? window.ENIGMES() : window.ENIGMES) || null;
  const nbSalles = () => window.NB_SALLES || ((donnees() && donnees().salles) || []).length || 5;
  const ID = "correction-collective";
  const disponible = () => typeof CORRECTION_JEU !== "undefined" || (typeof window.salleEnigmes === "function" && !!enigmesJson());
  let niveau = null, salle = 1, taille = 1, revele = new Set(), ordre = [];

  /* ---------------- La bonne réponse, selon le type d'énigme ---------------- */
  function reponseHTML(e){
    const d = (typeof donneesNiveau === "function") ? donneesNiveau(e) : (e.commun || e.cm2 || e.cm1 || {});
    const liste = l => `<ul class="cc-liste">${l.map(x => `<li>${x}</li>`).join("")}</ul>`;
    switch(e.type){
      case "qcm":
        return liste((d.questions || []).map(q => `<span class="cc-q">${q.q}</span> → <b class="cc-rep">${(q.options || [])[q.bonne]}</b>`));
      case "vraifaux":
        return liste((d.affirmations || []).map(a => `${a.txt} → <b class="cc-rep">${a.vrai ? "VRAI" : "FAUX"}</b>`));
      case "association":
        return liste((d.paires || []).map(p => `${p.icone ? p.icone + " " : ""}${p.g} <b class="cc-rep">⟷ ${p.d}</b>`));
      case "ordre": {
        const items = (d.items || []).map((it, i) => ({ ...it, rang: it.rang != null ? it.rang : i + 1 })).sort((a, b) => a.rang - b.rang);
        return `<ol class="cc-liste">${items.map(it => `<li><b class="cc-rep">${it.txt}</b>${it.sous ? ` <small>(${it.sous})</small>` : ""}</li>`).join("")}</ol>`;
      }
      case "tri":
        return `<div class="cc-colonnes">${(d.colonnes || []).map(col => `<div class="cc-col"><div class="cc-col-titre">${col.icone ? col.icone + " " : ""}${col.titre}</div>
          ${liste((d.cartes || []).filter(c => c.col === col.id).map(c => `<b class="cc-rep">${c.icone ? c.icone + " " : ""}${c.txt}</b>`))}</div>`).join("")}</div>`;
      case "trous":
        return `<p class="cc-texte">${String(d.texte || "").replace(/\[\[(.+?)\]\]/g, (_, r) => `<b class="cc-rep cc-trou">${r}</b>`)}</p>`;
      case "lettres":
        return `<p class="cc-mot">${(d.cible || []).map(l => `<span class="cc-lettre">${esc(l)}</span>`).join("")}</p>`;
      case "code":
        return liste((d.champs || []).map(c => `${c.libelle} : <b class="cc-rep">${esc(c.valeur)}</b>`));
      case "intrus": {
        const i = (d.cartes || []).find(c => c.intrus);
        return `<p class="cc-texte">L'intrus est : <b class="cc-rep">${i ? (i.icone ? i.icone + " " : "") + i.txt : "—"}</b></p>`;
      }
      case "plan":
        return liste((d.cases || []).map(c => `${c.libelle || "—"} → <b class="cc-rep">${c.reponse}</b>`));
      case "instrument":
        return liste((d.items || []).map(it => `${it.libelle || ""} : <b class="cc-rep">${String(it.valeur).replace(".", ",")} ${d.unite || ""}</b>`));
      default:
        return `<p class="cc-texte"><i>Réponse non disponible pour ce type d'énigme (${esc(e.type)}).</i></p>`;
    }
  }

  /* ---------------- Contenu d'une salle ---------------- */
  const propre = () => (typeof CORRECTION_JEU !== "undefined" ? CORRECTION_JEU : null);
  /** Énigmes de la salle n, sous une forme unique : { id, titre, consigne, reponse, correction }. */
  function listeSalle(n){
    if(propre()) return propre().enigmes(niveau, n);
    const ancien = ETAT.niveau; ETAT.niveau = niveau;
    try{
      const liste = typeof salleEnigmes === "function" ? salleEnigmes(n).slice() : [];
      return liste.map(e => ({
        id: e.id, titre: e.titre,
        consigne: typeof texteNiveau === "function" ? texteNiveau(e.consigne) : (e.consigne || ""),
        reponse: reponseHTML(e),
        correction: typeof texteNiveau === "function" ? texteNiveau(e.correction) : (e.correction || "")
      }));
    } finally { ETAT.niveau = ancien; }
  }
  function salleHTML(n){
    const D = donnees(), s = D && D.salles ? D.salles[n - 1] : null;
    const liste = listeSalle(n);
    ordre = [];
    const cartes = liste.map((e, i) => {
      const cle = `${n}|${e.id}`; ordre.push(cle);
      const ouvert = revele.has(cle);
      return `<section class="cc-enigme ${ouvert ? "ouverte" : ""}" data-cle="${esc(cle)}">
        <h3><span class="cc-num">${i + 1}</span> ${esc(e.titre)}</h3>
        <p class="cc-consigne">${e.consigne}</p>
        <button type="button" class="cc-voir" aria-expanded="${ouvert}">👁️ Voir la réponse</button>
        <div class="cc-reponse" ${ouvert ? "" : "hidden"}>
          ${e.reponse}
          ${e.correction ? `<p class="cc-rappel"><b>À retenir :</b> ${e.correction}</p>` : ""}
        </div>
      </section>`;
    }).join("");
    const mot = s && (s.motCle || s.fragment);
    return `<h2 class="cc-salle-titre">${esc((window.JEU && JEU.motSalle) || "Salle")} ${n}${s ? " — " + esc(s.titre) : ""}</h2>
      ${cartes || '<p class="cc-vide">Aucune énigme dans cette salle.</p>'}
      ${mot ? `<section class="cc-serrure"><span>🔑 Mot de la serrure de cette salle :</span> <button type="button" class="cc-voir cc-voir-mot" data-cle="${n}|mot" aria-expanded="${revele.has(n + "|mot")}">👁️ Voir le mot</button>
        <b class="cc-mot-serrure" ${revele.has(n + "|mot") ? "" : "hidden"}>${esc(mot)}</b></section>` : ""}`;
  }

  /* ---------------- Fenêtre projetable ---------------- */
  function styles(){
    if(document.getElementById("style-" + ID)) return;
    const s = document.createElement("style"); s.id = "style-" + ID;
    s.textContent = `
      #${ID}{position:fixed;inset:0;z-index:9500;background:#fffdf6;color:#1f2430;display:flex;flex-direction:column;font-family:Georgia,serif}
      #${ID} .cc-barre{display:flex;flex-wrap:wrap;gap:8px;align-items:center;padding:10px 16px;background:#1d3a8a;color:#fff}
      #${ID} .cc-barre b{flex:1;min-width:180px;font-size:1.1rem}
      #${ID} .cc-barre button,#${ID} .cc-barre select{font:inherit;font-weight:bold;border:0;border-radius:18px;padding:7px 14px;cursor:pointer;background:#fff;color:#1d3a8a}
      #${ID} .cc-barre button[disabled]{opacity:.4;cursor:default}
      #${ID} .cc-corps{flex:1;overflow:auto;padding:18px clamp(14px,4vw,48px) 40px;font-size:calc(1.15rem * var(--cc-t,1));line-height:1.5}
      #${ID} .cc-salle-titre{margin:0 0 12px;font-size:1.6em;color:#1d3a8a}
      #${ID} .cc-enigme{background:#fff;border:2px solid #e0cfa6;border-radius:14px;padding:12px 18px;margin:0 0 14px}
      #${ID} .cc-enigme h3{margin:0 0 4px;font-size:1.15em}
      #${ID} .cc-num{display:inline-block;min-width:1.6em;text-align:center;border-radius:50%;background:#1d3a8a;color:#fff;margin-right:6px}
      #${ID} .cc-consigne{margin:4px 0 8px;opacity:.85;font-size:.92em}
      #${ID} .cc-voir{font:inherit;font-size:.85em;font-weight:bold;border:2px dashed #1d3a8a;border-radius:16px;background:transparent;color:#1d3a8a;padding:4px 14px;cursor:pointer}
      #${ID} .cc-enigme.ouverte .cc-voir,#${ID} .cc-voir[aria-expanded="true"]{display:none}
      #${ID} .cc-reponse{margin-top:8px;padding:8px 14px;border-left:6px solid #2e7d32;background:#eef8ef;border-radius:0 10px 10px 0}
      #${ID} .cc-reponse[hidden],#${ID} .cc-mot-serrure[hidden]{display:none}
      #${ID} .cc-liste{margin:4px 0;padding-left:1.3em}
      #${ID} .cc-rep{color:#14532d;background:#d8f0dc;border-radius:6px;padding:0 6px}
      #${ID} .cc-q{opacity:.85}
      #${ID} .cc-colonnes{display:flex;flex-wrap:wrap;gap:14px}#${ID} .cc-col{flex:1 1 200px;border:2px solid #bcd8c0;border-radius:10px;padding:6px 10px}
      #${ID} .cc-col-titre{font-weight:bold;color:#14532d}
      #${ID} .cc-mot{display:flex;gap:6px;margin:6px 0}#${ID} .cc-lettre{display:inline-block;min-width:1.6em;text-align:center;font-weight:bold;font-size:1.3em;background:#d8f0dc;border:2px solid #2e7d32;border-radius:8px}
      #${ID} .cc-rappel{margin:8px 0 0;font-size:.92em}
      #${ID} .cc-serrure{margin-top:16px;padding:12px 18px;border-radius:14px;background:#fff6d8;border:2px solid #c9a227}
      #${ID} .cc-mot-serrure{font-size:1.5em;letter-spacing:.08em;color:#7a5200}
      body.calme #${ID} *{transition:none!important}
      @media print{body>*:not(#${ID}){display:none!important}#${ID}{position:static}#${ID} .cc-barre,#${ID} .cc-voir{display:none!important}#${ID} .cc-reponse,#${ID} .cc-mot-serrure{display:block!important}#${ID} .cc-corps{overflow:visible}}`;
    document.head.appendChild(s);
  }

  function dessiner(){
    const el = document.getElementById(ID); if(!el) return;
    const N = nbSalles();
    el.style.setProperty("--cc-t", taille);
    el.querySelector(".cc-corps").innerHTML = salleHTML(salle);
    el.querySelector(".cc-pos").textContent = `${salle} / ${N}`;
    el.querySelector(".cc-prec").disabled = salle <= 1;
    el.querySelector(".cc-suiv").disabled = salle >= N;
    el.querySelector(".cc-niv").value = niveau;
    el.querySelector(".cc-corps").scrollTop = 0;
  }
  function reveler(cle){
    revele.add(cle);
    const el = document.getElementById(ID); if(!el) return;
    const sec = [...el.querySelectorAll("[data-cle]")].find(x => x.dataset.cle === cle);
    if(!sec) return;
    if(sec.classList.contains("cc-enigme")){ sec.classList.add("ouverte"); sec.querySelector(".cc-reponse").hidden = false; sec.querySelector(".cc-voir").setAttribute("aria-expanded", "true"); }
    else { sec.setAttribute("aria-expanded", "true"); const m = el.querySelector(".cc-mot-serrure"); if(m) m.hidden = false; }
  }
  function revelerSuivante(){
    const cle = [...ordre, `${salle}|mot`].find(c => !revele.has(c));
    if(cle) reveler(cle);
  }
  function revelerTout(){ [...ordre, `${salle}|mot`].forEach(reveler); }
  function aller(n){ salle = Math.max(1, Math.min(nbSalles(), n)); dessiner(); }
  function surClavier(ev){
    if(!document.getElementById(ID)) return;
    if(ev.target && /^(INPUT|SELECT|TEXTAREA)$/.test(ev.target.tagName)) return;
    const k = ev.key;
    if(k === "ArrowRight"){ aller(salle + 1); ev.preventDefault(); }
    else if(k === "ArrowLeft"){ aller(salle - 1); ev.preventDefault(); }
    else if(k === " " || k === "Enter"){ if(ev.target && ev.target.tagName === "BUTTON") return; revelerSuivante(); ev.preventDefault(); }
    else if(k === "t" || k === "T"){ revelerTout(); }
    else if(k === "Escape"){ fermer(); }
    else if(k === "+" || k === "="){ taille = Math.min(2, taille + .1); dessiner(); }
    else if(k === "-"){ taille = Math.max(.7, taille - .1); dessiner(); }
  }

  function ouvrir(options){
    options = options || {};
    if(!disponible()) return false;
    styles();
    niveau = options.niveau || niveau || ETAT.niveau || "CM2";
    salle = options.salle || 1; revele = new Set(); taille = 1;
    fermer();
    const el = document.createElement("div");
    el.id = ID; el.setAttribute("role", "dialog"); el.setAttribute("aria-label", "Correction collective");
    el.innerHTML = `<div class="cc-barre">
        <b>🖥️ Correction collective — ${esc((window.JEU && JEU.titre) || document.title)}</b>
        <select class="cc-niv" aria-label="Niveau"><option value="CM1">CM1</option><option value="CM2">CM2</option></select>
        <button type="button" class="cc-prec">◀ Salle précédente</button><span class="cc-pos"></span><button type="button" class="cc-suiv">Salle suivante ▶</button>
        <button type="button" class="cc-tout" title="Révéler toutes les réponses de la salle (touche T)">👁️ Tout voir</button>
        <button type="button" class="cc-moins" aria-label="Texte plus petit">A−</button><button type="button" class="cc-plus" aria-label="Texte plus grand">A+</button>
        <button type="button" class="cc-imprimer">🖨️</button>
        <button type="button" class="cc-fermer">✖ Fermer</button>
      </div><div class="cc-corps"></div>`;
    document.body.appendChild(el);
    el.querySelector(".cc-prec").addEventListener("click", () => aller(salle - 1));
    el.querySelector(".cc-suiv").addEventListener("click", () => aller(salle + 1));
    el.querySelector(".cc-tout").addEventListener("click", revelerTout);
    el.querySelector(".cc-moins").addEventListener("click", () => { taille = Math.max(.7, taille - .1); dessiner(); });
    el.querySelector(".cc-plus").addEventListener("click", () => { taille = Math.min(2, taille + .1); dessiner(); });
    el.querySelector(".cc-imprimer").addEventListener("click", () => { revelerTout(); window.print(); });
    el.querySelector(".cc-fermer").addEventListener("click", fermer);
    el.querySelector(".cc-niv").addEventListener("change", ev => { niveau = ev.target.value; revele = new Set(); dessiner(); });
    el.querySelector(".cc-corps").addEventListener("click", ev => {
      const b = ev.target.closest(".cc-voir"); if(!b) return;
      const cle = b.classList.contains("cc-voir-mot") ? b.dataset.cle : b.closest(".cc-enigme").dataset.cle;
      reveler(cle);
    });
    document.addEventListener("keydown", surClavier);
    dessiner();
    el.querySelector(".cc-suiv").focus();
    return true;
  }
  function fermer(){
    const el = document.getElementById(ID);
    if(el) el.remove();
    document.removeEventListener("keydown", surClavier);
    const url = new URL(location.href);
    if(url.searchParams.get("correction") && history.replaceState && window.CORRECTION_DEPUIS_URL){
      url.searchParams.delete("correction"); history.replaceState(null, "", url);
      window.CORRECTION_DEPUIS_URL = false;
    }
  }

  /* ---------------- Entrées : écran de fin de partie, adresse ---------------- */
  function boutonFin(){
    const c = document.getElementById("fin-contenu");
    if(!c || c.querySelector("#btn-correction-collective")) return;
    const b = document.createElement("div");
    b.className = "boutons"; b.style.cssText = "text-align:center;margin:14px 0";
    b.innerHTML = `<button type="button" class="btn gris" id="btn-correction-collective" title="Pour la mise en commun avec toute la classe : les bonnes réponses, salle par salle">🖥️ Correction collective (à projeter)</button>`;
    b.querySelector("button").addEventListener("click", () => ouvrir({ niveau: ETAT.niveau }));
    const premiers = c.querySelector(".boutons");
    if(premiers) premiers.before(b); else c.appendChild(b);
  }
  if(typeof window.finDuJeu === "function"){
    const origine = window.finDuJeu;
    window.finDuJeu = function(){
      const r = origine.apply(this, arguments);
      boutonFin();
      return r;
    };
  }

  const p = new URLSearchParams(location.search);
  if(p.get("correction")){
    window.CORRECTION_DEPUIS_URL = true;
    const niv = /^CM[12]$/.test(p.get("niveau") || "") ? p.get("niveau") : "CM2";
    let essais = 0;
    const attendre = setInterval(() => {
      essais++;
      if(disponible() && donnees()){
        clearInterval(attendre); ouvrir({ niveau: niv, salle: +p.get("salle") || 1 });
      } else if(essais > 100){ clearInterval(attendre); }
    }, 100);
  }
  window.CORRECTION_COLLECTIVE = { ouvrir, fermer, reponseHTML, salleHTML, listeSalle };
})();
