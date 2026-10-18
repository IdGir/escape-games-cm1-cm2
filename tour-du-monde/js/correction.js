/* ============================================================
   CORRECTION COLLECTIVE (D7) — réponses des 5 énigmes du Tour du monde
   ------------------------------------------------------------
   Ce jeu écrit ses énigmes dans enigmes.js (une par salle) : les réponses sont
   lues dans ses propres constantes (CARTE_NIVEAUX, ITINERAIRES, CLIMATS, TRAJETS,
   TRANSPORTS, VILLES_FUSEAU, HEURE_LONDRES), pour commun/js/correction-collective.js.
   CORRECTION_JEU.enigmes(niveau, salle) → [{ id, titre, consigne, reponse (HTML) }]
   ============================================================ */
var CORRECTION_JEU = (function(){
  const liste = l => `<ul class="cc-liste">${l.map(x => `<li>${x}</li>`).join("")}</ul>`;
  const rep = t => `<b class="cc-rep">${t}</b>`;
  const h = n => String(n).padStart(2, "0") + " h";
  function planisphere(niveau){
    const cfg = CARTE_NIVEAUX[niveau] || CARTE_NIVEAUX.CM2;
    const terres = cfg.terres.map(t => `<path d="${FORMES_CARTE[t.id]}" fill="#cfe5d0" stroke="#2f7d6b" stroke-width="1.5"/><text x="${centreForme(t.id).x}" y="${centreForme(t.id).y}" text-anchor="middle" font-size="15" font-weight="bold" fill="#14532d">${t.nom}</text>`).join("");
    const eaux = cfg.eaux.map(o => { const g = OCEANS_CARTE[o.id]; return `<ellipse cx="${g.cx}" cy="${g.cy}" rx="${g.rx}" ry="${g.ry}" fill="rgba(59,110,165,.18)" stroke="#3b6ea5" stroke-dasharray="4 3"/><text x="${g.cx}" y="${g.cy + 4}" text-anchor="middle" font-size="13" font-style="italic" fill="#1d3a8a">${o.nom.replace("Océan ", "")}</text>`; }).join("");
    return `<svg viewBox="0 0 800 400" style="width:100%;max-width:760px;background:#eaf3fa;border-radius:10px" role="img" aria-label="Planisphère complété">
      <line x1="0" y1="200" x2="800" y2="200" stroke="#a33327" stroke-width="2" stroke-dasharray="9 6"/><line x1="400" y1="0" x2="400" y2="400" stroke="#2f7d6b" stroke-width="2" stroke-dasharray="9 6"/>${eaux}${terres}</svg>`;
  }
  function enigmes(niveau, n){
    const cm1 = niveau === "CM1";
    switch(n){
      case 1: return [{ id: "1", titre: "Le grand planisphère du Reform Club", consigne: "Poser le nom de chaque continent et de chaque océan sur la carte du monde.", reponse: planisphere(niveau) }];
      case 2: return [{ id: "2", titre: "Le carnet de route du « Mongolia »", consigne: "Remettre les escales dans l'ordre du voyage, et répondre à la question sur le canal de Suez.",
        reponse: `<ol class="cc-liste">${(ITINERAIRES[niveau] || ITINERAIRES.CM2).slice().sort((a, b) => a.rang - b.rang).map(e => `<li>${rep(e.txt)} <small>(${e.detail})</small></li>`).join("")}</ol>
          <p>${cm1 ? "À quoi sert le canal de Suez ?" : "Le canal de Suez, ouvert en 1869, relie :"} → ${rep(cm1 ? "à relier deux mers pour raccourcir le voyage" : "la mer Méditerranée et la mer Rouge")}</p>` }];
      case 3: return [{ id: "3", titre: "Le carnet des climats de Mrs Aouda", consigne: "Associer chaque paysage à son climat.",
        reponse: liste((CLIMATS[niveau] || CLIMATS.CM2).map(p => `${p.emoji} ${p.nom} ⟷ ${rep(p.climat)}`)) }];
      case 4: return [{ id: "4", titre: "Le calcul du timonier", consigne: "Pour chaque étape : choisir le bon moyen de transport et calculer la distance réelle (1 cm sur la carte = 200 km).",
        reponse: liste((TRAJETS[niveau] || TRAJETS.CM2).map(t => `${t.de} : ${rep((TRANSPORTS.find(x => x.id === t.bon) || {}).nom || t.bon)} · ${t.cm} cm × 200 = ${rep(t.km + " km")}`)) }];
      case 5: return [{ id: "5", titre: "L'horloge du monde — l'énigme du 80ᵉ jour", consigne: "Quand il est midi à Greenwich, quelle heure est-il dans chaque ville ? Et que s'est-il passé pour Phileas Fogg ?",
        reponse: liste((VILLES_FUSEAU[niveau] || VILLES_FUSEAU.CM2).map(v => `${v.nom} (${v.decalage > 0 ? "+" : ""}${v.decalage} h) → ${rep(h((HEURE_LONDRES + v.decalage + 24) % 24))}`))
          + `<p>Fogg a voyagé toujours vers l'est : ${rep("il a gagné un jour")} (79 jours au lieu de 80).</p>` }];
    }
    return [];
  }
  return { enigmes };
})();
