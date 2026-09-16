# Ce qui a changé — Phase J3

Sept chantiers, tous appliqués et vérifiés (58 tests automatiques passés sur
l'interface réelle, aucun échec).

---

## 1. Les fiches ciblées sont désormais rattachées à votre Classeur

**Ce que cela veut dire concrètement.** Avant, une fiche d'exercices imprimée
affichait une règle réécrite par l'application — correcte, mais ce n'était pas
la formulation que vos élèves ont dans leur classeur. Maintenant, l'application
va chercher la vraie leçon CM1 correspondante parmi vos 70 fiches et en extrait
trois choses, qu'elle imprime en tête de l'exercice :

- **la règle telle que vous l'avez écrite** (le bloc « règle » de votre fiche) ;
- **votre astuce, votre 💡** (le bloc « conseil ») ;
- **vos exemples** « X → Y » quand la fiche en contient (« un grand pied → de
  grands pieds »), imprimés dans un encadré « Les modèles de la leçon ».

Un bandeau discret rappelle en haut : *📘 Leçon du classeur : Le pluriel des
adjectifs (ORTH-23)*. L'élève sait donc **exactement quelle fiche relire**, et il
travaille sur la même formulation en classe et à la maison.

**J'ai aussi corrigé le rattachement lui-même**, qui était en partie faux :

| Catégorie | Leçon principale avant | Leçon principale maintenant |
|---|---|---|
| Accords | ORTH-23 *Pluriel des adjectifs* | **ORTH-24** *Les accords dans le groupe nominal* |
| Conjugaison | ORTH-24 *(accords du GN — hors sujet)* | **ORTH-25** *L'accord du verbe avec son sujet* |
| Majuscules | GRAM-02 *Ponctuation* | **GRAM-09** *Noms communs et noms propres* |
| Orthographe | ORTH-01 *Le son [j]* | **ORTH-07** *Les lettres finales muettes* |
| Lexique | VOCA-03 *Mots de la même famille* | **VOCA-07** *Les synonymes* |

Les 19 fiches de conjugaison (CONJ-01 à CONJ-19), qui n'étaient reliées à rien,
sont maintenant dans la chaîne.

---

## 2. Les groupes de besoin partent vers Notes & Suivi

Le pont expose une nouvelle adresse, `/api/integrations/export/groupes`. Notes &
Suivi y trouve, à chaque synchronisation, un groupe de travail par difficulté
repérée :

```
· Accords        8 élève(s) · leçon FR-ORTH-ACC-01 · Les accords dans le groupe nominal
· Homophones     6 élève(s) · leçon FR-ORTH-HOM-01 · Les homophones grammaticaux
· Conjugaison    5 élève(s) · leçon FR-CONJ-PRES-01 · Le verbe et son sujet
```

Chaque groupe transporte ses élèves, l'effectif, la remédiation conseillée, la
procédure et la leçon rattachée. **Vos ateliers arrivent tout constitués** dans
Notes & Suivi ; vous n'avez plus à les recréer à la main.

Les groupes sont aussi dans l'export JSON de secours (bouton « Exporter en JSON »).

---

## 3. Les élèves ne peuvent plus accéder qu'à leur module

**Paramètres → ⚙️ Réglages → 🔒 Espace élève : ce que chacun peut ouvrir.**

Trois protections, indépendantes l'une de l'autre.

### a) Sortir de l'espace élève

Une case **« Verrouiller l'espace élève »**. Une fois cochée :

- le bouton « Changer d'élève » **disparaît** de la barre de gauche ;
- à la place, un bouton **« 👋 J'ai fini ma séance »**, qui demande confirmation
  puis ramène à la liste des prénoms pour l'élève suivant ;
- le bouton « Espace enseignant » porte un **cadenas 🔒** et exige votre code.

**Important** : le verrou ne protège que s'il existe un code enseignant. Si vous
cochez la case sans code défini, l'application vous propose immédiatement d'en
créer un, et affiche un avertissement orange tant que ce n'est pas fait.

### b) Voir les données d'un autre élève

Un élève connecté ne voit que ses propres résultats et sa propre banque de mots.
Pour changer d'élève, il faut passer par l'écran de sortie explicite ci-dessus —
il n'y a plus de retour arrière discret.

### c) Ouvrir une activité non autorisée

Vous cochez les activités ouvertes — **Je me corrige**, **Je lis à voix haute**,
**Ma banque de mots** — d'abord globalement, puis **classe par classe** dans un
tableau d'exceptions. Une activité fermée :

- n'apparaît pas dans le menu de gauche de l'élève ;
- n'apparaît pas comme tuile sur son écran d'accueil ;
- **reste inatteignable même en forçant la navigation** : c'est le serveur qui
  décide, pas la page affichée. Un élève débrouillard ne peut pas contourner.

*Exemple d'usage : la semaine de l'évaluation de fluence, vous n'ouvrez que
« Je lis à voix haute » pour les CM2, et laissez tout ouvert pour les CM1.*

---

## 4. L'aide ne pose plus de question inutile

C'était votre remarque la plus fine, et elle change beaucoup de choses.

Avant, devant « souvan », l'application demandait *« Connais-tu un mot de la même
famille ? »*. Or il n'y en a pas : le **t** de « souvent » ne se déduit d'aucune
règle. L'élève cherchait pour rien, et se décourageait.

L'application classe maintenant chaque erreur d'orthographe en trois cas, et le
**dit franchement à l'élève** dans un bandeau coloré :

| Cas | Bandeau affiché | Question posée |
|---|---|---|
| 🌳 **Ça se retrouve** (grand, bruit, chant…) | « Ce mot, tu peux le retrouver — sa lettre muette s'entend dans un mot de la même famille » | « Connais-tu un mot de la même famille que… ? » puis l'indice *« Pense à grandeur »* |
| 🧠 **Ça ne se devine pas** (souvent, toujours, beaucoup…) | « **Ce mot ne se devine pas** — aucune règle ne permet de le retrouver : il faut le savoir, ou aller le vérifier » | « Es-tu sûr(e) de savoir comment il s'écrit, ou faut-il aller le vérifier ? » |
| ✏️ **C'est un accent** (ecole → école) | « C'est une question d'accent — le mot est bon, seul l'accent doit changer » | « Les accents sont-ils bien placés ? » |

L'application connaît une centaine de mots invariables et une soixantaine de mots
à famille repérable. Pour tout mot non répertorié se terminant par une consonne
muette, elle choisit la prudence : elle dit « il faut le vérifier » plutôt que de
promettre une famille qu'elle serait incapable de fournir.

**Quand l'IA est active**, la consigne lui est transmise explicitement : interdit
de demander un mot de la même famille sur un mot qui n'en a pas, interdit de poser
une question dont la réponse ne peut pas mener à la correction.

---

## 5. Un bouton « Voir la leçon » quand c'est pertinent

Dans l'aide, sous les pistes, un **grand bouton bleu pleine largeur** :
*📘 Voir la leçon : Les lettres finales muettes*.

Il n'apparaît que si une fiche du classeur correspond vraiment au cas, et **la
leçon proposée s'adapte au diagnostic** :

- mot qui ne se devine pas → **ORTH-12** *Les mots invariables* ;
- lettre muette retrouvable → **ORTH-07** *Les lettres finales muettes* ;
- problème d'accent → **ORTH-11** *Les accents* ;
- sinon → la leçon principale de la catégorie.

---

## 6. Les leçons du classeur sont enfin lisibles

Vos fiches sont dessinées au format carte A7 (7,4 cm de large) : à l'écran,
c'était minuscule.

La fenêtre de consultation a été refaite : **fenêtre élargie à 1000 px**, fiche
**agrandie à 180 % par défaut**, et un réglage **− / +** en haut à droite
(*Taille du texte : 180 %*), de 100 % à 340 % par pas de 20 %. Le cadre grandit
avec le zoom pour ne rien couper ; au-delà, il défile.

Le réglage est **mémorisé d'une fiche à l'autre** dans la séance. Même
visionneuse côté élève et côté enseignant (écran Classeur).

---

## 7. Plus de place pour les textes

Trois changements :

- **La zone de texte grandit avec son contenu.** Quand l'élève augmente la
  police avec `A+`, la zone s'agrandit d'autant : le texte n'est plus coupé.
- **Plafond raisonnable** à 62 % de la hauteur de l'écran, pour que les boutons
  du bas restent visibles. Au-delà, une barre de défilement apparaît — jamais de
  texte perdu, exactement comme vous le demandiez.
- **Le panneau d'aide se resserre** (340 px → 300 px) au profit du texte, et
  **passe entièrement au-dessus du texte** sur écran étroit (moins de 1150 px,
  cas des Chromebooks) plutôt que d'étrangler la zone d'écriture.

---

## Pour lancer / reconstruire

- **Essayer tout de suite** : double-cliquez sur `lancer.bat`.
- **Refaire le .exe** : double-cliquez sur `build_exe.bat`, attendez 3 à 6
  minutes ; le fichier apparaît dans `dist\CorrecteurPedagogique.exe`.

Aucun fichier supplémentaire n'est à ajouter au build.

---

## Où régler quoi

| Ce que vous voulez faire | Où aller |
|---|---|
| Verrouiller l'espace élève | Paramètres → Réglages → 🔒 Espace élève |
| Ouvrir/fermer une activité par classe | Paramètres → Réglages → 🔒 Espace élève |
| Créer ou changer le code enseignant | Paramètres → 🔐 Sécurité & données |
| Envoyer les groupes vers Notes & Suivi | Paramètres → 🔗 Notes & Suivi |
| Consulter une leçon en grand | Classeur (menu de gauche) |
