#!/bin/bash
# ============================================================
# ESCAPE GAMES PEDAGOGIQUES - Lancement (macOS / Linux)
# ============================================================
cd "$(dirname "$0")"
echo ""
echo "  ============================================================"
echo "    ESCAPE GAMES PÉDAGOGIQUES - CM1/CM2 - Serveur local"
echo "  ============================================================"
echo ""

if ! command -v python3 &> /dev/null; then
    echo "  [ERREUR] Python 3 n'est pas installé."
    echo "  Installez-le depuis https://www.python.org/downloads/"
    echo "  Ou jouez en ligne : https://idgir.github.io/escape-games-cm1-cm2/"
    echo ""
    read -p "Appuyez sur Entrée pour quitter..."
    exit 1
fi

echo "  Python détecté :"
python3 --version
echo ""
echo "  >> ACCUEIL (les 3 jeux + page de vérification)"
echo "     http://127.0.0.1:8000/"
echo ""
echo "  >> JEUX"
echo "     Le Secret de la Déclaration : http://127.0.0.1:8000/declaration/"
echo "     Le Tour du Monde            : http://127.0.0.1:8000/tour-du-monde/"
echo "     Mission géographique        : http://127.0.0.1:8000/mission-geo/"
echo ""
echo "  >> VÉRIFICATION (médias + accès direct aux énigmes)"
echo "     http://127.0.0.1:8000/verifier.html"
echo ""
echo "  Ctrl+C pour arrêter le serveur."
echo ""

# Ouvrir le navigateur après 2 secondes
(sleep 2 && open "http://127.0.0.1:8000/") &

python3 serveur.py 8000
