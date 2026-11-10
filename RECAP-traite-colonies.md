# Reprise : jeu n°12 « Les Archives du port » (traite-colonies) — à produire

État au 10/11/2026 (tâche planifiée) : **rien n'est écrit dans le dépôt**. Le jeu n'a pas été produit dans cette session : un jeu complet
(version classique + variante immersive 5 grades ≈ 19 000 lignes pour mouvement), sur un sujet sensible, ne tenait pas dans le
budget restant avec une relecture sérieuse. Seule la recherche de faits est commencée (ci-dessous).

Pour reprendre : nouvelle conversation, skill produire-escape-game, « mode B, jeu n°12 », en partant de ce fichier.

## Faits vérifiés en ligne (10/11/2026)

Source : BnF, France-Amériques, « Slave trade », Cécile Vidal, mai 2021, d'après Slave Voyages
(https://heritage.bnf.fr/france-ameriques/en/slave-trade-1) :
- traite transatlantique : plus de 12,5 millions de personnes déportées, du XVIe au XIXe siècle ;
- navires sous pavillon français (1551-1875) : 1 381 404 personnes, 4 118 expéditions, soit 11 % de la traite transatlantique ;
- Nantes : 44 % des expéditions françaises ; autres ports cités : Le Havre, La Rochelle, Saint-Malo, Honfleur (pas de pourcentage) ; Bordeaux : cité parmi les ports autorisés 1713-1721 ;
- environ 2/3 d'hommes, environ 27 % d'enfants ; mortalité pendant la traversée : environ 13 % ;
- 9 voyages sur 10 vers les Antilles et la Guyane ; Saint-Domingue : environ 3/4 des expéditions, 80 % des captifs vendus ;
- voyage moyen : environ 320 captifs, environ deux mois de traversée ;
- abolition par la Convention le 4 février 1794 ; rétablissement par Napoléon Bonaparte le 20 mai 1802.

Source : décret du 27 avril 1848 (texte : https://mjp.univ-perp.fr/france/1848esclavage.htm) :
- article 1er : « L'esclavage sera entièrement aboli dans toutes les colonies et possessions françaises », deux mois après la promulgation dans chaque colonie ;
- commission d'abolition présidée par Victor Schœlcher (décret du 4 mars 1848).

## À vérifier en ligne avant d'écrire (sources officielles)

- Code noir : édit de mars 1685 (Archives nationales d'outre-mer / Légifrance) ; formulation adaptée CM1/CM2.
- Loi n° 2001-434 du 21 mai 2001 (« loi Taubira », Légifrance) ; 10 mai journée nationale (depuis 2006 ; vie-publique.fr ne s'est pas chargé).
- Saint-Domingue : insurrection d'août 1791, Toussaint Louverture, indépendance d'Haïti le 1er janvier 1804 (Fondation pour la mémoire de l'esclavage).
- Produits du commerce triangulaire, richesse des ports : Musée d'histoire de Nantes, Musée d'Aquitaine. Ne pas généraliser un port à toute la France.
- Marronnage : définition (FME, Lumni).

## Plan (prompt `prompts-opus/12-traite-colonies.md`, § 9)

5 salles : commerce triangulaire (plan, association) · traite atlantique (ordre, vrai/faux) · plantations, Code noir, marronnage (tri, documents)
· échanges avec les colonies, ports (association, intrus) · résistances et abolitions 1791-1804, 1794, 1802, 1848, 10 mai (frise, code).
Élèves = enquêteurs d'archives, jamais de jeu de rôle d'esclave ; ton digne, pas d'image choquante, pas de points « gagnés » au profit de la traite ;
vocabulaire : personnes réduites en esclavage, captifs, traite négrière. Guide : consignes de discussion en classe.

## Autres points de la session du 10/11/2026

- Moteur (boutons enseignant) : déjà corrigé dans le commit 829811d (non poussé). Retesté : test-boutons-enseignant-direct.js 12/12 variantes vertes, test-boutons-enseignant.js 12/12.
- etats-matiere : 5 grades déjà complets (commit b74eade) ; test-immersif 568 vérifications, 0 échec.
- Accueil : 11 jeux publiés ouvrent l'immersif par défaut ; mouvement (n°11) absent de l'accueil (voir RECAP-integration-mouvement.md : affiche et bande-annonce = médias, accord nécessaire).
- verifier-isolation.sh échoue sur `sw-fichiers.js` (modifié par le commit 829811d, régénéré comme le demande le skill § 6.2) : ajouter ce fichier aux exceptions du script, ou accepter.
