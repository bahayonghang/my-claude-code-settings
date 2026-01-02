from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass


@dataclass(frozen=True)
class CategoryDef:
    key: str
    label: str
    emoji: str
    description: str
    color: str
    topic_keywords: tuple[str, ...]
    languages: tuple[str, ...] = ()


DEFAULT_CATEGORIES: list[CategoryDef] = [
    CategoryDef(
        key="ai",
        label="AI / LLM",
        emoji="🧠",
        description="LLMs, agents, RAG, tooling around AI development.",
        color="#bc8cff",
        topic_keywords=("llm", "ai", "openai", "agent", "rag", "chatgpt", "transformer", "embedding"),
    ),
    CategoryDef(
        key="systems",
        label="Systems",
        emoji="🛠️",
        description="Compilers, runtimes, OS, performance, low-level tooling.",
        color="#58a6ff",
        topic_keywords=("os", "kernel", "compiler", "runtime", "perf", "benchmark", "wasm", "linux"),
        languages=("rust", "c", "c++", "zig", "go"),
    ),
    CategoryDef(
        key="data",
        label="Data",
        emoji="🗄️",
        description="Databases, engines, streaming, analytics.",
        color="#3fb950",
        topic_keywords=("database", "sql", "olap", "etl", "spark", "duckdb", "clickhouse", "postgres"),
    ),
    CategoryDef(
        key="frontend",
        label="Frontend",
        emoji="🪄",
        description="UI frameworks, visualization, web tooling.",
        color="#d29922",
        topic_keywords=("frontend", "react", "vue", "svelte", "css", "visualization", "webgl"),
        languages=("typescript", "javascript", "dart"),
    ),
    CategoryDef(
        key="devtools",
        label="DevTools",
        emoji="🔧",
        description="Editors, terminals, CLIs, productivity tooling.",
        color="#ffa657",
        topic_keywords=("cli", "terminal", "editor", "vim", "neovim", "tmux", "productivity"),
    ),
    CategoryDef(
        key="other",
        label="Other",
        emoji="🛰️",
        description="Everything else (kept explicit for verifiability).",
        color="#8b949e",
        topic_keywords=(),
    ),
]


def normalize(s: str) -> str:
    return (s or "").strip().lower()


def repo_topics(repo: dict) -> list[str]:
    topics = repo.get("topics") or []
    return [normalize(t) for t in topics if t]


def repo_language(repo: dict) -> str:
    return normalize(repo.get("primaryLanguage") or repo.get("language") or "")


def score_category(repo: dict, cat: CategoryDef) -> int:
    topics = repo_topics(repo)
    lang = repo_language(repo)
    score = 0
    for kw in cat.topic_keywords:
        if kw in topics:
            score += 2
    if lang and lang in cat.languages:
        score += 1
    return score


def categorize_repo(repo: dict, defs: list[CategoryDef] = DEFAULT_CATEGORIES) -> str:
    best_key = "other"
    best_score = -1
    for d in defs:
        s = score_category(repo, d)
        if s > best_score:
            best_score = s
            best_key = d.key
    return best_key if best_score > 0 else "other"


def stars_by_category(stars_year: list[dict], defs: list[CategoryDef] = DEFAULT_CATEGORIES) -> dict[str, int]:
    counts = defaultdict(int)
    for s in stars_year:
        k = categorize_repo(s, defs)
        counts[k] += 1
    return dict(counts)


def top_repos_by_category(stars_year: list[dict], defs: list[CategoryDef] = DEFAULT_CATEGORIES, per_cat: int = 6) -> dict[str, list[dict]]:
    buckets: dict[str, list[dict]] = defaultdict(list)
    for s in stars_year:
        buckets[categorize_repo(s, defs)].append(s)
    out: dict[str, list[dict]] = {}
    for k, items in buckets.items():
        out[k] = sorted(items, key=lambda r: int(r.get("stargazerCount") or 0), reverse=True)[:per_cat]
    return out

