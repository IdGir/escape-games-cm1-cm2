/* ============================================================
   IMPRESSION — Fiches A4 préparatoires & évaluations
   Génération HTML dédiée + window.print()
   - Chaque fiche : entête, cartouche élève, pagination
   - Corrigés séparés (marqués « CORRIGÉ »)
   - Mise en page A4 optimisée (print.css)
   ============================================================ */

/* ---- Imprimer le bilan de fin de partie ---- */
function imprimerBilan(){
  const zone = preparerZoneImpression();
  const min = Math.floor(ETAT.msEcoules/60000);
  const sec = Math.floor((ETAT.msEcoules%60000)/1000);
  const nbBadges = Object.values(ETAT.badges).filter(Boolean).length;
  const scoreMax = (typeof SCORE_MAX === "number") ? SCORE_MAX : 85;
  let mention = ETAT.score>=78?"🏆 Maître du Tour du Monde"
    : ETAT.score>=64?"🥈 Grand Voyageur"
    : ETAT.score>=50?"🥉 Explorateur confirmé"
    : "🧭 Apprenti géographe";
  zone.innerHTML = `
    ${enteteFiche("Bilan de partie", "Élève", ETAT.equipe, false)}
    <div class="impr-bandeau-tricolore"></div>
    <div class="impr-titre-principal">Bilan — « Le Tour du Monde en 80 minutes »</div>
    <div class="impr-soustitre">Escape game de géographie · CM1-CM2 · d’après Jules Verne</div>
    ${cartoucheEleve(ETAT.equipe, ETAT.niveau)}
    <div style="text-align:center;margin:20px 0">
      <div style="font-size:2.6rem;color:#14304a;font-weight:bold">${ETAT.score} <span style="font-size:1rem;color:#888">/ ${scoreMax} points</span></div>
      <div style="font-size:1.2rem;color:#a33327;font-weight:bold">${mention}</div>
    </div>
    <table style="width:100%;border-collapse:collapse;margin:14px 0;font-size:10pt">
      <tr><td style="padding:6px;border:1px solid #ccc">⏱️ Temps total</td><td style="padding:6px;border:1px solid #ccc"><b>${min} min ${sec} s</b></td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc">🛂 Cachets de voyage obtenus</td><td style="padding:6px;border:1px solid #ccc"><b>${ETAT.fragments.length} / 4</b> ${ETAT.fragments.length?("("+ETAT.fragments.join(", ")+")"):""}</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc">📝 Quizz final</td><td style="padding:6px;border:1px solid #ccc"><b>${ETAT.quiz.score} / 5</b></td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc">🏅 Badges</td><td style="padding:6px;border:1px solid #ccc"><b>${nbBadges} / 4</b></td></tr>
    </table>
    <div class="impr-note-enseignant">💡 Notes de l'enseignant : <br><br><br></div>
    ${piedPageFiche(1,1,"Bilan")}
  `;
  window.print();
}

/* ---- Imprimer une catégorie de fiches ----
   Deux piles distinctes, assemblées dans cet ordre :
     1. tout ce qui est distribué aux ÉLÈVES,
     2. puis tous les CORRIGÉS.
   L'enseignant imprime une fois et sépare la liasse en deux ; il ne
   distribue jamais un corrigé par erreur. Chaque partie commence sur
   une page neuve. */
async function imprimerFiches(type){
  await chargerEvaluations();
  await chargerLecons();
  const zone = preparerZoneImpression();
  const niveau = ETAT.niveau || "CM2";

  const eleve = [];     // pages distribuées aux élèves
  const corrige = [];   // pages réservées à l'enseignant

  if(type==="prepa" || type==="tout"){
    eleve.push(fichesPreparatoiresHTML());
  }
  if(type==="qcm" || type==="tout"){
    eleve.push(qcmHTML(niveau, false));
    corrige.push(qcmHTML(niveau, true));
  }
  if(type==="fermees" || type==="tout"){
    eleve.push(fermeesHTML(niveau, false));
    corrige.push(fermeesHTML(niveau, true));
  }
  if(type==="docs" || type==="tout"){
    eleve.push(etudesDocsHTML(niveau, false));
    corrige.push(etudesDocsHTML(niveau, true));
  }

  // join() par un saut de page : chaque fiche démarre bien en haut d'une page
  const pages = [...eleve, ...(corrige.length ? [separateurCorriges()] : []), ...corrige];
  zone.innerHTML = pages.filter(Boolean).join(sautPage());

  window.print();
}

