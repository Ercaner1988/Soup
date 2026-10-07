# Independent native review of README.ar.md (score 7/10)

The translation is faithful and complete: numbers, caveats, the retraction wording and the structure all survive, and it reads fluently in most places. Several terminology and idiom errors still need fixing before publication. The worst are "الصحة" for "correctness", "المُبوَّب" for "gated", "يُطلق خطأً" for "raises", "نموذج" for a Pydantic model, and "لا تجامل قدرنا".

1. [major] line 264
   quote: التدريب المُبوَّب بالتقييم
   problem: "eval-gated training" is rendered with "مُبوَّب", which means classified or organized into sections, not gated by a pass/fail check. The meaning is lost.
   fix: التدريب المشروط ببوابة التقييم

2. [major] line 120
   quote: يُطلق خطأً على TRL 0.29
   problem: "raised" (an exception) became "يُطلق خطأً". The accusative "خطأً" reads as the adverb "mistakenly", which changes the meaning.
   fix: كان packing: true يُطلق استثناءً (خطأً برمجيًا) على TRL 0.29

3. [major] line 246
   quote: المفتاح الذي لا يعلنه أي نموذج
   problem: "model" here means a Pydantic schema model. In an LLM README "نموذج" reads as the language model, so the sentence is confusing.
   fix: المفتاح الذي لا يعرّفه أي نموذج في المخطط (Pydantic)

4. [major] line 66
   quote: قبل إصلاح الصحة في v0.73.0 الذي كلّف
خسارةً قدرها 4.8% عند 32B
   problem: "correctness repair" became "إصلاح الصحة", but "الصحة" means health. The same flaw appears at line 417 in "بروتوكول الصحة". "cost −4.8%" became "خسارةً", which reads as loss (the ML loss metric) rather than a throughput cost.
   fix: قبل إصلاح صحة النتائج في v0.73.0 الذي كلّف انخفاضًا قدره 4.8% في الأداء عند 32B (وفي السطر 417: بروتوكول التحقق من صحة النتائج)

5. [major] line 442
   quote: النتيجة التي لا تجامل قدرنا
   problem: "the result that does not flatter us" is mistranslated. "قدرنا" means our fate (or our worth), so the clause is odd and unidiomatic.
   fix: بما في ذلك النتيجة التي لا تصبّ في صالحنا: ثماني بطاقات بـ ZeRO-3 أبطأ من بطاقة واحدة تُجري التدريب مقيمًا في الذاكرة

6. [major] line 429
   quote: وينتظر تدفق الحساب نسخةً لمدة **0.20%** من الخطوة
   problem: "waits on a copy" means a copy operation. "نسخةً" means a duplicate or version of a document.
   fix: ويظل مسار الحساب (compute stream) ينتظر انتهاء عملية نسخ خلال 0.20% من زمن الخطوة

7. [major] line 93
   quote: كانت تُتحقَّق منها وتُوثَّق وتُقبَل
   problem: "تُتحقَّق" is ungrammatical. The verb takes "من" and so needs the impersonal masculine "يُتحقَّق", or a different verb. The same pattern recurs at lines 105-106 ("تُتحقَّق كلٌّ منها ثم تُهمَل"). Line 93 also reads stiffly.
   fix: ست خيارات تدريب كان يُتحقَّق من صحتها وتُوثَّق وتُقبَل، ثم لا يقرؤها شيء في تلك الواجهة الخلفية

8. [major] line 100
   quote: ويطبّق الكاشف إعادة التعيين للمفتاح
   problem: "remap" is rendered as "إعادة التعيين", which means reset. The sentence is also very stiff.
   fix: ويراعي الكاشف تحويل المفتاح lora: الواقع في المستوى الجذري إلى training.lora، وهو تحويل يعمل به المخطط منذ v0.40.1، ولذلك تُقبل هذه الصيغة ولا تُرفض

9. [major] line 375
   quote: إن وفّر لك Soup تشغيلة تدريب
   problem: "saved you a training run" needs "وفّر عليك"; "وفّر لك" means "provided you with". "تشغيلة" is also colloquial.
   fix: إن وفّر عليك Soup جولة تدريب

