from __future__ import annotations
from pathlib import Path
from datetime import datetime, timezone
import hashlib, html, json, os, textwrap

ROOT = Path(__file__).resolve().parents[1]
BASE = "/digital-governance-observatory"
SITE = "Digital Governance & Gulf Technology Observatory"
AUTHOR = "Nabil Ayshan"
VERSION = "v1.0.0"
PUBLISHED_AT = os.environ.get("PUBLISHED_AT", "2026-07-01T00:00:30Z")
DISCLAIMER_EN = (
    "This is an independent research and educational initiative. It is not affiliated with any government, "
    "regulator, bank, technology company, or standards body. The material is provided for general informational "
    "purposes and does not constitute legal, financial, compliance, or security advice."
)
DISCLAIMER_AR = (
    "هذه مبادرة بحثية وتعليمية مستقلة. وهي غير تابعة لأي حكومة أو جهة تنظيمية أو بنك أو شركة تقنية أو هيئة معايير. "
    "تُقدَّم المواد لأغراض معلوماتية عامة ولا تشكل نصيحة قانونية أو مالية أو امتثالية أو أمنية."
)

SOURCES = [
    ("NIST AI Risk Management Framework", "https://www.nist.gov/itl/ai-risk-management-framework"),
    ("NIST SP 800-63 Digital Identity Guidelines", "https://pages.nist.gov/800-63-4/"),
    ("IETF RFC 6749: OAuth 2.0", "https://www.rfc-editor.org/rfc/rfc6749"),
    ("IETF RFC 9700: OAuth 2.0 Security Best Current Practice", "https://www.rfc-editor.org/rfc/rfc9700"),
    ("OpenID Connect Core 1.0", "https://openid.net/specs/openid-connect-core-1_0.html"),
    ("W3C Web Authentication: WebAuthn Level 3", "https://www.w3.org/TR/webauthn-3/"),
    ("FATF Recommendations", "https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html"),
    ("UAE Central Bank AML/CFT", "https://www.centralbank.ae/en/our-operations/anti-money-laundering-and-combating-the-financing-of-terrorism/"),
    ("Saudi Data & AI Authority", "https://sdaia.gov.sa/"),
    ("Saudi Central Bank", "https://www.sama.gov.sa/"),
    ("Qatar National Cyber Security Agency", "https://ncsa.gov.qa/"),
    ("Central Bank of Bahrain Open Banking", "https://www.cbb.gov.bh/open-banking/"),
]

PROJECTS = {
    "agentconsent": {
        "name": "AgentConsent",
        "en": "A research project on human consent, revocable delegation, bounded authority for AI agents, consent records, audit trails, and agentic payments.",
        "ar": "مشروع بحثي حول موافقة الإنسان والتفويض القابل للإلغاء وحدود صلاحيات وكلاء الذكاء الاصطناعي وسجلات الموافقة ومسارات التدقيق والمدفوعات الوكيلية.",
    },
    "machineconsent": {
        "name": "MachineConsent",
        "en": "A research project on human oversight for autonomous machines, operational approvals, emergency stop policies, and limits on machine autonomy.",
        "ar": "مشروع بحثي حول الرقابة البشرية على الآلات الذاتية والموافقات التشغيلية وسياسات الإيقاف الطارئ وحدود استقلال الآلات.",
    },
    "gulfcompute": {
        "name": "GulfCompute",
        "en": "A research project on Gulf data centers, GPUs, high-performance computing, sovereign cloud, energy, water, and cooling requirements.",
        "ar": "مشروع بحثي حول مراكز البيانات الخليجية ووحدات GPU والحوسبة عالية الأداء والسحابة السيادية ومتطلبات الطاقة والمياه والتبريد.",
    },
    "gulfauth": {
        "name": "GulfAuth",
        "en": "A research project on authentication, passkeys, MFA, OAuth, OpenID Connect, authorization, federation, and digital identity in Gulf services.",
        "ar": "مشروع بحثي حول المصادقة ومفاتيح المرور والمصادقة متعددة العوامل وOAuth وOpenID Connect وإدارة الصلاحيات والهوية الاتحادية في الخدمات الخليجية.",
    },
    "gulfkyc": {
        "name": "GulfKYC",
        "en": "A research project on KYC, KYB, AML, identity verification, privacy, digital onboarding, and compliance education in Gulf markets.",
        "ar": "مشروع بحثي حول اعرف عميلك واعرف عملك ومكافحة غسل الأموال والتحقق من الهوية والخصوصية وفتح الحسابات الرقمية والتثقيف الامتثالي في الأسواق الخليجية.",
    },
}

