#!/usr/bin/env python3
"""Generate the WORTH Association RFP pitch concept site. Static HTML, no build step at runtime."""
import math, os, html

OUT = os.path.dirname(os.path.abspath(__file__))
ORG = "WORTH Association"  # ONE swappable constant for the client name

def dial_svg():
    cx, cy, r = 200, 190, 140
    def pt(a_deg, rr):
        a = math.radians(a_deg)
        return (cx + rr * math.sin(a), cy - rr * math.cos(a))
    ticks = []
    for a in range(-60, 61, 10):
        major = (a % 30 == 0)
        x1, y1 = pt(a, r - (16 if major else 9))
        x2, y2 = pt(a, r)
        w = 3 if major else 1.5
        ticks.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#201812" stroke-width="{w}" opacity="{0.85 if major else 0.4}"/>')
    sx, sy = pt(-60, r); ex, ey = pt(60, r)
    arc = f'M {sx:.1f} {sy:.1f} A {r} {r} 0 0 1 {ex:.1f} {ey:.1f}'
    return f'''<svg id="dial-svg" viewBox="0 0 400 330" role="img" aria-label="A dial gauge with its needle pointing upward, symbolising moving the dial for gender equity">
  <path d="{arc}" fill="none" stroke="#B23E2B" stroke-width="10" stroke-linecap="round"/>
  {''.join(ticks)}
  <circle cx="{cx}" cy="{cy}" r="12" fill="#201812"/>
  <g id="dial-needle" transform="rotate(-55 {cx} {cy})">
    <line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-118}" stroke="#201812" stroke-width="6" stroke-linecap="round"/>
    <circle cx="{cx}" cy="{cy-118}" r="7" fill="#B23E2B"/>
  </g>
  <text x="{cx}" y="300" text-anchor="middle" font-family="ui-monospace,Menlo,monospace" font-size="15" letter-spacing="6" fill="#6B5E50">MOVE THE DIAL</text>
</svg>'''

def brand_mark():
    return '''<svg class="brand-mark" viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="18" fill="none" stroke="#B23E2B" stroke-width="3"/><path d="M13 28 L17 12 L20 24 L23 12 L27 28" fill="none" stroke="#201812" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'''

NAV = [
    ("about.html", "About WORTH"),
    ("method.html", "Our Method"),
    ("work.html", "Work & Standards"),
    ("process.html", "Process"),
    ("pricing.html", "Pricing"),
    ("faq.html", "FAQ"),
]

def header(current):
    links = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ''
        links.append(f'<a href="{href}"{cur}>{label}</a>')
    links.append('<a class="nav-cta" href="contact.html">Respond to RFP</a>')
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="concept-banner"><strong>Design concept</strong> — an independent pitch by <a href="https://tiyandegital.com">Tiyan Digital</a> for {ORG}'s 2026 website RFP. Not an official {ORG} site.</div>
<header class="site-header"><div class="header-inner">
<a class="brand" href="index.html" aria-label="WORTH concept home">{brand_mark()}<span><span class="brand-name">{ORG}</span><span class="brand-sub">Website Concept · RFP 2026</span></span></a>
<button class="nav-toggle" aria-expanded="false" aria-controls="main-nav">Menu</button>
<nav class="main-nav" id="main-nav" aria-label="Primary">{''.join(links)}</nav>
</div></header>'''

def footer():
    return f'''<footer class="site-footer"><div class="wrap">
<div class="footer-grid">
<div><div class="footer-brand">{ORG}</div><p class="footer-tag">Women of Recreation, Tourism &amp; Hospitality — a concept redesign for the 2026 website RFP, crafted by Tiyan Digital.</p></div>
<div><h4>Explore</h4><ul><li><a href="index.html">Home</a></li><li><a href="about.html">About {ORG}</a></li><li><a href="method.html">Our Method</a></li><li><a href="work.html">Work &amp; Standards</a></li></ul></div>
<div><h4>Proposal</h4><ul><li><a href="process.html">Process</a></li><li><a href="pricing.html">Pricing Guidance</a></li><li><a href="faq.html">FAQ</a></li><li><a href="contact.html">Contact</a></li></ul></div>
<div><h4>Legal</h4><ul><li><a href="privacy.html">Privacy Policy</a></li><li><a href="terms.html">Terms</a></li><li><a href="cookies.html">Cookie Policy</a></li></ul></div>
</div>
<p class="footer-land">{ORG} operates on the traditional, ancestral and unceded territory of the Coast Salish peoples — the Musqueam, Stó:lō, Squamish and Tsleil-Waututh Nations. (As stated on worthassociation.com.)</p>
<div class="footer-legal"><span>© <span id="year">2026</span> Tiyan Digital. Independent design concept — not affiliated with or endorsed by {ORG}.</span><span>All copy about {ORG} is drawn from public sources; gaps are marked [Placeholder].</span></div>
</div></footer>'''

def page(filename, title, desc, current, body, h1_hidden=False):
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<script>document.documentElement.className += ' anim';</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="assets/style.css">
<script src="assets/site.js" defer></script>
</head>
<body>
{header(current)}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>'''
    with open(os.path.join(OUT, filename), "w") as f:
        f.write(doc)

