/* ============================================================
   ÉNIGMES — 5 énigmes interactives enrichies
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
   ÉNIGME 1 — Cahier de doléances codé
   ============================================================ */
function enigme1HTML(){
  const cm1 = ETAT.niveau==="CM1";
  const texte = cm1
    ? `<p class="texte-doc"><span class="lettre-clic cm1" data-l="L">L</span>es habitants demandent qu'on impose riches et pauvres. <span class="lettre-clic cm1" data-l="I">I</span>l faut que justice soit égale pour tous. <span class="lettre-clic cm1" data-l="B">B</span>eaucoup souffrent des taxes injustes. <span class="lettre-clic cm1" data-l="E">E</span>nfin, que règne la liberté. <span class="lettre-clic cm1" data-l="R">R</span>éunissons nos voix contre les abus. <span class="lettre-clic cm1" data-l="T">T</span>erminons les privilèges des nobles. <span class="lettre-clic cm1" data-l="É">É</span>galité pour tous les Français !</p>`
    : `<p class="texte-doc">Les habitants de la paroisse demandent que soient <span class="lettre-clic cm2" data-l="L">l</span>evées toutes les charges injustes qui pèsent sur le peuple ; qu'<span class="lettre-clic cm2" data-l="I">i</span>mposés également, riches et pauvres participent selon leurs moyens. Ils demandent que <span class="lettre-clic cm2" data-l="B">b</span>ientôt la justice ne soit plus vendue ni achetée ; qu'<span class="lettre-clic cm2" data-l="E">e</span>nfin les privilèges héréditaires soient abolis ; que la <span class="lettre-clic cm2" data-l="R">r</span>aison et la loi guident seuls le royaume ; que <span class="lettre-clic cm2" data-l="T">t</span>ous les Français soient égaux en droits, sans <span class="lettre-clic cm2" data-l="É">é</span>gard à leur naissance.</p>`;
  return `
    <h3>📖 Le cahier de doléances</h3>
    <div class="slots" id="slots-1">${Array.from({length:7}).map(()=>'<div class="slot vide"></div>').join("")}</div>
    ${texte}
    <div class="feedback" id="fb-1"></div>
    <div class="barre-outils"><button class="btn or" id="btn-indice">💡 Indice</button></div>
  `;
}
function activerEnigme1(){
  const cible = ["L","I","B","E","R","T","É"];
  let pos = 0;
  const slots = document.querySelectorAll("#slots-1 .slot");
  document.querySelectorAll(".lettre-clic").forEach(l=>{
    l.addEventListener("click", ()=>{
      if(l.classList.contains("utilisee")) return;
      const lettre = l.dataset.l;
      if(lettre === cible[pos]){
        l.classList.add("utilisee");
        const s = slots[pos];
        s.classList.remove("vide"); s.classList.add("ok"); s.textContent = lettre;
        pos++;
        if(pos === cible.length){
          document.getElementById("fb-1").className = "feedback succes show";
          document.getElementById("fb-1").innerHTML = "✨ Le mot mystère est : <b>LIBERTÉ</b> !";
          setTimeout(()=>validerSalle(1), 900);
        }
      }else{
        l.classList.add("mal"); setTimeout(()=>l.classList.remove("mal"),400);
        const fb = document.getElementById("fb-1");
        fb.className="feedback erreur show";
        fb.textContent = "Pas dans le bon ordre. Cherche la première lettre non encore trouvée.";
        setTimeout(()=>fb.classList.remove("show"),2000);
      }
    });
  });
  const indices = ETAT.niveau==="CM1"
    ? ["La première lettre à cliquer est un <b>L</b> majuscule, en rouge.", "Ensuite cherche un <b>I</b> majuscule rouge.", "Le mot veut dire « ne pas être prisonnier »."]
    : ["Les lettres à trouver sont en début de mots-clés du texte.", "Le mot cherché commence par <b>L</b> et finit par <b>É</b>.", "C'est l'un des trois mots de la devise de la France."];
  activerBoutonIndice(indices);
}

/* ============================================================
   ÉNIGME 2 — La Marseillaise mystérieuse
   ============================================================ */
