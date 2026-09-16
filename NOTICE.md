# Correcteur Pédagogique — Notice

Application pour la classe. Trois modules, un seul programme, **100 % hors ligne**.

| Module | Pour qui | Ce que ça fait |
|---|---|---|
| **1. Autocorrection** | Élève | Il charge un texte et le corrige lui-même, en 4 étapes |
| **2. Fluence de lecture** | Élève | Il lit à voix haute, chronomètre, obtient ses mots/minute (comptage à la main ou automatique, § 6) |
| **3. Analyse** | Enseignant | Résultats, graphiques, besoins de suivi, export vers Notes & Suivi |

### Nouveautés de cette version

Ajoutées **sans rien retirer** aux modules ci-dessus :

- **Code enseignant (facultatif)** : dans *Sécurité & données*, créez un code de 4 à 6
  chiffres pour protéger le tableau de bord et les réglages. Les élèves gardent leur
  accès habituel (classe → prénom). Tant qu'aucun code n'est créé, rien ne change.
  Un code de récupération (affiché une seule fois) permet de le réinitialiser.
- **Sauvegardes** (onglet *Sécurité & données*) : copie de sécurité automatique chaque
  jour d'utilisation (10 conservées) ; restauration en un clic. **Nouveau :** une
  *deuxième copie* peut être déposée automatiquement dans un dossier Nextcloud ou sur
  une clé USB — voir § 10.
- **Mode salle informatique** (même onglet) : active l'accès depuis les Chromebooks des
  élèves (adresse + QR code), sur le même wifi. Désactivé par défaut.
- **Pilotage fin** (onglet dédié) : grille des points faibles par catégorie et
  détection des élèves **en régression** (qui allaient bien et décrochent).
- **Devoirs** (onglet dédié) : assignez un texte à une classe ou à un élève ; il
  apparaît en tête de l'espace de l'élève concerné.
- **Fiche d'exercices ciblée** : depuis *Fiche élève*, générez une feuille imprimable
  de phrases à corriger, centrée sur le point faible de l'élève (avec corrigé).

---

## 1. Démarrer

### Essayer tout de suite
1. Décompresse le dossier où tu veux.
2. Double-clique sur **`lancer.bat`**.
3. Une fenêtre noire s'ouvre (laisse-la ouverte), puis l'application apparaît.

Au tout premier lancement, l'application installe deux composants : compte environ une minute, et une connexion internet **cette fois-là seulement**. Ensuite, tout fonctionne hors ligne.

Si un message dit que **Python n'est pas installé** :
- Va sur **https://www.python.org/downloads/**
- Clique sur le gros bouton jaune **Download Python**
- ⚠️ **Coche « Add Python to PATH »** tout en bas de la fenêtre d'installation
- Clique sur **Install Now**, puis relance `lancer.bat`

### Fabriquer le .exe
Double-clique sur **`build_exe.bat`**, attends 3 à 6 minutes. Ton programme se trouve alors dans **`dist\CorrecteurPedagogique.exe`**.

Copie ce seul fichier sur une clé USB ou sur les ordinateurs de la classe : **il fonctionne seul, sans installer Python ni rien d'autre**.

---

## 2. L'application

L'interface est celle d'une application web moderne, dans une vraie fenêtre : barre latérale à gauche, thème **clair ou sombre** (bouton 🌙 en haut à droite, effet immédiat).

Tu arrives dans l'**espace enseignant**. Pour lancer un élève : **🎓 Espace élève**, en bas de la barre latérale. L'élève choisit sa classe puis son prénom dans deux listes déroulantes — aucun clavier, aucun mot de passe. Il n'a **jamais** accès à tes analyses.

---

## 3. Avant de lancer les élèves

### 🏫 Classes & élèves
L'application arrive avec deux classes de démonstration. Pour mettre les tiennes : **➕ Nouvelle classe**, **➕ Nouvel élève**, ou **📥 Importer un CSV** (format : `prénom ; nom ; classe` — les classes absentes sont créées, les doublons ignorés). Quand tout est en place : **🧹 Effacer les données de démonstration**.

Le **niveau de la classe** compte : il fixe l'objectif de lecture (repère MCLM).

### 📚 Banques de textes — le point à ne pas rater

Pour les textes à corriger, **saisis toujours le corrigé**. C'est lui qui permet à l'application de savoir, sans la moindre ambiguïté, quels mots sont réellement fautifs.

