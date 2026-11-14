# Fabrique de nuit des médias

Chaque soir à 23 h, l'ordinateur fabrique les voix, les images et les vidéos du jeu immersif en tête de file,
puis s'arrête. Le lendemain, la tâche de finition de Claude vérifie, intègre et vous présente le jeu à valider.

## Installer (une seule fois, sur le PC qui a le dossier du projet)

1. Ouvrez le dossier `outils-medias\nuit` du projet dans l'Explorateur.
2. Double-cliquez sur **installer-nuit.bat**.
3. Si Windows refuse : clic droit sur le fichier, **Exécuter en tant qu'administrateur**.
4. Attendez « C'est installé », puis appuyez sur une touche.

Laissez l'ordinateur branché, en veille plutôt qu'éteint : la tâche le réveille. S'il était éteint, elle se lance
au prochain démarrage.

## Réglages

- Ordre des jeux : liste `FILE` en haut de `nuit-medias.py` (les nouveaux jeux s'ajoutent seuls à la fin).
- Dosage : 10 images et 5 vidéos par nuit ; arrêt de la partie Agnes au deuxième refus.
- Clé Agnes : `outils-medias\cle-agnes.txt` (jamais publiée).

## Suivre

- `journal.txt` : tout ce qui a été fait, nuit après nuit.
- `derniere-nuit.json` : le bilan de la dernière nuit (lu par Claude le matin).
- Essai sans rien appeler : `python outils-medias\nuit\nuit-medias.py --essai`.

## Arrêter

Double-cliquez sur **desinstaller-nuit.bat**.
