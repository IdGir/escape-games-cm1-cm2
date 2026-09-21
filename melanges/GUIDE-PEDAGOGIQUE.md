# Guide pédagogique — Le Laboratoire de Madame Mélange

Escape game de **sciences et technologie**, cycle 3, pour les **CM1 et CM2** (classes à double niveau).
Durée : **60 à 75 minutes** en une fois, ou **cinq séances de 25 minutes**.
Progression de l'enseignant : **Année B, période 1**.

> Lila, l'apprentie de Madame Mélange, a renversé toutes les fioles du laboratoire. Madame Mélange part
> à la retraite et lui a confié son testament de chimiste : un protocole en cinq opérations pour retrouver
> ses échantillons. La page est effacée ; chaque salle en cache une opération.

Énigmes, solutions et mécanisme final : [README.md](README.md). Médias facultatifs : [assets/README.md](assets/README.md).

---

## 1. Place dans les programmes

### L'extrait de la progression à couvrir

> États et constitution de la matière à l'échelle macroscopique. Comparer et mesurer des masses de différents
> objets ou liquide de diverses manières. Distinguer mélanges homogènes et hétérogènes. Séparer les constituants
> de mélanges solides ou solide-liquide.

### Correspondance avec le programme de cycle 3 (BO 2026, applicable à la rentrée 2026)

