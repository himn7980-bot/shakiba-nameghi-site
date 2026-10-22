#!/usr/bin/env python3
"""Builds en/, fa/, ar/ pages, sitemap.xml and robots.txt from one content file.

Edit the CONTENT dict below, then run:  python3 _src/build.py
To move to a custom domain, change SITE_URL.
"""
import html, json, pathlib

SITE_URL = "https://himn7980-bot.github.io/shakiba-nameghi-site/"
ROOT = pathlib.Path(__file__).resolve().parent.parent
VERSION = "11"
PHONE = "+9647773944470"
PHONE_SHOW = "+964 777 394 4470"
EMAIL = "business@shakibanameghi.com"
WHATSAPP = "https://wa.me/9647773944470"
LANGS = ["en", "fa", "ar"]
LANG_NAMES = {"en": "English", "fa": "فارسی", "ar": "العربية"}

CONTENT = {
"en": {
  "dir": "ltr", "locale": "en_US",
  "title": "Shakiba Nameghi — Architect, Project Manager & International Representative",
  "desc": "Official website of Shakiba Nameghi: architect, project manager and international representative working between Iran, Iraq and international partners.",
  "skip": "Skip to content", "menu": "Menu",
  "nav": ["About", "Expertise", "Projects", "Representation", "Credentials", "Contact"],
  "name": "Shakiba Nameghi",
  "role": "Architect, project manager and international representative",
  "intro": "Shakiba Nameghi works across architecture, project management and international representation, connecting projects, organisations and business opportunities in Iran and Iraq with international partners.",
  "cta_wa": "Message on WhatsApp", "cta_work": "See her experience",
  "route_cap": "Working between",
  "cities": [("Mashhad", "Iran"), ("Karbala", "Iraq")],
  "key": ("Farvardin Consortium", "Official representative in Iraq"),
  "photo_alt": "Portrait of Shakiba Nameghi",
  "about_h": "About",
  "about_p": "A practice built on projects, coordination and long-term international relationships.",
  "profile": "Since 2017–2018, Shakiba Nameghi has worked with Farvardin Consortium in project management, and later extended her professional work to Iraq as the consortium’s official representative. Her work today combines project leadership, design knowledge and international business coordination.",
  "facts": [("Based in", "Karbala, Iraq and Mashhad, Iran"), ("Scope", "Iran, Iraq and international"), ("Languages", "Persian, Arabic, English")],
  "exp_h": "Expertise", "exp_p": "One role that spans the whole project cycle.",
  "skills": [
    ("Architecture & design", "Architectural and interior design experience in hospitality and residential projects."),
    ("Project management", "Project leadership, stakeholder coordination, follow-up on execution and oversight of delivery."),
    ("International representation", "Business development, professional representation and coordination of cross-border cooperation in Iraq."),
  ],
  "proj_h": "Projects", "proj_p": "Selected experience in hospitality, architecture and building projects.",
  "pm": "Project management", "dc": "Design & execution", "mashhad": "Mashhad, Iran",
  "rep_h": "Representation", "rep_p": "A professional bridge between international companies and the Iraqi market.",
  "reps": [
    ("Farvardin Consortium", ["Iran", "Iraq"], "Official representative in Iraq. Consulting, design and construction projects."),
    ("RPSE", ["UAE", "Iraq"], "Authorised representative in Iraq. Oil and gas, petrochemicals, energy and process industries."),
    ("Panorama Commerce Ltd.", ["Canada", "Iraq"], "Regional representative. Industrial and investment opportunities."),
    ("Tav am GmbH", ["Germany", "Iraq"], "Official representative for the Iraqi import market."),
    ("Labkhand Salamat Mahboub", ["Iraq"], "Company representative in Iraq. Medical tourism, international patient services and business coordination."),
    ("Afnan Al-Nahrain Company", ["Iraq"], "Authorised to communicate and negotiate with companies and organisations on the company’s activities in real estate, investment and trade."),
  ],
  "cred_h": "Credentials", "cred_p": "The training and public roles behind her practice.",
  "creds": [
    ("2019", "DBA in Project Management", "Amin Institute of Higher Education. 400-hour professional programme."),
    ("2022", "Advisor on Women’s Affairs", "Islamic City Council of Mashhad."),
    ("", "International representation", "Construction, energy, trade, investment and medical tourism."),
  ],
  "contact_h": "Projects, partnerships and cross-border opportunities.",
  "contact_p": "For project enquiries, representation and cooperation in Iran and Iraq, the quickest way to reach her is WhatsApp.",
  "ch": ("WhatsApp", "Phone", "Email", "Based in"),
  "based": "Karbala, Iraq · Mashhad, Iran",
  "footer": "Architect · Project manager · International representative",
},
"fa": {
  "dir": "rtl", "locale": "fa_IR",
  "title": "شکیبا نامقی — معمار، مدیر پروژه و نماینده بین‌المللی",
  "desc": "وب‌سایت رسمی شکیبا نامقی؛ معمار، مدیر پروژه و نماینده بین‌المللی با تمرکز بر همکاری‌های ایران و عراق.",
  "skip": "رفتن به محتوا", "menu": "منو",
  "nav": ["درباره", "تخصص‌ها", "پروژه‌ها", "نمایندگی‌ها", "سوابق", "تماس"],
  "name": "شکیبا نامقی",
  "role": "معمار، مدیر پروژه و نماینده بین‌المللی",
  "intro": "شکیبا نامقی در حوزه معماری، مدیریت پروژه و نمایندگی بین‌المللی فعالیت می‌کند و میان پروژه‌ها، سازمان‌ها و فرصت‌های تجاری ایران، عراق و شرکای بین‌المللی ارتباط ایجاد می‌کند.",
  "cta_wa": "گفتگو در واتساپ", "cta_work": "دیدن سوابق",
  "route_cap": "محل فعالیت",
  "cities": [("مشهد", "ایران"), ("کربلا", "عراق")],
  "key": ("کنسرسیوم فروردین", "نماینده رسمی در عراق"),
  "photo_alt": "تصویر شکیبا نامقی",
  "about_h": "درباره",
  "about_p": "فعالیتی حرفه‌ای بر پایه پروژه، هماهنگی و روابط بین‌المللی بلندمدت.",
  "profile": "شکیبا نامقی از سال ۱۳۹۶ (۲۰۱۷–۲۰۱۸) همکاری خود را با کنسرسیوم فروردین در حوزه مدیریت پروژه آغاز کرد و سپس فعالیت حرفه‌ای خود را در عراق به‌عنوان نماینده رسمی این کنسرسیوم توسعه داد. فعالیت فعلی او ترکیبی از راهبری پروژه، شناخت طراحی و هماهنگی کسب‌وکار بین‌المللی است.",
  "facts": [("محل فعالیت", "کربلا، عراق و مشهد، ایران"), ("حوزه جغرافیایی", "ایران، عراق و بین‌المللی"), ("زبان‌ها", "فارسی، عربی، انگلیسی")],
  "exp_h": "تخصص‌ها", "exp_p": "نقشی چندرشته‌ای در سراسر چرخه پروژه.",
  "skills": [
    ("معماری و طراحی", "تجربه طراحی معماری و داخلی در پروژه‌های هتلداری و مسکونی."),
    ("مدیریت پروژه", "راهبری پروژه، هماهنگی ذی‌نفعان، پیگیری اجرا و نظارت بر روند تحویل."),
    ("نمایندگی بین‌المللی", "توسعه کسب‌وکار، نمایندگی حرفه‌ای و هماهنگی همکاری‌های فرامرزی در عراق."),
  ],
  "proj_h": "پروژه‌ها", "proj_p": "منتخب سوابق حرفه‌ای در هتلداری، معماری و پروژه‌های ساختمانی.",
  "pm": "مدیریت پروژه", "dc": "طراحی و اجرا", "mashhad": "مشهد، ایران",
  "rep_h": "نمایندگی‌ها", "rep_p": "پل حرفه‌ای میان مجموعه‌های بین‌المللی و بازار عراق.",
  "reps": [
    ("Farvardin Consortium", ["ایران", "عراق"], "نماینده رسمی در عراق؛ مشاوره، طراحی و پروژه‌های ساختمانی."),
    ("RPSE", ["امارات", "عراق"], "نماینده مجاز در عراق؛ نفت و گاز، پتروشیمی، انرژی و صنایع فرایندی."),
    ("Panorama Commerce Ltd.", ["کانادا", "عراق"], "نماینده منطقه‌ای؛ فرصت‌های صنعتی و سرمایه‌گذاری."),
    ("Tav am GmbH", ["آلمان", "عراق"], "نماینده رسمی در بازار واردات عراق."),
    ("لبخند سلامت محبوب", ["عراق"], "نماینده شرکت در عراق؛ گردشگری سلامت، خدمات بیماران بین‌المللی و هماهنگی کسب‌وکار."),
    ("Afnan Al-Nahrain Company", ["عراق"], "نماینده مجاز برای ارتباط و مذاکره با شرکت‌ها و نهادهای مرتبط درباره فعالیت‌های شرکت در املاک، سرمایه‌گذاری و تجارت."),
  ],
  "cred_h": "سوابق", "cred_p": "آموزش و نقش‌هایی که پشتوانه فعالیت حرفه‌ای او هستند.",
  "creds": [
    ("۱۳۹۸", "DBA مدیریت پروژه", "مؤسسه آموزش عالی امین؛ دوره حرفه‌ای ۴۰۰ ساعته (۲۰۱۹)."),
    ("۱۴۰۱", "مشاور امور بانوان", "شورای اسلامی شهر مشهد (۲۰۲۲)."),
    ("", "نمایندگی بین‌المللی", "ساخت‌وساز، انرژی، تجارت، سرمایه‌گذاری و گردشگری سلامت."),
  ],
  "contact_h": "پروژه‌ها، همکاری‌ها و فرصت‌های فرامرزی.",
  "contact_p": "برای پروژه، نمایندگی و همکاری در ایران و عراق، سریع‌ترین راه ارتباط واتساپ است.",
  "ch": ("واتساپ", "تلفن", "ایمیل", "محل فعالیت"),
  "based": "کربلا، عراق · مشهد، ایران",
  "footer": "معمار · مدیر پروژه · نماینده بین‌المللی",
},
"ar": {
  "dir": "rtl", "locale": "ar_IQ",
  "title": "شكيبا نامقي — مهندسة معمارية ومديرة مشاريع وممثلة دولية",
  "desc": "الموقع الرسمي لشكيبا نامقي؛ مهندسة معمارية ومديرة مشاريع وممثلة دولية تعمل بين إيران والعراق والشركاء الدوليين.",
  "skip": "انتقل إلى المحتوى", "menu": "القائمة",
  "nav": ["نبذة", "الخبرات", "المشاريع", "التمثيل", "المؤهلات", "التواصل"],
  "name": "شكيبا نامقي",
  "role": "مهندسة معمارية ومديرة مشاريع وممثلة دولية",
  "intro": "تعمل شكيبا نامقي في مجالات الهندسة المعمارية وإدارة المشاريع والتمثيل الدولي، وتربط بين المشاريع والمؤسسات والفرص التجارية في إيران والعراق ومع الشركاء الدوليين.",
  "cta_wa": "تواصل عبر واتساب", "cta_work": "اطّلع على خبراتها",
  "route_cap": "مقر العمل",
  "cities": [("مشهد", "إيران"), ("كربلاء", "العراق")],
  "key": ("كونسورتيوم فروردين", "الممثلة الرسمية في العراق"),
  "photo_alt": "صورة شكيبا نامقي",
  "about_h": "نبذة",
  "about_p": "ممارسة مهنية تقوم على المشاريع والتنسيق والعلاقات الدولية طويلة الأمد.",
  "profile": "منذ 2017/2018 تعاونت شكيبا نامقي مع كونسورتيوم فروردين في إدارة المشاريع، ثم وسّعت نشاطها المهني إلى العراق بصفتها الممثلة الرسمية للكونسورتيوم. ويجمع عملها الحالي بين قيادة المشاريع والمعرفة التصميمية والتنسيق في الأعمال الدولية.",
  "facts": [("المقر", "كربلاء، العراق ومشهد، إيران"), ("نطاق العمل", "إيران والعراق والنطاق الدولي"), ("اللغات", "الفارسية، العربية، الإنجليزية")],
  "exp_h": "الخبرات", "exp_p": "دور متعدد التخصصات عبر دورة حياة المشروع بأكملها.",
  "skills": [
    ("الهندسة المعمارية والتصميم", "خبرة في التصميم المعماري والداخلي ضمن مشاريع الضيافة والسكن."),
    ("إدارة المشاريع", "قيادة المشاريع وتنسيق أصحاب المصلحة ومتابعة التنفيذ والإشراف على مسار التسليم."),
    ("التمثيل الدولي", "تطوير الأعمال والتمثيل المهني وتنسيق التعاون العابر للحدود في العراق."),
  ],
  "proj_h": "المشاريع", "proj_p": "نماذج مختارة من الخبرة المهنية في الضيافة والعمارة والمشاريع الإنشائية.",
  "pm": "إدارة المشروع", "dc": "التصميم والتنفيذ", "mashhad": "مشهد، إيران",
  "rep_h": "التمثيل", "rep_p": "جسر مهني بين المؤسسات الدولية والسوق العراقي.",
  "reps": [
    ("Farvardin Consortium", ["إيران", "العراق"], "الممثلة الرسمية في العراق؛ الاستشارات والتصميم والمشاريع الإنشائية."),
    ("RPSE", ["الإمارات", "العراق"], "الممثلة المعتمدة في العراق؛ النفط والغاز والبتروكيماويات والطاقة والصناعات العملية."),
    ("Panorama Commerce Ltd.", ["كندا", "العراق"], "الممثلة الإقليمية؛ الفرص الصناعية والاستثمارية."),
    ("Tav am GmbH", ["ألمانيا", "العراق"], "الممثلة الرسمية في سوق الاستيراد العراقي."),
    ("شركة لبخند سلامت محبوب", ["العراق"], "ممثلة الشركة في العراق؛ السياحة العلاجية وخدمات المرضى الدوليين وتنسيق الأعمال."),
    ("Afnan Al-Nahrain Company", ["العراق"], "ممثلة مفوضة للتواصل والتفاوض مع الشركات والجهات ذات العلاقة بشأن أنشطة الشركة في العقارات والاستثمار والتجارة."),
  ],
  "cred_h": "المؤهلات", "cred_p": "التأهيل والأدوار العامة التي تدعم ممارستها المهنية.",
  "creds": [
    ("2019", "DBA في إدارة المشاريع", "معهد أمين للتعليم العالي؛ برنامج مهني بواقع 400 ساعة."),
    ("2022", "مستشارة شؤون المرأة", "المجلس الإسلامي لمدينة مشهد."),
    ("", "التمثيل الدولي", "الإنشاءات والطاقة والتجارة والاستثمار والسياحة العلاجية."),
  ],
  "contact_h": "المشاريع والشراكات والفرص العابرة للحدود.",
  "contact_p": "للاستفسار عن المشاريع والتمثيل والتعاون في إيران والعراق، أسرع وسيلة للتواصل هي واتساب.",
  "ch": ("واتساب", "الهاتف", "البريد الإلكتروني", "المقر"),
  "based": "كربلاء، العراق · مشهد، إيران",
  "footer": "مهندسة معمارية · مديرة مشاريع · ممثلة دولية",
},
}

