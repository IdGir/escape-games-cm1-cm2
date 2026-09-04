/* ============================================================
   ÉNIGMES — 5 énigmes de géographie, différenciées CM1 / CM2
   ------------------------------------------------------------
   Programme travaillé (cycle 3) :
     1. Le planisphère : continents et océans
     2. Se déplacer dans le monde : itinéraire, mers, canaux
     3. Climats et paysages du monde
     4. Transports, distances et échelle d'une carte
     5. Méridiens, parallèles et fuseaux horaires

   Contrat : enigmeSalle(n) rend le HTML, activerEnigme(n)
   attache les interactions, validerSalle(n) clôt l'étape.
   ============================================================ */

function enigmeSalle(n){
  return ({1:enigme1HTML,2:enigme2HTML,3:enigme3HTML,4:enigme4HTML,5:enigme5HTML}[n]||(()=>""))();
}
function activerEnigme(n){
  ({1:activerEnigme1,2:activerEnigme2,3:activerEnigme3,4:activerEnigme4,5:activerEnigme5}[n]||(()=>{}))();
}

/* Petit utilitaire : afficher un retour à l'élève */
function retour(id, type, html, duree){
  const fb = document.getElementById(id);
  if(!fb) return;
  fb.className = "feedback "+type+" show";
  fb.innerHTML = html;
  if(duree) setTimeout(()=>fb.classList.remove("show"), duree);
}
function melanger(tab){ return tab.slice().sort(()=>Math.random()-0.5); }

/* ============================================================
   ÉNIGME 1 — LE GRAND PLANISPHÈRE
   Placer les continents et les océans sur la carte du monde.
   ============================================================ */

/* Tracés schématiques du planisphère (viewBox 800 × 400) */
const FORMES_CARTE = {
  "amerique-n":  "M70,70 L180,58 L212,96 L188,132 L150,142 L140,182 L118,180 L122,132 L86,110 Z",
  "amerique-s":  "M150,202 L198,192 L216,224 L204,270 L182,320 L160,300 L152,250 Z",
  "amerique":    "M70,70 L180,58 L212,96 L188,132 L154,142 L216,224 L204,270 L182,320 L160,300 L150,238 L128,180 L122,132 L86,110 Z",
  "europe":      "M348,68 L420,62 L432,92 L404,118 L370,114 L350,94 Z",
  "afrique":     "M356,142 L448,134 L464,180 L436,238 L410,284 L386,258 L372,206 Z",
  "asie":        "M436,54 L678,50 L702,96 L650,142 L560,170 L494,152 L448,118 L432,84 Z",
  "oceanie":     "M636,238 L718,230 L732,268 L688,294 L648,280 Z",
  "antarctique": "M40,362 L762,358 L766,396 L36,398 Z",
};
/* Océans : zones cliquables en pleine eau */
const OCEANS_CARTE = {
  "pacifique": {cx:66,  cy:236, rx:50, ry:36},
  "atlantique":{cx:282, cy:232, rx:44, ry:42},
  "indien":    {cx:552, cy:262, rx:50, ry:36},
  "arctique":  {cx:400, cy:26,  rx:96, ry:20},
  "austral":   {cx:400, cy:334, rx:126,ry:18},
};

/* Ce qu'il faut placer, selon le niveau */
const CARTE_NIVEAUX = {
  CM1: {
    terres: [
      {id:"amerique", nom:"Amérique"},
      {id:"europe",   nom:"Europe"},
      {id:"afrique",  nom:"Afrique"},
      {id:"asie",     nom:"Asie"},
      {id:"oceanie",  nom:"Océanie"},
    ],
    eaux: [
      {id:"pacifique", nom:"Océan Pacifique"},
      {id:"atlantique",nom:"Océan Atlantique"},
      {id:"indien",    nom:"Océan Indien"},
    ]
  },
  CM2: {
    terres: [
      {id:"amerique-n", nom:"Amérique du Nord"},
      {id:"amerique-s", nom:"Amérique du Sud"},
      {id:"europe",     nom:"Europe"},
      {id:"afrique",    nom:"Afrique"},
      {id:"asie",       nom:"Asie"},
      {id:"oceanie",    nom:"Océanie"},
      {id:"antarctique",nom:"Antarctique"},
    ],
    eaux: [
      {id:"pacifique", nom:"Océan Pacifique"},
      {id:"atlantique",nom:"Océan Atlantique"},
      {id:"indien",    nom:"Océan Indien"},
      {id:"arctique",  nom:"Océan Arctique"},
      {id:"austral",   nom:"Océan Austral"},
    ]
  }
};

