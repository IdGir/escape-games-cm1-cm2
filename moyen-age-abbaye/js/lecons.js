/* ============================================================
   LEÇONS — Bibliothèque consultable à tout moment (📚)
   Modal superposé, ne quitte pas le jeu.
   Repris de declaration/js/lecons.js et complété pour ce jeu :
   lexique, schéma SVG, frise, document, sources en pied de leçon.
   Chaque énigme ouvre sa leçon par le champ "lecon" (enigmes.json).
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
    console.warn("Fetch lecons.json échoué (mode file:// ?). Bascule sur les leçons embarquées.");
  }
  if(!fetchOk || !LECONS_DATA || !LECONS_DATA.lecons){
    LECONS_DATA = JSON.parse(JSON.stringify(LECONS_FALLBACK));
  }
  return LECONS_DATA;
}

/* ---- Leçons embarquées minimales (secours file://) ---- */
const LECONS_FALLBACK = {
  lecons: [
    {id:"clovis", icone:"⚔️", titre:"Après l'Empire romain : Clovis, roi des Francs", duree:"3 min", niveau:"CM1-CM2", salle:1,
     objectifs:["Savoir qui est Clovis"],
     contenu:{cm1:"<p>Clovis, roi des Francs, est baptisé à Reims par l'évêque Remi, vers l'an 500.</p>",
              cm2:"<p>Clovis (roi de 481 à 511) est baptisé à Reims par l'évêque Remi. La date est discutée : 496, 499 ou 508.</p>"}},
    {id:"charlemagne", icone:"👑", titre:"Charlemagne, son empire et les écoles", duree:"4 min", niveau:"CM1-CM2", salle:2,
     objectifs:["Situer le couronnement de l'an 800"],
     contenu:{cm1:"<p>Charlemagne est couronné empereur à Rome le jour de Noël de l'an 800.</p>",
              cm2:"<p>Le 25 décembre 800, le pape Léon III couronne Charlemagne empereur. Il n'a pas inventé l'école.</p>"}},
    {id:"scriptorium", icone:"🕯️", titre:"Les moines : prier, copier, enseigner", duree:"4 min", niveau:"CM1-CM2", salle:3,
     objectifs:["Décrire le travail des moines"],
     contenu:{cm1:"<p>Au scriptorium, les moines recopient les livres à la main sur du parchemin.</p>"}},
    {id:"hotel-dieu", icone:"🕊️", titre:"L'Église auprès des pauvres et des malades", duree:"3 min", niveau:"CM1-CM2", salle:4,
     objectifs:["Décrire le rôle social de l'Église"],
     contenu:{cm1:"<p>L'hôtel-Dieu accueille gratuitement les malades pauvres.</p>"}},
    {id:"roman-gothique", icone:"⛪", titre:"Différencier l'art roman et l'art gothique", duree:"4 min", niveau:"CM1-CM2", salle:5,
     objectifs:["Reconnaître les deux arts"],
     contenu:{cm1:"<p>Roman : voûte en berceau, murs épais. Gothique : croisée d'ogives, arcs-boutants, vitraux.</p>"}}
  ]
};

/* ---- Ouvrir la bibliothèque ---- */
async function ouvrirBiblioLecons(){
  await chargerLecons();
  const overlay = document.getElementById("overlay-lecons");
  const corps = document.getElementById("corps-lecons");
  const lecons = LECONS_DATA.lecons || [];

  // CM2 a accès à toutes les leçons ; CM1 à celles qui ne sont pas réservées au CM2
  const niveau = (window.ETAT && ETAT.niveau) || "CM2";
  const visibles = lecons.filter(l=>!(l.niveau==="CM2" && niveau==="CM1"));

  corps.innerHTML = `
    <p style="font-style:italic;margin-bottom:14px">Clique sur une leçon pour la lire. Tu peux revenir au jeu quand tu veux.</p>
    <div class="biblio-grille">
      ${visibles.map(l=>`
        <button type="button" class="carte-lecon" data-id="${l.id}">
          <div class="icone" aria-hidden="true">${l.icone||"📜"}</div>
          <div class="titre">${l.salle?"Page "+l.salle+" · ":""}${l.titre}</div>
          <div class="duree">⏱️ ${l.duree||""}</div>
        </button>
      `).join("")}
    </div>
  `;
  corps.querySelectorAll(".carte-lecon").forEach(c=>{
    c.addEventListener("click", ()=>afficherLecon(c.dataset.id));
  });
  overlay.classList.add("show");
}

