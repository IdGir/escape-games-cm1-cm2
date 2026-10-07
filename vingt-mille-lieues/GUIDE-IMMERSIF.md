# Passer un escape game existant au modèle immersif

Le modèle immersif, c'est celui de « Vingt mille lieues sous les mers » : un **décor plein écran** (image + effets animés), des **objets cliquables** qui ouvrent les énigmes, un **personnage qui parle** (voix et sous-titres), des **cinématiques**, des **grades**, un **journal de bord** et un **coffre final**. Le moteur est le même pour tous les jeux ; seuls les données et le thème changent.

## 1. Le principe : une variante, jamais un écrasement

Le migrateur lit un jeu d'origine (`renaissance/`, `versailles/`…) et écrit **à côté**, dans `immersifs/<jeu>/`, une variante immersive complète. **Le jeu d'origine n'est pas touché** (le test le vérifie octet pour octet). Vous comparez, vous complétez, puis vous décidez du sort de l'original (§ 5).

```
python vingt-mille-lieues/outils/immersif/migrer-jeu.py --lister              # jeux migrables
python vingt-mille-lieues/outils/immersif/migrer-jeu.py renaissance           # une variante → immersifs/renaissance/
python vingt-mille-lieues/outils/immersif/migrer-jeu.py --tous                # toutes les variantes
node immersifs/renaissance/tests/test-immersif.js                             # joue toutes les énigmes de tous les grades
immersifs/renaissance/lancer.bat                                              # ouvre le jeu (Windows)
```

Chaque variante contient `MIGRATION-RAPPORT.md` : ce qui est fait, ce qu'il reste à faire, les avertissements.

## 2. Ce qui est converti automatiquement

| Jeu d'origine | Variante immersive |
|---|---|
| une **salle** | une **étape** (le mot affiché reste « salle », réglable dans le thème) |
| ses énigmes (10 types, `commun/js/enigmes.js`) | les mêmes énigmes, mêmes données, mêmes indices |
| `cm1` / `cm2` / `commun`, `niveaux: ["CM2"]` | grades **matelot** (CM1) et **timonier** (CM2) ; une énigme réservée au CM2 n'existe qu'à ce grade |
| `motCle` de chaque salle | mot du coffre final |
| personnages (`dialogues.json`) | personnages avec voix et **portrait dessiné automatiquement** (déposez une image pour le remplacer) |
| `dialogue_intro` / `dialogue_reussite` | cinématiques d'ouverture et de fin de chaque étape |
| leçons (`lecons.json`) | Bibliothèque : fiches « essentiel / approfondi / expert » |
| décors SVG animés | décor générique **à remplacer par une image** (voir `GUIDE-MEDIAS.md`) |

Jeux migrables : `alimentation`, `chateau-fort`, `constitution`, `melanges`, `moyen-age-abbaye`, `objets-techniques`, `renaissance`, `station-meteo`, `versailles`. Les jeux `declaration`, `tour-du-monde` et `mission-geo` ont une structure plus ancienne (pas de `salles` dans `enigmes.json`) : le migrateur le dit et ne crée rien ; ils se refont avec la skill (« nouveau jeu immersif »).

## 3. Ce qu'il reste à faire (brouillons)

