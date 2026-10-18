/* ============================================================
   CORRECTION COLLECTIVE (D7) — réponses des 5 énigmes de la Déclaration
   ------------------------------------------------------------
   Ce jeu écrit ses énigmes dans enigmes.js (une par salle) : leurs bonnes
   réponses sont donc listées ici, pour commun/js/correction-collective.js.
   Si une énigme change, mettre à jour la salle correspondante.
   CORRECTION_JEU.enigmes(niveau, salle) → [{ id, titre, consigne, reponse (HTML) }]
   ============================================================ */
var CORRECTION_JEU = (function(){
  const liste = l => `<ul class="cc-liste">${l.map(x => `<li>${x}</li>`).join("")}</ul>`;
  const rep = t => `<b class="cc-rep">${t}</b>`;
  const lettres = mot => `<p class="cc-mot">${[...mot].map(l => `<span class="cc-lettre">${l}</span>`).join("")}</p>`;
  const EVENEMENTS = [
    ["États généraux réunis à Versailles", "mai 1789"], ["Serment du Jeu de paume", "20 juin 1789"],
    ["Prise de la Bastille", "14 juillet 1789"], ["Adoption de la Déclaration des droits", "26 août 1789"],
    ["Marche des femmes à Versailles", "5 octobre 1789"]];
  const LIBELLES_PLAN = { pres: "Président", gauche: "Tribune gauche", droite: "Tribune droite", centre: "Centre", fond: "Tribune du fond", secret: "Secrétaire", date: "Date au fronton", lieu: "Lieu" };
  function enigmes(niveau, n){
    const cm1 = niveau === "CM1";
    switch(n){
      case 1: return [{ id: "1", titre: "Le cahier de doléances", consigne: "Classer dans les cases, dans le bon ordre, les lettres marquées du texte (certaines sont des pièges).",
        reponse: `<p>Le mot caché est :</p>${lettres("LIBERTÉ")}<p>Les lettres pièges : ${cm1 ? "A et S" : "S et P"}.</p>` }];
      case 2: return [cm1
        ? { id: "2", titre: "La Marseillaise mystérieuse", consigne: "Relier chaque extrait à l'image qui lui correspond.",
            reponse: liste(["« Aux armes, citoyens ! » ⟷ " + rep("🏰 Prise de la Bastille"), "« Allons enfants de la Patrie » ⟷ " + rep("🚶 Volontaires en marche"), "« Le jour de gloire est arrivé » ⟷ " + rep("🚩 Drapeau tricolore hissé")]) }
        : { id: "2", titre: "Les 5 grands événements de 1789", consigne: "Remettre les événements dans l'ordre chronologique.",
            reponse: `<ol class="cc-liste">${EVENEMENTS.map(e => `<li>${rep(e[0])} <small>(${e[1]})</small></li>`).join("")}</ol>` }];
      case 3: return [{ id: "3", titre: "Le rébus de la Déclaration", consigne: "Trouver les trois mots de la phrase à l'aide des rébus.",
        reponse: `<p>« Les hommes naissent ${rep("libres")} et ${rep("égaux")} en ${rep("droits")}. »</p>` }];
      case 4: {
        const paires = [["👑 Louis XVI", "« J'ai peu de confiance dans les assemblées. »"], ["🎤 Mirabeau", "« Nous sommes ici par la volonté du peuple. »"], ["🔊 Danton", "« De l'audace, encore de l'audace ! »"], ["⚖️ Robespierre", "« La vertu sans laquelle la terreur est funeste. »"]];
        if(!cm1){ paires.push(["🏛️ Bailly", "« La Bastille est prise ! »"], ["✒️ Olympe de Gouges", "« La femme naît libre et demeure égale à l'homme. »"]); }
        return [{ id: "4", titre: "Les grands personnages", consigne: "Relier chaque personnage à sa citation.", reponse: liste(paires.map(p => `${p[0]} ⟷ ${rep(p[1])}`)) }];
      }
      case 5: {
        const bons = (typeof PLAN_REPONSES !== "undefined" ? PLAN_REPONSES : {})[niveau] || {};
        return [{ id: "5", titre: "Le mécanisme de l'Assemblée", consigne: "Placer chaque étiquette dans la bonne case du plan de l'Assemblée.",
          reponse: liste(Object.keys(bons).map(k => `${LIBELLES_PLAN[k] || k} → ${rep(bons[k])}`)) }];
      }
    }
    return [];
  }
  return { enigmes };
})();
