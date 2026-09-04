/* ============================================================
   NARRATION — Personnages animés + voix (Web Speech API)
   - Affiche un personnage (portrait SVG animé ou image IA)
   - Prononce le dialogue en français (voix du navigateur)
   - Sous-titres synchronisés
   - Boutons : 🔊 réécouter, ⏭ passer
   ============================================================ */

const NARRATION = {
  voixDispo: [],
  voixFR: null,
  parlerActif: true,
  volume: 1,
  rate: 0.95,   // légèrement plus lent pour des enfants
  pitch: 1,
  enCours: null,
  configParVoix: {
    fogg:         {rate:0.86, pitch:0.88}, // lent, grave : le flegme britannique
    passepartout: {rate:1.06, pitch:1.10}, // vif, chaleureux, volubile
    aouda:        {rate:0.95, pitch:1.22}, // posée, claire
    fix:          {rate:1.00, pitch:0.95}, // sec, soupçonneux
  }
};

/* ---- Initialisation : charger les voix FR ---- */
function initVoix(){
  if(!("speechSynthesis" in window)){
    console.warn("Web Speech API non disponible — narration en sous-titres seuls.");
    return false;
  }
  const charger = ()=>{
    NARRATION.voixDispo = speechSynthesis.getVoices();
    // Préférence : voix française, ideally female pour Louise, male pour les autres
    const fr = NARRATION.voixDispo.filter(v=>/fr|FR|fran/.test(v.lang));
    NARRATION.voixFR = fr;
    if(fr.length===0){
      console.warn("Aucune voix française trouvée. Narration textuelle seulement.");
    }
  };
  charger();
  speechSynthesis.onvoiceschanged = charger;
  return true;
}

/* ---- Sélection d'une voix selon le personnage ---- */
function choisirVoix(perso){
  if(!NARRATION.voixFR || NARRATION.voixFR.length===0) return null;
  const nomsFeminins = ["amélie","amélie","google français","female","femme","virginie","julie","marie"];
  const nomsMasculins = ["thomas","google français","male","homme","henri","paul"];

  let pool = NARRATION.voixFR;
  if(perso === "aouda"){
    const f = pool.find(v=>nomsFeminins.some(n=>(v.name||"").toLowerCase().includes(n)));
    if(f) return f;
  }else{
    const m = pool.find(v=>nomsMasculins.some(n=>(v.name||"").toLowerCase().includes(n)));
    if(m) return m;
  }
  return pool[0];
}

/* ---- Afficher une scène de personnage + parler ---- */
/**
 * Affiche le personnage et prononce le texte.
 * @param {object} opts - {perso, nom, texte, onFini, conteneur}
 */
function afficherDialogue(opts){
  const {perso, nom, texte, onFini} = opts;
  const conteneur = opts.conteneur || document.getElementById("salle-contenu");

  // Supprimer une éventuelle scène perso précédente
  const ancien = conteneur.querySelector(".personnage-scene");
  if(ancien) ancien.remove();

  // Construire la scène
  const scene = document.createElement("div");
  scene.className = "personnage-scene entrer";
  scene.innerHTML = `
    <div class="pastille-perso">DIALOGUE</div>
    <div class="portrait" id="portrait-courant" data-perso="${perso}">
      ${htmlPortrait(perso)}
    </div>
    <div class="bulle">
      <div class="nom-perso">${nom}</div>
      <div class="texte" id="texte-dialogue"></div>
      <div class="controles-voix">
        <button class="btn petit or" id="btn-reecouter">🔊 Réécouter</button>
        <button class="btn petit gris" id="btn-passer">⏭ Passer</button>
      </div>
    </div>
  `;
  // Insérer après le décor (la scène), avant la consigne
  const zoneEnigme = conteneur.querySelector(".zone-enigme");
  if(zoneEnigme){
    conteneur.insertBefore(scene, zoneEnigme);
  }else{
    conteneur.appendChild(scene);
  }

  // Activer le portrait (image si dispo, sinon SVG)
  activerPortrait(scene.querySelector(".portrait-conteneur"));

  // Effet machine à écrire du texte (sous-titres)
  const elTexte = scene.querySelector("#texte-dialogue");
  machineEcrire(elTexte, texte);

  // Lancer la voix si activée
  if(NARRATION.parlerActif){
    setTimeout(()=>parler(perso, texte, scene, onFini), 250);
  }else{
    // Marquer comme "parlé" pour déclencher onFini après un délai
    scene.querySelector("#btn-passer").addEventListener("click", ()=>{
      if(onFini) onFini();
    });
  }

  // Bouton réécouter
  scene.querySelector("#btn-reecouter").addEventListener("click", ()=>{
    if(NARRATION.parlerActif){
      parler(perso, texte, scene);
    }else{
      machineEcrire(elTexte, texte);
    }
  });
  // Bouton passer
  scene.querySelector("#btn-passer").addEventListener("click", ()=>{
    if("speechSynthesis" in window) speechSynthesis.cancel();
    scene.querySelector(".portrait").classList.remove("parle");
    if(onFini) onFini();
  });
}

/* ---- Prononciation via Web Speech API ----
   On utilise l'événement "boundary" (émis à chaque mot/syllabe) pour
   piloter VRAIMENT la bouche du personnage → mouvement réaliste et synchro. */