ARTICLE_TOPICS = [
    ("agentconsent", "human-consent-records", "Human Consent Records for Autonomous AI Agents", "سجلات موافقة الإنسان لوكلاء الذكاء الاصطناعي الذاتيين"),
    ("agentconsent", "revocable-authorization", "Revocable Authorization in Agentic Systems", "التفويض القابل للإلغاء في الأنظمة الوكيلية"),
    ("machineconsent", "human-oversight-autonomous-machines", "Human Oversight for Autonomous Machines", "الرقابة البشرية على الآلات الذاتية"),
    ("machineconsent", "safe-revocation-emergency-stop", "Designing Safe Revocation and Emergency Stop Policies", "تصميم سياسات إلغاء وإيقاف طارئ آمنة"),
    ("gulfcompute", "mapping-gulf-ai-compute", "Mapping the Gulf AI Compute Landscape", "رسم مشهد حوسبة الذكاء الاصطناعي في الخليج"),
    ("gulfcompute", "energy-cooling-sovereign-compute", "Energy, Cooling, and Sovereign Compute Infrastructure", "الطاقة والتبريد والبنية الحاسوبية السيادية"),
    ("gulfauth", "passkeys-passwordless-gulf", "Passkeys and Passwordless Authentication in Gulf Markets", "مفاتيح المرور والمصادقة دون كلمات مرور في الأسواق الخليجية"),
    ("gulfauth", "identity-federation-regional-services", "Identity Federation for Regional Digital Services", "الهوية الاتحادية للخدمات الرقمية الإقليمية"),
    ("gulfkyc", "kyc-kyb-aml-overview", "KYC, KYB, and AML: A Practical Gulf-Oriented Overview", "اعرف عميلك واعرف عملك ومكافحة غسل الأموال: عرض عملي موجه للخليج"),
    ("gulfkyc", "privacy-preserving-onboarding", "Privacy-Preserving Digital Onboarding", "فتح الحسابات الرقمية مع الحفاظ على الخصوصية"),
]

CSS = """
:root{color-scheme:light dark;--bg:#f7f7f2;--fg:#17202a;--muted:#53616f;--card:#ffffff;--accent:#176b87;--accent2:#b66d2c;--border:#d9dfdf;--shadow:0 12px 36px rgba(23,32,42,.08)}
body.dark{--bg:#101418;--fg:#edf2f4;--muted:#b4c0c8;--card:#182028;--accent:#62c2e4;--accent2:#f0a35e;--border:#33414d;--shadow:0 12px 36px rgba(0,0,0,.28)}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font:18px/1.7 system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;background:var(--bg);color:var(--fg)}[dir=rtl] body{font-family:system-ui,Tahoma,Arial,sans-serif}.wrap{max-width:1120px;margin:auto;padding:1rem}header{border-bottom:1px solid var(--border);background:color-mix(in srgb,var(--card) 94%,transparent);position:sticky;top:0;z-index:5;backdrop-filter:blur(10px)}nav{display:flex;gap:.65rem;flex-wrap:wrap;align-items:center}.brand{font-weight:900;color:var(--accent);margin-inline-end:auto;letter-spacing:.01em}nav a,.button{color:var(--fg);text-decoration:none;border:1px solid var(--border);padding:.48rem .75rem;border-radius:999px;background:transparent;cursor:pointer}nav a:hover,.button:hover,nav a:focus,.button:focus{border-color:var(--accent);outline:2px solid transparent}main{padding:2rem 1rem}.hero{padding:3.5rem 0}.eyebrow{color:var(--accent2);font-weight:800;text-transform:uppercase;letter-spacing:.08em;font-size:.85rem}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1rem}.card{background:var(--card);border:1px solid var(--border);border-radius:22px;padding:1.25rem;box-shadow:var(--shadow)}.muted,.meta{color:var(--muted)}h1{font-size:clamp(2.1rem,5vw,4.6rem)}h2{font-size:clamp(1.45rem,3vw,2.1rem)}h1,h2,h3{line-height:1.18}a{color:var(--accent)}article{max-width:860px}.prose p{margin:1rem 0}.notice{border-inline-start:5px solid var(--accent2);padding:1rem;background:var(--card);border-radius:12px}.skip{position:absolute;left:-999px}.skip:focus{left:1rem;top:1rem;background:var(--card);padding:1rem;z-index:99}footer{border-top:1px solid var(--border);padding:2rem 0}.logo{display:inline-flex;align-items:center;gap:.5rem}.logo svg{width:34px;height:34px}code{background:var(--card);border:1px solid var(--border);padding:.1rem .3rem;border-radius:.35rem}@media(max-width:640px){body{font-size:16px}nav a,.button{padding:.42rem .6rem}.hero{padding:2rem 0}}
""".strip()


