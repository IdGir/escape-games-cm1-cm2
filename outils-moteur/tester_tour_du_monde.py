# -*- coding: utf-8 -*-
"""Partie complète du « Tour du monde en 80 jours » (moteur v2), CM1 et CM2.

    python -m http.server 8765          (à la racine du dépôt)
    python outils-moteur/tester_tour_du_monde.py

Escale 1 : une première réponse fausse (le bonus doit être perdu, seul le
nombre de noms bien placés est donné). Escales 2 à 5 : justes du premier
coup. Coffre final : une erreur puis les bons fragments. Vérifie le score.
"""
import asyncio
import sys
from playwright.async_api import async_playwright

BASE = "http://127.0.0.1:8765/tour-du-monde/index.html"
echecs = []


def ko(m):
    echecs.append(m)
    print("  ÉCHEC :", m)


RESOUDRE = r"""(n) => {
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
}"""

FAUX_1 = r"""() => {
  const clic = el => el.dispatchEvent(new MouseEvent('click', {bubbles:true}));
  const zones = [...document.querySelectorAll('.planisphere .zone-carte')];
  // noms décalés d'un cran : tout est faux
  zones.forEach((z, i) => {
    const voisin = zones[(i + 1) % zones.length].dataset.zone;
    clic(z); clic(document.querySelector('#banque-1 .etiquette[data-val="' + voisin + '"]'));
  });
  clic(document.getElementById('btn-verif-1'));
  const fb = document.getElementById('fb-1').innerText;
  // on efface tous les noms (un clic sur une zone nommée la vide et la sélectionne)
  zones.forEach(z => clic(z));
  clic(zones[zones.length - 1]);
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
            if "Pas tout juste" not in fb or "0 noms bien placés" not in fb or "bonus" not in fb:
                ko(f"{niveau} salle 1 : retour d'erreur inattendu : {fb!r}")
        await pg.evaluate(RESOUDRE, n)
        await pg.wait_for_timeout(300)
        fb = await pg.inner_text(f"#fb-{n}")
        attendu = "Résolue" if n == 1 else "premier coup"
        if attendu not in fb:
            ko(f"{niveau} salle {n} : retour de réussite inattendu : {fb!r}")
        if "✨" in fb or "Suez fait" in fb or "multiplie" in fb:
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
    print(f"  tour du monde {niveau} : score {st['score']}/{st['max']}, fragments {fragments}")
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
