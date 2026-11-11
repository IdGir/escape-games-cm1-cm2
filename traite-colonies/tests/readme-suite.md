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
  le retapent dans le **coffre final** — ici le coffre du registre (10 points du premier coup, 3 après une erreur ;
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

**Mentions** : 90 % → Historienne ou historien confirmé · 75 % → Enquêteur chevronné · 55 % → Enquêteur appliqué · en dessous → Enquêteur débutant.  
**Badges** : Équipe rapide (une salle en moins de 6 min) · Lecteur de registres (salle 2 sans indice) · Regard de conservateur
(salle 4 sans indice) · Enquêteur de confiance (3 indices au maximum sur la partie).

Les points récompensent la rigueur de l'enquête (lecture des documents, exactitude des dates), jamais une action liée au commerce de la traite.

---

## Les leçons (bouton « Leçons »)

Cinq leçons rédigées, une par salle, de 3 à 4 minutes de lecture, avec un texte CM1 et un texte CM2, des objectifs, un
lexique, un schéma et leurs sources en pied de leçon. Chaque énigme ouvre sa leçon par le bouton
« Leçon » (champ `lecon` de `enigmes.json`). L'enseignant peut interdire la consultation (⚙️ Réglages → Séance).
Les mêmes leçons existent en **version A4 imprimable** (`lecons-imprimables.html`, bouton « 📖 Leçons à imprimer » dans ⚙️ Réglages).

| Salle | Leçon (`id`) | Schéma |
|---|---|---|
| 1 | Le commerce triangulaire (`triangle`) | carte simplifiée de l'Atlantique et des trois trajets |
| 2 | La traite atlantique (`traite`) | frise des quatre siècles de la traite |
| 3 | La vie dans les plantations (`plantations`) | plan simplifié d'une habitation sucrière (sans personnage) ; document : le Code noir expliqué simplement |
| 4 | Les échanges avec les colonies (`ports`) | ce qui part des ports, ce qui y revient |
| 5 | Résistances et abolitions (`abolitions`) | frise 1685-2006 ; document : article 1er du décret du 27 avril 1848 |

Toutes les cartes et tous les schémas sont **dessinés en SVG** par script pour le jeu (simplifiés, sans échelle), jamais générés par IA.
Aucun dessin ne montre de personne réduite en esclavage ni de scène de violence.

---|---|---|
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
| les décors dessinés | `js/decors.js` |
| les personnages dessinés | `js/personnages.js` |

**Aucune énigme n'est écrite en dur** : le moteur est celui du tronc commun (`commun/js/enigmes.js`, partagé par tous les
jeux) ; aucun type d'énigme n'a été ajouté. Le jeu a été construit à partir du squelette de `mouvement/`.
On peut éditer les énigmes sans coder avec [editeur.html](../editeur.html).
Après une modification d'un fichier `js/` ou `css/`, augmentez son numéro de version dans `index.html` (`app.js?m2` → `app.js?m3`).
Ce README est régénéré à partir des données par `python traite-colonies/tests/generer-readme.py`.

```
traite-colonies/
├── index.html · prof.html · lecons-imprimables.html
├── README.md · GUIDE-PEDAGOGIQUE.md · A-VERIFIER.md · CHANGELOG.md
├── assets/
│   ├── data/      enigmes.json, dialogues.json, lecons.json, evaluations.json
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
python traite-colonies/tests/test_json.py
node traite-colonies/tests/test-jeu.js
node traite-colonies/tests/test-verifier.js
```

