# kove (site)

Public marketing + legal site for **KOVE**, published by 3 Bears Studio LLC. Hosted free on **GitHub
Pages** under the studio org — **no custom domain**. Mirrors the `anchored-site` / `getcowatch` pattern.

- **Org / repo:** `github.com/3bearsstudio/kove` (public)
- **Local working copy:** `~/appDevelopment/kove`
- **Live URLs:**
  - Home → https://3bearsstudio.github.io/kove/
  - **Privacy policy → https://3bearsstudio.github.io/kove/privacy.html**  ← the App Store Connect "Privacy Policy URL"

## Pages

- `index.html` — small landing page.
- `privacy.html` — the KOVE Privacy Policy. **Generated — do not edit here by hand.**

## Source of truth for the privacy policy

`privacy.html` is a **copy** produced by the KOVE app repo. Edit the policy in
`~/appDevelopment/Anchor/privacy-policy/privacy-policy.md`, run that folder's `build.sh` (it copies the
rendered HTML into this repo automatically), then commit and push here.

## Publish / update

```bash
cd ~/appDevelopment/kove
git add -A && git commit -m "Update site" && git push
```

GitHub Pages redeploys on push (usually within a minute). Pages is already enabled (Deploy from branch →
`main` / root), so no setup is needed.

## Contact

Both pages list `3bearsstudiollc@gmail.com` (the 3 Bears Studio LLC inbox). It's created — keep it monitored.