/* Intercalaire qui marque visiblement le début de la pile des corrigés */
function separateurCorriges(){
  return `
    <div style="text-align:center;padding:60mm 0">
      <div style="font-size:34pt">✂️</div>
      <div style="font-size:20pt;font-weight:bold;letter-spacing:3px;margin-top:10px">CORRIGÉS</div>
      <div style="font-size:11pt;font-style:italic;color:#555;margin-top:8px">
        Les pages qui suivent sont réservées à l'enseignant.<br>
        Séparez la liasse à partir d'ici avant de distribuer.
      </div>
    </div>`;
}

/* ---- Helpers de structure A4 ---- */
function preparerZoneImpression(){
  let zone = document.querySelector(".zone-impression");
  if(!zone){
    zone = document.createElement("div");
    zone.className = "zone-impression";
    document.body.appendChild(zone);
  }
  zone.innerHTML = "";
  return zone;
}
function sautPage(){
  return '<div style="page-break-after:always;break-after:page"></div>';
}
function enteteFiche(titreFiche, type, equipe, estCorrige){
  const maintenant = new Date();
  const dateStr = `${maintenant.getDate()}/${maintenant.getMonth()+1}/${maintenant.getFullYear()}`;
  return `<div class="impr-entete">
    <div class="gauche">
      <div class="logo">🧭</div>
      <div>
        <div class="titre-fiche">${titreFiche}</div>
        <div>Le Tour du Monde en 80 minutes · Géographie CM1-CM2 · d'après Jules Verne</div>
      </div>
    </div>
    <div class="droite">
      ${estCorrige?'<div class="impr-marque-corrige">CORRIGÉ</div>':""}
      <div>Type : ${type}</div>
      <div>Équipe : ${equipe||"—"}</div>
      <div>Date : ${dateStr}</div>
    </div>
  </div>`;
}
function cartoucheEleve(equipe, niveau){
  return `<div class="impr-cartouche">
    <div class="champ"><div class="label">Prénom(s) et Nom</div><div class="ligne"></div></div>
    <div class="champ"><div class="label">Classe</div><div class="ligne"></div></div>
    <div class="champ"><div class="label">Niveau</div><div class="ligne">${niveau||""}</div></div>
    <div class="champ"><div class="label">Date</div><div class="ligne"></div></div>
  </div>`;
}
function piedPageFiche(page, total, section){
  return `<div class="impr-pied">
    <div>${section} · « Le Tour du Monde en 80 minutes » · ${ETAT.niveau||""}</div>
    <div>Page ${page} / ${total}</div>
  </div>`;
}

/* ============================================================
   FICHES PRÉPARATOIRES
   ============================================================ */
