/* ============================================================
   MOTEUR AUDIO — Web Audio API (100 % synthétisé, 0 fichier)
   ------------------------------------------------------------
   - Ambiances par salle : pluie, imprimerie, jardins, incendie, assemblée
   - Effets : clic, réussite, erreur, fragment, déverrouillage, badge
   - Aucun fichier externe : fonctionne en double-clic hors-ligne
   - Démarrage différé au premier geste utilisateur (politique navigateurs)
   ============================================================ */

const AUDIO = {
  ctx: null,
  pret: false,
  actif: true,
  volume: 0.55,
  masterGain: null,
  ambianceGain: null,
  effetsGain: null,
  ambianceCourante: null,
  noeudsAmbiance: [],
  bufferBruit: null,
};

/* ---- Création différée du contexte (exigence navigateurs) ---- */
function initAudio(){
  if(AUDIO.ctx) return true;
  const AC = window.AudioContext || window.webkitAudioContext;
  if(!AC){
    console.warn("Web Audio non disponible — jeu silencieux.");
    return false;
  }
  try{
    AUDIO.ctx = new AC();
  }catch(e){
    console.warn("Impossible de créer le contexte audio :", e.message);
    return false;
  }

  // Chaîne : [ambiance] + [effets] -> master -> sortie
  AUDIO.masterGain = AUDIO.ctx.createGain();
  AUDIO.masterGain.gain.value = AUDIO.actif ? AUDIO.volume : 0;
  AUDIO.masterGain.connect(AUDIO.ctx.destination);

  AUDIO.ambianceGain = AUDIO.ctx.createGain();
  AUDIO.ambianceGain.gain.value = 0.38;      // ambiance discrète (classe scolaire)
  AUDIO.ambianceGain.connect(AUDIO.masterGain);

  AUDIO.effetsGain = AUDIO.ctx.createGain();
  AUDIO.effetsGain.gain.value = 0.85;
  AUDIO.effetsGain.connect(AUDIO.masterGain);

  AUDIO.bufferBruit = creerBufferBruit();
  AUDIO.pret = true;
  return true;
}

/* ---- Buffer de bruit blanc réutilisable (2 s, bouclé) ---- */
function creerBufferBruit(){
  const ctx = AUDIO.ctx;
  const longueur = ctx.sampleRate * 2;
  const buffer = ctx.createBuffer(1, longueur, ctx.sampleRate);
  const data = buffer.getChannelData(0);
  for(let i=0; i<longueur; i++){
    data[i] = Math.random()*2 - 1;
  }
  return buffer;
}

/* ---- Source de bruit bouclée ---- */
function sourceBruit(){
  const s = AUDIO.ctx.createBufferSource();
  s.buffer = AUDIO.bufferBruit;
  s.loop = true;
  return s;
}

/* ---- Réveil du contexte (Chrome suspend tant qu'il n'y a pas de geste) ---- */
function reveillerAudio(){
  if(!AUDIO.ctx) initAudio();
  if(AUDIO.ctx && AUDIO.ctx.state === "suspended"){
    AUDIO.ctx.resume().catch(()=>{});
  }
}

/* ============================================================
   EFFETS SONORES
   ============================================================ */

/**
 * Joue un effet sonore.
 * @param {string} nom - clic|survol|succes|erreur|fragment|deverrouille|badge|page|transition
 */
