import glob
import os
import re

all_html_files = glob.glob("*.html")
print(f"Total HTML files in directory: {len(all_html_files)}")

broken_links = []
valid_links_count = 0

for path in sorted(all_html_files):
    content = open(path, encoding='utf-8').read()
    links = re.findall(r'href=["\']([^"\'#]+?\.html(?:#[^"\']*)?)["\']', content)
    for link in links:
        # Strip anchor
        clean_link = link.split('#')[0]
        # Ignore external http/https links
        if clean_link.startswith('http://') or clean_link.startswith('https://'):
            continue
        
        target_path = clean_link
        if not os.path.isfile(target_path):
            broken_links.append((path, link, target_path))
        else:
            valid_links_count += 1

print(f"Total valid local HTML links verified: {valid_links_count}")
if broken_links:
    print(f"WARNING: Found {len(broken_links)} broken links:")
    for src, link, tgt in broken_links:
        print(f"  In {src}: link '{link}' -> target '{tgt}' NOT FOUND")
else:
    print("SUCCESS: 0 broken links found across all HTML files!")
