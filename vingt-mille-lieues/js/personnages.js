/* ============================================================
   PERSONNAGES — portraits animés (cadre ovale de laiton)
   ------------------------------------------------------------
   Cascade : fichier déposé assets/images/personnages/<id>.webp|.png|.jpg
   → portrait dessiné en SVG (ci-dessous). Animations CSS : respiration,
   clignement, bouche qui bouge pendant la voix (classe « parle »).
   Les fiches d'identité (PRODUCTION-MEDIAS.md) décrivent les mêmes
   traits : Nemo en redingote bleu marine à boutons dorés, barbe
   poivre et sel ; Aronnax en redingote brune ; Conseil à lunettes ;
   Ned Land en bonnet, barbe rousse.
   ============================================================ */
var VML = window.VML || (window.VML = {});

VML.sourcesPerso = {};

(function(){
  const tete = (o) => `
    <defs>
      <radialGradient id="peau-${o.id}" cx=".45" cy=".4" r=".65"><stop offset="0" stop-color="${o.peauClair}"/><stop offset="1" stop-color="${o.peau}"/></radialGradient>
      <radialGradient id="fond-${o.id}" cx=".5" cy=".35" r=".8"><stop offset="0" stop-color="${o.fond1}"/><stop offset="1" stop-color="${o.fond2}"/></radialGradient>
      <linearGradient id="habit-${o.id}" x1="0" x2="1"><stop offset="0" stop-color="${o.habitSombre}"/><stop offset=".5" stop-color="${o.habit}"/><stop offset="1" stop-color="${o.habitSombre}"/></linearGradient>
    </defs>
    <rect width="200" height="240" fill="url(#fond-${o.id})"/>
    <circle cx="150" cy="60" r="70" fill="${o.lumiere}" opacity=".18"/>
    <g class="p-corps">
      <path d="M20 240 Q30 170 100 165 Q170 170 180 240Z" fill="url(#habit-${o.id})"/>
      ${o.habitDetails || ""}
      <rect x="88" y="138" width="24" height="30" fill="${o.peau}"/>
      <g class="p-tete">
        ${o.arriere || ""}
        <ellipse cx="100" cy="100" rx="40" ry="50" fill="url(#peau-${o.id})"/>
        <ellipse cx="60" cy="104" rx="6" ry="11" fill="${o.peau}"/><ellipse cx="140" cy="104" rx="6" ry="11" fill="${o.peau}"/>
        ${o.cheveux || ""}
        <path d="M76 84 q10 -6 20 -1 M104 83 q10 -5 20 1" stroke="${o.sourcils}" stroke-width="${o.sourcilsE || 3.5}" fill="none" stroke-linecap="round"/>
        <g class="p-yeux">
          <ellipse cx="86" cy="96" rx="6" ry="4.2" fill="#f4f0ea"/><ellipse cx="114" cy="96" rx="6" ry="4.2" fill="#f4f0ea"/>
          <circle cx="86.5" cy="96.3" r="3.1" fill="${o.iris}"/><circle cx="114.5" cy="96.3" r="3.1" fill="${o.iris}"/>
          <circle cx="87.5" cy="95.2" r="1" fill="#fff"/><circle cx="115.5" cy="95.2" r="1" fill="#fff"/>
        </g>
        <g class="p-paupieres"><rect x="78" y="90" width="17" height="0" fill="${o.peau}"/><rect x="106" y="90" width="17" height="0" fill="${o.peau}"/></g>
        <path d="M100 98 q-4 14 -7 18 q7 3 13 0" stroke="${o.ombrePeau}" stroke-width="2" fill="none" stroke-linecap="round"/>
        ${o.barbe || ""}
        <g class="p-bouche">
          <path class="b-fermee" d="M89 126 q11 4 22 0" stroke="${o.levres}" stroke-width="3" fill="none" stroke-linecap="round"/>
          <ellipse class="b-ouverte" cx="100" cy="127" rx="9" ry="5" fill="#3a1410"/>
        </g>
        ${o.moustache || ""}
        ${o.lunettes || ""}
        ${o.coiffe || ""}
      </g>
    </g>`;

  const P = {
    nemo: {
      id: "nemo", peau: "#c9a084", peauClair: "#e6c2a6", ombrePeau: "#9a7058", levres: "#7a4a3a", iris: "#3a4a5a",
      fond1: "#1d4a63", fond2: "#081a26", lumiere: "#5fd0ff", habit: "#1b2a4a", habitSombre: "#0b1428",
      sourcils: "#8a8a88", sourcilsE: 4,
      cheveux: `<path d="M60 92 Q58 44 100 42 Q144 44 140 92 Q136 64 100 60 Q66 62 60 92Z" fill="#9c9c98"/><path d="M70 60 q30 -14 62 2" stroke="#c8c8c2" stroke-width="2" fill="none"/>`,
      barbe: `<path d="M62 106 Q64 150 100 156 Q136 150 138 106 Q130 132 112 134 Q100 120 88 134 Q70 132 62 106Z" fill="#7c7b78"/><path d="M70 120 l4 10 M80 130 l3 8 M120 130 l-3 8 M130 120 l-4 10" stroke="#bdbdb8" stroke-width="1.5"/>`,
      moustache: `<path d="M84 119 Q100 112 116 119 Q108 123 100 120 Q92 123 84 119Z" fill="#6c6b68"/>`,
      habitDetails: `<path d="M70 172 L100 220 L130 172" fill="#f2efe6"/><path d="M92 172 L100 200 L108 172Z" fill="#1d1d1d"/>${[0, 1, 2].map(i => `<circle cx="62" cy="${190 + i * 16}" r="4" fill="#e3b54a"/><circle cx="138" cy="${190 + i * 16}" r="4" fill="#e3b54a"/>`).join("")}<path d="M112 206 q14 6 24 -2" stroke="#e3b54a" stroke-width="1.5" fill="none"/>`
    },
    aronnax: {
      id: "aronnax", peau: "#d7a98a", peauClair: "#f0c9ad", ombrePeau: "#a8785c", levres: "#8a4e3e", iris: "#5a3a22",
      fond1: "#5a3a1c", fond2: "#1c0f06", lumiere: "#ffcf7a", habit: "#6a4428", habitSombre: "#3a2412",
      sourcils: "#3a2618",
      cheveux: `<path d="M60 96 Q56 48 100 44 Q146 48 140 96 Q138 66 112 62 Q96 70 76 64 Q64 74 60 96Z" fill="#3a2618"/><path d="M60 84 q-2 10 2 20 M140 84 q2 10 -2 20" stroke="#9a8a7a" stroke-width="3"/>`,
      barbe: `<path d="M62 100 Q60 124 72 130 Q70 112 66 100Z M138 100 Q140 124 128 130 Q130 112 134 100Z" fill="#3a2618"/>`,
      moustache: `<path d="M84 118 Q100 110 116 118 Q108 122 100 119 Q92 122 84 118Z" fill="#3a2618"/>`,
      habitDetails: `<path d="M74 170 L100 214 L126 170" fill="#efe6d4"/><path d="M90 172 Q100 182 110 172 L104 186 L96 186Z" fill="#7a1e1e"/><rect x="128" y="196" width="26" height="34" rx="3" fill="#d9ccaa" transform="rotate(-10 128 196)"/>`
    },
    conseil: {
      id: "conseil", peau: "#e0b496", peauClair: "#f5d3ba", ombrePeau: "#b08466", levres: "#9a5a48", iris: "#3a5a7a",
      fond1: "#2e4a3a", fond2: "#0c1a12", lumiere: "#b8ffb0", habit: "#2a2a30", habitSombre: "#121216",
      sourcils: "#8a6a3a", sourcilsE: 3,
      cheveux: `<path d="M60 92 Q58 46 100 44 Q142 46 140 92 Q140 62 120 56 L80 58 Q62 64 60 92Z" fill="#a8844a"/><path d="M78 58 q20 8 46 -2" stroke="#8a6a3a" stroke-width="2" fill="none"/>`,
      lunettes: `<circle cx="86" cy="96" r="10" fill="none" stroke="#b9a76a" stroke-width="2"/><circle cx="114" cy="96" r="10" fill="none" stroke="#b9a76a" stroke-width="2"/><path d="M96 96 h8 M76 94 l-14 -3 M124 94 l14 -3" stroke="#b9a76a" stroke-width="2"/>`,
      habitDetails: `<path d="M76 170 L100 206 L124 170" fill="#f6f2ea"/><path d="M92 176 L100 184 L108 176 L100 170Z" fill="#1a1a1a"/><path d="M100 206 V240" stroke="#3a3a42" stroke-width="2"/>${[0, 1].map(i => `<circle cx="104" cy="${216 + i * 14}" r="2.5" fill="#888"/>`).join("")}`
    },
    ned: {
      id: "ned", peau: "#c08a64", peauClair: "#dba680", ombrePeau: "#8e5e40", levres: "#7a3e2e", iris: "#2a4a3a",
      fond1: "#2c3e50", fond2: "#0a1018", lumiere: "#9fd0ff", habit: "#3a4a5a", habitSombre: "#1a2430",
      sourcils: "#8a3e1c", sourcilsE: 5,
      arriere: `<path d="M52 110 Q50 60 100 54 Q150 60 148 110" fill="#a04a22"/>`,
      barbe: `<path d="M60 104 Q62 152 100 158 Q138 152 140 104 Q132 128 114 132 Q100 122 86 132 Q68 128 60 104Z" fill="#a04a22"/>`,
      moustache: `<path d="M82 119 Q100 110 118 119 Q108 124 100 120 Q92 124 82 119Z" fill="#8a3a18"/>`,
      coiffe: `<path d="M56 84 Q56 30 100 28 Q144 30 144 84 Q100 72 56 84Z" fill="#5a2a2a"/><path d="M56 84 Q100 72 144 84 L144 92 Q100 80 56 92Z" fill="#7a3a3a"/>${[0, 1, 2, 3].map(i => `<path d="M${70 + i * 20} 40 v40" stroke="#4a2020" stroke-width="2"/>`).join("")}`,
      habitDetails: `<path d="M80 170 L100 196 L120 170" fill="#d8d0c0"/><path d="M40 190 L80 172 L84 240 L40 240Z M160 190 L120 172 L116 240 L160 240Z" fill="#5a3a22"/><path d="M168 240 L188 40" stroke="#6a4a2a" stroke-width="5"/><path d="M188 40 l-6 -20 l12 4z" fill="#c9c9c9"/>`
    }
  };

  VML.svgPortrait = function(id){
    const o = P[id] || P.aronnax;
    return `<svg viewBox="0 0 200 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="${(VML.perso && VML.perso(id) || {}).nom || id}">${tete(o)}</svg>`;
  };

  /** HTML d'un portrait (cadre ovale) ; la cascade fichier → dessin s'applique ensuite. */
  VML.htmlPortrait = function(id, classe){
    return `<div class="portrait-ovale ${classe || ""}" data-perso="${id}"><div class="portrait-contenu">${VML.svgPortrait(id)}</div><div class="portrait-cadre" aria-hidden="true"></div></div>`;
  };

  /** Remplace le dessin par le fichier déposé s'il existe. */
  VML.installerPortrait = async function(el){
    if(!el) return;
    const id = el.dataset.perso;
    if(VML.parametre && VML.parametre("secours") === "1") return;
    if(!(id in VML.sourcesPerso)){
      VML.sourcesPerso[id] = (async () => {
        for(const ext of [".webp", ".png", ".jpg"]){
          const r = await VML.sonderImage("assets/images/personnages/" + id + ext, 2500);
          if(r) return r.url;
        }
        return null;
      })();
    }
    const url = await VML.sourcesPerso[id];
    if(url){
      el.classList.add("fichier");
      el.querySelector(".portrait-contenu").innerHTML = `<img src="${url}" alt="${(VML.perso(id) || {}).nom || id}">`;
    }
  };
})();