# ---------------------------------------------------------------- bodies

HOME_BODY = f'''<section class="hero"><div class="wrap hero-grid">
<div class="hero-copy">
<p class="eyebrow fade-up">A website concept · Responding to the 2026 RFP</p>
<h1><span class="rise"><span>Move the dial</span></span><span class="rise"><span>for women in tourism.</span></span></h1>
<p class="lede fade-up d1">{ORG} educates, elevates and engages women across recreation, tourism and hospitality. Their RFP asks for a digital presence that is more engaging, more accessible and more resource-rich. This concept shows what that could look like — and how we would build it.</p>
<div class="hero-ctas fade-up d2"><a class="btn" href="method.html">See our method</a><a class="btn btn-ghost" href="contact.html">Respond to the RFP</a></div>
</div>
<div class="hero-art fade-up d2"><div class="dial-frame">{dial_svg()}<p class="dial-caption">Concept motif — “Help us move the dial”</p></div></div>
</div></section>

<div class="marquee" aria-hidden="true"><div class="marquee-track">
<span><b>EDUCATE</b> — mentorship, academy, training</span><span><b>ELEVATE</b> — leadership, advocacy, voice</span><span><b>ENGAGE</b> — community, events, connection</span>
<span><b>EDUCATE</b> — mentorship, academy, training</span><span><b>ELEVATE</b> — leadership, advocacy, voice</span><span><b>ENGAGE</b> — community, events, connection</span>
</div></div>

<section><div class="wrap">
<div class="section-head"><p class="eyebrow">Programs</p><h2>Three pillars, one community.</h2><p class="lede">Everything {ORG} does maps to educate, elevate and engage. A redesign should make that structure the navigation — so every visitor finds their door in one click.</p></div>
<div class="program-list">
<a class="program-row" href="about.html"><span class="program-num">01</span><h3>WORTH Academy</h3><p>Professional development that builds leadership confidence — including the flagship 6-week program for women advancing their careers.</p><span class="program-tag">Educate</span></a>
<a class="program-row" href="about.html"><span class="program-num">02</span><h3>Mentorship</h3><p>Emerging leaders matched with experienced industry professionals who understand the sector's challenges and opportunities.</p><span class="program-tag">Educate · Engage</span></a>
<a class="program-row" href="about.html"><span class="program-num">03</span><h3>Leadership Summit</h3><p>The annual gathering — 2025's theme: “All Ages, All Stages: Building the Future Together” — plus WORTH-shops and networking events.</p><span class="program-tag">Engage</span></a>
<a class="program-row" href="about.html"><span class="program-num">04</span><h3>Scholarships</h3><p>Financial support that breaks down barriers to professional development and leadership opportunities.</p><span class="program-tag">Elevate</span></a>
<a class="program-row" href="about.html"><span class="program-num">05</span><h3>Advocacy &amp; Research</h3><p>Data-driven advocacy for gender equity across the visitor economy, aligned with the UN Sustainable Development Goals.</p><span class="program-tag">Elevate</span></a>
</div></div></section>

<section class="band-dark"><div class="wrap">
<div class="section-head"><p class="eyebrow">Impact — stated with sources</p><h2>Real numbers, honestly shown.</h2><p class="lede">A nonprofit site earns trust with verifiable figures, never invented ones. Every number here names its source.</p></div>
<div class="impact-grid">
<div class="impact-cell"><div class="impact-num"><span data-count="5000" data-suffix="+">5,000+</span></div><p class="impact-label">women reached through advocacy, events and resources</p><p class="impact-src">Source: “Women of WORTH” gender-equality report, 4VI, 2023 (citing {ORG})</p></div>
<div class="impact-cell"><div class="impact-num"><span data-count="100" data-prefix="~">~100</span></div><p class="impact-label">women elevated through the mentorship program</p><p class="impact-src">Source: worthassociation.com blog, 2025</p></div>
<div class="impact-cell"><div class="impact-num">2018</div><p class="impact-label">incorporated as a non-profit society in British Columbia</p><p class="impact-src">Source: worthassociation.com/about-us</p></div>
<div class="impact-cell"><div class="impact-num"><span data-count="4445">4,445</span></div><p class="impact-label">LinkedIn community members and counting</p><p class="impact-src">Source: {ORG} LinkedIn page, Nov 2026</p></div>
</div></div></section>

<section><div class="wrap"><div class="quote-block">
<p class="eyebrow">In their words</p>
<blockquote>“We want to create opportunities for women to advance, learn, and make their voices heard, so that we can see more women in top leadership roles.”</blockquote>
<cite>Joanna Jagger — Founder &amp; Executive Director, {ORG} · STAY Magazine, 2025</cite>
</div></div></section>

<section style="padding-top:0"><div class="wrap"><div class="split">
<div><p class="eyebrow">Stay connected</p><h2>The newsletter is the community's front door.</h2><p class="lede">In the concept, signup sits one scroll from the hero — name, email, consent, done. No dark patterns, no pre-ticked boxes.</p></div>
<div><form class="form-card" data-demo action="#" method="post">
<div class="field"><label for="nl-name">First name</label><input id="nl-name" name="name" type="text" autocomplete="given-name"></div>
<div class="field"><label for="nl-email">Email <span class="req" aria-hidden="true">*</span></label><input id="nl-email" name="email" type="email" required autocomplete="email"><p class="hint">Program updates, event invites, mentorship calls. Unsubscribe anytime.</p></div>
<div class="consent"><input id="nl-consent" type="checkbox" required><p><label for="nl-consent">I agree to receive {ORG} updates by email. My details are used only for this newsletter.</label></p></div>
<button class="btn" type="submit">Join the newsletter</button>
<p class="form-notice placeholder-note" hidden tabindex="-1"><strong>Demo form.</strong> In this concept build nothing is sent anywhere — a production site would connect this to {ORG}'s email platform.</p>
</form></div>
</div></div></section>

<section class="final-cta"><div class="wrap">
<h2>This is a concept. Imagine it built for real.</h2>
<p>We would love to respond to {ORG}'s RFP properly — with a formal proposal, references and a fixed quote. The deadline is November 20, 2026.</p>
<a class="btn btn-light" href="contact.html">Start the conversation</a>
</div></section>'''

