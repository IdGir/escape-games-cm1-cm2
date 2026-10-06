/* ============================================================
   SONS — tous synthétisés (Web Audio), aucun fichier audio
   ------------------------------------------------------------
   Ambiances superposables : sousMarin (grondement filtré, bulles,
   sonar lointain), salon (orgue très doux), machines (bourdonnement
   électrique), carre / cabine (craquements de coque).
   Effets : succes, erreur, etincelle, alarme, sas, indice, page,
   orgue (accord), reaction-* (réactions du décor).
   Réglages : VML.reglage("sons") (oui/non), volume.
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
  };
  VML.couperAmbiances = function(){ Object.keys(ambiances).forEach(n => { ambiances[n].stop(); delete ambiances[n]; }); };
  VML.volumeSons = function(v){ if(init()) maitre.gain.value = Math.max(0, Math.min(1, v)); };
})();