function son(nom){
  if(!AUDIO.actif) return;
  if(!AUDIO.pret && !initAudio()) return;
  reveillerAudio();
  const ctx = AUDIO.ctx;
  const t = ctx.currentTime;

  switch(nom){

    /* Clic sec et boisé — bouton, sélection */
    case "clic": {
      bip({freq:880, type:"triangle", debut:t, duree:0.06, vol:0.16, glisseVers:520});
      souffle({debut:t, duree:0.04, vol:0.05, filtre:2600});
      break;
    }

    /* Survol discret */
    case "survol": {
      bip({freq:1200, type:"sine", debut:t, duree:0.05, vol:0.05});
      break;
    }

    /* Réussite — arpège majeur montant (do-mi-sol-do) */
    case "succes": {
      [523.25, 659.25, 783.99, 1046.5].forEach((f,i)=>{
        bip({freq:f, type:"triangle", debut:t + i*0.09, duree:0.4, vol:0.17});
      });
      break;
    }

    /* Erreur — deux notes descendantes douces (jamais punitif) */
    case "erreur": {
      bip({freq:392, type:"sine", debut:t,        duree:0.16, vol:0.15});
      bip({freq:294, type:"sine", debut:t + 0.14, duree:0.26, vol:0.15});
      break;
    }

    /* Fragment récupéré — scintillement cristallin */
    case "fragment": {
      [1318.5, 1760, 2093, 2637].forEach((f,i)=>{
        bip({freq:f, type:"sine", debut:t + i*0.07, duree:0.55, vol:0.11});
      });
      // Voile scintillant
      const s = sourceBruit();
      const bp = ctx.createBiquadFilter();
      bp.type = "bandpass"; bp.frequency.value = 5200; bp.Q.value = 12;
      const g = ctx.createGain();
      g.gain.setValueAtTime(0, t);
      g.gain.linearRampToValueAtTime(0.05, t + 0.08);
      g.gain.exponentialRampToValueAtTime(0.001, t + 0.9);
      s.connect(bp).connect(g).connect(AUDIO.effetsGain);
      s.start(t); s.stop(t + 0.95);
      break;
    }

    /* Déverrouillage — mécanisme de serrure */
    case "deverrouille": {
      clac({debut:t,        vol:0.20, freq:180});
      clac({debut:t + 0.13, vol:0.16, freq:150});
      bip({freq:660, type:"triangle", debut:t + 0.26, duree:0.35, vol:0.14, glisseVers:880});
      break;
    }

    /* Badge obtenu — fanfare courte */
    case "badge": {
      [523.25, 523.25, 659.25, 880].forEach((f,i)=>{
        bip({freq:f, type:"square", debut:t + i*0.11, duree:0.22, vol:0.09});
      });
      break;
    }

    /* Tourner une page / ouvrir un panneau */
    case "page": {
      const s = sourceBruit();
      const bp = ctx.createBiquadFilter();
      bp.type = "bandpass"; bp.frequency.setValueAtTime(1200, t);
      bp.frequency.exponentialRampToValueAtTime(3200, t + 0.22);
      bp.Q.value = 1.2;
      const g = ctx.createGain();
      g.gain.setValueAtTime(0, t);
      g.gain.linearRampToValueAtTime(0.09, t + 0.05);
      g.gain.exponentialRampToValueAtTime(0.001, t + 0.3);
      s.connect(bp).connect(g).connect(AUDIO.effetsGain);
      s.start(t); s.stop(t + 0.35);
      break;
    }

    /* Transition entre salles — balayage */
    case "transition": {
      const s = sourceBruit();
      const lp = ctx.createBiquadFilter();
      lp.type = "lowpass";
      lp.frequency.setValueAtTime(320, t);
      lp.frequency.exponentialRampToValueAtTime(4800, t + 0.5);
      const g = ctx.createGain();
      g.gain.setValueAtTime(0, t);
      g.gain.linearRampToValueAtTime(0.10, t + 0.25);
      g.gain.exponentialRampToValueAtTime(0.001, t + 0.75);
      s.connect(lp).connect(g).connect(AUDIO.effetsGain);
      s.start(t); s.stop(t + 0.8);
      break;
    }
  }
}

/* ---- Brique : note simple avec enveloppe douce ---- */
function bip({freq, type="sine", debut, duree=0.2, vol=0.15, glisseVers=null}){
  const ctx = AUDIO.ctx;
  const o = ctx.createOscillator();
  const g = ctx.createGain();
  o.type = type;
  o.frequency.setValueAtTime(freq, debut);
  if(glisseVers) o.frequency.exponentialRampToValueAtTime(glisseVers, debut + duree);
  g.gain.setValueAtTime(0, debut);
  g.gain.linearRampToValueAtTime(vol, debut + 0.012);
  g.gain.exponentialRampToValueAtTime(0.0001, debut + duree);
  o.connect(g).connect(AUDIO.effetsGain);
  o.start(debut);
  o.stop(debut + duree + 0.05);
}