ABOUT_BODY = f'''<section class="page-hero"><div class="wrap">
<p class="eyebrow">About {ORG}</p>
<h1><span class="rise"><span>Educate. Elevate.</span></span><span class="rise"><span>Engage.</span></span></h1>
<p class="lede fade-up d1" style="margin-top:24px">What follows is drawn only from {ORG}'s public materials. Where facts end, we say so — a redesign would fill these pages with the team's own words.</p>
</div></section>

<section style="padding-top:40px"><div class="wrap split">
<div class="prose">
<h2>Our purpose</h2>
<p>{ORG} — Women of Recreation, Tourism &amp; Hospitality — is a Canadian non-profit society working to advance equity across the visitor economy. It champions self-identifying women and gender-diverse people working in recreation, tourism and hospitality through mentorship, leadership development, advocacy and community connection.</p>
<p>While women represent a significant share of the industry's workforce, they remain underrepresented in decision-making roles. {ORG} exists to change that: equipping women with the tools and networks they need to thrive, and partnering with industry to build a more inclusive and resilient future.</p>
<h2>Our promise</h2>
<p>At {ORG}, the team drives positive change by advocating equity, diversity and inclusion in all aspects of its work — aligned with the UN Sustainable Development Goals, as part of a larger system-wide shift to dismantle structural barriers and foster gender-inclusive economies.</p>
<h2>How the work lands</h2>
<p>{ORG} creates pathways for women to grow, lead and thrive while shifting the broader industry toward greater equity. The work spans individual and systemic impact: supporting women directly through mentorship, training, scholarships and leadership development — and inviting senior leaders and companies into meaningful, collective action.</p>
<div class="placeholder-note"><strong>[Placeholder]</strong> Board of directors, staff team, annual reports and audited financials would live here — supplied by {ORG} in a production build, never invented.</div>
</div>
<div>
<div class="card" style="margin-bottom:24px"><span class="card-num">At a glance</span>
<ul style="list-style:none;margin:0"><li style="padding:8px 0;border-bottom:1px solid var(--line)"><strong>Founded:</strong> 2018 (BC non-profit society)</li>
<li style="padding:8px 0;border-bottom:1px solid var(--line)"><strong>Founder:</strong> Joanna Jagger, Executive Director</li>
<li style="padding:8px 0;border-bottom:1px solid var(--line)"><strong>Serves:</strong> women &amp; gender-diverse people in recreation, tourism, hospitality</li>
<li style="padding:8px 0"><strong>Reach:</strong> pan-Canadian programs &amp; partnerships</li></ul></div>
<div class="card"><span class="card-num">Publicly named partners</span><p>TOTA, BCHA and go2HR — named in {ORG}'s 2025 public writing as collaborators extending its reach. <span style="font-size:13px">(Source: worthassociation.com blog, 2025.)</span></p></div>
</div></div></section>

<section class="band-dark"><div class="wrap"><div class="quote-block">
<p class="eyebrow">Founder</p>
<blockquote>“WORTH is a small grassroots association, but our growth and achievements are worth bragging about. We have reached thousands of women in the province through our events, webinars and speaking engagements.”</blockquote>
<cite>Joanna Jagger — Founder &amp; Executive Director · worthassociation.com, 2025</cite>
</div></div></section>

<section><div class="wrap split">
<div class="prose"><h2>Belonging, stated plainly</h2><p>{ORG} uses an inclusive definition of the terms woman and female, and welcomes trans, queer and non-binary people — as well as allies — into its community. Its public materials particularly welcome applicants from diverse communities, including youth, Indigenous communities, newcomer Canadians, visible minorities, women, persons with disabilities and LGBTQ2I communities.</p></div>
<div class="prose"><h2>Land acknowledgment</h2><p>{ORG} operates on the traditional, ancestral and unceded territory of the Coast Salish peoples: the šxʷməθkʷəy̓əmaɁɬ təməxʷ (Musqueam), S’ólh Téméxw (Stó:lō), Skwxwú7mesh-ulh Temíx̱w (Squamish) and səl̓ilwətaɁɬ təməxʷ (Tsleil-Waututh) Nations — as stated on worthassociation.com.</p></div>
</div></section>'''

