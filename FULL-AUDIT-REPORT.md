# M-Smith Advocates — Full SEO Audit Report

**Site:** https://www.m-smithadvocates.com
**Audit Date:** May 2026
**Prepared by:** SEO Audit System

---

## OVERALL SEO HEALTH SCORE: 70 / 100

| Category | Weight | Score | Weighted |
|---|---|---|---|
| Technical SEO | 22% | 72/100 | 15.8 |
| Content Quality | 23% | 71/100 | 16.3 |
| On-Page SEO | 20% | 65/100 | 13.0 |
| Schema / Structured Data | 10% | 72/100 | 7.2 |
| Performance / CWV | 10% | 68/100 | 6.8 |
| AI Search Readiness | 10% | 71/100 | 7.1 |
| Images | 5% | 78/100 | 3.9 |
| **TOTAL** | **100%** | | **70.1** |

---

## SECTION 1: EXECUTIVE SUMMARY

**Site overview:** https://www.m-smithadvocates.com — Ugandan law firm, 19 pages, static HTML, Bluehost Apache.

### Top 5 Critical Issues

1. **Kampala address conflict** — website shows Tirupati Mazima Mall, Kabalagala but client brief says Plot 7 Mackinnon Road, Nakasero — this NAP conflict with GBP is actively suppressing local pack rankings.
2. **Geo coordinates inconsistent** — index.html uses (0.27450, 32.60120) and contact.html uses (0.299999, 32.596541) — two different map pins for the same office.
3. **13 of 16 title tags exceed 60 characters** — Google is rewriting the majority of titles in SERPs.
4. **sameAs property completely absent from all LegalService schema blocks** — Google cannot verify entity identity across sources.
5. **9 of 11 practice area pages are thin content (under 900 words)** for YMYL legal services.

### Top 5 Quick Wins

1. Fix title tags across 13 pages — 30-minute batch edit, immediate SERP impact.
2. Add sameAs to homepage LegalService schema with GBP URL and LinkedIn.
3. Unify geo coordinates to one confirmed set across all pages.
4. Add og:image to 5 pages missing it (/about, /practice-areas, /team, /contact, /real-estate).
5. Update robots.txt to explicitly allow GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot.

---

## SECTION 2: TECHNICAL SEO

**Score: 72/100**

| Check | Status | Notes |
|---|---|---|
| HTTPS | PASS | All canonical URLs use https:// |
| robots.txt | PASS with issues | See below |
| Sitemap | PASS with issues | See below |
| Canonicals | PASS | All 19 pages have correct self-referencing canonicals |
| Redirects | PASS | .htaccess handles extensionless URL rewrites and .html redirects |
| Mobile | PASS | Viewport meta present; responsive CSS with breakpoints at 320px, 375px, 480px, 580px, 768px, 900px, 1024px |
| Security | PARTIAL | HTTPS confirmed; X-Content-Type-Options present; no CSP header detected |
| Crawl depth | PASS | All pages at depth 1 from homepage |
| hreflang | NOT IMPLEMENTED | Not required yet (single English site); needed if Kenya-specific pages are created |
| lang attribute | PASS | lang="en" on all html elements |

**robots.txt detail:**
- Wildcard Allow: / present
- Google-Extended explicitly allowed
- GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot NOT explicitly configured — fix needed
- /privacy-policy, /terms, /disclaimer blocked from all crawlers — should be unblocked for AI crawlers as they contain E-E-A-T trust signals

**Sitemap detail:**
- 16 URLs (correctly excludes 3 noindexed pages)
- lastmod dates are batch-stamped — adopt per-page dates going forward
- Trailing slash on homepage only — internally consistent

---

## SECTION 3: CONTENT QUALITY & E-E-A-T

**Score: 71/100**

### E-E-A-T Breakdown

| Dimension | Score |
|---|---|
| Experience | 14/20 |
| Expertise | 18/25 |
| Authoritativeness | 17/25 |
| Trustworthiness | 22/30 |
| **Total** | **71/100** |

### Thin Content Pages (under 900 words — YMYL risk)