10. [major] line 266
   quote: [المحوّلات والسجل والحوكمة](docs/adapters-and-governance.md)
   problem: "adapters" is rendered "المحوّلات", which is the standard Arabic term for Transformers, in an LLM document where "transformers" also appears. Risk of confusion. The rest of the table keeps the English term in parentheses only once.
   fix: [المهايئات (Adapters) والسجل والحوكمة](docs/adapters-and-governance.md)، وتوحيد المصطلح في بقية الملف

11. [major] line 115
   quote: نقاط قراءة واجهة الويب وSSE تتطلب مصادقة
   problem: "read endpoints" lost "endpoint" (نقطة نهاية), which is the term used at line 265. "نقاط قراءة" is unclear.
   fix: نقاط نهاية القراءة في واجهة الويب وSSE تتطلب مصادقة

12. [major] line 97
   quote: تغيير كاسر: مفتاح إعداد غير معروف يرفض التحميل الآن.
   problem: "Breaking" is calqued as "كاسر", which is not a natural technical expression. It recurs at line 112.
   fix: تغيير غير متوافق مع الإصدارات السابقة: يؤدي أي مفتاح إعداد غير معروف إلى رفض التحميل الآن.

13. [major] line 436
   quote: بقي الاتجاه الأمامي
مطابقًا
   problem: "forward/backward" is rendered as "الاتجاه" (direction), but the standard terms are "التمرير الأمامي والخلفي" (forward pass and backward pass). The same wording is at lines 418 and 440.
   fix: بقي التمرير الأمامي مطابقًا بتًّا ببتّ (وكذلك في الأسطر 418 و440: التمرير الأمامي والخلفي)

14. [major] line 122
   quote: كان pip يحلّ إلى عجلات PyTorch لم تُختبر وتنهار
   problem: "wheels" is translated literally as "عجلات", and "resolve to" as "يحلّ إلى". Developers read "عجلات" as physical wheels. The same wording recurs at line 349.
   fix: كان pip يختار حزم PyTorch (wheels) غير مختبرة تنهار في الامتداد الأصلي قبل أن يبدأ Soup عمله أصلًا

15. [major] line 279
   quote: والتجزئة، والتداخل،
   problem: "sharding" and "interleaving" are rendered as "التجزئة" (hashing or fragmentation) and "التداخل" (overlap), which is ambiguous or wrong in a data pipeline.
   fix: والتقسيم إلى شظايا (sharding)، والدمج المتناوب (interleaving)

16. [minor] line 386
   quote: بوابات صريحة من نوع
«يتطلب \<العتاد\>»
   problem: "honest gates" became "صريحة" (explicit), so the "honesty" nuance is lost.
   fix: خلف بوابات صادقة من نوع «يتطلب <العتاد>» بدلًا من ادعاءات غير مُتحقَّق منها

17. [minor] line 54
   quote: وينتهي كل شيء.
   problem: "done" became "ينتهي كل شيء", which reads as "everything comes to an end", an ominous tone.
   fix: ملف إعدادات واحد، وأمر واحد، وانتهى الأمر.

18. [minor] line 62
   quote: **اضبط ضبطًا دقيقًا نموذجًا بحجم 8B
   problem: Awkward word order. Also, line 11 uses bare "اضبط" for fine-tune while elsewhere "الضبط الدقيق" is used, which is inconsistent.
   fix: اضبط نموذجًا بحجم 8B ضبطًا دقيقًا على وحدة معالجة رسومية لحاسوب محمول بسعة 4 GB. (وفي السطر 11: اضبط نماذج اللغة الكبيرة ضبطًا دقيقًا)

19. [minor] line 403
   quote: وكل ما يُقرأ أفضل كمحادثة
   problem: Calqued from "everything that reads better as a conversation". Also "إجابة على Discord" (line 405) takes the wrong preposition, and "المسألة" is used for issue where line 405 keeps "Issues".
   fix: وكل ما يُفضَّل أن يكون حوارًا مباشرًا؛ ... فالإجابة في Discord تفيد شخصًا واحدًا، بينما يفيد البلاغ (Issue) كل من يواجه الأمر نفسه.

