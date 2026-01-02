#!/usr/bin/env bash
set -euo pipefail

# Collect verifiable raw data for GitHub Wrapped using ONLY gh API.
#
# Output (recommended):
#   data/github-wrapped-$YEAR/raw/*.json
#
# Usage:
#   YEAR=2025 USER=octocat ./collect_raw.sh
#   YEAR=2025 ./collect_raw.sh                    # USER defaults to current gh auth user
#   YEAR=2025 OUT_BASE=data/github-wrapped-2025 ./collect_raw.sh
#
# Optional:
#   PREV_YEARS=2        # also collect contributions for YEAR-1..YEAR-PREV_YEARS
#   FETCH_EVENTS_90D=1  # best-effort; GitHub only keeps ~90 days

YEAR="${YEAR:-}"
if [[ -z "$YEAR" ]]; then
  echo "ERROR: YEAR is required (e.g. YEAR=2025)." >&2
  exit 2
fi

OUT_BASE="${OUT_BASE:-data/github-wrapped-${YEAR}}"
RAW_DIR="${OUT_BASE}/raw"
mkdir -p "$RAW_DIR/queries"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
QUERY_DIR="${SCRIPT_DIR}/queries"

if ! command -v gh >/dev/null 2>&1; then
  echo "ERROR: gh CLI not found. Install GitHub CLI first." >&2
  exit 2
fi

gh auth status >/dev/null

USER="${USER:-}"
if [[ -z "$USER" ]]; then
  USER="$(gh api user --jq .login)"
fi

echo "Collecting raw data: user=${USER} year=${YEAR}" >&2

# Save query files for audit/replay.
cp -f "${QUERY_DIR}"/*.graphql "${RAW_DIR}/queries/" 2>/dev/null || true

# 1) User profile (raw)
gh api user > "${RAW_DIR}/user.json"

# 2) Contributions (GraphQL)
FROM="${YEAR}-01-01T00:00:00Z"
TO="${YEAR}-12-31T23:59:59Z"

gh api graphql   -f query="$(cat "${QUERY_DIR}/contributions.graphql")"   -f user="$USER"   -f from="$FROM"   -f to="$TO"   > "${RAW_DIR}/contributions.json"

# Optional: previous years for YoY comparisons.
PREV_YEARS="${PREV_YEARS:-0}"
if [[ "$PREV_YEARS" != "0" ]]; then
  for ((i=1; i<=PREV_YEARS; i++)); do
    y=$((YEAR - i))
    gh api graphql       -f query="$(cat "${QUERY_DIR}/contributions.graphql")"       -f user="$USER"       -f from="${y}-01-01T00:00:00Z"       -f to="${y}-12-31T23:59:59Z"       > "${RAW_DIR}/contributions_${y}.json"
  done
fi

# 3) Starred repos (GraphQL, paginated pages)
gh api graphql --paginate --slurp   -f query="$(cat "${QUERY_DIR}/starred_repos.graphql")"   -f user="$USER"   > "${RAW_DIR}/starred_repos_pages.json"

# 4) Merged PRs in the year (GraphQL Search, paginated pages)
SEARCH_QUERY="author:${USER} is:pr is:merged merged:${YEAR}-01-01..${YEAR}-12-31"

gh api graphql --paginate --slurp   -f query="$(cat "${QUERY_DIR}/prs_merged.graphql")"   -f queryString="$SEARCH_QUERY"   > "${RAW_DIR}/prs_${YEAR}_pages.json"

# 5) Contributed repos (GraphQL, paginated pages)
gh api graphql --paginate --slurp   -f query="$(cat "${QUERY_DIR}/contributed_repos.graphql")"   -f user="$USER"   > "${RAW_DIR}/contributed_repos_pages.json"

# 6) User repos (REST, paginate)
gh api "users/${USER}/repos?per_page=100" --paginate > "${RAW_DIR}/user_repos.json"

# 7) Recent events (REST, best-effort only)
FETCH_EVENTS_90D="${FETCH_EVENTS_90D:-1}"
if [[ "$FETCH_EVENTS_90D" == "1" ]]; then
  # This may be rate-limited and is not a full-year history.
  if ! gh api "users/${USER}/events?per_page=100" --paginate > "${RAW_DIR}/events_90d.json"; then
    echo "WARN: Failed to fetch events; continuing (best-effort optional)." >&2
  fi
fi

echo "Done. Raw saved to: ${RAW_DIR}" >&2
