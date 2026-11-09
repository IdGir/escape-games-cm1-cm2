# Modèle des pages propres aux variantes immersives

`migrer-jeu.py` (migration et `--maj-moteur`) copie le moteur de `vingt-mille-lieues/`, puis applique ce modèle :

- `prof.html` : tableau de bord des variantes (`__SLUG__` = dossier du jeu) : pause, reprise, messages, fin de séance,
  coup de pouce, grade, correction collective, fiche de séquence, classement, bandeau « serveur introuvable ».
  Le tableau de bord de `vingt-mille-lieues/` (source) reste plus simple : il ne charge pas les greffons de `commun/`.
- `index.html` : `migrer-jeu.py` ajoute les greffons de `commun/` (`GREFFONS_INDEX`) et le lien « Version classique »
  quand `<slug>/index.html` existe.

Sans ce modèle, `--maj-moteur` remplaçait ces pages par celles de la source et faisait disparaître les boutons enseignant.
Test : `vingt-mille-lieues/tests/test-maj-moteur.py` (la mise à jour du moteur ne change aucun fichier d'une variante à jour).
