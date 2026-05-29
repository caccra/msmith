# M-Smith Advocates — Full SEO Audit Report
**Site:** https://www.m-smithadvocates.com  
**Audit Date:** May 2026  
**Business Type:** Local Legal Service — Full-Service Law Firm (Uganda + East Africa)  
**Auditor:** Live crawl + local file analysis

---

## SEO Health Score: 41 / 100

| Category | Score | Weight | Weighted |
|----------|-------|--------|---------|
| Technical SEO | 30/100 | 22% | 6.6 |
| Content Quality | 72/100 | 23% | 16.6 |
| On-Page SEO | 52/100 | 20% | 10.4 |
| Schema / Structured Data | 35/100 | 10% | 3.5 |
| Performance (CWV) | 50/100 | 10% | 5.0 |
| AI Search Readiness | 70/100 | 10% | 7.0 |
| Images | 40/100 | 5% | 2.0 |
| **Total** | | | **41.1** |

---

## Executive Summary

M-Smith Advocates has a technically competent website with strong content depth, but is suffering from a **near-total indexation failure**. Google has indexed only **2 pages** from the entire site — the homepage and a duplicate `/home/` page. The firm is invisible in search results for every high-value keyword it should own: "real estate lawyers Uganda," "immigration lawyers Kampala," "company registration Uganda," etc. Competitors (MMAKS, Mirembe & Co, INQ Advocates, Angualia Busiku) dominate every relevant SERP.

The root causes are: (1) a canonicalization/indexation block preventing inner pages from being crawled, (2) the articles section not yet deployed to the live server, (3) a stale sitemap on the live server, and (4) missing Google Search Console verification and submission.

Fixing these technical issues is the single highest-leverage action available. The content already exists and is good — it simply is not reaching Google.

---

## CRITICAL ISSUES (Fix Immediately)

### C1 — Only 2 Pages Indexed by Google
**Impact: Catastrophic**

`site:m-smithadvocates.com` returns only:
- `https://m-smithadvocates.com/` (homepage)
- `https://m-smithadvocates.com/home/` (duplicate)

The 12 practice area pages, about, team, contact, 10 articles, and all other pages are **not indexed**. The firm is completely invisible to Google for every commercial search term it should rank for.

**Likely causes:**
- GSC has never been verified — sitemap has never been submitted
- The www vs non-www version may not be properly consolidated
- Inner pages may have a crawling or rendering barrier preventing Googlebot from following links

**Fix:**
1. Deploy `google5c9821a3eb6009be.html` to the server root
2. Verify in Google Search Console immediately
3. Submit the updated sitemap to GSC
4. Check `.htaccess` for any accidental `Disallow` or redirect loops on inner pages
5. Use GSC URL Inspection to manually request indexing for the 10 highest-priority pages

---

### C2 — Articles Section Returns 404 on Live Server
**Impact: High**

`https://www.m-smithadvocates.com/articles` returns **HTTP 404**. The 10 article pages created locally have not been deployed to production. 10 substantive long-form guides are completely unavailable to users and search engines.

**Fix:** Deploy `articles.html` and the entire `articles/` folder to the production server.

---

### C3 — Duplicate `/home/` Page Indexed
**Impact: High**

`https://m-smithadvocates.com/home/` is indexed by Google as a separate page from the homepage. This dilutes crawl budget and sends mixed signals about the canonical homepage.

**Fix:** Add `301 redirect /home/ / ` to `.htaccess`, or add `<meta name="robots" content="noindex">` to that page.

---

### C4 — Live Sitemap is Stale and Inaccurate
**Impact: High**

The live `sitemap.xml` shows only **19 URLs** from an old version:
- Missing all 10 article pages
- Missing `disclaimer`, `privacy-policy`, `terms`, `fees`
- Shows `/mining-minerals` (wrong) instead of `/mining-transaction-advisory`
- Has no `changefreq` or `priority` values
- Does not signal the articles section at all

The updated 43-URL sitemap with full metadata exists locally and must be deployed.

**Fix:** Deploy the updated `sitemap.xml` and submit it in Google Search Console.

---

### C5 — Google Search Console Not Verified
**Impact: Blocks all GSC capabilities**

Without GSC, there is no way to submit the sitemap, monitor indexation, receive manual action notices, identify crawl errors, or track search performance. The verification file `google5c9821a3eb6009be.html` is ready — it just needs to go live.

**Fix:** Deploy the verification file, then verify at search.google.com/search-console.

---

## HIGH PRIORITY (Fix Within 1 Week)

### H1 — Internal Links Point to `/mining-minerals` (Old URL)
The live navigation on multiple pages links to `/mining-minerals` instead of `/mining-transaction-advisory`. The `mining-minerals.html` page has a canonical pointing to `/mining-transaction-advisory`, so link equity is being misrouted.

**Fix:** Update all nav links to `mining-transaction-advisory`. Add `301 Redirect /mining-minerals /mining-transaction-advisory` in `.htaccess`.

---

