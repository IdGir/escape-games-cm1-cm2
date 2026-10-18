/* ============================================================
   RÉGLAGE DE LA DIFFICULTÉ ÉNIGME PAR ÉNIGME — côté enseignant (N20)
   ------------------------------------------------------------
   Chargé par prof.html de chaque jeu à moteur commun :
       <script src="../commun/js/prof-difficulte.js" data-jeu="melanges"></script>
   Ajoute le bouton « 🎚️ Difficulté par énigme » aux actions du tableau de bord.
   Il ouvre, AVANT la partie, la liste des énigmes de chaque salle, avec un
   bouton − / + par énigme (de −2, plus facile, à +2, plus difficile).
   Le réglage S'AJOUTE au palier choisi par l'équipe (voir difficulte-enigme.js) :

        départ CM1 :   −1 aide renforcée · +1 données du CM2 · +2 défi
        départ CM2 :   −2 aide renforcée · −1 données du CM1 · +1 défi
        départ Découverte : +1 données du CM1 · +2 données du CM2

   « Enregistrer pour la classe » : envoyé au serveur local (lancer.bat), que les
   postes élèves interrogent au chargement du jeu, et gardé sur cet ordinateur.
   « Copier le lien élèves » : adresse du jeu avec les réglages (?dif=…),
   pour les postes sans serveur (site publié, tablettes seules).
   Un réglage à 0 revient à la valeur du champ « difficulte » de enigmes.json
   (0 s'il n'y en a pas) : le réglage écrit « 0 » n'est donc pas enregistré.
   ============================================================ */
