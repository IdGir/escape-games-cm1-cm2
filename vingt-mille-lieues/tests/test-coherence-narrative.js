/* ============================================================
   TEST DE COHÉRENCE NARRATIVE (cahier des charges § 3 bis)
   ------------------------------------------------------------
   Échoue si une énigme n'a pas : de décor existant, d'objet
   cliquable défini dans decors-fx.json, de personnage émetteur
   existant, d'épisode du roman, de problème et d'enjeu, de réaction
   du décor, de compétence, de raison d'utiliser ce savoir ici ;
   ou si deux énigmes d'une même escale utilisent le même objet ;
   ou si la fiche d'ancrage (champs obligatoires) est incomplète,
   ou absente du GUIDE-PEDAGOGIQUE.md.
   ============================================================ */
const fs = require("fs"), path = require("path");
const JEU = path.resolve(__dirname, "..");
const lire = f => JSON.parse(fs.readFileSync(path.join(JEU, "assets", "data", f), "utf8"));
const E = lire("enigmes.json"), FX = lire("decors-fx.json"), P = lire("personnages.json"), L = lire("lecons.json");
let oks = 0, echecs = 0;
const ok = (c, m) => { if(c) oks++; else { echecs++; console.log("  ✗ " + m); } };
const CHAMPS = ["id", "escale", "decor", "objets_cliquables", "personnage_emetteur", "probleme_narratif", "enjeu", "episode_du_roman",
  "competence_programme", "pourquoi_ce_savoir_ici", "reaction_du_decor", "niveau_variantes"];
const EFFETS = ["cable-neuf", "lumiere", "aiguilles", "hublots"];
const guide = fs.existsSync(path.join(JEU, "GUIDE-PEDAGOGIQUE.md")) ? fs.readFileSync(path.join(JEU, "GUIDE-PEDAGOGIQUE.md"), "utf8") : "";
const coherence = fs.existsSync(path.join(JEU, "COHERENCE.md")) ? fs.readFileSync(path.join(JEU, "COHERENCE.md"), "utf8") : "";

for(const es of E.escales){
  console.log(`== Escale ${es.numero} — ${es.titre} ==`);
  ok(es.scenarimage && fs.existsSync(path.join(JEU, es.scenarimage)), `escale ${es.numero} : scénarimage présent (${es.scenarimage})`);
  ok(es.mot && /^[A-ZÀ-Ü]+$/.test(es.mot), `escale ${es.numero} : mot (fragment) en majuscules`);
  const objets = [];
  for(const e of es.enigmes){
    CHAMPS.forEach(c => ok(e[c] != null && e[c] !== "" && !(Array.isArray(e[c]) && !e[c].length), `${e.id} : champ « ${c} » renseigné`));
    const d = FX.decors[e.decor];
    ok(!!d, `${e.id} : le décor « ${e.decor} » existe dans decors-fx.json`);
    if(d){
      const zones = (d.zones || []).map(z => z.id);
      ok(zones.includes(e.objet_principal), `${e.id} : l'objet principal « ${e.objet_principal} » est une zone cliquable du décor`);
      e.objets_cliquables.forEach(o => ok(zones.includes(o), `${e.id} : objet cliquable « ${o} » défini dans le décor`));
      ok(e.objets_cliquables.includes(e.objet_principal), `${e.id} : l'objet principal fait partie des objets cliquables`);
    }
    ok(!!P.personnages[e.personnage_emetteur], `${e.id} : personnage émetteur « ${e.personnage_emetteur} » connu`);
    ok(/Partie I+|ch\.|chapitre|vraisemblance/i.test(e.episode_du_roman), `${e.id} : épisode du roman cité (partie, chapitre) ou vraisemblance`);
    ok(e.reaction_du_decor && EFFETS.includes(e.reaction_du_decor.effet) && e.reaction_du_decor.description, `${e.id} : réaction du décor visible et décrite`);
    ok(L.lecons.some(l => l.id === e.lecon), `${e.id} : leçon de la Bibliothèque existante`);
    ok(e.probleme_narratif.length > 60 && e.enjeu.length > 30 && e.pourquoi_ce_savoir_ici.length > 40, `${e.id} : problème, enjeu et raison rédigés (pas une question en l'air)`);
    ["mousse", "matelot", "timonier", "lieutenant", "second"].forEach(g => ok(e[g] && e[g].dialogue && e[g].dialogue.length > 30, `${e.id} ${g} : le personnage pose le problème avec ses mots`));
    ok(!/réponds à cette question|question de cours|avant de continuer/i.test(JSON.stringify(e)), `${e.id} : pas de formule « question de cours »`);
    ok(guide.includes(e.id) && guide.includes(e.titre), `${e.id} : fiche d'ancrage reprise dans GUIDE-PEDAGOGIQUE.md`);
    ok(coherence.includes(e.id), `${e.id} : verdict de relecture dans COHERENCE.md`);
    objets.push(e.decor + "/" + e.objet_principal);
  }
  ok(new Set(objets).size === objets.length, `escale ${es.numero} : chaque énigme utilise un objet différent du décor`);
  const persos = new Set(es.enigmes.map(e => e.personnage_emetteur));
  ok(persos.size >= Math.min(3, es.enigmes.length), `escale ${es.numero} : au moins 3 personnages émetteurs différents`);
}
console.log(`\nCohérence narrative : ${oks} vérifications réussies, ${echecs} échec(s).`);
process.exit(echecs ? 1 : 0);
