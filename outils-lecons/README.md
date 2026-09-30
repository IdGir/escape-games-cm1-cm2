# Outils — leçons imprimables A4

Ce dossier fabrique les pages **`<jeu>/lecons-imprimables.html`** : les leçons de chaque escape
game, une page A4 par leçon, en CM1 ou en CM2, avec cartes, schémas, graphiques et photos.
Il ne sert qu'à l'enseignant qui veut **modifier** une leçon imprimée : pour imprimer, il suffit
d'ouvrir le jeu (⚙️ Réglages → 📖 Leçons à imprimer).

## Comment c'est fait

| Fichier | Rôle |
|---|---|
| `modele/lecons-imprimables.html`, `modele/lecons-a4.js`, `modele/lecons-a4.css` | La page commune à tous les jeux (copiée dans chaque jeu par `construire.py`). Elle lit `assets/data/lecons.json` (le texte des leçons, déjà utilisé dans le jeu) et `assets/data/lecons-a4.json` (les compléments pour l'impression), met en page et ajuste la taille du texte pour que chaque leçon tienne sur sa page. |
| `jeux/<jeu>.py` | La configuration d'un jeu : en-tête et couleurs, **compétence du programme** de chaque leçon, liste des visuels (cartes, schémas, graphiques, photos). Pour la Constitution, les cinq leçons rédigées pour l'impression sont ici (`LECONS_BASE`). |
| `graphiques.py` | Graphiques et schémas SVG : barres, courbes, diagramme climatique, calendrier circulaire, étapes, tableaux. |
| `carte.mjs` | Cartes SVG dessinées à partir de données géographiques réelles (projection conique conforme pour la France, Robinson pour le monde). |
| `construire.py` | Génère `<jeu>/assets/data/lecons-a4.json` et recopie la page commune dans le jeu. Les crédits des photos sont lus dans `<jeu>/assets/medias/CREDITS-medias.md`. |
| `brancher_boutons.py` | Ajoute le bloc « 📖 Leçons à imprimer » dans ⚙️ Réglages et un bouton dans `prof.html` (déjà fait ; sans effet s'il est relancé). |
| `verifier.py` | Contrôle automatique : une page par leçon, aucune page qui déborde, compétence et visuels présents, images affichées, boutons du volet enseignant. |

Ne modifiez pas `lecons-a4.json` à la main : éditez `jeux/<jeu>.py`, puis relancez la construction.
Le texte des leçons, lui, se modifie dans `<jeu>/assets/data/lecons.json` (il change alors aussi
dans le jeu) ; il n'y a rien à reconstruire.

## Régénérer après une modification

Outil : **Invite de commandes Windows** (touches Windows + R, taper `cmd`, Entrée), avec
**Python** et **Node.js** installés.

1. Aller dans le dépôt :
   ```
   E:
   cd "\IDRISS\PROJET ESCAPE GAMES\outils-lecons"
   ```
2. La première fois seulement, installer les bibliothèques de cartes et télécharger les données
   (environ 20 Mo, dans `outils-lecons/geo-donnees/`, qui n'est pas publié) :
   ```
   npm install
   mkdir geo-donnees
   curl -L -o geo-donnees/ne_10m_rivers_lake_centerlines.geojson https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_rivers_lake_centerlines.geojson
   curl -L -o geo-donnees/ne_10m_geography_regions_polys.geojson https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_geography_regions_polys.geojson
   curl -L -o geo-donnees/ne_50m_admin_0_countries.geojson https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_admin_0_countries.geojson
   curl -L -o geo-donnees/fr-regions-version-simplifiee.geojson https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/regions-version-simplifiee.geojson
   ```
3. Reconstruire un jeu (ou `tous`) :
   ```
   cd ..
   python outils-lecons\construire.py chateau-fort
   ```
4. Vérifier : lancer `lancer.bat`, puis ouvrir http://127.0.0.1:8000/chateau-fort/lecons-imprimables.html.
   Contrôle automatique complet (facultatif, nécessite `pip install playwright`) : serveur sur le
   port 8765 (`python -m http.server 8765`), puis `python outils-lecons\verifier.py`.

## Sources des visuels

- Fonds de carte, fleuves, massifs, pays et groupes de revenu : **Natural Earth** (domaine public).
- Contours des régions françaises : **france-geojson** (données IGN, Licence ouverte).
- Normales climatiques de Dijon-Longvic (station météo) : Météo-France, 1991-2020.
- Photos : celles du jeu (Wikimedia Commons, Gallica, Pixabay), crédit sous chaque photo.
- Les tracés historiques (royaumes vers 511, empire en 814) sont **simplifiés et approximatifs** :
  c'est indiqué sous chaque carte.
