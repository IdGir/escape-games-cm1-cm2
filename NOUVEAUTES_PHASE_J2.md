# Ce qui a changé — Phase J2

Toutes les modifications demandées ont été appliquées. Rien n'a été supprimé :
les écrans qui disparaissent du menu sont simplement rangés ailleurs.

---

## 1. Le menu de gauche est passé de 11 à 6 entrées

| Avant | Maintenant |
|---|---|
| Tableau de bord | **Tableau de bord** |
| Pilotage fin | → bouton **📈 Pilotage fin** en haut du tableau de bord |
| Fiche élève | → s'ouvre en cliquant une ligne de **Synthèse par élève** |
| Remédiation | **Remédiation** |
| Devoirs | **Devoirs** |
| Banques de textes | **Banques de textes** |
| Classeur | **Classeur** |
| Classes & élèves | → onglet de **⚙️ Paramètres** |
| Réglages | → onglet de **⚙️ Paramètres** |
| Sécurité & données | → onglet de **⚙️ Paramètres** |
| Notes & Suivi | → onglet de **⚙️ Paramètres** |

Le nouvel écran **Paramètres** contient quatre onglets en haut :
🏫 Classes & élèves · ⚙️ Réglages · 🔐 Sécurité & données · 🔗 Notes & Suivi.

Le pilotage fin et la fiche élève ont chacun un bouton
**« ← Retour au tableau de bord »** en haut à gauche.

---

## 2. Une statistique de lecture enfin utile

Le graphique **« Fluence moyenne par niveau (de texte) »** a été supprimé : il
mesurait surtout la difficulté du texte tiré au sort, pas les élèves.

Il est remplacé par **« Lecture : situation des élèves »**, qui répond à la vraie
question — *qui a besoin d'aide en lecture ?* Les élèves sont répartis en quatre
groupes par rapport au repère de leur niveau de classe (90 mots/min en CM1,
110 en CM2) :

- 🟢 **Au-delà** du repère (110 % et plus)
- 🔵 **Repère atteint** (90 à 110 %)
- 🟠 **Fragile** (75 à 90 %)
- 🔴 **En difficulté** (moins de 75 %)

Sous le graphique, deux indicateurs de progression : combien d'élèves progressent,
et le gain moyen en mots/minute entre la première et la dernière lecture.

---

## 3. Fiche élève : les deux modules ne sont plus mélangés

La fiche est découpée en trois blocs bien distincts, chacun avec sa couleur :

- **📝 Je me corrige — écriture** (bandeau bleu) : % corrigé, % sans aide,
  erreurs par catégorie, progression séance après séance.
- **📖 Je lis à voix haute — fluence** (bandeau cyan) : MCLM dernier, record,
  moyenne, courbe de progression avec la ligne du repère.
- **🩺 Besoins de suivi** (bandeau orange).

---

## 4. Une fiche d'exercice en face de chaque besoin

Dans la fiche élève **et** dans l'écran Remédiation, chaque besoin détecté
affiche maintenant son bouton d'impression **dans le même cadre**, à droite du
diagnostic. Le type de fiche s'adapte automatiquement au besoin :

| Besoin détecté | Bouton proposé |
|---|---|
| Erreurs d'une catégorie (accord, homophone…) | 🖨️ Fiche d'exercice ciblé |
| Fluence insuffisante | 🖨️ Fiche de lecture répétée |
| Autonomie faible | 🖨️ Fiche méthode de relecture |

Une quatrième carte, en bas de la fiche élève, permet de générer une fiche sur
**n'importe quelle catégorie**, même sans alerte, avec le nombre de phrases voulu.

---

## 5. Remédiation : les groupes de besoin passent en vedette

Les groupes ne sont plus une petite liste : ce sont désormais de **grandes cartes
colorées** placées tout en haut de l'écran, une par catégorie, avec :

- le bandeau de couleur de la catégorie et l'effectif dans une pastille,
- les prénoms des élèves concernés en étiquettes lisibles,
- un bouton **« 🖨️ Fiche d'exercice ciblé pour ce groupe »** — la fiche est alors
  éditée au nom du groupe, prête pour l'atelier.

Le détail élève par élève vient ensuite, les besoins prioritaires en premier
(marqués **PRIORITAIRE** en rouge).

---

## 6. Les fiches imprimables ont été entièrement redessinées

Fini la page Georgia en noir et blanc. Chaque fiche comporte maintenant :

- un **bandeau coloré** repris de la couleur de la catégorie travaillée, avec
  l'icône, le titre, et les cases *Nom* / *Date* (ou *Groupe* / *Date*) ;
- un encadré **« Ce qu'il faut regarder »** : le rappel de la règle, écrit pour
  l'élève, avant même le premier exercice ;
