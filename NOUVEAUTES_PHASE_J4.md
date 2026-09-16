# Ce qui a changé — Phase J4

71 tests automatiques passés sur l'interface réelle, aucun échec.

---

## 1. « Mon bilan » : l'élève voit enfin ses réussites

Nouvel onglet dans le menu de l'élève (et nouvelle tuile 🏆 sur son accueil).
Tout y est écrit pour un enfant de 9 à 11 ans, et **chaque chiffre est expliqué
en une phrase juste en dessous**. L'élève n'est jamais comparé aux autres :
seulement à lui-même, d'une semaine à l'autre.

### 🏆 Mes réussites — 9 badges à débloquer

| Badge | Comment l'obtenir |
|---|---|
| 🌱 Je me lance | Corriger un premier texte |
| 📚 Bon lecteur de mes textes | Corriger 5 textes |
| 🏅 Correcteur confirmé | Corriger 10 textes |
| ✨ Sans faute ! | Terminer un texte sans aucune erreur restante |
| 🎯 Je me débrouille seul | Corriger 6 erreurs sur 10 sans aide |
| 📖 Premier chrono | Faire une lecture chronométrée |
| 🚀 Je lis plus vite | Battre son premier score de lecture |
| 🏆 Objectif atteint | Lire 90 mots en une minute (repère CM1) |
| 🎒 Collectionneur de mots | Apprendre 10 mots difficiles |

Les badges obtenus sont **en vert avec leur emoji en couleur**. Les suivants
restent affichés en gris, avec **une petite jauge de progression** et le compte
exact (`7 / 10`) : l'élève voit toujours ce qui est à sa portée.

### 📝 Quand j'écris et je me corrige

Trois grands chiffres, chacun avec son explication :

- **textes corrigés** — « C'est le nombre de fois où tu es allé(e) au bout. »
- **erreurs réparées** — « Toutes tes corrections additionnées depuis le début. »
- **% trouvées tout(e) seul(e)** — « Sur 10 erreurs corrigées, tu en as trouvé 7
  sans aucune aide. »

Puis la courbe *« Mes corrections, texte après texte »*, avec sa légende :
« Chaque point est un texte. Plus le point est haut, plus tu as réparé
d'erreurs dans ce texte-là. »

### 📈 Ce que je réussis de mieux en mieux

L'application compare **les 3 derniers textes aux 3 précédents**, catégorie par
catégorie, et affiche `avant → maintenant` en gros. Les catégories en progrès
passent **en vert avec « 👏 tu en fais moins qu'avant »**. Tant qu'il n'y a pas
assez de textes pour comparer, elle le dit simplement au lieu d'inventer une
tendance.

Un bouton **📘 Revoir les leçons qui vont m'aider** conduit aux leçons du
classeur correspondant à ses trois difficultés du moment — **une seule leçon par
difficulté**.

### 📖 Quand je lis à voix haute

Une **jauge vers l'objectif** avec un message adapté : *« Mon meilleur score :
78 mots en 1 minute. Mon objectif : 90. Encore 12 mots et c'est gagné ! »* — ou
*« 🎉 Tu l'as déjà atteint, bravo ! »*. Plus le nombre de mots gagnés depuis la
première lecture, et la courbe avec la ligne d'objectif expliquée.

### 🎒 Ma banque de mots

Mots appris / mots à travailler, avec un bouton pour aller s'entraîner.

Un bouton **🖨️ Imprimer mon bilan** produit une version propre sur papier
(menus et boutons retirés) — utile pour le cahier ou pour la famille.

---

## 2. Les réussites sont fêtées au bon moment

À la fin d'une correction, si le texte vient de débloquer un badge, un **cadre
vert animé apparaît immédiatement** sous le bilan de séance :

> 🎉 **Nouvelle réussite débloquée !**
> ✨ **Sans faute !** — Terminer un texte sans aucune erreur

C'est le moment où l'élève est le plus réceptif. Un bouton conduit directement à
son bilan complet.

---

## 3. Les leçons sont vraiment agrandies (le défaut était réel)

