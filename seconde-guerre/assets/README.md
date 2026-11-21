# Médias attendus — Radio Londres

Le jeu fonctionne sans aucun média (décors dessinés, cinématiques en direct). Les images et vidéos sont produites par la fabrique de nuit du PC (`outils-medias/nuit/`), à partir de `../immersifs/seconde-guerre/medias.csv` (prompts complets, complétés par `tests/donnees/gen_medias.py`) ; prompts manuels : `../immersifs/seconde-guerre/PROMPTS-GOOGLE-FLOW.md`.

**SUJET TRÈS SENSIBLE** : aucun uniforme allemand, aucun symbole nazi, aucun combat, aucune arme pointée, aucune image de camp ni de barbelés, aucun visage réel ; lieux calmes, ton grave et retenu. Tout média raté (faux texte lisible, visage déformé, symbole politique, détail violent) va dans `_a-supprimer/`.

- 5 décors (salle de classe de 1938, petite gare en juin 1940, épicerie en hiver 1942, cabane de maquis dans la forêt du Morvan, place de la mairie pavoisée le 8 mai 1945) : image IA créditée « généré par IA » (reconstitution).
- 5 portraits de personnages inventés (Bastien, Paul, Madeleine, Marc, Lucie ; jamais de personne réelle).
- 5 vidéos de transition (image vers vidéo, 8 s, mouvements lents).
- Documents d'époque possibles (archives libres de droits, Wikimedia Commons ou Gallica, crédits automatiques) : ticket de rationnement, journal clandestin, affiche de l'appel du 18 Juin (vérifier la licence). Jamais de photo de camp, de déportés ou de combat.
- Cartes (France coupée en deux en 1940, Libération en 1944), frise 1919-1945 et schéma de la Résistance : dessinés en SVG par script (`tests/donnees/schemas.py`) ; ne jamais les remplacer par des images IA.
