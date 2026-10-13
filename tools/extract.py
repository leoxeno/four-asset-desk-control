"""Digest a run for grading and for the cost table in results.md.

Reads the qN.json files of one run directory and prints, per question:
turns, seconds, output tokens, bash calls, files opened with Read, whether
any call asked to leave the sandbox, the final ANSWER line if there is one,
the bold fragments, and the opening of the answer. With --full it prints the
whole answer text. Nothing here grades; a person does that in grading.yml.

Usage:
    python3 tools/extract.py control/run-1
    python3 tools/extract.py treatment/run-1 --full
    python3 tools/extract.py --table control/run-1 control/run-2 treatment/run-1 treatment/run-2
"""
import argparse
import json
import pathlib
import re
import statistics

ROOT = pathlib.Path(__file__).resolve().parents[1]


def load(run_dir: pathlib.Path) -> list[dict]:
    out = []
    for f in sorted(run_dir.glob("[qx]*.json"), key=lambda p: int(re.sub(r"\D", "", p.stem) or 0)):
        out.append(json.loads(f.read_text()))
    return out


FOLDER_FILES = ["README.md", "identity.md", "rules.md", "examples.md", "methodology.md", "data-dictionary.md", "monthly-adjusted-close.csv", "fetch-log.txt"]


def files_touched(d: dict) -> list[str]:
    """Folder files opened with the Read tool or named in a Bash command (cat, head, python open, ...), in order, without repeats."""
    seen: list[str] = []
    for c in d["tool_calls"]:
        names = []
        if c["tool"] == "Read" and c.get("file"):
            names = [pathlib.Path(c["file"]).name]
        elif c["tool"] == "Bash" and c.get("command"):
            names = [f for f in FOLDER_FILES if f in c["command"]]
        for n in names:
            if n not in seen:
                seen.append(n)
    return seen


def digest(d: dict, full: bool) -> str:
    txt = d.get("result_text") or ""
    answer_line = next((ln.strip() for ln in txt.splitlines() if ln.strip().startswith("ANSWER:") or ln.strip().startswith("`ANSWER:")), None)
    bolds = re.findall(r"\*\*(.+?)\*\*", txt)[:5]
    reads = files_touched(d)
    bash = sum(1 for c in d["tool_calls"] if c["tool"] == "Bash")
    left = sum(1 for c in d["tool_calls"] if c.get("asked_to_leave_sandbox"))
    words = len(re.findall(r"\b\w+\b", txt))
    lines = [
        f"### {d['label']}  [{d['status']}] turns {d['num_turns']}, {d['seconds']}s, out tokens {(d['usage'] or {}).get('output_tokens')}, words {words}, bash {bash}, files touched {reads}, left-sandbox {left}, denials {len(d.get('permission_denials') or [])}",
        f"answer line: {answer_line}",
        f"bold: {bolds}",
    ]
    lines.append(txt if full else "opening: " + txt[:400].replace("\n", " "))
    return "\n".join(lines) + "\n"


def table(run_dirs: list[pathlib.Path]) -> str:
    rows = ["| run | median s | median out tokens | median words | median turns | bash calls total | folder files touched per question (median) | left sandbox | denials |", "|---|---|---|---|---|---|---|---|---|"]
    for rd in run_dirs:
        qs = load(rd)
        if not qs:
            continue
        secs = statistics.median(q["seconds"] for q in qs)
        toks = statistics.median((q["usage"] or {}).get("output_tokens", 0) for q in qs)
        words = statistics.median(len(re.findall(r"\b\w+\b", q.get("result_text") or "")) for q in qs)
        turns = statistics.median(q["num_turns"] or 0 for q in qs)
        bash = sum(1 for q in qs for c in q["tool_calls"] if c["tool"] == "Bash")
        touched = statistics.median(len(files_touched(q)) for q in qs)
        left = sum(1 for q in qs for c in q["tool_calls"] if c.get("asked_to_leave_sandbox"))
        den = sum(len(q.get("permission_denials") or []) for q in qs)
        rows.append(f"| {rd.relative_to(ROOT) if rd.is_relative_to(ROOT) else rd} | {secs:.1f} | {toks:.0f} | {words:.0f} | {turns:.0f} | {bash} | {touched:.0f} | {left} | {den} |")
    return "\n".join(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dirs", nargs="+")
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--table", action="store_true")
    args = parser.parse_args()
    dirs = [(ROOT / p) if not pathlib.Path(p).is_absolute() else pathlib.Path(p) for p in args.run_dirs]
    if args.table:
        print(table(dirs))
        return
    for rd in dirs:
        print(f"## {rd}")
        for d in load(rd):
            print(digest(d, args.full))


if __name__ == "__main__":
    main()