METHOD_BODY = f'''<section class="page-hero"><div class="wrap">
<p class="eyebrow">Our method · Tiyan Digital</p>
<h1><span class="rise"><span>Psychology first,</span></span><span class="rise"><span>then design, then code.</span></span></h1>
<p class="lede fade-up d1" style="margin-top:24px">This is the process behind the concept — and the process we would bring to {ORG}'s rebuild. No generic templates, no invented claims, no accessibility afterthoughts.</p>
</div></section>

<section style="padding-top:40px"><div class="wrap">
<div class="steps">
<div class="step"><span class="step-n">01</span><div><span class="weeks">Discovery</span><h3>Listen before we draw</h3><p>Content audit of the current site, stakeholder interviews, analytics review, and an accessibility baseline. We map every audience — members, mentors, sponsors, press — to the one action each needs to take.</p></div></div>
<div class="step"><span class="step-n">02</span><div><span class="weeks">Strategy</span><h3>Psychology → design → code</h3><p>We define what each visitor must feel, trust and do. Then the design system: type voice, color position, layout idea, one signature moment per page. Only then do we write code.</p></div></div>
<div class="step"><span class="step-n">03</span><div><span class="weeks">Design</span><h3>Editorial, warm, assured</h3><p>Association sites win with clarity and humanity: real stories, honest numbers with sources, generous whitespace. The RFP's three asks — engaging, accessible, resource-rich — become design requirements, not adjectives.</p></div></div>
<div class="step"><span class="step-n">04</span><div><span class="weeks">Build</span><h3>Accessible as standard, not as add-on</h3><p>WCAG 2.2 AA contrast and keyboard support, semantic HTML, visible focus, reduced-motion support, plain-language copy. Performance budget: fast on a rural phone connection, not just downtown wifi.</p></div></div>
<div class="step"><span class="step-n">05</span><div><span class="weeks">Handover</span><h3>A site your team can actually run</h3><p>We hand over a CMS the communications team can update without a developer — with training, documentation, and a care plan for the months after launch.</p></div></div>
</div></div></section>

<section><div class="wrap">
<div class="section-head"><p class="eyebrow">Non-negotiables</p><h2>What every build ships with.</h2></div>
<div class="card-grid">
<div class="card"><span class="card-num">Accessibility</span><h3>WCAG 2.2 AA</h3><p>Contrast-verified palette, keyboard-navigable everything, screen-reader labels, captions on media, reduced-motion path. Checked, not claimed.</p></div>
<div class="card"><span class="card-num">Honesty</span><h3>No invented proof</h3><p>Every statistic carries a named source and year. No stock-photo testimonials, no fabricated reviews, no “#1” claims without basis.</p></div>
<div class="card"><span class="card-num">Performance</span><h3>Fast everywhere</h3><p>Optimized media, system fonts, no bloat. A donor on a phone in a small town gets the same experience as a sponsor on fiber.</p></div>
<div class="card"><span class="card-num">Ownership</span><h3>Yours, fully</h3><p>Domain in your name, code and content you own outright, portable to any host. No lock-in, ever.</p></div>
<div class="card"><span class="card-num">Privacy</span><h3>Plain-language policies</h3><p>Privacy, terms and cookie policies written for humans. Forms ask only for what's needed, with explicit consent.</p></div>
<div class="card"><span class="card-num">Local law</span><h3>Canadian context</h3><p>PIPEDA-aware data handling, CASL-compliant email consent, bilingual-ready structure for EN/FR content.</p></div>
</div></div></section>

<section class="final-cta"><div class="wrap">
<h2>The method is the pitch.</h2>
<p>We would rather show you a concept than send you a brochure. The formal proposal — scope, timeline, fixed quote — follows the same discipline.</p>
<a class="btn btn-light" href="contact.html">Talk to us about the RFP</a>
</div></section>'''

