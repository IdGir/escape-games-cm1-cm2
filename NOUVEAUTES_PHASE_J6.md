# Ce qui a changé — Phase J6 : la dictée qui s'adapte

116 tests automatiques passés sur l'interface réelle, aucun échec.

---

## L'idée

Une dictée de classe est la même pour tous : les uns s'ennuient, les autres
coulent. Celle-ci est fabriquée **à partir de ce que CET élève a réellement
raté**, dans cette application.

Trois sources, dans cet ordre :

1. **Sa banque de mots** — ceux qu'il rate en se corrigeant. Plus il a raté un
   mot, plus ce mot a de chances de sortir.
2. **Les mots qu'il a cherchés au dictionnaire** — ceux dont il *doute*. Ce
   sont souvent les plus intéressants : il ne les écrit jamais mal deux fois de
   la même façon, mais ils le bloquent.
3. **Sa difficulté du moment** — si sa banque est trop maigre, l'application
   complète avec des mots porteurs de sa catégorie d'erreur principale, puis
   avec du vocabulaire courant. La dictée est **toujours réalisable**, même au
   premier jour.

L'élève voit d'où viennent ses mots, écrit noir sur blanc :
*« Cette dictée contient 4 mots que tu rates souvent, 2 mots que tu as cherchés
au dictionnaire, 4 mots sur ta difficulté du moment. »*

---

## Comment ça se passe pour l'élève

### La voix

Chaque mot est **lu à voix haute** par la voix de Windows. Réglage de vitesse
avant de commencer (lente / normale / rapide), avec un bouton **🔊 Essayer**.
Le mot peut être réécouté autant de fois que voulu.

Quand une **phrase porteuse** existe — l'application la cherche dans vos textes
à corriger, vos textes de fluence et la banque d'exercices — un bouton
**💬 Écouter la phrase entière** la lit, puis répète le mot seul. Entendre un
mot en contexte fixe son sens et ses accords.

**Si aucune voix française n'est installée**, la dictée fonctionne quand même :
le mot s'affiche quatre secondes puis disparaît, à charge pour l'élève de le
réécrire de mémoire. C'est annoncé clairement, et l'adulte peut aussi lire.

### Le retour, immédiat

Après chaque mot, l'élève sait tout de suite. Et surtout, il sait **pourquoi**
c'est faux. C'est le cœur du dispositif :

| Ce qu'il a écrit | Diagnostic | Ce qu'on lui dit |
|---|---|---|
| *éléfan* pour **éléphant** | 🔤 **orthographe** | « Tu as bien entendu le mot : ça se prononce exactement comme ce que tu as écrit. C'est l'orthographe qui change. » |
| *ecole* pour **école** | ✏️ **accent** | « Il ne manque que les accents. Le reste du mot est juste. » |
| *chateau* pour **chapeau** | 🔍 **presque** | « Tu es tout près : un seul son ne va pas. Réécoute lentement, syllabe par syllabe. » |
| *voiture* pour **maison** | 👂 **écoute** | « Ce n'est pas le mot qui a été dicté. Réécoute-le attentivement. » |

Cette distinction est faite par le **moteur phonétique** construit en phase J5 :
il compare les *sons* du mot attendu et du mot écrit. Un élève qui écrit
*éléfan* n'a pas le même problème qu'un élève qui écrit *voiture* — et ce ne
sont pas les mêmes remédiations.

### Le bilan

Score en gros, message adapté au **type d'erreur dominant** :

> 💪 C'est en s'entraînant qu'on progresse. Tes erreurs sont surtout des erreurs
> d'orthographe : tu entends bien les mots, il faut maintenant retenir comment
> ils s'écrivent.

Puis la répartition des erreurs par type, et la liste mot par mot avec un
bouton **🔎 Voir ce mot** sur chaque erreur, qui ouvre le dictionnaire de la
phase J5 — définition, nature, famille de mots.

### Les effets

- Un mot **écrit juste** sort de la banque de mots (il est acquis).
- Un mot **raté** y entre ou y reste (il reviendra à la prochaine dictée).
- Deux nouveaux badges : **✍️ Première dictée** et **🎖️ Dictée sans faute**,
  fêtés à l'écran dès qu'ils sont débloqués.

---

## Ce que ça apporte à l'enseignant

La fiche élève gagne un bloc **✍️ Ma dictée** avec trois chiffres et, surtout,
une lecture pédagogique automatique :

- **% de mots justes** en moyenne ;
- **mots bien entendus mais mal écrits** ;
- **mots non reconnus à l'oreille**.

Et la conclusion qui va avec :

> *« Le repérage auditif est solide : le travail porte sur la mémorisation
> orthographique. »*

ou

> *« Beaucoup de mots ne sont pas reconnus à l'oreille : vérifier l'audition et
> la discrimination des sons. »*

Ce second message mérite votre attention : un élève qui accumule les erreurs
d'écoute peut avoir un souci auditif réel, et non un souci d'orthographe. C'est
le genre de signal qu'une dictée classique ne donne pas.

La courbe des scores complète le suivi. Tout remonte dans le bilan de l'élève.

---

## Réglages

**Paramètres → Réglages → 🔒 Espace élève** : la dictée s'ouvre ou se ferme
comme les autres activités, globalement ou classe par classe.

---

## Fichiers ajoutés

| Fichier | Rôle |
|---|---|
| `dictee.py` | Choix des mots, phrases porteuses, analyse des réponses |
| `web/js/dictee.js` | L'écran élève, la voix, le retour immédiat, le bilan |

La base de données se met à jour seule au premier lancement (migration v5 :
table des séances de dictée).

Aucun fichier supplémentaire à déclarer dans `build_exe.bat` cette fois.

---

## Une limite à connaître

La voix dépend de **Windows**, pas de l'application. Sur un poste sans voix
française installée, la dictée bascule en mode « le mot s'affiche puis
disparaît ». Pour installer une voix française sur Windows 11 :
*Paramètres → Heure et langue → Voix → Ajouter des voix → Français (France)*.

Cela vaut la peine de le vérifier une fois sur les postes de la classe.

---

## Où en est l'application

Cinq activités élève, toutes reliées entre elles :

| Activité | Ce qu'elle alimente |
|---|---|
| 📝 Je me corrige | la banque de mots, les besoins de suivi, les groupes |
| 📖 Je lis à voix haute | le suivi de fluence, les groupes de besoin |
| 🔎 Mon dictionnaire | les mots cherchés → la dictée, le suivi enseignant |
| ✍️ Ma dictée | la banque de mots, les badges, le suivi enseignant |
| 🏆 Mon bilan | rassemble tout, côté élève |

Les quatre autres pistes évoquées en phase J5 restent ouvertes : la chasse aux
mots, l'atelier d'écriture guidée, la lecture à deux voix et le passeport de
leçons.
