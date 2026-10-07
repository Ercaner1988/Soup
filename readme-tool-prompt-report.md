# PROMPT REPORT — "polyreadme": çok dilli README üretme / çevirme / senkron / kalite denetim aracı

Kaynak: Soup (MakazhanAlpamys/Soup), yerel klon `/home/user/Soup`, 2026-10-06.
Hedef okuyucu: bu raporu alıp yeni, bağımsız bir repo kuracak gelecekteki oturum.

---

## 0. Yöntem ve doğrulama beyanı (önce okuyun)

- **Alt-ajan delegasyonu yapılamadı.** Görev, her bölüm için paralel Haiku alt-ajanları istiyordu; bu oturumda
  `Agent` aracı yoktu (ToolSearch ile arandı, yalnızca SendMessage/TaskStop vb. döndü). Bu nedenle tüm okuma
  **doğrudan benim tarafımdan**, betikle özetleyerek (grep/python) yapıldı. Sonuç: aşağıdaki iddiaların hepsi
  birincil kaynaktan geliyor, alt-ajan özetinden gelen iddia **yok**. Bedeli: büyük README gövdeleri satır satır
  okunmadı; çeviri dosyaları tipografi/başlık/anchor/sayı ölçümleriyle ve review bulgularıyla incelendi.
- Repo'da **hiçbir dosya değiştirilmedi**, git yazma komutu çalıştırılmadı, GitHub'a hiçbir şey yazılmadı
  (yalnızca `gh api` ile salt-okunur commit/issue okuması). Mutasyon denemeleri scratchpad kopyasında yapıldı
  (`scratchpad/mut/`).
- **Klon sığ (shallow)**: `git rev-parse --is-shallow-repository` → `true`, 50 commit; README geçmişi yerelde tek
  commit gösteriyor. Geçmiş, GitHub API'den (salt-okunur) alındı.

**Kendim doğruladıklarım (V)** / **yalnızca kaynağa dayananlar (K)**:

| # | İddia | Durum |
|---|---|---|
| a1 | es çevirmeni "Donate"ı "Done" yazdı | V — `review.es.md` blocker #1 (L379); şu an `README.es.md:379` "Donar" |
| a2 | "What's New" başlığı İngilizce kalmalı iddiası yanlış; muafiyet konuma göre | V — `EXEMPT_SECTIONS` README.md'nin başlığıyla eşleşir (`tests/...:84-91, 127, 264`); ru ve zh reviewer'ları başlığın İngilizce kaldığını **major** işaretledi; `fix.py` ilk satırı `("## What's New","## Что нового")` |
| b | Stamp = LF-normalize README.md'nin, muaf bölüm gövdeleri çıkarılmış sha256'sı; naif hash farklı | V — `sha256sum README.md` → `899d4948…`, `readme_sha256()` → `39dcbfa5…` (stamp'teki değer) |
| c | README.md'deki her düzenleme (banner dahil) tüm stamp'leri bozar | V — `git diff README.md` yalnızca banner satırı; tr/ar/ja stamp'i `4dfed787…`→`39dcbfa5…` değişti. Ayrıca upstream `2131b68` (GPU marker commit'i) README.md'ye +1 satır ekledi ve README.tr.md'yi yeniden stamp'lemek zorunda kaldı |
| d | Stamp çeviri yapılmadan yeniden uygulanabilir | V — tr/ar/ja diff'i yalnızca stamp+banner (4 satır), ratchet 31/31 yeşil |
| e | İş akışı: paralel çeviri → ratchet → persona'lı native review (JSON) → fixer → ratchet | V (kısmen) — `reviews.json` (7 kayıt, `verdict/score_out_of_10/findings[severity,line,quote,problem,suggested_fix]`), `fix.py` (exact-string replace + `MISSING` uyarısı). Persona metni scratchpad'de yok → K |
| f | Zaten merge edilmiş tr/ja/ar da 7-8 aldı | V — tr 7, ar 7, ja 8. **Ek bulgu:** tr/ar/ja için review bulguları henüz **uygulanmamış** (`sayı`, `tekerlek`, `عجلات`, `كاسر`, `Kırıcı`, `ゲートの背後` hâlâ dosyada) |
| — | ~500 satır kuralı "release checklist Step 9" | K — #871 maintainer yorumu; checklist dosyası klonda **yok** (muhtemelen maintainer-yerel) |
| — | "Dil arkasında kimse yoksa kaldırılır" | V — #769, #774 maintainer yorumları; test docstring `:50-53` |

---

## 1. Hedef, kapsam, kapsam dışı, lisans duruşu

**Hedef.** Bir kaynak README'den (varsayılan `README.md`) N dilde çeviri üreten, bunları **kaynağa kilitli**
tutan (stamp + yapısal eşdeğerlik), drift'i CI'da **gürültülü** yapan ve çeviri kalitesini bağımsız
native-reviewer LLM'leriyle **tekrar çalıştırılabilir** biçimde denetleyen bir CLI + kütüphane + CI şablonu.

**Kapsam (v1):**
1. `stamp` — muafiyet-farkında, LF-normalize kaynak hash'i; stamp yazma/doğrulama.
2. `lint` — Soup ratchet'inin genelleştirilmiş hali (bölüm sayısı, fence'ler, URL, göreli link, inline code,
   sayılar, anchor çözümü, banner, maintainer) + Soup'un kaçırdığı kontroller (bkz. §5).