function enigme2HTML(){
  const cm1 = ETAT.niveau==="CM1";
  if(cm1){
    return `<h3>🎵 La Marseillaise mystérieuse</h3>
      <p style="text-align:center;opacity:.7;font-style:italic">Clique sur un extrait à gauche, puis sur l'image correspondante à droite.</p>
      <div class="rang-match">
        <div class="colonne-match" id="col-extraits">
          <div class="carte-match" data-id="e1" data-bon="i1">« Aux armes, citoyens ! »</div>
          <div class="carte-match" data-id="e2" data-bon="i2">« Allons enfants de la Patrie »</div>
          <div class="carte-match" data-id="e3" data-bon="i3">« Le jour de gloire est arrivé »</div>
        </div>
        <div class="colonne-match" id="col-images">
          <div class="carte-match" data-id="i1"><span class="emoji">🏰</span>Prise de la Bastille</div>
          <div class="carte-match" data-id="i2"><span class="emoji">🚶</span>Volontaires en marche</div>
          <div class="carte-match" data-id="i3"><span class="emoji">🚩</span>Drapeau tricolore hissé</div>
        </div>
      </div>
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
  const cm1 = ETAT.niveau==="CM1";
  if(cm1){
    let selG = null;
    document.querySelectorAll("#col-extraits .carte-match").forEach(c=>{
      c.addEventListener("click", ()=>{
        document.querySelectorAll("#col-extraits .carte-match").forEach(x=>x.classList.remove("select"));
        c.classList.add("select"); selG = c;
      });
    });
    document.querySelectorAll("#col-images .carte-match").forEach(img=>{
      img.addEventListener("click", ()=>{
        if(!selG) return;
        if(selG.dataset.bon === img.dataset.id){
          selG.classList.add("bien"); selG.classList.remove("select");
          img.classList.add("bien"); selG = null;
          if(document.querySelectorAll("#col-extraits .carte-match:not(.bien)").length===0){
            document.getElementById("fb-2").className="feedback succes show";
            document.getElementById("fb-2").innerHTML="✨ Toutes les associations sont correctes !";
            setTimeout(()=>validerSalle(2), 900);
          }
        }else{
          img.classList.add("mal"); setTimeout(()=>img.classList.remove("mal"),400);
          const fb=document.getElementById("fb-2");
          fb.className="feedback erreur show"; fb.textContent="Mauvaise association. Réessaie !";
          setTimeout(()=>fb.classList.remove("show"),1800);
        }
      });
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
      const ordre = [...document.querySelectorAll("#liste-ordre .item-ordre")].map(it=>it.dataset.rang).join("");
      if(ordre === "12345"){
        document.querySelectorAll("#liste-ordre .item-ordre").forEach(it=>it.style.borderColor="var(--vert)");
        document.getElementById("fb-2").className="feedback succes show";
        document.getElementById("fb-2").innerHTML="✨ Ordre chronologique parfait !";
        setTimeout(()=>validerSalle(2), 900);
      }else{
        document.getElementById("fb-2").className="feedback erreur show";
        document.getElementById("fb-2").textContent="L'ordre n'est pas correct. Lequel vient en premier : les États généraux ou la Bastille ?";
        setTimeout(()=>document.getElementById("fb-2").classList.remove("show"),2500);
      }
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
  const reponse = ["LIBRES","ÉGAUX","DROITS"];
  document.querySelectorAll(".choix-rebus").forEach(sel=>{
    sel.addEventListener("change", ()=>{
      const i = +sel.dataset.i;
      const trou = document.querySelector(`.trou[data-i="${i}"]`);
      trou.textContent = sel.value || "…";
      trou.classList.remove("ok");
    });
  });
  document.getElementById("btn-verif-rebus").addEventListener("click", ()=>{
    const choix = [...document.querySelectorAll(".choix-rebus")].map(s=>s.value);
    if(choix.every((v,i)=>v===reponse[i])){
      document.querySelectorAll(".trou").forEach(t=>t.classList.add("ok"));
      document.getElementById("fb-3").className="feedback succes show";
      document.getElementById("fb-3").innerHTML="✨ « Les hommes naissent <b>libres</b> et <b>égaux</b> en <b>droits</b>. » Article 1 retrouvé !";
      setTimeout(()=>validerSalle(3), 1000);
    }else{
      document.querySelectorAll(".trou").forEach((t,i)=>{ if(choix[i]===reponse[i]) t.classList.add("ok"); });
      document.getElementById("fb-3").className="feedback erreur show";
      document.getElementById("fb-3").textContent="Certaines réponses sont erronées. Réfléchis bien au symbole de chaque rébus.";
      setTimeout(()=>document.getElementById("fb-3").classList.remove("show"),2500);
    }
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
    <div class="rang-match">
      <div class="colonne-match" id="col-persos">
        ${persos.map(p=>`<div class="carte-match" data-id="${p.id}" data-bon="${p.bon}"><span class="emoji">${p.emoji}</span><b>${p.nom}</b><br><span style="font-size:.75rem;opacity:.7">${p.ev}</span></div>`).join("")}
      </div>
      <div class="colonne-match" id="col-citations">
        ${citations.map(c=>`<div class="carte-match" data-id="${c.id}">${c.txt}</div>`).join("")}
      </div>
    </div>
    <div class="feedback" id="fb-4"></div>
    <div class="barre-outils"><button class="btn or" id="btn-indice">💡 Indice</button></div>`;
}
function activerEnigme4(){
  let selP = null;
  document.querySelectorAll("#col-persos .carte-match").forEach(c=>{
    c.addEventListener("click", ()=>{
      document.querySelectorAll("#col-persos .carte-match").forEach(x=>x.classList.remove("select"));
      c.classList.add("select"); selP = c;
    });
  });
  document.querySelectorAll("#col-citations .carte-match").forEach(ci=>{
    ci.addEventListener("click", ()=>{
      if(!selP) return;
      if(selP.dataset.bon === ci.dataset.id){
        selP.classList.add("bien"); selP.classList.remove("select");
        ci.classList.add("bien"); selP = null;
        if(document.querySelectorAll("#col-persos .carte-match:not(.bien)").length===0){
          document.getElementById("fb-4").className="feedback succes show";
          document.getElementById("fb-4").innerHTML="✨ Toutes les associations sont correctes !";
          setTimeout(()=>validerSalle(4), 900);
        }
      }else{
        ci.classList.add("mal"); setTimeout(()=>ci.classList.remove("mal"),400);
        const fb=document.getElementById("fb-4");
        fb.className="feedback erreur show"; fb.textContent="Ce personnage n'a pas dit cela. Réessaie !";
        setTimeout(()=>fb.classList.remove("show"),1800);
      }
    });
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
    ${planHTML}
    <p style="text-align:center;font-size:.85rem;opacity:.7;margin-top:8px">Clique sur une case, puis choisis une étiquette ci-dessous.</p>
    <div class="banque" id="banque-etiquettes">
      ${etiquettes.map(e=>`<div class="etiquette" data-val="${e}">${e}</div>`).join("")}
    </div>
    <div class="center" style="margin-top:14px"><button class="btn vert" id="btn-verif-plan">✅ Vérifier le plan</button></div>
    <div class="feedback" id="fb-5"></div>
    <div class="barre-outils"><button class="btn or" id="btn-indice">💡 Indice</button></div>`;
}
function activerEnigme5(){
  const cm1 = ETAT.niveau==="CM1";
  const corrections = {};
  document.querySelectorAll("#plan-assemblee td[data-emp]").forEach(td=>{
    const empId = td.dataset.emp;
    const label = td.textContent.trim();
    corrections[empId] = {td, label, val:null};
    td.addEventListener("click", ()=>{
      document.querySelectorAll("#plan-assemblee td").forEach(x=>x.style.outline="");
      td.style.outline = "3px solid var(--bleu)";
      const handler = (ev)=>{
        const et = ev.target.closest(".etiquette");
        if(!et || et.classList.contains("utilisee")) return;
        td.innerHTML = `<b>${et.dataset.val}</b><br><span style="font-size:.7rem;opacity:.7">${label}</span>`;
        td.classList.add("etiquette-placee"); td.style.outline="";
        corrections[empId].val = et.dataset.val;
        et.classList.add("utilisee");
        document.getElementById("banque-etiquettes").removeEventListener("click", handler);
      };
      document.getElementById("banque-etiquettes").addEventListener("click", handler);
    });
  });
  document.getElementById("btn-verif-plan").addEventListener("click", ()=>{
    const bons = PLAN_REPONSES[ETAT.niveau];
    let nbErr = 0;
    Object.keys(bons).forEach(empId=>{
      const c = corrections[empId];
      if(c && c.val === bons[empId]) c.td.classList.add("bien");
      else if(c && c.val){ c.td.classList.add("mal"); nbErr++; setTimeout(()=>c.td.classList.remove("mal"),1500); }
      else nbErr++;
    });
    if(nbErr===0){
      document.getElementById("fb-5").className="feedback succes show";
      document.getElementById("fb-5").innerHTML="✨ Le plan est parfait ! Le mécanisme s'ouvre…";
      setTimeout(()=>validerSalle(5), 1100);
    }else{
      document.getElementById("fb-5").className="feedback erreur show";
      document.getElementById("fb-5").textContent = nbErr+" étiquette(s) mal placée(s) ou manquante(s). Réessaie !";
      setTimeout(()=>document.getElementById("fb-5").classList.remove("show"),2500);
    }
  });
  const indices = cm1
    ? ["Le <b>président</b> de l'Assemblée en 1789 est <b>Bailly</b>.","À <b>gauche</b> siègent les plus radicaux, comme <b>Robespierre</b>.","La <b>date</b> de la Déclaration est le <b>26 août 1789</b>."]
    : ["<b>Mirabeau</b> est au centre, entre les factions.","<b>Danton</b> siège à la tribune du fond.","<b>Olympe de Gouges</b> défendait les droits des femmes : place-la comme secrétaire (rôle fictif)."];
  activerBoutonIndice(indices);
}

window.enigmeSalle = enigmeSalle;
window.activerEnigme = activerEnigme;
window.PLAN_REPONSES = PLAN_REPONSES;
