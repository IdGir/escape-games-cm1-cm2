"""Correcteur Pédagogique — point d'entrée.

L'interface est une vraie interface web (HTML/CSS/JS), affichée dans une fenêtre
native par pywebview. L'enseignant double-clique, une application s'ouvre : il ne
voit aucun navigateur, aucune barre d'adresse.

Tout tourne en local. Aucune donnée ne quitte l'ordinateur.
"""
import socket
import sys

import api
import database as db
import integration_server as ig
import seed_data
from config_manager import config


def port_libre(depart=5173):
    """Trouve un port libre : le port de l'interface ne doit jamais entrer en
    conflit avec celui du pont Notes & Suivi (4100 par défaut)."""
    interdit = {int(config.get("integration_port", 4100))}
    p = depart
    while p < depart + 60:
        if p not in interdit:
            with socket.socket() as s:
                if s.connect_ex(("127.0.0.1", p)) != 0:
                    return p
        p += 1
    return depart


def main():
    migrations = db.initialiser()
    if migrations:
        print("Base de données mise à jour :", ", ".join(migrations))
    seed_data.peupler_si_vide()

    if config.get("integration_active", True):
        ok, msg = ig.demarrer()      # échec silencieux : ne bloque jamais
        print(msg)

    url = api.demarrer(port_libre())
    print("Interface :", url)

    try:
        import webview
        fenetre = webview.create_window(
            "Correcteur — correction et analyse de textes d'élèves",
            url, width=1280, height=860, min_size=(1024, 680),
            confirm_close=False,
        )
        webview.start()
    except Exception as e:
        # Repli : si la fenêtre native est indisponible, on ouvre le navigateur.
        print(f"Fenêtre native indisponible ({e}). Ouverture dans le navigateur.")
        import webbrowser
        webbrowser.open(url)
        input("Appuie sur Entrée pour fermer l'application…")

    ig.arreter()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback
        traceback.print_exc()
        input("\nUne erreur est survenue. Note ce message, puis appuie sur Entrée…")
