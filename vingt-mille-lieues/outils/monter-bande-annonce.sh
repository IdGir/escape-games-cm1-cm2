#!/bin/bash
# Monte la bande-annonce (≈ 20 s) à partir des vidéos d'ouverture déposées dans assets/videos/, avec fondus enchaînés.
# Aucun appel réseau, aucun coût : ffmpeg seulement.   Usage : bash vingt-mille-lieues/outils/monter-bande-annonce.sh
set -e
cd "$(dirname "$0")/../assets/videos"
CLIPS=(transition-e3 transition-e7 transition-e9 transition-e10 transition-e11)   # 5 plans de 5 s, fondus de 1 s
D=5; F=1; ARGS=(); FILT=""; n=${#CLIPS[@]}
for i in "${!CLIPS[@]}"; do ARGS+=(-i "${CLIPS[$i]}.mp4"); FILT+="[$i:v]trim=0:$D,setpts=PTS-STARTPTS,scale=1280:704,setsar=1,fps=24,format=yuv420p[v$i];"; done
last="v0"
for ((i=1;i<n;i++)); do off=$(( i*(D-F) )); FILT+="[$last][v$i]xfade=transition=fade:duration=$F:offset=$off[x$i];"; last="x$i"; done
FILT+="[$last]fade=t=in:st=0:d=1,fade=t=out:st=$(( n*(D-F)+F-1 )):d=1[out]"
ffmpeg -v error -y "${ARGS[@]}" -filter_complex "$FILT" -map "[out]" -c:v libx264 -crf 23 -preset medium -movflags +faststart -an bande-annonce.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 bande-annonce.mp4