3. `translate` — paralel çeviri orkestrasyonu, dil başına stil rehberi + terim tabanı + kural listesi + öz-test.
4. `review` — persona'lı native reviewer, katı JSON şeması, ciddiyet rubriği; **gönderilmiş** dosyalarda da çalışır.
5. `fix` — bulguları tek tek değerlendirip uygulayan/reddeden fixer; her red gerekçeli.
6. `ci` — GitHub Actions şablonu + pre-commit hook.

**Kapsam dışı (v1):** README dışı belge siteleri (docs/ ağacı — v2), MT motoru eğitimi, insan çevirmen
pazaryeri, otomatik PR açma/merge (araç yalnızca diff üretir; push insan kararıdır), RTL için görsel render testi
(v2'de Playwright ile), çeviri bellek sunucusu.

**Lisans duruşu.** Yeni repo Soup'tan **fikir** alır, kod kopyalarsa (ör. `_slug`, `_sections` mantığı)
Apache-2.0 §4 gereği LICENSE + NOTICE ataması gerekir. Soup'un kendi tutucu (holder) ifadesi tutarsız:
`LICENSE` "2025 Makazhan Alpamys", `NOTICE` "2026 Makazhan Alpamys", README "the Soup contributors" — bu
**MakazhanAlpamys/Soup#1677**'de açık soru olarak duruyor. **Karar verilmez**; öneri: yeni repo kodu
sıfırdan yazsın (clean-room), Soup'u README'de "inspired by" olarak ansın, kod kopyalanırsa #1677 netleşene
dek NOTICE'a Soup'un mevcut NOTICE metnini aynen taşısın. Çevirilerin kendisi kaynak README'nin türev
eseridir → araç, hedef repo'nun lisansını çeviri dosyasının altbilgisine **dokunmadan** korumalı
(License bölümü çevrilir ama lisans adı/URL'si invariant kalır).

---

## 2. Önerilen mimari ve repo düzeni

Dil: **Python 3.10+** (Soup ekosistemiyle aynı; markdown-it-py ile token tabanlı ayrıştırma). Soup'un
regex-satır tabanlı yaklaşımı çalışıyor ama setext başlık, girintili fence, `~~~` fence, HTML blok içi
markdown gibi durumlarda kırılgan → **markdown-it-py** AST'si önerilir, ama Soup'un davranışıyla
**geriye dönük uyumluluk testi** (Soup'un 31 testini fixture olarak port et) şart.

```
polyreadme/
  pyproject.toml                 # Apache-2.0 (bkz. §1), entry point: polyreadme
  src/polyreadme/
    cli.py                       # typer: init, stamp, lint, translate, review, fix, status, ci-template
    config.py                    # Pydantic v2: tek doğruluk kaynağı
    parse.py                     # markdown-it-py -> Section[] (title, level, fences, urls, links, code, numbers, anchors, tables, images)
    stamp.py                     # canonical bytes (LF, exempt bodies stripped) -> sha256; read/write stamp
    lint/
      checks.py                  # her kilit ayrı fonksiyon, Problem(code, file, section, msg, hint)
      mutations.py               # öz-mutasyon motoru (ratchet kendini kırabildiğini kanıtlar)
    orchestrate/
      translate.py               # paralel çeviri, chunking (bölüm bazlı), retry, self-test
      review.py                  # persona'lı reviewer, JSON şeması, skor
      fix.py                     # bulgu -> karar (apply/reject+gerekçe) -> exact-anchor patch
      llm.py                     # sağlayıcı adaptörü (Anthropic varsayılan; model id config'te)
    prompts/                     # §3'teki promptlar, Jinja2 şablon; versiyonlu (prompt_version stamp'e girer)
      translator.md  reviewer.md  fixer.md  orchestrator.md  master.md
    styleguides/{es,pt-BR,zh-CN,ru,tr,ja,ar}.md    # §4
    termbase/{es,pt-BR,zh-CN,ru,tr,ja,ar}.yaml     # terim -> çeviri | KEEP | FORBIDDEN listesi
  templates/
    github-workflow.yml          # lint her PR'da; review yalnızca workflow_dispatch / etiketle
    pre-commit-hook.yaml
  tests/
    test_soup_parity.py          # Soup'un 31 testinin portu
    test_mutations.py            # §5
    fixtures/soup/               # Soup README + 7 çeviri (izin/lisans netleşince), yoksa sentetik
```

**Config şeması (`.polyreadme.yaml`, Pydantic v2):**

```yaml
source: README.md
languages:
  - code: tr
    file: README.tr.md
    maintainers: ["@handle"]          # zorunlu; boşsa lint FAIL ("nobody behind it")
    styleguide: builtin:tr
    termbase: termbase/tr.yaml
exempt_sections: ["What's New"]       # kaynağın başlığıyla, KONUMA göre eşlenir
banner:
  anchor: '<img src="soup.png"'       # banner bu işaretten önceki bölgede aranır
  link_pattern: 'href="(README(?:\.[\w-]+)?\.md)"'
numbers:
  policy: source_digits               # source_digits | locale (locale = Soup'tan farklı, bilinçli seçim)
  multiset: true                      # Soup set kullanıyor -> bkz. gap G5
code_comments:
  hash_langs: [bash, sh, shell, yaml, yml, toml, python]
  commented_out_code_is_code: true    # Soup'ta false -> gap G4
review:
  min_score: 8.0
  block_on: [blocker, major]
  reviewers_per_language: 1           # 2 = çapraz doğrulama
max_source_lines: 500                 # Soup "release checklist Step 9" (~500), uyarı seviyesi
```

**Stamp formatı (Soup ile uyumlu + genişletilmiş):**
`<!-- synced-from: README.md sha256:<64hex> -->` — Soup ile birebir okunabilir kalmalı.
Opsiyonel ikinci satır: `<!-- polyreadme: reviewed sha256:<hex> score:8 prompt:v3 date:2026-10-06 -->`
→ "stamp çeviri olmadan yeniden uygulanabilir" (lesson d) açığını kısmen kapatır: **review stamp'i** ayrı
hash'tir ve yalnızca `review` + `fix` döngüsü geçince yazılır; CI, sync stamp'i yeni ama review stamp'i
eski olan dosyayı "unreviewed drift" olarak **uyarır** (fail değil; maliyet nedeniyle).

**Hash kanonikleştirme (Soup'tan birebir, `tests/test_readme_translation_sync.py:110-135`):**
1. bytes → `\r\n`→`\n`; 2. satır satır, ```` ``` ```` ile fence durumu tut; 3. fence dışındaki `## ` satırı
başlık; başlık muafsa gövdesini at, **başlık satırını tut**; 4. sha256. Not: fence içindeki `## What's New`
başlık sayılmaz (#1064 düzeltmesi, `:581-593`).

---

## 3. Promptlar (kopyala-yapıştır)

### 3.0 Master prompt (gelecek oturum için, yeni repo'yu kurdurur)

```text
You are building a new standalone open-source repository, "polyreadme": a CLI + Python library that
creates, translates, syncs and quality-audits multilingual READMEs. It generalises the translation
ratchet of the Soup project (MakazhanAlpamys/Soup, tests/test_readme_translation_sync.py).

Non-negotiable design rules:
1. A translation is locked to its source by a stamp line
   <!-- synced-from: README.md sha256:<hex> --> where <hex> = sha256 of the source with CRLF->LF and the
   bodies of exempt sections removed (exempt headings kept; '## ' lines inside code fences are not headings).
   Keep this format byte-compatible with Soup.
2. A missing stamp FAILS. Translations are discovered by glob, never a hand-written list.
3. A stamp proves WHEN, never WHAT. Structural equivalence is checked per '## ' section by position, in both
   directions (nothing dropped, nothing invented): fenced code (languages, order, content minus comments),
   external URLs, relative link targets, inline code spans, numbers in prose (source digits, multiset),
   section count (always, even for exempt sections), in-page anchors must resolve to a heading in the same
   file, banner links exactly the READMEs that exist, every language names a maintainer.
4. Every lint check ships with a mutation test that proves it can go red, plus a control proving the
   clean case stays green. "Green" alone is not evidence.
5. LLM stages (translate, review, fix) are orchestrated, schema-validated (JSON), re-runnable on already
   shipped files, and never push: they produce diffs for a human.
6. Heavy deps are lazy-imported; output via rich; Pydantic v2 config is the single source of truth;
   path containment uses os.path.realpath + os.path.commonpath.
Licensing: Apache-2.0 is the intended licence, but holder/NOTICE wording questions are open upstream in
MakazhanAlpamys/Soup#1677 — do not copy Soup code verbatim; write clean-room and credit Soup as inspiration.

Deliver phase 1 first (stamp + lint + mutation tests + CI template), with the Soup parity test suite
green. Do not start LLM stages until `polyreadme lint` reproduces Soup's 31 test outcomes on fixtures.
Report what you verified by running it versus what you assumed.
```

### 3.1 Translator prompt

```text
ROLE: You are a professional technical translator into {LANG_NAME} ({LOCALE}), native speaker, who
writes developer documentation for {AUDIENCE}. Follow the style guide and term base below exactly.

INPUT: the full source README (Markdown + HTML). Translate it into {LANG_NAME}. Output ONLY the file
content, starting with this exact first line:
{STAMP_LINE}

HARD RULES (a violation fails CI; there is no judgement call here):
R1  Keep every '## ' heading, in the same order and count. TRANSLATE every heading, including
    "What's New" — exemptions are by POSITION, never by keeping English text.
R2  Code fences: identical language tag, identical content. You may translate only '#' comments in
    bash/sh/shell/yaml/yml/toml/python. A commented-out config line (e.g. "# backend: unsloth") is CODE:
    do not translate it.
R3  URLs, relative link targets (docs/x.md#anchor), image src, HTML attributes other than alt/title:
    byte-identical. Link TEXT is translated.
R4  Inline code spans `like_this`: byte-identical, never translated, never added, never removed.
R5  Numbers: keep the source digits and separators exactly (119.6 stays 119.6, never 119,6 or ١١٩٫٦;
    3.32 GB stays 3.32 GB). Do not add numbers (no "22 en total" when the source had words), do not drop
    any. Numbers written as words in the source stay words.
R6  In-page anchors (#quick-start) must be rewritten to the slug of YOUR translated heading (GitHub
    slug: lowercase, keep letters/marks/digits/-/_/space, space->'-'). Check every one resolves.
R7  The language banner (above the logo) links every other README and bolds this one.
R8  Do not drop or merge sentences, bullets, table rows, footnotes or parentheticals, even if they
    seem redundant. Do not add explanations.
R9  Brand/product names, CLI commands, config keys, model names, file names: never translated.
R10 Calls to action are verbs in {LANG_NAME}: "Donate" -> the {LANG_NAME} verb for donate
    (NOT "Done"). Check every button/link label against its meaning, not its spelling.
R11 Use the term base: KEEP terms stay in English; FORBIDDEN renderings must never appear.

KNOWN TRAPS (seen in 7/7 languages of a previous project — avoid):
- "honest gates"/"ship behind gates" -> express the meaning (explicitly labelled "requires <hardware>"
  instead of unverified claims), never a literal gate/door/barrier.
- "existed nowhere" (of a computed value) -> "was never recorded/surfaced anywhere"; it DID exist.
- "running an issue" -> "running the experiment/benchmark the issue describes".
- "wheels" (pip) -> wheel packages, never physical wheels.
- "Breaking change" -> the established "incompatible change" term of your locale (see style guide).
- "model" meaning a Pydantic schema model -> disambiguate ("schema model"), never the bare LLM word.
- "autopilot" -> never the self-driving-car word; keep consistent with the `soup autopilot`-style command.
- "issue" (GitHub) -> per term base; never a word meaning "number/count" (tr "sayı").
- "serving" a model, "tracker", "trainer", "adapter", "upstream", "parity", "loop-hardening",
  "opt-in", "toys", "zoo", "resolves to" (DOI), "silent" (bug), "correctness repair" -> see term base.
- "N pull requests ... by M people" -> keep who-is-counted unambiguous.

SELF-TEST before answering (do it silently, then fix):
[ ] heading count equals source; every heading translated
[ ] each fence identical except '#' comments
[ ] multiset of numbers per section equals source
[ ] every inline code span and URL present exactly once more/less as in source
[ ] every #anchor resolves to one of my headings
[ ] every button/link label reviewed for false friends (Donate/Done, Contact, Support)
[ ] register consistent ({REGISTER}) from first to last line
If any box fails, fix the translation; never "explain" a failure.

STYLE GUIDE:
{STYLEGUIDE}
TERM BASE:
{TERMBASE_YAML}
SOURCE:
{SOURCE}
```

### 3.2 Native-reviewer prompt

```text
ROLE: You are {PERSONA}. You read technical documentation in {LANG_NAME} daily and you did NOT write this
translation. Your job is to find what a native developer would trip over, not to rewrite for taste.

PERSONA (fill per language, e.g. for pt-BR): "a senior backend engineer in São Paulo who maintains
Portuguese docs for an open-source ML library; reads PRs in English, writes docs in Brazilian Portuguese;
allergic to calques and false friends."

You receive: SOURCE (English), TRANSLATION ({LANG_NAME}) with line numbers, STYLE GUIDE, TERM BASE, and
LOCKED RULES. LOCKED RULES are enforced by CI and are NOT yours to change. Never suggest:
- localised decimal separators or digits (119.6 stays 119.6), even if your locale uses commas;
- translating code, inline code, URLs, link targets, command names, config keys;
- adding, removing or merging sections/bullets; changing numbers.
If you believe a locked rule hurts readers, put it in "policy_notes", not in findings.

Check, in priority: (1) meaning errors and omissions vs SOURCE, (2) false friends and calques,
(3) terminology consistency within the file and with TERM BASE, (4) grammar/agreement, (5) register and
punctuation per STYLE GUIDE, (6) headings and calls to action (every button label!), (7) untranslated prose.

SEVERITY RUBRIC:
- blocker: a reader is actively misled or an action fails (wrong CTA like "Done" for "Donate",
  inverted meaning, wrong number semantics, dropped warning).
- major: meaning changed or unclear to a native developer (false friend, calque that reads as
  nonsense, wrong technical term, untranslated heading, ambiguous antecedent of a fact).
- minor: correct but unnatural, inconsistent terminology, register slips.
- nit: polish.

OUTPUT: JSON only, matching this schema; "quote" MUST be copied verbatim from TRANSLATION (one line
if possible, never paraphrased), "suggested_fix" must be a drop-in replacement for "quote" that
keeps every locked token.
{
  "language": "{LOCALE}",
  "file_sha256": "<given>",
  "verdict": "<2-3 sentences>",
  "score_out_of_10": <number, 0.5 steps>,
  "findings": [
    {"id": "F1", "severity": "blocker|major|minor|nit", "category":
     "meaning|omission|false_friend|calque|terminology|grammar|register|punctuation|heading|cta|untranslated",
     "line": <int>, "quote": "<verbatim>", "problem": "<English>", "suggested_fix": "<verbatim replacement>",
     "recurs_at": [<int>], "touches_locked_token": false}
  ],
  "policy_notes": ["<disagreements with locked rules, if any>"]
}
Score anchor: 9-10 publishable as-is; 8 publishable after minors; 7 needs a fix pass; <=6 retranslate.
```

### 3.3 Fixer prompt

```text
ROLE: You are the original translator for {LANG_NAME}, applying an independent review. You are not
obliged to accept findings: judge each one.

For EACH finding output one decision:
{"id": "F3", "decision": "apply|apply_modified|reject",
 "reason": "<one sentence>",
 "anchor": "<verbatim, UNIQUE substring of the current file to replace>",
 "replacement": "<new text>"}

Reject (with reason) when the fix: breaks a LOCKED RULE (decimal commas, translated code/URLs/numbers,
added/removed numbers or sections); contradicts the term base; introduces a new false friend; or the
quote no longer exists. Prefer apply_modified when the problem is right but the fix is not.
For "recurs_at", produce one decision per occurrence (anchors must be unique; never global replace).
After all decisions, list terms you changed so the term base can be updated.
Output JSON array only.
```

Uygulama motoru notu (bu oturumdaki `fix.py`'den ders): exact-string replace + "MISSING" uyarısı iyi
desen; ama `str.replace` **tümünü** değiştiriyor ve sıralı kurallar çakışabiliyor
(`"модель целиком в памяти"` hem kendi başına hem daha uzun kalıpların içinde). Motor: her anchor dosyada
**tam 1 kez** geçmeli, yoksa karar `needs_human`; ardından ratchet yeniden koşar. Reviewer alıntıları
her zaman birebir değil (ja `正直なゲート` alıntısı dosyada bu haliyle yok, `正直な「…」というゲートの背後` var) →
anchor bulunamazsa fuzzy eşleme önerisi + insan onayı.

### 3.4 Orchestrator prompt

```text
ROLE: You orchestrate README localisation for {REPO}. You never push, open PRs or comment; you produce
local diffs and a report.

Pipeline (stop on any red):
1. `polyreadme lint` on the current tree; record baseline problems.
2. For each target language IN PARALLEL: run the translator prompt (fresh context, no access to other
   languages' outputs) -> write file -> run its self-test via `polyreadme lint --lang X`.
   On lint failure: feed the exact problem lines back to the same translator, max 2 retries; then mark
   the language "blocked" with the problems.
3. `polyreadme lint` must be fully green before any review.
4. For each language IN PARALLEL: independent reviewer (different model instance/persona from the
   translator; ideally a different model family) -> validate JSON schema -> reject findings with
   touches_locked_token=true into policy_notes.
5. Fixer per language -> apply decisions with unique anchors -> `polyreadme lint` again.
6. Optional second review round if score < min_score or any blocker/major was rejected.
7. Write report: per language score before/after, findings applied/rejected with reasons,
   policy_notes, remaining risks, maintainers. Ask a human before anything leaves the machine.
Also run steps 4-6 on languages that are already shipped and unchanged: shipped is not reviewed.
```

---

## 4. Dil başına stil rehberi tohumları

Ortak kural (Soup ratchet'iyle uyumlu): **ondalık ayırıcı ve rakam sistemi kaynaktaki gibi** (Batı rakamı,
nokta). Bu, pt/tr/ru reviewer'larının önerisiyle **çelişir** (pt major L64: "119,6"; tr minor L62; ru nit L83)
— bilinçli seçimdir (#852 review: karma yerelde `48.241 MiB` ≈ 48 okunur). Rehberde gerekçesiyle yazılı olmalı
ki reviewer tekrar önermesin. Birim ile sayı arasında boşluk kaynaktaki gibi (`3.32 GB`); yüzde işareti
kaynaktaki konumda (`4.8%`) — tr'de `%4.8` yazımı sayı kilidini geçer ama tutarlılık için rehberde karar ver
(öneri: tr `%4,8` değil `%4.8`, yani Türkçe önek konumu + kaynak rakamı; ratchet'i geçiyor, Soup tr böyle).

| Dil | Hitap/register | Noktalama & boşluk | Terim politikası (öneri) | Bilinen tuzaklar (review'dan) |
|---|---|---|---|---|
| **es** | Nötr uluslararası/LatAm, `usted` tutarlı | `«…»` veya `"…"` tek seçim; aralık "entre el 30 y el 50 %" ama kaynak rakamı korunur | KEEP: pull request, issue, wheel, endpoint; "laptop/computadora portátil" (Peninsular "portátil" isim değil) | "Done"↔Donate (blocker); "compuertas honestas"; "se escapan"(escaped); "ejecutar un issue"; "distinta a"→"distinta de"; "reportar/informar" tutarlılığı |
| **pt-BR** | `você`, Brezilya | Başlıkta cümle düzeni (Title Case değil) — pt'de karışıktı | KEEP: pull request, issue, wheel, endpoint, upstream; "compatível" > "suportado"; "solicitações de funcionalidades" > "pedidos de recursos" | "retratado" false friend; "destilação" yazımı; "travar"(hang) vs crash; "Interface Web" vs "Web UI" tutarsızlığı; "© os"; "modelos de brinquedo" |
| **zh-CN** | Nötr resmi, 您 kullanma (dokümanda kişisiz) | Tam genişlikte `，。：？（）`; CJK–Latin/rakam arası **tek boşluk** (zh'de 193 örnek, 0 ihlal — iyi); iç içe tam genişlik parantezden kaçın | KEEP: Soup, CLI adları; "机器遗忘"(unlearning), "默认关闭，需手动启用"(opt-in) | "自动驾驶"(autopilot = sürücüsüz araç); "对标"(parity yanlış); başlık "What's New" İngilizce kaldı (major); "当面聊"; Tracker/ticket karışık dil |
| **ru** | `вы` küçük harf, nötr-teknik | `«…»`; aralıkta en-dash `30–50%`; em-dash boşluklu | "несовместимое изменение"(breaking); "wheel-пакеты"; "валидационный лосс"; issue için tek seçim (задача **ya da** issue, karışık değil) | "Ломающее изменение"; "Пробы"(probes); "градиентные чекпойнты"; "вышестоящая библиотека"; başlık "What's New" İngilizce kaldı (major); "в памяти" vs VRAM belirsizliği |
| **tr** | "siz", resmi-teknik | Kesme işaretiyle ek: `GB'a`, `Soup'u`; `%` öne | "issue" → **"issue"/"konu"** (asla "sayı"); "wheel paketleri"; "sunum"→"servis etme/sunma (serving)"; "eğitici"→"trainer"; "geriye dönük uyumsuz değişiklik"; "nicemleme" vs "niceleme" kararı | "sayı"(issue, L68/77/78/446 — major, hâlâ dosyada); "tekerlekler"; "kapılandı" (uydurma fiil); "izleyici"(tracker); "işlem" vs "süreç"; "sonradan eğitim" |
| **ja** | です・ます体 tutarlı (madde sonunda düz biçim karışmasın) | Tam genişlikte `？：`; Japonca–Latin arası boşluk tutarlı (gövde `Soup は`, başlık `Soupを` — tutarsız); rakam: kaynak Arap rakamı (八枚 değil 8 枚 — kaynak rakamsa) | "レイヤー" ya da "層" — tek seçim; "オートパイロット"; "堅牢化"(hardening, 強化 değil → RL çağrışımı); "セキュリティ対策"(supply-chain controls) | "issue を実行"; "正直なゲート"; "管理" false friend; "モデル"(Pydantic); "駆動"; "解決される"(DOI) |
| **ar** | MSA, resmi; emir kipi tutarlı | `،` ve `؟`; **Batı rakamı** (Soup ar: 0 Arap-Hint rakamı — doğru); banner/merkez blokları `dir="rtl"` (Soup ar:10,14,75); karışık LTR çalıştırmalarda gerekirse U+2068/2069 izolasyonu (Soup'ta 0 — v2'de render testiyle doğrulanmalı) | "حزم wheel"; "تغيير غير متوافق"(breaking); "المحوّلات" yalnızca transformers için, adapter = "المهايئات/المحولات المساعدة" kararı; "نقطة نهاية"(endpoint) | "عجلات"; "كاسر"; "مُبوَّب"(gated); "إصلاح الصحة"(correctness); "نسخةً"(copy op); sayı-cins uyumu ("ست خيارات"→"ستة خيارات" — L93 civarı, hâlâ dosyada) |

Her dil için `termbase/<lang>.yaml` biçimi:
```yaml
- en: wheel
  policy: render         # keep | render | forbidden
  target: "wheel paketi"
  forbidden: ["tekerlek"]
  note: "pip binary package"
```

---

## 5. Kabul kriterleri, test planı, mutasyon testleri

### 5.1 Soup ratchet'inin yaptığı (V, `tests/test_readme_translation_sync.py`)
- 5 kilit testi (`:324-361`): stamp var, stamp güncel, yapı, banner, maintainer.
- 18 mutasyon/kontrol testi (`:425-536`) + 8 muafiyet testi (`:539-608`); toplam 31, yerelde **31 passed**
  (`pytest -o addopts=""` gerekti; repo `pyproject` `--cov` addopts'u pytest-cov olmadan kırılıyor).
- Muafiyet listesinin genişletilmesinin tespit edilen drift'i **susturduğunu** gösteren mutasyon testi
  (`:595-608`) — kopyalanması gereken en değerli fikir.

### 5.2 Soup ratchet'inin yakalayamadıkları (V — scratchpad mutasyonlarıyla ölçüldü)

| Kod | Mutasyon (README.es.md kopyası) | Sonuç |
|---|---|---|
| G1 | Sayı/kod/URL içermeyen bir madde silindi ("Cero SSH…") | **PASSES** |
| G2 | Olumsuzluk kaldırıldı (anlam tersine) | **PASSES** |
| G3 | Tamamen aynı içerikle stamp yeniden yazıldı | **PASSES** (tasarım gereği; lesson d) |
| G4 | Yorum satırına alınmış YAML ayarı değiştirildi (`# backend: unsloth`→`vllm`) | **PASSES** — `_code_body` `#` sonrasını atıyor (`:172-180`) |
| G5 | Aynı bölümde bir sayı başka bir sayıyla değiştirildi (`119.6`→`3.32`) | **PASSES** — sayılar `set` (`:222`), tekrarlar çöküyor |
| G6 | `###` başlık silindi | yakalandı ama **tesadüfen** (başlıkta sayı vardı); `###` yapısı karşılaştırılmıyor |
| G7 | Banner yalnızca logo işaretinden önce aranıyor (`:304`); logo yoksa tüm dosya | (okuma) |
| G8 | `_slug` GitHub'ın yinelenen başlık `-1` ekini ve emoji kurallarını modellemiyor | (okuma) |
| G9 | Bölüm başlıklarının çevrilip çevrilmediği/ yanlış çevrildiği kontrol edilmiyor (ru/zh "What's New") | (review ile bulundu) |
| G10 | Tablo satır/sütun sayısı, liste madde sayısı, `alt` metni, bold vurgu sayısı yok | (okuma) |

### 5.3 polyreadme kabul kriterleri
1. **Soup paritesi:** Soup'un 31 testi, port edilmiş fixture'larda aynı sonuçla geçer.
2. **G4, G5, G6, G10 kapatılmış:** sayılar multiset; yorumlanmış kod satırı (`#\s*[\w.-]+\s*:` YAML,
   `#\s*\$?\s*\w+ ` bash) kod sayılır; `###`/`####` sayısı ve sırası bölüm içinde eşit; tablo satır ve
   liste madde sayısı eşit (±0); `<img alt>` var/yok eşitliği.
3. **G1/G2 için yapısal vekil:** bölüm başına cümle-sayısı oranı (çeviri/kaynak) dil başına kalibre bant
   dışına çıkarsa **uyarı** (ör. ja 0.6–1.6). Fail değil (yanlış pozitif riski).
4. **G9:** "untranslated heading" uyarısı — çeviri başlığı kaynağınkiyle aynıysa ve termbase'de `keep`
   değilse (ör. `Docker`, `Web UI` keep).
5. Her kilit için: (a) temiz kontrol yeşil, (b) tek-mutasyon kırmızı, (c) mutasyon mesajı düzeltme
   ipucu içerir (Soup'un `keep README.md's digits` ipucu gibi, `:291-292`).
6. **Self-mutation komutu:** `polyreadme lint --prove` gerçek repo üzerinde her kilidi geçici kopyada
   kırar ve kırmızıya döndüğünü raporlar (Soup: "The ratchet must be shown able to fail").
7. Review JSON şema doğrulaması %100; `quote` alıntılarının ≥%95'i dosyada birebir bulunur (bulunamayanlar
   rapora `unanchored` olarak düşer).
8. Hash: Windows CRLF checkout'unda aynı stamp (CI matrisi 3 OS).

### 5.4 Mutasyon test listesi (minimum)
Soup'un tümü + şunlar: yorumlanmış config değişikliği; tekrarlanan sayının değişimi; `###` silme;
tablo satırı silme; liste maddesi silme; `alt` silme; `~~~` fence; girintili fence; fence içinde `## `;
setext başlık; BOM'lu dosya; `EXEMPT` listesini genişletmenin drift'i susturduğu (Soup `:595`);
muaf bölümün tamamen silinmesi sayımda yakalanır (Soup `:573`); yeni dil dosyası maintainer'sız
(Soup `:456`); banner'da var olmayan dosya; stamp silme; sahte ama iyi biçimli stamp.

---

## 6. Risk kaydı

| Risk | Olasılık / etki | Kanıt | Azaltma |
|---|---|---|---|
| **Halüsinasyonlu eksiltme** (fact içermeyen cümle/madde atlanır) | Yüksek / Orta | G1 PASSES | Cümle oranı uyarısı; reviewer'da "omission" kategorisi; translator R8 |
| **Anlam terslenmesi** | Orta / Yüksek | G2 PASSES; es "sin probar que fallan", ru CPU cümlesi (major) | Reviewer blocker; ikinci reviewer (farklı model) yüksek-riskli bölümlerde |
| **Sessiz drift** (re-stamp, çeviri yok) | Yüksek / Yüksek | Lesson d; G3 | Review stamp'i ayrı; `status` komutu "sync-stamp yeni, review-stamp eski" listesi |
| **Her README.md değişikliği CI'ı kırar** | Kesin / Orta | Lesson c; #852: "60 commit'in 54'ü main'e direkt push"; #1013: 62'nin 28'i yalnızca What's New | Konum-bazlı muafiyet; `polyreadme stamp --restamp-if-structurally-equal` yalnızca muaf olmayan bölümler **değişmemişse** (banner gibi) — ve bunu açık log'la |
| **Reviewer kural-çakışan öneri** (ondalık virgül) | Kesin / Düşük | pt major, tr minor, ru nit | Reviewer promptunda LOCKED RULES + `policy_notes`; fixer reddi gerekçeli |
| **Çevirmen kural yanılgısı** ("What's New" İngilizce kalmalı, "Done") | Orta / Yüksek | Lesson a | Açık kural listesi R1/R10 + öz-test + CI başlık uyarısı |
| **Gönderilmiş dosyalar hiç yeniden incelenmez** | Yüksek / Orta | tr/ja/ar 7-8, bulgular hâlâ uygulanmamış | `review` gönderilmiş dosyada da çalışır; periyodik (aylık) workflow_dispatch |
| **Bakımcısız dil** | Orta / Yüksek | Maintainer politikası (#769/#774): "a language with nobody behind it gets removed"; Soup'ta 7 dilin tümü tek kişi (@Ercaner1988) | Config'te maintainers zorunlu; `status` bus-factor=1 dilleri işaretler; README'de politika |
| **Lisans/atıf** | Düşük / Orta | #1677 açık | Clean-room; NOTICE; çeviri dosyasında lisans bölümü invariant |
| **Maliyet** | Orta / Orta | 7 dil × (çeviri ~480 satır + review + fix) | Bölüm-bazlı yeniden çeviri (yalnızca hash'i değişen bölümler); review yalnızca etiketle/elle; prompt caching |
| **Reviewer quote paraphrase'ı** | Orta / Düşük | ja `正直なゲート` | Fixer anchor zorunluluğu + fuzzy öneri + insan |
| **README uzunluk tavanı** | Düşük / Düşük | ~500 satır kuralı (#871, K) | `max_source_lines` uyarısı; muaf bölüm büyüdükçe docs'a taşı |
| **Tek model ailesinin kör noktası** | Orta / Orta | 7 reviewer aynı sınıf hataları buldu ama ilk çeviri de aynı sınıftan | Reviewer'ı farklı model/persona ile; mümkünse insan native spot-check |

---

## 7. Yineleyen hata sınıfları (7 review, 209 bulgu: 1 blocker, 67 major) — termbase tohumu

Sayımlar `reviews.json`'dan (V): es 8 (1 blocker/5 major/19 minor/5 nit), pt 7.5 (10/16/5), zh 8 (3/16/5),
ar 7 (15/13/3), ru 7 (13/17/3), tr 7 (13/15/2), ja 8 (8/18/4).

| Sınıf | Görüldüğü diller | Örnek |
|---|---|---|
| "honest gates" calque | es, pt, ru, ja, zh, ar | compuertas honestas / 正直なゲート / честные барьеры |
| "existed nowhere" çelişkisi | es, pt, ru, tr, ja, zh | "yoktu" (tr) — sonraki cümle hesaplandığını söylüyor |
| "running an issue" | es, pt, ja (+tr "konuları çalıştırıp") | issue を実行 |
| wheels → fiziksel tekerlek | tr, ar, ru("сборки") | tekerlekler / عجلات |
| Breaking change calque/tutarsız | ru, tr, ar | Ломающее / Kırıcı vs Geriye dönük / كاسر |
| "model" = Pydantic modeli | ar, ja, ru, pt, zh | — |
| loop-hardening | es, pt, ru, ja, tr, ar | Endurecimiento / 強化 |
| autopilot | ja, zh | 自动驾驶 |
| silent/toys/zoo/upstream/resolves to | çoğu | — |
| Başlık çevrilmemiş | ru, zh | "## What's New" |
| CTA false friend | es | Done ↔ Donate (tek blocker) |
| Terim tutarsızlığı (aynı EN terim 2-3 çeviri) | tümü | layer レイヤー/層; metrics ölçüm/ölçüt |
| Ondalık virgül önerisi (**ratchet ile çatışır**) | pt, tr, ru | 119,6 |

---

## 8. Fazlı yol haritası

**Faz 0 (gün 1):** repo iskeleti, lisans kararı ertelenmiş notla (#1677), `.polyreadme.yaml` şeması.
**Faz 1 (hafta 1): deterministik çekirdek** — stamp, lint, mutasyon, CI şablonu; Soup paritesi.
**Faz 2 (hafta 2-3): LLM boru hattı** — translator/reviewer/fixer promptları, JSON şema, orkestratör,
termbase + 7 stil rehberi; Soup'un tr/ja/ar dosyalarında **yalnızca review** koşarak 7-8 skorunu yeniden üret
(kalibrasyon).
**Faz 3 (hafta 4): artımlı çeviri** — yalnızca hash'i değişen bölümleri çevir; review stamp'i; `status`.
**Faz 4: genişleme** — docs/ ağacı, RTL render testi (Playwright), çapraz-model review, insan reviewer kuyruğu.

**İlk hafta görev listesi (sıralı, her biri PR-büyüklüğünde):**
1. `pyproject.toml`, `src/polyreadme/config.py` (Pydantic v2), `cli.py` iskeleti (`typer`, `rich`).
2. `parse.py`: markdown-it-py ile Section çıkarımı; Soup `_sections` ile aynı çıktıyı veren uyumluluk modu.
3. `stamp.py`: kanonik bayt + sha256; Soup'un `readme_sha256` ile Soup README'si üzerinde **aynı hex**
   (`39dcbfa5…` mevcut çalışma ağacı için) — kabul testi.
4. `lint/checks.py`: Soup'un 5 kilidi + G4/G5/G6/G10 kapatmaları; `Problem` nesneleri + ipuçları.
5. `tests/test_soup_parity.py`: Soup'un 31 testinin clean-room portu (sentetik `_EN`/`_TR` fixture'ları).
6. `tests/test_mutations.py` + `polyreadme lint --prove`.
7. `templates/github-workflow.yml` (3 OS × 3 Python, CRLF checkout hücresi dahil) ve pre-commit hook.
8. `prompts/*.md` ilk sürümleri (§3 metinleri) + `styleguides/*.md` tohumları (§4) + `termbase/*.yaml`
   (§7 tablosundan).
9. README (İngilizce) — kendi ratchet'inin altında; ilk çeviri (tr) Faz 2'de dogfooding olarak.

---

## 9. Soup'tan aktarılan somut kurallar (kaynak satırlarıyla)

- Glob ile keşif, eksik stamp = fail (`:50-53`, `:105-107`, `:147-148`).
- LF normalizasyonu (`:134`), test `:449-454`.
- Muafiyet: içerik muaf, **varlık** değil — bölüm sayısı her zaman (`:84-91`, `:258-262`, `:573-579`).
- Fence içinde yalnızca `#` yorumları serbest (`:24-26`, `:101`, `:172-180`).
- Sayılar kaynak rakamıyla, ipucu mesajıyla (`:29-32`, `:246-247`, `:291-292`).
- Anchor'lar karşılaştırılmaz, **çözülür** (`:34`, `:226-243`).
- Banner logo işaretinden önce, tam küme eşitliği (`:46-48`, `:300-311`).
- Maintainer zorunlu; kırmızı main kime ping atılacağını söyler (`:163-169`, `:356-361`).
- "Ratchet must be shown able to fail" + CONTROL testleri (`:364-366`, `:415`, `:473-476`, `:533-536`).
- Geçmiş (GitHub API, V): `ac4bd1e` tr + ratchet (#852, 09-11) → `4638685` #852 re-stamp açığı kapatıldı:
  fence içerikleri, linkler, anchor'lar, sayılar (#870, 09-13) → `670bff1` What's New muafiyeti (#1020, 09-17)
  → `e66f380` fence-farkında muafiyet (#1064, 09-18) → `ca6ea3f` ar + ja (09-21). Yerel, commit'lenmemiş:
  es/pt/zh/ru + banner + MAINTAINERS genişlemesi.
