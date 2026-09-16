# Ce qui a changé — Phase J10

189 tests automatiques passés sur l'interface réelle, aucun échec.

---

## 1. Le dictionnaire : non, ce n'était pas l'IA — c'était moi

Votre exemple était parfait : **« écureur » donné comme famille d'« écureuil »**.

La cause n'a rien à voir avec l'IA. Ma fonction comparait simplement les
**débuts de mots** : elle prenait les 6 premières lettres d'« écureuil »
(« écureu ») et retenait tout mot commençant pareil. « écureur » passait.

C'est corrigé par une vraie analyse morphologique. Un mot n'est de la famille
d'un autre que si :

1. il commence par un **radical** du mot de départ (au moins 4 lettres),
2. et que ce qui suit est un **vrai suffixe de dérivation** français
   (-age, -eur, -ier, -ment, -tion, -able, -er, -ir…).

Les préfixes sont gérés aussi (dire → redire, dédire, prédire), mais avec la
même exigence.

**Résultat, et c'est le point important :** la liste est parfois vide.

| Mot | Avant | Maintenant |
|---|---|---|
| écureuil | écureur, écureuse… | *(aucune)* |
| sang | sanglier, sangle… | *(aucune)* |
| chant | — | chanter, chanteur, chantage |
| grand | — | grandir, agrandir, grandeur |
| bruit | — | bruitage, bruiter, bruiteur |
| froid | — | froidir, froideur, froidure |
| dire | — | dédire, redire, prédire |

**Mieux vaut ne rien proposer qu'une fausse famille** : l'élève s'en sert pour
retrouver une lettre muette. Une famille inventée l'envoie dans le mur.

---

## 2. Le bilan de dictée n'apparaissait pas — vraie erreur, trouvée

Le test « ce bilan est-il vide ? » ne regardait que les corrections et les
lectures. **Un élève qui n'avait fait que des dictées voyait donc un bilan
vide**, alors que tout était bien enregistré.

Corrigé : le bilan n'est déclaré vide que si l'élève n'a rien fait du tout —
ni correction, ni lecture, ni dictée, ni banque de mots. La section ✍️ et ses
badges apparaissent maintenant normalement.

---

## 3. Les modes de dictée sont dans l'ordre

Ils sortaient dans l'ordre alphabétique — expressions, mots, phrases — parce
que Flask trie les clés JSON par défaut. Désactivé : l'ordre pédagogique
**mots → expressions → phrases** est respecté.

---

## 4. Les expressions ont maintenant une unité de sens

Vous aviez raison, c'était du ramassage de mots. J'extrayais tout ce qui suivait
un déterminant, sans vérifier ce que c'était.

Désormais l'application **vérifie la nature de chaque mot** dans le dictionnaire
embarqué et ne construit que de vrais groupes nominaux : *déterminant + nom
(+ adjectifs)*. Elle s'arrête net dès qu'apparaît un verbe, une préposition, une
conjonction ou un adverbe.

Avant : « des tomates bien », « la maison et », « un joli »
Après : *un joli chapeau · des légumes frais · un chocolat chaud · des
chaussures solides · le grincement familier · des formes géométriques*

Ce ne sont plus ni des phrases, ni des débuts de phrases.

---

## 5. Une banque de dictées, comme pour les textes

**Banques de textes → Dictées.** Trois onglets (Mots, Expressions, Phrases),
chacun avec ses trois niveaux et son compteur.

Deux façons de la remplir :

- **✨ Fabriquer avec l'IA** — nombre, niveau, thème facultatif. L'IA reçoit
  une consigne stricte selon le mode : formes de base uniquement pour les mots,
  unité de sens obligatoire pour les expressions, phrases complètes avec verbe
  conjugué pour les phrases. **Vous validez chaque proposition** avant
  enregistrement.
- **➕ Ajouter à la main** — un élément par ligne.

Un filtre automatique écarte ce qui ne respecte pas le format, même si l'IA se
trompe : un pluriel proposé en mode « mots » est rejeté, une phrase déguisée en
expression aussi.

**Ce que vous mettez dans la banque passe en premier** dans les dictées des
élèves, avant les mots tirés de leurs erreurs. C'est votre choix pédagogique qui
prime.

---

## 6. « Je me corrige » : la mise en page reprise

### Le bandeau supérieur a disparu

Vous aviez raison, il faisait doublon avec le titre juste en dessous, pour
90 pixels de hauteur. Il est remplacé par une **frise fine intégrée au titre** :
cinq pastilles rondes (✓ pour les passages faits, le numéro pour les autres),
le titre du passage, et « passage 5 sur 6 » à droite. Le tout sur une ligne.

### Plus rien ne semble décalé

C'était le vrai défaut visible sur votre capture : le cadre du texte s'arrêtait
haut, avec un grand blanc en dessous, pendant que la colonne de droite
continuait.

La cause : la colonne de droite était plus haute que le texte, et la grille
prenait la hauteur de la plus grande.

Corrigé : **la zone de texte s'étend maintenant jusqu'au bas de la colonne de
droite**. Les deux colonnes se terminent à la même hauteur, et l'aide s'ouvre
juste en dessous, sans blanc intermédiaire.

### Le dictionnaire accessible directement

Un bouton **🔎 Ouvrir le dictionnaire** apparaît dans l'encart du passage dès
que celui-ci porte sur l'orthographe, le lexique, les homophones ou la
segmentation. L'élève n'a plus besoin de cliquer d'abord sur une erreur.

---

## 7. Les graphiques du bilan : le bon compromis

Trop grands, puis trop petits. Ils sont maintenant à **640 px de large et
250 px de haut** (700 px sur grand écran) : assez pour se lire confortablement,
assez sobres pour garder la vue d'ensemble du bilan.

---

## 8. L'impression par défaut : 24 étiquettes

La planche proposée d'office est désormais **Avery L7159 — 24 par feuille,
3 colonnes × 8 lignes** (63,5 × 33,9 mm). Les dix autres références restent
disponibles dans la liste.

---

## Récapitulatif des corrections

| Point signalé | État |
|---|---|
| Cadres décalés dans Je me corrige | ✅ colonnes alignées en bas |
| Bandeau supérieur en doublon | ✅ remplacé par une frise fine |
| Dictionnaire à l'étape orthographe | ✅ bouton dans l'encart du passage |
| Familles de mots hasardeuses | ✅ analyse morphologique réelle |
| Graphiques du bilan trop petits | ✅ 640 × 250 px |
| Ordre des modes de dictée | ✅ mots → expressions → phrases |
| Banque de dictées par l'IA | ✅ trois modes, validation obligatoire |
| Bilan de dictée absent | ✅ bug trouvé et corrigé |
| Expressions sans unité de sens | ✅ vrais groupes nominaux vérifiés |
| Étiquettes : planche de 24 par défaut | ✅ Avery L7159 (3 × 8) |

Migration v8 automatique au premier lancement (banque de dictées).
`build_exe.bat` : rien à changer.

---

## Un point de méthode, pour la suite

Le défaut des familles de mots et celui du bilan vide ont un point commun :
**ils ne se voyaient qu'à l'usage**, avec de vraies données. Mes tests
automatiques vérifiaient que les fonctions répondaient, pas que leurs réponses
avaient du sens.

J'ai ajouté des tests qui vérifient maintenant le **contenu** : qu'« écureur »
n'est plus parent d'« écureuil », que « chanter » l'est bien de « chant », et
qu'un élève n'ayant fait que des dictées voit son bilan. Continuez à me signaler
ce genre de choses — ce sont les plus utiles.