WORK_BODY = f'''<section class="page-hero"><div class="wrap">
<p class="eyebrow">Work &amp; standards</p>
<h1><span class="rise"><span>Proof,</span></span><span class="rise"><span>not promises.</span></span></h1>
<p class="lede fade-up d1" style="margin-top:24px">One real project, shown honestly — and open slots where {ORG}'s future case studies would live. We never invent portfolio work.</p>
</div></section>

<section style="padding-top:40px"><div class="wrap">
<div class="section-head"><p class="eyebrow">Selected work</p><h2>Built, launched, verifiable.</h2></div>
<div class="card-grid">
<div class="card"><span class="card-num">E-commerce · Live</span><h3>Blue Dhaka</h3><p>Full e-commerce website for the contemporary womenswear brand Blue Dhaka — catalog, cart and checkout, designed and built by Tiyan Digital. Visit it, click everything: <strong>bluedhaka.com</strong>.</p></div>
<div class="card" style="opacity:.75"><span class="card-num">[Placeholder]</span><h3>Your nonprofit case study</h3><p>In a production engagement this slot holds a second verifiable project with outcomes, links and client permission. We don't fabricate one for the pitch.</p></div>
<div class="card" style="opacity:.75"><span class="card-num">[Placeholder]</span><h3>Your accessibility audit</h3><p>Same rule: real audits, real before/after scores. Ask us in the proposal and we'll include recent examples.</p></div>
</div></div></section>

<section><div class="wrap">
<div class="section-head"><p class="eyebrow">Design standards</p><h2>The bar we'd hold your site to.</h2><p class="lede">Pulled from our master design practice — the same checklist behind every build we ship.</p></div>
<div class="card-grid">
<div class="card"><span class="card-num">Type &amp; layout</span><h3>Editorial discipline</h3><p>One display voice, measured line lengths, deliberate whitespace. Headlines hand-broken, never auto-wrapped into awkward breaks.</p></div>
<div class="card"><span class="card-num">Imagery</span><h3>Real faces, real rooms</h3><p>Your summit photos, your mentors, your community — never stock strangers pretending to be members. Licensed or owned assets only.</p></div>
<div class="card"><span class="card-num">Motion</span><h3>Quiet confidence</h3><p>One signature moment per page, purposeful transitions, full reduced-motion support. Motion explains; it never decorates.</p></div>
<div class="card"><span class="card-num">Content</span><h3>Written to be read</h3><p>Short pages that say one thing well beat long pages that say everything badly. SEO and AI-search structure live underneath, invisibly.</p></div>
<div class="card"><span class="card-num">Trust</span><h3>Sourced everything</h3><p>Impact numbers with sources and years. Partner logos only with permission. Policies in plain language.</p></div>
<div class="card"><span class="card-num">Craft</span><h3>Sweat the details</h3><p>Focus rings, form states, empty states, 404s, selection color. The details are where “professional” is decided.</p></div>
</div></div></section>

<section class="final-cta"><div class="wrap">
<h2>Judge us on the work.</h2>
<p>Open bluedhaka.com on your phone right now. Then imagine this level of care applied to {ORG}'s mission.</p>
<a class="btn btn-light" href="contact.html">Request the full proposal</a>
</div></section>'''

PROCESS_BODY = f'''<section class="page-hero"><div class="wrap">
<p class="eyebrow">Process</p>
<h1><span class="rise"><span>From RFP</span></span><span class="rise"><span>to launch.</span></span></h1>
<p class="lede fade-up d1" style="margin-top:24px">An indicative 10-week arc for a project like {ORG}'s rebuild. The formal proposal would fix dates against your calendar — the RFP deadline is November 20, 2026.</p>
</div></section>

<section style="padding-top:40px"><div class="wrap split">
<div><div class="steps">
<div class="step"><span class="step-n">01</span><div><span class="weeks">Weeks 1–2</span><h3>Discovery &amp; content</h3><p>Stakeholder interviews, content audit, analytics and accessibility baseline. We agree the sitemap, the CMS choice and what success looks like.</p></div></div>
<div class="step"><span class="step-n">02</span><div><span class="weeks">Weeks 3–5</span><h3>Design</h3><p>Design system, homepage and key templates, reviewed with your team in clickable prototypes. Two structured revision rounds — no endless loops.</p></div></div>
<div class="step"><span class="step-n">03</span><div><span class="weeks">Weeks 6–8</span><h3>Build</h3><p>Semantic, accessible, performant code. CMS integration, forms, newsletter, events and resource library wired up and tested.</p></div></div>
<div class="step"><span class="step-n">04</span><div><span class="weeks">Week 9</span><h3>QA &amp; accessibility audit</h3><p>Cross-device testing, WCAG 2.2 AA audit with fixes, performance budget sign-off, content entry and team training.</p></div></div>
<div class="step"><span class="step-n">05</span><div><span class="weeks">Week 10</span><h3>Launch &amp; handover</h3><p>Staged launch, analytics and search setup, documentation, and a care plan so the site stays fast and current.</p></div></div>
</div></div>
<div>
<div class="card" style="margin-bottom:24px"><span class="card-num">What we'd need from {ORG}</span><ul style="list-style:none;margin:0">
<li style="padding:8px 0;border-bottom:1px solid var(--line)">Brand assets — logo files, colors, fonts</li>
<li style="padding:8px 0;border-bottom:1px solid var(--line)">Real photography — summits, mentors, community</li>
<li style="padding:8px 0;border-bottom:1px solid var(--line)">Program copy — or we draft, you approve</li>
<li style="padding:8px 0;border-bottom:1px solid var(--line)">One decision-maker for design reviews</li>
<li style="padding:8px 0">Hosting/DNS access at launch week</li></ul></div>
<div class="card"><span class="card-num">The RFP</span><h3>November 20, 2026</h3><p>Proposals go to <strong>paige@worthassociation.com</strong> (per {ORG}'s LinkedIn post, Oct 30, 2026). We will submit a formal, fixed-quote proposal by the deadline — this concept is the preview, not the submission.</p></div>
</div></div></section>

<section class="final-cta"><div class="wrap">
<h2>Ten weeks. One team. Zero surprises.</h2>
<p>Weekly demos, fixed scope, honest timelines. That's how we'd run your rebuild.</p>
<a class="btn btn-light" href="pricing.html">See pricing guidance</a>
</div></section>'''

