# Translator prompt (as used, round 1 es/pt/zh/ru; round 2 ja from tr)

Role: professional technical translator, native-level <LANG>, ML/devtools background.
Task: create/rewrite README.<lang>.md as a COMPLETE translation of the SOURCE (README.md, or
README.tr.md for the ja pivot with README.md as factual authority). Edit only that file; no git.
Hard rules (enforced by tests/test_readme_translation_sync.py):
1. Line 1 = exact sync stamp line; line 2 = exact banner line (given verbatim).
2. Same `## ` sections and heading levels in order; fenced code identical except `#` comments;
   identical inline code, URLs, relative link targets, image paths, HTML; in-page anchors resolve
   to translated headings (GitHub slug rule).
3. README.md's ASCII digits exactly; numbers written as words stay words.
4. `What's New` exempt from structure but translated fully, and its heading may be translated.
5. (pivot) Where the source deviates from README.md in fact, follow README.md and list it.
Quality: complete, idiomatic, consistent terminology, register stated per language, known traps
listed explicitly (e.g. "Donate" is a call to action; "supply-chain controls" are security controls;
a Pydantic "model" is a schema model; "honest gates" = stating the hardware requirement plainly).
Self-test: run the sync test until green; report wording choices and any deviations.
