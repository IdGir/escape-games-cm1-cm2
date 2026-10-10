/* ============================================================
   TEST DU CONTRÔLE DES enigmes.json (A7)
   Depuis la racine :  node commun/tests/test-enigmes-json.js
   Le contrôleur doit laisser passer les 12 jeux publiés, et
   attraper chaque erreur volontairement glissée dans une copie.
   ============================================================ */
const fs = require("fs"), os = require("os"), path = require("path");
const V = require("../../outils-tests/verifier-enigmes");
const RACINE = path.resolve(__dirname, "../..");
let ok = 0, ko = 0;
const verif = (c, m) => { if (c) { ok++; console.log("  ✓ " + m); } else { ko++; console.log("  ✗ " + m); } };

console.log("== A7 : contrôle des enigmes.json ==");
for (const j of V.jeuxDuDepot()) {
  const { R } = V.controlerJeu(j);
  verif(R.erreurs.length === 0, `${j} : aucune erreur bloquante` + (R.erreurs.length ? " — " + R.erreurs[0] : ""));
}
verif(!V.jeuxDuDepot().includes("vingt-mille-lieues"), "vingt-mille-lieues (autre format) n'est pas contrôlé");

/* Copie de melanges dans un dossier temporaire, puis erreurs glissées une à une */
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "a7-"));
const dataSrc = path.join(RACINE, "melanges", "assets", "data");
const base = path.join(tmp, "melanges"); fs.mkdirSync(path.join(base, "assets", "data"), { recursive: true });
const copier = () => ["enigmes.json", "dialogues.json", "lecons.json"].forEach(f => fs.copyFileSync(path.join(dataSrc, f), path.join(base, "assets", "data", f)));
const lire = f => JSON.parse(fs.readFileSync(path.join(base, "assets", "data", f), "utf8"));
const ecrire = (f, d) => fs.writeFileSync(path.join(base, "assets", "data", f), JSON.stringify(d, null, 1));
const erreurs = () => V.controlerJeu(base).R.erreurs.join(" | ");
const cas = (titre, f, modifier, attendu) => {
  copier(); const d = lire(f); modifier(d); ecrire(f, d);
  const e = erreurs(); verif(attendu.test(e), `${titre} → « ${e.slice(0, 110)} »`);
};
copier(); verif(erreurs() === "", "copie intacte : aucune erreur");
const E = (d, s, k) => d.salles[s].enigmes[k];
const parType = (d, t) => { for (const s of d.salles) for (const e of s.enigmes) if (e.type === t) return e; };
const niv = e => e.cm2 || e.commun;
cas("mot de serrure en double (accents ignorés)", "dialogues.json", d => { d.salles[4].motCle = "peser"; }, /serrure « peser » en double/);
cas("mot de serrure manquant", "dialogues.json", d => { delete d.salles[2].motCle; }, /motCle\) manquant/);
cas("identifiant d'énigme en double", "enigmes.json", d => { E(d, 1, 0).id = E(d, 0, 0).id; }, /en double/);
cas("plus d'énigmes en CM1 qu'en CM2", "enigmes.json", d => { d.salles[0].enigmes.forEach(e => e.niveaux = ["CM1"]); }, /aucune énigme en CM2|plus d'énigmes en CM1/);
cas("type inconnu", "enigmes.json", d => { E(d, 0, 0).type = "mots-croises"; }, /type « mots-croises » inconnu/);
cas("consigne manquante", "enigmes.json", d => { E(d, 0, 0).consigne = ""; }, /consigne manquante/);
cas("leçon introuvable", "enigmes.json", d => { E(d, 0, 0).lecon = "inexistante"; }, /leçon « inexistante » introuvable/);
cas("QCM : bonne réponse hors des options", "enigmes.json", d => { niv(parType(d, "qcm")).questions[0].bonne = 9; }, /hors des options/);
cas("ordre : rangs avec un doublon", "enigmes.json", d => { const it = niv(parType(d, "ordre")).items; it[1].rang = it[0].rang; }, /rangs doivent être/);
cas("intrus : deux intrus", "enigmes.json", d => { niv(parType(d, "intrus")).cartes.forEach(c => c.intrus = true); }, /exactement un intrus/);
cas("trous : réponse absente des étiquettes", "enigmes.json", d => { const x = niv(parType(d, "trous")); x.etiquettes = x.etiquettes.slice(1); }, /n'est pas dans les étiquettes/);
cas("tri : colonne inconnue", "enigmes.json", d => { niv(parType(d, "tri")).cartes[0].col = "zzz"; }, /colonne « zzz » inconnue/);
cas("association : clé « paires » manquante", "enigmes.json", d => { const e = parType(d, "association"); delete niv(e).paires; }, /« paires » manquant/);
cas("code : valeur attendue vide", "enigmes.json", d => { niv(parType(d, "code")).champs[0].valeur = ""; }, /sans « valeur »/);
cas("indices vides", "enigmes.json", d => { E(d, 2, 1).indices = []; }, /indices manquants/);
/* Clé en double dans le texte du fichier (JSON.parse l'aurait avalée) */
copier();
const f = path.join(base, "assets", "data", "enigmes.json");
fs.writeFileSync(f, fs.readFileSync(f, "utf8").replace('"titre"', '"titre": "doublon", "titre"'));
verif(/clé\(s\) en double.*titre/.test(erreurs()), "clé JSON en double détectée (« titre »)");
verif(V.clesEnDouble('{"a":1,"b":{"a":2},"c":[{"a":1},{"a":2}]}').length === 0, "mêmes clés dans des objets différents : pas de faux positif");
fs.writeFileSync(f, "{ pas du json");
verif(/JSON illisible/.test(erreurs()), "JSON illisible signalé");
fs.rmSync(tmp, { recursive: true, force: true });

console.log(`\nContrôle des énigmes (A7) : ${ok} vérifications réussies, ${ko} échec(s).`);
process.exitCode = ko ? 1 : 0;