/* ---- Brique : impact percussif (bois, mécanisme) ---- */
function clac({debut, vol=0.2, freq=200}){
  const ctx = AUDIO.ctx;
  const s = sourceBruit();
  const bp = ctx.createBiquadFilter();
  bp.type = "bandpass"; bp.frequency.value = freq; bp.Q.value = 3;
  const g = ctx.createGain();
  g.gain.setValueAtTime(vol, debut);
  g.gain.exponentialRampToValueAtTime(0.0001, debut + 0.09);
  s.connect(bp).connect(g).connect(AUDIO.effetsGain);
  s.start(debut); s.stop(debut + 0.12);
}

/* ---- Brique : souffle filtré court ---- */
function souffle({debut, duree=0.1, vol=0.06, filtre=2000}){
  const ctx = AUDIO.ctx;
  const s = sourceBruit();
  const lp = ctx.createBiquadFilter();
  lp.type = "lowpass"; lp.frequency.value = filtre;
  const g = ctx.createGain();
  g.gain.setValueAtTime(vol, debut);
  g.gain.exponentialRampToValueAtTime(0.0001, debut + duree);
  s.connect(lp).connect(g).connect(AUDIO.effetsGain);
  s.start(debut); s.stop(debut + duree + 0.05);
}

/* ============================================================
   AMBIANCES DE SALLE (boucles continues, fondu enchaîné)
   ============================================================ */

/**
 * Lance l'ambiance sonore d'une salle (fondu depuis l'ambiance précédente).
 * @param {string} nom - palais-royal|imprimerie|tuileries|bastille|assemblee|accueil
 */
function ambiance(nom){
  if(!AUDIO.actif) return;
  if(!AUDIO.pret && !initAudio()) return;
  reveillerAudio();
  if(AUDIO.ambianceCourante === nom) return;

  arreterAmbiance(1.2);
  AUDIO.ambianceCourante = nom;

  const ctx = AUDIO.ctx;
  const t = ctx.currentTime;

  // Bus dédié à cette ambiance, pour pouvoir la faire disparaître en fondu
  const bus = ctx.createGain();
  bus.gain.setValueAtTime(0, t);
  bus.gain.linearRampToValueAtTime(1, t + 1.6);   // fondu d'entrée
  bus.connect(AUDIO.ambianceGain);

  const noeuds = { bus, sources:[], timers:[] };

  /* Les 5 escales du Tour du Monde.
     Chaque ambiance est SYNTHÉTISÉE par le navigateur : aucun fichier
     audio à télécharger, aucune dépendance réseau. */
  switch(nom){
    // Escale 1 — le Reform Club : pendule, murmures feutrés, feu de cheminée
    case "reform-club": ambianceAssemblee(noeuds); ambianceImprimerie(noeuds); break;
    // Escale 2 — l'isthme de Suez : vent chaud du désert, oiseaux lointains
    case "suez":        ambianceJardins(noeuds); break;
    // Escale 3 — la jungle indienne : vent dans la canopée, cris d'oiseaux
    case "inde":        ambianceJardins(noeuds); break;
    // Escale 4 — la tempête en mer de Chine : pluie battante et tonnerre
    case "mer-chine":   ambiancePluie(noeuds); break;
    // Escale 5 — l'observatoire de Greenwich : tic-tac et silence nocturne
    case "greenwich":   ambianceAssemblee(noeuds); break;
    case "accueil":     ambianceAccueil(noeuds); break;
    default: break;
  }

  AUDIO.noeudsAmbiance.push(noeuds);
}

/* ---- Arrêt en fondu de toutes les ambiances en cours ---- */
function arreterAmbiance(dureeFondu=1.0){
  if(!AUDIO.ctx) return;
  const t = AUDIO.ctx.currentTime;
  AUDIO.noeudsAmbiance.forEach(n=>{
    try{
      n.bus.gain.cancelScheduledValues(t);
      n.bus.gain.setValueAtTime(n.bus.gain.value, t);
      n.bus.gain.linearRampToValueAtTime(0, t + dureeFondu);
    }catch(e){}
    // Couper les sources et minuteries après le fondu
    setTimeout(()=>{
      n.sources.forEach(s=>{ try{ s.stop(); }catch(e){} });
      n.timers.forEach(id=>clearInterval(id));
      try{ n.bus.disconnect(); }catch(e){}
    }, dureeFondu*1000 + 120);
  });
  AUDIO.noeudsAmbiance = [];
  AUDIO.ambianceCourante = null;
}

