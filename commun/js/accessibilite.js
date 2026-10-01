/* ============================================================
   LECTURE FACILITÉE — police et réglages « dyslexie » (amélioration E4)
   Tronc commun, greffon chargé après app.js dans les 9 jeux.
   ------------------------------------------------------------
   En complément des réglages déjà présents (texte jusqu'à 150 %,
   animations réduites), trois réglages de lecture :
     • Police : standard, « très lisible » (Atkinson Hyperlegible) ou
       « dyslexie » (OpenDyslexic) — fichiers dans commun/polices/,
       licence SIL OFL 1.1, aucun accès à internet nécessaire ;
     • Interlignage : normal, aéré (1,6) ou très aéré (1,9) ;
     • Espacement des lettres et des mots augmenté, texte aligné à
       gauche (jamais justifié).
   Les choix sont gardés sur l'appareil pour TOUS les jeux (clé
   « escape_lecture ») : un poste réglé pour un élève l'est partout.
   Ils apparaissent dans ⚙️ Réglages, sous « Accessibilité ».
   ============================================================ */
(function(){
  const CLE = "escape_lecture";
  const DEFAUT = { police: "standard", interligne: "normal", espacement: false };
  const lire = () => { try { return Object.assign({}, DEFAUT, JSON.parse(localStorage.getItem(CLE) || "{}")); } catch (e) { return Object.assign({}, DEFAUT); } };
  const ecrire = r => { try { localStorage.setItem(CLE, JSON.stringify(r)); } catch (e) {} };

  /* Polices : chemin relatif à CE fichier (commun/js/ → commun/polices/) */
  const ici = document.currentScript && document.currentScript.src;
  const P = n => { try { return ici ? new URL("../polices/" + n, ici).href : "../commun/polices/" + n; } catch (e) { return "../commun/polices/" + n; } };
  const TEXTE = ":is(p,li,td,th,label,blockquote,dd,dt,h2,h3,h4,.consigne,.texte,.feedback,.qcm-option,.q,.carte-match,.etiquette,.item-ordre,.vf-ligne,.bulle,.lecon-texte)";
  const style = document.createElement("style");
  style.id = "style-lecture";
  style.textContent = `
    @font-face{font-family:"OpenDyslexic";src:url("${P("opendyslexic-latin-400-normal.woff2")}") format("woff2");font-weight:400;font-display:swap}
    @font-face{font-family:"OpenDyslexic";src:url("${P("opendyslexic-latin-700-normal.woff2")}") format("woff2");font-weight:700;font-display:swap}
    @font-face{font-family:"Atkinson Hyperlegible";src:url("${P("atkinson-hyperlegible-latin-400-normal.woff2")}") format("woff2");font-weight:400;font-display:swap}
    @font-face{font-family:"Atkinson Hyperlegible";src:url("${P("atkinson-hyperlegible-latin-700-normal.woff2")}") format("woff2");font-weight:700;font-display:swap}
    body.police-dys, body.police-dys *:not(code):not(pre){font-family:"OpenDyslexic", "Comic Sans MS", sans-serif !important}
    body.police-lisible, body.police-lisible *:not(code):not(pre){font-family:"Atkinson Hyperlegible", Verdana, Arial, sans-serif !important}
    body.interligne-aere ${TEXTE}{line-height:1.6 !important}
    body.interligne-tres ${TEXTE}{line-height:1.9 !important}
    body.espacement-lecture ${TEXTE}{letter-spacing:.05em !important;word-spacing:.16em !important;text-align:left !important}
    .lecture-reglages{margin-top:10px;padding:10px 12px;border:1px dashed rgba(0,0,0,.25);border-radius:10px}
    .lecture-reglages .ligne-lecture{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;margin:6px 0}
    .lecture-reglages select{font-size:1rem;padding:4px 6px}
    .lecture-reglages .apercu-lecture{margin-top:6px;padding:8px;background:rgba(255,255,255,.7);border-radius:8px;font-size:1.05rem}
  `;
  document.head.appendChild(style);

  function appliquer(r){
    const b = document.body.classList;
    b.toggle("police-dys", r.police === "dys");
    b.toggle("police-lisible", r.police === "lisible");
    b.toggle("interligne-aere", r.interligne === "aere");
    b.toggle("interligne-tres", r.interligne === "tres");
    b.toggle("espacement-lecture", !!r.espacement);
  }

  /* Bloc de réglages, inséré sous « Accessibilité » dans ⚙️ Réglages */
  function bloc(){
    const r = lire();
    const d = document.createElement("div");
    d.className = "lecture-reglages";
    d.id = "lecture-reglages";
    d.innerHTML = `
      <b>📖 Lecture facilitée</b> <span style="font-size:.8rem;opacity:.75">(gardé sur cet appareil, pour tous les jeux)</span>
      <div class="ligne-lecture"><label for="lec-police">Police</label>
        <select id="lec-police">
          <option value="standard">Standard</option>
          <option value="lisible">Très lisible (Atkinson Hyperlegible)</option>
          <option value="dys">Dyslexie (OpenDyslexic)</option>
        </select></div>
      <div class="ligne-lecture"><label for="lec-interligne">Interlignage</label>
        <select id="lec-interligne">
          <option value="normal">Normal</option>
          <option value="aere">Aéré</option>
          <option value="tres">Très aéré</option>
        </select></div>
      <div class="ligne-lecture"><label><input type="checkbox" id="lec-espacement"> Lettres et mots plus espacés, texte aligné à gauche</label></div>
      <div class="apercu-lecture">Aperçu : « Les élèves lisent la consigne, puis cherchent l'indice dans la leçon. »</div>`;
    d.querySelector("#lec-police").value = r.police;
    d.querySelector("#lec-interligne").value = r.interligne;
    d.querySelector("#lec-espacement").checked = !!r.espacement;
    const maj = () => {
      const n = { police: d.querySelector("#lec-police").value, interligne: d.querySelector("#lec-interligne").value,
                  espacement: d.querySelector("#lec-espacement").checked };
      ecrire(n); appliquer(n);
    };
    d.addEventListener("change", maj);
    return d;
  }
  function inserer(){
    if (document.getElementById("lecture-reglages")) return;
    // 8 jeux « salles » : ligne « Animations réduites » (#reg-calme) ; Mission géographique : #r-anim
    const calme = document.getElementById("reg-calme");
    if (calme) { const l = calme.closest(".reglage-ligne") || calme.parentNode; l.after(bloc()); return; }
    const anim = document.getElementById("r-anim");
    if (anim) { const p = anim.closest("p") || anim.parentNode; p.after(bloc()); }
  }
  const obs = new MutationObserver(() => { if (document.getElementById("reg-calme") || document.getElementById("r-anim")) inserer(); });
  const demarrer = () => { appliquer(lire()); obs.observe(document.body, { childList: true, subtree: true }); };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", demarrer); else demarrer();

  window.LECTURE = { lire, ecrire, appliquer, inserer };
})();
