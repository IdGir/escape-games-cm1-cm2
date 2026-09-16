# Ce qui a changé — Phase J5 : le dictionnaire par consonance

93 tests automatiques passés sur l'interface réelle, aucun échec.

---

## Le problème que ça résout

Un dictionnaire papier suppose qu'on sache **déjà** écrire le mot. C'est
exactement ce qui manque à l'élève qui le cherche. Il veut écrire *éléphant*,
il tente *éléfan*, il cherche à la lettre E… et ne trouve rien.

Ici, il écrit le mot **comme il l'entend**, et l'application lui propose les
mots qui **sonnent pareil**, du plus probable au moins probable. Il clique,
il lit les définitions, **et c'est lui qui tranche**. L'application ne corrige
pas : elle présente les possibilités.

---

## Comment ça marche

### Le moteur phonétique (`phonetique.py`)

Il traduit une suite de lettres en une suite de **sons**. Deux mots qui se
prononcent pareil obtiennent le même code, quelle que soit leur orthographe :

| L'élève écrit | Code | Le mot juste | Code |
|---|---|---|---|
| éléfan | `ELEF2` | éléphant | `ELEF2` |
| oizo | `WZO` | oiseau | `WZO` |
| ortografe | `ORTOGRAF` | orthographe | `ORTOGRAF` |
| mézon | `MEZ3` | maison | `MEZ3` |
| kestion | `KESI3` | question | `KESI3` |

Il gère les nasales (an/en/on/in), les groupes de voyelles (eau, ou, oi, ai),
les consonnes composées (ch, ph, gn, qu), le *l* mouillé (travail, grenouille),
les lettres finales muettes, le *h* toujours muet, et une trentaine
d'exceptions françaises célèbres (femme, monsieur, oignon, automne, second…).

Le classement est **indulgent sur les sons que l'oreille confond** — é/i, o/u,
s/z, f/v, k/g, t/d, p/b — parce qu'un enfant qui hésite hésite justement là.

### La base de mots (`data_dictionnaire.txt`)

**70 501 mots français**, extraits du *Dictionnaire orthographique français
« classique » v7.0* d'Olivier R. (grammalecte.net), sous licence MPL 2.0.
Chaque mot est stocké avec :

- sa **nature** (nom masculin, nom féminin, adjectif, verbe, adverbe…) ;
- ses **codes phonétiques**, y compris ceux de ses formes courantes
  (*cheval* connaît aussi le son de *chevaux*, les verbes connaissent leurs
  formes conjuguées les plus écrites) ;
- son **rang de fréquence**, en 4 niveaux.

Ce dernier point est décisif. Sans lui, *abacule* sortirait devant *bateau*.
Le rang est établi à partir d'une liste de 811 mots du vocabulaire de base du
cycle 3, complétée automatiquement par **tout le vocabulaire de vos 70 leçons
et des textes fournis** — un signal de fréquence gratuit et parfaitement
adapté à votre classe.

Résultat : **le bon mot sort en première position** dans tous les cas testés,
en moins de 5 millisecondes.

---

## Ce que voit l'élève

### L'écran « 🔎 Mon dictionnaire »

Un grand champ de saisie, avec la consigne : *« Écris le mot comme tu
l'entends »*. La recherche se lance toute seule pendant la frappe.

Les résultats arrivent en liste numérotée, du plus probable au moins probable.
Chaque ligne montre **le mot, sa nature, une jauge de probabilité**, et une
étiquette verte **« même son »** pour les mots qui se prononcent exactement
comme ce qu'il a écrit.

Si le mot tapé existe déjà, un bandeau vert le dit :
*« ✅ éléphant existe et s'écrit bien comme ça. »*

### La définition, au clic

C'est le cœur du dispositif : **sans définition, l'élève ne peut pas choisir**
entre *ver*, *vers*, *verre*, *vert* et *vair* — qui sortent tous les cinq.

La définition vient de trois sources, dans cet ordre :

1. **la mémoire de l'application** — une définition obtenue une fois n'est
   jamais redemandée ;
2. **la banque intégrée** — 130 définitions écrites pour des enfants, portant
   précisément sur les mots que l'on confond (les homophones) ;
3. **l'IA**, si vous en avez activé une — et le résultat est mémorisé pour
   toute la classe.

**Même sans définition et sans IA**, l'élève n'est jamais laissé sans rien :
il voit **la nature du mot** (nom masculin, adjectif…) et **les mots de la même
famille**. C'est souvent suffisant pour trancher, et c'est cohérent avec la
leçon *Les lettres finales muettes* de votre classeur.

