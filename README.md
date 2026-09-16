# Correcteur Pédagogique — CM1 / CM2

Application d'**autocorrection guidée** des productions d'élèves : marquage clair des erreurs
(accord, conjugaison, homophone, orthographe, segmentation, ponctuation, majuscule, lexique),
renvoi aux fiches-leçons du classeur, banque de mots personnelle, dictées, tableau de bord enseignant.

- Lancer tout de suite (Windows) : double-cliquer sur `lancer.bat`
- Fabriquer l'exécutable : double-cliquer sur `build_exe.bat` (résultat dans `dist/`)
- Mode d'emploi complet : [NOTICE.md](NOTICE.md)

Pile technique : Python 3.11 · Flask (port 5173) · pywebview · SQLite · PyInstaller.
Pont avec *Notes & Suivi* : `integration_server.py` (port 4100).

---

## 🎲 Vous cherchez les escape games ?

Ils sont désormais dans la branche **[`escape-games`](https://github.com/IdGir/escape-games-cm1-cm2/tree/escape-games)**.

**Les liens pour jouer n'ont pas changé** : <https://idgir.github.io/escape-games-cm1-cm2/>

| Jeu | Jouer | Guide |
|---|---|---|
| Le Secret de la Déclaration | [en ligne](https://idgir.github.io/escape-games-cm1-cm2/declaration/) | [guide](https://github.com/IdGir/escape-games-cm1-cm2/tree/escape-games/declaration#readme) |
| Le Tour du Monde en 80 minutes | [en ligne](https://idgir.github.io/escape-games-cm1-cm2/tour-du-monde/) | [guide](https://github.com/IdGir/escape-games-cm1-cm2/tree/escape-games/tour-du-monde#readme) |
| Mission géographique — Année A | [en ligne](https://idgir.github.io/escape-games-cm1-cm2/mission-geo/) | [guide](https://github.com/IdGir/escape-games-cm1-cm2/tree/escape-games/mission-geo#readme) |
