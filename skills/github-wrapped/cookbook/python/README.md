# Python recipes

These are focused building blocks you can copy into your dataset builder.

Recommended workflow:

1. Collect raw data with `scripts/collect_raw.sh` (ensures pagination and saves query files).
2. Build `processed/dataset.json` deterministically from `raw/`.
3. Embed the dataset into a single HTML file (no runtime fetch).

Files:

- `io_utils.py`: JSON IO helpers + GraphQL-page flattening patterns.
- `time_utils.py`: ISO-8601 parsing and timezone-safe bucketing.
- `stars_analysis.py`: by-month star events, within-month scatter points, hour histograms, holiday filtering.
- `categories_analysis.py`: topic/language heuristics → categories + radar scoring inputs.
- `open_source_analysis.py`: merged PR aggregation → “open source award” + highlight selection.