| Page | Word Count |
|---|---|
| corporate-commercial | ~520w |
| litigation-arbitration | ~530w |
| insurance | ~530w |
| human-rights | ~540w |
| eac-law | ~570w |
| oil-gas-petroleum | ~580w |
| mining-minerals | ~580w |
| intellectual-property | ~590w |
| employment-labour | ~560w |

9 of 11 practice area pages fail the YMYL minimum threshold of 900 words.

### Strong Pages (set the standard)

- real-estate (~1,100w)
- immigration (~1,050w)

### Key Gaps

- No blog, no case study pages, no publication dates on any page.
- 6 verified matter outcomes in llms.txt are NOT published on the corresponding practice area pages — the UGX 2.4B real estate fraud case is the only outcome published on the site.
- No inline "this is not legal advice" notice on practice area pages.
- Aggregate rating schema uses unverified testimonials not linked to GBP or any third-party review platform.
- No year of enrollment to Roll of Advocates for any team member — this is the most fixable credential gap.

### AI Citation Readiness: 63/100

- llms.txt is excellent
- Site lacks dated informational content — the biggest single gap for AI citation

---

## SECTION 4: ON-PAGE SEO

**Score: 65/100**

### Title Tags

**Status: 2 pass, 13 fail, 1 borderline** — Google is rewriting most titles.

Recommended fixed titles:

| Page | Proposed Title | Characters |
|---|---|---|
| /about | About M-Smith Advocates \| Law Firm in Uganda | 44 |
| /practice-areas | Legal Services in Uganda \| M-Smith Advocates | 45 |
| /team | Lawyers in Kampala, Uganda \| M-Smith Advocates | 47 |
| /contact | Contact M-Smith Advocates \| Lawyers in Kampala | 47 |
| /litigation-arbitration | Litigation & Arbitration Lawyers Uganda \| M-Smith | 50 |
| /real-estate | Real Estate Lawyers Uganda \| M-Smith Advocates | 47 |
| /intellectual-property | Intellectual Property Lawyers Uganda \| M-Smith | 47 |
| /oil-gas-petroleum | Oil & Gas Lawyers in Uganda \| M-Smith Advocates | 48 |
| /mining-minerals | Mining & Minerals Lawyers Uganda \| M-Smith | 43 |
| /employment-labour | Employment & Labour Lawyers Uganda \| M-Smith | 45 |
| /corporate-commercial | Corporate & Commercial Lawyers Uganda \| M-Smith | 48 |
| /immigration | Immigration Lawyers Uganda \| M-Smith Advocates | 47 |
| /human-rights | Human Rights Lawyers in Uganda \| M-Smith | 41 |
| /eac-law | EAC Law Lawyers Uganda \| M-Smith Advocates | 43 |

### Meta Descriptions

**Status: 7 pass, 9 fail** — all failures are minor 2–9 character overruns; all descriptions are unique and compelling.

### Headings

- About page H1 is "Who We Are" — weak, no keyword; must be fixed.
- All other H1s are strong.
- All practice area pages follow a clean H1/H2/H3 hierarchy.

### Internal Links

- Full mesh between practice area pages via sidebar — PASS.
- About page body text does not link to any practice areas — add 3–4 links.

### Open Graph

- 5 pages missing og:image: /about, /practice-areas, /team, /contact, /real-estate.

### Twitter Cards

- All pages use `summary` instead of `summary_large_image`.
- twitter:image absent on most pages.

### Image Alt Text

- 95%+ coverage — PASS.
- One mislabeled filename: insurance image used for oil/gas card.

### URL Structure

- Extensionless, lowercase, hyphenated, top-level — PASS.

---

## SECTION 5: SCHEMA & STRUCTURED DATA

**Score: 72/100**

### Critical Issues

1. **Geo coordinates inconsistent:** index.html (0.27450, 32.60120) vs contact.html (0.299999, 32.596541) — same @id, conflicting values.
2. **real-estate FAQPage missing @id** — add `"https://www.m-smithadvocates.com/real-estate#faq"`.
3. **ContactPage.isPartOf points to #organization (wrong)** — must point to #website; add `"about": {"@id": "#organization"}`.
4. **sameAs completely absent from all LegalService blocks** — critical entity disambiguation gap.
5. **AggregateRating reviewCount is "6" (string) but only 3 Review objects exist** — fix count to 3 and use integers, not strings.