| Salle | Ce que font les élèves | Élément du programme (partie « La matière », CM1-CM2) |
|---|---|---|
| 1. La salle des balances | Comparer à la balance à plateaux, lire une balance électronique, peser un liquide dans un récipient, tarer, convertir g / kg | « Comparer les masses de différents corps à l'aide d'un dispositif simple » ; « Mesurer la masse d'un solide ou d'un liquide à l'aide d'une balance » ; « Effectuer des conversions d'unités de masse » |
| 2. La cuisine d'essai | Montrer avec la balance que le sucre dissous est toujours là ; distinguer dissoudre et fondre ; l'air a une masse | « Mettre en évidence expérimentalement que la masse totale se conserve lors du mélange d'un solide dans un liquide » ; « Observer que certains solides peuvent se dissoudre dans l'eau » ; attendu : décrire un échantillon de matière avec la grandeur masse |
| 3. La salle des fioles | Classer des mélanges en homogènes et hétérogènes, repérer un intrus, relier mélange et observation | « Caractériser la diversité de la matière à l'échelle macroscopique » ; progression de l'enseignant : « Distinguer mélanges homogènes et hétérogènes » |
| 4. L'atelier de tri | Choisir entre tri à la main, tamisage, aimantation, flottation ; ordonner les étapes | « Séparer les constituants d'un mélange de solides […] par tamisage » ; « Utiliser les propriétés physiques des matériaux pour les classer, notamment à des fins de tri » (le fer attiré par l'aimant) |
| 5. La saline | Décanter, filtrer, évaporer ; savoir qu'un solide dissous traverse le filtre ; ordonner un protocole | « Séparer les constituants […] d'un mélange solide-liquide par tamisage, décantation, filtration » ; « Il est possible de les récupérer [les solides dissous] par évaporation » |

**Hors programme de CM1-CM2 (situés en 6e), volontairement non travaillés :** la séparation de liquides non
miscibles (on observe l'eau et l'huile, on ne les sépare pas), l'étude quantitative de la saturation (évoquée
seulement : « au bout d'un moment, le sel ne se dissout plus »), la composition de l'air. Les mots *solution*,
*soluté*, *solvant* et *miscible* ne sont pas employés ; *dissous*, *mélange homogène* et *protocole* sont définis
dans les leçons.

### Compétences travaillées

- Pratiquer des démarches scientifiques : observer, mesurer, suivre et ordonner un protocole.
- Utiliser des outils de mesure : balance, unités de masse (g, kg ; t et mg en CM2).
- S'approprier un lexique précis : masse, équilibre, tare, dissoudre, homogène, hétérogène, tamiser, décanter, filtrer, évaporer.
- Mathématiques en appui : comparaison de nombres, additions et soustractions de masses, conversions (CM2).

### Liens avec les autres jeux

- **Suite : jeu n°10 (états de la matière).** Les notions d'évaporation (salle 5) et de « fondre » (salle 2) y seront reprises avec les changements d'état.
- **Lien possible avec le jeu n°08 (alimentation)** : le café filtré (filtration), le sel qui conserve les aliments, le sucre dissous.

---

## 2. Avant de jouer

### Prérequis conseillés

- Savoir lire un nombre jusqu'à 10 000 et comparer deux nombres entiers (CM1) ou deux nombres décimaux simples (CM2).
- Avoir déjà manipulé une balance, même rapidement.
- Idéalement, avoir fait **une manipulation d'accroche** avant le jeu : dissoudre un morceau de sucre dans un verre d'eau posé sur une balance de cuisine, et constater que l'affichage ne baisse pas.

### Le matériel (facultatif, pour les activités décrochées)

Balance de cuisine électronique (au gramme), balance à plateaux et masses marquées si l'école en dispose, verres ou gobelets transparents, sucre, sel fin, sable, gravier, sciure, un aimant, un tamis ou une passoire fine, des filtres à café et un entonnoir, une coupelle.

> **Limaille de fer** : si vous l'utilisez, en petite quantité, dans un sachet ou une boîte fermée pour les
> démonstrations ; lunettes pour les élèves qui manipulent ; pas de contact avec les yeux. On peut la remplacer par
> des trombones ou de petits clous mélangés au sable.

---

## 3. Mise en route, pas à pas

### A. En ligne (le plus simple)

1. Ouvrir **https://idgir.github.io/escape-games-cm1-cm2/melanges/** dans Chrome ou Edge (PC, TBI, tablette).
2. Chaque équipe tape son nom et choisit **CM1** ou **CM2**, puis clique sur « Entrer dans le laboratoire ».
3. La progression est gardée sur l'appareil : on peut reprendre la partie à la séance suivante.

### B. En local (sans internet, et avec le tableau de bord enseignant)

1. Double-cliquer sur `lancer.bat` à la racine du dossier (Windows).
2. Les élèves ouvrent l'adresse affichée dans la fenêtre noire, suivie de `/melanges/`.
3. L'enseignant ouvre `http://127.0.0.1:8000/melanges/prof.html` : suivi des équipes, pause générale, indices envoyés à la volée.

### C. Réglages à faire une fois (bouton ⚙️ dans le jeu)

- **Accessibilité** : taille des textes (jusqu'à 150 %), animations réduites.
- **Séance** : durée du minuteur (45 à 90 minutes), leçons autorisées ou non pendant le jeu.
- **Sons** : voix de synthèse des personnages, ambiances.
- **Impressions A4** : fiches préparatoires, QCM, vrai/faux et réponses courtes, étude de documents, avec corrigés.

Pour tester une salle ou une énigme sans toucher aux parties des élèves : `melanges/?salle=3&niveau=CM1`
(ajouter `&enigme=2` pour viser une énigme), ou la [page de vérification](https://idgir.github.io/escape-games-cm1-cm2/verifier.html#melanges).

---

## 4. Trois déroulés possibles

### Déroulé 1 — une séance longue (75 minutes)

| Temps | Phase |
|---|---|
| 5 min | Accroche : le verre d'eau sucrée sur la balance. Rappel de la règle « on ne goûte pas, on ne sent pas ». |
| 55 min | Jeu en équipes de 3-4. L'enseignant circule, relance à l'oral avant de laisser utiliser un indice. |
| 10 min | Mise en commun : le protocole PESER → OBSERVER → AIMANTER → ÉVAPORER → COMPARER écrit au tableau et expliqué. |
| 5 min | Quizz final dans le jeu ; trace écrite (leçon imprimée ou copiée). |

### Déroulé 2 — cinq séances de 25 minutes (recommandé en CM1)

Une salle par séance. La partie est sauvegardée sur l'appareil.

| Séance | Salle | 5 min avant | 15 min de jeu | 5 min après |
|---|---|---|---|---|
| 1 | La salle des balances | Manipuler une balance, comparer deux objets à la main puis à la balance | Salle 1 | Trace : peser un liquide = plein − vide |
| 2 | La cuisine d'essai | Le sucre dans l'eau, sur la balance | Salle 2 | Trace : la masse se conserve ; dissoudre ≠ fondre |
| 3 | La salle des fioles | Montrer 4 bocaux : eau salée, eau et huile, eau et sable, sirop à l'eau | Salle 3 | Trace : homogène / hétérogène, avec exemples |
| 4 | L'atelier de tri | Aimant, tamis, bassine d'eau sur une table de démonstration | Salle 4 | Trace : une méthode = une différence |
| 5 | La saline | Filtrer de l'eau boueuse ; mettre une coupelle d'eau salée sur un radiateur ou au soleil (résultat quelques jours plus tard) | Salle 5 + fin | Trace : le protocole ; quizz |

### Déroulé 3 — au TBI, classe entière

L'enseignant joue ; les équipes répondent sur ardoise avant chaque validation. Choisir le niveau CM2 pour une classe
de CM2, ou CM1 si le double niveau a besoin d'un rythme commun, et faire expliquer chaque correction à l'oral.
Compter une salle par séance de 20 minutes.

---

## 5. Différenciation CM1 / CM2

La différence ne tient pas seulement au nombre d'énigmes (15 / 20).

| | CM1 | CM2 |
|---|---|---|
| **Nombres et unités** | Masses entières en grammes, repères (1 kg = 1 000 g) | Conversions g / kg avec décimaux (0,2 kg ; 1,05 kg), tonne et milligramme |
| **Calculs** | Une opération (plein − vide, eau + sucre) | Deux étapes (bol + eau + sucre ; flacon en kg) |
| **Nombre d'éléments** | 3 à 6 éléments par énigme | 4 à 9 éléments, plus d'étiquettes pièges |
| **Abstraction** | Critère visible (« je vois une chose / deux choses ») | Vocabulaire « constituant », cas limites : air, eau du robinet, sel avant et après dissolution |
| **Chiffres donnés** | Pas de valeur à retenir | L'eau de mer contient en moyenne 35 g de sel par litre ; 1 L d'huile ≈ 920 g ; 1 L d'air ≈ 1,2 g |
| **Protocole final** | Testament explicite, étape par étape | Testament sous forme d'énigme, avec les masses (500 g, 30 g, 20 g) |
| **Énigmes en plus** | — | 1-4 unités de masse · 2-4 cadenas des masses · 3-4 idées fausses · 4-4 établi · 5-2 montage de filtration |

**Classe à double niveau** : on peut constituer des équipes mixtes jouant en CM2, un élève de CM2 « chimiste en chef »
lisant les consignes, ou des équipes par niveau jouant en même temps (la mise en commun porte alors sur le protocole
commun aux deux niveaux).

**Élèves en difficulté de lecture** : activer la voix de synthèse (⚙️ → Sons) ; augmenter la taille du texte ;
autoriser les leçons. **Élèves rapides** : leur confier la vérification des corrections à voix haute, ou la
rédaction du protocole de la salle 5 avec les masses.

---

## 6. Gestion de classe

- **Équipes de 3-4** avec des rôles : lecteur (lit la consigne), calculateur (pose les calculs), gardien du temps, porte-parole (demande un indice à l'enseignant avant de cliquer).
- **Les indices coûtent 2 points** : demander aux équipes de relire la leçon avant d'en ouvrir un.
- **Le tableau de bord** (mode local) montre la salle et l'énigme de chaque équipe : repérer une équipe bloquée plus de 5 minutes et aller la relancer.
- **Pause générale** depuis le tableau de bord pour une mise au point collective (par exemple sur « fondre / dissoudre » après la salle 2).
- **Rejouer** : le bouton « Rejouer » en fin de partie efface la sauvegarde de l'appareil.

---

## 7. Lexique à installer

| Mot | Définition pour les élèves | Salle |
|---|---|---|
| Masse | Ce que l'on mesure avec une balance, en grammes ou en kilogrammes | 1 |
| Équilibre | Les deux plateaux à la même hauteur : les masses sont égales | 1 |
| Tare | Touche qui remet la balance à zéro, récipient posé | 1 |
| Volume | La place qu'occupe un objet ou un liquide (en litres) | 1 |
| Se dissoudre | Se mélanger à un liquide au point de ne plus se voir, sans disparaître | 2 |
| Se conserver | Rester le même | 2 |
| Fondre | Passer de l'état solide à l'état liquide sous l'effet de la chaleur | 2 |
| Matière | Tout ce qui a une masse et occupe de la place : solides, liquides, gaz | 2 |
| Mélange, constituant | Matière formée d'au moins deux constituants ; chacune des matières présentes | 3 |
| Homogène / hétérogène | On ne distingue pas / on distingue au moins deux constituants à l'œil nu | 3 |
| Tamiser, aimanter, flottation | Séparer selon la taille ; avec un aimant ; dans l'eau (flotte / coule) | 4 |
| Décanter, filtrer, évaporer | Laisser reposer et verser ; retenir les grains ; faire partir l'eau en vapeur | 5 |
| Protocole | Liste ordonnée des opérations d'une expérience | 5 |
| Paludier | Personne qui récolte le sel dans les marais salants | 5 |

---

## 8. Évaluation

### Ce que le jeu mesure tout seul

Score (100 en CM1, 125 en CM2), énigmes résolues, indices utilisés par salle, temps par salle, quizz final
(5 questions), badges. Le bilan s'imprime en fin de partie.

### Les supports imprimables (⚙️ → Impressions A4)

| Support | CM1 | CM2 |
|---|---|---|
| Fiches préparatoires (une par salle) | 5 | 5 |
| QCM | 10 questions | 12 questions |
| Vrai/faux et réponses courtes | 8 | 8 |
| Études de documents | « L'expérience de Marius », « Le bac de Nadia » | « Le récit du paludier », « Le testament de Madame Mélange » |

Chaque impression comporte un **corrigé séparé** par un intercalaire.

### Grille d'observation pendant la séance

| Critère | Non acquis | En cours | Acquis |
|---|---|---|---|
| Compare deux masses et lit une balance | | | |
| Calcule la masse d'un liquide (plein − vide) | | | |
| Explique que la masse se conserve lors d'une dissolution | | | |
| Classe un mélange en homogène ou hétérogène et justifie | | | |
| Choisit une méthode de séparation adaptée et la justifie | | | |
| Sait qu'un solide dissous traverse le filtre et se récupère par évaporation | | | |
| Ordonne un protocole | | | |
| Respecte les règles de sécurité (ne pas goûter, ne pas sentir) | | | |

---

## 9. Activités décrochées (en classe, avec du vrai matériel)

1. **Le sucre sur la balance** (salle 2) : verre d'eau sur la balance, noter la masse ; peser un morceau de sucre ; le verser, remuer, relire. Comparer.
2. **Les quatre bocaux** (salle 3) : classer eau salée, eau et huile, eau et sable, sirop à l'eau. Laisser reposer une vinaigrette.
3. **Le bac de Nadia** (salle 4) : séparer gravier + sable + trombones (aimant, tamis) ; sciure + sable (bassine d'eau).
4. **Filtrer l'eau boueuse** (salle 5) : décantation, puis filtre à café dans un entonnoir. Faire constater que l'eau filtrée est plus claire, mais qu'on ne la boit pas.
5. **Récupérer le sel** (salle 5) : une coupelle d'eau très salée posée sur un radiateur ou au soleil ; observer les cristaux quelques jours plus tard.

**Dans toutes ces activités : on ne goûte pas, on ne sent pas, même le sucre ou le sel.** C'est la même règle que dans le jeu : elle construit l'habitude de travail du laboratoire.

---

## 10. Points de vigilance notionnels

| Erreur fréquente | Ce qu'il faut dire | Où c'est travaillé |
|---|---|---|
| « Le sucre a disparu. » | Il s'est **dissous** : on ne le voit plus, mais il est là. La balance le prouve : la masse ne baisse pas. | 2-1, 2-2, 2-3, leçon 2 |
| « Le sucre a fondu. » | **Fondre** demande de la chaleur (la glace fond). Dans l'eau froide, le sucre **se dissout**. | 2-1 (CM2), 2-3 (CM2), leçon 2 |
| « L'eau salée n'est pas un mélange. » | C'est un **mélange homogène** : eau + sel. Ne pas voir un constituant ne veut pas dire qu'il n'y est pas. | 3-1, 3-2, 3-4, leçon 3 |
| « L'air n'est pas de la matière. » | L'air est un mélange de gaz ; il occupe de la place et **a une masse** (un ballon gonflé pèse un peu plus que dégonflé). | 2-3, 3-3 (CM2), 3-4, leçon 2 |
| « L'eau du robinet est de l'eau pure. » | Elle contient des sels minéraux dissous : c'est un mélange homogène. | 3-1, 3-2, 3-4 (CM2) |
| « Un litre, c'est un kilo. » | Vrai seulement à peu près pour l'eau. Le litre mesure un **volume**, pas une masse ; 1 L d'huile pèse environ 920 g. | 1-2 (CM2), 1-3 (CM2), 1-4, leçon 1 |
| « On peut enlever le sel en filtrant. » | Le sel **dissous** traverse le filtre. Seule l'**évaporation** le récupère. | 5-1, 5-2, leçon 5 |
| « L'eau filtrée est potable. » | Filtrer retire les grains, pas ce qui est dissous ni les microbes. On ne boit pas une eau filtrée en classe. | 5-1 (correction), leçon 5 |
| « Un aimant attire tous les métaux. » | Il attire le fer et l'acier, pas l'aluminium, le cuivre ou l'or. | 4-3, leçon 4 |
| Goûter pour vérifier | **Jamais** au laboratoire, ni sentir un produit : on observe et on mesure. | Accueil, 2-1, 3-4, leçon 2 |

**Vocabulaire du collège** : *solution*, *solvant*, *soluté*, *miscible*, *masse volumique* ne sont pas utilisés.
Si un élève les emploie, les accepter et les traduire : une *solution*, c'est un mélange homogène obtenu en dissolvant
un solide dans un liquide.

**Précision sur l'eau et l'huile** : au CM, on les **observe** (deux couches, l'huile au-dessus). Leur séparation
(ampoule à décanter) relève de la 6e.

---

## 11. Sources

- Ministère de l'Éducation nationale, **Programme de sciences et technologie du cycle 3**, annexe publiée au Bulletin officiel en 2026, applicable à la rentrée 2026 — partie « La matière ». [PDF](https://www.education.gouv.fr/sites/default/files/document/Annexe%20%E2%80%93%20Programme%20de%20sciences%20et%20technologie%20du%20cycle%203-365166.pdf)
- Académie de Dijon, [présentation des nouveaux programmes de sciences et technologie au cycle 3](https://svt.wp.ac-dijon.fr/2026/06/18/nouveaux-programmes-de-sciences-et-technologie-au-cycle-3-publication-au-bulletin-officiel/).
- Fondation **La main à la pâte**, séquence [« À la découverte des mélanges »](https://fondation-lamap.org/sequence-d-activites/a-la-decouverte-des-melanges) (cycle 3) : mélanges homogènes et hétérogènes, dissolution, séparation, consignes de sécurité.
- Salinité moyenne de l'eau de mer (environ 35 g/L, entre 30 et 40 g/L selon les mers) et solubilité du sel (environ 36 g pour 100 mL d'eau à 20 °C) : données de référence en chimie (articles « Eau de mer » et « Chlorure de sodium »).
- Masse d'un litre d'air (environ 1,2 g à 20 °C) : valeur usuelle des cours de physique-chimie de 4e.
- **Cité des sciences et de l'industrie** et **Lumni** : vidéos et ressources de consolidation sur les mélanges et la séparation des constituants, à choisir par l'enseignant pour la trace écrite.

Les points restant à contrôler sont listés dans [A-VERIFIER.md](A-VERIFIER.md).
