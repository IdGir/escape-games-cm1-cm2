/* ============================================================
   SCÈNE — décor peint + calques d'effets animés + zones cliquables
   ------------------------------------------------------------
   Contrat de remplacement (cahier des charges § 7.5) :
     1. fichier déposé  assets/images/decors/<id>.webp | .jpg | .png
     2. image de référence de l'enseignant (decors-fx.json : « reference »)
     3. décor dessiné en SVG (js/decors-secours.js) — toujours disponible
   Le premier trouvé gagne. Zones et effets sont en % de l'image :
   le « cadre » qui les porte a exactement le format de l'image et
   la recouvre (object-fit: cover calculé à la main), donc une image
   16:9, 3:2 ou 4:3 fonctionne sans retouche.
   Paramètres d'adresse : ?secours=1 force le décor dessiné ;
   ?reference=0 ignore les images de référence.
   ============================================================ */
var VML = window.VML || (window.VML = {});

VML.EXT_DECOR = [".webp", ".jpg", ".png"];
VML.sourcesDecor = {};          // id → {type, url, ratio}

VML.sonderImage = function(url, delai){
  return new Promise(res => {
    const img = new Image();
    let fini = false;
    const t = setTimeout(() => { if(!fini){ fini = true; res(null); } }, delai || 3000);
    img.onload = () => { if(fini) return; fini = true; clearTimeout(t); res({ url, ratio: (img.naturalWidth && img.naturalHeight) ? img.naturalWidth / img.naturalHeight : 16/9 }); };
    img.onerror = () => { if(fini) return; fini = true; clearTimeout(t); res(null); };
    img.src = url;
  });
};

VML.parametre = function(nom){
  try{ return new URLSearchParams(location.search).get(nom); }catch(e){ return null; }
};

/** Résout la source d'un décor (mise en cache). */
VML.resoudreDecor = async function(id){
  if(VML.sourcesDecor[id]) return VML.sourcesDecor[id];
  const d = VML.decor(id) || {};
  let src = null;
  const forcerSecours = VML.parametre("secours") === "1";
  if(!forcerSecours){
    for(const ext of VML.EXT_DECOR){
      const r = await VML.sonderImage("assets/images/decors/" + id + ext);
      if(r){ src = { type: "depose", url: r.url, ratio: r.ratio }; break; }
    }
    const refOk = VML.parametre("reference") !== "0" && !(VML.reglage && VML.reglage("sansReference"));
    if(!src && d.reference && refOk){
      const r = await VML.sonderImage(d.reference);
      if(r) src = { type: "reference", url: r.url, ratio: r.ratio };
    }
  }
  if(!src) src = { type: "secours", url: null, ratio: 16/9 };
  VML.sourcesDecor[id] = src;
  return src;
};

/** Zones et effets pour la source utilisée (calages éventuels). */
VML.calageDecor = function(id, type){
  const d = VML.decor(id) || {};
  const c = (d.calages || {})[type] || {};
  return { zones: c.zones || d.zones || [], effets: c.effets || d.effets || [] };
};

VML.animationsReduites = function(){
  if(VML.reglage && VML.reglage("animationsReduites")) return true;
  try{ return window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches; }catch(e){ return false; }
};

