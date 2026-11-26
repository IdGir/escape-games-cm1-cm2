/* Configuration du jeu — GÉNÉRÉ par outils/immersif/migrer-jeu.py ; modifiable à la main (titres, grades, vocabulaire). */
/* === Mission géo : reprise des parties de la version classique et du PC de la classe ===
   Ajouté à js/jeu-config.js par mission-geo/tests/donnees/construire-immersif.py (ne pas modifier ici : relancer le script).
   Correspondance (mission-geo/REFONTE-IMMERSIVE.md, § 1) : séance N = escale N ; séance réussie = escale réussie, toutes ses énigmes
   résolues, points repris tels quels, sans bonus ; Découverte → mousse, CM1 → matelot, CM2 → timonier.
   1. Pas de partie immersive sur ce poste, mais une partie de la version classique (localStorage « mission_geo_annee_a_v1 ») : reprise d'office.
   2. Sinon, servi par le PC de la classe : « Reprendre la mission de mon équipe » (GET /api/parties?jeu=mission-geo).
   3. Chaque enregistrement est recopié sur le PC de la classe (format « mission-geo-partie » v2), comme la version classique.
   Ce bloc est placé AVANT la définition de l'objet VML_JEU : appliquer-grades.py relit cet objet par expression régulière jusqu'au dernier « }; » du fichier. */
