#!/usr/bin/env bash
# Two checks before every push. Exit 1 on any hit.
#   1. No em dashes in anything we wrote (house style of the ICM repos).
#      Raw model output is exempt: transcripts under control/, treatment/,
#      outside-check/ and the sandbox log are never edited, dashes included.
#   2. Nothing that looks like a key or token, anywhere.
set -u
cd "$(dirname "$0")/.."
status=0
raw=(':!tools/lint.sh' ':!control/**' ':!treatment/**' ':!outside-check/**' ':!tools/sandbox-check.log')

if git grep -nI $'\xe2\x80\x94' -- . "${raw[@]}" >/dev/null 2>&1; then
  echo "em dash found:"
  git grep -nI $'\xe2\x80\x94' -- . "${raw[@]}"
  status=1
fi

pattern='(sk-ant-[A-Za-z0-9_-]{8,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{12,}|srt\.[A-Za-z0-9+/=]+:[0-9a-f]{16,}@|Proxy-Authorization: Basic [A-Za-z0-9+/=]{8,}|(api[_-]?key|secret|token|password)[[:space:]]*[:=][[:space:]]*["'"'"'][A-Za-z0-9_/+=-]{12,})'
if git grep -nIE "$pattern" -- . ':!tools/lint.sh' >/dev/null 2>&1; then
  echo "possible secret found:"
  git grep -nIE "$pattern" -- . ':!tools/lint.sh'
  status=1
fi

[ "$status" -eq 0 ] && echo "lint: clean"
exit "$status"
