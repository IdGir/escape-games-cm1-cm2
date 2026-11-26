/* ============================================================
   IMPORT DES PARTIES DE « MISSION GÉOGRAPHIQUE » — convertisseur commun
   ------------------------------------------------------------
   Lit une partie de Mission géo, quelle que soit sa forme, et la met au
   format commun « mission-geo-partie » (version 2), que comprennent :
     - mission-geo/ (l'application actuelle, envoi automatique au PC de la classe),
     - importer-parties.html (tableau de bord : glisser-déposer des fichiers),
     - serveur.py (/api/parties : rangées sur le PC de la classe, jamais publiées),
     - la future variante immersive immersifs/mission-geo/ (séance N → escale N,
       voir mission-geo/REFONTE-IMMERSIVE.md).
   Formes reconnues :
     1. sauvegarde de l'application (localStorage « mission_geo_annee_a_v1 »,
        bouton ⚙️ → Progression → Exporter, ou script de secours) : { version: 1, sessions: {s01: …}, indices, final, … } ;
     2. fichier du script de secours : { cle: "mission_geo_annee_a_v1", valeur: "<texte>" } ;
     3. une partie déjà au format commun (version 2).
   Aucune perte : on ne garde que ce qui est lisible, et l'on ne retire
   jamais une séance réussie lors d'une fusion. Aucun service externe.
   ============================================================ */
