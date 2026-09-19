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
      id:"constitution", icone:"📘", titre:"Qu'est-ce qu'une Constitution ?", duree:"3 min", niveau:"CM1-CM2",
      objectifs:["Définir une Constitution","Comprendre qu'elle est au-dessus des lois","Nommer les trois pouvoirs"],
      contenu:{
        cm1:"<h4>La règle du jeu d'un pays</h4><p>Une <b>Constitution</b> regroupe l'ensemble des <b>règles</b> qui organisent un pays. Elle est <b>au-dessus de toutes les lois</b>.</p><div class='encadre'>Trois pouvoirs : <b>législatif</b> (voter les lois), <b>exécutif</b> (les appliquer), <b>judiciaire</b> (sanctionner ceux qui ne les respectent pas).</div>",
        cm2:"<h4>Une loi au-dessus des lois</h4><p>Une <b>Constitution</b> regroupe les règles qui organisent un pays. Elle garantit les droits et les libertés de chacun et se place au-dessus de toutes les lois.</p><div class='encadre'>Depuis <b>1789</b>, la France a connu <b>quinze</b> Constitutions ; celle de <b>1958</b> est celle de la Ve République. Les trois pouvoirs y sont séparés : législatif, exécutif, autorité judiciaire.</div>"
      },
      frise:[{"date":"1789","evt":"Révolution française"},{"date":"1958","evt":"Constitution de la Ve République"}],
      document:{type:"texte", titre:"Définition officielle", contenu:"« Une Constitution regroupe l'ensemble des règles qui organisent un pays, un peu comme une règle du jeu de la politique. »", source:"Fiche « La Constitution française », cycle 3."}
    },
    {
      id:"conseil", icone:"⚖️", titre:"Le Conseil constitutionnel", duree:"3 min", niveau:"CM1-CM2",
      objectifs:["Connaître sa composition","Comprendre son rôle"],
      contenu:{
        cm1:"<h4>Neuf Sages</h4><p>Créé en <b>1958</b>, le Conseil constitutionnel compte <b>9 membres</b> nommés pour <b>9 ans</b>. Il vérifie que les lois respectent la Constitution.</p>",
        cm2:"<h4>Neuf membres, neuf ans</h4><p>Trois membres nommés par le <b>président de la République</b>, trois par le <b>président de l'Assemblée nationale</b>, trois par le <b>président du Sénat</b>. Il contrôle les lois <b>avant</b> leur promulgation, et aussi <b>après</b>, au cours d'un procès. Il siège au <b>Palais-Royal</b>.</p>"
      },
      frise:[{"date":"1958","evt":"Création du Conseil constitutionnel"},{"date":"2010","evt":"Contrôle d'une loi déjà en vigueur"}],
      document:{type:"texte", titre:"Le rôle du Conseil constitutionnel", contenu:"« Il s'assure que les lois qui sont votées au Parlement respectent bien les règles de la Constitution. »", source:"Fiche « La Constitution française », cycle 3."}
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
    if(d.type==="image"){
      /* Image de document : assets/images/documents/<fichier>.jpg
         Si le fichier n'existe pas, l'encadré de secours indique à
         l'enseignant où le déposer et conserve le lien Wikimedia. */
      const base = d.fichier || lecon.id;
      const src = encodeURI("assets/images/documents/" + base + ".jpg");
      docHTML = `<h4>📄 Document d'époque</h4><div class="document-epoque">
        <img class="image-document" src="${src}" alt="${d.titre||""}"
             onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">
        <div class="placeholder-image" style="display:none">🖼️ ${d.titre||""}<br>
          <span style="font-size:.75rem">Déposez <code>${base}.jpg</code> dans <code>assets/images/documents/</code></span>
          ${d.url_wikimedia?`<br><a href="${d.url_wikimedia}" target="_blank" rel="noopener" style="color:var(--bleu);font-size:.8rem">Voir sur Wikimedia &rarr;</a>`:""}
        </div>
        <div style="font-weight:bold;margin-top:8px">${d.titre}</div>
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
