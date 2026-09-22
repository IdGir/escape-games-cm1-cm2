/* Lancement depuis la racine du dépôt : node objets-techniques/tests/test-verifier.js
   verifier.html : l'onglet du nouveau jeu et ceux des jeux existants se construisent. */
const fs=require("fs"), path=require("path"); const {JSDOM}=require("jsdom");
const RAC=path.resolve(__dirname,"..","..");
const dodo=ms=>new Promise(r=>setTimeout(r,ms));
async function ouvrir(hash){
  const html=fs.readFileSync(RAC+"/verifier.html","utf8");
  const srcs=[...html.matchAll(/<script src="([^"]+)"><\/script>/g)].map(m=>m[1]);
  const inline=[...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m=>m[1]);
  const dom=new JSDOM(html.replace(/<script[\s\S]*?<\/script>/g,""),{url:"http://localhost/verifier.html#"+hash,runScripts:"dangerously"});
  const w=dom.window, err=[];
  w.fetch=async(url,o={})=>{ const u=decodeURI(String(url).replace(/^http:\/\/localhost\//,"").split("?")[0].split("#")[0]);
    const f=path.join(RAC,u); const ok=!/^https?:|^\/api/.test(u)&&fs.existsSync(f)&&fs.statSync(f).isFile();
    return {ok,status:ok?200:404,headers:{get:()=>ok?String(fs.statSync(f).size):null},json:async()=>JSON.parse(fs.readFileSync(f,"utf8")),text:async()=>fs.readFileSync(f,"utf8")}; };
  w.addEventListener("error",e=>err.push(e.message));
  const inj=c=>{const e=w.document.createElement("script");e.textContent=c;w.document.body.appendChild(e);};
  for(const s of srcs) inj(fs.readFileSync(path.join(RAC,s),"utf8")); for(const s of inline) inj(s);
  w.document.dispatchEvent(new w.Event("DOMContentLoaded")); await dodo(1500);
  return {w,err};
}
(async()=>{
  let e=0; const ok=(c,m)=>{ if(!c){e++;console.log("  ✗ "+m);} else console.log("  ✓ "+m); };
  const {w,err}=await ouvrir("objets-techniques");
  const t=w.document.body.textContent;
  ok(t.includes("CM1 — 15 énigmes") && t.includes("CM2 — 20 énigmes"), "tests : 15 énigmes CM1, 20 CM2");
  const liens=[...w.document.querySelectorAll('a[href^="objets-techniques/?salle="]')].map(a=>a.getAttribute("href"));
  ok(liens.includes("objets-techniques/?salle=4&niveau=CM2&enigme=4") && liens.includes("objets-techniques/?salle=6&niveau=CM1"), `liens énigme par énigme (${liens.length})`);
  ok(t.includes("zoe") || t.includes("Zoé"), "personnages listés");
  ok(err.length===0, "erreurs : "+err.join(" | "));
  for(const id of ["declaration","tour-du-monde","mission-geo","constitution","moyen-age-abbaye","station-meteo","melanges"]){
    const r=await ouvrir(id);
    ok(r.err.length===0 && r.w.document.body.textContent.includes("Tester les énigmes"), "onglet "+id);
  }
  process.exit(e?1:0);
})();
