#!/usr/bin/env python3
"""Generate Oye Mex PWA icons (PIL)."""
import os
from PIL import Image, ImageDraw

GREEN = (47, 93, 58, 255)      # #verde
CREAM = (246, 241, 231, 255)   # #crema
GOLD  = (192, 101, 58, 255)

def play_triangle(d, cx, cy, r, color):
    h = r * 1.15
    pts = [(cx - r*0.42, cy - h/2), (cx - r*0.42, cy + h/2), (cx + r*0.72, cy)]
    d.polygon(pts, fill=color)

def make_icon(size, maskable=False, path=None):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if maskable:
        d.rectangle([0, 0, size, size], fill=GREEN)     # full-bleed
    else:
        d.rounded_rectangle([0, 0, size, size], radius=int(size*0.20), fill=GREEN)
    # simple brand mark: play triangle + a small gold accent dot
    cx = size * 0.45; cy = size * 0.5
    play_triangle(d, cx, cy, size*0.30, CREAM)
    r = size * 0.05
    d.ellipse([cx+size*0.55, size*0.16, cx+size*0.55+2*r, size*0.16+2*r], fill=GOLD)
    img.save(path)

os.makedirs("icons", exist_ok=True)
make_icon(192, False, "icons/icon-192.png")
make_icon(512, False, "icons/icon-512.png")
make_icon(512, True,  "icons/icon-maskable-512.png")
make_icon(180, False, "icons/apple-touch-icon.png")

# favicon 32
img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
d.rounded_rectangle([0, 0, 32, 32], radius=6, fill=GREEN)
play_triangle(d, 14, 16, 9, CREAM)
img.save("icons/favicon.png")

for f in sorted(os.listdir("icons")):
    p = os.path.join("icons", f)
    im = Image.open(p)
    print(f"{f}: {im.size[0]}x{im.size[1]} mode={im.mode}")