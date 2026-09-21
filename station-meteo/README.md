# 🌦️ La Station météo disparue

Escape game de **sciences et technologie** pour le **CM1** et le **CM2** (cycle 3), sur les
**mesures météorologiques** : lire un thermomètre, un anémomètre, une girouette et un
pluviomètre, organiser des relevés et les exploiter pour prévoir.

- ▶ **Jouer en ligne** : https://idgir.github.io/escape-games-cm1-cm2/station-meteo/
- 📖 **Guide pédagogique** : [GUIDE-PEDAGOGIQUE.md](GUIDE-PEDAGOGIQUE.md)
- 🎞️ **Médias facultatifs** : [assets/README.md](assets/README.md)
- ✅ **Points à contrôler** : [A-VERIFIER.md](A-VERIFIER.md)

| | |
|---|---|
| Programme | Sciences et technologie, cycle 3 — *La planète Terre* : réaliser et exploiter des mesures météorologiques en utilisant des capteurs (thermomètre, anémomètre, pluviomètre) |
| Progression de l'enseignant | Année A, période 1 — jeu n°03 |
| Durée | 60 à 75 minutes, ou cinq séances de 25 minutes |
| Énigmes | **15 en CM1** (3 par module), **20 en CM2** (4 par module) |
| Score maximal | **100 en CM1**, **125 en CM2** ; un indice coûte 2 points |
| Types d'énigmes | les 10 types du moteur + le type `instrument`, propre à ce jeu (11 en CM2, 10 en CM1) |
| Médias | aucun n'est nécessaire : décors et personnages dessinés en SVG et animés |
| Réseau | aucun : pas de CDN, pas de police distante, pas de bibliothèque externe |

## L'histoire

Un orage a traversé la nuit. Au matin, la station météo de l'école ne donne plus rien de
cohérent : le thermomètre a été sorti de son abri, la girouette a perdu ses points
cardinaux, le pluviomètre déborde et le cahier de relevés est trempé. La classe part en
sortie : il faut un bulletin. Les élèves, techniciens de **Météo-Junior**, remettent en
service les cinq modules de la station, dans l'ordre.

Chaque module rendu à la vie donne un **mot-clé**. Ensemble, ils forment la devise du
prévisionniste : **« MESURER, ORIENTER, CUMULER, ORGANISER — pour PRÉVOIR. »**
Le dernier cadenas s'ouvre avec la **valeur de vérité** de mercredi, le jour de l'orage :
trois mesures lues correctement dans les modules 1, 2 et 3 (**21 °C · 24 km/h · 7 mm**).

## Les 5 modules

| | Lieu | Notion | Personnage | Mot-clé |
|---|---|---|---|---|
| 1 | L'abri météo, dans la cour | Le thermomètre : lire une température (positive, négative), minimum et maximum, mesurer à l'ombre, sous abri, à 1,50 m | Madame Vasseur, prévisionniste | MESURER |
| 2 | Le mât du vent | L'anémomètre et la girouette : direction, vitesse, rose des vents, échelle de Beaufort | Capitaine Keïta, marin | ORIENTER |
| 3 | Le pluviomètre, au jardin | Hauteur de pluie en mm, 1 mm = 1 L/m², lecture graduée, cumul | Tiago, technicien | CUMULER |
| 4 | Le bureau des relevés | Tableau à double entrée, minimum, maximum, écart, cumul, valeur aberrante, diagramme | Lina, élève responsable de la station | ORGANISER |
| 5 | La salle de prévision | Des mesures au bulletin ; météo et climat | Madame Vasseur, puis Lina | PRÉVOIR |

### Des données cohérentes d'un module à l'autre

Toutes les valeurs chiffrées du jeu viennent d'une **station fictive** (aucune valeur
météorologique « réelle » n'est inventée) :

| | Lun | Mar | Mer | Jeu | Ven |
|---|---|---|---|---|---|
| Minimum (°C) | 9 | 11 | 12 | 8 | 7 |
| Maximum (°C) | 17 | 19 | **21** | 14 | 16 |
| Vent moyen (km/h) | 12 | 18 | **24** (ouest) | 30 | 8 |
| Pluie (mm) | 0 | 3 | **7** | 12 | 0 |

Les conventions de mesure, elles, sont réelles et sourcées (voir « Sources »).

