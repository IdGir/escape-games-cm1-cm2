"""sauvegarde.py — Sauvegardes automatiques rotatives de la base (Phase I).

Copie fiable via l'API sqlite3 .backup(), rotation des N plus récentes,
restauration avec filet de sécurité. Ne lève jamais en sauvegarde.

COPIE EXTERNE (ajout 2026-07)
-----------------------------
Les sauvegardes locales vivent à côté de la base : si le disque lâche, tout
part ensemble. On ajoute donc une COPIE dans un second dossier choisi par
l'enseignant — dossier Nextcloud synchronisé, clé USB, disque réseau…

Trois règles :
  · la copie externe n'est jamais bloquante — si la clé est débranchée ou le
    dossier introuvable, la sauvegarde locale a déjà réussi et l'application
    continue ; on garde seulement un message d'état pour l'écran Réglages ;
  · la rotation y est indépendante (on peut en garder plus qu'en local) ;
  · on peut restaurer indifféremment depuis le local ou depuis l'externe.
"""
import os
import shutil
import sqlite3
from datetime import datetime

NB_CONSERVEES = 10
NB_CONSERVEES_EXTERNE = 10
PREFIXE = "correcteur_"
SUFFIXE = ".db"


class GestionnaireSauvegardes:
    def __init__(self, chemin_base, dossier, nb_conservees=NB_CONSERVEES):
        self.chemin_base = str(chemin_base)
        self.dossier = str(dossier)
        self.nb_conservees = nb_conservees
        os.makedirs(self.dossier, exist_ok=True)
        # Copie externe (désactivée tant que l'enseignant n'a rien réglé)
        self.dossier_externe = ""
        self.externe_actif = False
        self.nb_externe = NB_CONSERVEES_EXTERNE
        self.dernier_message_externe = ""
        self.derniere_copie_externe = ""

    # ------------------------------------------------------------------
    #  Réglage de la copie externe
    # ------------------------------------------------------------------
    def configurer_externe(self, dossier="", actif=False, nb_conservees=None):
        """Applique les réglages. Sans effet de bord : rien n'est écrit ici."""
        self.dossier_externe = str(dossier or "").strip()
        self.externe_actif = bool(actif and self.dossier_externe)
        if nb_conservees:
            try:
                self.nb_externe = max(1, int(nb_conservees))
            except (TypeError, ValueError):
                pass

    @staticmethod
    def tester_dossier(dossier):
        """Vérifie qu'on peut vraiment écrire dans ce dossier.

        Renvoie (ok, message) — le message est destiné à l'enseignant, pas au
        journal technique.
        """
        chemin = str(dossier or "").strip()
        if not chemin:
            return False, "Aucun dossier indiqué."
        try:
            os.makedirs(chemin, exist_ok=True)
        except Exception:
            return False, ("Ce dossier ne peut pas être créé. Vérifiez que la clé USB "
                           "est branchée ou que le chemin est correct.")
        temoin = os.path.join(chemin, ".correcteur-test-ecriture")
        try:
            with open(temoin, "w", encoding="utf-8") as f:
                f.write("ok")
            os.remove(temoin)
        except Exception:
            return False, "Ce dossier existe mais l'application n'a pas le droit d'y écrire."
        return True, "Dossier accessible en écriture."

    def etat_externe(self):
        """Résumé pour l'écran Réglages."""
        joignable = False
        if self.dossier_externe:
            joignable = os.path.isdir(self.dossier_externe)
        return {
            "actif": self.externe_actif,
            "dossier": self.dossier_externe,
            "joignable": joignable,
            "nb_conservees": self.nb_externe,
            "nb_copies": len(self._fichiers_tries(self.dossier_externe)) if joignable else 0,
            "message": self.dernier_message_externe,
            "derniere_copie": self.derniere_copie_externe,
        }

    # ------------------------------------------------------------------
    #  Sauvegarde
    # ------------------------------------------------------------------
    def sauvegarder(self, etiquette="auto"):
        try:
            if not os.path.exists(self.chemin_base):
                return None
            h = datetime.now().strftime("%Y-%m-%d_%Hh%M")
            dest = os.path.join(self.dossier, f"{PREFIXE}{h}_{etiquette}{SUFFIXE}")
            src = sqlite3.connect(self.chemin_base)
            try:
                cible = sqlite3.connect(dest)
                try:
                    src.backup(cible)
                finally:
                    cible.close()
            finally:
                src.close()
            self._rotation()
            # La copie externe vient APRÈS : son échec ne remet jamais en
            # cause la sauvegarde locale, qui est déjà écrite.
            self._copier_externe(dest)
            return dest
        except Exception:
            return None

    def _copier_externe(self, chemin_source):
        if not self.externe_actif or not self.dossier_externe:
            return False
        try:
            os.makedirs(self.dossier_externe, exist_ok=True)
            cible = os.path.join(self.dossier_externe, os.path.basename(chemin_source))
            shutil.copy2(chemin_source, cible)
            self._rotation_externe()
            self.derniere_copie_externe = datetime.now().strftime("%d/%m/%Y à %Hh%M")
            self.dernier_message_externe = ""
            return True
        except Exception:
            # Cas courant et sans gravité : clé USB débranchée, dossier
            # Nextcloud momentanément indisponible. On le signale sans alarmer.
            self.dernier_message_externe = (
                "La copie de sécurité n'a pas pu être écrite dans le dossier externe "
                "(clé débranchée ou dossier indisponible). La sauvegarde locale, elle, "
                "a bien été faite."
            )
            return False

    def sauvegarde_quotidienne_si_absente(self):
        jour = datetime.now().strftime("%Y-%m-%d")
        for s in self.lister():
            if s["nom"].startswith(f"{PREFIXE}{jour}"):
                # Sauvegarde locale déjà faite aujourd'hui : on tente quand même
                # la copie externe si elle manque (clé rebranchée depuis).
                self._copier_manquantes_externe()
                return None
        return self.sauvegarder("quotidienne")

    def _copier_manquantes_externe(self):
        """Rattrape les copies externes manquantes (clé rebranchée)."""
        if not self.externe_actif or not os.path.isdir(self.dossier_externe or ""):
            return 0
        presents = {os.path.basename(c) for c in self._fichiers_tries(self.dossier_externe)}
        n = 0
        for chemin in self._fichiers_tries()[: self.nb_externe]:
            if os.path.basename(chemin) not in presents:
                if self._copier_externe(chemin):
                    n += 1
        return n

    # ------------------------------------------------------------------
    #  Listing / rotation
    # ------------------------------------------------------------------
    def _fichiers_tries(self, dossier=None):
        d = str(dossier or self.dossier)
        try:
            ch = [os.path.join(d, f) for f in os.listdir(d)
                  if f.startswith(PREFIXE) and f.endswith(SUFFIXE)]
        except OSError:
            return []
        return sorted(ch, key=os.path.getmtime, reverse=True)

    def _rotation(self):
        for c in self._fichiers_tries()[self.nb_conservees:]:
            try:
                os.remove(c)
            except OSError:
                pass

    def _rotation_externe(self):
        for c in self._fichiers_tries(self.dossier_externe)[self.nb_externe:]:
            try:
                os.remove(c)
            except OSError:
                pass

    def lister(self, externe=False):
        dossier = self.dossier_externe if externe else self.dossier
        if externe and not dossier:
            return []
        out = []
        for c in self._fichiers_tries(dossier):
            try:
                st = os.stat(c)
            except OSError:
                continue
            out.append({
                "nom": os.path.basename(c),
                "date": datetime.fromtimestamp(st.st_mtime).strftime("%d/%m/%Y à %Hh%M"),
                "taille_ko": round(st.st_size / 1024, 1),
                "ou": "externe" if externe else "local",
            })
        return out

    # ------------------------------------------------------------------
    #  Restauration
    # ------------------------------------------------------------------
    def restaurer(self, nom, externe=False):
        dossier = self.dossier_externe if externe else self.dossier
        if not dossier:
            return False
        src = os.path.join(dossier, os.path.basename(nom))
        if not os.path.exists(src):
            return False
        try:
            self.sauvegarder("avant-restauration")
            t = sqlite3.connect(src)
            t.execute("PRAGMA schema_version;")
            t.close()
            shutil.copy2(src, self.chemin_base)
            return True
        except Exception:
            return False
