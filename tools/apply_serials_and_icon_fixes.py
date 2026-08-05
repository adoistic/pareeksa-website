import os
import glob
import re

print("=== 1. FIXING BROKEN CHIP ICONS IN AI EXAMINATION FILES ===")
ai_files = [
    "ai-examination.html",
    "ai-examination-document-solutions.html",
    "AI-driven Examination & Document Solutions.html"
]

for af in ai_files:
    if os.path.isfile(af):
        content = open(af, encoding='utf-8').read()
        c_new = content.replace("assets/i8/ai.png", "assets/i8/sparkles.png").replace("assets/i8/security.png", "assets/i8/shield.png")
        if c_new != content:
            open(af, "w", encoding='utf-8').write(c_new)
            print(f"Fixed broken chip icons in: {af}")

print("\n=== 2. UPDATING CONTINUOUS GLOBAL SERVICE SERIALS (Service 01 / 25 to Service 25 / 25) ===")

master_services = [
    ("omr.html", "Service 01 / 25", "#ic-omr"),
    ("osm.html", "Service 02 / 25", "#ic-osm"),
    ("online-examination.html", "Service 03 / 25", "#ic-online"),
    ("pre-post-examination.html", "Service 04 / 25", "#ic-prepost"),
    ("ocr.html", "Service 05 / 25", "#ic-ocr"),
    ("icr.html", "Service 06 / 25", "#ic-icr"),
    ("document-scanning.html", "Service 07 / 25", "#ic-scan"),
    ("document-management.html", "Service 08 / 25", "#ic-dms"),
    ("printing.html", "Service 09 / 25", "#ic-print"),
    ("ai-examination.html", "Service 10 / 25", "#ic-ai"),
    ("custom-portals.html", "Service 11 / 25", "#ic-portals"),
    ("high-performance-platforms.html", "Service 12 / 25", "#ic-portals"),
    ("cloud-devops.html", "Service 13 / 25", "#ic-ai"),
    ("app-security.html", "Service 14 / 25", "#ic-security"),
    ("internet-of-things.html", "Service 15 / 25", "#ic-ai"),
    ("artificial-intelligence.html", "Service 16 / 25", "#ic-ai"),
    ("ai-modules.html", "Service 17 / 25", "#ic-ai"),
    ("agentic-ai.html", "Service 18 / 25", "#ic-voice"),
    ("translation.html", "Service 19 / 25", "#ic-translation"),
    ("blockchain-identity.html", "Service 20 / 25", "#ic-security"),
    ("data-analytics.html", "Service 21 / 25", "#ic-ocr"),
    ("drones-uavs.html", "Service 22 / 25", "#ic-scan"),
    ("robotics-systems.html", "Service 23 / 25", "#ic-ai"),
    ("solar-energy.html", "Service 24 / 25", "#ic-online"),
    ("tech-skilling.html", "Service 25 / 25", "#ic-translation"),
]

# File aliases dict to sync aliases
aliases = {
    "ai-examination.html": ["ai-examination-document-solutions.html", "AI-driven Examination & Document Solutions.html"],
    "high-performance-platforms.html": ["High Performance Platforms & Applications.html"],
    "cloud-devops.html": ["Cloud & DevOps.html"],
    "internet-of-things.html": ["Internet of Things.html"],
    "blockchain-identity.html": ["Blockchain & Identity.html"],
    "data-analytics.html": ["Data Analytics.html"],
    "drones-uavs.html": ["Drones & UAVs.html"],
    "robotics-systems.html": ["Robotics & Systems.html"],
    "solar-energy.html": ["Solar & Energy.html"],
    "tech-skilling.html": ["Tech Skilling.html"]
}

for page, serial, icon in master_services:
    target_files = [page] + aliases.get(page, [])
    for tf in target_files:
        if os.path.isfile(tf):
            content = open(tf, encoding='utf-8').read()
            # Replace serial
            c_new = re.sub(r'<span class="page-hero-serial">[^<]+</span>', f'<span class="page-hero-serial">{serial}</span>', content)
            if c_new != content:
                open(tf, "w", encoding='utf-8').write(c_new)
                print(f"Updated serial on {tf} -> {serial}")

