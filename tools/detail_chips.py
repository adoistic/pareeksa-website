import glob
import re

html_files = sorted(glob.glob("*.html"))

print("=== INSPECTING ALL CHIPS BLOCKS ACROSS ALL HTML FILES ===")
for path in html_files:
    content = open(path, encoding='utf-8').read()
    chips_matches = re.finditer(r'<ul class="chips">([\s\S]*?)</ul>', content)
    for m_idx, match in enumerate(chips_matches, start=1):
        chips_html = match.group(1)
        lis = re.findall(r'<li class="chip">([\s\S]*?)</li>', chips_html)
        print(f"\nFile: {path} (Chips Block #{m_idx})")
        for li in lis:
            has_i8 = 'class="i8"' in li or 'class="chip-ico"' in li or '<svg' in li or '<img' in li
            text = re.sub(r'<[^>]+>', '', li).strip()
            status = "OK (has icon)" if has_i8 else "MISSING ICON"
            print(f"  [{status}] '{text}' (raw: {li.strip()[:80]}...)")
