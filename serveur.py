#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
============================================================
 LE SECRET DE LA DÉCLARATION — Serveur local
 Escape game Révolution française · CM1-CM2
============================================================
 Serveur HTTP stdlib + mini-API REST pour le pilotage prof.
 Aucune dépendance externe : Python 3.6+ suffit.

 Usage :
    python serveur.py            # port 8000
    python serveur.py 8080       # port personnalisé
============================================================
"""
import os
import sys
import json
import time
import socket
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from urllib.parse import urlparse, parse_qs, unquote

# ---- État partagé des équipes (en mémoire) ----
ETATS_EQUIPES = {}        # { "Les Patriotes": {salle, score, fragments, ...} }
COMMANDES_PROF = {}       # { "equipe": {"pause":bool, "indice":"..."} }
LOCK = threading.Lock()
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

def get_ip_locale():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


class Handler(BaseHTTPRequestHandler):
    """Sert les fichiers statiques + expose /api/* pour la synchro."""

    def log_message(self, format, *args):
        # Log minimal
        pass

    # ---- Routage ----
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        if path.startswith("/api/"):
            self.router_api("GET", path, {})
        else:
            self.servir_fichier(path)

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        longueur = int(self.headers.get("Content-Length", 0))
        corps = self.rfile.read(longueur).decode("utf-8") if longueur else ""
        try:
            data = json.loads(corps) if corps else {}
        except Exception:
            data = {}
        if path.startswith("/api/"):
            self.router_api("POST", path, data)
        else:
            self.send_error(404)

    # ---- Fichiers statiques ----
    TYPES = {
        ".html": "text/html; charset=utf-8",
        ".css":  "text/css; charset=utf-8",
        ".js":   "application/javascript; charset=utf-8",
        ".json": "application/json; charset=utf-8",
        ".png":  "image/png",
        ".jpg":  "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".gif":  "image/gif",
        ".svg":  "image/svg+xml",
        ".ico":  "image/x-icon",
        ".wav":  "audio/wav",
        ".mp3":  "audio/mpeg",
        ".ogg":  "audio/ogg",
        # ---- Vidéo (décors filmés et cinématiques) ----
        ".mp4":  "video/mp4",
        ".webm": "video/webm",
        ".ogv":  "video/ogg",
        ".m4v":  "video/mp4",
        # ---- Sous-titres ----
        ".vtt":  "text/vtt; charset=utf-8",
        ".srt":  "application/x-subrip; charset=utf-8",
        # ---- Polices ----
        ".woff":  "font/woff",
        ".woff2": "font/woff2",
        ".ttf":   "font/ttf",
    }

    # Les vidéos sont envoyées par morceaux plutôt qu'en un bloc :
    # cela évite de charger un fichier de plusieurs centaines de Mo en mémoire.
    TAILLE_MORCEAU = 256 * 1024

    def servir_fichier(self, path):
        if path == "/" or path == "":
            path = "/index.html"

        # Décodage des URL (les dossiers peuvent contenir des espaces)
        path = unquote(path).lstrip("/")

        # Sécurité : interdire toute remontée hors du dossier du projet
        racine = os.path.abspath(".")
        chemin = os.path.abspath(os.path.join(racine, path))
        if not chemin.startswith(racine + os.sep) and chemin != racine:
            self.send_error(403, "Accès refusé")
            return
        if os.path.isdir(chemin):
            chemin = os.path.join(chemin, "index.html")

        try:
            taille = os.path.getsize(chemin)
        except OSError:
            self.send_error(404, "Fichier non trouvé : " + path)
            return

        ext = os.path.splitext(chemin)[1].lower()
        ctype = self.TYPES.get(ext, "application/octet-stream")

        # ---- Requête partielle (Range) ----
        # Indispensable pour la vidéo : sans elle, le navigateur ne peut
        # ni se positionner dans le film, ni démarrer la lecture avant
        # d'avoir tout téléchargé.
        debut, fin = 0, taille - 1
        partiel = False
        entete_range = self.headers.get("Range")
        if entete_range and entete_range.startswith("bytes="):
            plage = entete_range[6:].split(",")[0].strip()
            try:
                d, _, f = plage.partition("-")
                if d:
                    debut = int(d)
                    if f:
                        fin = min(int(f), taille - 1)
                else:
                    # Forme « bytes=-500 » : les 500 derniers octets
                    debut = max(0, taille - int(f))
                if debut > fin or debut >= taille:
                    self.send_response(416)
                    self.send_header("Content-Range", "bytes */%d" % taille)
                    self.end_headers()
                    return
                partiel = True
            except ValueError:
                debut, fin, partiel = 0, taille - 1, False

        longueur = fin - debut + 1
        self.send_response(206 if partiel else 200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(longueur))
        self.send_header("Accept-Ranges", "bytes")
        if partiel:
            self.send_header("Content-Range", "bytes %d-%d/%d" % (debut, fin, taille))
        # Les médias sont volumineux et ne changent pas : on les met en cache.
        if ctype.startswith(("video/", "audio/", "image/", "font/")):
            self.send_header("Cache-Control", "public, max-age=3600")
        else:
            self.send_header("Cache-Control", "no-cache")
        self.end_headers()

        try:
            with open(chemin, "rb") as f:
                f.seek(debut)
                restant = longueur
                while restant > 0:
                    morceau = f.read(min(self.TAILLE_MORCEAU, restant))
                    if not morceau:
                        break
                    self.wfile.write(morceau)
                    restant -= len(morceau)
        except (BrokenPipeError, ConnectionResetError):
            # L'élève a changé de page en cours de lecture : normal.
            pass
        except Exception:
            pass

    # ---- API REST ----
    def router_api(self, methode, path, data):
        if path == "/api/etat" and methode == "POST":
            # L'élève envoie son état
            equipe = data.get("equipe", "Anonyme")
            with LOCK:
                ETATS_EQUIPES[equipe] = {
                    "equipe": equipe,
                    # Quel escape game ? "declaration" (défaut) ou "tour-du-monde".
                    # Permet à chaque tableau de bord de n'afficher que ses équipes.
                    "jeu": data.get("jeu", "declaration"),
                    "niveau": data.get("niveau"),
                    "salle": data.get("salle"),
                    "score": data.get("score"),
                    "fragments": data.get("fragments", []),
                    "msEcoules": data.get("msEcoules"),
                    "enPause": data.get("enPause", False),
                    "fini": data.get("fini", False),
                    "timestamp": time.time()
                }
                # Récupérer d'éventuelles commandes prof en attente
                cmd = COMMANDES_PROF.pop(equipe, None)
            self.json_reponse({"ok": True, "commande": cmd})
        elif path == "/api/equipes" and methode == "GET":
            # Le prof récupère tous les états
            with LOCK:
                self.json_reponse({"equipes": list(ETATS_EQUIPES.values())})
        elif path == "/api/commande" and methode == "POST":
            # Le prof envoie une commande à une équipe (ou toutes)
            equipe = data.get("equipe", "*")
            cmd = data.get("commande", {})
            with LOCK:
                if equipe == "*":
                    for eq in list(ETATS_EQUIPES.keys()):
                        COMMANDES_PROF[eq] = cmd
                else:
                    COMMANDES_PROF[equipe] = cmd
            self.json_reponse({"ok": True})
        elif path == "/api/info" and methode == "GET":
            self.json_reponse({
                "serveur": "Le Secret de la Déclaration",
                "ip": get_ip_locale(),
                "port": PORT,
                "equipes_connectees": len(ETATS_EQUIPES)
            })
        elif path == "/api/export" and methode == "GET":
            # Export CSV simplifié
            with LOCK:
                lignes = ["jeu,equipe,niveau,salle,score,fragments,temps_min,fini"]
                for e in ETATS_EQUIPES.values():
                    lignes.append('{},"{}",{},{},{},{},{},{}'.format(
                        e.get("jeu",""),
                        e.get("equipe",""),
                        e.get("niveau",""),
                        e.get("salle",""),
                        e.get("score",0),
                        len(e.get("fragments",[])),
                        round((e.get("msEcoules",0) or 0)/60000, 1),
                        "oui" if e.get("fini") else "non"
                    ))
            csv = "\n".join(lignes)
            self.send_response(200)
            self.send_header("Content-Type", "text/csv; charset=utf-8")
            self.send_header("Content-Disposition", 'attachment; filename="scores_equipes.csv"')
            self.end_headers()
            self.wfile.write(csv.encode("utf-8"))
        else:
            self.send_error(404, "API inconnue : " + path)

    def json_reponse(self, obj):
        corps = json.dumps(obj).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(corps)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(corps)


