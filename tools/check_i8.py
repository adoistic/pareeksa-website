import glob
import os
import re

all_files = glob.glob("**/*", recursive=True)

missing_i8 = []
found_i8 = 0

for path in sorted(all_files):
    if not (path.endswith(".html") or path.endswith(".css") or path.endswith(".js")):
        continue
    try:
        content = open(path, encoding='utf-8').read()
        urls = re.findall(r'url\((["\']?assets/i8/[^"\'\)]+["\']?)\)', content)
        for u in urls:
            clean_u = u.strip("\"'").replace("%20", " ")
            if not os.path.isfile(clean_u):
                missing_i8.append((path, clean_u))
            else:
                found_i8 += 1
    except Exception:
        pass

print(f"Verified {found_i8} i8 icon background URLs.")
if missing_i8:
    print(f"Found {len(missing_i8)} missing i8 icon files:")
    for f, u in set(missing_i8):
        print(f"  In {f}: '{u}' NOT FOUND")
else:
    print("SUCCESS: 0 missing i8 icon files found!")
