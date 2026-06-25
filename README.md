# SpaceLinq Spec Pack

Working specs and interactive prototypes for **SpaceLinq** (NZ 3PL storage marketplace),
prepared for the Codeaza build team.

## Live site
Published automatically to Netlify on every push to `main`:
**https://codeaza-spacelink-specs.netlify.app**

## Structure
- `public/` — the live web pages (this is what Netlify serves)
  - `index.html` — the Spec Pack hub
  - `listing-field-spec.html`, `admin-revenue-architecture.html` — specs
  - `pricing-module.html`, `revenue-model.html`, `revenue-explainer.html` — prototypes & explainer
- `src/` — markdown sources + `build_pack.py` converter (not published)
- `netlify.toml` — tells Netlify to serve the `public/` folder

## Updating
Edit a source, rebuild the page, commit, and push — Netlify redeploys itself in ~30s.
