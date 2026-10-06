# Rapport de migration — De l'édit de Nantes à Versailles

Jeu d'origine : `versailles/` (**non modifié**). Variante immersive : `immersifs/versailles/`.

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
node immersifs/versailles/tests/test-immersif.js
```

Le test joue toutes les énigmes de tous les grades. Ouvrir ensuite le jeu avec `lancer-nautilus.bat` (adresse : `/immersifs/versailles/`).

## Suivi (7 octobre 2026) : narration et images

- ✅ **Images** : 5 décors et les portraits de tous les personnages produits avec Agnes (agnes-image-2.5-flash), déposés avec crédits ; **à valider par l'enseignant** (droits d'usage, fidélité à l'époque, cohérence des personnages).
- ✅ **Narration** : enjeu, situation, réaction du décor, objets cliquables, phrases des personnages (énigmes 2 à 4) et ton rédigés (`vingt-mille-lieues/outils/immersif/narration/<jeu>.json`, appliqués par `appliquer-narration.py`). Brouillons à relire et enrichir.
- ⬜ **Zones cliquables** : positions standard, à caler sur chaque image (`outils/caler-effets.html`).
- ⬜ **Vidéos** d'ouverture et de fin : non produites.
