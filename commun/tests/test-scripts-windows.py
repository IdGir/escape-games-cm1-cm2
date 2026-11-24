#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TEST DE SYNTAXE DES SCRIPTS WINDOWS (.bat, .cmd, .ps1) — chantier « distribution »
Depuis la racine du dépôt :  python commun/tests/test-scripts-windows.py
Les scripts ne peuvent pas être lancés ici (pas de Windows) : on vérifie ce qui casse le plus souvent.
  - fins de ligne CRLF partout, aucun caractère non ASCII (console Windows) ;
  - @echo off en tête ; cd /d "%~dp0" (ou équivalent) avant tout chemin relatif ;
  - parenthèses des blocs équilibrées, sans « ) » non échappée dans un echo d'un bloc ;
  - chaque goto / call :étiquette existe ; guillemets appariés sur chaque ligne ;
  - chemins variables (%~dp0, %CD%, %LOG%...) toujours entre guillemets (dossiers avec espaces) ;
  - rien qui exige l'administrateur (runas, /RL HIGHEST), jamais « git add . » ni « git push » ;
  - PowerShell : accolades et parenthèses équilibrées, CRLF (obligatoire pour outils-ecole/, simple alerte ailleurs) ;
  - lancer.bat des variantes immersives : passent par lancer.bat de la racine (ferme l'ancien serveur).
"""
import os, re, sys

RACINE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
verifs, echecs = 0, []
# Scripts du chantier « distribution » : règles strictes (en plus des règles générales).
NOUVEAUX = ("lancer.bat", "demarrer-ecole.bat", "diagnostic.bat", "mettre-a-jour-nextcloud.bat")
LITTERAUX = ("echo", "echo.", "title", "rem", "set", "set/a", "set/p")
CHEMINS = ("%~dp0", "%~f0", "%cd%", "%log%", "%sortie%", "%demarrer%", "%startup%", "%lanceur%", "%temp%")


def ok(cond, msg):
    global verifs
    verifs += 1
    if not cond:
        echecs.append(msg)
        print("  ✗", msg)


def scripts():
    for base, dossiers, fichiers in os.walk(RACINE):
        dossiers[:] = [d for d in dossiers if d not in (".git", "node_modules", "_a-supprimer", "archives-hors-ligne", "Michel strogoff", "Constitution 1958")]
        for f in fichiers:
            if f.lower().endswith((".bat", ".cmd", ".ps1")):
                yield os.path.join(base, f)


def est_commentaire(ligne):
    l = ligne.strip().lower()
    return l.startswith("rem ") or l == "rem" or l.startswith("::")


def blocs(lignes, nom):
    """Simule l'analyse des parenthèses de cmd.exe : renvoie la profondeur finale (0 attendu)."""
    prof = 0
    for n, ligne in enumerate(lignes, 1):
        if est_commentaire(ligne) or ligne.strip().startswith(":") and not ligne.strip().startswith("::") and prof == 0:
            continue
        mot, debut, guill, i = "", True, False, 0
        while i < len(ligne):
            c = ligne[i]
            if guill:
                if c == '"':
                    guill = False
                i += 1
                continue
            if c == "^":
                i += 2
                continue
            if c == '"':
                guill, debut = True, False
            elif c in "&|":
                debut, mot = True, ""
            elif c in " \t@":
                if mot:
                    debut = False
            elif c == "(":
                if mot.lower() not in LITTERAUX or debut:
                    prof += 1
                    debut, mot = True, ""
            elif c == ")":
                if prof > 0:
                    prof -= 1
                    debut, mot = True, ""
                elif mot.lower() not in LITTERAUX:
                    ok(False, "{} l.{} : « ) » sans bloc ouvert".format(nom, n))
            elif c == ">" and debut:
                # redirection en tête (>> "fichier" echo ...) : le mot qui suit le nom de fichier décide
                j = i
                while j < len(ligne) and ligne[j] == ">":
                    j += 1
                while j < len(ligne) and ligne[j] in " \t":
                    j += 1
                if j < len(ligne) and ligne[j] == '"':
                    j = ligne.find('"', j + 1) + 1 or len(ligne)
                else:
                    while j < len(ligne) and ligne[j] not in " \t":
                        j += 1
                i = j
                continue
            else:
                if debut:
                    mot += c
            i += 1
        ok(not guill, "{} l.{} : guillemets non appariés".format(nom, n))
    return prof


def controle_bat(chemin):
    nom = os.path.relpath(chemin, RACINE).replace(os.sep, "/")
    brut = open(chemin, "rb").read()
    ok(b"\n" not in brut.replace(b"\r\n", b""), nom + " : fins de ligne CRLF partout")
    try:
        texte = brut.decode("ascii")
    except UnicodeDecodeError:
        ok(False, nom + " : caractères non ASCII (accents mal affichés dans la console)")
        texte = brut.decode("utf-8", "replace")
    lignes = texte.replace("\r\n", "\n").split("\n")
    ok(lignes[0].strip().lower() == "@echo off", nom + " : @echo off en première ligne")
    prof = blocs(lignes, nom)
    ok(prof == 0, nom + " : parenthèses des blocs équilibrées (profondeur finale {})".format(prof))
    etiquettes = {l.strip()[1:].split()[0].lower() for l in lignes if re.match(r"^\s*:[A-Za-z_]", l)}
    for n, l in enumerate(lignes, 1):
        if est_commentaire(l):
            continue
        for m in re.finditer(r"\b(?:goto|call)\s+:?([A-Za-z_][\w-]*)", l, re.I):
            cible = m.group(1).lower()
            if cible == "eof" or (m.group(0).lower().startswith("call") and ":" not in m.group(0)):
                continue
            ok(cible in etiquettes, "{} l.{} : étiquette « :{} » introuvable".format(nom, n, cible))
        bas = l.lower()
        ok("runas" not in bas and "/rl highest" not in bas, "{} l.{} : ne doit pas exiger l'administrateur".format(nom, n))
        ok(not re.search(r"git\s+add\s+\.(\s|$)", bas) and not re.search(r"\bgit\s+push\b", bas),
           "{} l.{} : jamais « git add . » ni « git push » dans un script".format(nom, n))
        # chemins variables entre guillemets (sauf dans un echo, où ils ne sont qu'affichés)
        mots = bas.strip().lstrip("@").split()
        if mots and mots[0] in ("echo", "echo.", "title"):
            continue
        if '\\"' in bas:
            continue   # guillemets échappés \" pour le programme appelé (schtasks /TR) : cmd ne coupe pas sur les espaces
        hors = re.sub(r'"[^"]*"', '""', bas)
        if re.match(r"^\s*>>?\s*\"\"\s*echo\b", hors):
            continue
        for v in CHEMINS:
            if v in hors:
                ok(False, "{} l.{} : {} hors guillemets (chemin avec espaces)".format(nom, n, v))
    if nom in NOUVEAUX:
        corps = "\n".join(l for l in lignes if not est_commentaire(l)).lower()
        ok("setlocal" in corps, nom + " : setlocal (variables locales)")
        ok("cd /d" in corps, nom + " : cd /d vers le dossier des jeux")
        ok("chcp 65001" in corps, nom + " : chcp 65001")
        ok(not re.search(r"^\s*if\b.*\(\s*$", corps, re.M), nom + " : pas de bloc if sur plusieurs lignes (goto à la place)")
        ok(":trouver_python" in corps and "py -3" in corps, nom + " : cherche python puis py -3")


def controle_ps1(chemin):
    nom = os.path.relpath(chemin, RACINE).replace(os.sep, "/")
    brut = open(chemin, "rb").read()
    if nom.startswith("outils-ecole/"):
        ok(b"\n" not in brut.replace(b"\r\n", b""), nom + " : fins de ligne CRLF partout")
    elif b"\n" in brut.replace(b"\r\n", b""):
        print("  ⚠ {} : fins de ligne LF (PowerShell les accepte ; git les remet en CRLF au prochain checkout)".format(nom))
    texte = brut.decode("utf-8", "replace")
    sans = re.sub(r"(?m)#.*$", "", re.sub(r"'[^'\r\n]*'", "''", re.sub(r'"[^"\r\n]*"', '""', texte)))
    for o, f in ("{}", "()", "[]"):
        ok(sans.count(o) == sans.count(f), "{} : « {} » et « {} » équilibrés".format(nom, o, f))


def main():
    print("== Scripts Windows ==")
    vus = 0
    for chemin in sorted(scripts()):
        vus += 1
        (controle_ps1 if chemin.lower().endswith(".ps1") else controle_bat)(chemin)
    for jeu in sorted(os.listdir(os.path.join(RACINE, "immersifs"))) if os.path.isdir(os.path.join(RACINE, "immersifs")) else []:
        f = os.path.join(RACINE, "immersifs", jeu, "lancer.bat")
        if os.path.exists(f):
            t = open(f, "rb").read().decode("ascii", "replace")
            ok("call lancer.bat immersifs/{}/".format(jeu) in t, "immersifs/{}/lancer.bat passe par lancer.bat de la racine".format(jeu))
    for n in NOUVEAUX:
        ok(os.path.exists(os.path.join(RACINE, n)), n + " présent à la racine")
    # Le crochet qui écrit version.json : script sh (Git pour Windows le lance avec son sh)
    crochet = os.path.join(RACINE, "outils-tests", "hooks", "pre-commit")
    ok(os.path.exists(crochet), "outils-tests/hooks/pre-commit présent")
    if os.path.exists(crochet):
        c = open(crochet, "rb").read()
        ok(c.startswith(b"#!/bin/sh") and b"\r" not in c, "pre-commit : #!/bin/sh et fins de ligne LF")
        ok(b"version.json" in c and b"git add" in c, "pre-commit : écrit et ajoute version.json")
    print("  {} scripts lus, {} vérifications, {} échec(s)".format(vus, verifs, len(echecs)))
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
