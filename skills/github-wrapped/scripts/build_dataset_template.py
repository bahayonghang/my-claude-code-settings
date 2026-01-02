import argparse
import datetime as dt
import json
from collections import Counter, defaultdict
from pathlib import Path
from zoneinfo import ZoneInfo


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def parse_iso8601(ts: str) -> dt.datetime:
    if not ts:
        raise ValueError("empty timestamp")
    if ts.endswith("Z"):
        ts = ts[:-1] + "+00:00"
    return dt.datetime.fromisoformat(ts)


def to_local(ts: str, tz: ZoneInfo) -> dt.datetime:
    return parse_iso8601(ts).astimezone(tz)


def safe_int(x, default=0) -> int:
    try:
        return int(x)
    except Exception:
        return default


def flatten_starred_edges(starred_pages: list[dict]) -> list[dict]:
    edges: list[dict] = []
    for page in starred_pages:
        chunk = (((page.get("data") or {}).get("user") or {}).get("starredRepositories") or {}).get("edges") or []
        for e in chunk:
            if e:
                edges.append(e)
    return edges


def flatten_pr_nodes(pr_pages: list[dict]) -> list[dict]:
    nodes: list[dict] = []
    for page in pr_pages:
        chunk = (((page.get("data") or {}).get("search") or {}).get("nodes")) or []
        for n in chunk:
            if n:
                nodes.append(n)
    return nodes


