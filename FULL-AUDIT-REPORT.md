# SEO Full Audit Report — M-Smith Advocates
**URL:** https://www.m-smithadvocates.com
**Date:** May 2026
**Business Type:** Local Service — Law Firm (Kampala, Uganda; offices in Nairobi & Mombasa)
**Pages Audited:** 19 HTML files (all pages on disk)

---

## Overall SEO Health Score: 74 / 100

| Category | Weight | Score | Notes |
|---|---|---|---|
| Technical SEO | 22% | 70/100 | 3 undeployed pages, missing CSP, 3x H1 on homepage |
| Content Quality | 23% | 78/100 | Strong practice pages; contact/team pages thin |
| On-Page SEO | 20% | 68/100 | Title overflow, no analytics, stale "11" count on live |
| Schema / Structured Data | 10% | 82/100 | Solid per-page schema; missing Person/LocalBusiness |
| Performance (CWV) | 10% | 72/100 | Async fonts + preloaded hero good; no field data |
| AI Search Readiness | 10% | 91/100 | Excellent llms.txt, AI bot access, structured facts |
| Images | 5% | 98/100 | All alt text present, WebP throughout |

---

## Executive Summary

M-Smith Advocates has a well-structured site with strong content depth, solid schema implementation, and exceptional AI/GEO readiness. The biggest immediate risk is **three pages that are 404 on the live server** (family-law, nairobi, mombasa) — these are already linked from the homepage, creating broken user journeys today. Beyond that, the site has no analytics tracking, the homepage title exceeds the 60-character SERP limit, and there are three H1 tags on the homepage. AI search readiness is the site's standout strength, ahead of most law firms in the region.

### Top 5 Critical Issues
1. family-law, nairobi, and mombasa are 404 on the live site but linked from multiple pages
2. No Google Analytics or Tag Manager — zero organic traffic visibility
3. Homepage has 3 H1 tags (only the first is used by Google; the rest dilute signal)
4. Homepage title is 74 characters — truncated in SERPs (limit ~60)
5. Live homepage still shows "11 Practice Areas" (corrected locally, not yet deployed)

### Top 5 Quick Wins
1. Deploy pending files (family-law, nairobi, mombasa, updated sitemap, index.html)
2. Add Google Analytics 4 + verify Google Search Console
3. Trim homepage title to 60 characters or fewer
4. Remove duplicate H1s from homepage, keep one
5. Add Person schema to team.html for each advocate

---

## 1. Technical SEO

### Crawlability & Indexability

**robots.txt** is excellent. Explicitly allows all major AI crawlers: Google-Extended, GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot, Applebot-Extended. Disallows /terms, /disclaimer, /claude-seo/. References sitemap.

**Sitemap (live server):** 16 URLs. family-law, nairobi, mombasa are missing — the updated sitemap.xml has not been deployed.
**Sitemap (local disk):** 19 URLs including all three new pages. lastmod: 2026-05-22 on all entries. No changefreq or priority (acceptable).
**404 Pages:** family-law, nairobi, and mombasa all return HTTP 404 on the live server despite being linked from index.html, practice-areas.html, and about.html.

### Security Headers

| Header | Status |
|---|---|
| HTTPS + HSTS (max-age=31536000; includeSubDomains) | PASS |
| X-Frame-Options: SAMEORIGIN | PASS |
| X-Content-Type-Options: nosniff | PASS |
| Referrer-Policy: strict-origin-when-cross-origin | PASS |
| Permissions-Policy | PASS |
| Content-Security-Policy | MISSING |

Server: Apache. No X-Powered-By header exposed. Good.

### Canonical URLs
All pages carry self-referencing canonical tags. Correct.

### URL Structure
Clean slugs (/real-estate, /immigration). No query strings, no inconsistent trailing slashes.

### Font Loading
All main HTML files now use async font preloading with noscript fallback — eliminates render-blocking.

---

## 2. Content Quality (E-E-A-T)

### Word Counts by Page

