# Rapport de migration — Mission géographique

> **Construit par `mission-geo/tests/donnees/construire-immersif.py`** : les points 2, 3 et 5 ci-dessous sont faits (narration, phrases des personnages, 5 grades). Restent : zones des décors (après dépôt des images), médias (photos Wikimedia Commons pour les lieux réels), voix mp3. Ne pas modifier ce dossier à la main : relancer le script (voir mission-geo/REFONTE-IMMERSIVE.md, § 3).

Jeu d'origine : `mission-geo/` (**non modifié**). Variante immersive : `immersifs/mission-geo/`.

- 13 séances, 52 énigmes ; grades : CM1 → matelot, CM2 → timonier.
- Le moteur est une copie de celui de « Vingt mille lieues » ; seuls `js/jeu-config.js`, `css/theme.css` et `assets/data/*.json` sont propres à ce jeu.

## Ce qui est converti tel quel

Énigmes (types, données, consignes, indices), leçons (Bibliothèque), personnages, mots-clés du coffre, dialogues d'introduction et de réussite.

## Ce qu'il reste à faire (brouillons)

1. **Zones des décors** (13 décors) : 3 à 4 zones à positions standard. Déposer l'image du décor, puis caler avec `outils/caler-effets.html` et nommer chaque objet.
2. **Enjeu et réaction du décor** de chacune des 52 énigmes : rédiger (champs `enjeu`, `reaction_du_decor`, `probleme_narratif`).
3. **Phrases des personnages** pour les énigmes 2 à 4 de chaque séance : écrire ce que dit l'émetteur (champ `dialogue` de chaque grade).
4. **Médias** : `medias.csv` contient les prompts des décors, portraits et vidéos → `python outils/medias/produire.py --source <fournisseur>` (voir GUIDE-IMMERSIF.md).
5. **Grades supplémentaires** (mousse, lieutenant, second) : à écrire si souhaité (le moteur les prend en charge).

## Vérifier

```
node immersifs/mission-geo/tests/test-immersif.js
```

Le test joue toutes les énigmes de tous les grades. Ouvrir ensuite le jeu avec `lancer-nautilus.bat` (adresse : `/immersifs/mission-geo/`).