## Énigmes et solutions

<details>
<summary>⚠️ Solutions — à ne pas projeter en classe</summary>

### Module 1 — L'abri météo · mot-clé **MESURER**

**1-1 · Lire le thermomètre** — type `instrument` — CM1 et CM2 — leçon `thermometre`

- CM1 : Mercredi, 8 h → **12 °C**; Mercredi, midi → **18 °C**; Mercredi, 15 h → **21 °C**
- CM2 : Mercredi, 8 h → **12 °C**; Mercredi, 15 h → **21 °C**; Un matin de janvier → **−4 °C**; Règle : une nuit de gel à −3 °C → **−3 °C** (à régler)
- Correction : On lit le nombre de la graduation où s'arrête le haut du liquide. Sous zéro, on compte vers le bas et on écrit le signe moins : −4 °C se lit « moins quatre degrés ». Mercredi, la température la plus haute était de 21 °C, à 15 h.

**1-2 · Où placer le thermomètre ?** — type `qcm` — CM1 et CM2 — leçon `thermometre`

- CM1 : Pour mesurer la température de l'air, le thermomètre doit être… → **à l'ombre, dans son abri**; À quelle hauteur place-t-on le thermomètre dans l'abri ? → **à 1,50 m du sol**; Pourquoi l'abri météo est-il blanc ? → **pour renvoyer la lumière du soleil**
- CM2 : Pourquoi l'abri est-il percé d'ouvertures (des persiennes) ? → **pour que l'air circule autour du capteur**; Deux écoles comparent leurs températures. Pourquoi mesurent-elles toutes les deux à 1,50 m, sous abri ? → **pour que leurs mesures soient comparables**; La température maximale d'une journée, c'est… → **la température la plus haute relevée ce jour-là**
- Correction : Météo-France mesure la température de l'air sous abri, à 1,50 m du sol, dans un abri blanc et percé d'ouvertures. L'abri laisse passer l'air mais protège le capteur du soleil et de la pluie : ainsi, on mesure bien l'air, et toutes les stations peuvent comparer leurs relevés.

**1-3 · Du plus froid au plus chaud** — type `ordre` — CM1 et CM2 — leçon `thermometre`

- CM1 : 7 °C → 12 °C → 16 °C → 18 °C → 21 °C
- CM2 : −6 °C → −1 °C → 0 °C → 7 °C → 12 °C → 21 °C
- Correction : Pour comparer des températures, on les place sur la graduation du thermomètre : plus on est bas, plus il fait froid. −6 °C est plus froid que −1 °C, qui est plus froid que 0 °C.

**1-4 · Mesure fiable ou mesure faussée ?** — type `tri` — CM2 — leçon `thermometre`

- CM2 : **Mesure fiable** : Léo lit le thermomètre dans l'abri, à 1,50 m, tous les jours à 8 h. / Sara attend deux minutes avant de lire, sans toucher le thermomètre. / Noé note aussi le jour et l'heure à côté de chaque mesure. ; **Mesure faussée** : Inès tient le thermomètre serré dans sa main pendant la lecture. / Hugo pose le thermomètre sur le muret, en plein soleil. / Maëlle accroche le thermomètre contre le mur de la cantine, près de la sortie d'air chaud.
- Correction : Une mesure fiable se fait à l'ombre, sous abri ventilé, à 1,50 m, loin d'une source de chaleur, et toujours de la même façon (même lieu, même heure). Un thermomètre tenu à la main, posé au soleil ou près d'un mur chaud mesure autre chose que l'air.

### Module 2 — Le mât du vent · mot-clé **ORIENTER**

**2-1 · La rose des vents** — type `plan` — CM1 et CM2 — leçon `vent`

- CM1 : Là où le soleil se lève le matin → **Est**; Là où le soleil se couche le soir → **Ouest**; Là où se trouve le soleil à midi, en France → **Sud**; À l'opposé du soleil de midi → **Nord**
- CM2 : Branche 1 → **Nord**; Branche 2 → **Nord-Est**; Branche 3 → **Est**; Branche 4 → **Sud-Est**; Branche 5 → **Sud**; Branche 6 → **Sud-Ouest**; Branche 7 → **Ouest**; Branche 8 → **Nord-Ouest**
- Correction : Le soleil se lève à l'est et se couche à l'ouest ; en France, à midi, il est au sud. Le nord est à l'opposé. Entre deux points cardinaux, on nomme les directions intermédiaires : nord-est, sud-est, sud-ouest, nord-ouest.

