/* Lance tests/test_medias_sources.py (Python, faux service local) et compte ses vérifications — pour outils-tests/tous.js */
const { spawnSync } = require("child_process"), path = require("path");
const { compteur } = require(path.join(process.env.OUTILS_TESTS || path.resolve(__dirname, "../../outils-tests"), "charge"));
const { ok, fin } = compteur("Sources de médias (Python)");
const py = ["python3", "python"].find(p => spawnSync(p, ["--version"]).status === 0);
if(!py){ console.log("  Python introuvable : étape ignorée"); ok(true, "Python absent : tests des sources de médias ignorés"); }
else{
  const r = spawnSync(py, ["-W", "ignore", "-m", "unittest", "-v", path.join(__dirname, "test_medias_sources.py")], { encoding: "utf8", timeout: 170000, env: Object.assign({}, process.env, { PYTHONIOENCODING: "utf-8" }) });
  const sortie = (r.stderr || "") + (r.stdout || "");
  const n = +((sortie.match(/Ran (\d+) tests?/) || [])[1] || 0);
  ok(n >= 10, `${n} tests Python exécutés`);
  for(let i = 0; i < n; i++) ok(r.status === 0, `test Python ${i + 1}/${n}`);
  if(r.status !== 0) console.log(sortie.slice(-800));
}
fin();
