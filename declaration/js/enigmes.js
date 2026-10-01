/* ============================================================
   ÉNIGMES — 5 énigmes interactives (moteur v2, octobre 2026 :
   validation par bouton, nombre de réponses justes seulement,
   10 points du premier coup, 3 après une erreur)
   Chaque énigme : enigmeSalle(n) retourne le HTML,
                  activerEnigme(n) attache les interactions
   ============================================================ */

function enigmeSalle(n){
  switch(n){
    case 1: return enigme1HTML();
    case 2: return enigme2HTML();
    case 3: return enigme3HTML();
    case 4: return enigme4HTML();
    case 5: return enigme5HTML();
  }
  return "";
}
function activerEnigme(n){
  ({1:activerEnigme1,2:activerEnigme2,3:activerEnigme3,4:activerEnigme4,5:activerEnigme5}[n]||(()=>{}))();
}

/* ============================================================
   ÉNIGME 1 — Cahier de doléances codé (anagramme, v2)
   Les lettres marquées sont dans le désordre et deux sont des
   pièges : les élèves rangent les bonnes dans les cases.
   ============================================================ */
function lc(l, cls){ return `<span class="lettre-clic ${cls}" data-l="${l}">`; }
function enigme1HTML(){
  const cm1 = ETAT.niveau==="CM1";
  const texte = cm1
    ? `<p class="texte-doc">${lc("R","cm1")}R</span>éunissons nos voix contre les abus. ${lc("É","cm1")}É</span>coutez la plainte des paysans ! ${lc("A","cm1")}A</span>ssez de taxes injustes ! ${lc("T","cm1")}T</span>erminons les privilèges des nobles. ${lc("L","cm1")}L</span>es habitants demandent qu'on impose riches et pauvres. ${lc("S","cm1")}S</span>ans justice, pas de paix. ${lc("I","cm1")}I</span>l faut que la justice soit la même pour tous. ${lc("B","cm1")}B</span>eaucoup souffrent de la faim. ${lc("E","cm1")}E</span>nfin, que chacun puisse parler sans crainte !</p>`
    : `<p class="texte-doc">Les habitants de la paroisse demandent que soient ${lc("R","cm2")}r</span>etirées toutes les charges injustes qui pèsent sur le peuple ; qu'${lc("É","cm2")}é</span>galement imposés, riches et pauvres participent selon leurs moyens. Ils demandent que ${lc("B","cm2")}b</span>ientôt la justice ne soit plus vendue ni achetée ; que les ${lc("S","cm2")}s</span>eigneurs renoncent à leurs droits de chasse ; qu'${lc("E","cm2")}e</span>nfin les privilèges héréditaires soient abolis ; que la ${lc("L","cm2")}l</span>oi seule guide le royaume ; que ${lc("T","cm2")}t</span>ous les Français soient égaux en droits, sans égard à leur naissance ; que les ${lc("I","cm2")}i</span>mpôts soient votés par la nation, et que chacun ${lc("P","cm2")}p</span>uisse s'exprimer sans crainte.</p>`;
  return `
    <h3>📖 Le cahier de doléances</h3>
    ${v2Bandeau()}
    ${texte}
    <div class="slots-lettres" id="slots-1">${Array.from({length:7}).map(()=>'<button type="button" class="slot vide"></button>').join("")}</div>
    <div class="center"><button class="btn vert" id="btn-verif-1">✅ Vérifier le mot</button></div>
    <div class="feedback" id="fb-1"></div>
    <div class="barre-outils"><button class="btn or" id="btn-indice">💡 Indice</button></div>
  `;
}
function activerEnigme1(){
  v2Debut();
  const cible = ["L","I","B","E","R","T","É"];
  const ana = v2Anagramme("#slots-1 .slot", ".lettre-clic");
  document.getElementById("btn-verif-1").addEventListener("click", ()=>{
    if(!ana.complet()) return v2Incomplet("fb-1", "Remplis les 7 cases avant de vérifier. Un clic sur une case la vide.");
    const mot = ana.mot();
    const justes = mot.filter((l,i)=>l === cible[i]).length;
    if(justes === cible.length) v2Reussite("fb-1", err=>validerSalle(1, err));
    else v2Echec("fb-1", justes, cible.length, "lettres bien placées");
  });
  const indices = ETAT.niveau==="CM1"
    ? ["Le mot a 7 lettres et se termine par <b>É</b>.", "Les lettres <b>A</b> et <b>S</b> sont des pièges.", "Le mot veut dire « ne pas être prisonnier »."]
    : ["Le mot a 7 lettres : c'est un mot de la devise de la France.", "Deux lettres marquées ne servent pas : une consonne du début et une de la fin du texte.", "Le mot commence par <b>L</b> et finit par <b>É</b>."];
  activerBoutonIndice(indices);
}

