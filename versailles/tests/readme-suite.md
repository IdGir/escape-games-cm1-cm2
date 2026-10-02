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

**Mentions** : 90 % → Grand secrétaire du roi · 75 % → Secrétaire du cabinet · 55 % → Clerc des archives · en dessous → Apprenti secrétaire.  
**Badges** : Équipe rapide (une salle en moins de 6 min) · Esprit de tolérance (salle 2 sans indice) · Maître de l'étiquette
(salle 4 sans indice) · Secrétaire du roi (3 indices au maximum sur la partie).

---

## Les leçons (bouton « Leçons »)

Cinq leçons rédigées, une par salle, de 3 à 4 minutes de lecture, avec un texte CM1 et un texte CM2, des objectifs, un
lexique, un schéma ou une frise, un document et leurs sources en pied de leçon. Chaque énigme ouvre sa leçon par le bouton
« Leçon » (champ `lecon` de `enigmes.json`). L'enseignant peut interdire la consultation (⚙️ Réglages → Séance).
Les mêmes leçons existent en **version A4 imprimable** (`lecons-imprimables.html`, bouton « 📖 Leçons à imprimer » dans ⚙️ Réglages).

| Salle | Leçon (`id`) | Schéma ou frise |
|---|---|---|
| 1 | La Réforme et les guerres de Religion (`reforme-guerres`) | frise 1517-1598 |
| 2 | L'édit de Nantes (`edit-de-nantes`) | schéma « permis / limité » |
| 3 | Versailles, le château du Roi-Soleil (`chateau-versailles`) | schéma du domaine |
| 4 | Une journée du roi à Versailles (`journee-du-roi`) | frise de la journée |
| 5 | La monarchie absolue (`monarchie-absolue`) | schéma + frise des trois règnes |

---

## Modifier le contenu

| Pour changer… | Fichier |
|---|---|
| les énigmes : questions, réponses, indices, corrections | `assets/data/enigmes.json` |
| les dialogues, les lieux, les mots-clés | `assets/data/dialogues.json` |
| les leçons | `assets/data/lecons.json` |
| les évaluations imprimables et le quizz final | `assets/data/evaluations.json` |
| les leçons A4 imprimables | `outils-lecons/jeux/versailles.py`, puis `python outils-lecons/construire.py versailles` |
| les décors dessinés | `js/decors.js` |
| les personnages dessinés | `js/personnages.js` |

**Aucune énigme n'est écrite en dur** : le moteur est celui du tronc commun (`commun/js/enigmes.js`, partagé par tous les
jeux) ; aucun type d'énigme n'a été ajouté. Le jeu a été construit à partir du squelette de `chateau-fort/` (déjà
aligné sur `constitution/` et le tronc commun). On peut éditer les énigmes sans coder avec [editeur.html](../editeur.html).
Après une modification d'un fichier `js/` ou `css/`, augmentez son numéro de version dans `index.html` (`app.js?m2` → `app.js?m3`).
Ce README est régénéré à partir des données par `python versailles/tests/generer-readme.py`.

```
versailles/
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
python versailles/tests/test_json.py
node versailles/tests/test-jeu.js
```

`test_json.py` contrôle les données (JSON valides, clés uniques, liens énigme → leçon, règles du cahier des charges, absence d'emoji).
`test-jeu.js` joue les parties complètes CM1 et CM2 (scores 185 et 235), teste les mauvaises réponses, les indices, les leçons,
le mode vérification, les réglages, les impressions et le tableau de bord. `node outils-tests/tous.js` lance les tests de tous les jeux.

---

## Sources

- Programme d'histoire-géographie du cycle 3 : arrêté du 22 avril 2026, [BO n° 22 du 28 mai 2026](https://www.education.gouv.fr/bo/2026/Hebdo22/MENE2608631A) ; [Eduscol, cycle 3](https://eduscol.education.gouv.fr/4356/enseigner-au-cycle-3).
- Progression de l'enseignant : `programmation histoire-géo sciences 2026.pdf` (racine du dépôt), année A, période 2.
- Château de Versailles, ressources pédagogiques : [« La journée du roi », par Mathieu da Vinha](https://www.chateauversailles.fr/ressources-pedagogiques/rois-reines-versailles/louis-xiv/journee-roi-mathieu-da-vinha-directeur) (horaires, citation de Saint-Simon) ; [« La journée du roi Louis XIV »](https://www.chateauversailles.fr/ressources-pedagogiques/rois-reines-versailles/louis-xiv/journee-roi-louis-xiv).
- Château de Versailles : [« La galerie des Glaces »](https://www.chateauversailles.fr/decouvrir/domaine/chateau/galerie-glaces) (73 m, 357 miroirs, 17 arcades, 1678-1684, Hardouin-Mansart, Le Brun, 30 compositions) ; [« Louis XIV »](https://www.chateauversailles.fr/decouvrir/histoire/grands-personnages/louis-xiv) (installation le 6 mai 1682, emblème du Soleil, Apollon, Le Vau, Le Nôtre, Colbert) ; [« Les tables royales »](https://en.chateauversailles.fr/discover/history/key-dates/royal-tables) (grand et petit couvert).
- Musée protestant : [« L'édit de Nantes (1598) »](https://museeprotestant.org/notice/ledit-de-nantes-1598/) ; [« Martin Luther (1483-1546) »](https://museeprotestant.org/notice/martin-luther-1483-1546/).
- Archives nationales : l'édit de Nantes (un original est conservé aux Archives nationales).
- Encyclopédie Larousse : [« révocation de l'édit de Nantes »](https://www.larousse.fr/encyclopedie/divers/r%C3%A9vocation_de_l%C3%A9dit_de_Nantes/186072) (18 octobre 1685, Fontainebleau ; 200 000 à 300 000 exilés ; pays d'accueil).
- Wikipédia : [« Guerres de Religion (France) »](https://fr.wikipedia.org/wiki/Guerres_de_Religion_(France)) (1562-1598, huit guerres, Wassy, Saint-Barthélemy) ; [« Henri IV (roi de France) »](https://fr.wikipedia.org/wiki/Henri_IV_(roi_de_France)) (abjuration du 25 juillet 1593 ; « Paris vaut bien une messe » attribué à tort).
- Vikidia : [« Louis XIV »](https://fr.vikidia.org/wiki/Louis_XIV) (fin du règne, hiver 1709) ; [« Galerie des Glaces »](https://fr.vikidia.org/wiki/Galerie_des_Glaces).
- Lumni (vidéos et dossiers « Henri IV », « Louis XIV », « Versailles ») : [lumni.fr](https://www.lumni.fr/) ; L'Histoire par l'image : [histoire-image.org](https://histoire-image.org/).
