/* ============================================================
   MOTEUR v2 — aides communes aux jeux à moteur propre
   (Déclaration, Tour du monde). Octobre 2026.
   Fichier maître : outils-moteur/v2-ancien.js → <jeu>/js/v2.js

   Règles v2 :
   - chaque énigme se valide par un bouton ; tout juste du premier
     coup = 10 points, après une erreur = 3 points ;
   - en cas d'erreur, on dit COMBIEN de réponses sont justes,
     jamais lesquelles ;
   - aucun texte de correction après la réussite ;
   - le mot gagné n'est affiché qu'une fois : les élèves le notent
     sur leur fiche de mission et le recopient dans le coffre final.
   ============================================================ */
const PTS_PREMIER_COUP   = 10;
const PTS_APRES_ERREUR   = 3;
const PTS_COFFRE_PREMIER = 10;
const PTS_COFFRE_APRES   = 3;

let V2_ERREURS = 0;          // erreurs sur l'énigme en cours
function v2Debut(){ V2_ERREURS = 0; }

function v2Normaliser(s){
  return String(s||"").trim().toLowerCase()
    .normalize("NFD").replace(/[̀-ͯ]/g, "")
    .replace(/[^a-z0-9]/g, "");
}
function v2Melanger(t){
  const a = t.slice();
  for(let i = a.length-1; i > 0; i--){ const j = Math.floor(Math.random()*(i+1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a;
}

/* Bandeau du barème, en tête de chaque énigme */
function v2Bandeau(){
  return `<div class="bandeau-bareme">🎯 Tout juste du premier coup : <b>${PTS_PREMIER_COUP} points</b> · après une erreur : ${PTS_APRES_ERREUR} points seulement. Relisez la leçon avant de valider !</div>`;
}

function v2Fb(fbId){ return document.getElementById(fbId); }

/* Réponse incomplète : pas une erreur, rien n'est compté */
function v2Incomplet(fbId, msg){
  const fb = v2Fb(fbId);
  fb.className = "feedback indice show";
  fb.innerHTML = "✋ " + msg;
}

/* Réponse fausse : seulement le nombre de réponses justes */
function v2Echec(fbId, justes, total, unites){
  V2_ERREURS++;
  if(typeof ETAT !== "undefined") ETAT.erreursTotal = (ETAT.erreursTotal||0) + 1;
  if(typeof son === "function") son("erreur");
  const fb = v2Fb(fbId);
  fb.className = "feedback erreur show";
  fb.innerHTML = `✗ <b>Pas tout juste.</b> ${justes} ${unites||"réponses justes"} sur ${total}.`
    + (V2_ERREURS === 1 ? `<div class="perte-bonus">Le bonus du premier coup est perdu : vérifiez dans la leçon avant de revalider.</div>` : "");
  const zone = fb.closest(".zone-enigme");
  if(zone){ zone.classList.remove("secoue"); void zone.offsetWidth; zone.classList.add("secoue"); }
  if(typeof sauvegarder === "function") sauvegarder();
}

/* Réponse juste : points du premier coup ou non, puis suite(erreurs) */
function v2Reussite(fbId, suite){
  const erreurs = V2_ERREURS;
  const fb = v2Fb(fbId);
  const zone = fb.closest(".zone-enigme") || document;
  zone.querySelectorAll("button, select, input").forEach(b=>{ if(!b.closest(".barre-outils")) b.disabled = true; });
  zone.classList.add("resolue");
  if(!erreurs && typeof ETAT !== "undefined") ETAT.enigmesPremierCoup = (ETAT.enigmesPremierCoup||0) + 1;
  fb.className = "feedback succes" + (erreurs ? "" : " premier-coup") + " show";
  fb.innerHTML = erreurs ? `✔ Résolue : +${PTS_APRES_ERREUR} points.` : `🎯 <b>Tout juste du premier coup !</b> +${PTS_PREMIER_COUP} points`;
  if(typeof son === "function") son("succes");
  setTimeout(()=>suite(erreurs), 700);
}

/* ---- Anagramme : lettres marquées (data-l) → cases ----
   Clic sur une lettre : elle va dans la première case vide.
   Clic sur une case : elle se vide. Les leurres sont permis. */
function v2Anagramme(slotsSel, lettresSel){
  const slots = [...document.querySelectorAll(slotsSel)];
  const lettres = [...document.querySelectorAll(lettresSel)];
  const contenu = slots.map(()=>null);
  const dessiner = ()=>slots.forEach((s,i)=>{
    s.textContent = contenu[i] ? contenu[i].dataset.l : "";
    s.classList.toggle("ok", !!contenu[i]);
    s.classList.toggle("vide", !contenu[i]);
  });
  lettres.forEach(l=>l.addEventListener("click", ()=>{
    if(l.classList.contains("utilisee")) return;
    const i = contenu.indexOf(null);
    if(i < 0) return;
    contenu[i] = l; l.classList.add("utilisee");
    if(typeof son === "function") son("clic");
    dessiner();
  }));
  slots.forEach((s,i)=>s.addEventListener("click", ()=>{
    if(!contenu[i]) return;
    contenu[i].classList.remove("utilisee"); contenu[i] = null; dessiner();
  }));
  dessiner();
  return {
    complet: ()=>contenu.every(Boolean),
    mot: ()=>contenu.map(l=>l ? l.dataset.l : "")
  };
}

/* ---- Association gauche → droite, validée par un bouton ----
   Clic à gauche puis à droite : la paire reçoit un numéro.
   Recliquer un élément déjà apparié défait sa paire. */
function v2Association(gaucheSel, droiteSel){
  const G = [...document.querySelectorAll(gaucheSel)];
  const D = [...document.querySelectorAll(droiteSel)];
  const paires = new Map();     // élément gauche → élément droit
  let sel = null;
  [...G, ...D].forEach(c=>{ if(!c.querySelector(".num-paire")) c.insertAdjacentHTML("afterbegin", '<span class="num-paire"></span>'); });
  const dessiner = ()=>{
    [...G, ...D].forEach(c=>{ c.classList.remove("apparie"); c.querySelector(".num-paire").textContent = ""; });
    let k = 1;
    G.forEach(g=>{ const d = paires.get(g); if(!d) return;
      g.classList.add("apparie"); d.classList.add("apparie");
      g.querySelector(".num-paire").textContent = k; d.querySelector(".num-paire").textContent = k; k++; });
    G.forEach(g=>g.classList.toggle("select", g === sel));
  };
  G.forEach(g=>g.addEventListener("click", ()=>{
    if(paires.has(g)){ paires.delete(g); sel = g; }
    else sel = (sel === g) ? null : g;
    dessiner();
  }));
  D.forEach(d=>d.addEventListener("click", ()=>{
    for(const [g, x] of paires) if(x === d){ paires.delete(g); }
    if(sel){ paires.set(sel, d); sel = null; if(typeof son === "function") son("clic"); }
    dessiner();
  }));
  dessiner();
  return {
    complet: ()=>paires.size === G.length,
    justes: attr=>G.filter(g=>paires.get(g) && paires.get(g).dataset.id === g.dataset[attr||"bon"]).length,
    total: G.length
  };
}

/* ---- Mot à noter (fin d'étape) ---- */
function v2MotANoter(libelle, mot){
  return `<div class="mot-cle">
      <div class="lib">${libelle}</div>
      <div class="val">${mot}</div>
      <div class="a-noter">✍️ Notez-le sur votre fiche de mission : il ne sera plus affiché !</div>
    </div>`;
}

/* ---- Coffre final : recopier les mots notés ----
   lignes : [{label, mot}] ; onPoints(pts, premierCoup) ; suite() */
function v2Coffre(zone, titre, lignes, onPoints, suite){
  let erreurs = 0;
  zone.innerHTML = `
    <div class="coffre-final" id="coffre-final">
      <h3>🔐 ${titre}</h3>
      <div class="bandeau-bareme">🎯 Tout juste du premier coup : <b>${PTS_COFFRE_PREMIER} points</b> · après une erreur : ${PTS_COFFRE_APRES} points seulement</div>
      <div class="consigne">Recopiez les mots que vous avez notés sur votre fiche de mission. Les accents et les majuscules ne comptent pas.</div>
      ${lignes.map((l,i)=>`<div class="coffre-ligne"><label for="coffre-${i}">${l.label}</label>
        <input type="text" id="coffre-${i}" autocomplete="off" spellcheck="false" maxlength="24"></div>`).join("")}
      <div class="feedback" id="fb-coffre"></div>
      <div class="center"><button class="btn grand vert" id="btn-coffre">🔓 Ouvrir le coffre</button></div>
    </div>`;
  const fb = document.getElementById("fb-coffre");
  const champs = lignes.map((l,i)=>document.getElementById("coffre-"+i));
  document.getElementById("btn-coffre").addEventListener("click", ()=>{
    if(champs.some(c=>!c.value.trim())){ fb.className = "feedback indice show"; fb.innerHTML = "✋ Il manque au moins un mot."; return; }
    const justes = lignes.filter((l,i)=>v2Normaliser(champs[i].value) === v2Normaliser(l.mot)).length;
    if(justes === lignes.length){
      champs.forEach(c=>c.disabled = true);
      document.getElementById("btn-coffre").disabled = true;
      onPoints(erreurs ? PTS_COFFRE_APRES : PTS_COFFRE_PREMIER, !erreurs);
      fb.className = "feedback succes" + (erreurs ? "" : " premier-coup") + " show";
      fb.innerHTML = erreurs ? `✔ Le coffre s'ouvre : +${PTS_COFFRE_APRES} points.` : `🎯 <b>Tout juste du premier coup !</b> +${PTS_COFFRE_PREMIER} points`;
      if(typeof son === "function") son("deverrouille");
      setTimeout(suite, 900);
    }else{
      erreurs++;
      if(typeof ETAT !== "undefined") ETAT.erreursTotal = (ETAT.erreursTotal||0) + 1;
      if(typeof son === "function") son("erreur");
      fb.className = "feedback erreur show";
      fb.innerHTML = `✗ <b>Le coffre reste fermé.</b> ${justes} mot${justes>1?"s":""} juste${justes>1?"s":""} sur ${lignes.length}.`
        + (erreurs === 1 ? `<div class="perte-bonus">Le bonus du premier coup est perdu : vérifiez votre fiche de mission.</div>` : "");
    }
  });
  zone.scrollIntoView({behavior:"smooth", block:"center"});
}

/* Le personnage se tait dès que les élèves touchent l'énigme */
function v2TairePersonnage(zone){
  if(zone) zone.addEventListener("pointerdown", ()=>{ if("speechSynthesis" in window) speechSynthesis.cancel(); }, {once:true});
}