20. [minor] line 411
   quote: وهو يصل إلى الشخص نفسه وبديل مقبول.
   problem: Broken syntax. "وبديل مقبول" is coordinated to a pronoun clause, and "a fine fallback" is clumsy.
   fix: وهو يصل إلى الشخص نفسه، ويصلح بديلًا احتياطيًا عند الحاجة.

21. [minor] line 436
   quote: عيب صامت في التدرّجات الخاطئة، اكتُشف وأُصلح.
   problem: Clumsy construct for "a silent wrong-gradient defect". "المكتبة الأصلية" for "upstream library" is also not the usual term.
   fix: عيب صامت يُنتج تدرّجات خاطئة، اكتُشف وأُصلح. (وفي الجملة التالية: وقد حُدِّد السبب في المكتبة المصدرية (upstream) وأُبلغ عنه هناك)

22. [minor] line 439
   quote: بدلًا من نماذج لعبة من ثلاث طبقات
   problem: "toys" calqued literally as "نماذج لعبة".
   fix: بدلًا من نماذج تجريبية مبسّطة من ثلاث طبقات

23. [minor] line 103
   quote: والفحص محدود.
   problem: "the scan is bounded" is ambiguous: "محدود" reads as weak or limited. The intent is that it is capped in size. "escaping" as "تُنقّى" is also loose.
   fix: وتُهرَّب (escaping) أسماء المفاتيح قبل أن تصل إلى الطرفية، ويخضع الفحص لسقف أقصى للحجم

24. [minor] line 263
   quote: ومخططات الوصفات DAG
   problem: "مخططات" is used for schemas at lines 100 and 278, so using it for DAGs creates inconsistency and ambiguity.
   fix: ورسوم الوصفات الموجَّهة (DAG)

25. [minor] line 119
   quote: كان `training.loraplus_lr_ratio` يُسقط كل تشغيل يضبطه
   problem: "crashed" is rendered by "يُسقط" (drops or knocks down), which is imprecise. Line 118 "يُغلق القيد المعروف" is a calque of "closes".
   fix: كان training.loraplus_lr_ratio يتسبب في انهيار كل تشغيل يضبطه. (وفي السطر 118: يعالج القيد المعروف في v0.74.0)

26. [minor] line 68
   quote: وهو اختياري (`stream_layers: true`)
   problem: "Opt-in" is softened to "اختياري" (optional), losing the sense of explicit activation. Same at line 367 ("اختياري تمامًا", strictly opt-in).
   fix: وهو لا يُفعَّل إلا بطلب صريح (stream_layers: true) ولا يزال تجريبيًا (BETA). (وفي السطر 367: القياس عن بُعد لا يعمل إلا بموافقتك الصريحة)

27. [minor] line 168
   quote: وينفع الأمر نفسه
   problem: "ينفع" is colloquial and "الأمر نفسه" is vague for the venv alternative.
   fix: كما يفي بالغرض تنفيذ `python3 -m venv .venv && source .venv/bin/activate` ثم استخدام pip العادي.

28. [minor] line 447
   quote: هو معرّف DOI المفهومي
   problem: "concept DOI" is calqued as "المفهومي", which is unclear to readers.
   fix: هو معرّف DOI الشامل (Concept DOI) الذي يحيل دائمًا إلى أحدث إصدار

29. [nit] line 260
   quote: كواشف تحصين الحلقات
   problem: "loop-hardening detectors" is ambiguous. "الحلقات" evokes rings or circles rather than loops.
   fix: كواشف تحصين الحلقات التكرارية (loops) ضد الأعطال

30. [nit] line 64
   quote: القياس على RTX 3050 Laptop بسعة 4 GB:
   problem: A verbless noun phrase for "Measured on", which is stiff.
   fix: قِيس الأداء على RTX 3050 Laptop بسعة 4 GB:

31. [nit] line 98
   quote: كان v0.74 يحذّر وحدّد هذا الإصدار موعدًا نهائيًا.
   problem: Mixed imperfect and perfect verbs. "v0.74 warned and named this release as the deadline" would read more smoothly.
   fix: كان v0.74 يكتفي بالتحذير، وحدّد هذا الإصدار موعدًا نهائيًا.
