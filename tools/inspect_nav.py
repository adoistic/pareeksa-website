import glob
import re

desktop_items = {}
mobile_items = {}
all_pages = glob.glob('*.html')

for path in sorted(all_pages):
    content = open(path, encoding='utf-8').read()
    
    # Desktop nav mega menu
    dm = re.search(r'class="nav-dropdown-menu nav-mega-menu">([\s\S]*?)</div>\s*</div>\s*</div>', content)
    if dm:
        cols = re.findall(r'<h4 class="nav-mega-title">([^<]+)</h4>([\s\S]*?)(?=<h4|$)', dm.group(1))
        for col_title, col_content in cols:
            items = re.findall(r'<a href="([^"]+)">([^<]+)</a>', col_content)
            for href, text in items:
                desktop_items[text.strip()] = href.strip()

    # Mobile nav mega menu
    mm = re.search(r'class="mobile-dropdown-menu mobile-mega-menu">([\s\S]*?)</div>\s*</div>', content)
    if mm:
        secs = re.findall(r'<h4 class="mobile-mega-title">([^<]+)</h4>([\s\S]*?)(?=<h4|$)', mm.group(1))
        for sec_title, sec_content in secs:
            items = re.findall(r'<a href="([^"]+)">([^<]+)</a>', sec_content)
            for href, text in items:
                mobile_items[text.strip()] = href.strip()

print("--- DESKTOP CAPABILITIES MENU ---")
for text, href in desktop_items.items():
    print(f"Text: '{text}' -> Href: '{href}'")

print("\n--- MOBILE CAPABILITIES MENU ---")
for text, href in mobile_items.items():
    print(f"Text: '{text}' -> Href: '{href}'")
