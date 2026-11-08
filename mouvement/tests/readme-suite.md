## Score

<!-- moteur-v2 -->
### Règles du moteur v2 (octobre 2026)

- **Tout juste du premier coup** : chaque énigme rapporte **10 points** si la première vérification est juste,
  **3 points seulement** après une erreur. Le barème est rappelé en tête de chaque énigme : les élèves ont
  intérêt à relire la leçon (bouton 📚) avant de valider.
- **Retour d'erreur** : le jeu dit seulement **combien** de réponses sont justes (« 2 associations justes sur 4 »),
  jamais lesquelles. Une réponse incomplète n'est pas comptée comme une erreur.
- **Aucun texte après la réussite** : ni correction, ni explication, ni dialogue de réussite. Le bouton suivant
  apparaît tout de suite ; le personnage se tait dès que les élèves touchent l'énigme (le chrono ne s'arrête jamais).
- **Mots à noter** : le mot gagné en fin de salle n'est affiché **qu'une fois** (« ✍️ Notez ce mot ») ; les élèves
  le recopient sur la **fiche de mission** (⚙️ Réglages › Impression › « ✍️ Fiche de mission », une par équipe), puis
  le retapent dans le **coffre final** — ici le coffre du Grand Prix (10 points du premier coup, 3 après une erreur ;
  accents et majuscules ignorés).
- **Lettres cachées** : les lettres marquées sont **dans le désordre**, avec des **leurres** ; on les range dans les cases.


| | CM1 | CM2 |
|---|---|---|
| Énigmes justes du premier coup (10 pts ; 3 pts après une erreur) | 15 × 10 = 150 | 20 × 10 = 200 |
| Coffre final ouvert du premier coup (10 pts ; 3 après une erreur) | 10 | 10 |
| Bonus de rapidité (3 pts par salle) | 15 | 15 |
| Quizz final (2 pts × 5) | 10 | 10 |
| **Total maximal** | **185** | **235** |

Un indice consulté retire **2 points**. Le bonus de rapidité tombe à 2 points si la salle a demandé un indice, et à 0
au-delà de 8 minutes (CM1) ou 10 minutes (CM2) par salle.

**Mentions** : 90 % → Commissaire en chef · 75 % → Commissaire confirmé · 55 % → Commissaire adjoint · en dessous → Commissaire débutant.  
**Badges** : Équipe rapide (une salle en moins de 6 min) · As du chronomètre (salle 2 sans indice) · Œil de l'astronome
(salle 4 sans indice) · Commissaire de confiance (3 indices au maximum sur la partie).

---

## Les leçons (bouton « Leçons »)

Cinq leçons rédigées, une par salle, de 3 à 4 minutes de lecture, avec un texte CM1 et un texte CM2, des objectifs, un
lexique, un schéma et leurs sources en pied de leçon. Chaque énigme ouvre sa leçon par le bouton
« Leçon » (champ `lecon` de `enigmes.json`). L'enseignant peut interdire la consultation (⚙️ Réglages → Séance).
Les mêmes leçons existent en **version A4 imprimable** (`lecons-imprimables.html`, bouton « 📖 Leçons à imprimer » dans ⚙️ Réglages).

| Salle | Leçon (`id`) | Schéma |
|---|---|---|
| 1 | Mesurer une distance (`distance`) | ruban gradué : départ à 4 m, arrivée à 16 m |
| 2 | Mesurer une durée (`duree`) | deux instants (10 h 15, 10 h 40) et la durée de 25 min |
| 3 | Comparer des déplacements (`comparer`) | même distance, trois durées (barres) |
| 4 | Trajectoires : droite, cercle ou courbe (`trajectoires`) | rectiligne, circulaire, curviligne |
| 5 | Tout dépend de l'observateur (`observateur`) | le même voyageur vu par son voisin et depuis le quai ; document : le carnet d'Hugo |

Tous les schémas (ruban gradué, reports du décamètre, circuit, Soleil et planètes, trajectoires, observateurs) sont **dessinés
en SVG** par script pour le jeu (simplifiés, sans échelle), jamais générés par IA.

---

## Modifier le contenu

| Pour changer… | Fichier |
|---|---|
| les énigmes, les leçons, les dialogues, les évaluations | `tests/donnees/gen_enigmes.py`, `gen_lecons.py`, `gen_dialogues_eval.py` (schémas : `schemas.py`), puis relancer les trois scripts avec le dossier `assets/data` en argument |
| ou directement les données | `assets/data/*.json` (attention : un nouveau lancement des scripts écrase les modifications faites à la main) |
| les leçons A4 imprimables | `outils-lecons/jeux/mouvement.py`, puis `python outils-lecons/construire.py mouvement` |
| les décors dessinés | `js/decors.js` |
| les personnages dessinés | `js/personnages.js` |

