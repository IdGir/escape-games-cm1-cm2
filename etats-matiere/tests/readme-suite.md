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
  le retapent dans le **coffre final** — ici le pupitre de la Fabrique (10 points du premier coup, 3 après une erreur ;
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

**Mentions** : 90 % → Ingénieur en chef · 75 % → Ingénieur confirmé · 55 % → Ingénieur stagiaire confirmé · en dessous → Ingénieur stagiaire.  
**Badges** : Équipe rapide (une salle en moins de 6 min) · Peseur d'air (salle 2 sans indice) · Maître de la balance
(salle 4 sans indice) · Ingénieur de confiance (3 indices au maximum sur la partie).

---

## Les leçons (bouton « Leçons »)

Cinq leçons rédigées, une par salle, de 3 à 4 minutes de lecture, avec un texte CM1 et un texte CM2, des objectifs, un
lexique, un schéma et leurs sources en pied de leçon. Chaque énigme ouvre sa leçon par le bouton
« Leçon » (champ `lecon` de `enigmes.json`). L'enseignant peut interdire la consultation (⚙️ Réglages → Séance).
Les mêmes leçons existent en **version A4 imprimable** (`lecons-imprimables.html`, bouton « 📖 Leçons à imprimer » dans ⚙️ Réglages).

| Salle | Leçon (`id`) | Schéma |
|---|---|---|
| 1 | Solide, liquide ou gaz : comment les reconnaître ? (`etats`) | trois récipients : glaçon, eau, gaz invisible |
| 2 | L'air est de la matière (`air`) | ballon de basket pesé avant et après 10 L d'air pompés (données inventées) |
| 3 | Les changements d'état de l'eau (`changements`) | solide, liquide, gaz et les quatre flèches de changement d'état |
| 4 | Ce qui change et ce qui se conserve (`conservation`) | glaçons pesés avant et après la fusion ; document : le carnet de Fatou |
| 5 | Les propriétés de la matière et le cycle de l'eau (`proprietes`) | le cycle de l'eau : évaporation, nuage, précipitations, ruissellement |

Tous les schémas (bouteille avant et après le congélateur, changements d'état, cycle de l'eau, balances) sont **dessinés
en SVG** par script pour le jeu (simplifiés, sans échelle), jamais générés par IA.

---

## Modifier le contenu

| Pour changer… | Fichier |
|---|---|
| les énigmes : questions, réponses, indices, corrections | `assets/data/enigmes.json` |
| les dialogues, les lieux, les mots-clés | `assets/data/dialogues.json` |
| les leçons | `assets/data/lecons.json` |
| les évaluations imprimables et le quizz final | `assets/data/evaluations.json` |
| les leçons A4 imprimables | `outils-lecons/jeux/etats_matiere.py`, puis `python outils-lecons/construire.py etats-matiere` |
| les décors dessinés | `js/decors.js` |
| les personnages dessinés | `js/personnages.js` |

**Aucune énigme n'est écrite en dur** : le moteur est celui du tronc commun (`commun/js/enigmes.js`, partagé par tous les
jeux) ; aucun type d'énigme n'a été ajouté (les thermomètres de la salle 3 utilisent le type `instrument`, déjà présent dans le
moteur commun). Le jeu a été construit à partir du squelette de `lumiere/` (aligné sur le tronc commun et les greffons).
On peut éditer les énigmes sans coder avec [editeur.html](../editeur.html).
Après une modification d'un fichier `js/` ou `css/`, augmentez son numéro de version dans `index.html` (`app.js?m2` → `app.js?m3`).
Ce README est régénéré à partir des données par `python etats-matiere/tests/generer-readme.py`.