1. **Images** des décors et portraits : `medias.csv` contient déjà un prompt par média → `GUIDE-MEDIAS.md`.
2. **Zones cliquables** : chaque décor reçoit 3 à 4 zones à positions standard. Déposez l'image du décor, puis calez avec `outils/caler-effets.html` (zones et effets en % de l'image) et nommez chaque objet dans `assets/data/decors-fx.json`.
3. **Enjeu, réaction du décor, problème narratif** de chaque énigme (`assets/data/enigmes.json`) : le migrateur écrit une phrase d'attente (« À préciser… ») ; un champ `_brouillon` liste ce qui est provisoire.
4. **Phrases des personnages** pour les énigmes 2 à 4 de chaque étape (champ `dialogue` de chaque grade) et le texte des cinématiques (`dialogues.json`).
5. **Les 5 grades** (mousse, matelot, timonier, lieutenant, second) : le migrateur ne convertit que **matelot** (CM1) et **timonier** (CM2). Mousse, lieutenant et second sont **à écrire pour chaque énigme** (bloc par grade, indices, `dialogue`, parfois un autre type ; lieutenant et second avec **justification**), sur le modèle de `vingt-mille-lieues/assets/data/enigmes.json`. Un jeu immersif complet a 5 salles, 3 à 4 énigmes par salle (15 à 20), à tous les grades. `--grades cm1:matelot,cm2:timonier,cm1:mousse` reprend le CM1 en « mousse » comme point de départ à réécrire.
6. Après chaque modification d'un JSON : `python immersifs/<jeu>/outils/embarquer-donnees.py`, puis le test.

## 4. Personnaliser le thème

Copiez `outils/immersif/theme-defaut.json`, modifiez-le, puis `migrer-jeu.py <jeu> --theme mon-theme.json --force` (⚠ `--force` régénère aussi les données : à faire AVANT de les corriger à la main).

- `mots` : « escale » → « salle », « étape », « station »… (féminin ; remplacé dans tout le texte affiché).
- `textes` : titre, sous-titre, nom du journal, de la bibliothèque, du coffre, de la pause.
- `noms_grades` : noms et icônes des grades (Apprenti, Compagnon, Maître…).
- `palette` : variables CSS (`laiton`, `ocean`, `acajou`, `ambre`…) → `css/theme.css`.
- `style_visuel`, `negatif` : charte des prompts d'images.

Le titre, les grades et la clé de sauvegarde de chaque jeu sont aussi dans `immersifs/<jeu>/js/jeu-config.js` (modifiable à la main).

## 5. Le sort du jeu d'origine

| Option | Comment | Quand |
|---|---|---|
| **Garder les deux** (recommandé au début) | rien à faire : l'original reste, la variante est à `/immersifs/<jeu>/` | pendant la validation |
| **Remplacer l'original** | l'enseignant décide, puis déplace `immersifs/<jeu>/` à la place du dossier d'origine (`git mv`) ; le garde-fou ne l'accepte que si on le **déverrouille jeu par jeu** : `bash outils-tests/verifier-isolation.sh --autoriser <jeu>` | une fois la variante complète et validée |
| **Brancher au catalogue** | `commun/donnees/catalogue.js`, `index.html`, `verifier.html`, `serveur.py`… (procédure de la skill, § 4) | au moment du remplacement |

⚠ Remplacer, c'est modifier des fichiers existants : le garde-fou `outils-tests/verifier-isolation.sh` refuse tant que l'enseignant n'a pas autorisé le jeu concerné. Hors remplacement, il laisse libres `vingt-mille-lieues/` et `immersifs/`, et protège tout le reste.

## 6. Faire évoluer le moteur sans perdre son travail

Le moteur de référence est `vingt-mille-lieues/js/`. Quand il évolue :

```
python vingt-mille-lieues/outils/immersif/migrer-jeu.py --maj-moteur immersifs/renaissance
```

Remplace `js/`, `css/`, les pages, les tests et les outils médias ; **conserve** les données, les médias, la config, le thème, `medias.csv`.

## 7. Tests

| Test | Ce qu'il fait |
|---|---|
| `tests/test-migration.js` | migre un jeu, vérifie que l'original est inchangé, la variante complète, les refus (sortie = source, structure inconnue), la mise à jour du moteur, puis **joue la variante** |
| `immersifs/<jeu>/tests/test-immersif.js` | données (grades, zones, leçons, fuites du thème « Nautilus », clés d'API) + partie complète : toutes les énigmes de tous les grades |
| `tests/test-medias-sources.js` | production de médias avec un faux service (§ `GUIDE-MEDIAS.md`) |
