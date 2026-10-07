# Independent native review of README.ja.md (score 8/10)

This is a faithful, complete and mostly natural translation with no omitted sections, and its numbers and caveats are accurate. A handful of mistranslations (the "run an issue" instruction, "loop-hardening" rendered as 強化, "supply-chain controls" rendered as 管理, and an ambiguous "no model declares") plus recurring calques and punctuation inconsistencies should be fixed before publishing.

1. [major] line 385
   quote: の issue のいずれかを実行して数値を投稿することは
   problem: English 'running one of the help wanted issues' means running the benchmark/verification described in the issue. 'issue を実行する' is nonsensical in Japanese, so a contributor would not know what to do.
   fix: の issue のいずれかに書かれた検証を実行して、その数値を投稿していただくことは、GPU 時間に資金を提供するのと同じくらい助けになります。

2. [major] line 261
   quote: ループ強化検出器
   problem: 'loop-hardening' means making the loop robust (堅牢化). '強化' strongly evokes 強化学習 (reinforcement learning) in an ML document, so it misleads the reader.
   fix: ループ堅牢化の検出器

3. [major] line 248
   quote: どのモデルも宣言していないキー
   problem: 'A key no model declares' refers to the Pydantic schema models. In a fine-tuning README, 'モデル' reads as an LLM, which is confusing and wrong.
   fix: スキーマのどのモデル（Pydantic モデル）にも定義されていないキー

4. [major] line 267
   quote: サプライチェーン管理（scan/sign/BOM/attest/audit/airgap）
   problem: 'supply-chain controls' means security controls or safeguards. '管理' reads as supply-chain management (logistics), which is a false friend.
   fix: サプライチェーンの統制・対策（scan/sign/BOM/attest/audit/airgap）

5. [major] line 381
   quote: これらは、検証されていない主張ではなく、正直な「\<ハードウェア\>が必要」というゲートの背後で提供されています。
   problem: A literal calque. '正直なゲート' and 'ゲートの背後で提供' are unnatural, and the 'honest limits' point (state the hardware requirement instead of claiming without verification) is blurred.
   fix: これらの機能は、未検証のまま「動く」と主張するのではなく、「\<ハードウェア\>が必要」と明示するゲートを設けた状態で提供されています。

6. [major] line 107
   quote: MLX はライブ
  ダッシュボード、トラッカー、`soup ui` も駆動し
   problem: 'MLX also drives the live dashboard…' is rendered literally as 駆動. A native reader would not say a backend 'drives' a dashboard, so the sentence is unnatural and the meaning is unclear.
   fix: MLX での学習も、ライブダッシュボード、トラッカー、`soup ui` に反映されるようになり、

7. [major] line 437
   quote: サイレントな勾配誤りの欠陥を発見し、修正しました。
   problem: '勾配誤りの欠陥' is a stiff, awkward calque of 'silent wrong-gradient defect'.
   fix: 勾配が黙って誤った値になる不具合を発見し、修正しました。

8. [major] line 453
   quote: その数値の裏付けとなる測定記録はすべて
   problem: English says 'the measurement records behind every number in it (the paper)'. 'その数値' has no antecedent and drops 'every number in the paper'.
   fix: 論文中のすべての数値の裏付けとなる測定記録は、すべて [`benchmarks/`](benchmarks/) にあり、

9. [minor] line 376
   quote: メンテナーの登記事業者である **MePlay, Inc.**
   problem: '登記事業者' is an unnatural coinage for 'registered business'.
   fix: メンテナーが登記している事業体である **MePlay, Inc.**

10. [minor] line 109
   quote: 検証損失はどこにも存在しませんでした。
   problem: 'existed nowhere' is translated literally. The point is that it was never surfaced anywhere.
   fix: 検証損失は、どこにも現れていませんでした。

11. [minor] line 266
   quote: デプロイ自動操縦
   problem: Terminology inconsistency. 'autopilot' is rendered as 自動操縦 here, but as オートパイロット on line 269 and in the `soup autopilot` command.
   fix: デプロイのオートパイロット

12. [minor] line 264
   quote: Axolotl/LF 互換パイプライン
   problem: 'parity' means feature-equivalent, not 'compatible' (互換); the nuance is changed.
   fix: Axolotl/LF と同等機能のパイプライン

13. [minor] line 131
   quote: 最もきれいなインストール方法は、専用の環境を与えて
`soup` を `PATH` に置くことです。
   problem: 'きれいな' and '環境を与える' are calques of 'cleanest' and 'gives it its own environment'. The same '与える' recurs on line 168.
   fix: 最もすっきりしたインストール方法は、専用の環境を用意して `soup` を `PATH` に置くことです。

14. [minor] line 165
   quote: と出ましたか?
   problem: A half-width '?' is used in Japanese prose. A full-width '？' is conventional. The same applies to line 206 'お好みですか?'. Half-width colons ':' after Japanese text also recur (lines 62, 174, 190-style captions).
   fix: と表示されましたか？ / ブラウザのほうがお好みですか？（全角の「？」「：」に統一）