### H2 — Meta Descriptions Not Rendering in HTML Source
Across every page tested — homepage, about, immigration, real-estate, contact, litigation, team — no meta description was detectable in the crawled HTML. This strongly suggests they are JavaScript-injected, making them invisible to Google's basic HTML crawler. Google then writes its own snippet from page content, which is typically worse.

**Fix:** Confirm meta descriptions are in the server-rendered `<head>` tag. Open page source (`Ctrl+U`) and search for `<meta name="description"` — if absent, the tags are JS-rendered and must be moved to static HTML.

---

### H3 — Canonical Tags Not Rendering in HTML Source
No `<link rel="canonical">` was detected in the crawled HTML of any page. Without server-rendered canonicals, Google may not know which URL version to prefer, especially given the www/non-www ambiguity.

**Fix:** Ensure canonical tags are in the static HTML `<head>`, not injected by JavaScript.

---

### H4 — www vs non-www Canonicalization Not Confirmed
Google's index shows `m-smithadvocates.com` (non-www) while all local canonical/OG tags reference `www.m-smithadvocates.com`. If both versions resolve without a 301 redirect, Google may treat them as separate sites and split link equity.

**Fix:**
1. Confirm `.htaccess` has: `RewriteRule ^(.*)$ https://www.m-smithadvocates.com/$1 [R=301,L]` for non-www → www
2. Set preferred domain in Google Search Console
3. Ensure all canonical and OG URL tags consistently use `www`

---

### H5 — Schema Markup Not Rendering on Live Pages
The local HTML files contain detailed JSON-LD (LegalService, FAQPage, BreadcrumbList, Article, LocalBusiness, Person). However, live crawls detected no schema on most pages. Schema must be in the static HTML to qualify for rich results.