Vous aviez raison : **seul le cadre grandissait**. Vos fiches sont dessinées
entièrement en millimètres, et j'appliquais l'agrandissement à un élément
(`.sheet`) qui n'existe pas dans ces fiches — le texte ne bougeait donc pas d'un
pixel.

C'est corrigé : l'agrandissement porte maintenant sur **la carte elle-même**, et
il **recalcule vraiment la mise en page** (les tailles en millimètres sont
converties), au lieu d'étirer une image.

- **Ouverture à 220 % par défaut**, partout : dans l'aide de « Je me corrige »
  **comme dans le Classeur** de l'enseignant.
- Réglage **− / +** de 140 % à 360 %, mémorisé d'une fiche à l'autre.
- La hauteur du cadre suit exactement la hauteur réelle de la carte : plus rien
  n'est coupé.
- Le trou de perforation et la marge de reliure, utiles à l'impression, sont
  masqués à l'écran — ils ne mangent plus la place.

---

## 4. Une seule leçon dans l'aide, et non plus cinq

Dans « Je me corrige », l'aide affichait **le bouton ciblé plus toute la liste
des fiches de la catégorie** — soit cinq ou six boutons. Demander à un élève de
choisir sa leçon, c'est le détourner de sa correction.

Il n'en reste **qu'une seule** : celle qui correspond exactement au cas
diagnostiqué (mot invariable → *Les mots invariables* ; lettre muette →
*Les lettres finales muettes* ; accent → *Les accents* ; sinon la leçon
principale de la catégorie).

---

## 5. Les questions s'appuient sur la phrase de l'élève

Une question générique ne dit pas **où regarder**. L'application repère
maintenant les mots voisins dans la phrase réellement écrite par l'élève, et
les cite.

| Phrase de l'élève | Avant | Maintenant |
|---|---|---|
| *Elle a mangé des pommes **rouge**.* | « le déterminant est-il au singulier ou au pluriel ? » | « **Dans ce groupe, il y a « des » : c'est du pluriel.** Alors, comment doit s'écrire « rouge » ? » |
| *Les enfants **joue** dans la cour.* | « Qui est-ce qui joue ? » | « Qui est-ce qui « joue » ? **C'est « Les enfants » : ils sont plusieurs.** Quelle terminaison faut-il ? » |
| *Tu **prend** ton cartable.* | « Remplace le sujet par il, elle… » | « Le sujet, c'est « Tu ». **Quelle terminaison le verbe prend-il avec « tu » ?** » |
| *Il va **a** l'école.* | « peux-tu le remplacer ? » | « **Ici, faut-il écrire « a » ou « à » ?** Comment le vérifier ? » |
| *je m'appelle paul.* | « début de phrase ou nom propre ? » | « **« je » ouvre la phrase.** Par quoi commence toujours une phrase ? » |
| *Nous habitons à **paris**.* | (même question) | « **« paris » : est-ce le nom d'une personne, d'une ville ou d'un pays ?** » |

Deux corrections de fond au passage : quand le sujet est **déjà un pronom**, on
ne demande plus de le remplacer par un pronom ; et pour un adjectif, on remonte
jusqu'au **déterminant qui commande le groupe**, même s'il est trois mots plus
tôt.

---

## 6. Côté enseignant : voir les réussites de l'élève

Sur la fiche d'un élève, un bouton **🏆 Voir les réussites telles que l'élève les
voit** ouvre exactement son tableau de badges, avec la progression vers ceux qui
restent. Pratique en entretien avec la famille : on part de ce qui est réussi.

---

## Pour lancer / reconstruire

- **Essayer tout de suite** : double-cliquez sur `lancer.bat`.
- **Refaire le .exe** : double-cliquez sur `build_exe.bat` (3 à 6 minutes) ;
  le fichier apparaît dans `dist\CorrecteurPedagogique.exe`.

---

## Deux réglages faciles à ajuster si besoin

| Ce que vous voulez changer | Où, dans quel fichier |
|---|---|
| Le zoom des leçons par défaut (220 %) | `web/js/noyau.js`, ligne `zoom: 2.2` |
| Les seuils des badges (5 textes, 10 textes, 10 mots…) | `api.py`, fonction `_badges` |
