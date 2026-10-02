/* ============================================================
   LEÇONS — « L'Atelier de Léonard à Amboise »
   Bibliothèque consultable à tout moment (bouton « Leçons »),
   dans une fenêtre superposée qui ne quitte pas le jeu.
   ------------------------------------------------------------
   Repris de declaration/js/lecons.js (leçons rédigées en texte),
   avec en plus : lexique, schéma SVG, titre de frise et pied de
   leçon indiquant les sources.
   ============================================================ */

let LECONS_DATA = null;

async function chargerLecons(){
  if(LECONS_DATA) return LECONS_DATA;
  let fetchOk = false;
  try{
    const resp = await fetch("assets/data/lecons.json", {cache:"no-store"});
    if(resp.ok){
      LECONS_DATA = await resp.json();
      fetchOk = true;
    }
  }catch(e){
    console.warn("Fetch lecons.json échoué (mode file:// ?). Bascule sur la leçon embarquée.");
  }
  if(!fetchOk || !LECONS_DATA || !LECONS_DATA.lecons){
    LECONS_DATA = JSON.parse(JSON.stringify(LECONS_FALLBACK));
  }
  return LECONS_DATA;
}

/* ---- Leçon embarquée minimale (ouverture en file:// sans serveur) ---- */
const LECONS_FALLBACK = {
  lecons: [
    {
      id:"renaissance-humanisme", icone:"I", titre:"L'Atelier de Léonard à Amboise", duree:"2 min", niveau:"CM1-CM2",
      objectifs:["Situer François Ier et Léonard de Vinci"],
      contenu:{
        cm1:"<p>La Renaissance commence en Italie : on redécouvre l'art de l'Antiquité. François Ier, roi en 1515, est un mécène : il invite Léonard de Vinci à Amboise en 1516. Léonard, peintre et ingénieur, y meurt en 1519.</p>",
        cm2:"<p>Humanistes et imprimerie diffusent les savoirs antiques. François Ier protège les arts (Léonard, Chambord commencé en 1519) et les lettres (lecteurs royaux 1530, Villers-Cotterêts 1539). Les peintres utilisent la perspective et étudient les proportions.</p>"
      },
      sources:"Leçon de secours : lancez le jeu avec lancer.bat ou en ligne pour disposer des cinq leçons."
    }
  ]
};

/* ---- Ouvrir la bibliothèque ---- */
async function ouvrirBiblioLecons(){
  await chargerLecons();
  const overlay = document.getElementById("overlay-lecons");
  const corps = document.getElementById("corps-lecons");
  const lecons = LECONS_DATA.lecons || [];
  const niveau = ETAT.niveau || "CM2";
  const visibles = lecons.filter(l=>!(l.niveau==="CM2" && niveau==="CM1"));

  corps.innerHTML = `
    <p style="opacity:.8;font-style:italic;margin-bottom:14px">Clique sur une leçon pour la lire. Tu peux revenir au jeu quand tu veux.</p>
    <div class="biblio-grille">
      ${visibles.map(l=>`
        <div class="carte-lecon" data-id="${l.id}" role="button" tabindex="0">
          <div class="icone">${l.icone||""}</div>
          <div class="titre">${l.titre}</div>
          <div class="duree">${l.salle?`Salle ${l.salle} · `:""}${l.duree||""}</div>
        </div>
      `).join("")}
    </div>
  `;
  corps.querySelectorAll(".carte-lecon").forEach(c=>{
    c.addEventListener("click", ()=>afficherLecon(c.dataset.id));
    c.addEventListener("keydown", e=>{ if(e.key==="Enter"||e.key===" "){ e.preventDefault(); afficherLecon(c.dataset.id); } });
  });
  overlay.classList.add("show");
}

/* ---- Afficher une leçon en détail ---- */
function afficherLecon(id){
  const lecon = ((LECONS_DATA && LECONS_DATA.lecons)||[]).find(l=>l.id===id);
  if(!lecon) return;
  const niveau = (ETAT.niveau || "CM2").toLowerCase();
  const contenu = (lecon.contenu && (lecon.contenu[niveau] || lecon.contenu.cm2 || lecon.contenu.cm1)) || "";
  const corps = document.getElementById("corps-lecons");

  const objectifs = (lecon.objectifs && lecon.objectifs.length)
    ? `<div class="encadre" style="margin-bottom:14px"><b>Tu vas apprendre à :</b><ul style="margin:6px 0 0 18px">${lecon.objectifs.map(o=>`<li>${o}</li>`).join("")}</ul></div>` : "";

  const schema = (lecon.schema && lecon.schema.svg)
    ? `<h4>${lecon.schema.titre||"Schéma"}</h4><div class="schema-lecon">${lecon.schema.svg}</div>` : "";

  const frise = (lecon.frise && lecon.frise.length)
    ? `<h4>${lecon.frise_titre||"Frise chronologique"}</h4><div class="frise">${lecon.frise.map(e=>`<div class="evt"><span class="date">${e.date}</span>${e.evt}</div>`).join("")}</div>` : "";

  const lexique = (lecon.lexique && lecon.lexique.length)
    ? `<h4>Lexique</h4><dl class="lexique-lecon">${lecon.lexique.map(m=>`<dt><b>${m.mot}</b></dt><dd>${m.def}</dd>`).join("")}</dl>` : "";

  let docHTML = "";
  if(lecon.document){
    const d = lecon.document;
    if(d.type==="image"){
      /* Image facultative : assets/images/documents/<fichier>.jpg.
         Sans fichier, l'encadré indique où la déposer. */
      const base = d.fichier || lecon.id;
      const src = encodeURI("assets/images/documents/" + base + ".jpg");
      docHTML = `<h4>Document</h4><div class="document-epoque">
        <img class="image-document" src="${src}" alt="${d.titre||""}"
             onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">
        <div class="placeholder-image" style="display:none">${d.titre||""}<br>
          <span style="font-size:.75rem">Image facultative : déposez <code>${base}.jpg</code> dans <code>assets/images/documents/</code></span>
        </div>
        <div style="font-weight:bold;margin-top:8px">${d.titre||""}</div>
        <div class="legende-doc">${d.source||""}</div>
      </div>`;
    }else if(d.type==="text" || d.type==="texte"){
      docHTML = `<h4>Document</h4><div class="document-epoque">
        <div style="font-style:italic;padding:8px;border-left:3px solid var(--or)">${d.contenu||""}</div>
        <div style="font-weight:bold;margin-top:8px">${d.titre||""}</div>
        <div class="legende-doc">${d.source||""}</div>
      </div>`;
    }
  }

  const pied = lecon.sources
    ? `<p class="pied-lecon" style="margin-top:16px;font-size:.8rem;opacity:.8;border-top:1px dotted var(--parchemin-ombre);padding-top:8px">Sources : ${lecon.sources}</p>` : "";

  corps.innerHTML = `
    <div class="lecon-contenu">
      <button class="btn petit gris" id="btn-retour-biblio" style="margin-bottom:14px">← Retour aux leçons</button>
      <h3 style="color:var(--bleu-fonce);border-bottom:2px solid var(--or);padding-bottom:6px;margin-bottom:10px">${lecon.titre}</h3>
      ${objectifs}
      ${contenu}
      ${schema}
      ${frise}
      ${lexique}
      ${docHTML}
      ${pied}
    </div>
  `;
  document.getElementById("btn-retour-biblio").addEventListener("click", ouvrirBiblioLecons);
  corps.scrollTop = 0;
}

window.chargerLecons = chargerLecons;
window.ouvrirBiblioLecons = ouvrirBiblioLecons;
window.afficherLecon = afficherLecon;