def clean_dir() -> None:
    keep = {".git", "scripts"}
    for child in ROOT.iterdir():
        if child.name in keep:
            continue
        if child.is_dir():
            import shutil
            shutil.rmtree(child)
        elif child.name not in {"package.json"}:
            child.unlink()


def href(path: str) -> str:
    if path.startswith("http") or path.startswith("mailto:") or path.startswith("#"):
        return path
    if not path.startswith("/"):
        path = "/" + path
    return BASE + path


def nav(lang: str) -> str:
    items = [("About", "/about/"), ("Projects", "/projects/"), ("Research", "/research/"), ("Sources", "/sources/"), ("History", "/history/"), ("Contact", "/contact/")]
    if lang == "ar":
        items = [("من نحن", "/ar/about/"), ("المشروعات", "/ar/projects/"), ("الأبحاث", "/ar/research/"), ("المصادر", "/ar/sources/"), ("السجل", "/ar/history/"), ("تواصل", "/ar/contact/")]
    lang_link = href("/" if lang == "ar" else "/ar/")
    lang_text = "English" if lang == "ar" else "العربية"
    return "\n".join([f'<a class="brand logo" href="{href("/ar/" if lang=="ar" else "/")}"><svg viewBox="0 0 64 64" role="img" aria-label="DGGT logo"><circle cx="32" cy="32" r="29" fill="none" stroke="currentColor" stroke-width="5"/><path d="M18 35h28M22 23h20M22 47h20" stroke="currentColor" stroke-width="5" stroke-linecap="round"/></svg><span>DGGT Observatory</span></a>'] + [f'<a href="{href(u)}">{t}</a>' for t,u in items] + [f'<a href="{lang_link}">{lang_text}</a>', '<button class="button" type="button" onclick="document.body.classList.toggle(\'dark\');localStorage.dark=document.body.classList.contains(\'dark\')">☾</button>'])


def layout(title: str, body: str, lang: str, path: str, description: str | None = None) -> str:
    direction = "rtl" if lang == "ar" else "ltr"
    description = description or "Independent bilingual research observatory on AI agent governance, Gulf compute, identity, authentication, and KYC/KYB/AML."
    canonical = f"https://nabilayshan.github.io{href(path)}"
    disclaimer = DISCLAIMER_AR if lang == "ar" else DISCLAIMER_EN
    jsonld = {"@context":"https://schema.org","@type":"ResearchProject","name":SITE,"founder":{"@type":"Person","name":AUTHOR},"datePublished":PUBLISHED_AT,"inLanguage":["en","ar"],"url":canonical}
    return f"""<!doctype html>
<html lang="{lang}" dir="{direction}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} | {SITE}</title>
  <meta name="description" content="{html.escape(description)}">
  <link rel="stylesheet" href="{href('/assets/styles.css')}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" type="application/rss+xml" title="{SITE}" href="{href('/feed.xml')}">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(description)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta name="twitter:card" content="summary">
  <script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header><div class="wrap"><nav aria-label="Primary navigation">{nav(lang)}</nav></div></header>
  <main id="main" class="wrap">{body}</main>
  <footer><div class="wrap"><p class="notice">{disclaimer}</p><p class="meta">Version {VERSION} · Published {PUBLISHED_AT} UTC · No cookies, accounts, behavioral advertising, or invasive analytics.</p></div></footer>
  <script>if(localStorage.dark==='true')document.body.classList.add('dark')</script>
</body>
</html>
"""


