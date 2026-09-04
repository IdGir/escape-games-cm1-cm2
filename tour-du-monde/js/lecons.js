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

/* ---- Leçons embarquées minimales (fallback file://) ----
   La version complète (6 leçons) est dans assets/data/lecons.json ;
   ces deux-ci suffisent à jouer même sans accès au fichier. ---- */
const LECONS_FALLBACK = {
  lecons: [
    {
      id:"planisphere", icone:"🗺️", titre:"Les continents et les océans", duree:"4 min", niveau:"CM1-CM2",
      objectifs:["Nommer les 6 continents","Nommer les 5 océans","Les situer sur un planisphère"],
      contenu:{
        cm1:"<h4>La Terre, vue à plat</h4><p>Un <b>planisphère</b> est une carte qui montre toute la Terre à plat. On y voit les <b>continents</b> (les grandes terres) et les <b>océans</b> (les grandes étendues d'eau).</p><div class='encadre'><b>Les 6 continents :</b><br>Europe · Asie · Afrique · Amérique du Nord · Amérique du Sud · Océanie<br>(et l'<b>Antarctique</b>, tout au sud, couvert de glace)</div><div class='encadre'><b>Les 5 océans :</b><br>Pacifique (le plus grand) · Atlantique · Indien · Arctique · Austral</div>",
        cm2:"<h4>Lire un planisphère</h4><p>Un <b>planisphère</b> représente la sphère terrestre à plat : les formes sont donc un peu déformées, surtout près des pôles.</p><div class='encadre'><b>Repères utiles :</b><br>• L'<b>Asie</b> est le plus vaste des continents.<br>• L'<b>Afrique</b> et l'<b>Amérique du Sud</b> sont traversées par l'<b>équateur</b>.<br>• L'<b>Antarctique</b> entoure le pôle Sud.<br>• Le <b>Pacifique</b> est le plus grand océan, l'<b>Arctique</b> le plus petit.</div><p>Les océans couvrent environ <b>70 %</b> de la surface de la Terre.</p>"
      },
      frise:[{date:"1492",evt:"Colomb atteint l'Amérique"},{date:"1522",evt:"Premier tour du monde"},{date:"1872",evt:"Le pari de Phileas Fogg"}],
      document:{type:"text", titre:"Le monde en quatre-vingts jours", contenu:"« Londres — Suez, 7 jours ; Suez — Bombay, 13 jours ; Bombay — Calcutta, 3 jours ; Calcutta — Hong-Kong, 13 jours… Total : quatre-vingts jours. »", source:"Jules Verne, Le Tour du monde en quatre-vingts jours, 1873."}
    },
    {
      id:"fuseaux", icone:"⏰", titre:"Méridiens, parallèles et fuseaux horaires", duree:"5 min", niveau:"CM1-CM2",
      objectifs:["Distinguer méridiens et parallèles","Comprendre les fuseaux horaires","Expliquer le jour gagné vers l'est"],
      contenu:{
        cm1:"<h4>Des lignes imaginaires</h4><div class='encadre'><b>L'équateur</b> : la ligne horizontale qui coupe la Terre en deux moitiés.<br><b>Le méridien de Greenwich</b> : la ligne verticale de référence, qui passe par Londres.</div><h4>Il n'est pas la même heure partout</h4><p>La Terre tourne sur elle-même : quand il fait jour chez nous, il fait nuit de l'autre côté. Quand il est <b>midi à Londres</b>, il est <b>13 h à Paris</b> et <b>20 h à Hong Kong</b>.</p>",
        cm2:"<h4>Le quadrillage de la Terre</h4><div class='encadre'><b>Les parallèles</b> sont des cercles horizontaux : ils donnent la <b>latitude</b>.<br><b>Les méridiens</b> vont d'un pôle à l'autre : ils donnent la <b>longitude</b>, à partir de <b>Greenwich</b>.</div><h4>Les 24 fuseaux horaires</h4><div class='encadre'>360° ÷ 24 h = <b>15° par heure</b><br>Vers l'<b>est</b> → on <b>ajoute</b> une heure par fuseau.<br>Vers l'<b>ouest</b> → on <b>retire</b> une heure par fuseau.</div><p>En faisant le tour complet vers l'est, Phileas Fogg a ajouté 24 fois une heure : <b>24 heures, soit un jour entier</b>. Il croyait avoir mis 81 jours ; il n'en avait mis que 80.</p>"
      },
      frise:[{date:"1675",evt:"Fondation de l'observatoire de Greenwich"},{date:"1884",evt:"Greenwich devient le méridien de référence"}],
      document:{type:"text", titre:"Le jour gagné", contenu:"« Il y a trois cent soixante degrés sur la circonférence terrestre, et ces trois cent soixante degrés, multipliés par quatre minutes, donnent précisément vingt-quatre heures. »", source:"Jules Verne, chapitre XXXVII."}
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
      docHTML = `<h4>📄 Document</h4><div class="document-epoque">
        <img class="image-document" src="${src}" alt="${d.titre||""}"
             onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">
        <div class="placeholder-image" style="display:none">🖼️ ${d.titre||""}<br>
          <span style="font-size:.75rem">Déposez <code>${base}.jpg</code> dans <code>assets/images/documents/</code></span>
          ${d.url_wikimedia?`<br><a href="${d.url_wikimedia}" target="_blank" rel="noopener" style="color:var(--azur);font-size:.8rem">Voir sur Wikimedia &rarr;</a>`:""}
        </div>
        <div style="font-weight:bold;margin-top:8px">${d.titre||""}</div>
        <div class="legende-doc">${d.source||""}</div>
      </div>`;
    }else if(d.type==="text"){
      docHTML = `<h4>📄 Document</h4><div class="document-epoque">
        <div style="font-style:italic;padding:8px;border-left:3px solid var(--laiton)">${d.contenu}</div>
        <div style="font-weight:bold;margin-top:8px">${d.titre}</div>
        <div class="legende-doc">${d.source}</div>
      </div>`;
    }
  }
  /* Carte ou illustration facultative. Une leçon peut déclarer :
       "carte": {"base":"planisphere-vierge", "legende":"…", "source":"…"}
     Le fichier attendu est assets/images/cartes/<base>.jpg ; s'il est
     absent, un encadré discret indique où le déposer. */
  let carteHTML = "";
  if(lecon.carte && typeof htmlIllustration === "function"){
    carteHTML = htmlIllustration(lecon.carte.base, lecon.carte.legende, lecon.carte.source);
  }

  /* Vidéo pédagogique facultative. Une leçon peut déclarer :
       "video": {"base":"lecon-fuseaux", "titre":"…", "source":"…"}
     Le fichier attendu est assets/videos/<base>.mp4. */
  let videoHTML = "";
  if(lecon.video && typeof htmlVideoDoc === "function"){
    videoHTML = `<h4>🎬 La leçon en vidéo</h4>` +
      htmlVideoDoc(lecon.video.base, lecon.video.titre || lecon.titre, lecon.video.source || "");
  }

  // Objectifs
  const objectifs = lecon.objectifs ? `<div class="encadre" style="margin-bottom:14px"><b>🎯 Tu vas apprendre à :</b><ul style="margin:6px 0 0 18px">${lecon.objectifs.map(o=>`<li>${o}</li>`).join("")}</ul></div>` : "";

  corps.innerHTML = `
    <div class="lecon-contenu">
      <button class="btn petit gris" id="btn-retour-biblio" style="margin-bottom:14px">← Retour à la bibliothèque</button>
      <h3 style="color:var(--abysse-2);border-bottom:2px solid var(--laiton);padding-bottom:6px;margin-bottom:10px">${lecon.icone} ${lecon.titre}</h3>
      ${objectifs}
      ${contenu}
      ${carteHTML}
      ${videoHTML}
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
