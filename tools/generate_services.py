import os
import glob
import re

# Template data for missing services
missing_services = {
    "artificial-intelligence.html": {
        "title": "Artificial Intelligence solutions — Pareeksa Technologies",
        "h1": "Artificial Intelligence solutions",
        "serial": "Service 10 / 21",
        "icon": "#ic-ai",
        "meta_desc": "Artificial Intelligence solutions — enterprise machine learning models, predictive intelligence, automated decision systems, and custom neural architectures built for operational scale. Pareeksa Technologies.",
        "lead": "Custom AI models and machine learning pipelines engineered for real-world enterprise operations. We build, fine-tune, and deploy intelligent algorithms tailored specifically to your data ecosystem.",
        "flow": [
            ("01", "Data Engineering", "Raw data ingestion, cleaning, structuring, and feature engineering.", "assets/i8/server.png"),
            ("02", "Model Training", "Training bespoke machine learning models on domain specific datasets.", "assets/i8/text.png"),
            ("03", "Validation & Safety", "Testing model outputs for accuracy, bias mitigation, and safety confidence.", "assets/i8/check-quality.png"),
            ("04", "Production Deployment", "High throughput REST and gRPC API integration into enterprise applications.", "assets/i8/cloud.png"),
        ],
        "chips": ["Machine Learning", "Neural Networks", "Predictive Analytics", "Natural Language Processing", "Computer Vision", "Automated Decisioning", "Model Fine-tuning", "Enterprise MLOps"],
        "adv": [
            ("Automation at scale", "Eliminate repetitive manual decision making with high confidence AI inference.", "assets/i8/target.png"),
            ("Domain adaptation", "Models trained directly on your institution's proprietary workflows and terminology.", "assets/i8/check-quality.png"),
            ("Real-time telemetry", "Instant predictions with continuous monitoring and drift detection.", "assets/i8/speed.png"),
            ("Secure & Private", "On-premise or sovereign cloud deployment options with zero external data exposure.", "assets/i8/server.png"),
            ("Cost efficiency", "Optimized model architectures designed for low latency and minimal compute overhead.", "assets/i8/money.png"),
        ],
        "spec_left": ["Custom PyTorch & TensorFlow architectures", "Real-time API endpoints", "Automated retraining pipelines", "Model performance telemetry", "Enterprise SLA support"],
        "spec_right": ["End-to-end data privacy", "Strict RBAC security controls", "Audit logging for AI decisions", "High availability redundancy", "Zero vendor lock-in"],
        "related": [
            ("ai-modules.html", "#ic-ai", "AI Modules", "Task-scoped AI modules for document processing, search, and research."),
            ("agentic-ai.html", "#ic-voice", "Agentic AI Voice Calls", "Autonomous conversational AI agents for automated call handling."),
            ("data-analytics.html", "#ic-ocr", "Data Analytics", "Transform enterprise data into actionable intelligence dashboards.")
        ]
    },
    "drones-uavs.html": {
        "title": "Drones & UAV solutions — Pareeksa Technologies",
        "h1": "Drones & UAV solutions",
        "serial": "Service 11 / 21",
        "icon": "#ic-scan",
        "meta_desc": "Drones & UAV solutions — aerial surveying, mapping, automated inspection, computer vision analysis, and UAV software integrations for large scale infrastructure. Pareeksa Technologies.",
        "lead": "Autonomous aerial intelligence and unmanned aerial vehicle solutions. We deliver aerial scanning, telemetry processing, GIS mapping, and custom software for UAV fleet operations.",
        "flow": [
            ("01", "Mission Planning", "Autonomous flight path definition and sensor configuration.", "assets/i8/scan.png"),
            ("02", "Aerial Capture", "High resolution multispectral imagery and LiDAR point cloud acquisition.", "assets/i8/speed.png"),
            ("03", "Photogrammetry", "Automated image stitching, elevation modeling, and 3D reconstruction.", "assets/i8/form.png"),
            ("04", "Analytics Report", "AI-assisted defect detection, asset tracking, and spatial analytics.", "assets/i8/server.png"),
        ],
        "chips": ["Aerial Surveying", "LiDAR Point Cloud", "Photogrammetry 3D", "Defect Detection", "GIS Mapping", "Thermal Imaging", "Autonomous Flight", "Asset Management"],
        "adv": [
            ("Rapid area coverage", "Inspect hundreds of acres in hours rather than weeks of manual field surveys.", "assets/i8/speed.png"),
            ("Millimeter precision", "High precision GPS and RTK position correction for accurate spatial maps.", "assets/i8/target.png"),
            ("Hazard reduction", "Inspect high voltage, high altitude, or dangerous infrastructure safely from the ground.", "assets/i8/check-quality.png"),
            ("AI vision processing", "Automated anomaly detection pinpoints structural flaws or environmental shifts.", "assets/i8/text.png"),
            ("Comprehensive audit", "Historical digital twin records for long-term infrastructural planning.", "assets/i8/cloud.png"),
        ],
        "spec_left": ["RTK/PPK centimetre accuracy", "Multi-spectral & thermal payloads", "Automated mission autopilot", "Cloud spatial GIS viewer", "Export to CAD/BIM formats"],
        "spec_right": ["DGCA compliant operations", "Secure data transmission", "Encrypted storage vaults", "Role-based project access", "Disaster recovery backups"],
        "related": [
            ("robotics-systems.html", "#ic-ai", "Robotics & Systems", "Hardware and software integration for autonomous robotics."),
            ("solar-energy.html", "#ic-online", "Solar & Energy", "Thermal aerial inspection and yield optimization for energy sites."),
            ("document-scanning.html", "#ic-scan", "Document Scanning", "Digitize physical archives and spatial survey records.")
        ]
    },
    "high-performance-platforms.html": {
        "title": "High Performance Platforms & Applications — Pareeksa Technologies",
        "h1": "High Performance Platforms & Applications",
        "serial": "Service 12 / 21",
        "icon": "#ic-portals",
        "meta_desc": "High Performance Platforms & Applications — ultra-low latency web platforms, high scale backend systems, microservices, and distributed applications built for heavy load. Pareeksa Technologies.",
        "lead": "Architected for extreme scale, low latency, and zero downtime. We engineer high performance web applications, microservices, and distributed platforms capable of handling millions of concurrent users.",
        "flow": [
            ("01", "Architecture", "Designing event-driven, distributed systems with clear domain boundaries.", "assets/i8/server.png"),
            ("02", "Core Development", "High performance coding in Rust, Go, Node.js, and modern frontend frameworks.", "assets/i8/speed.png"),
            ("03", "Stress Testing", "Rigorous load testing simulating peak traffic concurrent user floods.", "assets/i8/batch.png"),
            ("04", "Global Rollout", "Multi-region deployment with automated failover and edge caching.", "assets/i8/cloud.png"),
        ],
        "chips": ["Low Latency", "Event-Driven", "Microservices", "High Throughput", "Distributed Caching", "Load Balancing", "Zero Downtime", "Horizontal Scaling"],
        "adv": [
            ("Sub-millisecond response", "Optimized database queries and in-memory caching deliver rapid load times.", "assets/i8/speed.png"),
            ("Unmatched concurrency", "Engineered to withstand sudden traffic spikes without degradation.", "assets/i8/target.png"),
            ("Resilient architecture", "Self-healing microservices ensure isolated failures never bring down the site.", "assets/i8/check-quality.png"),
            ("Elastic scaling", "Auto-scaling infrastructure grows dynamically with real-time user demand.", "assets/i8/cloud.png"),
            ("Reduced cloud bill", "Efficient compute utilization minimizes infrastructure costs per request.", "assets/i8/money.png"),
        ],
        "spec_left": ["Distributed event streams", "Redis/Memcached caching layers", "Kubernetes cluster orchestration", "Automated CI/CD pipelines", "Real-time APM telemetry"],
        "spec_right": ["99.99% uptime SLA guarantee", "SOC2 compliant design", "Zero-downtime rolling updates", "End-to-end TLS encryption", "DDoS mitigation built-in"],
        "related": [
            ("custom-portals.html", "#ic-portals", "Custom Portals", "Tailor-made portals built around your specific workflow."),
            ("cloud-devops.html", "#ic-ai", "Cloud & DevOps", "Cloud infrastructure setup, container management, and DevOps."),
            ("app-security.html", "#ic-security", "App Security Testing", "Attacker's eye testing for web apps and APIs.")
        ]
    },
    "cloud-devops.html": {
        "title": "Cloud & DevOps services — Pareeksa Technologies",
        "h1": "Cloud & DevOps services",
        "serial": "Service 13 / 21",
        "icon": "#ic-ai",
        "meta_desc": "Cloud & DevOps services — multi-cloud migration, Infrastructure as Code, CI/CD automation, Kubernetes management, and cloud security optimization. Pareeksa Technologies.",
        "lead": "Streamline software delivery and ensure cloud reliability. We design, build, and maintain cloud infrastructure, automated deployment pipelines, and continuous monitoring environments.",
        "flow": [
            ("01", "Cloud Audit", "Evaluating existing workloads, architecture bottlenecks, and security posture.", "assets/i8/search.png"),
            ("02", "IaC Definition", "Codifying infrastructure using Terraform, Pulumi, and Ansible templates.", "assets/i8/text.png"),
            ("03", "CI/CD Pipeline", "Automating testing, security scanning, and seamless deployments.", "assets/i8/speed.png"),
            ("04", "24/7 Monitoring", "Continuous telemetry, log aggregation, and automated alerting.", "assets/i8/server.png"),
        ],
        "chips": ["AWS & Azure", "Terraform IaC", "Kubernetes (K8s)", "Docker Containers", "CI/CD Pipelines", "Cost Optimization", "Site Reliability", "Cloud Security"],
        "adv": [
            ("Faster release velocity", "Ship code updates safely multiple times a day with automated testing.", "assets/i8/speed.png"),
            ("Reproducible infrastructure", "Entire server environments defined in code, eliminating configuration drift.", "assets/i8/target.png"),
            ("Cost optimization", "Right-sizing instances and eliminating idle resources lowers cloud expenses.", "assets/i8/money.png"),
            ("High availability", "Multi-availability zone failover guarantees continuous service uptime.", "assets/i8/check-quality.png"),
            ("Proactive security", "Automated vulnerability patching and compliance governance.", "assets/i8/cloud.png"),
        ],
        "spec_left": ["Multi-cloud orchestration", "Automated container builds", "Infrastructure as Code", "Prometheus & Grafana metrics", "Zero-downtime deployments"],
        "spec_right": ["SOC2 & ISO 27001 readiness", "Encrypted storage at rest/transit", "Strict IAM permissions", "Disaster recovery automation", "24/7 incident response"],
        "related": [
            ("high-performance-platforms.html", "#ic-portals", "High Performance Platforms", "Ultra-low latency web platforms and applications."),
            ("app-security.html", "#ic-security", "App Security Testing", "Vulnerability assessment and pentesting."),
            ("custom-portals.html", "#ic-portals", "Custom Portals", "Web and mobile applications custom built for institutions.")
        ]
    },
    "internet-of-things.html": {
        "title": "Internet of Things (IoT) solutions — Pareeksa Technologies",
        "h1": "Internet of Things (IoT) solutions",
        "serial": "Service 14 / 21",
        "icon": "#ic-ai",
        "meta_desc": "Internet of Things (IoT) solutions — smart sensor networks, IoT gateways, real-time edge telemetry, embedded software, and industrial monitoring platforms. Pareeksa Technologies.",
        "lead": "Bridge physical assets with digital intelligence. We engineer IoT device software, sensor networks, cloud data pipelines, and real-time monitoring dashboards for industrial and institutional use.",
        "flow": [
            ("01", "Sensor Deployment", "Selecting and calibrating IoT hardware, microcontrollers, and sensors.", "assets/i8/scan.png"),
            ("02", "Edge Telemetry", "Ingesting real-time device signals over MQTT, CoAP, and HTTP protocols.", "assets/i8/speed.png"),
            ("03", "Data Processing", "Stream processing data pipelines filtering signals and detecting triggers.", "assets/i8/server.png"),
            ("04", "Live Dashboard", "Visualizing metrics, alerts, and historical trends in responsive portals.", "assets/i8/form.png"),
        ],
        "chips": ["Smart Sensors", "MQTT Protocol", "Edge Computing", "Real-Time Telemetry", "Industrial IoT", "Embedded Firmware", "Predictive Maintenance", "IoT Dashboards"],
        "adv": [
            ("Real-time visibility", "Monitor equipment performance, temperature, and environmental status remotely.", "assets/i8/speed.png"),
            ("Predictive maintenance", "Detect anomalous readings early to service hardware before critical failure.", "assets/i8/target.png"),
            ("Automated alerts", "Instant instant SMS/email notifications when sensor thresholds are breached.", "assets/i8/check-quality.png"),
            ("Low bandwidth efficient", "Optimized binary data protocols designed for remote or weak cellular links.", "assets/i8/cloud.png"),
            ("Operational intelligence", "Historical sensory data drives efficiency gains and resource savings.", "assets/i8/money.png"),
        ],
        "spec_left": ["MQTT, LoRaWAN, Cellular connectivity", "Firmware Over-The-Air (FOTA)", "Stream analytics processing", "Edge device management", "Custom sensor calibration"],
        "spec_right": ["Hardware root-of-trust security", "End-to-end payload encryption", "Role-based telemetry dashboards", "Scalable to 100,000+ devices", "Industrial grade reliability"],
        "related": [
            ("robotics-systems.html", "#ic-ai", "Robotics & Systems", "Hardware and control systems engineering."),
            ("solar-energy.html", "#ic-online", "Solar & Energy", "Smart meter and energy generation monitoring."),
            ("data-analytics.html", "#ic-ocr", "Data Analytics", "Transform sensor data streams into actionable operational insights.")
        ]
    },
    "blockchain-identity.html": {
        "title": "Blockchain & Identity solutions — Pareeksa Technologies",
        "h1": "Blockchain & Identity solutions",
        "serial": "Service 15 / 21",
        "icon": "#ic-security",
        "meta_desc": "Blockchain & Identity solutions — tamper-proof credential verification, decentralized identity (DID), smart contracts, and immutable digital audit trails. Pareeksa Technologies.",
        "lead": "Immutable trust and tamper-proof digital verification. We build blockchain verification systems, cryptographic credential issuance platforms, and decentralized identity solutions for institutions.",
        "flow": [
            ("01", "Credential Generation", "Digitally signing certificates, mark sheets, and official records.", "assets/i8/text.png"),
            ("02", "Cryptographic Hashing", "Computing unique SHA-256 hashes anchored to blockchain nodes.", "assets/i8/target.png"),
            ("03", "Verification Portal", "Public or private verification interface for instant authenticity checks.", "assets/i8/search.png"),
            ("04", "Audit Trail", "Permanent, unalterable historical ledger of issuance and verification events.", "assets/i8/server.png"),
        ],
        "chips": ["Tamper-Proof Records", "Cryptographic Verification", "Smart Contracts", "Decentralized ID (DID)", "Zero Knowledge Proofs", "Immutable Audit", "Digital Certificates", "Key Management"],
        "adv": [
            ("Zero forgery risk", "Degrees, certificates, and records cannot be altered or falsified.", "assets/i8/target.png"),
            ("Instant verification", "Employers and third parties verify document authenticity in seconds via QR.", "assets/i8/speed.png"),
            ("Self-sovereign identity", "Users control their credential data without relying on central single points of failure.", "assets/i8/check-quality.png"),
            ("Regulatory compliance", "Cryptographic proof satisfies stringent legal and audit standards.", "assets/i8/cloud.png"),
            ("Cost reduction", "Eliminate manual manual background verification calls and physical document mailings.", "assets/i8/money.png"),
        ],
        "spec_left": ["EVM & Permissioned Ledgers", "W3C Verifiable Credentials", "Public key cryptography", "Automated QR verification", "RESTful verification APIs"],
        "spec_right": ["Zero Knowledge privacy controls", "Hardware security modules (HSM)", "GDPR compliance compatibility", "Immutable tamper logging", "High speed verification SLAs"],
        "related": [
            ("app-security.html", "#ic-security", "App Security Testing", "Attacker's eye penetration testing for portals and APIs."),
            ("printing.html", "#ic-print", "Printing Services", "Secure physical printing with anti-counterfeit features."),
            ("custom-portals.html", "#ic-portals", "Custom Portals", "Tailor-made web and mobile application portals.")
        ]
    },
    "data-analytics.html": {
        "title": "Data Analytics services — Pareeksa Technologies",
        "h1": "Data Analytics services",
        "serial": "Service 16 / 21",
        "icon": "#ic-ocr",
        "meta_desc": "Data Analytics services — business intelligence, automated reporting, data warehousing, executive dashboards, and statistical modeling. Pareeksa Technologies.",
        "lead": "Turn disparate institutional data into clear, actionable intelligence. We build custom data pipelines, central data warehouses, and interactive visual analytics dashboards.",
        "flow": [
            ("01", "Ingestion & ETL", "Extracting data from databases, APIs, legacy sheets, and external streams.", "assets/i8/server.png"),
            ("02", "Data Warehousing", "Structuring relational and dimensional data models for fast query performance.", "assets/i8/batch.png"),
            ("03", "Statistical Modeling", "Applying statistical analysis, trend forecasting, and metric aggregation.", "assets/i8/text.png"),
            ("04", "Interactive Dashboards", "Deploying responsive executive portals with live drill-down capabilities.", "assets/i8/form.png"),
        ],
        "chips": ["Business Intelligence", "ETL Data Pipelines", "Data Warehousing", "Interactive Dashboards", "Statistical Modeling", "Trend Forecasting", "Executive Reporting", "Real-Time Metrics"],
        "adv": [
            ("Single source of truth", "Unify scattered operational data into centralized, audited dashboards.", "assets/i8/target.png"),
            ("Faster decision making", "Real-time key performance indicators eliminate delayed monthly reporting.", "assets/i8/speed.png"),
            ("Predictive insights", "Identify bottlenecks, student performance patterns, or resource operational trends.", "assets/i8/check-quality.png"),
            ("Automated distribution", "Scheduled PDF reports and instant anomaly alerts sent to stakeholders.", "assets/i8/cloud.png"),
            ("Cost efficiency", "Identify operational waste and optimize resource allocation.", "assets/i8/money.png"),
        ],
        "spec_left": ["Modern data warehouse stack", "Automated ETL/ELT pipelines", "Custom interactive visual charts", "SQL & NoSQL optimization", "Role-based dashboard views"],
        "spec_right": ["Data anonymization & masking", "Granular row-level security", "Full audit trail access logs", "HIPAA / FERPA compliance ready", "Automated backups"],
        "related": [
            ("artificial-intelligence.html", "#ic-ai", "Artificial Intelligence", "Predictive modeling and custom AI algorithms."),
            ("document-management.html", "#ic-dms", "Document Management", "Full-text search, versioning, and document archives."),
            ("custom-portals.html", "#ic-portals", "Custom Portals", "Web and mobile portals engineered for your institution.")
        ]
    },
    "robotics-systems.html": {
        "title": "Robotics & Systems — Pareeksa Technologies",
        "h1": "Robotics & Systems",
        "serial": "Service 17 / 21",
        "icon": "#ic-ai",
        "meta_desc": "Robotics & Systems — autonomous mobile robots, robotic process automation (RPA), hardware-software integration, and control systems. Pareeksa Technologies.",
        "lead": "Bridging intelligent software control with physical hardware automation. We design robotic systems, custom control interfaces, and hardware-integrated software solutions.",
        "flow": [
            ("01", "Systems Design", "Hardware selection, kinematic modeling, and interface specifications.", "assets/i8/form.png"),
            ("02", "Control Software", "Developing real-time embedded control algorithms and ROS nodes.", "assets/i8/speed.png"),
            ("03", "Integration", "Connecting sensors, actuators, motor controllers, and cloud telemetry.", "assets/i8/server.png"),
            ("04", "Field Deployment", "Calibration, safety compliance testing, and site commissioning.", "assets/i8/check-quality.png"),
        ],
        "chips": ["Robot Operating System (ROS)", "Autonomous Mobile Robots", "Control Systems", "Hardware Integration", "Embedded C++ / Python", "Computer Vision", "Telemetry Control", "Safety Systems"],
        "adv": [
            ("High precision operation", "Repeatable physical task execution with sub-millimeter precision.", "assets/i8/target.png"),
            ("24/7 autonomous labor", "Continuous system operation reducing human fatigue and danger exposure.", "assets/i8/speed.png"),
            ("Real-time telemetry", "Stream motor diagnostics, power draw, and positional coordinates live.", "assets/i8/cloud.png"),
            ("Modular scalability", "Expand robotic fleets seamlessly with standardized software protocols.", "assets/i8/check-quality.png"),
            ("Reduced operational cost", "Lower long-term maintenance and task overhead costs.", "assets/i8/money.png"),
        ],
        "spec_left": ["ROS / ROS2 architecture", "Real-time micro-controller interfaces", "CAN bus & Modbus communication", "Autonomous navigation algorithms", "Remote telemetry control"],
        "spec_right": ["Hardware fail-safe interlocks", "Emergency stop mechanisms", "ISO safety standard compliance", "Encrypted wireless links", "Proactive sensor diagnostics"],
        "related": [
            ("drones-uavs.html", "#ic-scan", "Drones & UAVs", "Aerial surveillance and surveying solutions."),
            ("internet-of-things.html", "#ic-ai", "Internet of Things (IoT)", "Smart sensors and edge hardware telemetry."),
            ("ai-modules.html", "#ic-ai", "AI Modules", "Task-scoped AI modules for automation.")
        ]
    },
    "solar-energy.html": {
        "title": "Solar & Energy solutions — Pareeksa Technologies",
        "h1": "Solar & Energy solutions",
        "serial": "Service 18 / 21",
        "icon": "#ic-online",
        "meta_desc": "Solar & Energy solutions — renewable energy monitoring, solar farm yield optimization, smart grid telemetry, and energy management software. Pareeksa Technologies.",
        "lead": "Maximize clean energy output and grid efficiency. We develop software platforms for solar farm monitoring, inverter telemetry, energy yield forecasting, and grid analytics.",
        "flow": [
            ("01", "Telemetry Setup", "Connecting solar inverters, weather stations, and meters to edge gateways.", "assets/i8/scan.png"),
            ("02", "Data Aggregation", "Ingesting power generation metrics, irradiation data, and grid frequency.", "assets/i8/server.png"),
            ("03", "Analytics & AI", "Analyzing string performance, detecting panel soiling, and predicting yield.", "assets/i8/speed.png"),
            ("04", "Optimization", "Automating battery storage dispatch and grid feedback routines.", "assets/i8/cloud.png"),
        ],
        "chips": ["Solar PV Monitoring", "Inverter Telemetry", "Energy Yield Optimization", "Smart Grid Integration", "Thermal Defect Detection", "Predictive Generation", "Battery Management", "Clean Tech Software"],
        "adv": [
            ("Maximize power yield", "Identify degraded or dirty solar strings early to restore maximum generation.", "assets/i8/target.png"),
            ("Automated fault alerts", "Instant notifications when inverter efficiency drops or grid trips occur.", "assets/i8/check-quality.png"),
            ("Accurate forecasting", "AI-based weather and solar irradiance forecasting for grid scheduling.", "assets/i8/speed.png"),
            ("Remote asset control", "Monitor geographically dispersed solar plants from a single central portal.", "assets/i8/cloud.png"),
            ("Faster ROI", "Optimized maintenance and higher uptime shorten payback periods.", "assets/i8/money.png"),
        ],
        "spec_left": ["Modbus RTU / TCP & SunSpec API", "Real-time inverter telemetry", "AI generation forecasting", "String level fault diagnosis", "Centralized SCADA dashboard"],
        "spec_right": ["Cybersecurity grid compliance", "Encrypted data streams", "Multi-site tenant access", "Historical data retention", "99.9% uptime SLA"],
        "related": [
            ("drones-uavs.html", "#ic-scan", "Drones & UAVs", "Thermal aerial inspection of solar arrays."),
            ("internet-of-things.html", "#ic-ai", "Internet of Things (IoT)", "Smart sensors and edge data telemetry."),
            ("data-analytics.html", "#ic-ocr", "Data Analytics", "Executive dashboards for operational energy metrics.")
        ]
    },
    "tech-skilling.html": {
        "title": "Tech Skilling & Training — Pareeksa Technologies",
        "h1": "Tech Skilling & Training",
        "serial": "Service 19 / 21",
        "icon": "#ic-translation",
        "meta_desc": "Tech Skilling & Training — institutional technical training, hands-on software workshops, emerging technology bootcamps, and developer skill assessments. Pareeksa Technologies.",
        "lead": "Empower your workforce and students with modern technology capabilities. We provide technical curriculum, hands-on software workshops, and verified skill assessment platforms.",
        "flow": [
            ("01", "Needs Assessment", "Evaluating current skill benchmarks and target competency goals.", "assets/i8/search.png"),
            ("02", "Curriculum Design", "Structuring practical, project-based learning modules and labs.", "assets/i8/text.png"),
            ("03", "Interactive Execution", "Delivering live coding sessions, workshops, and mentored projects.", "assets/i8/speed.png"),
            ("04", "Evaluation & Certs", "Proctored skill assessments and verifiable digital credential issuance.", "assets/i8/check-quality.png"),
        ],
        "chips": ["Software Engineering", "AI & ML Bootcamps", "Cloud & DevOps Labs", "Cybersecurity Training", "Proctored Skill Exams", "Hands-on Projects", "Digital Certification", "Corporate Skilling"],
        "adv": [
            ("Industry relevant curriculum", "Train on production ready tools and modern engineering practices.", "assets/i8/target.png"),
            ("Hands-on lab environments", "Practical coding exercises rather than purely theoretical lectures.", "assets/i8/speed.png"),
            ("Proctored assessments", "Verify student mastery using Pareeksa's secure evaluation tech.", "assets/i8/check-quality.png"),
            ("Verifiable credentials", "Tamper-proof digital certificates issued upon course completion.", "assets/i8/cloud.png"),
            ("Accelerated productivity", "Shorten onboarding time for new software engineers and technical staff.", "assets/i8/money.png"),
        ],
        "spec_left": ["Hands-on sandbox environments", "Custom enterprise curriculum", "Live proctored exams", "Automated code grading", "Skill progress telemetry"],
        "spec_right": ["Verifiable digital certificates", "Role-based admin portals", "Comprehensive reporting", "Scalable cohort sizes", "Continuous mentor support"],
        "related": [
            ("online-examination.html", "#ic-online", "Online Examination", "Platform for online question banks, randomized sets, and invigilation."),
            ("blockchain-identity.html", "#ic-security", "Blockchain & Identity", "Verifiable tamper-proof digital certificates."),
            ("custom-portals.html", "#ic-portals", "Custom Portals", "Custom LMS and student portal development.")
        ]
    }
}