function enigme1HTML(){
  const cfg = CARTE_NIVEAUX[ETAT.niveau] || CARTE_NIVEAUX.CM2;
  const aPlacer = [...cfg.terres, ...cfg.eaux];

  // Tracé des continents demandés
  const terres = cfg.terres.map(t=>
    `<path class="zone-carte" data-zone="${t.id}" d="${FORMES_CARTE[t.id]}"></path>
     <text class="etiq-carte" id="txt-${t.id}" x="${centreForme(t.id).x}" y="${centreForme(t.id).y}"></text>`
  ).join("");

  // Zones océaniques demandées
  const eaux = cfg.eaux.map(o=>{
    const g = OCEANS_CARTE[o.id];
    return `<ellipse class="zone-carte" data-zone="${o.id}" cx="${g.cx}" cy="${g.cy}" rx="${g.rx}" ry="${g.ry}"></ellipse>
            <text class="etiq-carte etiq-ocean" id="txt-${o.id}" x="${g.cx}" y="${g.cy+4}"></text>`;
  }).join("");

  return `
    <h3>🗺️ Le grand planisphère du Reform Club</h3>
    <p class="center" style="opacity:.75;font-style:italic">
      Clique sur une <b>zone de la carte</b>, puis sur son <b>nom</b> dans la liste du bas.
    </p>
    <div class="planisphere">
      <svg viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg" role="img"
           aria-label="Planisphère à compléter">
        <!-- Grille : parallèles et méridiens -->
        <g stroke="#9dc4dc" stroke-width="1" opacity=".55">
          <line x1="0" y1="100" x2="800" y2="100"/>
          <line x1="0" y1="200" x2="800" y2="200"/>
          <line x1="0" y1="300" x2="800" y2="300"/>
          <line x1="200" y1="0" x2="200" y2="400"/>
          <line x1="400" y1="0" x2="400" y2="400"/>
          <line x1="600" y1="0" x2="600" y2="400"/>
        </g>
        <!-- L'équateur, en évidence -->
        <line x1="0" y1="200" x2="800" y2="200" stroke="#a33327" stroke-width="2" stroke-dasharray="9 6"/>
        <text x="12" y="194" font-size="12" fill="#a33327" font-family="Georgia" font-style="italic">Équateur</text>
        <!-- Le méridien de Greenwich -->
        <line x1="400" y1="0" x2="400" y2="400" stroke="#2f7d6b" stroke-width="2" stroke-dasharray="9 6"/>
        <text x="406" y="392" font-size="12" fill="#2f7d6b" font-family="Georgia" font-style="italic">Méridien 0°</text>
        ${eaux}
        ${terres}
      </svg>
    </div>
    <div class="legende-carte">
      <span><i style="background:rgba(47,125,107,.55);border:1px solid #2f7d6b"></i>bien placé</span>
      <span><i style="background:rgba(255,255,255,.4);border:1px dashed #102a41"></i>à compléter</span>
      <span>🔴 équateur &nbsp;·&nbsp; 🟢 méridien de Greenwich</span>
    </div>
    <div class="banque" id="banque-1">
      ${melanger(aPlacer).map(e=>
        `<div class="etiquette ${e.id.startsWith("oc")||OCEANS_CARTE[e.id]?"ocean":""}" data-val="${e.id}">${e.nom}</div>`
      ).join("")}
    </div>
    <div class="feedback" id="fb-1"></div>
    <div class="barre-outils"><button class="btn laiton" id="btn-indice">💡 Indice</button></div>
  `;
}

/* Centre approximatif d'un tracé, pour y poser l'étiquette */
function centreForme(id){
  const centres = {
    "amerique-n":{x:140,y:105},"amerique-s":{x:182,y:252},"amerique":{x:150,y:180},
    "europe":{x:390,y:94},"afrique":{x:412,y:206},"asie":{x:566,y:104},
    "oceanie":{x:684,y:264},"antarctique":{x:400,y:382},
  };
  return centres[id] || {x:400,y:200};
}

