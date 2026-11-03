# DESIGN.md — WORTH Association RFP Pitch Site (concept)

## Project
A multipage design-concept pitch site for WORTH Association's 2026 "Website Design & Development partner" RFP, built by Tiyan Digital as an independent concept demonstration — not an official WORTH site. Vercel-ready static HTML/CSS/JS.

## Overview
WORTH Association = Women of Recreation, Tourism & Hospitality, a Canadian non-profit society (incorporated 2018, BC) working to advance equity across the visitor economy. Their RFP (LinkedIn, 2026-10-30, deadline 2026-11-20, contact paige@worthassociation.com) asks for "a more engaging, accessible, and resource-rich digital experience."

## Psychology brief
- **Visitor:** WORTH's RFP evaluation committee + their community (women in recreation/tourism/hospitality, partners, sponsors).
- **Pain:** current site feels dated and thin; the RFP wants a partner who can make their digital presence worthy of the mission.
- **One action:** committee members should think "this team gets nonprofits like ours" and email a reply / request the formal proposal.
- **Trust gap:** will this partner understand a women's nonprofit, accessibility, and honest impact storytelling — without inventing claims?
- **Emotion:** warm, confident, professional — leadership taken seriously.

## Mood (three words)
Warm · Editorial · Assured

## Signature idea
**"The Dial."** WORTH's own language is "move the dial for equality." The hero carries an SVG dial/gauge whose needle sweeps on load (scroll-triggered on the impact section), and section numerals are oversized ghost numerals. One memorable moment per page, everything else quiet.

## Tokens
| Token | Value |
|---|---|
| `--bg` | `#FAF5EE` warm paper |
| `--surface` | `#F1E7D8` warm sand |
| `--ink` | `#201812` warm near-black |
| `--muted` | `#6B5E50` warm grey |
| `--line` | `rgba(32,24,18,.14)` hairlines |
| `--accent` | `#B23E2B` rosewood terracotta — CTAs, labels, active nav only |
| `--accent-deep` | `#8E2F20` hover state |

Accent appears on at most 3 element types (CTA buttons, eyebrow labels, active states). No gradients, no glow, no blobs. Depth via hairlines + surface steps only.

## Typography
- **Display:** Georgia, 'Palatino Linotype', 'Times New Roman', serif — H1 `clamp(44px,8vw,96px)`, line-height 0.95, tracking −0.03em, hand-broken to 2–3 lines.
- **Body:** system-ui, -apple-system, 'Segoe UI', sans-serif — 17px, line-height 1.65, measure ≤ 70ch.
- **Labels:** ui-monospace, 'SF Mono', Menlo, monospace — 11–12px, uppercase, +0.18em tracking, 60% opacity.
- Max 2 families + 1 mono. Fonts are system stacks — fully offline-safe, zero third-party loads.

## Layout ideas
- Asymmetric editorial hero: left column (eyebrow → H1 → sub → CTAs), right plane (SVG dial art, oversized 112%).
- Numbered editorial program rows (01–05) with hairline dividers — not icon cards.
- Impact band: dark ink section, count-up numbers, every number with a named source + year.
- Marquee strip of the three pillars: EDUCATE — ELEVATE — ENGAGE.
- **Phone is a second composition:** 16–20px margins, single column, dial art stacks below headline.

## Motion
- One timeline per page: eyebrow → H1 (masked line rise, 100ms stagger) → sub → CTAs, 0.8s, cubic-bezier(0.16,1,0.3,1), done by ~1.5s.
- Needle sweep + count-ups trigger on IntersectionObserver, run once, to completion.
- `prefers-reduced-motion`: everything visible, no animation. If JS fails, content is fully readable (no opacity-0 initial states in CSS).

## Copy rules
- H1s: 3–9 words, two-beat statements ("Move the dial / for women in tourism.").
- Every claim is either a public fact (sourced) or marked **[Placeholder]** / "concept".
- Concept banner on every page: "Independent design concept by Tiyan Digital for WORTH Association's 2026 website RFP."

## Verified facts used (sources)
- WORTH = Women of Recreation, Tourism & Hospitality; Canadian non-profit society; incorporated 2018 (worthassociation.com/about-us).
- Purpose/pillars: educate, elevate, engage (worthassociation.com).
- Programs: WORTH Academy, mentorship, Leadership Summits, WORTH-shops, scholarships, advocacy/research (worthassociation.com, worthsummit.ca).
- ~5,000 women reached via advocacy, events and resources (4VI "Women of WORTH" report, 2023, citing WORTH).
- "Nearly 100 women" elevated through the mentorship program (worthassociation.com blog, 2025).
- Founder: Joanna Jagger, Executive Director & founder (worthassociation.com).
- Partners named publicly: TOTA, BCHA, go2HR (worthassociation.com blog, 2025).
- Territory acknowledgment: Coast Salish peoples — Musqueam, Stó:lō, Squamish, Tsleil-Waututh (worthassociation.com).
- RFP: LinkedIn post 2026-10-30, proposals to paige@worthassociation.com by 2026-11-20.
- Quote: Joanna Jagger, STAY Magazine 2025 — attributed verbatim.

## Known gaps
- Photography is abstract SVG (no licensed photos of WORTH's community; their photos are copyrighted). A production build would use WORTH's real assets.
- Sitemap uses a placeholder domain — replace with the live demo URL on deploy.
- Contact/newsletter forms are demo-only (no backend); marked as such.
- Board/staff, financials, annual reports are [Placeholder] slots, not facts.
