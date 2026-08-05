import glob
import os
import re

html_files = sorted(glob.glob("*.html"))

print("=== 1. CHECKING BROKEN USE HREF IN SVG SPRITE ===")
for path in html_files:
    content = open(path, encoding='utf-8').read()
    
    # Extract sprite symbols
    sprite_m = re.search(r'<svg[^>]*class="sprite"[^>]*>([\s\S]*?)</svg>', content)
    symbols = set()
    if sprite_m:
        symbols = set(re.findall(r'<symbol\s+id="([^"]+)"', sprite_m.group(1)))
    
    # Find all <use href="#...">
    uses = re.findall(r'<use\s+href="#([^"]+)"', content)
    for u in uses:
        if u not in symbols:
            print(f"File: {path} | Broken SVG use href: '#{u}' not defined in sprite!")

print("\n=== 2. CHECKING BROKEN URL IN STYLE ATTRIBUTES ===")
for path in html_files:
    content = open(path, encoding='utf-8').read()
    urls = re.findall(r'style="[^"]*url\(([^)]+)\)', content)
    for u in urls:
        clean_u = u.strip("\"'").replace("%20", " ")
        if clean_u.startswith("http://") or clean_u.startswith("https://") or clean_u.startswith("data:"):
            continue
        if not os.path.isfile(clean_u):
            print(f"File: {path} | Broken background URL: '{clean_u}' not found on disk!")

print("\n=== 3. CHECKING INCONSISTENT ICON MISSING IN CARDS / LISTS ===")
for path in html_files:
    content = open(path, encoding='utf-8').read()

    # Check chips
    chips = re.findall(r'<li class="chip">([\s\S]*?)</li>', content)
    if chips:
        has_icons = [('class="i8"' in c or '<svg' in c or '<img' in c) for c in chips]
        if any(has_icons) and not all(has_icons):
            for c in chips:
                if not ('class="i8"' in c or '<svg' in c or '<img' in c):
                    txt = re.sub(r'<[^>]+>', '', c).strip()
                    print(f"File: {path} | Inconsistent chip missing icon: '{txt}'")

    # Check adv-grid items
    advs = re.findall(r'<li class="adv[^"]*">([\s\S]*?)</li>', content)
    if advs:
        has_icons = [('adv-ico' in a or 'class="i8"' in a or '<svg' in a) for a in advs]
        if any(has_icons) and not all(has_icons):
            for a in advs:
                if not ('adv-ico' in a or 'class="i8"' in a or '<svg' in a):
                    h3 = re.search(r'<h3>([^<]+)</h3>', a)
                    txt = h3.group(1) if h3 else a.strip()[:30]
                    print(f"File: {path} | Inconsistent adv item missing icon: '{txt}'")

    # Check related cards
    rels = re.findall(r'<a class="related-card[^"]*"[^>]*>([\s\S]*?)</a>', content)
    if rels:
        has_icons = [('related-ico' in r or '<svg' in r or '<img' in r) for r in rels]
        if any(has_icons) and not all(has_icons):
            for r in rels:
                if not ('related-ico' in r or '<svg' in r or '<img' in r):
                    h3 = re.search(r'<h3>([^<]+)</h3>', r)
                    txt = h3.group(1) if h3 else r.strip()[:30]
                    print(f"File: {path} | Inconsistent related card missing icon: '{txt}'")