(function(){
  const sc = document.currentScript;
  const dossierJeu = location.pathname.split("/").filter(Boolean).slice(-2, -1)[0] || "jeu";
  const JEU_ID = (sc && sc.dataset && sc.dataset.jeu) || (/\/immersifs\//.test(location.pathname) ? "immersif-" : "") + dossierJeu;
  const CLE = "escape_difficulte_" + JEU_ID;
  const esc = s => String(s == null ? "" : s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const borne = n => Math.max(-2, Math.min(2, n));
  let enigmes = null, valeurs = {};

  async function charger(){
    if(!enigmes){
      try{ enigmes = await (await fetch("assets/data/enigmes.json", { cache: "no-store" })).json(); }catch(e){ enigmes = null; }
    }
    valeurs = {};
    try{ valeurs = JSON.parse(localStorage.getItem(CLE) || "{}") || {}; }catch(e){}
    try{
      const r = await fetch("/api/difficulte?jeu=" + encodeURIComponent(JEU_ID), { cache: "no-store" });
      if(r.ok){ const d = await r.json(); if(d && d.valeurs && typeof d.valeurs === "object") valeurs = d.valeurs; }
    }catch(e){}
    return enigmes;
  }
  const propres = () => Object.fromEntries(Object.entries(valeurs).filter(([, v]) => +v !== 0 && Number.isFinite(+v)).map(([k, v]) => [k, borne(Math.round(+v))]));
  const LIBELLES = { "-2": "−2 · beaucoup plus facile", "-1": "−1 · plus facile", "0": "0 · inchangée", "1": "+1 · plus difficile", "2": "+2 · beaucoup plus difficile" };

  function lien(){
    const p = propres();
    const dif = Object.entries(p).map(([k, v]) => `${k}:${v > 0 ? "+" : ""}${v}`).join(",");
    const base = location.href.replace(/prof\.html.*$/, "");
    return base + (dif ? "?dif=" + dif : "");
  }
  async function enregistrer(){
    const p = propres();
    try{ localStorage.setItem(CLE, JSON.stringify(p)); }catch(e){}
    let serveur = false;
    try{
      const r = await fetch("/api/difficulte", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ jeu: JEU_ID, valeurs: p }) });
      const d = await r.json(); serveur = !!(d && d.ok);
    }catch(e){}
    return { serveur, nb: Object.keys(p).length };
  }

  function ligne(e){
    const v = +valeurs[e.id] || 0, defaut = +e.difficulte || 0;
    const niveaux = (e.niveaux || (enigmes && enigmes.escales ? ["tous les grades"] : ["CM1", "CM2"])).join(" + ");
    return `<tr data-id="${esc(e.id)}"><td><b>${esc(e.id)}</b></td><td>${esc(e.titre)}<br><small style="opacity:.65">${esc(e.type)} · ${niveaux}${defaut ? ` · réglage du jeu : ${defaut > 0 ? "+" : ""}${defaut}` : ""}</small></td>
      <td class="pd-ctl"><button type="button" class="pd-moins" aria-label="Plus facile">−</button><span class="pd-val ${v ? (v < 0 ? "neg" : "pos") : ""}">${LIBELLES[v]}</span><button type="button" class="pd-plus" aria-label="Plus difficile">+</button></td></tr>`;
  }
  function contenu(){
    const immersif = !!(enigmes && enigmes.escales);
    const salles = enigmes ? (enigmes.salles || enigmes.escales || []) : [];
    return `<p style="margin:0 0 8px;font-size:.9rem">${immersif
      ? "Le réglage <b>s'ajoute</b> au grade de l'équipe : +1 décale l'énigme d'un grade vers le haut (données et consigne du grade au-dessus), −1 vers le bas ; le grade le plus bas donne l'aide renforcée (premier indice offert, un choix faux écarté). Les extrémités sont plafonnées."
      : "Le réglage <b>s'ajoute</b> au palier choisi par l'équipe. Départ CM1 : −1 aide renforcée · +1 données du CM2 · +2 défi (indices −2 pts de plus). Départ CM2 : −2 aide renforcée · −1 données du CM1 · +1 défi. Découverte : +1 données du CM1 · +2 données du CM2."}</p>
      ${salles.map(s => `<h4 style="margin:12px 0 4px">${esc((s.titre ? (immersif ? "Étape " : "Salle ") + (s.num != null ? s.num : s.numero) + " — " + s.titre : "Salle " + (s.num != null ? s.num : s.numero)))}</h4>
        <table class="pd-table">${(s.enigmes || []).map(ligne).join("")}</table>`).join("") || "<p>Les énigmes du jeu n'ont pas pu être chargées.</p>"}`;
  }

  function styles(){
    if(document.getElementById("style-prof-difficulte")) return;
    const s = document.createElement("style"); s.id = "style-prof-difficulte";
    s.textContent = `
      #prof-difficulte{position:fixed;inset:0;z-index:300;background:rgba(0,0,0,.7);display:flex;align-items:center;justify-content:center;padding:12px}
      #prof-difficulte .pd-boite{background:#fff;color:#222;border-radius:14px;max-width:760px;width:100%;max-height:92vh;display:flex;flex-direction:column;overflow:hidden}
      #prof-difficulte .pd-tete{padding:14px 18px;background:#4a2c8a;color:#fff;font-weight:bold}
      #prof-difficulte .pd-corps{padding:12px 18px;overflow:auto;flex:1}
      #prof-difficulte .pd-pied{padding:10px 18px;border-top:1px solid #ddd;display:flex;gap:8px;flex-wrap:wrap;align-items:center}
      #prof-difficulte button{font:inherit;border:0;border-radius:8px;padding:6px 14px;cursor:pointer;background:#e9e3f7;color:#2c1a5c;font-weight:bold}
      #prof-difficulte .pd-pied .principal{background:#4a2c8a;color:#fff}
      #prof-difficulte table{width:100%;border-collapse:collapse}#prof-difficulte td{padding:5px 6px;border-bottom:1px solid #eee;vertical-align:middle}
      #prof-difficulte .pd-ctl{white-space:nowrap;text-align:right}
      #prof-difficulte .pd-ctl button{width:34px;font-size:1.1rem;padding:2px 0}
      #prof-difficulte .pd-val{display:inline-block;min-width:190px;text-align:center;font-size:.85rem}
      #prof-difficulte .pd-val.neg{color:#14532d}#prof-difficulte .pd-val.pos{color:#7a3d00;font-weight:bold}
      #prof-difficulte .pd-msg{font-size:.85rem;flex:1;min-width:180px}`;
    document.head.appendChild(s);
  }
  async function ouvrir(){
    styles();
    await charger();
    fermer();
    const el = document.createElement("div");
    el.id = "prof-difficulte"; el.setAttribute("role", "dialog"); el.setAttribute("aria-label", "Difficulté énigme par énigme");
    el.innerHTML = `<div class="pd-boite"><div class="pd-tete">🎚️ Difficulté énigme par énigme</div><div class="pd-corps">${contenu()}</div>
      <div class="pd-pied"><span class="pd-msg" role="status"></span>
        <button type="button" class="pd-zero">Tout remettre à 0</button><button type="button" class="pd-lien">🔗 Copier le lien élèves</button>
        <button type="button" class="pd-fermer">Fermer</button><button type="button" class="principal pd-ok">Enregistrer pour la classe</button></div></div>`;
    document.body.appendChild(el);
    const msg = t => { el.querySelector(".pd-msg").textContent = t; };
    el.querySelector(".pd-corps").addEventListener("click", ev => {
      const b = ev.target.closest(".pd-moins, .pd-plus"); if(!b) return;
      const tr = b.closest("tr"), id = tr.dataset.id;
      valeurs[id] = borne((+valeurs[id] || 0) + (b.classList.contains("pd-plus") ? 1 : -1));
      const v = valeurs[id], sp = tr.querySelector(".pd-val");
      sp.textContent = LIBELLES[v]; sp.className = "pd-val " + (v ? (v < 0 ? "neg" : "pos") : "");
    });
    el.querySelector(".pd-zero").addEventListener("click", () => { valeurs = {}; el.querySelector(".pd-corps").innerHTML = contenu(); msg("Tous les réglages sont remis à 0 (pas encore enregistré)."); });
    el.querySelector(".pd-fermer").addEventListener("click", fermer);
    el.querySelector(".pd-lien").addEventListener("click", async () => {
      const l = lien();
      try{ await navigator.clipboard.writeText(l); msg("Lien copié : " + l); }catch(e){ msg("Lien : " + l); }
    });
    el.querySelector(".pd-ok").addEventListener("click", async () => {
      const r = await enregistrer();
      msg(r.nb ? `✓ ${r.nb} énigme(s) réglée(s), ${r.serveur ? "envoyé aux postes élèves (serveur local) et " : ""}gardé sur cet ordinateur.${r.serveur ? "" : " Sans serveur local : utilisez « Copier le lien élèves »."}`
                : `✓ Aucun réglage : les énigmes sont jouées au palier choisi.`);
    });
  }
  function fermer(){ const el = document.getElementById("prof-difficulte"); if(el) el.remove(); }

  function bouton(){
    const zone = document.querySelector(".actions, .barre");
    if(!zone || zone.querySelector(".btn-prof-difficulte")) return;
    const b = document.createElement("button");
    b.type = "button"; b.className = "bleu btn-prof-difficulte";
    b.title = "Avant la partie : rendre une énigme plus facile ou plus difficile, sans changer le palier de toute la salle";
    b.textContent = "🎚️ Difficulté par énigme";
    b.addEventListener("click", ouvrir);
    zone.appendChild(b);
  }
  if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", bouton); else bouton();
  window.PROF_DIFFICULTE = { ouvrir, fermer, charger, enregistrer, lien, propres, get valeurs(){ return valeurs; }, JEU_ID };
})();
