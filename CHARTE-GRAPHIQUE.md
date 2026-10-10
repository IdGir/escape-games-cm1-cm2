# Charte graphique commune — escape games CM1/CM2

Une page pour que les jeux, produits un par un, gardent **une même identité visuelle**.
Elle décrit ce que les 12 jeux « salles » font déjà (relevé sur le code en octobre 2026) et le fixe
comme règle pour les suivants. Contrôle automatique : `node outils-tests/verifier-charte.js`.

## 1. Le socle commun (identique dans tous les jeux)

| Rôle | Variable CSS | Valeur |
|---|---|---|
| Fond des cartes (papier) | `--parchemin` · `--parchemin-clair` · `--parchemin-ombre` | `#f4e9d0` · `#fbf3dd` · `#e0cfa6` |
| Texte (encre) | `--encre` · `--encre-doux` | `#2b1d10` · `#4a3825` |
| Blanc cassé (texte sur bouton) | `--blanc` | `#fbf6e9` |
| Or (récompenses, coffre, bouton actif) | `--or` · `--or-clair` | `#c9a227` · `#e6c757` |
| Alerte | `--rouge-vif` | `#d62828` |

- **Typographie** : Georgia (titres et texte), `font-family:inherit` pour les boutons. Les polices
  d'accessibilité (Atkinson Hyperlegible, OpenDyslexic — `commun/polices/`) remplacent Georgia sur choix
  de l'élève : ne jamais figer une police en dur dans un texte d'énigme.
- **Formes** : cartes à coins arrondis (`--radius`), boutons « pilule » (`border-radius:30px`),
  ombre portée basse sous les boutons.
- **Or** : jamais de texte blanc sur l'or (contraste 2,2:1) — texte `#3a2a00`.

**Exception assumée** : *Le Laboratoire de Madame Mélange* (`melanges`) remplace le papier par un
« papier de laboratoire » vert d'eau (`--parchemin:#e8f0ed`, `--encre:#1b2a2e`). C'est la seule.

## 2. Les deux couleurs propres à chaque jeu

