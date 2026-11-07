/* ============================================================
   SONS — tous synthétisés (Web Audio), aucun fichier audio
   ------------------------------------------------------------
   Ambiances superposables : sousMarin (grondement filtré, bulles,
   sonar lointain), salon (orgue très doux), machines (bourdonnement
   électrique), carre / cabine (craquements de coque).
   Effets : succes, erreur, etincelle, alarme, sas, indice, page,
   orgue (accord), reaction-* (réactions du décor).
   Ambiances ajoutées (novembre 2026, jeux hors Nautilus) : piece (silence habité), brise (souffle irrégulier,
   sans va-et-vient de ressac), oiseaux, murmure (foule lointaine), crepitement (feu, chandelle), atelier (tocs,
   outils), horloge, mijotage (bulles), ruisseau (eau vive), cloches, pluie.
   MUSIQUE D'AMBIANCE générée (Web Audio, aucun fichier) : un style par jeu, choisi dans js/jeu-config.js
   (clé "musique" : "medieval", "abbaye", "renaissance", "baroque", "solennel", "sciences", "nature", "atelier",
   ou {"style": "...", "racine": Hz}). Réglages : VML.reglage("musiqueFond") (oui/non), ("volumeFond") (0 à 1).
   Fichiers audio facultatifs (libres de droits, déposés par l'enseignant) :
     assets/audio/ambiances/<décor>.mp3   boucle d'ambiance d'un décor (remplace l'ambiance synthétisée) ;
     assets/audio/musiques/<cinématique>.mp3   musique d'une cinématique : intro, fin, transition-e<N>, fin-e<N>,
       sinon musiques/transition.mp3, musiques/fin-salle.mp3, musiques/intro.mp3, musiques/fin.mp3 (repli par famille).
   Sans fichier, les ambiances synthétisées restent. Réglages : VML.reglage("sons") (oui/non), volume,
   VML.reglage("volumeMusique") et ("volumeAmbiance") (0 à 1).
   ============================================================ */
var VML = window.VML || (window.VML = {});

