from __future__ import annotations

from collections import defaultdict


def is_external_repo(repo: dict, user_login: str) -> bool:
    owner = ((repo.get("owner") or {}).get("login")) or repo.get("ownerLogin") or ""
    return owner.lower() != (user_login or "").lower()


def pr_lines(pr: dict) -> int:
    return int(pr.get("additions") or 0) + int(pr.get("deletions") or 0)


def aggregate_external_prs(prs: list[dict], user_login: str) -> dict[str, dict]:
    """
    Returns per-repo aggregates for *external* merged PRs.
    """
    by_repo: dict[str, dict] = defaultdict(lambda: {"repo": None, "count": 0, "additions": 0, "deletions": 0, "lines": 0})
    for pr in prs:
        repo = pr.get("repository") or {}
        name = repo.get("nameWithOwner")
        if not name:
            continue
        if not is_external_repo(repo, user_login):
            continue
        agg = by_repo[str(name)]
        agg["repo"] = repo
        agg["count"] += 1
        agg["additions"] += int(pr.get("additions") or 0)
        agg["deletions"] += int(pr.get("deletions") or 0)
        agg["lines"] += pr_lines(pr)
    return dict(by_repo)


def pick_open_source_award(agg_by_repo: dict[str, dict]) -> dict | None:
    """
    Pick a winner:
    - Primary: merged PR count (higher is better)
    - Tie-breaker: total lines changed
    """
    best = None
    for name, agg in agg_by_repo.items():
        cand = {"nameWithOwner": name, **agg}
        if not best:
            best = cand
            continue
        if cand["count"] > best["count"]:
            best = cand
        elif cand["count"] == best["count"] and cand["lines"] > best["lines"]:
            best = cand
    return best


def pick_pr_highlights(prs: list[dict], user_login: str, limit: int = 7) -> list[dict]:
    """
    Select highlight PRs for rendering:
    - External repos only
    - Sorted by code change lines descending
    """
    external = [pr for pr in prs if is_external_repo(pr.get("repository") or {}, user_login)]
    return sorted(external, key=pr_lines, reverse=True)[:limit]