La liste affiche « ✔ fourni » ou « ⚠ manquant ». Un bouton **⧉ Recopier le texte pour le corriger** t'évite de tout retaper : tu répares les fautes, c'est tout. L'élève ne voit jamais ce corrigé.

---

## 4. Comment l'application sait ce qui est vraiment faux

C'est le cœur de l'outil. Deux minutes de lecture, elles valent le coup.

**Quand le corrigé est connu** — texte généré par l'application, texte de ta banque avec son corrigé, ou texte de l'élève passé par le correcteur — l'application **compare** simplement, mot à mot. Elle ne devine rien. Conséquence : **un mot correct n'est jamais souligné**, et un élève qui a tout corrigé arrive toujours à zéro.

**Quand l'élève écrit son propre texte**, l'application le fait d'abord corriger :
- par **DeepSeek** (cloud, clé API), ou
- par **Ollama** (local, gratuit, aucune donnée ne sort), ou
- à défaut, par ses **règles hors ligne** — toujours disponibles.

Dans ce dernier cas seulement, elle distingue :
- les **vraies erreurs** (surlignées, comptées) — celles dont le contexte prouve la faute : « il *et* parti », « ils *on* mangé », « il a *manger* », « les *enfant* » ;
- les **mots à vérifier** (soulignés en pointillé, **jamais comptés**) — « ces / ses », « ou / où », « la / là ». Aucune règle simple ne tranche : le mot est peut-être parfaitement juste. L'application invite à vérifier, mais **ne pénalise pas**.

> Désactivable dans ⚙️ Réglages → *Module 1 — repérage des erreurs*.

---

## 5. Module 1 — L'élève se corrige

**Trois sources** : ⌨️ il écrit son texte · 📚 il choisit un texte de la classe · 🎲 l'ordinateur lui fabrique un texte surprise (nombre de phrases au choix). Le texte surprise fonctionne **même sans internet**.

**Les 4 étapes**

1. **Je cherche seul** — les zones fautives sont surlignées **en jaune**, sans aucun indice. L'élève ne sait pas *quelle* erreur c'est : il doit chercher. Le surlignage disparaît quand il corrige juste.
2. **J'utilise les outils** — les erreurs restantes prennent **la couleur de leur catégorie**. En cliquant dessus, la leçon s'ouvre : la règle, la procédure de vérification, des exemples, le piège classique. Plus les tableaux de conjugaison.
3. **Un camarade relit** — facultatif.
4. **Ma version finale** — bilan : erreurs au départ, corrigées, restantes, **% corrigées sans aide**, temps, et le détail catégorie par catégorie.

> **L'indicateur qui compte vraiment** : le **% corrigé sans aide** (écart entre l'étape 1 et l'étape 2). Un élève qui corrige tout *après* avoir lu la leçon n'a pas le même besoin qu'un élève qui ne trouve rien. L'application distingue les deux.

**Les 8 catégories** : Accords · Conjugaison · Homophones · Orthographe · Segmentation · Ponctuation · Majuscules · Lexique. Chacune est reliée à une leçon portant un identifiant (`FR-ORTH-ACC-01`…), pour brancher plus tard tes propres contenus.

**🔎 Confort de lecture** (barre au-dessus de chaque texte) : A− / A+ (12 à 44 pt), polices **dys** (OpenDyslexic, Luciole, Andika… si installées), **syllabes colorées**, une **ligne sur deux colorée**, **règle de lecture**, fonds crème/bleuté/verdâtre, interligne réglable. Réglages mémorisés d'une séance à l'autre.

---

## 6. Module 2 — Fluence de lecture

L'élève choisit un **niveau (1 à 5)**, puis un texte affiché en gros caractères.

1. **▶ Démarrer la lecture** — l'élève ou toi, si tu es assis à côté.
2. Il lit à voix haute, puis **⏹ J'ai fini de lire**.
3. On saisit : le **nombre de mots mal lus**, le **nombre de mots réellement lus**, et **qui a compté**.

```
MCLM = (mots lus − erreurs) ÷ temps en minutes
```

Le score s'affiche en grand, comparé au **repère du niveau de classe** (CP 30 · CE1 50 · CE2 70 · CM1 90 · CM2 110 · 6e 120), avec la progression et le record personnel. **15 textes** sont fournis sur les 5 niveaux.

### 🎤 Compter les mots automatiquement (facultatif)

