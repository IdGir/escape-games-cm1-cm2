/* Tests automatiques — Le Tour du monde en 80 minutes (Node + jsdom)
   Depuis la racine du dépôt :  node tour-du-monde/tests/test-jeu.js
   (jsdom requis : voir outils-tests/README.md). Étapes : partie, divers. */
require("../../outils-tests/moteur-ancien").lancer(__dirname + "/..", {
  titre: "Le Tour du monde en 80 minutes",
  resoudre: `(n) => {
    const clic = el => el.dispatchEvent(new MouseEvent('click', {bubbles:true}));
    const qcm = id => { const b = document.getElementById(id); clic(b.querySelector('.qcm-option[data-j="' + b.dataset.bonne + '"]')); };
    if(n === 1){
      document.querySelectorAll('.planisphere .zone-carte').forEach(z => {
        clic(z);
        clic([...document.querySelectorAll('#banque-1 .etiquette:not(.utilisee)')].find(e => e.dataset.val === z.dataset.zone));
      });
      clic(document.getElementById('btn-verif-1'));
    }else if(n === 2){
      const l = document.getElementById('carnet-route');
      [...l.children].sort((a,b) => a.dataset.rang - b.dataset.rang).forEach(x => l.appendChild(x));
      qcm('q-canal'); clic(document.getElementById('btn-verif-2'));
    }else if(n === 3){
      document.querySelectorAll('#grille-paysages .paysage').forEach(p => {
        clic(p); clic(document.querySelector('#col-climats .carte-match[data-id="' + p.dataset.bon + '"]'));
      });
      clic(document.getElementById('btn-verif-3'));
    }else if(n === 4){
      document.querySelectorAll('.table-bord tbody tr').forEach(tr => {
        tr.querySelector('.sel-transport').value = tr.dataset.bon;
        tr.querySelector('.inp-km').value = tr.dataset.km;
      });
      clic(document.getElementById('btn-verif-4'));
    }else if(n === 5){
      document.querySelectorAll('#fuseaux .fuseau-champ').forEach(ch => ch.querySelector('.sel-heure').value = ch.dataset.bon);
      qcm('q-jour'); clic(document.getElementById('btn-verif-5'));
    }
  }`,
  faux1: `() => {
    const clic = el => el.dispatchEvent(new MouseEvent('click', {bubbles:true}));
    const zones = [...document.querySelectorAll('.planisphere .zone-carte')];
    zones.forEach((z, i) => {
      const voisin = zones[(i + 1) % zones.length].dataset.zone;
      clic(z); clic(document.querySelector('#banque-1 .etiquette[data-val="' + voisin + '"]'));
    });
    clic(document.getElementById('btn-verif-1'));
    const fb = document.getElementById('fb-1').textContent;
    zones.forEach(z => clic(z));
    clic(zones[zones.length - 1]);
    return fb;
  }`,
  attenduFaux1: ["0 noms bien placés"],
  interdits: ["✨", "Suez fait", "multiplie"]
});
