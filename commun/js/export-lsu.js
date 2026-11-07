/* ============================================================
   EXPORT DU PASSEPORT AU FORMAT LSU (amélioration N24) — tronc commun
   ------------------------------------------------------------
   Au moment des bilans périodiques, l'enseignant reporte dans le LSU (Livret Scolaire Unique)
   ce que le passeport de compétences (C3) a cumulé. Le LSU a ses propres intitulés (éléments de
   programme, compétences du cycle 3) : ce module regroupe les compétences notées de l'élève sous
   l'intitulé LSU le plus proche (table : commun/donnees/lsu.js, qui s'appuie sur la correspondance
   du bandeau BO, C2) et propose, par intitulé, un niveau LSU SUGGÉRÉ :

       toutes les compétences notées sont « Acquis »           → Objectifs atteints
       aucune « Acquis » ni « En cours » (toutes « Non acquis ») → Objectifs non atteints
       sinon                                                   → Objectifs partiellement atteints
       (« dépassés » n'est jamais proposé : c'est le jugement de l'enseignant)

   C'est UNE AIDE, PAS UNE VALIDATION : rien n'est envoyé nulle part ; le résultat est un tableau
   à lire, un texte à copier-coller et un fichier CSV. L'enseignant garde la main sur la saisie.
   Une évaluation incomplète (compétences non notées) et une correspondance approchée sont
   signalées sur chaque ligne.

   API : EXPORT_LSU.construire({ eleves, notes, competences, depuis, donnees, catalogue })
         → { lignes, csv, texte, avertissement, approchees, partielles }
     eleves       [prénoms] ; notes { élève: { cle: {v:"N|E|A", date} } }
     competences  [{ cle, jeu, lecon, titre, matiere, texte }]  (PASSEPORT.COMPETENCES)
     depuis       "AAAA-MM-JJ" facultatif : ne compte que les notes de cette date ou plus récentes
     donnees      la table LSU (commun/donnees/lsu.js) ; catalogue : CATALOGUE (bandeau BO, C2)
   Utilisé par passeport.html (bouton « Exporter pour le LSU »).
   ============================================================ */
