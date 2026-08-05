import glob
import re

print("=== CHECKING ALL HTML, JS, TXT, XML FILES FOR REFERENCES ===")

files = glob.glob("**/*", recursive=True)
for file_path in sorted(files):
    if not (file_path.endswith('.html') or file_path.endswith('.js') or file_path.endswith('.txt') or file_path.endswith('.xml') or file_path.endswith('.md')):
        continue
    try:
        content = open(file_path, encoding='utf-8').read()
        links = re.findall(r'href=["\']([^"\'#]+?\.html)["\']', content)
        if links:
            print(f"\n{file_path} references HTML files:")
            for l in sorted(set(links)):
                print(f"  - {l}")
    except Exception as e:
        pass