function activerEnigme1(){
  const cfg = CARTE_NIVEAUX[ETAT.niveau] || CARTE_NIVEAUX.CM2;
  const noms = {};
  [...cfg.terres, ...cfg.eaux].forEach(e=>noms[e.id] = e.nom);
  const total = Object.keys(noms).length;

  let zoneVisee = null;
  let placees = 0;

  const planisphere = document.querySelector(".planisphere");
  const svg = planisphere.querySelector("svg");
  const banque = document.getElementById("banque-1");

  /* Fond de carte facultatif : si l'enseignant a déposé
     assets/images/cartes/planisphere.jpg, il se glisse SOUS les zones
     cliquables, qui restent parfaitement utilisables. Sans fichier,
     le tracé schématique dessiné suffit. */
  if(typeof poserFondCarte === "function"){
    poserFondCarte(planisphere, "planisphere", "fond-planisphere");
  }

  // 1. Sélection d'une zone de la carte
  svg.querySelectorAll(".zone-carte").forEach(z=>{
    z.addEventListener("click", ()=>{
      if(z.classList.contains("bien")) return;
      svg.querySelectorAll(".zone-carte").forEach(x=>x.classList.remove("visee"));
      z.classList.add("visee");
      zoneVisee = z;
      if(typeof son === "function") son("clic");
    });
  });

  // 2. Choix du nom dans la banque
  banque.addEventListener("click", e=>{
    const et = e.target.closest(".etiquette");
    if(!et || et.classList.contains("utilisee")) return;

    if(!zoneVisee){
      retour("fb-1","indice","👉 Choisis d'abord une <b>zone sur la carte</b>, puis son nom.",2200);
      return;
    }
    const attendu = zoneVisee.dataset.zone;
    if(et.dataset.val === attendu){
      zoneVisee.classList.remove("visee");
      zoneVisee.classList.add("bien");
      const txt = document.getElementById("txt-"+attendu);
      if(txt) txt.textContent = noms[attendu];
      et.classList.add("utilisee");
      placees++;
      if(typeof son === "function") son("succes");
      zoneVisee = null;
      if(placees === total){
        retour("fb-1","succes","✨ Le planisphère est complet ! Phileas Fogg peut tracer sa route.");
        setTimeout(()=>validerSalle(1), 1000);
      }
    }else{
      const rate = zoneVisee;
      rate.classList.add("mal");
      setTimeout(()=>rate.classList.remove("mal"), 500);
      if(typeof son === "function") son("erreur");
      retour("fb-1","erreur","Ce n'est pas le bon nom pour cette zone. Regarde bien sa position par rapport à l'<b>équateur</b> et au <b>méridien</b>.",2600);
    }
  });

  const indices = ETAT.niveau==="CM1"
    ? ["L'<b>Europe</b> est le plus petit des continents de la carte : elle est en haut, juste au-dessus de l'Afrique.",
       "L'<b>Afrique</b> est traversée en son milieu par l'<b>équateur</b> (le trait rouge).",
       "L'<b>océan Pacifique</b> est le plus grand : il se trouve à gauche de la carte, entre l'Amérique et l'Asie."]
    : ["L'<b>Antarctique</b> est le continent tout en bas : il est couvert de glace.",
       "L'<b>océan Arctique</b> est tout en haut, autour du pôle Nord ; l'<b>océan Austral</b> entoure l'Antarctique.",
       "L'<b>Amérique du Sud</b> est traversée par l'équateur ; l'<b>Amérique du Nord</b> est entièrement au-dessus."];
  activerBoutonIndice(indices);
}

/* ============================================================
   ÉNIGME 2 — L'ITINÉRAIRE DU « MONGOLIA »
   Remettre les escales dans l'ordre + comprendre le canal de Suez.
   ============================================================ */
const ITINERAIRES = {
  CM1: [
    {id:"a", txt:"Londres",  detail:"Angleterre · le départ",             rang:1},
    {id:"b", txt:"Suez",     detail:"Égypte · l'entrée du canal",         rang:2},
    {id:"c", txt:"Bombay",   detail:"Inde · côte de l'océan Indien",      rang:3},
    {id:"d", txt:"Calcutta", detail:"Inde · au bord du golfe du Bengale", rang:4},
  ],
  CM2: [
    {id:"a", txt:"Londres",  detail:"Angleterre · Europe",                       rang:1},
    {id:"b", txt:"Paris",    detail:"France · Europe",                           rang:2},
    {id:"c", txt:"Brindisi", detail:"Italie · port sur la mer Méditerranée",     rang:3},
    {id:"d", txt:"Suez",     detail:"Égypte · Afrique · sortie du canal",        rang:4},
    {id:"e", txt:"Aden",     detail:"Yémen · Asie · entrée de la mer Rouge",     rang:5},
    {id:"f", txt:"Bombay",   detail:"Inde · Asie · océan Indien",                rang:6},
    {id:"g", txt:"Calcutta", detail:"Inde · Asie · golfe du Bengale",            rang:7},
  ]
};

