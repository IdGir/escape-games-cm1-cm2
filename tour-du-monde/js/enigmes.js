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
   attache les interactions, validerSalle(n, erreurs) clôt l'étape.

   Moteur v2 (octobre 2026) : chaque énigme se valide par un bouton ;
   en cas d'erreur, seul le NOMBRE de réponses justes est donné ;
   10 points du premier coup, 3 après une erreur ; aucun texte de
   correction après la réussite (voir js/v2.js).
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

/* Tracés du planisphère (viewBox 800 × 400).
   Calibrés sur la vraie carte assets/images/cartes/planisphere.jpg (1920×960,
   même ratio 2:1 que le viewBox, posée en fond via poserFondCarte avec
   object-fit:cover) : les zones cliquables tombent donc sur les bons
   continents de la photo, pas seulement sur le dessin de secours. */
const FORMES_CARTE = {
  "amerique-n":  "M0,63 L125,8 L283,58 L346,104 L258,96 L208,175 L146,196 L63,138 L0,92 Z",
  "amerique-s":  "M200,204 L258,200 L292,225 L275,271 L250,313 L233,354 L217,375 L208,313 L192,250 Z",
  "amerique":    "M0,63 L125,8 L283,58 L346,104 L292,225 L275,271 L250,313 L233,354 L217,375 L208,313 L192,250 L208,175 L146,196 L63,138 L0,92 Z",
  "europe":      "M350,92 L400,70 L450,75 L488,104 L482,140 L438,150 L396,129 L358,117 Z",
  "afrique":     "M375,175 L417,163 L471,160 L513,179 L500,229 L479,271 L450,313 L433,346 L413,313 L396,250 L383,208 Z",
  "asie":        "M417,167 L479,83 L604,8 L800,8 L800,188 L708,250 L604,271 L521,229 L458,188 Z",
  "oceanie":     "M692,250 L771,254 L800,271 L800,333 L763,346 L708,333 L688,292 Z",
  "antarctique": "M0,379 L800,379 L800,398 L0,398 Z",
};
/* Océans : zones cliquables en pleine eau, mêmes coordonnées calibrées */
const OCEANS_CARTE = {
  "pacifique": {cx:29,  cy:188, rx:27, ry:117},
  "atlantique":{cx:325, cy:188, rx:29, ry:104},
  "indien":    {cx:583, cy:292, rx:75, ry:42},
  "arctique":  {cx:400, cy:10,  rx:375,ry:8},
  "austral":   {cx:400, cy:373, rx:375,ry:8},
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
    ${v2Bandeau()}
    <p class="center" style="opacity:.75;font-style:italic">
      Clique sur une <b>zone de la carte</b>, puis sur son <b>nom</b> dans la liste du bas. Un clic sur une zone nommée efface son nom.
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
      <span><i style="background:rgba(59,110,165,.35);border:1px solid #3b6ea5"></i>nom posé</span>
      <span><i style="background:rgba(255,255,255,.4);border:1px dashed #102a41"></i>à compléter</span>
      <span>🔴 équateur &nbsp;·&nbsp; 🟢 méridien de Greenwich</span>
    </div>
    <div class="banque" id="banque-1">
      ${melanger(aPlacer).map(e=>
        `<div class="etiquette ${e.id.startsWith("oc")||OCEANS_CARTE[e.id]?"ocean":""}" data-val="${e.id}">${e.nom}</div>`
      ).join("")}
    </div>
    <div class="center"><button class="btn jade" id="btn-verif-1">✅ Vérifier la carte</button></div>
    <div class="feedback" id="fb-1"></div>
    <div class="barre-outils"><button class="btn laiton" id="btn-indice">💡 Indice</button></div>
  `;
}

/* Centre approximatif d'un tracé, pour y poser l'étiquette */
function centreForme(id){
  const centres = {
    "amerique-n":{x:159,y:103},"amerique-s":{x:236,y:278},"amerique":{x:190,y:190},
    "europe":{x:419,y:107},"afrique":{x:439,y:237},"asie":{x:599,y:155},
    "oceanie":{x:746,y:297},"antarctique":{x:400,y:388},
  };
  return centres[id] || {x:400,y:200};
}

function activerEnigme1(){
  const cfg = CARTE_NIVEAUX[ETAT.niveau] || CARTE_NIVEAUX.CM2;
  const noms = {};
  [...cfg.terres, ...cfg.eaux].forEach(e=>noms[e.id] = e.nom);
  const total = Object.keys(noms).length;

  v2Debut();
  let zoneVisee = null;
  const poses = {};            // zone → étiquette posée

  const planisphere = document.querySelector(".planisphere");
  const svg = planisphere.querySelector("svg");
  const banque = document.getElementById("banque-1");

  /* Fond de carte facultatif : si l'enseignant a déposé
     assets/images/cartes/planisphere.jpg, il se glisse SOUS les zones
     cliquables, qui restent parfaitement utilisables. */
  if(typeof poserFondCarte === "function"){
    poserFondCarte(planisphere, "planisphere", "fond-planisphere");
  }
  const dessiner = ()=>svg.querySelectorAll(".zone-carte").forEach(z=>{
    const id = z.dataset.zone, et = poses[id];
    z.classList.toggle("placee", !!et);
    z.classList.toggle("visee", z === zoneVisee);
    const txt = document.getElementById("txt-"+id);
    if(txt) txt.textContent = et ? et.textContent : "";
  });

  // 1. Sélection d'une zone de la carte (une zone nommée se vide)
  svg.querySelectorAll(".zone-carte").forEach(z=>{
    z.addEventListener("click", ()=>{
      const id = z.dataset.zone;
      if(poses[id]){ poses[id].classList.remove("utilisee"); delete poses[id]; zoneVisee = z; }
      else zoneVisee = (zoneVisee === z) ? null : z;
      if(typeof son === "function") son("clic");
      dessiner();
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
    poses[zoneVisee.dataset.zone] = et;
    et.classList.add("utilisee");
    zoneVisee = null;
    if(typeof son === "function") son("clic");
    dessiner();
  });

  document.getElementById("btn-verif-1").addEventListener("click", ()=>{
    const zones = Object.keys(noms);
    if(zones.some(id=>!poses[id])) return v2Incomplet("fb-1", "Pose un nom sur chaque zone de la carte avant de vérifier.");
    const justes = zones.filter(id=>poses[id].dataset.val === id).length;
    if(justes === zones.length) v2Reussite("fb-1", err=>validerSalle(1, err));
    else v2Echec("fb-1", justes, zones.length, "noms bien placés");
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
    ${v2Bandeau()}
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
  v2Debut();
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
    if(choixCanal === null) return v2Incomplet("fb-2", "Réponds aussi à la question sur le <b>canal</b> avant de vérifier.");
    const justes = items.filter((it,i)=> +it.dataset.rang === i+1).length + (choixCanal === bonneCanal ? 1 : 0);
    const total = items.length + 1;
    if(justes === total) v2Reussite("fb-2", err=>validerSalle(2, err));
    else v2Echec("fb-2", justes, total, "réponses justes (escales à la bonne place + question du canal)");
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
    ${v2Bandeau()}
    <p class="center" style="opacity:.75;font-style:italic">
      Clique sur un <b>paysage</b>, puis sur le <b>climat</b> qui lui correspond. Un nouveau clic défait la paire.
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
    <div class="center"><button class="btn jade" id="btn-verif-3">✅ Vérifier les climats</button></div>
    <div class="feedback" id="fb-3"></div>
    <div class="barre-outils"><button class="btn laiton" id="btn-indice">💡 Indice</button></div>
  `;
}