/* ---- Salle 1 : pluie sur les pavés du Palais-Royal ---- */
function ambiancePluie(n){
  const ctx = AUDIO.ctx;
  // Nappe de pluie = bruit filtré passe-bande
  const s = sourceBruit();
  const bp = ctx.createBiquadFilter();
  bp.type = "bandpass"; bp.frequency.value = 1400; bp.Q.value = 0.5;
  const hp = ctx.createBiquadFilter();
  hp.type = "highpass"; hp.frequency.value = 500;
  const g = ctx.createGain(); g.gain.value = 0.30;
  s.connect(bp).connect(hp).connect(g).connect(n.bus);
  s.start();
  n.sources.push(s);

  // Ondulation lente de l'intensité (averse qui respire)
  const lfo = ctx.createOscillator();
  const lfoG = ctx.createGain();
  lfo.frequency.value = 0.09;
  lfoG.gain.value = 0.10;
  lfo.connect(lfoG).connect(g.gain);
  lfo.start();
  n.sources.push(lfo);

  // Gouttes isolées sur les pavés
  n.timers.push(setInterval(()=>{
    if(Math.random() < 0.55){
      const t = ctx.currentTime;
      const o = ctx.createOscillator();
      const og = ctx.createGain();
      o.type = "sine";
      o.frequency.setValueAtTime(900 + Math.random()*1400, t);
      o.frequency.exponentialRampToValueAtTime(320, t + 0.09);
      og.gain.setValueAtTime(0.05, t);
      og.gain.exponentialRampToValueAtTime(0.0001, t + 0.11);
      o.connect(og).connect(n.bus);
      o.start(t); o.stop(t + 0.14);
    }
  }, 620));

  // Tonnerre lointain occasionnel
  n.timers.push(setInterval(()=>{
    if(Math.random() < 0.22) tonnerre(n);
  }, 14000));
}

function tonnerre(n){
  const ctx = AUDIO.ctx;
  const t = ctx.currentTime;
  const s = sourceBruit();
  const lp = ctx.createBiquadFilter();
  lp.type = "lowpass"; lp.frequency.value = 160;
  const g = ctx.createGain();
  g.gain.setValueAtTime(0, t);
  g.gain.linearRampToValueAtTime(0.22, t + 0.35);
  g.gain.exponentialRampToValueAtTime(0.0001, t + 2.6);
  s.connect(lp).connect(g).connect(n.bus);
  s.start(t); s.stop(t + 2.8);
}

