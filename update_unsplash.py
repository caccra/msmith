import os, re

BASE = r"c:/Users/USER/Desktop/anti gravity/msmith"

# Unsplash photo IDs chosen per practice area
# Format: https://images.unsplash.com/photo-{ID}?auto=format&fit=crop&w=800&q=80
UNSPLASH = {
    "litigation":  "FaTLrG5-ViE",   # wooden gavel on dark surface
    "real_estate": "-t6ihNradj8",   # aerial suburban neighbourhood
    "ip":          "fIq0tET6llw",   # person holding lightbulb
    "oil":         "pPjKPDLTyYw",   # oil refinery towers against blue sky
    "mining":      "Mk2ls9UBO2E",   # excavators at mining area
    "employment":  "FD9ncnQo9Ew",   # business meeting top-view
    "corporate":   "GWe0dlVD9e0",   # oval conference table & chairs
    "immigration": "0QcSnCM0aMc",   # person holding passports
    "insurance":   "nGQHF5opInc",   # silhouette with umbrella
    "humanrights": "qDhm-RwJbaY",   # people marching with protest signs
    "eac":         "LPvlpdZ99O0",   # East African Community passport
}

def cdn(photo_id, w=800):
    return f"https://images.unsplash.com/photo-{photo_id}?auto=format&fit=crop&w={w}&q=80"

# ── Local src → Unsplash CDN (cards in index.html & practice-areas.html) ──
SRC_REPLACEMENTS = [
    # Litigation
    ('src="images/m-smithadvocates%20Litigation.png"',
     f'src="{cdn(UNSPLASH["litigation"])}"'),
    # Real Estate
    ('src="images/oleksandrpidvalnyi-real-estate-6688945.jpg"',
     f'src="{cdn(UNSPLASH["real_estate"])}"'),
    # Intellectual Property
    ('src="images/M-Smithadvocates-Intellectual-property.jpg"',
     f'src="{cdn(UNSPLASH["ip"])}"'),
    # Oil Gas
    ('src="images/m-smithadvocates_Oil%20and%20gas.webp"',
     f'src="{cdn(UNSPLASH["oil"])}"'),
    # Mining
    ('src="images/fietzfotos-architecture-5999913.jpg"',
     f'src="{cdn(UNSPLASH["mining"])}"'),
    # Employment
    ('src="images/activedia-law-1063249.jpg"',
     f'src="{cdn(UNSPLASH["employment"])}"'),
    # Corporate
    ('src="images/m-smithadvocates_commercial%20and%20corporate%20law.png"',
     f'src="{cdn(UNSPLASH["corporate"])}"'),
    # Immigration
    ('src="images/m-smithadvocates_Immigration%20Law.jpg"',
     f'src="{cdn(UNSPLASH["immigration"])}"'),
    # Insurance
    ('src="images/m-smithadvocates_Insurance%20law%20(1).jpg"',
     f'src="{cdn(UNSPLASH["insurance"])}"'),
    # Human Rights
    ('src="images/cqf-avocat-justice-2755765.jpg"',
     f'src="{cdn(UNSPLASH["humanrights"])}"'),
    # EAC
    ('src="images/M-smithadvocates-EAC-.png"',
     f'src="{cdn(UNSPLASH["eac"])}"'),
]

# ── Inline background-image → Unsplash CDN (individual page headers) ──
BG_REPLACEMENTS = {
    "litigation-arbitration.html": (
        "images/m-smithadvocates%20Litigation.png",
        cdn(UNSPLASH["litigation"], 1200)),
    "real-estate.html": (
        "images/oleksandrpidvalnyi-real-estate-6688945.jpg",
        cdn(UNSPLASH["real_estate"], 1200)),
    "intellectual-property.html": (
        "images/M-Smithadvocates-Intellectual-property.jpg",
        cdn(UNSPLASH["ip"], 1200)),
    "oil-gas-petroleum.html": (
        "images/m-smithadvocates_Oil%20and%20gas.webp",
        cdn(UNSPLASH["oil"], 1200)),
    "mining-minerals.html": (
        "images/fietzfotos-architecture-5999913.jpg",
        cdn(UNSPLASH["mining"], 1200)),
    "employment-labour.html": (
        "images/activedia-law-1063249.jpg",
        cdn(UNSPLASH["employment"], 1200)),
    "corporate-commercial.html": (
        "images/m-smithadvocates_commercial%20and%20corporate%20law.png",
        cdn(UNSPLASH["corporate"], 1200)),
    "immigration.html": (
        "images/m-smithadvocates_Immigration%20Law.jpg",
        cdn(UNSPLASH["immigration"], 1200)),
    "insurance.html": (
        "images/m-smithadvocates_Insurance%20law%20(1).jpg",
        cdn(UNSPLASH["insurance"], 1200)),
    "human-rights.html": (
        "images/cqf-avocat-justice-2755765.jpg",
        cdn(UNSPLASH["humanrights"], 1200)),
    "eac-law.html": (
        "images/M-smithadvocates-EAC-.png",
        cdn(UNSPLASH["eac"], 1200)),
}

CARD_FILES = ["index.html", "practice-areas.html"]
ALL_FILES  = CARD_FILES + list(BG_REPLACEMENTS.keys())

for fname in ALL_FILES:
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        print(f"  SKIP (not found): {fname}")
        continue

    with open(path, encoding="utf-8") as f:
        html = f.read()

    changed = False

    # Card src replacements (applies to index.html + practice-areas.html)
    if fname in CARD_FILES:
        for old, new in SRC_REPLACEMENTS:
            if old in html:
                html = html.replace(old, new)
                changed = True

    # Background-image replacement (individual pages)
    if fname in BG_REPLACEMENTS:
        old_img, new_img = BG_REPLACEMENTS[fname]
        old_bg = f"background-image: url('{old_img}')"
        new_bg = f"background-image: url('{new_img}')"
        if old_bg in html:
            html = html.replace(old_bg, new_bg)
            changed = True
        else:
            print(f"  BG not matched in {fname} — looking for: {old_bg[:60]}")

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  Updated: {fname}")
    else:
        print(f"  No changes: {fname}")

print("\nDone.")
