# -*- coding: utf-8 -*-
"""Vérifie les leçons imprimables de tous les jeux (Chromium via Playwright).

    python -m http.server 8765        (à la racine du dépôt, dans un autre terminal)
    python outils-lecons/verifier.py  [--pdf dossier]

Pour chaque jeu et chaque niveau : la page se charge sans erreur, il y a une page A4
par leçon, aucune page ne déborde, toutes les images s'affichent, chaque leçon porte
sa compétence du programme ; le PDF produit a bien une page par leçon.
Puis, dans chaque jeu : le bloc « Leçons à imprimer » du volet enseignant existe et
ouvre la bonne adresse.
"""
import asyncio
import json
import os
import subprocess
import sys

from playwright.async_api import async_playwright

BASE = "http://127.0.0.1:8765"
JEUX = ["moyen-age-abbaye", "chateau-fort", "station-meteo", "objets-techniques", "melanges",
        "constitution", "declaration", "tour-du-monde", "mission-geo", "versailles", "renaissance", "alimentation", "lumiere"]
erreurs = []


def ko(msg):
    erreurs.append(msg)
    print("  ÉCHEC :", msg)


async def verifier_page(ctx, jeu, niveau, dossier_pdf):
    pg = await ctx.new_page()
    msgs = []
    pg.on("pageerror", lambda e: msgs.append(str(e)))
    pg.on("console", lambda m: msgs.append(m.text) if m.type == "error" else None)
    await pg.goto(f"{BASE}/{jeu}/lecons-imprimables.html?niveau={niveau}&lecon=toutes")
    await pg.wait_for_selector("body[data-pret='1']", timeout=30000)
    r = await pg.evaluate("""() => ({
        pages: [...document.querySelectorAll('.feuille')].map(f => ({
            id: f.dataset.id, deborde: f.classList.contains('deborde'),
            e: parseFloat(f.style.getPropertyValue('--echelle')),
            competence: !!f.querySelector('.competence'),
            visuels: f.querySelectorAll('.visuel').length,
            imgKo: [...f.querySelectorAll('img')].filter(i => !i.complete || i.naturalWidth === 0).length
        })),
        niveau: document.querySelector('.bascule .actif') && document.querySelector('.bascule .actif').dataset.niveau
    })""")
    n = len(r["pages"])
    if n == 0:
        ko(f"{jeu} {niveau} : aucune leçon")
    for p in r["pages"]:
        if p["deborde"]:
            ko(f"{jeu} {niveau} {p['id']} : la page déborde")
        if not p["competence"]:
            ko(f"{jeu} {niveau} {p['id']} : compétence du programme absente")
        if p["visuels"] == 0:
            ko(f"{jeu} {niveau} {p['id']} : aucun visuel")
        if p["imgKo"]:
            ko(f"{jeu} {niveau} {p['id']} : {p['imgKo']} image(s) non affichée(s)")
        if p["e"] < 0.7:
            print(f"  (texte réduit à {p['e']:.2f} : {jeu} {niveau} {p['id']})")
    for m in msgs:
        if "favicon" not in m:
            ko(f"{jeu} {niveau} : erreur console : {m}")
    if dossier_pdf:
        chemin = os.path.join(dossier_pdf, f"{jeu}-{niveau}.pdf")
        await pg.pdf(path=chemin, format="A4", print_background=True, prefer_css_page_size=True)
        info = subprocess.run(["pdfinfo", chemin], capture_output=True, text=True).stdout
        pages_pdf = int([l for l in info.splitlines() if l.startswith("Pages")][0].split()[-1])
        if pages_pdf != n:
            ko(f"{jeu} {niveau} : {pages_pdf} pages PDF pour {n} leçons")
    # une seule leçon, par salle (jeux dont les leçons sont rattachées à une salle)
    a_salles = await pg.evaluate("window.LECONS_A4.etat.lecons.some(l => l.salle)")
    if not a_salles:
        await pg.close()
        print(f"  {jeu} {niveau} : {n} pages, compétences et visuels présents")
        return n
    await pg.goto(f"{BASE}/{jeu}/lecons-imprimables.html?niveau={niveau}&salle=2")
    await pg.wait_for_selector("body[data-pret='1']", timeout=30000)
    n1 = await pg.evaluate("document.querySelectorAll('.feuille').length")
    if n1 != 1:
        ko(f"{jeu} {niveau} : salle=2 donne {n1} pages (attendu 1)")
    await pg.close()
    print(f"  {jeu} {niveau} : {n} pages, compétences et visuels présents")
    return n


async def verifier_bouton(ctx, jeu):
    pg = await ctx.new_page()
    await pg.goto(f"{BASE}/{jeu}/index.html")
    await pg.wait_for_timeout(800)
    if jeu == "mission-geo":
        await pg.evaluate("REGLAGES.ouvrir()")
        ids = ("#r-imp-lecon-a4", "#r-imp-lecons-a4")
    else:
        await pg.evaluate("ouvrirReglages()")
        ids = ("#btn-lecons-a4-cm1", "#btn-lecons-a4-cm2")
    await pg.wait_for_timeout(300)
    for sel in ids:
        if not await pg.query_selector(sel):
            ko(f"{jeu} : bouton {sel} absent du volet enseignant")
            continue
        async with ctx.expect_page() as info:
            await pg.click(sel)
        nouvelle = await info.value
        await nouvelle.wait_for_selector("body[data-pret='1']", timeout=30000)
        n = await nouvelle.evaluate("document.querySelectorAll('.feuille').length")
        print(f"  {jeu} : {sel} → {nouvelle.url.split('/')[-1]} ({n} page(s))")
        if n == 0:
            ko(f"{jeu} : {sel} ouvre une page vide")
        await nouvelle.close()
    await pg.close()


async def main():
    dossier_pdf = sys.argv[sys.argv.index("--pdf") + 1] if "--pdf" in sys.argv else None
    if dossier_pdf:
        os.makedirs(dossier_pdf, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context()
        total = 0
        for jeu in JEUX:
            print(jeu)
            for niveau in ("CM1", "CM2"):
                total += await verifier_page(ctx, jeu, niveau, dossier_pdf)
            await verifier_bouton(ctx, jeu)
        await b.close()
    print(f"\n{total} pages vérifiées, {len(erreurs)} échec(s).")
    sys.exit(1 if erreurs else 0)


asyncio.run(main())
