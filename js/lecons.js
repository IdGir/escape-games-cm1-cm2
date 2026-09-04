/* ============================================================
   LEÇONS — Bibliothèque consultable à tout moment
   Modal superposé, ne quitte pas le jeu
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
    console.warn("Fetch lecons.json échoué (mode file:// ?). Bascule sur leçons embarquées.");
  }
  if(!fetchOk || !LECONS_DATA || !LECONS_DATA.lecons){
    LECONS_DATA = JSON.parse(JSON.stringify(LECONS_FALLBACK));
  }
  return LECONS_DATA;
}

/* ---- Leçons embarquées minimales (fallback file://) ---- */
const LECONS_FALLBACK = {
  lecons: [
    {
      id:"causes", icone:"⚖️", titre:"Les causes de la Révolution", duree:"4 min", niveau:"CM1-CM2",
      objectifs:["Comprendre la société d'ordres","Identifier la crise de 1789"],
      contenu:{
        cm1:"<h4>Avant 1789, la France est divisée en 3 groupes</h4><div class='encadre'><b>1. Le Clergé</b> (prêtres) : peu d'impôts.<br><b>2. La Noblesse</b> : privilèges, pas d'impôts.<br><b>3. Le Tiers État</b> : le peuple (97 % des Français), qui paie tout.</div><h4>En 1789, c'est la crise !</h4><p>Le roi <b>Louis XVI</b> n'a plus d'argent. Le pain est trop cher. Le peuple a faim.</p>",
        cm2:"<h4>La société d'ordres : une France inégalitaire</h4><div class='encadre'>Sous l'Ancien Régime, la société est divisée en <b>trois ordres</b> :<br>• <b>Le Clergé</b> (≈ 0,5 %) : privilèges fiscaux.<br>• <b>La Noblesse</b> (≈ 1,5 %) : exemptions d'impôts.<br>• <b>Le Tiers État</b> (≈ 98 %) : supporte toute la fiscalité.</div><h4>La crise de 1789</h4><p>Le royaume est en <b>faillite</b>. L'hiver 1788-1789 est très rude : <b>pain à prix record</b>. Les philosophes des <b>Lumières</b> (Voltaire, Rousseau) diffusent des idées d'égalité.</p>"
      },
      frise:[{"date":"1788-89","evt":"Hiver rude, crise"},{"date":"mai 1789","evt":"États généraux"}],
      document:{type:"text", titre:"Extrait du cahier de doléances (adapté)", contenu:"« Les habitants demandent qu'imposés également, riches et pauvres participent selon leurs moyens. »", source:"Cahiers de doléances, printemps 1789."}
    },
    {
      id:"declaration", icone:"✍️", titre:"La Déclaration des droits de l'homme et du citoyen", duree:"4 min", niveau:"CM1-CM2",
      objectifs:["Date : 26 août 1789","Articles fondamentaux"],
      contenu:{
        cm1:"<h4>26 août 1789 : un texte fondateur</h4><p>Le <b>26 août 1789</b>, l'Assemblée vote la <b>Déclaration des droits de l'homme et du citoyen</b>.</p><div class='encadre'><b>Article 1 (simplifié) :</b> « Les hommes naissent <b>libres</b> et <b>égaux</b> en <b>droits</b>. »</div>",
        cm2:"<h4>26 août 1789 — un texte universel</h4><p>Votée le <b>26 août 1789</b>, la <b>DDHC</b> comporte <b>17 articles</b>. Elle inspirera la <b>Déclaration universelle des droits de l'homme</b> de l'ONU (1948).</p><div class='encadre'><b>Article 1 :</b> « Les hommes naissent et demeurent libres et égaux en droits. »<br><b>Article 2 :</b> <b>liberté, propriété, sûreté, résistance à l'oppression</b>.<br><b>Article 3 :</b> Souveraineté dans la <b>Nation</b>.</div>"
      },
      frise:[{"date":"26 aoû. 1789","evt":"Adoption de la DDHC"},{"date":"1948","evt":"Déclaration universelle ONU"}],
      document:{type:"text", titre:"Article 1 de la DDHC", contenu:"« Les hommes naissent et demeurent libres et égaux en droits. »", source:"DDHC, 26 août 1789."}
    }
  ]
};

