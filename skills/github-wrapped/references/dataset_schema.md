# Dataset schema (recommended)

Keep the dataset stable and backwards-compatible. Treat it like a public API between your data pipeline and your single-file HTML.

## Principles

- Additive changes are preferred (add new fields, keep old fields).
- Keep optional fields nullable (`null`) rather than omitting them (simplifies rendering).
- Put all caveats in `meta.dataProvenance.notes[]` and also show them in-page.

## Top-level

- `meta`
  - `year`: number
  - `timezone`: string
  - `generatedAt`: ISO timestamp
  - `dataProvenance`
    - `rawDir`: string (path)
    - `notes`: string[] (limitations, best-effort disclaimers)

- `user`
  - `login`, `name`, `avatarUrl`, `createdAt`
  - `followers`, `following`

- `year`
  - `contributions`
    - `total`, `totalCommits`, `totalPrs`, `totalIssues`
    - `calendarWeeks` (pass-through weeks for heatmap)
    - `busiestDay` (`date`, `count`)
    - `longestStreak` (`days`, `start`, `end`)
    - `weekdaySums` (7 ints)
    - `byMonth` (12 items)
  - `stars`
    - `totalInYear`, `totalAllTime`
    - `byYear` (map)
    - `byMonthInYear[]`
      - `month`: YYYY-MM
      - `count`: int
      - `events[]`: timeline points for that month
        - `starredAt`, `nameWithOwner`, `stars`, `url`
  - `repos`
    - `ownTotal`
    - `ownStarsTotalSnapshot`, `ownForksTotalSnapshot`
  - `openSourceAward` (nullable)

## Versioning

If you expect frequent evolution, add `meta.schemaVersion` (e.g. `1`) and keep the renderer compatible with older versions.
