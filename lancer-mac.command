#!/bin/bash
# ============================================================
# ESCAPE GAMES PEDAGOGIQUES - Lancement (macOS / Linux)
# ============================================================
cd "$(dirname "$0")"
echo ""
echo "  ============================================================"
echo "    LE SECRET DE LA DÉCLARATION - Lancement"
echo "    Escape game sur la Révolution française - CM1/CM2"
echo "  ============================================================"
echo ""

if ! command -v python3 &> /dev/null; then
    echo "  [ERREUR] Python 3 n'est pas installé."
    echo "  Installez-le depuis https://www.python.org/downloads/"
    echo "  Ou ouvrez directement index.html (mode autonome, sans serveur prof)."
    echo ""
    read -p "Appuyez sur Entrée pour quitter..."
    exit 1
fi

echo "  Python détecté :"
python3 --version
echo ""
echo "  Démarrage du serveur sur le port 8000..."
echo ""
echo "  >> POSTES ÉLÈVES"
echo "     Histoire (Révolution)   : http://127.0.0.1:8000/"
echo "     Géographie (Jules Verne): http://127.0.0.1:8000/tour-du-monde/"
echo "     Mission géographique    : http://127.0.0.1:8000/mission-geo/"
echo ""
echo "  >> TABLEAUX DE BORD ENSEIGNANT"
echo "     Histoire   : http://127.0.0.1:8000/prof.html"
echo "     Géographie : http://127.0.0.1:8000/tour-du-monde/prof.html"
echo ""
echo "  Ctrl+C pour arrêter le serveur."
echo ""

# Ouvrir le navigateur après 2 secondes
(sleep 2 && open "http://127.0.0.1:8000/") &

python3 serveur.py 8000