PRICING_BODY = f'''<section class="page-hero"><div class="wrap">
<p class="eyebrow">Pricing guidance</p>
<h1><span class="rise"><span>Honest pricing,</span></span><span class="rise"><span>in the open.</span></span></h1>
<p class="lede fade-up d1" style="margin-top:24px">Indicative tiers from our published service catalog (Oct 2026). A nonprofit's every dollar matters — so we publish ours. The formal RFP proposal would carry a fixed quote, not a range.</p>
</div></section>

<section style="padding-top:40px"><div class="wrap">
<div class="price-grid">
<div class="price-card"><p class="price-tier">Website · Basic</p><p class="price-amount">$199</p><p class="price-per">one-time</p>
<ul><li>3-page responsive website</li><li>Contact form</li><li>Social links</li><li>Basic SEO meta</li><li class="no">CMS</li><li class="no">Blog &amp; resource library</li><li class="no">Copywriting</li></ul>
<a class="btn btn-ghost" href="contact.html">Discuss</a></div>
<div class="price-card featured"><p class="price-tier">Website · Standard</p><p class="price-amount">$399</p><p class="price-per">one-time</p>
<ul><li>5–7 page multipage site</li><li>SEO basics</li><li>Blog setup</li><li>Contact + quote forms</li><li>Google Maps &amp; Analytics</li><li class="no">E-commerce</li><li class="no">Custom web apps</li></ul>
<a class="btn" href="contact.html">Discuss</a></div>
<div class="price-card"><p class="price-tier">Website · Premium</p><p class="price-amount">$899</p><p class="price-per">one-time</p>
<ul><li>10+ page custom site</li><li>Speed optimization</li><li>30-day post-launch support</li><li>Advanced SEO structure</li><li>Accessibility audit included</li><li class="no">Custom SaaS features</li><li class="no">Ongoing maintenance</li></ul>
<a class="btn btn-ghost" href="contact.html">Discuss</a></div>
</div>
<div class="placeholder-note" style="margin-top:32px"><strong>Guidance, not a quote.</strong> These are our standard catalog tiers. For an RFP of {ORG}'s scope — engaging, accessible, resource-rich, CMS-driven — the honest fit is typically Standard or Premium, quoted fixed in the proposal. Care Plan (updates, backups, small changes): <strong>$49/mo</strong>, cancel anytime.</div>
</div></section>

<section><div class="wrap split">
<div class="prose"><h2>What “resource-rich” costs to run</h2><p>A resource library, event calendar and newsletter are inexpensive to build and priceless to maintain. We price the build once and teach your team to run it — so the site doesn't quietly rot six months after launch.</p></div>
<div class="prose"><h2>No surprises, in writing</h2><p>Fixed quote before work starts. Change requests priced before they're built. You own the domain, the code and the content — in your name, from day one.</p></div>
</div></section>

<section class="final-cta"><div class="wrap">
<h2>The proposal carries the number.</h2>
<p>Transparent tiers here; a fixed, itemized quote in the formal RFP response — submitted by November 20, 2026.</p>
<a class="btn btn-light" href="contact.html">Get the formal proposal</a>
</div></section>'''

