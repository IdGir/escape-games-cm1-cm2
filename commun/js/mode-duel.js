/* ============================================================
   MODE DUEL — deux équipes face à face sur un même écran (N4)
   ------------------------------------------------------------
   Pour le TBI : sur l'écran d'accueil, « ⚔️ Duel » et le nom des deux
   équipes (adresse directe : …/melanges/?duel=1). Les équipes jouent À
   TOUR DE RÔLE : une énigme chacune (une salle chacune dans Déclaration
   et Tour du monde), avec les mêmes règles et le même barème.
     • tous les points gagnés ou perdus (indices) pendant un tour vont à
       l'équipe dont c'est le tour ; le coffre final et le quizz aussi ;
     • un bandeau affiche les deux scores et l'équipe qui joue ; un
       rideau annonce chaque changement de tour ;
     • à la fin : vainqueur (ou égalité), points et énigmes de chacune.
   Le duel est gardé avec la partie (reprise sur le même appareil).
   Chargé après app.js et mode-solo.js, sans modifier app.js.
   ============================================================ */
(function(){
  if(typeof ETAT === "undefined" || !document.getElementById("input-equipe")) return;
  const params = new URLSearchParams(location.search);
  const CLE = "escape_duel_" + (typeof CLE_SAUVEGARDE !== "undefined" ? CLE_SAUVEGARDE : ((typeof JEU !== "undefined" && JEU.id) || ""));
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const inp = document.getElementById("input-equipe");
  let placeholder1 = inp.placeholder;

  const style = document.createElement("style");
  style.textContent = `
    .bascule-duel{display:flex;flex-direction:column;align-items:center;gap:6px;margin:0 0 10px;font-size:.95rem}
    .bascule-duel label{display:inline-flex;gap:8px;align-items:center;cursor:pointer;padding:6px 12px;border-radius:999px;background:rgba(255,255,255,.6)}
    .bascule-duel input[type=text]{display:none;font:inherit;padding:10px 14px;border-radius:12px;border:2px solid var(--parchemin-ombre,#e0cfa6);width:min(100%,420px)}
    .bascule-duel.actif input[type=text]{display:block}
    #duel-hud{position:fixed;top:8px;left:50%;transform:translateX(-50%);z-index:900;display:none;gap:4px;align-items:stretch;
      background:rgba(20,20,30,.88);color:#fff;border-radius:999px;padding:4px;font-size:.95rem;box-shadow:0 4px 14px rgba(0,0,0,.3)}
    body.duel-actif #duel-hud{display:flex}
    #duel-hud .eq{padding:4px 14px;border-radius:999px;opacity:.65;white-space:nowrap;max-width:40vw;overflow:hidden;text-overflow:ellipsis}
    #duel-hud .eq.joue{opacity:1;background:var(--or,#c9a227);color:#2b1d10;font-weight:bold}
    #duel-hud .vs{align-self:center;opacity:.7;padding:0 2px}
    .rideau-duel{position:fixed;inset:0;z-index:950;display:flex;align-items:center;justify-content:center;background:rgba(15,15,25,.82);color:#fff;
      font-size:clamp(1.4rem,4vw,2.6rem);text-align:center;padding:20px;animation:duel-rideau 1.8s ease both;pointer-events:none}
    body.calme .rideau-duel{animation:none;opacity:.95}
    @keyframes duel-rideau{0%{opacity:0}15%{opacity:1}80%{opacity:1}100%{opacity:0}}
    .resultat-duel{margin:10px auto 18px;max-width:680px;padding:14px 18px;border-radius:14px;background:#fff8e1;border:2px solid var(--or,#c9a227);text-align:center}
    .resultat-duel table{margin:8px auto;border-collapse:collapse}.resultat-duel td,.resultat-duel th{padding:4px 12px}
    .resultat-duel .gagnant{font-size:1.3rem;font-weight:bold}`;
  document.head.appendChild(style);

  /* ---- Accueil : bascule et second nom ---- */
  const bascule = document.createElement("div");
  bascule.className = "bascule-duel";
  bascule.innerHTML = `<label><input type="checkbox" id="mode-duel"> ⚔️ Duel : deux équipes face à face sur cet écran</label>
    <input type="text" id="input-equipe-2" maxlength="40" placeholder="Nom de l'équipe adverse" aria-label="Nom de l'équipe adverse">`;
  inp.after(bascule);
  const caseDuel = bascule.querySelector("#mode-duel"), inp2 = bascule.querySelector("#input-equipe-2");
  const caseSolo = document.getElementById("mode-solo");
  function maj(){
    bascule.classList.toggle("actif", caseDuel.checked);
    if(caseDuel.checked && caseSolo && caseSolo.checked){ caseSolo.checked = false; caseSolo.dispatchEvent(new Event("change")); }
    if(caseDuel.checked){ if(inp.placeholder !== "Nom de la première équipe") placeholder1 = inp.placeholder; inp.placeholder = "Nom de la première équipe"; }
    else if(inp.placeholder === "Nom de la première équipe") inp.placeholder = placeholder1;
  }
  caseDuel.addEventListener("change", maj);
  if(caseSolo) caseSolo.addEventListener("change", () => { if(caseSolo.checked && caseDuel.checked){ caseDuel.checked = false; maj(); } });
  if(params.get("duel") === "1"){ caseDuel.checked = true; maj(); }

  /* Démarrage : contrôlé avant le jeu (phase de capture) */
  let enAttente = null;
  document.addEventListener("click", ev => {
    if(!(ev.target && ev.target.closest && ev.target.closest("#btn-demarrer"))) return;
    if(!caseDuel.checked){ enAttente = null; return; }
    const a = inp.value.trim(), b = inp2.value.trim();
    if(b.length < 2 || a.toLowerCase() === b.toLowerCase()){
      ev.preventDefault(); ev.stopImmediatePropagation();
      inp2.focus();
      if(typeof toast === "function") toast(b.length < 2 ? "⚔️ Écrivez le nom de l'équipe adverse." : "⚔️ Les deux équipes doivent avoir des noms différents.");
      return;
    }
    enAttente = [a, b];
  }, true);
  const go = document.getElementById("btn-demarrer");
  if(go) go.addEventListener("click", () => {
    sauve = null;
    if(!enAttente){ ETAT.duel = null; ecrire(); document.body.classList.remove("duel-actif"); return; }
    ETAT.duel = { equipes: enAttente, scores: [0, 0], enigmes: [0, 0], tour: 0 };
    ETAT.equipe = `${enAttente[0]} contre ${enAttente[1]}`;
    ETAT.solo = false;
    enAttente = null; dernier = null; ecrire(); hud();
  });

  /* ---- Suivi des points et des tours ---- */
  const progres = () => typeof ETAT.enigmesReussies === "number" ? ETAT.enigmesReussies : Object.keys(ETAT.tempsParSalle || {}).length;
  let dernier = null;   // {score, progres}
  function ecrire(){ try{ ETAT.duel ? localStorage.setItem(CLE, JSON.stringify({ equipe: ETAT.equipe, duel: ETAT.duel })) : localStorage.removeItem(CLE); }catch(e){} }
  function suivre(){
    if(!ETAT.duel && sauve && ETAT.debut && !ETAT.fini && ETAT.equipe === sauve.equipe){ ETAT.duel = sauve.duel; sauve = null; dernier = null; hud(); }
    const D = ETAT.duel;
    if(!D || !ETAT.debut) return;
    const p = progres(), s = ETAT.score || 0;
    if(!dernier){ dernier = { score: s, progres: p }; return; }
    if(s !== dernier.score){ D.scores[D.tour] += s - dernier.score; dernier.score = s; ecrire(); hud(); }
    if(p > dernier.progres){
      D.enigmes[D.tour] += p - dernier.progres; dernier.progres = p;
      if(!ETAT.fini){ D.tour = 1 - D.tour; rideau(); }
      ecrire(); hud();
    }
  }
  setInterval(suivre, 250);
  window.addEventListener("pagehide", suivre);

  function hud(){
    const D = ETAT.duel;
    document.body.classList.toggle("duel-actif", !!D && !ETAT.fini);
    if(!D) return;
    let h = document.getElementById("duel-hud");
    if(!h){ h = document.createElement("div"); h.id = "duel-hud"; h.setAttribute("role", "status"); document.body.appendChild(h); }
    h.innerHTML = D.equipes.map((n, i) => `<span class="eq ${D.tour === i ? "joue" : ""}">${D.tour === i ? "▶ " : ""}${esc(n)} · ${D.scores[i]} pts</span>`).join(`<span class="vs">⚔️</span>`);
  }
  function rideau(){
    const D = ETAT.duel; if(!D) return;
    const r = document.createElement("div");
    r.className = "rideau-duel"; r.setAttribute("role", "status");
    r.innerHTML = `<div>⚔️ À l'équipe<br><b>${esc(D.equipes[D.tour])}</b><br>de jouer !</div>`;
    document.body.appendChild(r);
    setTimeout(() => r.remove(), 1900);
  }

  /* ---- Reprise d'une partie en duel (même appareil) : rétabli dès que la partie reprend ---- */
  var sauve = null;
  try{
    const s = JSON.parse(localStorage.getItem(CLE) || "null");
    const partie = JSON.parse(localStorage.getItem(typeof CLE_SAUVEGARDE !== "undefined" ? CLE_SAUVEGARDE : "") || "null");
    if(s && partie && !partie.fini && partie.equipe === s.equipe && !params.get("salle")) sauve = s;
  }catch(e){}

  /* ---- Écran de fin : résultat du duel ---- */
  if(typeof window.finDuJeu === "function"){
    const origine = window.finDuJeu;
    window.finDuJeu = function(){
      suivre();
      const r = origine.apply(this, arguments);
      const D = ETAT.duel, c = document.getElementById("fin-contenu");
      if(D && c && !document.getElementById("resultat-duel")){
        const d = document.createElement("section");
        d.id = "resultat-duel"; d.className = "resultat-duel";
        c.insertBefore(d, c.firstChild.nextSibling);
        const peindre = () => {
          const [a, b] = D.scores;
          const titre = a === b ? "🤝 Égalité parfaite !" : `🏆 Victoire de l'équipe « ${esc(D.equipes[a > b ? 0 : 1])} »`;
          d.innerHTML = `<h2 style="margin:0">⚔️ Résultat du duel</h2><p class="gagnant">${titre}</p>
            <table><tr><th></th><th>Points</th><th>Énigmes résolues</th></tr>
            ${D.equipes.map((n, i) => `<tr><th>${esc(n)}</th><td>${D.scores[i]}</td><td>${D.enigmes[i]}</td></tr>`).join("")}</table>
            <p style="font-size:.85rem;opacity:.8">Le coffre final et le quizz comptent pour l'équipe dont c'était le tour.</p>`;
        };
        peindre();
        // le quizz final ajoute encore des points : le tableau suit
        let n = 0; const t = setInterval(() => { suivre(); peindre(); if(++n > 240) clearInterval(t); }, 500);
      }
      document.body.classList.remove("duel-actif");
      return r;
    };
  }
  window.MODE_DUEL = { suivre, hud, get etat(){ return ETAT.duel; } };
})();
