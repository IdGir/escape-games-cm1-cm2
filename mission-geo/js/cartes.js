/* =========================================================
   CARTES — fonds de carte et schémas dessinés (SVG)
   ---------------------------------------------------------
   Ces dessins servent à deux choses :
     - de repli quand aucune image ni vidéo n'a été déposée ;
     - de fond pour les activités « étiquettes à placer ».
   Ils sont volontairement simplifiés : lisibles au vidéoprojecteur,
   suffisants pour repérer fleuves, massifs, régions et continents.
   Toutes les coordonnées d'étiquettes des séances sont exprimées
   en POURCENTAGE de la boîte : elles restent donc valables si
   l'enseignant remplace le dessin par une vraie carte.
   ========================================================= */

const CARTES = (function(){

  /* ---------- Contour simplifie de la France (viewBox 620x520) ---------- */
  const CONTOUR_FRANCE =
    "M314,18 L282,23 L222,93 L154,83 L138,138 L38,148 L30,168 L82,183 " +
    "L130,203 L146,243 L170,258 L178,288 L170,338 L154,393 L338,443 " +
    "L374,388 L434,403 L510,383 L482,323 L462,258 L522,188 L530,138 " +
    "L546,118 L450,93 L342,38 Z";

  const CONTOUR_CORSE =
    "M566,433 L592,433 L600,448 L598,473 L590,498 L570,488 L562,458 Z";

  function enveloppe(interieur, vb){
    return '<svg viewBox="' + (vb || "0 0 620 520") + '" xmlns="http://www.w3.org/2000/svg" ' +
           'role="img" style="width:100%;height:auto;background:#dceaf6">' + interieur + '</svg>';
  }

  /* =========================================================
     1. FRANCE — fleuves et massifs
     ========================================================= */
  function franceFleuves(opt){
    opt = opt || {};
    const massif = (d, nom) =>
      '<path d="' + d + '" fill="#c9a06a" stroke="#a97f4a" stroke-width="1.5" opacity=".85"/>' +
      (opt.noms ? '<text class="nom-massif">' + nom + '</text>' : '');

    return enveloppe(
      /* mers */
      '<rect x="0" y="0" width="620" height="520" fill="#bfe0f2"/>' +
      '<path d="' + CONTOUR_FRANCE + '" fill="#dff0d5" stroke="#4a6b3c" stroke-width="2.5"/>' +
      '<path d="' + CONTOUR_CORSE + '" fill="#dff0d5" stroke="#4a6b3c" stroke-width="2.5"/>' +

      /* massifs : blobs arrondis */
      massif("M478,140 q22,-6 26,20 q4,26 -16,32 q-22,4 -24,-22 q-2,-24 14,-30 Z", "Vosges") +
      massif("M440,214 q26,-10 32,16 q6,26 -14,34 q-22,8 -30,-16 q-8,-24 12,-34 Z", "Jura") +
      massif("M456,272 q34,-8 40,30 q6,40 -22,52 q-30,10 -40,-28 q-10,-40 22,-54 Z", "Alpes") +
      massif("M304,272 q46,-14 54,32 q8,46 -30,58 q-42,10 -52,-32 q-10,-44 28,-58 Z", "Massif central") +
      massif("M180,398 q70,-16 128,26 q28,20 -6,28 q-64,-6 -122,-26 q-24,-12 0,-28 Z", "Pyrénées") +
      massif("M570,442 q20,-4 22,26 q2,30 -14,32 q-18,0 -20,-28 q-2,-28 12,-30 Z", "Corse") +

      /* fleuves */
      '<g fill="none" stroke="#1f6fb8" stroke-width="4" stroke-linecap="round">' +
        '<path d="M406,178 L382,153 L312,126 L262,98 L222,93"/>' +   /* Seine   */
        '<path d="M386,328 L344,218 L294,173 L246,198 L156,208 L130,203"/>' + /* Loire */
        '<path d="M246,428 L276,388 L195,326 L178,288"/>' +          /* Garonne */
        '<path d="M462,258 L412,280 L410,371 L406,401"/>' +          /* Rhone   */
        '<path d="M522,188 L530,138 L546,118"/>' +                   /* Rhin    */
      '</g>' +

      /* reperes textuels toujours utiles */
      '<text x="60" y="300" font-size="15" fill="#2c6c99" font-style="italic">Océan Atlantique</text>' +
      '<text x="220" y="45" font-size="15" fill="#2c6c99" font-style="italic">Manche</text>' +
      '<text x="400" y="470" font-size="15" fill="#2c6c99" font-style="italic">Mer Méditerranée</text>' +
      '<g font-size="13" fill="#3a4a5c">' +
        '<text x="330" y="12">N</text>' +
      '</g>'
    );
  }

  /* =========================================================
     2. FRANCE — mers et oceans (fond du littoral)
     ========================================================= */
  function franceMers(){
    return enveloppe(
      '<rect x="0" y="0" width="620" height="520" fill="#bfe0f2"/>' +
      '<path d="' + CONTOUR_FRANCE + '" fill="#e6f2da" stroke="#4a6b3c" stroke-width="2.5"/>' +
      '<path d="' + CONTOUR_CORSE + '" fill="#e6f2da" stroke="#4a6b3c" stroke-width="2.5"/>' +
      '<g stroke="#1f6fb8" stroke-width="2" fill="none" opacity=".5">' +
        '<path d="M60,120 q30,-12 60,0"/><path d="M60,150 q30,-12 60,0"/>' +
        '<path d="M470,470 q30,-12 60,0"/><path d="M420,470 q-30,-12 -60,0"/>' +
      '</g>'
    );
  }

  /* =========================================================
     3. FRANCE — les 13 regions metropolitaines (pastilles)
     ========================================================= */
  const REGIONS = [
    {n:1,  x:102, y:158, nom:"Bretagne"},
    {n:2,  x:186, y:193, nom:"Pays de la Loire"},
    {n:3,  x:222, y:113, nom:"Normandie"},
    {n:4,  x:330, y:68,  nom:"Hauts-de-France"},
    {n:5,  x:442, y:133, nom:"Grand Est"},
    {n:6,  x:318, y:133, nom:"Île-de-France"},
    {n:7,  x:286, y:193, nom:"Centre-Val de Loire"},
    {n:8,  x:410, y:208, nom:"Bourgogne-Franche-Comté"},
    {n:9,  x:398, y:293, nom:"Auvergne-Rhône-Alpes"},
    {n:10, x:226, y:308, nom:"Nouvelle-Aquitaine"},
    {n:11, x:306, y:378, nom:"Occitanie"},
    {n:12, x:458, y:373, nom:"Provence-Alpes-Côte d'Azur"},
    {n:13, x:582, y:458, nom:"Corse"}
  ];

  function franceRegions(){
    const pastilles = REGIONS.map(r =>
      '<circle cx="' + r.x + '" cy="' + r.y + '" r="15" fill="#1f6fb8" stroke="#fff" stroke-width="2.5"/>' +
      '<text x="' + r.x + '" y="' + (r.y + 5) + '" text-anchor="middle" font-size="15" ' +
      'font-weight="700" fill="#fff">' + r.n + '</text>').join("");
    return enveloppe(
      '<rect x="0" y="0" width="620" height="520" fill="#bfe0f2"/>' +
      '<path d="' + CONTOUR_FRANCE + '" fill="#f2ead6" stroke="#7a6a4a" stroke-width="2.5"/>' +
      '<path d="' + CONTOUR_CORSE + '" fill="#f2ead6" stroke="#7a6a4a" stroke-width="2.5"/>' +
      pastilles
    );
  }

  /* =========================================================
     4. PLANISPHERE simplifie
     variante : "riches" colore les continents par niveau de vie
     ========================================================= */
  const CONTINENTS = {
    "amerique-nord":
      "M33,67 L111,83 L153,114 L175,161 L208,194 L231,206 L269,222 L278,181 " +
      "L292,153 L317,125 L347,119 L333,89 L292,61 L236,50 L153,56 Z",
    "amerique-sud":
      "M278,228 L306,217 L333,236 L361,250 L403,267 L394,300 L367,319 L339,347 " +
      "L319,375 L306,397 L292,375 L303,333 L306,300 L286,264 Z",
    "europe":
      "M472,150 L500,128 L528,144 L556,139 L578,136 L583,125 L611,117 L611,83 " +
      "L583,67 L569,53 L528,75 L514,83 L486,111 L472,131 Z",
    "afrique":
      "M453,208 L500,208 L542,189 L589,164 L597,194 L619,217 L642,217 L617,256 " +
      "L611,292 L597,311 L569,344 L550,344 L533,300 L522,239 L486,236 Z",
    "asie":
      "M611,117 L667,97 L722,83 L778,50 L889,50 L1000,67 L1000,97 L944,111 " +
      "L889,125 L875,153 L839,167 L833,189 L792,222 L764,236 L722,228 L700,194 " +
      "L667,181 L639,172 L619,217 L597,194 L589,164 L583,125 Z",
    "oceanie":
      "M814,311 L858,283 L894,281 L906,303 L917,319 L925,328 L917,356 L889,356 " +
      "L858,339 L819,344 Z",
    "antarctique":
      "M80,468 L200,452 L340,462 L470,450 L600,462 L740,452 L900,470 L920,500 " +
      "L60,500 Z"
  };

  const NOMS_CONTINENTS = {
    "amerique-nord":{t:"Amérique du Nord", x:180, y:130},
    "amerique-sud" :{t:"Amérique du Sud",  x:330, y:315},
    "europe"       :{t:"Europe",           x:540, y:100},
    "afrique"      :{t:"Afrique",          x:545, y:265},
    "asie"         :{t:"Asie",             x:800, y:140},
    "oceanie"      :{t:"Océanie",          x:865, y:322},
    "antarctique"  :{t:"Antarctique",      x:500, y:487}
  };

  /* Niveau de vie tres simplifie, calque sur la carte du livret */
  const RICHESSE = {
    "amerique-nord":"riche", "europe":"riche", "oceanie":"riche",
    "asie":"mixte", "amerique-sud":"pauvre", "afrique":"tres-pauvre",
    "antarctique":"tres-pauvre"
  };
  const COULEUR_RICHESSE = {
    "riche":"#d9382c", "mixte":"#f0a23c", "pauvre":"#f6c96a", "tres-pauvre":"#fbe6a2"
  };

  function planisphere(opt){
    opt = opt || {};
    let corps = '<rect x="0" y="0" width="1000" height="500" fill="#bfe0f2"/>';
    if(opt.grille){
      corps += '<g stroke="#9cc4dd" stroke-width="1" opacity=".8">';
      for(let y=0; y<=500; y+=62.5) corps += '<line x1="0" y1="'+y+'" x2="1000" y2="'+y+'"/>';
      for(let x=0; x<=1000; x+=83.3) corps += '<line x1="'+x+'" y1="0" x2="'+x+'" y2="500"/>';
      corps += '</g>';
    }
    /* equateur */
    corps += '<line x1="0" y1="250" x2="1000" y2="250" stroke="#4a6b8c" stroke-dasharray="8 6" stroke-width="1.5"/>' +
             '<text x="8" y="245" font-size="13" fill="#3a5a7c" font-style="italic">équateur</text>';

    for(const [id, d] of Object.entries(CONTINENTS)){
      const fond = (opt.richesse && id !== "antarctique")
        ? COULEUR_RICHESSE[RICHESSE[id]] : "#e7dfc6";
      corps += '<path data-continent="' + id + '" d="' + d + '" fill="' + fond +
               '" stroke="#8a7f5f" stroke-width="1.5"/>';
    }
    if(opt.noms !== false){
      for(const [id, n] of Object.entries(NOMS_CONTINENTS)){
        corps += '<text x="' + n.x + '" y="' + n.y + '" text-anchor="middle" font-size="17" ' +
                 'font-weight="700" fill="#4a4030">' + n.t + '</text>';
      }
    }
    if(opt.richesse){
      const legendes = [["riche","Pays riches"],["mixte","Situations contrastees"],
                        ["pauvre","Pays pauvres"],["tres-pauvre","Pays tres pauvres"]];
      corps += '<g font-size="13" fill="#2a2a2a">' +
        '<rect x="14" y="382" width="212" height="104" fill="#ffffffdd" stroke="#8a7f5f"/>' +
        legendes.map(([cle, txt], i) =>
          '<rect x="24" y="' + (394 + i*24) + '" width="22" height="16" fill="' + COULEUR_RICHESSE[cle] + '" stroke="#7a6a4a"/>' +
          '<text x="54" y="' + (407 + i*24) + '">' + txt + '</text>').join("") +
        '</g>';
    }
    return enveloppe(corps, "0 0 1000 500");
  }

  /* =========================================================
     5. Profil d'un cours d'eau : de l'amont vers l'aval
     ========================================================= */
  function coursEau(){
    return enveloppe(
      '<rect x="0" y="0" width="900" height="420" fill="#e9f4fb"/>' +
      /* relief */
      '<path d="M0,300 L120,110 L200,180 L280,90 L360,210 L470,250 L620,280 L900,300 L900,420 L0,420 Z" ' +
        'fill="#cbb78e" stroke="#9c8558" stroke-width="2"/>' +
      '<path d="M60,300 L120,110 L180,300 Z" fill="#f3f6f8" opacity=".9"/>' +
      '<path d="M230,300 L280,90 L330,300 Z" fill="#f3f6f8" opacity=".9"/>' +
      /* cours d'eau */
      '<path d="M280,120 C300,190 250,230 300,260 C360,295 420,270 470,300 ' +
        'C540,340 640,320 700,350 L900,360" fill="none" stroke="#2b86cd" stroke-width="9" stroke-linecap="round"/>' +
      '<path d="M120,140 C150,200 220,220 260,245" fill="none" stroke="#2b86cd" stroke-width="5"/>' +
      '<path d="M470,300 C520,270 560,290 600,330" fill="none" stroke="#2b86cd" stroke-width="5"/>' +
      /* mer */
      '<path d="M820,320 L900,320 L900,420 L790,420 Z" fill="#7fc0e8"/>' +
      /* legendes generiques */
      '<g font-size="16" fill="#33475e" font-weight="600">' +
        '<text x="245" y="80">amont</text>' +
        '<text x="770" y="310">aval</text>' +
      '</g>'
    );
  }

  /* =========================================================
     6. Paysage « ou va cette eau ? »  (usages de l'eau)
     ========================================================= */
  function paysageEau(){
    return enveloppe(
      '<rect x="0" y="0" width="900" height="480" fill="#cfe9f7"/>' +
      '<path d="M0,150 L120,60 L230,140 L330,50 L450,150 L560,110 L700,160 L900,120 L900,480 L0,480 Z" fill="#a9c98d"/>' +
      '<path d="M0,150 L120,60 L230,140 L330,50 L450,150 L360,150 L0,180 Z" fill="#cbb78e"/>' +
      '<path d="M300,90 C330,180 260,240 320,300 C380,360 520,340 600,400 L900,430 L900,480 L520,480 Z" ' +
        'fill="none" stroke="#2b86cd" stroke-width="12" stroke-linecap="round"/>' +
      /* ville */
      '<g fill="#e6e6ea" stroke="#8c8c96">' +
        '<rect x="70" y="300" width="40" height="90"/><rect x="120" y="330" width="34" height="60"/>' +
        '<rect x="164" y="310" width="30" height="80"/>' +
      '</g>' +
      /* champs */
      '<g fill="#e3d27a" stroke="#b7a44e">' +
        '<rect x="480" y="230" width="130" height="50"/><rect x="630" y="250" width="120" height="46"/>' +
      '</g>' +
      /* usine */
      '<g fill="#c9ced6" stroke="#7d848f">' +
        '<rect x="760" y="270" width="90" height="70"/><rect x="800" y="230" width="16" height="42"/>' +
      '</g>' +
      '<text x="20" y="30" font-size="20" font-weight="700" fill="#0b3d91">Où va cette eau ?</text>',
      "0 0 900 480"
    );
  }

  /* =========================================================
     7. Village vu du ciel (commune rurale)
     ========================================================= */
  function villageAerien(){
    return enveloppe(
      '<rect x="0" y="0" width="800" height="560" fill="#7f9f5e"/>' +
      '<g fill="#8fae6a" stroke="#6f8c50">' +
        '<rect x="20" y="20" width="220" height="150"/><rect x="560" y="30" width="210" height="170"/>' +
        '<rect x="40" y="400" width="240" height="140"/><rect x="520" y="380" width="250" height="160"/>' +
      '</g>' +
      /* routes */
      '<g stroke="#e8e3d2" stroke-width="16" fill="none">' +
        '<path d="M0,300 L800,290"/><path d="M400,0 L390,560"/><path d="M390,300 L640,120"/>' +
      '</g>' +
      /* bourg */
      '<g fill="#cf7f5c" stroke="#8a4f36">' +
        '<rect x="330" y="250" width="26" height="22"/><rect x="362" y="246" width="24" height="20"/>' +
        '<rect x="404" y="252" width="30" height="24"/><rect x="352" y="282" width="26" height="22"/>' +
        '<rect x="398" y="288" width="24" height="20"/><rect x="428" y="262" width="22" height="18"/>' +
      '</g>' +
      /* eglise */
      '<g fill="#b9b2a2" stroke="#6f695c">' +
        '<rect x="368" y="212" width="34" height="26"/><rect x="378" y="188" width="12" height="26"/>' +
      '</g>' +
      /* lotissement */
      '<g fill="#e0c98d" stroke="#9c8a55">' +
        '<rect x="150" y="330" width="20" height="18"/><rect x="180" y="330" width="20" height="18"/>' +
        '<rect x="210" y="330" width="20" height="18"/><rect x="150" y="358" width="20" height="18"/>' +
        '<rect x="180" y="358" width="20" height="18"/><rect x="210" y="358" width="20" height="18"/>' +
      '</g>',
      "0 0 800 560"
    );
  }

  /* =========================================================
     8. Carte quadrillee de la Corse (piste finale)
     ========================================================= */
  function corseGrille(opt){
    opt = opt || {};
    const c = opt.colonnes || 5, l = opt.lignes || 5;
    const L = 500, H = 500;
    let s = '<rect x="0" y="0" width="' + L + '" height="' + H + '" fill="#bfe0f2"/>';
    /* silhouette de la Corse occidentale, agrandie */
    s += '<path d="M250,20 L330,40 L400,30 L470,60 L480,200 L440,330 L400,470 L300,480 ' +
         'L250,430 L200,300 L150,220 L170,120 Z" fill="#e3d9bd" stroke="#8a7a55" stroke-width="2"/>';
    s += '<path d="M250,20 L170,120 L150,220 L200,300 L250,430 L300,480 L120,480 L120,20 Z" fill="#bfe0f2"/>';
    /* golfes */
    s += '<g fill="#9fd0ea" stroke="#4a90b8">' +
         '<path d="M170,120 q40,20 10,50 q-40,10 -30,-40 Z"/>' +
         '<path d="M200,240 q50,10 20,50 q-45,5 -30,-45 Z"/>' +
         '</g>';
    s += '<g font-size="14" fill="#2c6c99" font-style="italic">' +
         '<text x="14" y="270">Mer Méditerranée</text><text x="380" y="120">CORSE</text></g>';
    /* quadrillage */
    s += '<g stroke="#4a5a6a" stroke-width="1.5" opacity=".8">';
    for(let i=0;i<=c;i++) s += '<line x1="'+(i*L/c)+'" y1="0" x2="'+(i*L/c)+'" y2="'+H+'"/>';
    for(let j=0;j<=l;j++) s += '<line x1="0" y1="'+(j*H/l)+'" x2="'+L+'" y2="'+(j*H/l)+'"/>';
    s += '</g>';
    /* reperes */
    s += '<g font-size="15" font-weight="700" fill="#0b3d91">';
    for(let i=0;i<c;i++) s += '<text x="'+(i*L/c + L/(2*c))+'" y="18" text-anchor="middle">'+(i+1)+'</text>';
    for(let j=0;j<l;j++) s += '<text x="10" y="'+(j*H/l + H/(2*l))+'">'+(j+1)+'</text>';
    s += '</g>';
    return enveloppe(s, "0 0 500 500");
  }

  /* =========================================================
     Table de correspondance nom -> dessin
     ========================================================= */
  const DECORS = {
    "france-fleuves":      () => franceFleuves({noms:false}),
    "france-mers":         franceMers,
    "france-regions":      franceRegions,
    "planisphere":         () => planisphere({noms:true}),
    "planisphere-muet":    () => planisphere({noms:false}),
    "planisphere-grille":  () => planisphere({noms:true, grille:true}),
    "planisphere-richesses": () => planisphere({noms:true, richesse:true}),
    "cours-eau":           coursEau,
    "paysage-eau":         paysageEau,
    "village-aerien":      villageAerien,
    "corse-grille":        corseGrille
  };

  function decor(nom){
    const f = DECORS[nom];
    return f ? f() : null;
  }

  return { decor, REGIONS, CONTINENTS, planisphere, corseGrille, disponibles: Object.keys(DECORS) };
})();
