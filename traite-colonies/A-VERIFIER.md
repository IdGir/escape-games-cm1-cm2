# À vérifier — Les Archives du port

Points relevés pendant la production (11 novembre 2026, tâche planifiée non surveillée). Rien de bloquant pour jouer.
Sujet sensible : **relire tout le jeu avant de le proposer aux élèves** (voir aussi le guide, section 9).

1. **Loi d'abrogation du Code noir (2026)** : le jeu écrit « En 2026, une loi l'a officiellement abrogé » (leçon 3 CM2,
   correction 3-2, leçon 5 CM2). Sources : rapport du Sénat (adoption conforme en commission le 14 octobre 2026, séance
   publique prévue le 20 octobre 2026) et titre de la page vie-publique.fr « Abrogation du Code noir : loi du 2 novembre 2026 »
   (page non lisible par l'outil). Vérifier la date et le numéro de la loi au Journal officiel (Légifrance) ; en cas de doute,
   supprimer la phrase dans `tests/donnees/gen_lecons.py` et `gen_enigmes.py`.
2. **Code noir, contenu** : formulation adaptée (« biens meubles », « punitions très sévères ») d'après le rapport du Sénat ;
   aucun article n'est cité. Le texte intégral (Légifrance / Archives nationales d'outre-mer) n'a pas été relu.
3. **Bordeaux** : le jeu dit seulement que Bordeaux « s'enrichit aussi du commerce des produits coloniaux » et qu'elle fait
   partie des ports autorisés à la traite en 1713-1721 (BnF). Les expressions « premier port colonial » ou un rang de
   Bordeaux pour la traite n'ont **pas** été retenues, faute de source officielle lue ; à compléter avec le musée d'Aquitaine.
4. **Le Havre, La Rochelle, Saint-Malo, Honfleur** : cités par la BnF comme ports suivants de la traite française, sans
   pourcentage. Carte 4-4 : positions **approximatives** (carte simplifiée dessinée par script).
5. **Toussaint Louverture** : « né esclave vers 1740 », « gouverneur en 1798 », « mort prisonnier en France » (BnF). La date
   et le lieu exacts de sa mort (fort de Joux, 1803) ne sont pas écrits dans le jeu.
6. **1er janvier 1804** : date de l'indépendance d'Haïti lue sur Hérodote (la BnF dit « 1804 ») ; date très largement admise.
7. **Travail dans l'habitation** : étapes (coupe, dépaillage, moulin, vesou, sucrerie, purgerie, barriques) et « plus de
   18 heures pendant la roulaison » d'après l'académie de Martinique. Le détail « sécher et blanchir le sucre dans la purgerie »
   (énigme 3-1 CM2) est une formulation simplifiée à confirmer.
8. **« Garder des chants, des contes et des croyances venus d'Afrique »** (leçon 3 CM1, tri 3-3) : forme de résistance
   culturelle très généralement enseignée, mais non lue telle quelle dans les sources consultées (Fondation pour la mémoire de
   l'esclavage, Lumni : à consulter).
9. **Durée de la traite « du XVIe au XIXe siècle »** et pic au XVIIIe siècle pour la France : d'après la BnF (1551-1875 pour la
   France ; année record 1790 à Saint-Domingue). La frise de la leçon 2 place un repère au XVIIIe siècle sans date précise.
10. **Mémorial et musées** : « quatorze salles » au musée d'histoire de Nantes (article des Anneaux de la mémoire) ; le
    musée d'Aquitaine « présente le commerce atlantique et l'esclavage » (formulation volontairement générale).
