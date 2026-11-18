/* ============================================================
   FIN DE SÉANCE EN UN CLIC (A5) — mise à jour du passeport
   ------------------------------------------------------------
   Appelé par resultats.html?fin=<jeu> (bouton « Terminer la séance »
   de l'espace enseignant), après le bilan de séance imprimable
   (rapport-seance.js). Pour chaque équipe de la séance, on retrouve
   les élèves (composition des équipes du passeport, réglage « Temps
   majoré », sinon le nom de l'équipe = un élève ou une liste de
   prénoms) et on propose une note par compétence du jeu :
     • détail énigme par énigme disponible : réussite du premier coup
       sur les énigmes de la leçon — 75 % et plus « Acquis »,
       40 % et plus « En cours », sinon « Non acquis » ;
     • sinon, score global de la partie avec les mêmes seuils.
   Une note posée À LA MAIN par l'enseignant n'est JAMAIS remplacée ;
   une note d'une séance précédente est remplacée par la plus récente.
   Chaque note ajoutée porte src:"seance" (repérable, modifiable dans
   passeport.html comme les autres). Données : navigateur de l'enseignant
   (localStorage « escape_passeport »), rien n'est envoyé ailleurs.
   ============================================================ */
(function(){
  "use strict";
  const SEUIL_A = 75, SEUIL_E = 40;
  const norm = s => String(s == null ? "" : s).normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/\s+/g, " ").trim().toLowerCase();
  const noteDe = pc => pc >= SEUIL_A ? "A" : pc >= SEUIL_E ? "E" : "N";

  /** Élèves d'une équipe : composition connue, sinon nom = élève, sinon liste « Léa, Tom et Inès ». */
  function elevesDe(equipe, eleves, compositions){
    const n = norm(equipe);
    const cle = Object.keys(compositions || {}).find(k => norm(k) === n);
    if(cle) return (compositions[cle] || []).map(e => eleves.find(x => norm(x) === norm(e))).filter(Boolean);
    const seul = eleves.find(x => norm(x) === n);
    if(seul) return [seul];
    const morceaux = String(equipe || "").split(/\s*(?:,|;|&|\+|\bet\b)\s*/i).map(norm).filter(Boolean);
    return eleves.filter(x => morceaux.includes(norm(x)) || morceaux.includes(norm(x).split(" ")[0]));
  }
  /**
   * @param o { parties, jeu, competences:[{cle, lecon}], passeport:{eleves, notes}, compositions, jour }
   * @return { passeport, ajoutees, eleves:[…], equipesSansEleve:[…] }
   */
  function majPasseport(o){
    const P = { eleves: (o.passeport && o.passeport.eleves) || [], notes: JSON.parse(JSON.stringify((o.passeport && o.passeport.notes) || {})) };
    const comps = o.competences || [];
    const jour = o.jour || new Date().toISOString().slice(0, 10);
    const t = new Date().toISOString();
    const res = { passeport: P, ajoutees: 0, gardees: 0, eleves: [], equipesSansEleve: [] };
    if(!comps.length) return res;
    // une équipe = sa dernière partie de la séance (une partie terminée l'emporte)
    const parEquipe = new Map();
    for(const r of o.parties || []){
      if(!r || r.jeu !== o.jeu || r.mode === "solo") continue;
      const k = norm(r.eleve); const cur = parEquipe.get(k);
      if(!cur || (!!r.termine > !!cur.termine) || (!!r.termine === !!cur.termine && String(r.date) > String(cur.date))) parEquipe.set(k, r);
    }
    for(const r of parEquipe.values()){
      const qui = elevesDe(r.eleve, P.eleves, o.compositions);
      if(!qui.length){ res.equipesSansEleve.push(String(r.eleve || "(sans nom)")); continue; }
      // taux de réussite du premier coup par leçon (détail N12), sinon score global
      const parLecon = {};
      for(const n of Array.isArray(r.detail) ? r.detail : []){
        if(!n || n.id === "coffre" || !n.l) continue;
        const s = parLecon[n.l] || (parLecon[n.l] = { n: 0, pc: 0 }); s.n++; if(n.pc) s.pc++;
      }
      const global = r.scoreMax ? Math.round(100 * (+r.score || 0) / r.scoreMax) : null;
      for(const c of comps){
        const s = c.lecon && parLecon[c.lecon];
        const pc = s && s.n ? Math.round(100 * s.pc / s.n) : (Object.keys(parLecon).length ? null : global);
        if(pc == null) continue;                              // leçon pas jouée (escale non faite) : rien
        for(const e of qui){
          const notes = P.notes[e] || (P.notes[e] = {});
          const ex = notes[c.cle];
          if(ex && ex.src !== "seance"){ res.gardees++; continue; }   // note de l'enseignant : jamais remplacée
          notes[c.cle] = { v: noteDe(pc), date: jour, t, src: "seance", pc };
          res.ajoutees++;
        }
      }
      qui.forEach(e => { if(!res.eleves.includes(e)) res.eleves.push(e); });
    }
    return res;
  }
  /** Compétences d'un jeu, avec les mêmes clés que passeport.html (« <dossier>|<rang> »). */
  async function competencesDuJeu(catalogue, jeu, lireJson){
    const j = ((catalogue && catalogue.jeux) || []).find(x => x.dossier === jeu || x.id === jeu);
    if(!j || !j.dossier) return [];
    const a4 = await lireJson(`${j.dossier}/assets/data/lecons-a4.json`);
    const l = a4 && a4.lecons ? Object.entries(a4.lecons).filter(([, x]) => x && x.competence).map(([k]) => k) : (j.classique === false ? [] : [""]);
    return l.map((lecon, i) => ({ cle: `${j.dossier}|${i + 1}`, lecon }));
  }
  window.FIN_SEANCE = { SEUIL_A, SEUIL_E, elevesDe, majPasseport, competencesDuJeu, noteDe };
})();
