# -*- coding: utf-8 -*-
"""Joue une partie complète de chaque jeu à moteur commun, en CM1 et en CM2 (Chromium).

    python -m http.server 8765          (à la racine du dépôt, autre terminal)
    python outils-moteur/tester_parties.py [jeu ...]

Pour chaque partie : la première énigme est d'abord validée avec une réponse fausse
(elle doit rapporter PTS_APRES_ERREUR et n'afficher que le nombre de réponses justes),
toutes les autres sont justes du premier coup (PTS_PREMIER_COUP). On contrôle :
  - aucun texte de correction après la résolution ;
  - le mot de la salle s'affiche une fois avec « Notez-le » et n'est plus visible ensuite ;
  - aucune attente : le bouton de la salle suivante est là tout de suite ;
  - le coffre final refuse des mots faux et ne se remplit pas tout seul ;
  - le score final est exactement celui du barème.
"""
import asyncio
import sys

from playwright.async_api import async_playwright

BASE = "http://127.0.0.1:8765"
TOUTES_FAUSSES = "--toutes-fausses" in sys.argv
JEUX = ["melanges", "chateau-fort", "moyen-age-abbaye", "station-meteo", "objets-techniques", "constitution"]
echecs = []

SOLVEUR = r"""
(async ({faux}) => {
  const attendre = ms => new Promise(r => setTimeout(r, ms));
  const carte = [...document.querySelectorAll('.enigme-carte')].find(c => !c.classList.contains('resolue') && c.id !== 'coffre-final');
  if(!carte) return {etat:'aucune'};
  const id = carte.id.replace('enigme-','');
  let e = null;
  (ENIGMES.salles||[]).forEach(s => (s.enigmes||[]).forEach(x => { if(x.id === id) e = x; }));
  if(!e && ENIGMES.final && ENIGMES.final.id === id) e = ENIGMES.final;
  const d = donneesNiveau(e);
  const clic = el => el.dispatchEvent(new MouseEvent('click', {bubbles:true}));
  const valider = () => clic(carte.querySelector('[data-valider]'));
  const t = e.type;
  // remise à zéro d'une tentative précédente (comme le ferait un élève)
  carte.querySelectorAll('.slots-lettres .slot.ok').forEach(clic);
  carte.querySelectorAll('.trou[data-pose], .plan-case[data-pose]').forEach(clic);
  if(t === 'qcm'){
    d.questions.forEach((q,i) => { const qi = carte.querySelector(`.qcm-question[data-i="${i}"]`);
      const j = faux && i === 0 ? (q.bonne + 1) % q.options.length : q.bonne;
      clic(qi.querySelector(`.qcm-option[data-j="${j}"]`)); });
    valider();
  } else if(t === 'vraifaux'){
    d.affirmations.forEach((a,i) => { const l = carte.querySelector(`.vf-ligne[data-i="${i}"]`);
      const v = faux && i === 0 ? !a.vrai : !!a.vrai;
      clic(l.querySelector(`.vf-btn[data-rep="${v ? 'vrai' : 'faux'}"]`)); });
    valider();
  } else if(t === 'association'){
    const g = [...carte.querySelectorAll('[data-col="g"] .carte-match')];
    g.forEach((c,i) => { clic(c); let bon = c.dataset.bon;
      if(faux && g.length > 1){ bon = g[(i + 1) % g.length].dataset.bon; }
      clic(carte.querySelector(`[data-col="d"] [data-id="${bon}"]`)); });
    valider();
  } else if(t === 'ordre'){
    const liste = carte.querySelector('.liste-ordre');
    const it = [...liste.children].sort((a,b) => (+a.dataset.rang) - (+b.dataset.rang));
    if(faux) [it[0], it[1]] = [it[1], it[0]];
    it.forEach(x => liste.appendChild(x));
    valider();
  } else if(t === 'tri'){
    const cartes = [...carte.querySelectorAll('.carte-tri')];
    const cols = [...carte.querySelectorAll('.tri-colonne')];
    cartes.forEach((c,i) => { clic(c); let col = c.dataset.col;
      if(faux && i === 0){ col = (cols.find(k => k.dataset.col !== col) || cols[0]).dataset.col; }
      clic(carte.querySelector(`.tri-colonne[data-col="${CSS.escape(col)}"] .tri-zone`)); });
    valider();
  } else if(t === 'trous' || t === 'plan'){
    const cibles = [...carte.querySelectorAll(t === 'trous' ? '.trou' : '.plan-case')];
    const reps = cibles.map(c => c.dataset.rep);
    if(faux && reps.length > 1) [reps[0], reps[1]] = [reps[1], reps[0]];
    cibles.forEach((c,i) => {
      const et = [...carte.querySelectorAll('.etiquette:not(.posee)')].find(x => normaliser(x.dataset.mot) === normaliser(reps[i]));
      clic(et); clic(c); });
    valider();
  } else if(t === 'lettres'){
    const cible = d.cible.slice();
    if(faux) [cible[0], cible[cible.length-1]] = [cible[cible.length-1], cible[0]];
    if(faux && normaliser(cible.join('')) === normaliser(d.cible.join(''))) cible.reverse();
    cible.forEach(L => { const el = [...carte.querySelectorAll('[data-l]:not(.utilisee)')].find(x => normaliser(x.dataset.l) === normaliser(L)); clic(el); });
    valider();
  } else if(t === 'code'){
    d.champs.forEach((c,i) => { carte.querySelector('#code-' + i).value = faux && i === 0 ? '0000999' : c.valeur; });
    valider();
  } else if(t === 'intrus'){
    const cs = [...carte.querySelectorAll('.carte-intrus')];
    clic(cs.find(c => (c.dataset.intrus === '1') !== !!faux));
    valider();
  } else if(t === 'instrument'){
    carte.querySelectorAll('.instr-item').forEach(it => {
      const item = d.items[+it.dataset.i];
      if(it.dataset.mode === 'lire') it.querySelector('.instr-champ').value = faux ? String(item.valeur + 1) : String(item.valeur).replace('.', ',');
      else { const cran = it.querySelector(`.instr-cran[data-v="${item.valeur}"]`);
        if(cran && !faux) clic(cran); else { it.dataset.niveau = faux ? item.valeur + 1 : item.valeur; } }
    });
    valider();
  } else return {etat:'type inconnu', type:t};
  await attendre(80);
  const fb = carte.querySelector('.feedback');
  return {etat: carte.classList.contains('resolue') ? 'resolue' : 'erreur', id, type:t,
          fb: fb ? fb.innerText : '', correction: !!carte.querySelector('.correction, .explication.show')};
})
"""


