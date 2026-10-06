# Produire ou ajouter des images et des vidéos

Rien n'est généré sans que vous le demandiez, aucun média n'entre dans le jeu sans votre choix, et la clé d'API n'est jamais écrite ni affichée. Le jeu fonctionne sans aucun média (décors dessinés, cinématiques en direct) ; les médias le rendent plus beau.

Deux voies, que l'on peut mêler :

| Voie | Pour qui | Commande |
|---|---|---|
| **A. Produire avec une source** (Agnes, OpenAI, tout service ajouté) | génération automatique à partir des prompts de `medias.csv` | `outils/medias/produire.py` |
| **B. Déposer ce qu'on a fait ailleurs** (Midjourney, ChatGPT, Runway, photo, dessin) | aucune clé, aucun réglage | `outils/medias/importer-image.py` |

## 1. Où vont les fichiers

| Média | Fichier | Remarque |
|---|---|---|
| fond d'un décor | `assets/images/decors/<décor>.webp` (ou .png / .jpg) | 1920×1080 ; le moteur le prend aussitôt, **sinon** décor dessiné de secours |
| portrait | `assets/images/personnages/<id>.webp` | 1200×1600 ; sinon portrait dessiné |
| **point de départ d'une vidéo** | `assets/medias-depart/<vidéo>.jpg` | 1280×720 ; lu par le service de vidéo |
| vidéo d'ouverture / de fin | `assets/videos/transition-e<N>.mp4`, `fin-e<N>.mp4`, `intro.mp4`, `fin.mp4` | se pose sur le **premier plan** de la cinématique du même nom ; voix et sous-titres restent dans le jeu |

Le moteur choisit toujours le fichier déposé s'il existe ; **supprimez-le pour revenir au décor de secours**. Si une vidéo ne se lit pas, elle disparaît et le décor animé continue.

## 2. Voie B — déposer une image faite ailleurs (le plus simple)

Une même image peut servir de **fond** et de **point de départ de vidéo** :

```
python outils/medias/importer-image.py atelier.png --decor imprimerie --source "Midjourney v6"
python outils/medias/importer-image.py atelier.png --decor imprimerie --depart transition-e1       # fond ET départ de la vidéo transition-e1
python outils/medias/importer-image.py visage.png --portrait tommaso
python outils/medias/importer-image.py clip.mp4  --video transition-e2 --source "Runway"           # vidéo déjà faite (piste audio retirée)
python outils/medias/importer-image.py https://…/image.png --decor sas                              # le fichier peut être une adresse
```

**Par dossier** (glisser-déposer) : mettez les fichiers dans `assets/medias-a-importer/`, nommés `decor-<id>.png`, `portrait-<id>.jpg`, `depart-<vidéo>.jpg`, `video-<nom>.mp4`, puis `python outils/medias/importer-image.py --dossier`. Les fichiers traités sont rangés dans `importes/`.

L'import convertit et recadre au bon format, met à jour `medias.csv` (« déposé ») et ajoute une ligne à `assets/medias/CREDITS-medias.md` (source, droits d'usage, date). Précisez `--source` et `--licence`.

## 3. Voie A — produire avec une source

```
python outils/medias/produire.py --liste-sources                       # sources connues, clé définie ou non
python outils/medias/produire.py --essai --id decor-imprimerie         # montre l'appel, ne l'exécute pas
python outils/medias/produire.py --id decor-imprimerie --variantes 2   # 2 propositions d'image
python outils/medias/produire.py --source openai-images --id portrait-tommaso
```

Les propositions arrivent dans `assets/medias-proposes/` (jamais publié). Comparez-les dans `outils/choisir-medias.html`, puis déposez la bonne avec la voie B (`importer-image.py proposition.webp --decor …`).

**Plafonds de sécurité** : 4 images et **0 vidéo** par exécution tant que vous n'ajoutez pas `--max-images N` / `--max-videos N`. Chaque source indique son coût dans `--liste-sources`.

### Vidéos

```
python outils/medias/produire.py --types video --id video-transition-e1 --max-videos 1 --depart assets/medias-depart/transition-e1.jpg
python outils/medias/produire.py --types video --id video-transition-e1 --max-videos 1 --depart-decor imprimerie   # départ pris dans le décor déposé
python outils/medias/produire.py --reprendre                                                                        # reprend un travail déjà créé
```