(function(){
  const LIB = { N: "Non acquis", E: "En cours", A: "Acquis" };
  const ORDRE_DISC = ["Histoire et géographie", "Enseignement moral et civique", "Sciences et technologie"];

  function discipline(jeuId, donnees, catalogue){
    const j = catalogue && catalogue.jeux && catalogue.jeux.find(x => x.dossier === jeuId || x.id === jeuId);
    const cle = j && (j.programme || []).find(k => donnees.disciplines[k]);
    return { discipline: cle ? donnees.disciplines[cle] : "(discipline à préciser)", programmes: j ? (j.programme || []).map(k => catalogue.programmes && catalogue.programmes[k] && catalogue.programmes[k].texte).filter(Boolean) : [] };
  }
  function cible(c, donnees, catalogue){
    const ligne = ((donnees.correspondance || {})[c.jeu] || {})[c.lecon];
    const item = ligne && donnees.items[ligne[0]];
    const base = discipline(c.jeu, donnees, catalogue);
    if(item) return { id: ligne[0], discipline: item.discipline, type: item.type, libelle: item.libelle, exacte: ligne[1] === "=", programmes: base.programmes };
    return { id: "?" + base.discipline, discipline: base.discipline, type: "À rattacher", libelle: "(à rattacher dans votre LSU)", exacte: false, programmes: base.programmes };
  }
  function niveau(n, donnees){
    if(!n.N && !n.E && !n.A) return "";
    if(n.A && !n.N && !n.E) return donnees.niveaux.A;
    if(!n.A && !n.E) return donnees.niveaux.N;
    return donnees.niveaux.E;
  }
  const csvCase = v => /[;"\n\r]/.test(String(v)) ? '"' + String(v).replace(/"/g, '""') + '"' : String(v);

  function construire(o){
    const donnees = o.donnees, catalogue = o.catalogue, depuis = o.depuis || "";
    const comps = (o.competences || []).map(c => Object.assign({}, c, { _cible: cible(c, donnees, catalogue) }));
    const lignes = [];
    for(const eleve of (o.eleves || [])){
      const notes = (o.notes || {})[eleve] || {}, groupes = new Map();
      for(const c of comps){
        const t = c._cible;
        if(!groupes.has(t.id)) groupes.set(t.id, { t, N: 0, E: 0, A: 0, total: 0, notees: 0, jeux: new Set(), derniere: "", exacte: true });
        const g = groupes.get(t.id);
        g.total++; g.jeux.add(c.titre); if(!t.exacte) g.exacte = false;
        const n = notes[c.cle];
        if(n && LIB[n.v] && (!depuis || String(n.date || "") >= depuis)){ g[n.v]++; g.notees++; if((n.date || "") > g.derniere) g.derniere = n.date || ""; }
      }
      for(const g of groupes.values()){
        if(!g.notees) continue;        // rien d'évalué sous cet intitulé : rien à reporter
        const detail = [g.A ? `${g.A} acquise${g.A > 1 ? "s" : ""}` : "", g.E ? `${g.E} en cours` : "", g.N ? `${g.N} non acquise${g.N > 1 ? "s" : ""}` : ""].filter(Boolean).join(", ");
        lignes.push({
          eleve, discipline: g.t.discipline, type: g.t.type, intitule: g.t.libelle, niveau: niveau(g, donnees),
          acquises: g.A, enCours: g.E, nonAcquises: g.N, notees: g.notees, total: g.total,
          partielle: g.notees < g.total, approchee: !g.exacte, derniere: g.derniere,
          detail: `${detail} — ${g.notees} notée${g.notees > 1 ? "s" : ""} sur ${g.total}`,
          jeux: [...g.jeux].join(" ; "), programme: g.t.programmes.join(" ; ")
        });
      }
    }
    const rang = d => { const i = ORDRE_DISC.indexOf(d); return i < 0 ? 99 : i; };
    lignes.sort((a, b) => (o.eleves.indexOf(a.eleve) - o.eleves.indexOf(b.eleve)) || (rang(a.discipline) - rang(b.discipline)) || a.type.localeCompare(b.type, "fr") * -1 || a.intitule.localeCompare(b.intitule, "fr"));
    return { lignes, csv: versCsv(lignes), texte: versTexte(lignes, o.eleves, donnees, depuis), avertissement: donnees.avertissement,
      approchees: lignes.filter(l => l.approchee).length, partielles: lignes.filter(l => l.partielle).length };
  }

  function versCsv(lignes){
    const t = [["eleve", "discipline_LSU", "type", "intitule_LSU", "niveau_suggere", "detail", "evaluation_complete", "correspondance", "derniere_date", "jeux", "programme_de_reference"]];
    for(const l of lignes) t.push([l.eleve, l.discipline, l.type, l.intitule, l.niveau, l.detail, l.partielle ? "partielle" : "complète", l.approchee ? "approchée" : "exacte", l.derniere, l.jeux, l.programme]);
    return "﻿" + t.map(r => r.map(csvCase).join(";")).join("\r\n");
  }
  function versTexte(lignes, eleves, donnees, depuis){
    const out = [`AIDE À LA SAISIE LSU — ${donnees.avertissement}`, depuis ? `Notes prises en compte depuis le ${depuis}.` : ""].filter(Boolean);
    for(const e of eleves){
      const mes = lignes.filter(l => l.eleve === e);
      out.push("", e.toUpperCase());
      if(!mes.length){ out.push("  (aucune compétence notée dans le passeport)"); continue; }
      let disc = null;
      for(const l of mes){
        if(l.discipline !== disc){ disc = l.discipline; out.push(`  ${disc}`); }
        out.push(`    • ${l.type === "Compétence" ? "Compétence" : "Élément"} : ${l.intitule} → ${l.niveau} (${l.detail})${l.partielle ? " [évaluation partielle]" : ""}${l.approchee ? " [correspondance approchée]" : ""}`);
      }
    }
    return out.join("\n");
  }

  const API = { construire, LIB, niveau };
  if(typeof window !== "undefined") window.EXPORT_LSU = API;
  if(typeof module !== "undefined") module.exports = API;
})();