**Fix:** Deploy updated HTML files. After deployment, test each page with [Google's Rich Results Test](https://search.google.com/test/rich-results).

---

### H6 — robots.txt Disallows `/terms` and `/disclaimer`
These pages are blocked from all crawlers including Googlebot. While low SEO value, blocking them means they receive no link equity and can't be evaluated by Google.

**Fix:** Remove both from `Disallow`. If de-indexation is wanted without blocking crawling, add `<meta name="robots" content="noindex, follow">` to each page instead.

---

### H7 — No Google Analytics Installed
No GA4, GTM, or analytics code was detected on any live page. Without analytics there is no way to measure organic traffic, conversion rates, or the impact of any SEO work.

**Fix:** Install Google Analytics 4 via a `<script>` tag in the `<head>` of every page, or via GTM.

---

## MEDIUM PRIORITY (Fix Within 1 Month)

### M1 — Not Appearing in Any Key SERP

| Query | Top Rankers | M-Smith |
|-------|-------------|---------|
| Real estate lawyers Uganda | MMAKS, Mirembe, INQ, Angualia Busiku | ❌ Not found |
| Immigration lawyers Kampala | INQ, Ahamark, Favour Advocates | ❌ Not found |
| Company registration Uganda lawyer | Directory listings | ❌ Not found |
| Law firm Kampala Uganda | MMAKS, MBS, CM Advocates | ❌ Not found |

This is primarily a consequence of the indexation failure (C1). Once inner pages are indexed, the firm's content quality gives it a realistic shot at ranking for niche long-tail terms first, then broader terms over time.

**Realistic quick-win ranking targets (low-competition, M-Smith has specific content):**
- "how to verify land title Uganda"
- "bibanja rights Uganda"
- "Class G work permit Uganda 2026"
- "EAC free movement employers Uganda"
- "mining transaction advisory Uganda"
- "arbitration vs litigation Uganda"

---

### M2 — No Person Schema on Team Page
Individual lawyer profiles have no structured data. Google cannot extract individual advocate credentials for rich results.

**Fix:** Add `Person` schema for each advocate with `name`, `jobTitle`, `worksFor`, `alumniOf`, `knowsAbout`.

---

### M3 — Team Page Content Thin (~950 words)
All other pages are 1,500–3,200 words. The team page has fewer than 1,000 words total for 5 professionals.

**Fix:** Expand each bio with specific sub-specialisms, notable matters handled, years of PQE, and a personal statement.

---

### M4 — Google Business Profile Not Optimised
M-Smith is not appearing in Google Maps or the local pack for any Kampala law firm searches.

**Fix:**
- Verify GBP ownership at business.google.com
- Add all 12 practice areas as GBP Services
- Upload office photos (interior, team, reception)
- Post regularly (weekly legal tips, news, articles)
- Actively request reviews from satisfied clients

---

### M5 — No Backlink Profile
The firm has no inbound links from authoritative domains beyond tabloid news (Red Pepper) and directory listings. Domain Authority is effectively 0.

**Fix:**
- Optimize Lawzana profile to appear in "10 best" lists
- Submit to HG.org, Martindale, lawyers.com, Africa Legal Network
- Contribute guest articles to Uganda Law Society publications and EALS
- Publish press releases for significant matters (with client permission)

---

### M6 — Image Filenames Contain Spaces
Several images use filenames with spaces: `m-smithadvocates_employement and labour.jpeg`, `m-smithadvocates Litigation.webp`. These require `%20` URL encoding and are poor practice for SEO.

**Fix:** Rename files using hyphens, update all references in HTML. Descriptive names like `employment-labour-law-uganda.jpeg` also improve image search visibility.

---

### M7 — `/mining-minerals.html` Orphan Page
This page has no inbound internal links, its canonical points to `/mining-transaction-advisory`, and it is a duplicate. It wastes crawl budget.

**Fix:** Delete the file and add `301 Redirect /mining-minerals /mining-transaction-advisory` in `.htaccess`.

---

## LOW PRIORITY (Backlog)

### L1 — No Dedicated OG Images Per Practice Area
All pages use the logo as the OG image. Dedicated featured images per practice area would significantly improve click-through on social sharing.

### L2 — Related-Card Images Missing Explicit Dimensions
The 3 related-article card images at the bottom of each article page have no `width`/`height` attributes, which can cause minor CLS.

### L3 — Google Fonts External Dependency
Loading from fonts.googleapis.com adds a DNS lookup + connection on first visit (~150-200ms). Consider self-hosting fonts for a marginal performance gain.

### L4 — No Structured FAQ for Homepage
The homepage has a comparative table and testimonials but no FAQ schema. Adding an FAQ with 5-8 questions would create rich result eligibility for the homepage SERP listing.

---

## ROBOTS.TXT ANALYSIS

```
User-agent: *
Allow: /
Disallow: /terms          ← Remove this (blocks indexation)
Disallow: /disclaimer     ← Remove this (blocks indexation)
Disallow: /claude-seo/    ← Fine (internal dev tool)

User-agent: Google-Extended   ← Excellent AI bot configuration
User-agent: GPTBot            ← All correctly allowed
User-agent: OAI-SearchBot
User-agent: ClaudeBot
User-agent: PerplexityBot
User-agent: Applebot-Extended

# llms.txt reference: ✅ Present
Sitemap: ✅ Present (but pointing to stale file)
```

The AI bot allowlist is excellent — ahead of most law firm sites globally.

---

## DEPLOYMENT CHECKLIST

These files must be deployed to production to unlock indexation:

- [ ] `google5c9821a3eb6009be.html` → enables GSC verification
- [ ] `sitemap.xml` → 43-URL updated sitemap with articles + metadata
- [ ] `llms.txt` → updated with 10 article summaries
- [ ] `articles.html` → articles index page (currently 404 live)
- [ ] `articles/` folder → all 10 article pages (currently 404 live)
- [ ] All updated practice area pages → ensure schema/meta in static HTML
- [ ] `.htaccess` → www redirect + mining-minerals redirect + /home/ redirect

**Post-deployment actions:**
- [ ] Verify site in Google Search Console
- [ ] Submit sitemap in GSC
- [ ] Request indexing of 10 priority pages via URL Inspection tool
- [ ] Set preferred domain (www) in GSC settings
- [ ] Install Google Analytics 4
- [ ] Test schema with Rich Results Test on 3 pages
- [ ] Verify and optimise Google Business Profile

---

## AI SEARCH READINESS

| Signal | Status | Notes |
|--------|--------|-------|
| `llms.txt` present | ✅ | Well-structured, includes team, matters, practice areas |
| Articles in `llms.txt` | ✅ | 10 guides summarised (updated locally) |
| AI bot allowlist in robots.txt | ✅ | GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot all allowed |
| Factual specificity | ✅ | Case references, act names, court names, dates |
| Named entity density | ✅ | Uganda Land Act Cap 227, URSB, DCIC, etc. |
| Passage-level structure | ✅ | Clean H2/H3 hierarchy throughout |
| External citations | ⚠️ | No authoritative third-party sites link or reference M-Smith |
| AI Overview eligibility | ⚠️ | Blocked by indexation failure — fix C1 first |

---

## CONTENT QUALITY SUMMARY

| Page | Words | FAQ | Schema | E-E-A-T |
|------|-------|-----|--------|---------|
| Homepage | ~4,500 | ❌ | ⚠️ | ✅ |
| About | ~2,200 | ❌ | ⚠️ | ✅ |
| Real Estate | ~3,200 | ✅ | ⚠️ | ✅ |
| Immigration | ~2,500 | ✅ | ⚠️ | ✅ |
| Corporate | ~2,200 | ✅ | ✅ | ✅ |
| Litigation | ~1,550 | ✅ | ⚠️ | ✅ |
| Family Law | ~1,900 | ✅ | ⚠️ | ✅ |
| Team | ~950 | ❌ | ❌ | ⚠️ |
| Contact | ~800 | ❌ | ⚠️ | ✅ |
| Articles (×10) | ~1,600 avg | ❌ | ✅ | ✅ |

---

*Report generated: May 2026. Live data sourced from direct crawl of https://www.m-smithadvocates.com.*
