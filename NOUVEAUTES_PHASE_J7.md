# Ce qui a changé — Phase J7

137 tests automatiques passés sur l'interface réelle, aucun échec.

---

## 1. La voix par IA : la réponse est non, et voici pourquoi

J'ai vérifié les deux pistes.

**DeepSeek ne fait pas de synthèse vocale.** L'API n'accepte que du texte et ne
renvoie que du texte. Tous les projets « voix + DeepSeek » qu'on trouve
branchent un service tiers (ElevenLabs, Azure…) pour la partie audio.

**Albert non plus.** L'API d'Albert (DINUM) fait de l'audio, mais **dans
l'autre sens** : `/v1/audio/transcriptions` transforme la parole en texte
(modèle Whisper). Il n'y a pas d'endpoint de synthèse vocale exposé.

Donc la voix de Windows que nous utilisons reste la bonne solution : gratuite,
instantanée, hors ligne, et sans qu'aucune donnée d'élève ne sorte de la classe.
Une voix IA coûterait à chaque mot dicté et exigerait internet.

**Ce que j'ai amélioré à la place :** les voix Windows 11 « Natural » sont
nettement meilleures que les anciennes. L'application les repère et **les met
d'office en tête**, avec une ⭐. S'il y a plusieurs voix françaises installées,
un menu permet d'en changer, et le choix est mémorisé.

*Pour installer les bonnes voix : Paramètres Windows → Heure et langue → Voix →
Ajouter des voix → Français. Choisissez celles marquées « Natural ».*

---

## 2. Deux moteurs IA, chacun sur ce qu'il fait de mieux

Votre intuition était juste, même si ce n'est pas pour la voix. **Paramètres →
Réglages → 🤝 Un second moteur IA (facultatif)** permet maintenant de régler un
deuxième moteur, puis de dire **lequel s'occupe de quoi** :

| Tâche | Moteur |
|---|---|
| Corriger les textes des élèves | au choix |
| Formuler les questions et les indices | au choix |
| Fabriquer les textes et les titres | au choix |
| Écrire les définitions du dictionnaire | au choix |

Vous pouvez donc garder **DeepSeek pour la correction** — où il est
effectivement bon — et confier la rédaction à un autre service.