L'**image de départ** peut venir de n'importe où (voie B, `--depart`) ou du décor déjà déposé (`--depart-decor`). Les services de vidéo lisent cette image par **adresse publique** : le fichier de `assets/medias-depart/` doit être poussé sur GitHub (`git add`, `commit`, `push`) ; l'outil vérifie qu'il est lisible et le dit sinon. Hébergement ailleurs : `hebergement_images` dans `sources-medias.json`. Les files d'attente pleines (503) et les quotas (429) sont réessayés tout seuls.

## 4. La clé d'API

Chaque source donne le **nom** de sa variable d'environnement (Agnes : `AGNES_API_KEY`). Deux façons de la fournir, au choix :

- Windows PowerShell, pour la session : `$env:AGNES_API_KEY = "…"` ;
- ou une ligne `AGNES_API_KEY=…` dans le fichier **`cles-api.local`** à la racine du jeu : ce fichier est dans `.gitignore`, il n'est **jamais publié**.

Ne la collez jamais dans un fichier du dépôt, un message de commit ou une conversation. Le test du jeu refuse une clé qui se trouverait dans les données ou la configuration.

## 5. Ajouter une nouvelle source (sans programmer)

Ouvrez `outils/medias/sources-medias.json`, copiez le bloc `exemple-http-generique`, renommez-le et adaptez :

```json
"mon-service": {
  "nom": "Mon service",
  "base_url": "https://api.mon-service.fr",
  "cle": { "env": "MONSERVICE_API_KEY", "en_tete": "X-Api-Key", "format": "{cle}" },
  "image": {
    "methode": "POST", "url": "{base_url}/generate", "modeles": ["modele-a"],
    "corps": { "text": "{prompt}", "model": "{modele}", "aspect": "{ratio}", "image_urls": "{refs}" },
    "reponse": { "b64": "result.image_base64", "url": "result.image_url" }
  },
  "video": {
    "modeles": ["modele-v"],
    "creer":  { "url": "{base_url}/video/jobs", "corps": { "text": "{prompt}", "first_image": "{depart}", "duration": "{secondes}" }, "reponse": { "id": "job.id" } },
    "sonder": { "url": "{base_url}/video/jobs/{id}", "statut": "job.state", "termine": ["done"], "echec": ["error"], "url_video": "job.output.url" },
    "depart": { "mode": "url" }
  }
}
```

- **Valeurs disponibles** dans les modèles : `{prompt}`, `{negatif}`, `{modele}`, `{ratio}`, `{taille}`, `{refs}` (images de référence), `{depart}` / `{fin}` (images de départ et d'arrivée d'une vidéo), `{secondes}`, `{id}`, `{base_url}`. Un champ dont la valeur est vide est **retiré** de la requête.
- **Réponse** : chemins pointés (`data.0.b64_json`). Une image peut revenir en base64 ou par adresse.
- **Départ d'une vidéo** : `"mode": "url"` (adresse publique), `"base64"` ou `"data-uri"` selon ce que le service accepte.
- **Source par défaut** : `"defaut": { "image": "mon-service", "video": "agnes" }`. Pour une seule fois : `--source mon-service`.
- **Service hors cadre** (fichiers multipart, signature de requête…) : ajoutez `"adaptateur": "mon_adaptateur.py"` ; ce fichier définit `produire_image(source, prompt, ratio, taille, refs, negatif)` et/ou `produire_video(source, prompt, depart, fin, secondes)` et rend les octets de l'image ou l'adresse de la vidéo.
- **Vérifier** : `produire.py --liste-sources` (clé détectée ?) puis `produire.py --essai --id <média> --source mon-service` (aucun appel).

Sources fournies : `agnes` (images et vidéos ; vidéo « flash » gratuite à ce jour), `openai-images` (API compatible OpenAI), `exemple-http-generique` (modèle à copier), `fichier-local` (voie B).

## 6. Le fil complet pour un jeu migré

1. `migrer-jeu.py <jeu>` → `immersifs/<jeu>/` avec `medias.csv` (décors, portraits, vidéos d'ouverture).
2. Fonds : voie A ou B pour chaque décor ; vérifier à l'écran (`?verif=1&escale=1&niveau=matelot&enigme=1`).
3. Caler zones et effets sur l'image (`outils/caler-effets.html`).
4. Vidéos d'ouverture : `--depart-decor <décor>` puis `--max-videos 1`.
5. Pousser, valider, fusionner.