### Warnings

6. ItemList on practice-areas.html uses `"url"` instead of `"item"` in ListItem.
7. Review objects have no datePublished.
8. Person entities on team.html missing `"image"` and `"description"`.
9. Maweu Christopher Kituu hasCredential missing `"recognizedBy"` on MPPM and BASS credentials.
10. SearchAction urlTemplate may not resolve to a working search — verify or remove potentialAction.

### Enhancements

11. Add WebPage entity to about.html.
12. Add ProfilePage entity to team.html.
13. Add memberOf (Uganda Law Society) to each Person entity.
14. Add speakable schema to FAQ answers and overview paragraphs.
15. Add legalServiceType property to Service schema on practice pages.

### FAQPage Status

Present on: immigration, real-estate, corporate-commercial, litigation-arbitration.
Absent from: 7 practice area pages that have FAQ content — add FAQPage JSON-LD to all 11.

> Note: FAQPage will NOT generate Google accordion rich results for commercial sites (Aug 2023 restriction) — retain for AI/LLM citation value only.

---

## SECTION 6: PERFORMANCE / CORE WEB VITALS

**Score: 68/100**

### Already Optimized (this session)

- 37 images converted to WebP (avg 90–99% size reduction: 7MB → 54KB for activedia, 3.3MB → 25KB for real estate).
- loading="lazy" on 27 below-fold images.
- Google Fonts non-blocking via preload + onload swap.
- script.js deferred.
- hero-bg.png preloaded with fetchpriority="high".

### Remaining Issues

| Issue | Priority | Estimated Gain |
|---|---|---|
| TTFB likely 300–600ms on Bluehost shared hosting | High | Upgrade to VPS or Cloudflare free tier |
| No gzip/brotli compression confirmed | High | Add mod_deflate to .htaccess |
| No browser caching headers confirmed | High | Add Cache-Control to .htaccess for static assets |
| CSS is 76KB unminified | Medium | Minification saves ~15–20KB |
| styles.css and script.js have no versioned filenames | Medium | Add ?v= cache busting |
| No critical CSS inlining | Low | Inline above-fold styles to eliminate render-blocking CSS request |

---

## SECTION 7: LOCAL SEO

**Score: 47/100**

### Critical Issues

1. **Kampala address conflict:** website shows Tirupati Mazima Mall, Kabalagala; client brief states Plot 7 Mackinnon Road, Nakasero — must verify and unify across website, GBP, and all citations.
2. **No /nairobi or /mombasa landing pages** — Kenya offices are invisible to local search.
3. **No confirmed separate GBP listings** for Nairobi or Mombasa offices.
4. **sameAs completely missing** — Google cannot verify NAP consistency against external sources.

### High Priority Issues

5. Geo coordinate conflict (see Schema section).
6. aggregateRating reviewCount discrepancy (see Schema section).
7. Uganda Law Society + Law Society of Kenya directory listings unconfirmed.
8. Kenya-specific content: zero pages target Nairobi/Mombasa/Kenya keywords.
9. No review generation strategy visible; 6 testimonials are unverified (not from GBP).

### GBP Status

| Office | Status |
|---|---|
| Kampala | GBP exists — confirmed by embed Place ID 0x177dbc682aec96db:0x1642c7c722d128ac |
| Nairobi | Unknown — no embed or Place ID found in code |
| Mombasa | Unknown — no embed or Place ID found in code |

> GBP primary category cannot be confirmed remotely — must be set to "Law Firm" not "Lawyer".

---

## SECTION 8: AI SEARCH READINESS / GEO

**Score: 71/100**

### Strengths

- **llms.txt: 74/100** — best-in-class for an East African law firm; factually dense; includes 6 verified case outcomes with court references and UGX figures; all 11 practice areas deep-linked.
- **Static HTML: 95/100 technical accessibility** — all content in DOM, no JS-rendered text.
- FAQPage schema on 4 pages with jurisdiction-specific answers.
- Statute citations throughout (Land Act Cap 227, Employment Act 2006, Advocates Act Cap 267, etc.).

### Gaps

