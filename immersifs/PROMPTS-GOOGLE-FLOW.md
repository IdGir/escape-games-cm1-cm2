# Prompts Google Flow : index des variantes immersives

Chaque variante a son fichier `PROMPTS-GOOGLE-FLOW.md` : 5 décors 16:9 (objets d'énigme placés aux zones du moteur, bas de l'image dégagé pour la plaque de dialogue) et un portrait 3:4 par personnage, avec la charte graphique du jeu. Les décors servent ensuite de points de départ aux vidéos produites par Agnes.

| Jeu | Titre | Prompts | Décors | Portraits |
|---|---|---|---|---|
| `alimentation` | Le Grand Repas du chef | [alimentation/PROMPTS-GOOGLE-FLOW.md](alimentation/PROMPTS-GOOGLE-FLOW.md) | 5 | 4 |
| `chateau-fort` | Le Secret du donjon | [chateau-fort/PROMPTS-GOOGLE-FLOW.md](chateau-fort/PROMPTS-GOOGLE-FLOW.md) | 5 | 5 |
| `constitution` | Le Sceau de la République | [constitution/PROMPTS-GOOGLE-FLOW.md](constitution/PROMPTS-GOOGLE-FLOW.md) | 5 | 4 |
| `lumiere` | Le Phare de l'île Lumière | [lumiere/PROMPTS-GOOGLE-FLOW.md](lumiere/PROMPTS-GOOGLE-FLOW.md) | 5 | 5 |
| `melanges` | Le Laboratoire de Madame Mélange | [melanges/PROMPTS-GOOGLE-FLOW.md](melanges/PROMPTS-GOOGLE-FLOW.md) | 5 | 5 |
| `moyen-age-abbaye` | Le Manuscrit de l'abbaye | [moyen-age-abbaye/PROMPTS-GOOGLE-FLOW.md](moyen-age-abbaye/PROMPTS-GOOGLE-FLOW.md) | 5 | 4 |
| `objets-techniques` | L'Atelier de l'inventeur | [objets-techniques/PROMPTS-GOOGLE-FLOW.md](objets-techniques/PROMPTS-GOOGLE-FLOW.md) | 5 | 4 |
| `renaissance` | L'Atelier de Léonard à Amboise | [renaissance/PROMPTS-GOOGLE-FLOW.md](renaissance/PROMPTS-GOOGLE-FLOW.md) | 5 | 5 |
| `station-meteo` | La Station météo disparue | [station-meteo/PROMPTS-GOOGLE-FLOW.md](station-meteo/PROMPTS-GOOGLE-FLOW.md) | 5 | 4 |
| `versailles` | De l'édit de Nantes à Versailles | [versailles/PROMPTS-GOOGLE-FLOW.md](versailles/PROMPTS-GOOGLE-FLOW.md) | 5 | 5 |

Ordre conseillé : produire d'abord les portraits (les valider), puis les décors, puis déposer les fichiers avec `importer-image.py` (`--decor`, `--portrait`, `--depart`), caler les zones avec `outils/caler-effets.html`, enfin lancer les vidéos Agnes (`produire.py --types video --depart-decor <décor>`).
