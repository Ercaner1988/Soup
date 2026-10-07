# Independent native review of README.ru.md (score 7/10)

The translation is faithful and complete in substance, with accurate numbers, caveats and structure. It falls short of publish quality because of one untranslated heading, several calqued or ungrammatical sentences (notably in "Citing Soup") and a few places where the meaning drifted (the CPU-for-testing sentence, "причина названа", "с тем же результатом"). A native editor should do one more pass before release.

1. [major] line 91
   quote: ## What's New
   problem: Section heading left untranslated in an otherwise fully Russian document.
   fix: ## Что нового

2. [major] line 432
   quote: Что делает v3, так это **отзывает объяснение, которое мы опубликовали**
   problem: The calque of 'What v3 does is withdraw...' is ungrammatical in Russian ('так это' followed by a finite verb). The sentence also reads clumsily overall.
   fix: Название и главное утверждение не изменились — 8B на 4 GB, — и ни одно измеренное число не менялось со времён v1. Зато v3 **отзывает объяснение, которое мы публиковали раньше**, и это же самый короткий способ сказать, зачем нужна эта статья:

3. [major] line 342
   quote: Все задачи обучения для тестирования запускаются на CPU (квантизация отключается автоматически).
   problem: The meaning changed. The English says every training task CAN run on CPU for testing purposes. The Russian says that the tasks 'for testing' are run on CPU, which sounds like a fixed rule.
   fix: Для тестирования все задачи обучения можно запускать на CPU (квантизация при этом отключается автоматически).

4. [major] line 447
   quote: Причина названа в вышестоящей библиотеке и сообщена там
   problem: The English means the cause lies in an upstream library and was reported to it. 'Названа в' reads as 'mentioned in', and 'вышестоящая библиотека' is a calque of 'upstream'.
   fix: Причина оказалась в одной из библиотек, от которых зависит Soup (апстрим), и о ней сообщено её авторам; исправление проверено на контрольных запусках на реальных моделях 32B и 72B.

5. [major] line 256
   quote: так что запуск продолжался с тем же результатом: настройка просто не применялась
   problem: 'С тем же результатом' is invented and obscures the point. The original says the run proceeded and the setting was simply not applied.
   fix: раньше проходил проверку и молча отбрасывался: запуск продолжался, а настройка просто не применялась.

6. [major] line 254
   quote: Ключ, который не объявлен ни в одной модели
   problem: In an LLM README 'модель' means an ML model. The English 'no model declares' refers to the Pydantic schema models, so this is misleading.
   fix: Ключ, который не объявлен ни в одной модели схемы (Pydantic)

7. [major] line 414
   quote: относится в Issues или Discussions
   problem: Ungrammatical: 'относится в' is wrong for 'belongs in'. The preceding clause ('находимым', 'должно оставаться') is also stiff.
   fix: Всё, что должно остаться доступным для поиска и через полгода, оставляйте в Issues или Discussions: ответ в Discord помогает одному человеку, а issue — всем, кто столкнётся с тем же.

8. [major] line 63
   quote: Дообучите модель на 8B на ноутбучной GPU с 4 GB.
   problem: 'Ноутбучная GPU' is slangy and stiff. '4 GB' is ambiguous (RAM or VRAM), and 'модель на 8B' is a stylistic slip. The phrase recurs in lines 44, 424, 77 and 78.
   fix: Дообучите модель с 8B параметров на видеокарте ноутбука с 4 GB VRAM.

9. [major] line 270
   quote: градиентные чекпойнты
   problem: 'Gradient checkpointing' is a technique (recomputing activations). 'Градиентные чекпойнты' suggests saved checkpoints of gradients.
   fix: градиентное чекпойнтирование (gradient checkpointing)

10. [major] line 272
   quote: | [Оценка и пробы](docs/evaluation.md) |
   problem: 'Пробы' means 'samples' or 'trial runs' in Russian, not ML probes. The 'Дизайн и гейт оценки' and 'обучение с оценочным гейтом' wording in the same row is also a stiff calque.
   fix: [Оценка и зондирование (probes)] — в столбце: проектирование оценки и гейт, обучение с гейтом по метрикам оценки, бенчмарки, ..., посттренировочное «рентгеновское» зондирование модели, ...

11. [major] line 113
   quote: **Потери на валидации не существовали нигде.**
   problem: A calque of 'existed nowhere' that sounds absurd. 'Потери на валидации' is also non-idiomatic for validation loss.
   fix: **Валидационный лосс нигде не сохранялся.** Он вычислялся на каждом бэкенде и выбрасывался: ни столбца в метриках, ни поля в событии, ничего на панели. Теперь он записывается, передаётся потоком и отображается.

12. [major] line 390
   quote: Они поставляются за честными барьерами «требуется \<оборудование\>», а не с непроверенными заявлениями
   problem: The 'honest gates' wording is a literal translation and sounds odd ('поставляются за барьерами'). The 'honest limits' tone is lost.
   fix: Эти задачи честно помечены ограничением «требуется \<оборудование\>» и не сопровождаются непроверенными заявлениями, так что если у вас есть доступ к машине помощнее или неиспользуемые GPU-кредиты, ...

