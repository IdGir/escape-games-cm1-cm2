# Crédits et licences des médias

Le jeu fonctionne **sans aucun de ces fichiers** (décors et personnages dessinés en SVG).
Quand ils sont installés, les crédits ci-dessous doivent rester affichés : ils sont repris
dans ⚙️ Réglages → « Crédits des médias » à l'intérieur du jeu.

## 1. Photographies des lieux réels

Aucun bâtiment n'est inventé : les cinq salles du jeu utilisent des photographies
de leurs lieux réels, publiées sous licence libre sur Wikimedia Commons.

| Salle | Lieu photographié | Fichier | Auteur | Licence |
|---|---|---|---|---|
| salle1 | Palais-Royal, Paris — siège du Conseil constitutionnel | [Cour d'honneur du Palais-Royal et colonnes de Buren](https://commons.wikimedia.org/wiki/File:Paris_Palais_Royal_Colonnes_de_Buren_4.jpg) | Zairon | CC BY-SA 4.0 |
| salle2 | Archives nationales, Paris | [Salle de consultation du CARAN, Archives nationales](https://commons.wikimedia.org/wiki/File:Centre-d'acceuil-et-de-recherche-des-Archives-nationales-Architecte-Stanislas-Fiszer-Salle-de-consultation-.jpg) | Archives nationales (France) | CC BY-SA 3.0 |
| salle3 | Palais Bourbon, Paris | [Hémicycle de l'Assemblée nationale](https://commons.wikimedia.org/wiki/File:Assemblée_nationale_(visite_septembre_2024)_41.jpg) | PanierAvide | CC BY-SA 4.0 |
| salle4 | Palais du Luxembourg, Paris | [Hémicycle du Sénat](https://commons.wikimedia.org/wiki/File:Hémicycle_du_Sénat_(tribunes).jpg) | Tangopaso | Domaine public |
| salle5 | Conseil constitutionnel, Palais-Royal, Paris | [Salle des délibérés du Conseil constitutionnel](https://commons.wikimedia.org/wiki/File:Conseil_Constitutionnel_-_Salle_des_délibérés.JPG) | Faqscl | CC BY-SA 4.0 |

**Obligations à respecter :** pour chaque photo sous licence CC BY-SA, l'auteur, la licence et
le lien vers le fichier d'origine doivent accompagner l'image, et toute version modifiée
(recadrage, animation) doit être diffusée sous la même licence. C'est le cas ici : les photos
sont utilisées telles que Wikimedia Commons les sert, et la cinématique d'ouverture, dérivée de
la photo du Palais-Royal, hérite de la licence CC BY-SA 4.0 de cette photo.

## 2. Schémas des énigmes

Cinq illustrations sont des **schémas dessinés pour ce jeu** (fichiers `e1-3`, `e2-1`,
`e3-1`, `e4-2`, `e5-1` dans `assets/images/cartes/`). Ils ne sont pas générés par une IA :
chaque information y est reprise mot pour mot des fiches officielles du Conseil
constitutionnel, citées en bas de chaque schéma. Ils sont réutilisables librement.

## 3. Images et vidéos générées

Les personnages et deux illustrations sont générés avec l'**API Agnes AI**
(`agnes-image-2.1-flash` et `agnes-video-v2.0`). Les personnages sont **fictifs** :
les prompts demandent explicitement de ne ressembler à aucune personne réelle, et
l'enfant du jeu (Nour) est rendue en style illustré, non photoréaliste.

| Fichier | Contenu | Production |
|---|---|---|
| `berthier.png` | Monsieur Berthier — gardien-archiviste | Agnes — image |
| `nour.png` | Nour — déléguée de classe (10 ans) | Agnes — image |
| `ferrand.png` | Madame Ferrand — députée | Agnes — image |
| `sylla.png` | Maître Sylla — juriste au Conseil constitutionnel | Agnes — image |
| `e1-1.jpg` | Énigme 1-1 — le coffre scellé | Agnes — image |
| `e5-3.jpg` | Énigme 5-3 — la Constitution au quotidien | Agnes — image |
| `berthier.mp4` | Monsieur Berthier — gardien-archiviste (au repos) | Agnes — vidéo, animation de berthier.png |
| `berthier-parle.mp4` | Monsieur Berthier — gardien-archiviste (en train de parler) | Agnes — vidéo, animation de berthier.png |
| `nour.mp4` | Nour — déléguée de classe (10 ans) (au repos) | Agnes — vidéo, animation de nour.png |
| `nour-parle.mp4` | Nour — déléguée de classe (10 ans) (en train de parler) | Agnes — vidéo, animation de nour.png |
| `ferrand.mp4` | Madame Ferrand — députée (au repos) | Agnes — vidéo, animation de ferrand.png |
| `ferrand-parle.mp4` | Madame Ferrand — députée (en train de parler) | Agnes — vidéo, animation de ferrand.png |
| `sylla.mp4` | Maître Sylla — juriste au Conseil constitutionnel (au repos) | Agnes — vidéo, animation de sylla.png |
| `sylla-parle.mp4` | Maître Sylla — juriste au Conseil constitutionnel (en train de parler) | Agnes — vidéo, animation de sylla.png |
| `intro.mp4` | Cinématique d'ouverture (cour du Palais-Royal) | Agnes — vidéo, à partir de la photo du Palais-Royal |
| `final.mp4` | Cinématique de fin (le coffre s'ouvre) | Agnes — vidéo, animation de e1-1.jpg |

## 4. Produire ou refaire les médias

Double-cliquez sur `produire-medias.bat` dans ce dossier. Le script :

1. télécharge les cinq photos des lieux (aucune clé nécessaire) ;
2. génère les images des personnages avec l'API Agnes ;
3. génère les vidéos, en animant les images de l'étape 2.

Les fichiers déjà présents ne sont jamais regénérés : supprimez un fichier pour le refaire.
La clé API se place dans `cle-agnes.txt` (dans ce dossier) ou dans la variable d'environnement
`AGNES_API_KEY` ; ce fichier n'est jamais publié sur GitHub.

Tous les textes de prompt sont dans `medias.json` : les modifier change ce qui est produit,
sans toucher au code du jeu.
