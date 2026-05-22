"""
Fixes:
  1. dateModified 2025-05-22 -> 2026-05-22 on all pages
  2. Homepage + real-estate meta description trim to <= 160 chars
  3. FAQPage schema added to 7 pages
  4. Sitemap lastmod dates updated to 2026-05-22
"""

import re

# ── helpers ──────────────────────────────────────────────────────────────────

def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  updated: {path}")

# ── 1. Fix dateModified year across all HTML pages ────────────────────────────

html_pages = [
    "index.html", "about.html", "team.html", "practice-areas.html", "contact.html",
    "corporate-commercial.html", "real-estate.html", "immigration.html",
    "employment-labour.html", "eac-law.html", "litigation-arbitration.html",
    "intellectual-property.html", "oil-gas-petroleum.html", "mining-minerals.html",
    "insurance.html", "human-rights.html",
]

print("=== Fix 1: dateModified year ===")
for page in html_pages:
    html = read(page)
    if "2025-05-22" in html:
        html = html.replace("2025-05-22", "2026-05-22")
        write(page, html)

# ── 2. Trim meta descriptions ─────────────────────────────────────────────────

print("\n=== Fix 2: Meta descriptions ===")

# Homepage: 191 chars -> trim to 155 chars
idx_html = read("index.html")
old_idx_desc = 'content="M-Smith Advocates is a Kampala-based law firm specializing in corporate law, litigation, real estate, immigration, intellectual property, and EAC legal services across Uganda and East Africa."'
new_idx_desc = 'content="M-Smith Advocates is a Kampala-based law firm specializing in corporate law, litigation, real estate, immigration, IP, and EAC legal services across Uganda."'
if old_idx_desc in idx_html:
    idx_html = idx_html.replace(old_idx_desc, new_idx_desc)
    write("index.html", idx_html)
else:
    print("  index.html: description not matched — check manually")

# real-estate: 169 chars -> trim by removing "Book a consultation."
re_html = read("real-estate.html")
old_re_desc = 'content="Trusted real estate lawyers in Uganda. M-Smith Advocates handles property transactions, title verification, conveyancing &amp; land disputes in Kampala. Book a consultation."'
new_re_desc = 'content="Trusted real estate lawyers in Uganda. M-Smith Advocates handles property transactions, title verification, conveyancing &amp; land disputes in Kampala."'
if old_re_desc in re_html:
    re_html = re_html.replace(old_re_desc, new_re_desc)
    write("real-estate.html", re_html)
else:
    # try with & instead of &amp;
    old_re_desc2 = 'content="Trusted real estate lawyers in Uganda. M-Smith Advocates handles property transactions, title verification, conveyancing & land disputes in Kampala. Book a consultation."'
    new_re_desc2 = 'content="Trusted real estate lawyers in Uganda. M-Smith Advocates handles property transactions, title verification, conveyancing & land disputes in Kampala."'
    if old_re_desc2 in re_html:
        re_html = re_html.replace(old_re_desc2, new_re_desc2)
        write("real-estate.html", re_html)
    else:
        print("  real-estate.html: description not matched — check manually")

# ── 3. Add FAQPage schema to 7 pages ─────────────────────────────────────────

print("\n=== Fix 3: FAQPage schema ===")