function enigme2HTML(){
  const etapes = melanger(ITINERAIRES[ETAT.niveau] || ITINERAIRES.CM2);
  const questionCanal = ETAT.niveau==="CM1"
    ? {q:"À quoi sert le canal de Suez ?",
       options:[{t:"À relier deux mers pour raccourcir le voyage",ok:true},
                {t:"À arroser le désert",ok:false},
                {t:"À produire de l'électricité",ok:false}]}
    : {q:"Le canal de Suez, ouvert en 1869, relie :",
       options:[{t:"la mer Méditerranée et la mer Rouge",ok:true},
                {t:"l'océan Atlantique et l'océan Pacifique",ok:false},
                {t:"la mer Noire et la mer Baltique",ok:false}]};
  const optionsCanal = melanger(questionCanal.options);

  return `
    <h3>🚢 Le carnet de route du « Mongolia »</h3>
    <p class="center" style="opacity:.75;font-style:italic">
      Les pages du carnet se sont mélangées. Remets les escales dans l'<b>ordre du voyage</b> avec les flèches ▲▼.
    </p>
    <div class="carnet-route" id="carnet-route">
      ${etapes.map(e=>`
        <div class="item-ordre" data-id="${e.id}" data-rang="${e.rang}">
          <span class="rang">?</span>
          <div class="contenu"><b>${e.txt}</b><br><span style="font-size:.8rem;opacity:.7">${e.detail}</span></div>
          <div class="controles-ordre">
            <button class="btn-monter" aria-label="Monter cette escale">▲</button>
            <button class="btn-descendre" aria-label="Descendre cette escale">▼</button>
          </div>
        </div>`).join("")}
    </div>

    <div class="qcm-question" id="q-canal" data-bonne="${optionsCanal.findIndex(o=>o.ok)}">
      <div class="q">🧭 ${questionCanal.q}</div>
      ${optionsCanal.map((o,j)=>`<label class="qcm-option" data-j="${j}">${o.t}</label>`).join("")}
    </div>

    <div class="center"><button class="btn jade" id="btn-verif-2">✅ Vérifier le carnet</button></div>
    <div class="feedback" id="fb-2"></div>
    <div class="barre-outils"><button class="btn laiton" id="btn-indice">💡 Indice</button></div>
  `;
}

function activerEnigme2(){
  const liste = document.getElementById("carnet-route");
  const bonneCanal = +document.getElementById("q-canal").dataset.bonne;
  let choixCanal = null;

  function rafraichirRangs(){
    liste.querySelectorAll(".item-ordre").forEach((it,i)=>it.querySelector(".rang").textContent = i+1);
  }
  liste.addEventListener("click", e=>{
    const item = e.target.closest(".item-ordre");
    if(!item) return;
    if(e.target.classList.contains("btn-monter")){
      const prev = item.previousElementSibling;
      if(prev) liste.insertBefore(item, prev);
    }else if(e.target.classList.contains("btn-descendre")){
      const next = item.nextElementSibling;
      if(next) liste.insertBefore(next, item);
    }else return;
    rafraichirRangs();
    if(typeof son === "function") son("clic");
  });
  rafraichirRangs();

  // QCM sur le canal
  const bloc = document.getElementById("q-canal");
  bloc.querySelectorAll(".qcm-option").forEach(opt=>{
    opt.addEventListener("click", ()=>{
      bloc.querySelectorAll(".qcm-option").forEach(x=>x.classList.remove("select"));
      opt.classList.add("select");
      choixCanal = +opt.dataset.j;
    });
  });

  document.getElementById("btn-verif-2").addEventListener("click", ()=>{
    const items = [...liste.querySelectorAll(".item-ordre")];
    const ordreOk = items.every((it,i)=> +it.dataset.rang === i+1);
    const canalOk = choixCanal === bonneCanal;

    items.forEach((it,i)=>{
      it.style.borderColor = (+it.dataset.rang === i+1) ? "var(--jade)" : "var(--sceau)";
    });

    if(ordreOk && canalOk){
      retour("fb-2","succes","✨ L'itinéraire est reconstitué ! Le canal de Suez fait gagner des semaines : sans lui, il faudrait contourner toute l'Afrique.");
      if(typeof son === "function") son("succes");
      setTimeout(()=>validerSalle(2), 1200);
    }else if(!ordreOk){
      retour("fb-2","erreur","L'ordre du voyage n'est pas encore le bon. Souviens-toi : Fogg part vers l'<b>est</b>, de l'Europe vers l'Asie.",3200);
      if(typeof son === "function") son("erreur");
    }else{
      retour("fb-2","erreur","L'itinéraire est bon ! Mais la réponse sur le <b>canal de Suez</b> est incorrecte.",3200);
      if(typeof son === "function") son("erreur");
    }
  });

  const indices = ETAT.niveau==="CM1"
    ? ["Le voyage <b>commence</b> à Londres : c'est la ville de Phileas Fogg.",
       "Après l'Europe, le navire passe par l'Égypte, en <b>Afrique</b> : c'est Suez.",
       "Bombay est sur la côte <b>ouest</b> de l'Inde, Calcutta sur la côte <b>est</b> : on traverse donc l'Inde de Bombay vers Calcutta."]
    : ["De Londres, Fogg gagne d'abord <b>Paris</b>, puis descend l'Italie jusqu'au port de <b>Brindisi</b>.",
       "Le canal de Suez fait passer de la <b>Méditerranée</b> à la <b>mer Rouge</b>. Aden en garde la sortie.",
       "Ensuite seulement vient l'<b>océan Indien</b> : Bombay puis, en traversant l'Inde en train, Calcutta."];
  activerBoutonIndice(indices);
}

