#!/usr/bin/env python3
"""Recherche et téléchargement d'images libres : Wikimedia Commons, Gallica (BnF), Openverse.

Usage :
  python scripts/images.py commons  "abbaye de Cluny" [-n 5] [--download] [--width 1200]
  python scripts/images.py gallica  "carte Bourgogne"  [-n 5] [--download] [--width 1200]
  python scripts/images.py openverse "poterie"         [-n 5] [--download]

Sans --download : affiche seulement les résultats (titre, licence, auteur, URL).
Avec --download : enregistre dans images/ et ajoute les crédits à images/credits.json.
Aucune dépendance externe (bibliothèque standard Python 3.8+).
"""
import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

UA = "ImagesLibresScript/1.0 (usage pedagogique; contact: kou657@gmail.com)"
OUT_DIR = Path("images")
CREDITS = OUT_DIR / "credits.json"


def http_get(url, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    return data if binary else data.decode("utf-8", "replace")


def strip_html(s):
    return re.sub(r"<[^>]+>", "", s or "").strip()


def slug(s, n=60):
    s = re.sub(r"[^\w\-]+", "_", s, flags=re.UNICODE).strip("_")
    return s[:n] or "image"


# ---------- Wikimedia Commons ----------
def search_commons(query, n, width):
    params = {
        "action": "query", "generator": "search", "gsrnamespace": "6",
        "gsrsearch": f"filetype:bitmap {query}", "gsrlimit": str(n),
        "prop": "imageinfo", "iiprop": "url|extmetadata|size",
        "iiurlwidth": str(width), "format": "json",
    }
    url = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params)
    data = json.loads(http_get(url))
    pages = sorted(data.get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 0))
    res = []
    for p in pages:
        ii = (p.get("imageinfo") or [{}])[0]
        meta = ii.get("extmetadata", {})
        res.append({
            "source": "commons",
            "title": p.get("title", "").replace("File:", ""),
            "author": strip_html(meta.get("Artist", {}).get("value")),
            "license": meta.get("LicenseShortName", {}).get("value", "?"),
            "page_url": ii.get("descriptionurl"),
            "image_url": ii.get("thumburl") or ii.get("url"),
        })
    return res


# ---------- Gallica (SRU + IIIF) ----------
def search_gallica(query, n, width):
    cql = f'(gallica all "{query}") and (dc.type all "image")'
    params = {"operation": "searchRetrieve", "version": "1.2",
              "maximumRecords": str(n), "query": cql}
    url = "https://gallica.bnf.fr/SRU?" + urllib.parse.urlencode(params)
    root = ET.fromstring(http_get(url))
    res = []
    for rec in root.iter("{http://www.loc.gov/zing/srw/}record"):
        title = creator = rights = ark = None
        for el in rec.iter():
            tag = el.tag.split("}")[-1]
            txt = (el.text or "").strip()
            if tag == "title" and not title:
                title = txt
            elif tag == "creator" and not creator:
                creator = txt
            elif tag == "rights" and not rights:
                rights = txt
            elif tag == "identifier" and "ark:/12148/" in txt and not ark:
                ark = txt
        if not ark:
            continue
        m = re.search(r"ark:/12148/[\w]+", ark)
        if not m:
            continue
        ark_id = m.group(0)
        res.append({
            "source": "gallica",
            "title": title or ark_id,
            "author": creator or "",
            "license": rights or "voir conditions de réutilisation BnF",
            "page_url": f"https://gallica.bnf.fr/{ark_id}",
            "image_url": f"https://gallica.bnf.fr/iiif/{ark_id}/f1/full/{width},/0/native.jpg",
        })
    return res


# ---------- Openverse ----------
def search_openverse(query, n, width):
    params = {"q": query, "page_size": str(n)}
    url = "https://api.openverse.org/v1/images/?" + urllib.parse.urlencode(params)
    data = json.loads(http_get(url))
    return [{
        "source": "openverse",
        "title": r.get("title") or "",
        "author": r.get("creator") or "",
        "license": f"{r.get('license', '?')} {r.get('license_version') or ''}".strip(),
        "page_url": r.get("foreign_landing_url"),
        "image_url": r.get("url"),
    } for r in data.get("results", [])]


SOURCES = {"commons": search_commons, "gallica": search_gallica, "openverse": search_openverse}


def download(item, idx):
    OUT_DIR.mkdir(exist_ok=True)
    ext = Path(urllib.parse.urlparse(item["image_url"]).path).suffix.lower()
    if ext not in (".jpg", ".jpeg", ".png", ".gif", ".webp", ".tif", ".tiff"):
        ext = ".jpg"
    path = OUT_DIR / f"{item['source']}_{slug(item['title'])}{ext}"
    path.write_bytes(http_get(item["image_url"], binary=True))
    item["file"] = str(path)
    credits = json.loads(CREDITS.read_text("utf-8")) if CREDITS.exists() else []
    credits = [c for c in credits if c.get("file") != item["file"]]
    credits.append(item)
    CREDITS.write_text(json.dumps(credits, ensure_ascii=False, indent=2), "utf-8")
    return path


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", choices=SOURCES)
    ap.add_argument("query")
    ap.add_argument("-n", type=int, default=5, help="nombre de résultats (défaut 5)")
    ap.add_argument("--width", type=int, default=1200, help="largeur max en px (défaut 1200)")
    ap.add_argument("--download", action="store_true", help="télécharge dans images/")
    a = ap.parse_args()

    try:
        items = SOURCES[a.source](a.query, a.n, a.width)
    except Exception as e:
        sys.exit(f"Erreur de recherche ({a.source}) : {e}")
    if not items:
        sys.exit("Aucun résultat.")

    for i, it in enumerate(items, 1):
        print(f"[{i}] {it['title']}\n    auteur : {it['author'] or '?'} | licence : {it['license']}"
              f"\n    page : {it['page_url']}\n    image : {it['image_url']}")
        if a.download:
            try:
                print(f"    -> enregistrée : {download(it, i)}")
            except Exception as e:
                print(f"    -> échec téléchargement : {e}")
            time.sleep(1)  # politesse envers les serveurs
    if a.download:
        print(f"\nCrédits : {CREDITS}")


if __name__ == "__main__":
    main()
