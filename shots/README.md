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
python3 RETOUCH.py          # writes /tmp/kove-shots/out
sips -Z 620 <file> --out shots/<name>.png
```
