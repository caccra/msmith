# SEO Action Plan - M-Smith Advocates
Generated: May 2026 | Health Score: 74/100
Site: https://www.m-smithadvocates.com

---

## CRITICAL - Fix Immediately

### C1. Deploy pending pages - 3 pages are 404 on the live server

Files to upload: family-law.html, nairobi.html, mombasa.html, sitemap.xml (19 URLs),
index.html (12 practice areas, new FAQ entries), about/contact/practice-areas/team.html (async fonts).

Multiple pages already link to family-law. Every visit from the homepage is a dead end right now.
After deploying, submit the sitemap in Google Search Console > Sitemaps.

---

### C2. Add Google Analytics 4 + Google Search Console

Zero analytics are installed. No way to measure organic traffic, enquiries, or SEO impact.

1. Create a GA4 property at analytics.google.com - get Measurement ID (G-XXXXXXXX)
2. Add the GA4 gtag snippet to every <head> tag across all 22 HTML pages
3. Verify the site in Google Search Console and link it to GA4
4. Set up a Conversion event that fires on the success: true JSON response from contact.php

---

## HIGH - Fix Within 1 Week

### H1. Trim homepage title from 74 chars to under 60
File: index.html

Current:  M-Smith Advocates | Corporate, Property & Litigation Lawyers in Uganda (74 chars)
Proposed: M-Smith Advocates | Lawyers in Kampala, Uganda (47 chars)
Also update the twitter:title tag to match.

### H2. Fix 3 H1 tags on homepage - keep only one
File: index.html

Three H1s: (1) Trusted Legal Solutions for Individuals, Businesses & Institutions
           (2) Uganda's Advocates for Business, Property & Justice
           (3) Your Trusted Legal Partner
Keep H1 #1. Change H1 #2 and H1 #3 to H2.

### H3. Add Person schema to team.html for all 5 advocates
File: team.html

Add a Person @graph node for: Masari Aim Smith, Namulindwa Rose, Makhoka John,
Nalumansi Sylvia, Maweu Christopher Kituu. Each node needs: name, jobTitle, worksFor,
alumniOf (Makerere University), memberOf (Uganda Law Society, East African Law Society).

### H4. Add explicit LocalBusiness schema to homepage and contact page
Files: index.html, contact.html

The current LegalService schema lacks the LocalBusiness type that Google uses for local pack.
Add a node with: @type LegalService+LocalBusiness, address (Tirupati Mazima Mall, Kabalagala),
geo (lat: 0.2963, lng: 32.5922), telephone, openingHours Mo-Fr 08:00-17:00, hasMap.

### H5. Remove meta keywords tags from all 22 pages
Search for meta name=keywords and delete those lines. Ignored by Google since 2009.

### H6. Fix nairobi.html meta description - 163 chars, limit is 155
File: nairobi.html
Trim 8-10 characters from the end to prevent SERP truncation.

---

## MEDIUM - Fix Within 1 Month

### M1. Create and verify Google Business Profile
Visit business.google.com. Create/claim the Kampala listing using exact site NAP:
  Name: M-Smith Advocates
  Address: Tirupati Mazima Mall, Kabalagala, Kampala
  Phone: +(256) 782 776 074
  Category: Law Firm
  Hours: Monday-Friday 08:00-17:00
Add office photos and link to the website. Repeat for Nairobi and Mombasa once live.
GBP is the single most impactful action for Google Maps / local pack ranking.

### M2. Embed Google Map on contact.html
Replace the Get Directions text link with an embedded Google Maps iframe for the Kampala office.
Also add hasMap to the LocalBusiness schema (H4 above).

### M3. Expand mombasa.html before deployment (currently 891 words - thin)
File: mombasa.html
Add 400+ words on: Mombasa-specific services (maritime, port logistics, coastal real estate),
local courts, Kenya coastal land law, and a 2-3 question local FAQ section.

### M4. Add Content-Security-Policy header
All other security headers pass. Add CSP to .htaccess covering: self, gtag, GA4, Google Fonts.

### M5. Self-host Google Fonts
Download Cinzel, EB Garamond, Lato, Manrope as woff2 files and serve from the same origin.
Removes external DNS+TLS round-trip to fonts.googleapis.com on every first visit.
Use google-webfonts-helper to generate the CSS and download the files.

### M6. Create practice-area-specific OG images (1200x630)
Every page shares the same logo.png OG image. When shared on LinkedIn or WhatsApp all links
look identical. Create distinct images for: immigration, real-estate, corporate-commercial,
litigation-arbitration, family-law.

---

## LOW - Backlog

### L1. Start a legal blog
Monthly articles build topical authority and AI citability. Starter topics:
- How to verify a land title in Uganda (step-by-step)
- Uganda work permit costs 2026: Class G and Class M explained
- Company registration at URSB: timeline and costs
- Bibanja rights: what occupants and landlords must know

### L2. Add visible breadcrumb navigation
BreadcrumbList schema already present. Add a visible breadcrumb bar on all inner pages.

### L3. Expand individual advocate bios on team.html
200-400 words per advocate: education, bar enrolment year, notable case types.

### L4. Create llms-full.txt
Full markdown text of each practice area page for deeper AI retrieval.

### L5. Add Cloudflare (free tier)
CDN edge caching, Brotli compression, lower TTFB for Nairobi/Mombasa visitors.

### L6. Link statute names to authoritative sources (ulii.org, ursb.go.ug, mia.go.ug)
Outbound links to government/legal authority sites improve trust signals for AI engines.

### L7. Add AggregateRating schema once GBP reviews reach 5+
Surfaces star ratings in branded SERP results.

### L8. Submit to African legal directories
Africa Legal, ULII attorney database. Consistent NAP citations strengthen local SEO.

---

## Summary

Priority  | Count | Effort   | Impact
Critical  |   2   | Low      | Very High (fix now)
High      |   6   | Low-Med  | High
Medium    |   6   | Medium   | Medium-High
Low       |   8   | Med-High | Medium (long-term)
