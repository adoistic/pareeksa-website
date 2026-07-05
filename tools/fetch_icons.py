#!/usr/bin/env python3
"""Fetch a curated icons8 line-icon set via the sanctioned MCP endpoint, self-host as PNG.
Rendered on-site via CSS mask-image so they recolour to brand + dark mode."""
import json, os, urllib.request, time

MCP = "https://mcp.icons8.com/mcp/"
OUT = "/Users/siraj/Pareeksa Website/assets/i8"
os.makedirs(OUT, exist_ok=True)

# slug -> search query. Line-style (ios7) preferred for stroke consistency.
TERMS = {
    "speed": "speedometer", "batch": "stack", "cloud": "cloud", "report": "combo-chart",
    "error-detect": "bug", "formats": "file", "realtime": "pulse", "database": "database",
    "lock": "lock", "remote": "globe", "users": "conference-call", "api": "api",
    "dashboard": "dashboard", "tag": "tags", "search": "search", "text": "text",
    "handwriting": "autograph", "version": "time-machine", "signature": "signature",
    "audit": "todo-list", "eye": "visible", "shuffle": "shuffle", "clock": "clock",
    "certificate": "diploma", "ticket": "ticket", "registration": "add-user-group-man-man",
    "printer": "print", "package": "box", "chat": "chat", "trending": "positive-dynamic",
    "star": "star", "sparkles": "sparkling", "calendar": "calendar", "phone": "phone",
    "headset": "headset", "pipeline": "flow-chart", "refresh": "recurring-appointment",
    "gauge": "dashboard-layout", "archive": "archive", "devices": "devices",
    "key": "key", "shield": "security-checked", "scan": "scanner", "translate": "translation",
    "network": "workflow", "brush": "design", "check-quality": "checked-checkbox",
    "book": "book", "robot": "bot", "integration": "integration", "camera": "camera",
    "layers": "layers", "monitor": "monitor", "form": "fill-form", "money": "cheap-2",
    "target": "target", "puzzle": "puzzle", "link": "link", "folder": "folder",
    "upload": "upload", "download": "download", "server": "server", "graph": "line-chart",
}

def rpc(method, params):
    body = json.dumps({"jsonrpc":"2.0","id":1,"method":method,"params":params}).encode()
    req = urllib.request.Request(MCP, data=body, headers={
        "Content-Type":"application/json",
        "Accept":"application/json, text/event-stream"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())

def pick(icons):
    order = ["ios7","ios","ios-glyphs","material-outlined","material-rounded","windows","win10"]
    for plat in order:
        for ic in icons:
            if ic.get("platform")==plat and not ic.get("isColor"):
                return ic
    for ic in icons:
        if not ic.get("isColor"):
            return ic
    return icons[0] if icons else None

manifest = {}
for slug, q in TERMS.items():
    dest = os.path.join(OUT, slug+".png")
    if os.path.exists(dest) and os.path.getsize(dest) > 200:
        manifest[slug] = "cached"; continue
    try:
        res = rpc("tools/call", {"name":"search_icons","arguments":{"query":q,"amount":12}})
        txt = res["result"]["content"][0]["text"]
        data = json.loads(txt)
        ic = pick(data.get("icons", []))
        if not ic:
            print(f"  MISS {slug} ({q})"); continue
        url = f"https://img.icons8.com/?id={ic['id']}&format=png&size=200"
        urllib.request.urlretrieve(url, dest)
        sz = os.path.getsize(dest)
        manifest[slug] = {"id":ic["id"],"name":ic["name"],"platform":ic["platform"],"q":q,"bytes":sz}
        print(f"  ok  {slug:16s} id={ic['id']:8s} {ic['platform']:18s} {sz}b")
    except Exception as e:
        print(f"  ERR {slug} ({q}): {e}")
    time.sleep(0.05)

with open(os.path.join(OUT,"_manifest.json"),"w") as f:
    json.dump(manifest, f, indent=2)
print(f"\nDone: {len([v for v in manifest.values() if v!='cached'])} fetched, saved to {OUT}")
