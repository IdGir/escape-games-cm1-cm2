# Rapport de migration — Le Phare de l'île Lumière

Jeu d'origine : `lumiere/` (**non modifié**). Variante immersive : `immersifs/lumiere/`.

- 5 salles, 20 énigmes ; grades : CM1 → matelot, CM2 → timonier.
- Le moteur est une copie de celui de « Vingt mille lieues » ; seuls `js/jeu-config.js`, `css/theme.css` et `assets/data/*.json` sont propres à ce jeu.

## Ce qui est converti tel quel

Énigmes (types, données, consignes, indices), leçons (Bibliothèque), personnages, mots-clés du coffre, dialogues d'introduction et de réussite.

## Ce qu'il reste à faire (brouillons)

1. **Zones des décors** (5 décors) : 3 à 4 zones à positions standard. Déposer l'image du décor, puis caler avec `outils/caler-effets.html` et nommer chaque objet.
2. **Enjeu et réaction du décor** de chacune des 20 énigmes : rédiger (champs `enjeu`, `reaction_du_decor`, `probleme_narratif`).
3. **Phrases des personnages** pour les énigmes 2 à 4 de chaque salle : écrire ce que dit l'émetteur (champ `dialogue` de chaque grade).
4. **Médias** : `medias.csv` contient les prompts des décors, portraits et vidéos → `python outils/medias/produire.py --source <fournisseur>` (voir GUIDE-IMMERSIF.md).
5. **Grades supplémentaires** (mousse, lieutenant, second) : à écrire si souhaité (le moteur les prend en charge).

## Vérifier

```
node immersifs/lumiere/tests/test-immersif.js
```

Le test joue toutes les énigmes de tous les grades. Ouvrir ensuite le jeu avec `lancer-nautilus.bat` (adresse : `/immersifs/lumiere/`).

## Suivi (7 octobre 2026) : narration

- ✅ **Narration** : enjeu, situation, réaction du décor, objets cliquables, phrases des personnages (énigmes 2 à 4) et ton rédigés (`vingt-mille-lieues/outils/immersif/narration/lumiere.json`, appliqués par `appliquer-narration.py`). Brouillons à relire et enrichir.
- ✅ Test immersif : 272 vérifications réussies, 0 échec.
- ⬜ **Images** (5 décors, portraits) : non produites, en attente de l'accord de l'enseignant (source et budget).
- ⬜ **Zones cliquables** : positions standard, à caler sur chaque image (`outils/caler-effets.html`).
- ⬜ **Vidéos** d'ouverture et de fin : non produites.

## Suivi (7 octobre 2026) : 5 grades, identité du jeu, voix

- ✅ **5 grades** : Allumeur (mousse), Veilleur (matelot), Gardien (timonier), Opticien (lieutenant), Expert du phare (second) ; noms neutres, liés à la lumière. Mousse et matelot jouent 15 énigmes, les trois autres 20 (la 4e énigme de chaque salle). Blocs écrits par `vingt-mille-lieues/outils/immersif/grades/lumiere_s1.py` à `_s5.py`, appliqués par `appliquer-grades.py lumiere`. Justification (lieutenant, second) contrôlée mot pour mot dans les fiches. Test immersif : 555 vérifications réussies.
- ✅ **Un guide par salle** (Maëlle, Salomé, Nils, Achille, Yasmine) au lieu d'un émetteur différent à chaque énigme.
- ✅ **Charte graphique propre** : nuit bleu marine et jaune de phare, fenêtre d'énigme claire à accents bleus (`css/theme.css`).
- ✅ **Voix Edge, une par personnage** : Denise, Vivienne, Remy (voix plus aiguë et rapide), Henri (grave, lent), Eloise ; 57 répliques en mp3 dans `assets/audio/voix/` (1,7 Mo environ). Ré-écouter quelques répliques avant de livrer ; régénérer avec `python outils/voix/generer-voix.py` après tout changement de dialogue.
- ✅ **Portraits dessinés** aux traits des personnages (en attendant les images).
- ⬜ À vérifier (faits dérivés ou valeurs inventées) : lumière du Soleil à la Terre en environ 8 minutes (150 millions de km à 300 000 km/s) ; premier quartier vers le 7e jour, dernier quartier vers le 22e jour d'une lunaison ; relevés d'ombres « fictifs » de la salle 4 ; durée de la lumière sur 30 km (0,0001 s).
- ⬜ **Images** (décors, portraits) à fournir par l'enseignant (ou à produire) ; vidéos Agnes à partir de ces images ; zones cliquables à caler sur les images.
