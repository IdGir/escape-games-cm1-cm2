# diffusion/ — référencement sur les plateformes nationales de ressources libres (N14)

Le projet est public (site GitHub Pages) et le kit « adopter ce projet » (`adopter.html`, N2) explique comment
l'utiliser, mais il n'est visible que par qui connaît l'adresse. Ce dossier prépare sa **diffusion sur les
plateformes nationales**. L'état des quatre étapes de l'amélioration :

| Étape | État | Où |
|---|---|---|
| 1. Choisir et ajouter une licence | ⏳ **décision de l'auteur** — rien n'est ajouté tant qu'elle n'est pas prise | [LICENCES-PROPOSITIONS.md](LICENCES-PROPOSITIONS.md) |
| 2. Vérifier les crédits et licences des images et vidéos | ✅ **audit fait** : 500 médias contrôlés, **27 sans crédit** et **70 aux droits « à préciser »** à régler avant d'apposer une licence libre | [AUDIT-MEDIAS.md](AUDIT-MEDIAS.md), `python outils-docs/audit-licences.py` |
| 3. Fiche de présentation | ✅ rédigée (niveau, disciplines, compétences, durée, captures, liens) | [FICHE-PRESENTATION.md](FICHE-PRESENTATION.md) |
| 4. Plateformes : conditions de dépôt, puis dépôt | ✅ conditions vérifiées pour les trois plateformes visées ; **dépôt possible seulement sur la Forge** (après les étapes 1 et 2) | [PLATEFORMES.md](PLATEFORMES.md) |

## Ce qu'il reste à faire, dans l'ordre

1. **Décider de la licence** (contenus et code) — voir les propositions et leurs conséquences.
2. **Régler les médias** signalés par l'audit : retrouver la source et la licence des 27 médias sans crédit (ou les
   retirer), préciser les droits d'usage des 70 images Agnes AI / Google Flow des variantes immersives, décider du sort des 5
   photos Pixabay (licence propre, non compatible avec une licence libre choisie).
3. Ajouter le fichier de licence et la mention dans `README.md`, `adopter.html` et le pied des pages.
4. Déposer le projet sur la Forge des communs numériques éducatifs, puis proposer la fiche à la Ressourcerie.

L'audit est rejouable (`python outils-docs/audit-licences.py`) : il doit afficher **0 sans crédit** avant la diffusion.
