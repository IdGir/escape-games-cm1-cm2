"""Page HTML « immersifs/PROMPTS-GOOGLE-FLOW.html » : tous les prompts des jeux immersifs dans des cadres avec un bouton Copier.

Lit les PROMPTS-GOOGLE-FLOW.md générés par prompts-flow.py (à relancer avant) :
    python vingt-mille-lieues/outils/immersif/prompts-flow.py --tous
    python vingt-mille-lieues/outils/immersif/prompts-flow-html.py
"""
import html, json, os, re, sys

RACINE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
IMM = os.path.join(RACINE, "immersifs")
e = html.escape


def inline(t):
    t = e(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", t)


def carte(texte, titre="", etiquette="Copier"):
    return ('<div class="carte">' + (f'<div class="carte-t">{e(titre)}</div>' if titre else "")
            + f'<pre class="prompt">{e(texte)}</pre>'
            + f'<button type="button" class="copier">{e(etiquette)}</button></div>')


def convertir(md, jeu):
    out, L, i = [], md.split("\n"), 0
    dernier = ""
    while i < len(L):
        l = L[i]
        if l.startswith("```"):
            j = i + 1
            bloc = []
            while j < len(L) and not L[j].startswith("```"):
                bloc.append(L[j]); j += 1
            out.append(carte("\n".join(bloc), dernier))
            i = j + 1
            continue
        if l.startswith("> "):
            bloc = []
            while i < len(L) and L[i].startswith(">"):
                bloc.append(L[i][1:].strip()); i += 1
            txt = "\n".join(bloc).strip()
            out.append(carte(txt, "Charte de style (à ajouter si besoin)"))
            continue
        m = re.match(r"(#{1,3}) (.*)", l)
        if m:
            n = len(m.group(1))
            if len(m.group(1)) == 1:
                i += 1
                continue  # le titre de page est mis par jeu
            dernier = re.sub(r"[`*]", "", m.group(2))
            out.append(f"<h{n + 1}>{inline(m.group(2))}</h{n + 1}>")
        elif l.startswith("|"):
            rows = []
            while i < len(L) and L[i].startswith("|"):
                if not re.match(r"\|[-| ]+\|$", L[i]):
                    rows.append([c.strip() for c in L[i].strip("|").split("|")])
                i += 1
            t = "<table>" + "".join(("<tr>" + "".join(f"<{'th' if k == 0 else 'td'}>{inline(c)}</{'th' if k == 0 else 'td'}>" for c in r) + "</tr>") for k, r in enumerate(rows)) + "</table>"
            out.append(t)
            continue
        elif re.match(r"\s*(-|\d+\.) ", l):
            q = re.search(r"« (.+) »", l)
            item = re.sub(r"^\s*(-|\d+\.) ", "", l)
            if q and "départ" in l:
                nom = re.match(r"`([^`]+)`", item)
                out.append(f'<div class="video"><p>{inline(re.sub(r"« .+ »", "", item)).rstrip(" :")}</p>' + carte(q.group(1), "Prompt de mouvement (Agnes)") + "</div>")
            else:
                out.append(f"<p class=\"li\">{inline(item)}</p>")
        elif l.strip():
            out.append(f"<p>{inline(l)}</p>")
        i += 1
    return "\n".join(out)


PAGE = """<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Prompts Google Flow</title>
<style>
:root{--fond:#f6f4ef;--texte:#1d2430;--carte:#fff;--bord:#cfc8b8;--accent:#1f5f8b;--accent-t:#fff;--ok:#1d7a3e;--code:#f0ede4}
@media (prefers-color-scheme:dark){:root{--fond:#14181f;--texte:#e8e6df;--carte:#1c222c;--bord:#3a4352;--accent:#6fb1e0;--accent-t:#0b1118;--ok:#5fd08a;--code:#232b37}}
*{box-sizing:border-box}body{margin:0;background:var(--fond);color:var(--texte);font:16px/1.5 system-ui,Segoe UI,sans-serif}
header{position:sticky;top:0;background:var(--fond);border-bottom:1px solid var(--bord);padding:10px 16px;z-index:5}
header h1{font-size:1.15rem;margin:0 0 6px}nav{display:flex;flex-wrap:wrap;gap:6px}
nav a{padding:3px 10px;border:1px solid var(--bord);border-radius:99px;color:var(--texte);text-decoration:none;font-size:.9rem}
nav a:hover,nav a:focus{background:var(--accent);color:var(--accent-t)}
main{max-width:980px;margin:0 auto;padding:16px}
section.jeu{margin-bottom:48px}section.jeu>h2{font-size:1.5rem;border-bottom:2px solid var(--accent);padding-bottom:4px}
h3{margin:28px 0 8px;font-size:1.2rem}h4{margin:20px 0 6px;font-size:1.05rem}h5{margin:14px 0 4px}
.carte{background:var(--carte);border:1px solid var(--bord);border-radius:10px;padding:10px 12px;margin:8px 0 14px;position:relative}
.carte-t{font-size:.8rem;opacity:.7;margin-bottom:4px}
pre.prompt{margin:0 0 8px;white-space:pre-wrap;word-wrap:break-word;font:inherit;background:var(--code);padding:10px;border-radius:6px;user-select:all}
button.copier{background:var(--accent);color:var(--accent-t);border:0;border-radius:8px;padding:8px 18px;font-size:1rem;cursor:pointer;min-height:40px}
button.copier.ok{background:var(--ok);color:#fff}
code{background:var(--code);padding:1px 5px;border-radius:4px}table{border-collapse:collapse;width:100%;margin:8px 0;font-size:.92rem}
td,th{border:1px solid var(--bord);padding:4px 8px;text-align:left;vertical-align:top}.li{margin:3px 0}
details{margin:6px 0}summary{cursor:pointer;font-weight:600}
@media (max-width:600px){main{padding:12px}}
</style></head><body>
<header><h1>Prompts Google Flow — jeux immersifs</h1><nav>%NAV%</nav></header>
<main>
<p>Cliquez sur <strong>Copier</strong> sous un cadre, puis collez dans Google Flow (Images : 16:9 pour les décors, 3:4 pour les portraits). Les prompts de mouvement servent ensuite à Agnes. Vérifiez chaque image : objets numérotés visibles, bas de l'image calme, aucun texte, aucune personne réelle.</p>
%CORPS%
</main>
<script>
document.addEventListener("click",function(ev){
  var b=ev.target.closest("button.copier"); if(!b) return;
  var t=b.parentNode.querySelector("pre.prompt").textContent;
  function ok(){var v=b.textContent;b.textContent="Copié !";b.classList.add("ok");setTimeout(function(){b.textContent=v;b.classList.remove("ok");},1500);}
  function repli(){var r=document.createRange();r.selectNodeContents(b.parentNode.querySelector("pre.prompt"));var s=getSelection();s.removeAllRanges();s.addRange(r);try{document.execCommand("copy");ok();}catch(e){}}
  if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(ok,repli);}else{repli();}
});
</script></body></html>
"""

jeux = sorted(d for d in os.listdir(IMM) if os.path.isfile(os.path.join(IMM, d, "PROMPTS-GOOGLE-FLOW.md")))
nav, corps = [], []
for j in jeux:
    md = open(os.path.join(IMM, j, "PROMPTS-GOOGLE-FLOW.md"), encoding="utf-8").read()
    titre = (re.match(r"# Prompts Google Flow — (.*)", md) or [None, j])[1]
    # la section « Mode d'emploi » et les consignes sont communes : on les replie
    corps_j = convertir(md, j)
    corps_j = re.sub(r"(<h3>Mode d&#x27;emploi</h3>)(.*?)(?=<h3>)", r"<details><summary>Mode d&#x27;emploi</summary>\2</details>", corps_j, flags=re.S)
    nav.append(f'<a href="#{j}">{e(titre)}</a>')
    corps.append(f'<section class="jeu" id="{j}"><h2>{e(titre)}</h2>\n{corps_j}</section>')
sortie = os.path.join(IMM, "PROMPTS-GOOGLE-FLOW.html")
open(sortie, "w", encoding="utf-8", newline="\n").write(PAGE.replace("%NAV%", "".join(nav)).replace("%CORPS%", "\n".join(corps)))
print(os.path.relpath(sortie, RACINE), len(jeux), "jeux")