/* ---- Salle 2 : atelier d'imprimerie ---- */
function ambianceImprimerie(n){
  const ctx = AUDIO.ctx;
  // Ton de pièce sourd (cave voûtée)
  const s = sourceBruit();
  const lp = ctx.createBiquadFilter();
  lp.type = "lowpass"; lp.frequency.value = 260;
  const g = ctx.createGain(); g.gain.value = 0.22;
  s.connect(lp).connect(g).connect(n.bus);
  s.start();
  n.sources.push(s);

  // Crépitement de la bougie
  n.timers.push(setInterval(()=>{
    if(Math.random() < 0.4){
      const t = ctx.currentTime;
      const cs = sourceBruit();
      const bpc = ctx.createBiquadFilter();
      bpc.type = "bandpass"; bpc.frequency.value = 3000 + Math.random()*2000; bpc.Q.value = 6;
      const cg = ctx.createGain();
      cg.gain.setValueAtTime(0.035, t);
      cg.gain.exponentialRampToValueAtTime(0.0001, t + 0.05);
      cs.connect(bpc).connect(cg).connect(n.bus);
      cs.start(t); cs.stop(t + 0.07);
    }
  }, 420));

  // Presse à imprimer : grincement du levier puis impact du plateau
  n.timers.push(setInterval(()=>{
    const t = ctx.currentTime;
    // Grincement (glissando filtré)
    const o = ctx.createOscillator();
    const og = ctx.createGain();
    o.type = "sawtooth";
    o.frequency.setValueAtTime(120, t);
    o.frequency.linearRampToValueAtTime(180, t + 0.5);
    const lpg = ctx.createBiquadFilter();
    lpg.type = "lowpass"; lpg.frequency.value = 700;
    og.gain.setValueAtTime(0, t);
    og.gain.linearRampToValueAtTime(0.045, t + 0.2);
    og.gain.exponentialRampToValueAtTime(0.0001, t + 0.62);
    o.connect(lpg).connect(og).connect(n.bus);
    o.start(t); o.stop(t + 0.7);
    // Impact du plateau
    const t2 = t + 0.68;
    const is = sourceBruit();
    const ibp = ctx.createBiquadFilter();
    ibp.type = "lowpass"; ibp.frequency.value = 400;
    const ig = ctx.createGain();
    ig.gain.setValueAtTime(0.26, t2);
    ig.gain.exponentialRampToValueAtTime(0.0001, t2 + 0.28);
    is.connect(ibp).connect(ig).connect(n.bus);
    is.start(t2); is.stop(t2 + 0.32);
  }, 6500));
}

/* ---- Salle 3 : jardins des Tuileries ensoleillés ---- */
function ambianceJardins(n){
  const ctx = AUDIO.ctx;
  // Vent léger dans les feuillages
  const s = sourceBruit();
  const bp = ctx.createBiquadFilter();
  bp.type = "bandpass"; bp.frequency.value = 800; bp.Q.value = 0.4;
  const g = ctx.createGain(); g.gain.value = 0.16;
  s.connect(bp).connect(g).connect(n.bus);
  s.start();
  n.sources.push(s);

  const lfo = ctx.createOscillator();
  const lfoG = ctx.createGain();
  lfo.frequency.value = 0.13; lfoG.gain.value = 0.09;
  lfo.connect(lfoG).connect(g.gain);
  lfo.start();
  n.sources.push(lfo);

  // Chants d'oiseaux (petites modulations aiguës)
  n.timers.push(setInterval(()=>{
    if(Math.random() < 0.65) oiseau(n);
  }, 2600));
}

function oiseau(n){
  const ctx = AUDIO.ctx;
  const t = ctx.currentTime;
  const notes = 2 + Math.floor(Math.random()*3);
  const base = 2000 + Math.random()*1400;
  for(let i=0; i<notes; i++){
    const d = t + i*0.1;
    const o = ctx.createOscillator();
    const g = ctx.createGain();
    o.type = "sine";
    o.frequency.setValueAtTime(base, d);
    o.frequency.exponentialRampToValueAtTime(base*(1.25 + Math.random()*0.35), d + 0.055);
    g.gain.setValueAtTime(0, d);
    g.gain.linearRampToValueAtTime(0.045, d + 0.012);
    g.gain.exponentialRampToValueAtTime(0.0001, d + 0.09);
    o.connect(g).connect(n.bus);
    o.start(d); o.stop(d + 0.12);
  }
}

