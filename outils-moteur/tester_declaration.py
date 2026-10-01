# -*- coding: utf-8 -*-
"""Partie complète de « Le Secret de la Déclaration » (moteur v2), CM1 et CM2.

    python -m http.server 8765          (à la racine du dépôt)
    python outils-moteur/tester_declaration.py

Salle 1 : une première réponse fausse (le bonus doit être perdu, seul le
nombre de lettres bien placées est donné). Salles 2 à 5 : justes du premier
coup. Coffre final : une erreur puis les bons fragments. Vérifie le score.
"""
import asyncio
import sys
from playwright.async_api import async_playwright

BASE = "http://127.0.0.1:8765/declaration/index.html"
echecs = []


def ko(m):
    echecs.append(m)
    print("  ÉCHEC :", m)


RESOUDRE = r"""(n) => {
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
}"""

FAUX_1 = r"""() => {
  const clic = el => el.dispatchEvent(new MouseEvent('click', {bubbles:true}));
  // mot faux : les 7 premières lettres du texte (pièges compris)
  [...document.querySelectorAll('.lettre-clic')].slice(0,7).forEach(clic);
  clic(document.getElementById('btn-verif-1'));
  const fb = document.getElementById('fb-1').innerText;
  // on vide les cases pour la vraie réponse
  document.querySelectorAll('#slots-1 .slot').forEach(clic);
  return fb;
}"""


async def partie(ctx, niveau):
    pg = await ctx.new_page()
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    await pg.goto(f"{BASE}?salle=1&niveau={niveau}")
    await pg.wait_for_timeout(1500)
    await pg.evaluate("ETAT.reglages.cinematiques = false; setNarrationActif(false)")
    fragments = []
    for n in range(1, 6):
        await pg.wait_for_selector(".zone-enigme", timeout=8000)
        if n == 1:
            fb = await pg.evaluate(FAUX_1)
            if "Pas tout juste" not in fb or "sur 7" not in fb or "bonus" not in fb:
                ko(f"{niveau} salle 1 : retour d'erreur inattendu : {fb!r}")
        await pg.evaluate(RESOUDRE, n)
        await pg.wait_for_timeout(300)
        fb = await pg.inner_text(f"#fb-{n}")
        attendu = "Résolue" if n == 1 else "premier coup"
        if attendu not in fb:
            ko(f"{niveau} salle {n} : retour de réussite inattendu : {fb!r}")
        if "Article" in fb or "parfait" in fb.lower():
            ko(f"{niveau} salle {n} : texte de correction après réussite : {fb!r}")
        await pg.wait_for_timeout(900)
        if n < 5:
            txt = await pg.inner_text(".zone-enigme")
            if "Notez" not in txt:
                ko(f"{niveau} salle {n} : « Notez » absent")
            fragments.append(await pg.inner_text(".mot-cle .val"))
            if await pg.query_selector("#salle-contenu .personnage-scene"):
                ko(f"{niveau} salle {n} : un dialogue reste affiché après la réussite")
            await pg.click("#btn-salle-suivante")
            await pg.wait_for_timeout(500)
    # coffre final
    await pg.click("#btn-coffre-final")
    champs = await pg.query_selector_all("#coffre-final input")
    if len(champs) != 4:
        ko(f"{niveau} : le coffre a {len(champs)} champs (attendu 4)")
    for c in champs:
        if await c.input_value():
            ko(f"{niveau} : coffre prérempli")
    for i, c in enumerate(champs):
        await c.fill("FAUX" if i == 0 else fragments[i])
    await pg.click("#btn-coffre")
    fb = await pg.inner_text("#fb-coffre")
    if "3 mots justes sur 4" not in fb:
        ko(f"{niveau} : retour du coffre inattendu : {fb!r}")
    await champs[0].fill(fragments[0].lower())
    await pg.click("#btn-coffre")
    await pg.wait_for_timeout(2500)
    if not await pg.evaluate("document.getElementById('ecran-fin').classList.contains('actif')"):
        ko(f"{niveau} : l'écran de fin n'est pas affiché")
    st = await pg.evaluate("({score:ETAT.score, max:SCORE_MAX, pc:ETAT.enigmesPremierCoup, err:ETAT.erreursTotal, coffre:ETAT.coffreOuvert})")
    attendu = 3 + 4*10 + 5*5 + 3
    if st["score"] != attendu:
        ko(f"{niveau} : score {st['score']} (attendu {attendu})")
    if st["max"] != 95 or st["pc"] != 4 or st["err"] != 2 or not st["coffre"]:
        ko(f"{niveau} : état final inattendu {st}")
    for e in errs:
        ko(f"{niveau} : erreur JS : {e}")
    print(f"  déclaration {niveau} : score {st['score']}/{st['max']}, fragments {fragments}")
    await pg.close()


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context()
        for niv in ("CM1", "CM2"):
            await partie(ctx, niv)
        await b.close()
    print(f"\n{len(echecs)} échec(s)")
    sys.exit(1 if echecs else 0)


asyncio.run(main())