print("\n=== 3. EXPANDING HOME PAGE (index.html) CAPABILITIES GRID ===")

capabilities_section_html = '''  <!-- CAPABILITIES -->
  <section class="section" id="capabilities" aria-labelledby="cap-h">
    <div class="wrap">
      <header class="section-head">
        <p class="eyebrow reveal">Beyond the exam hall</p>
        <h2 class="section-title reveal" id="cap-h">Everything around it</h2>
        <p class="section-lead reveal">The same care applied to documents, software and AI — for institutions and companies that need the work done right.</p>
      </header>

      <div class="cap-block">
        <div class="cap-aside reveal">
          <span class="cap-aside-tag mono">Documents</span>
          <h3 class="cap-aside-title">Document intelligence</h3>
          <p class="cap-aside-desc">Capture, read, organise and print the paper and files an institution runs on — turned into data you can search and trust.</p>
        </div>
        <ul class="cap-list">
          <li class="cap-item reveal">
            <span class="cap-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-ocr"/></svg></span>
            <div class="cap-item-body">
              <div class="cap-item-head"><h4><a class="cap-link" href="ocr.html">OCR</a></h4><svg class="cap-go" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg><span class="cap-item-num mono">05</span></div>
              <p>Turn scanned pages and PDFs into text you can search and edit: printed forms, registers, books, ledgers. We tune the model to your documents instead of a generic one.</p>
            </div>
          </li>
          <li class="cap-item reveal">
            <span class="cap-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-icr"/></svg></span>
            <div class="cap-item-body">
              <div class="cap-item-head"><h4><a class="cap-link" href="icr.html">ICR</a></h4><svg class="cap-go" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg><span class="cap-item-num mono">06</span></div>
              <p>Read hand-printed characters from filled forms and application boxes. Every field comes back with a confidence score, so a person checks only what is doubtful.</p>
            </div>
          </li>
          <li class="cap-item reveal">
            <span class="cap-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-scan"/></svg></span>
            <div class="cap-item-body">
              <div class="cap-item-head"><h4><a class="cap-link" href="document-scanning.html">Document scanning</a></h4><svg class="cap-go" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg><span class="cap-item-num mono">07</span></div>
              <p>High-volume scanning of files, registers and archives. We come to you or you ship to us; you get organised digital copies, named and indexed the way you work.</p>
            </div>
          </li>
          <li class="cap-item reveal">
            <span class="cap-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-dms"/></svg></span>
            <div class="cap-item-body">
              <div class="cap-item-head"><h4><a class="cap-link" href="document-management.html">Document management</a></h4><svg class="cap-go" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg><span class="cap-item-num mono">08</span></div>
              <p>A place to store, find and control documents: version history, access by role, full-text search, retention dates. Built around your filing logic, not a stock template.</p>
            </div>
          </li>
          <li class="cap-item reveal">
            <span class="cap-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-print"/></svg></span>
            <div class="cap-item-body">
              <div class="cap-item-head"><h4><a class="cap-link" href="printing.html">Printing</a></h4><svg class="cap-go" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg><span class="cap-item-num mono">09</span></div>
              <p>Print work tied to exams and records: question papers under controlled handling, OMR sheets, certificates, mark sheets, variable-data runs. Secure where it has to be.</p>
            </div>
          </li>
          <li class="cap-item reveal">
            <span class="cap-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-ai"/></svg></span>
            <div class="cap-item-body">
              <div class="cap-item-head"><h4><a class="cap-link" href="ai-examination.html">AI-driven examination &amp; document solutions</a></h4><svg class="cap-go" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg><span class="cap-item-num mono">10</span></div>
              <p>Task-scoped AI for document processing, intelligent archive search, and proctored automated evaluation systems.</p>
            </div>
          </li>
        </ul>
      </div>

      <div class="cap-block">
        <div class="cap-aside reveal">
          <span class="cap-aside-tag mono">Engineering</span>
          <h3 class="cap-aside-title">Digital engineering</h3>
          <p class="cap-aside-desc">Ultra-low latency web platforms, scalable APIs, and secure applications built to fit your organizational workflow.</p>
        </div>
        <ul class="cap-list">
          <li class="cap-item reveal">
            <span class="cap-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-portals"/></svg></span>
            <div class="cap-item-body">
              <div class="cap-item-head"><h4><a class="cap-link" href="custom-portals.html">Custom portals</a></h4><svg class="cap-go" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg><span class="cap-item-num mono">11</span></div>
              <p>Web and mobile apps built to fit your process. Admin portals, candidate apps, dashboards. We build, then maintain.</p>
            </div>
          </li>
          <li class="cap-item reveal">
            <span class="cap-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-portals"/></svg></span>
            <div class="cap-item-body">
              <div class="cap-item-head"><h4><a class="cap-link" href="high-performance-platforms.html">High performance platforms &amp; applications</a></h4><svg class="cap-go" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg><span class="cap-item-num mono">12</span></div>
              <p>Architected for extreme scale, low latency, and zero downtime. Microservices and distributed applications built for heavy load.</p>
            </div>
          </li>
          <li class="cap-item reveal">
            <span class="cap-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-ai"/></svg></span>
            <div class="cap-item-body">
              <div class="cap-item-head"><h4><a class="cap-link" href="cloud-devops.html">Cloud &amp; DevOps</a></h4><svg class="cap-go" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg><span class="cap-item-num mono">13</span></div>
              <p>Streamline software delivery and ensure cloud reliability. Infrastructure as Code, CI/CD pipelines, and 24/7 telemetry.</p>
            </div>
          </li>
          <li class="cap-item reveal">
            <span class="cap-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-security"/></svg></span>
            <div class="cap-item-body">
              <div class="cap-item-head"><h4><a class="cap-link" href="app-security.html">App security testing</a></h4><svg class="cap-go" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg><span class="cap-item-num mono">14</span></div>
              <p>We test your app the way an attacker would and report what breaks, with steps to reproduce and a fix priority.</p>
            </div>
          </li>
          <li class="cap-item reveal">
            <span class="cap-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-ai"/></svg></span>
            <div class="cap-item-body">
              <div class="cap-item-head"><h4><a class="cap-link" href="internet-of-things.html">Internet of Things (IoT)</a></h4><svg class="cap-go" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg><span class="cap-item-num mono">15</span></div>
              <p>Bridge physical assets with digital intelligence. Smart sensor networks, real-time edge telemetry, and monitoring dashboards.</p>
            </div>
          </li>
        </ul>
      </div>

      <div class="cap-block">
        <div class="cap-aside reveal">
          <span class="cap-aside-tag mono">AI &amp; Systems</span>
          <h3 class="cap-aside-title">AI &amp; intelligent systems</h3>
          <p class="cap-aside-desc">Machine learning algorithms, voice agents, data analytics, and tamper-proof verification built for scale.</p>
        </div>
        <ul class="cap-list">
          <li class="cap-item reveal">
            <span class="cap-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-ai"/></svg></span>
            <div class="cap-item-body">
              <div class="cap-item-head"><h4><a class="cap-link" href="artificial-intelligence.html">Artificial intelligence</a></h4><svg class="cap-go" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg><span class="cap-item-num mono">16</span></div>
              <p>Custom AI models and machine learning pipelines engineered for real-world enterprise operations and intelligent decisioning.</p>
            </div>
          </li>
          <li class="cap-item reveal">
            <span class="cap-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-ai"/></svg></span>
            <div class="cap-item-body">
              <div class="cap-item-head"><h4><a class="cap-link" href="ai-modules.html">AI modules</a></h4><svg class="cap-go" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg><span class="cap-item-num mono">17</span></div>
              <p>Specific AI dropped into a real task: search across messy archives, research assistants, and automated workflow scripting.</p>
            </div>
          </li>
          <li class="cap-item reveal">
            <span class="cap-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-voice"/></svg></span>
            <div class="cap-item-body">
              <div class="cap-item-head"><h4><a class="cap-link" href="agentic-ai.html">Agentic AI voice calls</a></h4><svg class="cap-go" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg><span class="cap-item-num mono">18</span></div>
              <p>An AI that takes phone calls and holds a real conversation. It follows your flow, answers questions, and routes outcomes.</p>
            </div>
          </li>
          <li class="cap-item reveal">
            <span class="cap-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-translation"/></svg></span>
            <div class="cap-item-body">
              <div class="cap-item-head"><h4><a class="cap-link" href="translation.html">Translation</a></h4><svg class="cap-go" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg><span class="cap-item-num mono">19</span></div>
              <p>Documents and content moved between languages by people who read both, with the meaning kept intact.</p>
            </div>
          </li>
          <li class="cap-item reveal">
            <span class="cap-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-security"/></svg></span>
            <div class="cap-item-body">
              <div class="cap-item-head"><h4><a class="cap-link" href="blockchain-identity.html">Blockchain &amp; identity</a></h4><svg class="cap-go" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg><span class="cap-item-num mono">20</span></div>
              <p>Immutable trust and tamper-proof digital verification. Cryptographic credential issuance and decentralized identity solutions.</p>
            </div>
          </li>
          <li class="cap-item reveal">
            <span class="cap-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-ocr"/></svg></span>
            <div class="cap-item-body">
              <div class="cap-item-head"><h4><a class="cap-link" href="data-analytics.html">Data analytics</a></h4><svg class="cap-go" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg><span class="cap-item-num mono">21</span></div>
              <p>Turn disparate institutional data into clear, actionable intelligence with ETL pipelines, data warehouses, and executive dashboards.</p>
            </div>
          </li>
        </ul>
      </div>

      <div class="cap-block">
        <div class="cap-aside reveal">
          <span class="cap-aside-tag mono">Emerging</span>
          <h3 class="cap-aside-title">Emerging technologies</h3>
          <p class="cap-aside-desc">Next-generation hardware, aerial surveying, solar energy software, and technical skilling for modern teams.</p>
        </div>
        <ul class="cap-list">
          <li class="cap-item reveal">
            <span class="cap-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-scan"/></svg></span>
            <div class="cap-item-body">
              <div class="cap-item-head"><h4><a class="cap-link" href="drones-uavs.html">Drones &amp; UAVs</a></h4><svg class="cap-go" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg><span class="cap-item-num mono">22</span></div>
              <p>Autonomous aerial intelligence, high precision LiDAR mapping, thermal inspection, and custom UAV software integrations.</p>
            </div>
          </li>
          <li class="cap-item reveal">
            <span class="cap-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-ai"/></svg></span>
            <div class="cap-item-body">
              <div class="cap-item-head"><h4><a class="cap-link" href="robotics-systems.html">Robotics &amp; systems</a></h4><svg class="cap-go" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg><span class="cap-item-num mono">23</span></div>
              <p>Bridging intelligent software control with physical hardware automation, robotics systems, and real-time telemetry.</p>
            </div>
          </li>
          <li class="cap-item reveal">
            <span class="cap-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-online"/></svg></span>
            <div class="cap-item-body">
              <div class="cap-item-head"><h4><a class="cap-link" href="solar-energy.html">Solar &amp; energy</a></h4><svg class="cap-go" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg><span class="cap-item-num mono">24</span></div>
              <p>Clean energy monitoring, solar farm yield optimization, inverter telemetry, and predictive generation analytics.</p>
            </div>
          </li>
          <li class="cap-item reveal">
            <span class="cap-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#ic-translation"/></svg></span>
            <div class="cap-item-body">
              <div class="cap-item-head"><h4><a class="cap-link" href="tech-skilling.html">Tech skilling</a></h4><svg class="cap-go" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg><span class="cap-item-num mono">25</span></div>
              <p>Institutional technical training, hands-on software workshops, emerging technology bootcamps, and skill assessment platforms.</p>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </section>'''

idx_content = open("index.html", encoding='utf-8').read()
idx_new = re.sub(
    r'<!-- CAPABILITIES -->\s*<section class="section" id="capabilities" aria-labelledby="cap-h">[\s\S]*?</section>',
    capabilities_section_html,
    idx_content
)

if idx_new != idx_content:
    open("index.html", "w", encoding='utf-8').write(idx_new)
    print("Successfully expanded Capabilities section in index.html with all 21 items (05 to 25)")

print("=== ALL UPDATES APPLIED SUCCESSFULLY ===")