/* ---- Salle 4 : place de la Bastille, incendie et foule ---- */
function ambianceEmeute(n){
  const ctx = AUDIO.ctx;
  // Grondement de foule (bruit basse fréquence modulé)
  const s = sourceBruit();
  const lp = ctx.createBiquadFilter();
  lp.type = "lowpass"; lp.frequency.value = 420;
  const g = ctx.createGain(); g.gain.value = 0.26;
  s.connect(lp).connect(g).connect(n.bus);
  s.start();
  n.sources.push(s);

  const lfo = ctx.createOscillator();
  const lfoG = ctx.createGain();
  lfo.frequency.value = 0.22; lfoG.gain.value = 0.13;
  lfo.connect(lfoG).connect(g.gain);
  lfo.start();
  n.sources.push(lfo);

  // Crépitement du feu
  const f = sourceBruit();
  const fbp = ctx.createBiquadFilter();
  fbp.type = "bandpass"; fbp.frequency.value = 2400; fbp.Q.value = 0.8;
  const fg = ctx.createGain(); fg.gain.value = 0.10;
  f.connect(fbp).connect(fg).connect(n.bus);
  f.start();
  n.sources.push(f);

  // Détonations lointaines (canon)
  n.timers.push(setInterval(()=>{
    if(Math.random() < 0.35){
      const t = ctx.currentTime;
      const cs = sourceBruit();
      const clp = ctx.createBiquadFilter();
      clp.type = "lowpass"; clp.frequency.value = 130;
      const cg = ctx.createGain();
      cg.gain.setValueAtTime(0.30, t);
      cg.gain.exponentialRampToValueAtTime(0.0001, t + 1.5);
      cs.connect(clp).connect(cg).connect(n.bus);
      cs.start(t); cs.stop(t + 1.6);
    }
  }, 11000));

  // Cloche du tocsin
  n.timers.push(setInterval(()=>{
    if(Math.random() < 0.4) cloche(n);
  }, 17000));
}

function cloche(n){
  const ctx = AUDIO.ctx;
  const t = ctx.currentTime;
  // Une cloche = fondamentale + partiels inharmoniques
  [1, 2.76, 5.4, 8.9].forEach((mult, i)=>{
    const o = ctx.createOscillator();
    const g = ctx.createGain();
    o.type = "sine";
    o.frequency.value = 220 * mult;
    const vol = 0.09 / (i+1);
    g.gain.setValueAtTime(0, t);
    g.gain.linearRampToValueAtTime(vol, t + 0.008);
    g.gain.exponentialRampToValueAtTime(0.0001, t + 3.2);
    o.connect(g).connect(n.bus);
    o.start(t); o.stop(t + 3.4);
  });
}

/* ---- Salle 5 : Assemblée nationale ---- */
function ambianceAssemblee(n){
  const ctx = AUDIO.ctx;
  // Murmure de l'hémicycle
  const s = sourceBruit();
  const bp = ctx.createBiquadFilter();
  bp.type = "bandpass"; bp.frequency.value = 600; bp.Q.value = 0.6;
  const g = ctx.createGain(); g.gain.value = 0.19;
  s.connect(bp).connect(g).connect(n.bus);
  s.start();
  n.sources.push(s);

  const lfo = ctx.createOscillator();
  const lfoG = ctx.createGain();
  lfo.frequency.value = 0.17; lfoG.gain.value = 0.08;
  lfo.connect(lfoG).connect(g.gain);
  lfo.start();
  n.sources.push(lfo);

  // Balancier de la pendule (régulier, apaisant)
  n.timers.push(setInterval(()=>{
    const t = ctx.currentTime;
    const o = ctx.createOscillator();
    const og = ctx.createGain();
    o.type = "triangle";
    o.frequency.setValueAtTime(340, t);
    o.frequency.exponentialRampToValueAtTime(190, t + 0.05);
    og.gain.setValueAtTime(0.055, t);
    og.gain.exponentialRampToValueAtTime(0.0001, t + 0.09);
    o.connect(og).connect(n.bus);
    o.start(t); o.stop(t + 0.12);
  }, 2000));

  // Coup de maillet occasionnel
  n.timers.push(setInterval(()=>{
    if(Math.random() < 0.3){
      clac({debut: ctx.currentTime, vol:0.13, freq:220});
    }
  }, 13000));
}

/* ---- Écran d'accueil : nappe solennelle tricolore ---- */
function ambianceAccueil(n){
  const ctx = AUDIO.ctx;
  // Accord grave tenu (do - sol - mi), très discret
  [130.81, 196.00, 329.63].forEach((f, i)=>{
    const o = ctx.createOscillator();
    const g = ctx.createGain();
    o.type = "sine";
    o.frequency.value = f;
    g.gain.value = 0.035 / (i*0.5 + 1);
    o.connect(g).connect(n.bus);
    o.start();
    n.sources.push(o);
    // Léger vibrato pour éviter l'effet synthétique figé
    const v = ctx.createOscillator();
    const vg = ctx.createGain();
    v.frequency.value = 0.15 + i*0.05;
    vg.gain.value = 0.4;
    v.connect(vg).connect(o.frequency);
    v.start();
    n.sources.push(v);
  });
}