```
etats-matiere/
├── index.html · prof.html · lecons-imprimables.html
├── README.md · GUIDE-PEDAGOGIQUE.md · A-VERIFIER.md · CHANGELOG.md
├── assets/
│   ├── data/      enigmes.json, dialogues.json, lecons.json, evaluations.json, lecons-a4.json
│   ├── videos/    décors et cinématiques (+ personnages/) — facultatif
│   └── images/    decors/, personnages/, cartes/, documents/ — facultatif
├── css/           style, enigmes, impression (les autres styles viennent de commun/)
├── js/            jeu, app, reglages, decors, personnages, lecons (le moteur vient de commun/)
└── tests/         test-jeu.js, test-verifier.js (Node + jsdom), test_json.py, generer-readme.py
```

---

## Tests automatiques

Depuis la racine du dépôt (Invite de commandes, voir `outils-tests/README.md` pour installer jsdom une fois) :

```
python etats-matiere/tests/test_json.py
node etats-matiere/tests/test-jeu.js
node etats-matiere/tests/test-verifier.js
```

`test_json.py` contrôle les données (JSON valides, clés uniques, liens énigme → leçon, règles du cahier des charges, absence d'emoji).
`test-jeu.js` joue les parties complètes CM1 et CM2 (scores 185 et 235), teste les mauvaises réponses, les indices, les leçons,
le mode vérification, les réglages, les impressions et le tableau de bord. `node outils-tests/tous.js` lance les tests de tous les jeux.

---

## Sources

- Programme de sciences et technologie, cycles 2 et 3 : arrêté du 5 juin 2026, [BO n° 24 du 11 juin 2026](https://www.education.gouv.fr/bo/2026/Hebdo24/MENE2611650A) — annexe 2, programme du cycle 3, « La matière, les mouvements et les signaux » (états physiques et changements d'état au CM2 ; masse et mélanges au CM1) ; [Eduscol, cycle 3](https://eduscol.education.gouv.fr/4356/enseigner-au-cycle-3). Libellés exacts à relire sur l'annexe (voir [A-VERIFIER.md](A-VERIFIER.md)).
- Progression de l'enseignant : `programmation histoire-géo sciences 2026.pdf` (racine du dépôt), année B, période 2.
- La main à la pâte : [« Les états de l'eau et les changements d'états »](https://fondation-lamap.org/sites/default/files/sequence_pdf/les-etats-de-l-eau-et-les-changements-d-etats.pdf) ; [« Les changements d'état » (centre pilote de Nogent-sur-Oise)](https://lamap-nogent.rep.ac-amiens.fr/wp-content/uploads/Les-changements-d%C3%A9tat_version_2015_V2.pdf) ; [« Est-ce que l'air est pesant ? », livret enseignant](https://fondation-lamap.org/sites/default/files/sequence_pdf/Est-ce-que-l-air-est-pesant-livret-enseignant.pdf).
- Académie de Grenoble : [fiche cycle 3 « Les états et la constitution de la matière »](https://sciences-26.web.ac-grenoble.fr/sites/default/files/media-fichiers/2019-04/fiche_cycle_3-matiere_mvt_energie_info-_les_etats_et_la_constitution_de_la_matiere.pdf) ; [fiche connaissance « L'air »](https://sciences-technologie-38.web.ac-grenoble.fr/sites/default/files/media-fichiers/2021-12/fiche%20connaissance%20air%20%28002%29.pdf) (un litre d'air a une masse d'environ 1,2 g).
- Vikidia : [« Glace »](https://fr.vikidia.org/wiki/Glace) (la glace occupe plus de volume que l'eau liquide et flotte) ; « Cycle de l'eau ».
- IRM, Institut royal météorologique de Belgique : [« Nuages : composition »](https://www.meteo.be/fr/infos/dico-meteo/nuages-composition) (un nuage est fait de gouttelettes d'eau ou de cristaux de glace) ; Météo-France (cycle de l'eau).
- Données inventées pour le jeu, signalées comme telles : la Fabrique des états et ses personnages ; les masses des expériences (ballon de basket de 600 g, glaçons de 25 g, bouteille de 500 g ou 1 500 g) ; le relevé de températures de Paolo (évaluations). Les calculs utilisent 1 L d'air ≈ 1,2 g et 1 000 mL d'eau → environ 1 090 mL de glace.
