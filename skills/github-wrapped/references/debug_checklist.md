# Debug checklist (single-file HTML)

This checklist targets the most common failure mode: the page shows the cover but buttons do nothing.

## 1) Verify the data pipeline

- Raw files exist and are valid JSON:
  - `raw/user.json`
  - `raw/contributions.json`
  - `raw/starred_repos_pages.json`
  - `raw/prs_${YEAR}_pages.json`
  - `raw/contributed_repos_pages.json`
  - `raw/user_repos.json`

- `processed/dataset.json` exists and can be parsed:

  - `python -c 'import json; json.load(open(".../dataset.json"))'`

If any file is missing, do not guess. Re-run raw collection.

## 2) Verify the embedded dataset block

- The HTML contains exactly one dataset anchor:

  - `<script id="dataset" type="application/json">...`

- The embedded JSON is valid:

  - Copy the JSON into a validator, or use DevTools:
    - `JSON.parse(document.getElementById("dataset").textContent)`

- Make sure `<` is escaped as `<` in the embedded JSON.

## 3) Check for JS errors that stop everything

Open DevTools Console and look for:

- SyntaxError (a single error prevents all handlers)
- Duplicate declarations (`const X` declared twice)
- Uncaught exceptions during startup (e.g. dataset parsing)

A good pattern is: show a visible overlay when initialization fails.

## 4) Confirm interactions aren’t blocked by CSS

- `pointer-events: none` on a container can kill all clicks.
- A full-screen overlay with higher z-index can swallow clicks.
- In page mode, scroll-lock code may prevent wheel/touch; ensure there is a clear exit.

## 5) Treat external scripts as optional

- Fonts / icons / html2canvas / SoundCloud can fail to load.
- Never make core navigation depend on an external script.
- If autoplay is blocked, retry playback on a user gesture (e.g. “Start”).
