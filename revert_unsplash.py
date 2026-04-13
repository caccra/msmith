import os

BASE = r"c:/Users/USER/Desktop/anti gravity/msmith"

# Reverse of update_unsplash.py — Unsplash CDN → local image paths
SRC_REPLACEMENTS = [
    ('src="https://images.unsplash.com/photo-FaTLrG5-ViE?auto=format&fit=crop&w=800&q=80"',
     'src="images/m-smithadvocates%20Litigation.png"'),
    ('src="https://images.unsplash.com/photo--t6ihNradj8?auto=format&fit=crop&w=800&q=80"',
     'src="images/oleksandrpidvalnyi-real-estate-6688945.jpg"'),
    ('src="https://images.unsplash.com/photo-fIq0tET6llw?auto=format&fit=crop&w=800&q=80"',
     'src="images/M-Smithadvocates-Intellectual-property.jpg"'),
    ('src="https://images.unsplash.com/photo-pPjKPDLTyYw?auto=format&fit=crop&w=800&q=80"',
     'src="images/m-smithadvocates_Oil%20and%20gas.webp"'),
    ('src="https://images.unsplash.com/photo-Mk2ls9UBO2E?auto=format&fit=crop&w=800&q=80"',
     'src="images/fietzfotos-architecture-5999913.jpg"'),
    ('src="https://images.unsplash.com/photo-FD9ncnQo9Ew?auto=format&fit=crop&w=800&q=80"',
     'src="images/activedia-law-1063249.jpg"'),
    ('src="https://images.unsplash.com/photo-GWe0dlVD9e0?auto=format&fit=crop&w=800&q=80"',
     'src="images/m-smithadvocates_commercial%20and%20corporate%20law.png"'),
    ('src="https://images.unsplash.com/photo-0QcSnCM0aMc?auto=format&fit=crop&w=800&q=80"',
     'src="images/m-smithadvocates_Immigration%20Law.jpg"'),
    ('src="https://images.unsplash.com/photo-nGQHF5opInc?auto=format&fit=crop&w=800&q=80"',
     'src="images/m-smithadvocates_Insurance%20law%20(1).jpg"'),
    ('src="https://images.unsplash.com/photo-qDhm-RwJbaY?auto=format&fit=crop&w=800&q=80"',
     'src="images/cqf-avocat-justice-2755765.jpg"'),
    ('src="https://images.unsplash.com/photo-LPvlpdZ99O0?auto=format&fit=crop&w=800&q=80"',
     'src="images/M-smithadvocates-EAC-.png"'),
]

BG_REPLACEMENTS = {
    "litigation-arbitration.html": (
        "https://images.unsplash.com/photo-FaTLrG5-ViE?auto=format&fit=crop&w=1200&q=80",
        "images/m-smithadvocates%20Litigation.png"),
    "real-estate.html": (
        "https://images.unsplash.com/photo--t6ihNradj8?auto=format&fit=crop&w=1200&q=80",
        "images/oleksandrpidvalnyi-real-estate-6688945.jpg"),
    "intellectual-property.html": (
        "https://images.unsplash.com/photo-fIq0tET6llw?auto=format&fit=crop&w=1200&q=80",
        "images/M-Smithadvocates-Intellectual-property.jpg"),
    "oil-gas-petroleum.html": (
        "https://images.unsplash.com/photo-pPjKPDLTyYw?auto=format&fit=crop&w=1200&q=80",
        "images/m-smithadvocates_Oil%20and%20gas.webp"),
    "mining-minerals.html": (
        "https://images.unsplash.com/photo-Mk2ls9UBO2E?auto=format&fit=crop&w=1200&q=80",
        "images/fietzfotos-architecture-5999913.jpg"),
    "employment-labour.html": (
        "https://images.unsplash.com/photo-FD9ncnQo9Ew?auto=format&fit=crop&w=1200&q=80",
        "images/activedia-law-1063249.jpg"),
    "corporate-commercial.html": (
        "https://images.unsplash.com/photo-GWe0dlVD9e0?auto=format&fit=crop&w=1200&q=80",
        "images/m-smithadvocates_commercial%20and%20corporate%20law.png"),
    "immigration.html": (
        "https://images.unsplash.com/photo-0QcSnCM0aMc?auto=format&fit=crop&w=1200&q=80",
        "images/m-smithadvocates_Immigration%20Law.jpg"),
    "insurance.html": (
        "https://images.unsplash.com/photo-nGQHF5opInc?auto=format&fit=crop&w=1200&q=80",
        "images/m-smithadvocates_Insurance%20law%20(1).jpg"),
    "human-rights.html": (
        "https://images.unsplash.com/photo-qDhm-RwJbaY?auto=format&fit=crop&w=1200&q=80",
        "images/cqf-avocat-justice-2755765.jpg"),
    "eac-law.html": (
        "https://images.unsplash.com/photo-LPvlpdZ99O0?auto=format&fit=crop&w=1200&q=80",
        "images/M-smithadvocates-EAC-.png"),
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

    if fname in CARD_FILES:
        for old, new in SRC_REPLACEMENTS:
            if old in html:
                html = html.replace(old, new)
                changed = True

    if fname in BG_REPLACEMENTS:
        old_img, new_img = BG_REPLACEMENTS[fname]
        old_bg = f"background-image: url('{old_img}')"
        new_bg = f"background-image: url('{new_img}')"
        if old_bg in html:
            html = html.replace(old_bg, new_bg)
            changed = True

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  Reverted: {fname}")
    else:
        print(f"  No changes: {fname}")

print("\nDone.")
