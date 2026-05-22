"""
SEO fixes: C2, C4, C5 (partial), H4, H5, H7, H9 (partial), M11
Run once from the project root.
"""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))

def read(name):
    with open(os.path.join(ROOT, name), encoding='utf-8') as f:
        return f.read()

def write(name, content):
    with open(os.path.join(ROOT, name), 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  updated {name}")

# ─── Title / og:title / twitter:title replacements ───────────────────────────
TITLES = {
    'about.html': (
        'About Our Law Firm | Top Lawyers in Kampala Uganda | M-Smith Advocates',
        'About M-Smith Advocates | Top Law Firm in Uganda'),
    'eac-law.html': (
        'EAC Law Advocates in Uganda | East African Community | M-Smith Advocates Kampala',
        'EAC Law Lawyers Uganda | M-Smith Advocates'),
    'contact.html': (
        'Find Lawyers Near You in Kampala Uganda | Contact M-Smith Advocates',
        'Contact M-Smith Advocates | Lawyers in Kampala'),
    'practice-areas.html': (
        'Legal Services in Uganda | Practice Areas | M-Smith Advocates Kampala',
        'Practice Areas | Legal Services Uganda | M-Smith Advocates'),
    'team.html': (
        'Our Lawyers in Kampala Uganda | The Team | M-Smith Advocates',
        'Legal Team | M-Smith Advocates Uganda'),
    'litigation-arbitration.html': (
        'Litigation & Arbitration Lawyers in Uganda | M-Smith Advocates Kampala',
        'Litigation & Arbitration Lawyers | M-Smith Uganda'),
    'real-estate.html': (
        'Real Estate Lawyer Uganda | Property Law Kampala | M-Smith Advocates',
        'Real Estate Lawyers Uganda | Property Law | M-Smith'),
    'intellectual-property.html': (
        'Intellectual Property Lawyers in Uganda | M-Smith Advocates Kampala',
        'Intellectual Property Lawyers Uganda | M-Smith'),
    'oil-gas-petroleum.html': (
        'Oil, Gas & Petroleum Lawyers in Uganda | M-Smith Advocates Kampala',
        'Oil &amp; Gas Lawyers Uganda | M-Smith Advocates'),
    'mining-minerals.html': (
        'Mining & Minerals Lawyers in Uganda | M-Smith Advocates Kampala',
        'Mining &amp; Minerals Lawyers Uganda | M-Smith'),
    'employment-labour.html': (
        'Employment & Labour Lawyers in Uganda | M-Smith Advocates Kampala',
        'Employment &amp; Labour Lawyers Uganda | M-Smith'),
    'corporate-commercial.html': (
        'Corporate & Commercial Lawyers in Uganda | M-Smith Advocates Kampala',
        'Corporate &amp; Commercial Lawyers | M-Smith Uganda'),
    'immigration.html': (
        'Immigration Lawyers in Uganda | Work Permits & Visas | M-Smith Advocates Kampala',
        'Immigration Lawyers Uganda | Work Permits &amp; Visas'),
    'human-rights.html': (
        'Human Rights Lawyers in Uganda | Constitutional Law | M-Smith Advocates Kampala',
        'Human Rights Lawyers Uganda | M-Smith Advocates'),
}

# ─── Meta description replacements ────────────────────────────────────────────
META_DESC = {
    'index.html': (
        'M-Smith Advocates is one of the best law firms in Uganda, offering expert lawyers in Kampala for real estate, litigation, corporate law &amp; more. Call +(256) 782 776 074.',
        'M-Smith Advocates is one of the best law firms in Uganda, offering expert lawyers in Kampala for real estate, litigation, corporate law &amp; more.'),
    'practice-areas.html': (
        'Explore legal services offered by M-Smith Advocates in Uganda. From litigation to real estate law, our Kampala lawyers cover 11 practice areas across East Africa.',
        'Explore legal services offered by M-Smith Advocates in Uganda. From litigation to real estate law, our Kampala lawyers cover 11 practice areas.'),
    'eac-law.html': (
        'Expert EAC law advocates in Uganda. M-Smith Advocates advises on East African Community legal frameworks, cross-border transactions, and regional compliance from Kampala.',
        'Expert EAC law advocates in Uganda. M-Smith Advocates advises on EAC legal frameworks, cross-border transactions, and regional compliance in Kampala.'),
    'human-rights.html': (
        'Expert human rights lawyers in Uganda. M-Smith Advocates provides constitutional rights advocacy, civil liberties defense, and human rights litigation in Kampala.',
        'Expert human rights lawyers in Uganda. M-Smith Advocates provides constitutional advocacy, civil liberties defense, and human rights litigation in Kampala.'),
    'intellectual-property.html': (
        'Expert intellectual property lawyers in Uganda. M-Smith Advocates handles trademark registration, patents, copyright, and IP enforcement in Kampala and East Africa.',
        'Expert intellectual property lawyers in Uganda. M-Smith Advocates handles trademark registration, patents, copyright, and IP enforcement in Kampala.'),
    'litigation-arbitration.html': (
        'Expert litigation and arbitration lawyers in Uganda. M-Smith Advocates provides aggressive court advocacy and dispute resolution in Kampala and across East Africa.',
        'Expert litigation and arbitration lawyers in Uganda. M-Smith Advocates provides court advocacy and dispute resolution in Kampala and across East Africa.'),
    'mining-minerals.html': (
        'Expert mining and minerals lawyers in Uganda. M-Smith Advocates guides clients through mining licences, mineral agreements, and exploration compliance in Kampala.',
        'Expert mining and minerals lawyers in Uganda. M-Smith Advocates guides clients through mining licences, mineral agreements, and exploration compliance.'),
    'real-estate.html': (
        'Trusted real estate lawyers in Uganda. M-Smith Advocates handles property transactions, title verification, conveyancing &amp; land disputes in Kampala. Book a consultation.',
        'Trusted real estate lawyers in Uganda. M-Smith Advocates handles property transactions, title verification, conveyancing &amp; land disputes in Kampala.'),
    'team.html': (
        'Meet the experienced advocates at M-Smith Advocates, one of the best law firms in Uganda. Our qualified lawyers in Kampala deliver exceptional legal representation.',
        'Meet the legal team at M-Smith Advocates, one of Uganda\'s best law firms. Our qualified lawyers in Kampala deliver exceptional legal representation.'),
}

# ─── Pages missing og:image ────────────────────────────────────────────────────
NEEDS_OG_IMAGE = ['about.html', 'practice-areas.html', 'team.html', 'contact.html', 'real-estate.html']
OG_IMAGE_TAG = '<meta property="og:image" content="https://www.m-smithadvocates.com/logo.png">\n'
TWITTER_IMAGE_TAG = '    <meta name="twitter:image" content="https://www.m-smithadvocates.com/logo.png">\n'

# ─── Process each file ────────────────────────────────────────────────────────
all_html = [f for f in os.listdir(ROOT) if f.endswith('.html')]
changed = set()

for fname in all_html:
    html = read(fname)
    orig = html

    # 1. Title tag replacements (title, og:title, twitter:title)
    if fname in TITLES:
        old_t, new_t = TITLES[fname]
        html = html.replace(f'<title>{old_t}</title>', f'<title>{new_t}</title>')
        html = html.replace(f'content="{old_t}"', f'content="{new_t}"')

    # 2. Meta description replacements
    if fname in META_DESC:
        old_d, new_d = META_DESC[fname]
        html = html.replace(old_d, new_d)

    # 3. Add og:image after og:url where missing
    if fname in NEEDS_OG_IMAGE and 'og:image' not in html:
        html = html.replace(
            '<meta property="og:site_name"',
            OG_IMAGE_TAG + '    <meta property="og:site_name"')

    # 4. Add twitter:image after twitter:description where missing
    if fname in NEEDS_OG_IMAGE and 'twitter:image' not in html:
        html = re.sub(
            r'(<meta name="twitter:description"[^>]+>)',
            r'\1\n' + '    <meta name="twitter:image" content="https://www.m-smithadvocates.com/logo.png">',
            html)

    # 5. Upgrade twitter:card from summary to summary_large_image
    html = html.replace(
        '<meta name="twitter:card" content="summary">',
        '<meta name="twitter:card" content="summary_large_image">')

    if html != orig:
        write(fname, html)
        changed.add(fname)

print(f"\nDone. {len(changed)} file(s) updated.")
