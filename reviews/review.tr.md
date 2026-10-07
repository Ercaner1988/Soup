# Independent native review of README.tr.md (score 7/10)

The translation is complete and faithful: I found no omitted caveats, changed numbers or softened "honest limits" wording, and most prose reads fluently. It is held back by a handful of false friends (issue rendered as "sayı", Serving as "Sunum", tutorial as "eğitim", wheel as "tekerlek"), a few calqued neologisms, and inconsistent terminology, so it needs one targeted polish pass before publishing.

1. [major] line 68
   quote: yeniden ölçüm [#361](https://github.com/MakazhanAlpamys/Soup/issues/361)
sayısında bekliyor
   problem: "issue" is rendered as "sayı" (number/count), a false friend that makes the sentence confusing. The same error recurs on lines 77, 78 and 446. Elsewhere the same word is "konu" (393) and "sorun takipçisi" (406), while 412-413 keep "Issues"/"issue", so the file is inconsistent. Use the GitHub term "issue" everywhere.
   fix: yeniden ölçüm [#361](https://github.com/MakazhanAlpamys/Soup/issues/361) numaralı issue'da bekliyor

2. [major] line 272
   quote: [Sunum ve dışa aktarma](docs/serving-and-export.md)
   problem: "Serving" is translated as "Sunum", which means a presentation or slide deck in Turkish, not serving a model. The link label is misleading.
   fix: [Model servisi ve dışa aktarma](docs/serving-and-export.md)

3. [major] line 178
   quote: eski bir eğitimden kopyaladıysanız
   problem: "tutorial" is rendered as "eğitim", which means training or education here and gives the wrong meaning.
   fix: eski bir öğreticiden (tutorial) kopyaladıysanız

4. [major] line 450
   quote: onarım, gerçek 32B
  ve 72B üzerinde kontrollere karşı kapılandı.
   problem: "kapılandı" is an invented verb that does not exist in Turkish. "gated against controls" is not conveyed.
   fix: onarım, gerçek 32B ve 72B modellerde kontrol çalıştırmalarına karşı doğrulama kapısından geçirildi.

5. [major] line 128
   quote: yerel
> eklentide çöken, test edilmemiş PyTorch tekerleklerini çözümlüyordu
   problem: "wheels" is translated literally as "tekerlekler" (physical wheels). Developers say "wheel paketleri". The same issue is on line 352 ("CUDA tekerlekleri"). Also "eklenti" means plugin, which clashes with "native extension" and with "eklentiler" (plugins) on line 275.
   fix: pip'in, Soup daha hiç çalışmadan yerel (native) uzantıda çöken, test edilmemiş PyTorch wheel paketlerini seçtiği görülüyordu

6. [major] line 111
   quote: MLX ayrıca canlı panoyu, izleyiciyi ve `soup ui`'yi
  sürüyor
   problem: "tracker" (experiment tracker) is rendered as "izleyici" (viewer or watcher). "drives" is calqued as "sürüyor". The meaning is unclear to a native reader.
   fix: MLX artık canlı panoyu, deney takipçisini ve `soup ui`'yi de besliyor

7. [major] line 123
   quote: her tercih eğiticisi ölüydü
   problem: "trainer" is rendered as "eğitici" (an instructor) and "dead" is calqued as "ölüydü". The sentence is also stiff and the tenses shift ("içe aktarılamıyor").
   fix: 2.5.1'de `trl>=0.29` içe aktarılamıyordu ve hiçbir tercih trainer'ı çalışmıyordu

8. [major] line 98
   quote: **Kırıcı değişiklik: bilinmeyen
   problem: "Breaking" is rendered as "Kırıcı" here but as "Geriye dönük uyumsuz" on line 115, so the term is inconsistent. "Kırıcı değişiklik" is a calque.
   fix: **Geriye dönük uyumsuz değişiklik: bilinmeyen bir yapılandırma anahtarı artık yüklemeyi reddediyor.**

9. [major] line 284
   quote: Her biçim için çalışılmış bir örnekle şemalar
   problem: "worked example" is calqued as "çalışılmış örnek", which is not idiomatic. "belge alımı" for "document ingestion" is also odd ("alım" means purchase or intake).
   fix: Her biçim için adım adım çözümlü bir örnekle şemalar ve veri ardışık düzeni (uzak URI'ler, akış, parçalama, iç içe geçirme, sözcük dağarcığı genişletme, belge içe aktarma)

10. [major] line 269
   quote: kayıt biçimleri
   problem: "save formats" is rendered as "kayıt biçimleri", which reads as record or registry formats. "kayıt defteri" is used for registry on line 273. "gradyan denetim noktası" is also unusual for gradient checkpointing.
   fix: kaydetme biçimleri, Cut Cross-Entropy, gradyan checkpointing'i (kontrol noktası)

11. [major] line 11
   quote: LLM'lere tek komutla ince ayar ve sonradan eğitim uygulayın.
   problem: "post-train" is rendered as "sonradan eğitim", which is unnatural. Line 271 uses "eğitim sonrası" for the same concept.
   fix: LLM'lere tek komutla ince ayar ve eğitim sonrası (post-training) uygulayın. SSH yok, yapılandırma cehennemi yok.

12. [major] line 113
   quote: Doğrulama kaybı hiçbir yerde yoktu. Her arka uçta hesaplanıp atılıyordu
   problem: "yoktu" (did not exist) directly contradicts the next sentence, which says it was computed. Also "akıtılıyor" for "streamed" is odd.
   fix: Doğrulama kaybı hiçbir yerde görünmüyordu. Her arka uçta hesaplanıp atılıyordu: metrik sütunu yok, olay alanı yok, panoda hiçbir şey yok. Artık kaydediliyor, canlı aktarılıyor ve gösteriliyor.

13. [major] line 73
   quote: (işlemi 4 GB ile
sınırlar
   problem: "process" is rendered as "işlem" (transaction or operation) instead of "süreç". The same term is "alt süreç" on line 122.
   fix: (süreci 4 GB ile sınırlar, ardından akışlı bir modelin normal bir modelle bit düzeyinde özdeş olduğunu doğrular)

14. [minor] line 62
   quote: **119.6 tok/s, 3.32 GB tepe**
   problem: Numbers use the English decimal point (119.6, 3.32, 113.00, %0.20, %71.3). Turkish uses a decimal comma, and a dot can be read as a thousands separator. This applies throughout lines 62-78 and 435-446.
   fix: **119,6 tok/s, 3,32 GB tepe**; %0,20; %71,3; %9,8

15. [minor] line 66
   quote: 32B'de −%4.8'e mal olan v0.73.0 doğruluk
onarımından önce
   problem: "−%4.8'e mal olan" is awkward, since "mal olmak" with a negative percent is confusing. "doğruluk onarımı" is ambiguous with accuracy (correctness is meant). The sentence is also very long.
   fix: (Her iki rakam da 32B'de %4,8 yavaşlamaya yol açan v0.73.0 sonuç-doğruluğu onarımından önce, v0.72.2'de ölçüldü.)

16. [minor] line 78
   quote: toplu iş 1, dizi 512
   problem: "batch" is rendered as "toplu iş" and the labels are missing, which reads stiff. Line 88 has "Toplu iş boyutu".
   fix: batch boyutu 1, dizi uzunluğu 512

17. [minor] line 102
   quote: Tespit edici,
  şemanın v0.40.1'den beri desteklediği
   problem: "The detector" is rendered as "Tespit edici", which is stiff. "dedektör" on line 267 is a third rendering. "yoksayılıyor" on line 100 should be written "yok sayılıyor" (line 255 uses "göz ardı").
   fix: Algılama adımı, şemanın v0.40.1'den beri desteklediği kök düzeyindeki `lora:` yeniden eşlemesini uyguluyor; yani bu yazım reddedilmiyor, kabul ediliyor.

18. [minor] line 99
   quote: v0.74 uyarmış ve son tarih olarak bu sürümü belirlemişti.
   problem: "uyarmış ... belirlemişti" mixes the evidential ("-mış") and past perfect ("-mıştı") in a way that reads wrong.
   fix: v0.74 uyarı vermiş ve son tarih olarak bu sürümü açıklamıştı.

19. [minor] line 115
   quote: yayımlanmış dizi düzeyi hedef fonksiyonudur**
  (arXiv:2507.18071); bir dolgu belirtecinin
   problem: "objective" is rendered as "hedef fonksiyonu" (the standard term is "amaç fonksiyonu"). "sezgisel" for "heuristic" needs "yöntem". "yeniden üretmeyecek" should be "yeniden üretemeyecek" (will not be able to).
   fix: `grpo_variant: gspo` artık yayımlanmış dizi düzeyi amaç fonksiyonudur (arXiv:2507.18071); bir dolgu belirtecinin aynı sütunu paylaşan her satırın gradyanını da kaydırdığı sütun merkezleme sezgisel yönteminin yerini alıyor. Mevcut gspo yapılandırmaları önceki çalıştırmaları yeniden üretemeyecek.

20. [minor] line 107
   quote: **MLX, kabul ettiği yapılandırmaya uyuyor.**
   problem: The sense of "honours" (now actually applies) is weak. "uyuyor" suggests conformity rather than applying the settings.
   fix: **MLX artık kabul ettiği yapılandırmayı gerçekten uyguluyor.**

21. [minor] line 273
   quote: [Bağdaştırıcılar, kayıt defteri ve yönetişim]
   problem: "Adapters" is rendered as "Bağdaştırıcılar", which is unnatural for developers. "Adaptör" is the common term in ML. The same applies in the same cell ("Bağdaştırıcı yaşam döngüsü"). "supply-chain controls" as "denetimleri" blurs with "audit".
   fix: [Adaptörler, model kayıt defteri ve yönetişim] ... Adaptör yaşam döngüsü/yönetimi ... tedarik zinciri kontrolleri (scan/sign/BOM/attest/audit/airgap)

22. [minor] line 267
   quote: görü/ses/TTS, unutturma, RAFT/RA-DIT, döngü sağlamlaştırma dedektörleri
   problem: "görü" (vision) is archaic or unnatural, and appears again on lines 281 and 322. "unutturma" and "döngü sağlamlaştırma dedektörleri" are literal. "dedektör" is not used consistently.
   fix: görsel/ses/TTS, unlearning (öğrenileni silme), RAFT/RA-DIT, döngü sertleştirme algılayıcıları

23. [minor] line 268
   quote: optimizer ve PEFT koleksiyonu
   problem: "zoo" is rendered as "koleksiyonu", which loses the sense of a large variety.
   fix: optimizer ve PEFT çeşitliliği

24. [minor] line 275
   quote: tamamlamalar, eklentiler, yardımcı komutlar
   problem: "completions" (shell completions) is rendered as "tamamlamalar", which is meaningless alone. "Ekler" for pip extras (277, 343) is also ambiguous next to "eklentiler" (plugins).
   fix: kabuk otomatik tamamlama, eklentiler (plugin), yardımcı komutlar; ve "pip ekleri" yerine "pip isteğe bağlı bağımlılık grupları (extras)"

25. [minor] line 211
   quote: canlı ölçümler
   problem: "metrics" is rendered as "ölçümler" (measurements), the same word used for "measurements" on line 72. "NLG ölçütleri" on line 271 is a third rendering. Terminology is inconsistent.
   fix: canlı metrikler (and likewise "NLG metrikleri")

26. [minor] line 369
   quote: Telemetri kesinlikle isteğe bağlıdır
   problem: "strictly opt-in" means off unless you explicitly enable it. "kesinlikle isteğe bağlı" is vague, since "isteğe bağlı" can also mean on by default but can be turned off.
   fix: Telemetri yalnızca siz açıkça etkinleştirirseniz çalışır (`SOUP_TELEMETRY=1`, varsayılan olarak kapalı;

27. [minor] line 410
   quote: sohbet olarak daha iyi okunan her şey
   problem: "everything that reads better as a conversation" is calqued. "sohbet olarak okunan" is unnatural.
   fix: Canlı sohbet, kurulum yardımı ve karşılıklı konuşarak çözülmesi daha kolay olan her şey için

28. [minor] line 375
   quote: açık
  olarak geliştirilir ve sürdürülür
   problem: "in the open" is rendered as "açık olarak", which is ambiguous. It reads like "openly" in a vague sense, not "publicly, in an open-source way".
   fix: herkesin gözü önünde, açık kaynak olarak geliştirilir ve sürdürülür

29. [minor] line 379
   quote: en çok yardımı sağlar
   problem: "helps most" is rendered as "yardımı sağlar", which is stiff.
   fix: en çok işe yarar ve hiçbir maliyeti yoktur

30. [minor] line 447
   quote: üst akış kütüphanesinde
   problem: "upstream" is calqued as "üst akış". Developers say "upstream" or "kaynak (upstream) kütüphane". "oyuncaklar" (451) for "toys" is also too literal.
   fix: Neden, upstream kütüphanede adıyla belirtildi ve orada bildirildi ... üç katmanlı oyuncak modeller yerine

31. [nit] line 253
   quote: eskiden şemadan geçip göz ardı ediliyordu ... raporluyordu
   problem: "validate clean and be discarded" loses "clean". "raporluyordu" is colloquial.
   fix: eskiden şema doğrulamasından sorunsuz geçip atılıyordu ... v0.74 bunu yükleme anında, muhtemelen kastettiğiniz alanı belirterek bildiriyordu

32. [nit] line 399
   quote: Topluluk tarafından inşa edildi
   problem: "Built by the community" as "inşa edildi" is stiff for software.
   fix: Topluluk tarafından geliştirildi ❤️

33. [nit] line 88
   quote: niceleme
   problem: "quantization" is rendered as "niceleme" throughout. The more common term in Turkish ML writing is "nicemleme". Not an error, but worth a deliberate decision.
   fix: nicemleme (or consistently keep "quantization")
