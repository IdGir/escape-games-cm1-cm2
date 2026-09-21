/* ============================================================
   LEÇONS — Bibliothèque consultable à tout moment (bouton 📚)
   Leçons rédigées en texte (comme « Le Secret de la Déclaration »
   et « Le Tour du Monde ») : aucune dépendance à un fichier.
   Chaque leçon : objectifs, contenu CM1 / CM2, lexique, schéma
   SVG facultatif, sources. Les énigmes s'y rattachent par le
   champ "lecon" de enigmes.json.
   ============================================================ */

let LECONS_DATA = null;

async function chargerLecons(){
  if(LECONS_DATA) return LECONS_DATA;
  let fetchOk = false;
  try{
    const resp = await fetch("assets/data/lecons.json", {cache:"no-store"});
    if(resp.ok){ LECONS_DATA = await resp.json(); fetchOk = true; }
  }catch(e){
    console.warn("Fetch lecons.json échoué (mode file:// ?). Bascule sur la leçon embarquée.");
  }
  if(!fetchOk || !LECONS_DATA || !LECONS_DATA.lecons){
    LECONS_DATA = JSON.parse(JSON.stringify(LECONS_FALLBACK));
  }
  return LECONS_DATA;
}

/* ---- Leçon embarquée minimale (ouverture en double-clic, sans serveur) ---- */
const LECONS_FALLBACK = {
  lecons: [
    {
      id:"thermometre", icone:"🌡️", titre:"Mesurer la température de l'air", salle:1, duree:"3 min", niveau:"CM1-CM2",
      objectifs:["Lire un thermomètre", "Savoir où placer un thermomètre"],
      contenu:{
        cm1:"<p>On mesure la température de l'air avec un <b>thermomètre</b>. Elle s'exprime en <b>degrés Celsius (°C)</b>.</p><div class='encadre'>Pour que la mesure soit juste, le thermomètre est placé <b>à l'ombre</b>, dans un <b>abri</b> blanc et aéré, à <b>1,50 m</b> du sol.</div>",
        cm2:"<p>La température de l'air se mesure <b>sous abri</b>, à <b>1,50 m</b> du sol, dans un abri blanc et ventilé qui protège le capteur du soleil et de la pluie (Météo-France).</p>"
      },
      sources:["Météo-France, « Qu'est-ce que la température ? »"]
    }
  ]
};

const _esc = s => String(s==null?"":s).replace(/[&<>"']/g,
  c => ({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[c]));

/* ---- Ouvrir la bibliothèque ---- */
async function ouvrirBiblioLecons(){
  await chargerLecons();
  const overlay = document.getElementById("overlay-lecons");
  const corps = document.getElementById("corps-lecons");
  const lecons = LECONS_DATA.lecons || [];
  const niveau = (window.ETAT && ETAT.niveau) || "CM2";
  const visibles = lecons.filter(l=>!(l.niveau==="CM2" && niveau==="CM1"));

  corps.innerHTML = `
    <p class="biblio-intro">Une leçon par module. Clique pour la lire ; tu peux revenir au jeu quand tu veux.</p>
    <div class="biblio-grille">
      ${visibles.map(l=>`
        <div class="carte-lecon" data-id="${_esc(l.id)}" role="button" tabindex="0">
          <div class="icone">${l.icone||"📄"}</div>
          <div class="titre">${l.salle?`Module ${l.salle} · `:""}${_esc(l.titre)}</div>
          <div class="duree">⏱️ ${_esc(l.duree||"")}</div>
        </div>`).join("")}
    </div>`;
  corps.querySelectorAll(".carte-lecon").forEach(c=>{
    c.addEventListener("click", ()=>afficherLecon(c.dataset.id));
    c.addEventListener("keydown", ev=>{ if(ev.key==="Enter"||ev.key===" "){ ev.preventDefault(); afficherLecon(c.dataset.id); } });
  });
  overlay.classList.add("show");
  corps.scrollTop = 0;
}

/* ---- Afficher une leçon ---- */
function afficherLecon(id){
  if(!LECONS_DATA) return;
  const lecon = (LECONS_DATA.lecons||[]).find(l=>l.id===id);
  if(!lecon) return;
  const niveau = ((window.ETAT && ETAT.niveau) || "CM2").toLowerCase();
  const contenu = (lecon.contenu && (lecon.contenu[niveau] || lecon.contenu.cm2 || lecon.contenu.cm1)) || "";
  const corps = document.getElementById("corps-lecons");

  const objectifs = (lecon.objectifs||[]).length
    ? `<div class="encadre" style="margin-bottom:14px"><b>🎯 Tu vas apprendre à :</b>
         <ul style="margin:6px 0 0 18px">${lecon.objectifs.map(o=>`<li>${o}</li>`).join("")}</ul></div>` : "";

  // Schéma : { svg, legende } ou { cm1:{…}, cm2:{…} }
  let schema = lecon.schema || null;
  if(schema && (schema.cm1 || schema.cm2)) schema = schema[niveau] || schema.cm2 || schema.cm1;
  const schemaHTML = schema && schema.svg
    ? `<div class="lecon-schema">${schema.svg}${schema.legende?`<div class="legende">${schema.legende}</div>`:""}</div>` : "";

  const lexique = (lecon.lexique||[]).filter(m=>!(m.niveau==="CM2" && niveau==="cm1"));
  const lexiqueHTML = lexique.length
    ? `<h4>📖 Lexique</h4><div class="lecon-lexique">${lexique.map(m=>`<div><b>${m.mot}</b> : ${m.def}</div>`).join("")}</div>` : "";

  const friseHTML = (lecon.frise||[]).length
    ? `<h4>📅 Repères</h4><div class="frise">${lecon.frise.map(e=>`<div class="evt"><span class="date">${e.date}</span>${e.evt}</div>`).join("")}</div>` : "";

  const sourcesHTML = (lecon.sources||[]).length
    ? `<div class="lecon-sources"><b>Sources :</b> ${lecon.sources.map(s=>_esc(s)).join(" · ")}</div>` : "";

  corps.innerHTML = `
    <div class="lecon-contenu">
      <button class="btn petit gris" id="btn-retour-biblio" style="margin-bottom:14px">← Retour aux leçons</button>
      <h3 style="color:var(--bleu-fonce);border-bottom:2px solid var(--or);padding-bottom:6px;margin-bottom:10px">${lecon.icone||""} ${_esc(lecon.titre)}</h3>
      ${objectifs}
      ${contenu}
      ${schemaHTML}
      ${lexiqueHTML}
      ${friseHTML}
      ${sourcesHTML}
    </div>`;
  document.getElementById("btn-retour-biblio").addEventListener("click", ouvrirBiblioLecons);
  corps.scrollTop = 0;
}

window.chargerLecons = chargerLecons;
window.ouvrirBiblioLecons = ouvrirBiblioLecons;
window.afficherLecon = afficherLecon;
window.LECONS_FALLBACK = LECONS_FALLBACK;