| Page | Words | Status |
|---|---|---|
| index.html | ~3,900 | Good |
| real-estate.html | ~3,200 | Excellent |
| immigration.html | ~2,600 | Excellent |
| family-law.html | ~2,200 | Good (not yet live) |
| eac-law.html | ~2,200 | Good |
| corporate-commercial.html | ~2,200 | Good |
| employment-labour.html | ~2,000 | Good |
| mining-minerals.html | ~1,800 | Adequate |
| human-rights.html | ~1,800 | Adequate |
| intellectual-property.html | ~1,800 | Adequate |
| litigation-arbitration.html | ~1,700 | Adequate |
| oil-gas-petroleum.html | ~1,700 | Adequate |
| insurance.html | ~1,600 | Adequate |
| about.html | ~1,600 | Adequate |
| team.html | ~1,100 | Thin — no full bios |
| nairobi.html | ~1,050 | Thin (not yet live) |
| practice-areas.html | ~1,100 | Index page, acceptable |
| mombasa.html | ~891 | Thin (not yet live) |
| contact.html | ~490 | Very thin |

### E-E-A-T Signals

**Strengths:**
- Advocate credentials stated (LLB MUK, Dip. LDC, Uganda Law Council enrolment)
- Verifiable case outcomes: UGX 2.4 billion fraud case, Misc. Cause 277/2018, UGX 680 million debt recovery
- Regulatory memberships: Uganda Law Council, Uganda Law Society, East African Law Society, Uganda Bar Association
- Directory listings: FindLegal Africa, Lawzana, ULII, Uganda Law Council Approved Firms Register
- AML/FIA compliance and Data Protection Act 2019 compliance stated
- Founded 2013 — 12+ years operational track record

**Gaps:**
- team.html has advocate names and specialisms but no detailed individual bios (education, notable cases, publications)
- No client testimonials with schema markup
- No blog or educational content hub — significant authority-building gap
- No dedicated case study pages (outcomes buried in homepage text)

---

## 3. On-Page SEO

### Title Tags

| Page | Characters | Issue |
|---|---|---|
| index.html | 74 | Over limit — truncated in SERPs |
| insurance.html | 59 | Marginal |
| All other pages | 37-58 | OK |

**Current homepage title:** "M-Smith Advocates | Corporate, Property & Litigation Lawyers in Uganda"
**Recommended:** "M-Smith Advocates | Lawyers in Kampala, Uganda" (47 chars)

### Meta Descriptions
All pages: 143-155 characters. Within the ~155 character safe zone. Location keywords present. OK.

### H1 Tags
- **index.html: 3 H1 tags.** The three are: "Trusted Legal Solutions for Individuals, Businesses & Institutions" / "Uganda's Advocates for Business, Property & Justice" / "Your Trusted Legal Partner". Google treats the first as the primary heading; the others should be H2.
- All other pages: exactly 1 H1 each. OK.

### Meta Keywords Tag
All pages still include `<meta name="keywords">`. This tag has been ignored by Google since 2009 and adds no value. Remove from all pages.

### Analytics & Tracking
**Zero.** No Google Analytics 4, no Google Tag Manager, no heatmap tool detected on any page. There is no way to measure organic traffic, track form completions, or understand which practice area pages generate enquiries.

### Stale Live Content
The deployed homepage shows "11 Practice Areas" in three places (hero stats, outcomes strip, CTA link). The corrected index.html (with "12") exists locally and needs to be deployed.

---

## 4. Schema / Structured Data

### Architecture
Every page uses a single JSON-LD `@graph` block. Clean, parseable, no inline schema mixed with HTML.

| Page | Schema Types |
|---|---|
| Homepage | LegalService, WebSite, WebPage, FAQPage |
| About | LegalService, BreadcrumbList |
| Practice area pages | LegalService, BreadcrumbList, FAQPage, Service, WebPage |
| Contact | LegalService, ContactPage, BreadcrumbList |
| Team | LegalService, BreadcrumbList |

### Gaps

**No explicit LocalBusiness node.** Google's local knowledge panel and local pack rely on `LocalBusiness` (or its subtype `LegalService`) with `address`, `geo` (lat/lng), `openingHours`, and optionally `hasMap`. The current `LegalService` schema does not inherit `LocalBusiness` explicitly. Adding this to the homepage and contact page improves local pack eligibility.

**No Person schema on team.html.** Each advocate should have `Person` schema with `name`, `jobTitle`, `alumniOf`, `memberOf` fields. This tells AI engines and Google exactly who the firm's experts are and in what fields.

**No Review / AggregateRating schema.** If the firm has Google reviews, these can surface star ratings directly in SERPs with appropriate markup.