def write(path: str, title: str, body: str, lang: str = "en", description: str | None = None) -> None:
    out = ROOT / path.strip("/") / "index.html" if path.strip("/") else ROOT / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(layout(title, body, lang, "/" + path.strip("/") + ("/" if path.strip("/") else ""), description), encoding="utf-8")


def sources_list(limit: int | None = None) -> str:
    selected = SOURCES[:limit] if limit else SOURCES
    return "<ul>" + "\n".join(f'<li><a href="{url}">{html.escape(name)}</a></li>' for name, url in selected) + "</ul>"


def article_sections_en(project_key: str, title: str) -> list[tuple[str, str]]:
    project = PROJECTS[project_key]["name"]
    return [
        ("Why the topic matters", f"{title} is a practical governance question rather than a slogan. The relevant systems may trigger payments, open support tickets, change access rights, request identity checks, schedule machine actions, or recommend operational decisions. A trustworthy design therefore begins with a narrow statement of purpose: what the system is allowed to do, what it is not allowed to do, what evidence is retained, and who can reverse the action. For {project}, the central research concern is not whether automation is useful; it is how automation remains accountable when it crosses organizational, technical, or jurisdictional boundaries."),
        ("Governance pattern", "A useful pattern is to separate policy, authorization, execution, and evidence. Policy defines the allowed action class and risk tier. Authorization records the human or institutional approval, including scope, duration, revocation method, and any spending or safety limit. Execution systems should consume only the minimum authorization needed for the next step. Evidence should be tamper-evident enough for audit, but not so invasive that it becomes a privacy risk. This pattern is compatible with standards-based identity, modern authentication, security logging, and risk-management practices."),
        ("Gulf market context", "Gulf digital markets combine ambitious public digital services, regulated financial services, cloud and data-center investment, and cross-border users who expect Arabic and English experiences. The region is not a single regulatory environment, so the safer research stance is to map common design questions instead of presenting one compliance answer. Important questions include where data is processed, who operates the identity provider, whether a service depends on a regulated financial institution, and whether a decision affects a person, a company, or a machine process."),
        ("Implementation considerations", "Teams evaluating this topic should document threat models, consent or approval ceremonies, authentication strength, fallback procedures, and incident response paths. High-impact actions should require stronger authentication, short-lived authorization, clear notices, and post-action receipts. Revocation should be tested like a production feature, not described only in policy text. Logs should record decision context without collecting unnecessary personal documents. If a vendor or model provider is involved, the boundary between the local service and external processing should be visible to reviewers."),
        ("Limits and cautions", "This observatory does not claim that a single framework solves all governance problems. NIST, IETF, W3C, OpenID, FATF, and official Gulf sources provide useful anchors, but each implementation still needs local legal, security, and operational review. The safest conclusion is modest: well-designed records, revocable authority, strong authentication, privacy minimization, and human escalation paths make autonomous or digital services easier to inspect and safer to improve."),
    ]