/* ============================================================
   ÉNIGME 2 — La Marseillaise mystérieuse
   ============================================================ */
function enigme2HTML(){
  const cm1 = ETAT.niveau==="CM1";
  if(cm1){
    return `<h3>🎵 La Marseillaise mystérieuse</h3>
      ${v2Bandeau()}
      <p style="text-align:center;opacity:.7;font-style:italic">Clique sur un extrait à gauche, puis sur l'image qui lui correspond à droite. Un nouveau clic défait la paire.</p>
      <div class="rang-match">
        <div class="colonne-match" id="col-extraits">
          <div class="carte-match" data-id="e1" data-bon="i1">« Aux armes, citoyens ! »</div>
          <div class="carte-match" data-id="e2" data-bon="i2">« Allons enfants de la Patrie »</div>
          <div class="carte-match" data-id="e3" data-bon="i3">« Le jour de gloire est arrivé »</div>
        </div>
        <div class="colonne-match" id="col-images">
          ${v2Melanger([
            '<div class="carte-match" data-id="i1"><span class="emoji">🏰</span>Prise de la Bastille</div>',
            '<div class="carte-match" data-id="i2"><span class="emoji">🚶</span>Volontaires en marche</div>',
            '<div class="carte-match" data-id="i3"><span class="emoji">🚩</span>Drapeau tricolore hissé</div>']).join("")}
        </div>
      </div>
      <div class="center"><button class="btn vert" id="btn-verif-2">✅ Vérifier les associations</button></div>
      <div class="feedback" id="fb-2"></div>
      <div class="barre-outils"><button class="btn or" id="btn-indice">💡 Indice</button></div>`;
  }
  // CM2 : ordre chronologique
  const evts = [
    {id:"eg", txt:"États généraux réunis à Versailles", date:"mai 1789", rang:1},
    {id:"jp", txt:"Serment du Jeu de paume", date:"20 juin 1789", rang:2},
    {id:"ba", txt:"Prise de la Bastille", date:"14 juillet 1789", rang:3},
    {id:"dec", txt:"Adoption de la Déclaration des droits", date:"26 août 1789", rang:4},
    {id:"mf", txt:"Marche des femmes à Versailles", date:"5 octobre 1789", rang:5},
  ];
  evts.sort(()=>Math.random()-0.5);
  return `<h3>🎵 Les 5 grands événements de 1789</h3>
    ${v2Bandeau()}
    <p style="text-align:center;opacity:.7;font-style:italic">Remets-les dans l'ordre chronologique avec les flèches ▲▼.</p>
    <div class="liste-ordre" id="liste-ordre">
      ${evts.map(e=>`<div class="item-ordre" data-id="${e.id}" data-rang="${e.rang}">
        <span class="rang">${e.rang}</span>
        <div class="contenu"><b>${e.txt}</b><br><span style="font-size:.8rem;opacity:.7">${e.date}</span></div>
        <div class="controles-ordre">
          <button class="btn-monter" aria-label="Monter">▲</button>
          <button class="btn-descendre" aria-label="Descendre">▼</button>
        </div>
      </div>`).join("")}
    </div>
    <div class="center"><button class="btn vert" id="btn-verif-ordre">✅ Vérifier l'ordre</button></div>
    <div class="feedback" id="fb-2"></div>
    <div class="barre-outils"><button class="btn or" id="btn-indice">💡 Indice</button></div>`;
}
function activerEnigme2(){
  v2Debut();
  const cm1 = ETAT.niveau==="CM1";
  if(cm1){
    const asso = v2Association("#col-extraits .carte-match", "#col-images .carte-match");
    document.getElementById("btn-verif-2").addEventListener("click", ()=>{
      if(!asso.complet()) return v2Incomplet("fb-2", "Associe chaque extrait à une image avant de vérifier.");
      const j = asso.justes();
      if(j === asso.total) v2Reussite("fb-2", err=>validerSalle(2, err));
      else v2Echec("fb-2", j, asso.total, "associations justes");
    });
    activerBoutonIndice(["La Bastille est attaquée quand on crie « Aux armes ! ».","« Enfants de la Patrie » = des volontaires qui marchent ensemble.","Le drapeau est hissé quand « le jour de gloire est arrivé »."]);
  }else{
    const liste = document.getElementById("liste-ordre");
    liste.addEventListener("click", e=>{
      const item = e.target.closest(".item-ordre");
      if(!item) return;
      if(e.target.classList.contains("btn-monter")){
        const prev = item.previousElementSibling;
        if(prev) liste.insertBefore(item, prev);
      }else if(e.target.classList.contains("btn-descendre")){
        const next = item.nextElementSibling;
        if(next) liste.insertBefore(next, item);
      }
      rafraichirRangs();
    });
    function rafraichirRangs(){
      document.querySelectorAll("#liste-ordre .item-ordre").forEach((it,i)=>it.querySelector(".rang").textContent = i+1);
    }
    rafraichirRangs();
    document.getElementById("btn-verif-ordre").addEventListener("click", ()=>{
      const rangs = [...document.querySelectorAll("#liste-ordre .item-ordre")].map(it=>+it.dataset.rang);
      const justes = rangs.filter((r,i)=>r === i+1).length;
      if(justes === rangs.length) v2Reussite("fb-2", err=>validerSalle(2, err));
      else v2Echec("fb-2", justes, rangs.length, "événements à la bonne place");
    });
    activerBoutonIndice(["Le tout premier événement de 1789 est la réunion des <b>États généraux</b> (mai 1789).","La <b>prise de la Bastille</b> (14 juillet) vient avant la <b>Déclaration</b> (26 août).","Le dernier est la <b>marche des femmes</b> (5 octobre)."]);
  }
}

