import os, re

BASE = r"c:/Users/USER/Desktop/anti gravity/msmith"

DROPDOWN_HTML = """\
<li class="nav-item-dropdown">
                    <a href="practice-areas.html" class="nav-link {active}dropdown-toggle" aria-haspopup="true" aria-expanded="false">
                        Expertise
                        <svg class="dropdown-arrow" xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    </a>
                    <div class="dropdown-menu" role="menu">
                        <a href="practice-areas.html" class="dropdown-all-link">
                            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
                            All Practice Areas
                        </a>
                        <div class="dropdown-grid">
                            <a href="litigation-arbitration.html" class="dropdown-item {c_lit}">Litigation &amp; Arbitration</a>
                            <a href="real-estate.html" class="dropdown-item {c_re}">Real Estate &amp; Land</a>
                            <a href="intellectual-property.html" class="dropdown-item {c_ip}">Intellectual Property</a>
                            <a href="oil-gas-petroleum.html" class="dropdown-item {c_oil}">Oil, Gas &amp; Petroleum</a>
                            <a href="mining-minerals.html" class="dropdown-item {c_min}">Mining &amp; Minerals</a>
                            <a href="employment-labour.html" class="dropdown-item {c_emp}">Employment &amp; Labour</a>
                            <a href="corporate-commercial.html" class="dropdown-item {c_corp}">Corporate &amp; Commercial</a>
                            <a href="immigration.html" class="dropdown-item {c_imm}">Immigration Law</a>
                            <a href="insurance.html" class="dropdown-item {c_ins}">Insurance Law</a>
                            <a href="human-rights.html" class="dropdown-item {c_hr}">Human Rights</a>
                            <a href="eac-law.html" class="dropdown-item {c_eac}">EAC Law</a>
                        </div>
                    </div>
                </li>"""

# Old nav item patterns to replace (active or not)
OLD_ACTIVE   = '<li><a href="practice-areas.html" class="nav-link active">Expertise</a></li>'
OLD_INACTIVE = '<li><a href="practice-areas.html" class="nav-link">Expertise</a></li>'

# Map filename → which dropdown-item gets current-area class
CURRENT_MAP = {
    "litigation-arbitration.html": "c_lit",
    "real-estate.html":            "c_re",
    "intellectual-property.html":  "c_ip",
    "oil-gas-petroleum.html":      "c_oil",
    "mining-minerals.html":        "c_min",
    "employment-labour.html":      "c_emp",
    "corporate-commercial.html":   "c_corp",
    "immigration.html":            "c_imm",
    "insurance.html":              "c_ins",
    "human-rights.html":           "c_hr",
    "eac-law.html":                "c_eac",
}

# Pages where Expertise toggle itself should be active
EXPERTISE_ACTIVE = {"practice-areas.html"} | set(CURRENT_MAP.keys())

ALL_FILES = [
    "index.html", "about.html", "practice-areas.html",
    "team.html", "contact.html",
] + list(CURRENT_MAP.keys())

for fname in ALL_FILES:
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        print(f"  SKIP (not found): {fname}")
        continue

    with open(path, encoding="utf-8") as f:
        html = f.read()

    # Build current-area markers dict (all empty by default)
    markers = {k: "" for k in ["c_lit","c_re","c_ip","c_oil","c_min","c_emp","c_corp","c_imm","c_ins","c_hr","c_eac"]}
    if fname in CURRENT_MAP:
        markers[CURRENT_MAP[fname]] = "current-area "

    active = "active " if fname in EXPERTISE_ACTIVE else ""
    new_li = DROPDOWN_HTML.format(active=active, **markers)

    if OLD_ACTIVE in html:
        html = html.replace(OLD_ACTIVE, new_li)
        print(f"  Updated (active):   {fname}")
    elif OLD_INACTIVE in html:
        html = html.replace(OLD_INACTIVE, new_li)
        print(f"  Updated (inactive): {fname}")
    else:
        print(f"  NOT MATCHED:        {fname}")
        continue

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

print("\nDone.")