**Aucune énigme n'est écrite en dur** : le moteur est celui du tronc commun (`commun/js/enigmes.js`, partagé par tous les
jeux) ; aucun type d'énigme n'a été ajouté. Le jeu a été construit à partir du squelette de `etats-matiere/`.
On peut éditer les énigmes sans coder avec [editeur.html](../editeur.html).
Après une modification d'un fichier `js/` ou `css/`, augmentez son numéro de version dans `index.html` (`app.js?m2` → `app.js?m3`).
Ce README est régénéré à partir des données par `python mouvement/tests/generer-readme.py`.

```
mouvement/
├── index.html · prof.html · lecons-imprimables.html
├── README.md · GUIDE-PEDAGOGIQUE.md · A-VERIFIER.md · CHANGELOG.md
├── assets/
│   ├── data/      enigmes.json, dialogues.json, lecons.json, evaluations.json, lecons-a4.json
│   ├── videos/    décors et cinématiques (+ personnages/) — facultatif
│   └── images/    decors/, personnages/, cartes/, documents/ — facultatif
├── css/           style, enigmes, impression (les autres styles viennent de commun/)
├── js/            jeu, app, reglages, decors, personnages, lecons (le moteur vient de commun/)
└── tests/         test-jeu.js, test-verifier.js (Node + jsdom), test_json.py, generer-readme.py, donnees/ (scripts des données)
```

---

## Tests automatiques

Depuis la racine du dépôt (Invite de commandes, voir `outils-tests/README.md` pour installer jsdom une fois) :

```
python mouvement/tests/test_json.py
node mouvement/tests/test-jeu.js
node mouvement/tests/test-verifier.js
```

`test_json.py` contrôle les données (JSON valides, clés uniques, liens énigme → leçon, règles du cahier des charges, absence d'emoji).
`test-jeu.js` joue les parties complètes CM1 et CM2 (scores 185 et 235), teste les mauvaises réponses, les indices, les leçons,
le mode vérification, les réglages, les impressions et le tableau de bord. `node outils-tests/tous.js` lance les tests de tous les jeux.

---

## Sources

- Programme de sciences et technologie, cycles 2 et 3 : arrêté du 5 juin 2026, [BO n° 24 du 11 juin 2026](https://www.education.gouv.fr/bo/2026/Hebdo24/MENE2611650A) — [annexe 2, programme du cycle 3](https://www.education.gouv.fr/sites/default/files/document/annexe-2-programme-de-sciences-et-technologie-du-cycle-3-519023.pdf), « Différents types de mouvement » (CM1 : mesurer une distance, mesurer une durée comme intervalle entre deux instants ; CM2 : mouvement rectiligne ou circulaire en fonction de l'observateur, la Terre et le Soleil, conversions ; sixième : comparaison qualitative des vitesses, sans formule).
- Progression de l'enseignant : `programmation histoire-géo sciences 2026.pdf` (racine du dépôt), année B, période 2.
- Eduscol : [ressources d'accompagnement du programme de sciences et technologie au cycle 3](https://eduscol.education.gouv.fr/6878/ressources-d-accompagnement-du-programme-de-sciences-et-technologie-au-cycle-3) (« Matière, mouvement, énergie, information »).
- La main à la pâte : ressources « Mouvement » du cycle 3.
- Vikidia : [« Terre »](https://fr.vikidia.org/wiki/Terre) (troisième planète ; tour du Soleil en environ 365 jours et 6 heures) ; [« TGV »](https://fr.vikidia.org/wiki/TGV) (vitesse commerciale de 320 km/h) ; [« Vitesse des animaux »](https://fr.vikidia.org/wiki/Vitesse_des_animaux) (guépard : 115 km/h sur 300 m ; escargot : 0,05 km/h au plus).
- Fédération française de randonnée : [« À quelle vitesse marche un piéton en ville ? »](https://www.ffrandonnee.fr/s-informer/actualites/a-quelle-vitesse-marche-un-pieton-en-ville) (4 km/h utilisés par les aménageurs ; 2,6 km/h mesurés en ville).
- Club des villes et territoires cyclables : [« Comment ça roule ? »](https://villes-cyclables.org/mediacenter/uploads/comment-ca-roule.pdf) (vitesse moyenne des cyclistes : 15 km/h).
- Code de la route, article R413-3 : 50 km/h au plus en agglomération.
- Données inventées pour le jeu, signalées comme telles : le Grand Prix, le plateau et ses personnages ; toutes les distances, durées, horaires et classements des énigmes (dont le code 47925).