def build_service_html(filename, data):
    flow_items_html = ""
    for idx, (num, title, desc, img) in enumerate(data["flow"]):
        flow_items_html += f'''  <li class="flow-step" style="--n:{idx}">
    <span class="flow-num-dot">{num}</span>
    <div class="flow-node">
      <div class="flow-top"><span class="flow-ico"><span class="i8" style="--i:url({img})" aria-hidden="true"></span></span><span class="flow-num"></span></div>
      <h3>{title}</h3><p>{desc}</p>
    </div>
  </li>\n'''

    chips_html = "\n".join([f'    <li class="chip"><span class="i8" style="--i:url(assets/i8/check-quality.png)" aria-hidden="true"></span><span>{chip}</span></li>' for chip in data["chips"]])

    adv_html = ""
    for title, desc, img in data["adv"]:
        adv_html += f'''    <li class="adv reveal">
      <span class="adv-ico"><span class="i8" style="--i:url({img})" aria-hidden="true"></span></span>
      <h3>{title}</h3><p>{desc}</p>
    </li>\n'''

    spec_left_html = "\n".join([f'      <li>{item}</li>' for item in data["spec_left"]])
    spec_right_html = "\n".join([f'      <li>{item}</li>' for item in data["spec_right"]])

    related_html = ""
    for r_href, r_icon, r_title, r_desc in data["related"]:
        related_html += f'''    <a class="related-card reveal" href="{r_href}">
      <span class="related-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="{r_icon}"/></svg></span>
      <h3>{r_title}</h3>
      <p>{r_desc}</p>
      <span class="go">View service <svg viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg></span>
    </a>\n'''

    return f'''<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{data["title"]}</title>
<meta name="description" content="{data["meta_desc"]}">
<link rel="canonical" href="https://pareeksa.com/{filename}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="author" content="Pareeksa Technologies">
<meta name="theme-color" content="#F7F8FA" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0E0F13" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Pareeksa Technologies">
<meta property="og:title" content="{data["title"]}">
<meta property="og:description" content="{data["meta_desc"]}">
<meta property="og:url" content="https://pareeksa.com/{filename}">
<meta property="og:locale" content="en_IN">
<meta property="og:image" content="https://pareeksa.com/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{data["title"]}">
<meta name="twitter:description" content="{data["meta_desc"]}">
<meta name="twitter:image" content="https://pareeksa.com/assets/og-image.png">
<link rel="icon" href="favicon.ico" sizes="48x48">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="preload" href="fonts/Geist-variable.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/GeistMono-variable.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="styles.css">
<link rel="stylesheet" href="services.css">
<script>
  (function () {{
    try {{
      var t = localStorage.getItem('theme');
      if (t !== 'light' && t !== 'dark') {{ t = matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'; }}
      document.documentElement.setAttribute('data-theme', t);
    }} catch (e) {{}}
    document.documentElement.classList.add('js');
  }})();
</script>
<script type="application/ld+json">
{{
 "@context": "https://schema.org",
 "@graph": [
  {{
   "@type": "Service",
   "@id": "https://pareeksa.com/{filename}#service",
   "serviceType": "{data["h1"]}",
   "name": "{data["h1"]}",
   "description": "{data["meta_desc"]}",
   "url": "https://pareeksa.com/{filename}",
   "provider": {{
    "@id": "https://pareeksa.com/#org"
   }},
   "areaServed": "IN"
  }},
  {{
   "@type": "BreadcrumbList",
   "itemListElement": [
    {{
     "@type": "ListItem",
     "position": 1,
     "name": "Home",
     "item": "https://pareeksa.com/"
    }},
    {{
     "@type": "ListItem",
     "position": 2,
     "name": "{data["h1"]}",
     "item": "https://pareeksa.com/{filename}"
    }}
   ]
  }}
 ]
}}
</script>
<script src="script.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<svg width="0" height="0" class="sprite" aria-hidden="true" focusable="false">
  <symbol id="nib" viewBox="448 280 1152 1488">
    <path fill="currentColor" d="M 1070.65 328.425 C 1107.82 342.689 1109.87 370.358 1119.09 404.773 C 1124.88 427.193 1131.17 449.485 1137.93 471.632 C 1158.86 536.275 1184.62 599.253 1214.99 660.032 C 1281.84 791.541 1377.02 921.969 1489.9 1017.78 C 1503.68 1030.02 1523.76 1041.81 1535.28 1055.41 C 1550.67 1073.62 1555.72 1098.41 1548.66 1121.19 C 1543.15 1138.99 1522.01 1166.31 1511.08 1183.56 C 1497.13 1205.93 1483.83 1228.69 1471.19 1251.83 C 1408.52 1366.07 1367.16 1490.78 1349.16 1619.84 C 1344.12 1656.48 1342.81 1683.93 1339.88 1719.96 L 708.518 1719.93 C 696.003 1516.58 637.673 1332.38 523.554 1162.75 C 507.993 1139.62 493.317 1122.24 496.728 1091.96 C 501.662 1048.15 545.063 1033.91 572.219 1005.91 C 722.235 872.725 830.471 696.263 897.771 509.854 C 908.918 478.32 918.812 446.358 927.431 414.041 C 937.524 377.171 937.935 345.895 976.893 328.938 C 978.242 333.249 977.626 368.169 977.615 375.245 L 977.514 479.128 L 977.487 836 C 977.477 901.161 976.744 967.872 977.704 1032.92 C 972.699 1034.83 967.739 1036.86 962.828 1039 C 923.759 1055.86 893.205 1087.86 878.159 1127.66 C 863.396 1166.56 864.658 1209.73 881.667 1247.7 C 912.303 1315.89 992.103 1356.3 1064.85 1334.78 C 1214.7 1290.45 1220.16 1085.64 1070.58 1033.19 C 1069.06 999.571 1070.29 956.216 1070.29 921.653 L 1070.32 704.865 L 1070.25 460.184 C 1070.24 418.19 1069.16 370.117 1070.65 328.425 z"/>
  </symbol>
  <symbol id="wa" viewBox="0 0 24 24">
    <path fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.002-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.885-9.885 9.885m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413"/>
  </symbol>
  <symbol id="arrow" viewBox="0 0 24 24">
    <path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M5 12h14M13 6l6 6-6 6"/>
  </symbol>

  <!-- Service line-icons -->
  <symbol id="ic-omr" viewBox="0 0 24 24"><rect x="5" y="3" width="14" height="18" rx="2" pathLength="1"/><circle cx="9" cy="8.5" r="1.3" pathLength="1"/><circle cx="9" cy="13.5" r="1.3" pathLength="1"/><path d="M12.5 8.5H16M12.5 13.5H16" pathLength="1"/></symbol>
  <symbol id="ic-osm" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="13" rx="2" pathLength="1"/><path d="M8.4 10.6l2.4 2.4 4.8-4.9" pathLength="1"/><path d="M9.5 20.5h5M12 17v3.5" pathLength="1"/></symbol>
  <symbol id="ic-online" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2" pathLength="1"/><path d="M3 8.5h18" pathLength="1"/><circle cx="12" cy="14.5" r="3" pathLength="1"/><path d="M12 13v1.6l1.1.9" pathLength="1"/></symbol>
  <symbol id="ic-prepost" viewBox="0 0 24 24"><rect x="5" y="4.5" width="14" height="16.5" rx="2" pathLength="1"/><rect x="9" y="2.6" width="6" height="3.6" rx="1.2" pathLength="1"/><path d="M8.5 11l1.3 1.3 2.4-2.6M8.5 16l1.3 1.3 2.4-2.6" pathLength="1"/></symbol>
  <symbol id="ic-ocr" viewBox="0 0 24 24"><path d="M14 3H7v18h10V7z" pathLength="1"/><path d="M14 3v4h3" pathLength="1"/><path d="M9.5 12h5M9.5 15h5M9.5 18h3" pathLength="1"/></symbol>
  <symbol id="ic-icr" viewBox="0 0 24 24"><path d="M4 17.5c1.4-7.5 3.6-7.5 4.8-1.6M5 13.7h4.3" pathLength="1"/><path d="M13.6 14.6l5-5 2.2 2.2-5 5-2.9.7z" pathLength="1"/></symbol>
  <symbol id="ic-scan" viewBox="0 0 24 24"><path d="M4 8V5.5A1.5 1.5 0 0 1 5.5 4H8M16 4h2.5A1.5 1.5 0 0 1 20 5.5V8M20 16v2.5a1.5 1.5 0 0 1-1.5 1.5H16M8 20H5.5A1.5 1.5 0 0 1 4 18.5V16" pathLength="1"/><path d="M4 12h16" pathLength="1"/></symbol>
  <symbol id="ic-dms" viewBox="0 0 24 24"><path d="M9 4h6l4 4v10H9z" pathLength="1"/><path d="M15 4v4h4" pathLength="1"/><path d="M9 8H5v12h10v-2" pathLength="1"/></symbol>
  <symbol id="ic-print" viewBox="0 0 24 24"><path d="M7 9V4h10v5" pathLength="1"/><path d="M7 18H5a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2h-2" pathLength="1"/><rect x="7" y="15" width="10" height="6" rx="1" pathLength="1"/></symbol>
  <symbol id="ic-portals" viewBox="0 0 24 24"><rect x="3" y="4" width="13" height="11" rx="2" pathLength="1"/><path d="M3 8h13" pathLength="1"/><rect x="13.5" y="10.5" width="7.5" height="10.5" rx="1.6" pathLength="1"/></symbol>
  <symbol id="ic-ai" viewBox="0 0 24 24"><rect x="7" y="7" width="10" height="10" rx="2" pathLength="1"/><circle cx="12" cy="12" r="2" pathLength="1"/><path d="M12 7V4.5M12 19.5V17M7 12H4.5M19.5 12H17" pathLength="1"/></symbol>
  <symbol id="ic-voice" viewBox="0 0 24 24"><path d="M5 13v-1.5a7 7 0 0 1 14 0V13" pathLength="1"/><rect x="3" y="13" width="4" height="6" rx="1.8" pathLength="1"/><rect x="17" y="13" width="4" height="6" rx="1.8" pathLength="1"/><path d="M19 19v.4a3 3 0 0 1-3 3h-2.5" pathLength="1"/></symbol>
  <symbol id="ic-security" viewBox="0 0 24 24"><path d="M12 3l7.5 3v5.2c0 4.6-3.2 7.8-7.5 9.3-4.3-1.5-7.5-4.7-7.5-9.3V6z" pathLength="1"/><path d="M9 12l2.2 2.2 4-4.4" pathLength="1"/></symbol>
  <symbol id="ic-translation" viewBox="0 0 24 24"><path d="M3 5.5h10v7H7.5L4.5 15v-2.5H3z" pathLength="1"/><path d="M11 11.5h10v7h-2.5L15.5 21v-2.5H11z" pathLength="1"/></symbol>
</svg>

<header class="site-header" id="top">
  <div class="wrap header-inner">
    <a class="lockup" href="index.html" aria-label="Pareeksa Technologies — home">
      <svg class="lockup-mark" aria-hidden="true"><use href="#nib"/></svg>
      <span class="lockup-word">Pareeksa</span>
    </a>
    <nav class="nav" aria-label="Primary">
      <div class="nav-dropdown">
        <a href="#" class="nav-dropdown-trigger" aria-haspopup="true" aria-expanded="false">
          Examinations <span class="nav-arrow"></span>
        </a>
        <div class="nav-dropdown-menu">
          <a href="omr.html">OMR Software &amp; Services</a>
          <a href="osm.html">On-screen Marking</a>
          <a href="online-examination.html">Online Examination</a>
          <a href="pre-post-examination.html">Pre &amp; Post Examination</a>
        </div>
      </div>
      <div class="nav-dropdown">
        <a href="#" class="nav-dropdown-trigger" aria-haspopup="true" aria-expanded="false">
          Capabilities <span class="nav-arrow"></span>
        </a>
        <div class="nav-dropdown-menu nav-mega-menu">
          <div class="nav-mega-column">
            <h4 class="nav-mega-title">Document Intelligence</h4>
            <a href="ocr.html">OCR</a>
            <a href="icr.html">ICR</a>
            <a href="document-scanning.html">Document Scanning</a>
            <a href="document-management.html">Document Management</a>
            <a href="printing.html">Printing</a>
            <a href="ai-examination.html">AI-driven Examination &amp; Document Solutions</a>
          </div>
          <div class="nav-mega-column">
            <h4 class="nav-mega-title">Digital Engineering</h4>
            <a href="custom-portals.html">Custom Portals</a>
            <a href="high-performance-platforms.html">High Performance Platforms &amp; Applications</a>
            <a href="cloud-devops.html">Cloud &amp; DevOps</a>
            <a href="app-security.html">App Security Testing</a>
            <a href="internet-of-things.html">Internet of Things (IoT)</a>
          </div>
          <div class="nav-mega-column">
            <h4 class="nav-mega-title">AI &amp; Intelligent Systems</h4>
            <a href="artificial-intelligence.html">Artificial Intelligence</a>
            <a href="ai-modules.html">AI Modules</a>
            <a href="agentic-ai.html">Agentic AI Voice Calls</a>
            <a href="translation.html">Translation</a>
            <a href="blockchain-identity.html">Blockchain &amp; Identity</a>
            <a href="data-analytics.html">Data Analytics</a>
          </div>
          <div class="nav-mega-column">
            <h4 class="nav-mega-title">Emerging Technologies</h4>
            <a href="drones-uavs.html">Drones &amp; UAVs</a>
            <a href="robotics-systems.html">Robotics &amp; Systems</a>
            <a href="solar-energy.html">Solar &amp; Energy</a>
            <a href="tech-skilling.html">Tech Skilling</a>
          </div>
        </div>
      </div>
      <a href="index.html#contact">Contact</a>
    </nav>
    <div class="header-actions">
      <button class="theme-toggle" type="button" aria-label="Switch colour theme" title="Switch theme">
        <svg class="i-sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.2" fill="currentColor"/><g stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2.5v2.6M12 18.9v2.6M21.5 12h-2.6M5.1 12H2.5M18.4 5.6l-1.8 1.8M7.4 16.6l-1.8 1.8M18.4 18.4l-1.8-1.8M7.4 7.4 5.6 5.6"/></g></svg>
        <svg class="i-moon" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M20.5 14.2A8.2 8.2 0 0 1 9.8 3.5a.7.7 0 0 0-.93-.84A9.6 9.6 0 1 0 21.34 15.1a.7.7 0 0 0-.84-.92Z"/></svg>
      </button>
      <a class="btn btn-primary header-cta" href="https://wa.me/919999026602" target="_blank" rel="noopener">
        <svg class="btn-ico" viewBox="0 0 24 24" aria-hidden="true"><use href="#wa"/></svg>
        <span>WhatsApp</span>
      </a>
      <button class="menu-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-nav">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
  <nav class="mobile-nav" id="mobile-nav" aria-label="Mobile" hidden>
    <div class="mobile-dropdown">
      <button class="mobile-dropdown-trigger" type="button" aria-expanded="false">
        Examinations <span class="nav-arrow"></span>
      </button>
      <div class="mobile-dropdown-menu">
        <a href="omr.html">OMR Software &amp; Services</a>
        <a href="osm.html">On-screen Marking</a>
        <a href="online-examination.html">Online Examination</a>
        <a href="pre-post-examination.html">Pre &amp; Post Examination</a>
      </div>
    </div>
    <div class="mobile-dropdown">
      <button class="mobile-dropdown-trigger" type="button" aria-expanded="false">
        Capabilities <span class="nav-arrow"></span>
      </button>
      <div class="mobile-dropdown-menu mobile-mega-menu">
        <div class="mobile-mega-section">
          <h4 class="mobile-mega-title">Document Intelligence</h4>
          <a href="ocr.html">OCR</a>
          <a href="icr.html">ICR</a>
          <a href="document-scanning.html">Document Scanning</a>
          <a href="document-management.html">Document Management</a>
          <a href="printing.html">Printing</a>
          <a href="ai-examination.html">AI-driven Examination &amp; Document Solutions</a>
        </div>
        <div class="mobile-mega-section">
          <h4 class="mobile-mega-title">Digital Engineering</h4>
          <a href="custom-portals.html">Custom Portals</a>
          <a href="high-performance-platforms.html">High Performance Platforms &amp; Applications</a>
          <a href="cloud-devops.html">Cloud &amp; DevOps</a>
          <a href="app-security.html">App Security Testing</a>
          <a href="internet-of-things.html">Internet of Things (IoT)</a>
        </div>
        <div class="mobile-mega-section">
          <h4 class="mobile-mega-title">AI &amp; Intelligent Systems</h4>
          <a href="artificial-intelligence.html">Artificial Intelligence</a>
          <a href="ai-modules.html">AI Modules</a>
          <a href="agentic-ai.html">Agentic AI Voice Calls</a>
          <a href="translation.html">Translation</a>
          <a href="blockchain-identity.html">Blockchain &amp; Identity</a>
          <a href="data-analytics.html">Data Analytics</a>
        </div>
        <div class="mobile-mega-section">
          <h4 class="mobile-mega-title">Emerging Technologies</h4>
          <a href="drones-uavs.html">Drones &amp; UAVs</a>
          <a href="robotics-systems.html">Robotics &amp; Systems</a>
          <a href="solar-energy.html">Solar &amp; Energy</a>
          <a href="tech-skilling.html">Tech Skilling</a>
        </div>
      </div>
    </div>
    <a href="index.html#contact">Contact</a>
    <a class="mobile-cta" href="https://wa.me/919999026602" target="_blank" rel="noopener">Message on WhatsApp</a>
  </nav>
</header>

<main id="main">

  <section class="page-hero">
    <svg class="page-hero-mark" aria-hidden="true"><use href="#nib"/></svg>
    <div class="wrap">
      <div class="page-hero-inner">
        <nav class="crumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a><span class="sep">/</span>
          <a href="index.html#capabilities">Capabilities</a>
          <span class="sep">/</span><span aria-current="page">{data["h1"]}</span>
        </nav>
        <div class="page-hero-top">
          <span class="page-hero-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="{data["icon"]}"/></svg></span>
          <span class="page-hero-serial">{data["serial"]}</span>
        </div>
        <h1>{data["h1"]}</h1>
        <p class="page-lead">{data["lead"]}</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="https://wa.me/919999026602" target="_blank" rel="noopener">
            <svg class="btn-ico" viewBox="0 0 24 24" aria-hidden="true"><use href="#wa"/></svg>
            <span>Talk to us about this</span>
          </a>
          <a class="btn btn-ghost" href="#flow"><span>How it works</span><svg class="btn-ico" viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg></a>
        </div>
      </div>
    </div>
  </section>

  <section class="svc-section" id="flow" aria-labelledby="flow-h">
    <div class="wrap">
      <header class="svc-head">
        <span class="eyebrow reveal">The workflow</span>
        <h2 class="reveal" id="flow-h">How it works</h2>
        <p class="reveal">Each step hands checked work to the next, so there's no manual re-key in the middle and no black box at the end.</p>
      </header>
      <div class="pipeline-wrap reveal">
<ol class="flow" aria-label="How it works, step by step">
{flow_items_html}</ol>
      </div>
    </div>
  </section>

  <section class="svc-section section-alt" aria-labelledby="feat-h">
    <div class="wrap">
      <header class="svc-head">
        <span class="eyebrow reveal">What's inside</span>
        <h2 class="reveal" id="feat-h">Built in from the start</h2>
      </header>
      <div class="reveal">
  <ul class="chips">
{chips_html}
  </ul>
      </div>
    </div>
  </section>

  <section class="svc-section" aria-labelledby="adv-h">
    <div class="wrap">
      <header class="svc-head">
        <span class="eyebrow reveal">Why it's worth it</span>
        <h2 class="reveal" id="adv-h">What you get out of it</h2>
      </header>
  <ul class="adv-grid">
{adv_html}  </ul>
    </div>
  </section>

  <section class="svc-section section-alt" aria-labelledby="spec-h">
    <div class="wrap">
      <header class="svc-head">
        <span class="eyebrow reveal">Enterprise-ready</span>
        <h2 class="reveal" id="spec-h">Fits into how you already run</h2>
      </header>
      <div class="reveal">
  <div class="spec-grid">
    <div class="spec reveal">
      <p class="spec-h"><span class="i8" style="--i:url(assets/i8/server.png)" aria-hidden="true"></span>Enterprise capabilities</p>
      <ul>
{spec_left_html}
      </ul>
    </div>
    <div class="spec reveal">
      <p class="spec-h"><span class="i8" style="--i:url(assets/i8/check-quality.png)" aria-hidden="true"></span>Quality assurance</p>
      <ul>
{spec_right_html}
      </ul>
    </div>
  </div>
      </div>
    </div>
  </section>

  <section class="svc-section" aria-labelledby="rel-h">
    <div class="wrap">
      <header class="svc-head">
        <span class="eyebrow reveal">Keep looking</span>
        <h2 class="reveal" id="rel-h">Related services</h2>
      </header>
  <div class="related-grid">
{related_html}  </div>
    </div>
  </section>

  <section class="brand-band" aria-labelledby="cta-h">
    <svg class="brand-band-nib" aria-hidden="true"><use href="#nib"/></svg>
    <div class="wrap brand-band-inner">
      <div class="brand-band-copy">
        <p class="eyebrow reveal">Get started</p>
        <h2 class="section-title reveal" id="cta-h">Tell us what you need done</h2>
        <p class="section-lead reveal">Message us on WhatsApp or send an email. Tell us the job and we'll reply with who's right for it and what happens next.</p>
        <div class="hero-actions reveal">
          <a class="btn btn-on-blue" href="https://wa.me/919999026602" target="_blank" rel="noopener"><svg class="btn-ico" viewBox="0 0 24 24" aria-hidden="true"><use href="#wa"/></svg><span>Message on WhatsApp</span></a>
          <a class="btn btn-ghost-blue" href="mailto:corp@pareeksa.com"><span>corp@<wbr>pareeksa.com</span></a>
        </div>
      </div>
    </div>
  </section>
</main>
<footer class="site-footer">
  <div class="wrap footer-inner">
    <div class="footer-brand">
      <a class="lockup lockup-stacked" href="index.html" aria-label="Pareeksa Technologies — home">
        <svg class="lockup-mark" aria-hidden="true"><use href="#nib"/></svg>
        <span class="lockup-word">Pareeksa</span>
      </a>
      <p class="footer-tag mono">The exam, examined.</p>
    </div>
    <nav class="footer-nav" aria-label="Footer">
      <h2 class="footer-h">Site</h2>
      <a href="index.html#examinations">Examinations</a>
      <a href="index.html#capabilities">Capabilities</a>
      <a href="index.html#contact">Contact</a>
      <a href="brand.html">Brand</a>
    </nav>
    <div class="footer-contact">
      <h2 class="footer-h">Reach us</h2>
      <a href="https://wa.me/919999026602" target="_blank" rel="noopener" class="mono">+91 99990 26602</a>
      <a href="mailto:corp@pareeksa.com" class="mono">corp@<wbr>pareeksa.com</a>
      <address class="footer-address">New Delhi – 110059, India</address>
    </div>
  </div>
  <div class="wrap footer-creds">
    <span class="footer-creds-label">Registered with</span>
    <span class="cred"><img src="assets/badges/gem.png" width="273" height="178" alt="Registered on GeM — Government e-Marketplace" loading="lazy"></span>
    <span class="cred"><img src="Importance-1-e1536998812445.png" width="394" height="394" alt="MSME registered — Micro, Small &amp; Medium Enterprises" loading="lazy"></span>
  </div>
  <div class="wrap footer-base">
    <p>© <span id="year">2026</span> Pareeksa Technologies</p>
    <p class="mono footer-gst">GST 07ECOPS6433P1ZL</p>
  </div>
</footer>
<button type="button" class="demo-float" aria-label="Request a demo">
  <span>Request a Demo</span>
</button>
<a class="wa-float" href="https://wa.me/919999026602" target="_blank" rel="noopener" aria-label="Message Pareeksa on WhatsApp" title="Message us on WhatsApp">
  <svg viewBox="0 0 24 24" aria-hidden="true"><use href="#wa"/></svg>
</a>

<!-- Demo Modal -->
<div id="demo-modal" class="modal" aria-hidden="true">
  <div class="modal__overlay" tabindex="-1"></div>
  <div class="modal__container" role="dialog" aria-modal="true" aria-labelledby="modal-title">
    <button type="button" class="modal__close" aria-label="Close modal">&times;</button>
    <div class="modal__content">
      <h2 id="modal-title" class="modal__title">Request a Demo</h2>
      <p class="modal__lead">Fill out the details below, and we will get back to you to schedule a live demo.</p>
      
      <form class="contact-form modal-form" action="https://api.web3forms.com/submit" method="POST" aria-label="Request a demo form">
        <input type="hidden" name="access_key" value="YOUR_WEB3FORMS_ACCESS_KEY">
        <div class="contact-form__row">
          <div class="contact-form__group">
            <label class="contact-form__label" for="modal-name">Name</label>
            <input class="contact-form__input" type="text" id="modal-name" name="name" placeholder="Your name" required>
          </div>
          <div class="contact-form__group">
            <label class="contact-form__label" for="modal-phone">Mobile Number</label>
            <input class="contact-form__input" type="tel" id="modal-phone" name="phone" placeholder="+91 " required>
          </div>
        </div>
        <div class="contact-form__row contact-form__row--single">
          <div class="contact-form__group">
            <label class="contact-form__label" for="modal-email">Email Address</label>
            <input class="contact-form__input" type="email" id="modal-email" name="email" placeholder="your.email@example.com" required>
          </div>
        </div>
        <div class="contact-form__row contact-form__row--single">
          <div class="contact-form__group">
            <label class="contact-form__label" for="modal-org">Institute / Organization Name</label>
            <input class="contact-form__input" type="text" id="modal-org" name="organization" placeholder="Your institute or organization">
          </div>
        </div>
        <div class="contact-form__row contact-form__row--single">
          <div class="contact-form__group">
            <label class="contact-form__label" for="modal-message">Message</label>
            <textarea class="contact-form__textarea" id="modal-message" name="message" rows="4" placeholder="How can we help?"></textarea>
          </div>
        </div>
        <div class="contact-form__row contact-form__row--single">
          <div class="contact-form__alert contact-form__alert--success" hidden></div>
          <div class="contact-form__alert contact-form__alert--error" hidden></div>
        </div>
        <div class="contact-form__row contact-form__row--single">
          <button type="submit" class="btn btn-primary contact-form__submit">
            <span>Request a Demo</span>
          </button>
        </div>
      </form>
    </div>
  </div>
</div>

</body>
</html>
'''

