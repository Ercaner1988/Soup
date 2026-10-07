export const meta = { name: 'es-pt-opus-review', description: 'Independent read-only Opus reviews of the parked Spanish and Portuguese READMEs', phases: [{ title: 'Review' }] }
const S = '/tmp/claude-0/-home-user-Soup/3128d5e5-c81a-53d8-9eba-d7cec93ccd70/scratchpad'
const L = [
  { f: S + '/README.es.md', lang: 'Spanish (neutral Latin-American/international)', persona: 'a native Spanish speaker, a senior technical editor for Spanish developer documentation' },
  { f: S + '/README.pt.md', lang: 'Brazilian Portuguese', persona: 'a native Brazilian Portuguese speaker, a senior technical editor for Brazilian developer documentation' },
]
const SCHEMA = { type: 'object', properties: { verdict: { type: 'string' }, score_out_of_10: { type: 'number' }, source_language_check: { type: 'string' }, findings: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['blocker', 'major', 'minor', 'nit'] }, line: { type: 'number' }, quote: { type: 'string' }, problem: { type: 'string' }, suggested_fix: { type: 'string' } }, required: ['severity', 'line', 'quote', 'problem', 'suggested_fix'] } } }, required: ['verdict', 'score_out_of_10', 'source_language_check', 'findings'] }
const out = await parallel(L.map(x => () => agent(
`You are ${x.persona}. You think and read in ${x.lang}; your only other skill is reading English so you can compare against the source. You are an independent reviewer and have seen no other reviewer's work and no translator's notes. This file was already revised once after an earlier review; judge it fresh.

READ-ONLY: never edit, create or delete any file, never run git. Review ${x.f}, a translation of /home/user/Soup/README.md (Soup, a CLI for fine-tuning LLMs). Read both completely, section by section.

Judge as a demanding native reader:
1. Completeness and fidelity: anything omitted, invented, softened, or whose meaning changed (numbers, claims, caveats, negations, the 'honest limits' wording).
2. Mistranslations, false friends, wrong words in context (link labels and calls to action included).
3. Naturalness: stiff, calqued or machine-like sentences, grammar, agreement, register, punctuation conventions of ${x.lang}.
4. Terminology consistency across the file.
5. English prose left untranslated that should be translated (code, commands, flags, paths, URLs, product names excepted).
6. Source-language check: say whether any passage reads as if translated via another language (e.g. Turkish word order or calques) rather than directly from the English; quote it if so.
Do NOT report code-block contents, URLs or ASCII decimal points as errors (the repo requires README.md's digits). At most 25 findings, most severe first, each with severity, line number, exact quote, problem in English, and a corrected replacement in ${x.lang}. Give a 2-sentence verdict and a publish-readiness score out of 10.`,
{ label: 'review:' + x.f.split('/').pop(), phase: 'Review', model: 'opus', schema: SCHEMA })))
return L.map((x, i) => ({ file: x.f.split('/').pop(), result: out[i] }))