13. [major] line 98
   quote: **Ломающее изменение: неизвестный ключ конфигурации теперь прерывает загрузку.**
   problem: 'Ломающее изменение' is a calque of 'Breaking change'. The standard term is 'несовместимое изменение'. The same applies at line 116.
   fix: **Несовместимое изменение: неизвестный ключ конфигурации теперь прерывает загрузку.**

14. [minor] line 99
   quote: раньше отбрасывался, а запуск продолжался без применения настройки; теперь он завершается ошибкой
   problem: The pronoun 'он' is ambiguous (the run or the key). The original says the load is refused.
   fix: раньше молча отбрасывался, а запуск продолжался без применения настройки; теперь загрузка конфигурации завершается ошибкой в CLI (код выхода 1) и в API (`ValueError`)

15. [minor] line 175
   quote: потому что эти файлы ведёт и `apt`
   problem: 'Ведёт' is wrong in this sense (colloquial or incorrect). The English is 'manages'.
   fix: потому что этими файлами управляет и `apt`

16. [minor] line 93
   quote: Шесть обучающих опций проходили проверку, были описаны в документации, принимались — и ничем не читались на этом бэкенде.
   problem: 'Ничем не читались' is a stiff calque of 'read by nothing'.
   fix: Шесть обучающих опций проходили проверку, были описаны в документации, принимались — но этот бэкенд их попросту не читал.

17. [minor] line 447
   quote: Тихий дефект с неверным градиентом найден и исправлен.
   problem: 'Тихий' is a calque of 'silent' (as in 'silent bug'). 'Скрытый' or 'молчаливый' is better.
   fix: Найден и исправлен скрытый дефект: градиенты вычислялись неверно, и никаких сигналов об этом не было.

18. [minor] line 353
   quote: Сборки CUDA, несовпадения версий:
   problem: 'CUDA wheels' means the pip packages (wheels) built with CUDA. 'Сборки CUDA' is misleading.
   fix: Wheel-пакеты с CUDA, несовместимость версий:

19. [minor] line 268
   quote: детекторы зацикливания
   problem: 'Loop-hardening detectors' means hardening against loops, not just detecting them. Also 'зрение' alone is not natural.
   fix: детекторы и защита от зацикливания; мультимодальность (изображения/аудио/TTS)

20. [minor] line 271
   quote: конвейер с паритетом Axolotl/LF
   problem: Stiff calque of 'parity pipeline'.
   fix: конвейер, совместимый по возможностям с Axolotl/LF

21. [minor] line 274
   quote: [Адаптеры, реестр и governance]
   problem: 'Governance' is left in English in the heading and the table, along with 'steering', and in line 275 next to 'комплаенс', which is also a loanword. The terminology is inconsistent.
   fix: [Адаптеры, реестр и управление (governance)]; ... управление активациями (steering) ...

22. [minor] line 289
   quote: ## Основные команды
   problem: 'Common' means 'frequently used', not 'main'. This shifts the meaning slightly.
   fix: ## Часто используемые команды

23. [minor] line 404
   quote: ## Связь
   problem: The heading is bare and less natural as a section title. 'Contact' is normally 'Контакты' or 'Связаться с нами'.
   fix: ## Контакты

24. [minor] line 65
   quote: при котором модель целиком лежит в памяти
   problem: 'Resident' means entirely in VRAM. 'В памяти' is ambiguous, since the streamed variant keeps the model in host RAM. The same applies at lines 426, 453 and 455.
   fix: при котором модель целиком находится в видеопамяти

25. [minor] line 436
   quote: ([запись](benchmarks/probe-v0.73.0-what-bounds-streaming.md))
   problem: 'The record' here means the measurement record or log. The bare label 'запись' reads as a recording or entry.
   fix: ([протокол измерения](benchmarks/probe-v0.73.0-what-bounds-streaming.md))

26. [minor] line 439
   quote: сам шаг выполняется на **71.3%** от потолка GEMM
   problem: 'Runs at X% of ceiling' is calqued ('на ... от').
   fix: сам шаг достигает **71.3%** потолка GEMM этой же карты в той же сессии

27. [minor] line 106
   quote: а сам перебор ограничен по объёму
   problem: 'Scan is bounded' is rendered unnaturally. 'Перебор' implies brute-force enumeration.
   fix: а сам проход по ключам ограничен по объёму

28. [minor] line 414
   quote: issue — всем
   problem: Terminology is inconsistent: 'issue' is rendered as 'задача' (lines 69, 77, 393) and as 'трекер задач' (407), but left as 'issue' and 'Issues' here.
   fix: Use one term throughout, for example 'issue (задача)' on first use and then consistently 'issue' or 'задача'.

29. [nit] line 283
   quote: все они автоматически определяются в JSONL, JSON, CSV, Parquet или TXT
   problem: Wrong preposition. Formats are detected from the file, not 'in' it.
   fix: все они определяются автоматически в файлах JSONL, JSON, CSV, Parquet или TXT

30. [nit] line 83
   quote: 30-50% времени
   problem: A range should use an en dash. The decimal separator in Russian is a comma, although the dot is tolerable in technical text such as '3.32 GB', which is used consistently.
   fix: 30–50 % времени