/* ============================================================
   RÉGLAGES (pilotés par le module enseignant)
   ============================================================ */
function setSonsActifs(actif){
  AUDIO.actif = !!actif;
  if(!AUDIO.masterGain) return;
  const t = AUDIO.ctx.currentTime;
  AUDIO.masterGain.gain.cancelScheduledValues(t);
  AUDIO.masterGain.gain.setValueAtTime(AUDIO.masterGain.gain.value, t);
  AUDIO.masterGain.gain.linearRampToValueAtTime(AUDIO.actif ? AUDIO.volume : 0, t + 0.3);
  if(!AUDIO.actif) arreterAmbiance(0.3);
}

function setVolumeSons(v){
  AUDIO.volume = Math.max(0, Math.min(1, v));
  if(!AUDIO.masterGain) return;
  const t = AUDIO.ctx.currentTime;
  AUDIO.masterGain.gain.cancelScheduledValues(t);
  AUDIO.masterGain.gain.linearRampToValueAtTime(AUDIO.actif ? AUDIO.volume : 0, t + 0.2);
}

/* ============================================================
   BRANCHEMENT AUTOMATIQUE SUR L'INTERFACE
   Aucune modification des énigmes n'est nécessaire :
   on observe le DOM et on écoute les clics.
   ============================================================ */
function brancherAudioInterface(){

  // 1) Premier geste utilisateur → démarrage du moteur audio
  const demarrer = ()=>{
    reveillerAudio();
    document.removeEventListener("pointerdown", demarrer);
    document.removeEventListener("keydown", demarrer);
  };
  document.addEventListener("pointerdown", demarrer);
  document.addEventListener("keydown", demarrer);

  // 2) Sons de clic sur tous les éléments interactifs (délégation globale)
  document.addEventListener("pointerdown", (e)=>{
    const cible = e.target.closest(
      ".btn, .hud-bouton, .opt-niveau, .lettre, .slot, .item-match, "+
      ".rebus-item, .portrait-choix, .etiquette, .case-plan, .fermer, "+
      ".bascule, .onglet-lecon, button"
    );
    if(cible && !cible.disabled) son("clic");
  }, true);

  // 3) Réussite / erreur : on observe les zones de feedback des énigmes
  const observateur = new MutationObserver((mutations)=>{
    mutations.forEach(m=>{
      if(m.type !== "attributes" || m.attributeName !== "class") return;
      const el = m.target;
      if(!el.classList || !el.classList.contains("feedback")) return;
      if(!el.classList.contains("show")) return;
      // Éviter de rejouer le son si la classe est réécrite à l'identique
      const etat = el.classList.contains("succes") ? "succes"
                 : el.classList.contains("erreur") ? "erreur"
                 : el.classList.contains("indice") ? "page" : null;
      if(!etat) return;
      if(el.dataset.dernierSon === etat) return;
      el.dataset.dernierSon = etat;
      son(etat);
      if(etat === "succes") setTimeout(()=>son("deverrouille"), 420);
      // Autoriser un nouveau son après un court délai
      setTimeout(()=>{ delete el.dataset.dernierSon; }, 800);
    });
  });
  observateur.observe(document.body, {
    subtree: true,
    attributes: true,
    attributeFilter: ["class"]
  });

  // 4) Ambiance de l'écran d'accueil
  document.addEventListener("pointerdown", function lancerAccueil(){
    const accueil = document.getElementById("ecran-accueil");
    if(accueil && accueil.classList.contains("actif")) ambiance("accueil");
    document.removeEventListener("pointerdown", lancerAccueil);
  });
}

if(document.readyState === "loading"){
  document.addEventListener("DOMContentLoaded", brancherAudioInterface);
}else{
  brancherAudioInterface();
}

/* ---- Exposition globale ---- */
window.AUDIO = AUDIO;
window.son = son;
window.ambiance = ambiance;
window.arreterAmbiance = arreterAmbiance;
window.setSonsActifs = setSonsActifs;
window.setVolumeSons = setVolumeSons;
window.initAudio = initAudio;