**No SiteLinksSearchBox** on the homepage (minor — only relevant for large branded traffic).

---

## 5. Performance (Core Web Vitals)

*No CrUX field data available (no Google Search Console connected). Lab-based assessment only.*

### Strengths
- Hero image uses `<link rel="preload" as="image" fetchpriority="high">` — directly improves LCP
- WebP images throughout — efficient file sizes
- Async font loading eliminates render-blocking; noscript fallback present
- HTTPS with no mixed content detected

### Risk Areas
- **Google Fonts external dependency.** Even with async loading, the browser must open a connection to fonts.googleapis.com and fonts.gstatic.com on each first visit. Self-hosting the four font families would remove this latency entirely.
- **No CDN detected.** The site is served from an Apache origin. A CDN (Cloudflare free tier) would reduce TTFB for visitors in Nairobi, Mombasa, and other East African locations outside Kampala.
- **Below-fold lazy loading.** Could not verify without full rendering, but images not in the initial viewport should carry `loading="lazy"`.

---

## 6. AI Search Readiness (GEO)

**Score: 91/100 — the site's strongest area.**

| Signal | Status |
|---|---|
| llms.txt present, well-structured, CC0 licensed | PASS |
| All major AI bots explicitly allowed in robots.txt | PASS |
| Factual, citable content with specific figures | PASS |
| JSON-LD schema on every page | PASS |
| Server-rendered HTML (no JS-gated content) | PASS |
| Practice pages directly answer "Who handles X in Uganda?" | PASS |
| llms.txt referenced in robots.txt | PASS |
| llms.txt updated to 12 practice areas | PASS |

### Why This Matters
When someone asks ChatGPT, Perplexity, or Google AI Overviews "best immigration lawyers in Kampala" or "law firm for work permits Uganda", a well-structured llms.txt + schema + citable facts significantly increases the likelihood of being cited. M-Smith is well positioned here.

### Minor Gaps
- No `llms-full.txt` — a full-text companion file improves AI retrieval for complex multi-topic queries
- Nairobi and Mombasa offices not yet in llms.txt — add after those pages go live
- No outbound links to source legislation (Uganda Land Act, Advocates Act, etc.) — external citations add authority signals for AI fact-checking

---

## 7. Local SEO

### NAP Consistency
Consistent across all pages:
- Kampala: Tirupati Mazima Mall, Kabalagala — +(256) 782 776 074
- Nairobi: Ruprani House, 3rd Floor, Suite 317 — +254 720 124 592
- Mombasa: NSSF House, 7th Floor — +254 708 990 273

### Location Pages
- nairobi.html (~1,047 words) and mombasa.html (~891 words) exist locally but are 404 on the live server
- nairobi.html meta description is 163 characters — 8 characters over the safe 155-character limit

### Gaps
- No Google Business Profile link or verification badge on the site
- No embedded Google Map on contact.html (text link only — "Get Directions")
- No Review/AggregateRating schema — star ratings in SERPs require this
- mombasa.html at ~891 words is thin — expand with Mombasa-specific legal context before deploying
- No Kampala neighborhood landing pages for hyper-local search (Kabalagala, Kololo, Nakasero)

---

## 8. Images

**100% of images across all 17 pages have descriptive alt text.** WebP format used consistently. OG images reference logo.png (file exists on server). No oversized images detected from local file inspection.

**Opportunity:** Every page shares the same OG image (logo.png). Practice-area-specific OG images would improve social media click-through rates and recognition when links are shared on LinkedIn, WhatsApp, or X.

---

## 9. Sitemap

| Item | Status |
|---|---|
| Referenced in robots.txt | PASS |
| Accessible via HTTPS | PASS |
| Live URL count | 16 (3 new pages missing) |
| Local URL count | 19 (correct) |
| lastmod format | Valid (2026-05-22) |
| changefreq | Not set (acceptable) |
| Legal/utility pages correctly excluded | PASS |

---

## 10. Internal Linking

- Practice area pages cross-link to each other. Good.
- Homepage links to all 12 practice areas including family-law — which is currently 404.
- nairobi.html and mombasa.html not linked from main navigation or footer; reachable only via sitemap.
- BreadcrumbList schema present on all inner pages but no visible breadcrumb UI — a visual breadcrumb bar would aid navigation and reinforce the schema.