Deux boutons complètent la fiche : **🎒 Ajouter à ma banque de mots** et
**⧉ Copier le mot**.

---

## L'appel depuis « Je me corrige »

Quand l'élève clique sur une erreur d'**orthographe, d'homophone, de lexique ou
de segmentation**, un bouton apparaît sous l'aide :
**🔎 Chercher ce mot dans le dictionnaire**.

Le dictionnaire s'ouvre **en fenêtre, sans quitter son texte**, pré-rempli avec
le mot qu'il a écrit. Quand il a lu les définitions et choisi, un bouton
**« ✓ C'est ce mot-là, je l'utilise »** pose le mot à la place du mot fautif,
directement dans son texte. Le repérage se met à jour aussitôt.

Ce recours au dictionnaire est **compté comme une aide** dans le score
d'autonomie : c'est un outil, pas un raccourci gratuit.

Le bouton n'apparaît pas sur les erreurs d'accord, de conjugaison, de
ponctuation ou de majuscule — un dictionnaire n'y sert à rien.

---

## Ce que ça apporte à l'enseignant

Nouvel écran, depuis le tableau de bord : **🔎 Mots cherchés**.

Les mots qu'un élève cherche au dictionnaire sont une information rare : ce
sont ceux dont il **doute**. Ils n'apparaissent pas dans une dictée surveillée,
mais ils le bloquent en rédaction.

Trois listes, en nuages de mots :

- **📖 Les mots retenus** — il a cherché, lu la définition, et choisi. Avec le
  nombre de fois.
- **🤔 Les essais sans choix** — il a cherché mais n'a ouvert aucune
  définition : le mot lui a échappé.
- **❌ Les essais sans aucun résultat** — l'orthographe tentée était trop
  éloignée. **Ces mots-là méritent une leçon** : l'élève ne s'en approche même
  pas à l'oreille.

Plus le détail des dernières recherches, avec l'élève, ce qu'il a écrit, ce
qu'il a retenu, et s'il venait du dictionnaire ou de « Je me corrige ».

---

## Réglages

Le dictionnaire est une activité comme les autres : **Paramètres → Réglages →
🔒 Espace élève** permet de l'ouvrir ou de le fermer, globalement ou classe par
classe. Utile en évaluation.

---

## Pour reconstruire l'exe

`build_exe.bat` a été mis à jour pour embarquer `data_dictionnaire.txt`.
Double-cliquez dessus, attendez 3 à 6 minutes ; le fichier apparaît dans
`dist\CorrecteurPedagogique.exe`. L'exe grossit d'environ 2,4 Mo.

---

## Fichiers ajoutés

| Fichier | Rôle |
|---|---|
| `phonetique.py` | Le moteur « comment ça sonne » |
| `dictionnaire.py` | La recherche, les familles de mots, les définitions |
| `data_dictionnaire.txt` | Les 70 501 mots (MPL 2.0, voir l'en-tête du fichier) |
| `web/js/dico.js` | L'écran élève et la fenêtre appelée depuis Je me corrige |

La base de données se met à jour toute seule au premier lancement (migration
v4 : mémoire des définitions et journal des recherches).

---

## Idées d'activités à rattacher, si vous voulez aller plus loin

Par ordre de rapport utilité / effort, selon moi :

1. **La dictée qui s'adapte** — l'application fabrique une courte dictée à
   partir des mots que CET élève rate le plus (sa banque de mots) et de ceux
   qu'il a cherchés au dictionnaire. Tout existe déjà : les mots, le moteur
   phonétique pour comparer ce qu'il tape, et le suivi. C'est le prolongement
   le plus naturel.
2. **La chasse aux mots** — un texte s'affiche, l'élève doit y retrouver tous
   les mots d'une catégorie (tous les verbes, tous les noms propres). La
   nature de chaque mot est déjà dans le dictionnaire.
3. **L'atelier d'écriture guidée** — une amorce de texte, une contrainte
   (« emploie trois mots de ta banque »), et le passage direct en correction.
4. **La lecture à deux voix** — pour la fluence : le texte alterne deux
   couleurs, l'élève lit une couleur, l'adulte l'autre. Très efficace sur les
   lecteurs fragiles, et le module de fluence existe déjà.
5. **Le passeport de leçons** — l'élève valide une leçon du classeur quand il
   a réussi trois textes sans erreur de la catégorie correspondante. Cela
   donnerait un sens progressif au classeur.

Dites-moi si l'une d'elles vous intéresse.
