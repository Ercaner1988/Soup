export const meta = { name: 'readme-native-review', description: 'Seven independent native-speaker reviews of README translations (read-only)', phases: [{ title: 'Review' }] }
const L = [
  { f: 'README.es.md', lang: 'Spanish (neutral Latin-American/international)', persona: 'a native Spanish speaker, a senior technical editor for Spanish developer documentation' },
  { f: 'README.pt.md', lang: 'Brazilian Portuguese', persona: 'a native Brazilian Portuguese speaker, a senior technical editor for Brazilian developer documentation' },
  { f: 'README.zh.md', lang: 'Simplified Chinese (zh-CN)', persona: 'a native Mandarin speaker from mainland China, a senior technical editor for Chinese developer documentation' },
  { f: 'README.ru.md', lang: 'Russian', persona: 'a native Russian speaker, a senior technical editor for Russian developer documentation' },
  { f: 'README.tr.md', lang: 'Turkish', persona: 'a native Turkish speaker, a senior technical editor for Turkish developer documentation' },
  { f: 'README.ja.md', lang: 'Japanese', persona: 'a native Japanese speaker, a senior technical editor for Japanese developer documentation' },
  { f: 'README.ar.md', lang: 'Arabic (Modern Standard, tech-register)', persona: 'a native Arabic speaker, a senior technical editor for Arabic developer documentation' },
]
const SCHEMA = { type: 'object', properties: { verdict: { type: 'string' }, score_out_of_10: { type: 'number' }, findings: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['blocker', 'major', 'minor', 'nit'] }, line: { type: 'number' }, quote: { type: 'string' }, problem: { type: 'string' }, suggested_fix: { type: 'string' } }, required: ['severity', 'line', 'quote', 'problem', 'suggested_fix'] } } }, required: ['verdict', 'score_out_of_10', 'findings'] }
const out = await parallel(L.map(x => () => agent(
`You are ${x.persona}. You think and read in ${x.lang}; your only other skill is reading English so you can compare against the source. You are an independent reviewer and have seen no other reviewer's work and no translator's notes.

Task (READ-ONLY: never edit, create or delete any file, never run git): review /home/user/Soup/${x.f}, a translation of /home/user/Soup/README.md (Soup, a CLI for fine-tuning LLMs). Read both files completely, section by section.

Judge as a demanding native reader, not as a checker of formatting:
1. Completeness and fidelity: anything omitted, invented, softened, or whose meaning changed (numbers, claims, caveats, negations, 'honest limits' wording).
2. Mistranslations and wrong word choices, including false friends and words that mean something else in context (e.g. a link label or call-to-action that does not mean what the English means).
3. Naturalness: would a native developer find any sentence stiff, calqued, machine-like, ungrammatical, or in the wrong register? Agreement, case, particles, counters, honorific level, punctuation and spacing conventions of ${x.lang}.
4. Terminology consistency across the whole file (same English term always rendered the same way; sensible choice of what stays in English).
5. English prose left untranslated that should have been translated (ignore code, commands, flags, paths, URLs, product names, badge alt texts only if conventionally kept).
6. Headings: natural, and any in-page link text matching its heading.
Do NOT report code-block contents or URLs as errors; do not pad. Report at most 30 findings, most severe first. Each finding: severity (blocker = wrong meaning or unusable; major = clear error or very unnatural; minor; nit), the line number in ${x.f}, the exact quoted text, the problem (in English), and a concrete corrected replacement written in ${x.lang}. Also give an overall verdict (2 sentences) and a score out of 10 for publish-readiness.`,
{ label: 'review:' + x.f, phase: 'Review', schema: SCHEMA })))
return L.map((x, i) => ({ file: x.f, result: out[i] }))