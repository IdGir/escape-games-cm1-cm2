/* ============================================================
   LEÇONS — Bibliothèque des leçons rédigées (bouton 📚)
   Une leçon par salle, lue dans assets/data/lecons.json :
     contenu {cm1, cm2}, objectifs, schema (SVG), lexique, sources.
   Chaque énigme renvoie à sa leçon par son champ "lecon".
   ============================================================ */

/* ---- Repli minimal si la page est ouverte en double-clic (file://) ---- */
const LECONS_FALLBACK = {
  salles: {"1":"Salle 1 — Le besoin et la fonction d'usage"},
  lecons: [
    {id:"besoin-fonction", icone:"🎯", titre:"À quoi sert un objet ?", salle:1, duree:"3 min", niveau:"CM1-CM2",
     objectifs:["Relier un objet au besoin auquel il répond"],
     contenu:{
       cm1:"<p>Un <b>objet technique</b> est fabriqué par l'être humain pour répondre à un <b>besoin</b>. Ce à quoi il sert s'appelle sa <b>fonction d'usage</b>.</p>",
       cm2:"<p>Un <b>objet technique</b> est conçu et fabriqué pour répondre à un <b>besoin</b>. Sa <b>fonction d'usage</b> dit ce qu'il permet de faire ; sa <b>fonction d'estime</b> dit pourquoi il plaît.</p>"},
     lexique:[{mot:"fonction d'usage", def:"ce à quoi sert l'objet"}],
     sources:["Programme de sciences et technologie du cycle 3 (éduscol)."]}
  ]
};

let LECONS_DATA = null;

async function chargerLecons(){
  if(LECONS_DATA) return LECONS_DATA;
  let ok = false;
  try{
    const r = await fetch("assets/data/lecons.json", {cache:"no-store"});
    if(r.ok){ LECONS_DATA = await r.json(); ok = true; }
  }catch(e){
    console.warn("Fetch lecons.json échoué (mode file:// ?). Bascule sur les leçons embarquées.");
  }
  if(!ok || !LECONS_DATA || !LECONS_DATA.lecons){
    LECONS_DATA = JSON.parse(JSON.stringify(LECONS_FALLBACK));
  }
  return LECONS_DATA;
}

const _echap = s => String(s==null?"":s).replace(/[&<>"']/g,
  c => ({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[c]));

/* ---- Ouvrir la bibliothèque ---- */
async function ouvrirBiblioLecons(){
  await chargerLecons();
  const overlay = document.getElementById("overlay-lecons");
  const corps   = document.getElementById("corps-lecons");
  const lecons  = LECONS_DATA.lecons || [];
  const salles  = LECONS_DATA.salles || {};
  const niveau  = (window.ETAT && ETAT.niveau) || "CM2";
  const visibles = lecons.filter(l => !(l.niveau === "CM2" && niveau === "CM1"));

  const groupes = [];
  visibles.forEach(l=>{
    const cle = String(l.salle || 0);
    let g = groupes.find(x=>x.cle===cle);
    if(!g){ g = {cle, titre: salles[cle] || ("Salle " + cle), items: []}; groupes.push(g); }
    g.items.push(l);
  });
  groupes.sort((a,b)=>Number(a.cle)-Number(b.cle));

  corps.innerHTML = `
    <p class="biblio-intro">Une leçon par salle. Clique sur une leçon pour la lire ;
    tu peux revenir au jeu quand tu veux.</p>
    ${groupes.map(g=>`
      <h4 class="biblio-salle">${_echap(g.titre)}</h4>
      <div class="biblio-grille">
        ${g.items.map(l=>`
          <div class="carte-lecon" data-id="${_echap(l.id)}" role="button" tabindex="0">
            <div class="icone">${l.icone||"📄"}</div>
            <div class="titre">${_echap(l.titre)}</div>
            <div class="duree">⏱️ ${_echap(l.duree||"")}</div>
          </div>`).join("")}
      </div>`).join("")}
  `;
  corps.querySelectorAll(".carte-lecon").forEach(c=>{
    c.addEventListener("click", ()=>afficherLecon(c.dataset.id));
    c.addEventListener("keydown", e=>{ if(e.key==="Enter"||e.key===" "){ e.preventDefault(); afficherLecon(c.dataset.id); } });
  });
  overlay.classList.add("show");
  corps.scrollTop = 0;
}

/* ---- Afficher une leçon ---- */
function afficherLecon(id){
  const lecon = ((LECONS_DATA && LECONS_DATA.lecons) || []).find(l=>l.id===id);
  if(!lecon) return;
  const corps  = document.getElementById("corps-lecons");
  const niveau = ((window.ETAT && ETAT.niveau) || "CM2").toLowerCase();
  const contenu = (lecon.contenu && (lecon.contenu[niveau] || lecon.contenu.cm2 || lecon.contenu.cm1)) || "";

  const objectifs = (lecon.objectifs && lecon.objectifs.length)
    ? `<div class="encadre" style="margin-bottom:14px"><b>🎯 Tu vas apprendre à :</b>
         <ul style="margin:6px 0 0 18px">${lecon.objectifs.map(o=>`<li>${_echap(o)}</li>`).join("")}</ul></div>` : "";
  const schema = lecon.schema
    ? `<h4>📐 Schéma</h4><div class="lecon-schema" style="background:#fff;border:1px solid var(--parchemin-ombre);border-radius:10px;padding:10px;margin:8px 0;text-align:center">${lecon.schema}</div>` : "";
  const lexique = (lecon.lexique && lecon.lexique.length)
    ? `<h4>📖 Lexique</h4><dl class="lecon-lexique" style="margin:6px 0 12px">${lecon.lexique.map(x=>
        `<div style="margin:4px 0"><dt style="display:inline;font-weight:bold">${_echap(x.mot)}</dt> : <dd style="display:inline;margin:0">${_echap(x.def)}</dd></div>`).join("")}</dl>` : "";
  const sources = (lecon.sources && lecon.sources.length)
    ? `<p class="doc-source" style="font-size:.8rem;opacity:.8;border-top:1px dotted var(--parchemin-ombre);padding-top:8px;margin-top:12px">
         <b>Sources :</b> ${lecon.sources.map(_echap).join(" · ")}</p>` : "";

  corps.innerHTML = `
    <div class="lecon-contenu">
      <button class="btn petit gris" id="btn-retour-biblio" style="margin-bottom:14px">← Retour aux leçons</button>
      <h3 style="color:var(--bleu-fonce);border-bottom:2px solid var(--or);padding-bottom:6px;margin-bottom:10px">${lecon.icone||""} ${_echap(lecon.titre)}</h3>
      <p style="font-size:.85rem;opacity:.75;margin-bottom:10px">⏱️ ${_echap(lecon.duree||"")} de lecture · niveau ${niveau.toUpperCase()}</p>
      ${objectifs}
      ${contenu}
      ${schema}
      ${lexique}
      ${sources}
    </div>`;
  document.getElementById("btn-retour-biblio").addEventListener("click", ouvrirBiblioLecons);
  corps.scrollTop = 0;
}

/* ---- Liste des leçons (utilisée par les tests et l'impression) ---- */
function listeFiches(){
  const d = LECONS_DATA || LECONS_FALLBACK;
  return (d.lecons || []).map(l => ({id:l.id, titre:l.titre, salle:l.salle}));
}

window.chargerLecons      = chargerLecons;
window.ouvrirBiblioLecons = ouvrirBiblioLecons;
window.afficherLecon      = afficherLecon;
window.listeFiches        = listeFiches;