/* ---- Ouvrir la bibliothèque ---- */
async function ouvrirBiblioLecons(){
  await chargerLecons();
  const overlay = document.getElementById("overlay-lecons");
  const corps = document.getElementById("corps-lecons");
  const lecons = LECONS_DATA.lecons || [];

  // Filtrer selon le niveau (CM2 a accès à toutes ; CM1 aux leçons non CM2-seules)
  const niveau = ETAT.niveau || "CM2";
  const visibles = lecons.filter(l=>!(l.niveau==="CM2" && niveau==="CM1"));

  corps.innerHTML = `
    <p style="opacity:.8;font-style:italic;margin-bottom:14px">Clique sur une leçon pour la consulter. Tu peux revenir au jeu quand tu veux !</p>
    <div class="biblio-grille">
      ${visibles.map(l=>`
        <div class="carte-lecon" data-id="${l.id}">
          <div class="icone">${l.icone}</div>
          <div class="titre">${l.titre}</div>
          <div class="duree">⏱️ ${l.duree}</div>
        </div>
      `).join("")}
    </div>
  `;
  // Clic sur une leçon
  corps.querySelectorAll(".carte-lecon").forEach(c=>{
    c.addEventListener("click", ()=>afficherLecon(c.dataset.id));
  });
  overlay.classList.add("show");
}

/* ---- Afficher une leçon en détail ---- */
function afficherLecon(id){
  const lecon = (LECONS_DATA.lecons||[]).find(l=>l.id===id);
  if(!lecon) return;
  // Les clés dans lecons.json sont en minuscules ("cm1" / "cm2")
  const niveau = (ETAT.niveau || "CM2").toLowerCase();
  const contenu = (lecon.contenu && lecon.contenu[niveau]) || lecon.contenu.cm2 || lecon.contenu.cm1 || "";
  const corps = document.getElementById("corps-lecons");

  // Construire la frise chronologique si présente
  let friseHTML = "";
  if(lecon.frise && lecon.frise.length){
    friseHTML = `<h4>📅 Frise chronologique</h4><div class="frise">${lecon.frise.map(e=>`<div class="evt"><span class="date">${e.date}</span>${e.evt}</div>`).join("")}</div>`;
  }
  // Document d'époque
  let docHTML = "";
  if(lecon.document){
    const d = lecon.document;
    if(d.type==="image" && d.url_wikimedia){
      docHTML = `<h4>📄 Document d'époque</h4><div class="document-epoque">
        <div class="placeholder-image">🖼️ ${d.titre}<br><span style="font-size:.75rem">Document historique (à intégrer par l'enseignant)</span><br><a href="${d.url_wikimedia}" target="_blank" style="color:var(--bleu);font-size:.8rem">Voir sur Wikimedia →</a></div>
        <div class="legende-doc">${d.source}</div>
      </div>`;
    }else if(d.type==="text"){
      docHTML = `<h4>📄 Document d'époque</h4><div class="document-epoque">
        <div style="font-style:italic;padding:8px;border-left:3px solid var(--or)">${d.contenu}</div>
        <div style="font-weight:bold;margin-top:8px">${d.titre}</div>
        <div class="legende-doc">${d.source}</div>
      </div>`;
    }
  }
  // Objectifs
  const objectifs = lecon.objectifs ? `<div class="encadre" style="margin-bottom:14px"><b>🎯 Tu vas apprendre à :</b><ul style="margin:6px 0 0 18px">${lecon.objectifs.map(o=>`<li>${o}</li>`).join("")}</ul></div>` : "";

  corps.innerHTML = `
    <div class="lecon-contenu">
      <button class="btn petit gris" id="btn-retour-biblio" style="margin-bottom:14px">← Retour à la bibliothèque</button>
      <h3 style="color:var(--bleu-fonce);border-bottom:2px solid var(--or);padding-bottom:6px;margin-bottom:10px">${lecon.icone} ${lecon.titre}</h3>
      ${objectifs}
      ${contenu}
      ${friseHTML}
      ${docHTML}
    </div>
  `;
  document.getElementById("btn-retour-biblio").addEventListener("click", ouvrirBiblioLecons);
  corps.scrollTop = 0;
}

window.chargerLecons = chargerLecons;
window.ouvrirBiblioLecons = ouvrirBiblioLecons;
window.afficherLecon = afficherLecon;
