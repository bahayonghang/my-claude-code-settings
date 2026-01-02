# Data sources (verifiable, no fabricated numbers)

This skill requires that every displayed number can be traced back to a saved `gh api` response.

## Required raw files

Recommended structure:

- `data/github-wrapped-$YEAR/raw/user.json`
  - Source: `gh api user`
  - Used for: `login`, avatar, account `created_at` ("how long since we met GitHub")

- `data/github-wrapped-$YEAR/raw/contributions.json`
  - Source: GraphQL `contributionsCollection(from,to)`
  - Used for:
    - Year total: `contributionCalendar.totalContributions`
    - Commits/PRs/Issues totals: `total*Contributions`
    - Heatmap: `contributionCalendar.weeks[].contributionDays[]`
    - Top repos by contribution: `*ContributionsByRepository`

- `data/github-wrapped-$YEAR/raw/user_repos.json`
  - Source: REST `users/$USER/repos?per_page=100 --paginate`
  - Used for:
    - Your own repo list and language distribution
    - "Created in YEAR" by filtering `created_at`
    - Stars/forks snapshots (must be disclosed as snapshots)

- `data/github-wrapped-$YEAR/raw/starred_repos_pages.json`
  - Source: GraphQL `starredRepositories(orderBy: STARRED_AT)` with pagination
  - Used for:
    - Stars in YEAR by filtering `starredAt`
    - Topics/language preference (from repo topics / primaryLanguage)
    - "New interests unlocked" by comparing YEAR vs pre-YEAR topic counts
    - Per-month star timeline events (each event is a `starredAt` point)

- `data/github-wrapped-$YEAR/raw/prs_${YEAR}_pages.json`
  - Source: GraphQL Search (merged PRs in YEAR) with pagination
  - Used for:
    - PR counts in YEAR
    - Additions/deletions (best-effort for "impact")
    - "Open Source Award" (group external PRs by repo)

- `data/github-wrapped-$YEAR/raw/contributed_repos_pages.json`
  - Source: GraphQL `repositoriesContributedTo` with pagination
  - Used for:
    - External repos you contributed to (for leaderboard / awards)

- `data/github-wrapped-$YEAR/raw/events_90d.json` (optional)
  - Source: REST `users/$USER/events --paginate`
  - Limit: GitHub keeps only ~90 days.
  - Allowed use: "best-effort" easter eggs ONLY, and must be labeled as such.

## Prohibited

- Inventing numbers for unavailable metrics.
- Using placeholder numbers when raw data is missing.
- Presenting snapshots as year-increment without explicit collection of a year-scoped timeline.
