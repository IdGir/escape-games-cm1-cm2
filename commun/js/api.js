/* TRONC COMMUN (commun/js/) — un seul fichier pour tous les jeux : les textes
   propres à chaque jeu sont dans <jeu>/js/jeu.js (objet JEU). */
/* ============================================================
   API IA — Intégration optionnelle (Albert / DeepSeek)
   Si une clé est saisie dans le module prof, génère des dialogues
   dynamiquement. En cas d'échec → fallback sur contenu statique.
   ============================================================ */

const API_ENDPOINTS = {
  deepseek: "https://api.deepseek.com/v1/chat/completions",
  albert:   "https://chat.albert-marie-victoire.education.fr/api/v1/chat/completions"
};

const VOIX_PERSONNAGES = ((typeof JEU !== "undefined" && JEU.ia && JEU.ia.personnages) || {});

/**
 * Génère dynamiquement un dialogue via l'API.
 * @param {object} ctx - {perso, situation, niveau, tempsEcoule, reussite}
 * @returns {Promise<string|null>} - texte généré ou null si échec/disabled
 */
async function genererDialogue(ctx){
  const r = ETAT.reglages;
  if(!r.apiActive || !r.apiCle) return null;
  try{
    const prompt = construirePrompt(ctx);
    const texte = await appelerAPI(r.apiFournisseur, r.apiCle, prompt);
    return texte;
  }catch(e){
    console.warn("API IA échec, fallback statique:", e.message);
    return null;
  }
}

function construirePrompt(ctx){
  const ia = (typeof JEU !== "undefined" && JEU.ia) || {};
  const voix = VOIX_PERSONNAGES[ctx.perso] || VOIX_PERSONNAGES[ia.persoDefaut] || "";
  const regles = (ia.regles || []).map(r=>"- "+r).join("\n");
  return `${ia.presentation ? "Tu incarnes le personnage suivant, qui se présente ainsi :\n\n" : ""}${voix}

CONTEXTE DU JEU : ${ia.contexte || "Escape game pédagogique"} pour des élèves de ${ctx.niveau} (${ctx.niveau==="CM1"?"8-9 ans":"10-11 ans"}).
SITUATION : ${ctx.situation}
${ctx.reussite?"Les joueurs viennent de RÉUSSIR l'énigme. Félicite-les et donne un indice pour la suite.":"Les joueurs sont en DIFFICULTÉ. Reformule la consigne avec un indice concret, encourage sans brusquer."}
${ctx.tempsEcoule && ctx.tempsEcoule>300000?"Ils ont pris beaucoup de temps : ajoute un conseil supplémentaire.":""}

TÂCHE : Rédige un dialogue de 2 à 4 phrases dans la voix du personnage, adapté à des ${ctx.niveau==="CM1"?"8-9":"10-11"} ans.
${regles ? regles + "\n" : ""}- Garde un ton bienveillant et scolaire.`;
}


async function appelerAPI(fournisseur, cle, prompt){
  const endpoint = API_ENDPOINTS[fournisseur] || API_ENDPOINTS.deepseek;
  const modele = fournisseur==="albert" ? "albert-large" : "deepseek-chat";
  const resp = await fetch(endpoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer "+cle
    },
    body: JSON.stringify({
      model: modele,
      messages: [
        {role:"system", content:((typeof JEU !== "undefined" && JEU.ia && JEU.ia.systeme) || "Tu es un assistant pédagogique destiné à des élèves de primaire (CM1-CM2) en France. Tu restes factuel, bienveillant et adapté à l'âge.")},
        {role:"user", content:prompt}
      ],
      temperature: 0.7,
      max_tokens: 300
    })
  });
  if(!resp.ok){
    throw new Error("HTTP "+resp.status);
  }
  const data = await resp.json();
  return data.choices && data.choices[0] && data.choices[0].message && data.choices[0].message.content;
}

async function testerCleAPI(fournisseur, cle){
  try{
    const texte = await appelerAPI(fournisseur, cle, "Dis juste \"OK\" en un mot.");
    return !!(texte && texte.trim());
  }catch(e){
    return false;
  }
}

window.genererDialogue = genererDialogue;
window.testerCleAPI = testerCleAPI;