FAQ_BODY = f'''<section class="page-hero"><div class="wrap">
<p class="eyebrow">FAQ</p>
<h1><span class="rise"><span>Asked,</span></span><span class="rise"><span>answered.</span></span></h1>
<p class="lede fade-up d1" style="margin-top:24px">Straight answers about this concept, the RFP and how we'd work together.</p>
</div></section>

<section style="padding-top:40px"><div class="wrap" style="max-width:860px">
<div class="faq-item"><button class="faq-q">Is this {ORG}'s official website?</button><div class="faq-a"><p>No. This is an independent design concept built by Tiyan Digital as a pitch for {ORG}'s 2026 website RFP. It is not affiliated with or endorsed by {ORG}. All copy about the organization is drawn from its public materials, and gaps are marked [Placeholder].</p></div></div>
<div class="faq-item"><button class="faq-q">Will you actually respond to the RFP?</button><div class="faq-a"><p>Yes. The RFP asks for proposals to be sent to paige@worthassociation.com by November 20, 2026. This concept is the preview; the formal submission will include scope, timeline, team, references and a fixed quote.</p></div></div>
<div class="faq-item"><button class="faq-q">Can you meet accessibility requirements?</button><div class="faq-a"><p>Accessibility is our default, not an upsell. We build to WCAG 2.2 AA: verified color contrast, full keyboard navigation, semantic HTML, visible focus states, captions on media and a reduced-motion path — audited before launch, not after.</p></div></div>
<div class="faq-item"><button class="faq-q">Will our team be able to update the site?</button><div class="faq-a"><p>Yes. We hand over a CMS your communications team can run without a developer, plus training and documentation. If you can write an email, you can publish a program update.</p></div></div>
<div class="faq-item"><button class="faq-q">Do you write the copy too?</button><div class="faq-a"><p>We can. We draft in your voice from stakeholder interviews and public materials; your team approves every word. Nothing ships that you haven't signed off.</p></div></div>
<div class="faq-item"><button class="faq-q">What does a project like this cost?</button><div class="faq-a"><p>Our published website tiers run $199–$899 one-time, with a $49/mo care plan. An RFP of this scope — multipage, CMS-driven, accessibility-audited — would be quoted fixed in the formal proposal. No hourly billing, no surprise invoices.</p></div></div>
<div class="faq-item"><button class="faq-q">Who owns the site when it's done?</button><div class="faq-a"><p>You do — domain in your name, code and content owned outright, portable to any host. We never hold a client's domain or lock them into our infrastructure.</p></div></div>
<div class="faq-item"><button class="faq-q">Who is Tiyan Digital?</button><div class="faq-a"><p>A digital agency building websites, AI automation and chat systems. Recent verifiable work includes the full e-commerce site for Blue Dhaka (bluedhaka.com). We publish our pricing, our process and our standards — this concept is us practicing what we pitch.</p></div></div>
</div></section>

<section class="final-cta"><div class="wrap">
<h2>Still curious?</h2>
<p>Ask us anything — about the concept, the RFP, or the rebuild. We reply like humans.</p>
<a class="btn btn-light" href="contact.html">Contact us</a>
</div></section>'''

CONTACT_BODY = f'''<section class="page-hero"><div class="wrap">
<p class="eyebrow">Contact</p>
<h1><span class="rise"><span>Let's talk</span></span><span class="rise"><span>about the RFP.</span></span></h1>
<p class="lede fade-up d1" style="margin-top:24px">Questions about the concept, the formal proposal, or the rebuild itself — send them here.</p>
</div></section>

<section style="padding-top:40px"><div class="wrap split">
<div>
<form class="form-card" data-demo action="#" method="post">
<div class="field"><label for="c-name">Your name <span class="req" aria-hidden="true">*</span></label><input id="c-name" name="name" type="text" required autocomplete="name"></div>
<div class="field"><label for="c-org">Organization</label><input id="c-org" name="organization" type="text" autocomplete="organization"></div>
<div class="field"><label for="c-email">Email <span class="req" aria-hidden="true">*</span></label><input id="c-email" name="email" type="email" required autocomplete="email"></div>
<div class="field"><label for="c-msg">Message <span class="req" aria-hidden="true">*</span></label><textarea id="c-msg" name="message" rows="5" required></textarea><p class="hint">Tell us about your timeline, must-haves and anything the RFP doesn't cover.</p></div>
<div class="consent"><input id="c-consent" type="checkbox" required><p><label for="c-consent">I consent to Tiyan Digital storing my details to reply to this message. Nothing is shared or sold.</label></p></div>
<button class="btn" type="submit">Send message</button>
<p class="form-notice placeholder-note" hidden tabindex="-1"><strong>Demo form.</strong> In this concept build the form doesn't send — a production site would deliver it to the team's inbox with spam protection.</p>
</form></div>
<div>
<div class="card" style="margin-bottom:24px"><span class="card-num">The RFP</span><h3>Responding formally</h3><p style="margin-top:12px">Per {ORG}'s LinkedIn post (Oct 30, 2026): review the attached RFP and submit proposals to <strong>paige@worthassociation.com</strong> by <strong>November 20, 2026</strong>.</p></div>
<div class="card"><span class="card-num">Tiyan Digital</span><h3>The team behind the concept</h3><p style="margin-top:12px">Websites, AI automation and chat systems. See the standards we build to on the <a href="work.html" style="color:var(--accent);font-weight:600">Work &amp; Standards</a> page — and the proof at bluedhaka.com.</p></div>
</div></div></section>'''

