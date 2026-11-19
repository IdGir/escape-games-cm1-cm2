# Médias attendus — Les Lettres du poilu

Le jeu fonctionne sans aucun média (décors dessinés, cinématiques en direct). Les images et vidéos sont produites par la fabrique de nuit du PC (`outils-medias/nuit/`), à partir de `../immersifs/grande-guerre/medias.csv` (prompts complets, complétés par `tests/donnees/gen_medias.py`) ; prompts manuels : `../immersifs/grande-guerre/PROMPTS-GOOGLE-FLOW.md`.

**SUJET SENSIBLE** : aucun blessé, aucun combat, aucune explosion, aucune arme pointée, aucun visage réel ; lieux calmes, ton du souvenir. Tout média raté (faux texte lisible, visage déformé, détail violent) va dans `_a-supprimer/`.

- 5 décors (place du village en août 1914, abri de tranchée calme, atelier d'usine d'obus, salle de classe devenue hôpital aux lits vides, monument aux morts en 1922) : image IA créditée « généré par IA » (reconstitution).
- 5 portraits de personnages inventés (Jeanne, Louis, Marcelle, Odette, Émile ; jamais de personne réelle).
- 5 vidéos de transition (image vers vidéo, 8 s, mouvements lents).
- Documents d'époque possibles (photos d'archives libres de droits, Wikimedia Commons ou Europeana, crédits automatiques) : affiche de mobilisation générale de 1914, monument aux morts d'une commune de Côte-d'Or, munitionnettes au travail. Jamais de photo de blessé ni de champ de bataille.
- Schémas (coupe de tranchée, monument, frise 1914-1922, alliances, front et arrière) : dessinés en SVG par script (`tests/donnees/schemas.py`), ne jamais les remplacer par des images IA. Cartes : jamais générées par IA.
