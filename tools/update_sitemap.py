new_urls = [
    "ai-examination.html",
    "high-performance-platforms.html",
    "cloud-devops.html",
    "internet-of-things.html",
    "artificial-intelligence.html",
    "blockchain-identity.html",
    "data-analytics.html",
    "drones-uavs.html",
    "robotics-systems.html",
    "solar-energy.html",
    "tech-skilling.html"
]

with open("sitemap.xml", "r", encoding="utf-8") as f:
    content = f.read()

url_blocks = []
for u in new_urls:
    url_blocks.append(f'''  <url>
    <loc>https://pareeksa.com/{u}</loc>
    <lastmod>2026-07-21</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.8</priority>
  </url>''')

addition = "\n" + "\n".join(url_blocks) + "\n</urlset>"
new_content = content.replace("</urlset>", addition.lstrip())

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated sitemap.xml with new service URLs")