`test_json.py` contrôle les données (JSON valides, clés uniques, liens énigme → leçon, règles du cahier des charges, absence d'emoji).
`test-jeu.js` joue les parties complètes CM1 et CM2 (scores 185 et 235), teste les mauvaises réponses, les indices, les leçons,
le mode vérification, les réglages, les impressions et le tableau de bord. `node outils-tests/tous.js` lance les tests de tous les jeux.

---

## Sources

Faits vérifiés en ligne le 10 et le 11 novembre 2026.

- Programme d'histoire-géographie du cycle 3 : arrêté du 22 avril 2026, [BO n° 22 du 28 mai 2026](https://www.education.gouv.fr/bo/2026/Hebdo22/MENE2608631A), thème « Explorations et conquêtes ».
- Progression de l'enseignant : `programmation histoire-géo sciences 2026.pdf` (racine du dépôt), année A, période 3.
- BnF, France-Amériques, [« Slave trade » / « La traite négrière »](https://heritage.bnf.fr/france-ameriques/en/slave-trade-1) (Cécile Vidal, 2021, d'après la base Slave Voyages) : plus de 12,5 millions de personnes déportées ; 1 381 404 captifs et 4 118 expéditions sous pavillon français (1551-1875), environ 11 % ; Nantes 44 % des expéditions françaises, puis Le Havre, La Rochelle, Saint-Malo, Honfleur ; Bordeaux parmi les ports autorisés en 1713-1721 ; environ 320 captifs par navire, environ deux mois de traversée, environ 13 % de morts, environ 27 % d'enfants ; Saint-Domingue principale destination à partir de 1715 (trois quarts des expéditions), neuf voyages sur dix vers les Antilles et la Guyane ; Compagnie des Indes occidentales (1664) ; abolition le 4 février 1794, rétablissement le 20 mai 1802 ; insurrection d'août 1791.
- BnF, France-Amériques, [« Toussaint Louverture »](https://heritage.bnf.fr/france-ameriques/en/haiti) : né esclave vers 1740, chef de la révolte de 1791, gouverneur en 1798, mort prisonnier en France ; indépendance d'Haïti en 1804. Date du 1er janvier 1804 : [Hérodote](https://www.herodote.net/1er_janvier_1804-evenement-18040101.php).
- Académie de Bordeaux, [« Bordeaux et le commerce triangulaire »](https://ent2d.ac-bordeaux.fr/disciplines/lettres-histoire/wp-content/uploads/sites/5/2018/08/Bordeaux-et-le-commerce-triangulaire.pdf) (d'après le musée d'Aquitaine) : cargaison de La Licorne (départ le 8 janvier 1787, retour en août 1788) ; denrées des colonies (sucre, café, cacao, coton, indigo).
- Académie de Martinique, [« Le travail à l'habitation-sucrerie »](https://site.ac-martinique.fr/wp-content/uploads/sites/15/2019/03/Le-travail.pdf) (M. Descas-Ravoteur) : récolte de janvier à juin, coupe, dépaillage, moulin, vesou, sucrerie, purgerie ; journées de plus de 18 heures pendant la roulaison.
- Académie de Guyane, [livret « Le marronnage »](https://hist-geographie.dis.ac-guyane.fr/IMG/pdf/livret-marronnage-v8.pdf) : petit et grand marronnage, origine du mot (cimarrón).
- Sénat, [rapport sur la proposition de loi d'abrogation du Code noir](https://www.senat.fr/lessentiel/ppl25-672.pdf) (2026) : édit de mars 1685, esclaves assimilés à des « biens meubles », abrogation implicite en 1794 et en 1848 ; loi d'abrogation du 2 novembre 2026 (vie-publique.fr, voir A-VERIFIER.md).
- Ministère de la Culture, [« Mémoires de la traite, de l'esclavage et de leurs abolitions »](https://www.culture.gouv.fr/fr/thematiques/sciences-du-patrimoine/thematiques-de-recherche/patrimoine-et-societe/Patrimoine-de-la-traite-negriere-et-de-l-esclavage-Dossier-thematique/Memoires-de-la-traite-de-l-esclavage-des-abolitions) : loi n° 2001-434 du 21 mai 2001 ; décret n° 2006-388 fixant le 10 mai.
- Décret du 27 avril 1848 relatif à l'abolition de l'esclavage ([texte](https://mjp.univ-perp.fr/france/1848esclavage.htm)) : article 1er ; commission présidée par Victor Schœlcher.
- Musée d'histoire de Nantes, [présentation de la traite atlantique](https://www.anneauxdelamemoire.org/post/presenting-the-atlantic-slave-trade-and-colonial-slavery-at-the-nantes-history-museum-en-fr) : Nantes, premier port négrier français aux XVIIIe et XIXe siècles ; quatorze salles consacrées au sujet.
- Inventés pour le jeu, signalés comme tels : les Archives du port et leurs cinq personnages. Aucun chiffre n'est inventé.
