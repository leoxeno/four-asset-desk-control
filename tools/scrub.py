"""Redact the sandbox's own per-command proxy credentials from raw output.

Every Bash call inside Claude Code's sandbox goes through a local proxy on
localhost:3128 with a throwaway username and password unique to that call
(the username is "srt." plus the tool-call id in base64, the password a
random hex string). They die with the call and cannot be reused, but they
are credential-shaped, and the bare model printed them when it ran `env`
and `curl -v` while trying to download prices. Secret scanners flag them.

This is the only transformation ever applied to raw output. It replaces
exactly these strings with a visible placeholder and nothing else; the
model's words, its commands and its results are untouched. tools/run_arm.py
applies it before saving any file, and it was applied once, retroactively,
to the four cold-control transcripts recorded before it existed (see the
commit that added this file).

Usage:
    python3 tools/scrub.py <file> [<file> ...]     # rewrite in place, print counts
"""
import pathlib
import re
import sys

PATTERNS = [
    # http://srt.<base64>:<hex>@localhost:3128  and socks5h://... variants
    (re.compile(r"srt\.[A-Za-z0-9+/=]+:[0-9a-f]{16,}@"), "[REDACTED-SANDBOX-PROXY-CREDENTIAL]@"),
    # the same credential sent as a header
    (re.compile(r"Proxy-Authorization: Basic [A-Za-z0-9+/=]+"), "Proxy-Authorization: Basic [REDACTED-SANDBOX-PROXY-CREDENTIAL]"),
]


def scrub_text(text: str) -> tuple[str, int]:
    total = 0
    for pattern, replacement in PATTERNS:
        text, n = pattern.subn(replacement, text)
        total += n
    return text, total


def main() -> None:
    for name in sys.argv[1:]:
        path = pathlib.Path(name)
        text, n = scrub_text(path.read_text())
        if n:
            path.write_text(text)
        print(f"{path}: {n} redacted")


if __name__ == "__main__":
    main()
