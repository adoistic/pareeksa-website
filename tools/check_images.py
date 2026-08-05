import glob
import os
import re

all_html_files = glob.glob("*.html")

missing_images = []
found_images = 0

for path in sorted(all_html_files):
    content = open(path, encoding='utf-8').read()
    # Find img src
    srcs = re.findall(r'<img[^>]+src=["\']([^"\'#]+)["\']', content)
    for src in srcs:
        if src.startswith("http://") or src.startswith("https://") or src.startswith("data:"):
            continue
        # Unquote URL encoding like %20
        clean_src = src.replace("%20", " ")
        if not os.path.isfile(clean_src):
            missing_images.append((path, src))
        else:
            found_images += 1

print(f"Verified {found_images} image tags across {len(all_html_files)} HTML files.")
if missing_images:
    print(f"Found {len(missing_images)} missing image files:")
    for page, src in missing_images:
        print(f"  In {page}: '{src}' NOT FOUND")
else:
    print("SUCCESS: 0 missing image files found!")
