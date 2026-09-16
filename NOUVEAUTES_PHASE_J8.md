# Ce qui a changé — Phase J8 : la lecture en autonomie

141 tests automatiques passés sur l'interface réelle, aucun échec.

---

## La réponse à votre question, sans détour

**Oui, mais partiellement.** Il faut être précis, parce que la nuance décide de
l'usage que vous en ferez.

### Ce que l'élève peut maintenant faire seul

- lancer sa lecture, la faire, l'arrêter ;
- obtenir **immédiatement** son nombre de mots corrects par minute ;
- voir **son texte relu, mot par mot**, avec ce qui a été sauté, remplacé, ou
  pas atteint ;
- recommencer autant de fois qu'il veut, sans mobiliser personne.

C'est un vrai changement : l'entraînement à la fluence demande de la
**répétition**, et la répétition demandait jusqu'ici votre présence. Un élève
peut désormais relire trois fois le même texte pendant que vous êtes ailleurs.

### Ce que la machine ne sait pas faire

Les moteurs de transcription **réparent ce qu'ils entendent**. Ils écrivent le
mot qu'ils comprennent, pas la façon dont il a été dit. Concrètement :

| L'élève… | La machine le voit ? |
|---|---|
| saute un mot, une ligne | ✅ oui, très bien |
| dit un autre mot à la place | ✅ oui |
| s'arrête au milieu du texte | ✅ oui, elle sait où |
| hésite, reprend une syllabe | ❌ non |
| déchiffre péniblement mais juste | ❌ non |
| lit sans ton, sans respecter la ponctuation | ❌ non |

**Le comptage est donc optimiste.** Un élève qui déchiffre lentement mais
correctement obtiendra un bon score de précision, alors que sa lecture n'est pas
fluide. Le MCLM (la vitesse) reste juste, lui, puisqu'il vient du chronomètre.

**Conséquence pratique :** c'est excellent pour **l'entraînement en autonomie**
et pour suivre une progression. Ce n'est pas un remplaçant pour **l'évaluation**
d'un lecteur fragile, où votre oreille reste irremplaçable.

L'application le dit d'ailleurs à l'élève, à chaque fois, dans un encadré
orange : *« Ce comptage est une proposition… le résultat est plutôt optimiste.
Corrigez-le si besoin avant d'enregistrer. »* Et les deux chiffres — erreurs et
mots lus — **restent modifiables** avant enregistrement.

---

## Comment ça marche

1. L'élève coche **🎙️ L'ordinateur m'écoute et compte tout seul** (case
   proposée seulement si vous avez activé la fonction et si un micro existe).
2. Il appuie sur Démarrer : le navigateur demande l'autorisation du micro, puis
   une pastille rouge clignotante indique que ça enregistre.
3. Il lit, puis appuie sur « J'ai fini ».
4. L'enregistrement part vers le service de transcription, revient en texte.
5. L'application **compare mot à mot** le texte attendu et le texte entendu.

La comparaison ignore les accents et la ponctuation : on ne pénalise pas un
élève parce que le moteur a écrit « eleve » sans accent.

### Le compte rendu

Quatre chiffres en gros (MCLM, mots bien lus, mots sautés ou remplacés, mots
atteints sur le total), puis **le texte entier recoloré** :

- **noir** : bien lu
- **orange souligné** : un autre mot a été entendu (survolez pour voir lequel)
- **rouge barré** : sauté
- **gris pâle** : pas atteint, l'élève s'est arrêté avant

C'est ce qui rend le résultat vérifiable d'un coup d'œil — par l'élève comme
par vous.

---

## Ce qu'il faut savoir avant d'activer

C'est désactivé par défaut, et l'écran de réglage affiche cet avertissement :

- **La voix de l'élève quitte l'ordinateur.** Elle est envoyée au service que
  vous réglez, le temps de la transcription. L'application ne conserve aucun
  enregistrement — il est utilisé puis abandonné.
- **Prévenez les familles et votre direction.** La voix est une donnée
  personnelle. Avec Albert, le traitement a lieu en France, sur un service de
  l'État — c'est le point fort de ce choix par rapport à un service américain.
- **Un micro-casque est vivement conseillé.** À plusieurs dans une salle, la
  transcription se dégrade beaucoup : le moteur capte les voisins.
- **Il faut internet** pendant la séance, et une clé Albert (demande auprès de
  la DINUM, réservée aux agents publics).

---

## Où régler

**Paramètres → Réglages → 🎙️ Lecture en autonomie.**

Les valeurs d'Albert sont pré-remplies : il ne reste que la clé à coller. Un
bouton **🔌 Tester le service** vérifie la connexion sans mobiliser un élève.

Si vous préférez un autre service, n'importe quelle API compatible OpenAI
(`/v1/audio/transcriptions`) convient — OpenAI, un serveur Whisper local…

---

## Si ça ne marche pas, rien ne casse

C'est le point auquel j'ai fait le plus attention. À chaque étape, l'échec
ramène simplement au fonctionnement d'avant :

| Situation | Ce qui se passe |
|---|---|
| Fonction non activée | La case n'apparaît pas, comptage à la main comme avant |
| Micro refusé par l'élève | Message, puis comptage à la main |
| Pas d'internet, service en panne | Message, puis comptage à la main |
| Transcription vide (micro trop faible) | Message, puis comptage à la main |
| Enregistrement trop long (> 12 Mo) | Refusé avant tout envoi |

L'élève n'est jamais bloqué, et aucune lecture n'est perdue.

---

## Fichier ajouté

| Fichier | Rôle |
|---|---|
| `transcription.py` | Envoi de l'audio, transcription, comparaison mot à mot |

Migration de base : aucune. `build_exe.bat` : rien à changer.

---

## Une piste que cela ouvre

Puisque la comparaison mot à mot fonctionne, la même mécanique permettrait
**la lecture à deux voix** évoquée en phase J5 : le texte alterne deux couleurs,
l'élève lit sa couleur, l'ordinateur vérifie qu'il a bien lu la sienne et
enchaîne. C'est un exercice très efficace sur les lecteurs fragiles, et
l'essentiel du travail est maintenant fait.
