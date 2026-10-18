/* ============================================================
   TEST DU DOSSIER DE DIFFUSION (N14)
   Depuis la racine :  node commun/tests/test-diffusion.js
   Contrôle l'audit des licences (rejouable), la fiche de présentation (chiffres à jour avec le
   catalogue, liens et captures existants) et que RIEN n'a décidé la licence à la place de l'auteur.
   ============================================================ */
const fs = require("fs"), path = require("path"), cp = require("child_process");
const RACINE = path.resolve(__dirname, "../..");
let ok = 0, ko = 0;
const verif = (c, m) => { if (c) { ok++; console.log("  ✓ " + m); } else { ko++; console.log("  ✗ " + m); } };
const lire = f => fs.readFileSync(path.join(RACINE, f), "utf8");
console.log("== N14 : dossier de diffusion ==");

let sortie = "";
try { sortie = cp.execFileSync("python", [path.join(RACINE, "outils-docs/audit-licences.py"), "--stdout"], { encoding: "utf8", env: Object.assign({}, process.env, { PYTHONIOENCODING: "utf-8" }) }); } catch (e) { sortie = ""; }
verif(/# Audit des crédits et licences des médias/.test(sortie) && /\*\*\d+ médias\*\*/.test(sortie), "l'audit des licences s'exécute et chiffre les médias");
const n = +((sortie.match(/\*\*(\d+) médias\*\*/) || [])[1] || 0);
verif(n > 400, `audit : ${n} médias inventoriés`);
verif(/Pixabay/.test(sortie) && /CC BY-SA/.test(sortie) && /Agnes/.test(sortie), "audit : licences CC BY-SA, Pixabay et images générées relevées, avec leurs conséquences");
const audit = lire("diffusion/AUDIT-MEDIAS.md");
verif(audit.includes("Médias sans crédit") && audit.includes("| Jeu | Médias |"), "rapport diffusion/AUDIT-MEDIAS.md présent");

// la fiche suit le catalogue
const cat = new Function(lire("commun/donnees/catalogue.js") + "; return CATALOGUE;")();
const publies = cat.jeux.filter(j => j.dossier);
const fiche = lire("diffusion/FICHE-PRESENTATION.md");
const mots = { 13: "treize" };
verif(new RegExp(`\\*\\*${publies.length} escape games\\*\\*`).test(fiche), `fiche : ${publies.length} jeux, comme le catalogue`);
verif(publies.every(j => fiche.includes(j.titre.replace(/’/g, "'"))), "fiche : tous les jeux publiés sont cités");
verif(/\*\*CM1\*\*.*\*\*CM2\*\*/.test(fiche) && /histoire/.test(fiche) && /sciences/.test(fiche) && /Compétences/.test(fiche) && /Durée/.test(fiche), "fiche : niveau, disciplines, compétences, durée");
const liensLocaux = [...fiche.matchAll(/\]\(([^)]+)\)/g)].map(m => m[1]).filter(h => !/^https?:/.test(h) && !h.startsWith("#"));
const morts = liensLocaux.filter(h => !fs.existsSync(path.join(RACINE, "diffusion", h.split("#")[0])));
verif(morts.length === 0, "fiche : liens locaux existants " + morts.join(", "));
const caps = [...fiche.matchAll(/`([a-z-]+\.jpg)`/g)].map(m => m[1]);
verif(caps.length >= 5 && caps.every(c => fs.existsSync(path.join(RACINE, "presentation/captures", c))), `fiche : ${caps.length} captures d'écran existantes`);
verif(/idgir\.github\.io\/escape-games-cm1-cm2/.test(fiche) && /github\.com\/IdGir\/escape-games-cm1-cm2/.test(fiche), "fiche : liens vers le jeu et le dépôt");

// plateformes : trois plateformes, conclusion claire
const pf = lire("diffusion/PLATEFORMES.md");
verif(/Éduthèque/.test(pf) && /Apps\.education\.fr/.test(pf) && /La Digitale/.test(pf) && /Forge/.test(pf), "plateformes : Éduthèque, Apps.education.fr, La Digitale analysées");
verif(/Lumni/.test(pf) && /5R/.test(pf), "plateformes : conditions (remplacement d'Éduthèque, ressources libres 5R) documentées");

// la licence n'a pas été décidée à la place de l'auteur
const racine = fs.readdirSync(RACINE).filter(f => /^(LICEN[CS]E|COPYING)/i.test(f));
verif(racine.length === 0, "aucun fichier de licence ajouté sans décision de l'auteur" + (racine.length ? " : " + racine.join(", ") : ""));
verif(/décision de l'auteur/.test(lire("diffusion/LICENCES-PROPOSITIONS.md")) && /CC BY-SA 4\.0/.test(lire("diffusion/LICENCES-PROPOSITIONS.md")) && /MIT/.test(lire("diffusion/LICENCES-PROPOSITIONS.md")), "propositions de licences (contenus, code, médias de tiers) présentées");
console.log(`\nDossier de diffusion : ${ok} vérifications réussies, ${ko} échec(s).`);
process.exit(ko ? 1 : 0);
