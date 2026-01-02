# Single-file engineering notes

## Keep it maintainable

A 2000+ line HTML is normal for a high-polish Wrapped page. You still need structure.

Suggested layout inside the HTML:

1. `:root` design tokens (colors, typography, spacing, motion)
2. Base components (cards, buttons, badges, chips)
3. Scene sections (each scene self-contained)
4. Chart renderers (canvas/SVG helpers)
5. Data layer (dataset parsing + validation)
6. Scene controller (scroll/page mode, navigation)
7. Extras (share card screenshot, music widget, fireworks)

## Motion consistency

- Define global motion tokens: `--ease`, `--dur-fast`, `--dur-normal`, `--dur-slow`.
- Prefer `transform` + `opacity` and `will-change` sparingly.
- Use one transition system for all scenes (avoid mixing ad-hoc timeouts).

## Data integrity UX

- Always provide a "Data integrity" entry in the UI.
- If dataset is missing/corrupted: show a blocking overlay with clear remediation steps.
- Any best-effort facts (events API) must be labeled.

## Evolution strategy

- Keep `dataset.json` as the source of truth.
- Add fields, don’t break fields.
- When changing story/UI, regenerate dataset from raw and re-embed.