# Each entry: (filename, @id, list of (question, answer))
faq_data = {
    "employment-labour.html": {
        "id": "https://www.m-smithadvocates.com/employment-labour#faq",
        "qa": [
            (
                "What are the legal requirements for terminating an employee in Uganda?",
                "Under the Employment Act 2006, termination must be for a valid reason (misconduct, incapacity, or redundancy) and must follow a fair procedure, including notice or payment in lieu, and a hearing for disciplinary terminations. Failure to comply can result in unfair dismissal claims before the Industrial Court. We advise on termination processes and represent employers in disputes."
            ),
            (
                "Are employment contracts mandatory in Uganda?",
                "While verbal contracts are legally recognized, the Employment Act requires written contracts for employment of more than six months or for expatriate employees. Written contracts are strongly recommended in all cases as they define the terms of the relationship and reduce the risk of disputes. We draft comprehensive employment contracts tailored to your business needs."
            ),
            (
                "How does Uganda's Industrial Court handle employment disputes?",
                "The Industrial Court has exclusive jurisdiction over trade disputes and employment matters in Uganda. It aims to resolve disputes quickly and fairly, with mediation available as a first step before formal hearing. We represent both employers and employees before the Industrial Court and related labour dispute mechanisms."
            ),
        ],
    },
    "eac-law.html": {
        "id": "https://www.m-smithadvocates.com/eac-law#faq",
        "qa": [
            (
                "What are the main EAC protocols that affect business in Uganda?",
                "The key protocols affecting business include the EAC Customs Union Protocol (tariffs and trade), the EAC Common Market Protocol (free movement of goods, persons, services, and capital), and the EAC Monetary Union Protocol (financial integration). Each creates both opportunities and compliance obligations. We advise on how to leverage these frameworks and remain compliant with evolving regional regulations."
            ),
            (
                "Can I bring a dispute against an EAC Partner State to the East African Court of Justice?",
                "Yes. The EACJ has jurisdiction over disputes arising from the EAC Treaty, including complaints that a Partner State has failed to fulfil its Treaty obligations. Both individuals and legal entities can bring cases before the Court following the exhaustion of local remedies, in most circumstances. We assess the merits of potential EACJ cases and handle filings and representation before the Court."
            ),
            (
                "Does Uganda recognize and enforce judgments from other EAC countries?",
                "Recognition and enforcement of foreign judgments in Uganda follows both common law principles and the Reciprocal Enforcement of Judgments Act. For EAC countries, enforcement is generally more straightforward than for non-EAC jurisdictions, though the specific procedure depends on the country of origin and nature of the judgment. We advise on enforcement strategy and manage enforcement proceedings in Ugandan courts."
            ),
        ],
    },
    "insurance.html": {
        "id": "https://www.m-smithadvocates.com/insurance#faq",
        "qa": [
            (
                "What should I do if my insurance claim is denied in Uganda?",
                "First, request a written explanation of the denial from your insurer. Then seek legal advice on whether the denial is justified under the policy wording. Many denials can be successfully challenged through internal complaints, Insurance Regulatory Authority complaints, or litigation. We review denied claims and advise on the strongest course of action."
            ),
            (
                "Are insurance companies in Uganda regulated?",
                "Yes. The Insurance Regulatory Authority of Uganda (IRA) supervises all insurers, reinsurers, brokers, and agents operating in Uganda under the Insurance Act. The IRA also has a complaints mechanism for consumers. We advise clients on making regulatory complaints and can represent them in IRA proceedings."
            ),
            (
                "What is subrogation in insurance law?",
                "Subrogation is the right of an insurer, after paying a claim, to step into the shoes of the insured and recover the amount paid from the party responsible for the loss. We advise insurers on pursuing subrogation actions and help policyholders understand their obligations when their insurer asserts subrogation rights."
            ),
        ],
    },
    "human-rights.html": {
        "id": "https://www.m-smithadvocates.com/human-rights#faq",
        "qa": [
            (
                "How can I challenge a violation of my constitutional rights in Uganda?",
                "Constitutional rights violations are challenged through a Constitutional Petition filed in the Constitutional Court of Uganda. In urgent cases involving unlawful detention, an application for habeas corpus can be filed in the High Court for immediate relief. We advise on the most appropriate remedy for your specific situation and handle the filing and prosecution of all constitutional applications."
            ),
            (
                "Can individuals take human rights cases to the East African Court of Justice?",
                "Yes. The East African Court of Justice (EACJ) has jurisdiction to hear human rights matters arising from the EAC Treaty. Individuals can file cases alleging violations of Treaty provisions by EAC Partner States. We have experience before the EACJ and advise on whether a given situation meets the admissibility criteria for a regional case."
            ),
            (
                "Do you handle human rights cases pro bono?",
                "We consider pro bono representation on a case-by-case basis, particularly for matters of significant public interest or where the client has no means to pay. We are committed to ensuring that financial barriers do not prevent access to justice. Please contact us to discuss your situation and we will advise on available options."
            ),
        ],
    },
    "intellectual-property.html": {
        "id": "https://www.m-smithadvocates.com/intellectual-property#faq",
        "qa": [
            (
                "How do I register a trademark in Uganda?",
                "Trademark registration is handled through the Uganda Registration Services Bureau. The process involves a trademark search, filing an application, publication in the Uganda Gazette, and — if unopposed — issuance of a registration certificate. The process typically takes 6–12 months. We handle the entire process on your behalf."
            ),
            (
                "Does my Ugandan trademark protect me across East Africa?",
                "A Ugandan trademark only provides protection within Uganda. For broader protection, we can file a regional application through ARIPO (African Regional Intellectual Property Organization), which covers up to 22 member states, including Kenya, Tanzania, Rwanda, and Zambia."
            ),
            (
                "What can I do if someone is copying my brand or product in Uganda?",
                "If your IP is registered, you can seek an injunction, damages, and an account of profits through the courts. We also assist with cease-and-desist letters, customs recordal to intercept counterfeit goods, and criminal prosecution where applicable. Early legal action is usually the most effective response."
            ),
        ],
    },
    "oil-gas-petroleum.html": {
        "id": "https://www.m-smithadvocates.com/oil-gas-petroleum#faq",
        "qa": [
            (
                "What is Uganda's national content requirement for oil and gas companies?",
                "Uganda's Petroleum (Exploration, Development and Production) Act requires licensees and their contractors to give preferential treatment to Ugandan goods and services and to employ and train Ugandan nationals. We advise on structuring operations to meet these requirements and prepare national content plans for submission to the Petroleum Authority of Uganda."
            ),
            (
                "How are oil and gas disputes resolved in Uganda?",
                "Disputes can be resolved through negotiation, mediation, arbitration (domestic or international), or litigation in Ugandan courts. Most Production Sharing Agreements specify international arbitration as the dispute resolution mechanism. We advise on dispute prevention strategies and represent clients in all forms of dispute resolution."
            ),
            (
                "Can a foreign company bid for oil and gas contracts in Uganda?",
                "Yes, foreign companies can participate, but must comply with national content regulations and licensing requirements. A joint venture with a Ugandan company is often beneficial — both for regulatory compliance and for building local relationships. We advise on structuring joint ventures and preparing licence applications."
            ),
        ],
    },
    "mining-minerals.html": {
        "id": "https://www.m-smithadvocates.com/mining-minerals#faq",
        "qa": [
            (
                "What licences are required to mine in Uganda?",
                "Depending on the scale and stage of operations, you may need a prospecting licence, location licence, or mining lease, all issued by the Directorate of Geological Survey and Mines. For artisanal mining, a separate artisanal mining permit is required. We guide clients through the correct licence type and application process for their specific situation."
            ),
            (
                "How are mineral royalties calculated in Uganda?",
                "Mineral royalties under Uganda's Mining Act are calculated as a percentage of the gross value of minerals produced, with rates varying by mineral type. Gold, for example, attracts a 3% royalty. We advise on royalty obligations, reporting requirements, and tax planning strategies compliant with Uganda's mining fiscal regime."
            ),
            (
                "What are the environmental obligations for mining operations in Uganda?",
                "Mining operators must conduct an Environmental Impact Assessment (EIA) approved by the National Environment Management Authority (NEMA), prepare an environmental management plan, and comply with environmental monitoring requirements throughout the operation. We advise on environmental compliance and help clients establish the necessary frameworks before commencing operations."
            ),
        ],
    },
}