- deux ou trois **astuces** en pastilles (les procédures de vérification) ;
- des **exercices numérotés dans des pastilles rondes**, avec une vraie ligne
  d'écriture sous chaque phrase ;
- une bande d'**auto-évaluation** en bas (🙂 😐 🙁) ;
- le **corrigé enseignant sur une page séparée**, en vert, avec l'indice de
  chaque phrase.

Trois formats existent :

1. **Fiche d'exercices** (les 8 catégories) ;
2. **Fiche de lecture répétée** : un texte tiré de votre banque de fluence, trois
   cases chronométrées (passage 1, 2, 3) et l'objectif en mots/minute ;
3. **Fiche méthode de relecture** : les 5 passages de relecture, chacun avec sa
   case à cocher.

Un bandeau noir en haut de l'écran propose le bouton **🖨️ Imprimer / PDF**
(il ne s'imprime pas, lui).

---

## 7. Tout texte généré arrive avec un titre

Chaque texte fabriqué par l'application reçoit automatiquement un **titre en
rapport avec son contenu** — par exemple *« Les élèves rangent leurs cahiers »* —
que vous pouvez modifier avant d'enregistrer.

Un bouton **✨ Proposer un titre** est aussi disponible dans l'éditeur, pour les
textes que vous écrivez ou collez vous-même.

*Le titre est proposé par l'IA si elle est active ; sinon l'application le
fabrique elle-même, hors ligne, à partir de la première phrase.*

---

## 8. Créer plusieurs textes d'un coup

**Banques de textes → Textes à corriger → ⚡ Générer plusieurs textes…**

Vous indiquez : combien de textes (jusqu'à 30), combien de phrases par texte, et
le niveau. L'application fabrique le tout — texte, corrigé et titre — et
l'enregistre directement dans la banque.

Un compteur rappelle en permanence la taille de votre banque, avec un conseil
tant qu'elle compte moins de 15 textes.

---

## 9. Textes de fluence : génération en lot **et** extraits littéraires

**Banques de textes → Textes de fluence**, deux nouveaux boutons :

- **⚡ Générer plusieurs textes…** — des textes courts inventés, sans erreur.
- **📖 Chercher des extraits littéraires…** — l'IA va chercher des extraits
  d'œuvres de **littérature de jeunesse du domaine public** (La Fontaine,
  Perrault, Comtesse de Ségur, Hector Malot, Jules Verne, Andersen, Selma
  Lagerlöf…), adaptés à des élèves de 9 à 11 ans.

**Rien n'est enregistré sans vous.** Une fenêtre affiche chaque proposition avec
son titre modifiable, sa source (œuvre + auteur) et son texte modifiable, chacune
avec une case à cocher. Vous décochez ce que vous ne voulez pas, puis
« Ajouter les textes cochés ».

*Sans IA active, l'application puise dans sa propre sélection de 10 extraits
classiques du domaine public — la fonction marche donc toujours, même hors ligne.*

---

## 10. Module élève

### Page d'accueil : plus aucune liste déroulante

Grand titre dégradé, puis deux étapes numérotées :

1. **Ma classe** — de grandes cartes cliquables (🏫 nom de la classe + effectif).
2. **Mon prénom** — dès que la classe est choisie, les prénoms apparaissent en
   dessous sous forme de **boutons avec l'initiale dans un rond de couleur**.

L'élève clique deux fois et il est entré. Un lien *« ← changer de classe »*
permet de revenir en arrière. S'il n'y a qu'une seule classe, les prénoms
s'affichent directement.

### Bilan de « Je me corrige » : beaucoup plus lisible

- Le message de félicitations passe en **38 px**, suivi d'une **grande jauge
  verte animée** indiquant le pourcentage d'erreurs corrigées.
- Trois **grands cadres colorés** avec des chiffres en 76 px :
  *Erreurs au départ* (rouge) **→** *J'ai corrigé* (vert) · *Il reste* (orange).
- Les indicateurs secondaires (sans aide, indices, temps) passent en dessous,
  en plus petit.
- Les catégories deviennent des **cartes colorées** en grille, avec le passage
  `avant → après` en gros et une mention *« ✅ tout corrigé »* ou
  *« 👍 3 corrigée(s) »*.

---

## Vérifications effectuées

38 tests automatiques ont été passés sur l'interface réelle (menu, navigation,
onglets, boutons de fiche, propositions de textes, accueil élève) : **tous
réussis**. Les trois formats de fiche ont été générés et contrôlés.

---

## Pour lancer / reconstruire

- **Essayer tout de suite** : double-cliquez sur `lancer.bat`.
- **Refaire le .exe** : double-cliquez sur `build_exe.bat`, attendez 3 à 6
  minutes ; le fichier apparaît dans `dist\CorrecteurPedagogique.exe`.

Aucun nouveau fichier à ajouter au build : les nouveautés sont dans des fichiers
déjà pris en compte.
