/* ============================================================
   FICHE SYNTHÈSE POUR LES FAMILLES (amélioration N30) — tronc commun
   ------------------------------------------------------------
   Le passeport de compétences (C3) et la fiche imprimable (C5) parlent le langage du programme. Les
   familles n'ont aucun retour simple sur la séance. Ce module fabrique, SANS rédaction de l'enseignant,
   une fiche d'une demi-page : le nom du jeu, 2 ou 3 points travaillés dits en langage de tous les jours
   (commun/donnees/familles.js), une phrase sur le déroulé du jeu, et un « mot de l'enseignant » facultatif.

   D'où viennent les points :
     • un ÉLÈVE : les compétences notées dans le passeport pour ce jeu, les mieux maîtrisées d'abord
       (« bien en place », puis « en progrès », puis « à consolider ») ; jamais de note chiffrée ni de
       mot « non acquis » ;
     • une ÉQUIPE : les leçons des énigmes de sa dernière partie du jeu (compte-rendu N12, champ « detail »),
       réussies d'abord ;
     • rien de noté (pas de passeport, pas de détail) : « pendant ce jeu, la classe a travaillé… » (les
       premières leçons du jeu), sans rien affirmer sur l'enfant.
   La fiche existe en deux versions : à imprimer (deux par feuille A4) et en texte à copier dans un ENT
   ou un cahier de liaison numérique. Rien n'est envoyé nulle part.

   API : FICHE_FAMILLE.construire({ jeu, sujet:{type:"eleve"|"equipe", nom}, notes, competences,
           resultats, donnees (FAMILLES), catalogue, mot }) → { titreJeu, sujet, points:[{texte,niveau,etiquette}],
           neutre, deroule, mot, texte, date }
         FICHE_FAMILLE.jeuxDe(...) : jeux utilisables (au moins une leçon formulée)
   ============================================================ */
(function(){
  const ORDRE = { A: 0, E: 1, N: 2 };
  const maj = s => s ? s.charAt(0).toUpperCase() + s.slice(1) : s;
  const fr = d => d ? new Date(d.length > 10 ? d : d + "T12:00:00").toLocaleDateString("fr-FR", { day: "numeric", month: "long", year: "numeric" }) : "";

  function jeuxDe(competences, donnees){
    return [...new Set(competences.map(c => c.jeu))].filter(j => donnees.jeux[j]);
  }
  /** Niveau d'une leçon pour une équipe : réussie → bien en place ; jouée mais pas réussie → en progrès. */
  function niveauEquipe(detail, lecon){
    const lignes = (detail || []).filter(n => n.l === lecon);
    if(!lignes.length) return "";
    return lignes.every(n => n.ok) ? "A" : "E";
  }
  function construire(o){
    const D = o.donnees, J = D.jeux[o.jeu];
    if(!J) throw new Error("Jeu sans formulation pour les familles : " + o.jeu);
    const comps = (o.competences || []).filter(c => c.jeu === o.jeu && J.lecons[c.lecon]);
    const info = (o.catalogue && o.catalogue.jeux || []).find(j => j.dossier === o.jeu || j.id === o.jeu) || {};
    const sujet = o.sujet || { type: "eleve", nom: "" };
    let candidats = [], date = "";
    if(sujet.type === "equipe"){
      const parties = (o.resultats || []).filter(r => r.jeu === o.jeu && String(r.eleve).trim().toLowerCase() === String(sujet.nom).trim().toLowerCase() && Array.isArray(r.detail))
        .sort((a, b) => String(b.date || "").localeCompare(String(a.date || "")));
      const p = parties[0];
      if(p){
        date = String(p.date || "").slice(0, 10);
        candidats = comps.map(c => ({ c, niveau: niveauEquipe(p.detail, c.lecon) })).filter(x => x.niveau);
      }
    } else {
      const n = (o.notes || {})[sujet.nom] || {};
      candidats = comps.filter(c => n[c.cle] && D.niveaux[n[c.cle].v]).map(c => ({ c, niveau: n[c.cle].v, date: n[c.cle].date || "" }));
      date = candidats.reduce((m, x) => x.date > m ? x.date : m, "");
    }
    candidats.sort((a, b) => ORDRE[a.niveau] - ORDRE[b.niveau] || a.c.rang - b.c.rang);
    let neutre = false, retenus = candidats.slice(0, 3);
    if(!retenus.length){            // rien de noté : on dit seulement ce que le jeu fait travailler
      neutre = true;
      retenus = comps.slice(0, 3).map(c => ({ c, niveau: "" }));
    }
    const points = retenus.map(x => ({ texte: maj(J.lecons[x.c.lecon]), niveau: x.niveau, etiquette: x.niveau ? D.niveaux[x.niveau] : "" }));
    const mot = String(o.mot || "").trim();
    const sujetTexte = sujet.type === "equipe" ? `l'équipe « ${sujet.nom} »` : sujet.nom;
    const titreJeu = info.titre || o.jeu;
    const lignes = [
      `Un escape game en classe : « ${titreJeu} »`,
      sujet.nom ? `${maj(sujetTexte)}${date ? " — " + fr(date) : ""}` : "",
      "",
      J.deroule,
      "",
      neutre ? "Pendant ce jeu, la classe a travaillé à :" : `${sujet.type === "equipe" ? "Ce que l'équipe a travaillé" : "Ce que " + sujet.nom + " a travaillé"} :`,
      ...points.map(p => `• ${p.texte}${p.etiquette ? " (" + p.etiquette + ")" : ""}`),
      mot ? "" : null, mot ? `Mot de l'enseignant : ${mot}` : null,
      "", "Pas de note chiffrée : ce sont des repères pour en parler ensemble. N'hésitez pas à demander à l'enseignant."
    ].filter(l => l !== null && l !== undefined);
    return { titreJeu, sujet: sujetTexte, nom: sujet.nom, type: sujet.type, points, neutre, deroule: J.deroule, mot, date, texte: lignes.join("\n") };
  }

  const API = { construire, jeuxDe, niveauEquipe, maj };
  if(typeof window !== "undefined") window.FICHE_FAMILLE = API;
  if(typeof module !== "undefined") module.exports = API;
})();
