# SpaceLink Spec Pack — How to publish & keep it updated

A plain-English guide for sending your designs and specs to the build team as **one link**.
*(This file is just for you — you don't need to send it to anyone.)*

---

## What's in this folder

| File | What it is |
|------|------------|
| `index.html` | The **hub** — the landing page the team sees first. Links to everything else. |
| `listing-field-spec.html` | The Listing Field spec, as a readable web page. |
| `admin-revenue-architecture.html` | The Admin Revenue Architecture spec, as a web page. |
| `pricing-module.html` | Your interactive pricing prototype. |
| `revenue-model.html` | Your interactive revenue calculators. |
| `build_pack.py` | The little converter that turns a Markdown doc into a branded page (Claude runs this — you don't need to). |
| `_src_*.md` / `_template.md` | Source files kept for re-editing later. The leading `_` keeps them tidy. |

**The golden rule:** the file named `index.html` is what loads first. Keep it in the folder.

---

## Publish it to Netlify (about 60 seconds)

1. Make sure you're logged in at **app.netlify.com**.
2. Go to **app.netlify.com/drop**.
3. Drag the **whole `codeaza-spacelink-specs` folder** onto the drop zone — the folder, not the individual files, and not a zip.
4. Netlify gives you a random link. Open **Site configuration → Change site name** and rename it to:
   `codeaza-spacelink-specs`
   → your link becomes **codeaza-spacelink-specs.netlify.app**
5. Open the link to check it works, then send that one link to Muhammad and the team.

That single link now shows the hub, and every spec and prototype is one click away.

---

## Update it later (same link, new content)

When something changes, you don't make a new link — you replace the contents of the existing one:

- Open your site in Netlify → **Deploys** tab → drag the updated folder onto the drop zone at the bottom. The same link now shows the new version.

---

## Add a NEW document to the pack

This is the repeatable part. When you've got a new spec, design, or idea:

1. **Hand it to me (Claude) in this Cowork project.** Markdown, a Word doc, or just written notes — whatever you have.
2. I'll convert it into a branded page that matches the others, and add a card for it on the hub.
3. You re-drop the folder onto Netlify (the *Update* step above). Done — same link, new page included.

So your workflow from now on is simply: **write the idea → give it to me → drop the folder → send the link.** No formatting, no code, no design work on your side.

---

## A few do's and don'ts (from Netlify's guide)

- ✅ Always keep the main file named `index.html`.
- ✅ Keep the `codeaza-` prefix on the site name so all your published pages stay grouped and recognisable.
- ✅ Hard-refresh (Ctrl/Cmd + Shift + R) if you don't see your latest changes — your browser may have cached the old version.
- ⚠️ A `.netlify.app` link is **public to anyone who has it**. These pages are fine to share, but never publish anything confidential (contracts, salaries, credentials) this way.
- ⚠️ Drag the **folder**, never a single file or a zip — dropping a lone file gives a "Page not found".

---

*Naming suggestion for future packs: keep using `codeaza-spacelink-<topic>` so links stay tidy and guessable — e.g. `codeaza-spacelink-brand`, `codeaza-spacelink-onboarding`.*
