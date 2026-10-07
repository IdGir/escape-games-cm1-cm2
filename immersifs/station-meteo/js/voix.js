/* ============================================================
   VOIX — dialogues sur la plaque de laiton
   ------------------------------------------------------------
   Portrait animé + nom + texte qui s'écrit + voix du navigateur
   (fr-FR, débit et hauteur propres à chaque personnage). Les
   sous-titres restent toujours affichés (classe sans voix, TBI muet).
   Le personnage se tait dès que les élèves touchent l'énigme.
   ============================================================ */
var VML = window.VML || (window.VML = {});

(function(){
  let voixFR = [];
  function chargerVoix(){
    if(!("speechSynthesis" in window)) return;
    voixFR = speechSynthesis.getVoices().filter(v => /^fr/i.test(v.lang));
  }
  if("speechSynthesis" in window){ chargerVoix(); speechSynthesis.onvoiceschanged = chargerVoix; }

  VML.voixActive = () => !(VML.reglage && VML.reglage("voix") === false) && ("speechSynthesis" in window);

  VML.taire = function(){
    try{ if("speechSynthesis" in window) speechSynthesis.cancel(); }catch(e){}
    document.querySelectorAll(".portrait-ovale.parle").forEach(p => p.classList.remove("parle"));
    clearTimeout(VML._finParole);
  };

  /** Dit un texte ; résout la promesse à la fin (ou après une durée estimée sans voix). */
  VML.dire = function(perso, texte, portraitEl){
    VML.taire();
    const p = VML.perso(perso) || {};
    const brut = String(texte || "").replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
    return new Promise(res => {
      const estimee = Math.max(2500, brut.length * 62);
      const fin = () => { if(portraitEl) portraitEl.classList.remove("parle"); res(); };
      if(!brut){ res(); return; }
      if(!VML.voixActive()){
        if(portraitEl){ portraitEl.classList.add("parle"); }
        VML._finParole = setTimeout(fin, Math.min(estimee, 6000));
        return;
      }
      const u = new SpeechSynthesisUtterance(brut);
      u.lang = "fr-FR";
      const v = p.voix || {};
      u.rate = (v.rate || 1) * (VML.reglage ? (VML.reglage("debitVoix") || 1) : 1);
      u.pitch = v.pitch || 1;
      if(voixFR.length) u.voice = voixFR[Math.abs([...perso || "x"].reduce((a, c) => a + c.charCodeAt(0), 0)) % voixFR.length] || voixFR[0];
      u.onstart = () => { if(portraitEl) portraitEl.classList.add("parle"); };
      u.onend = fin; u.onerror = fin;
      VML._finParole = setTimeout(fin, estimee + 4000);
      try{ speechSynthesis.speak(u); }catch(e){ fin(); }
    });
  };

  /** Texte qui s'écrit (respecte « animations réduites »). */
  VML.ecrire = function(el, html){
    if(!el) return;
    clearInterval(el._t);
    if(VML.animationsReduites && VML.animationsReduites()){ el.innerHTML = html; return; }
    const brut = String(html);
    let i = 0;
    el.innerHTML = "";
    el._t = setInterval(() => {
      i += 2;
      if(brut[i - 1] === "<"){ const j = brut.indexOf(">", i); if(j > 0) i = j + 1; }
      el.innerHTML = brut.slice(0, i);
      if(i >= brut.length) clearInterval(el._t);
    }, 22);
  };

  /**
   * Affiche la plaque de dialogue.
   * @param {HTMLElement} hote  conteneur .plaque
   * @param {object} o  {perso, texte, source (ligne « 📖 … »), boutons:[{libelle, action}]}
   */
  VML.plaque = function(hote, o){
    const p = VML.perso(o.perso) || { nom: o.perso || "" };
    hote.innerHTML = `
      <div class="plaque-dialogue" role="dialog" aria-live="polite">
        ${o.perso ? VML.htmlPortrait(o.perso, "plaque-portrait") : ""}
        <div class="plaque-texte">
          ${o.perso ? `<div class="plaque-nom">${p.nom}</div>` : ""}
          <div class="plaque-phrase"></div>
          ${o.source ? `<div class="plaque-source">${o.source}</div>` : ""}
          <div class="plaque-boutons">
            <button class="btn-laiton petit" data-reecouter>🔊 Réécouter</button>
            ${(o.boutons || []).map((b, i) => `<button class="btn-laiton ${b.classe || ""}" data-b="${i}">${b.libelle}</button>`).join("")}
          </div>
        </div>
      </div>`;
    hote.classList.add("visible");
    const portrait = hote.querySelector(".portrait-ovale");
    if(portrait) VML.installerPortrait(portrait);
    VML.ecrire(hote.querySelector(".plaque-phrase"), o.texte);
    hote.querySelector("[data-reecouter]").addEventListener("click", () => VML.dire(o.perso, o.texte, portrait));
    hote.querySelectorAll("[data-b]").forEach(b => b.addEventListener("click", () => { VML.taire(); (o.boutons[+b.dataset.b].action || (() => {}))(); }));
    return VML.dire(o.perso, o.texte, portrait);
  };
  VML.masquerPlaque = function(hote){ if(hote){ hote.classList.remove("visible"); hote.innerHTML = ""; } VML.taire(); };
})();
