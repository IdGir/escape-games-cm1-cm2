# Points à vérifier — Le Grand Repas du chef

Repris du pack de contenu (`prompts-opus/alimentation-pack/A-VERIFIER.md`), complété lors de l'intégration (3 octobre 2026).

## Points du pack

1. **Colonne du programme** : dans le BO n°24 du 11 juin 2026, vérifier si « Alimentation humaine » est rangé en CM1 ou en CM2 (la mise en page du PDF consulté est ambiguë). Le jeu reste en Année A, période 2, quoi qu'il en soit.
2. **Besoins en énergie** (salle 2, leçon `besoins`) : enfant de 10 ans 1 800-2 200 kcal ; adulte 2 000-2 700 kcal. Ces chiffres ont été lus dans des sources secondaires qui citent l'ANSES : confirmer sur anses.fr.
3. **Coureur cycliste** : environ 2 800 kcal au repos et 6 000 kcal un jour d'étape de montagne. Ce sont des ordres de grandeur couramment cités, sans source officielle trouvée. Garder « environ ».
4. **Dents** : 20 dents de lait (sans prémolaires), 32 dents chez l'adulte (dents de sagesse comprises).
5. **Intestin grêle** : « environ 6 m ». Les valeurs varient selon les sources (de 5 à 7 m).
6. **Fréquence cardiaque** : au repos, 95 ± 30 battements par minute à 6-12 ans (Wikipédia). Les 160 battements par minute après un effort intense sont une valeur plausible, sous le maximum théorique de 220 − âge.
7. **Données fictives** : le poussin Caramel (40 → 450 g en 4 semaines, 700 g de nourriture) et la toise de Lou (115 → 137 cm) sont inventées mais vraisemblables. Elles sont signalées comme « relevé fictif » à l'écran.
8. **Menu final** : à adapter à la classe (allergies, régimes).

## Contrôles faits lors de l'intégration (3 octobre 2026)

- **Programme** : référence BO n° 24 du 11 juin 2026 (arrêté du 5 juin 2026, NOR MENE2611650A) reprise du catalogue du dépôt
  (vérifiée le 1er octobre 2026). La lecture en ligne du PDF n'a pas permis de retrouver mot pour mot les cinq libellés de
  compétences du pack : ils sont gardés tels quels (point 1 ci-dessus toujours ouvert).
- **Point 2** : La Revue du praticien (« Besoins énergétiques moyens de l'enfant et de l'adolescent ») donne environ 2 000 à
  2 100 kcal par jour à 10 ans (filles / garçons) : cohérent avec la fourchette 1 800-2 200 kcal du pack. La valeur ANSES elle-même
  n'a pas été consultée.
- **Point 4** : confirmé par Vikidia, « Dent » (20 dents de lait ; 32 dents avec les 4 dents de sagesse ; rôles des incisives,
  canines, prémolaires, molaires).
- **Point 5** : Vikidia, « Intestin grêle » : « longueur moyenne de 6 mètres » chez l'adulte. « Environ 6 m » conservé.
- **Point 6** : Wikipédia, « Fréquence cardiaque » : 95 ± 30 battements par minute à 6-12 ans ; maximum théorique 220 − âge.
- **Ajout du jeu** : « la digestion d'un repas dure plusieurs heures » (leçon `digestion`, CM2) : formulation volontairement vague.

## Écarts au pack, à relire

- **1-3 « La toise de la cuisine »** : le pack la donne en vrai/faux ; elle est jouée comme un **tri** (colonnes « Vrai » / « Faux »),
  mêmes phrases, pour que la salle 1 compte une manipulation (règle du cahier des charges, contrôlée par `tests/test_json.py`).
- **Quizz final** : le pack place toujours la bonne réponse en premier ; le moteur n'en mélange pas l'ordre : les propositions ont été
  réordonnées. En CM2, le quizz reprend les 5 questions du pack avec une quatrième proposition (et le foie en question 4).
- Ajouts nécessaires au format : 3 indices par niveau, consignes, sources, explications, textes à lettres cachées (3-3, 5-4),
  documents et paragraphes complémentaires des leçons (3 à 4 minutes de lecture en CM2), dialogues de réussite, évaluations imprimables.
- **Menu final** : à adapter à la classe (allergies, régimes, pratiques des familles).