/* ============================================================
   ÉNIGME 3 — Le rébus de la Déclaration
   ============================================================ */
function enigme3HTML(){
  const mots = [
    {symbole:"🔓", libelle:"chaîne brisée", bonne:"LIBRES", options:["LIBRES","PRISON","OR"]},
    {symbole:"⚖️", libelle:"balance égale", bonne:"ÉGAUX", options:["ÉGAUX","FORTS","RICHES"]},
    {symbole:"📜", libelle:"parchemin signé", bonne:"DROITS", options:["DROITS","POIDS","DEVOIRS"]},
  ];
  return `<h3>🔮 Le rébus de la Déclaration</h3>
    ${v2Bandeau()}
    <div class="rebus">
      ${mots.map((m,i)=>`<div class="rebus-item">
        <span class="symbole">${m.symbole}</span>
        <div class="libelle">${m.libelle}</div>
        <select data-i="${i}" class="choix-rebus">
          <option value="">— choisir —</option>
          ${m.options.map(o=>`<option value="${o}">${o}</option>`).join("")}
        </select>
      </div>`).join("")}
    </div>
    <div class="phrase-trou" id="phrase-trou">« Les hommes naissent <span class="trou" data-i="0">…</span> et <span class="trou" data-i="1">…</span> en <span class="trou" data-i="2">…</span>. »</div>
    <div class="center"><button class="btn vert" id="btn-verif-rebus">✅ Vérifier la phrase</button></div>
    <div class="feedback" id="fb-3"></div>
    <div class="barre-outils"><button class="btn or" id="btn-indice">💡 Indice</button></div>`;
}
function activerEnigme3(){
  v2Debut();
  const reponse = ["LIBRES","ÉGAUX","DROITS"];
  document.querySelectorAll(".choix-rebus").forEach(sel=>{
    sel.addEventListener("change", ()=>{
      const trou = document.querySelector(`.trou[data-i="${sel.dataset.i}"]`);
      trou.textContent = sel.value || "…";
    });
  });
  document.getElementById("btn-verif-rebus").addEventListener("click", ()=>{
    const choix = [...document.querySelectorAll(".choix-rebus")].map(s=>s.value);
    if(choix.some(v=>!v)) return v2Incomplet("fb-3", "Choisis un mot pour chaque rébus avant de vérifier.");
    const justes = choix.filter((v,i)=>v === reponse[i]).length;
    if(justes === reponse.length) v2Reussite("fb-3", err=>validerSalle(3, err));
    else v2Echec("fb-3", justes, reponse.length, "mots justes");
  });
  const indices = ETAT.niveau==="CM1"
    ? ["Une chaîne brisée, c'est l'inverse d'être prisonnier → c'est être…","La balance égale des deux plateaux → le mot commence par É-.","Le parchemin signé protège ce qu'on possède : nos…"]
    : ["Pense au mot de la devise qui s'oppose à « prison ».","Le second rébus est un jeu phonétique : « = eau » → égaux.","Le parchemin signé garantit nos droits (et nos devoirs)."];
  activerBoutonIndice(indices);
}

