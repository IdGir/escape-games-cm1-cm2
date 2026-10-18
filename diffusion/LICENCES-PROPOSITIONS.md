# Choisir une licence — propositions (décision de l'auteur)

> Le dépôt n'a **aucune licence** : légalement, sans licence, personne n'est autorisé à réutiliser, modifier ou
> redistribuer le projet (« tous droits réservés » par défaut). Choisir une licence est une **décision de l'auteur**
> et engage ses droits : elle n'a pas été prise à sa place. Ce document n'est pas un avis juridique.

## Pourquoi il en faut une (et laquelle les plateformes attendent)

La Forge des communs numériques éducatifs et sa Ressourcerie ne présentent que des **ressources éducatives libres** :
une ressource est dite libre quand sa licence accorde les permissions des « 5R » (réutiliser, retenir, remixer, remanier,
redistribuer). Conséquence : les licences qui interdisent l'**usage commercial** (Creative Commons « NC ») ou les
**modifications** (« ND ») ne conviennent pas.

## Trois contenus, trois questions

| Contenu | Exemples | Propositions |
|---|---|---|
| **Contenus pédagogiques de l'auteur** | énigmes (`enigmes.json`), leçons, dialogues, guides, fiches, dessins SVG des décors et personnages, textes | **CC BY-SA 4.0** (attribution, partage dans les mêmes conditions : les adaptations restent libres) — ou **CC BY 4.0** (plus ouverte) — ou **Licence ouverte Etalab 2.0** (courante dans l'administration) |
| **Code** | `commun/js`, `app.js`, `serveur.py`, scripts `outils-*` | **MIT** (très permissive) — ou **AGPL-3.0 / GPL-3.0** (copyleft : les versions modifiées restent libres) — ou **CeCILL** (licence libre française) |
| **Médias de tiers** | photos Wikimedia Commons, Gallica, Pixabay | **gardent leur licence d'origine**, indiquée dans `assets/medias/CREDITS-medias.md` ; la licence du dépôt ne s'y applique pas |

Une **mention unique** peut les distinguer : « Contenus : CC BY-SA 4.0 · Code : MIT · Médias de tiers : voir les crédits ».

## Ce que l'audit des médias change (voir AUDIT-MEDIAS.md)

- **CC BY-SA** (≈ 29 médias) : compatible avec des contenus en CC BY-SA 4.0 ; avec une licence plus ouverte (MIT, CC BY), ces
  médias restent en CC BY-SA, ce qui est permis tant qu'ils sont crédités. Les **vidéos animées à partir d'une photo CC BY-SA**
  héritent de cette licence (déjà noté dans les crédits).
- **Pixabay** (5 photos, château fort) : licence propre, **pas une licence libre** : ne peut pas être incluse dans un dépôt présenté comme
  libre. À remplacer (photo Wikimedia libre) ou à retirer avant dépôt.
- **Images et vidéos générées par IA** (≈ 266, Agnes AI ; variantes immersives : Agnes AI, Google Flow) : les conditions d'usage de
  l'outil et le statut de droit d'auteur d'une création générée sont à confirmer ; 70 images des variantes immersives sont
  notées « **à préciser (droits d'usage)** ». Tant que ce n'est pas réglé, le plus prudent est de **ne pas les placer sous la
  licence libre** (ou de ne pas les diffuser sur les plateformes).
- **27 médias sans crédit** : à documenter ou retirer.

## Une proposition prête à adopter (si elle vous convient)

> **Contenus pédagogiques : CC BY-SA 4.0 · Code : MIT · Médias de tiers et images générées : licence propre indiquée dans les crédits.**

À la décision : ajouter `LICENCE-CONTENUS.md` et `LICENSE` (code), la mention dans `README.md`, `adopter.html` et `faq.html`,
et (si vous le souhaitez) une ligne dans le pied de chaque jeu. Ce travail est court une fois le choix fait.