**2-2 · Girouette et anémomètre** — type `vraifaux` — CM1 et CM2 — leçon `vent`

- CM1 : La girouette indique d'où vient le vent. → **Vrai**; L'anémomètre mesure la vitesse du vent. → **Vrai**; Un vent d'ouest souffle vers l'ouest. → **Faux**; La vitesse du vent se mesure en degrés. → **Faux**
- CM2 : La girouette indique d'où vient le vent. → **Vrai**; Un vent d'ouest souffle vers l'ouest. → **Faux**; Mercredi, l'anémomètre indique 24 km/h : c'est une jolie brise, force 4 sur l'échelle de Beaufort. → **Vrai**; Pour une mesure fiable, on place l'anémomètre au ras du sol, à l'abri des murs. → **Faux**; Un vent de 1 m/s correspond à 3,6 km/h. → **Vrai**; La rafale est la vitesse moyenne du vent sur dix minutes. → **Faux**
- Correction : La girouette indique la direction d'où vient le vent ; l'anémomètre mesure sa vitesse, en km/h ou en m/s. Un vent d'ouest vient de l'ouest. Pour être comparables, les mesures de vent se font à 10 m de haut, en terrain dégagé.

**2-3 · L'échelle de Beaufort** — type `association` — CM1 et CM2 — leçon `vent`

- CM1 : Calme : moins de 1 km/h ↔ La fumée monte tout droit.; Légère brise : 6 à 11 km/h ↔ On sent le vent sur le visage, les feuilles frémissent.; Jolie brise : 20 à 28 km/h (mercredi : 24 km/h) ↔ La poussière se soulève, les petites branches bougent sans arrêt.; Vent frais : 39 à 49 km/h ↔ Les grosses branches s'agitent, le parapluie se tient mal.
- CM2 : Force 0 · moins de 1 km/h ↔ La fumée monte verticalement.; Force 2 · 6 à 11 km/h ↔ On sent le vent sur le visage, les feuilles frémissent.; Force 4 · 20 à 28 km/h ↔ La poussière se soulève, les petites branches bougent sans arrêt.; Force 6 · 39 à 49 km/h ↔ Les grosses branches s'agitent, les fils tendus sifflent.; Force 12 · 118 km/h et plus ↔ Ouragan : des dégâts très importants.
- Correction : L'échelle de Beaufort classe le vent de 0 (calme) à 12 (ouragan), d'après sa vitesse et ses effets visibles. Mercredi, à 24 km/h, le vent était de force 4 : une jolie brise.

**2-4 · Le carnet du capitaine** — type `trous` — CM2 — leçon `vent`

- CM2 : Mots attendus, dans l'ordre : **direction**, **anémomètre**, **vitesse**, **10 m**, **rafale**
- Correction : La girouette donne la direction d'où vient le vent, l'anémomètre sa vitesse. On les installe à 10 m au-dessus d'un terrain dégagé. La vitesse retenue est une moyenne sur dix minutes ; une pointe brève et plus forte s'appelle une rafale.

### Module 3 — Le pluviomètre · mot-clé **CUMULER**

**3-1 · Lire le pluviomètre** — type `instrument` — CM1 et CM2 — leçon `pluie`

- CM1 : Mardi matin → **3 mm**; Mercredi matin → **7 mm**; Jeudi matin → **12 mm**
- CM2 : Mercredi matin → **7 mm**; Jeudi matin → **12 mm**; Pluviomètre du jardin partagé → **4,5 mm**; Règle : 9,5 mm → **9,5 mm** (à régler)
- Correction : On lit la graduation qui touche le haut de l'eau, les yeux bien en face. Mercredi, le pluviomètre indiquait 7 mm de pluie tombée en 24 heures.

**3-2 · Un millimètre de pluie** — type `qcm` — CM1 et CM2 — leçon `pluie`

