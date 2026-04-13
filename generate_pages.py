import os

BASE = r"c:/Users/USER/Desktop/anti gravity/msmith"

FOOTER_HTML = """
    <footer class="site-footer">
        <div class="container footer-container">
            <div class="footer-brand">
                <a href="/" class="brand-logo">
                    <img src="logo.png" alt="M-Smith Advocates Logo" style="max-height: 60px;">
                </a>
                <p class="footer-tagline" style="margin-bottom: 16px;">Pursuing justice with integrity and excellence since 2013.</p>
                <div class="footer-contact-info" style="display: flex; flex-direction: column; gap: 8px;">
                    <a href="tel:+256782776074" class="footer-contact-link">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--accent-base); flex-shrink: 0;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                        <span>+(256) 782 776 074</span>
                    </a>
                    <a href="mailto:info@m-smithadvocates.com" class="footer-contact-link">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--accent-base); flex-shrink: 0;"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                        <span>info@m-smithadvocates.com</span>
                    </a>
                </div>
            </div>
            <div class="footer-links-group">
                <h4 class="footer-heading">Quick Links</h4>
                <ul class="footer-links">
                    <li><a href="/">Home</a></li>
                    <li><a href="about.html">About Us</a></li>
                    <li><a href="practice-areas.html">Expertise</a></li>
                    <li><a href="team.html">Our Team</a></li>
                    <li><a href="contact.html">Contact Us</a></li>
                </ul>
            </div>
            <div class="footer-links-group">
                <h4 class="footer-heading">Legal</h4>
                <ul class="footer-links">
                    <li><a href="#">Privacy Policy</a></li>
                    <li><a href="#">Terms of Service</a></li>
                    <li><a href="#">Disclaimer</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <div class="container">
                <p>&copy; <span id="current-year"></span> M-Smith Advocates. All rights reserved.</p>
            </div>
        </div>
    </footer>
    <script src="script.js"></script>
"""

ALL_AREAS = [
    ("Litigation & Arbitration",   "litigation-arbitration.html"),
    ("Real Estate & Land",         "real-estate.html"),
    ("Intellectual Property",      "intellectual-property.html"),
    ("Oil, Gas & Petroleum Law",   "oil-gas-petroleum.html"),
    ("Mining & Mineral Resources", "mining-minerals.html"),
    ("Employment & Labour",        "employment-labour.html"),
    ("Corporate & Commercial",     "corporate-commercial.html"),
    ("Immigration Law",            "immigration.html"),
    ("Insurance Law",              "insurance.html"),
    ("Human Rights",               "human-rights.html"),
    ("EAC Law",                    "eac-law.html"),
]