CLOSING = '        }\n      ]\n    }\n    </script>'

def build_faqpage(faq_id, qa_pairs):
    items = []
    for q, a in qa_pairs:
        items.append(
            '            {\n'
            '              "@type": "Question",\n'
            f'              "name": {json_str(q)},\n'
            '              "acceptedAnswer": {\n'
            '                "@type": "Answer",\n'
            f'                "text": {json_str(a)}\n'
            '              }\n'
            '            }'
        )
    entities = ',\n'.join(items)
    return (
        '        },\n'
        '        {\n'
        '          "@type": "FAQPage",\n'
        f'          "@id": "{faq_id}",\n'
        '          "mainEntity": [\n'
        f'{entities}\n'
        '          ]\n'
        '        }\n'
        '      ]\n'
        '    }\n'
        '    </script>'
    )

def json_str(s):
    escaped = s.replace('\\', '\\\\').replace('"', '\\"')
    return f'"{escaped}"'

for filename, data in faq_data.items():
    html = read(filename)
    if "FAQPage" in html:
        print(f"  {filename}: FAQPage already present — skipped")
        continue
    if CLOSING not in html:
        print(f"  {filename}: closing pattern not found — skipped")
        continue
    replacement = build_faqpage(data["id"], data["qa"])
    html = html.replace(CLOSING, replacement)
    write(filename, html)

# ── 4. Update sitemap lastmod dates ──────────────────────────────────────────

print("\n=== Fix 4: Sitemap lastmod dates ===")

sitemap = read("sitemap.xml")

# All pages were updated today
updated_urls = [
    "https://www.m-smithadvocates.com/",
    "https://www.m-smithadvocates.com/about",
    "https://www.m-smithadvocates.com/practice-areas",
    "https://www.m-smithadvocates.com/team",
    "https://www.m-smithadvocates.com/contact",
    "https://www.m-smithadvocates.com/litigation-arbitration",
    "https://www.m-smithadvocates.com/real-estate",
    "https://www.m-smithadvocates.com/intellectual-property",
    "https://www.m-smithadvocates.com/oil-gas-petroleum",
    "https://www.m-smithadvocates.com/mining-minerals",
    "https://www.m-smithadvocates.com/employment-labour",
    "https://www.m-smithadvocates.com/corporate-commercial",
    "https://www.m-smithadvocates.com/immigration",
    "https://www.m-smithadvocates.com/insurance",
    "https://www.m-smithadvocates.com/human-rights",
    "https://www.m-smithadvocates.com/eac-law",
]

# Replace any existing lastmod value for each url
for url in updated_urls:
    pattern = rf'(<loc>{re.escape(url)}</loc>\s*<lastmod>)[^<]+(</lastmod>)'
    replacement = r'\g<1>2026-05-22\g<2>'
    sitemap = re.sub(pattern, replacement, sitemap)

write("sitemap.xml", sitemap)

print("\nDone.")