PROJECTS = [("Khayyam Hotel", "pm"), ("Zeytoon Hotel", "pm"), ("Olympia Hotel", "pm"),
            ("Siba Hotel", "pm"), ("Habib Hotel", "pm"), ("Doctors Building", "dc")]
IDS = ["about", "expertise", "projects", "representation", "credentials", "contact"]

e = html.escape
ARCH_MARK = ('<svg viewBox="0 0 30 34" aria-hidden="true"><path d="M1 33V14C1 7 8 3 15 1c7 2 14 6 14 13v19z" fill="none" '
             'stroke="currentColor" stroke-width="1.6"/><path d="M8 33V17c0-3 3-5.5 7-6.5 4 1 7 3.5 7 6.5v16" fill="none" '
             'stroke="#23807B" stroke-width="1.6"/></svg>')
WA_ICON = ('<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2'
           'a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1'
           'c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2'
           ' 5.1 5.1 0 0 0 1.1 2.7 11.7 11.7 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg>')
MENU_ICON = ('<svg class="bars" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 8h16M4 16h16" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>'
             '<svg class="x" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>')


def url(lang):
    return f"{SITE_URL}{lang}/"


def head(lang, c):
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{url(l)}">' for l in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}">'
    person = {
        "@context": "https://schema.org", "@type": "Person", "name": "Shakiba Nameghi",
        "alternateName": ["شکیبا نامقی", "شكيبا نامقي"], "url": url(lang), "image": SITE_URL + "portrait.jpg",
        "jobTitle": ["Architect", "Project Manager", "International Representative"],
        "telephone": PHONE, "email": EMAIL, "knowsLanguage": ["fa", "ar", "en"],
        "workLocation": [{"@type": "Place", "name": "Karbala, Iraq"}, {"@type": "Place", "name": "Mashhad, Iran"}],
    }
    others = [l for l in LANGS if l != lang]
    return f'''<!doctype html>
<html lang="{lang}" dir="{c["dir"]}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(c["title"])}</title>
<meta name="description" content="{e(c["desc"])}">
<meta name="theme-color" content="#EEF1EF">
<link rel="canonical" href="{url(lang)}">{alts}
<meta property="og:type" content="profile">
<meta property="og:title" content="{e(c["title"])}">
<meta property="og:description" content="{e(c["desc"])}">
<meta property="og:url" content="{url(lang)}">
<meta property="og:image" content="{SITE_URL}og.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:locale" content="{c["locale"]}">{"".join(f'<meta property="og:locale:alternate" content="{CONTENT[l]["locale"]}">' for l in others)}
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="../apple-touch-icon.png">
<link rel="preload" href="../fonts/{"marcellus-latin-400-normal" if lang == "en" else "noto-naskh-arabic-arabic-700-normal"}.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="../style.css?v={VERSION}">
<script>document.documentElement.classList.remove('no-js')</script>
<script defer src="../script.js?v={VERSION}"></script>
<script type="application/ld+json">{json.dumps(person, ensure_ascii=False)}</script>
</head>
'''


