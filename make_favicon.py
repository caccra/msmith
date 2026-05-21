"""
Generate M-Smith Advocates favicons from the logo concept:
Three panels — scales of justice | S | a — in brand colors.
Outputs: favicon.ico (16/32/48), favicon-32.png, favicon-192.png,
         apple-touch-icon.png (180x180), favicon.svg
"""
from PIL import Image, ImageDraw, ImageFont
import os, math

RED   = (204, 34, 0)
BLACK = (10, 10, 10)
WHITE = (255, 255, 255)

def draw_scales(draw, cx, cy, size):
    """Draw a simplified scales-of-justice icon."""
    s = size / 48  # scale factor
    lw = max(1, round(2 * s))

    # Vertical post
    draw.line([(cx, cy - 18*s), (cx, cy + 18*s)], fill=RED, width=lw)
    # Base
    draw.line([(cx - 10*s, cy + 18*s), (cx + 10*s, cy + 18*s)], fill=RED, width=lw)
    # Horizontal beam
    draw.line([(cx - 18*s, cy - 12*s), (cx + 18*s, cy - 12*s)], fill=RED, width=lw)
    # Top knob
    r = max(2, round(3 * s))
    draw.ellipse([(cx - r, cy - 18*s - r), (cx + r, cy - 18*s + r)], fill=RED)

    # Left pan
    bx, by = cx - 18*s, cy - 12*s
    draw.line([(bx, by), (bx - 7*s, by + 14*s)], fill=RED, width=lw)
    draw.line([(bx, by), (bx + 7*s, by + 14*s)], fill=RED, width=lw)
    pr = max(1, round(2 * s))
    draw.arc(
        [(bx - 7*s - pr, by + 14*s - pr*2), (bx + 7*s + pr, by + 14*s + pr*2)],
        start=0, end=180, fill=RED, width=lw
    )

    # Right pan
    bx2 = cx + 18*s
    draw.line([(bx2, by), (bx2 - 7*s, by + 14*s)], fill=RED, width=lw)
    draw.line([(bx2, by), (bx2 + 7*s, by + 14*s)], fill=RED, width=lw)
    draw.arc(
        [(bx2 - 7*s - pr, by + 14*s - pr*2), (bx2 + 7*s + pr, by + 14*s + pr*2)],
        start=0, end=180, fill=RED, width=lw
    )

    # Left/right hanging cords
    draw.line([(bx, by), (cx - 3*s, by - 2*s)], fill=RED, width=lw)
    draw.line([(bx2, by), (cx + 3*s, by - 2*s)], fill=RED, width=lw)