(function(){
  let ctx = null, maitre = null, bruitBuf = null;
  const ambiances = {};      // nom → {stop()}

  function init(){
    if(ctx) return ctx;
    const AC = window.AudioContext || window.webkitAudioContext;
    if(!AC) return null;
    try{ ctx = new AC(); }catch(e){ return null; }
    maitre = ctx.createGain();
    maitre.gain.value = 0.8;
    maitre.connect(ctx.destination);
    const n = ctx.sampleRate * 2;
    bruitBuf = ctx.createBuffer(1, n, ctx.sampleRate);
    const d = bruitBuf.getChannelData(0);
    for(let i = 0; i < n; i++) d[i] = Math.random() * 2 - 1;
    return ctx;
  }
  const actif = () => !(VML.reglage && VML.reglage("sons") === false);
  VML.reveillerSon = function(){ const c = init(); if(c && c.state === "suspended") c.resume(); };
  ["click", "keydown", "touchstart"].forEach(ev => document.addEventListener(ev, () => VML.reveillerSon(), { once: false, passive: true }));

  function bruit(){ const s = ctx.createBufferSource(); s.buffer = bruitBuf; s.loop = true; return s; }
  function osc(freq, type, debut, duree, vol, glisse){
    const o = ctx.createOscillator(), g = ctx.createGain();
    o.type = type || "sine"; o.frequency.setValueAtTime(freq, debut);
    if(glisse) o.frequency.exponentialRampToValueAtTime(glisse, debut + duree);
    g.gain.setValueAtTime(0.0001, debut);
    g.gain.exponentialRampToValueAtTime(vol, debut + 0.02);
    g.gain.exponentialRampToValueAtTime(0.0001, debut + duree);
    o.connect(g); g.connect(maitre); o.start(debut); o.stop(debut + duree + 0.05);
  }
  function souffle(debut, duree, vol, freq, q){
    const s = bruit(), f = ctx.createBiquadFilter(), g = ctx.createGain();
    f.type = "bandpass"; f.frequency.value = freq || 1500; f.Q.value = q || 1;
    g.gain.setValueAtTime(0.0001, debut); g.gain.exponentialRampToValueAtTime(vol, debut + 0.01);
    g.gain.exponentialRampToValueAtTime(0.0001, debut + duree);
    s.connect(f); f.connect(g); g.connect(maitre); s.start(debut); s.stop(debut + duree + 0.05);
  }
  function accord(notes, debut, duree, vol){
    notes.forEach((f, i) => {
      [1, 2, 3].forEach(h => osc(f * h, h === 1 ? "triangle" : "sine", debut + i * 0.03, duree, vol / (h * 1.6)));
    });
  }

  VML.son = function(nom){
    if(!actif() || !init()) return;
    const t = ctx.currentTime + 0.01;
    switch(nom){
      case "succes": [523, 659, 784, 1047].forEach((f, i) => osc(f, "triangle", t + i * 0.09, 0.5, 0.12)); break;
      case "erreur": osc(180, "sawtooth", t, 0.35, 0.08, 110); souffle(t, 0.25, 0.05, 400, 2); break;
      case "etincelle": for(let i = 0; i < 6; i++) souffle(t + Math.random() * 0.25, 0.04, 0.05, 3000 + Math.random() * 3000, 4); break;
      case "alarme": for(let i = 0; i < 3; i++){ osc(660, "square", t + i * 0.6, 0.28, 0.05); osc(520, "square", t + i * 0.6 + 0.3, 0.28, 0.05); } break;
      case "sas": osc(90, "sine", t, 1.2, 0.2, 60); souffle(t, 1.4, 0.08, 600, 0.7); break;
      case "indice": osc(880, "sine", t, 0.25, 0.08); osc(1320, "sine", t + 0.12, 0.3, 0.06); break;
      case "page": souffle(t, 0.18, 0.06, 2500, 0.8); break;
      case "sonar": osc(1180, "sine", t, 1.6, 0.07); osc(1180, "sine", t + 1.8, 1.2, 0.025); break;
      case "orgue": accord([196, 247, 294, 392], t, 2.6, 0.06); break;
      case "fragment": accord([262, 330, 392, 523], t, 3, 0.07); break;
      case "reaction-cable-neuf": osc(300, "triangle", t, 0.2, 0.08, 600); break;
      case "reaction-lumiere": osc(60, "sawtooth", t, 1.5, 0.05, 120); osc(120, "sine", t, 1.5, 0.06); souffle(t, 0.3, 0.06, 4000, 3); break;
      case "reaction-aiguilles": for(let i = 0; i < 8; i++) souffle(t + i * 0.09, 0.03, 0.08, 5000, 6); break;
      case "reaction-hublots": souffle(t, 2.2, 0.12, 300, 0.5); osc(70, "sawtooth", t, 2, 0.05, 50); setTimeout(() => VML.son("sonar"), 1600); break;
      case "clic": souffle(t, 0.03, 0.05, 3000, 5); break;
      case "fil": osc(1400, "sine", t, 0.08, 0.05); break;
      case "courtcircuit": souffle(t, 0.5, 0.2, 2500, 0.6); osc(90, "sawtooth", t, 0.4, 0.1, 40); break;
    }
  };

  /** Bruit filtré constant et très discret (fond de pièce, feu, pluie…). */
  function nappe(type, freq, q, vol){
    const s = bruit(), f = ctx.createBiquadFilter(), g = ctx.createGain();
    f.type = type; f.frequency.value = freq; f.Q.value = q || 0.7; g.gain.value = 0.0001;
    g.gain.setTargetAtTime(vol, ctx.currentTime, 0.8);
    s.connect(f); f.connect(g); g.connect(maitre); s.start();
    return { stop(){ try{ g.gain.setTargetAtTime(0, ctx.currentTime, 0.4); s.stop(ctx.currentTime + 1.8); }catch(e){} } };
  }
  /** Appelle fn(t) à des intervalles irréguliers (jamais périodiques : c'est ce qui évite l'effet « vague »). */
  function hasard(minMs, maxMs, fn){
    let id = null, vivant = true;
    const suite = () => {
      if(!vivant) return;
      if(actif() && ctx && ctx.state === "running") fn(ctx.currentTime + 0.02);
      id = setTimeout(suite, minMs + Math.random() * (maxMs - minMs));
    };
    id = setTimeout(suite, 200 + Math.random() * minMs);
    return { stop(){ vivant = false; clearTimeout(id); } };
  }

  /* ---------------- Ambiances ---------------- */
  const FABRIQUES = {
    sousMarin(){
      const s = bruit(), f = ctx.createBiquadFilter(), g = ctx.createGain(), lfo = ctx.createOscillator(), lg = ctx.createGain();
      f.type = "lowpass"; f.frequency.value = 180; g.gain.value = 0.18;
      lfo.frequency.value = 0.07; lg.gain.value = 0.07; lfo.connect(lg); lg.connect(g.gain);
      s.connect(f); f.connect(g); g.connect(maitre); s.start(); lfo.start();
      const id = setInterval(() => {
        if(!actif()) return;
        const t = ctx.currentTime;
        if(Math.random() < 0.5) for(let i = 0; i < 3; i++) osc(400 + Math.random() * 500, "sine", t + i * 0.08, 0.09, 0.025, 900 + Math.random() * 400);
        if(Math.random() < 0.08) VML.son("sonar");
      }, 2600);
      return { stop(){ clearInterval(id); try{ g.gain.setTargetAtTime(0, ctx.currentTime, 0.4); s.stop(ctx.currentTime + 1.5); lfo.stop(ctx.currentTime + 1.5); }catch(e){} } };
    },
    machines(){
      const o1 = ctx.createOscillator(), o2 = ctx.createOscillator(), g = ctx.createGain(), f = ctx.createBiquadFilter();
      o1.type = "sawtooth"; o1.frequency.value = 50; o2.type = "sine"; o2.frequency.value = 100;
      f.type = "lowpass"; f.frequency.value = 260; g.gain.value = 0.035;
      o1.connect(f); o2.connect(f); f.connect(g); g.connect(maitre); o1.start(); o2.start();
      return { stop(){ try{ g.gain.setTargetAtTime(0, ctx.currentTime, 0.3); o1.stop(ctx.currentTime + 1.2); o2.stop(ctx.currentTime + 1.2); }catch(e){} } };
    },
    salon(){
      const id = setInterval(() => { if(actif() && Math.random() < 0.25) accord([131, 165, 196], ctx.currentTime, 3.5, 0.02); }, 7000);
      return { stop(){ clearInterval(id); } };
    },
    vent(){
      const s = bruit(), f = ctx.createBiquadFilter(), g = ctx.createGain(), lfo = ctx.createOscillator(), lg = ctx.createGain();
      f.type = "bandpass"; f.frequency.value = 500; f.Q.value = 0.6; g.gain.value = 0.05;
      lfo.frequency.value = 0.12; lg.gain.value = 300; lfo.connect(lg); lg.connect(f.frequency);
      s.connect(f); f.connect(g); g.connect(maitre); s.start(); lfo.start();
      return { stop(){ try{ g.gain.setTargetAtTime(0, ctx.currentTime, 0.4); s.stop(ctx.currentTime + 1.5); lfo.stop(ctx.currentTime + 1.5); }catch(e){} } };
    },
    vagues(){
      const id = setInterval(() => { if(actif()){ const t = ctx.currentTime; souffle(t, 2.2, 0.05, 350, 0.5); } }, 4200);
      return { stop(){ clearInterval(id); } };
    },
    vapeur(){
      const id = setInterval(() => { if(actif() && Math.random() < 0.5){ const t = ctx.currentTime; souffle(t, 0.9, 0.04, 2600, 1.2); osc(55, "sawtooth", t, 0.5, 0.02, 45); } }, 2300);
      return { stop(){ clearInterval(id); } };
    },
    glace(){
      const id = setInterval(() => { if(actif() && Math.random() < 0.3){ const t = ctx.currentTime; osc(1800 + Math.random() * 900, "sine", t, 0.4, 0.015, 900); osc(90, "triangle", t + 0.2, 0.8, 0.03, 60); } }, 3500);
      return { stop(){ clearInterval(id); } };
    },

    /* ---- Ambiances ajoutées : sobres, sans va-et-vient régulier (donc jamais de ressac) ---- */
    piece(){ return nappe("lowpass", 150, 0.5, 0.03); },
    brise(){
      const s = bruit(), f = ctx.createBiquadFilter(), g = ctx.createGain();
      f.type = "bandpass"; f.frequency.value = 650; f.Q.value = 0.45; g.gain.value = 0.012;
      s.connect(f); f.connect(g); g.connect(maitre); s.start();
      const r = hasard(4500, 11000, t => {          // rafales irrégulières : montée lente, retombée plus lente
        f.frequency.setTargetAtTime(420 + Math.random() * 520, t, 1.4);
        g.gain.setTargetAtTime(0.03 + Math.random() * 0.05, t, 1.6);
        g.gain.setTargetAtTime(0.012, t + 2.4 + Math.random() * 1.5, 2.4);
      });
      return { stop(){ r.stop(); try{ g.gain.setTargetAtTime(0, ctx.currentTime, 0.4); s.stop(ctx.currentTime + 1.8); }catch(e){} } };
    },
    oiseaux(){
      return hasard(2200, 7500, t => {
        const n = 2 + Math.floor(Math.random() * 3), base = 2300 + Math.random() * 1900, v = Math.random() < 0.5;
        for(let i = 0; i < n; i++) osc(base * (v ? 1 + i * 0.06 : 1), "sine", t + i * (v ? 0.11 : 0.16), 0.08, 0.045, base * (v ? 1.3 : 0.8));
      });
    },
    murmure(){
      const s = bruit(), f = ctx.createBiquadFilter(), f2 = ctx.createBiquadFilter(), g = ctx.createGain();
      f.type = "bandpass"; f.frequency.value = 500; f.Q.value = 1.4; f2.type = "lowpass"; f2.frequency.value = 1400; g.gain.value = 0.0001;
      s.connect(f); f.connect(f2); f2.connect(g); g.connect(maitre); s.start();
      const r = hasard(140, 420, t => {              // « syllabes » : petites bouffées de voix lointaines
        f.frequency.setTargetAtTime(280 + Math.random() * 700, t, 0.05);
        g.gain.setTargetAtTime(0.02 + Math.random() * 0.09, t, 0.06);
      });
      return { stop(){ r.stop(); try{ g.gain.setTargetAtTime(0, ctx.currentTime, 0.4); s.stop(ctx.currentTime + 1.8); }catch(e){} } };
    },
    crepitement(){
      const base = nappe("lowpass", 110, 0.5, 0.025);
      const r = hasard(120, 1000, t => souffle(t, 0.02 + Math.random() * 0.03, 0.04 + Math.random() * 0.08, 1500 + Math.random() * 3200, 3));
      return { stop(){ r.stop(); base.stop(); } };
    },
    atelier(){
      const base = nappe("lowpass", 150, 0.5, 0.02);
      const r = hasard(1300, 4600, t => {
        const f = 170 + Math.random() * 140;
        osc(f, "triangle", t, 0.07, 0.08, f * 0.5); souffle(t, 0.04, 0.07, 1800, 3);
        if(Math.random() < 0.35){ osc(f * 1.1, "triangle", t + 0.16, 0.07, 0.06, f * 0.55); souffle(t + 0.16, 0.04, 0.05, 2000, 3); }
        if(Math.random() < 0.12) souffle(t + 0.4, 0.55, 0.03, 3400, 1);
      });
      return { stop(){ r.stop(); base.stop(); } };
    },
    horloge(){
      let alt = false;
      const id = setInterval(() => {
        if(!actif() || ctx.state !== "running") return;
        const t = ctx.currentTime + 0.01; alt = !alt;
        souffle(t, 0.02, 0.07, alt ? 2600 : 2100, 8); osc(alt ? 1700 : 1400, "sine", t, 0.025, 0.025);
      }, 1000);
      return { stop(){ clearInterval(id); } };
    },
    mijotage(){
      const base = nappe("lowpass", 230, 0.6, 0.025);
      const r = hasard(250, 1200, t => { const f = 260 + Math.random() * 380; osc(f, "sine", t, 0.07, 0.05, f * 2); });
      return { stop(){ r.stop(); base.stop(); } };
    },
    ruisseau(){
      const s = bruit(), f = ctx.createBiquadFilter(), g = ctx.createGain();
      f.type = "bandpass"; f.frequency.value = 1900; f.Q.value = 0.8; g.gain.value = 0.03;
      s.connect(f); f.connect(g); g.connect(maitre); s.start();
      const r = hasard(60, 210, t => {               // clapotis rapide et irrégulier (jamais de balancement lent)
        f.frequency.setTargetAtTime(1200 + Math.random() * 1700, t, 0.04);
        g.gain.setTargetAtTime(0.02 + Math.random() * 0.03, t, 0.04);
      });
      return { stop(){ r.stop(); try{ g.gain.setTargetAtTime(0, ctx.currentTime, 0.4); s.stop(ctx.currentTime + 1.8); }catch(e){} } };
    },
    cloches(){
      return hasard(16000, 34000, t => {
        const f = Math.random() < 0.5 ? 330 : 392, coups = 1 + Math.floor(Math.random() * 3);
        for(let c = 0; c < coups; c++) [[1, 0.06], [2.76, 0.028], [5.4, 0.014]].forEach(([k, v]) => osc(f * k, "sine", t + c * 2, 3.5, v));
      });
    },
    pluie(){
      const base = nappe("bandpass", 3200, 0.35, 0.04);
      const r = hasard(90, 500, t => souffle(t, 0.03, 0.04, 2500 + Math.random() * 3000, 4));
      return { stop(){ r.stop(); base.stop(); } };
    },
    carre(){ return FABRIQUES.coque(); },
    cabine(){ return FABRIQUES.coque(); },
    coque(){
      const id = setInterval(() => { if(actif() && Math.random() < 0.35){ const t = ctx.currentTime; osc(70 + Math.random() * 40, "triangle", t, 0.6, 0.03, 50); } }, 5000);
      return { stop(){ clearInterval(id); } };
    }
  };

  VML.ambianceDecor = function(noms){
    if(!init()) return;
    const voulues = actif() ? (noms || []) : [];
    Object.keys(ambiances).forEach(n => { if(!voulues.includes(n)){ ambiances[n].stop(); delete ambiances[n]; } });
    voulues.forEach(n => { if(!ambiances[n] && FABRIQUES[n]) ambiances[n] = FABRIQUES[n](); });
    if(VML.majMusiqueFond) VML.majMusiqueFond();
  };
  VML.couperAmbiances = function(){ Object.keys(ambiances).forEach(n => { ambiances[n].stop(); delete ambiances[n]; }); };
  VML.volumeSons = function(v){ if(init()) maitre.gain.value = Math.max(0, Math.min(1, v)); };

  /* ---------------- Musique d'ambiance générée ----------------
     Une boucle lente qui ne se répète jamais à l'identique : nappe d'accords tenus, bourdon facultatif et mélodie
     qui se promène sur la gamme du style. Un style par jeu (clé "musique" de js/jeu-config.js).               */
  const STYLES = {
    medieval:    { racine: 146.83, gamme: [0, 2, 3, 5, 7, 9, 10], tempo: 0.72, mesure: 8, voix: "flute",    bourdon: true,  densite: 0.45, accords: [[0, 4], [-2, 2], [-1, 3], [0, 4]] },
    abbaye:      { racine: 110,    gamme: [0, 2, 3, 5, 7, 9, 10], tempo: 1.1,  mesure: 8, voix: "flute",    bourdon: true,  densite: 0.28, accords: [[0, 4], [-3, 1]] },
    renaissance: { racine: 196,    gamme: [0, 2, 4, 5, 7, 9, 10], tempo: 0.5,  mesure: 12, voix: "luth",    bourdon: false, densite: 0.55, accords: [[0, 2, 4], [-3, -1, 1], [-2, 0, 2], [0, 2, 4]] },
    baroque:     { racine: 196,    gamme: [0, 2, 4, 5, 7, 9, 11], tempo: 0.4,  mesure: 16, voix: "clavecin", bourdon: false, densite: 0.8,  arpege: true, accords: [[0, 2, 4], [-3, -1, 1], [-2, 0, 2], [-4, -2, 0]] },
    solennel:    { racine: 130.81, gamme: [0, 2, 4, 5, 7, 9, 11], tempo: 1.0,  mesure: 8, voix: "harpe",    bourdon: true,  densite: 0.35, accords: [[0, 2, 4], [-2, 0, 2], [-3, -1, 1], [0, 2, 4]] },
    sciences:    { racine: 261.63, gamme: [0, 2, 4, 7, 9],           tempo: 0.55, mesure: 8, voix: "marimba",  bourdon: false, densite: 0.5,  accords: [[0, 2], [-1, 1], [-2, 0]] },
    nature:      { racine: 196,    gamme: [0, 2, 4, 7, 9],           tempo: 0.7,  mesure: 8, voix: "harpe",    bourdon: false, densite: 0.4,  accords: [[0, 2, 4], [-1, 1, 3]] },
    atelier:     { racine: 220,    gamme: [0, 3, 5, 7, 10],          tempo: 0.45, mesure: 8, voix: "marimba",  bourdon: false, densite: 0.6,  accords: [[0, 2], [-2, 0]] }
  };
  let fond = null;           // {cle, bus, id, noeuds, etat}
  let sourdine = false;      // vrai pendant une cinématique avec fichier musical
  const confMusique = () => { const m = (window.VML_JEU || {}).musique; return !m ? null : typeof m === "string" ? { style: m } : m; };
  const voulueFond = () => actif() && !(VML.reglage && VML.reglage("musiqueFond") === false);
  const gainFond = () => Math.max(0, Math.min(1, (VML.reglage && typeof VML.reglage("volumeFond") === "number") ? VML.reglage("volumeFond") : 0.6)) * 1.3 * (sourdine ? 0.25 : 1);
  const hzDegre = (st, deg, decal) => { const n = st.gamme.length, o = Math.floor(deg / n), i = ((deg % n) + n) % n; return (st.racine) * Math.pow(2, (st.gamme[i] + 12 * o + (decal || 0)) / 12); };

  /** Une note de la voix du style, branchée sur le bus de la musique. */
  function noteMusique(voix, f, t, v, bus){
    const env = (g, att, dec, pic) => { g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(pic, t + att); g.gain.exponentialRampToValueAtTime(0.0001, t + att + dec); };
    const note = (type, fr, att, dec, pic, filtre) => {
      const o = ctx.createOscillator(), g = ctx.createGain(); let sortie = g;
      o.type = type; o.frequency.value = fr; env(g, att, dec, pic);
      o.connect(g);
      if(filtre){ const lp = ctx.createBiquadFilter(); lp.type = "lowpass"; lp.frequency.value = filtre; g.connect(lp); sortie = lp; }
      sortie.connect(bus); o.start(t); o.stop(t + att + dec + 0.1);
      return o;
    };
    if(voix === "flute"){
      const o = note("sine", f, 0.14, 1.5, v), vib = ctx.createOscillator(), vg = ctx.createGain();
      vib.frequency.value = 5; vg.gain.value = f * 0.004; vib.connect(vg); vg.connect(o.frequency); vib.start(t + 0.25); vib.stop(t + 1.7);
      note("sine", f * 2, 0.14, 1.1, v * 0.12);
    }else if(voix === "luth"){
      note("triangle", f, 0.006, 1.5, v, 2400); note("sine", f * 2, 0.006, 0.8, v * 0.3);
    }else if(voix === "clavecin"){
      note("sawtooth", f, 0.004, 0.8, v * 0.55, 3000); note("sine", f * 2, 0.004, 0.5, v * 0.3);
      souffle2(t, 0.012, v * 0.7, bus);
    }else if(voix === "harpe"){
      note("sine", f, 0.005, 2.4, v); note("triangle", f * 2, 0.005, 1.4, v * 0.22); note("sine", f * 3, 0.005, 0.9, v * 0.08);
    }else{ // marimba
      note("sine", f, 0.004, 0.75, v); note("sine", f * 4, 0.004, 0.14, v * 0.22);
    }
  }
  function souffle2(t, duree, vol, bus){
    const s = bruit(), f = ctx.createBiquadFilter(), g = ctx.createGain();
    f.type = "bandpass"; f.frequency.value = 2600; f.Q.value = 2;
    g.gain.setValueAtTime(vol, t); g.gain.exponentialRampToValueAtTime(0.0001, t + duree);
    s.connect(f); f.connect(g); g.connect(bus); s.start(t); s.stop(t + duree + 0.05);
  }
  /** Nappe d'accord tenu (deux oscillateurs légèrement désaccordés par note). */
  function nappeAccord(st, degres, t, duree, bus){
    degres.forEach(d => {
      [-4, 4].forEach(cents => {
        const o = ctx.createOscillator(), g = ctx.createGain(), lp = ctx.createBiquadFilter();
        o.type = "triangle"; o.frequency.value = hzDegre(st, d, 0); o.detune.value = cents;
        lp.type = "lowpass"; lp.frequency.value = 900;
        g.gain.setValueAtTime(0.0001, t); g.gain.linearRampToValueAtTime(0.011, t + Math.min(2.5, duree * 0.4));
        g.gain.setValueAtTime(0.011, t + duree); g.gain.linearRampToValueAtTime(0.0001, t + duree + 3);
        o.connect(g); g.connect(lp); lp.connect(bus); o.start(t); o.stop(t + duree + 3.1);
      });
    });
  }
  function pasMusique(c, e, t){
    const st = c.st, nb = st.gamme.length;
    if(e.pas % st.mesure === 0){
      e.accord = st.accords[(e.pas / st.mesure) % st.accords.length];
      nappeAccord(st, e.accord, t, st.mesure * st.tempo, c.bus);
    }
    const pos = e.pas % st.mesure, v = st.voix === "flute" ? 0.06 : 0.05;
    if(st.arpege){
      const d = e.accord[pos % e.accord.length] + nb * (1 + (Math.floor(pos / e.accord.length) % 2));
      if(Math.random() < st.densite) noteMusique(st.voix, hzDegre(st, d), t, v, c.bus);
      return;
    }
    if(Math.random() > st.densite || (pos === st.mesure - 1 && Math.random() < 0.6)) return;
    // marche aléatoire sur la gamme, attirée par les notes de l'accord en cours
    if(Math.random() < 0.45){
      const cibles = e.accord.map(d => d + nb * (1 + (Math.random() < 0.3 ? 1 : 0)));
      e.deg = cibles.reduce((a, b) => Math.abs(b - e.deg) < Math.abs(a - e.deg) ? b : a, cibles[0]);
    }else{
      e.deg += [-2, -1, -1, 1, 1, 2][Math.floor(Math.random() * 6)];
    }
    e.deg = Math.max(nb - 3, Math.min(nb * 2 + 1, e.deg));
    noteMusique(st.voix, hzDegre(st, e.deg), t, v, c.bus);
  }
  function demarrerFond(){
    const conf = confMusique();
    if(!conf || !voulueFond() || !init()) return;
    const style = conf.style, cle = style + "|" + (conf.racine || "");
    if(fond && fond.cle === cle) return;
    arreterFond();
    const base = STYLES[style]; if(!base) return;
    const st = Object.assign({}, base, conf.racine ? { racine: conf.racine } : {});
    const bus = ctx.createGain(); bus.gain.value = 0.0001; bus.gain.setTargetAtTime(gainFond(), ctx.currentTime, 2.5); bus.connect(maitre);
    const c = { cle, st, bus, noeuds: [], etat: { pas: 0, deg: st.gamme.length + 2, accord: st.accords[0], prochain: ctx.currentTime + 1.2 } };
    if(st.bourdon){
      [[0.5, 0.016], [0.75, 0.008]].forEach(([k, v]) => {
        const o = ctx.createOscillator(), g = ctx.createGain(); o.type = "sine"; o.frequency.value = st.racine * k; g.gain.value = v;
        o.connect(g); g.connect(bus); o.start(); c.noeuds.push(o);
      });
    }
    c.id = setInterval(() => {
      if(!voulueFond()){ arreterFond(); return; }
      if(ctx.state !== "running"){ c.etat.prochain = ctx.currentTime + 0.5; return; }
      while(c.etat.prochain < ctx.currentTime + 1.2){
        pasMusique(c, c.etat, c.etat.prochain);
        c.etat.prochain += st.tempo * (1 + (Math.random() * 0.05 - 0.025)); c.etat.pas++;
      }
    }, 400);
    fond = c;
  }
  function arreterFond(){
    if(!fond) return;
    const c = fond; fond = null; clearInterval(c.id);
    try{ c.bus.gain.setTargetAtTime(0, ctx.currentTime, 0.6); c.noeuds.forEach(o => o.stop(ctx.currentTime + 3)); setTimeout(() => { try{ c.bus.disconnect(); }catch(e){} }, 3500); }catch(e){}
  }
  /** Appelée par les réglages (case « musique d'ambiance », volume, sons coupés ou rétablis). */
  VML.majMusiqueFond = function(){
    if(!ctx && !voulueFond()) return;
    if(!voulueFond()) return arreterFond();
    if(fond){ try{ fond.bus.gain.setTargetAtTime(gainFond(), ctx.currentTime, 0.3); }catch(e){} } else demarrerFond();
  };
  VML.arreterMusiqueFond = arreterFond;
  /** Pour les tests hors ligne : planifie d'un coup la musique d'un style sur la durée donnée (contexte OfflineAudioContext). */
  VML._rendreMusique = function(style, secondes, racine){
    if(!init()) return false;
    const base = STYLES[style]; if(!base) return false;
    const st = Object.assign({}, base, racine ? { racine } : {});
    const bus = ctx.createGain(); bus.gain.value = 0.5; bus.connect(maitre);
    if(st.bourdon) [[0.5, 0.016], [0.75, 0.008]].forEach(([k, v]) => { const o = ctx.createOscillator(), g = ctx.createGain(); o.type = "sine"; o.frequency.value = st.racine * k; g.gain.value = v; o.connect(g); g.connect(bus); o.start(0); o.stop(secondes); });
    const c = { st, bus }, e = { pas: 0, deg: st.gamme.length + 2, accord: st.accords[0] };
    for(let t = 0.3; t < secondes - 3; t += st.tempo, e.pas++) pasMusique(c, e, t);
    return true;
  };

  /* ---------- Fichiers audio : ambiances de décor et musiques de cinématique ---------- */
  const absents = {};
  let ambFichier = null, musiqueEnCours = null;
  const vol = (nom, defaut) => { const v = VML.reglage ? VML.reglage(nom) : null; return typeof v === "number" ? Math.max(0, Math.min(1, v)) : defaut; };
  const rapide = () => !!window.VML_RAPIDE || typeof Audio === "undefined";
  function fondu(a, vers, ms, fin){
    const depart = a.volume, t0 = Date.now();
    clearInterval(a._f);
    a._f = setInterval(() => {
      const k = Math.min(1, (Date.now() - t0) / Math.max(1, ms));
      a.volume = Math.max(0, Math.min(1, depart + (vers - depart) * k));
      if(k >= 1){ clearInterval(a._f); if(fin) fin(); }
    }, 40);
  }
  /** Joue le premier fichier existant de la liste ; rend l'élément audio, ou null si aucun. */
  function essayer(urls, boucle, volume, quand){
    const url = urls.find(u => !absents[u]);
    if(!url){ if(quand) quand(null); return null; }
    const a = new Audio(url);
    a.loop = boucle; a.volume = 0; a.preload = "auto";
    a.onerror = () => { absents[url] = true; a._mort = true; const suite = essayer(urls, boucle, volume, quand); if(a._relais) a._relais(suite); };
    const lancement = a.play();
    if(lancement && lancement.then) lancement.then(() => { if(!a._mort){ fondu(a, volume, 1200); if(quand) quand(a); } }).catch(() => { if(!a._mort && quand) quand(null); });
    return a;
  }
  VML.urlsMusique = id => {
    const fam = /^transition/.test(id) ? "transition" : /^fin-e/.test(id) ? "fin-salle" : id;
    return ["assets/audio/musiques/" + id + ".mp3"].concat(fam !== id ? ["assets/audio/musiques/" + fam + ".mp3"] : []);
  };
  VML.urlAmbiance = decor => "assets/audio/ambiances/" + decor + ".mp3";
  VML.ambianceFichier = function(decor){
    if(rapide() || !actif() || !decor) return;
    if(ambFichier && ambFichier.decor === decor) return;
    if(ambFichier){ const vieux = ambFichier.a; fondu(vieux, 0, 800, () => vieux.pause()); ambFichier = null; }
    const a = essayer([VML.urlAmbiance(decor)], true, vol("volumeAmbiance", 0.35), ok => { if(ok && VML.couperAmbiances) VML.couperAmbiances(); });
    if(a) ambFichier = { decor, a };
  };
  VML.musique = function(id){
    if(rapide() || !actif() || !id) return;
    VML.arreterMusique(300);
    if(ambFichier) fondu(ambFichier.a, vol("volumeAmbiance", 0.35) * 0.3, 600);
    const m = { id, a: essayer(VML.urlsMusique(id), false, vol("volumeMusique", 0.5), ok => { if(ok){ sourdine = true; VML.majMusiqueFond(); } }) };
    musiqueEnCours = m;
    if(m.a) m.a.addEventListener("ended", () => { if(musiqueEnCours === m) VML.arreterMusique(300); });
  };
  VML.arreterMusique = function(ms){
    const m = musiqueEnCours; musiqueEnCours = null;
    if(m && m.a){ const a = m.a; a._mort = true; fondu(a, 0, ms || 800, () => a.pause()); }
    if(ambFichier) fondu(ambFichier.a, vol("volumeAmbiance", 0.35), ms || 800);
    if(sourdine){ sourdine = false; if(VML.majMusiqueFond) VML.majMusiqueFond(); }
  };
})();