/* ============================================================
   ÉNIGME 3 — LE CARNET DES CLIMATS
   Associer un paysage à son climat (et sa zone, en CM2).
   ============================================================ */
const CLIMATS = {
  CM1: [
    {id:"p1", emoji:"🏜️", nom:"Le désert du Sahara", image:"paysage-desert",     bon:"c1", climat:"Chaud et très sec"},
    {id:"p2", emoji:"🌴", nom:"La jungle de l'Inde", image:"paysage-jungle",      bon:"c2", climat:"Chaud et très humide"},
    {id:"p3", emoji:"🏔️", nom:"Les sommets de l'Himalaya", image:"paysage-montagne",bon:"c3", climat:"Froid en altitude"},
    {id:"p4", emoji:"🌳", nom:"La campagne anglaise", image:"paysage-campagne",     bon:"c4", climat:"Doux et pluvieux"},
  ],
  CM2: [
    {id:"p1", emoji:"🏜️", nom:"Le désert du Sahara", image:"paysage-desert",       bon:"c1", climat:"Aride : chaud, presque sans pluie · zone chaude"},
    {id:"p2", emoji:"🌴", nom:"La forêt de l'Inde", image:"paysage-jungle",         bon:"c2", climat:"Équatorial : chaud et humide toute l'année · zone chaude"},
    {id:"p3", emoji:"🏔️", nom:"Les sommets de l'Himalaya", image:"paysage-montagne",  bon:"c3", climat:"Montagnard : froid dû à l'altitude"},
    {id:"p4", emoji:"🌳", nom:"La campagne anglaise", image:"paysage-campagne",       bon:"c4", climat:"Océanique : doux et pluvieux · zone tempérée"},
    {id:"p5", emoji:"🧊", nom:"La banquise du pôle", image:"paysage-banquise",        bon:"c5", climat:"Polaire : glacé toute l'année · zone froide"},
    {id:"p6", emoji:"🦁", nom:"La savane africaine", image:"paysage-savane",        bon:"c6", climat:"Tropical : une saison sèche, une saison des pluies"},
  ]
};

function enigme3HTML(){
  const jeu = CLIMATS[ETAT.niveau] || CLIMATS.CM2;
  const cartes = jeu.map((p,i)=>({id:"c"+(i+1), txt:p.climat}));
  return `
    <h3>🌡️ Le carnet des climats de Mrs Aouda</h3>
    <p class="center" style="opacity:.75;font-style:italic">
      Clique sur un <b>paysage</b>, puis sur le <b>climat</b> qui lui correspond.
    </p>
    <div class="grille-paysages" id="grille-paysages">
      ${jeu.map(p=>`
        <div class="paysage" data-id="${p.id}" data-bon="${p.bon}" data-image="${p.image}">
          <div class="vignette">${p.emoji}</div>
          <div class="nom">${p.nom}</div>
        </div>`).join("")}
    </div>
    <div class="colonne-match" id="col-climats" style="max-width:560px;margin:0 auto">
      <div class="titre-colonne">Les climats</div>
      ${melanger(cartes).map(c=>`<div class="carte-match" data-id="${c.id}">${c.txt}</div>`).join("")}
    </div>
    <div class="feedback" id="fb-3"></div>
    <div class="barre-outils"><button class="btn laiton" id="btn-indice">💡 Indice</button></div>
  `;
}