Si tu n'as pas le temps de t'asseoir à côté de chaque élève, l'application peut
**compter les mots à ta place** : l'élève lit à voix haute, l'ordinateur écoute,
transcrit, et compare mot à mot avec le texte attendu. Tu obtiens directement les
mots sautés, les mots remplacés, l'endroit où l'élève s'est arrêté, et le MCLM.

**Ce qu'il faut savoir avant de l'activer** — les moteurs de transcription
*réparent* ce qu'ils entendent : ils écrivent le mot qu'ils comprennent, pas les
hésitations. Une lecture hachée, une syllabe reprise, un mot déchiffré péniblement
seront transcrits comme un mot juste. **La mesure est donc optimiste sur la qualité
du déchiffrage.** C'est pourquoi le résultat arrive comme une **proposition
modifiable**, jamais comme une note enregistrée d'office : tu relis, tu corriges si
besoin, puis tu valides. Un avertissement le rappelle à chaque analyse.

**Pour l'activer** : ⚙️ Réglages → *Lecture en autonomie*. Le service par défaut est
**Albert (DINUM)**, l'IA de l'État français — modèle `whisper-large-v3-turbo`. Il
faut une clé d'accès. N'importe quel service compatible OpenAI convient aussi.

**Si tu ne l'actives pas, rien ne change** : le comptage à la main reste le
fonctionnement normal. Et même activée, si l'élève refuse le micro ou si le service
ne répond pas, l'application repasse toute seule au comptage manuel — jamais de
blocage en pleine séance.

**Vie privée** : l'enregistrement de la voix de l'élève **n'est jamais conservé** —
il est envoyé pour transcription, puis jeté. Attention tout de même : il s'agit de la
voix d'un enfant transmise à un service extérieur. Vérifie la position de ton école
avant de généraliser (la CNIL a publié en juin 2026 une fiche pratique sur l'usage
d'un système d'IA par les enseignants).

---

## 7. Module 3 — Ce que tu en tires

**📊 Tableau de bord** — vue de classe : % d'erreurs corrigées, % sans aide, mots/minute. Deux graphiques : les erreurs par catégorie (quelle notion bloque *la classe*) et la fluence par niveau.

**👤 Fiche élève** — courbe de progression en fluence (face à son objectif), courbe du % d'erreurs corrigées séance après séance, catégories qui le bloquent.

**🩺 Remédiation — l'onglet le plus utile.** L'application détecte seule :
- **Écrit** : une catégorie revient trop souvent → la leçon à retravailler est nommée
- **Méthode** : l'élève corrige peu sans aide → il sait corriger, mais pas *chercher*
- **Lecture** : fluence trop en dessous du repère → lecture répétée, 5 min par jour

Et surtout : les **groupes de besoin**. L'application regroupe les élèves qui butent sur la même notion — de quoi monter un atelier de 4 élèves sur les homophones sans y passer une soirée. Export CSV.

Seuils réglables : séances prises en compte (3), erreurs d'une catégorie déclenchant l'alerte (3), autonomie minimale attendue (50 %), écart maximal au repère MCLM (25 %).

---

## 8. Brancher une IA (facultatif)

Sert à **corriger** les textes libres des élèves et à **générer** des textes plus variés. L'application marche sans, mais la correction des textes libres est alors plus modeste.