def make_icon(size):
    """Render the three-panel logo at `size` x `size` pixels."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    border = max(1, size // 32)
    panel_w = size // 3

    # Panel 1 — scales on white
    draw.rectangle([0, 0, panel_w - 1, size - 1], fill=WHITE)
    draw.rectangle([0, 0, panel_w - 1, size - 1], outline=BLACK, width=border)
    draw_scales(draw, panel_w // 2, size // 2, size * 0.75)

    # Panel 2 — "S" in white on black
    x1, x2 = panel_w, panel_w * 2 - 1
    draw.rectangle([x1, 0, x2, size - 1], fill=BLACK)
    draw.rectangle([x1, 0, x2, size - 1], outline=BLACK, width=border)
    # Draw S using a bold font if available, else construct from arcs
    font_size = int(size * 0.65)
    cx2 = (x1 + x2) // 2
    try:
        font_paths = [
            "C:/Windows/Fonts/arialbd.ttf",
            "C:/Windows/Fonts/georgia.ttf",
            "C:/Windows/Fonts/Arial.ttf",
        ]
        font = None
        for fp in font_paths:
            if os.path.exists(fp):
                font = ImageFont.truetype(fp, font_size)
                break
        if font is None:
            font = ImageFont.load_default()
        bbox = draw.textbbox((0, 0), "S", font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        tx = cx2 - tw // 2 - bbox[0]
        ty = size // 2 - th // 2 - bbox[1]
        draw.text((tx, ty), "S", fill=WHITE, font=font)
    except Exception:
        pass

    # Panel 3 — "a" in red on white
    x3, x4 = panel_w * 2, size - 1
    draw.rectangle([x3, 0, x4, size - 1], fill=WHITE)
    draw.rectangle([x3, 0, x4, size - 1], outline=BLACK, width=border)
    cx3 = (x3 + x4) // 2
    try:
        bbox = draw.textbbox((0, 0), "a", font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        tx = cx3 - tw // 2 - bbox[0]
        ty = size // 2 - th // 2 - bbox[1]
        draw.text((tx, ty), "a", fill=RED, font=font)
    except Exception:
        pass

    return img


# --- Generate assets ---
out = os.path.dirname(os.path.abspath(__file__))

# favicon.ico — 16, 32, 48 packed
sizes = [16, 32, 48]
imgs = [make_icon(s) for s in sizes]
ico_path = os.path.join(out, "favicon.ico")
imgs[0].save(ico_path, format="ICO", sizes=[(s, s) for s in sizes],
             append_images=imgs[1:])
print(f"favicon.ico   ({', '.join(str(s) for s in sizes)}px)")

# favicon-32.png
p32 = os.path.join(out, "favicon-32.png")
make_icon(32).save(p32, "PNG")
print("favicon-32.png")

# favicon-192.png  (Android / PWA)
p192 = os.path.join(out, "favicon-192.png")
make_icon(192).save(p192, "PNG")
print("favicon-192.png")

# apple-touch-icon.png 180x180
ati = os.path.join(out, "apple-touch-icon.png")
apple = make_icon(192).resize((180, 180), Image.LANCZOS)
apple.save(ati, "PNG")
print("apple-touch-icon.png")

# favicon.svg — scalable vector version
svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">
  <!-- Panel 1: scales on white -->
  <rect x="0" y="0" width="16" height="48" fill="white" stroke="black" stroke-width="0.8"/>
  <!-- scales icon -->
  <line x1="8" y1="8" x2="8" y2="40" stroke="#CC2200" stroke-width="1.4"/>
  <line x1="3" y1="40" x2="13" y2="40" stroke="#CC2200" stroke-width="1.4"/>
  <line x1="2" y1="15" x2="14" y2="15" stroke="#CC2200" stroke-width="1.4"/>
  <circle cx="8" cy="8" r="1.5" fill="#CC2200"/>
  <!-- left pan -->
  <line x1="2" y1="15" x2="0.5" y2="22" stroke="#CC2200" stroke-width="1"/>
  <line x1="2" y1="15" x2="3.5" y2="22" stroke="#CC2200" stroke-width="1"/>
  <path d="M0.5,22 Q2,24 3.5,22" fill="none" stroke="#CC2200" stroke-width="1"/>
  <!-- right pan -->
  <line x1="14" y1="15" x2="12.5" y2="22" stroke="#CC2200" stroke-width="1"/>
  <line x1="14" y1="15" x2="15.5" y2="22" stroke="#CC2200" stroke-width="1"/>
  <path d="M12.5,22 Q14,24 15.5,22" fill="none" stroke="#CC2200" stroke-width="1"/>

  <!-- Panel 2: S on black -->
  <rect x="16" y="0" width="16" height="48" fill="black" stroke="black" stroke-width="0.8"/>
  <text x="24" y="36" font-family="Georgia,serif" font-size="32" font-weight="bold"
        fill="white" text-anchor="middle">S</text>

  <!-- Panel 3: a on white -->
  <rect x="32" y="0" width="16" height="48" fill="white" stroke="black" stroke-width="0.8"/>
  <text x="40" y="36" font-family="Georgia,serif" font-size="32" font-weight="bold"
        fill="#CC2200" text-anchor="middle">a</text>
</svg>"""

svg_path = os.path.join(out, "favicon.svg")
with open(svg_path, "w") as f:
    f.write(svg)
print("favicon.svg")

print("\nAll favicon assets generated.")
