#!/bin/bash
# Garantit qu'une branche ne touche PAS aux jeux existants de la collection.
#
# Règles :
#  - ZONES ÉVOLUTIVES (fichiers ajoutables ET modifiables) : vingt-mille-lieues/, immersifs/, prompts-opus/ et ce script ;
#  - AJOUTS seulement : commun/(js|css|donnees)/nouveaux/ ;
#  - tout le reste (les 12 jeux d'origine, commun/, serveur.py, index.html…) : INTERDIT de modifier, supprimer, renommer ou ajouter.
#
# Pour transformer VRAIMENT un jeu d'origine (mode « remplacer » du migrateur), l'enseignant doit l'autoriser
# explicitement, jeu par jeu :  bash outils-tests/verifier-isolation.sh --autoriser renaissance [--autoriser versailles …]
#
# Usage : bash outils-tests/verifier-isolation.sh [--autoriser <dossier-de-jeu>]… [branche-de-base]   (défaut : origin/escape-games)
BASE="origin/escape-games"
EVOLUTIVES='vingt-mille-lieues/|immersifs/|prompts-opus/|outils-tests/verifier-isolation\.sh$'
AJOUTS_SEULS='commun/(js|css|donnees)/nouveaux/'
AUTORISES_JEUX=""
while [ $# -gt 0 ]; do
  case "$1" in
    --autoriser) AUTORISES_JEUX="$AUTORISES_JEUX|$(echo "$2" | sed 's#/*$##')/"; shift 2 ;;
    *) BASE="$1"; shift ;;
  esac
done
[ -n "$AUTORISES_JEUX" ] && EVOLUTIVES="$EVOLUTIVES$AUTORISES_JEUX"
git rev-parse --verify -q "$BASE" >/dev/null || { echo "Base introuvable : $BASE"; exit 2; }
MB=$(git merge-base "$BASE" HEAD)
echo "Base : $BASE ($MB)"
[ -n "$AUTORISES_JEUX" ] && echo "⚠️  Jeux d'origine déverrouillés par l'enseignant : ${AUTORISES_JEUX#|}"
echo "--- Fichiers touchés par la branche ---"
git diff --name-status --no-renames "$MB" HEAD | sed 's/^/  /'
# Modifié / supprimé : permis seulement dans les zones évolutives
MODIF=$(git diff --name-status --no-renames "$MB" HEAD | grep -v '^A' | awk '{print $1" "$2}' | grep -Ev "^[A-Z] ($EVOLUTIVES)" || true)
# Ajouté : permis dans les zones évolutives et dans les dossiers « nouveaux »
HORS=$(git diff --name-status --no-renames "$MB" HEAD | awk '$1=="A"{print $2}' | grep -Ev "^($EVOLUTIVES|$AJOUTS_SEULS)" || true)
ERR=0
if [ -n "$MODIF" ]; then echo; echo "❌ ÉCHEC : fichiers protégés modifiés/supprimés :"; echo "$MODIF"; ERR=1; fi
if [ -n "$HORS" ]; then echo; echo "❌ ÉCHEC : fichiers ajoutés hors des dossiers autorisés :"; echo "$HORS"; ERR=1; fi
if [ $ERR -eq 0 ]; then echo; echo "✅ OK : aucun fichier protégé n'a été modifié ; les 12 jeux d'origine sont intacts (octet pour octet)."; fi
exit $ERR
