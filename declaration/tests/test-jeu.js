/* Tests automatiques — Le Secret de la Déclaration (Node + jsdom)
   Depuis la racine du dépôt :  node declaration/tests/test-jeu.js
   (jsdom requis : voir outils-tests/README.md). Étapes : partie, divers. */
require("../../outils-tests/moteur-ancien").lancer(__dirname + "/..", {
  titre: "Le Secret de la Déclaration",
  resoudre: `(n) => {
    const niv = ETAT.niveau;
    const clic = el => el.dispatchEvent(new MouseEvent('click', {bubbles:true}));
    const paires = (g, d, attr) => document.querySelectorAll(g).forEach(x => {
      clic(x); clic(document.querySelector(d + '[data-id="' + x.dataset[attr||'bon'] + '"]'));
    });
    if(n === 1){
      for(const L of ['L','I','B','E','R','T','É'])
        clic([...document.querySelectorAll('.lettre-clic:not(.utilisee)')].find(x => x.dataset.l === L));
      clic(document.getElementById('btn-verif-1'));
    }else if(n === 2 && niv === 'CM1'){
      paires('#col-extraits .carte-match', '#col-images .carte-match'); clic(document.getElementById('btn-verif-2'));
    }else if(n === 2){
      const l = document.getElementById('liste-ordre');
      [...l.children].sort((a,b) => a.dataset.rang - b.dataset.rang).forEach(x => l.appendChild(x));
      clic(document.getElementById('btn-verif-ordre'));
    }else if(n === 3){
      ['LIBRES','ÉGAUX','DROITS'].forEach((v,i) => { const s = document.querySelector('.choix-rebus[data-i="'+i+'"]'); s.value = v; s.dispatchEvent(new Event('change')); });
      clic(document.getElementById('btn-verif-rebus'));
    }else if(n === 4){
      paires('#col-persos .carte-match', '#col-citations .carte-match'); clic(document.getElementById('btn-verif-4'));
    }else if(n === 5){
      const bons = PLAN_REPONSES[niv];
      Object.keys(bons).forEach(k => {
        clic(document.querySelector('#plan-assemblee td[data-emp="'+k+'"]'));
        clic([...document.querySelectorAll('#banque-etiquettes .etiquette:not(.utilisee)')].find(e => e.dataset.val === bons[k]));
      });
      clic(document.getElementById('btn-verif-plan'));
    }
  }`,
  faux1: `() => {
    const clic = el => el.dispatchEvent(new MouseEvent('click', {bubbles:true}));
    [...document.querySelectorAll('.lettre-clic')].slice(0,7).forEach(clic);
    clic(document.getElementById('btn-verif-1'));
    const fb = document.getElementById('fb-1').textContent;
    document.querySelectorAll('#slots-1 .slot').forEach(clic);
    return fb;
  }`,
  attenduFaux1: ["sur 7"],
  interdits: ["Article", "parfait", "Parfait"]
});