Chaque jeu choisit **deux couleurs d'accent** et les range toujours dans les mêmes variables
(`--bleu` = couleur principale : bandeau, boutons, titres ; `--rouge` = seconde couleur : bouton de
validation, accents), avec leurs nuances `-fonce` et `--bleu-nuit` (fond de l'écran de jeu).
Règle de lisibilité : **contraste ≥ 4,5:1** de chacune avec `--blanc` (texte des boutons).

| Jeu | `--bleu` | `--rouge` | Esprit |
|---|---|---|---|
| declaration · constitution | `#1d3a8a` | `#b22222` | bleu et rouge républicains |
| station-meteo · tour-du-monde | `#1d3a8a` | `#b22222` | palette par défaut, reprise telle quelle |
| moyen-age-abbaye | `#1f3f8f` | `#a8261b` | lapis et vermillon des enluminures |
| chateau-fort | `#3d5266` | `#8f3a2d` | ardoise et brique |
| versailles | `#2a3f6b` | `#8a2626` | bleu roi et pourpre |
| renaissance | `#8a4b1e` | `#2f5d5a` | sanguine et vert-de-gris |
| alimentation | `#2b5d6b` | `#a8432a` | bleu canard et terre cuite |
| objets-techniques | `#1e5a6e` | `#a8461b` | bleu acier et cuivre |
| lumiere | `#1d3557` | `#b03a2e` | nuit marine et feu du phare |
| melanges | `#1f5f6b` | `#8e3b62` | sarcelle et prune |

Pour un **nouveau jeu** : choisir un couple qui n'est pas déjà pris (station-meteo et tour-du-monde
gardent pour l'instant la palette par défaut), vérifier le contraste, l'écrire dans `css/style.css`.

## 3. Les décors dessinés (`js/decors.js`)

- **Format** : `viewBox="0 0 800 300"`, `preserveAspectRatio="xMidYMid slice"` (le décor remplit la scène).
- **Style** : aplats vectoriels simples, pas de contours noirs. Un contour est **une teinte plus foncée
  du remplissage** (bois `#8a5d33` → contour `#4a2f16`).
- **Profondeur en 3 plans** : ciel en **dégradé vertical** à 2 arrêts (`linearGradient`) ; plan du fond
  clair et un peu transparent (`opacity` .6-.7) ; premier plan plus foncé et plus contrasté. Horizon
  entre y = 180 et y = 225.
- **Épaisseurs de trait** (relevé des 12 jeux) :

  | Usage | `stroke-width` |
  |---|---|
  | détails fins : joints de pierre, lattes, gravures | 1 à 1,5 |
  | contour normal d'un objet | **2** (le plus fréquent) à 3 |
  | objets forts, roues, cordages | 4 à 5 |
  | maximum (rivière, rayon du phare) | 7 à 12, rare |

- **Mouvement** : lent et discret (nuages 100 à 130 s, oiseaux ~40 s, mécanismes ~9 s), en SMIL
  (`<animate>`) ou par les classes de `commun/css/animations.css`. Tout s'arrête avec « animations
  réduites » (`body.calme`).
- **Pas de texte dans le décor** : le lieu et la description sont dans le bandeau du jeu.
- Ordre d'affichage (`commun/js/media.js`) : vidéo → photo → décor dessiné. Le dessin est la
  version qui reste toujours disponible : il doit se suffire à lui-même.

## 4. Les personnages (`js/personnages.js`)

- **Format** : plein corps, `viewBox="0 0 200 320"`, même squelette dans tous les jeux (classes
  `.tete .yeux .paupiere .bouche .sourcils .buste .bras-g/-d .avant-g/-d .main-g/-d .jambes`) : la
  bouche bouge avec la voix, les gestes (`.geste-pointe`, `-joie`, `-inquiet`, `-salue`) sont communs.
- **Carnations** (objet `PEAU`, une couleur + son ombre) :
  `claire #f6dcc0/#e9c49e` · `hale #e2b183/#c48f5e` · `foncee #a2663c/#7d4a28` · `pale #f8e6d2/#ecd0b4`.
  Une équipe de personnages mélange les carnations.
- **Style** : proportions réalistes d'enfant ou d'adulte (pas de grosse tête de mascotte), visage
  simple (yeux ronds, sourcils marqués, bouche animée), vêtements fidèles à l'époque du jeu, dans les
  couleurs du jeu et des tons naturels (bruns, beiges, gris).
- **Jamais une personne réelle** reconnaissable, même historique : on invente un témoin plausible
  (un apprenti, une meunière) ; les personnages historiques sont évoqués, pas dessinés en héros.

## 5. Photos, images et vidéos

- **Lieux réels** : photographies libres (Wikimedia Commons, Gallica…), crédit (auteur, licence, URL)
  dans `assets/medias/CREDITS-medias.md` et affiché dans le jeu. Rien d'inventé : un bâtiment montré
  doit être le vrai.
- **Images générées** (personnages, scènes génériques) : photoréalistes, calmes, **sans texte**, sans
  logo, aucune ressemblance avec une personne connue.
- **Vidéos de décor** : 5 s, mouvement de caméra lent (travelling avant), rien de nouveau n'apparaît,
  pas de texte à l'écran ; sous-titres `.vtt` du même nom (voir `outils-medias/sous-titres.py`).
- **Cartes et schémas** : jamais générés par IA ; SVG calibrés sur des sources officielles (IGN, SANDRE,
  SHOM), source affichée sous la carte.

## 6. Ce qu'on vérifie avant de publier

1. `node outils-tests/verifier-charte.js` : socle identique, couleurs d'accent lisibles, formats des
   décors (800 × 300) et des personnages (200 × 320), carnations de la palette.
2. Un coup d'œil au jeu avec « animations réduites » : plus rien ne bouge, tout reste lisible.
3. Un coup d'œil en noir et blanc (impression) : les cartes et schémas restent compréhensibles.
