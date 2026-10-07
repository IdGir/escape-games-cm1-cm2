/* Test des voix : la clé d'une réplique est la même en JavaScript (js/voix.js) et en Python
   (outils/voix/generer-voix.py), les mp3 existants correspondent à une réplique du jeu,
   chaque personnage a UNE voix Edge, et deux personnages n'ont jamais la même.
   node vingt-mille-lieues/tests/test-voix.js */
const fs = require("fs"), path = require("path"), cp = require("child_process"), vm = require("vm");
const JEU = path.resolve(__dirname, "..");
let ok = 0, ko = 0;
const t = (c, m) => { if(c){ ok++; } else { ko++; console.log("✖", m); } };

const win = { VML: {} };
win.window = win;
vm.runInNewContext(fs.readFileSync(path.join(JEU, "js", "voix.js"), "utf8"), { window: win, unescape, encodeURIComponent, Array, document: {}, console, setTimeout, clearTimeout, clearInterval, setInterval, Math });
const VML = win.VML;
const exemples = ["Bonjour !", "L'éclat du phare — très loin…", "  Texte   avec <b>balises</b>\n et espaces ", "œuvre, Maëlle & Yasmine : « signal »"];
const py = cp.spawnSync("python", ["-c", "import sys,importlib.util as u;s=u.spec_from_file_location('g',sys.argv[1]);m=u.module_from_spec(s);s.loader.exec_module(m);import json;print(json.dumps([m.cle_replique(x) for x in json.loads(sys.argv[2])]))", path.join(JEU, "outils", "voix", "generer-voix.py"), JSON.stringify(exemples)], { encoding: "utf8" });
t(py.status === 0, "Python lance cle_replique : " + (py.stderr || ""));
if(py.status === 0){
  const cles = JSON.parse(py.stdout);
  exemples.forEach((x, i) => t(VML.cleReplique(x) === cles[i], `clé JS = clé Python pour « ${x.trim().slice(0, 25)} »`));
}
t(VML.cleReplique("a  b") === VML.cleReplique("a b") && VML.cleReplique("<i>a</i> b") === VML.cleReplique("a b"), "balises et espaces ignorés");
t(VML.urlVoix("maelle", "Bonjour") === "assets/audio/voix/maelle/" + VML.cleReplique("Bonjour") + ".mp3", "adresse du fichier de voix");

const persos = JSON.parse(fs.readFileSync(path.join(JEU, "assets", "data", "personnages.json"), "utf8")).personnages;
const prises = {};
for(const [id, p] of Object.entries(persos)){
  const e = p.voix && p.voix.edge;
  if(!e) continue;                                  // jeux sans voix Edge : voix du navigateur
  t(/^fr-[A-Z]{2}-\w+Neural$/.test(e), `${id} : identifiant de voix Edge valide (${e})`);
  (prises[e] = prises[e] || []).push(id);
}
for(const [v, qui] of Object.entries(prises)) t(qui.length === 1, `voix ${v} partagée par ${qui.join(", ")}`);
const index = path.join(JEU, "assets", "audio", "voix", "index.json");
if(fs.existsSync(index)){
  const I = JSON.parse(fs.readFileSync(index, "utf8"));
  for(const [k, emp] of Object.entries(I)){
    const [perso, cle] = k.split("/");
    t(fs.existsSync(path.join(JEU, "assets", "audio", "voix", perso, cle + ".mp3")), `mp3 présent : ${k}`);
    t(VML.cleReplique(emp[3]) === cle, `clé de l'index conforme au texte : ${k}`);
    t(persos[perso] && persos[perso].voix && persos[perso].voix.edge === emp[0], `${perso} : la voix de l'index est celle de personnages.json (une voix tout au long du jeu)`);
  }
}
console.log(`\nVoix : ${ok} vérifications réussies, ${ko} échec(s).`);
process.exit(ko ? 1 : 0);
