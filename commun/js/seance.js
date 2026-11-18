/* ============================================================
   SÉANCE DU JOUR — outils communs (lot 2 : A1, A2, B1, B2, A5)
   ------------------------------------------------------------
   Utilisé par l'accueil (index.html : seul un grand bouton « Jouer »
   quand une séance est fixée), l'espace enseignant (enseignant.html :
   Préparer · Lancer · Terminer), la page à projeter (tableau.html) et
   le pack d'impression (pack-impression.html).
   • Avec le serveur local : la séance est gardée par serveur.py
     (GET/POST /api/seance, fichier seance-du-jour.json dans le dossier
     de données, jamais publié).
   • Sans serveur (GitHub Pages) : même effet avec un lien
     « ?jeu=<id>&grade=<grade> » que l'espace enseignant fabrique.
   Le grade choisi est imposé sur le Chromebook en écrivant le réglage
   « niveauImpose » du jeu immersif (même adresse, donc même stockage).
   ============================================================ */
(function(){
  "use strict";
  const GRADES = ["mousse", "matelot", "timonier", "lieutenant", "second"];
  const NOMS_PERIODES = { P1: "septembre-octobre", P2: "novembre-décembre", P3: "janvier-février", P4: "mars-avril", P5: "mai-juin" };
  const CLE_CHOIX = "escape_seance_choix";
  const URL_EN_LIGNE = "https://idgir.github.io/escape-games-cm1-cm2/";

  /** Période scolaire d'une date : P1 sept.-oct. … P5 mai-juin ; juillet-août → P1 (rentrée suivante). */
  function periodeDe(d){
    d = d && typeof d.getMonth === "function" ? d : new Date();
    const m = d.getMonth() + 1;
    return m >= 9 && m <= 10 ? "P1" : m >= 11 ? "P2" : m <= 2 ? "P3" : m <= 4 ? "P4" : m <= 6 ? "P5" : "P1";
  }
  /** Année du cycle : A en 2026-2027, B en 2027-2028, puis on alterne. */
  function anneeDe(d){
    d = d && typeof d.getMonth === "function" ? d : new Date();
    const debut = d.getMonth() + 1 >= 7 ? d.getFullYear() : d.getFullYear() - 1;
    return ((debut - 2026) % 2 + 2) % 2 === 0 ? "A" : "B";
  }
  const jouable = j => !!(j && (j.immersif || j.dossier));
  const adresse = j => j ? (j.immersif || j.dossier || "") + "/" : "";
  /** Les jeux prévus pour la période (calendrier du catalogue), dans l'ordre de la progression. */
  function jeuxDeLaPeriode(catalogue, d){
    const p = periodeDe(d), a = anneeDe(d);
    return ((catalogue && catalogue.jeux) || []).filter(j => jouable(j) && !j.libre && String(j.annee || "").includes(a) && (j.periodes || []).includes(p))
      .sort((x, y) => (parseInt(x.num, 10) || 90) - (parseInt(y.num, 10) || 90));
  }
  const infoJeu = (catalogue, id) => ((catalogue && catalogue.jeux) || []).find(j => j.id === id || j.dossier === id || (j.immersif || "") === "immersifs/" + id) || null;
  const idDe = j => j ? (j.dossier || j.id) : "";
  /** Lien que l'espace enseignant donne aux élèves sans serveur (et qu'on met en favori sur les Chromebooks). */
  function lienEleves(base, jeu, grade){
    const u = new URL(base || URL_EN_LIGNE);
    u.search = ""; u.hash = "";
    u.pathname = u.pathname.replace(/[^/]*$/, "");
    if(jeu) u.searchParams.set("jeu", jeu);
    if(jeu && GRADES.includes(grade)) u.searchParams.set("grade", grade);
    return u.href;
  }
  const cleReglages = jeu => "vml_" + String(jeu).replace(/-/g, "_") + "_reglages";
  /** Impose le grade sur cet appareil (réglage « Grade imposé » du jeu immersif) ; grade vide : au choix des équipes. */
  function imposerGrade(jeu, grade, stock){
    try{
      stock = stock || window.localStorage;
      const cle = cleReglages(jeu);
      const r = JSON.parse(stock.getItem(cle) || "{}") || {};
      r.niveauImpose = GRADES.includes(grade) ? grade : null;
      stock.setItem(cle, JSON.stringify(r));
      return true;
    }catch(e){ return false; }
  }
  const http = () => typeof location !== "undefined" && /^https?:$/.test(location.protocol);
  async function appel(url, options, delai){
    if(!http() || typeof fetch !== "function") return null;
    try{
      const ctrl = typeof AbortController === "function" ? new AbortController() : null;
      const t = ctrl ? setTimeout(() => ctrl.abort(), delai || 2500) : null;
      const r = await fetch(url, Object.assign({ cache: "no-store" }, options || {}, ctrl ? { signal: ctrl.signal } : {}));
      if(t) clearTimeout(t);
      if(!r || !r.ok) return null;
      return await r.json();
    }catch(e){ return null; }
  }
  /** Séance fixée : par le lien (?jeu=) d'abord, sinon par le serveur. → { jeu, grade, source, local } ou { jeu:"", local } */
  async function lire(base){
    let q = null; try{ q = new URLSearchParams(location.search); }catch(e){}
    const jeu = q && (q.get("jeu") || "").trim().toLowerCase();
    if(jeu && /^[a-z0-9-]{1,60}$/.test(jeu)) return { jeu, grade: GRADES.includes(q.get("grade")) ? q.get("grade") : "", source: "lien", local: false };
    const r = await appel((base || "") + "api/seance", null, 1500);
    if(r && r.seance && r.seance.jeu) return Object.assign({ source: "serveur", local: !!r.local, grade: "" }, r.seance);
    return { jeu: "", local: !!(r && r.local), serveur: !!r };
  }
  async function fixer(jeu, grade, titre, base){
    return appel((base || "") + "api/seance", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ jeu, grade: grade || "", titre: titre || "" }) }, 4000);
  }
  async function terminer(base){
    return appel((base || "") + "api/seance", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ fin: true }) }, 4000);
  }
  async function sante(base){ return appel((base || "") + "api/sante", null, 8000); }
  async function info(base){ return appel((base || "") + "api/info", null, 2000); }
  /** Choix gardé dans le navigateur de l'enseignant (marche aussi sans serveur). */
  function choixLocal(v){
    try{
      if(v === undefined) return JSON.parse(localStorage.getItem(CLE_CHOIX) || "null");
      if(v === null) localStorage.removeItem(CLE_CHOIX); else localStorage.setItem(CLE_CHOIX, JSON.stringify(v));
    }catch(e){}
    return v || null;
  }
  /** Niveau de la version classique et des évaluations : CM1 pour Mousse et Matelot, CM2 au-dessus. */
  const niveauScolaire = grade => (grade === "mousse" || grade === "matelot" || grade === "CM1") ? "CM1" : "CM2";

  window.SEANCE = { GRADES, NOMS_PERIODES, URL_EN_LIGNE, periodeDe, anneeDe, jeuxDeLaPeriode, infoJeu, idDe, adresse, jouable,
    lienEleves, cleReglages, imposerGrade, lire, fixer, terminer, sante, info, choixLocal, niveauScolaire };
})();
