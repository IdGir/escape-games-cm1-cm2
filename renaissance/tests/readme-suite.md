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

**Mentions** : 90 % → Maître de la Renaissance · 75 % → Compagnon de l'atelier · 55 % → Apprenti de Léonard · en dessous → Jeune curieux.  
**Badges** : Équipe rapide (une salle en moins de 6 min) · Ami du mécène (salle 2 sans indice) · Lecteur de plans
(salle 4 sans indice) · Apprenti de Léonard (3 indices au maximum sur la partie).

---

## Les leçons (bouton « Leçons »)

Cinq leçons rédigées, une par salle, de 3 à 4 minutes de lecture, avec un texte CM1 et un texte CM2, des objectifs, un
lexique, un schéma ou une frise, un document et leurs sources en pied de leçon. Chaque énigme ouvre sa leçon par le bouton
« Leçon » (champ `lecon` de `enigmes.json`). L'enseignant peut interdire la consultation (⚙️ Réglages → Séance).
Les mêmes leçons existent en **version A4 imprimable** (`lecons-imprimables.html`, bouton « 📖 Leçons à imprimer » dans ⚙️ Réglages).

| Salle | Leçon (`id`) | Schéma ou frise |
|---|---|---|
| 1 | La Renaissance et l'humanisme (`renaissance-humanisme`) | frise de l'Antiquité à 1516 |
| 2 | François Ier, roi mécène (`francois-mecene`) | schéma « les arts / les lettres » |
| 3 | Léonard de Vinci, l'artiste invité (`leonard-de-vinci`) | frise de la vie de Léonard |
| 4 | Les châteaux de la Renaissance (`chateaux-renaissance`) | schéma château fort / château Renaissance |
| 5 | L'art de la Renaissance (`art-renaissance`) | schéma de la perspective |

---

## Modifier le contenu

| Pour changer… | Fichier |
|---|---|
| les énigmes : questions, réponses, indices, corrections | `assets/data/enigmes.json` |
| les dialogues, les lieux, les mots-clés | `assets/data/dialogues.json` |
| les leçons | `assets/data/lecons.json` |
| les évaluations imprimables et le quizz final | `assets/data/evaluations.json` |
| les leçons A4 imprimables | `outils-lecons/jeux/renaissance.py`, puis `python outils-lecons/construire.py renaissance` |
| les décors dessinés | `js/decors.js` |
| les personnages dessinés | `js/personnages.js` |

**Aucune énigme n'est écrite en dur** : le moteur est celui du tronc commun (`commun/js/enigmes.js`, partagé par tous les
jeux) ; aucun type d'énigme n'a été ajouté. Le jeu a été construit à partir du squelette de `versailles/` (déjà
aligné sur le tronc commun). On peut éditer les énigmes sans coder avec [editeur.html](../editeur.html).
Après une modification d'un fichier `js/` ou `css/`, augmentez son numéro de version dans `index.html` (`app.js?m2` → `app.js?m3`).
Ce README est régénéré à partir des données par `python renaissance/tests/generer-readme.py`.

```
renaissance/
├── index.html · prof.html · lecons-imprimables.html
├── README.md · GUIDE-PEDAGOGIQUE.md · A-VERIFIER.md · CHANGELOG.md
├── assets/
│   ├── data/      enigmes.json, dialogues.json, lecons.json, evaluations.json, lecons-a4.json
│   ├── videos/    décors et cinématiques (+ personnages/) — facultatif
│   └── images/    decors/, personnages/, cartes/, documents/ — facultatif
├── css/           style, enigmes, impression (les autres styles viennent de commun/)
├── js/            jeu, app, reglages, decors, personnages, lecons (le moteur vient de commun/)
└── tests/         test-jeu.js (Node + jsdom), test_json.py, generer-readme.py
```

---

## Tests automatiques

Depuis la racine du dépôt (Invite de commandes, voir `outils-tests/README.md` pour installer jsdom une fois) :

```
python renaissance/tests/test_json.py
node renaissance/tests/test-jeu.js
```

`test_json.py` contrôle les données (JSON valides, clés uniques, liens énigme → leçon, règles du cahier des charges, absence d'emoji).
`test-jeu.js` joue les parties complètes CM1 et CM2 (scores 185 et 235), teste les mauvaises réponses, les indices, les leçons,
le mode vérification, les réglages, les impressions et le tableau de bord. `node outils-tests/tous.js` lance les tests de tous les jeux.

---

## Sources

- Programme d'histoire-géographie du cycle 3 : arrêté du 22 avril 2026, [BO n° 22 du 28 mai 2026](https://www.education.gouv.fr/bo/2026/Hebdo22/MENE2608631A) ; [Eduscol, cycle 3](https://eduscol.education.gouv.fr/4356/enseigner-au-cycle-3).
- Progression de l'enseignant : `programmation histoire-géo sciences 2026.pdf` (racine du dépôt), année B, période 2.
- Château royal d'Amboise : [notice de visite 2026](https://www.chateau-amboise.com/wp-content/uploads/2025/12/notice-2026-FR_compressed.pdf) (Léonard arrive en 1516 à 64 ans, manoir du Cloux, titre de « premier peintre, ingénieur et architecte du roi », mort le 2 mai 1519, chapelle Saint-Hubert ; enfance de François Ier à Amboise ; retour d'Italie de Charles VIII en 1496 ; fêtes de 1518).
- Château du Clos Lucé : [vinci-closluce.com](https://www.vinci-closluce.com/) (le manoir du Cloux, les maquettes construites d'après les dessins de Léonard).
- Académie de Nice, fiche EAC [« Le château de Chambord »](https://www.pedagogie.ac-nice.fr/dsden06/eac/wp-content/uploads/sites/5/2018/04/Le-chateau-de-Chambord.pdf) (chantier commencé en 1519, plus de 400 pièces, environ 80 escaliers et 300 cheminées, escalier à double révolution, salamandre) ; [Vikidia, « Château de Chambord »](https://fr.vikidia.org/wiki/Ch%C3%A2teau_de_Chambord) (rôle « probable » de Léonard).
- Collège de France : [« Cinq siècles d'histoire »](https://www.college-de-france.fr/fr/institution-et-son-histoire/5-siecles-histoire) (lecteurs royaux, 1530, Guillaume Budé, hébreu, grec, mathématiques).
- Vikidia : [« François Ier de France »](https://fr.vikidia.org/wiki/Fran%C3%A7ois_Ier_de_France) (12 septembre 1494, roi le 1er janvier 1515, Marignan, dépôt légal 1537) ; [« Ordonnance de Villers-Cotterêts »](https://fr.vikidia.org/wiki/Ordonnance_de_Villers-Cotter%C3%AAts) (août 1539) ; [« Homme de Vitruve »](https://fr.vikidia.org/wiki/Homme_de_Vitruve) (vers 1490, Venise).
- Encyclopædia Universalis : [« La Joconde »](https://www.universalis.fr/encyclopedie/la-joconde-portrait-de-mona-lisa/) (Lisa Gherardini, huile sur peuplier, 77 × 53 cm, sfumato, entrée dans la collection de François Ier) ; Musée du Louvre.
- Encyclopédie Larousse : « Renaissance », « humanisme », « Gutenberg », « perspective », « Léonard de Vinci ».
- Lumni (dossiers « François Ier », « Léonard de Vinci », « la Renaissance ») : [lumni.fr](https://www.lumni.fr/).
