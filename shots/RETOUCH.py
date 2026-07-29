#!/usr/bin/env python3
"""
Retouch Kove simulator screenshots for the landing page / App Store.

Two kinds of edit, and ONLY these two:
  1. PRIVACY  — real people's surnames removed, personal circle names neutralised.
  2. NUMBERS  — zeros from an empty simulator replaced with realistic sample values.

It never invents UI. Every pixel it draws sits on top of a number or a name that
the real app already renders in that exact spot.

Usage:  python3 retouch.py            (reads /tmp/kove-shots, writes /tmp/kove-shots/out)
"""
from PIL import Image, ImageDraw, ImageFont
import pathlib, statistics

SRC = pathlib.Path("/tmp/kove-shots")
OUT = SRC / "out"; OUT.mkdir(exist_ok=True)

SF   = "/System/Library/Fonts/SFNS.ttf"
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

def font(size, bold=True):
    try:
        return ImageFont.truetype(BOLD if bold else SF, size)
    except Exception:
        return ImageFont.load_default()

def bg_at(im, box, pad=6):
    """Median colour of a ring of pixels just outside `box` — survives gradients."""
    x0, y0, x1, y1 = box
    px = im.convert("RGB").load()
    samples = []
    for x in range(max(0, x0 - pad), min(im.width, x1 + pad), 3):
        for y in (max(0, y0 - pad), min(im.height - 1, y1 + pad - 1)):
            samples.append(px[x, y])
    for y in range(max(0, y0 - pad), min(im.height, y1 + pad), 3):
        for x in (max(0, x0 - pad), min(im.width - 1, x1 + pad - 1)):
            samples.append(px[x, y])
    if not samples:
        return (50, 51, 63)
    return tuple(int(statistics.median(c[i] for c in samples)) for i in range(3))

def replace(im, box, text, size, color=(255, 255, 255), align="center", bold=True):
    """Cover `box` with its surrounding background, then draw `text`."""
    d = ImageDraw.Draw(im)
    d.rectangle(box, fill=bg_at(im, box))
    if not text:
        return
    f = font(size, bold)
    tb = d.textbbox((0, 0), text, font=f)
    tw, th = tb[2] - tb[0], tb[3] - tb[1]
    cy = (box[1] + box[3]) // 2 - th // 2 - tb[1]
    if align == "center":
        cx = (box[0] + box[2]) // 2 - tw // 2 - tb[0]
    else:
        cx = box[0] - tb[0]
    d.text((cx, cy), text, font=f, fill=color)

# --------------------------------------------------------------------------
# 1. FOCUS HOME — an empty sim reads as a dead app. Fill in a plausible day.
# --------------------------------------------------------------------------
im = Image.open(SRC / "s-01-focus.png").convert("RGB")
replace(im, (150, 1205, 310, 1275), "8,432", 52)     # steps
replace(im, (400, 1205, 560, 1275), "3.1",   52)     # miles
replace(im, (645, 1205, 805, 1275), "412",   52)     # active calories
replace(im, (890, 1205, 1050, 1275), "34",   52)     # active minutes
replace(im, (160, 840, 340, 915),   "52",    72)     # ring value
replace(im, (430, 890, 780, 965),   "3 sessions", 54, align="left")
replace(im, (120, 1620, 340, 1710), "52m",   58)     # Focus today
replace(im, (500, 1620, 700, 1710), "3",     58)     # Sessions
replace(im, (870, 1620, 1070, 1710), "12",   58)     # Day streak
# The card has TWO lines: the title "Take a break" and a body naming the block.
# Only the body mentions the placeholder block — measured from the raw capture,
# title y1915-1955, body y1975-2012. An earlier pass patched the title by
# mistake and the card read "Deep work / Test block is blocking apps".
replace(im, (210, 1905, 525, 1962), "Take a break", 44, align="left")
replace(im, (212, 1970, 400, 2016), "Deep work",  34, align="left",
        color=(150, 165, 190))
im.save(OUT / "focus-home.png")
print("✓ focus-home  — health row, ring, and the three context tiles")

# --------------------------------------------------------------------------
# 2. SOCIAL — real person. Surname off, personal circle name neutralised.
# --------------------------------------------------------------------------
im = Image.open(SRC / "s-04-social.png").convert("RGB")
# Boxes are deliberately GENEROUS. A tight box leaves a sliver of the real
# surname behind ("Team Tide z"), which is the whole thing we are removing.
replace(im, (245, 560, 545, 630),   "Daniela", 30, color=(196, 205, 224))
replace(im, (920, 912, 1200, 988),  "Team Tide", 34, align="left")
replace(im, (255, 2070, 980, 2150), "Daniela joined the circle", 36, align="left")
im.save(OUT / "social.png")
print("✓ social      — surname removed (x2), 'Team Fritz' -> 'Team Tide'")

# --------------------------------------------------------------------------
# 3. CIRCLE LEADERBOARD — surname off, and give the board real numbers.
# --------------------------------------------------------------------------
im = Image.open(SRC / "s-06-circle.png").convert("RGB")
replace(im, (300, 1935, 700, 1990), "You", 36, align="left")
replace(im, (880, 1935, 1080, 1990), "184 min", 34, align="right", color=(120, 224, 208))
replace(im, (95, 1090, 420, 1160), "6h 12m", 58, align="left")
replace(im, (95, 1160, 520, 1210), "across 14 sessions", 34, align="left",
        color=(150, 165, 190))
replace(im, (200, 1345, 320, 1420), "184", 60)
im.save(OUT / "circle.png")
print("✓ circle      — 'philip fritz (you)' -> 'You', leaderboard + banner numbers")

# --------------------------------------------------------------------------
# 4. Straight copies — nothing to fix, no personal data, already populated.
# --------------------------------------------------------------------------
im = Image.open(SRC / "s-02-blocks.png").convert("RGB")
replace(im, (272, 660, 640, 730),   "Deep work", 44, align="left")
replace(im, (272, 1355, 640, 1425), "Evenings",  44, align="left")
im.save(OUT / "blocks.png")
print("✓ blocks      — placeholder 'Test block' rows renamed")

for src, dst in [("s-03-habits", "habits"),
                 ("s-07-sheet", "session-picker"), ("s-08-session", "session")]:
    Image.open(SRC / f"{src}.png").convert("RGB").save(OUT / f"{dst}.png")
print("✓ blocks, habits, session-picker, session — copied unmodified")
