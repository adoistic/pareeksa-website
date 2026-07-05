# tools/

Build scripts for the generated parts of the site. The 14 service detail pages
(`omr.html`, `osm.html`, … `translation.html`) are **generated** — do not hand-edit
them. Edit the data/templates in `build_services.py` and re-run it.

## Regenerate the service pages

```bash
python3 tools/build_services.py
```

Reads the `SERVICES` data model plus the SVG sprite and shared header/footer
(pulled live from `index.html` so they stay in sync), and writes each
`<slug>.html` at the repo root. After adding or renaming a service, also update
`sitemap.xml`, `llms.txt`, and the landing page's links/OfferCatalog by hand.

## Refresh the feature icons

```bash
python3 tools/fetch_icons.py
```

Pulls a curated set of Icons8 line icons (ios7 style) via the Icons8 MCP endpoint
and saves them to `assets/i8/`. They are rendered on-site as CSS `mask-image` with
`background: currentColor`, so they inherit the brand colour and dark mode. Cached
files are skipped. See `assets/i8/_manifest.json` for what maps to which Icons8 id.