function parler(perso, texte, scene, onFini){
  if(!("speechSynthesis" in window)) {
    if(onFini) onFini();
    return;
  }
  speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(nettoyerPourParole(texte));
  const voix = choisirVoix(perso);
  if(voix) u.voice = voix;
  u.lang = "fr-FR";
  u.volume = NARRATION.volume;
  const cfg = NARRATION.configParVoix[perso] || {};
  u.rate = cfg.rate || NARRATION.rate;
  u.pitch = cfg.pitch || NARRATION.pitch;

  const portrait = scene.querySelector(".portrait");
  const bouche = portrait.querySelector(".bouche");
  let timerBouche = null;
  // États d'ouverture de bouche, choisis pseudo-aléatoirement à chaque syllabe
  // pour imiter la variation naturelle de la parole.
  const etatsBouche = ["bouche-petite","bouche-moyenne","bouche-grande","bouche-moyenne","bouche-petite","bouche-grande"];
  let idxBouche = 0;

  function animerBouche(){
    if(!bouche) return;
    // Nettoyer les classes précédentes
    bouche.classList.remove("bouche-petite","bouche-moyenne","bouche-grande","bouche-fermee");
    // Choisir un état (pseudo-aléatoire déterministe pour rester fluide)
    const etat = etatsBouche[idxBouche % etatsBouche.length];
    bouche.classList.add(etat);
    idxBouche++;
  }
  function stopperBouche(){
    if(timerBouche){ clearInterval(timerBouche); timerBouche = null; }
    if(bouche){
      bouche.classList.remove("bouche-petite","bouche-moyenne","bouche-grande","bouche-fermee");
    }
  }

  // Gestes ponctuant le discours (personnage plein corps)
  let timerGestes = null;
  function lancerGestes(){
    if(typeof geste !== "function") return;
    // Un geste d'accroche dès le début du propos
    setTimeout(()=>geste(portrait, "pointe", 1500), 700);
    // Puis un geste aléatoire toutes les ~6 s tant que le personnage parle
    timerGestes = setInterval(()=>{
      const choix = ["pointe","salue","pointe"];
      geste(portrait, choix[Math.floor(Math.random()*choix.length)], 1600);
    }, 6200);
  }
  function stopperGestes(){
    if(timerGestes){ clearInterval(timerGestes); timerGestes = null; }
    if(typeof geste === "function") geste(portrait, "neutre", 0);
  }

  u.onstart = ()=>{
    portrait.classList.add("parle");
    // Animation de secours au cas où boundary n'est pas supporté (Firefox ancien)
    timerBouche = setInterval(animerBouche, 120);
    animerBouche();
    lancerGestes();
  };
  // boundary = événement émis à chaque mot/phrase selon le navigateur
  u.onboundary = (ev)=>{
    // À chaque frontière détectée, on fait bouger la bouche
    animerBouche();
  };
  u.onend = ()=>{
    portrait.classList.remove("parle");
    stopperBouche();
    stopperGestes();
    if(onFini) onFini();
  };
  u.onerror = ()=>{
    portrait.classList.remove("parle");
    stopperBouche();
    stopperGestes();
    if(onFini) onFini();
  };
  NARRATION.enCours = u;
  speechSynthesis.speak(u);
}

/* ---- Nettoyer le texte pour la parole ( retirer emojis, balises) ---- */
function nettoyerPourParole(html){
  const tmp = document.createElement("div");
  tmp.innerHTML = html;
  let txt = tmp.textContent || tmp.innerText || "";
  // Retirer les emojis et symboles
  txt = txt.replace(/[\u{1F000}-\u{1FFFF}]/gu, "");
  txt = txt.replace(/[🔊⏭🎯📜⏱️⭐🔓⚖️🤝🚪🎭🗣️🔊]/g, "");
  return txt.trim();
}

/* ---- Effet machine à écrire ---- */
function machineEcrire(el, html){
  el.innerHTML = "";
  el.classList.add("dactylographie");
  // Extraire le texte simple pour l'effet (on garde le HTML final à la fin)
  const tmp = document.createElement("div");
  tmp.innerHTML = html;
  const texteComplet = tmp.textContent || tmp.innerText || "";
  let i = 0;
  const vitesse = Math.max(15, Math.min(40, 1500/Math.max(texteComplet.length,1)));
  const interval = setInterval(()=>{
    if(i >= texteComplet.length){
      clearInterval(interval);
      el.classList.remove("dactylographie");
      el.innerHTML = html; // restaurer le HTML complet (gras, etc.)
      el.onclick = null;   // nettoyer le handler une fois terminé
      return;
    }
    i++;
    el.textContent = texteComplet.slice(0,i);
  }, vitesse);
  // Permettre de skipper en cliquant
  el.onclick = ()=>{
    if(interval){
      clearInterval(interval);
      el.classList.remove("dactylographie");
      el.innerHTML = html;
      el.onclick = null;
    }
  };
}

/* ---- Réglages de la narration (depuis module prof) ---- */
function setNarrationActif(actif){ NARRATION.parlerActif = actif; }
function setVolume(v){ NARRATION.volume = Math.max(0, Math.min(1, v)); }
function setRate(r){ NARRATION.rate = r; }

window.NARRATION = NARRATION;
window.initVoix = initVoix;
window.afficherDialogue = afficherDialogue;
window.parler = parler;
window.setNarrationActif = setNarrationActif;
window.setVolume = setVolume;