async def jouer(ctx, jeu, niveau):
    pg = await ctx.new_page()
    err = []
    pg.on("pageerror", lambda e: err.append(str(e)))
    await pg.goto(f"{BASE}/{jeu}/?salle=1&niveau={niveau}")
    await pg.wait_for_function("typeof ENIGMES !== 'undefined' && ENIGMES && document.querySelector('.enigme-carte')", timeout=20000)
    await pg.evaluate("ETAT.reglages.cinematiques = false; if(window.NARRATION) NARRATION.parlerActif = false;")
    await pg.evaluate("ETAT.score = 0")
    nb = await pg.evaluate("nbEnigmesTotal()")
    premiere = True
    tours = 0
    while tours < 200:
        tours += 1
        await pg.wait_for_timeout(120)
        if await pg.evaluate("document.getElementById('ecran-fin') && document.getElementById('ecran-fin').classList.contains('actif') || ETAT.fini"):
            break
        # coffre final
        if await pg.query_selector("#coffre-final input:not([disabled])"):
            vides = await pg.evaluate("[...document.querySelectorAll('#coffre-final input')].every(i => !i.value)")
            if not vides:
                echecs.append(f"{jeu} {niveau} : le coffre final est pré-rempli")
            await pg.evaluate("document.querySelectorAll('#coffre-final input').forEach(i => i.value = 'faux')")
            await pg.click("#btn-coffre")
            if await pg.evaluate("ETAT.coffreOuvert"):
                echecs.append(f"{jeu} {niveau} : le coffre s'ouvre avec des mots faux")
            await pg.evaluate("DONNEES.salles.forEach((s,i) => document.getElementById('coffre-'+i).value = s.motCle.toLowerCase())")
            await pg.click("#btn-coffre")
            await pg.wait_for_timeout(1300)
            continue
        for sel in ("#btn-enigme-suivante", "#btn-salle-suivante", "#btn-coffre-final"):
            b = await pg.query_selector(sel)
            if b and await b.is_visible():
                if sel == "#btn-salle-suivante":
                    txt = await pg.evaluate("document.getElementById('zone-enigme').innerText")
                    if "Notez ce mot" not in txt:
                        echecs.append(f"{jeu} {niveau} : pas de consigne « Notez ce mot »")
                await b.click()
                break
        else:
            r = await pg.evaluate(SOLVEUR, {"faux": premiere})
            if r["etat"] == "aucune":
                continue
            if r["etat"] == "type inconnu":
                echecs.append(f"{jeu} {niveau} : type inconnu {r['type']}"); break
            if premiere:
                if r["etat"] != "erreur":
                    echecs.append(f"{jeu} {niveau} : la réponse fausse a été acceptée ({r['type']})")
                elif "Pas tout juste" not in r["fb"]:
                    echecs.append(f"{jeu} {niveau} : message d'erreur inattendu : {r['fb'][:80]}")
                premiere = TOUTES_FAUSSES
                r = await pg.evaluate(SOLVEUR, {"faux": False})
            if r["etat"] != "resolue":
                echecs.append(f"{jeu} {niveau} : énigme {r.get('id')} ({r.get('type')}) non résolue : {r.get('fb','')[:100]}"); break
            if r["correction"]:
                echecs.append(f"{jeu} {niveau} : texte de correction affiché après {r['id']}")
            # après la salle : les mots des salles précédentes ne doivent pas être lisibles
            vis = await pg.evaluate("[...document.querySelectorAll('.serrure .mot')].map(x=>x.innerText).join(' ')")
            if await pg.evaluate("!ETAT.coffreOuvert") and any(w in vis for w in await pg.evaluate("DONNEES.salles.map(s=>s.motCle)")):
                echecs.append(f"{jeu} {niveau} : un mot est encore affiché dans les serrures")
    # quizz final : tout juste
    await pg.wait_for_selector("#quizz .qcm-question", timeout=15000)
    await pg.evaluate("""quizzCourant().forEach((q,i) => document.querySelector(`#quizz .qcm-question[data-i="${i}"] .qcm-option[data-j="${q.bonne}"]`).click())""")
    await pg.click("#btn-voir-score")
    await pg.wait_for_timeout(300)
    res = await pg.evaluate("""({score: ETAT.score, max: scoreMax(), pc: ETAT.enigmesPremierCoup, err: ETAT.erreursTotal,
        cons: PTS_PREMIER_COUP, apres: PTS_APRES_ERREUR, rap: PTS_RAPIDITE, ns: NB_SALLES, q: NB_QUIZ*PTS_QUIZ,
        fermoir: typeof ENIGMES.final === 'object' && !!ENIGMES.final})""")
    attendu = ((nb * res["apres"]) if TOUTES_FAUSSES else ((nb - 1) * res["cons"] + res["apres"])) + 3 + res["ns"] * res["rap"] + res["q"] + ((res["apres"] if TOUTES_FAUSSES else res["cons"]) if res["fermoir"] else 0)
    ok = res["score"] == attendu
    if not ok:
        echecs.append(f"{jeu} {niveau} : score {res['score']} (attendu {attendu})")
    if not TOUTES_FAUSSES and res["score"] != res["max"] - (res["cons"] - res["apres"]) - 7:
        echecs.append(f"{jeu} {niveau} : maximum {res['max']} incohérent avec le score {res['score']}")
    for m in err:
        echecs.append(f"{jeu} {niveau} : erreur JavaScript : {m}")
    print(f"  {jeu} {niveau} : {nb} énigmes, score {res['score']}/{res['max']}, {res['pc']} du premier coup, {res['err']} erreur(s) comptée(s)")
    await pg.close()


async def main():
    jeux = [a for a in sys.argv[1:] if not a.startswith('--')] or JEUX
    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context()
        for jeu in jeux:
            for niveau in ("CM1", "CM2"):
                try:
                    await jouer(ctx, jeu, niveau)
                except Exception as ex:
                    echecs.append(f"{jeu} {niveau} : {type(ex).__name__} {str(ex)[:200]}")
        await b.close()
    print(f"\n{len(echecs)} échec(s)")
    for e in echecs:
        print("  ÉCHEC :", e)
    sys.exit(1 if echecs else 0)


asyncio.run(main())
