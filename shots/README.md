# Screenshots

Captured from the iOS Simulator (iPhone 17 Pro, 402x874pt) with the app's own
night palette, then retouched by `RETOUCH.py`.

**Status bar** is set to the Apple marketing convention before capture:

```bash
xcrun simctl status_bar <UDID> override --time "9:41" \
  --batteryState charged --batteryLevel 100 --cellularBars 4 --wifiBars 3 --dataNetwork wifi
```

## What was edited, and what was not

`RETOUCH.py` makes exactly two kinds of change, and re-running it reproduces
every image from the raw captures:

1. **Privacy** — a real person's surname removed (first name only), and
   "Team Fritz" renamed, since a circle name carrying a founder's surname is
   identifying. Placeholder block names ("Test block") renamed to realistic ones.
2. **Numbers** — the simulator has no HealthKit data and no focus history, so
   every metric captured as `0`. Those are replaced with realistic sample values.

**No UI is invented.** Every pixel drawn sits on top of a number or a name the
real app already renders in that exact position. Sample data in store
screenshots is normal and permitted; fabricated functionality is not, and it is
the kind of thing that surfaces in App Review.

## Known gap

**Insights is missing.** The simulator has no Screen Time data at all — the tab
renders "Screen Time data only appears on a real device". The
distracting/neutral/productive split is one of the strongest screens in the app
and it can only be captured on a physical device. Same for the shield UI and
real health values.

## Reproducing

Raw captures live in `/tmp/kove-shots/s-*.png` at capture time (not committed —
they contain the unredacted surname). Re-capture, then:

```bash
python3 RETOUCH.py          # writes /tmp/kove-shots/out  (1206x2622, retouched)
python3 ~/appDevelopment/3bears-studio-site/tools/prep-shots.py \
  /tmp/kove-shots/out shots --widths 1206,620 --quality 92
```

That writes `<name>-620.webp` and `<name>-1206.webp`, which is what `index.html`
references via `srcset`.

### ⚠️ Do not use `sips -Z` here — it is why the shots shipped blurry

The original instruction was `sips -Z 620`. **`-Z` constrains the LONGEST side, not
the width.** On a 1206x2622 portrait capture it scales the *height* to 620 and
leaves the width at **285** — so every screenshot was 46% of the intended width
while `index.html` correctly declared `width="620"`. The browser upscaled 2.2x
before device pixel ratio was even applied; on a DPR-3 phone that is a ~6.5x
upscale, and it looked exactly as bad as that sounds.

If you ever go back to `sips`, the flag you want is `--resampleWidth 620`:

```bash
sips -Z 620              # 1206x2622 -> 285x620   WRONG
sips --resampleWidth 620 # 1206x2622 -> 620x1348  right
```

**Sizing target.** The hero `.phone` caps at 292px and carousel slides are 262px,
so the largest an image is ever displayed is ~274 CSS px. At DPR 3 that wants
~822px of real pixels — which is why 1206 (the iPhone 17 Pro's native capture
width, and the most that exists) is the top rung of the `srcset`.
