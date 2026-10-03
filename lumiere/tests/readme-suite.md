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
  le retapent dans le **coffre final** — ici le tableau de commande du phare (10 points du premier coup, 3 après une erreur ;
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

**Mentions** : 90 % → Gardien du phare · 75 % → Gardien adjoint · 55 % → Apprenti gardien confirmé · en dessous → Apprenti gardien.  
**Badges** : Équipe rapide (une salle en moins de 6 min) · Maître des vitres (salle 2 sans indice) · Lecteur de cadran solaire
(salle 4 sans indice) · Gardien de confiance (3 indices au maximum sur la partie).

---

## Les leçons (bouton « Leçons »)

Cinq leçons rédigées, une par salle, de 3 à 4 minutes de lecture, avec un texte CM1 et un texte CM2, des objectifs, un
lexique, un schéma, un document et leurs sources en pied de leçon. Chaque énigme ouvre sa leçon par le bouton
« Leçon » (champ `lecon` de `enigmes.json`). L'enseignant peut interdire la consultation (⚙️ Réglages → Séance).
Les mêmes leçons existent en **version A4 imprimable** (`lecons-imprimables.html`, bouton « 📖 Leçons à imprimer » dans ⚙️ Réglages).

| Salle | Leçon (`id`) | Schéma |
|---|---|---|
| 1 | D'où vient la lumière ? Comment voyage-t-elle ? (`sources`) | trajet de la lumière : lampe du phare → voile → œil ; document : le code Morse |
| 2 | Transparent, translucide, opaque (`matieres`) | une lampe devant une vitre, un papier calque, une planche ; document : la lentille de Fresnel |
| 3 | Ombre propre, ombre portée (`ombres`) | lampe, balle et écran, avec les rayons qui frôlent la balle |
| 4 | L'ombre d'un bâton au fil de la journée (`soleil`) | trajet apparent du Soleil (est, sud, ouest) ; relevé d'Achille |
| 5 | Les phases de la Lune (`lune`) | les huit phases vues depuis la France ; la lunaison |

Tous les schémas (trajet de la lumière, ombres, cour vue de dessus, phases de la Lune) sont **dessinés en SVG** par script
pour le jeu (simplifiés, sans échelle), jamais générés par IA. Les dessins de la Lune sont ceux d'un observateur en France
(hémisphère nord : la partie éclairée grandit d'abord à droite).

---

## Modifier le contenu

| Pour changer… | Fichier |
|---|---|
| les énigmes : questions, réponses, indices, corrections | `assets/data/enigmes.json` |
| les dialogues, les lieux, les mots-clés | `assets/data/dialogues.json` |
| les leçons | `assets/data/lecons.json` |
| les évaluations imprimables et le quizz final | `assets/data/evaluations.json` |
| les leçons A4 imprimables | `outils-lecons/jeux/lumiere.py`, puis `python outils-lecons/construire.py lumiere` |
| les décors dessinés | `js/decors.js` |
| les personnages dessinés | `js/personnages.js` |

**Aucune énigme n'est écrite en dur** : le moteur est celui du tronc commun (`commun/js/enigmes.js`, partagé par tous les
jeux) ; aucun type d'énigme n'a été ajouté (le message Morse est une énigme `code` à champs texte). Le jeu a été construit
à partir du squelette d'`alimentation/` (lui-même issu de `renaissance/`, aligné sur le tronc commun et les greffons).
On peut éditer les énigmes sans coder avec [editeur.html](../editeur.html).
Après une modification d'un fichier `js/` ou `css/`, augmentez son numéro de version dans `index.html` (`app.js?m2` → `app.js?m3`).
Ce README est régénéré à partir des données par `python lumiere/tests/generer-readme.py`.

```
lumiere/
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
python lumiere/tests/test_json.py
node lumiere/tests/test-jeu.js
node lumiere/tests/test-verifier.js
```

`test_json.py` contrôle les données (JSON valides, clés uniques, liens énigme → leçon, règles du cahier des charges, absence d'emoji).
`test-jeu.js` joue les parties complètes CM1 et CM2 (scores 185 et 235), teste les mauvaises réponses, les indices, les leçons,
le mode vérification, les réglages, les impressions et le tableau de bord. `node outils-tests/tous.js` lance les tests de tous les jeux.

---

## Sources

- Programme de sciences et technologie, cycles 2 et 3 : arrêté du 5 juin 2026, [BO n° 24 du 11 juin 2026](https://www.education.gouv.fr/bo/2026/Hebdo24/MENE2611650A) — [annexe 2, programme du cycle 3](https://www.education.gouv.fr/sites/default/files/document/annexe-2-programme-de-sciences-et-technologie-du-cycle-3-519023.pdf), CM1, « La matière, les mouvements et les signaux », Signaux — Lumière ; [Eduscol, cycle 3](https://eduscol.education.gouv.fr/4356/enseigner-au-cycle-3).
- Progression de l'enseignant : `programmation histoire-géo sciences 2026.pdf` (racine du dépôt), année A, période 2.
- La main à la pâte : [« La lumière, cycle 3 », document de travail pour les maîtres (centre pilote de Nogent-sur-Oise)](https://sites.ac-nancy-metz.fr/ia57sciences/IMG/pdf/Lumiere_MAP_sequence_complete.pdf) (la lumière se déplace en ligne droite ; sources primaires et objets qui renvoient la lumière dans l'œil) ; [« Parcours 8 : Ombres et lumière, cycle III »](https://lamap-espe.univ-lorraine.fr/sites/espe.univ-lorraine.fr.lamap/files/ressources/map_parcours_8.pdf) (transparent, translucide, opaque ; ombre propre, ombre portée ; objet à mi-distance : ombre deux fois plus grande) ; [séquence « La Terre en mouvement »](https://fondation-lamap.org/sites/default/files/sequence_pdf/la-terre-en-mouvement.pdf) (ombre d'un bâton ; ombre la plus courte vers 14 h en été).
- Vikidia : [« Phases de la Lune »](https://fr.vikidia.org/wiki/Phase_lunaire) (lunaison : 29,53 jours ; pleine lune environ 15 jours après la nouvelle lune) ; [« Alphabet morse »](https://fr.vikidia.org/wiki/Alphabet_morse) (code international, SOS) ; [« Phare »](https://fr.vikidia.org/wiki/Phare) (rythme propre à chaque phare) ; [« Vitesse de la lumière »](https://fr.vikidia.org/wiki/Vitesse_de_la_lumi%C3%A8re) (environ 300 000 km/s).
- Ministère de la Transition écologique (DREAL) : [fiche « Les phares »](https://webissimo.developpement-durable.gouv.fr/IMG/pdf/6_1_les_phares_cle59531c.pdf) (lentille de Fresnel, 1823, essayée au phare de Cordouan ; Cordouan en service depuis 1611).
- Sécurité des yeux (Soleil) : consignes publiques pour l'éclipse du 12 août 2026, par exemple [gouvernement du Luxembourg](https://gouvernement.lu/fr/actualites/toutes_actualites/communiques/2026/08-aout/11-eclipse-solaire.html) (ne jamais regarder le Soleil sans protection adaptée ; les lunettes de soleil ne protègent pas).
- Données inventées pour le jeu, signalées comme telles : l'île Lumière et ses personnages ; le relevé d'ombres d'Achille (fin juin, bâton de 1 m : 118, 62, 47, 76 et 151 cm de 10 h à 18 h), calculé pour une journée de fin juin en France (voir [A-VERIFIER.md](A-VERIFIER.md)).