- CM1 : Dans quelle unité lit-on une hauteur de pluie ? → **en millimètres (mm)**; Où installe-t-on le pluviomètre ? → **dans un endroit dégagé, loin des arbres et des murs**; 1 mm de pluie, cela représente… → **1 litre d'eau sur chaque mètre carré**
- CM2 : Pourquoi Tiago vide-t-il le pluviomètre chaque matin, après la lecture ? → **pour mesurer la pluie de chaque journée séparément**; Pourquoi ne faut-il pas installer le pluviomètre près d'un mur ? → **le mur peut arrêter la pluie ou la renvoyer vers le tube**; La cour mesure 200 m². Mercredi, il est tombé 7 mm. Combien de litres d'eau sont tombés sur la cour ? → **1 400 litres**
- Correction : Une hauteur de 1 mm d'eau sur une surface de 1 m² représente 1 litre (1 mm × 1 m² = 1 dm³). Le pluviomètre s'installe dans un endroit dégagé, loin des arbres et des murs, et on le vide après chaque lecture.

**3-3 · Du plus sec au plus arrosé** — type `ordre` — CM1 et CM2 — leçon `pluie`

- CM1 : Lundi : 0 mm → Mardi : 3 mm → Mercredi : 7 mm → Jeudi : 12 mm
- CM2 : Une bruine : 0,5 mm → Mardi : 3 mm → Mercredi : 7 litres tombés sur 1 m² → Jeudi : 12 mm → Un orage d'été : 15 litres tombés sur 1 m²
- Correction : Pour comparer des pluies, on compare leurs hauteurs en millimètres. Comme 1 L/m² = 1 mm, 7 litres tombés sur 1 m² font 7 mm, et 15 litres sur 1 m² font 15 mm.

**3-4 · Le cadenas du cumul** — type `code` — CM2 — leçon `pluie`

- CM2 : Cumul de la semaine (en mm) → **22**; Litres tombés mercredi sur le potager de 10 m² → **70**
- Correction : Le cumul est la somme des hauteurs : 0 + 3 + 7 + 12 + 0 = 22 mm. Mercredi, 7 mm sur 10 m² : 7 × 10 = 70 litres.

### Module 4 — Le tableau des relevés · mot-clé **ORGANISER**

**4-1 · Les cases effacées** — type `plan` — CM1 et CM2 — leçon `releves`

- CM1 : Case A : minimum de mardi → **11 °C**; Case B : maximum de mercredi → **21 °C**; Case C : vent de mercredi → **24 km/h**; Case D : pluie de jeudi → **12 mm**
- CM2 : Case A : minimum de mardi → **11 °C**; Case B : maximum de mercredi → **21 °C**; Case C : vent de mercredi → **24 km/h**; Case D : pluie de jeudi → **12 mm**; Case E : écart de mercredi → **9 °C**
- Correction : Dans un tableau à double entrée, chaque case croise une ligne (la grandeur mesurée) et une colonne (le jour). L'unité dépend de la ligne : °C pour la température, km/h pour le vent, mm pour la pluie. L'écart de mercredi vaut 21 − 12 = 9 °C.

**4-2 · La valeur impossible** — type `intrus` — CM1 et CM2 — leçon `releves`

- CM1 : Intrus : **Jeudi : 41 °C maximum**
- CM2 : Intrus : **Jeudi minimum 14 °C · maximum 8 °C**
- Correction : Une valeur aberrante est une mesure qui ne peut pas être juste : trop éloignée des autres, ou impossible (un minimum ne peut pas être plus élevé que le maximum du même jour). On ne la garde pas : on cherche d'où vient l'erreur.

**4-3 · Ce que dit le tableau** — type `trous` — CM1 et CM2 — leçon `releves`

- CM1 : Mots attendus, dans l'ordre : **7 °C**, **21 °C**, **14 °C**, **jeudi**
- CM2 : Mots attendus, dans l'ordre : **7 °C**, **21 °C**, **14 °C**, **22 mm**, **2**, **jeudi**
- Correction : Le minimum de la semaine est la plus petite valeur (7 °C, vendredi), le maximum la plus grande (21 °C, mercredi) ; l'écart est la différence : 21 − 7 = 14 °C. Le cumul de pluie est la somme : 22 mm.

**4-4 · Le graphique de la pluie** — type `qcm` — CM2 — leçon `releves`

