/* ============================================================
   ACCUEIL EN SÉANCE (A1) — un seul bouton pour les élèves
   ------------------------------------------------------------
   Quand l'enseignant a fixé le jeu du jour (serveur local) ou quand
   la page est ouverte par le lien « ?jeu=<id>&grade=<grade> » (GitHub
   Pages), l'accueil n'affiche qu'un grand bouton « ▶ Jouer » vers la
   version immersive du jeu du jour. Les autres jeux restent visibles
   sur l'ordinateur de l'enseignant (le serveur le reconnaît) et avec
   « ?tous=1 ». Sans séance, l'accueil est inchangé.
   Chargé dans le <head> d'index.html, après commun/js/seance.js.
   ============================================================ */
(function(){
  "use strict";
  let q = null; try{ q = new URLSearchParams(location.search); }catch(e){}
  if(q && q.get("tous") === "1") return;
  const racine = document.documentElement;
  // Le temps de demander au serveur (1,5 s au plus), on cache la liste des jeux : pas de clic sur un autre jeu.
  const attendre = (q && q.get("jeu")) || /^https?:$/.test(location.protocol);
  if(attendre){
    racine.classList.add("seance-attente");
    setTimeout(() => racine.classList.remove("seance-attente"), 1800);
  }
  const style = document.createElement("style");
  style.textContent = `
    html.seance-attente body>*:not(#seance-eleves){visibility:hidden}
    html.seance-eleves body>*:not(#seance-eleves){display:none!important}
    html.seance-eleves body{overflow:hidden}
    #seance-eleves{position:fixed;inset:0;z-index:1000;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:clamp(12px,3vh,26px);
      padding:24px 16px;text-align:center;color:#fff;background:radial-gradient(900px 500px at 50% 0,rgba(255,255,255,.18),transparent 65%),linear-gradient(150deg,var(--c1,#1d3a8a),var(--c2,#0b1536))}
    #seance-eleves .icone{font-size:clamp(3rem,10vh,5.5rem);line-height:1}
    #seance-eleves h1{margin:0;font:700 clamp(1.7rem,6vw,3.2rem)/1.1 Georgia,"Palatino Linotype",serif;text-shadow:0 3px 18px rgba(0,0,0,.35);max-width:22ch}
    #seance-eleves p{margin:0;max-width:40rem;font-size:clamp(1rem,2.4vw,1.2rem);opacity:.92}
    #seance-eleves a.jouer-seance{display:inline-flex;align-items:center;justify-content:center;gap:.4em;min-width:min(78vw,420px);min-height:clamp(84px,16vh,130px);
      padding:0 1.2em;border-radius:999px;background:#fff;color:var(--c1,#1d3a8a);font:800 clamp(2rem,7vw,3.4rem)/1 system-ui,sans-serif;text-decoration:none;
      box-shadow:0 14px 40px rgba(0,0,0,.35),0 0 0 8px rgba(255,255,255,.22);transition:transform .15s}
    #seance-eleves a.jouer-seance:hover,#seance-eleves a.jouer-seance:focus-visible{transform:scale(1.04);outline:none;box-shadow:0 14px 40px rgba(0,0,0,.35),0 0 0 12px rgba(255,255,255,.5)}
    #seance-eleves .grade{font-size:1rem;padding:4px 14px;border-radius:999px;background:rgba(255,255,255,.18)}
    .bandeau-seance-prof{position:sticky;top:0;z-index:50;margin:0;padding:10px 16px;background:#14532d;color:#fff;font:600 .95rem/1.4 system-ui,sans-serif;text-align:center}
    .bandeau-seance-prof a{color:#bbf7d0}
    @media (prefers-reduced-motion:reduce){#seance-eleves a.jouer-seance{transition:none}}`;
  document.head.appendChild(style);

  const esc = s => String(s == null ? "" : s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  async function nomDuGrade(dossier, grade){
    if(!grade) return "";
    try{
      const r = await fetch(dossier + "assets/data/enigmes.json", { cache: "no-store" });
      const n = r.ok ? ((await r.json()).niveaux || []).find(x => x.id === grade) : null;
      return n ? `${n.icone || ""} ${n.nom}` : "";
    }catch(e){ return ""; }
  }
  function afficherEleves(s){
    const C = window.CATALOGUE, S = window.SEANCE;
    const j = S.infoJeu(C, s.jeu) || { titre: s.titre || s.jeu, icone: "🎮", couleurs: [], immersif: "immersifs/" + s.jeu };
    const href = s.adresse || S.adresse(j);
    const div = document.createElement("div");
    div.id = "seance-eleves";
    div.setAttribute("role", "main");
    div.style.setProperty("--c1", (j.couleurs || [])[0] || "#1d3a8a");
    div.style.setProperty("--c2", "#0b1536");
    div.innerHTML = `<div class="icone" aria-hidden="true">${esc(j.icone || "🎮")}</div>
      <h1>${esc(j.titre)}</h1>
      ${j.resume ? `<p>${esc(j.resume)}</p>` : ""}
      <span class="grade" hidden></span>
      <a class="jouer-seance" href="${esc(href)}">▶ Jouer</a>`;
    document.body.appendChild(div);
    racine.classList.add("seance-eleves");
    racine.classList.remove("seance-attente");
    document.title = j.titre + " — Escape game";
    const a = div.querySelector("a.jouer-seance");
    a.addEventListener("click", () => { if(j.immersif || /^immersifs\//.test(href)) S.imposerGrade(S.idDe(j) || s.jeu, s.grade || ""); });
    try{ a.focus(); }catch(e){}
    nomDuGrade(href, s.grade).then(t => { const g = div.querySelector(".grade"); if(t){ g.textContent = "Grade : " + t; g.hidden = false; } });
  }
  function bandeauEnseignant(s){
    const C = window.CATALOGUE, S = window.SEANCE, j = S.infoJeu(C, s.jeu) || { titre: s.jeu };
    const p = document.createElement("p");
    p.className = "bandeau-seance-prof";
    p.innerHTML = `✅ Séance du jour : <b>${esc(j.titre)}</b>. Les élèves ne voient qu'un bouton « Jouer » ; vous voyez tous les jeux (ordinateur de l'enseignant).
      <a href="enseignant.html">Espace enseignant</a> · <a href="tableau.html">QR code à projeter</a>`;
    document.body.insertBefore(p, document.body.firstChild);
  }
  async function demarrer(){
    if(!window.SEANCE){ racine.classList.remove("seance-attente"); return; }
    const s = await window.SEANCE.lire("");
    if(s.jeu && !s.local) afficherEleves(s);
    else{
      racine.classList.remove("seance-attente");
      if(s.jeu && s.local) bandeauEnseignant(s);
    }
    window.__seanceAccueil = s;
  }
  let lance = false;
  const une = () => { if(!lance){ lance = true; demarrer(); } };
  if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", une);
  else setTimeout(une, 0);
})();
