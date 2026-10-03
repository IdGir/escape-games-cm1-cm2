/* ============================================================
   Génère README.md (solutions de toutes les énigmes, tous grades)
   et la section « Fiches d'ancrage » de GUIDE-PEDAGOGIQUE.md
   (entre les marqueurs <!-- ANCRAGE:DEBUT --> et <!-- ANCRAGE:FIN -->)
   à partir de assets/data/enigmes.json.
   Usage : node vingt-mille-lieues/outils/generer-docs.js
   ============================================================ */
const fs = require("fs"), path = require("path");
const JEU = path.resolve(__dirname, "..");
const ctx = {}; new Function("globalThis", fs.readFileSync(path.join(JEU, "js/solutions.js"), "utf8").replace('typeof window !== "undefined" ? window : globalThis', "globalThis"))(ctx);
const sol = ctx.VML.solutionTexte;
const D = JSON.parse(fs.readFileSync(path.join(JEU, "assets/data/enigmes.json"), "utf8"));
const L = JSON.parse(fs.readFileSync(path.join(JEU, "assets/data/lecons.json"), "utf8"));
const P = JSON.parse(fs.readFileSync(path.join(JEU, "assets/data/personnages.json"), "utf8")).personnages;
const G = D.niveaux;
const net = s => String(s || "").replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
const fiche = id => { const l = L.lecons.find(x => x.id === id); const r = L.rayons.find(x => x.id === (l || {}).rayon); return l ? `${r ? r.titre : ""}, fiche ${l.fiche} « ${l.titre} »` : id; };

/* ---------- README.md ---------- */
let R = `# ⚓ Vingt mille lieues sous les mers — Le Journal du Nautilus

Escape game immersif de cycle 3 (CM1-CM2), d'après le roman de Jules Verne (1869-1870, domaine public), **5 grades** de
difficulté, campagne prévue en **11 escales**. **État : campagne complète, 11 escales et coffre final (en attente de validation des escales 3 à 11).**

- Jouer : \`vingt-mille-lieues/index.html\` (en ligne, ou \`lancer.bat\` puis http://127.0.0.1:8000/vingt-mille-lieues/).
- Tableau de bord enseignant (mode local) : \`prof.html\` · médias : \`medias.html\` · leçons A4 : \`lecons-imprimables.html\`.
- Vérifier une énigme sans rien enregistrer : \`index.html?verif=1&escale=2&niveau=lieutenant&enigme=3\`
  (\`&secours=1\` : décors dessinés ; \`&fin=1\` : écran de fin d'escale).
- Guide : [GUIDE-PEDAGOGIQUE.md](GUIDE-PEDAGOGIQUE.md) · cohérence : [COHERENCE.md](COHERENCE.md) · plan : [PLAN.md](PLAN.md) ·
  médias : [PRODUCTION-MEDIAS.md](PRODUCTION-MEDIAS.md) · faits à vérifier : [A-VERIFIER.md](A-VERIFIER.md) ·
  intégration au site (seconde PR) : [INTEGRATION.md](INTEGRATION.md).

> Fichier généré par \`node vingt-mille-lieues/outils/generer-docs.js\` à partir de \`assets/data/enigmes.json\`.

## Grades (équivalences réservées à l'enseignant)

| Grade affiché | Équivalent | Profil |
|---|---|---|
${G.map(g => `| ${g.icone} ${g.nom} | ${g.equivalent} | ${g.profil} |`).join("\n")}

## Barème

10 points tout juste du premier coup, 3 après une erreur, −2 par indice (Mousse : premier indice offert). Bonus :
📚 « Bien documenté » +2 (réussite du premier coup après avoir ouvert la bonne fiche pendant l'énigme), 🏊 « Maître-nageur » +5
(escale sans indice), ⏱️ rapidité +5 (≤ durée de référence − 5 min) ou +3 (≤ durée de référence ; 25 min par défaut, plus les
minutes accordées). **Maximum par escale de 4 énigmes : 4 × 12 + 5 + 5 = 58 points, à tous les grades.** La jauge d'air est un
décor : elle ne retire aucun point. Anti-tâtonnement : 3 erreurs en 60 s → sas verrouillé 20 s, puis 40 s, puis 80 s.

## Solutions
`;
for(const es of D.escales){
  R += `\n### Escale ${es.numero} — ${es.titre} · mot du journal : **${es.mot}**\n\n*${es.episode}*\n`;
  for(const e of es.enigmes){
    R += `\n#### ${es.numero}.${e.ordre} ${e.titre} — ${e.decor}, objet « ${e.objet_principal} », ${P[e.personnage_emetteur].nom}\n\n`;
    R += `Compétence : ${e.competence_programme} · Fiche : ${fiche(e.lecon)}\n\n`;
    for(const g of G){ const b = e[g.id]; R += `- **${g.icone} ${g.nom}** (${b.type || e.type}) — ${sol(e, g.id).join(" · ")}\n`; }
  }
}
fs.writeFileSync(path.join(JEU, "README.md"), R);

/* ---------- Fiches d'ancrage dans le guide ---------- */
let A = "";
for(const es of D.escales) for(const e of es.enigmes){
  A += `\n### ${e.id} — ${e.titre}\n\n| Champ | Contenu |\n|---|---|\n` +
    [["id", e.id], ["escale", e.escale], ["decor", e.decor], ["objets_cliquables", e.objets_cliquables.join(", ") + ` (objet principal : ${e.objet_principal})`],
     ["personnage_emetteur", P[e.personnage_emetteur].nom], ["probleme_narratif", e.probleme_narratif], ["enjeu", e.enjeu],
     ["episode_du_roman", e.episode_du_roman], ["competence_programme", e.competence_programme], ["pourquoi_ce_savoir_ici", e.pourquoi_ce_savoir_ici],
     ["reaction_du_decor", e.reaction_du_decor.description], ["liberte_ou_anachronisme", e.liberte_ou_anachronisme || "—"],
     ["niveau_variantes", e.niveau_variantes], ["fiche de la Bibliothèque", fiche(e.lecon)],
     ["types par grade", G.map(g => `${g.icone} ${e[g.id].type || e.type}`).join(" · ")]]
      .map(([k, v]) => `| \`${k}\` | ${net(v).replace(/\|/g, "/")} |`).join("\n") + "\n";
}
const gp = path.join(JEU, "GUIDE-PEDAGOGIQUE.md");
const guide = fs.readFileSync(gp, "utf8");
fs.writeFileSync(gp, guide.replace(/<!-- ANCRAGE:DEBUT -->[\s\S]*<!-- ANCRAGE:FIN -->/, `<!-- ANCRAGE:DEBUT -->\n${A}\n<!-- ANCRAGE:FIN -->`));
console.log("écrits : README.md, GUIDE-PEDAGOGIQUE.md (fiches d'ancrage)");