def article_sections_ar(project_key: str, title: str) -> list[tuple[str, str]]:
    project = PROJECTS[project_key]["name"]
    return [
        ("أهمية الموضوع", f"يمثل موضوع {title} سؤالًا عمليًا في الحوكمة وليس مجرد شعار تقني. قد تؤدي الأنظمة المعنية إلى تشغيل مدفوعات أو فتح طلبات دعم أو تغيير صلاحيات أو طلب تحقق من الهوية أو جدولة أفعال آلية أو اقتراح قرارات تشغيلية. لذلك يبدأ التصميم الموثوق بتحديد ضيق للغرض: ما المسموح للنظام بفعله، وما المحظور عليه، وما الدليل الذي يُحتفظ به، ومن يستطيع عكس الإجراء. في مشروع {project} لا ينحصر الاهتمام في فائدة الأتمتة، بل في إبقاء الأتمتة قابلة للمساءلة عندما تعبر حدودًا مؤسسية أو تقنية أو إقليمية."),
        ("نمط حوكمة عملي", "النمط المفيد هو الفصل بين السياسة والتفويض والتنفيذ والدليل. تحدد السياسة فئة الإجراء ومستوى المخاطر. يسجل التفويض الموافقة البشرية أو المؤسسية، بما في ذلك النطاق والمدة وطريقة الإلغاء وأي حد للإنفاق أو السلامة. ينبغي لأنظمة التنفيذ ألا تستهلك إلا الحد الأدنى من الصلاحية اللازمة للخطوة التالية. أما الدليل فيجب أن يكون قابلًا للتدقيق دون أن يتحول إلى مخاطر خصوصية. يتوافق هذا النمط مع الهوية المبنية على المعايير والمصادقة الحديثة وسجلات الأمن وممارسات إدارة المخاطر."),
        ("السياق الخليجي", "تجمع الأسواق الرقمية الخليجية بين خدمات حكومية رقمية طموحة وخدمات مالية منظمة واستثمارات في السحابة ومراكز البيانات ومستخدمين عابرين للحدود يتوقعون تجارب عربية وإنجليزية. المنطقة ليست بيئة تنظيمية واحدة، ولذلك فإن النهج البحثي الأكثر أمانًا هو رسم الأسئلة المشتركة بدل تقديم إجابة امتثال واحدة. من الأسئلة المهمة: أين تعالج البيانات، من يشغل مزود الهوية، هل تعتمد الخدمة على مؤسسة مالية منظمة، وهل يؤثر القرار في شخص أو شركة أو عملية آلية."),
        ("اعتبارات التنفيذ", "ينبغي للفرق التي تدرس هذا الموضوع توثيق نماذج التهديد ومراسم الموافقة أو الاعتماد وقوة المصادقة وإجراءات الرجوع ومسارات الاستجابة للحوادث. يجب أن تتطلب الإجراءات عالية الأثر مصادقة أقوى وتفويضًا قصير الأجل وإشعارات واضحة وإيصالات بعد التنفيذ. وينبغي اختبار الإلغاء كميزة إنتاجية لا كنص في السياسة فقط. كما يجب أن تسجل السجلات سياق القرار دون جمع وثائق شخصية غير ضرورية. وإذا شارك مزود نموذج أو مزود خدمة خارجي، فيجب أن يكون الحد الفاصل بين الخدمة المحلية والمعالجة الخارجية مرئيًا للمراجعين."),
        ("حدود وتنبيهات", "لا يدعي هذا المرصد أن إطارًا واحدًا يحل جميع مشكلات الحوكمة. توفر NIST وIETF وW3C وOpenID وFATF والمصادر الخليجية الرسمية نقاط ارتكاز مفيدة، لكن كل تطبيق يحتاج إلى مراجعة قانونية وأمنية وتشغيلية محلية. الخلاصة الأكثر اتزانًا أن السجلات المصممة جيدًا والتفويض القابل للإلغاء والمصادقة القوية وتقليل البيانات ومسارات التصعيد البشرية تجعل الخدمات الذاتية أو الرقمية أسهل في الفحص وأكثر أمانًا للتحسين."),
    ]


def render_article(project_key: str, title: str, lang: str) -> str:
    sections = article_sections_ar(project_key, title) if lang == "ar" else article_sections_en(project_key, title)
    project = PROJECTS[project_key]["name"]
    sources_title = "المصادر" if lang == "ar" else "Sources"
    return f"""
<article class="prose">
  <p class="meta">Published {PUBLISHED_AT} UTC · Author: {AUTHOR} · Project: <a href="{href(('/ar' if lang=='ar' else '') + '/projects/' + project_key + '/')}">{project}</a></p>
  {''.join(f'<h2>{h}</h2>\n<p>{p}</p>' for h,p in sections)}
  <h2>{sources_title}</h2>
  {sources_list(8)}
</article>
"""


