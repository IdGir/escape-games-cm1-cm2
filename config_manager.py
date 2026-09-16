"""Gestion de la configuration (fichier config.json dans le dossier de données)."""
import json
from paths import chemin_config

DEFAUTS = {
    # --- Apparence ---
    "theme_sombre": False,

    # --- Génération de texte par IA (module 1, source 3) ---
    "ia_active": False,
    "ia_moteur": "deepseek",           # "deepseek" | "ollama" | "api" | "hors_ligne"
    "ia_cle_api": "",
    "ia_url_ollama": "http://localhost:11434",
    "ia_modele_ollama": "gemma3:12b",
    # --- API personnalisée (tout service compatible OpenAI : OpenAI, Mistral,
    #     Groq, OpenRouter, un serveur local, etc.) ---
    "ia_url_api": "https://api.openai.com/v1",
    "ia_cle_api_perso": "",
    "ia_modele_api": "gpt-4o-mini",
    "ia_nom_api": "Mon service IA",    # nom affiché
    # --- Second moteur IA ---
    # Un moteur peut être meilleur en correction et l'autre pour rédiger.
    # « ia_taches » dit, pour chaque tâche, lequel des deux employer.
    "ia_moteur_secondaire": "aucun",   # "aucun" | "deepseek" | "ollama" | "api2"
    "ia_url_api2": "https://albert.api.etalab.gouv.fr/v1",
    "ia_cle_api2": "",
    "ia_modele_api2": "albert-large",
    "ia_nom_api2": "Albert",
    "ia_taches": {"correction": "principal", "aide": "principal",
                  "generation": "principal", "definitions": "principal"},

    "ia_nb_phrases": 5,
    "ia_niveau": 2,                    # 1 à 5
    "ia_theme": "la vie quotidienne à l'école",   # conservé pour compatibilité
    # Plusieurs thèmes peuvent être cochés : la génération en lot les fait
    # tourner, ce qui évite dix textes identiques sur le même sujet.
    "ia_themes": ["La vie quotidienne à l'école", "Les animaux",
                  "La nature et les saisons"],
    "ia_categories_ciblees": ["accord", "conjugaison", "homophone", "orthographe"],

    # --- Aide guidée (questions + indice) ---
    "aide_ia_active": True,            # laisser l'IA formuler question/indice si dispo
    "aide_penalise_score": True,      # tenir compte de l'aide dans l'autonomie

    # --- Critères d'évaluation du travail de correction (module 1) ---
    "eval_seuil_reussi": 60,          # % d'erreurs corrigées pour un travail « réussi »
    "eval_seuil_excellent": 90,       # % d'erreurs corrigées pour « excellent »
    "eval_objectif_autonomie": 60,    # % corrigées SANS aide visé (objectif d'autonomie)
    "eval_bonus_sans_aide": True,     # afficher un encouragement si l'objectif est atteint

    # --- Module 1 : repérage ---
    "vigilance_active": True,   # montrer les « points à vérifier » (jamais comptés)

    # --- Module 1 : sources autorisées pour les élèves ---
    "source_saisie_libre": True,
    "source_texte_impose": True,
    "source_generation_ia": True,

    # --- Cloisonnement de l'espace élève ---
    # Quand le mode est actif, l'élève ne peut plus revenir côté enseignant :
    # la sortie exige le code enseignant. Il ne voit que ses propres résultats
    # et seules les activités autorisées lui sont proposées.
    "eleve_verrouille": False,
    "activites_autorisees": ["correction", "fluence", "banque", "dico", "dictee"],
    # Restrictions par classe : {"3": ["correction"]}. Une classe absente de ce
    # dictionnaire suit « activites_autorisees ».
    "activites_par_classe": {},

    # --- Lecture en autonomie : transcription automatique de la voix ---
    # Désactivée par défaut. Quand elle est active, l'enregistrement de la
    # voix de l'élève est envoyé au service réglé ci-dessous pour être
    # transcrit. Rien n'est envoyé tant que l'enseignant n'a pas activé.
    "stt_active": False,
    "stt_url": "https://albert.api.etalab.gouv.fr/v1",
    "stt_cle": "",
    "stt_modele": "whisper-large-v3-turbo",
    "stt_nom": "Albert (DINUM)",
    "stt_conserver_audio": False,   # l'enregistrement n'est jamais gardé

    # --- Sauvegardes : copie dans un second dossier ---
    # Les sauvegardes automatiques vivent à côté de la base : si le disque
    # lâche, elles disparaissent avec elle. On peut donc en déposer une copie
    # dans un dossier synchronisé (Nextcloud) ou sur une clé USB. Vide et
    # inactif par défaut : rien ne sort de l'ordinateur sans réglage explicite.
    "sauvegarde_externe_active": False,
    "sauvegarde_externe_dossier": "",
    "sauvegarde_externe_nb": 10,

    # --- Module 2 : fluence ---
    "fluence_afficher_nb_mots": True,
    "fluence_niveau_classe": "CM1",    # sert de repère MCLM
    "fluence_qui_saisit_erreurs": "eleve_ou_enseignant",

    # --- Module 3 : seuils de détection des besoins de suivi ---
    "seuil_categorie_alerte": 3,       # nb d'occurrences d'une catégorie sur les N dernières séances
    "seuil_nb_seances": 3,             # N séances considérées
    "seuil_autonomie_faible": 50,      # % d'erreurs corrigées seul en dessous duquel on alerte
    "seuil_mclm_ecart": 25,            # % en dessous du repère MCLM déclenchant une alerte

    # --- Intégration Notes & Suivi / Portail Enseignant (pont, port 4100) ---
    "integration_active": True,
    "integration_port": 4100,
    "integration_code_app": "correcteur-pedagogique",
    "integration_jeton": "",           # facultatif, si vide pas de contrôle
    "integration_anonymiser_nom": True,  # RGPD : ne transmettre que le prénom
    # Écoute LAN du pont (0.0.0.0) pour consulter le Portail depuis la
    # tablette/le téléphone À LA MAISON. Désactivée par défaut, STRICTEMENT
    # indépendante du « mode salle » (qui ne concerne que l'espace élève de
    # l'interface principale). Garde-fou : quand le mode salle est actif, le
    # pont repasse d'office en 127.0.0.1, quelle que soit cette option.
    "integration_ecoute_lan": False,
}


class Config:
    def __init__(self):
        self._d = dict(DEFAUTS)
        self.charger()

    def charger(self):
        p = chemin_config()
        if p.exists():
            try:
                enregistre = json.loads(p.read_text(encoding="utf-8"))
                for k, v in enregistre.items():
                    self._d[k] = v
            except Exception:
                pass  # config corrompue : on repart des défauts

    def sauver(self):
        chemin_config().write_text(
            json.dumps(self._d, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    def get(self, cle, defaut=None):
        return self._d.get(cle, DEFAUTS.get(cle, defaut))

    def set(self, cle, valeur):
        self._d[cle] = valeur

    def tout(self):
        return dict(self._d)

    def reinitialiser(self):
        self._d = dict(DEFAUTS)
        self.sauver()


config = Config()
