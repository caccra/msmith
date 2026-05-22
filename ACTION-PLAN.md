# M-Smith Advocates — SEO Action Plan

**Site:** https://www.m-smithadvocates.com
**Date:** May 2026

---

## CRITICAL — Fix Immediately
*Blocking rankings or causing active errors*

| # | Issue | File(s) | Fix |
|---|---|---|---|
| C1 | Kampala address conflict — verify correct address and unify across website + GBP + all citations | All pages (footer), index.html schema, contact.html schema | Confirm physical address; update every LegalService PostalAddress block; update GBP |
| C2 | Geo coordinates inconsistent | index.html line ~42 (0.27450, 32.60120) vs contact.html (0.299999, 32.596541) | Verify GPS for actual office building; apply one consistent value to both pages |
| C3 | sameAs missing from all LegalService schema | index.html and all 19 pages | Add `"sameAs": ["[GBP URL]", "[LinkedIn URL]", "[ULS directory URL]"]` to primary LegalService on index.html |
| C4 | 13 title tags exceed 60 characters — Google rewriting in SERPs | about, practice-areas, team, contact, litigation-arbitration, real-estate, intellectual-property, oil-gas-petroleum, mining-minerals, employment-labour, corporate-commercial, immigration, human-rights, eac-law | Use the shortened titles listed in Section 4 of FULL-AUDIT-REPORT.md |
| C5 | aggregateRating reviewCount:"6" but only 3 Review objects exist | index.html | Change reviewCount to 3 (integer); change ratingValue/bestRating/worstRating to integers (not strings) |

---

## HIGH — Fix Within 1 Week

| # | Issue | File(s) | Fix |
|---|---|---|---|
| H1 | ContactPage.isPartOf points to #organization instead of #website | contact.html | Change isPartOf @id to https://www.m-smithadvocates.com/#website; add `"about": {"@id": ".../#organization"}` |
| H2 | real-estate FAQPage missing @id | real-estate.html | Add `"@id": "https://www.m-smithadvocates.com/real-estate#faq"` |
| H3 | ItemList uses "url" instead of "item" in ListItem | practice-areas.html | Replace all "url" properties with "item" in ItemList ListItem objects |
| H4 | 9 meta descriptions exceed 160 characters by 2–9 chars | Multiple pages | Trim end phrases; homepage: remove phone number from meta description |
| H5 | 5 pages missing og:image | about, practice-areas, team, contact, real-estate | Add `<meta property="og:image" content="https://www.m-smithadvocates.com/logo.png">` |
| H6 | About page H1 "Who We Are" has no keyword | about.html | Change to "About M-Smith Advocates — Law Firm in Uganda" |
| H7 | robots.txt missing explicit AI crawler entries | robots.txt | Add explicit `Allow: /` for GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot; remove /privacy-policy from Disallow |
| H8 | Claim/verify GBP for all three offices | External (GBP) | Create/verify listings for Kampala, Nairobi, Mombasa; set primary category to "Law Firm" |
| H9 | Review objects have no datePublished | index.html | Add `"datePublished": "YYYY-MM-DD"` (ISO 8601) to each of the 3 Review objects |

---

## MEDIUM — Fix Within 30 Days

