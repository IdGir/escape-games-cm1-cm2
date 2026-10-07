## Images libres de droits

Pour trouver ou télécharger une image libre, utiliser le script `scripts/images.py` (Python, sans dépendance) :

- `python scripts/images.py commons "mot-clé" -n 5` : Wikimedia Commons
- `python scripts/images.py gallica "mot-clé" -n 5` : Gallica (BnF)
- `python scripts/images.py openverse "mot-clé" -n 5` : Openverse
- Ajouter `--download` pour enregistrer dans `images/` (crédits dans `images/credits.json`).

Règles : toujours afficher d'abord les résultats, vérifier la licence avant de télécharger, et citer auteur + licence + URL source à côté de chaque image utilisée (fiche, diaporama, jeu). Pour Gallica, vérifier les conditions de réutilisation du document.