def pages() -> None:
    write("", SITE, f"""
<section class="hero"><p class="eyebrow">Independent research initiative</p><h1>{SITE}</h1><p class="muted">A bilingual educational observatory on AI agent governance, machine oversight, Gulf compute infrastructure, authentication, digital identity, and KYC/KYB/AML.</p><p><a class="button" href="{href('/projects/')}">Explore projects</a> <a class="button" href="{href('/research/')}">Read research</a></p></section>
<section class="grid">{''.join(f'<article class="card"><h2>{p["name"]}</h2><p>{p["en"]}</p><a href="{href("/projects/"+k+"/")}">Open project</a></article>' for k,p in PROJECTS.items())}</section>
""")
    write("ar", SITE, f"""
<section class="hero"><p class="eyebrow">مبادرة بحثية مستقلة</p><h1>{SITE}</h1><p class="muted">مرصد تعليمي ثنائي اللغة حول حوكمة وكلاء الذكاء الاصطناعي والرقابة على الآلات والبنية الحاسوبية الخليجية والمصادقة والهوية الرقمية وKYC/KYB/AML.</p><p><a class="button" href="{href('/ar/projects/')}">استكشف المشروعات</a> <a class="button" href="{href('/ar/research/')}">اقرأ الأبحاث</a></p></section>
<section class="grid">{''.join(f'<article class="card"><h2>{p["name"]}</h2><p>{p["ar"]}</p><a href="{href("/ar/projects/"+k+"/")}">فتح المشروع</a></article>' for k,p in PROJECTS.items())}</section>
""", "ar")
    for lang in ("en", "ar"):
        prefix = "ar/" if lang == "ar" else ""
        write(prefix + "about", "من نحن" if lang == "ar" else "About", "<h1>من نحن</h1><p>هذا المرصد منشور بحثي وتعليمي مستقل يديره Nabil Ayshan. لا يمثل المرصد شركة مسجلة أو جهة حكومية أو بنكًا أو هيئة تنظيمية أو هيئة معايير، ولا يقدم خدمات تجارية أو نصائح شخصية.</p>" if lang == "ar" else "<h1>About</h1><p>This observatory is an independent research and educational publication maintained by Nabil Ayshan. It is not a registered company, government body, bank, regulator, or standards organization, and it does not provide commercial services or personalized advice.</p>", lang)
        write(prefix + "projects", "المشروعات" if lang == "ar" else "Projects", f"<h1>{'المشروعات' if lang=='ar' else 'Projects'}</h1><section class='grid'>" + "".join(f'<article class="card"><h2>{p["name"]}</h2><p>{p["ar" if lang=="ar" else "en"]}</p><a href="{href("/"+prefix+"projects/"+k+"/")}">{"فتح" if lang=="ar" else "Open"}</a></article>' for k,p in PROJECTS.items()) + "</section>", lang)
        write(prefix + "research", "الأبحاث والمقالات" if lang == "ar" else "Research", f"<h1>{'الأبحاث والمقالات' if lang=='ar' else 'Research'}</h1><section class='grid'>" + "".join(f'<article class="card"><h2>{ar if lang=="ar" else en}</h2><p class="meta">{PROJECTS[pk]["name"]}</p><a href="{href("/"+prefix+"research/"+slug+"/")}">{"قراءة" if lang=="ar" else "Read"}</a></article>' for pk,slug,en,ar in ARTICLE_TOPICS) + "</section>", lang)
        write(prefix + "sources", "المصادر" if lang == "ar" else "Sources", f"<h1>{'المصادر' if lang=='ar' else 'Sources'}</h1><p>{'مصادر أولية ورسمية مستخدمة في المرصد.' if lang=='ar' else 'Primary standards and official sources used across the observatory.'}</p>{sources_list()}", lang)
        write(prefix + "history", "سجل المشروع" if lang == "ar" else "Project History", f"<h1>{'سجل المشروع' if lang=='ar' else 'Project History'}</h1><ul><li>{'أول نشر حقيقي' if lang=='ar' else 'First public-ready publication'}: {PUBLISHED_AT} UTC.</li><li>{'الإصدار' if lang=='ar' else 'Version'}: {VERSION}.</li><li>{'هذا السجل يوثق توقيت النشر فقط ولا يثبت ملكية علامة تجارية.' if lang=='ar' else 'This record documents publication timing only and does not prove trademark ownership.'}</li></ul>", lang)
        write(prefix + "contact", "تواصل" if lang == "ar" else "Contact", f"<h1>{'تواصل' if lang=='ar' else 'Contact'}</h1><p>{'استخدم GitHub Issues للتصحيحات واقتراح المصادر وبلاغات الوصول. لا ترسل وثائق هوية أو بيانات KYC حساسة.' if lang=='ar' else 'Use GitHub Issues for corrections, source suggestions, and accessibility reports. Do not submit identity documents or sensitive KYC data.'}</p><p class='notice'>@agentconsent · @machineconsent · @gulfcompute · @gulfauth · @gulfkyc</p>", lang)
        write(prefix + "privacy", "سياسة الخصوصية" if lang == "ar" else "Privacy Policy", f"<h1>{'سياسة الخصوصية' if lang=='ar' else 'Privacy Policy'}</h1><p>{'هذا الموقع الثابت لا يستخدم ملفات تعريف ارتباط أو حسابات أو تحليلات تتبع أو نماذج تجمع بيانات شخصية. قد يعالج مزود الاستضافة سجلات خادم قياسية.' if lang=='ar' else 'This static site does not use cookies, accounts, tracking analytics, or forms that collect personal data. The hosting provider may process standard server logs.'}</p>", lang)
        write(prefix + "terms", "شروط الاستخدام" if lang == "ar" else "Terms of Use", f"<h1>{'شروط الاستخدام' if lang=='ar' else 'Terms of Use'}</h1><p>{'استخدم المواد للمعلومات العامة فقط، ولا تعتمد عليها كنصيحة قانونية أو مالية أو امتثالية أو أمنية.' if lang=='ar' else 'Use the material for general information only. Do not rely on it as legal, financial, compliance, or security advice.'}</p>", lang)
        write(prefix + "disclaimer", "إخلاء المسؤولية" if lang == "ar" else "Disclaimer", f"<h1>{'إخلاء المسؤولية' if lang=='ar' else 'Disclaimer'}</h1><p>{DISCLAIMER_AR if lang=='ar' else DISCLAIMER_EN}</p>", lang)
        for key, p in PROJECTS.items():
            related = [a for a in ARTICLE_TOPICS if a[0] == key]
            write(prefix + f"projects/{key}", p["name"], f"<h1>{p['name']}</h1><p>{p['ar' if lang=='ar' else 'en']}</p><p class='notice'>{DISCLAIMER_AR if lang=='ar' else DISCLAIMER_EN}</p><h2>{'مقالات المشروع' if lang=='ar' else 'Project articles'}</h2><ul>" + "".join(f'<li><a href="{href("/"+prefix+"research/"+slug+"/")}">{ar if lang=="ar" else en}</a></li>' for _,slug,en,ar in related) + "</ul>", lang)
        for pk, slug, en, ar in ARTICLE_TOPICS:
            title = ar if lang == "ar" else en
            write(prefix + f"research/{slug}", title, f"<h1>{title}</h1>" + render_article(pk, title, lang), lang)
    write("404", "Not found", "<h1>404</h1><p>The requested page was not found. Use the navigation links to continue.</p>")


