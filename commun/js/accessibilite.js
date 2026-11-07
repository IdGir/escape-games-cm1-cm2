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

   TAILLE DU TEXTE ET DES BOUTONS (amélioration N29) — confort de lecture en salle projetée ou sur
   tablette : trois tailles (Normal / Grand / Très grand) qui agrandissent ensemble le texte, les
   boutons et les espacements (base de la page ×1,125 puis ×1,25, boutons et champs plus hauts).
   Gardé sur l'appareil dans la même clé « escape_lecture » (champ « taille »), donc pour tous les
   jeux, et CUMULATIF avec la police, l'interlignage et l'espacement ci-dessus, ainsi qu'avec le
   curseur « taille du texte » propre à chaque jeu. Réservé à l'écran : l'impression n'est pas touchée.
   ============================================================ */
(function(){
  const CLE = "escape_lecture";
  const DEFAUT = { police: "standard", interligne: "normal", espacement: false, taille: "normal" };
  const TAILLES = ["normal", "grand", "tres"];
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
    @media screen{
      html.taille-grand{font-size:18px}
      html.taille-tres{font-size:20px}
      html.taille-grand.base-echelle{font-size:calc(1.125rem * var(--echelle,1) * 1.125)}
      html.taille-tres.base-echelle{font-size:calc(1.125rem * var(--echelle,1) * 1.25)}
      @media (max-width:760px){
        html.taille-grand.base-echelle{font-size:calc(1.0625rem * var(--echelle,1) * 1.125)}
        html.taille-tres.base-echelle{font-size:calc(1.0625rem * var(--echelle,1) * 1.25)}
      }
      @media (max-width:480px){
        html.taille-grand.base-echelle{font-size:calc(1rem * var(--echelle,1) * 1.125)}
        html.taille-tres.base-echelle{font-size:calc(1rem * var(--echelle,1) * 1.25)}
      }
      html.taille-grand :where(button,.btn,select,input:not([type=checkbox]):not([type=radio]):not([type=range]),textarea){min-height:2.9rem}
      html.taille-tres :where(button,.btn,select,input:not([type=checkbox]):not([type=radio]):not([type=range]),textarea){min-height:3.3rem}
      html.taille-grand :where(button,.btn){padding-block:.55em}
      html.taille-tres :where(button,.btn){padding-block:.7em}
      html.taille-grand :where(input[type=checkbox],input[type=radio]){width:1.25em;height:1.25em}
      html.taille-tres :where(input[type=checkbox],input[type=radio]){width:1.5em;height:1.5em}
      html.taille-grand :where(p,li,td,th,dd,dt,.consigne,.texte,.feedback,.bulle,.lecon-texte){line-height:1.55}
      html.taille-tres :where(p,li,td,th,dd,dt,.consigne,.texte,.feedback,.bulle,.lecon-texte){line-height:1.65}
      html.taille-grand :where(p,li,.consigne,.texte,.feedback,.bulle){margin-block:.6em}
      html.taille-tres :where(p,li,.consigne,.texte,.feedback,.bulle){margin-block:.8em}
    }
    .lecture-reglages{margin-top:10px;padding:10px 12px;border:1px dashed rgba(0,0,0,.25);border-radius:10px}
    .lecture-reglages .ligne-lecture{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;margin:6px 0}
    .lecture-reglages select{font-size:1rem;padding:4px 6px}
    .lecture-reglages .boutons-taille{display:flex;flex-wrap:wrap;gap:8px}
    .lecture-reglages .boutons-taille button{font:inherit;padding:6px 12px;border:2px solid rgba(0,0,0,.35);border-radius:10px;background:rgba(255,255,255,.85);color:inherit;cursor:pointer}
    .lecture-reglages .boutons-taille button[aria-pressed=true]{border-color:#1f5fbf;background:#dce9ff;font-weight:700}
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
    const h = document.documentElement.classList, t = TAILLES.includes(r.taille) ? r.taille : "normal";
    h.toggle("taille-grand", t === "grand");
    h.toggle("taille-tres", t === "tres");
    // Mission géographique règle sa taille de base sur la variable --echelle : on l'agrandit au lieu de la remplacer
    h.toggle("base-echelle", (t !== "normal") && !!getComputedStyle(document.documentElement).getPropertyValue("--echelle").trim());
  }

  /* Bloc de réglages, inséré sous « Accessibilité » dans ⚙️ Réglages */
  function bloc(){
    const r = lire();
    const d = document.createElement("div");
    d.className = "lecture-reglages";
    d.id = "lecture-reglages";
    d.innerHTML = `
      <b>📖 Lecture facilitée</b> <span style="font-size:.8rem;opacity:.75">(gardé sur cet appareil, pour tous les jeux)</span>
      <div class="ligne-lecture" role="group" aria-labelledby="lec-taille-titre"><b id="lec-taille-titre">🔎 Taille du texte et des boutons</b>
        <span class="boutons-taille">
          <button type="button" data-taille="normal" aria-pressed="false">Normal</button>
          <button type="button" data-taille="grand" aria-pressed="false">Grand</button>
          <button type="button" data-taille="tres" aria-pressed="false">Très grand</button>
        </span></div>
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
    const marquer = t => d.querySelectorAll("[data-taille]").forEach(x => x.setAttribute("aria-pressed", String(x.dataset.taille === t)));
    marquer(r.taille);
    const maj = taille => {
      const n = { police: d.querySelector("#lec-police").value, interligne: d.querySelector("#lec-interligne").value,
                  espacement: d.querySelector("#lec-espacement").checked, taille: taille || lire().taille };
      ecrire(n); appliquer(n); marquer(n.taille);
    };
    d.addEventListener("change", () => maj());
    d.addEventListener("click", e => { const b = e.target.closest("[data-taille]"); if (b) maj(b.dataset.taille); });
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
