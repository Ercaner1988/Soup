# Reviewer prompt (as used; see ../workflows/*.js for the exact text and JSON schema)

Persona: native speaker of <LANG>, senior technical editor; reads English only to compare.
Independent: no other reviewer's work, no translator notes. READ-ONLY.
Checks: fidelity (omissions, inventions, softened caveats/negations/numbers); mistranslations and
false friends incl. link labels; naturalness/register/punctuation; terminology consistency;
untranslated English prose; (round 2) whether the text reads as relayed through another language.
Exclusions: code-block contents, URLs, ASCII decimal points (repo rule).
Output: <= 25-30 findings, most severe first: severity (blocker/major/minor/nit), line, exact quote,
problem (English), corrected replacement (target language); 2-sentence verdict; score /10.
