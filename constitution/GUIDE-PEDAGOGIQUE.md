# 📖 Guide pédagogique — Le Sceau de la République

**Escape game d'enseignement moral et civique · cycle 3 (CM1 / CM2) · la Constitution du 4 octobre 1958**

Ce guide accompagne le jeu : place dans les programmes, mise en route pas à pas, déroulés
possibles, différenciation, lexique, évaluation, et passerelle vers le concours national
« Découvrons notre Constitution ».

Le détail des énigmes et leurs solutions se trouvent dans le [README du jeu](README.md).

---

## 1. Place dans les programmes

Le programme d'**enseignement moral et civique** publié au **Bulletin officiel n° 24 du
13 juin 2024** s'applique à tous les niveaux depuis la **rentrée 2026**. Il organise le cycle 3
autour d'un thème annuel :

| Niveau | Thème annuel | Ce que le jeu apporte |
|---|---|---|
| **CM1** | *Faire société* | Les règles communes, la loi qui s'applique à tous, les valeurs partagées, la séparation des pouvoirs présentée simplement |
| **CM2** | *Vivre en République* | La Constitution et le bloc de constitutionnalité, les institutions, le parcours d'une loi, le Conseil constitutionnel, les principes de l'article 1er |

Le jeu convient donc particulièrement au **CM2**, et se joue en CM1 dans sa version réduite
(15 énigmes au lieu de 20). En classe à double niveau, les deux parcours tournent en parallèle
sur les mêmes postes : le niveau est choisi par l'équipe à l'écran d'accueil.

> Reportez-vous au BO pour la formulation exacte des attendus, et ajustez la fiche de
> compétences du § 8 à votre progression.

**Compétences travaillées, toutes disciplines**

- Comprendre et appliquer des règles communes ; distinguer règle, loi et Constitution.
- Identifier les institutions de la République et le rôle de chacune.
- Lire et prélever des informations dans un texte juridique simplifié.
- Argumenter, justifier un choix, coopérer dans un petit groupe.
- Utiliser un vocabulaire civique précis.