class ServeurMultiThread(ThreadingMixIn, HTTPServer):
    """Un thread par requête.

    Indispensable depuis l'ajout de la vidéo : une classe entière peut
    télécharger des décors filmés en même temps, sans jamais bloquer les
    petites requêtes /api/etat qui font vivre le tableau de bord du prof.
    """
    daemon_threads = True
    allow_reuse_address = True


def preparer_console():
    """Autorise les emojis dans la console Windows.

    Sans cela, une console configurée en cp1252 (ou une sortie redirigée
    vers un fichier) fait planter le serveur au démarrage sur le premier
    caractère accentué ou emoji de la bannière.
    """
    for flux in (sys.stdout, sys.stderr):
        try:
            flux.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def main():
    preparer_console()
    ip = get_ip_locale()
    print("=" * 62)
    print("  ESCAPE GAMES PÉDAGOGIQUES — Serveur local · CM1-CM2")
    print("=" * 62)
    print()
    print("  ✅ Serveur démarré sur le port {} (multi-thread, vidéo activée)".format(PORT))
    print()
    print("  📱 ADRESSES À DONNER AUX ÉLÈVES :")
    print("     Révolution française  →  http://{}:{}/".format(ip, PORT))
    print("     Tour du Monde (géo.)  →  http://{}:{}/tour-du-monde/".format(ip, PORT))
    print()
    print("  👨‍🏫 TABLEAUX DE BORD ENSEIGNANT :")
    print("     http://127.0.0.1:{}/prof.html".format(PORT))
    print("     http://127.0.0.1:{}/tour-du-monde/prof.html".format(PORT))
    print()
    print("  ⌨️  Ctrl+C pour arrêter le serveur.")
    print()
    print("-" * 62)
    serveur = ServeurMultiThread(("0.0.0.0", PORT), Handler)
    try:
        serveur.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServeur arrêté. À bientôt !\n")
        serveur.server_close()


if __name__ == "__main__":
    main()