15. [minor] line 174
   quote: [理由と正確なエラー](docs/models.md#quoting-the-extra)
   problem: '正確なエラー' is a calque of 'the exact error'. It should mean the actual error message. Also 'これが理由です' is slightly off ('原因').
   fix: [原因と実際のエラーメッセージ](docs/models.md#quoting-the-extra)

16. [minor] line 245
   quote: 唯一の信頼できる情報源
   problem: The standard rendering of 'single source of truth' is 信頼できる唯一の情報源.
   fix: `config/schema.py` は、すべてのフィールドについての信頼できる唯一の情報源です。

17. [minor] line 403
   quote: Discord の回答が
助けるのは一人ですが、issue は同じことに遭遇するすべての人を助けます。
   problem: '助ける' with an inanimate subject is a calque ('helps one person').
   fix: Discord での回答が役立つのは一人だけですが、issue は同じ問題に遭遇するすべての人の役に立ちます。

18. [minor] line 405
   quote: [行動規範](CODE_OF_CONDUCT.md) はそこでも適用されます。
   problem: 'there too' becomes the ambiguous 'そこ'. It should refer to both Discord and Telegram.
   fix: [行動規範](CODE_OF_CONDUCT.md) は、Discord と Telegram でも同様に適用されます。

19. [minor] line 444
   quote: ZeRO-3 の八枚のカードは、常駐で学習する
  一枚のカードより遅い。
   problem: Register mismatch: a plain-form '遅い。' ends a bullet in an otherwise ですます document, and the mix of kanji and Arabic numerals is inconsistent (八枚, 一枚, 三層, 十項目 versus 32 層, 8 GB).
   fix: ZeRO-3 の 8 枚のカードは、常駐で学習する 1 枚のカードより遅い、という結果です。

20. [minor] line 441
   quote: 三層のおもちゃではなく
   problem: 'おもちゃ' alone is a bare calque of 'toys'. It also does not match the 層/レイヤー usage elsewhere.
   fix: 3 層だけのおもちゃのようなモデルではなく

21. [minor] line 443
   quote: 学習済みモデルの品質を初めて測定**し、常駐実行と区別がつきませんでした。
   problem: The subject is dropped, so it reads as if the measurer could not tell them apart. It should say the measured result is indistinguishable.
   fix: **学習済みモデルの品質を初めて測定**しました。結果は常駐実行と区別がつきませんでした。

22. [minor] line 449
   quote: 常に最新バージョン
（現時点では v3）に解決されます。
   problem: '解決される' is a calque of 'resolves to'. It is unnatural for a DOI.
   fix: 常に最新バージョン（現時点では v3）を指します。

23. [minor] line 437
   quote: 修正は、実際の 32B と 72B でのコントロールに対して
  ゲートされています。
   problem: 'ゲートされています' is a calque. 'controls' as control experiments is unclear in 'コントロール'.
   fix: 修正は、実際の 32B と 72B を対象とした対照実験で検証されており、これに合格しない限り取り込まれません。

24. [minor] line 80
   quote: ## なぜSoupなのか
   problem: Headings 'なぜSoupなのか', 'Soupを支援する' and 'Soupの引用' omit the spaces around Soup that the body text consistently uses ('Soup は'). The style is inconsistent.
   fix: ## なぜ Soup なのか / ## Soup を支援する / ## Soup の引用

25. [minor] line 62
   quote: レイヤーストリーミングは、凍結したベースモデルを
   problem: Terminology split: 'layer' is レイヤー (レイヤーストリーミング, レイヤーごと, レイヤーあたり) in some places and 層 (デコーダー層, 32 層, 三層) in others.
   fix: どちらかに統一する（例: 「レイヤー」に統一し、デコーダーレイヤー、32 レイヤー）

26. [minor] line 99
   quote: ルート階層の `lora:` の読み替え
   problem: 'root-level' is more naturally トップレベル. '読み替え' for 'remap' is acceptable but vague.
   fix: トップレベルの `lora:` を `training.lora` として扱う読み替え

27. [nit] line 77
   quote: 動画（90 秒）
   problem: 'Full video (90s)' loses 'Full'.
   fix: 動画の全編（90 秒）

28. [nit] line 54
   quote: LLM のファインチューニングの面倒をシンプルなワークフローに変えます。
   problem: 'pain' is softened to '面倒', and 'の…の' repeats.
   fix: LLM ファインチューニングのつらさを、シンプルなワークフローに変えます。

29. [nit] line 371
   quote: Soup のおかげで学習を一回分節約できたなら
   problem: '学習を一回分節約' is stiff for 'saved you a training run'.
   fix: Soup のおかげで学習の手間をひとつ省けたなら、

30. [nit] line 434
   quote: 元とはまったく異なるハードウェアでの再現
   problem: '元' is ambiguous (original what?).
   fix: 元の環境とはまったく異なるハードウェアでの再現