def meta_files() -> None:
    (ROOT / "assets").mkdir(exist_ok=True)
    (ROOT / "assets/styles.css").write_text(CSS + "\n", encoding="utf-8")
    urls = []
    for f in sorted(ROOT.rglob("index.html")):
        if ".git" in f.parts:
            continue
        rel = "/" if f.parent == ROOT else "/" + str(f.parent.relative_to(ROOT)).replace(os.sep, "/") + "/"
        urls.append(rel)
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(f"  <url><loc>https://nabilayshan.github.io{href(u)}</loc></url>" for u in urls) + "\n</urlset>\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: {BASE}/\nSitemap: https://nabilayshan.github.io{href('/sitemap.xml')}\n", encoding="utf-8")
    (ROOT / "feed.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel>\n' + f"<title>{SITE}</title><link>https://nabilayshan.github.io{BASE}/</link><description>Independent bilingual research observatory.</description>\n" + "\n".join(f"<item><title>{html.escape(en)}</title><link>https://nabilayshan.github.io{href('/research/'+slug+'/')}</link></item>" for _,slug,en,_ in ARTICLE_TOPICS) + "\n</channel></rss>\n", encoding="utf-8")
    (ROOT / ".well-known").mkdir(exist_ok=True)
    (ROOT / ".well-known/security.txt").write_text("Contact: https://github.com/nabilayshan/digital-governance-observatory/issues\nPreferred-Languages: en, ar\n", encoding="utf-8")
    (ROOT / "_headers").write_text("/*\n  Content-Security-Policy: default-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline'; img-src 'self' data:; base-uri 'self'; form-action 'none'; frame-ancestors 'none'\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  Permissions-Policy: geolocation=(), microphone=(), camera=()\n", encoding="utf-8")
    (ROOT / ".github/workflows").mkdir(parents=True, exist_ok=True)
    (ROOT / ".github/workflows/pages.yml").write_text("""name: Deploy static site to GitHub Pages
on:
  push:
    branches: [main, work]
  workflow_dispatch:
permissions:
  contents: read
  pages: write
  id-token: write
concurrency:
  group: pages
  cancel-in-progress: true
jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: .
      - id: deployment
        uses: actions/deploy-pages@v4
""", encoding="utf-8")
    (ROOT / "README.md").write_text(f"""# {SITE}

Independent bilingual research and educational static site. Version {VERSION} first prepared for publication {PUBLISHED_AT} UTC.

The site is designed for GitHub Pages under `{BASE}/`, not only from the domain root. It uses static HTML, CSS, a small inline theme toggle, no database, no cookies, no paid services, and no invasive analytics.

## Local checks

```bash
npm run build
npm run test:links
npm run test:content
npm run review:final
```
""", encoding="utf-8")
    (ROOT / "CHANGELOG.md").write_text(f"# Changelog\n\n## {VERSION} - {PUBLISHED_AT}\n- Initial bilingual observatory with five research projects, ten English articles, ten Arabic article versions, legal pages, source files, and GitHub Pages workflow.\n", encoding="utf-8")
    (ROOT / "AUTHORS.md").write_text("# Authors\n\n- Nabil Ayshan\n", encoding="utf-8")
    (ROOT / "LICENSE").write_text("Code: MIT License. Content: Creative Commons Attribution 4.0 International (CC BY 4.0).\n", encoding="utf-8")
    (ROOT / "PROJECT_HISTORY.md").write_text(f"# Project History\n\n- {PUBLISHED_AT} UTC: First public-ready version {VERSION} prepared. This documents publication timing only and is not evidence of trademark ownership.\n", encoding="utf-8")
    (ROOT / "SOURCES.md").write_text("# Sources\n\n" + "".join(f"- [{name}]({url})\n" for name, url in SOURCES), encoding="utf-8")
    (ROOT / "CITATION.cff").write_text(f"cff-version: 1.2.0\ntitle: \"{SITE}\"\nauthors:\n  - family-names: Ayshan\n    given-names: Nabil\nversion: 1.0.0\ndate-released: \"{PUBLISHED_AT[:10]}\"\n", encoding="utf-8")
    (ROOT / "BRAND_SCREENING_NOTES.md").write_text(f"""# Brand Screening Notes

Date searched: {PUBLISHED_AT} UTC. This preliminary screening is not legal advice, not a final trademark clearance, and does not claim ownership or exclusivity.

Databases/sources checked where accessible: web search, GitHub search, WIPO Global Brand Database, USPTO search, EUIPO search, and SAIP public search availability. Automated access to some trademark databases may be limited; results should be reviewed by qualified counsel before commercial use.

| Name | Notable observations | Initial risk |
|---|---|---|
| Digital Governance & Gulf Technology Observatory | Descriptive components and similar technology observatory names exist, but no exact prominent match was identified in quick screening. | Low |
| AgentConsent | Descriptive phrase appears in AI consent discussions and software contexts. Used here only as an independent research project title. | Medium |
| MachineConsent | Sparse exact results; phrase may appear descriptively in machine autonomy discussions. | Low |
| GulfCompute | Similar Gulf computer/computing names may exist; exact research-title use was not identified in quick screening. | Medium |
| GulfAuth | Sparse exact results; authentication is descriptive. | Low |
| GulfKYC | Sparse exact results; KYC is descriptive in compliance and onboarding contexts. | Low |
""", encoding="utf-8")


def publication_manifest() -> None:
    import subprocess
    commit = os.environ.get("COMMIT_HASH")
    if not commit:
        try:
            commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
        except Exception:
            commit = "uncommitted-build"
    created = os.environ.get("MANIFEST_CREATED_AT", datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"))
    files = []
    for p in sorted(ROOT.rglob("*")):
        if p.is_file() and ".git" not in p.parts and p.name != "PUBLICATION_MANIFEST_SHA256.json":
            files.append({"path": str(p.relative_to(ROOT)).replace(os.sep, "/"), "sha256": hashlib.sha256(p.read_bytes()).hexdigest()})
    manifest = {"created_utc": created, "version": VERSION, "commit_hash_at_manifest_creation": commit, "notice": "This manifest documents the publication package hash set only; it is not evidence of trademark ownership.", "base_path": BASE, "files": files}
    (ROOT / "PUBLICATION_MANIFEST_SHA256.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    clean_dir()
    pages()
    meta_files()
    publication_manifest()

if __name__ == "__main__":
    main()