var MISSION_GEO_IMPORT = (function(){
  "use strict";
  const CLE_ANCIENNE = "mission_geo_annee_a_v1";
  const FORMAT = "mission-geo-partie";
  /* Les 16 séances de l'Année A (id de l'application → numéro → période). */
  const SEANCES = [
    ["s01", "Le grand départ", 1], ["s02", "Direction Dijon !", 1], ["s03", "Vivre à Clamecy, vivre dans une commune rurale", 1],
    ["s04", "Besançon, travailler en ville", 1], ["s05", "Profitons des loisirs de la montagne", 1], ["s06", "Étretat, station balnéaire", 2],
    ["s07", "Le littoral atlantique", 2], ["s08", "Niveaux de vie dans le monde", 2], ["s09", "Les pratiques alimentaires", 3],
    ["s10", "Les produits consommés", 3], ["s11", "Chaînes de production", 4], ["s12", "L'heure du ravitaillement", 4],
    ["s13", "L'eau en France : fleuves et massifs", 4], ["s14", "Le trajet de l'eau, de la source à la mer", 5],
    ["s15", "Besoin en eau", 5], ["s16", "Au secours, il n'y a plus d'eau !", 5]
  ].map(([id, titre, periode], i) => ({ id, numero: i + 1, titre, periode }));
  const PAR_ID = Object.fromEntries(SEANCES.map(s => [s.id, s]));
  /* Niveau de l'application → grade du modèle immersif (5 grades). */
  const GRADE_DE = { decouverte: "mousse", CM1: "matelot", CM2: "timonier" };

  const nombre = (v, def) => { const n = Number(v); return Number.isFinite(n) && n >= 0 ? n : def; };
  const date = v => { const t = typeof v === "string" ? Date.parse(v) : NaN; return Number.isFinite(t) ? new Date(t).toISOString() : null; };
  const texte = (v, max) => typeof v === "string" ? v.trim().slice(0, max || 80) : "";
  const idSeance = k => {
    const m = /^s?0*(\d{1,2})$/.exec(String(k).trim());
    const n = m ? +m[1] : 0;
    return n >= 1 && n <= 16 ? SEANCES[n - 1].id : "";
  };

  /** Trouve l'objet « sauvegarde » dans ce qui a été lu (fichier, localStorage, script de secours). */
  function deballer(brut){
    let o = brut;
    if(typeof o === "string"){ try{ o = JSON.parse(o); }catch(e){ return null; } }
    if(!o || typeof o !== "object") return null;
    if(o.cle === CLE_ANCIENNE && typeof o.valeur === "string"){ const dedans = deballer(o.valeur); return dedans ? Object.assign(dedans, { __exporte_le: o.exporte_le }) : null; }
    if(o[CLE_ANCIENNE] && typeof o[CLE_ANCIENNE] === "string") return deballer(o[CLE_ANCIENNE]);
    return o;
  }

  /**
   * Convertit en partie commune. Renvoie { ok, partie, alertes: [...], erreurs: [...] }.
   * options : { equipe, classe, grade, fichier } (l'enseignant peut corriger l'équipe ou imposer un grade).
   */
  function convertir(brut, options){
    options = options || {};
    const alertes = [], erreurs = [];
    const o = deballer(brut);
    if(!o){ return { ok: false, partie: null, alertes, erreurs: ["Fichier illisible : ce n'est pas un fichier de partie (texte JSON attendu)."] }; }
    const v2 = o.format === FORMAT;
    const sessions = v2 ? o.seances : o.sessions;
    if(!sessions || typeof sessions !== "object" || Array.isArray(sessions)){
      return { ok: false, partie: null, alertes, erreurs: ["Ce fichier ne contient pas de séances de Mission géo (rubrique « sessions » absente)."] };
    }
    const seances = {};
    for(const [k, s] of Object.entries(sessions)){
      const id = idSeance(v2 ? (s && s.id) || k : k);
      if(!id){ alertes.push("Séance inconnue ignorée : « " + texte(k, 20) + " »."); continue; }
      if(!s || typeof s !== "object"){ alertes.push("Séance " + PAR_ID[id].numero + " illisible : ignorée."); continue; }
      const r = {
        id, numero: PAR_ID[id].numero, titre: PAR_ID[id].titre,
        reussie: !!s.reussie, points: nombre(s.points, 0), maximum: nombre(s.maximum, null),
        duree: nombre(s.duree, null), date: date(s.date)
      };
      if(Array.isArray(s.resultats)) r.resultats = s.resultats.slice(0, 20).map(x => x && typeof x === "object" ? { reussi: !!x.reussi, essais: nombre(x.essais, 0), points: nombre(x.points, 0) } : null);
      if(s.date && !r.date) alertes.push("Séance " + r.numero + " : date illisible (gardée sans date).");
      seances[r.numero] = r;
    }
    const indices = [];
    for(const i of Array.isArray(o.indices) ? o.indices : []){
      const id = i && idSeance(i.session || i.numero);
      if(!id){ alertes.push("Indice sans séance reconnue : ignoré."); continue; }
      if(indices.some(x => x.session === id)) continue;
      const x = { session: id, numero: PAR_ID[id].numero, type: i.type === "fait" ? "fait" : "nombre", libelle: texte(i.libelle, 160) };
      if(x.type === "nombre"){ x.symbole = texte(i.symbole, 20); x.valeur = nombre(i.valeur, null); }
      else x.texte = texte(i.texte || i.valeur, 200);
      indices.push(x);
      if(!seances[x.numero]){ alertes.push("Indice de la séance " + x.numero + " présent sans la séance : la séance est comptée réussie."); seances[x.numero] = { id, numero: x.numero, titre: PAR_ID[id].titre, reussie: true, points: 0, maximum: null, duree: null, date: null }; }
    }
    for(const s of Object.values(seances)) if(s.reussie && !indices.some(i => i.session === s.id)) alertes.push("Séance " + s.numero + " réussie sans son indice dans le carnet (l'indice sera redonné en rejouant le dénouement).");
    const f = o.final && typeof o.final === "object" ? o.final : {};
    const niveau = ["CM1", "CM2"].includes(o.niveau) ? o.niveau : "CM2";
    const palier = o.palier === "decouverte" ? "decouverte" : "";
    const equipe = texte(options.equipe, 40) || texte(o.equipe, 40);
    if(!equipe) alertes.push("Nom d'équipe absent : à saisir avant l'import.");
    const dates = Object.values(seances).map(s => s.date).filter(Boolean).sort();
    const partie = {
      format: FORMAT, version: 2,
      equipe, classe: texte(options.classe, 40) || texte(o.classe, 40),
      niveau, palier, grade: options.grade || (v2 && o.grade) || GRADE_DE[palier || niveau],
      debut: date(o.debut) || dates[0] || null, derniere: dates[dates.length - 1] || null,
      erreurs: nombre(o.erreurs, 0),
      seances, indices,
      final: { pays: texte(f.pays, 40) || null, colonne: f.colonne != null ? texte(String(f.colonne), 4) : null, ligne: f.ligne != null ? texte(String(f.ligne), 4) : null,
               code: f.code != null ? texte(String(f.code), 12) : null, resolu: !!f.resolu },
      profil: o.profil && typeof o.profil === "object" ? Object.fromEntries(Object.entries(o.profil).filter(([, v]) => typeof v === "string" || typeof v === "number").map(([k, v]) => [k, typeof v === "string" ? v.slice(0, 80) : v])) : {},
      recompense: o.recompense && typeof o.recompense === "object" ? { active: !!o.recompense.active, titre: texte(o.recompense.titre, 120), texte: texte(o.recompense.texte, 600), media: texte(o.recompense.media, 80) } : null,
      reglages: o.reglages && typeof o.reglages === "object" ? o.reglages : undefined,
      source: v2 && o.source ? o.source : { format: CLE_ANCIENNE, version: nombre(o.version, 1), fichier: texte(options.fichier, 120), exporte_le: date(o.__exporte_le) },
      importe_le: new Date().toISOString()
    };
    if(!Object.keys(seances).length && !indices.length) alertes.push("Aucune séance commencée dans ce fichier.");
    return { ok: !erreurs.length, partie, alertes, erreurs };
  }

  /** Résumé pour un aperçu : séances réussies, points, dernier jour. */
  function resume(p){
    const ss = Object.values(p.seances || {});
    const reussies = ss.filter(s => s.reussie).map(s => s.numero).sort((a, b) => a - b);
    return { equipe: p.equipe, grade: p.grade, niveau: p.niveau, reussies, nbReussies: reussies.length,
             points: ss.reduce((t, s) => t + (s.points || 0), 0), indices: (p.indices || []).length,
             derniere: p.derniere, finale: !!(p.final && p.final.resolu) };
  }

  /** Fusion sans perte : une séance réussie le reste, on garde le meilleur score et la date la plus récente. */
  function fusionner(existante, nouvelle){
    if(!existante) return nouvelle;
    const p = JSON.parse(JSON.stringify(existante));
    for(const [n, s] of Object.entries(nouvelle.seances || {})){
      const a = p.seances[n];
      if(!a){ p.seances[n] = s; continue; }
      p.seances[n] = Object.assign({}, a, s, {
        reussie: !!(a.reussie || s.reussie), points: Math.max(a.points || 0, s.points || 0),
        date: [a.date, s.date].filter(Boolean).sort().pop() || null
      });
    }
    for(const i of nouvelle.indices || []) if(!p.indices.some(x => x.session === i.session)) p.indices.push(i);
    p.indices.sort((a, b) => a.numero - b.numero);
    if(nouvelle.final && nouvelle.final.resolu) p.final = nouvelle.final;
    else for(const k of ["pays", "colonne", "ligne", "code"]) if(p.final[k] == null && nouvelle.final && nouvelle.final[k] != null) p.final[k] = nouvelle.final[k];
    p.erreurs = Math.max(p.erreurs || 0, nouvelle.erreurs || 0);
    const dates = Object.values(p.seances).map(s => s.date).filter(Boolean).sort();
    p.debut = [p.debut, nouvelle.debut, dates[0]].filter(Boolean).sort()[0] || null;
    p.derniere = dates[dates.length - 1] || p.derniere || null;
    if(nouvelle.grade) p.grade = nouvelle.grade;
    p.importe_le = new Date().toISOString();
    return p;
  }

  /** Différence pour l'aperçu : séances ajoutées par l'import. */
  function nouveautes(existante, nouvelle){
    if(!existante) return Object.values(nouvelle.seances || {}).filter(s => s.reussie).map(s => s.numero);
    return Object.values(nouvelle.seances || {}).filter(s => s.reussie && !(existante.seances[s.numero] && existante.seances[s.numero].reussie)).map(s => s.numero);
  }

  /** Retour vers la sauvegarde de l'application actuelle (mission-geo/), pour reprendre sur un autre poste. */
  function versAncien(p, base){
    const e = Object.assign({}, base || {}, { version: 1, equipe: p.equipe, niveau: p.niveau, palier: p.palier || "", debut: p.debut, erreurs: p.erreurs || 0 });
    e.sessions = {};
    for(const s of Object.values(p.seances || {})){
      e.sessions[s.id] = { reussie: s.reussie, points: s.points, maximum: s.maximum, duree: s.duree, date: s.date };
      if(s.resultats) e.sessions[s.id].resultats = s.resultats;
    }
    e.indices = (p.indices || []).map(i => Object.assign({ session: i.session, numero: i.numero, seance: PAR_ID[i.session].titre }, i));
    e.final = Object.assign({ pays: null, colonne: null, ligne: null, code: null, resolu: false }, p.final || {});
    if(p.profil && Object.keys(p.profil).length) e.profil = Object.assign({}, e.profil || {}, p.profil);
    if(p.recompense) e.recompense = Object.assign({}, e.recompense || {}, p.recompense);
    if(p.reglages) e.reglages = Object.assign({}, p.reglages, e.reglages || {});
    return e;
  }

  /** Nom de fichier sûr pour une équipe (serveur et téléchargements). */
  const slug = s => String(s || "equipe").normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^A-Za-z0-9]+/g, "-").replace(/^-|-$/g, "").toLowerCase().slice(0, 40) || "equipe";

  return { CLE_ANCIENNE, FORMAT, SEANCES, GRADE_DE, convertir, resume, fusionner, nouveautes, versAncien, slug };
})();
if(typeof module !== "undefined" && module.exports) module.exports = MISSION_GEO_IMPORT;
