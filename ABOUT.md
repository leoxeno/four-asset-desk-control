# About this repository

Entry for Clief Notes Weekly Comp 14, "The Control", by Stavros Stavroglou, 13 October 2026.

The folder under test is the five files at the root: `README.md` (the map), `identity.md`, `rules.md`, `examples.md` and `reference/`. It answers numeric questions about four ETFs from one month-end price file under one written methodology. This file is not part of the folder and is never shown to the model.

The test around it:

| Path | What it is |
|------|------------|
| `questions.md` | eight questions with expected answers and grading rules, committed before any run; numbers computed by `tools/answer_key.py` |
| `PROTOCOL.md` | how both arms were run, command by command, and how to re-run them |
| `control/` | the bare model, no folder, no files; two runs |
| `treatment/` | the folder; two runs per map version (`v1/`, `v2/`, `v3/`), plus the walk test |
| `results.md` | what changed, question by question, losses and ties first |
| `grading.yml` | the verdicts behind the scoreboard; `tools/score.py` renders them |
| `outside-check/` | questions written by a blank session that never saw the folder, keyed before any run on them |
| `tools/` | fetch, answer key, runner, sandbox check, digest, scoreboard, lint |

Order of events, provable from the commit log: questions and data, then the control runs, then the folder with its first map, then the walk test, then treatment v1 and results v1, then the second map and treatment v2, then the third map and treatment v3, then the outside check keyed and run on both arms with the third map.

A private pilot preceded this repo. On the morning of 13 October 2026 I ran the same questions, the same harness and the same data snapshot in a private repository with three arms: the two here plus a data-only arm that held the price file and its dictionary without the folder. The folder's map was refined there, over three versions, against these same questions; the only cost the pilot found in the folder was that the first map made the model read seven files per question. This repo is the clean two-arm run the brief asks for. It starts from the pilot's first map and re-runs the two map changes in its own history, each applied after its cause appeared in this repo's own runs. Every transcript here was recorded in this repo, in the order the commit log shows; nothing was copied from a pilot run. The pilot's data-only arm matched the answer key on every question, which is why `results.md` says plainly that a cold-versus-folder comparison cannot separate the data from the structure.

Headline, from `results.md`: against nothing, the folder won every question that needed the data and tied the two that did not, on the eight committed questions and on three a stranger wrote; the bare model declined and invented nothing. What the folder cost was reading, seven files per question until one line in the map brought it to four; what it bought was a checkable answer line on forty-seven of forty-eight answers and the method named every time.
