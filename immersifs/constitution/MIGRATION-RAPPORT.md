# Rapport de migration — Le Sceau de la République

Jeu d'origine : `constitution/` (**non modifié**). Variante immersive : `immersifs/constitution/`.

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
node immersifs/constitution/tests/test-immersif.js
```

Le test joue toutes les énigmes de tous les grades. Ouvrir ensuite le jeu avec `lancer-nautilus.bat` (adresse : `/immersifs/constitution/`).
