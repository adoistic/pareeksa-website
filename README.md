# Pareeksa Technologies — website

A single-page marketing site for Pareeksa Technologies. Static, no build step, no
dependencies. Hand-tuned to the Pareeksa brand (the fountain-pen nib, Geist + Geist Mono,
institutional blue and ink, "Quiet Precision"). Designed to be crisp from ~280 px
(watch-class) up to 4K, in light and dark.

**Tagline:** The exam, examined.
**Live (production):** https://pareeksa.com

## Files

```
index.html          The page. All copy, SEO meta, Open Graph/Twitter, JSON-LD.
styles.css          Brand design system. Fluid type/space, light + dark, all breakpoints.
script.js           Theme toggle, mobile menu, scroll reveal, year. No libraries.
index.md            Markdown counterpart of the whole page.
llms.txt            Curated index for language models (llmstxt.org format).
llms-full.txt       Full company + services reference in one file.
agents.txt          Guidance for AI agents (how to read and how to contact).
robots.txt          Crawlers welcome; points to the sitemap.
sitemap.xml         URL list.
site.webmanifest    PWA manifest.
favicon.svg/.ico    App-icon (blue tile + white nib) favicons.
apple-touch-icon.png 180×180 home-screen icon.
fonts/              Self-hosted Geist + Geist Mono (variable woff2) + OFL licence.
assets/             Icons, OG images, brand mark. og/ holds the OG image generators.
CNAME               The custom domain (pareeksa.com) — required by GitHub Pages, no extension.
.nojekyll           Tells GitHub Pages to serve files as-is (no Jekyll).
```

## Preview locally

```bash
cd "Pareeksa Website"
python3 -m http.server 8000
# open http://localhost:8000
```

## Deploy to GitHub Pages

1. Create a repo and push these files to the default branch.
   ```bash
   git init && git add -A && git commit -m "Pareeksa Technologies website"
   gh repo create pareeksa-website --public --source=. --push   # or push manually
   ```
2. Repo → **Settings → Pages** → Source: **Deploy from a branch** → Branch: `main` / `/ (root)`.
3. Wait ~1 minute. The site goes live at `https://<user>.github.io/<repo>/`.

`.nojekyll` is included so every file (including `llms.txt`, `agents.txt`, dotfiles) is served verbatim.

## Custom domain (pareeksa.com) — connected

The repo root has a `CNAME` file containing `pareeksa.com`, and Settings → Pages → Custom
domain is set to match — that side is done. The remaining step is DNS, at whichever
registrar/DNS provider holds the domain (this project uses Cloudflare):

- Four apex `A` records → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`,
  `185.199.111.153` (DNS-only / grey-cloud until HTTPS is issued, see below)
- A `CNAME` for `www` → `adoistic.github.io`
- Once DNS resolves, tick **Enforce HTTPS** in Settings → Pages (can take up to ~24h to
  appear after GitHub verifies the domain and issues the certificate)

All canonical, Open Graph, sitemap and llms.txt URLs already use `https://pareeksa.com`, so
SEO and link previews are correct the moment DNS propagates.

## Editing

- **Copy:** all text lives in `index.html`. Keep the voice plain and concrete — no marketing
  puffery. If you change a service, update `index.md`, `llms.txt` and `llms-full.txt` to match.
- **Contact details:** phone/WhatsApp `+91 99990 26602`, email `corp@pareeksa.com`, address and
  GST appear in `index.html` (contact + footer + JSON-LD), `index.md`, `llms*.txt`, `agents.txt`.
- **Regenerate OG images** (after editing `assets/og/og.html` or `og-square.html`):
  ```bash
  CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
  "$CHROME" --headless=new --hide-scrollbars --force-device-scale-factor=2 \
    --window-size=1200,630 --screenshot=assets/og-image.png assets/og/og.html
  sips -z 630 1200 assets/og-image.png
  ```

## Roadmap — contact form

The site intentionally ships without a form; contact is WhatsApp + email. The plan is a small
open-source form backend you self-host on **Cloudflare Workers** (a free alternative to
Formspree): the Worker validates a POST, emails it to `corp@pareeksa.com`, and the site's
contact section gets a progressive-enhancement form that posts to it. To be specced and built
after this site is deployed.

## Fonts / licence

Geist and Geist Mono are licensed under the SIL Open Font License; see `fonts/OFL.txt`.