PAGES = [
    {
        "filename": "litigation-arbitration.html",
        "title": "Litigation & Arbitration",
        "subtitle": "Aggressive advocacy and strategic planning for court disputes and arbitration across East Africa.",
        "overview": "We provide full-service legal representation in court disputes and independent arbitration processes throughout East Africa. Our approach is characterised by rigorous preparation, aggressive advocacy, and strategic planning — ensuring our clients' interests are staunchly protected at every stage.",
        "body": [
            "Our litigation team has extensive experience handling complex commercial disputes, contractual disagreements, and multi-party civil litigation across the regional courts of Uganda and East Africa. We understand that litigation is not always the desired outcome, and where appropriate, we pursue negotiated settlements that protect our clients' interests efficiently.",
            "For arbitration matters, we represent clients before both domestic and international arbitral tribunals, bringing the same level of preparation and advocacy that has defined our courtroom practice.",
        ],
        "services": [
            "Commercial and civil litigation",
            "Contractual dispute resolution",
            "Arbitration representation",
            "Mediation and negotiated settlements",
            "Appeal proceedings",
            "Enforcement of judgments and awards",
            "Injunctions and interim relief",
            "Cross-border dispute resolution",
        ],
    },
    {
        "filename": "real-estate.html",
        "title": "Real Estate & Land Transactions",
        "subtitle": "Expert guidance through property and land transactions, eliminating fraud and streamlining every acquisition.",
        "overview": "Navigating the property market in East Africa requires deep local knowledge and meticulous due diligence. We provide comprehensive legal guidance through the complexities of buying, selling, and developing land — with a specific focus on eliminating fraud risks and ensuring clean, secure transactions.",
        "body": [
            "Our real estate team handles transactions ranging from individual residential plots to large-scale commercial and industrial land deals. We work with developers, investors, financial institutions, and individual buyers to provide end-to-end legal support from initial due diligence through to final registration.",
            "With the prevalence of fraudulent land transactions in the region, our verification process is thorough and systematic — giving our clients confidence that every acquisition is legally sound.",
        ],
        "services": [
            "Title verification and due diligence",
            "Sale agreement drafting and review",
            "Property transfer and registration",
            "Land lease agreements",
            "Mortgage and charge documentation",
            "Property dispute resolution",
            "Conveyancing services",
            "Developer and investor advisory",
        ],
    },
    {
        "filename": "intellectual-property.html",
        "title": "Intellectual Property",
        "subtitle": "Protecting your ideas, brands, and innovations through expert IP registration and enforcement across East Africa.",
        "overview": "Your intellectual property is among your most valuable assets. We provide comprehensive legal support for Patents, Trade Marks, and Copyrights — from registration strategy through to active enforcement and litigation within the East African region.",
        "body": [
            "Whether you are a startup protecting your brand, a creator safeguarding your work, or a corporation enforcing your patents, our IP team brings the expertise to navigate both national and regional registration processes effectively.",
            "We also advise on IP licensing structures, help businesses draft robust licensing agreements, and represent clients in IP disputes before domestic courts and the African Regional Intellectual Property Organization (ARIPO).",
        ],
        "services": [
            "Trademark registration and renewal",
            "Patent filing and prosecution",
            "Copyright registration",
            "ARIPO regional applications",
            "IP licensing and assignment agreements",
            "Infringement investigations and litigation",
            "Brand protection strategy",
            "Trade secret protection",
        ],
    },
    {
        "filename": "oil-gas-petroleum.html",
        "title": "Oil, Gas & Petroleum Law",
        "subtitle": "Specialized legal consultancy for the energy sector — from licensing to production and national content compliance.",
        "overview": "As the East African energy sector continues to evolve, we offer specialized legal consultancy on Exploration, Development, and Production regulations. We help clients navigate national content requirements, sector participation frameworks, and complex licensing processes that govern the oil and gas industry.",
        "body": [
            "Our energy law team advises international oil companies, national oil companies, service contractors, and local content companies operating across the region. We have in-depth knowledge of Uganda's Petroleum (Exploration, Development and Production) Act and related regulations.",
            "We support clients from the earliest stages of exploration licensing through to production sharing agreements, field development plans, and decommissioning — providing practical, commercially-focused legal advice throughout.",
        ],
        "services": [
            "Exploration and production licensing",
            "Production sharing agreement advisory",
            "National content compliance",
            "Regulatory filing and approvals",
            "Joint operating agreements",
            "Farm-in and farm-out transactions",
            "Environmental compliance advisory",
            "Decommissioning planning",
        ],
    },
    {
        "filename": "mining-minerals.html",
        "title": "Mining & Mineral Resources",
        "subtitle": "Expert legal guidance through the regulatory frameworks governing mineral exploration and exploitation in East Africa.",
        "overview": "The mining and extractives sector presents unique legal complexities — from securing the right licenses to managing community relations and environmental obligations. We advise mining companies, investors, and local operators on navigating the full spectrum of legal requirements in East Africa.",
        "body": [
            "Our mining law practice covers all stages of the mining lifecycle, from initial prospecting licenses to full-scale mining leases and beyond. We have experience advising on both artisanal and large-scale mining operations, and understand the interplay between mining regulations, land law, and environmental requirements.",
            "We also assist clients with community development agreements and benefit-sharing frameworks, helping to build sustainable relationships between mining operations and local communities.",
        ],
        "services": [
            "Prospecting and exploration licenses",
            "Mining lease applications",
            "Mineral export permits",
            "Environmental impact advisory",
            "Community development agreements",
            "Mining contracts and joint ventures",
            "Royalty and tax advisory",
            "Regulatory compliance and reporting",
        ],
    },
    {
        "filename": "employment-labour.html",
        "title": "Employment & Labour",
        "subtitle": "Comprehensive legal counsel on workplace relations, employment contracts, and the resolution of complex labour disputes.",
        "overview": "The employment relationship is one of the most complex in commercial law. We provide expert legal counsel to both employers and employees across all aspects of workplace relations — from drafting robust employment contracts to representing parties in labour disputes before the Industrial Court.",
        "body": [
            "Our employment law team advises multinationals, SMEs, NGOs, and individual employees across Uganda and the broader East African region. We understand the importance of balancing commercial objectives with legal compliance and employee rights.",
            "We also help businesses develop comprehensive HR policies, staff handbooks, and internal grievance procedures — providing a framework that protects the organization while treating employees fairly.",
        ],
        "services": [
            "Employment contract drafting and review",
            "Staff handbook and HR policy development",
            "Unfair dismissal and redundancy claims",
            "Industrial Court representation",
            "Collective bargaining and union relations",
            "Workplace investigation support",
            "Executive severance negotiations",
            "Expatriate employment advisory",
        ],
    },
    {
        "filename": "corporate-commercial.html",
        "title": "Corporate & Commercial",
        "subtitle": "Full-spectrum corporate legal services — from company secretarial to complex commercial transactions and governance.",
        "overview": "Our corporate desk serves as the trusted legal partner for businesses at every stage of their growth — from initial incorporation through to complex commercial transactions, mergers, and governance matters. We act as general legal advisors, ensuring your organization operates in full compliance with applicable law.",
        "body": [
            "We provide both transactional and advisory services, helping businesses structure deals, negotiate commercial contracts, manage corporate governance, and navigate regulatory requirements. Our team is experienced in working with multinationals, family businesses, NGOs, and public sector entities.",
            "Our company secretarial services ensure that your statutory obligations are met on time and in full — giving business owners and boards the confidence to focus on growth.",
        ],
        "services": [
            "Company incorporation and registration",
            "Company secretarial services",
            "Corporate governance advisory",
            "Commercial contract drafting and negotiation",
            "Mergers, acquisitions, and restructuring",
            "Due diligence",
            "Debt recovery and collections",
            "Property management legal support",
        ],
    },
    {
        "filename": "immigration.html",
        "title": "Immigration Law",
        "subtitle": "Legal assistance for residency, work permits, visas, and all immigration-related regulatory matters in East Africa.",
        "overview": "Navigating immigration law in East Africa can be complex and time-sensitive. We provide comprehensive legal assistance for individuals, families, and businesses dealing with residency applications, work permits, visas, and other immigration-related regulatory matters in Uganda and the broader EAC region.",
        "body": [
            "Our immigration team assists both individuals relocating to Uganda and businesses bringing in expatriate staff. We manage the entire application process — from initial assessment through to submission and follow-up with the relevant authorities — minimising delays and ensuring compliance.",
            "We also advise on long-term immigration strategy for businesses, helping to structure workforce arrangements that meet both operational needs and regulatory requirements.",
        ],
        "services": [
            "Work permit applications and renewals",
            "Residence permit applications",
            "Entry visa advisory",
            "Dependent and spouse permits",
            "Business immigration strategy",
            "Special pass applications",
            "EAC free movement advisory",
            "Immigration compliance audits",
        ],
    },
    {
        "filename": "insurance.html",
        "title": "Insurance Law",
        "subtitle": "Specialized legal services for insurance policy interpretation, complex claims resolution, and risk management.",
        "overview": "Insurance disputes are often technically complex and commercially significant. We provide specialized legal services to both insurers and the insured — helping clients navigate policy interpretation, complex claims, and regulatory requirements within the East African insurance market.",
        "body": [
            "Our insurance law team has experience across the full range of insurance product lines, including property, liability, marine, life, and professional indemnity insurance. We understand the technical language of insurance contracts and the regulatory framework that governs the industry in Uganda.",
            "For insurers, we provide advisory support on underwriting documentation, policy wording, and claims handling. For policyholders, we advocate for fair and timely settlement of legitimate claims — and pursue litigation where insurers act in bad faith.",
        ],
        "services": [
            "Insurance policy interpretation",
            "Complex claims negotiation and resolution",
            "Insurer defense representation",
            "Policyholder advocacy",
            "Insurance litigation",
            "Subrogation and recovery actions",
            "Regulatory compliance advisory",
            "Reinsurance matters",
        ],
    },
    {
        "filename": "human-rights.html",
        "title": "Human Rights",
        "subtitle": "Unwavering advocacy and legal support for human rights issues — upholding justice, dignity, and constitutional protections.",
        "overview": "Human rights law is at the core of our firm's values. We provide dedicated advocacy and legal support for individuals and groups whose fundamental rights have been violated — ensuring that constitutional protections and international human rights standards are upheld.",
        "body": [
            "Our human rights practice covers constitutional rights petitions, public interest litigation, and representation before domestic courts and regional human rights mechanisms. We work with individuals, civil society organizations, and communities who face discrimination, unlawful detention, or denial of fundamental freedoms.",
            "We believe that access to justice is itself a human right, and we are committed to making expert legal representation available to those who need it most.",
        ],
        "services": [
            "Constitutional rights petitions",
            "Public interest litigation",
            "Unlawful detention and habeas corpus",
            "Discrimination and equality claims",
            "Freedom of expression and assembly",
            "Land rights and eviction challenges",
            "Refugee and asylum legal support",
            "Regional human rights body submissions",
        ],
    },
    {
        "filename": "eac-law.html",
        "title": "EAC Law",
        "subtitle": "Niche expertise in regional legal frameworks and cross-border legalities within the East African Community.",
        "overview": "The East African Community represents one of the most dynamic regional integration frameworks in Africa. We bring niche expertise in EAC legal frameworks, cross-border trade legalities, and the evolving protocols that govern commerce, investment, and dispute resolution within the Community.",
        "body": [
            "Our EAC law practice supports businesses, investors, and individuals operating across Uganda, Kenya, Tanzania, Rwanda, Burundi, South Sudan, and the DRC. We advise on the legal implications of EAC protocols — from the Customs Union and Common Market to the emerging Monetary Union.",
            "We also represent clients before the East African Court of Justice (EACJ) and advise on how to leverage the EAC framework to structure cross-border transactions, protect investments, and resolve regional disputes effectively.",
        ],
        "services": [
            "EAC treaty and protocol interpretation",
            "Cross-border trade facilitation",
            "Common Market compliance advisory",
            "East African Court of Justice representation",
            "Regional investment structuring",
            "Customs Union advisory",
            "Cross-border dispute resolution",
            "Regional regulatory compliance",
        ],
    },
]