/* ============================================================
   ÉNIGME 4 — Les personnages clés
   ============================================================ */
function enigme4HTML(){
  const cm1 = ETAT.niveau==="CM1";
  let persos = [
    {id:"louis", emoji:"👑", nom:"Louis XVI", bon:"c-louis", ev:"États généraux"},
    {id:"mira", emoji:"🎤", nom:"Mirabeau", bon:"c-mira", ev:"Séance royale"},
    {id:"dant", emoji:"🔊", nom:"Danton", bon:"c-dant", ev:"Chute monarchie"},
    {id:"robe", emoji:"⚖️", nom:"Robespierre", bon:"c-robe", ev:"La Terreur"},
  ];
  let citations = [
    {id:"c-louis", txt:"« J'ai peu de confiance dans les assemblées. »"},
    {id:"c-mira", txt:"« Nous sommes ici par la volonté du peuple. »"},
    {id:"c-dant", txt:"« De l'audace, encore de l'audace ! »"},
    {id:"c-robe", txt:"« La vertu sans laquelle la terreur est funeste. »"},
  ];
  if(!cm1){
    persos.push({id:"bail", emoji:"🏛️", nom:"Bailly", bon:"c-bail", ev:"Maire de Paris"});
    persos.push({id:"olym", emoji:"✒️", nom:"Olympe de Gouges", bon:"c-olym", ev:"Droits des femmes"});
    citations.push({id:"c-bail", txt:"« La Bastille est prise ! »"});
    citations.push({id:"c-olym", txt:"« La femme naît libre et demeure égale à l'homme. »"});
  }
  citations.sort(()=>Math.random()-0.5);
  return `<h3>👥 Les grands personnages</h3>
    ${v2Bandeau()}
    <p style="text-align:center;opacity:.7;font-style:italic">Clique sur un portrait, puis sur sa citation. Un nouveau clic défait la paire.</p>
    <div class="rang-match">
      <div class="colonne-match" id="col-persos">
        ${persos.map(p=>`<div class="carte-match" data-id="${p.id}" data-bon="${p.bon}"><span class="emoji">${p.emoji}</span><b>${p.nom}</b><br><span style="font-size:.75rem;opacity:.7">${p.ev}</span></div>`).join("")}
      </div>
      <div class="colonne-match" id="col-citations">
        ${citations.map(c=>`<div class="carte-match" data-id="${c.id}">${c.txt}</div>`).join("")}
      </div>
    </div>
    <div class="center"><button class="btn vert" id="btn-verif-4">✅ Vérifier les associations</button></div>
    <div class="feedback" id="fb-4"></div>
    <div class="barre-outils"><button class="btn or" id="btn-indice">💡 Indice</button></div>`;
}
function activerEnigme4(){
  v2Debut();
  const asso = v2Association("#col-persos .carte-match", "#col-citations .carte-match");
  document.getElementById("btn-verif-4").addEventListener("click", ()=>{
    if(!asso.complet()) return v2Incomplet("fb-4", "Associe chaque personnage à une citation avant de vérifier.");
    const j = asso.justes();
    if(j === asso.total) v2Reussite("fb-4", err=>validerSalle(4, err));
    else v2Echec("fb-4", j, asso.total, "associations justes");
  });
  const indices = ETAT.niveau==="CM1"
    ? ["<b>Danton</b> est connu pour réclamer « de l'audace ».","<b>Louis XVI</b> est le roi, peu favorable aux assemblées.","<b>Olympe de Gouges</b> défendait les droits des femmes (si présente)."]
    : ["<b>Mirabeau</b> a défié le roi le 23 juin 1789.","<b>Robespierre</b> est associé à la Terreur et à la vertu.","<b>Bailly</b> a annoncé la prise de la Bastille, en tant que maire de Paris."];
  activerBoutonIndice(indices);
}

