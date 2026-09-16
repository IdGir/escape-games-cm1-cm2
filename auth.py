"""auth.py — Sécurité de l'espace enseignant (Phase I).

Code PIN enseignant (4–6 chiffres) haché, code de récupération à usage unique,
sessions en mémoire avec expiration (verrouillage automatique). Le PIN est
FACULTATIF : tant qu'il n'est pas créé, l'espace enseignant fonctionne comme
avant. Une fois créé, il protège l'accès au tableau de bord et aux réglages.

Rangé dans config.json sous la clé "securite" (jamais en clair).
"""
import hashlib
import hmac
import secrets
import time

DELAI_VERROU_DEFAUT_MIN = 15
ITERATIONS = 120_000


def _hacher(pin, sel):
    return hashlib.pbkdf2_hmac("sha256", pin.encode("utf-8"),
                               bytes.fromhex(sel), ITERATIONS).hex()


def _code_recuperation():
    a = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    return "-".join("".join(secrets.choice(a) for _ in range(4)) for _ in range(3))


class GestionnaireAuth:
    def __init__(self, config):
        self.config = config
        self._sessions = {}

    def _bloc(self):
        return self.config.get("securite", {}) or {}

    def _ecrire(self, bloc):
        self.config.set("securite", bloc)
        try:
            self.config.sauver()
        except Exception:
            pass

    def pin_defini(self):
        return bool(self._bloc().get("pin_hash"))

    def delai_verrou_min(self):
        return int(self._bloc().get("delai_verrou_min", DELAI_VERROU_DEFAUT_MIN))

    def definir_delai_verrou(self, minutes):
        bloc = self._bloc()
        bloc["delai_verrou_min"] = max(1, min(120, int(minutes)))
        self._ecrire(bloc)

    @staticmethod
    def _pin_valide(pin):
        return pin.isdigit() and 4 <= len(pin) <= 6

    def creer_pin(self, pin):
        if self.pin_defini():
            raise ValueError("Un code est déjà défini.")
        if not self._pin_valide(pin):
            raise ValueError("Le code doit contenir 4 à 6 chiffres.")
        sel, sel_rec = secrets.token_hex(16), secrets.token_hex(16)
        code = _code_recuperation()
        self._ecrire({
            "pin_hash": _hacher(pin, sel), "pin_sel": sel,
            "rec_hash": _hacher(code.replace("-", ""), sel_rec), "rec_sel": sel_rec,
            "delai_verrou_min": DELAI_VERROU_DEFAUT_MIN,
        })
        return code

    def _verifier_pin(self, pin):
        b = self._bloc()
        if not b.get("pin_hash"):
            return False
        return hmac.compare_digest(b["pin_hash"], _hacher(pin, b["pin_sel"]))

    def deverrouiller(self, pin):
        if not self._verifier_pin(pin):
            return None
        jeton = secrets.token_urlsafe(24)
        self._sessions[jeton] = time.time()
        return jeton

    def session_valide(self, jeton):
        if not jeton or jeton not in self._sessions:
            return False
        if time.time() - self._sessions[jeton] > self.delai_verrou_min() * 60:
            self._sessions.pop(jeton, None)
            return False
        self._sessions[jeton] = time.time()
        return True

    def verrouiller(self, jeton):
        self._sessions.pop(jeton, None)

    def _verifier_recuperation(self, code):
        b = self._bloc()
        if not b.get("rec_hash"):
            return False
        n = code.replace("-", "").replace(" ", "").upper()
        return hmac.compare_digest(b["rec_hash"], _hacher(n, b["rec_sel"]))

    def reinitialiser_par_recuperation(self, code, nouveau_pin):
        if not self._verifier_recuperation(code):
            raise ValueError("Code de récupération incorrect.")
        if not self._pin_valide(nouveau_pin):
            raise ValueError("Le code doit contenir 4 à 6 chiffres.")
        b = self._bloc()
        sel, sel_rec = secrets.token_hex(16), secrets.token_hex(16)
        nouveau = _code_recuperation()
        b.update({"pin_hash": _hacher(nouveau_pin, sel), "pin_sel": sel,
                  "rec_hash": _hacher(nouveau.replace("-", ""), sel_rec),
                  "rec_sel": sel_rec})
        self._ecrire(b)
        self._sessions.clear()
        return nouveau

    def changer_pin(self, jeton, ancien, nouveau):
        if not self.session_valide(jeton):
            raise PermissionError("Session enseignante requise.")
        if not self._verifier_pin(ancien):
            raise ValueError("Ancien code incorrect.")
        if not self._pin_valide(nouveau):
            raise ValueError("Le code doit contenir 4 à 6 chiffres.")
        b = self._bloc()
        sel = secrets.token_hex(16)
        b["pin_hash"] = _hacher(nouveau, sel)
        b["pin_sel"] = sel
        self._ecrire(b)

    def supprimer_pin(self, jeton):
        if not self.session_valide(jeton):
            raise PermissionError("Session enseignante requise.")
        self.config.set("securite", {})
        try:
            self.config.sauver()
        except Exception:
            pass
        self._sessions.clear()
