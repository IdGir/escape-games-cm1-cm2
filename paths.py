"""Résolution des chemins, compatible exécution normale et .exe PyInstaller."""
import os, sys
from pathlib import Path

def est_gele() -> bool:
    return getattr(sys, "frozen", False)

def dossier_ressources() -> Path:
    if est_gele():
        return Path(getattr(sys, "_MEIPASS", os.path.dirname(sys.executable)))
    return Path(__file__).resolve().parent

def dossier_donnees() -> Path:
    """Dossier inscriptible où vivent la base et la configuration."""
    if os.name == "nt":
        base = Path(os.environ.get("APPDATA", Path.home())) / "CorrecteurPedagogique"
    else:
        base = Path.home() / ".correcteur_pedagogique"
    base.mkdir(parents=True, exist_ok=True)
    return base

def chemin_base() -> Path:
    return dossier_donnees() / "correcteur.db"

def chemin_config() -> Path:
    return dossier_donnees() / "config.json"

def dossier_exports() -> Path:
    d = dossier_donnees() / "exports"
    d.mkdir(parents=True, exist_ok=True)
    return d
