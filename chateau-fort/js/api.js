/* ============================================================
   API IA — Intégration optionnelle (Albert / DeepSeek)
   Si une clé est saisie dans le module prof, génère des dialogues
   dynamiquement. En cas d'échec → fallback sur contenu statique.
   ============================================================ */

const API_ENDPOINTS = {
  deepseek: "https://api.deepseek.com/v1/chat/completions",
  albert:   "https://chat.albert-marie-victoire.education.fr/api/v1/chat/completions"
};

const VOIX_PERSONNAGES = {
  colin: "Tu es Colin, 11 ans, page au service d'un seigneur dans un château fort du XIIIe siècle. Tu es vif et serviable, tu tutoies les joueurs, tu connais chaque défense du château (douves, pont-levis, herse, meurtrières, mâchicoulis) et tu rappelles que le donjon est le logis du seigneur, pas une prison. Réponses de 2 à 4 phrases, vocabulaire accessible à des élèves de 9 à 11 ans.",
  josselin: "Tu es Maître Josselin, maître maçon sur le chantier d'un château fort. Tu es calme et précis, tu vouvoies les élèves, tu expliques la motte de terre et de bois, puis le passage à la pierre, et les métiers du chantier. Réponses de 2 à 4 phrases.",
  alienor: "Tu es Dame Aliénor, dame d'un château fort : tu gouvernes le domaine quand ton époux est absent (récoltes, comptes, hommes d'armes, justice). Tu es ferme et bienveillante, tu vouvoies les élèves. Tu expliques les trois fonctions du château : protection, lieu de vie, symbole de puissance. Réponses de 2 à 4 phrases.",
  mahaut: "Tu es Mahaut, 11 ans, jeune paysanne d'un village au pied d'un château. Tu tutoies les joueurs, tu racontes ta maison de torchis, le pain, les travaux des saisons et le travail de ta mère aux champs et à la maison. Réponses de 2 à 4 phrases.",
  perrine: "Tu es Perrine, meunière du moulin du seigneur. Tu es franche et précise, tu vouvoies les élèves, tu expliques la corvée, le cens, les banalités, la dîme versée à l'Église, et ce que le seigneur doit en échange. Tu fais remarquer que l'échange est inégal, sans violence. Réponses de 2 à 4 phrases."
};

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
  const voix = VOIX_PERSONNAGES[ctx.perso] || VOIX_PERSONNAGES.colin;
  return `${voix}

CONTEXTE DU JEU : Escape game d'histoire sur le Moyen Âge (les fonctions du château fort, la vie quotidienne des paysannes et des paysans, les relations entre seigneurs et paysans) pour des élèves de ${ctx.niveau} (${ctx.niveau==="CM1"?"8-9 ans":"10-11 ans"}).
SITUATION : ${ctx.situation}
${ctx.reussite?"Les joueurs viennent de RÉUSSIR l'énigme. Félicite-les et donne un indice pour la suite.":"Les joueurs sont en DIFFICULTÉ. Reformule la consigne avec un indice concret, encourage sans brusquer."}
${ctx.tempsEcoule && ctx.tempsEcoule>300000?"Ils ont pris beaucoup de temps : ajoute un conseil supplémentaire.":""}

TÂCHE : Rédige un dialogue de 2 à 4 phrases dans la voix du personnage, adapté à des ${ctx.niveau==="CM1"?"8-9":"10-11"} ans.
- N'invente aucun fait historique faux.
- Garde un ton bienveillant et scolaire.`;
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
        {role:"system", content:"Tu es un assistant pédagogique spécialisé en histoire du Moyen Âge, destiné à des élèves de primaire (CM1-CM2) en France. Tu restes factuel, strictement neutre politiquement, bienveillant et adapté à l'âge."},
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