/* ============================================================ */
VML.Scene = class {
  constructor(hote){
    this.hote = hote;
    hote.classList.add("scene-nautilus");
    hote.innerHTML = `
      <div class="sc-cadre">
        <div class="sc-kb">
          <div class="sc-fond"></div>
          <canvas class="sc-fx" aria-hidden="true"></canvas>
          <div class="sc-reactions" aria-hidden="true"></div>
          <div class="sc-zones"></div>
        </div>
      </div>
      <div class="sc-vignette" aria-hidden="true"></div>
      <div class="sc-grain" aria-hidden="true"></div>
      <div class="sc-alarme" aria-hidden="true"></div>
      <div class="sc-source" aria-hidden="true"></div>`;
    this.cadre = hote.querySelector(".sc-cadre");
    this.kb = hote.querySelector(".sc-kb");
    this.fond = hote.querySelector(".sc-fond");
    this.canvas = hote.querySelector(".sc-fx");
    this.zonesEl = hote.querySelector(".sc-zones");
    this.reactionsEl = hote.querySelector(".sc-reactions");
    this.ctx = (this.canvas.getContext && !/jsdom/i.test(navigator.userAgent)) ? this.canvas.getContext("2d") : null;
    this.particules = [];
    this.t0 = performance.now();
    this.ratio = 16/9;
    this.etat = "normal";
    this.focus = null;
    this._boucle = this._boucle.bind(this);
    this._redim = () => this.disposer();
    window.addEventListener("resize", this._redim);
  }

  /**
   * @param {string} id      décor
   * @param {object} o       { etat, cible, actives:[ids], onZone(id), mode:"cover"|"contain" }
   */
  async afficher(id, o = {}){
    this.id = id;
    this.options = o;
    const d = VML.decor(id) || { titre: id };
    const src = await VML.resoudreDecor(id);
    if(!this.hote.ownerDocument || !this.hote.ownerDocument.defaultView || !this.hote.isConnected) return src;
    this.source = src;
    this.ratio = src.ratio || 16/9;
    const { zones, effets } = VML.calageDecor(id, src.type);
    this.zones = zones; this.effets = effets;
    this.hote.dataset.decor = id;
    this.hote.dataset.source = src.type;
    if(src.type === "secours"){
      this.fond.innerHTML = (VML.SVG_DECORS && VML.SVG_DECORS[id]) ? VML.SVG_DECORS[id] : VML.svgGenerique(d);
      this.fond.classList.add("svg");
    }else{
      this.fond.classList.remove("svg");
      this.fond.innerHTML = `<img src="${src.url}" alt="">`;
    }
    this.hote.querySelector(".sc-source").textContent =
      src.type === "depose" ? "image déposée" : src.type === "reference" ? "image de référence" : "décor dessiné";
    this.hote.setAttribute("aria-label", d.titre || id);
    this.dessinerZones(o.cible, o.actives);
    this.focus = o.cible ? zones.find(z => z.id === o.cible) : null;
    this.setEtat(o.etat || "normal");
    this.disposer();
    this.initParticules();
    const kb = d.kenBurns || {};
    this.kb.style.setProperty("--kb-echelle", kb.echelle || 1.05);
    this.kb.style.setProperty("--kb-duree", (kb.duree || 34) + "s");
    this.kb.classList.toggle("ken-burns", !VML.animationsReduites());
    const vi = effets.find(e => e.type === "vignette");
    this.hote.style.setProperty("--vignette", vi ? vi.force : 0.5);
    const gr = effets.find(e => e.type === "grain");
    this.hote.style.setProperty("--grain", gr ? gr.force : 0);
    if(!this.raf) this.raf = requestAnimationFrame(this._boucle);
    if(VML.ambianceDecor) VML.ambianceDecor(d.ambiance || []);
    return src;
  }

  setEtat(etat){
    this.etat = etat;
    const d = VML.decor(this.id) || {};
    const e = (d.etats || {})[etat] || {};
    this.fond.style.filter = e.filtre || "none";
    this.hote.classList.toggle("en-alarme", !!e.alarme);
    this.hote.classList.toggle("ocean-ouvert", !!e.ocean);
    this.hote.dataset.etat = etat;
  }

  dessinerZones(cible, actives){
    this.zonesEl.innerHTML = "";
    (this.zones || []).forEach(z => {
      if(actives && !actives.includes(z.id)) return;
      const b = document.createElement("button");
      b.type = "button";
      b.className = "zone" + (z.id === cible ? " cible" : "");
      b.dataset.zone = z.id;
      b.style.left = z.x + "%"; b.style.top = z.y + "%";
      b.style.width = z.w + "%"; b.style.height = z.h + "%";
      b.setAttribute("aria-label", z.libelle + (z.id === cible ? " (à examiner)" : ""));
      b.innerHTML = `<span class="zone-etiquette">${z.libelle}</span>${z.id === cible ? '<span class="zone-loupe" aria-hidden="true">🔍</span>' : ""}`;
      b.addEventListener("click", () => { if(this.options && this.options.onZone) this.options.onZone(z.id, z); });
      this.zonesEl.appendChild(b);
    });
  }

  marquerCible(id){
    this.zonesEl.querySelectorAll(".zone").forEach(b => {
      const c = b.dataset.zone === id;
      b.classList.toggle("cible", c);
      const l = b.querySelector(".zone-loupe");
      if(c && !l) b.insertAdjacentHTML("beforeend", '<span class="zone-loupe" aria-hidden="true">🔍</span>');
      if(!c && l) l.remove();
    });
  }

  zone(id){ return (this.zones || []).find(z => z.id === id) || null; }

  /** Rectangle écran (px, relatif à la scène) d'une zone. */
  rectZone(id){
    const z = this.zone(id); if(!z) return null;
    const c = this.cadre.getBoundingClientRect(), h = this.hote.getBoundingClientRect();
    return { x: c.left - h.left + c.width * z.x / 100, y: c.top - h.top + c.height * z.y / 100, w: c.width * z.w / 100, h: c.height * z.h / 100 };
  }

  /** Cadre au format de l'image, qui recouvre la scène (ou la contient sur écran étroit). */
  disposer(){
    const W = this.hote.clientWidth || 1280, H = this.hote.clientHeight || 720, r = this.ratio || 16/9;
    const contenir = (this.options && this.options.mode === "contain") || (W / H < 1.15);
    let w, h;
    if(contenir ? (W / H > r) : (W / H < r)){ h = H; w = H * r; } else { w = W; h = W / r; }
    let left = (W - w) / 2, top = (H - h) / 2;
    /* La zone visée reste visible quand l'image est rognée */
    if(!contenir && this.focus && w > W){
      const cx = w * (this.focus.x + this.focus.w / 2) / 100;
      const min = W - w, max = 0;
      const vis = cx + left;
      if(vis < W * 0.15) left = Math.min(max, W * 0.15 - cx);
      if(vis > W * 0.85) left = Math.max(min, W * 0.85 - cx);
    }
    Object.assign(this.cadre.style, { width: w + "px", height: h + "px", left: left + "px", top: top + "px" });
    this.hote.classList.toggle("contenue", contenir);
    const dpr = Math.min(window.devicePixelRatio || 1, 1.5);
    if(this.canvas){
      this.canvas.width = Math.round(w * dpr); this.canvas.height = Math.round(h * dpr);
      this.canvas.style.width = w + "px"; this.canvas.style.height = h + "px";
      this.echelle = dpr;
    }
    this.L = w; this.Hh = h;
  }

  /* ---------------- Particules ---------------- */
  initParticules(){
    this.particules = [];
    const reduit = VML.animationsReduites();
    (this.effets || []).forEach((ef, k) => {
      const n = reduit ? 0 : (ef.nombre || 0);
      for(let i = 0; i < n; i++) this.particules.push(this.nouvelleParticule(ef, k, true));
      ef._prochaineEtincelle = 0;
    });
  }
  nouvelleParticule(ef, k, debut){
    const p = { k, type: ef.type };
    const rx = () => ef.x + Math.random() * (ef.w || 0), ry = () => ef.y + Math.random() * (ef.h || 0);
    if(ef.type === "bulles"){ p.x = rx(); p.y = debut ? ry() : ef.y + ef.h; p.r = 0.5 + Math.random() * 1.6; p.v = 1.2 + Math.random() * 2.2; p.ph = Math.random() * 6; }
    if(ef.type === "poussiere"){ p.x = rx(); p.y = ry(); p.r = 0.4 + Math.random() * 1.1; p.vx = (Math.random() - .5) * .25; p.vy = (Math.random() - .5) * .18; p.ph = Math.random() * 6; }
    if(ef.type === "poissons"){ p.dir = Math.random() < .5 ? 1 : -1; p.x = debut ? rx() : (p.dir > 0 ? ef.x - 2 : ef.x + ef.w + 2); p.y = ry(); p.taille = 0.6 + Math.random() * 0.9; p.v = 0.8 + Math.random() * 1.6; p.ph = Math.random() * 6; p.meduse = !!ef.meduses && Math.random() < .5; }
    if(ef.type === "fumee"){ p.x = rx(); p.y = debut ? ry() : ef.y + ef.h; p.r = 2 + Math.random() * 3; p.v = 1.5 + Math.random() * 2; p.vie = debut ? Math.random() : 0; }
    return p;
  }

  _boucle(now){
    this.raf = null;
    if(!document.body.contains(this.hote)) return;
    if(!this.ctx || VML.animationsReduites()){ this.dessinerStatique(); return; }
    const dt = Math.min(0.05, ((now || performance.now()) - (this._dernier || now || 0)) / 1000) || 0.016;
    this._dernier = now || performance.now();
    const t = ((now || performance.now()) - this.t0) / 1000;
    this.dessiner(t, dt);
    this.raf = requestAnimationFrame(this._boucle);
  }

  dessinerStatique(){
    if(!this.ctx) return;
    this.dessiner(0, 0, true);
  }

  dessiner(t, dt, statique){
    const ctx = this.ctx, e = this.echelle || 1, W = this.canvas.width, H = this.canvas.height;
    ctx.clearRect(0, 0, W, H);
    const X = v => v / 100 * W, Y = v => v / 100 * H, U = Math.min(W, H) / 100;
    const actif = ef => !ef.etat || ef.etat === this.etat;
    (this.effets || []).forEach((ef, k) => {
      if(!actif(ef)) return;
      ctx.save();
      if(ef.type === "lueur"){
        let a = 0.55 + (ef.pulse || 0) * Math.sin(t * 1.6 + k);
        if(ef.scintille) a += (Math.random() - .5) * 0.15;
        if(this.etat === "panne" && this.hote.classList.contains("en-alarme")) a *= 0.35;
        const g = ctx.createRadialGradient(X(ef.x), Y(ef.y), 0, X(ef.x), Y(ef.y), ef.r * U * 1.6);
        g.addColorStop(0, VML.rgba(ef.couleur, 0.45 * a));
        g.addColorStop(0.4, VML.rgba(ef.couleur, 0.18 * a));
        g.addColorStop(1, VML.rgba(ef.couleur, 0));
        ctx.globalCompositeOperation = "lighter";
        ctx.fillStyle = g;
        ctx.fillRect(X(ef.x) - ef.r * U * 2, Y(ef.y) - ef.r * U * 2, ef.r * U * 4, ef.r * U * 4);
      }
      if(ef.type === "caustiques"){
        ctx.globalCompositeOperation = "lighter";
        ctx.beginPath(); ctx.ellipse(X(ef.x + ef.w / 2), Y(ef.y + ef.h / 2), X(ef.w / 2), Y(ef.h / 2), 0, 0, Math.PI * 2); ctx.clip();
        const n = 9, I = ef.intensite || 0.5;
        for(let i = 0; i < n; i++){
          const px = ef.x + ef.w * ((i * 0.37 + 0.5 * Math.sin(t * 0.35 + i * 1.7)) % 1 + 1) % 1;
          const py = ef.y + ef.h * ((i * 0.53 + 0.4 * Math.cos(t * 0.28 + i * 2.3)) % 1 + 1) % 1;
          const r = (2.2 + 1.2 * Math.sin(t * 0.9 + i)) * U;
          const g = ctx.createRadialGradient(X(px), Y(py), 0, X(px), Y(py), r * 2.2);
          g.addColorStop(0, `rgba(150,240,255,${0.16 * I})`); g.addColorStop(0.5, `rgba(90,210,255,${0.07 * I})`); g.addColorStop(1, "rgba(60,180,255,0)");
          ctx.fillStyle = g; ctx.fillRect(X(px) - r * 2.2, Y(py) - r * 2.2, r * 4.4, r * 4.4);
        }
        ctx.strokeStyle = `rgba(200,250,255,${0.08 * I})`; ctx.lineWidth = 1.2 * e;
        for(let i = 0; i < 6; i++){
          ctx.beginPath();
          for(let s = 0; s <= 20; s++){
            const xx = ef.x + ef.w * s / 20;
            const yy = ef.y + ef.h * (i + .5) / 6 + 1.6 * Math.sin(s * 0.9 + t * 1.1 + i * 2);
            s ? ctx.lineTo(X(xx), Y(yy)) : ctx.moveTo(X(xx), Y(yy));
          }
          ctx.stroke();
        }
      }
      if(ef.type === "rayons"){
        ctx.globalCompositeOperation = "lighter";
        for(let i = 0; i < 4; i++){
          const a = 0.05 + 0.03 * Math.sin(t * 0.5 + i * 1.3);
          const x0 = X(ef.x - ef.w / 2 + ef.w * (i + .5) / 4);
          const g = ctx.createLinearGradient(0, Y(ef.y), 0, Y(ef.y + ef.h));
          g.addColorStop(0, `rgba(170,220,255,${a})`); g.addColorStop(1, "rgba(170,220,255,0)");
          ctx.fillStyle = g;
          ctx.beginPath(); ctx.moveTo(x0 - 1.2 * U, Y(ef.y)); ctx.lineTo(x0 + 1.2 * U, Y(ef.y));
          ctx.lineTo(x0 + 7 * U + i * U, Y(ef.y + ef.h)); ctx.lineTo(x0 + 1 * U + i * U, Y(ef.y + ef.h)); ctx.closePath(); ctx.fill();
        }
      }
      if(ef.type === "etincelles" && !statique){
        if(t > (ef._prochaineEtincelle || 0)){
          ef._prochaineEtincelle = t + 1.2 + Math.random() * 2.8;
          for(let i = 0; i < 14; i++) this.particules.push({ k, type: "etincelle", x: ef.x, y: ef.y, vx: (Math.random() - .5) * 18, vy: -Math.random() * 14, vie: 1 });
          if(VML.son && this.hote.offsetParent !== null && this.hote.closest(".ecran.actif")) VML.son("etincelle");
        }
      }
      ctx.restore();
    });
    /* Particules mobiles */
    ctx.save();
    const garder = [];
    for(const p of this.particules){
      const ef = this.effets[p.k];
      if(!ef || !actif(ef)){ garder.push(p); continue; }
      if(p.type === "bulles"){
        p.y -= p.v * dt * 3; const wob = Math.sin(t * 2 + p.ph) * 0.3;
        if(p.y < ef.y){ Object.assign(p, this.nouvelleParticule(ef, p.k, false)); }
        ctx.globalCompositeOperation = "lighter";
        ctx.strokeStyle = "rgba(210,245,255,.55)"; ctx.lineWidth = 1 * e;
        ctx.beginPath(); ctx.arc(X(p.x + wob), Y(p.y), p.r * U * 0.35, 0, Math.PI * 2); ctx.stroke();
        ctx.fillStyle = "rgba(230,250,255,.35)"; ctx.beginPath(); ctx.arc(X(p.x + wob) - p.r * U * .1, Y(p.y) - p.r * U * .1, p.r * U * .1, 0, Math.PI * 2); ctx.fill();
      }else if(p.type === "poussiere"){
        p.x += p.vx * dt; p.y += p.vy * dt;
        if(p.x < ef.x || p.x > ef.x + ef.w) p.vx *= -1;
        if(p.y < ef.y || p.y > ef.y + ef.h) p.vy *= -1;
        const a = 0.25 + 0.25 * Math.sin(t * 1.3 + p.ph);
        ctx.globalCompositeOperation = "lighter";
        ctx.fillStyle = `rgba(255,236,190,${a})`;
        ctx.beginPath(); ctx.arc(X(p.x), Y(p.y), p.r * e, 0, Math.PI * 2); ctx.fill();
      }else if(p.type === "poissons"){
        p.x += p.dir * p.v * dt;
        if(p.x < ef.x - 3 || p.x > ef.x + ef.w + 3) Object.assign(p, this.nouvelleParticule(ef, p.k, false));
        ctx.save();
        ctx.beginPath(); ctx.rect(X(ef.x), Y(ef.y), X(ef.w), Y(ef.h)); ctx.clip();
        if(p.meduse){
          const yy = p.y + Math.sin(t * 0.8 + p.ph) * 1.5, s = p.taille * U * 1.2;
          ctx.globalCompositeOperation = "lighter";
          ctx.fillStyle = "rgba(220,200,255,.28)";
          ctx.beginPath(); ctx.ellipse(X(p.x), Y(yy), s, s * 0.7, 0, Math.PI, 0); ctx.fill();
          ctx.strokeStyle = "rgba(220,210,255,.25)"; ctx.lineWidth = 1 * e;
          for(let i = -2; i <= 2; i++){ ctx.beginPath(); ctx.moveTo(X(p.x) + i * s * .35, Y(yy)); ctx.quadraticCurveTo(X(p.x) + i * s * .35 + Math.sin(t * 2 + i) * s * .3, Y(yy) + s, X(p.x) + i * s * .3, Y(yy) + s * 1.8); ctx.stroke(); }
        }else{
          const yy = p.y + Math.sin(t * 1.5 + p.ph) * 0.4, s = p.taille * U;
          ctx.fillStyle = "rgba(10,40,60,.55)";
          ctx.translate(X(p.x), Y(yy)); ctx.scale(p.dir, 1);
          ctx.beginPath(); ctx.ellipse(0, 0, s, s * 0.38, 0, 0, Math.PI * 2); ctx.fill();
          ctx.beginPath(); ctx.moveTo(-s * .8, 0); ctx.lineTo(-s * 1.5, -s * .4 * (1 + .3 * Math.sin(t * 8 + p.ph))); ctx.lineTo(-s * 1.5, s * .4); ctx.closePath(); ctx.fill();
        }
        ctx.restore();
      }else if(p.type === "fumee"){
        p.y -= p.v * dt; p.vie += dt * 0.18; p.r += dt * 1.2;
        if(p.vie > 1 || p.y < ef.y - 10) Object.assign(p, this.nouvelleParticule(ef, p.k, false));
        const a = 0.22 * Math.sin(Math.PI * Math.min(1, p.vie));
        const g = ctx.createRadialGradient(X(p.x), Y(p.y), 0, X(p.x), Y(p.y), p.r * U);
        g.addColorStop(0, `rgba(70,70,72,${a})`); g.addColorStop(1, "rgba(70,70,72,0)");
        ctx.globalCompositeOperation = "source-over";
        ctx.fillStyle = g; ctx.beginPath(); ctx.arc(X(p.x), Y(p.y), p.r * U, 0, Math.PI * 2); ctx.fill();
      }else if(p.type === "etincelle"){
        p.vie -= dt * 1.6; if(p.vie <= 0) continue;
        p.x += p.vx * dt * .4; p.y += p.vy * dt * .4; p.vy += 30 * dt;
        ctx.globalCompositeOperation = "lighter";
        ctx.fillStyle = `rgba(255,${200 + Math.round(55 * p.vie)},140,${p.vie})`;
        ctx.beginPath(); ctx.arc(X(p.x), Y(p.y), 1.6 * e, 0, Math.PI * 2); ctx.fill();
      }
      garder.push(p);
    }
    this.particules = garder;
    ctx.restore();
  }

  /* ---------------- Réactions du décor (aucun texte) ---------------- */
  reaction(effet, zoneId){
    const r = this.reactionsEl;
    const z = zoneId ? this.zone(zoneId) : null;
    const pos = z ? `left:${z.x}%;top:${z.y}%;width:${z.w}%;height:${z.h}%` : "inset:0";
    const el = document.createElement("div");
    el.className = "reaction reaction-" + effet;
    el.setAttribute("style", pos);
    if(effet === "cable-neuf"){
      el.innerHTML = `<svg viewBox="0 0 200 120" preserveAspectRatio="xMidYMid meet"><defs><linearGradient id="cuivre" x1="0" x2="1"><stop offset="0" stop-color="#7a3f12"/><stop offset=".5" stop-color="#f0a35e"/><stop offset="1" stop-color="#8a4b17"/></linearGradient></defs>
        <path d="M20 80 C 60 20, 100 120, 140 60 S 190 70, 185 40" fill="none" stroke="#1d1d1f" stroke-width="13" stroke-linecap="round"/>
        <path d="M20 80 C 60 20, 100 120, 140 60 S 190 70, 185 40" fill="none" stroke="#3a3a3e" stroke-width="7" stroke-linecap="round"/>
        <circle cx="20" cy="80" r="6" fill="url(#cuivre)"/><circle cx="185" cy="40" r="6" fill="url(#cuivre)"/></svg>`;
      this.setEtat("normal");
    }
    if(effet === "lumiere"){ this.hote.classList.add("flash-lumiere"); setTimeout(() => this.hote.classList.remove("flash-lumiere"), 1600); this.setEtat("normal"); }
    if(effet === "aiguilles"){ el.innerHTML = '<div class="balayage"></div>'; }
    if(effet === "hublots"){ this.setEtat("victoire"); this.hote.classList.add("tremble"); setTimeout(() => this.hote.classList.remove("tremble"), 1200); }
    /* Réactions génériques, posées sur la zone de l'objet (aucun texte) */
    if(effet === "eclat") el.innerHTML = Array.from({ length: 14 }, (_, i) => `<span class="etoile" style="left:${(i * 37) % 100}%;top:${(i * 53) % 100}%;animation-delay:${(i % 7) * 0.12}s"></span>`).join("");
    if(effet === "vapeur") el.innerHTML = Array.from({ length: 8 }, (_, i) => `<span class="nuage" style="left:${10 + i * 11}%;animation-delay:${i * 0.15}s"></span>`).join("");
    if(effet === "secousse"){ this.hote.classList.add("tremble", "flash-blanc"); setTimeout(() => this.hote.classList.remove("tremble", "flash-blanc"), 1300); }
    if(effet === "ouverture") el.innerHTML = '<div class="volet g"></div><div class="volet d"></div>';
    if(effet === "carte") el.innerHTML = '<svg viewBox="0 0 100 100" preserveAspectRatio="none"><path class="trace" d="M5 80 C 30 20, 60 90, 95 15" /></svg>';
    if(effet === "givre") el.innerHTML = '<div class="givre"></div>';
    if(effet === "alarme"){ this.hote.classList.add("en-alarme"); setTimeout(() => this.hote.classList.remove("en-alarme"), 2400); }
    if(effet === "calme"){ this.setEtat("normal"); }
    r.appendChild(el);
    if(VML.son) VML.son("reaction-" + effet);
    return el;
  }

  viderReactions(){ this.reactionsEl.innerHTML = ""; }

  detruire(){
    window.removeEventListener("resize", this._redim);
    if(this.raf) cancelAnimationFrame(this.raf);
    this.raf = null;
  }
};