| # | Issue | File(s) | Fix |
|---|---|---|---|
| M1 | 9 practice area pages under 900 words (YMYL thin content) | corporate-commercial, litigation-arbitration, insurance, human-rights, eac-law, oil-gas-petroleum, mining-minerals, intellectual-property, employment-labour | Add "Regulatory Framework" section citing 2+ specific statutes; expand FAQs from 3 to 6–8 questions |
| M2 | No inline YMYL disclaimer on practice area pages | All 11 practice area pages | Add one line at top of main content: "This page provides general information only, not legal advice. Contact us for advice specific to your situation." |
| M3 | Verified matter outcomes not on practice area pages | employment-labour, corporate-commercial, intellectual-property, litigation-arbitration | Move llms.txt case outcomes onto corresponding pages (Industrial Court result → employment-labour; UGX 680M debt recovery → corporate-commercial; IP enforcement → intellectual-property) |
| M4 | Create /nairobi and /mombasa landing pages | New files: nairobi.html, mombasa.html | Each: unique H1+meta, full NAP, Maps embed, Kenya-specific legal content, separate LegalService JSON-LD, sameAs to Kenya GBP listing |
| M5 | FAQPage JSON-LD missing from 7 practice area pages | employment-labour, oil-gas-petroleum, intellectual-property, mining-minerals, insurance, human-rights, eac-law | Add FAQPage @graph node with existing FAQ content as mainEntity array |
| M6 | Person schema missing image and description | team.html | Add `"image": {"@type": "ImageObject", "url": "..."}` and `"description": "..."` to all 5 Person entities |
| M7 | Maweu Christopher Kituu hasCredential missing recognizedBy | team.html | Add `"recognizedBy": {"@type": "EducationalOrganization", "name": "..."}` to MPPM and BASS credentials |
| M8 | Add year of enrollment to Roll of Advocates in team bios | team.html | Add bar admission year to each advocate's visible bio text and schema |
| M9 | Add "Last reviewed" date to all practice area pages | All 11 practice area pages | Add visible "Last reviewed: [Month Year]" line to each page |
| M10 | Internal links missing from about.html body | about.html | Link "Real Estate", "EAC Law", "Oil & Gas", "Human Rights" mentions to their practice area pages |
| M11 | Twitter cards using summary instead of summary_large_image | All pages | Change twitter:card to summary_large_image; add twitter:image to all pages |
| M12 | WebPage entity missing from about.html | about.html | Add WebPage @graph node with @id, url, name, description, isPartOf, about properties |
| M13 | llms.txt missing last-updated date, RSL 1.0 license, advocate-practice mapping | llms.txt | Add `> Last updated: May 2026`; add ## License section; add practice specializations per advocate |

---

## LOW — Backlog

| # | Issue | File(s) | Fix |
|---|---|---|---|
| L1 | Launch legal insights blog (highest long-term E-E-A-T impact) | New /blog/ section | Start with 6 articles: land tenure Uganda, company registration guide, work permit guide, bibanja rights, EAC free movement, Uganda employment law |
| L2 | Submit to legal directories (Justia, Avvo, FindLaw, HG.org, Martindale-Hubbell, Africa Legal) | External | Create firm + individual attorney profiles on each; use consistent NAP |
| L3 | Apply for Chambers Africa, Legal 500, IFLR1000 | External | Submit for corporate, energy, real estate practices; 12–18 month process |
| L4 | Add speakable schema to FAQ answers | All practice area pages | Add `"speakable": {"@type": "SpeakableSpecification", "cssSelector": [".faq-a"]}` to each page's @graph |
| L5 | Add outbound links to authoritative sources | All practice area pages | Link statute names to ulii.org; URSB to ursb.go.ug; DCIC to mia.go.ug; link ULII case record from about.html |
| L6 | ProfilePage schema on team.html | team.html | Add ProfilePage @graph node referencing all 5 Person @id values |
| L7 | memberOf (Uganda Law Society) on Person schema | team.html | Add `"memberOf": {"@type": "Organization", "name": "Uganda Law Society", "url": "https://www.uls.or.ug"}` to each Person |
| L8 | Add gzip compression and browser caching headers | .htaccess | Add mod_deflate and mod_expires rules |
| L9 | Minify styles.css (76KB → ~60KB) | styles.css | Run through a CSS minifier; consider splitting critical CSS |
| L10 | Adopt per-page lastmod dates in sitemap.xml | sitemap.xml | Update lastmod per actual file modification dates going forward |
| L11 | Verify or remove SearchAction potentialAction | index.html | Test if /practice-areas?q= resolves a working search; if not, remove potentialAction from WebSite schema |
| L12 | Add Google review widget and review generation flow | index.html, contact.html | Embed live Google review count; add GBP review link to contact form confirmation state |
| L13 | postalCode missing from all PostalAddress blocks | All pages | Add postbox number or remove field; do not leave absent |
| L14 | Rename mismatched image file | images/ | Rename "m-smithadvocates_Insurance law (10).jpg" used as oil/gas card image |
| L15 | Upgrade to Cloudflare (free) for CDN and HTTPS headers | Hosting/DNS | Point DNS through Cloudflare; enables HSTS, brotli compression, caching, TTFB improvement |