- CM2 : Quel jour a été le plus arrosé ? → **jeudi**; Combien de millimètres de plus sont tombés jeudi que mercredi ? → **5 mm**; Combien de jours sans pluie compte cette semaine ? → **2**
- Correction : Dans un diagramme en barres, la hauteur de chaque barre se lit sur l'axe gradué. Jeudi (12 mm) a reçu 5 mm de plus que mercredi (7 mm). Lundi et vendredi n'ont pas de barre : il n'a pas plu.

### Module 5 — Le bulletin du jour · mot-clé **PRÉVOIR**

**5-1 · Météo ou climat ?** — type `tri` — CM1 et CM2 — leçon `bulletin`

- CM1 : **Météo** : Demain, il pleuvra l'après-midi. / Ce matin, il fait 12 °C dans la cour. / Mercredi, le vent soufflait à 24 km/h. ; **Climat** : Au Sahara, il pleut très peu tout au long de l'année. / En général, il pleut plus à Brest qu'à Marseille. / Chez nous, l'hiver est en général plus froid que l'été.
- CM2 : **Météo** : Demain, il pleuvra l'après-midi. / Ce matin, il fait 12 °C dans la cour. / Cette nuit, un orage a déréglé la station. / Jeudi, le vent a soufflé à 30 km/h. ; **Climat** : Au Sahara, il pleut très peu tout au long de l'année. / En moyenne, il pleut plus à Brest qu'à Marseille. / Les « normales » de température sont calculées sur trente ans. / Chez nous, les hivers sont en général plus froids que les étés.
- Correction : La météo décrit le temps qu'il fait à un endroit et à un moment donnés : il change d'heure en heure. Le climat décrit le temps habituel d'une région, calculé comme une moyenne sur une longue période (trente ans pour les climatologues).

**5-2 · Prévoir la sortie** — type `association` — CM1 et CM2 — leçon `bulletin`

- CM1 : Pluie annoncée l'après-midi ↔ Prendre un vêtement de pluie; Vent frais, force 6 ↔ Reporter la sortie en bateau; Soleil et 21 °C ↔ Casquette et gourde d'eau; −2 °C au petit matin ↔ Bonnet, gants, attention au sol glissant
- CM2 : Averses en fin de journée ↔ Prévoir un vêtement de pluie pour le retour; Vent frais, force 6 ↔ Reporter la sortie en bateau; Soleil et 21 °C ↔ Casquette et gourde d'eau; −2 °C au petit matin ↔ Bonnet, gants, attention au sol glissant; Orage annoncé ↔ Rester à l'abri, loin des arbres isolés
- Correction : Une prévision sert à décider : on s'équipe contre la pluie, le froid ou le soleil, et on renonce à une activité quand le vent ou l'orage la rendent dangereuse.

**5-3 · Le mot caché du bulletin** — type `lettres` — CM2 — leçon `bulletin`

- CM2 : Mot : **OUEST**
- Correction : Mercredi, la girouette indiquait un vent venant de l'ouest : le mot caché est OUEST. Un vent d'ouest vient de l'ouest et souffle vers l'est.

**5-4 · La valeur de vérité** — type `code` — CM1 et CM2 — leçon `bulletin`

- CM1 : Température maximale (°C) → **21**; Vent moyen (km/h) → **24**; Hauteur de pluie (mm) → **7**
- CM2 : Température maximale (°C) → **21**; Vent moyen (km/h) → **24**; Hauteur de pluie (mm) → **7**
- Correction : Mercredi : 21 °C au maximum sous abri (module 1), un vent moyen de 24 km/h venant de l'ouest (module 2), 7 mm de pluie (module 3). Trois mesures fiables, prises avec les bons instruments et au bon endroit : c'est la base de toute prévision.


</details>

## Score

| | CM1 | CM2 |
|---|---|---|
| Énigmes (5 points chacune) | 15 × 5 = 75 | 20 × 5 = 100 |
| Rapidité (3 points par module bouclé en moins de 8 min en CM1, 10 min en CM2, sans indice ; 2 points avec indice) | 15 | 15 |
| Quizz final (5 questions, 2 points chacune) | 10 | 10 |
| **Total** | **100** | **125** |

Chaque indice consulté retire 2 points. Quatre badges : *Équipe rapide*, *Lecture précise*
(module 1 sans indice), *Bon observateur* (module 4 sans indice), *Prévisionniste*
(3 indices au plus sur la partie).

## Les leçons (📚)