/** Décor de secours générique (si ni fichier, ni référence, ni dessin propre) : ambiance sans objet. */
VML.svgGenerique = function(d){
  const chaud = /pont|cambuse|vapeur|cabine|salon|carre|orgue|vigo/.test((d && d.titre || "").toLowerCase() + JSON.stringify(d && d.ambiance || ""));
  return `<svg viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="${(d && d.titre) || "décor"} (décor de secours)">
    <defs><radialGradient id="gG" cx=".5" cy=".4" r=".8"><stop offset="0" stop-color="${chaud ? "#6a3d1c" : "#1f6a8a"}"/><stop offset="1" stop-color="#05121a"/></radialGradient></defs>
    <rect width="1600" height="900" fill="url(#gG)"/>
    ${Array.from({ length: 9 }, (_, i) => `<path d="M${i * 200} 900 Q ${i * 200 + 100} ${620 + (i % 3) * 30} ${i * 200 + 200} 900Z" fill="#000" opacity=".25"/>`).join("")}
  </svg>`;
};

VML.rgba = function(hex, a){
  const h = String(hex || "#ffffff").replace("#", "");
  const n = parseInt(h.length === 3 ? h.split("").map(c => c + c).join("") : h, 16);
  return `rgba(${(n >> 16) & 255},${(n >> 8) & 255},${n & 255},${Math.max(0, Math.min(1, a)).toFixed(3)})`;
};
