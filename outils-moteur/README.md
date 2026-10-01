# outils-moteur — moteur d'énigmes v2 (octobre 2026)

Règles communes aux 9 escape games : 10 points juste du premier coup, 3 après une erreur ; en cas
d'erreur, seulement le **nombre** de réponses justes ; aucun texte après la réussite ; le mot de fin
de salle affiché une seule fois, noté sur la **fiche de mission** et retapé dans le **coffre final** ;
lettres cachées mélangées avec des leurres. Le personnage se tait dès que les élèves touchent l'énigme.

## Fichiers maîtres

| Fichier | Rôle | Installé dans |
|---|---|---|
| `enigmes.js` | moteur des 10 types d'énigmes (validation par bouton, retours chiffrés) | `<jeu>/js/enigmes.js` (6 jeux à moteur commun) |
| `enigmes-v2.css` | styles du barème, des paires numérotées, des cases de lettres, du coffre | fin de `<jeu>/css/enigmes.css` |
| `fiche-mission.js` | fiche de mission A4 (⚙️ Réglages → Impression) | `<jeu>/js/fiche-mission.js` (8 jeux) |
| `v2-ancien.js` | aides v2 pour les jeux à moteur propre (anagramme, association, coffre…) | `declaration/js/v2.js`, `tour-du-monde/js/v2.js` |
| `theme-tour-du-monde.css` | charte « carnet de voyage » du Tour du monde | fin de `tour-du-monde/css/style.css` |

Mission géographique a son propre moteur (`mission-geo/js/activites.js`), adapté directement.

## Installer / réinstaller (idempotent)

Ouvrir l'**Invite de commandes** (touche Windows + R, taper `cmd`, Entrée), puis :

```
E:
cd "\IDRISS\PROJET ESCAPE GAMES"
python outils-moteur\installer.py
python outils-moteur\installer_anciens.py
python outils-moteur\lettres_v2.py
python outils-moteur\maj_docs.py
```

- `installer.py` : copie le moteur dans les 6 jeux, patche `app.js` (barème, coffre final, mot à noter,
  fin des dialogues de réussite, compteurs), branche la fiche de mission et les numéros de version.
- `installer_anciens.py` : fichiers communs de Déclaration et Tour du monde (et leurs feuilles de style).
- `lettres_v2.py` : réécrit les énigmes « lettres » (abbaye 2-4 modifiée à la main : format compact).
- `maj_docs.py` : met à jour README et guides.

## Tester

**Tests rapides, sans navigateur (recommandé)** : `node outils-tests/tous.js` — les 9 jeux, voir
[outils-tests/README.md](../outils-tests/README.md).

**Tests dans un vrai navigateur (Playwright)**, plus lents :

Dans une première invite de commandes, à la racine du dépôt : `python -m http.server 8765`.
Dans une seconde (Playwright requis : `pip install playwright` puis `python -m playwright install chromium`) :

```
python outils-moteur\tester_parties.py                 (6 jeux, CM1 et CM2, ~10 min)
python outils-moteur\tester_parties.py --toutes-fausses (chaque énigme d'abord fausse)
python outils-moteur\tester_declaration.py
python outils-moteur\tester_tour_du_monde.py
python outils-moteur\tester_mission_geo.py             (16 séances + fiche de mission)
```

Chaque script affiche « 0 échec(s) » quand tout va bien.
