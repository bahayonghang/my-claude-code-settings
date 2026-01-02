from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Any
from zoneinfo import ZoneInfo

from .time_utils import hour_bucket, parse_iso8601, utc_month_range


@dataclass(frozen=True)
class StarEvent:
    starred_at: str
    name_with_owner: str
    url: str | None
    stars: int


def stars_in_year(stars: list[dict], year: int) -> list[dict]:
    prefix = f"{year}-"
    return [s for s in stars if isinstance(s, dict) and str(s.get("starredAt", "")).startswith(prefix)]


def group_star_events_by_month(stars_year: list[dict]) -> dict[str, list[StarEvent]]:
    by_month: dict[str, list[StarEvent]] = defaultdict(list)
    for s in stars_year:
        ts = str(s.get("starredAt") or "")
        repo = str(s.get("nameWithOwner") or "")
        if not ts or not repo:
            continue
        by_month[ts[:7]].append(
            StarEvent(
                starred_at=ts,
                name_with_owner=repo,
                url=s.get("url"),
                stars=int(s.get("stargazerCount") or 0),
            )
        )
    for m in list(by_month.keys()):
        by_month[m].sort(key=lambda e: e.starred_at)
    return by_month


def within_month_ratio(starred_at: str) -> float:
    dt_utc = parse_iso8601(starred_at).astimezone(tz=None)
    year = dt_utc.year
    month = dt_utc.month
    start_ms, end_ms = utc_month_range(year, month)
    t_ms = int(dt_utc.timestamp() * 1000)
    span = max(1, end_ms - start_ms)
    return max(0.0, min(1.0, (t_ms - start_ms) / span))


def hour_histogram(stars_year: list[dict], tz: ZoneInfo) -> list[int]:
    buckets = [0] * 24
    for s in stars_year:
        ts = s.get("starredAt")
        if not ts:
            continue
        buckets[hour_bucket(str(ts), tz)] += 1
    return buckets


def top_starred_repos(stars_year: list[dict], n: int = 10) -> list[tuple[str, int]]:
    counts = Counter()
    for s in stars_year:
        repo = s.get("nameWithOwner")
        if repo:
            counts[str(repo)] += 1
    return counts.most_common(n)


def filter_stars_by_date(stars_year: list[dict], yyyy_mm_dd: str) -> list[dict]:
    return [s for s in stars_year if str(s.get("starredAt") or "")[:10] == yyyy_mm_dd]


def build_holiday_cards(stars_year: list[dict], holidays: list[tuple[str, str]]) -> list[dict[str, Any]]:
    """
    holidays: list of (label, yyyy-mm-dd)
    Output: list of card dicts with verifiable repo lists.
    """
    out: list[dict[str, Any]] = []
    for label, date in holidays:
        hits = filter_stars_by_date(stars_year, date)
        if not hits:
            continue
        repos = sorted(hits, key=lambda s: int(s.get("stargazerCount") or 0), reverse=True)
        out.append(
            {
                "label": label,
                "date": date,
                "count": len(repos),
                "repos": [
                    {
                        "nameWithOwner": r.get("nameWithOwner"),
                        "url": r.get("url"),
                        "stars": int(r.get("stargazerCount") or 0),
                        "starredAt": r.get("starredAt"),
                    }
                    for r in repos[:4]
                ],
            }
        )
    return out