**Liens avec les autres enseignements** : histoire (la Révolution française, la naissance de la
République, la Ve République) ; français (lecture de documents, lexique, argumentation) ;
questionner le monde / sciences (la Charte de l'environnement).

---

## 2. Avant de jouer

### Prérequis conseillés

Aucun prérequis n'est indispensable : les leçons 📚 sont consultables pendant la partie, et
chaque énigme donne sa correction après validation. Le jeu fonctionne donc aussi bien
**en découverte** qu'**en révision**.

Il gagne toutefois à être précédé de deux ou trois séances :

1. La devise et les symboles de la République.
2. « Qu'est-ce qu'une loi ? Qui la fait ? »
3. Le vote et l'élection (si possible, une élection de délégués dans la classe).

### Le lien avec « Le Secret de la Déclaration »

Si votre classe a joué à l'escape game sur la Révolution française, l'entrée en matière est
immédiate : le jeu s'ouvre **dans la même cour du Palais-Royal**, et le coffre porte la mention
« Aux apprentis du 26 août 1789 ». La Déclaration des droits de l'homme et du citoyen que les
élèves y avaient sauvée est aujourd'hui l'un des **quatre textes du bloc de constitutionnalité** :
c'est exactement ce qu'ils découvrent dans la salle 2.

Si votre classe n'y a pas joué, rien ne manque : le rappel est fait dans le dialogue d'ouverture.

---

## 3. Mise en route, pas à pas

### A. Le plus simple — en ligne

1. Ouvrez **Chrome** (ou Edge) sur l'ordinateur de la classe, le TBI ou les tablettes.
2. Allez à l'adresse : `https://idgir.github.io/escape-games-cm1-cm2/constitution/`
3. Mettez-la en favori une fois pour toutes.

Tout fonctionne en ligne : jeu, leçons, fiches à imprimer. **Seul le tableau de bord enseignant
en direct demande le mode local** (ci-dessous).

### B. En local — sans internet, et avec le tableau de bord enseignant

**Outil à démarrer : l'invite de commandes Windows (ou simplement un double-clic).**

*Méthode « double-clic », la plus simple :*

1. Ouvrez l'**Explorateur de fichiers** Windows.
2. Allez dans le dossier `E:\IDRISS\PROJET ESCAPE GAMES`.
3. Double-cliquez sur **`lancer.bat`**.
4. Une fenêtre noire s'ouvre et affiche les adresses. Le navigateur s'ouvre tout seul sur
   `http://127.0.0.1:8000/`.
5. **Laissez la fenêtre noire ouverte** pendant toute la séance. Pour arrêter le serveur :
   cliquez dans la fenêtre noire et appuyez sur **Ctrl + C**.

*Méthode « ligne de commande », si le double-clic ne fonctionne pas :*

1. Appuyez sur **Windows + R**, tapez `cmd`, puis **Entrée** : l'**invite de commandes** s'ouvre.
2. Tapez exactement, puis **Entrée** :
   ```
   E:
   ```
3. Puis, toujours suivi d'**Entrée** :
   ```
   cd "\IDRISS\PROJET ESCAPE GAMES"
   ```
4. Puis :
   ```
   python serveur.py
   ```
5. La fenêtre affiche les adresses à donner aux élèves, par exemple
   `http://192.168.1.20:8000/constitution/`. Recopiez-la au tableau.
6. Pour arrêter : **Ctrl + C** dans cette même fenêtre.

> Si le message « python n'est pas reconnu » apparaît, installez Python 3 depuis
> <https://www.python.org/downloads/> en **cochant « Add Python to PATH »**, puis recommencez
> à l'étape 1. En attendant, la méthode A (en ligne) fonctionne sans rien installer.

**Adresses utiles en mode local**

| Pour | Adresse |
|---|---|
| Les élèves | `http://<adresse affichée>:8000/constitution/` |
| Le tableau de bord enseignant | `http://127.0.0.1:8000/constitution/prof.html` |
| La page de vérification | `http://127.0.0.1:8000/verifier.html#constitution` |

### C. Réglages à faire une fois, avant les élèves

Cliquez sur **⚙️** en haut à droite :

- **Durée du minuteur** : 60 min par défaut, 45 si votre créneau est court.
- **Voix des personnages** : à couper si plusieurs postes sont dans la même salle sans casques.
- **Ambiances et bruitages** : idem.
- **Bibliothèque de leçons 📚** : laissez-la active en découverte, coupez-la en évaluation.
- **Concours** : **désactivé par défaut**. Voir le § 9.

Puis **💾 Enregistrer les réglages** : ils restent sur le poste.

---

## 4. Trois déroulés possibles

### Déroulé 1 — une séance longue (75 minutes)

| Temps | Phase | Ce que fait l'enseignant |
|---|---|---|
| 0-5 min | Mise en situation | Projeter l'écran d'accueil, écouter Monsieur Berthier, rappeler le jeu sur 1789 |
| 5-10 min | Constitution des équipes | 3 ou 4 élèves, rôles distribués (§ 6) ; saisie du nom d'équipe et du niveau |
| 10-25 min | Serrures 1 et 2 | Circuler, relancer sans donner la réponse, renvoyer vers 📚 |
| 25-30 min | **Pause collective** | Bouton ⏸ : faire verbaliser « qu'est-ce qu'une Constitution ? » |
| 30-55 min | Serrures 3 et 4 | Idem ; signaler le temps restant |
| 55-65 min | Serrure 5 et ouverture du coffre | Lecture collective de l'article 1er projeté |
| 65-75 min | Bilan, quizz, trace écrite | Impression du bilan ; institutionnalisation |

### Déroulé 2 — cinq séances de 25 minutes (recommandé en CM1)

Une salle par séance, avec à chaque fois : rappel de 5 min → jeu 15 min → trace écrite 5 min.
À la fin de chaque séance, cliquez sur **⏸** et notez le nom de l'équipe : le jeu propose de
**reprendre la partie en cours** à la séance suivante, sur le même poste et le même navigateur.

| Séance | Salle | Trace écrite attendue |
|---|---|---|
| 1 | La cour du Palais-Royal | Définition de « Constitution » + les trois pouvoirs |
| 2 | La salle des Textes | La frise des quatre textes (1789, 1946, 1958, 2004) |
| 3 | L'hémicycle | Le schéma des institutions |
| 4 | La navette parlementaire | Les étapes du parcours d'une loi |
| 5 | La salle des séances | Les articles 1 et 2 + trois exemples du quotidien |

### Déroulé 3 — au TBI, classe entière

Un seul poste, l'enseignant manipule, les élèves débattent avant chaque clic. Choisir le niveau
**CM2** (les énigmes supplémentaires nourrissent la discussion), agrandir les textes à 130 %
dans ⚙️ Accessibilité, et couper le minuteur de la pression en annonçant qu'il est indicatif.

---

## 5. Différenciation CM1 / CM2

Le niveau est choisi par l'équipe à l'écran d'accueil et change **tout** le contenu, pas
seulement sa quantité.

| | CM1 | CM2 |
|---|---|---|
| Nombre d'énigmes | 15 (3 par salle) | 20 (4 par salle) |
| Score maximal | 100 points | 125 points |
| Consignes | Phrases courtes, une action par phrase | Consignes plus denses, avec mise en garde |
| QCM | 3 propositions | 4 propositions, dont un distracteur plausible |
| Vrai / faux | 4 affirmations | 6 affirmations |
| Associations et tris | 3 à 6 éléments | 4 à 9 éléments |
| Frises | Dates affichées sur les cartes | Dates masquées, indices dans le contenu |
| Textes à trous | 4 trous, étiquettes proches | 6 trous, distracteurs ajoutés |
| Énigmes propres au CM2 | — | Lettres cachées, deux cadenas à chiffres, la frise des présidents, la fiche d'identité du Conseil constitutionnel |
| Rythme attendu | 8 min par salle avant perte du bonus | 10 min par salle |

**Autres leviers, sans changer de niveau**

- ⚙️ **Agrandissement des textes** (jusqu'à 150 %) pour les élèves malvoyants ou dyslexiques.
- ⚙️ **Animations réduites** pour les élèves sensibles au mouvement, ou sur un poste lent.
- ⚙️ **Voix des personnages** : la synthèse vocale lit les dialogues — utile aux lecteurs fragiles,
  avec un casque.
- **Bibliothèque 📚** : les 16 fiches officielles sont les mêmes pour tous, mais rangées par salle ; les infographies d'une page conviennent aux CM1, les dossiers de 3 à 5 pages aux CM2 et à la préparation.
- **Indices** : trois par énigme, de plus en plus explicites. Ils coûtent 2 points, jamais la
  réussite : une équipe qui prend tous les indices finit le jeu.

---

## 6. Gestion de classe

**Équipes de 3 ou 4**, avec des rôles tournant à chaque salle :

| Rôle | Ce qu'il fait |
|---|---|
| **Le greffier** | Tient la souris ou le clavier. Il n'a pas le droit de cliquer sans l'accord du groupe. |
| **Le lecteur** | Lit à voix haute la consigne et les propositions. |
| **Le documentaliste** | Seul autorisé à ouvrir 📚 et à chercher dans la leçon. |
| **Le porte-parole** | Explique à l'enseignant ce que le groupe a compris, avant de demander de l'aide. |

**Règle d'or** : l'enseignant ne donne jamais une réponse. Il renvoie vers le bouton 💡, vers la
bibliothèque 📚, ou pose une question qui relance (« relis la deuxième phrase : qui vote ? »).

**Le tableau de bord** (mode local) affiche en direct, pour chaque équipe : la salle, l'énigme en
cours, le score, les serrures ouvertes, le temps. Il permet une **pause générale**, un **message
diffusé à toutes les équipes**, et un **indice envoyé à une équipe précise**. C'est l'outil idéal
pour repérer une équipe bloquée sans se déplacer.

**Bruit** : si plusieurs postes sont dans la même salle, coupez les voix et les ambiances
(⚙️ Sons), ou prévoyez des casques.

---

## 7. Lexique à installer

| Mot | Définition à faire formuler |
|---|---|
| Constitution | L'ensemble des règles qui organisent un pays ; le texte le plus important, au-dessus de toutes les lois |
| Préambule | Le texte d'introduction, placé avant les articles |
| Bloc de constitutionnalité | Les quatre textes sur lesquels s'appuie le Conseil constitutionnel |
| Référendum | Un vote où les citoyens répondent directement par oui ou par non |
| Promulguer | Rendre une loi officielle |
| Projet de loi | Un texte dont l'idée vient du Gouvernement |
| Proposition de loi | Un texte dont l'idée vient d'un député ou d'un sénateur |
| Amendement | Une modification proposée puis votée sur un texte |
| Navette | L'aller-retour du texte entre l'Assemblée nationale et le Sénat |
| Journal officiel | La publication où paraissent les textes de loi |
| Suffrage universel direct / indirect | Les citoyens votent eux-mêmes / ce sont des élus qui votent |
| Laïcité | La séparation des religions et de l'État ; l'État reste neutre |
| Indivisible | Partout en France, les mêmes droits et les mêmes devoirs |

Les cinq **fiches préparatoires** imprimables (⚙️ → Impressions) reprennent ce lexique salle par
salle, avec les objectifs et un court texte de contexte : elles peuvent être distribuées avant
chaque séance du déroulé 2.

---

## 8. Évaluation

### Ce que le jeu mesure tout seul

Le bilan imprimable (bouton 🖨️ à la fin, ou ⚙️ → Impressions) donne pour chaque équipe : le
score, le temps, le nombre d'énigmes résolues, les serrures ouvertes, le nombre d'indices
consultés, le résultat au quizz et les badges. **Le score est un indicateur de coopération et de
méthode, pas une note.**

### Les supports imprimables

⚙️ → **Impressions A4** produit, avec les corrigés **séparés par un intercalaire** :

| Support | CM1 | CM2 |
|---|---|---|
| Fiches préparatoires (5 salles) | oui | oui |
| QCM | 10 questions | 12 questions |
| Vrai / faux et réponses courtes | 8 questions | 8 questions |
| Étude de documents | 2 documents | 2 documents |

Imprimez une seule fois avec « 📚 Tout imprimer » : la liasse est dans l'ordre, élèves d'abord,
corrigés ensuite, séparés par une page ✂️ CORRIGÉS.

### Grille d'observation pendant la séance

| Observable | Non acquis | En cours | Acquis |
|---|---|---|---|
| Distingue règle, loi et Constitution | | | |
| Nomme les trois pouvoirs et qui les exerce | | | |
| Situe 1789, 1946, 1958, 2004 sur une frise | | | |
| Ordonne les étapes du parcours d'une loi | | | |
| Explique le rôle du Conseil constitutionnel | | | |
| Cite un droit garanti par la Constitution dans sa vie quotidienne | | | |
| Écoute les autres et justifie son choix avant de cliquer | | | |
| Cherche dans la leçon avant de demander un indice | | | |

---

## 9. Le concours « Découvrons notre Constitution »

### L'option dans le jeu

Elle est **désactivée par défaut**, et **la participation au concours est facultative** : n'activez
l'option que si vous envisagez sérieusement d'y inscrire la classe, pour ne pas créer d'attente.

1. Cliquez sur **⚙️**.
2. Section **🏛️ Concours** : basculez **« Annoncer le concours en fin de partie »**.
3. Cliquez sur **👁️ Aperçu de l'encart** pour voir ce que les élèves verront.
4. **💾 Enregistrer les réglages**.

L'encart apparaît alors **à la toute fin**, après le bilan et le quizz : présentation du concours,
calendrier, liens officiels, et un bouton **🖨️ Fiche de projet** qui imprime une feuille de route
A4 à remplir en classe (ce que nous avons appris · notre sujet · notre forme · qui fait quoi ·
pour quand · le calendrier officiel).

### Ce qu'il faut savoir

- Organisé par le **ministère de l'Éducation nationale** et le **Conseil constitutionnel**.
- Ouvert du **CM1 au lycée**, participation **collective** : une classe, plusieurs classes ou un
  établissement.
- Catégorie qui vous concerne : **cycle 3 (CM1, CM2, 6e)**.
- **Grande liberté de forme** : texte, dossier, film, affiche, production plastique, théâtre,
  chorégraphie, site internet.
- Session **2026-2027**, thème **« L'État de droit »**.

| Étape | Date | Comment |
|---|---|---|
| Inscription | jusqu'au **vendredi 29 janvier 2027** | via l'application **ADAGE** ; formulaire officiel si l'établissement n'y a pas accès |
| Dépôt des productions | **mardi 4 mai 2027** | auprès du référent académique |
| Jury académique | avant le **27 mai 2027** | sélection transmise au jury national |
| Jury national | fin juin / début juillet 2027 | |
| Remise des prix | septembre-octobre 2027 | au Conseil constitutionnel, à Paris |

Règlement, formulaire d'inscription et fiche de présentation :
<https://eduscol.education.gouv.fr/3295/concours-decouvrons-notre-constitution>
Ressources : <https://www.decouvronsnotreconstitution.fr/concours-decouvrons-notre-constitution>
Contact national : **laconstitution.dgesco@education.gouv.fr**

> ⚠️ Thème et dates relevés le 19 septembre 2026 sur les sites officiels. **Seul le règlement de
> la session en cours fait foi** : vérifiez-le et prévenez votre référent académique avant toute
> inscription. Pour mettre l'encart à jour l'année suivante, modifiez simplement
> `assets/data/concours.json` — aucun code à toucher.

### Cinq projets qui découlent directement du jeu

| Salle | Projet possible | Forme |
|---|---|---|
| 1 | « La Constitution de notre classe » : écrire un préambule et dix articles, puis les faire adopter par un vote | Affiche grand format ou livret |
| 2 | La frise des quatre textes, illustrée et commentée par les élèves | Frise murale photographiée |
| 3 | Un reportage : « Qui décide quoi ? », avec interview du maire ou d'un élu local | Film de 3 à 5 minutes |
| 4 | « Le voyage d'une loi » : une loi imaginaire suivie de son dépôt à son application | Théâtre ou bande dessinée |
| 5 | « L'État de droit près de chez nous » : cinq situations du quotidien, cinq articles | Exposition de cinq panneaux |

Le thème de la session, **« L'État de droit »**, est directement servi par les salles 4 et 5 :
l'idée que personne, pas même ceux qui gouvernent, n'est au-dessus de la loi, et qu'un juge
indépendant le vérifie.

---

## 10. Points de vigilance notionnels

Quelques confusions fréquentes chez les élèves, à anticiper :

- **« Loi » et « Constitution »** : la Constitution n'est pas une loi parmi d'autres, elle est
  au-dessus. Image utile : la règle du jeu, qu'on ne change pas en pleine partie.
- **« Le président fait les lois »** : non, il les **promulgue**. Ce sont les députés et les
  sénateurs qui les votent.
- **« Projet » et « proposition »** : moyen mnémotechnique — **PRO**jet = **G**ouvernement (il
  *projette*, il gouverne) ; **PRO**position = **P**arlementaires.
- **« On vote pour les sénateurs »** : non, ce sont de grands électeurs (maires, conseillers,
  députés) qui les élisent — c'est le suffrage universel **indirect**.
- **« La laïcité, c'est interdire les religions »** : non, c'est la neutralité de l'État et la
  liberté de croire ou de ne pas croire.
- **« Publiée » et « appliquée »** : la loi est d'abord publiée au Journal officiel, puis elle
  entre en vigueur.
- **Neutralité** : le jeu ne cite aucun parti politique et ne porte aucun jugement sur les
  personnes. Les présidents de la Ve République n'y apparaissent que comme repères
  chronologiques. Si un élève engage un débat partisan, ramenez-le aux institutions.

---

## 11. Sources

Le contenu des énigmes et des leçons est construit à partir des ressources pédagogiques
officielles du **Conseil constitutionnel** et du **ministère de l'Éducation nationale**, publiées
sur <https://www.decouvronsnotreconstitution.fr> :

| Fiche officielle | Format | Utilisée dans |
|---|---|---|
| *La Constitution française* | Infographie — 1 page | salle 1 — énigmes 1-1, 1-3 |
| *Qu'est-ce qu'une Constitution ? (dossier)* | Dossier élève — 5 rubriques | salle 1 — énigmes 1-4 |
| *Jeu : Sais-tu ce qu'est une Constitution ?* (fiche-jeu) | Fiche-jeu — 6 questions, corrigé inclus | salle 1 — énigmes 1-2 |
| *Les textes de notre Constitution* | Infographie — 1 page | salle 2 — énigmes 2-1, 2-2 |
| *Le texte de la Constitution de la Ve République (dossier)* | Dossier élève — 4 à 5 pages | salle 2 — énigmes 2-3, 2-4 |
| *Jeu : Es-tu incollable sur la Constitution de la Ve République ?* (fiche-jeu) | Fiche-jeu — 6 questions, corrigé inclus | salle 2 — révision / prolongement |
| *Comment la Constitution organise la vie démocratique* | Dossier élève — 3 pages | salle 3 — énigmes 3-1, 3-3 |
| *Le président de la République* | Infographie — 1 page | salle 3 — énigmes 3-2, 3-4 |
| *Le parcours d'une loi* | Infographie — 1 page | salle 4 — énigmes 4-1, 4-2 |
| *La procédure d'élaboration des lois (dossier 2025)* | Dossier élève — 3 pages | salle 4 — énigmes 4-4, 5-4 |
| *Jeu : Que sais-tu sur la procédure d'élaboration des lois ?* (fiche-jeu) | Fiche-jeu — 5 vrai/faux, corrigé inclus | salle 4 — énigmes 4-3 |
| *Les valeurs et principes de la République française* | Infographie — 1 page | salle 5 — énigmes 5-1, 5-2 |
| *Les symboles de la République française* | Infographie — 1 page | salle 5 — révision / prolongement |
| *Les libertés en France* | Infographie — 1 page | salle 5 — révision / prolongement |
| *La Constitution au quotidien* | Infographie — 1 page | bonus — énigmes 5-3 |
| *La Constitution dans ta vie quotidienne (dossier)* | Dossier élève — 3 pages | bonus — révision / prolongement |

Ces 16 documents **sont** les leçons du jeu : le bouton 📚 les ouvre tels quels (visionneuse
PDF intégrée, téléchargement, lien vers la page d'origine), et chaque énigme porte un bouton
**📚 Fiche source** qui ouvre le document dont elle est tirée. Ils sont installés dans
`constitution/assets/lecons/` ; sans eux, le jeu bascule automatiquement sur les liens en ligne.

**Réutilisation :** Contenus librement diffusables et reproductibles pour un usage non commercial, sous réserve de citer la source, de conserver le titre, la date d'extraction et le nom de l'illustrateur, et de ne pas altérer les contenus (mentions légales du site).

Le texte des articles 1er et 2 est celui de la **Constitution du 4 octobre 1958** dans sa
rédaction en vigueur. Chaque énigme affiche sa source sous le bouton d'indice, et chaque leçon
cite le document dont elle est tirée : les élèves voient que ces informations ne sortent pas de
nulle part.

---

*Bonne séance — et si vos élèves ouvrent le coffre en moins de 40 minutes, offrez-leur la
lecture intégrale de l'article 1er, à voix haute, debout.*