/* ---- Afficher une leçon en détail ---- */
function afficherLecon(id){
  const lecon = ((LECONS_DATA && LECONS_DATA.lecons)||[]).find(l=>l.id===id);
  if(!lecon) return;
  const niveau = ((window.ETAT && ETAT.niveau) || "CM2").toLowerCase();
  const c = lecon.contenu || {};
  const contenu = c[niveau] || c.cm2 || c.cm1 || "";
  const corps = document.getElementById("corps-lecons");

  const objectifs = lecon.objectifs && lecon.objectifs.length
    ? `<div class="encadre" style="margin-bottom:14px"><b>🎯 Tu vas apprendre à :</b><ul style="margin:6px 0 0 18px">${lecon.objectifs.map(o=>`<li>${o}</li>`).join("")}</ul></div>` : "";

  const schema = lecon.schema && lecon.schema.svg
    ? `<h4>📐 ${lecon.schema.titre||"Schéma"}</h4><figure class="lecon-schema">${lecon.schema.svg}
         ${lecon.schema.legende?`<figcaption class="legende">${lecon.schema.legende}</figcaption>`:""}</figure>` : "";

  const frise = lecon.frise && lecon.frise.length
    ? `<h4>📅 Frise chronologique</h4><div class="frise">${lecon.frise.map(e=>`<div class="evt"><span class="date">${e.date}</span>${e.evt}</div>`).join("")}</div>` : "";

  const lexique = lecon.lexique && lecon.lexique.length
    ? `<h4>🔤 Les mots de la leçon</h4><div class="lecon-lexique">${lecon.lexique.map(m=>`<div class="mot"><b>${m.mot}</b>${m.def}</div>`).join("")}</div>` : "";

  let docHTML = "";
  if(lecon.document){
    const d = lecon.document;
    if(d.type==="image"){
      const base = d.fichier || lecon.id;
      const src = encodeURI("assets/images/documents/" + base + ".jpg");
      docHTML = `<h4>📄 Document</h4><div class="document-epoque">
        <img class="image-document" src="${src}" alt="${d.titre||""}"
             onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">
        <div class="placeholder-image" style="display:none">🖼️ ${d.titre||""}<br>
          <span style="font-size:.75rem">Déposez <code>${base}.jpg</code> dans <code>assets/images/documents/</code></span></div>
        <div style="font-weight:bold;margin-top:8px">${d.titre||""}</div>
        <div class="legende-doc">${d.source||""}</div>
      </div>`;
    }else if(d.type==="text" || d.type==="texte"){
      docHTML = `<h4>📄 Document</h4><div class="document-epoque">
        <div style="font-style:italic;padding:8px;border-left:3px solid var(--or)">${d.contenu}</div>
        <div style="font-weight:bold;margin-top:8px">${d.titre||""}</div>
        <div class="legende-doc">${d.source||""}</div>
      </div>`;
    }
  }

  const sources = lecon.sources && lecon.sources.length
    ? `<div class="lecon-sources"><b>Sources :</b> ${lecon.sources.map(s=>s.url
        ? `<a href="${s.url}" target="_blank" rel="noopener">${s.titre}</a>` : s.titre).join(" · ")}</div>` : "";

  corps.innerHTML = `
    <div class="lecon-contenu">
      <button class="btn petit gris" id="btn-retour-biblio" style="margin-bottom:14px">← Retour aux leçons</button>
      <h3 style="color:var(--bleu-fonce);border-bottom:2px solid var(--or);padding-bottom:6px;margin-bottom:10px">${lecon.icone||""} ${lecon.titre}</h3>
      ${objectifs}
      ${contenu}
      ${schema}
      ${frise}
      ${lexique}
      ${docHTML}
      ${sources}
    </div>
  `;
  document.getElementById("btn-retour-biblio").addEventListener("click", ouvrirBiblioLecons);
  corps.scrollTop = 0;
}

window.chargerLecons = chargerLecons;
window.ouvrirBiblioLecons = ouvrirBiblioLecons;
window.afficherLecon = afficherLecon;