# Generate all missing service pages
for filename, data in missing_services.items():
    html_content = build_service_html(filename, data)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Generated service page: {filename}")

# Generate ai-examination-document-solutions.html (same as ai-examination.html)
if os.path.exists("ai-examination.html"):
    with open("ai-examination.html", "r", encoding="utf-8") as f:
        ai_exam_content = f.read()
    with open("ai-examination-document-solutions.html", "w", encoding="utf-8") as f:
        f.write(ai_exam_content)
    print("Created alias: ai-examination-document-solutions.html")

# Create redirect/alias files for raw space-containing filenames found in brand.html or legacy code
raw_aliases = {
    "AI-driven Examination & Document Solutions.html": "ai-examination.html",
    "High Performance Platforms & Applications.html": "high-performance-platforms.html",
    "Cloud & DevOps": "cloud-devops.html",
    "Cloud & DevOps.html": "cloud-devops.html",
    "Internet of Things.html": "internet-of-things.html",
    "Blockchain & Identity.html": "blockchain-identity.html",
    "Data Analytics.html": "data-analytics.html",
    "Drones & UAVs.html": "drones-uavs.html",
    "Robotics & Systems.html": "robotics-systems.html",
    "Solar & Energy.html": "solar-energy.html",
    "Tech Skilling.html": "tech-skilling.html"
}