function activerEnigme3(){
  let selection = null;
  const paysages = document.querySelectorAll("#grille-paysages .paysage");

  /* Photos de paysage facultatives : assets/images/cartes/paysage-desert.jpg,
     paysage-jungle.jpg… Sans fichier, le pictogramme reste affiché. */
  if(typeof illustrerVignette === "function"){
    paysages.forEach(p=>illustrerVignette(p.querySelector(".vignette"), p.dataset.image));
  }

  paysages.forEach(p=>{
    p.addEventListener("click", ()=>{
      if(p.classList.contains("bien")) return;
      paysages.forEach(x=>x.classList.remove("select"));
      p.classList.add("select");
      selection = p;
      if(typeof son === "function") son("clic");
    });
  });

  document.querySelectorAll("#col-climats .carte-match").forEach(c=>{
    c.addEventListener("click", ()=>{
      if(!selection){
        retour("fb-3","indice","👉 Choisis d'abord un <b>paysage</b> en haut.",2000);
        return;
      }
      if(selection.dataset.bon === c.dataset.id){
        selection.classList.remove("select");
        selection.classList.add("bien");
        c.classList.add("bien");
        selection = null;
        if(typeof son === "function") son("succes");
        if(document.querySelectorAll("#grille-paysages .paysage:not(.bien)").length === 0){
          retour("fb-3","succes","✨ Tous les climats sont identifiés ! Plus on s'éloigne de l'équateur, plus il fait froid.");
          setTimeout(()=>validerSalle(3), 1100);
        }
      }else{
        c.classList.add("mal");
        setTimeout(()=>c.classList.remove("mal"), 500);
        if(typeof son === "function") son("erreur");
        retour("fb-3","erreur","Ce climat ne correspond pas à ce paysage. Pense à la <b>chaleur</b> et à la <b>pluie</b>.",2400);
      }
    });
  });

  const indices = ETAT.niveau==="CM1"
    ? ["Dans un <b>désert</b>, il ne pleut presque jamais.",
       "Une <b>jungle</b> a besoin de beaucoup de pluie et de chaleur pour pousser.",
       "En <b>montagne</b>, plus on monte, plus il fait froid : c'est pour cela qu'il y a de la neige au sommet."]
    : ["Le climat <b>équatorial</b> est chaud et humide toute l'année ; le climat <b>tropical</b> alterne saison sèche et saison des pluies.",
       "Le climat <b>océanique</b> de l'Angleterre est adouci par la mer : hivers doux, pluie fréquente.",
       "Les <b>zones froides</b> se trouvent près des pôles ; les <b>zones chaudes</b> de part et d'autre de l'équateur."];
  activerBoutonIndice(indices);
}

/* ============================================================
   ÉNIGME 4 — LE CALCUL DU TIMONIER
   Moyens de transport + lecture de l'échelle d'une carte.
   ============================================================ */
const TRAJETS = {
  CM1: [
    {de:"Londres → Paris",        bon:"train",    cm:2, km:400},
    {de:"Suez → Bombay",          bon:"paquebot", cm:9, km:1800},
    {de:"Kholby → Allahabad",     bon:"elephant", cm:1, km:200},
  ],
  CM2: [
    {de:"Londres → Paris",             bon:"train",    cm:2,  km:400},
    {de:"Brindisi → Suez",             bon:"paquebot", cm:7,  km:1400},
    {de:"Kholby → Allahabad (jungle)", bon:"elephant", cm:1,  km:200},
    {de:"Hong Kong → Yokohama",        bon:"paquebot", cm:12, km:2400},
    {de:"San Francisco → New York",    bon:"train",    cm:22, km:4400},
  ]
};
const TRANSPORTS = [
  {id:"train",    nom:"🚂 Train à vapeur"},
  {id:"paquebot", nom:"🚢 Paquebot à vapeur"},
  {id:"elephant", nom:"🐘 Éléphant"},
  {id:"traineau", nom:"🛷 Traîneau à voile"},
];

function enigme4HTML(){
  const trajets = TRAJETS[ETAT.niveau] || TRAJETS.CM2;
  return `
    <h3>🧮 Le calcul du timonier</h3>
    <p class="center" style="opacity:.75;font-style:italic">
      Pour chaque étape : choisis le <b>bon moyen de transport</b>, puis calcule la <b>distance réelle</b> grâce à l'échelle.
    </p>
    <div class="echelle">
      <span><b>Échelle de la carte :</b></span>
      <span class="barre" aria-hidden="true"></span>
      <span>1 cm sur la carte = <b>200 km</b> en vrai</span>
    </div>
    <table class="table-bord">
      <thead>
        <tr><th>Étape</th><th>Transport</th><th>Sur la carte</th><th>Distance réelle</th></tr>
      </thead>
      <tbody>
        ${trajets.map((t,i)=>`
          <tr data-i="${i}" data-bon="${t.bon}" data-km="${t.km}">
            <td>${t.de}</td>
            <td>
              <select class="sel-transport" data-i="${i}" aria-label="Transport pour ${t.de}">
                <option value="">— choisir —</option>
                ${TRANSPORTS.map(tr=>`<option value="${tr.id}">${tr.nom}</option>`).join("")}
              </select>
            </td>
            <td><b>${t.cm} cm</b></td>
            <td><input type="number" class="inp-km" data-i="${i}" min="0" step="100" placeholder="? km" aria-label="Distance réelle pour ${t.de}"> km</td>
          </tr>`).join("")}
      </tbody>
    </table>
    <div class="center"><button class="btn jade" id="btn-verif-4">✅ Vérifier le journal de bord</button></div>
    <div class="feedback" id="fb-4"></div>
    <div class="barre-outils"><button class="btn laiton" id="btn-indice">💡 Indice</button></div>
  `;
}

