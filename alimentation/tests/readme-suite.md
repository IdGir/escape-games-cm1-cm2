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
  le retapent dans le **coffre final** (10 points du premier coup, 3 après une erreur ; accents et majuscules ignorés).
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

**Mentions** : 90 % → Grand chef de cuisine · 75 % → Second de cuisine · 55 % → Commis confirmé · en dessous → Apprenti commis.  
**Badges** : Équipe rapide (une salle en moins de 6 min) · Maître des menus (salle 2 sans indice) · Explorateur du Grand Tunnel
(salle 4 sans indice) · Commis de confiance (3 indices au maximum sur la partie).

---

## Les leçons (bouton « Leçons »)

Cinq leçons rédigées, une par salle, de 3 à 4 minutes de lecture, avec un texte CM1 et un texte CM2, des objectifs, un
lexique, un schéma, un document et leurs sources en pied de leçon. Chaque énigme ouvre sa leçon par le bouton
« Leçon » (champ `lecon` de `enigmes.json`). L'enseignant peut interdire la consultation (⚙️ Réglages → Séance).
Les mêmes leçons existent en **version A4 imprimable** (`lecons-imprimables.html`, bouton « 📖 Leçons à imprimer » dans ⚙️ Réglages).

| Salle | Leçon (`id`) | Schéma |
|---|---|---|
| 1 | Grandir, c'est fabriquer de la matière (`croissance`) | courbe de masse de Caramel et toise de Lou (relevés fictifs) |
| 2 | Des besoins qui changent (`besoins`) | barres des besoins en énergie (ordres de grandeur) |
| 3 | Dans la bouche : mâcher (`mastication`) | mâchoire du bas, vue de dessus, légendée |
| 4 | Le trajet des aliments (`digestion`) | appareil digestif vu de face, légendé |
| 5 | Le sang livre les nutriments (`circulation`) | intestin → cœur → muscles ; pouls de Lou (leçon A4) |

Les schémas anatomiques (mâchoire, appareil digestif) sont **dessinés en SVG** pour le jeu (simplifiés, sans échelle),
jamais générés par IA.

---

## Modifier le contenu

| Pour changer… | Fichier |
|---|---|
| les énigmes : questions, réponses, indices, corrections | `assets/data/enigmes.json` |
| les dialogues, les lieux, les mots-clés | `assets/data/dialogues.json` |
| les leçons | `assets/data/lecons.json` |
| les évaluations imprimables et le quizz final | `assets/data/evaluations.json` |
| les leçons A4 imprimables | `outils-lecons/jeux/alimentation.py`, puis `python outils-lecons/construire.py alimentation` |
| les décors dessinés | `js/decors.js` |
| les personnages dessinés | `js/personnages.js` |

**Aucune énigme n'est écrite en dur** : le moteur est celui du tronc commun (`commun/js/enigmes.js`, partagé par tous les
jeux) ; aucun type d'énigme n'a été ajouté. Le jeu a été construit à partir du squelette de `renaissance/` (déjà
aligné sur le tronc commun et les greffons). Le contenu (énigmes, leçons) vient du pack rédigé
`prompts-opus/alimentation-pack/`, converti au format de `renaissance/assets/data/`. On peut éditer les énigmes sans coder avec [editeur.html](../editeur.html).
Après une modification d'un fichier `js/` ou `css/`, augmentez son numéro de version dans `index.html` (`app.js?m2` → `app.js?m3`).
Ce README est régénéré à partir des données par `python alimentation/tests/generer-readme.py`.

```
alimentation/
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
python alimentation/tests/test_json.py
node alimentation/tests/test-jeu.js
node alimentation/tests/test-verifier.js
```

`test_json.py` contrôle les données (JSON valides, clés uniques, liens énigme → leçon, règles du cahier des charges, absence d'emoji).
`test-jeu.js` joue les parties complètes CM1 et CM2 (scores 185 et 235), teste les mauvaises réponses, les indices, les leçons,
le mode vérification, les réglages, les impressions et le tableau de bord. `node outils-tests/tous.js` lance les tests de tous les jeux.

---

## Sources

- Programme de sciences et technologie, cycles 2 et 3 : arrêté du 5 juin 2026, [BO n° 24 du 11 juin 2026](https://www.education.gouv.fr/bo/2026/Hebdo24/MENE2611650A) — thème « Le corps humain et la santé », Alimentation humaine : besoins alimentaires et nutrition humaine ; [Eduscol, cycle 3](https://eduscol.education.gouv.fr/4356/enseigner-au-cycle-3).
- Progression de l'enseignant : `programmation histoire-géo sciences 2026.pdf` (racine du dépôt), année A, période 2.
- Santé publique France : [mangerbouger.fr](https://www.mangerbouger.fr/) (repères de consommation, activité physique ; aucun aliment interdit).
- La Revue du praticien : [« Besoins énergétiques moyens de l'enfant et de l'adolescent »](https://www.larevuedupraticien.fr/outil/besoins-energetiques-moyens-de-lenfant-et-de-ladolescent) (vers 10 ans : environ 2 000 à 2 100 kcal par jour).
- Vikidia : [« Dent »](https://fr.vikidia.org/wiki/Dent) (20 dents de lait ; 32 dents chez l'adulte avec les dents de sagesse ; rôle des incisives, canines, prémolaires, molaires) ; [« Intestin grêle »](https://fr.vikidia.org/wiki/Intestin_gr%C3%AAle) (longueur moyenne : 6 m).
- Wikipédia : [« Fréquence cardiaque »](https://fr.wikipedia.org/wiki/Fr%C3%A9quence_cardiaque) (6-12 ans : 95 ± 30 battements par minute au repos ; maximum théorique 220 − âge).
- La main à la pâte : ressources « Alimentation » et « Le corps humain » ([fondation-lamap.org](https://fondation-lamap.org/)).
- Données inventées pour le jeu, signalées comme telles à l'écran : le poussin Caramel (40 → 450 g en 4 semaines, 700 g de nourriture), la toise de Lou (115 → 137 cm), le pouls de Lou (88 et 160 battements par minute). Les besoins de Basile (environ 2 800 et 6 000 kcal) sont des ordres de grandeur couramment cités, sans source officielle (voir [A-VERIFIER.md](A-VERIFIER.md)).