**Trois réglages tout prêts** évitent la saisie d'adresses : **Albert**
(service de l'État, données en France, clé auprès de la DINUM), **OpenAI** et
**Mistral**. Un bouton teste le second moteur séparément.

Si le second moteur n'est pas réglé, tout passe par le principal : rien ne
change et rien ne casse.

---

## 3. Le bug de classification : corrigé, et c'était sérieux

Vous aviez raison, et le problème était plus large que prévu.

**Ce qui se passait :** quand seule la terminaison changeait (`prend → prends`,
`mangeon → mangeons`), l'application ne pouvait pas distinguer un verbe d'un
nom. Elle rangeait tout dans « Accords ». Résultat : des erreurs de conjugaison
comptées comme des accords du groupe nominal, un suivi faussé, et l'élève
renvoyé vers la mauvaise leçon.

**Ce que j'ai mis en place**, dans cet ordre :

1. **Terminaison exclusivement verbale** → conjugaison, sans hésiter. La liste
   a été considérablement étoffée (présent, imparfait, futur, conditionnel,
   passé simple, subjonctif, infinitif, participe), et je repère aussi les
   terminaisons *-ent, -ons, -ez, -ont* même quand le radical change
   (`dort → dorment`).
2. **Couples infinitif / participe** (`je suis aller → allé`) → conjugaison.
3. **Terminaison exclusivement nominale** (*-aux, -eaux, -euse…*) → accord.
4. **Cas ambigu** (un simple *s* ou *t* final) → on interroge **le dictionnaire
   des 70 000 mots** : il sait que « rouges » est un adjectif et « prends » un
   verbe. C'est un fait, pas une supposition.
5. **En dernier recours**, on regarde la phrase : après « tu », c'est un verbe ;
   après « les », c'est un nom.

**Bonus :** les mots écrits phonétiquement mais très éloignés (`fotes → fautes`,
une seule lettre commune) étaient classés en « lexique » — c'est-à-dire
« mauvais mot » — alors que l'élève avait juste mal orthographié. Le moteur
phonétique de la phase J5 sert maintenant de dernier filet : deux mots qui se
prononcent pareil sont une erreur d'orthographe.

Testé sur 35 cas types : **35 sur 35 corrects**, dont les 9 vérifiés en
permanence par les tests automatiques.

---

## 4. L'aide passe en pleine largeur, sous le texte

Le passage guidé n'est plus en deux colonnes. Le texte de l'élève occupe
**toute la largeur**, et sous lui vient un **bandeau horizontal** : le compteur
de zones à revoir à gauche, la consigne au centre, l'astuce à droite — le tout
sur une seule ligne.

Quand l'élève clique sur une erreur, l'aide s'ouvre **sous le texte, sur toute
la largeur** : les pistes s'affichent sur deux colonnes, la question est plus
grande, et les boutons « Voir la leçon » et « Chercher au dictionnaire » ne sont
plus écrasés dans une colonne de 300 pixels.

---

## 5. Les flash cards dans « Ma banque de mots »

Votre idée de subitizing appliquée aux mots, exactement.

**🎒 Ma banque de mots → ⚡ M'entraîner en éclair.** Le mot s'affiche **deux
secondes** avec un compte à rebours, puis disparaît. L'élève le réécrit de
mémoire. C'est ce geste qui installe l'image orthographique du mot — bien plus
efficace que de le recopier vingt fois en le regardant.

**Un mot n'est acquis qu'après trois réussites**, matérialisées par trois
étoiles ☆☆☆ → ★★★. Une seule erreur remet le compteur à zéro : une réussite
peut être un coup de chance, trois non. Un bouton « 👁 Revoir le mot » réaffiche
le mot une seconde, pour ne pas bloquer.

Les mots acquis **sortent automatiquement de la banque**, et le bilan final
affiche la liste de ce qui est gagné.

Les mots de la banque étant exactement ceux que reprend **Ma dictée**, les deux
activités se répondent : on mémorise en éclair, on vérifie sous dictée.

---

## 6. « À faire la prochaine fois » : l'analyse propose, vous validez

Nouveau bouton sur le tableau de bord : **🎯 À faire la prochaine fois**.

Au lieu de lire les tableaux et de décider vous-même, l'analyse vous propose
directement l'activité de reprise, élève par élève, avec **le motif** :

| Ce qui est repéré | Ce qui est proposé |
|---|---|
| 12 mots en attente dans sa banque | ⚡ Mémoriser ses mots (flash cards) |
| Dernière dictée à 40 % | ✍️ Une dictée sur ses mots |
| 7 erreurs d'accord sur les séances récentes | 📘 Revoir : Accords + texte à corriger |
| 62 mots/min pour un repère de 90 | 📖 Lecture répétée |

Les cas prioritaires sont en rouge. Vous assignez d'un clic, ou d'un seul bouton
**« ✓ Tout assigner (prioritaires) »** pour la classe entière.

**Côté élève**, l'activité apparaît tout en haut de son menu, avant les
activités libres :

> 🎯 **Ce que le maître veut que tu fasses d'abord**
> ⚡ Mémoriser ses mots · ✍️ Une dictée sur ses mots

Un clic l'emmène directement au bon écran, et l'activité se marque terminée.
Pour une leçon, la fiche du classeur s'ouvre d'abord, puis le texte à corriger.

---

## Pour reconstruire

`lancer.bat` pour essayer, `build_exe.bat` pour refaire l'exe. La base de
données se met à jour seule au premier lancement (migration v6 : activités à
faire).

---

## Ce qui reste ouvert

Des pistes évoquées en phase J5, il reste : la chasse aux mots, l'atelier
d'écriture guidée, la lecture à deux voix, et le passeport de leçons.

S'ajoute maintenant une piste qui n'existait pas avant : **Albert sait
transcrire la parole**. On pourrait donc faire lire l'élève à voix haute et
faire compter les mots correctement lus **automatiquement**, au lieu que
l'adulte compte à la main. Ce serait un vrai gain sur le module de fluence —
mais cela suppose une clé Albert et une connexion pendant la séance.