function activerEnigme4(){
  document.getElementById("btn-verif-4").addEventListener("click", ()=>{
    const lignes = [...document.querySelectorAll(".table-bord tbody tr")];
    let erreurs = 0, vides = 0;

    lignes.forEach(tr=>{
      const i    = tr.dataset.i;
      const sel  = tr.querySelector(`.sel-transport[data-i="${i}"]`);
      const inp  = tr.querySelector(`.inp-km[data-i="${i}"]`);
      const tdT  = sel.closest("td");
      const tdK  = inp.closest("td");
      tdT.classList.remove("ok","ko");
      tdK.classList.remove("ok","ko");

      if(!sel.value || inp.value === ""){ vides++; return; }

      if(sel.value === tr.dataset.bon) tdT.classList.add("ok");
      else { tdT.classList.add("ko"); erreurs++; }

      if(Number(inp.value) === Number(tr.dataset.km)) tdK.classList.add("ok");
      else { tdK.classList.add("ko"); erreurs++; }
    });

    if(vides > 0){
      retour("fb-4","indice", `Il reste <b>${vides}</b> ligne(s) incomplète(s) : choisis un transport et calcule la distance.`, 3000);
      return;
    }
    if(erreurs === 0){
      retour("fb-4","succes","✨ Journal de bord exact ! Pour lire une carte, on multiplie la mesure en cm par ce qu'indique l'échelle.");
      if(typeof son === "function") son("succes");
      setTimeout(()=>validerSalle(4), 1200);
    }else{
      retour("fb-4","erreur", `<b>${erreurs}</b> erreur(s) — les cases en rouge sont à corriger. Rappel : 1 cm = 200 km, donc <b>distance = cm × 200</b>.`, 4000);
      if(typeof son === "function") son("erreur");
    }
  });

  const indices = ETAT.niveau==="CM1"
    ? ["Pour traverser une <b>mer</b> ou un <b>océan</b>, il faut un bateau : le paquebot à vapeur.",
       "Dans la <b>jungle</b>, là où la voie ferrée s'arrête, Fogg achète un éléphant.",
       "Pour la distance : 2 cm × 200 km = <b>400 km</b>. Fais pareil pour les autres lignes."]
    : ["Le <b>train</b> sert sur la terre ferme (Europe, Inde, États-Unis) ; le <b>paquebot</b> sur les mers.",
       "Le <b>traîneau à voile</b> n'est utilisé qu'une fois, sur la neige des grandes plaines américaines : il ne sert pas ici.",
       "L'échelle se lit comme une multiplication : 12 cm × 200 = <b>2400 km</b>."];
  activerBoutonIndice(indices);
}

/* ============================================================
   ÉNIGME 5 — L'HORLOGE DU MONDE  (finale)
   Fuseaux horaires, méridien de Greenwich, et le jour gagné.
   ============================================================ */
const VILLES_FUSEAU = {
  CM1: [
    {nom:"Paris",     decalage:1,  sens:"est"},
    {nom:"Le Caire",  decalage:2,  sens:"est"},
    {nom:"Hong Kong", decalage:8,  sens:"est"},
  ],
  CM2: [
    {nom:"Paris",         decalage:1,  sens:"est"},
    {nom:"Le Caire",      decalage:2,  sens:"est"},
    {nom:"Hong Kong",     decalage:8,  sens:"est"},
    {nom:"New York",      decalage:-5, sens:"ouest"},
    {nom:"San Francisco", decalage:-8, sens:"ouest"},
  ]
};
const HEURE_LONDRES = 12;

function enigme5HTML(){
  const villes = VILLES_FUSEAU[ETAT.niveau] || VILLES_FUSEAU.CM2;
  const options = Array.from({length:24}, (_,h)=>`<option value="${h}">${String(h).padStart(2,"0")} h</option>`).join("");
  const repJour = melanger([
    {t:"Il a <b>gagné</b> un jour : il croyait avoir mis 80 jours, il n'en avait mis que 79.", ok:true},
    {t:"Il a <b>perdu</b> un jour : il avait mis 81 jours.", ok:false},
    {t:"Rien du tout : le temps est le même partout sur la Terre.", ok:false},
  ]);

  return `
    <h3>⏰ L'horloge du monde — l'énigme du 80ᵉ jour</h3>
    <p class="center" style="opacity:.8;font-style:italic">
      À l'observatoire de Greenwich, il est <b>midi (12 h)</b>. La Terre est découpée en
      <b>24 fuseaux horaires</b> : chaque fuseau vers l'<b>est</b> ajoute 1 heure, chaque fuseau
      vers l'<b>ouest</b> en retire 1.
    </p>

    <div class="cadran-monde" aria-hidden="true">
      <div class="meridien"></div>
      <div class="noyau">Greenwich<br><b style="font-size:1.2rem">12 h</b><br>méridien 0°</div>
      <div class="ville" style="left:50%;top:8%">LONDRES<span class="h">12 h</span></div>
      <div class="ville" style="left:88%;top:50%">EST →<span class="h">+</span></div>
      <div class="ville" style="left:12%;top:50%">← OUEST<span class="h">−</span></div>
    </div>

    <div class="fuseaux-champs" id="fuseaux">
      ${villes.map((v,i)=>`
        <div class="fuseau-champ" data-i="${i}" data-bon="${(HEURE_LONDRES + v.decalage + 24) % 24}">
          <div class="ville-nom">${v.nom}</div>
          <div class="decalage">${v.decalage>0?"+":""}${v.decalage} h · vers l'${v.sens}</div>
          <select class="sel-heure" aria-label="Heure à ${v.nom}">
            <option value="">— h ? —</option>${options}
          </select>
        </div>`).join("")}
    </div>

    <div class="qcm-question" id="q-jour" data-bonne="${repJour.findIndex(r=>r.ok)}">
      <div class="q">🌍 Phileas Fogg a fait le tour du monde en voyageant toujours vers l'<b>est</b>.
        À son retour, que s'est-il passé ?</div>
      ${repJour.map((r,j)=>`<label class="qcm-option" data-j="${j}">${r.t}</label>`).join("")}
    </div>

    <div class="center"><button class="btn jade grand" id="btn-verif-5">🔓 Ouvrir le carnet de Phileas Fogg</button></div>
    <div class="feedback" id="fb-5"></div>
    <div class="barre-outils"><button class="btn laiton" id="btn-indice">💡 Indice</button></div>
  `;
}

