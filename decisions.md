# Decisions and rules learned on MakazhanAlpamys/Soup (2026-10-06 .. 10-07)

Source of truth: the PR and issue threads named here. Quotes are paraphrased unless marked.

## Maintainer rules (binding for Soup)

1. **A translation goes in only with a named human reader.** "A README translation is taken only
   when a named person reads that language and keeps the file in sync; an LLM prompted as a native
   speaker does not count as a reviewer" (#1680, 2026-10-07).
2. **Wording changes go in on the maintainer's word, only for what that person can vouch for.**
   Turkish (native) and Arabic (upper-intermediate) accepted; Japanese at lower-intermediate was not
   (#1681).
3. **Russian:** accepted, @MakazhanAlpamys reads it and is its MAINTAINERS entry (#1680).
4. **Spanish, Portuguese:** parked, not rejected, until a native reader is named maintainer (#1691).
5. **Chinese:** belongs to #1632 (@Momoyeyu, zh-Hans, staged locally). Do not compete with it.
6. **Ratchet rules** (tests/test_readme_translation_sync.py): stamp = sha256 of LF-normalised
   README.md with `What's New` bodies stripped; any README.md edit (even the banner) re-stamps every
   translation; code blocks byte-identical except `#` comments; URLs, link targets, inline code and
   ASCII digits identical (119.6, never 119,6); `What's New` exempt from structure but not from
   existence; banner lists exactly the READMEs that exist; MAINTAINERS entry required per file.
7. **Changelog:** fragment `changelog.d/<latest-release>/<PR number>.<category>.md`, text mentions
   `#<PR number>`; validate with `scripts/assemble_changelog.py --root <copy>` (it consumes files).
8. **Do not widen a PR** to fix unrelated CI; a maintainer writes CI-breakage fixes (#1675 -> #1682).
9. **Be exact about who reviewed.** Saying "native-speaker reviewers" for LLMs was the one thing the
   maintainer had to ask about; the fix was to say it plainly in the PR, changelog and a comment.

## What the review rounds showed

- Round 1 (Sonnet 5.5, 7 reviewers, 209 findings): scores 7-8/10; no dropped facts, but recurring
  calque classes across languages: "honest gates", "existed nowhere", "running an issue", "wheels",
  "breaking change", Pydantic "model" read as an LLM, "loop-hardening" read as reinforcement,
  "supply-chain controls" read as logistics management.
- Translators made errors a ratchet cannot see: "Donate" -> "Done" (es); claiming an exempt heading
  must stay English (zh, ru); an added code span the English lacks (ja:100); added glosses
  ("(Pydantic)", "multimodal" for "vision") in ru.
- Round 2 (Opus 5.5): es 8.5, pt 8, ja-from-tr 8.5; source check found no relay through another
  language for es/pt.
- Pivot translation tr -> ja surfaced two real drifts in README.tr.md ("filtered" vs "escaped";
  added "only" before 1.4%), fixed in #1681. Pivoting is a cross-check, not only a risk.
- Ratchet blind spots (mutation-tested): dropped fact-free sentence, flipped negation, re-stamp
  without re-translation, commented-out YAML, a number swapped for another in the same section.

## PR map

| PR | Content | State 2026-10-07 |
|---|---|---|
| #1677 | Apache-2.0 / NOTICE housekeeping questions | open, no reply |
| #1680 | README.ru.md, maintainer @MakazhanAlpamys | ready for review |
| #1681 | tr + ar rewording, two tr factual fixes | ready for review |
| #1691 | es + pt, parked | draft |
| #1696 | ja retranslated from tr; asks how to group es/pt/ja | draft |

## Tools used

Claude Code (cloud session) and the Claude desktop app. Round 1 agents: Claude Sonnet 5.5 (session
model, no override). Round 2 and later edits: Claude Opus 5.5.
