# Correctif — les boutons « Tester » ne fonctionnaient pas correctement

148 tests automatiques passés, aucun échec.

---

## Ce qui n'allait pas

Vos deux captures montrent le **même défaut de conception**, et il venait de
moi.

Les boutons « Tester le second moteur » et « Tester le service » interrogeaient
les réglages **enregistrés dans le fichier de configuration**, pas ce que vous
veniez de taper à l'écran. Conséquence :

- vous collez votre clé Albert ;
- vous cliquez sur « Tester » ;
- le serveur teste l'**ancienne** valeur (vide) ;
- vous recevez `HTTP Error 401: Unauthorized` ou
  `Renseignez l'adresse et la clé` — alors que tout est bien renseigné à
  l'écran.

Il aurait fallu enregistrer avant de tester, ce que rien n'indiquait clairement.
C'est absurde : on teste justement pour savoir si l'on peut enregistrer.

---

## Ce qui est corrigé

### 1. Les tests portent sur ce que vous voyez

Les deux boutons envoient maintenant **l'adresse, la clé et le modèle affichés
à l'écran**. Plus besoin d'enregistrer avant d'essayer — c'est écrit sous les
boutons.

### 2. Les messages d'erreur disent quoi corriger

Fini les codes bruts. Chaque erreur est traduite :

| Avant | Maintenant |
|---|---|
| `HTTP Error 401: Unauthorized` | « Clé d'accès refusée. Vérifiez que la clé est complète, sans espace au début ou à la fin, et qu'elle est bien active. » |
| `HTTP Error 403` | « Clé valide mais accès refusé : ce compte n'a peut-être pas le droit d'utiliser ce modèle. » |
| `HTTP Error 404` | « Adresse ou modèle introuvable. Vérifiez l'adresse de l'API et le nom exact du modèle. » |
| `HTTP Error 422` | « Le service a refusé la demande : le nom du modèle est probablement incorrect. » |
| `HTTP Error 429` | « Trop de demandes d'un coup. Réessayez dans une minute. » |
| `URLError…` | « Impossible de joindre le service. Vérifiez l'adresse et la connexion internet. » |

Quand le service renvoie une explication, elle est ajoutée à la suite.

### 3. Un bouton « 📋 Voir les modèles disponibles »

C'est l'ajout le plus utile pour votre cas. Il interroge la route standard
`/v1/models` et affiche **la liste exacte des modèles auxquels votre clé donne
accès**, sous forme de boutons cliquables : un clic recopie le nom dans le champ.

Cela résout deux choses d'un coup :

- **il vérifie la clé** indépendamment du modèle (si la liste s'affiche, la clé
  est bonne) ;
- **il donne les noms exacts**. `albert-large` n'est peut-être pas le bon
  identifiant sur votre compte — les noms de modèles changent, et c'est une
  cause fréquente d'erreur 404 ou 422.

Le bouton est présent aux deux endroits, et filtre intelligemment : les modèles
de discussion pour le second moteur IA, les modèles de transcription (Whisper)
pour la lecture en autonomie.

### 4. L'adresse accepte les deux formes

Votre capture montre `https://albert.api.etalab.gouv.fr/v1/audio/transcriptions`
alors que l'aide affichait `…/v1`. Les deux fonctionnent désormais, et l'aide le
dit. Une adresse terminée par `/chat/completions` ou `/models` est également
reconnue et corrigée.

### 5. Le test de transcription ne ment plus

Tester la transcription envoie une demi-seconde de silence. Le service répond
donc… une transcription vide. C'était compté comme un échec. C'est maintenant
compris comme le **résultat normal** : si le service a répondu, il fonctionne.
C'est expliqué sous le bouton.

---

## Ce que je vous suggère de faire, dans l'ordre

1. Ouvrez **Paramètres → Réglages → 🤝 Un second moteur IA**.
2. Cliquez sur **Albert (service public français)** — adresse et modèle
   se remplissent.
3. Collez votre clé.
4. Cliquez sur **📋 Voir les modèles disponibles**.
   - **La liste s'affiche** → votre clé est bonne. Cliquez sur le modèle qui
     vous convient, il se recopie dans le champ.
   - **Un message d'erreur s'affiche** → il vous dira si c'est la clé,
     l'adresse ou la connexion.
5. Cliquez sur **🔌 Tester le second moteur** pour confirmer.
6. **Enregistrez les réglages**, puis répartissez les tâches.

Même démarche pour **🎙️ Lecture en autonomie** : le bouton « Voir les modèles »
vous donnera le nom exact du modèle Whisper disponible sur votre compte.

---

## Si la liste des modèles échoue aussi

Ce serait alors un vrai problème de clé ou de droits, et non plus un défaut de
l'application. Deux pistes :

- la clé Albert est-elle bien **active** ? Elles ont parfois une date de fin ;
- votre compte a-t-il accès aux **modèles de transcription** ? Ils ne sont pas
  toujours ouverts en même temps que les modèles de texte.

Dans les deux cas, le message affiché vous le dira, et c'est vers la DINUM qu'il
faudra se tourner.