function activerEnigme5(){
  let choixJour = null;
  const blocJour = document.getElementById("q-jour");
  const bonneJour = +blocJour.dataset.bonne;
  blocJour.querySelectorAll(".qcm-option").forEach(opt=>{
    opt.addEventListener("click", ()=>{
      blocJour.querySelectorAll(".qcm-option").forEach(x=>x.classList.remove("select"));
      opt.classList.add("select");
      choixJour = +opt.dataset.j;
      if(typeof son === "function") son("clic");
    });
  });

  document.getElementById("btn-verif-5").addEventListener("click", ()=>{
    const champs = [...document.querySelectorAll("#fuseaux .fuseau-champ")];
    let erreurs = 0, vides = 0;

    champs.forEach(ch=>{
      const sel = ch.querySelector(".sel-heure");
      ch.classList.remove("ok","ko");
      if(sel.value === ""){ vides++; return; }
      if(Number(sel.value) === Number(ch.dataset.bon)) ch.classList.add("ok");
      else { ch.classList.add("ko"); erreurs++; }
    });

    if(vides > 0){
      retour("fb-5","indice", `Il reste <b>${vides}</b> ville(s) sans heure.`, 2600);
      return;
    }
    if(choixJour === null){
      retour("fb-5","indice","Réponds aussi à la question sur le <b>jour gagné</b>.", 2600);
      return;
    }
    if(erreurs === 0 && choixJour === bonneJour){
      retour("fb-5","succes","✨ Le carnet s'ouvre ! Vous avez compris le secret du 80ᵉ jour.");
      if(typeof son === "function") son("deverrouille");
      setTimeout(()=>validerSalle(5), 1400);
    }else if(erreurs > 0){
      retour("fb-5","erreur", `<b>${erreurs}</b> heure(s) incorrecte(s). Pars de <b>12 h</b> à Londres, puis <b>ajoute</b> ou <b>retire</b> le décalage indiqué.`, 4000);
      if(typeof son === "function") son("erreur");
    }else{
      retour("fb-5","erreur","Les heures sont exactes ! Mais réfléchis encore à ce qui arrive quand on avance vers l'est en faisant le tour complet de la Terre…", 4000);
      if(typeof son === "function") son("erreur");
    }
  });

  const indices = ETAT.niveau==="CM1"
    ? ["À Paris il est <b>+1 h</b> : si Londres affiche 12 h, Paris affiche <b>13 h</b>.",
       "Pour Hong Kong, ajoute 8 heures à 12 h.",
       "En allant vers l'est, on va <b>à la rencontre du soleil</b> : les journées de voyage sont un peu plus courtes."]
    : ["Vers l'<b>est</b> on additionne, vers l'<b>ouest</b> on soustrait. New York : 12 − 5 = <b>7 h</b>.",
       "La Terre tourne sur elle-même en 24 h et fait 360° : 360 ÷ 24 = <b>15° par heure</b>, soit un fuseau.",
       "En faisant le tour complet vers l'est, Fogg a additionné 24 fois une heure : il a vu un lever de soleil de plus que les Londoniens. Il a donc <b>gagné un jour</b>."];
  activerBoutonIndice(indices);
}

window.enigmeSalle = enigmeSalle;
window.activerEnigme = activerEnigme;
window.CARTE_NIVEAUX = CARTE_NIVEAUX;
window.ITINERAIRES = ITINERAIRES;
