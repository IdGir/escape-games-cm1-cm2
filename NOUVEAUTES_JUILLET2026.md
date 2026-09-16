# Nouveautés — juillet 2026 (Phase J)

Ce fichier récapitule ce qui a été ajouté à ta version Phase H+I.
Rien n'a été supprimé ni cassé : tous les tests de non-régression passent
(zéro faux positif, migrations, PIN, sauvegardes).

## 1. Le classeur — tes 70 vraies fiches, dans l'application

Tes fiches CM1 (orthographe, grammaire, conjugaison, vocabulaire) sont
maintenant DANS le Correcteur, pas juste sur papier :

- **Côté enseignant** : nouvel onglet **📘 Classeur** dans le menu de gauche.
  Filtre par domaine, clique sur une fiche pour la voir en grand — et tu
  peux l'imprimer directement depuis cette fenêtre (Ctrl+P).
- **Côté élève** : quand il clique sur une erreur pendant la correction
  guidée, un bouton **« 📘 Voir la fiche »** apparaît si une de tes fiches
  correspond à cette catégorie d'erreur — c'est la vraie fiche du cahier,
  pas une explication générique.

Fichiers ajoutés : `lecons_manuel.py`, `data_lecons_manuel.json`,
`data_lecons_manuel.css`. Rattachement fiches ↔ catégories dans
`lecons_manuel.py` (variable `RATTACHEMENT`), modifiable si tu veux
changer quelles fiches apparaissent pour quelle catégorie.

## 2. Ma banque de mots — banque lexicale personnelle par élève

Nouvelle tuile **🎒 Ma banque de mots** dans le menu de l'élève.

- À chaque correction, les mots que l'élève a ratés en lexique, orthographe
  ou homophones sont mémorisés — pas une liste générique, SES mots à lui.
- Un mot raté plusieurs fois voit son compteur augmenter ("raté 3 fois").
- L'élève peut cocher **« Je le sais maintenant »** : le mot disparaît de
  sa liste (mais l'historique reste en base si jamais il le rerate).

Table ajoutée : `mots_a_travailler`. Aucune migration nécessaire — la table
se crée automatiquement au prochain démarrage, même sur une base existante.

## Comment essayer

1. `lancer.bat` comme d'habitude.
2. **Espace enseignant → Classeur** : parcours les 70 fiches.
3. **Espace élève → Je me corrige** → corrige un texte avec des mots de
   vocabulaire ratés → clique sur l'erreur → bouton « Voir la fiche ».
4. Termine la correction → retourne au menu élève → **🎒 Ma banque de mots**.

## Comment fabriquer l'exe

Comme avant : `build_exe.bat`. Les nouveaux fichiers de données
(`data_lecons_manuel.json/.css`) sont maintenant inclus automatiquement.

## À venir (pas encore fait)

- Détection de régression (élève qui décroche).
- Capture de ce que trouve le camarade à l'étape de relecture.
- Fiches d'exercices imprimables générées à la demande.
