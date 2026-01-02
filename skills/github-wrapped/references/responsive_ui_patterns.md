# Responsive UI Patterns (Single-file GitHub Wrapped)

These patterns come from building a single-file “GitHub Wrapped 2025” that must work as:

- **Desktop cinematic** (wide, detailed, screenshot-friendly)
- **Mobile slide deck** (paged navigation, minimal on-page density)

Use them to avoid regressions when the file grows into thousands of lines.

## 1) Gate mobile layout changes (don’t break desktop)

Prefer a **two-signal gate**:

- CSS: `@media (max-width: 620px) and (pointer: coarse)`
- JS: `IS_MOBILE_LAYOUT()` checks `matchMedia()` + viewport width

Avoid width-only rules; they can affect small desktop windows and ruin desktop typography.

## 2) Two modes: `paged` vs `free`

- **Free**: normal scroll (user-controlled).
- **Paged**: scene snapping/locking (wheel/keys); on mobile, swipe up/down flips scenes.

Implementation tips:

- Keep a single source of truth: `scroller.dataset.mode = "paged" | "free"`.
- Page mode should prevent accidental inner scroll and keep navigation predictable.
- Update a HUD hint dynamically per scene, not a static “how to use” banner.

## 3) Mobile paged mode: fit one viewport

If a scene cannot fit on a phone screen:

- Hide heavy blocks in paged mode with `data-mhide="paged"`.
- Provide a **details entry** (button) that opens a modal/bottom sheet.

Critical: do not “shrink everything” on mobile; it becomes unreadable and still overflows.

## 4) Bottom sheet that moves DOM nodes (keeps IDs & listeners)

Avoid duplicating content into a modal via `innerHTML` (it breaks IDs and event listeners).

Pattern:

1. When opening: move an existing DOM node into the sheet container.
2. Insert a placeholder comment/node at the original position.
3. When closing: move it back to the placeholder location.

Edge cases:

- Preserve focus (return focus to the trigger button).
- Ensure the sheet body is scrollable (`overflow:auto`) for long lists.
- Add `touch-action: pan-y` to allow natural scroll.

## 5) Draggable floating controls (mode toggle / music)

Mobile UIs often need floating controls. To avoid overlap:

- Make them draggable via Pointer Events (`pointerdown` → `setPointerCapture`).
- Clamp positions to the viewport and respect safe-area insets:
  - `env(safe-area-inset-top/right/bottom/left)`
- Keep hit targets ≥ 44px.

Optional: persist position in `localStorage`.

## 6) Canvas charts: DPR-aware sizing (fix “squashed radar”)

Never rely on CSS stretching a canvas. Instead:

- Read the rendered size: `const rect = canvas.getBoundingClientRect()`
- Use devicePixelRatio: `const dpr = devicePixelRatio || 1`
- Set backing store: `canvas.width = rect.width * dpr`, `canvas.height = rect.height * dpr`
- Draw in CSS pixels: `ctx.setTransform(dpr,0,0,dpr,0,0)`

Pointer coordinates must be in **CSS pixels**:

- `x = event.clientX - rect.left`
- `y = event.clientY - rect.top`

## 7) Stacking context pitfalls (unclickable buttons after transforms)

If buttons become unclickable after 3D transforms / overlays, suspect:

- A transformed parent creating a new stacking context
- An invisible overlay capturing pointer events

Fix checklist:

- Add `position: relative` + `z-index` to the clickable header area
- Set `pointer-events: none` on decorative layers
- Use `isolation: isolate` and `overflow: hidden` to contain overlays

## 8) Overflow rules for long tokens (repo/topic names)

- Prefer `overflow-wrap: break-word` for readability.
- Use `overflow-wrap: anywhere` only as a last resort to prevent horizontal overflow.
- For dense grids, avoid ellipsis on desktop if it removes key info; use wrapping + spacing instead.

## 9) Avoid “inner scroll everywhere”

On mobile paged mode:

- Keep the **scene itself** non-scrollable whenever possible.
- Move overflow into a bottom sheet (where scroll is expected).

On desktop:

- Avoid needless inner scroll containers; they feel broken when the page mode is already snapping.

## 10) External dependencies are optional

CDN fonts/icons/music/widgets are allowed, but:

- The report must remain navigable and readable without them.
- Treat load failures as “degrade gracefully”, not fatal errors.

## 11) Quick regression checks (desktop + mobile)

- “Cover only, buttons dead” → likely JS parse error or dataset JSON parse error; show an overlay.
- Paged/free behave differently (not just labels).
- Touch swipe works in paged mode; free mode scrolls normally.
- No unexpected horizontal overflow on any scene.
- Modals/sheets scroll properly on long content.