Cinq leçons rédigées, une par module (3 à 4 minutes de lecture), avec un contenu CM1 et un
contenu CM2, des objectifs, un lexique, un schéma SVG et leurs sources. Chaque énigme ouvre
sa leçon par le bouton « 📚 Leçon ».

| Leçon | Module | Schéma |
|---|---|---|
| `thermometre` — Mesurer la température de l'air | 1 | abri météo (CM1), lecture d'une température négative (CM2) |
| `vent` — Mesurer le vent : direction et vitesse | 2 | rose des vents |
| `pluie` — Mesurer la pluie avec un pluviomètre | 3 | 1 mm sur 1 m² = 1 litre |
| `releves` — Organiser et exploiter des relevés | 4 | courbes des minimums et maximums |
| `bulletin` — De la mesure à la prévision : météo et climat | 5 | chaîne mesurer → prévoir |

## Module enseignant (⚙️ dans le jeu)

Taille du texte, animations réduites (fige aussi les décors SVG), sons et voix, durée du
minuteur, accès aux leçons, IA facultative, inventaire des médias, et **impressions A4** :
fiches préparatoires des cinq modules, QCM, questions fermées, études de documents, avec
corrigés séparés (contenu : `assets/data/evaluations.json`).

Tableau de bord en direct (mode local) : `http://127.0.0.1:8000/station-meteo/prof.html`.

## Vérifier une énigme précise

`station-meteo/?salle=N&niveau=CM1` (ou `CM2`) ouvre le module N ; `&enigme=K` vise la
K-ième énigme du module ; `salle=6` ouvre l'écran de fin. Rien n'est sauvegardé.
Exemple : [module 3, énigme 4, CM2](https://idgir.github.io/escape-games-cm1-cm2/station-meteo/?salle=3&niveau=CM2&enigme=4).

## Modifier le contenu

- `assets/data/enigmes.json` : les 20 énigmes (blocs `cm1` / `cm2` / `commun`, champ `niveaux`).
- `assets/data/lecons.json` : les 5 leçons.
- `assets/data/dialogues.json` : lieux, personnages, dialogues, mots-clés.
- `assets/data/evaluations.json` : quizz final, fiches préparatoires, évaluations.
- `js/decors.js` et `js/personnages.js` : décors et personnages SVG.

### Le type d'énigme `instrument` (propre à ce jeu)

Un thermomètre ou un pluviomètre gradué, dessiné en SVG. Deux modes par item : **lire**
(l'élève écrit la valeur ; « −4 », « -4 °C » ou « 4,5 » sont acceptés) et **régler**
(l'élève monte ou descend le niveau avec ▲ ▼ ou en cliquant sur l'échelle ; aucun nombre
n'est affiché, il doit lire la graduation lui-même).

```json
{"instrument": "thermometre", "unite": "°C", "min": -10, "max": 30, "pas": 1, "etiquettes": 5,
 "items": [{"libelle": "Un matin de janvier", "mode": "lire", "valeur": -4},
           {"libelle": "Règle −3 °C", "mode": "regler", "valeur": -3, "depart": 0}]}
```

## Sources

- **Météo-France**, « Qu'est-ce que la température ? » : température mesurée sous abri, à
  1,50 m du sol, dans un abri blanc et ventilé, selon les normes de l'OMM.
  https://meteofrance.com/comprendre-la-meteo/temperatures/quest-ce-que-la-temperature
- **Météo-France**, « Quelle différence entre météo et climat ? » : périodes de référence de
  30 ans. https://meteofrance.com/meteo-a-z/quelle-difference-entre-meteo-et-climat
- **Organisation météorologique mondiale**, *Guide des instruments et des méthodes
  d'observation* (OMM-N° 8) : vent mesuré à 10 m, moyenne sur 10 minutes ; échelle de Beaufort.
- **Eaufrance**, « Les volumes de précipitations » : 1 mm = 1 L/m².
  https://www.eaufrance.fr/les-volumes-de-precipitations
- **Fondation La main à la pâte**, « Construire quelques instruments d'une station
  météorologique » (cycle 3).
  https://fondation-lamap.org/sequence-d-activites/construire-quelques-instruments-d-une-station-meteorologique
- **Programme** de sciences et technologie du cycle 3 (Eduscol) et progression de l'enseignant
  (Année A, période 1).
