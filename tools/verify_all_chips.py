import glob
import os
import re

html_files = sorted(glob.glob("*.html"))

all_valid = True
for path in html_files:
    content = open(path, encoding='utf-8').read()
    chips = re.findall(r'<li class="chip">([\s\S]*?)</li>', content)
    for c in chips:
        bg_m = re.search(r'url\((assets/i8/[^)]+)\)', c)
        if bg_m:
            img_path = bg_m.group(1).strip("\"'").replace("%20", " ")
            if not os.path.isfile(img_path):
                print(f"File: {path} | Invalid chip icon URL: '{img_path}'")
                all_valid = False
        else:
            txt = re.sub(r'<[^>]+>', '', c).strip()
            print(f"File: {path} | Chip missing url(): '{txt}'")
            all_valid = False

if all_valid:
    print("SUCCESS: Every chip across all HTML files has a valid existing i8 icon!")