def page(lang):
    c = CONTENT[lang]
    nav = "".join(f'<a href="#{i}">{e(t)}</a>' for i, t in zip(IDS, c["nav"]))
    langs = "".join(
        f'<a href="../{l}/" lang="{l}" hreflang="{l}"{" aria-current=\"page\"" if l == lang else ""}>{LANG_NAMES[l]}</a>' for l in LANGS)
    (c1, k1), (c2, k2) = c["cities"]
    facts = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in c["facts"])
    skills = "".join(f'<div class="skill"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in c["skills"])
    projects = "".join(
        f'<li><h3>{e(n)}</h3><span class="city">{e(c["mashhad"])}</span>'
        f'<span class="tag{" alt" if k == "dc" else ""}">{e(c[k])}</span></li>' for n, k in PROJECTS)
    reps = ""
    for n, countries, d in c["reps"]:
        title = f'<h3 class="native">{e(n)}</h3>' if not n.isascii() else (f'<h3 lang="en"><bdi>{e(n)}</bdi></h3>' if lang != "en" else f"<h3>{e(n)}</h3>")
        reps += (f'<article class="rep"><div class="countries">{"".join(f"<span>{e(x)}</span>" for x in countries)}</div>'
                 f'{title}<p>{e(d)}</p></article>')
    creds = ""
    for y, t, d in c["creds"]:
        yr = f'<span class="yr">{e(y)}</span>' if y else ""
        creds += f'<div class="cred{"" if y else " noyr"}">{yr}<div><h3>{e(t)}</h3><p>{e(d)}</p></div></div>'
    wa, ph, em, bs = c["ch"]
    flang = "".join(f'<a href="../{l}/" lang="{l}">{LANG_NAMES[l]}</a>' for l in LANGS if l != lang)

    body = f'''<body>
<a class="skip" href="#main">{e(c["skip"])}</a>
<header class="site-header">
  <div class="wrap bar">
    <a class="brand" href="./" aria-label="Shakiba Nameghi">{ARCH_MARK}<span>SHAKIBA NAMEGHI</span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="panel" aria-label="{e(c["menu"])}">{MENU_ICON}</button>
    <div class="panel" id="panel">
      <nav class="nav" aria-label="{e(c["menu"])}">{nav}</nav>
      <div class="lang">{langs}</div>
    </div>
  </div>
</header>
<main id="main">
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-text">
      <h1>{e(c["name"])}</h1>
      <p class="role">{e(c["role"])}</p>
      <p class="intro">{e(c["intro"])}</p>
      <div class="actions">
        <a class="btn btn-solid" href="{WHATSAPP}" target="_blank" rel="noopener">{WA_ICON}{e(c["cta_wa"])}</a>
        <a class="btn btn-line" href="#projects">{e(c["cta_work"])}</a>
      </div>
      <div class="route">
        <p class="route-cap">{e(c["route_cap"])}</p>
        <div class="route-line"><b>{e(c1)}<small>{e(k1)}</small></b><i></i><b>{e(c2)}<small>{e(k2)}</small></b></div>
      </div>
    </div>
    <figure class="arch">
      <div class="arch-shape arch-back"></div>
      <div class="arch-shape arch-photo"><img src="../portrait.jpg" alt="{e(c["photo_alt"])}" width="720" height="900" fetchpriority="high"></div>
      <figcaption class="arch-key"><strong>{e(c["key"][0])}</strong>{e(c["key"][1])}</figcaption>
    </figure>
  </div>
</section>

<section class="section" id="about">
  <div class="wrap split">
    <div class="head"><h2>{e(c["about_h"])}</h2><p>{e(c["about_p"])}</p></div>
    <div><p class="profile">{e(c["profile"])}</p><dl class="facts">{facts}</dl></div>
  </div>
</section>

<section class="section" id="expertise">
  <div class="wrap split">
    <div class="head"><h2>{e(c["exp_h"])}</h2><p>{e(c["exp_p"])}</p></div>
    <div class="skills">{skills}</div>
  </div>
</section>

<section class="section" id="projects">
  <div class="wrap split">
    <div class="head"><h2>{e(c["proj_h"])}</h2><p>{e(c["proj_p"])}</p></div>
    <ul class="projects">{projects}</ul>
  </div>
</section>

<section class="section on-dark" id="representation">
  <div class="wrap split">
    <div class="head"><h2>{e(c["rep_h"])}</h2><p>{e(c["rep_p"])}</p></div>
    <div class="reps">{reps}</div>
  </div>
</section>

<section class="section" id="credentials">
  <div class="wrap split">
    <div class="head"><h2>{e(c["cred_h"])}</h2><p>{e(c["cred_p"])}</p></div>
    <div class="creds">{creds}</div>
  </div>
</section>

<section class="section on-dark contact" id="contact">
  <div class="wrap contact-grid">
    <div>
      <h2>{e(c["contact_h"])}</h2>
      <p class="lead">{e(c["contact_p"])}</p>
      <div class="actions"><a class="btn btn-solid" href="{WHATSAPP}" target="_blank" rel="noopener">{WA_ICON}{e(c["cta_wa"])}</a></div>
    </div>
    <ul class="channels">
      <li><span>{e(wa)}</span><a href="{WHATSAPP}" target="_blank" rel="noopener"><bdi class="ltr">{PHONE_SHOW}</bdi></a></li>
      <li><span>{e(ph)}</span><a href="tel:{PHONE}"><bdi class="ltr">{PHONE_SHOW}</bdi></a></li>
      <li><span>{e(em)}</span><a href="mailto:{EMAIL}"><bdi class="ltr">{EMAIL}</bdi></a></li>
      <li><span>{e(bs)}</span><strong>{e(c["based"])}</strong></li>
    </ul>
  </div>
</section>
</main>
<footer class="site-footer">
  <div class="wrap"><span>© <span class="yr-now">2026</span> Shakiba Nameghi · {e(c["footer"])}</span><nav aria-label="Languages">{flang}</nav></div>
</footer>
</body>
</html>
'''
    return head(lang, c) + body


def main():
    for lang in LANGS:
        out = ROOT / lang / "index.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(page(lang), encoding="utf-8")
    alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{url(l)}"/>' for l in LANGS)
    alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE_URL}"/>'
    urls = "".join(f"<url><loc>{url(l)}</loc>{alts}</url>\n" for l in LANGS)
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        f'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n{urls}</urlset>\n', encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n", encoding="utf-8")
    print("built", LANGS)


if __name__ == "__main__":
    main()
