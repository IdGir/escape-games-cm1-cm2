# Ce qui a changé — Phase J11

204 tests automatiques passés sur l'interface réelle, aucun échec.

---

## 1. Dix textes, dix titres identiques — cause trouvée

Le réglage ne proposait **qu'un seul thème à la fois**. Vos dix textes parlaient
donc tous du même sujet, et l'IA leur donnait logiquement le même titre.

Trois corrections :

- **Les thèmes se cochent maintenant en nombre libre** (voir point 2), et la
  génération en lot **les fait tourner** : texte 1 sur le thème A, texte 2 sur
  le thème B, et ainsi de suite.
- **Un contrôle d'unicité** garantit qu'aucun titre ne se répète dans la banque.
  Si un titre existe déjà, il est complété par un mot marquant du texte
  (« Le chat de la voisine — muret ») et, en dernier recours seulement, par un
  numéro.
- **Bug annexe corrigé** : « sœur » devenait « s ur » dans les titres. Le œ ne
  faisait pas partie des lettres reconnues.

Vérifié : dix textes produisent bien **dix titres différents**.

---

## 2. Les thèmes se cochent, autant qu'on veut

**Paramètres → Réglages → Thèmes des textes générés.**

Les douze thèmes sont désormais des cases à cocher, avec **☑ Tout cocher** et
**☐ Tout décocher**. Un compteur indique combien sont retenus.

En dessous, une zone libre permet d'ajouter **vos propres thèmes**, un par
ligne — ils s'ajoutent aux cases cochées.

---

## 3. L'interface gagne 62 pixels de hauteur

La bande du haut répétait le titre de la page juste en dessous. **Elle a
disparu.** Les deux boutons (⚙️ réglages et 🌙 clair/sombre) flottent maintenant
au niveau du titre, en haut à droite.

C'est autant de gagné sur tous les écrans de l'application.

---

## 4. « Je me corrige » : la disposition demandée

| Élément | Emplacement |
|---|---|
| Frise des passages + titre + **bouton « Passage suivant »** | une seule ligne, en tête |
| **Erreurs corrigées** / **Erreurs à corriger** | bandeau **au-dessus du texte**, en cadres bas |
| **Zones à revoir** (passage en cours) | colonne de droite |
| **L'aide** | sous le texte, sur toute la largeur |

Les deux compteurs sont passés en format horizontal compact : le grand chiffre
à gauche, le titre et les étiquettes à droite. Ils occupent deux fois moins de
hauteur qu'avant.

Dans l'aide, les boutons **📘 Voir la leçon**, **🔎 Chercher ce mot**,
**📖 Tableaux de conjugaison** et **🆘 J'ai encore besoin d'un indice** sont
maintenant **sur une seule ligne**.

Le bouton d'avancement n'apparaît plus qu'une fois, sur la ligne du titre.

---

## 5. Le dictionnaire s'ouvre plus bas et se déplace

Appelé depuis « Je me corrige », il s'ouvre désormais **dans la moitié basse de
l'écran**, de sorte que le texte de l'élève reste visible au-dessus.

Et il est **déplaçable** : la zone du titre porte la mention *✥ déplaçable*, et
l'élève peut le faire glisser où il veut, à la souris ou au doigt. Le fond est
moins sombre pour que le texte reste lisible derrière.

---

## 6. Le bilan : chiffres à côté du graphique

En écriture comme en lecture, les trois chiffres passent **en colonne à gauche**
et le graphique occupe la place restante à droite — il est donc **plus grand**
(280 px de haut) tout en tenant sur la même hauteur d'écran.

Le **nombre de mots gagnés est arrondi**.

---

## 7. Les fiches deviennent des documents de suivi

### Renommage

« Fiche d'exercice ciblé » devient **« Fiche de remédiation »**. Le bandeau
affiche « Remédiation · Étude de la langue » au lieu de « Fiche ciblée ».

### Plus aucune mention de génération automatique

L'ancien pied de page disait « fiche générée automatiquement à partir des
besoins repérés dans l'application ». Il devient :

> **Remédiation individualisée — établie d'après le suivi des séances.**
> Vu par l'enseignant : \_\_\_\_\_\_  Vu par la famille : \_\_\_\_\_\_

### Les références nécessaires

Le bandeau porte maintenant, en clair :

- **Élève** (ou **Groupe**) et son nom ;
- **Date**, avec sa ligne à remplir ;
- **Domaine** : Étude de la langue, Lecture, Méthodologie, Orthographe lexicale ;
- **Objectif pédagogique** en sous-titre : *« Repérer le donneur d'accord et
  accorder le groupe nominal »*, *« Identifier le sujet et accorder le verbe »*… ;
- **Référence** de la leçon du classeur (ORTH-24, GRAM-02…).

### Le document enseignant refait

La page réservée à l'enseignant s'appelle désormais **« Corrigé et grille
d'observation »**. Elle porte les mêmes références (élève, date, leçon) et
ajoute :

- **deux cases à cocher par item** — vert « réussi », orange « à retravailler » ;
- un **cadre d'observations** avec trois lignes ;
- un total **items réussis \_\_ / 6** et une ligne **suite à donner**.

De quoi ranger la fiche dans un dossier de suivi et la comparer d'une séance à
l'autre.

---

## 8. Les groupes de besoin couvrent lecture et dictée

Jusqu'ici, seules les erreurs écrites formaient des groupes. Trois nouveaux
besoins constituent désormais des groupes à part entière :

| Groupe | Déclenché par |
|---|---|
| 🔵 **Fluence de lecture** | vitesse en retrait de plus de 25 % du repère |
| 🟠 **Orthographe sous dictée** | moins de 60 % de mots justes sur les 3 dernières |
| 🔴 **Discrimination auditive** | 4 mots ou plus non reconnus à l'oreille, et davantage d'erreurs d'écoute que d'orthographe |

Ce dernier mérite votre attention : il signale un élève qui **n'entend pas
correctement les mots**, ce qui n'est pas un problème d'orthographe. La
procédure proposée invite à faire répéter le mot avant l'écriture, et à
signaler au médecin scolaire si cela persiste.

Chaque groupe reçoit la fiche adaptée : **fiche de lecture répétée** pour la
fluence, **fiche de mémorisation** pour la dictée (tableau « je regarde, je
copie, j'écris de mémoire, je vérifie », rempli avec les mots de l'élève).

---

## Récapitulatif

| Point signalé | État |
|---|---|
| Dix textes, même titre | ✅ thèmes tournants + unicité garantie |
| Sélection multiple des thèmes | ✅ cases à cocher + thèmes personnels |
| Bilan : stats à côté du graphique | ✅ colonne à gauche, graphique agrandi |
| Mots gagnés non arrondis | ✅ arrondi |
| Dictionnaire trop haut, fixe | ✅ ouvert plus bas et déplaçable |
| Compteurs à replacer au-dessus | ✅ bandeau compact |
| Zones à revoir à droite | ✅ conservé |
| Aide en pleine largeur, boutons alignés | ✅ une seule ligne |
| Bouton suivant sur la ligne du titre | ✅ |
| Bande du haut en doublon | ✅ supprimée, boutons descendus |
| « Fiches ciblées » → « Remédiation » | ✅ |
| Mention de génération automatique | ✅ supprimée |
| Références sur la fiche enseignant | ✅ élève, date, domaine, objectif, leçon |
| Groupes de besoin : dictée et lecture | ✅ trois nouveaux groupes |

Aucune migration de base cette fois. `build_exe.bat` : rien à changer.
