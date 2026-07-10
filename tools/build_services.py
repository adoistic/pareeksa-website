#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the 14 Pareeksa service detail pages from one data model.
Single source of truth: same head boilerplate, sprite, header/footer, SEO shape.
Copy is written in the site's humanised voice (not the PDF's generic corporate prose)."""
import os, re, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://pareeksa.com"
I8DIR = os.path.join(ROOT, "assets", "i8")
I8 = {f[:-4] for f in os.listdir(I8DIR) if f.endswith(".png")}

# ---- extract the SVG sprite from index.html so it stays in sync ------------
idx = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
SPRITE = re.search(r'(<svg width="0" height="0" class="sprite".*?</svg>)', idx, re.S).group(1)

# ---- feature keyword -> icons8 slug ---------------------------------------
FMAP = [
    ("high-speed", "speed"), ("fast", "speed"), ("real-time", "realtime"),
    ("real time", "realtime"), ("batch", "batch"), ("bulk", "layers"),
    ("cloud", "cloud"), ("report", "report"), ("analytic", "dashboard"),
    ("dashboard", "dashboard"), ("error", "error-detect"), ("bug", "error-detect"),
    ("multi-format", "formats"), ("multi format", "formats"), ("multi-language", "translate"),
    ("multi-lingual", "translate"), ("localis", "translate"), ("localiz", "translate"),
    ("translat", "translate"), ("secure", "lock"), ("security", "shield"),
    ("authentication", "key"), ("access", "key"), ("role-based", "key"),
    ("remote", "remote"), ("multi-evaluator", "users"), ("multi-user", "users"),
    ("multi-agent", "network"), ("candidate", "registration"), ("registration", "registration"),
    ("api", "api"), ("integration", "integration"), ("erp", "integration"),
    ("crm", "integration"), ("metadata", "tag"), ("indexing", "tag"),
    ("search", "search"), ("text recognition", "text"), ("searchable", "search"),
    ("ocr", "text"), ("handwrit", "handwriting"), ("pattern", "puzzle"),
    ("version", "version"), ("signature", "signature"), ("audit", "audit"),
    ("proctor", "eye"), ("monitor", "monitor"), ("randomiz", "shuffle"),
    ("randomis", "shuffle"), ("time management", "clock"), ("scheduling", "calendar"),
    ("schedul", "calendar"), ("certificate", "certificate"), ("hall ticket", "ticket"),
    ("print", "printer"), ("packaging", "package"), ("nlp", "chat"),
    ("predictive", "trending"), ("recommendation", "star"), ("generative", "sparkles"),
    ("virtual assist", "headset"), ("calling", "phone"), ("call", "phone"),
    ("ci/cd", "pipeline"), ("regression", "refresh"), ("performance", "gauge"),
    ("archiv", "archive"), ("responsive", "devices"), ("multi-device", "devices"),
    ("multi-platform", "devices"), ("camera", "camera"), ("book", "book"),
    ("automat", "refresh"), ("workflow", "network"), ("autonom", "robot"),
    ("decision", "target"), ("context", "target"), ("intelligent search", "search"),
    ("data valid", "check-quality"), ("validation", "check-quality"), ("quality", "check-quality"),
    ("verification", "check-quality"), ("evaluation", "check-quality"), ("compil", "layers"),
    ("mark", "signature"), ("script", "text"), ("scal", "trending"),
    ("repository", "server"), ("storage", "server"), ("store", "server"),
    ("centralised", "server"), ("centralized", "server"), ("high resolution", "camera"),
    ("offset", "printer"), ("digital printing", "printer"), ("custom", "brush"),
    ("design", "brush"), ("dashboard", "dashboard"), ("data manage", "database"),
    ("data handling", "database"), ("data process", "database"), ("data extraction", "download"),
    ("data entry", "form"), ("digital sign", "signature"), ("upload", "upload"),
    ("high-fidelity", "gauge"), ("high accuracy", "target"), ("machine learning", "robot"),
    ("ai ", "sparkles"), ("website", "devices"), ("technical", "puzzle"),
    ("document translation", "translate"), ("human review", "eye"), ("smart search", "search"),
    ("digital script", "text"), ("transparent", "eye"), ("high production", "layers"),
    ("customiz", "brush"), ("customis", "brush"), ("packag", "package"),
]
def icon_for(feature):
    f = feature.lower()
    for k, slug in FMAP:
        if k in f and slug in I8:
            return slug
    return "check-quality"

# ---- service data model ----------------------------------------------------
# num, slug, icon(sprite), title, tag(short), lead, meta, flow[], features[],
# advantages[{icon,title,body}], capabilities[], qa[], related[slugs]
SERVICES = [
{
 "num":"01","slug":"omr","icon":"ic-omr","title":"OMR software &amp; services",
 "nav":"OMR","tag":"Optical mark recognition for answer sheets and forms, with scanning run as a service.",
 "lead":"Optical mark recognition reads the bubbles on answer sheets, surveys and feedback forms and turns them into scored data. We supply the reading software and run the scans ourselves, from a few thousand sheets to a few hundred thousand. Every sheet comes back checked, with an audit trail you can point to if a result is ever questioned.",
 "meta":"OMR software and scanning as a service — read answer sheets, surveys and forms into checked, audited data. Pareeksa Technologies, New Delhi.",
 "flow":[
   ("signature","Marking","A candidate fills the bubbles on a printed OMR sheet."),
   ("scan","Scanning","Sheets run through high-speed scanners — in your building or ours."),
   ("download","Data extraction","The software reads every mark and pulls out the responses."),
   ("check-quality","Evaluation","Answers are scored against the key, with error checks on every sheet."),
   ("report","Reports","Results and statistics come out the far end, ready to publish."),
 ],
 "features":["High-Speed Processing","Batch Evaluation","AI &amp; Cloud Integration","Automated Report Generation","Error Detection","Multi-format Support","Real-Time Processing","Bulk Data Handling"],
 "advantages":[
   ("target","Accuracy first","The reader catches stray marks and misreads before they reach a result, so human error stays out of the score."),
   ("speed","Less manual work","Scanning replaces hand-checking, which is where the hours and the mistakes usually go."),
   ("money","Lower cost","No manual checking, no paper shuffling — the same job with far fewer people on it."),
   ("clock","Faster results","Sheets become scored data in one pass, so you can declare results in days, not weeks."),
   ("trending","Scales up","The same pipeline handles a classroom test or a few hundred thousand competitive-exam sheets."),
 ],
 "capabilities":["Detailed analytics and statistics","Secure cloud deployment","Role-based data repository","API integration with ERP, LMS and exam systems","OMR sheets, surveys, feedback and assessment forms"],
 "qa":["Error detection and validation","Secure data handling","High processing accuracy","Continuous monitoring and reporting","Reliable performance at volume"],
 "related":["osm","online-examination","pre-post-examination"],
},
{
 "num":"02","slug":"osm","icon":"ic-osm","title":"On-screen marking",
 "nav":"On-screen marking","tag":"Score scanned booklets on screen with blind, webcam-verified marking; one instance per institution.",
 "lead":"Markers score scanned answer booklets on screen instead of carrying paper around. The candidate's identity stays hidden while the work is marked, so a name or a roll number can't sway a grade, and a webcam check confirms the right marker is doing the marking. Each institution runs its own instance, in its own name.",
 "meta":"On-screen marking (OSM) — blind, webcam-verified marking of scanned answer booklets, one instance per institution. Pareeksa Technologies.",
 "flow":[
   ("scan","Scan &amp; upload","Answer booklets are scanned and loaded onto a secure server."),
   ("shuffle","Blind allocation","Scripts go out to markers with the candidate's identity stripped off."),
   ("signature","On-screen marking","Markers annotate and score with proper marking tools, on screen."),
   ("eye","Verified marking","A webcam check confirms the right person is marking, and only them."),
   ("layers","Auto-compiled results","The system totals the marks and builds the reports itself."),
 ],
 "features":["Digital Script Evaluation","Secure Access Control","Remote Evaluation","Automated Mark Compilation","Real-Time Monitoring","High Accuracy","Transparent Assessment","Multi-Evaluator Support"],
 "advantages":[
   ("clock","Faster turnaround","Scripts move to a marker the moment they're scanned, so results close sooner."),
   ("eye","Marking you can defend","Blind allocation and a webcam check mean a grade rests on the work, not the name behind it."),
   ("cloud","Less paper to move","No vans of scripts between centres — the booklets travel as scans."),
   ("shield","Tamper-resistant","Access is controlled and every action is logged, so scripts can't quietly change hands."),
   ("trending","Built for scale","One large exam or many small ones, the same setup absorbs it."),
 ],
 "capabilities":["Cloud-based evaluation","Role-based access control","Analytics and reporting","Audit trails on every script","ERP integration"],
 "qa":["Secure data handling","Controlled evaluation process","Error detection","Continuous monitoring","Reliable performance"],
 "related":["omr","online-examination","pre-post-examination"],
},
{
 "num":"03","slug":"online-examination","icon":"ic-online","title":"Online examination",
 "nav":"Online examination","tag":"On-screen tests end to end — question banks, timed papers, randomised sets, live invigilation.",
 "lead":"Run a test on screen from start to finish. Build the question bank, set the timer, randomise the paper so no two candidates see the same order, and watch the room live while it runs. When the exam closes the results are already there — nobody spends the next fortnight marking.",
 "meta":"Online examination — question banks, timed papers, randomised sets, AI proctoring and instant results, on any device. Pareeksa Technologies.",
 "flow":[
   ("registration","Registration","Candidates enrol and get their credentials."),
   ("key","Login &amp; auth","Identity is checked before anyone can start."),
   ("monitor","Examination","The timed paper runs on screen, invigilated live."),
   ("upload","Auto-submission","Answers save and submit on their own when time runs out."),
   ("check-quality","Evaluation","Objective questions score instantly against the key."),
   ("report","Results","Scores and reports are ready as the exam closes."),
 ],
 "features":["Remote Exam Access","Auto Evaluation","Secure Browser Support","Real-Time Monitoring","Question Randomization","Time Management","Scalable Architecture","Instant Results"],
 "advantages":[
   ("remote","Sit it anywhere","A candidate needs a browser and a connection, not a hall and a seat."),
   ("money","Cheaper to run","No printing, no venue, no army of invigilators for a mid-term."),
   ("clock","Results at the buzzer","Objective papers are scored the second the exam ends."),
   ("shield","Harder to cheat","A locked-down browser, live proctoring and a shuffled paper make malpractice a lot of work."),
   ("trending","Thousands at once","The architecture holds up whether a class or a cohort sits together."),
 ],
 "capabilities":["Cloud deployment","AI-based proctoring","Analytics dashboard","ERP integration","Multi-device support"],
 "qa":["Anti-cheating measures","Secure authentication","System monitoring","Reliable performance","Backup and recovery"],
 "related":["omr","osm","pre-post-examination"],
},
{
 "num":"04","slug":"pre-post-examination","icon":"ic-prepost","title":"Pre &amp; post examination services",
 "nav":"Pre &amp; post exam","tag":"Registration, hall tickets, seating, scanning, tabulation and result processing.",
 "lead":"The work that surrounds an exam but rarely gets budgeted for: registering candidates, printing hall tickets, sorting seating and attendance, scanning the scripts, tabulating and processing results, issuing certificates. We take the parts you'd rather not staff and hand back checked output at each stage.",
 "meta":"Pre and post examination services — registration, hall tickets, seating, scanning, tabulation, result processing and certificates. Pareeksa Technologies.",
 "flow":[
   ("registration","Registration","Candidates enrol and the exam is scheduled."),
   ("ticket","Hall tickets","Admit cards are generated and issued."),
   ("monitor","Conduct","The exam runs, on paper or on screen."),
   ("check-quality","Evaluation","Scripts are marked and assessed."),
   ("layers","Result processing","Marks are tabulated and results compiled."),
   ("certificate","Certificates","Certificates issue and records are kept."),
 ],
 "features":["Candidate Registration","Hall Ticket Generation","OMR Evaluation","Result Processing","Certificate Management","Analytics Dashboard","Data Management","Report Generation"],
 "advantages":[
   ("refresh","One hand-off, not ten","The whole lifecycle sits with one team, so nothing falls between vendors."),
   ("clock","Results sooner","Each stage feeds the next without a manual re-key in between."),
   ("users","Less to staff","You keep the decisions; we run the repetitive, high-volume parts."),
   ("eye","A visible trail","Every step is recorded, so a query about one candidate has an answer."),
   ("shield","Handled securely","Candidate data and scripts are controlled end to end."),
 ],
 "capabilities":["ERP integration","Analytics dashboard","Cloud deployment","Data security","Centralised repository"],
 "qa":["Error validation","Data security","Process monitoring","Audit trails","Reliable performance"],
 "related":["omr","osm","online-examination"],
},
{
 "num":"05","slug":"ocr","icon":"ic-ocr","title":"OCR services",
 "nav":"OCR","tag":"Scanned pages and PDFs into searchable, editable text, tuned to your documents.",
 "lead":"OCR turns scanned pages and PDFs into text you can search and edit — printed forms, registers, books, ledgers. Instead of running your paperwork through a generic engine and hoping, we tune the model to the documents you actually have, which is where the accuracy on a real archive comes from.",
 "meta":"OCR services — convert scanned documents, images and PDFs into searchable, editable text, with the model tuned to your documents. Pareeksa Technologies.",
 "flow":[
   ("scan","Scanned","Pages and files are captured as images."),
   ("text","Recognition","The engine reads the characters off each page."),
   ("form","Editable text","Images become text you can search, copy and edit."),
   ("server","Stored","The result is filed digitally, indexed for retrieval."),
 ],
 "features":["Text Recognition","Searchable PDFs","Batch Processing","Multi-language Support","High-Speed Processing","AI-Based Extraction","Metadata Indexing","Cloud Integration"],
 "advantages":[
   ("form","Less re-typing","Data comes off the page automatically instead of someone keying it back in."),
   ("search","Findable records","A searchable PDF turns a shelf of files into something you can query."),
   ("target","Tuned accuracy","Trained on your document types, it misreads far less than an off-the-shelf engine."),
   ("cloud","Goes paperless","Whole archives move to digital without a manual transcription project."),
   ("money","Lower running cost","Retrieval and data entry stop eating staff time."),
 ],
 "capabilities":["AI-based OCR engine","API integration","Multi-format support","Analytics dashboard","Cloud storage"],
 "qa":["Image enhancement","Error detection","Data validation","Secure processing","High accuracy"],
 "related":["icr","document-scanning","document-management"],
},
{
 "num":"06","slug":"icr","icon":"ic-icr","title":"ICR services",
 "nav":"ICR","tag":"Hand-printed form fields read with a confidence score per field.",
 "lead":"ICR is OCR for handwriting. It reads hand-printed characters out of filled forms and application boxes and returns each field with a confidence score, so a person only checks the fields the machine wasn't sure about — not the whole stack.",
 "meta":"ICR services — read hand-printed form fields into digital data with a confidence score per field, so review focuses only on what's doubtful. Pareeksa Technologies.",
 "flow":[
   ("form","Handwritten form","A filled, hand-printed document comes in."),
   ("scan","Scanning","The form is captured as an image."),
   ("puzzle","Pattern analysis","The model studies the strokes in each box."),
   ("handwriting","Recognition","Characters are read into digital fields."),
   ("check-quality","Verified output","Each field returns with a confidence score for review."),
 ],
 "features":["Handwriting Recognition","AI-Based Learning","Automated Data Entry","Pattern Analysis","Multi-format Support","Batch Processing","Data Validation","High-Speed Processing"],
 "advantages":[
   ("form","Forms enter themselves","Hand-filled applications become structured data without manual typing."),
   ("target","Review only the doubt","A confidence score per field points a checker straight at the uncertain ones."),
   ("refresh","It learns your forms","The model improves on the specific hands and layouts it keeps seeing."),
   ("speed","Faster processing","A batch of forms clears in a fraction of the manual time."),
   ("money","Fewer data-entry hours","The keyboard work shrinks to spot-checks."),
 ],
 "capabilities":["AI and machine-learning integration","OCR compatibility","API integration","Analytics dashboard","Secure data processing"],
 "qa":["Intelligent validation","Image enhancement","Error detection","Data verification","Reliable recognition"],
 "related":["ocr","document-scanning","pre-post-examination"],
},
{
 "num":"07","slug":"document-scanning","icon":"ic-scan","title":"Document scanning services",
 "nav":"Document scanning","tag":"High-volume scanning of files, registers and archives, indexed to your system.",
 "lead":"High-volume scanning of files, registers and archives. We come to you or you ship to us; either way you get organised digital copies, named and indexed the way you already work, not dumped into a folder of numbered images nobody can navigate.",
 "meta":"Document scanning services — high-volume digitisation of files, registers and archives, indexed and searchable, delivered the way you file. Pareeksa Technologies.",
 "flow":[
   ("folder","Collection","Files, registers and archives are gathered."),
   ("scan","Scanning","Everything runs through high-speed scanners."),
   ("brush","Image processing","Pages are cleaned, straightened and made legible."),
   ("tag","Indexing","Each document is named and tagged to your scheme."),
   ("server","Digital storage","The set is stored, searchable and backed up."),
 ],
 "features":["High-Speed Scanning","OCR Integration","Metadata Indexing","Bulk Processing","Secure Storage","Multi-format Output","Digital Archiving","Searchable Documents"],
 "advantages":[
   ("search","Retrieval in seconds","Indexed scans mean you find a record by searching, not by walking to a shelf."),
   ("money","Reclaim the storage","Rooms of paper become a searchable archive that takes no floor space."),
   ("shield","Safer than paper","Digital copies survive fire, damp and a misfiled folder."),
   ("speed","Cleared at volume","Bulk scanning gets through a backlog that manual filing never would."),
   ("integration","Filed your way","Naming and indexing follow your logic, so it drops into how you already work."),
 ],
 "capabilities":["OCR support","Cloud storage","API integration","Analytics dashboard","Multi-format support"],
 "qa":["Image enhancement","Quality validation","Secure processing","Backup support","Continuous monitoring"],
 "related":["ocr","icr","document-management"],
},
{
 "num":"08","slug":"document-management","icon":"ic-dms","title":"Document management system",
 "nav":"Document management","tag":"Version history, role-based access, full-text search and retention.",
 "lead":"A place to store, find and control documents — with version history, access by role, full-text search and retention dates. Built around your filing logic rather than a stock template, so people can actually find what they need and you can prove who touched it and when.",
 "meta":"Document management system (DMS) — store, find and control documents with version history, role-based access, full-text search, audit trails and retention. Pareeksa Technologies.",
 "flow":[
   ("upload","Capture","Documents arrive by scan, upload or system feed."),
   ("tag","Index","Metadata and full text make every file findable."),
   ("server","Store","Files sit in a secure, versioned repository."),
   ("search","Retrieve","Anyone with the right role finds them in seconds."),
   ("link","Share","Controlled access, audit trails and retention on every share."),
 ],
 "features":["Centralised Repository","Smart Search","Metadata Indexing","Version Control","OCR Support","Role-Based Access","Digital Signatures","Audit Trails"],
 "advantages":[
   ("search","Nothing goes missing","Full-text search and indexing mean the file is where the search says, every time."),
   ("audit","Provable history","Versioning and audit trails show who changed what, which matters when someone asks."),
   ("key","Right eyes only","Role-based access keeps sensitive documents in front of the people cleared for them."),
   ("money","Less paper overhead","Storage, copying and re-filing costs drop as the paper does."),
   ("shield","Compliance-ready","Retention rules and trails give an auditor a straight answer."),
 ],
 "capabilities":["High-fidelity OCR","Analytics dashboard","ERP integration","Multi-format support","Cloud deployment"],
 "qa":["Image enhancement","Secure storage","Data validation","Backup and recovery","Reliability monitoring"],
 "related":["document-scanning","ocr","custom-portals"],
},
{
 "num":"09","slug":"printing","icon":"ic-print","title":"Printing services",
 "nav":"Printing","tag":"Secure exam and record printing — question papers, OMR sheets, certificates, mark sheets.",
 "lead":"Print work tied to exams and records: question papers under controlled handling, OMR sheets, certificates, mark sheets, variable-data runs where every copy differs. Digital or offset depending on the run, secure where it has to be, delivered packaged and accounted for.",
 "meta":"Printing services — secure question papers, OMR sheets, certificates and variable-data records, digital or offset, packaged and delivered. Pareeksa Technologies.",
 "flow":[
   ("brush","Design prep","Artwork and data files are prepared for print."),
   ("form","Formatting","Content is laid out and proofed to spec."),
   ("printer","Printing","Runs go out on digital or offset presses."),
   ("check-quality","Quality checks","Colour and accuracy are verified before packing."),
   ("package","Pack &amp; deliver","Materials are packaged securely and sent."),
 ],
 "features":["Digital Printing","Offset Printing","Bulk Printing","Customized Printing","High Resolution Output","Fast Production","Packaging Support","Quality Inspection"],
 "advantages":[
   ("money","Priced for the run","Digital for short and variable jobs, offset for volume — you pay for the right one."),
   ("layers","Real capacity","Bulk runs go out on time because the press capacity is actually there."),
   ("shield","Secure handling","Question papers and certificates are printed and moved under control."),
   ("brush","Made to spec","Variable data, certificates, mark sheets — each job set up for what it is."),
   ("gauge","Print that holds up","Colour accuracy and inspection keep the output consistent across a run."),
 ],
 "capabilities":["Automated printing","Bulk processing","Print management","Quality monitoring","Packaging support"],
 "qa":["Colour accuracy","Print validation","Quality inspection","Error detection","Reliable output"],
 "related":["pre-post-examination","omr","document-scanning"],
},
{
 "num":"10","slug":"custom-portals","icon":"ic-portals","title":"Custom portal development",
 "nav":"Custom portals","tag":"Web and mobile apps built to fit your process, then maintained.",
 "lead":"Web and mobile apps built to fit your process, not bent around a framework you'll be fighting in a year. Admin portals, candidate apps, dashboards — designed for how your work actually runs. We build it, then we stay on to maintain it.",
 "meta":"Custom portal development — web and mobile apps built to fit your process and maintained after launch, with role-based access and integrations. Pareeksa Technologies.",
 "flow":[
   ("form","Requirements","We map how your process actually works."),
   ("brush","Design &amp; build","The portal is designed and developed to fit it."),
   ("integration","Integrate","Database, features and your other systems are wired in."),
   ("devices","Go live","Users reach it through a secure web or mobile interface."),
 ],
 "features":["Custom Dashboard","Role-Based Access","Responsive Design","API Integration","Secure Authentication","Cloud Deployment","Multi-User Support","Analytics &amp; Reporting"],
 "advantages":[
   ("target","Fits your process","Built around how you work, so people don't fight the tool to do their job."),
   ("refresh","Smoother day-to-day","The clicks match the workflow, which is where the time savings actually live."),
   ("devices","Works on any screen","Responsive from a desk monitor to a phone in the field."),
   ("trending","Grows with you","The architecture takes more users and more features without a rebuild."),
   ("shield","Secure by default","Role-based access and proper authentication from the first release."),
 ],
 "capabilities":["ERP integration","CRM integration","Analytics dashboard","Cloud hosting","Multi-platform support"],
 "qa":["Performance testing","Security validation","Backup and recovery","Ongoing maintenance","Reliable uptime"],
 "related":["ai-modules","agentic-ai","app-security"],
},
{
 "num":"11","slug":"ai-modules","icon":"ic-ai","title":"AI modules",
 "nav":"AI modules","tag":"Task-scoped AI — archive search, research assistants, automation scripting.",
 "lead":"Specific AI dropped into a real task, not a demo looking for a use. Search across a messy archive, a research assistant that reads what you can't get to, scripting that clears repetitive work. Scoped to the job, measured on whether it does it.",
 "meta":"AI modules — task-scoped AI for archive search, research assistants and automation, built into your workflow and measured on the job. Pareeksa Technologies.",
 "flow":[
   ("target","Scope","We pin down the one task worth automating."),
   ("database","Data","The relevant data is gathered and prepared."),
   ("robot","Model","The model runs — search, extraction or a prediction."),
   ("network","In your workflow","The output lands where the work already happens."),
 ],
 "features":["Machine Learning","NLP Processing","Predictive Analytics","Automation","Recommendation Engine","Generative AI","Intelligent Search","Real-Time Insights"],
 "advantages":[
   ("refresh","Repetition gone","The dull, repeating work gets handed to a script that doesn't tire."),
   ("target","Scoped, not vague","Each module answers one real question, so you can tell if it's working."),
   ("trending","Faster calls","Analysis that took a day of digging comes back in minutes."),
   ("search","Finds the needle","Intelligent search reaches into archives that plain keyword search can't."),
   ("money","Pays for the task","Priced against the work it removes, not a platform subscription."),
 ],
 "capabilities":["Cloud AI deployment","API integration","Analytics dashboard","Workflow automation","Data processing engine"],
 "qa":["Data validation","Model monitoring","Continuous learning","Error detection","Secure processing"],
 "related":["agentic-ai","custom-portals","app-security"],
},
{
 "num":"12","slug":"agentic-ai","icon":"ic-voice","title":"Agentic AI &amp; voice calling",
 "nav":"Agentic AI","tag":"An AI that takes phone calls and handles the conversation like a person.",
 "lead":"An AI that takes phone calls and holds a real conversation — it follows your flow, answers questions, and books or routes the outcome. It works around the clock, and it sounds human enough that most callers won't clock it. Under the hood it can plan a task, reach into your tools and databases, and finish the job, not just chat.",
 "meta":"Agentic AI and voice calling — an AI that answers phone calls, holds a real conversation, and completes tasks across your tools, around the clock. Pareeksa Technologies.",
 "flow":[
   ("phone","Instruction","A caller speaks, or a task is handed to the agent."),
   ("target","Understand","It works out what the goal actually is."),
   ("network","Plan &amp; act","It plans the steps and carries them out."),
   ("integration","Use your tools","It reaches into your systems and databases to do the work."),
   ("check-quality","Deliver","It books, routes or answers — and closes the loop."),
 ],
 "features":["Autonomous Decision Making","Workflow Automation","AI Calling Agents","Multi-Agent Systems","Task Scheduling","Intelligent Search","Virtual Assistance","Context Awareness"],
 "advantages":[
   ("clock","Answers at 3am","It picks up around the clock, so no call waits for office hours."),
   ("refresh","Handles the routine","Repetitive calls and tasks run themselves, freeing people for the hard ones."),
   ("trending","Scales on demand","A spike in calls is more agents, not a hiring round."),
   ("headset","Sounds human","The conversation is natural enough that callers just get their answer."),
   ("money","Cheaper coverage","Round-the-clock handling without a night shift on payroll."),
 ],
 "capabilities":["API integration","Multi-agent architecture","Cloud deployment","Analytics dashboard","Real-time processing"],
 "qa":["Monitoring and logging","Error detection","Secure processing","Response validation","Continuous learning"],
 "related":["ai-modules","custom-portals","app-security"],
},
{
 "num":"13","slug":"app-security","icon":"ic-security","title":"App security testing",
 "nav":"App security","tag":"Attacker's-eye testing of web, mobile and APIs, with reproducible findings.",
 "lead":"We test your app the way an attacker would and tell you what breaks — with the steps to reproduce it and a priority for the fix. Web, mobile, and the APIs behind them. It runs under our Pod Armour testing platform, which folds the checks into your build so problems surface before a release, not after.",
 "meta":"App security testing — attacker's-eye testing of web, mobile and APIs with reproducible findings and fix priorities, via the Pod Armour platform. Pareeksa Technologies.",
 "flow":[
   ("integration","Code integration","Tests hook into your build pipeline."),
   ("refresh","Test execution","Automated and manual checks run against the app."),
   ("error-detect","Bug detection","Weak points surface with steps to reproduce."),
   ("gauge","Performance analysis","Behaviour under load and stress is measured."),
   ("report","Reporting","You get findings ranked by priority, not a raw dump."),
 ],
 "features":["Automated Testing","API Testing","Performance Monitoring","Bug Tracking","CI/CD Integration","Regression Testing","Real-Time Reports","Quality Metrics"],
 "advantages":[
   ("error-detect","Caught early","Finding a hole in the build is cheap; finding it in production is not."),
   ("shield","Actually reliable","Regression and load testing keep a fix from breaking the next release."),
   ("clock","Ship with less fear","Automated checks on every build mean you release faster, not slower."),
   ("refresh","Less manual QA","The repetitive test passes run themselves on each commit."),
   ("trending","Scales with the app","The suite grows as the codebase does, without a testing team ballooning."),
 ],
 "capabilities":["CI/CD support","Analytics dashboard","Performance monitoring","API integration","Cloud-based testing"],
 "qa":["Test validation","Continuous monitoring","Performance analysis","Error tracking","Reliable reporting"],
 "related":["custom-portals","ai-modules","agentic-ai"],
},
{
 "num":"14","slug":"translation","icon":"ic-translation","title":"Translation services",
 "nav":"Translation","tag":"Human translation of documents and content, with the meaning kept intact.",
 "lead":"Documents and content moved between languages by people who read both, with AI to speed the first pass and a human to keep the meaning. For when records, certificates or material have to cross a language line and still say exactly what they said before.",
 "meta":"Translation services — human translation of documents, websites and content across languages, AI-assisted and quality-checked, meaning kept intact. Pareeksa Technologies.",
 "flow":[
   ("form","Source in","Your content and its context arrive."),
   ("translate","Translate","Human translators and AI tools do the pass together."),
   ("check-quality","Quality check","A reviewer verifies meaning, context and accuracy."),
   ("download","Delivered","The finished translation comes back, formatted and ready."),
 ],
 "features":["Multi-Language Support","AI-Assisted Translation","Human Review","Localization","Technical Translation","Document Translation","Website Translation","Quality Verification"],
 "advantages":[
   ("translate","Reaches more people","Content in the reader's language lands the way the original did."),
   ("target","Meaning survives","A human reviewer catches the context a machine translation flattens."),
   ("headset","Fits the region","Localisation adapts tone and detail to where it's being read, not just the words."),
   ("clock","Quicker turnaround","AI handles the bulk first pass so the human time goes where it counts."),
   ("book","Handles the technical","Specialist and document translation, not just everyday text."),
 ],
 "capabilities":["AI translation engine","Multilingual database","Website localisation","API integration","Content management support"],
 "qa":["Human validation","Quality checks","Context verification","Accuracy monitoring","Continuous improvement"],
 "related":["ai-modules","document-management","custom-portals"],
},
]
SVC = {s["slug"]: s for s in SERVICES}

# ---- shared partials -------------------------------------------------------
def head(s):
    url = f"{BASE}/{s['slug']}.html"
    title = f"{re.sub('&amp;','&',s['title'])} — Pareeksa Technologies"
    # Service + Breadcrumb structured data
    ld = {
      "@context":"https://schema.org","@graph":[
        {"@type":"Service","@id":f"{url}#service","serviceType":re.sub('&amp;','&',s['title']),
         "name":re.sub('&amp;','&',s['title']),"description":re.sub('&amp;','&',s['meta']),
         "url":url,"provider":{"@id":f"{BASE}/#org"},"areaServed":"IN"},
        {"@type":"BreadcrumbList","itemListElement":[
          {"@type":"ListItem","position":1,"name":"Home","item":f"{BASE}/"},
          {"@type":"ListItem","position":2,"name":re.sub('&amp;','&',s['title']),"item":url}]}
      ]}
    return f'''<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{s['meta']}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="author" content="Pareeksa Technologies">
<meta name="theme-color" content="#F7F8FA" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0E0F13" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Pareeksa Technologies">
<meta property="og:title" content="{re.sub('&amp;','&',s['title'])} — Pareeksa Technologies">
<meta property="og:description" content="{s['meta']}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="en_IN">
<meta property="og:image" content="{BASE}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{re.sub('&amp;','&',s['title'])} — Pareeksa Technologies">
<meta name="twitter:description" content="{s['meta']}">
<meta name="twitter:image" content="{BASE}/assets/og-image.png">
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
{json.dumps(ld, ensure_ascii=False, indent=1)}
</script>
<script src="script.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{SPRITE}
'''

def header():
    return '''<header class="site-header" id="top">
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
          </div>
          <div class="nav-mega-column">
            <h4 class="nav-mega-title">Build &amp; AI</h4>
            <a href="custom-portals.html">Custom Portals</a>
            <a href="ai-modules.html">AI Modules</a>
            <a href="agentic-ai.html">Agentic AI Voice Calls</a>
            <a href="app-security.html">App Security Testing</a>
            <a href="translation.html">Translation</a>
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
        </div>
        <div class="mobile-mega-section">
          <h4 class="mobile-mega-title">Build &amp; AI</h4>
          <a href="custom-portals.html">Custom Portals</a>
          <a href="ai-modules.html">AI Modules</a>
          <a href="agentic-ai.html">Agentic AI Voice Calls</a>
          <a href="app-security.html">App Security Testing</a>
          <a href="translation.html">Translation</a>
        </div>
      </div>
    </div>
    <a href="index.html#contact">Contact</a>
    <a class="mobile-cta" href="https://wa.me/919999026602" target="_blank" rel="noopener">Message on WhatsApp</a>
  </nav>
</header>
'''

def footer():
    return '''<footer class="site-footer">
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
    <span class="cred"><img src="assets/badges/msme.svg" width="394" height="394" alt="MSME registered — Micro, Small &amp; Medium Enterprises" loading="lazy"></span>
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
</html>'''

def i8span(slug):
    return f'<span class="i8" style="--i:url(assets/i8/{slug}.png)" aria-hidden="true"></span>'

def flow_html(steps):
    out = ['<ol class="flow" aria-label="How it works, step by step">']
    n = len(steps)
    for i,(ic,title,note) in enumerate(steps):
        out.append(f'''  <li class="flow-step" style="--n:{i}">
    <span class="flow-num-dot">{i+1:02d}</span>
    <div class="flow-node">
      <div class="flow-top"><span class="flow-ico">{i8span(ic)}</span><span class="flow-num"></span></div>
      <h3>{title}</h3><p>{note}</p>
    </div>
  </li>''')
    out.append('</ol>')
    return "\n".join(out)

def chips_html(features):
    lis = "\n".join(f'    <li class="chip">{i8span(icon_for(f))}<span>{f}</span></li>' for f in features)
    return f'  <ul class="chips">\n{lis}\n  </ul>'

def adv_html(advs):
    out = ['  <ul class="adv-grid">']
    for ic,t,b in advs:
        out.append(f'''    <li class="adv reveal">
      <span class="adv-ico">{i8span(ic)}</span>
      <h3>{t}</h3><p>{b}</p>
    </li>''')
    out.append('  </ul>')
    return "\n".join(out)

def spec_html(caps, qa):
    def col(icon, label, items):
        lis = "\n".join(f'      <li>{it}</li>' for it in items)
        return f'''    <div class="spec reveal">
      <p class="spec-h">{i8span(icon)}{label}</p>
      <ul>
{lis}
      </ul>
    </div>'''
    return f'  <div class="spec-grid">\n{col("server","Enterprise capabilities",caps)}\n{col("check-quality","Quality assurance",qa)}\n  </div>'

def related_html(s):
    out = ['  <div class="related-grid">']
    for slug in s["related"]:
        r = SVC[slug]
        out.append(f'''    <a class="related-card reveal" href="{slug}.html">
      <span class="related-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#{r['icon']}"/></svg></span>
      <h3>{r['title']}</h3>
      <p>{r['tag']}</p>
      <span class="go">View service <svg viewBox="0 0 24 24" aria-hidden="true"><use href="#arrow"/></svg></span>
    </a>''')
    out.append('  </div>')
    return "\n".join(out)

def page(s):
    return f'''{head(s)}{header()}
<main id="main">

  <section class="page-hero">
    <svg class="page-hero-mark" aria-hidden="true"><use href="#nib"/></svg>
    <div class="wrap">
      <div class="page-hero-inner">
        <nav class="crumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a><span class="sep">/</span>
          <a href="index.html#{'examinations' if int(s['num'])<=4 else 'capabilities'}">{'Examinations' if int(s['num'])<=4 else 'Capabilities'}</a>
          <span class="sep">/</span><span aria-current="page">{re.sub('&amp;','&',s['title'])}</span>
        </nav>
        <div class="page-hero-top">
          <span class="page-hero-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#{s['icon']}"/></svg></span>
          <span class="page-hero-serial">Service {s['num']} / 14</span>
        </div>
        <h1>{s['title']}</h1>
        <p class="page-lead">{s['lead']}</p>
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
{flow_html(s['flow'])}
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
{chips_html(s['features'])}
      </div>
    </div>
  </section>

  <section class="svc-section" aria-labelledby="adv-h">
    <div class="wrap">
      <header class="svc-head">
        <span class="eyebrow reveal">Why it's worth it</span>
        <h2 class="reveal" id="adv-h">What you get out of it</h2>
      </header>
{adv_html(s['advantages'])}
    </div>
  </section>

  <section class="svc-section section-alt" aria-labelledby="spec-h">
    <div class="wrap">
      <header class="svc-head">
        <span class="eyebrow reveal">Enterprise-ready</span>
        <h2 class="reveal" id="spec-h">Fits into how you already run</h2>
      </header>
      <div class="reveal">
{spec_html(s['capabilities'], s['qa'])}
      </div>
    </div>
  </section>

  <section class="svc-section" aria-labelledby="rel-h">
    <div class="wrap">
      <header class="svc-head">
        <span class="eyebrow reveal">Keep looking</span>
        <h2 class="reveal" id="rel-h">Related services</h2>
      </header>
{related_html(s)}
    </div>
  </section>

  <section class="brand-band" aria-labelledby="cta-h">
    <svg class="brand-band-nib" aria-hidden="true"><use href="#nib"/></svg>
    <div class="wrap brand-band-inner">
      <div class="brand-band-copy">
        <p class="eyebrow reveal">Get started</p>
        <h2 class="section-title reveal" id="cta-h">Tell us what you need {'marked' if int(s['num'])<=4 else 'done'}</h2>
        <p class="section-lead reveal">Message us on WhatsApp or send an email. Tell us the job and we'll reply with who's right for it and what happens next.</p>
        <div class="hero-actions reveal">
          <a class="btn btn-on-blue" href="https://wa.me/919999026602" target="_blank" rel="noopener"><svg class="btn-ico" viewBox="0 0 24 24" aria-hidden="true"><use href="#wa"/></svg><span>Message on WhatsApp</span></a>
          <a class="btn btn-ghost-blue" href="mailto:corp@pareeksa.com"><span>corp@<wbr>pareeksa.com</span></a>
        </div>
      </div>
    </div>
  </section>
</main>
{footer()}
'''

# ---- emit ------------------------------------------------------------------
for s in SERVICES:
    with open(os.path.join(ROOT, f"{s['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(page(s))
    print("wrote", s["slug"]+".html")
print(f"\n{len(SERVICES)} pages generated.")