def build_sidebar_links(current_filename):
    items = ""
    for name, fname in ALL_AREAS:
        css = ' class="current"' if fname == current_filename else ''
        items += f'                        <a href="{fname}"{css}>{name}</a>\n'
    return items


def build_page(p):
    sidebar_links = build_sidebar_links(p["filename"])
    services_html = "".join(f"                        <li>{s}</li>\n" for s in p["services"])
    body_html = "".join(
        f'                    <p class="practice-body-text animate-on-scroll">{t}</p>\n'
        for t in p["body"]
    )
    title_lower = p["title"].lower()

    return f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{p['subtitle']} M-Smith Advocates, Kampala.">
    <title>{p['title']} | M-Smith Advocates</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=EB+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Lato:wght@300;400;700&family=Manrope:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>

<body data-theme="light">
    <header class="site-header">
        <div class="container header-container">
            <a href="/" class="brand-logo">
                <img src="logo.png" alt="M-Smith Advocates Logo" style="max-height: 50px;">
            </a>
            <button class="mobile-menu-toggle" aria-label="Toggle Navigation" aria-expanded="false" aria-controls="primary-navigation">
                <span class="hamburger-line"></span>
                <span class="hamburger-line"></span>
                <span class="hamburger-line"></span>
            </button>
            <nav id="primary-navigation" class="primary-navigation">
                <ul class="nav-list">
                    <li><a href="/" class="nav-link">Home</a></li>
                    <li><a href="about.html" class="nav-link">About</a></li>
                    <li><a href="practice-areas.html" class="nav-link active">Expertise</a></li>
                    <li><a href="team.html" class="nav-link">The Team</a></li>
                    <li><a href="contact.html" class="nav-link">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main id="main-content">
        <section class="page-header section-padding">
            <div class="container animate-on-scroll">
                <div class="breadcrumb">
                    <a href="practice-areas.html">Practice Areas</a>
                    <span>/</span>
                    <span style="color: rgba(255,255,255,0.7);">{p['title']}</span>
                </div>
                <span class="section-eyebrow" style="color: rgba(219,167,89,0.85);">Practice Area</span>
                <h1 class="section-title">{p['title']}</h1>
                <p class="section-description">{p['subtitle']}</p>
            </div>
        </section>

        <section class="section-padding">
            <div class="container">
                <div class="practice-detail-grid">
                    <div class="practice-main">
                        <p class="practice-overview animate-on-scroll">{p['overview']}</p>