function activerEnigme3(){
  v2Debut();
  const paysages = document.querySelectorAll("#grille-paysages .paysage");

  /* Photos de paysage facultatives : assets/images/cartes/paysage-desert.jpg,
     paysage-jungle.jpg… Sans fichier, le pictogramme reste affiché. */
  if(typeof illustrerVignette === "function"){
    paysages.forEach(p=>illustrerVignette(p.querySelector(".vignette"), p.dataset.image));
  }

  const asso = v2Association("#grille-paysages .paysage", "#col-climats .carte-match");
  document.getElementById("btn-verif-3").addEventListener("click", ()=>{
    if(!asso.complet()) return v2Incomplet("fb-3", "Associe chaque paysage à un climat avant de vérifier.");
    const j = asso.justes();
    if(j === asso.total) v2Reussite("fb-3", err=>validerSalle(3, err));
    else v2Echec("fb-3", j, asso.total, "associations justes");
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
    ${v2Bandeau()}
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
  v2Debut();
  document.getElementById("btn-verif-4").addEventListener("click", ()=>{
    const lignes = [...document.querySelectorAll(".table-bord tbody tr")];
    let justes = 0, vides = 0;
    lignes.forEach(tr=>{
      const sel = tr.querySelector(".sel-transport"), inp = tr.querySelector(".inp-km");
      if(!sel.value || inp.value === ""){ vides++; return; }
      if(sel.value === tr.dataset.bon) justes++;
      if(Number(inp.value) === Number(tr.dataset.km)) justes++;
    });
    if(vides > 0) return v2Incomplet("fb-4", `Il reste <b>${vides}</b> ligne(s) incomplète(s) : choisis un transport et calcule la distance.`);
    const total = lignes.length * 2;
    if(justes === total) v2Reussite("fb-4", err=>validerSalle(4, err));
    else v2Echec("fb-4", justes, total, "cases justes (transports et distances)");
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
    ${v2Bandeau()}
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
  v2Debut();
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
    const vides = champs.filter(ch=>ch.querySelector(".sel-heure").value === "").length;
    if(vides > 0) return v2Incomplet("fb-5", `Il reste <b>${vides}</b> ville(s) sans heure.`);
    if(choixJour === null) return v2Incomplet("fb-5", "Réponds aussi à la question sur le <b>jour gagné</b>.");
    const justes = champs.filter(ch=>Number(ch.querySelector(".sel-heure").value) === Number(ch.dataset.bon)).length
      + (choixJour === bonneJour ? 1 : 0);
    const total = champs.length + 1;
    if(justes === total) v2Reussite("fb-5", err=>validerSalle(5, err));
    else v2Echec("fb-5", justes, total, "réponses justes (heures + question du jour)");
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
