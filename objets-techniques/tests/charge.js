/* Chargeur commun des tests : ouvre un jeu (index.html) dans jsdom, sans réseau. */
const fs = require("fs"), path = require("path");
const { JSDOM } = require("jsdom");
async function charger(dossierJeu, query=""){
  const html = fs.readFileSync(path.join(dossierJeu, "index.html"), "utf8");
  const srcs = [...html.matchAll(/<script src="([^"?]+)[^"]*"><\/script>/g)].map(m=>m[1]);
  const inline = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m=>m[1]);
  const sansScripts = html.replace(/<script[\s\S]*?<\/script>/g, "");
  const erreurs = [];
  const dom = new JSDOM(sansScripts, { url: "http://localhost/jeu/index.html" + query, runScripts: "dangerously", pretendToBeVisual: true });
  const w = dom.window;
  w.fetch = async (url, opts={}) => {
    const u = String(url).split("?")[0].replace(/^http:\/\/localhost\/jeu\//, "");
    const f = path.join(dossierJeu, decodeURI(u));
    const ok = !u.startsWith("/") && !u.startsWith("http") && fs.existsSync(f) && fs.statSync(f).isFile();
    return { ok, status: ok?200:404, json: async()=>JSON.parse(fs.readFileSync(f,"utf8")), text: async()=>fs.readFileSync(f,"utf8") };
  };
  w.print = ()=>{}; w.scrollTo = ()=>{}; w.confirm = ()=>true; w.alert = ()=>{};
  w.HTMLElement.prototype.scrollIntoView = function(){};
  w.HTMLMediaElement.prototype.play = function(){ return Promise.resolve(); };
  w.HTMLMediaElement.prototype.pause = function(){};
  w.HTMLMediaElement.prototype.load = function(){};
  w.Image = class { set src(v){ setTimeout(()=>this.onerror && this.onerror(), 0); } };
  w.addEventListener("error", e=>erreurs.push("JS: "+e.message));
  w.console.error = (...a)=>erreurs.push(a.join(" "));
  const injecter = code => { const el = w.document.createElement("script"); el.textContent = code; w.document.body.appendChild(el); };
  for(const s of srcs) injecter(fs.readFileSync(path.join(dossierJeu, s), "utf8"));
  for(const s of inline) injecter(s);
  w.document.dispatchEvent(new w.Event("DOMContentLoaded"));
  await new Promise(r=>setTimeout(r, 300));
  return { dom, w, erreurs };
}
module.exports = { charger };
