# Protocol: how every arm was run, command by command

Instructions for whoever re-runs this. Written 13 October 2026. Every arm was run by one script, `tools/run_arm.py`, through Claude Code's headless mode, so a re-run is one command per arm. The brief's claude.ai method is described at the end as the fallback for anyone without Claude Code.

A private pilot by the same author preceded this repo, on the same machine, with the same harness, the same data snapshot and the same pre-registered questions; `ABOUT.md` says what it was. Every transcript here was recorded in this repo, in the order the commit log shows.

## The arms

| Arm | Output folder | Working directory holds | Extra system-prompt line | What it measures |
|-----|---------------|-------------------------|--------------------------|------------------|
| cold | `control/` | nothing | none | the bare model: memory, priors, hedging, invention. The brief's "no folder". |
| treatment | `treatment/` | `README.md`, `identity.md`, `rules.md`, `examples.md`, `reference/methodology.md`, `reference/data/data-dictionary.md`, `reference/data/monthly-adjusted-close.csv`, `reference/data/fetch-log.txt` | `Read README.md first and follow it.` | the folder |

The base system prompt in every arm is the single sentence `Answer the user's question.` The extra line is the headless analogue of claude.ai project instructions: it says what is in the project and nothing more. Each run's exact system prompt is saved as `system-prompt.txt` beside its transcript.

Every arm runs twice (`run-1/`, `run-2/`). Each question is answered in a fresh session from a throwaway working directory under `/srv/comp14-runs/` that holds only that arm's files and is deleted after the answer. `questions.md`, `tools/`, `control/`, `treatment/`, `grading.yml` and `results.md` are never inside a working directory, and the sandbox denies reads of the repo's location anyway.

Within a run the questions run concurrently, `--jobs 8`, each in its own session and its own working directory; the transcript keeps the committed order. The pilot tested three concurrent sandboxed sessions per arm: the network was still refused, the answers were unchanged and no session could see another's working directory. Each run's `run-info.json` records the job count used.

Order of events: cold control (both runs) first, before the folder existed. Then the folder, committed and walk-tested. Then treatment (both runs). Then results. Then the outside check: three questions written by a blank session, keyed and committed, then run on both arms (both runs). The commit timestamps on GitHub are the record; each run's `run-info.json` names the commit it ran against.

## Settings, identical in every arm

| Setting | Value | Why |
|---------|-------|-----|
| Model | `claude-opus-5-5`, pinned with `--model`; the stream's init event records the resolved model | same model in every arm |
| Effort | `high` | same in every arm |
| Tools | `Bash, Read, Write, Glob, Grep` only, via `--tools`; `WebSearch` and `WebFetch` also removed via `--disallowedTools`; `Read` and `Write` scoped to the working directory via `--allowedTools` | the same calculator in every arm; no web search, no web fetch, no subagents |
| Permissions | `--permission-mode dontAsk`, `--permission-prompts none` | allowed tools run, anything else is refused and recorded in `permission_denials`; nothing can prompt a human who is not there |
| Sandbox | Claude Code sandbox on with `failIfUnavailable` (a machine without it cannot run the arm unsandboxed by mistake) and `allowUnsandboxedCommands: false` (a blocked command cannot be retried outside the sandbox); network: no domains, strict allow-list; writes confined to the working directory; reads denied under `/root`, `/home`, `/mnt`, `/tmp`, `/var/tmp`, plus `blockReadsOutsideWorkingDirectories` for the file tools and Bash | a control that can download prices is not a control; a session must not find another session's files or this repo |
| Customisations | `--safe-mode`, `--strict-mcp-config`, `--setting-sources ""` | no CLAUDE.md, memory, skills, plugins, hooks or MCP servers from this machine |
| Sessions | `--no-session-persistence`, one fresh session per question | nothing carries over between questions or runs |
| Prompt | passed as the argument, verbatim from the `Prompt:` line in `questions.md` | the same words in every arm |
| Output | `--output-format stream-json --verbose`, saved raw as `qN.jsonl`; result object as `qN.json`; `run-info.json` with the command, settings, versions, repo commit and times; `transcript.md` rendered from the events, unedited | a mod reads tokens, seconds, turns, tool calls, the files the model opened, and whether it ever asked to leave the sandbox |

Why `allowUnsandboxedCommands: false` is there: in a smoke test before any scored run of the pilot, the bare model, asked question 8, had its price requests blocked by the sandbox and then re-issued two commands with the sandbox switched off, which the default settings allow, and came back with live October prices. That smoke run was discarded and the setting added before any scored run, there or here. Every scored run's transcript carries a per-question count of "asked to leave sandbox" so a reader can see it never happened.

The sandbox was proved on this repo before any scored run with `python3 tools/check_sandbox.py`; its output is kept in `tools/sandbox-check.log`. In it, a `curl` to Yahoo Finance and a `find` for the price file are refused by the permission layer before they run, a Python `urlopen` that does run is closed by the proxy without a response, and the Read tool is refused outside the working directory.

Two artefacts a reader will notice in transcripts. First, Claude Code adds its own environment block to every session (working directory, platform, today's date), so the bare model knows the date; that is identical across arms. Second, the sandbox creates a `.claude` folder and masks dotfiles inside the working directory; the model may mention "config files" it did not ask for. Neither is part of any arm.

## Re-run an arm

Needs Python 3.10+, Claude Code on your PATH and logged in, and on Linux the sandbox dependencies `bubblewrap` and `socat` (`apt install bubblewrap socat`). macOS uses the built-in sandbox. Run from the repo root:

```bash
python3 tools/check_sandbox.py                 # prove the network is sealed on your machine first
python3 tools/run_arm.py cold 3 --jobs 8       # any run number that does not exist yet
python3 tools/run_arm.py treatment 3 --jobs 8
```

`--jobs 1` runs the questions one after another and changes nothing else. The runner never overwrites a run. Each run's `run-info.json` names the commit it ran against; check that commit out first to reproduce the folder exactly as it was.

To grade a run, read `questions.md` and apply its rules to each `qN.json` `result_text`, then record verdicts in `grading.yml` and run `python3 tools/score.py --write`. `python3 tools/extract.py control/run-1` prints a digest of a run for grading.

## The one redaction

Every Bash call inside the sandbox goes through a local proxy with a throwaway username and password unique to that call; they die with the call. The bare model prints them when it runs `env` or `curl -v` while trying to download prices, and secret scanners flag them. `tools/scrub.py` replaces exactly those strings with `[REDACTED-SANDBOX-PROXY-CREDENTIAL]`. The runner applies it before saving any file and records the count per question in `qN.json` as `sandbox_proxy_credentials_redacted`; a count above zero in a cold session means the model printed its environment, nothing more. Nothing else in any transcript is ever changed, and the lint fails on the pattern. If a scanner flags a string the pattern missed, it is the same kind of dead credential: resolve it as revoked and leave the history alone.

## What counts as an incident

A timed-out or crashed question is recorded as a failed answer in its `qN.json` and the run continues. A run is never restarted to get a nicer answer. If a run had to be abandoned, its folder stays, with a note in `run-info.json`.

## Fallback: the brief's method in claude.ai

Without Claude Code: the cold arm is a fresh claude.ai chat with no project; the treatment is a project whose knowledge holds the folder files listed above, with the project instruction `Read README.md first and follow it.` Same model in every arm, web search off, memory off, the analysis tool on in both arms, one message per question in order, no follow-ups, no regenerate. claude.ai's own system prompt differs from the CLI's, so expect some drift in wording, not in numbers.

## What this protocol never allows

Editing a transcript. Dropping a run. Changing a setting between arms. Letting any arm reach the network.