- No blog / informational articles — biggest single gap; AI systems cannot cite service pages for how-to queries.
- No outbound links to authoritative sources (ulii.org, ursb.go.ug, mia.go.ug) — zero outbound citation links on any page.
- FAQ answers in `<details>`/`<summary>` on real-estate hide content from non-JS parsers.
- No speakable schema.
- No RSL 1.0 license declaration in llms.txt.
- llms.txt missing last-updated date and advocate-to-practice mapping.
- OAI-SearchBot, ClaudeBot, PerplexityBot not explicitly in robots.txt.
- External entity corroboration: no Wikipedia, no linked ULII case record, no LinkedIn profiles linked.

### Platform Scores

| Platform | Score |
|---|---|
| Google AI Overviews | 58/100 |
| ChatGPT Web Search | 44/100 |
| Perplexity | 52/100 |
| Bing Copilot | 61/100 |

---

## SECTION 9: BACKLINKS & DOMAIN AUTHORITY

- **Estimated referring domains:** <10 (below competitive ranking threshold)
- **Confirmed citations:** ULII (mentioned, not linked), Lawzana, FindLegal Africa, Uganda Law Council Approved Firms Register
- **Unconfirmed / missing:** Chambers Africa, Legal 500, IFLR1000, Justia, Avvo, FindLaw
- **No sameAs** in schema linking to any external directory
- **Competitor gap:** established Ugandan firms (MMAKS, KAA, AF Mpanga) estimated at 60–150 referring domains

### Top 20 Citation Targets (Prioritized)

| # | Target | Domain Authority | Notes |
|---|---|---|---|
| 1 | Google Business Profile — Kampala | — | CRITICAL |
| 2 | Google Business Profile — Nairobi | — | CRITICAL |
| 3 | LinkedIn Company Page | DA 98 | |
| 4 | Uganda Law Society directory | DA ~40 | Most relevant local citation |
| 5 | Justia international directory | DA 87 | |
| 6 | FindLaw directory | DA 85 | |
| 7 | Martindale-Hubbell | DA 82 | |
| 8 | Avvo — firm + individual attorney profiles | DA 80 | |
| 9 | Africa Legal | DA ~50 | Regional authority |
| 10 | LawInfo | DA 72 | |
| 11 | HG.org | DA 68 | |
| 12 | Kenya Law Society / LSK directory | DA ~45 | |
| 13 | Chambers & Partners Africa | Editorial | 12–18 month process |
| 14 | Legal 500 Sub-Saharan Africa | Editorial | 12–18 month process |
| 15 | IFLR1000 | Editorial | Strong fit for oil/gas, mining |
| 16 | Kompass Uganda | DA 65 | B2B directory |
| 17 | Uganda Yellow Pages | DA ~30 | |
| 18 | Kenya Yellow Pages | DA ~35 | |
| 19 | Yelp | DA 94 | Brand signal |
| 20 | Thomson Reuters Legal Solutions | — | |

### Linkable Asset Ideas

- Uganda Oil & Gas Legal Guide (annual)
- Uganda Investment Climate FAQ for foreign investors
- East African Mining Regulations Comparison
- Uganda Employment Law Compliance Checklist

---

## SECTION 10: SXO — SEARCH EXPERIENCE OPTIMIZATION

**Key finding:** The site's best pages (real-estate, immigration) are aligned with transactional intent — a prospective client finding these pages would understand the services, trust the firm, and be able to contact them. The gap is that 9 practice area pages do not achieve this standard.

### User Intent Gaps

- Informational queries ("how to register a company Uganda", "work permit Uganda") have no dedicated pages — users landing on service pages for informational queries will bounce.
- No fee transparency anywhere on the site — a major friction point for cost-comparison searches.
- CTAs are strong ("Schedule a Free Consultation") but only appear at the end of pages — add an inline CTA midway through content on each page.

### Persona Scoring (1–10)

| Persona | Score | Notes |
|---|---|---|
| Corporate client (company registration) | 7/10 | Good schema, but thin content on corporate-commercial page |
| Expat (work permit) | 9/10 | Immigration page is detailed, process clear, CTAs strong |
| Individual with land dispute | 8/10 | Real-estate page is the strongest page on the site |