/* ============================================================
   ÉNIGME 5 — Le mécanisme de l'Assemblée (FINALE)
   ============================================================ */
const PLAN_REPONSES = {
  CM1: {pres:"Bailly", gauche:"Robespierre", droite:"Mounier", date:"26 août 1789", lieu:"Versailles"},
  CM2: {pres:"Bailly", gauche:"Robespierre", droite:"Mounier", centre:"Mirabeau", fond:"Danton", date:"26 août 1789", lieu:"Versailles", secret:"Olympe de Gouges"}
};
function enigme5HTML(){
  const cm1 = ETAT.niveau==="CM1";
  const labels = cm1
    ? {pres:"Président", gauche:"Tribune gauche", droite:"Tribune droite", date:"Date au fronton", lieu:"Lieu"}
    : {pres:"Président", gauche:"Tribune gauche", droite:"Tribune droite", centre:"Centre", fond:"Tribune du fond", date:"Date au fronton", lieu:"Lieu", secret:"Secrétaire"};
  const reponses = PLAN_REPONSES[ETAT.niveau];
  const etiquettes = Object.values(reponses).slice().sort(()=>Math.random()-0.5);
  const planHTML = cm1 ? `
    <div class="plan" id="plan-assemblee">
      <table>
        <tr><td colspan="3" data-emp="pres">${labels.pres}</td></tr>
        <tr>
          <td data-emp="gauche">${labels.gauche}</td>
          <td class="estrade">🏛️</td>
          <td data-emp="droite">${labels.droite}</td>
        </tr>
        <tr><td data-emp="date">${labels.date}</td><td class="vide-neutre"></td><td data-emp="lieu">${labels.lieu}</td></tr>
      </table>
    </div>` : `
    <div class="plan" id="plan-assemblee">
      <table>
        <tr><td colspan="3" data-emp="pres">${labels.pres}</td></tr>
        <tr>
          <td data-emp="gauche">${labels.gauche}</td>
          <td data-emp="centre">${labels.centre}</td>
          <td data-emp="droite">${labels.droite}</td>
        </tr>
        <tr>
          <td data-emp="fond">${labels.fond}</td>
          <td data-emp="secret">${labels.secret}</td>
          <td class="vide-neutre"></td>
        </tr>
        <tr><td data-emp="date">${labels.date}</td><td colspan="2" data-emp="lieu">${labels.lieu}</td></tr>
      </table>
    </div>`;
  return `<h3>🏛️ Le mécanisme de l'Assemblée</h3>
    ${v2Bandeau()}
    ${planHTML}
    <p style="text-align:center;font-size:.85rem;opacity:.7;margin-top:8px">Clique sur une case, puis sur une étiquette ci-dessous. Un clic sur une case remplie la vide.</p>
    <div class="banque" id="banque-etiquettes">
      ${etiquettes.map(e=>`<div class="etiquette" data-val="${e}">${e}</div>`).join("")}
    </div>
    <div class="center" style="margin-top:14px"><button class="btn vert" id="btn-verif-plan">✅ Vérifier le plan</button></div>
    <div class="feedback" id="fb-5"></div>
    <div class="barre-outils"><button class="btn or" id="btn-indice">💡 Indice</button></div>`;
}
function activerEnigme5(){
  v2Debut();
  const cm1 = ETAT.niveau==="CM1";
  const cases = {};          // emplacement → {td, label, et (étiquette posée)}
  let caseSel = null;
  const banque = document.getElementById("banque-etiquettes");
  const dessiner = ()=>Object.values(cases).forEach(c=>{
    c.td.innerHTML = c.et ? `<b>${c.et.dataset.val}</b><br><span style="font-size:.7rem;opacity:.7">${c.label}</span>` : c.label;
    c.td.classList.toggle("etiquette-placee", !!c.et);
    c.td.style.outline = (c === caseSel) ? "3px solid var(--bleu)" : "";
  });
  document.querySelectorAll("#plan-assemblee td[data-emp]").forEach(td=>{
    const c = {td, label: td.textContent.trim(), et: null};
    cases[td.dataset.emp] = c;
    td.addEventListener("click", ()=>{
      if(c.et){ c.et.classList.remove("utilisee"); c.et = null; caseSel = c; }
      else caseSel = (caseSel === c) ? null : c;
      dessiner();
    });
  });
  banque.addEventListener("click", ev=>{
    const et = ev.target.closest(".etiquette");
    if(!et || et.classList.contains("utilisee") || !caseSel) return;
    caseSel.et = et; et.classList.add("utilisee");
    caseSel = null;
    dessiner();
  });
  document.getElementById("btn-verif-plan").addEventListener("click", ()=>{
    const bons = PLAN_REPONSES[ETAT.niveau];
    const cles = Object.keys(bons);
    if(cles.some(k=>!cases[k] || !cases[k].et)) return v2Incomplet("fb-5", "Place une étiquette dans chaque case du plan avant de vérifier.");
    const justes = cles.filter(k=>cases[k].et.dataset.val === bons[k]).length;
    if(justes === cles.length) v2Reussite("fb-5", err=>validerSalle(5, err));
    else v2Echec("fb-5", justes, cles.length, "étiquettes bien placées");
  });
  const indices = cm1
    ? ["Le <b>président</b> de l'Assemblée en 1789 est <b>Bailly</b>.","À <b>gauche</b> siègent les plus radicaux, comme <b>Robespierre</b>.","La <b>date</b> de la Déclaration est le <b>26 août 1789</b>."]
    : ["<b>Mirabeau</b> est au centre, entre les factions.","<b>Danton</b> siège à la tribune du fond.","<b>Olympe de Gouges</b> défendait les droits des femmes : place-la comme secrétaire (rôle fictif)."];
  activerBoutonIndice(indices);
}

window.enigmeSalle = enigmeSalle;
window.activerEnigme = activerEnigme;
window.PLAN_REPONSES = PLAN_REPONSES;