for raw_name, target_file in raw_aliases.items():
    with open(target_file, "r", encoding="utf-8") as f:
        content = f.read()
    with open(raw_name, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created alias file: '{raw_name}' -> '{target_file}'")

# Standardized Nav Blocks
desktop_nav_mega = '''<div class="nav-dropdown-menu nav-mega-menu">
          <div class="nav-mega-column">
            <h4 class="nav-mega-title">Document Intelligence</h4>
            <a href="ocr.html">OCR</a>
            <a href="icr.html">ICR</a>
            <a href="document-scanning.html">Document Scanning</a>
            <a href="document-management.html">Document Management</a>
            <a href="printing.html">Printing</a>
            <a href="ai-examination.html">AI-driven Examination &amp; Document Solutions</a>
          </div>
          <div class="nav-mega-column">
            <h4 class="nav-mega-title">Digital Engineering</h4>
            <a href="custom-portals.html">Custom Portals</a>
            <a href="high-performance-platforms.html">High Performance Platforms &amp; Applications</a>
            <a href="cloud-devops.html">Cloud &amp; DevOps</a>
            <a href="app-security.html">App Security Testing</a>
            <a href="internet-of-things.html">Internet of Things (IoT)</a>
          </div>
          <div class="nav-mega-column">
            <h4 class="nav-mega-title">AI &amp; Intelligent Systems</h4>
            <a href="artificial-intelligence.html">Artificial Intelligence</a>
            <a href="ai-modules.html">AI Modules</a>
            <a href="agentic-ai.html">Agentic AI Voice Calls</a>
            <a href="translation.html">Translation</a>
            <a href="blockchain-identity.html">Blockchain &amp; Identity</a>
            <a href="data-analytics.html">Data Analytics</a>
          </div>
          <div class="nav-mega-column">
            <h4 class="nav-mega-title">Emerging Technologies</h4>
            <a href="drones-uavs.html">Drones &amp; UAVs</a>
            <a href="robotics-systems.html">Robotics &amp; Systems</a>
            <a href="solar-energy.html">Solar &amp; Energy</a>
            <a href="tech-skilling.html">Tech Skilling</a>
          </div>
        </div>'''

mobile_nav_mega = '''<div class="mobile-dropdown-menu mobile-mega-menu">
        <div class="mobile-mega-section">
          <h4 class="mobile-mega-title">Document Intelligence</h4>
          <a href="ocr.html">OCR</a>
          <a href="icr.html">ICR</a>
          <a href="document-scanning.html">Document Scanning</a>
          <a href="document-management.html">Document Management</a>
          <a href="printing.html">Printing</a>
          <a href="ai-examination.html">AI-driven Examination &amp; Document Solutions</a>
        </div>
        <div class="mobile-mega-section">
          <h4 class="mobile-mega-title">Digital Engineering</h4>
          <a href="custom-portals.html">Custom Portals</a>
          <a href="high-performance-platforms.html">High Performance Platforms &amp; Applications</a>
          <a href="cloud-devops.html">Cloud &amp; DevOps</a>
          <a href="app-security.html">App Security Testing</a>
          <a href="internet-of-things.html">Internet of Things (IoT)</a>
        </div>
        <div class="mobile-mega-section">
          <h4 class="mobile-mega-title">AI &amp; Intelligent Systems</h4>
          <a href="artificial-intelligence.html">Artificial Intelligence</a>
          <a href="ai-modules.html">AI Modules</a>
          <a href="agentic-ai.html">Agentic AI Voice Calls</a>
          <a href="translation.html">Translation</a>
          <a href="blockchain-identity.html">Blockchain &amp; Identity</a>
          <a href="data-analytics.html">Data Analytics</a>
        </div>
        <div class="mobile-mega-section">
          <h4 class="mobile-mega-title">Emerging Technologies</h4>
          <a href="drones-uavs.html">Drones &amp; UAVs</a>
          <a href="robotics-systems.html">Robotics &amp; Systems</a>
          <a href="solar-energy.html">Solar &amp; Energy</a>
          <a href="tech-skilling.html">Tech Skilling</a>
        </div>
      </div>'''

# Replace mega menus across ALL html files
all_html_files = glob.glob("*.html")
for path in all_html_files:
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    
    # Replace desktop mega menu
    c_new = re.sub(
        r'<div class="nav-dropdown-menu nav-mega-menu">[\s\S]*?</div>\s*</div>\s*</div>',
        desktop_nav_mega + '\n      </div>',
        c
    )
    
    # Replace mobile mega menu
    c_new = re.sub(
        r'<div class="mobile-dropdown-menu mobile-mega-menu">[\s\S]*?</div>\s*</div>',
        mobile_nav_mega + '\n    </div>',
        c_new
    )
    
    if c != c_new:
        with open(path, "w", encoding="utf-8") as f:
            f.write(c_new)
        print(f"Updated navigation in: {path}")

print("=== ALL MISSING SERVICE PAGES GENERATED AND NAV MENUS UPDATED ===")
