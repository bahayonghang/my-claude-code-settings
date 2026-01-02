import argparse
import json
import re
from pathlib import Path


def embed(dataset_path: Path, html_path: Path) -> None:
    data = json.loads(dataset_path.read_text(encoding="utf-8"))
    json_text = json.dumps(data, ensure_ascii=False, indent=2).replace("<", "\\u003c")

    html = html_path.read_text(encoding="utf-8")

    # Case 1: placeholder-based template
    if "__DATASET_JSON__" in html:
        html_path.write_text(html.replace("__DATASET_JSON__", json_text), encoding="utf-8")
        return

    # Case 2: normal dataset <script> block exists
    block_pattern = r'(<script id="dataset" type="application/json">\s*)\{.*?\}(\s*</script>)'

    if re.search(block_pattern, html, flags=re.S):
        def repl(m: re.Match) -> str:
            return m.group(1) + json_text + m.group(2)

        html2 = re.sub(block_pattern, repl, html, flags=re.S)
        html_path.write_text(html2, encoding="utf-8")
        return

    raise SystemExit('dataset block not found: expected <script id="dataset" type="application/json">...')


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", required=True, type=Path)
    ap.add_argument("--html", required=True, type=Path)
    args = ap.parse_args()

    embed(dataset_path=args.dataset, html_path=args.html)
    print(f"embedded {args.dataset} -> {args.html}")


if __name__ == "__main__":
    main()