(function(){
  "use strict";
  var CLE = "vml_mission_geo_partie";
  var CLASSIQUE = "mission_geo_annee_a_v1";
  var ESC = {"1": {"mot": "COMMUNE", "titre": "Le grand départ", "ids": ["e1-1", "e1-2", "e1-3", "e1-4"], "indice": {"type": "nombre", "symbole": "etoile", "valeur": 5, "libelle": "Nombre de lettres de la ville de rendez-vous"}}, "2": {"mot": "EMBOÎTÉS", "titre": "Direction Dijon !", "ids": ["e2-1", "e2-2", "e2-3", "e2-4"], "indice": {"type": "nombre", "symbole": "cercle", "valeur": 7, "libelle": "Nombre de continents sur le planisphère"}}, "3": {"mot": "DENSITÉ", "titre": "Vivre à Clamecy", "ids": ["e3-1", "e3-2", "e3-3", "e3-4"], "indice": {"type": "nombre", "symbole": "nuage", "valeur": 7, "libelle": "Total des trois densités calculées"}}, "4": {"mot": "TERTIAIRE", "titre": "Besançon, travailler en ville", "ids": ["e4-1", "e4-2", "e4-3", "e4-4"], "indice": {"type": "fait", "texte": "Le pays recherché se trouve en Amérique latine.", "libelle": "Confidence d'une source à Besançon"}}, "5": {"mot": "TOURISME", "titre": "Les loisirs de la montagne", "ids": ["e5-1", "e5-2", "e5-3", "e5-4"], "indice": {"type": "fait", "texte": "Le pays recherché est situé dans l'hémisphère nord.", "libelle": "Remarque d'un skieur au refuge"}}, "6": {"mot": "BALNÉAIRE", "titre": "Étretat, station balnéaire", "ids": ["e6-1", "e6-2", "e6-3", "e6-4"], "indice": {"type": "nombre", "symbole": "pentagone", "valeur": 4, "libelle": "Nombre de lettres du premier mot de la définition"}}, "7": {"mot": "LITTORAL", "titre": "Le littoral atlantique", "ids": ["e7-1", "e7-2", "e7-3", "e7-4"], "indice": {"type": "nombre", "symbole": "trapeze", "valeur": 15, "libelle": "Coefficient multiplicateur de la densité en été"}}, "8": {"mot": "INÉGALITÉS", "titre": "Niveaux de vie dans le monde", "ids": ["e8-1", "e8-2", "e8-3", "e8-4"], "indice": {"type": "fait", "texte": "Le drapeau du pays recherché comporte du vert et du blanc.", "libelle": "Photographie froissée récupérée à Dhaka"}}};
  var GRADE_DE = { decouverte: "mousse", CM1: "matelot", CM2: "timonier" };
  var GRADES = ["mousse", "matelot", "timonier", "lieutenant", "second"];
  var NAV = typeof window !== "undefined" && typeof document !== "undefined" && typeof location !== "undefined";
  var SURPC = NAV && /^https?:$/.test(location.protocol) && !/github\.io$/.test(location.hostname);
  var verif = NAV && /[?&]verif=1/.test(location.search);
  function lire(k){ try{ return JSON.parse(localStorage.getItem(k) || "null"); }catch(e){ return null; } }
  function croissant(a, b){ return a - b; }
  function nums(){ return Object.keys(ESC).map(Number).sort(croissant); }
  function pad(n){ return (n < 10 ? "s0" : "s") + n; }
  function slug(s){ return String(s || "equipe").normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^A-Za-z0-9]+/g, "-").replace(/^-|-$/g, "").toLowerCase().slice(0, 40) || "equipe"; }

  /* Sauvegarde de l'application classique → partie commune (minimum utile : séances, indices, final, niveau). */
  function depuisClassique(o){
    if(!o || typeof o !== "object" || !o.sessions) return null;
    var seances = {}, k, m, s;
    for(k in o.sessions){
      m = /^s?0*(\d{1,2})$/.exec(k); s = o.sessions[k];
      if(!m || !s || typeof s !== "object") continue;
      seances[+m[1]] = { id: pad(+m[1]), numero: +m[1], reussie: !!s.reussie, points: Math.max(0, Number(s.points) || 0) };
    }
    return { format: "mission-geo-partie", version: 2, equipe: String(o.equipe || "").slice(0, 40), niveau: o.niveau === "CM1" ? "CM1" : "CM2",
             palier: o.palier === "decouverte" ? "decouverte" : "", seances: seances, indices: Array.isArray(o.indices) ? o.indices : [],
             final: o.final || {}, erreurs: Number(o.erreurs) || 0 };
  }

  /* Partie commune → état du moteur immersif (VML.ETAT). */
  function versEtat(p){
    var faites = [], resolues = {}, mots = [], score = 0, liste = nums(), i, j, n, s, pts, ids;
    for(i = 0; i < liste.length; i++){
      n = liste[i]; s = (p.seances || {})[n] || (p.seances || {})[String(n)];
      if(!s || !s.reussie) continue;
      faites.push(n); mots.push(ESC[n].mot);
      pts = Math.max(0, Number(s.points) || 0); score += pts; ids = ESC[n].ids;
      for(j = 0; j < ids.length; j++) resolues[ids[j]] = { pts: j === 0 ? pts : 0, bienDoc: 0, erreurs: 0, indices: 0, fiches: [], ms: 0, premier: false, importe: true };
    }
    var reste = liste.filter(function(x){ return faites.indexOf(x) < 0; });
    var grade = GRADES.indexOf(p.grade) >= 0 ? p.grade : (GRADE_DE[p.palier || p.niveau] || "timonier");
    var fini = !reste.length && faites.length > 0;
    var escale = reste.length ? reste[0] : (faites[faites.length - 1] || liste[0]);
    return { version: 2, equipe: String(p.equipe || "Équipe").slice(0, 24), niveau: grade, escale: escale, indexEnigme: fini ? ESC[escale].ids.length : 0,
             score: score, resolues: resolues, enigmes: {}, fichesConsultees: [], indicesTotal: 0, indicesEscale: 0, erreursTotal: Number(p.erreurs) || 0,
             msEcoules: 0, msTotal: 0, debut: Date.now(), enPause: false, escaleTerminee: fini, mots: mots, motVu: fini, bonus: {}, bonusEscales: {},
             escalesFaites: faites, air: 100, introVue: false, delaiAccordeMin: 0, coffreOuvert: false, final: false,
             carnetMissionGeo: Array.isArray(p.indices) ? p.indices : [], finalMissionGeo: p.final || {}, origine: "mission-geo (reprise)" };
  }

  var EXPORT = { depuisClassique: depuisClassique, versEtat: versEtat, versPartie: versPartie, ESC: ESC };   // fonctions déclarées : remontées
  if(typeof module !== "undefined" && module.exports) module.exports = EXPORT;
  if(!NAV) return;

  /* 1. Reprise d'office d'une partie de la version classique, sur le même poste. */
  if(!verif && !lire(CLE)){
    var c = depuisClassique(lire(CLASSIQUE));
    if(c && c.equipe && Object.keys(c.seances).length){
      try{ localStorage.setItem(CLE, JSON.stringify(versEtat(c))); }catch(e){}
    }
  }

  /* 2. Reprise depuis le PC de la classe. */
  function proposer(){
    if(verif || !SURPC || lire(CLE)) return;
    fetch("/api/parties?jeu=mission-geo", { cache: "no-store" }).then(function(r){ return r.ok ? r.json() : null; }).then(afficher).catch(function(){ return null; });
  }
  function afficher(r){
    var parties = r && r.parties || [];
    var ancre = document.getElementById("reprise");
    if(!parties.length || !ancre || document.getElementById("reprise-pc")) return;
    var bloc = document.createElement("div");
    bloc.id = "reprise-pc"; bloc.className = "reprise";
    var opts = parties.map(function(p){ return "<option value=\"" + p.slug + "\">" + String(p.equipe || p.slug).replace(/[<>&"]/g, "") + " · séances réussies : " + ((p.reussies || []).join(", ") || "aucune") + "</option>"; }).join("");
    bloc.innerHTML = "<p>🖥️ Mission déjà commencée ? Choisissez votre équipe :</p><select id=\"reprise-pc-choix\">" + opts + "</select> " +
                     "<button class=\"btn-laiton principal\" id=\"reprise-pc-btn\">▶️ Reprendre la mission de mon équipe</button>";
    ancre.parentNode.insertBefore(bloc, ancre.nextSibling);
    document.getElementById("reprise-pc-btn").onclick = reprendre;
  }
  function reprendre(){
    var s = document.getElementById("reprise-pc-choix").value;
    fetch("/api/parties?jeu=mission-geo&equipe=" + encodeURIComponent(s), { cache: "no-store" }).then(function(r){ return r.json(); }).then(function(r){
      if(!r || !r.ok || !r.partie) throw new Error("absente");
      localStorage.setItem(CLE, JSON.stringify(versEtat(r.partie)));
      location.reload();
    }).catch(function(){ alert("Partie introuvable sur le PC de la classe."); });
  }

  /* 3. Copie sur le PC de la classe ; compteur de fragments du HUD (le moteur affiche « /11 », nombre d'escales du Nautilus). */
  var minuteur = null;
  function versPartie(E){
    var seances = {}, indices = [], f = E.escalesFaites || [], i, n, x, V = typeof window !== "undefined" ? window.VML : null;
    for(i = 0; i < f.length; i++){
      n = f[i]; if(!ESC[n]) continue;
      seances[n] = { id: pad(n), numero: n, titre: ESC[n].titre, reussie: true, points: V && V.scoreEscale ? V.scoreEscale(n) : 0,
                     maximum: V && V.scoreMaxEscale ? V.scoreMaxEscale(n) : null, date: new Date().toISOString() };
      x = ESC[n].indice; if(x) indices.push(Object.assign({ session: pad(n), numero: n }, x));
    }
    var niv = E.niveau === "mousse" || E.niveau === "matelot" ? "CM1" : "CM2";
    return { format: "mission-geo-partie", version: 2, equipe: E.equipe, niveau: niv, palier: E.niveau === "mousse" ? "decouverte" : "", grade: E.niveau,
             seances: seances, indices: indices, final: E.finalMissionGeo || {}, erreurs: E.erreursTotal || 0, source: { format: "immersifs/mission-geo" } };
  }
  function envoyer(){
    var E = window.VML && VML.ETAT;
    if(!SURPC || verif || !E || !E.equipe || !(E.escalesFaites || []).length) return;
    clearTimeout(minuteur);
    minuteur = setTimeout(function(){
      try{ fetch("/api/parties?jeu=mission-geo", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ jeu: "mission-geo", partie: versPartie(E) }) }).catch(function(){ return null; }); }catch(e){}
    }, 3000);
  }
  function brancher(){
    var V = window.VML;
    if(!V || !V.sauver || V.__repriseMissionGeo) return;
    V.__repriseMissionGeo = true;
    var sauver = V.sauver, hud = V.majHUD;
    V.sauver = function(){ sauver.apply(this, arguments); envoyer(); };
    if(hud) V.majHUD = function(){
      hud.apply(this, arguments);
      var el = document.getElementById("hud-fragments"), E = V.ETAT;
      if(el && E) el.textContent = (E.mots || []).length + "/" + (V.escalesJouables ? V.escalesJouables().length : nums().length);
    };
  }
  document.addEventListener("DOMContentLoaded", proposer);
  window.addEventListener("load", brancher);
})();

window.VML_JEU = {
  "id": "mission-geo",
  "decorAccueil": "bureau-atlas",
  "prefixeStockage": "vml_mission_geo",
  "grades": [
    "mousse",
    "matelot",
    "timonier",
    "lieutenant",
    "second"
  ],
  "textes": {
    "auteur": "Escape game · cycle 3 · géographie",
    "titre": "Mission géographique",
    "sousTitre": "Le bureau du Professeur Atlas",
    "journal": "Le carnet de mission",
    "hud": "🧭 Mission géographique",
    "bibliotheque": "Les fiches de l'agent",
    "coffre": "🔐 Le coffre du Professeur Atlas",
    "pause": "⏸ Mission en pause",
    "mission": "✍️ Fiche de mission",
    "lecons": "Leçons A4 — Les fiches de l'agent",
    "fichierExport": "mission-geo",
    "escale": "Séance"
  },
  "mots": {
    "escale": "séance",
    "escales": "séances"
  },
  "musique": "sciences"
};
