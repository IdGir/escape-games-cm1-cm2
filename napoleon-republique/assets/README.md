# Médias attendus — Le Testament de l'Empereur

Le jeu fonctionne sans aucun média (décors dessinés, cinématiques en direct). Les images et vidéos sont produites par la fabrique de nuit du PC (`outils-medias/nuit/`), à partir de `../immersifs/napoleon-republique/medias.csv` (prompts complets, complétés par `tests/donnees/gen_medias.py`) ; prompts manuels : `../immersifs/napoleon-republique/PROMPTS-GOOGLE-FLOW.md`.

Règles : aucune personne réelle (jamais Napoléon, Joséphine ou le pape en personne), aucun combat, aucune blessure ; tout média raté (faux texte lisible, visage déformé, sosie de Napoléon) va dans `_a-supprimer/`.

- 5 décors : antichambre des Tuileries (1800), Notre-Dame décorée pour le sacre (1804), tente du bivouac de la Grande Armée, dôme des Invalides (aujourd'hui), salle des mariages d'une mairie (aujourd'hui). Reconstitutions : image IA créditée « généré par IA ». Lieux réels d'aujourd'hui (dôme des Invalides) : de préférence une photo Wikimedia Commons (crédits automatiques).
- 5 portraits de personnages inventés (Antoine, Rose, Jeanne, Hugo, Inès).
- 5 vidéos de transition (image vers vidéo, 8 s, mouvements lents).
- Œuvres réelles possibles (Wikimedia Commons, domaine public) : le tableau du Sacre de David (Louvre), l'Arc de triomphe, la colonne Vendôme. Ne jamais générer ces œuvres par IA.
- Frise, carte de l'Europe, schéma du tableau du Sacre, plan de Paris et place de la commune : dessinés en SVG par script (`tests/donnees/schemas.py`) ; ne jamais les remplacer par des images IA.