function fichesPreparatoiresHTML(){
  const fiches = EVAL_DATA.fiches_preparatoires || [];
  let html = "";
  fiches.forEach((f, i)=>{
    html += (i>0?sautPage():"") + `
      ${enteteFiche("Fiche préparatoire — Escale "+f.salle, "Élève", ETAT.equipe, false)}
      <div class="impr-bandeau-tricolore"></div>
      <div class="impr-titre-principal">Fiche préparatoire n°${f.salle}</div>
      <div class="impr-soustitre">${f.titre}</div>
      ${cartoucheEleve(ETAT.equipe, ETAT.niveau)}

      <div class="impr-fiche-prepa">
        <div class="objectifs">
          <b>🎯 Objectifs de cette escale</b>
          <ul>${f.objectifs.map(o=>`<li>${o}</li>`).join("")}</ul>
        </div>
        <div class="vocabulaire">
          <b>📖 Vocabulaire à connaître</b>
          <table style="width:100%;border-collapse:collapse;margin-top:6px;font-size:10pt">
            ${f.vocabulaire.map(v=>`<tr><td style="padding:4px 8px;border:1px solid #e0cfa6;width:30%"><span class="mot">${v.mot}</span></td><td style="padding:4px 8px;border:1px solid #e0cfa6">${v.def}</td></tr>`).join("")}
          </table>
        </div>
        <div style="margin-top:14px">
          <b>🌍 Contexte géographique</b>
          <p style="margin-top:4px">${f.contexte}</p>
        </div>
        <div class="impr-note-enseignant">💡 À lire avant de commencer l’escale ${f.salle} du jeu.</div>
      </div>
      ${piedPageFiche(f.salle, fiches.length, "Fiche préparatoire")}
    `;
  });
  return html;
}

/* ============================================================
   QCM
   ============================================================ */
function qcmHTML(niveau, corrige){
  const questions = (EVAL_DATA.qcm && EVAL_DATA.qcm[niveau]) || [];
  const total = questions.reduce((s,q)=>s+q.pts,0);
  let html = `
    ${enteteFiche("QCM — "+niveau, corrige?"Corrigé":"Évaluation", ETAT.equipe, corrige)}
    <div class="impr-bandeau-tricolore"></div>
    <div class="impr-titre-principal">QCM — Géographie : le tour du monde</div>
    <div class="impr-soustitre">Niveau ${niveau} · ${questions.length} questions · Barème : ${total} points</div>
    ${!corrige?cartoucheEleve(ETAT.equipe, niveau):""}
    <div class="impr-note-enseignant">Consigne : entoure la bonne réponse.${corrige?" <b>(Corrigé — les bonnes réponses sont surlignées en vert.)</b>":""}</div>
    <div class="${corrige?"impr-corrige":""}">
  `;
  questions.forEach((q, i)=>{
    html += `<div class="impr-question">
      <div><span class="num">Question ${i+1}.</span> ${q.q} <span class="barre-pts">/${q.pts} pt</span></div>
      <div class="cases-qcm">
        ${q.options.map((o, j)=>`<div class="opt ${corrige && j===q.bonne?"bonne":""}"><span class="case">○</span> ${String.fromCharCode(97+j)}) ${o}</div>`).join("")}
      </div>
    </div>`;
  });
  html += `</div>
    ${baremeHTML("QCM "+niveau, total, questions.length)}
    ${piedPageFiche(1, 1, "QCM "+niveau)}
  `;
  return html;
}

/* ============================================================
   QUESTIONS FERMÉES (V/F + réponses courtes)
   ============================================================ */
function fermeesHTML(niveau, corrige){
  const questions = (EVAL_DATA.questions_fermees && EVAL_DATA.questions_fermees[niveau]) || [];
  const total = questions.reduce((s,q)=>s+q.pts,0);
  let html = `
    ${enteteFiche("Questions — "+niveau, corrige?"Corrigé":"Évaluation", ETAT.equipe, corrige)}
    <div class="impr-bandeau-tricolore"></div>
    <div class="impr-titre-principal">Questions — Vrai/Faux et réponses courtes</div>
    <div class="impr-soustitre">Niveau ${niveau} · ${questions.length} questions · Barème : ${total} points</div>
    ${!corrige?cartoucheEleve(ETAT.equipe, niveau):""}
    <div class="${corrige?"impr-corrige":""}">
  `;
  questions.forEach((q, i)=>{
    html += `<div class="impr-question">
      <div><span class="num">Question ${i+1}.</span> ${q.q} <span class="barre-pts">/${q.pts} pt${q.pts>1?"s":""}</span></div>`;
    if(q.type==="vf"){
      html += `<div class="vrai-faux">
        ${corrige
          ? `<span><b>Réponse :</b> ${q.bonne==="vrai"?"✓ VRAI":"✗ FAUX"}</span>`
          : `<span><span class="case">○</span> VRAI</span><span><span class="case">○</span> FAUX</span>`}
      </div>`;
    }else if(q.type==="court"){
      if(corrige){
        html += `<div class="reponse-attendue"><b>Réponse attendue :</b> ${q.rep}</div>`;
      }else{
        html += `<div class="reponses-courtes"><div class="ligne-rep"></div></div>`;
      }
    }
    html += `</div>`;
  });
  html += `</div>
    ${baremeHTML("Questions fermées "+niveau, total, questions.length)}
    ${piedPageFiche(1, 1, "Questions "+niveau)}
  `;
  return html;
}

