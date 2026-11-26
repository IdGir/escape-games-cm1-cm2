# À vérifier — Mission géographique (Année A)

Points relevés par l'audit de la refonte (26/11/2026). La page du BO n° 22 du 28 mai 2026 n'a pas pu être ouverte
(erreur du site) ; le projet du CSP indique que le CM2 aborde « l'organisation du territoire français » et
« l'eau en France », et que le programme étudie aussi les différences à l'échelle mondiale.

1. **Niveau de chaque séance au BO n° 22** : séances 1 à 5 (organisation du territoire) et 13 à 16 (l'eau en France) semblent
   relever du **CM2** ; séances 8 à 12 (inégalités, se nourrir) : niveau et libellé exacts à relire dans l'annexe du programme.
2. **Libellés « BO » du README** : le tableau des séances parle de « géographie Année B » alors que le jeu est l'« Année A » ;
   les compétences citées viennent de l'ancien programme (BO n° 31 du 30 juillet 2020) : à réécrire mot pour mot depuis le BO 2026.
3. **Chiffres des documents du livret** (densités, superficies, population, niveaux de vie, kilomètres alimentaires, consommation
   d'eau) : à rapprocher de l'INSEE, de l'IGN, du SANDRE et de l'Office international de l'eau, avec l'année de la donnée.
4. **Cartes** : remplacer les cartes sans source par des cartes IGN (Géoportail), SANDRE (cours d'eau) ou SHOM (littoral)
   créditées, ou les redessiner en SVG avec la source en légende ; 10 médias de `mission-geo/assets/images/` sans crédit (AUDIT-MEDIAS).
5. **Activités « ouvertes »** (8) : non corrigées par le jeu ; décider dans la refonte entre énigme fermée et trace écrite sur la fiche.

## Version immersive, étape P1 (séances 1 à 5) — 26/11/2026

6. **Séance 5 de la version classique, activité 4** : « Combien de lettres compte le mot intrus ? » attend **9**, mais « écologie »
   compte **8** lettres. Corrigé dans la version immersive (la question n'y est plus posée) ; la version classique n'a pas été touchée.
7. **La Dôle** : le sommet (1 677 m, et non 1 678) est **en Suisse** (canton de Vaud) ; son domaine skiable est relié à la station
   des Rousses (Jura). La version immersive situe la séance 5 « à la station des Rousses, au pied de la Dôle » (office de tourisme des Rousses).
8. **Chiffres mis à jour dans la version immersive** : 34 875 communes au 1er janvier 2026 (DGCL) ; environ 69 millions d'habitants
   (Insee, bilan démographique 2025) ; emplois 2024 : tertiaire 76,6 %, industrie 12,6 %, construction 6,6 %, agriculture 2,3 % (Insee,
   enquête Emploi 2024) ; 1911 : près de 40 % des actifs dans l'agriculture (ministère de l'Agriculture, CEP, 2016). Le livret classique
   garde 68 millions et 2,1 / 18,2 / 79,7 % : à mettre à jour si l'on réimprime.
9. **Village, bourg, ville** : le seuil de 2 000 habitants est celui du livret (il rappelle le seuil historique de l'Insee pour les unités
   urbaines) ; « bourg » n'est pas une catégorie de l'Insee, qui classe aujourd'hui les communes par une grille de densité. À garder comme
   repère d'école, ou à nuancer en CM2.
10. **Densités « 1 000 hab/km² en ville, moins de 10 dans certains villages de montagne »** (fiche de la séance 3) : ordres de grandeur
    à confirmer avec une source Insee datée.
11. **Médias** : les lieux de la période 1 sont réels (Dijon, Clamecy, Besançon, Les Rousses) : leurs décors doivent être des **photos
    Wikimedia Commons** créditées ; `immersifs/mission-geo/medias.csv` contient pour l'instant des prompts d'IA génériques (à revoir
    avant toute production, avec l'accord de l'enseignante).

## Version immersive, étape P2 (séances 6 à 8) — 26/11/2026

12. **Tableau du PNUD (séance 8, livret)** : les chiffres du Koweït ne sont pas ceux du Rapport sur le développement humain 2025 (données 2023) :
    80,4 ans, 15,9 ans de scolarisation attendue, 56 612 $ (le livret : 79,2 / 15,3 / 58 056). Norvège, Guinée équatoriale et Bangladesh sont justes.
    L'appariement du livret (Guinée équatoriale « en voie de développement », Bangladesh « pays pauvre ») n'est pas la classification du PNUD : les deux pays
    sont au « développement humain moyen » (IDH 0,674 et 0,685). La version immersive le remplace par une lecture du tableau (vrai / faux, calculs).
13. **Étretat** : 1 102 habitants (Insee, population municipale en vigueur au 1er janvier 2026), 1 469 en 2011, 4,07 km². Fréquentation : « un million »
    (Francetvinfo, 2022), 1,2 à 1,5 million selon la presse 2023-2025 : la version immersive écrit « plus d'un million ». Le livret garde 1 200 habitants
    et « 400 habitants partis en 20 ans » (non vérifié) : remplacé par les chiffres de l'Insee.
14. **« 15 000 touristes en plus » (séance 7 du livret)** : chiffre non sourcé, gardé comme **hypothèse de calcul** (« imagine un jour d'été ») ;
    le grade Géographe utilise « jusqu'à 10 000 visiteurs par jour » (association Étretat Demain, citée par L'Écho touristique, 2023).
15. **Panneau « Étretat saturée pendant deux heures »** : non retrouvé dans les sources ; présenté comme une hypothèse (« Imagine que la mairie affiche… »).
16. **Caricature du gâteau (« Selçuk, 1997 » dans le livret)** : attribution non vérifiée ; la version immersive la décrit en mots (« un dessin de presse »)
    sans la reproduire ni l'attribuer. Si l'image est ajoutée, vérifier l'auteur, la date et les droits.
17. **Carte des richesses par continent** (`js/cartes.js`, `RICHESSE`) : trop simplifiée (toute l'Amérique du Sud « pauvre », légende sans accents).
    Non utilisée par la version immersive (diagramme des revenus du PNUD à la place) ; à revoir pour la version classique.
18. **Revenus « en dollars »** : il s'agit du revenu national brut par habitant en dollars PPA 2021 (PNUD) ; simplifié pour les élèves.
    Les seuils « plus de 40 000 $ » et « moins de 3 000 $ » sont choisis pour l'exercice : ce n'est pas une classification officielle.
19. **Médias de la période 2** : lieux réels (falaises d'Étretat, Grande Plage de Biarritz, marché de Dhaka) → photos Wikimedia Commons créditées ;
    pour Dhaka, éviter toute photo d'enfant identifiable.
