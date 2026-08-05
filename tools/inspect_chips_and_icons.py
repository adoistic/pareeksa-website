import glob
import re

html_files = sorted(glob.glob("*.html"))

print("=== CHECKING FOR MISSING CHIPS / CARD ICONS IN SECTIONS ===")

for path in html_files:
    content = open(path, encoding='utf-8').read()
    
    # Check chips in "Built in from the start" or .chips
    chips_blocks = re.findall(r'<ul class="chips">([\s\S]*?)</ul>', content)
    for idx, cb in enumerate(chips_blocks):
        items = re.findall(r'<li class="chip">([\s\S]*?)</li>', cb)
        missing_count = 0
        total = len(items)
        missing_labels = []
        for it in items:
            has_icon = ('class="i8"' in it) or ('<svg' in it) or ('<img' in it)
            label = re.sub(r'<[^>]+>', '', it).strip()
            if not has_icon:
                missing_count += 1
                missing_labels.append(label)
        if missing_count > 0:
            print(f"File: {path} | .chips block {idx+1}: {missing_count}/{total} items missing icons -> {missing_labels}")

    # Check adv-grid
    adv_blocks = re.findall(r'<ul class="adv-grid">([\s\S]*?)</ul>', content)
    for idx, ab in enumerate(adv_blocks):
        items = re.findall(r'<li class="adv[^"]*">([\s\S]*?)</li>', ab)
        missing_count = 0
        total = len(items)
        missing_labels = []
        for it in items:
            has_icon = ('adv-ico' in it) or ('class="i8"' in it) or ('<svg' in it)
            h3 = re.search(r'<h3>([^<]+)</h3>', it)
            label = h3.group(1) if h3 else "unknown"
            if not has_icon:
                missing_count += 1
                missing_labels.append(label)
        if missing_count > 0:
            print(f"File: {path} | .adv-grid block {idx+1}: {missing_count}/{total} items missing icons -> {missing_labels}")

    # Check spec-grid
    spec_blocks = re.findall(r'<div class="spec-grid">([\s\S]*?)</div>\s*</div>', content)
    for idx, sb in enumerate(spec_blocks):
        specs = re.findall(r'<div class="spec[^"]*">([\s\S]*?)</div>', sb)
        for s_idx, sp in enumerate(specs):
            spec_h = re.search(r'<p class="spec-h">([\s\S]*?)</p>', sp)
            if spec_h:
                sh_text = spec_h.group(1)
                has_sh_icon = ('class="i8"' in sh_text) or ('<svg' in sh_text)
                sh_label = re.sub(r'<[^>]+>', '', sh_text).strip()
                if not has_sh_icon:
                    print(f"File: {path} | .spec-h missing icon: '{sh_label}'")

    # Check flow steps
    flow_blocks = re.findall(r'<ol class="flow"[^>]*>([\s\S]*?)</ol>', content)
    for idx, fb in enumerate(flow_blocks):
        steps = re.findall(r'<li class="flow-step"[^>]*>([\s\S]*?)</li>', fb)
        for s_idx, st in enumerate(steps):
            has_ico = ('flow-ico' in st) or ('class="i8"' in st)
            h3 = re.search(r'<h3>([^<]+)</h3>', st)
            label = h3.group(1) if h3 else "step"
            if not has_ico:
                print(f"File: {path} | flow-step missing icon in step '{label}'")