LEGAL = {
"privacy.html": ("Privacy Policy", "How this concept site handles your data.", f'''<section class="page-hero"><div class="wrap"><p class="eyebrow">Legal</p><h1>Privacy Policy</h1></div></section>
<section style="padding-top:40px"><div class="wrap prose" style="max-width:760px">
<p><strong>Plain version:</strong> this concept site collects nothing. There is no analytics, no tracking, no cookies, no account system.</p>
<h2>Demo forms</h2><p>The newsletter and contact forms on this concept build are demonstrations — submissions are not transmitted, stored or processed anywhere. A production site would connect them to the organization's email platform, with the consent stated beside each form.</p>
<h2>What a production site would do</h2><p>For {ORG}'s real rebuild, we would publish a full policy covering: what data forms collect and why, email consent under Canada's CASL, analytics (if any) with opt-out, data retention, and how to request deletion — in plain language, before launch.</p>
<h2>Contact</h2><p>Questions about this policy: use the <a href="contact.html">contact page</a>.</p>
<p style="color:var(--muted);font-size:14px">Last updated: November 2026.</p></div></section>'''),
"terms.html": ("Terms & Conditions", "The ground rules for this concept site.", f'''<section class="page-hero"><div class="wrap"><p class="eyebrow">Legal</p><h1>Terms &amp; Conditions</h1></div></section>
<section style="padding-top:40px"><div class="wrap prose" style="max-width:760px">
<h2>What this site is</h2><p>An independent design concept created by Tiyan Digital as a pitch for {ORG}'s 2026 website RFP. It is not the official website of {ORG}, and is not affiliated with or endorsed by them.</p>
<h2>Content</h2><p>Descriptions of {ORG} are drawn from the organization's public materials and are marked [Placeholder] where facts were unavailable. Nothing here constitutes an official statement by {ORG}.</p>
<h2>Use</h2><p>You may browse and share this concept freely. The design and code are the work of Tiyan Digital; the {ORG} name, programs and quotes referenced belong to their respective owners and are used here for pitch purposes only.</p>
<p style="color:var(--muted);font-size:14px">Last updated: November 2026.</p></div></section>'''),
"cookies.html": ("Cookie Policy", "Do we use cookies? No.", f'''<section class="page-hero"><div class="wrap"><p class="eyebrow">Legal</p><h1>Cookie Policy</h1></div></section>
<section style="padding-top:40px"><div class="wrap prose" style="max-width:760px">
<p><strong>Short version: this concept site uses no cookies and no trackers.</strong> There is nothing to consent to and no banner to dismiss.</p>
<h2>A production site</h2><p>{ORG}'s real rebuild would use minimal, disclosed cookies at most (e.g. remembering a preference) — with a proper consent banner and this page updated to list each one, its purpose and its expiry.</p>
<p style="color:var(--muted);font-size:14px">Last updated: November 2026.</p></div></section>'''),
}

PAGES = [
    ("index.html", f"Home — {ORG} Website Concept (2026 RFP)", f"An independent website design concept by Tiyan Digital for {ORG}'s 2026 RFP — warm, editorial, accessible. Move the dial for women in recreation, tourism and hospitality.", "index.html", HOME_BODY),
    ("about.html", f"About {ORG} — Website Concept", f"What {ORG} is: a Canadian non-profit advancing equity for women across recreation, tourism and hospitality. From public sources.", "about.html", ABOUT_BODY),
    ("method.html", "Our Method — Tiyan Digital", "Psychology first, then design, then code. The process behind the WORTH concept — and the process we'd bring to the rebuild.", "method.html", METHOD_BODY),
    ("work.html", "Work & Standards — Tiyan Digital", "Proof, not promises: verifiable work including bluedhaka.com, and the design standards we'd hold the rebuild to.", "work.html", WORK_BODY),
    ("process.html", "Process — From RFP to Launch", "An indicative 10-week arc from RFP response to launch for the WORTH Association website rebuild.", "process.html", PROCESS_BODY),
    ("pricing.html", "Pricing Guidance — Tiyan Digital", "Honest, published pricing tiers for the website rebuild. Indicative guidance; the formal RFP proposal carries a fixed quote.", "pricing.html", PRICING_BODY),
    ("faq.html", "FAQ — WORTH Website Concept", "Straight answers about the concept, the RFP, accessibility, pricing and ownership.", "faq.html", FAQ_BODY),
    ("contact.html", "Contact — Talk About the RFP", "Contact Tiyan Digital about the WORTH Association 2026 website RFP.", "contact.html", CONTACT_BODY),
]

def main():
    for fname, title, desc, current, body in PAGES:
        page(fname, title, desc, current, body)
    for fname, (title, desc, body) in LEGAL.items():
        page(fname, f"{title} — {ORG} Concept", desc, "", body)
    # 404
    page("404.html", "Page not found — WORTH Concept", "This page doesn't exist in the concept.", "",
         '''<section class="page-hero center"><div class="wrap"><p class="eyebrow">404</p><h1>Lost your way?</h1><p class="lede" style="margin:24px auto;max-width:52ch">This page doesn't exist in the concept. The dial, however, still points forward.</p><a class="btn" href="index.html">Back to home</a></div></section>''')
    # robots + sitemap (placeholder domain — replace on deploy)
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: https://https://worth-association-proposal.vercel.app/sitemap.xml\n")
    urls = ["", "about.html", "method.html", "work.html", "process.html", "pricing.html", "faq.html", "contact.html", "privacy.html", "terms.html", "cookies.html"]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f'  <url><loc>https://https://worth-association-proposal.vercel.app/{u}</loc><changefreq>monthly</changefreq></url>')
    sm.append('</urlset>')
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write("\n".join(sm) + "\n")
    print("generated", len(PAGES) + len(LEGAL) + 1, "pages")

if __name__ == "__main__":
    main()
