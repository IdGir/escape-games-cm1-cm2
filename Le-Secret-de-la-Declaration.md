# 🏛️ LE SECRET DE LA DÉCLARATION

## Escape game immersif sur la Révolution française (1789)

**Niveau visé :** CM1 – CM2
**Durée :** 45 à 60 minutes
**Modalités :** Jeu en équipes de 4-5 élèves / ou classe entière (TBI)
**Matériel :** Ordinateur ou tablette + connexion à une API de dialogue (Albert ou DeepSeek)
**Auteur :** Conçu avec GLM 5.2

---

## 📑 SOMMAIRE

1. [Guide de lecture rapide (pour l'enseignant)](#1--guide-de-lecture-rapide-pour-lenseignant)
2. [Scénario et objectif pédagogique](#2--scénario-et-objectif-pédagogique)
3. [Personnages et dialogues](#3--personnages-et-dialogues)
4. [Les 5 salles immersives](#4--les-5-salles-immersives)
5. [Les 5 énigmes complètes](#5--les-5-énigmes-complètes)
6. [Adaptation dynamique de la difficulté](#6--adaptation-dynamique-de-la-difficulté)
7. [Usage de l'API (Albert / DeepSeek)](#7--usage-de-lapi-albert--deepseek)
8. [Déroulé minute par minute](#8--déroulé-minute-par-minute)
9. [Grille d'évaluation des compétences](#9--grille-dévaluation-des-compétences)
10. [Bilan final et quizz](#10--bilan-final-et-quizz)
11. [Prolongements pédagogiques](#11--prolongements-pédagogiques)
12. [Gestion de classe et sécurité](#12--gestion-de-classe-et-sécurité)
13. [ANNEXES – Fiches élèves à imprimer](#13--annexes--fiches-élèves-à-imprimer)

---

## 1) 📖 GUIDE DE LECTURE RAPIDE (pour l'enseignant)

> **Vous n'avez jamais animé d'escape game ?** Lisez ce bloc, puis allez directement à la [Section 8 (Déroulé)](#8--déroulé-minute-par-minute) et à la [Section 13 (Annexes)](#13--annexes--fiches-élèves-à-imprimer).

| Vous voulez… | Allez à la section… |
|---|---|
| Comprendre l'histoire en 2 min | [§2 Scénario](#2--scénario-et-objectif-pédagogique) |
| Imprimer les supports élèves | [§13 Annexes](#13--annexes--fiches-élèves-à-imprimer) |
| Savoir quoi dire à chaque minute | [§8 Déroulé](#8--déroulé-minute-par-minute) |
| Préparer les requêtes API | [§7 API](#7--usage-de-lapi-albert--deepseek) |
| Évaluer vos élèves | [§9 Grille](#9--grille-dévaluation-des-compétences) |

**Check-list matériel (15 min avant) :**
- [ ] Imprimer les annexes A1 à A5 (1 jeu par équipe)
- [ ] Préparer un minuteur visible (projecteur / TBI / téléphone)
- [ ] Ouvrir l'interface API (Albert ou DeepSeek) dans un onglet
- [ ] Préparer 5 enveloppes (1 par salle) contenant les indices à remettre
- [ ] Couper le fond sonore si la classe est agitée (le garder si possible pour l'immersion)
- [ ] Avoir un sifflet ou une clochette pour signaler la fin de chaque salle

**Règle d'or :** l'API ne remplace jamais l'enseignant. C'est un **outil d'animation** qui enrichit les dialogues. En cas de panne, tous les dialogues-clés sont écrits dans la [Section 3](#3--personnages-et-dialogues) et peuvent être lus directement.

---

## 2) 🎭 SCÉNARIO ET OBJECTIF PÉDAGOGIQUE

### L'accroche (à lire aux élèves ou à projeter)

> 📜 **« Paris, le 26 août 1789. »**
>
> *Il y a quelques jours, l'Assemblée nationale a adopté la **Déclaration des droits de l'homme et du citoyen**. C'est un texte immense, qui affirme que tous les hommes naissent libres et égaux en droits.*
>
> *Mais ce que personne ne sait, c'est qu'il existait un **article secret**, le 18ᵉ, trop dangereux pour être rendu public. Il a été inscrit sur un manuscrit volé dans la nuit.*
>
> *Si cet article tombait entre de mauvaises mains, il pourrait changer le cours de l'Histoire…*
>
> *Vous êtes un groupe d'**apprentis historiens du temps**. Vous avez été envoyés depuis le futur pour une mission : **retrouver le manuscrit volé avant qu'il ne disparaisse à jamais**. Vous avez 60 minutes. Le temps file… »*

### La mission (objectif des joueurs)

Retrouver les **4 fragments du manuscrit** dispersés à travers le Paris de 1789, puis reconstituer l'**article secret** dans la salle de l'Assemblée.

Chaque salle réussie délivre :
- un **fragment** du manuscrit (1 mot-clé),
- un **indice** pour la salle suivante,
- la confiance d'un **personnage**.

### Objectifs pédagogiques

À la fin de la séance, l'élève est capable de :
- **Connaître** les événements-clés de 1789 : États généraux, serment du Jeu de paume, prise de la Bastille, Déclaration des droits de l'homme et du citoyen (26 août 1789).
- **Comprendre** les notions de *liberté, égalité, fraternité, souveraineté nationale*.
- **Reconnaître** les grands personnages (Louis XVI, Mirabeau, Danton, Robespierre) et leur rôle.
- **Lire** des documents d'époque adaptés (cahier de doléances, affiche, gravure).
- **Coopérer** : écouter, argumenter, se répartir les tâches.

### Compétences du socle mobilisées

- **Histoire / EMC** : se repérer dans le temps, comprendre les bouleversements de 1789, les valeurs de la République.
- **Français** : lecture compréhension, vocabulaire, déduction.
- **Maîtrise des langages** : argumenter, coopérer, présentation orale.

---

## 3) 🗣️ PERSONNAGES ET DIALOGUES

Chaque personnage a un **rôle**, une **voix** et un **seuil de confiance**. Les dialogues types ci-dessous peuvent être lus par l'enseignant **ou générés dynamiquement par l'API** (voir [§7](#7--usage-de-lapi-albert--deepseek)).

### 🧒 Louise — la petite parisienne (12 ans)

- **Rôle :** guide, repère dans la ville. Apparaît salle 1, revient salle 3.
- **Caractère :** vive, malicieuse, parle vite, tutoie les joueurs, cœur sur la main.
- **Seuil de confiance :** faible. Donne un indice dès qu'on lui parle avec respect.
- **Voix API :** *« Tu es Louise, 12 ans, fille du peuple à Paris en 1789. Tu parles avec entrain, tutoies les joueurs, utilises des mots simples et des expressions de l'époque ("palsambleu", "ventrebleu"). Tes réponses font 2 à 4 phrases. »*

**Dialogue d'accueil (toujours joué en salle 1) :**
> *« Eh ! Vous, là ! Vous avez une drôle de mise… Vous venez d'où, vous ? Ah, j'm'en fiche ! Écoutez bien, parce que moi j'connais Paris comme ma poche. Y'a un manuscrit qui s'est fait voler cette nuit, au palais. Tout le monde en parle. Si vous m'aidez à comprendre un truc, j'vous file un renseignement. Marché conclu ? »*

**Si les joueurs réussissent l'énigme :**
> *« Palsambleu, vous êtes malins ! D'accord, d'accord, j'vous le dis : le voleur est passé par l'imprimerie. Cherchez Maître Gutenberg, rue de la Harpe. Et… prenez garde, la foule gronde dans les rues. »*

**Si les joueurs échouent ou tâtonnent (>3 min) :**
> *« Bon, vous séchez ? J'vais vous aider, mais parce que j'aime bien votre tête. Regardez les lettres soulignées. Y'a un truc qui se cache là-dedans. Allez, concentrez-vous ! »*

**Exemple de dialogue généré par l'API (réussite rapide) :**
> *« Ventrebleu, vous avez trouvé en moins de deux minutes ! Vous n'êtes pas des enfants du quartier, vous ? J'vous soupçonne d'être des espions du roi… Non ? Tant mieux. Prenez ce fragment, et filez à l'imprimerie. Mais chut ! Personne ne doit vous voir. »*

---

### 🖨️ Maître Gutenberg — l'imprimeur

- **Rôle :** refuge des idées nouvelles. Apparaît salle 2.
- **Caractère :** posé, érudit, cite les Lumières (Voltaire, Rousseau), parle avec gravité.
- **Seuil de confiance :** moyen. Pose une **question sur les droits de l'homme**.
- **Voix API :** *« Tu es Maître Gutenberg, imprimeur parisien en 1789, passionné par les Lumières. Tu t'exprimes avec gravité, cites Rousseau ou Voltaire, vouvoies les joueurs. Réponses en 3 à 5 phrases. »*

**Dialogue d'accueil (salle 2) :**
> *« Entrez, entrez vite, et refermez cette porte. La presse tourne encore, et c'est tant mieux : c'est par l'imprimé que les idées voyagent. Vous cherchez le manuscrit, n'est-ce pas ? Je le sais. Tout Paris le sait. Mais avant de vous aider, je veux savoir une chose : selon vous, qu'est-ce qui rend les hommes égaux ? Répondez-moi, apprentis. »*

**Bonne réponse attendue :** *« Nous naissons tous libres et égaux en droits »* (idée centrale de la Déclaration).

**Si réussite :**
> *« Joli. Voici le fragment que j'ai retrouvé coincé entre deux pages d'un cahier de doléances. Et tenez, un conseil : le marquis de Montclair rôde aux Tuileries. Ne le sous-estimez pas. Méfiez-vous, mais écoutez-le. »*

**Exemple API (échec partiel) :**
> *« Votre réponse est incomplète. Rousseau, dans son Contrat social, disait que "l'homme est né libre, mais partout il est dans les fers". Réfléchissez : qu'est-ce qui, dès la naissance, nous rend semblables les uns aux autres ? La liberté, oui… et quoi d'autre ? »*

---

### 🎩 Le Marquis de Montclair — l'aristocrate mystérieux

- **Rôle :** faussement hostile, en réalité allié secret. Apparaît salle 3.
- **Caractère :** hautain, ironique, parle bien, teste la lucidité des joueurs.
- **Seuil de confiance :** élevé. Teste si les joueurs savent **observer et déduire**.
- **Twist :** il cherche lui aussi le manuscrit, mais pour le **protéger** (sa famille est menacée).
- **Voix API :** *« Tu es le Marquis de Montclair, aristocrate français en 1789. Tu es hautain, ironique, mais en réalité tu protèges les joueurs. Tu vouvoies avec une légère moquerie. Réponses en 3 à 6 phrases, avec un ton théâtral. »*

**Dialogue d'accueil (salle 3) :**
> *« Ah. Les voilà, les apprentis du futur. Je vous attendais. Croyez-vous vraiment que ce manuscrit vous attendrait sagement ? Allons. Je le cherche aussi. Non, non, ne faites pas cette tête effarouchée. Je ne suis pas votre ennemi… à condition que vous me prouviez votre perspicacité. Regardez autour de vous. Que voyez-vous ? »*

**Si réussite de l'énigme d'observation :**
> *« Hmm. Vous avez l'œil. Soit. Sachez ceci : le vrai voleur n'est pas un révolutionnaire, ni un aristocrate. C'est un homme qui veut **vendre** l'article secret au plus offrant. Il se trouve en ce moment même à l'Assemblée. Voici le fragment que j'ai pu soustraire. Et maintenant, allez. Le temps vous est compté. »*

**Exemple API (réussite brillante) :**
> *« Étonnant. Je dois reconnaître que je vous ai sous-estimés. Prenez ce fragment, et sachez-le : le dernier se trouve scellé dans le mécanisme de l'Assemblée. Un plan, des étiquettes, un ordre précis… Bonne chance, apprentis. La République vous regarde. »*

---

### ⚖️ Maximilien — le jeune avocat

- **Rôle :** figure morale (inspiré de Robespierre, mais **adouci** et nommé par prénom). Pose les **questions finales** sur les droits.
- **Caractère :** passionné de justice, sérieux, croit en la loi.
- **Apparition :** introduction (mission) + salle 5 (final).
- **Voix API :** *« Tu es Maximilien, jeune avocat en 1789, passionné par la justice et la loi. Tu t'exprimes avec sérieux, citations brèves, vouvoies avec respect. Réponses en 2 à 4 phrases. »*

**Dialogue d'introduction (mission, 1ʳᵉ minute) :**
> *« Apprentis, écoutez. Je suis Maximilien, avocat. La Déclaration que nous venons d'adopter est notre plus grand espoir. Mais un article secret a été volé. Sans lui, la justice est incomplète. Retrouvez les quatre fragments. Vous avez une heure. Le sort de la liberté est entre vos mains. »*

**Dialogue final (après résolution salle 5) :**
> *« Vous avez réussi. L'article secret est retrouvé. Voici ce qu'il disait : "Nul ne peut être accusé, arrêté ni détenu que dans les cas déterminés par la Loi." C'était le cœur de notre Déclaration. Vous avez sauvé l'esprit de 1789. Au nom du peuple, merci. »*

---

## 4) 🏰 LES 5 SALLES IMMERSIVES

> 💡 **Conseil immersion :** pour chaque salle, **lisez à voix haute le bloc « décor »** pendant que les élèves découvrent le support imprimé. Si possible, lancez un **fond sonore** (lien YouTube gratuit dans la [Section 12](#12--gestion-de-classe-et-sécurité)). Demandez aux élèves : *« Que voyez-vous ? Qu'entendez-vous ? Que ressentez-vous ? »*

---

### 🚪 SALLE 1 — La cour du Palais-Royal

**📅 Contexte :** matin du 26 août 1789, Paris bruie de rumeurs.

**🖼️ Décor (5 sens) :**
> *La pluie fine fouette les pavés luisants. Des affiches révolutionnaires, fraîchement collées, suintent sous l'humidité — vous pouvez sentir l'**encre encore humide** et la **pâte de farine** qui sert de colle. Au loin, la **rumeur d'une foule** monte et descend comme une marée, ponctuée du **tintement d'une cloche**. Une **odeur de pain chaud** s'échappe d'une boulangerie voisine. Une jeune fille en haillons, **Louise**, s'approche de vous, un regard malicieux dans les yeux. Elle tient un papier froissé…*

**🔊 Indice sonore :** pluie + foule lointaine + cloche (lien suggéré : ambiance pluie Paris).
**🔎 Éléments interactifs :** cliquer sur une affiche → la lire ; examiner le papier froissé de Louise.
**🎁 Récompense :** Fragment n°1 (mot **« LIBERTÉ »**) + indice « imprimerie, rue de la Harpe ».

---

### 🚪 SALLE 2 — L'imprimerie clandestine

**📅 Contexte :** atelier de Maître Gutenberg, sous les toits de Paris.

**🖼️ Décor (5 sens) :**
> *La porte grince et se referme sur le bruit de la rue. Ici, c'est le **cliquetis régulier de la presse à bras** qui domine, accompagné du **froissement des feuilles** qu'on tire une à une. L'air sent la **plomb fondu**, l'**encre grasse** et la **poussière de papier**. Des **cahiers de doléances** s'entassent sur une table, éclairés par une **chandelle** dont la flamme vacille. Au mur, un portrait gravé de **Voltaire** semble vous observer. Maître Gutenberg, tablier taché d'encre, vous accueille d'un regard grave.*

**🔊 Indice sonore :** presse mécanique + crépitement de bougie.
**🔎 Éléments interactifs :** feuilleter les cahiers de doléances ; examiner la partition musicale posée à côté.
**🎁 Récompense :** Fragment n°2 (mot **« ÉGALITÉ »**) + indice « Tuileries, cherchez le marquis ».

---

### 🚪 SALLE 3 — Le jardin des Tuileries

**📅 Contexte :** jardins du palais, lieu de rencontre des factions.

**🖼️ Décor (5 sens) :**
> *Le **soleil perce les nuages** sur les allées de sable. Des **paons** crient près d'une volière. L'**odeur des tilleuls en fleur** se mêle au **parfum de poudre de riz** laissé par les nobles qui se promènent. Au loin, des **gardes suisses** montent la garde, leurs **pas cadencés** résonnant sur les graviers. Sur un banc, un homme élégant, **le Marquis de Montclair**, feint de lire un journal. Mais ses yeux ne quittent pas votre groupe.*

**🔊 Indice sonore :** oiseaux + pas sur gravier + murmures.
**🔎 Éléments interactifs :** observer les portraits exposés ; repérer le détail caché dans la gravure de la Bastille.
**🎁 Récompense :** Fragment n°3 (mot **« FRATERNITÉ »**) + indice « Assemblée, mécanisme scellé ».

---

### 🚪 SALLE 4 — La rue en émeute (Place de la Bastille)

**📅 Contexte :** souvenir de la prise de la Bastille (14 juillet 1789), quelques semaines plus tôt.

**🖼️ Décor (5 sens) :**
> *On dirait que le combat vient à peine de cesser. La **fumée de poudre** pique encore les yeux. Des **débris de pierre** jonchent le sol, mêlés à des **débris d'affiches arrachées**. Une **odeur métallique** flotte dans l'air. Au loin, la **forteresse de la Bastille** fume, à demi démantelée. Des **volontaires de la Garde nationale** circulent en chantant. Sur une table abandonnée, des **portraits** de personnages célèbres sont éparpillés. Un fragment de **partition** s'envole au vent.*

**🔊 Indice sonore :** chants révolutionnaires + vent + cris lointains.
**🔎 Éléments interactifs :** associer les portraits aux citations ; replacer la partition dans l'ordre.
**🎁 Récompense :** Fragment n°4 (mot **« 1789 »**) + indice « mécanisme de l'Assemblée, ordre des députés ».

---

### 🚪 SALLE 5 — La salle de l'Assemblée nationale (FINALE)

**📅 Contexte :** la salle où siège l'Assemblée, jour de l'adoption de la Déclaration.

**🖼️ Décor (5 sens) :**
> *La salle est **vaste et pleine d'écho**. Des **gradins en bois** entourent une **estrade** où trône un **fauteuil de président**. L'air sent la **cire fraîche** et le **bois vernis**. Au mur, un **grand plan de la salle** porte des **symboles étranges**. Des **étiquettes** attendent sur une table : noms de députés, dates, lieux. Une **horloge** bat la mesure — *tic, tac, tic, tac* — car le temps vous est compté. Au centre du dispositif, un **mécanisme scellé** attend qu'on le déverrouille.*

**🔊 Indice sonore :** tic-tac d'horloge amplifié (pression temporelle) + murmures lointains de députés.
**🔎 Éléments interactifs :** placer les étiquettes aux bons emplacements du plan.
**🎁 Récompense :** l'**article secret** révélé par Maximilien + dénouement.

---

## 5) 🧩 LES 5 ÉNIGMES COMPLÈTES

> Chaque énigme suit la même fiche : **Support → Consigne élève → Solution → Différenciation CM1/CM2 → Adaptation dynamique**. Les supports imprimables sont en [Annexes (§13)](#13--annexes--fiches-élèves-à-imprimer).

---

### 🧩 ÉNIGME 1 — Le cahier de doléances codé *(Salle 1)*

**📜 Support :** extrait authentique (adapté) d'un cahier de doléances du tiers état. Certaines lettres sont **soulignées**.

**🗣️ Consigne élève :**
> *« Louise vous tend un vieux cahier. "Y'a un mot caché là-dedans, j'en suis sûre. Les lettres soulignées, lis-les dans l'ordre !" Lisez le texte, repérez les lettres soulignées et reconstituez le mot mystère. »*

**✅ Solution :** les lettres soulignées forment **LIBERTÉ**. (Voir Annexe A1 : lettres **L-I-B-E-R-T-É** placées en début de mots-clés.)

**🎯 Différenciation :**
- **CM1 :** les lettres sont soulignées en **rouge**, espacées tous les 2-3 mots.
- **CM2 :** lettres soulignées discrètement dans un texte plus long ; les élèves doivent d'abord **comprendre** quelles lignes sont pertinentes (indice sémantique : "lignes qui parlent de droits").

**⚡ Adaptation dynamique :**
- **Réussite < 3 min :** Louise, impressionnée, donne un **2ᵉ indice bonus** ("Le voleur boite légèrement").
- **Échec / > 5 min :** Louise **entoure** elle-même la 1ʳᵉ lettre au tableau et dit *"Commence par là"*.
- **CM1 en difficulté :** fournir la **fiche A1-bis** où le mot est déjà pré-souligné en couleur.

---

### 🧩 ÉNIGME 2 — La Marseillaise mystérieuse *(Salle 2)*

**📜 Support :** fragment de la partition de *la Marseillaise* (Rouget de Lisle, 1792 — bien que postérieure, son usage symbolique est accepté pour l'émotion) + extraits de paroles + images d'événements.

**🗣️ Consigne élève :**
> *« Maître Gutenberg a glissé une partition dans les cahiers. Associez chaque extrait de paroles à l'image qui lui correspond. Le bon ordre vous donnera un mot. »*

**✅ Solution :**
- *"Aux armes, citoyens !"* → **Prise de la Bastille**
- *"Allons enfants de la Patrie"* → **Volontaires en marche**
- *"Le jour de gloire est arrivé"* → **Drapeau tricolore hissé**

→ Les 1ʳᵉ lettres des images associées forment **B-V-D** → non ; on prend les **initiales des thèmes** : **B**astille, **V**olontaires, **D**rapeau → l'enseignant valide et remet le fragment **« ÉGALITÉ »**.

> ✏️ *Note pratique :* pour simplifier, c'est l'**enseignant** qui valide l'association correcte et remet le fragment. Le mot clé remis est **« ÉGALITÉ »**.

**🎯 Différenciation :**
- **CM1 :** association **image ↔ texte** simple, 3 paires, images explicites.
- **CM2 :** **5 couplets à remettre dans l'ordre chronologique** des événements de 1789 (États généraux → Jeu de paume → Bastille → Nuit des droits → Marche des femmes).

**⚡ Adaptation dynamique :**
- **Réussite rapide :** Maître Gutenberg pose une **question bonus** : *"Citez un droit de la Déclaration"* → bonus de points équipe.
- **Échec :** il **lit lui-même** la 1ʳᵉ association comme exemple.
- **API :** générer un court commentaire de Gutenberg sur la *Marseillaise* et son rôle.

---

### 🧩 ÉNIGME 3 — Le rébus de la Déclaration *(Salle 3)*

**📜 Support :** version simplifiée de l'**article 1** de la Déclaration des droits de l'homme et du citoyen, où des mots-clés sont remplacés par des **rébus / symboles**.

**🗣️ Consigne élève :**
> *« Le Marquis vous tend un parchemin incomplet. Déchiffrez les rébus pour reconstituer la phrase célèbre. »*

**✅ Solution (article 1 simplifié) :**
> *"Les hommes naissent **libres** et **égaux** en **droits**."*

Rébus :
- 🔓 chaîne brisée → **LIBRES**
- ⚖️ balance → **ÉGAUX**
- 📜 parchemin signé → **DROITS**

→ Le fragment remis est **« FRATERNITÉ »** (la 3ᵉ valeur, liée au personnage qui examine le cœur des joueurs).

**🎯 Différenciation :**
- **CM1 :** rébus **illustrés** et explicites (dessins clairs).
- **CM2 :** rébus **abstraits** avec jeux de mots (ex. : "égaux" illustré par deux = identiques + symbole "aux" de l'eau → jeu phonétique).

**⚡ Adaptation dynamique :**
- **Réussite brillante :** le Marquis **révèle son vrai motif** (il protège les joueurs) + bonus.
- **Échec :** il donne **un rébus résolu comme exemple**.
- **API :** générer une remarque ironique mais utile du Marquis.

---

### 🧩 ÉNIGME 4 — Les personnages clés *(Salle 4)*

**📜 Support :** portraits + courtes biographies de personnages historiques + citations.

**🗣️ Consigne élève :**
> *« Associez chaque portrait à sa citation et à l'événement qui le caractérise. Une fois le bon ordre trouvé, un code s'affiche. »*

**✅ Solution :**
- **Louis XVI** → *"J'ai peu de confiance dans les assemblées."* → **États généraux** (1789)
- **Mirabeau** → *"Allez dire à votre maître…"* → **Séance royale** (23 juin 1789)
- **Danton** → *"De l'audace, encore de l'audace…"* → **Chute de la monarchie** (1792)
- **Robespierre** → *"La vertu, sans laquelle la terreur est funeste…"* → **Terreur** (1793-94)

→ Une fois les 4 associations correctes, l'**ordre chronologique** donne le fragment **« 1789 »**.

**🎯 Différenciation :**
- **CM1 :** **4 personnages** + indices évidents (images codées par couleur).
- **CM2 :** **6 personnages** (+ Bailly, Olympe de Gouges) + indices subtils + **dates à replacer** sur une frise.

**⚡ Adaptation dynamique :**
- **Réussite :** une **fiche bonus** "Olympe de Gouges et les femmes" est remise (ouverture culturelle).
- **Échec :** l'enseignant **donne une association** comme modèle.
- **API :** générer une anecdote courte sur un personnage choisi.

---

### 🧩 ÉNIGME 5 (FINALE) — Le mécanisme de l'Assemblée *(Salle 5)*

**📜 Support :** grand **plan de la salle de l'Assemblée** avec des emplacements numérotés + **étiquettes** (noms de députés, dates, lieux) à placer.

**🗣️ Consigne élève :**
> *« Placez les étiquettes aux bons emplacements sur le plan. Le bon ordre révèle l'emplacement du manuscrit et active le mécanisme final. »*

**✅ Solution :**
1. **Président** → **Bailly** (ou Mirabeau, selon version)
2. **Tribune gauche** → **Robespierre**
3. **Tribune droite** → **Monarchiens** (Mounier)
4. **Date au fronton** → **26 août 1789**
5. **Lieu** → **Versailles** (puis Paris)

→ Le dernier emplacement révèle l'**article secret** :
> *« Art. 18 secret : Nul ne peut être accusé, arrêté ni détenu que dans les cas déterminés par la Loi. »* (librement adapté de l'esprit de l'article 7 réel).

**🎯 Différenciation :**
- **CM1 :** **5 étiquettes**, emplacements colorés, plan simplifié.
- **CM2 :** **8 étiquettes**, distinctions **gauche/droite/centre**, frise chronologique à compléter.

**⚡ Adaptation dynamique :**
- **Réussite totale :** Maximilien apparaît (API ou enseignant) pour le **dénouement solennel**.
- **Échec partiel :** un indice visuel **clignote** sur l'emplacement manquant.
- **Pression temporelle :** le tic-tac s'accélère les 5 dernières minutes.

---

## 6) 🎚️ ADAPTATION DYNAMIQUE DE LA DIFFICULTÉ

> Cette section explique **comment adapter le jeu en temps réel** grâce aux retours des joueurs et à l'API.

### Signaux observés par l'enseignant / l'API

| Signal | Signification | Action recommandée |
|---|---|---|
| Réussite < 3 min | Équipe à l'aise | Énigme suivante **plus dure** (version CM2 ou 1 indice en moins) |
| Réussite 3-7 min | Rythme idéal | Maintenir le niveau |
| Échec ou > 7 min | Difficulté | Personnage donne **un indice supplémentaire** ou énigme alternative plus simple |
| Silence prolongé | Blocage | API génère un **message d'encouragement** personnalisé |
| Agitation | Perte d'attention | Raccourcir la salle, accélérer le rythme |

### Différenciation par niveau

- **CM1 :** textes courts, consignes explicites, aides visuelles nombreuses, énigmes à 3-4 éléments.
- **CM2 :** textes plus denses, déduction, mise en relation, énigmes à 5-6 éléments, frises chronologiques.

### Mécanismes de motivation

- **⭐ Points** par énigme résolue (10 pts/salle, bonus pour rapidité).
- **🏆 Badges** : *« Esprit de la Bastille »* (vitesse), *« Avocat »* (raisonnement), *« Frère »* (coopération).
- **⏱️ Chronomètre** commun visible.
- **📊 Classement** optionnel (à manier avec prudence — privilégier la **coopération** à la compétition).

---

## 7) 🤖 USAGE DE L'API (ALBERT / DEEPSEEK)

> L'API **enrichit** les dialogues et **personnalise** l'expérience. Elle n'est **jamais obligatoire** : les dialogues-clés sont déjà écrits en [§3](#3--personnages-et-dialogues).

### Quand solliciter l'API

| Moment | Type de requête |
|---|---|
| Accueil d'un personnage | Génération d'une **phrase d'accroche** variant selon l'équipe |
| Réussite d'une énigme | **Félicitations personnalisées** + indice suivant |
| Échec / tâtonnement | **Indice supplémentaire** formulé avec la voix du personnage |
| Bilan final | **Résumé narratif** des exploits de l'équipe |
| Différenciation | Génération de **variantes** d'énigme (CM1 / CM2) |

### Modèle de prompt réutilisable

Copiez-collez ce squelette dans Albert ou DeepSeek, en remplaçant les `[...]` :

```
Tu vas incarner un personnage d'un escape game sur la Révolution française,
destiné à des élèves de [CM1 / CM2].

PERSONNAGE : [Louise / Gutenberg / Marquis / Maximilien]
VOIX : [cf. §3 de la fiche personnage]
SITUATION : Les joueurs viennent de [réussir / échouer / tâtonner] l'énigme
[1 cahier de doléances / 2 Marseillaise / 3 rébus / 4 portraits / 5 Assemblée].

CONTEXTE ÉQUIPE :
- Niveau : [CM1 / CM2]
- Temps écoulé : [X] minutes
- Indice déjà donné : [oui/non]

TÂCHE : Rédige un dialogue de [2 à 4 phrases] dans la voix du personnage.
- Si réussite : félicite ET donne l'indice suivant.
- Si échec : reformule la consigne avec un indice concret.
- Garde un ton adapté à des [8-9 ans / 10-11 ans].
- N'invente aucun fait historique faux.
```

### Exemples concrets prêts à l'emploi

**Exemple A — Louise, réussite rapide (CM2) :**
```
PERSONNAGE : Louise (12 ans, tutoie, vive, expressions d'époque).
SITUATION : Les joueurs ont trouvé "LIBERTÉ" en 2 min 30.
TÂCHE : Félicite-les avec émerveillement, donne l'indice "imprimerie rue de la Harpe",
et ajoute un conseil bonus car ils ont été rapides.
```
*Réponse attendue :* *« Palsambleu, vous êtes des phénomènes ! Deux minutes, à peine ! Prenez ce fragment, et écoutez : le voleur est passé chez Gutenberg, rue de la Harpe. Un conseil bonus, parce que vous le méritez — il boite légèrement. Filez ! »*

**Exemple B — Gutenberg, échec (CM1) :**
```
PERSONNAGE : Maître Gutenberg (grave, cite les Lumières, vouvoie).
SITUATION : Les joueurs n'arrivent pas à associer les couplets de la Marseillaise.
TÂCHE : Reformule la consigne simplement, donne un exemple concret,
encourage sans brusquer. Niveau CM1 (8-9 ans).
```
*Réponse attendue :* *« Patience, jeunes amis. Regardez bien : le refrain dit "Aux armes, citoyens !". À quelle image cela vous fait-il penser ? À des combattants qui prennent une forteresse, n'est-ce pas ? Associez ce refrain à l'image de la Bastille. Maintenant, essayez les autres. »*

**Exemple C — Marquis, réussite brillante (CM2) :**
```
PERSONNAGE : Marquis de Montclair (hautain, ironique, en réalité protecteur).
SITUATION : Les joueurs ont déchiffré tous les rébus.
TÂCHE : Révèle que vous cherchez aussi le manuscrit mais pour le protéger,
donnez le fragment, et lancez-les vers l'Assemblée avec un avertissement.
```

**Exemple D — Maximilien, bilan final :**
```
PERSONNAGE : Maximilien (jeune avocat, sérieux, solennel).
SITUATION : Les joueurs ont retrouvé les 4 fragments et résolu le mécanisme.
TÂCHE : Rédige le discours de clôture solennel, cite l'article secret,
félicite l'équipe et rappelle la valeur de la Déclaration.
```

### ⚠️ Précautions avec l'API

- **Vérifier** chaque réponse générée (exactitude historique).
- **Filtrer** tout contenu inadapté (violence, anachronisme).
- **Préparer un plan B** : les dialogues écrits en §3 suffisent en cas de panne.
- **Ne pas laisser l'API seule** avec les élèves : toujours un enseignant présent.

---

## 8) ⏱️ DÉROULLÉ MINUTE PAR MINUTE

**Durée totale : 55 minutes** (+ 5 min de bilan). Pour une classe entière au TBI, doubler les temps de recherche et viser 60-70 min.

| ⏱️ Min | Phase | Action enseignant | Action API |
|---|---|---|---|
| 0-2 | **Accueil** | Présenter la mission, lancer le minuteur | Maximilien : discours d'intro |
| 2-3 | **Transition salle 1** | Lire le décor du Palais-Royal, distribuer A1 | Louise : phrase d'accroche |
| 3-12 | **Énigme 1** (10 min) | Observer, aider si blocage | Louise : réaction selon réussite |
| 12-13 | **Transition salle 2** | Lire le décor imprimerie, distribuer A2 | Gutenberg : accueil + question |
| 13-22 | **Énigme 2** (10 min) | Valider les associations | Gutenberg : commentaire Marseillaise |
| 22-23 | **Transition salle 3** | Lire décor Tuileries, distribuer A3 | Marquis : entrée théâtrale |
| 23-32 | **Énigme 3** (10 min) | Aider à déchiffrer les rébus | Marquis : indice ou révélation |
| 32-33 | **Transition salle 4** | Lire décor Bastille, distribuer A4 | — (ambiance sonore) |
| 33-42 | **Énigme 4** (10 min) | Valider les portraits | API : anecdote sur un personnage |
| 42-43 | **Transition salle 5** | Lire décor Assemblée, distribuer A5 | Tic-tac amplifié (pression) |
| 43-52 | **Énigme finale** (10 min) | Aider au placement des étiquettes | Maximilien : apparaît si blocage |
| 52-55 | **Dénouement** | Révéler l'article secret | Maximilien : discours de clôture |
| 55-60 | **Bilan + quizz** | Lancer le quizz [§10](#10--bilan-final-et-quizz) | API : résumé narratif (optionnel) |

### Gestion du temps

- **Minuteur visible** dès la minute 0 (projecteur / TBI / téléphone).
- **Clochette ou sifflet** à chaque transition (toutes les 10 min).
- **5 dernières minutes** : tic-tac accéléré pour la pression dramatique (à doser selon le groupe).

---

## 9) 📋 GRILLE D'ÉVALUATION DES COMPÉTENCES

> À remplir **par équipe** ou **par élève**. Cocher la case correspondante.

### Grille par équipe (1 ligne par équipe)

| Équipe | Connaissances historiques *(/5)* | Lecture / déduction *(/5)* | Coopération / écoute *(/5)* | Réussite globale *(/5)* | **Total /20** |
|---|:---:|:---:|:---:|:---:|:---:|
| | | | | | |
| | | | | | |
| | | | | | |

### Grille détaillée par élève

| Compétence observée | 🟢 Acquis | 🟡 En cours | 🔴 À renforcer |
|---|:---:|:---:|:---:|
| **Se repérer dans le temps** (dates-clés de 1789) | | | |
| **Connaître** les événements (États généraux, Bastille, Déclaration) | | | |
| **Reconnaître** les personnages (Louis XVI, Mirabeau, Danton, Robespierre) | | | |
| **Comprendre** liberté / égalité / fraternité | | | |
| **Lire** un document d'époque adapté | | | |
| **Déduire** à partir d'indices | | | |
| **Coopérer** : écouter, argumenter, se répartir les tâches | | | |
| **Présenter** oralement un résultat | | | |

### Badges attribuables

- 🥖 **Badge "Esprit de la Bastille"** : équipe la plus rapide sur une énigme.
- ⚖️ **Badge "L'Avocat"** : raisonnement le plus clair.
- 🤝 **Badge "Fraternité"** : meilleure coopération observée.
- 📚 **Badge "Lettre et Lumière"** : meilleure lecture de document.

---

## 10) 🎯 BILAN FINAL ET QUIZZ

### Bilan oral (3 min)

Questions à poser à la classe entière :
1. *Avez-vous retrouvé le manuscrit ? Quel était l'article secret ?*
2. *Qu'avez-vous appris sur 1789 ?*
3. *Quelle énigme avez-vous préférée ? Pourquoi ?*

### Quizz final (5 questions — validation des acquis)

> **Réponses en bas.**

**Q1.** Quand a été adoptée la Déclaration des droits de l'homme et du citoyen ?
- a) 14 juillet 1789
- b) 26 août 1789
- c) 21 janvier 1793

**Q2.** Que signifie "liberté" dans la Déclaration ?
- a) Faire tout ce qu'on veut
- b) Pouvoir agir sans nuire aux droits des autres
- c) Ne plus avoir de lois

**Q3.** Qui prend la Bastille le 14 juillet 1789 ?
- a) Le roi et ses gardes
- b) Le peuple parisien
- c) L'armée anglaise

**Q4.** Qu'est-ce qu'un "cahier de doléances" ?
- a) Un cahier d'écolier
- b) Un texte où le peuple exprime ses plaintes au roi
- c) Un journal intime

**Q5.** Quel symbole représente l'égalité dans la Révolution ?
- a) La balance ⚖️
- b) La couronne 👑
- c) L'épée 🗡️

**✅ Réponses :** 1-b, 2-b, 3-b, 4-b, 5-a.

---

## 11) 📚 PROLONGEMENTS PÉDAGOGIQUES

- **✍️ Production d'écrit :** rédiger un **article de journal** (1789) sur la découverte du manuscrit.
- **🎭 Théâtre :** jouer un dialogue entre deux personnages (Louise / Marquis).
- **🎨 Arts visuels :** créer une **affiche révolutionnaire** ("Liberté, Égalité, Fraternité").
- **🗺️ Géographie / histoire :** situer les lieux parisiens sur un plan (Palais-Royal, Bastille, Tuileries).
- **👩‍🏫 Éducation à l'égalité :** étudier **Olympe de Gouges** et la *Déclaration des droits de la femme et de la citoyenne* (1791).
- **🔗 EMC :** débat — *"Quels droits sont encore à défendre aujourd'hui ?"*

---

## 12) 🛡️ GESTION DE CLASSE ET SÉCURITÉ

### Avant la séance

- **Tester l'API** une fois (avec les prompts de la [§7](#7--usage-de-lapi-albert--deepseek)) pour vérifier la pertinence des réponses.
- **Imprimer** les annexes (1 jeu par équipe).
- **Préparer** 5 enveloppes avec les fragments / indices.
- **Vérifier** la connexion internet et le matériel son.

### Pendant la séance

- **Toujours valider** les contenus générés par l'API avant de les lire à la classe.
- **Ne jamais laisser** les élèves interagir seuls avec l'API (l'enseignant est l'interface).
- **Adapter le fond sonore** au niveau d'attention : baisser si agitation, couper si besoin.
- **Gérer la pression temporelle** : si une équipe panique, stopper le minuteur et rassurer.

### Liens sonores suggérés (à vérifier avant usage)

- *Ambiance pluie ville* — nombreux extraits libres sur YouTube.
- *Presse d'imprimerie ancienne* — sons libres (Freesound, CC).
- *Chants révolutionnaires (la Marseillaise, Ça ira)* — versions instrumentales libres.
- *Tic-tac d'horloge* — pour la pression finale.

> ⚠️ **Toujours** vérifier les droits d'utilisation et prévisualiser les contenus avant diffusion en classe.

### En cas de panne d'API

1. **Rassurer** la classe : *"Le voyage dans le temps a un petit bug, mais l'aventure continue !"*
2. **Lire** les dialogues écrits en [§3](#3--personnages-et-dialogues) (ils suffisent à animer toute la séance).
3. **Continuer** normalement les énigmes papier.

---

## 13) 🖨️ ANNEXES — FICHES ÉLÈVES À IMPRIMER

> Une fiche par énigme. Imprimer **1 jeu complet par équipe**. Les cases 🔴 correspondent aux lettres soulignées à repérer.

---

### 📄 ANNEXE A1 — Le cahier de doléances codé *(Salle 1)*

**Consigne :** *« Lis le texte. Certaines lettres sont soulignées en rouge. Note-les dans l'ordre, elles forment un mot. »*

```
Texte du cahier de doléances du tiers état (adapté) :

[🔴L]es habitants de la paroisse demandent que l'on
[🔴i]mpose également riches et pauvres, car
[🔴b]eaucoup souffrent des taxes injustes. Que
[🔴e]nfin la justice soit la même pour tous, et que
[🔴r]ègne la liberté dans le royaume. Nous souhaitons
[🔴t]erminer les privilèges des nobles, afin que
[🔴é]galité soit réelle entre tous les Français.
```

**Mot mystère :** _ _ _ _ _ _ _  *(7 lettres)*

**Grille de réponse (CM1) :** dessiner 7 cases vides à remplir.

> 🔑 **Pour l'enseignant — Solution :** **L – I – B – E – R – T – É**
> Fragment remis : **« LIBERTÉ »**

---

### 📄 ANNEXE A1-bis — Version simplifiée CM1 (pré-soulignée)

*« Voici les lettres que Louise a déjà repérées pour toi. Remets-les dans l'ordre ! »*

```
_ _ _ _ _ _ _

Lettres mélangées :  É  R  I  L  B  T  É

Indice : ça veut dire "ne pas être prisonnier".
```

> 🔑 Solution : **LIBERTÉ**

---

### 📄 ANNEXE A2 — La Marseillaise mystérieuse *(Salle 2)*

**Consigne :** *« Relie chaque extrait de paroles à la bonne image. »*

| Extrait de paroles | → | Image (à découper) |
|---|:---:|---|
| 1. *"Aux armes, citoyens !"* | → | 🏰 Bastille attaquée |
| 2. *"Allons enfants de la Patrie"* | → | 🚶 Volontaires en marche |
| 3. *"Le jour de gloire est arrivé"* | → | 🚩 Drapeau tricolore hissé |

**Pour les CM2 — ordre chronologique des couplets :**
> Replace ces 5 événements dans l'ordre :
> - Prise de la Bastille *(14 juillet 1789)*
> - Marche des femmes *(5 octobre 1789)*
> - États généraux *(mai 1789)*
> - Adoption de la Déclaration *(26 août 1789)*
> - Serment du Jeu de paume *(20 juin 1789)*

> 🔑 **Solution CM2 :** États généraux → Jeu de paume → Bastille → Déclaration → Marche des femmes.
> Fragment remis : **« ÉGALITÉ »**

---

### 📄 ANNEXE A3 — Le rébus de la Déclaration *(Salle 3)*

**Consigne :** *« Déchiffre les rébus pour compléter la phrase célèbre. »*

> *« Les hommes naissent [🔓] et [⚖️] en [📜]. »*

**Rébus à déchiffrer :**

| Symbole | Mot attendu |
|:---:|---|
| 🔓 (chaîne brisée) | _______ |
| ⚖️ (balance) | _______ |
| 📜 (parchemin signé) | _______ |

**Pour les CM2 — rébus plus abstraits :**
- 🔓 + 🔁 → *libre* (répétition de "libre")
- = (signe égal) + eau (eau) → *égaux* (jeu phonétique)
- ✍️ + ⚖️ → *droits* (droit écrit)

> 🔑 **Solution :** *« Les hommes naissent **LIBRES** et **ÉGAUX** en **DROITS**. »* (Article 1, adapté)
> Fragment remis : **« FRATERNITÉ »**

---

### 📄 ANNEXE A4 — Les personnages clés *(Salle 4)*

**Consigne :** *« Associe chaque portrait à sa citation et à son événement. Puis range-les dans l'ordre chronologique. »*

| Portrait | Citation | Événement | Date |
|---|---|---|---|
| 👑 **Louis XVI** | *"J'ai peu de confiance dans les assemblées."* | États généraux | 1789 |
| 🎤 **Mirabeau** | *"Allez dire à votre maître que nous sommes ici par la volonté du peuple."* | Séance royale | 23 juin 1789 |
| 🔊 **Danton** | *"De l'audace, encore de l'audace, toujours de l'audace."* | Chute de la monarchie | 1792 |
| ⚖️ **Robespierre** | *"La vertu, sans laquelle la terreur est funeste."* | La Terreur | 1793-1794 |

**Pour les CM2 — personnages supplémentaires :**
- 🏛️ **Bailly** — premier maire de Paris — *14 juillet 1789*
- ✒️ **Olympe de Gouges** — *Déclaration des droits de la femme* — *1791*

> 🔑 **Solution (ordre chronologique) :** Louis XVI → Mirabeau → Danton → Robespierre.
> Fragment remis : **« 1789 »**

---

### 📄 ANNEXE A5 — Le mécanisme de l'Assemblée *(Salle 5 — Finale)*

**Consigne :** *« Place les étiquettes aux bons emplacements sur le plan. Le bon ordre révèle l'emplacement du manuscrit. »*

**Plan de la salle (à dessiner au tableau ou projeter) :**

```
            ╔══════════════════════════════╗
            ║   [1] ___________ (Président) ║
            ╠══════════════════════════════╣
   [2] ____   ║        TRIBUNE        ║   [3] ____
  (Gauche)    ║   ╔══════════════╗    ║  (Droite)
            ║   ║  MANUSCRIT ?  ║    ║
            ║   ╚══════════════╝    ║
            ╠══════════════════════════════╣
            ║   [4] Date : ______________ ║
            ║   [5] Lieu : ______________ ║
            ╚══════════════════════════════╝
```

**Étiquettes à placer :**
1. Président → **Bailly** *(ou Mirabeau)*
2. Tribune gauche → **Robespierre**
3. Tribune droite → **Monarchiens / Mounier**
4. Date → **26 août 1789**
5. Lieu → **Versailles** *(puis Paris)*

**Pour les CM2 — étiquettes supplémentaires :**
6. Centre → **Mirabeau**
7. Tribune du fond → **Danton**
8. Secrétaire → **Olympe de Gouges** *(rôle fictif pour inclusion)*

> 🔑 **Une fois toutes les étiquettes placées, l'enseignant révèle l'article secret :**
>
> 📜 **Article 18 secret :**
> *« Nul ne peut être accusé, arrêté ni détenu que dans les cas déterminés par la Loi et selon les formes qu'elle a prescrites. »* *(Librement adapté de l'esprit de l'article 7 réel.)*

---

### 📄 FEUILLE D'ÉQUIPE (à distribuer en début de jeu)

```
┌─────────────────────────────────────────────┐
│  🏛️ LE SECRET DE LA DÉCLARATION             │
│  Équipe : ____________________________       │
│  Niveau :  CM1 ☐   CM2 ☐                   │
├─────────────────────────────────────────────┤
│  FRAGMENTS RECOLTÉS :                       │
│   □ Salle 1 : ____________ (LIBERTÉ)        │
│   □ Salle 2 : ____________ (ÉGALITÉ)        │
│   □ Salle 3 : ____________ (FRATERNITÉ)     │
│   □ Salle 4 : ____________ (1789)           │
│  ARTICLE SECRET RETROUVÉ : ☐               │
├─────────────────────────────────────────────┤
│  POINTS :  ___ / 50                         │
│  BADGES :  ☐ Bastille  ☐ Avocat  ☐ Fraternité  ☐ Lumière │
│  TEMPS TOTAL :  ______ min                  │
└─────────────────────────────────────────────┘
```

---

## ✅ DOCUMENT PRÊT À L'EMPLOI

Ce script contient tout ce qu'il faut pour animer **« Le Secret de la Déclaration »** :
- 📖 Le scénario complet et l'objectif pédagogique
- 🏰 Les 5 salles immersives (5 sens + son)
- 🗣️ Les 4 personnages avec dialogues types
- 🧩 Les 5 énigmes complètes avec solutions et différenciation
- 🤖 Les instructions API prêtes à copier-coller
- ⏱️ Le déroulé minute par minute
- 📋 La grille d'évaluation et le quizz
- 🖨️ Les fiches élèves imprimables (Annexes A1 à A5 + feuille d'équipe)

**Bonne aventure, apprentis historiens ! 🏛️⚡**