**Google AI Studio / Gemini — gratuit, le plus simple pour démarrer.** Va sur
`aistudio.google.com/apikey`, connecte-toi avec un compte Google, clique sur *Créer une
clé API* : c'est gratuit et **sans carte bancaire**. Puis ⚙️ Réglages → coche « Utiliser
une IA », moteur **Autre API**, clique sur le réglage tout prêt **« Google AI Studio
(Gemini) »** (il remplit l'adresse et le modèle), colle la clé → **🔌 Tester le moteur**.

> Les modèles **Flash** et **Flash-Lite** sont ceux qui restent gratuits, avec des quotas
> par minute et par jour — largement suffisants pour une classe.
>
> ⚠️ **À savoir** : sur l'offre gratuite, Google se réserve le droit d'utiliser ce qui est
> envoyé pour améliorer ses produits (ce n'est pas le cas de l'offre payante). Réserve-la
> donc à la **génération de textes et d'exercices**, et évite-la pour les **productions
> écrites des élèves**. Pour celles-ci : Albert (données en France) ou Ollama (local).

**DeepSeek** (cloud, quelques centimes) : compte sur `platform.deepseek.com` → clé API → ⚙️ Réglages → coche « Utiliser une IA », moteur `deepseek`, colle la clé → **🔌 Tester le moteur**.

**Ollama** (local, gratuit, **aucune donnée ne sort de l'ordinateur**) : installe depuis `ollama.com`, puis `ollama pull gemma3:12b` → Réglages → moteur `ollama`.

**Une seule clé pour les trois applications.** Si tu as déjà saisi une clé dans le Cahier
Journal (Réglages → Assistance IA → *Clés partagées*), le Correcteur la reprend
automatiquement : rien à recoller ici. Une clé saisie dans cet écran reste prioritaire.

> Si l'IA est en panne ou reformule au lieu de corriger, l'application **la rejette et bascule seule** sur ses règles. Un élève n'est jamais bloqué en pleine séance.

---

## 9. Connexion avec « Notes & Suivi »

Notes & Suivi chiffre ses données et n'expose aucun serveur : **on ne peut pas aller lire dedans**. En revanche, elle sait aller **chercher** les données d'une application partenaire.

On inverse donc : **le Correcteur ouvre une petite porte locale, et Notes & Suivi vient s'y servir.**

**À faire une seule fois :**
1. 🔗 Notes & Suivi → vérifie que le pont est **actif** (il démarre tout seul).
2. Ouvre Notes & Suivi, déverrouille avec ton PIN.
3. Dans ses réglages d'intégration, mets : **`http://localhost:4100`** *(le réglage `nes_cahier_url`)*.
4. Lance une synchronisation.

Elle récupérera alors toute seule, toutes les 5 minutes : la liste des élèves, l'évaluation **« Autocorrection — français écrit »** (note /100), l'évaluation **« Fluence de lecture (MCLM) »** (note /100), et le détail de chaque séance avec les 8 catégories en compétences. Les bulletins et graphiques de Notes & Suivi se remplissent sans que tu tapes quoi que ce soit.

**RGPD** : seul le **prénom** est transmis par défaut. Tous les échanges sont tracés dans un journal. Rien ne quitte l'ordinateur : tout passe par `localhost`.

**Si ça ne marche pas** : deux boutons de secours — export **JSON** (à importer dans Notes & Suivi) ou **CSV** (tableur).

---

## 10. Questions courantes

**Où sont mes données ?**
`C:\Users\<toi>\AppData\Roaming\CorrecteurPedagogique\correcteur.db`. Les exports vont dans le sous-dossier `exports`. Pour sauvegarder : copie ce dossier.

**Et si mon disque dur lâche ?**
Les sauvegardes automatiques sont à côté de la base : sur le **même disque**. Elles ne
protègent donc que des mauvaises manipulations, pas d'une panne matérielle.

Va dans **⚙️ Sécurité & données → 🗄️ Deuxième copie**, coche la case et indique un
second dossier : ton dossier **Nextcloud** synchronisé, une **clé USB**, un disque
externe. À chaque sauvegarde, une copie y est déposée automatiquement (10 conservées).

Le bouton **Tester** vérifie tout de suite que l'application peut écrire à cet endroit —
utilise-le, ça évite de croire qu'on est sauvegardé alors qu'on ne l'est pas.

Si la clé est débranchée le jour où la sauvegarde tourne, **rien n'est perdu** : la
sauvegarde locale se fait normalement, l'écran te le signale, et les copies manquantes
sont rattrapées automatiquement dès que le dossier redevient accessible. Les copies
externes se restaurent exactement comme les locales.

**Je mets à jour l'application, vais-je perdre mes résultats ?**
Non. La base se met à jour toute seule au démarrage, sans rien perdre. **Tu n'auras jamais à supprimer ta base.**

**Le port 4100 est déjà pris.**
Le pont Notes & Suivi utilise 4100, l'interface un port au-delà de 5173 — ils ne se gênent pas. Si 4100 est occupé par autre chose, l'application te le dit et continue de fonctionner.

**Le correcteur rate des fautes.**
Sans IA, les règles hors ligne sont honnêtes mais modestes. Branche Ollama (gratuit, local) : la correction devient nettement meilleure. Et surtout : **saisis les corrigés de tes textes** — c'est là que se joue la fiabilité.

**Une erreur soulignée alors que le mot est juste.**
Cela ne doit plus arriver quand un corrigé existe : c'est une garantie du fonctionnement, pas une amélioration. Si tu en vois une sur un texte **libre** sans IA, signale-la.
