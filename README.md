# kove-site

Public marketing + legal site for **KOVE** (published by 3 Bears Studio LLC), hosted free on **GitHub
Pages** — no custom domain. Mirrors the `anchored-site` pattern.

## Pages

- `index.html` — small landing page.
- `privacy.html` — the KOVE Privacy Policy. **Generated — do not edit here by hand.**

## Source of truth for the privacy policy

`privacy.html` is a **copy** produced by the KOVE repo. Edit the policy in
`~/appDevelopment/Anchor/privacy-policy/privacy-policy.md`, run that folder's `build.sh` (it copies the
rendered HTML here automatically), then commit and push this repo.

## Publish / update

```bash
cd ~/appDevelopment/kove-site
git add -A && git commit -m "Update site" && git push
```

GitHub Pages redeploys on push (usually within a minute).

## One-time GitHub Pages setup

Repo → **Settings → Pages** → Source: **Deploy from a branch** → Branch: **main** / **/(root)** → Save.
The live URLs are then:

- Home: `https://hoebears-prog.github.io/kove-site/`
- **Privacy policy: `https://hoebears-prog.github.io/kove-site/privacy.html`** ← put this in App Store Connect.

## Before relying on it publicly

The contact address on both pages is `3bearsstudio@gmail.com`. Make sure that inbox exists.
