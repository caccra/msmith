"""
AI Search SEO pass:
1. max-snippet meta on all indexable pages
2. Author meta tag
3. WebPage + speakable schema node on practice area pages
4. YMYL disclaimer + Last reviewed date on practice area pages
5. FAQ schema additions for new guide content
"""
import os, re, json

ROOT = os.path.dirname(os.path.abspath(__file__))

def read(name):
    with open(os.path.join(ROOT, name), encoding='utf-8') as f:
        return f.read()

def write(name, content):
    with open(os.path.join(ROOT, name), 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  {name}")

# ── Practice area pages and their page metadata ──────────────────────────────
PRACTICE_PAGES = {
    'corporate-commercial.html': {
        'slug': 'corporate-commercial',
        'title': 'Corporate & Commercial Lawyers | M-Smith Uganda',
        'desc': 'Top corporate and commercial lawyers in Uganda. M-Smith Advocates offers company formation, governance, M&A, and commercial contracts in Kampala.',
        'new_faqs': [
            {
                'q': 'What is the minimum investment for a foreign investor in Uganda?',
                'a': 'Foreign investors are required to register with the Uganda Investment Authority (UIA) with a minimum capital of USD 250,000. Citizens of EAC Partner States qualify at a lower threshold of USD 100,000. UIA registration grants access to investment protections, tax incentives, and facilitates work permit applications for key staff.'
            },
            {
                'q': 'What are the fiduciary duties of a company director under Ugandan law?',
                'a': 'Under the Companies Act 2012, directors owe duties to act in good faith in the best interests of the company, exercise reasonable care and skill, avoid conflicts of interest, not use company information for personal gain, and act within the powers granted by the articles of association. Breach of fiduciary duty can result in personal liability and civil claims by the company or shareholders.'
            }
        ]
    },
    'real-estate.html': {
        'slug': 'real-estate',
        'title': 'Real Estate Lawyers Uganda | Property Law | M-Smith',
        'desc': 'Trusted real estate lawyers in Uganda. M-Smith Advocates handles property transactions, title verification, conveyancing & land disputes in Kampala.',
        'new_faqs': [
            {
                'q': 'What is a Certificate of Title in Uganda and why does it matter?',
                'a': 'A Certificate of Title is the official document issued by the Uganda Registration Services Bureau (URSB) evidencing registered ownership of land. Under the Registration of Titles Act (Cap 230), a registered title is generally indefeasible — meaning it cannot be challenged except on grounds of fraud. Verifying a title means physically confirming the certificate against the URSB register, not relying on a copy provided by the seller.'
            },
            {
                'q': 'What is stamp duty on property in Uganda?',
                'a': 'Stamp duty on property transfers in Uganda is 1% of the declared property value, payable by the buyer to the Uganda Revenue Authority (URA) before the transfer instrument can be lodged at URSB. Failure to pay stamp duty prevents legal registration of the transfer in the buyer\'s name.'
            }
        ]
    },
    'immigration.html': {
        'slug': 'immigration',
        'title': 'Immigration Lawyers Uganda | Work Permits & Visas',
        'desc': 'Expert immigration lawyers in Uganda. M-Smith Advocates handles work permits, entry permits, residency, visas, and citizenship matters in Kampala.',
        'new_faqs': [
            {
                'q': 'What documents are required for a Class G work permit in Uganda?',
                'a': 'A Class G work permit application requires: a completed DCIC Form 11 signed by the employer, a valid passport, certified copies of qualifications, Certificate of Incorporation and Trading Licence of the employer, an offer letter confirming position and salary, a skills justification letter demonstrating the role cannot be filled by a Ugandan, a letter of undertaking from the employer, and two passport photographs. Professional roles may also require endorsement from the relevant Ugandan professional body.'
            },
            {
                'q': 'What is the minimum investment for a Class A investor permit in Uganda?',
                'a': 'A Class A (Investor) Entry Permit requires a Uganda Investment Authority (UIA) Investment Licence, which has a minimum capital threshold of USD 250,000 for non-EAC foreign nationals and USD 100,000 for citizens of EAC Partner States. The investor must also provide proof of capital introduction, company incorporation documents, and a business plan. Processing typically takes 6–12 weeks after submission of a complete application.'
            }
        ]
    },
    'employment-labour.html': {
        'slug': 'employment-labour',
        'title': 'Employment & Labour Lawyers Uganda | M-Smith',
        'desc': 'Expert employment and labour lawyers in Uganda. M-Smith Advocates handles employment contracts, HR compliance, redundancy, and labour disputes in Kampala.',
        'new_faqs': [
            {
                'q': 'How much notice must an employer give to terminate a monthly-paid employee in Uganda?',
                'a': 'Under Section 58 of the Employment Act 2006, an employer must give a monthly-paid employee a minimum of one month\'s notice (or one month\'s pay in lieu of notice) before termination. Shorter periods apply for weekly or daily-paid employees. These are statutory minimums — employment contracts may provide longer notice periods, and any contract term purporting to reduce them below the statutory floor is unenforceable.'
            },
            {
                'q': 'What are the annual leave entitlements for employees in Uganda?',
                'a': 'Under the Employment Act 2006, employees are entitled to a minimum of 21 working days\' paid annual leave after 12 months of continuous employment. Leave accrues monthly and must not be forfeited without compensation. Employees are also entitled to 60 working days\' maternity leave (paid), 4 working days\' paternity leave (paid), and up to one month on full pay and two months on half pay for sick leave per year.'
            },
            {
                'q': 'How much must employers contribute to NSSF in Uganda?',
                'a': 'Employers must contribute 10% of each employee\'s gross monthly salary to the National Social Security Fund (NSSF), while employees contribute 5% of their gross salary (deducted from pay). Total NSSF contribution is therefore 15% of gross salary per employee per month. Failure to deduct, remit, or register employees with NSSF is a criminal offence under the NSSF Act and attracts significant penalties.'
            }
        ]
    },
    'eac-law.html': {
        'slug': 'eac-law',
        'title': 'EAC Law Lawyers Uganda | M-Smith Advocates',
        'desc': 'Expert EAC law advocates in Uganda. M-Smith Advocates advises on EAC legal frameworks, cross-border transactions, and regional compliance in Kampala.',
        'new_faqs': [
            {
                'q': 'What is the EAC Common External Tariff and how does it affect imports?',
                'a': 'The EAC Common External Tariff (CET) is the harmonised tariff applied to goods imported from outside the East African Community. It operates on a three-band structure: 0% for raw materials and capital goods, 10% for intermediate goods, and 25% for finished goods. All EAC Partner States apply the same CET rates, meaning a business importing machinery from outside the EAC pays the same duty rate whether it enters through Mombasa or Kampala.'
            },
            {
                'q': 'How do I obtain a Certificate of Origin for EAC trade?',
                'a': 'A Certificate of Origin (Form CO) for intra-EAC trade is issued by the competent authority in the exporting country — in Uganda, by the Uganda National Bureau of Standards (UNBS) or the Uganda Revenue Authority (URA). To qualify, the exported goods must meet the EAC Rules of Origin, generally requiring that goods are wholly produced in the EAC or have undergone sufficient value addition. The certificate must accompany the goods to qualify for duty-free treatment in the importing Partner State.'
            }
        ]
    },
    'litigation-arbitration.html': {
        'slug': 'litigation-arbitration',
        'title': 'Litigation & Arbitration Lawyers | M-Smith Uganda',
        'desc': 'Expert litigation and arbitration lawyers in Uganda. M-Smith Advocates provides court advocacy and dispute resolution in Kampala and across East Africa.',
        'new_faqs': []
    },
    'intellectual-property.html': {
        'slug': 'intellectual-property',
        'title': 'Intellectual Property Lawyers Uganda | M-Smith',
        'desc': 'Expert intellectual property lawyers in Uganda. M-Smith Advocates handles trademark registration, patents, copyright, and IP enforcement in Kampala.',
        'new_faqs': []
    },
    'oil-gas-petroleum.html': {
        'slug': 'oil-gas-petroleum',
        'title': 'Oil & Gas Lawyers Uganda | M-Smith Advocates',
        'desc': 'Expert oil, gas, and petroleum lawyers in Uganda. M-Smith Advocates advises on licensing, energy transactions, and national content compliance in Kampala.',
        'new_faqs': []
    },
    'mining-minerals.html': {
        'slug': 'mining-minerals',
        'title': 'Mining & Minerals Lawyers Uganda | M-Smith',
        'desc': 'Expert mining and minerals lawyers in Uganda. M-Smith Advocates guides clients through mining licences, mineral agreements, and exploration compliance.',
        'new_faqs': []
    },
    'insurance.html': {
        'slug': 'insurance',
        'title': 'Insurance Law Lawyers in Uganda | M-Smith Advocates Kampala',
        'desc': 'Expert insurance law lawyers in Uganda. M-Smith Advocates handles insurance claims, policy disputes, and risk management legal advice in Kampala.',
        'new_faqs': []
    },
    'human-rights.html': {
        'slug': 'human-rights',
        'title': 'Human Rights Lawyers Uganda | M-Smith Advocates',
        'desc': 'Expert human rights lawyers in Uganda. M-Smith Advocates provides constitutional advocacy, civil liberties defense, and human rights litigation in Kampala.',
        'new_faqs': []
    },
}

DISCLAIMER = '''
                        <div class="animate-on-scroll" style="background:var(--bg-subtle,#f8f7f5); border-left:3px solid var(--accent-base); padding:var(--space-4) var(--space-5); border-radius:0 var(--radius-md) var(--radius-md) 0; margin-bottom:var(--space-6);">
                            <p style="margin:0; font-size:0.88rem; color:var(--text-muted); line-height:1.6;"><strong>General information only.</strong> This page provides general legal information, not legal advice. Laws change and individual circumstances vary. Contact M-Smith Advocates for advice specific to your situation.</p>
                        </div>
'''

LAST_REVIEWED = '<p class="animate-on-scroll" style="font-size:0.82rem; color:var(--text-muted); margin-top:var(--space-8); padding-top:var(--space-4); border-top:1px solid var(--border-subtle);">Last reviewed: May 2026 &mdash; M-Smith Advocates Legal Team</p>'

changed = []

for fname, meta in PRACTICE_PAGES.items():
    html = read(fname)
    orig = html
    slug = meta['slug']
    base = f"https://www.m-smithadvocates.com/{slug}"

    # 1. max-snippet
    html = html.replace(
        'content="index, follow"',
        'content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"')

    # 2. Author meta (after viewport)
    if 'name="author"' not in html:
        html = html.replace(
            '<meta name="viewport"',
            '<meta name="author" content="M-Smith Advocates">\n    <meta name="viewport"')

    # 3. WebPage + speakable schema node — add before </script> close of ld+json
    wp_node = f'''        ,{{
          "@type": "WebPage",
          "@id": "{base}#webpage",
          "url": "{base}",
          "name": "{meta['title']}",
          "description": "{meta['desc']}",
          "inLanguage": "en",
          "dateModified": "2025-05-22",
          "isPartOf": {{"@id": "https://www.m-smithadvocates.com/#website"}},
          "about": {{"@id": "https://www.m-smithadvocates.com/#organization"}},
          "speakable": {{
            "@type": "SpeakableSpecification",
            "cssSelector": [".practice-overview", ".faq-a", ".practice-sub-title"]
          }}
        }}'''

    if '"@type": "WebPage"' not in html:
        html = re.sub(r'(\s*\]\s*\}\s*\n\s*</script>)', wp_node + r'\1', html, count=1)

    # 4. Add new FAQs to FAQPage schema
    if meta['new_faqs']:
        for faq in meta['new_faqs']:
            q = faq['q'].replace('"', '\\"')
            a = faq['a'].replace('"', '\\"')
            new_q = f'''            ,{{
              "@type": "Question",
              "name": "{q}",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "{a}"
              }}
            }}'''
            # Insert before the closing ] of mainEntity
            if q not in html:
                html = re.sub(
                    r'("mainEntity":\s*\[.*?)(\s*\]\s*\})',
                    lambda m: m.group(1) + new_q + m.group(2),
                    html, count=1, flags=re.DOTALL)

    # 5. YMYL disclaimer after page-header section
    if 'General information only' not in html:
        html = html.replace(
            '<h2 class="practice-sub-title animate-on-scroll">What We Handle</h2>',
            DISCLAIMER + '\n                        <h2 class="practice-sub-title animate-on-scroll">What We Handle</h2>')

    # 6. Last reviewed date before "Back to all Practice Areas"
    if 'Last reviewed' not in html:
        html = html.replace(
            '<div class="animate-on-scroll" style="margin-top: var(--space-6); padding-top: var(--space-6); border-top: 1px solid var(--border-color);">',
            LAST_REVIEWED + '\n                        <div class="animate-on-scroll" style="margin-top: var(--space-6); padding-top: var(--space-6); border-top: 1px solid var(--border-color);">')

    if html != orig:
        write(fname, html)
        changed.append(fname)

# Also update max-snippet on non-practice indexable pages
for fname in ['index.html', 'about.html', 'team.html', 'practice-areas.html', 'contact.html']:
    html = read(fname)
    orig = html
    html = html.replace(
        'content="index, follow"',
        'content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"')
    if 'name="author"' not in html:
        html = html.replace(
            '<meta name="viewport"',
            '<meta name="author" content="M-Smith Advocates">\n    <meta name="viewport"')
    if html != orig:
        write(fname, html)
        changed.append(fname)

print(f"\nDone. {len(changed)} files updated.")
