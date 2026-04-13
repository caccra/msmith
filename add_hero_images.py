import os, re

BASE = r"c:/Users/USER/Desktop/anti gravity/msmith"

# Map each page to its best hero image
IMAGE_MAP = {
    "litigation-arbitration.html": "images/m-smithadvocates%20Litigation.png",
    "real-estate.html":            "images/oleksandrpidvalnyi-real-estate-6688945.jpg",
    "intellectual-property.html":  "images/M-Smithadvocates-Intellectual-property.jpg",
    "oil-gas-petroleum.html":      "images/m-smithadvocates_Oil%20and%20gas.webp",
    "mining-minerals.html":        "images/fietzfotos-architecture-5999913.jpg",
    "employment-labour.html":      "images/activedia-law-1063249.jpg",
    "corporate-commercial.html":   "images/m-smithadvocates_commercial%20and%20corporate%20law.png",
    "immigration.html":            "images/m-smithadvocates_Immigration%20Law.jpg",
    "insurance.html":              "images/m-smithadvocates_Insurance%20law%20(1).jpg",
    "human-rights.html":           "images/cqf-avocat-justice-2755765.jpg",
    "eac-law.html":                "images/M-smithadvocates-EAC-.png",
}

OLD = '<section class="page-header section-padding">'

for fname, img in IMAGE_MAP.items():
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        print(f"  SKIP (not found): {fname}")
        continue

    with open(path, encoding="utf-8") as f:
        html = f.read()

    new = f'<section class="page-header section-padding" style="background-image: url(\'{img}\');">'

    if OLD in html:
        html = html.replace(OLD, new)
        print(f"  Updated: {fname}")
    elif 'background-image' in html and 'page-header' in html:
        print(f"  Already has bg image: {fname}")
        continue
    else:
        print(f"  NOT MATCHED: {fname}")
        continue

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

print("\nDone.")
