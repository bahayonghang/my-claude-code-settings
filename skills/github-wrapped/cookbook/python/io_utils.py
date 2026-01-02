from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def flatten_graphql_pages(pages: Iterable[dict]) -> list[dict]:
    """
    `gh api graphql --paginate --slurp` yields a JSON array of "page" objects.
    This helper normalizes the common case where you want a flat list of those pages.
    """
    out: list[dict] = []
    for p in pages:
        if isinstance(p, dict):
            out.append(p)
    return out


def flatten_starred_edges(starred_pages: list[dict]) -> list[dict]:
    edges: list[dict] = []
    for page in starred_pages:
        chunk = (((page.get("data") or {}).get("user") or {}).get("starredRepositories") or {}).get("edges") or []
        for e in chunk:
            if isinstance(e, dict):
                edges.append(e)
    return edges


def flatten_search_nodes(search_pages: list[dict]) -> list[dict]:
    nodes: list[dict] = []
    for page in search_pages:
        chunk = (((page.get("data") or {}).get("search") or {}).get("nodes")) or []
        for n in chunk:
            if isinstance(n, dict):
                nodes.append(n)
    return nodes

