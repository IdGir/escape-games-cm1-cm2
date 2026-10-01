# -*- coding: utf-8 -*-
"""Les 16 séances de « Mission géographique » (moteur v2) + la fiche de mission.

    python -m http.server 8765          (à la racine du dépôt)
    python outils-moteur/tester_mission_geo.py

Pour chaque séance (mode vérification ?seance=N) : chaque énigme est
résolue avec la correction du moteur, puis vérifiée. Séance 1, énigme 1 :
d'abord une vérification vide (fausse) : le retour ne doit donner que le
NOMBRE de bonnes réponses, sans marquer lesquelles. Contrôles : barème
10 / 3, dénouement sans texte (ni récit ni leçon), indice à recopier,
carnet sans valeurs d'indices, fiche de mission imprimable.
"""
import asyncio
import sys
from playwright.async_api import async_playwright

BASE = "http://127.0.0.1:8765/mission-geo/index.html"
echecs = []


def ko(m):
    echecs.append(m)
    print("  ÉCHEC :", m)


ESPION = """() => { const o = ACTIVITES.rendre; ACTIVITES.rendre = (a, h, x) => { const r = o(a, h, x); window.__m = r.moteur; return r; }; }"""


async def seance(ctx, n):
    pg = await ctx.new_page()
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    await pg.goto(f"{BASE}?seance={n}")
    await pg.wait_for_timeout(700)
    await pg.evaluate(ESPION)
    nb = await pg.evaluate("APP.courant.s.activites.length")
    if "10 points" not in await pg.inner_text("#session-scene"):
        ko(f"séance {n} : barème absent de l'introduction")
    await pg.click("text=Commencer la mission")
    attendu = 0
    for k in range(nb):
        await pg.wait_for_selector(".activite", timeout=5000)
        if n == 1 and k == 0:
            await pg.click(".activite .barre-actions .bouton-principal")
            fb = await pg.inner_text(".activite .retour")
            marques = await pg.evaluate("document.querySelectorAll('.activite .corps .bon, .activite .corps .faux, .activite .corps .mauvais').length")
            if marques:
                ko(f"séance 1 : {marques} réponse(s) marquée(s) juste/fausse après une erreur")
            erreur = "Pas tout juste" in fb
            if not erreur and "✋" not in fb:
                ko(f"séance 1 : retour d'erreur inattendu {fb!r}")
            attendu += 3 if erreur else 10
        else:
            attendu += 10
        await pg.evaluate("window.__m.corriger()")
        await pg.click(".activite .barre-actions .bouton-principal")
        fb = await pg.inner_text(".activite .retour")
        if "✋" in fb:   # répartition libre (sans solution) : on place tous les jetons
            await pg.evaluate("""() => { const plus = [...document.querySelectorAll('.activite .poste .boutons button:last-child')];
              for(let k = 0; k < 500 && !document.querySelector('.reste-a-placer.ok'); k++) plus[k % plus.length].click(); }""")
            await pg.click(".activite .barre-actions .bouton-principal")
            fb = await pg.inner_text(".activite .retour")
        if not ("points" in fb and ("premier coup" in fb or "Résolue" in fb or "enregistrée" in fb)):
            ko(f"séance {n} énigme {k+1} : retour de réussite inattendu {fb!r}")
        await pg.click("#session-scene .pied-scene .bouton-principal")
    await pg.wait_for_timeout(300)
    txt = await pg.inner_text("#session-scene")
    pts = await pg.evaluate("APP.courant ? APP.courant.points : -1")
    if pts != attendu:
        ko(f"séance {n} : {pts} points (attendu {attendu})")
    if "Recopie cet indice" not in txt:
        ko(f"séance {n} : consigne « Recopie cet indice » absente")
    if await pg.query_selector("#session-scene .narration") or await pg.query_selector("#session-scene .lecon, #session-scene .a-retenir"):
        ko(f"séance {n} : texte (récit ou leçon) après la résolution")
    for e in errs:
        ko(f"séance {n} : erreur JS : {e}")
    print(f"  séance {n:2d} : {nb} énigmes, {pts}/{nb*10} points")
    await pg.close()


async def carnet_et_fiche(ctx):
    pg = await ctx.new_page()
    await pg.add_init_script("window.print = () => { window.__imprime = (window.__imprime || 0) + 1; }")
    await pg.goto(f"{BASE}?seance=final")
    await pg.wait_for_timeout(800)
    txt = await pg.inner_text("#final-scene")
    if "→" in txt and "?" in txt:
        ko("piste finale : les valeurs des indices sont encore recopiées automatiquement")
    await pg.evaluate("REGLAGES.ouvrir()")
    await pg.wait_for_timeout(300)
    await pg.click("#r-imp-mission")
    await pg.wait_for_timeout(600)
    lignes = await pg.evaluate("document.querySelectorAll('.table-fiche-mission tr').length")
    if lignes != 17 or not await pg.evaluate("window.__imprime || 0"):
        ko(f"fiche de mission : {lignes} lignes, impression lancée : {await pg.evaluate('window.__imprime || 0')}")
    await pg.pdf(path="/tmp/fiche-mission-geo.pdf", format="A4", print_background=True)
    print(f"  fiche de mission : {lignes-1} séances")
    await pg.close()


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context()
        for n in range(1, 17):
            await seance(ctx, n)
        await carnet_et_fiche(ctx)
        await b.close()
    print(f"\n{len(echecs)} échec(s)")
    sys.exit(1 if echecs else 0)


asyncio.run(main())
