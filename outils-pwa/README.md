# outils-pwa — application installable, hors connexion (A4)

Les jeux s'installent comme une application sur une tablette, un Chromebook ou un PC, et
fonctionnent **sans internet et sans lancer `serveur.py`**.

| Fichier | Rôle |
|---|---|
| `../manifest.webmanifest` | nom, icônes, couleurs de l'application |
| `../sw.js` | service worker : garde les fichiers et répond hors connexion |
| `../sw-fichiers.js` | **généré** : liste des fichiers gardés et numéro de version |
| `../commun/js/pwa.js` | enregistre le service worker (accueil et chaque jeu) |
| `maj-hors-ligne.py` | régénère `sw-fichiers.js` |
| `icones.py` | redessine les icônes `commun/icones/*.png` (Pillow) |

## Sans serveur ni internet : une archive zip par jeu (N9)

`archives-hors-ligne.py` fabrique `archives-hors-ligne/<jeu>-hors-ligne.zip` (tous les jeux, ou ceux nommés) :
le jeu, le tronc commun, `JOUER.html` (double-clic) et `LISEZ-MOI.txt`. Ouverte d'un double-clic, une page
ne peut pas lire de fichier `.json` : les données (`assets/data/*.json`, `medias.json`) sont donc embarquées
dans `<jeu>/js/donnees-embarquees.js`, chargé en premier par `index.html` et `lecons-imprimables.html` dans
l'archive. Seuls les fichiers suivis par git sont copiés ; le dépôt n'est pas modifié. Publication
automatique dans la release « hors-ligne » : `.github/workflows/archives-hors-ligne.yml`.
Test : `node commun/tests/test-archives.js`.

## Sur la tablette (une seule fois, avec internet)

1. Ouvrir **https://idgir.github.io/escape-games-cm1-cm2/** dans Chrome ou Edge.
2. Attendre « ✅ Prêt hors connexion » dans le bloc **📲 Sur tablette, sans internet** de l'accueil.
3. (Facultatif) **📥 Garder aussi les images de tous les jeux** (environ 75 Mo).
4. **📲 Installer l'application** (ou menu ⋮ → « Installer l'application » / « Ajouter à l'écran d'accueil »).

Hors connexion, les **vidéos** ne sont pas disponibles (trop lourdes) : chaque jeu affiche alors l'image
ou le décor dessiné, comme lorsqu'une vidéo manque. Le tableau de bord en direct et l'écran de classement
restent réservés au mode local (`lancer.bat`).

## Après une modification du dépôt (avant de publier)

**Outil : l'Invite de commandes** (touche Windows + R, `cmd`, Entrée), Python installé :

```
E:
cd "\IDRISS\PROJET ESCAPE GAMES"
python outils-pwa\maj-hors-ligne.py
git add sw-fichiers.js
```

Le numéro de version change dès qu'un fichier change : les appareils installés téléchargent la nouvelle
version à la prochaine connexion. Le test `node commun/tests/test-hors-ligne.js` signale un oubli.
