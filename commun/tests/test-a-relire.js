/* Test de la page « À relire » (a-relire.html) — Node + jsdom. Depuis la racine : node commun/tests/test-a-relire.js */
const { charger, compteur, dodo, RACINE } = require("../../outils-tests/charge");
const T = compteur("Page À relire"); const ok = T.ok;
(async () => {
  const mem = {};
  const r = await charger(RACINE, "", { page: "a-relire.html", attente: 600,
    avant: w => { Object.defineProperty(w, "localStorage", { value: { getItem: k => mem[k] || null, setItem: (k, v) => { mem[k] = v; } }, configurable: true }); } });
  const d = r.w.document; ok(r.erreurs.filter(e => !/api\/relectures|fetch/i.test(e)).length === 0, "aucune erreur JS : " + r.erreurs.slice(0,3).join(" | "));
  const cartes = () => d.querySelectorAll(".pt");
  ok(cartes().length > 50, "des points à relire sont affichés : " + cartes().length);
  ok(d.querySelector("details.jeu .sens"), "les jeux sensibles sont signalés");
  ok([...cartes()].every(c => c.querySelector(".srcs a")), "chaque point a au moins un lien source");
  ok([...cartes()].every(c => c.querySelector(".liens a")), "chaque point a un lien direct");
  const premier = cartes()[0], id = premier.getAttribute("data-id");
  premier.querySelector('button[data-a="ok"]').click(); await dodo(50);
  ok(JSON.parse(mem["relectures-v1"])[id].e === "ok", "« Valider » est enregistré");
  ok(d.querySelector('.pt[data-id="' + id + '"]').classList.contains("ok"), "un point validé reste visible (annulable) pendant la visite");
  d.querySelector('.seg button[data-f="relire"]').click(); await dodo(50);
  ok(!d.querySelector('.pt[data-id="' + id + '"]'), "puis il quitte la liste « À relire »");
  d.querySelector('.seg button[data-f="ok"]').click(); await dodo(50);
  const v = d.querySelector('.pt[data-id="' + id + '"]');
  ok(v && v.classList.contains("ok"), "il apparaît dans « Validés »");
  v.querySelector('button[data-a=""]').click(); await dodo(50);
  ok(!JSON.parse(mem["relectures-v1"])[id], "« Remettre à relire » l'efface");
  d.querySelector('.seg button[data-f="relire"]').click(); await dodo(50);
  d.querySelector('.pt button[data-a="corriger"]').click(); await dodo(50);
  ok(d.querySelector(".pt.corriger input"), "« À corriger » ouvre la zone de note");
  T.fin ? T.fin() : process.exit(T.echecs ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