/* ============================================================
   ÉTUDE DE DOCUMENTS
   ============================================================ */
function etudesDocsHTML(niveau, corrige){
  const docs = (EVAL_DATA.etudes_documents && EVAL_DATA.etudes_documents[niveau]) || [];
  let html = `
    ${enteteFiche("Étude de documents — "+niveau, corrige?"Corrigé":"Évaluation", ETAT.equipe, corrige)}
    <div class="impr-bandeau-tricolore"></div>
    <div class="impr-titre-principal">Étude de documents</div>
      <div class="impr-soustitre">Niveau ${niveau} · Géographie</div>
    ${!corrige?cartoucheEleve(ETAT.equipe, niveau):""}
    <div class="${corrige?"impr-corrige":""}">
  `;
  docs.forEach((d, i)=>{
    const totalQ = d.questions.reduce((s,q)=>s+q.pts,0);
    html += `<div class="impr-document">
      <div style="font-weight:bold;font-size:11pt;margin-bottom:6px">Document ${i+1} — ${d.titre}</div>
      <div style="font-style:italic;padding:8px;border-left:3px solid #c9a227;margin:6px 0">${d.document.contenu}</div>
      <div class="legende-doc">Source : ${d.document.source}</div>
    </div>`;
    if(d.document.url_wikimedia){
      html += `<div style="font-size:8pt;color:#666;margin:4px 0 10px">🖼️ Document visuel à imprimer par l'enseignant : <a href="${d.document.url_wikimedia}">${d.document.url_wikimedia}</a></div>`;
    }
    html += `<p style="font-weight:bold;margin-top:8px">Questions sur le document ${i+1} <span class="barre-pts">/${totalQ} pts</span></p>`;
    d.questions.forEach((q, j)=>{
      html += `<div class="impr-question">
        <div><span class="num">${i+1}.${j+1}.</span> ${q.q} <span class="barre-pts">/${q.pts} pt${q.pts>1?"s":""}</span></div>`;
      if(corrige){
        if(q.rep_attendue){
          html += `<div class="reponse-attendue"><b>Éléments attendus :</b> ${q.rep_attendue}</div>`;
        }else{
          html += `<div class="reponse-attendue"><b>Réponse :</b> ${q.rep||""}</div>`;
        }
      }else{
        if(q.type==="ouverte"){
          html += `<div class="impr-lignes-reponse"><div class="ligne"></div><div class="ligne"></div><div class="ligne"></div></div>`;
        }else{
          html += `<div class="reponses-courtes"><div class="ligne-rep"></div></div>`;
        }
      }
      html += `</div>`;
    });
  });
  html += `</div>${piedPageFiche(1, 1, "Étude de documents "+niveau)}`;
  return html;
}

/* ============================================================
   BARÈME RÉCAPITULATIF
   ============================================================ */
function baremeHTML(titre, total, nbQ){
  return `<div class="impr-bareme">
    <table>
      <tr><th>Évaluation</th><th>Questions</th><th>Total</th><th>Appréciation</th></tr>
      <tr>
        <td>${titre}</td>
        <td>${nbQ}</td>
        <td><b>${total} / ${total}</b></td>
        <td style="width:30%">__________________</td>
      </tr>
    </table>
  </div>`;
}

window.imprimerBilan = imprimerBilan;
window.imprimerFiches = imprimerFiches;
window.separateurCorriges = separateurCorriges;
