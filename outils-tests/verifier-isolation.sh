#!/bin/bash
# Garantit qu'une branche n'a MODIFIÉ, SUPPRIMÉ ni RENOMMÉ aucun fichier existant de la branche de base :
# elle ne peut qu'AJOUTER des fichiers (dans les dossiers autorisés).
# Usage : bash outils-tests/verifier-isolation.sh [branche-de-base]   (défaut : origin/escape-games)
BASE="${1:-origin/escape-games}"
AUTORISES='^(vingt-mille-lieues/|prompts-opus/|outils-tests/verifier-isolation.sh$|commun/(js|css|donnees)/nouveaux/)'
git rev-parse --verify -q "$BASE" >/dev/null || { echo "Base introuvable : $BASE"; exit 2; }
MB=$(git merge-base "$BASE" HEAD)
echo "Base : $BASE ($MB)"
echo "--- Fichiers touchés par la branche ---"
git diff --name-status --no-renames "$MB" HEAD | sed 's/^/  /'
MODIF=$(git diff --name-status --no-renames "$MB" HEAD | grep -v '^A' || true)
HORS=$(git diff --name-status --no-renames "$MB" HEAD | awk '$1=="A"{print $2}' | grep -Ev "$AUTORISES" || true)
ERR=0
if [ -n "$MODIF" ]; then echo; echo "❌ ÉCHEC : fichiers existants modifiés/supprimés :"; echo "$MODIF"; ERR=1; fi
if [ -n "$HORS" ]; then echo; echo "❌ ÉCHEC : fichiers ajoutés hors des dossiers autorisés :"; echo "$HORS"; ERR=1; fi
if [ $ERR -eq 0 ]; then echo; echo "✅ OK : aucun fichier existant n'a été modifié ; les 12 jeux sont intacts (octet pour octet)."; fi
exit $ERR