def build_dataset(raw_dir: Path, year: int, tz: ZoneInfo) -> dict:
    # 1) user
    user_raw = load_json(raw_dir / "user.json")

    # 2) contributions (GraphQL)
    contrib_raw = load_json(raw_dir / "contributions.json")
    cc = (((contrib_raw.get("data") or {}).get("user") or {}).get("contributionsCollection")) or {}
    calendar = cc.get("contributionCalendar") or {}
    weeks = calendar.get("weeks") or []

    days = []
    for w in weeks:
        for d in (w.get("contributionDays") or []):
            days.append(
                {
                    "date": d.get("date"),
                    "count": safe_int(d.get("contributionCount")),
                    "weekday": safe_int(d.get("weekday")),
                }
            )
    days = [d for d in days if d.get("date")]
    days.sort(key=lambda x: x["date"])

    # busiest day
    max_count = max((d["count"] for d in days), default=0)
    busiest = next((d for d in days if d["count"] == max_count and max_count > 0), {"date": None, "count": 0})

    # longest streak (simple consecutive positive days)
    longest = {"days": 0, "start": None, "end": None}
    cur = 0
    cur_start = None
    prev_date = None

    for d in days:
        date = dt.date.fromisoformat(d["date"])
        if d["count"] > 0:
            if cur == 0:
                cur_start = date
            cur += 1
        else:
            if cur > longest["days"]:
                longest = {"days": cur, "start": cur_start.isoformat() if cur_start else None, "end": prev_date.isoformat() if prev_date else None}
            cur = 0
            cur_start = None
        prev_date = date

    if cur > longest["days"]:
        longest = {"days": cur, "start": cur_start.isoformat() if cur_start else None, "end": prev_date.isoformat() if prev_date else None}

    # month totals
    month_totals = defaultdict(int)
    for d in days:
        month_totals[d["date"][:7]] += d["count"]

    # weekday distribution
    weekday_sums = [0] * 7
    for d in days:
        wd = d.get("weekday")
        if isinstance(wd, int) and 0 <= wd <= 6:
            weekday_sums[wd] += d["count"]

    # 3) starred repos (GraphQL pages)
    starred_pages = load_json(raw_dir / "starred_repos_pages.json")
    star_edges = flatten_starred_edges(starred_pages)

    stars = []
    for e in star_edges:
        node = e.get("node") or {}
        stars.append(
            {
                "starredAt": e.get("starredAt"),
                "nameWithOwner": node.get("nameWithOwner"),
                "url": node.get("url"),
                "description": node.get("description"),
                "stargazerCount": safe_int(node.get("stargazerCount")),
                "forkCount": safe_int(node.get("forkCount")),
                "primaryLanguage": ((node.get("primaryLanguage") or {}).get("name")),
                "topics": [
                    ((t.get("topic") or {}).get("name"))
                    for t in (((node.get("repositoryTopics") or {}).get("nodes")) or [])
                    if ((t.get("topic") or {}).get("name"))
                ],
                "owner": ((node.get("owner") or {}).get("login")),
            }
        )

    stars = [s for s in stars if s.get("starredAt") and s.get("nameWithOwner")]
    stars.sort(key=lambda s: s["starredAt"], reverse=True)

    stars_2025 = [s for s in stars if (s["starredAt"] or "").startswith(f"{year}-")]
    stars_before = [s for s in stars if not (s["starredAt"] or "").startswith(f"{year}-")]

    stars_by_year = Counter([(s["starredAt"] or "")[:4] for s in stars if s.get("starredAt")])

    # star events by month (for per-month timeline charts)
    star_events_by_month: dict[str, list[dict]] = defaultdict(list)
    for s in stars_2025:
        month = (s["starredAt"] or "")[:7]
        star_events_by_month[month].append(
            {
                "starredAt": s["starredAt"],
                "nameWithOwner": s["nameWithOwner"],
                "stars": s["stargazerCount"],
                "url": s.get("url"),
            }
        )
    for k in list(star_events_by_month.keys()):
        star_events_by_month[k].sort(key=lambda x: x.get("starredAt") or "")

    # 4) repos (REST)
    repos = load_json(raw_dir / "user_repos.json")
    repos = [r for r in repos if isinstance(r, dict)]

    # 5) PR pages (GraphQL search)
    pr_path = raw_dir / f"prs_{year}_pages.json"
    pr_pages = load_json(pr_path) if pr_path.exists() else []
    pr_nodes = flatten_pr_nodes(pr_pages)

    login = (user_raw.get("login") or "").lower()
    external_prs = []
    for pr in pr_nodes:
        repo = pr.get("repository") or {}
        owner = ((repo.get("owner") or {}).get("login") or "").lower()
        if owner and login and owner != login:
            external_prs.append(pr)

    # Select a simple “Open Source Award” candidate.
    pr_score_by_repo = defaultdict(lambda: {"count": 0, "additions": 0, "deletions": 0, "repo": None})
    for pr in external_prs:
        repo = pr.get("repository") or {}
        name = repo.get("nameWithOwner")
        if not name:
            continue
        rec = pr_score_by_repo[name]
        rec["repo"] = repo
        rec["count"] += 1
        rec["additions"] += safe_int(pr.get("additions"))
        rec["deletions"] += safe_int(pr.get("deletions"))

    def score(rec: dict) -> int:
        return rec["count"] * 1000 + rec["additions"] + rec["deletions"]

    best_repo_name = None
    best_rec = None
    for name, rec in pr_score_by_repo.items():
        if not best_rec or score(rec) > score(best_rec):
            best_repo_name = name
            best_rec = rec

    award = None
    if best_rec and best_repo_name:
        repo = best_rec.get("repo") or {}
        award = {
            "nameWithOwner": best_repo_name,
            "url": repo.get("url"),
            "stargazerCount": safe_int(repo.get("stargazerCount")),
            "language": ((repo.get("primaryLanguage") or {}).get("name")),
            "mergedPrs": best_rec["count"],
            "additions": best_rec["additions"],
            "deletions": best_rec["deletions"],
        }

    # month list (YYYY-01..YYYY-12) for stable rendering
    months = [f"{year}-{m:02d}" for m in range(1, 13)]

    dataset = {
        "meta": {
            "year": year,
            "timezone": str(tz),
            "generatedAt": dt.datetime.now(dt.timezone.utc).isoformat(),
            "dataProvenance": {
                "rawDir": str(raw_dir),
                "notes": [
                    "All numbers are derived from saved gh API raw JSON (no fabricated data).",
                    "GitHub Events API keeps only ~90 days of history; any 'late night' facts must be marked best-effort.",
                    "Repository stars/forks are snapshots (not year increment) unless you collected a stargazer timeline.",
                ],
            },
        },
        "user": {
            "login": user_raw.get("login"),
            "name": user_raw.get("name"),
            "avatarUrl": user_raw.get("avatar_url"),
            "createdAt": user_raw.get("created_at"),
            "followers": safe_int(user_raw.get("followers")),
            "following": safe_int(user_raw.get("following")),
        },
        "year": {
            "contributions": {
                "total": safe_int((calendar.get("totalContributions"))),
                "totalCommits": safe_int(cc.get("totalCommitContributions")),
                "totalPrs": safe_int(cc.get("totalPullRequestContributions")),
                "totalIssues": safe_int(cc.get("totalIssueContributions")),
                "calendarWeeks": weeks,
                "busiestDay": busiest,
                "longestStreak": longest,
                "weekdaySums": weekday_sums,
                "byMonth": [{"month": m, "contributions": safe_int(month_totals.get(m, 0))} for m in months],
            },
            "repos": {
                "ownTotal": len(repos),
                "ownStarsTotalSnapshot": sum(safe_int(r.get("stargazers_count")) for r in repos),
                "ownForksTotalSnapshot": sum(safe_int(r.get("forks_count")) for r in repos),
            },
            "stars": {
                "totalInYear": len(stars_2025),
                "totalAllTime": len(stars),
                "byYear": dict(sorted(stars_by_year.items())),
                "byMonthInYear": [
                    {
                        "month": m,
                        "count": sum(1 for s in stars_2025 if (s["starredAt"] or "").startswith(m)),
                        "events": star_events_by_month.get(m, []),
                    }
                    for m in months
                ],
            },
            "openSourceAward": award,
        },
    }

    return dataset


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True, help="Base dir, e.g. data/github-wrapped-2025")
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--tz", default="Asia/Shanghai")
    args = ap.parse_args()

    base = Path(args.base)
    raw_dir = base / "raw"
    out_dir = base / "processed"
    out_dir.mkdir(parents=True, exist_ok=True)

    dataset = build_dataset(raw_dir=raw_dir, year=args.year, tz=ZoneInfo(args.tz))

    out_path = out_dir / "dataset.json"
    out_path.write_text(json.dumps(dataset, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