{body_html}
                        <h2 class="practice-sub-title animate-on-scroll">What We Handle</h2>
                        <ul class="practice-services-list animate-on-scroll">
{services_html}                        </ul>

                        <div class="animate-on-scroll" style="margin-top: var(--space-6); padding-top: var(--space-6); border-top: 1px solid var(--border-color);">
                            <a href="practice-areas.html" style="color: var(--text-muted); font-size: 0.9rem; display: inline-flex; align-items: center; gap: 6px; transition: color 0.3s;">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                                Back to all Practice Areas
                            </a>
                        </div>
                    </div>

                    <aside class="practice-sidebar animate-on-scroll delay-2">
                        <div class="sidebar-card sidebar-card-cta">
                            <h3>Ready to Get Started?</h3>
                            <p>Our team is ready to provide expert legal counsel for your {title_lower} needs.</p>
                            <a href="contact.html" class="btn btn-primary">Book a Consultation</a>
                        </div>

                        <div class="sidebar-card">
                            <h3>Contact Us Directly</h3>
                            <div style="display: flex; flex-direction: column; gap: 12px; margin-top: var(--space-2);">
                                <a href="tel:+256782776074" style="display: flex; align-items: center; gap: 10px; color: var(--text-muted); font-size: 0.9rem;">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--accent-base); flex-shrink: 0;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                                    +(256) 782 776 074
                                </a>
                                <a href="mailto:info@m-smithadvocates.com" style="display: flex; align-items: center; gap: 10px; color: var(--text-muted); font-size: 0.9rem;">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--accent-base); flex-shrink: 0;"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                                    info@m-smithadvocates.com
                                </a>
                            </div>
                        </div>

                        <div class="sidebar-card">
                            <h3>Other Practice Areas</h3>
                            <div class="sidebar-areas-list">
{sidebar_links}                            </div>
                        </div>
                    </aside>
                </div>
            </div>
        </section>
    </main>
{FOOTER_HTML}
</body>
</html>
"""


for p in PAGES:
    path = os.path.join(BASE, p["filename"])
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_page(p))
    print(f"Created: {p['filename']}")

print("Done — 11 pages generated.")
