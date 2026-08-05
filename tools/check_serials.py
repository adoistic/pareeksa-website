import glob
import re

service_pages = [
    "omr.html",
    "osm.html",
    "online-examination.html",
    "pre-post-examination.html",
    "ocr.html",
    "icr.html",
    "document-scanning.html",
    "document-management.html",
    "printing.html",
    "ai-examination.html",
    "custom-portals.html",
    "high-performance-platforms.html",
    "cloud-devops.html",
    "app-security.html",
    "internet-of-things.html",
    "artificial-intelligence.html",
    "ai-modules.html",
    "agentic-ai.html",
    "translation.html",
    "blockchain-identity.html",
    "data-analytics.html",
    "drones-uavs.html",
    "robotics-systems.html",
    "solar-energy.html",
    "tech-skilling.html"
]

print("=== CHECKING SERVICE PAGES SERIALS AND ICONS ===")
for idx, p in enumerate(service_pages, start=1):
    try:
        content = open(p, encoding='utf-8').read()
        serial_m = re.search(r'<span class="page-hero-serial">([^<]+)</span>', content)
        serial = serial_m.group(1) if serial_m else "NOT FOUND"
        icon_m = re.search(r'<span class="page-hero-ico"><svg[^>]*><use href="([^"]+)"', content)
        icon = icon_m.group(1) if icon_m else "NOT FOUND"
        print(f"[{idx:02d}/25] {p:35s} -> Serial: '{serial}' | Icon: '{icon}'")
    except Exception as e:
        print(f"[{idx:02d}/25] {p:35s} -> ERROR: {e}")
