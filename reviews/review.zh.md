# Independent native review of README.zh.md (score 8/10)

The translation is faithful and numerically exact. I found no omissions, softened caveats, or changed figures, and it reads fluently in most places. It is not quite publishable: one heading is still in English, one hardware-gate sentence has garbled logic, and a few terminology choices (自动驾驶, 遗忘学习, 对标) would strike a native developer as wrong or odd.

1. [major] line 380
   quote: 推动这些事项的另一种方式是提供**硬件本身**。它们之所以设置了如实的
“需要 \<硬件\>”门槛，而不是给出未经验证的说法，正是因为如此。所以，如果你能用上配置更高的
机器
   problem: The English says these items ship behind honest 'requires <hardware>' gates instead of unverified claims, and therefore hardware helps. The Chinese turns this into a confusing causal clause ('之所以…正是因为如此') with an unclear antecedent, so the logic is garbled.
   fix: 想推动这些事项，另一个办法是提供**硬件本身**。这些事项都带有如实标注的“需要 \<硬件\>”门槛，而不是未经验证的说法。因此，如果你能用上配置更高的机器，或有闲置的 GPU 额度，……

2. [major] line 90
   quote: ## What's New
   problem: Section heading left in English although the whole page is translated. It is the only prose heading not translated.
   fix: ## 最新动态

3. [major] line 264
   quote: 部署自动驾驶
   problem: 'deploy autopilot' is rendered as 自动驾驶, which to a Chinese reader means self-driving cars. It is also inconsistent with line 267, where 'autopilot' stays in English, and with the command `soup autopilot`.
   fix: 部署 autopilot（自动部署）

4. [minor] line 259
   quote: 遗忘学习（unlearning）
   problem: '遗忘学习' is not the established term. The standard Chinese term for unlearning in ML is 机器遗忘.
   fix: 机器遗忘（unlearning）

5. [minor] line 262
   quote: 对标 Axolotl/LF 的流水线
   problem: 'parity' is mistranslated. 对标 means 'benchmark against', not 'feature-equivalent to'.
   fix: 与 Axolotl/LF 功能对齐的流水线

6. [minor] line 108
   quote: 验证损失此前根本不存在。它在每个后端上都会被计算出来，然后被丢掉
   problem: A literal rendering of 'existed nowhere'. It contradicts the next sentence, which says the loss was computed. The intended meaning is that it was never surfaced.
   fix: 验证损失此前无处可见。每个后端都会计算它，随后又把它丢弃：

7. [minor] line 103
   quote: MLX 现在会遵循它所接受的配置。
   problem: '遵循' is a calque of 'honours' and sounds stiff for a config. 'Accepted' also reads oddly.
   fix: MLX 现在会真正按配置执行。

8. [minor] line 92
   quote: 却在该后端上无人读取
   problem: Calque of 'read by nothing'. A native would not say 无人读取 for a code path.
   fix: 却在该后端上没有任何代码读取

9. [minor] line 436
   quote: 发现并修复了一个静默的梯度错误缺陷。
   problem: '静默的梯度错误缺陷' is clunky, with stacked nouns. It is a literal rendering of 'silent wrong-gradient defect'.
   fix: 发现并修复了一个会悄无声息地产生错误梯度的缺陷。

10. [minor] line 449
   quote: 上述撤回之所以作为新版本发布，正是为了让我们何时声称了什么的
记录保持完整。
   problem: The nominalised clause '我们何时声称了什么的记录' is awkward and hard to parse.
   fix: 上述撤回之所以以新版本的形式发布，正是为了让“我们在何时主张过什么”这份记录保持完整。

11. [minor] line 366
   quote: 它在公开环境中构建和维护，
靠的只是一台 4 GB 的笔记本，因此这些文档中的每一个性能数字都是实测得出，
而非自说自话。
   problem: 'in the open' is rendered as 公开环境, which is unnatural. '自说自话' is colloquial and mildly pejorative, a mismatch for 'claimed'.
   fix: 它以公开透明的方式开发和维护，只用了一台 4 GB 的笔记本，因此这些文档中的每个性能数字都是实测得出的，而非空口宣称。

12. [minor] line 362
   quote: 遥测严格采用选择加入的方式（`SOUP_TELEMETRY=1`，默认关闭
   problem: '选择加入' is a calque of 'opt-in'. Chinese docs usually say that the feature is off by default and must be enabled by the user.
   fix: 遥测完全由用户主动开启（`SOUP_TELEMETRY=1`，默认关闭

13. [minor] line 401
   quote: 以及一切更适合当面聊的事情
   problem: 'reads better as a conversation' became '当面聊', which implies face-to-face talk. An online chat is meant.
   fix: 以及一切更适合边聊边解决的问题

14. [minor] line 405
   quote: [行为准则](CODE_OF_CONDUCT.md)在那里同样适用。
   problem: '在那里' has an unclear referent (Discord and Telegram).
   fix: [行为准则](CODE_OF_CONDUCT.md)在这些渠道同样适用。

15. [minor] line 116
   quote: 另外修复了：设置 `training.loraplus_lr_ratio`
会导致每次运行崩溃，以及 `packing: true` 在 TRL 0.29 上抛出异常的问题。
   problem: The sentence structure is lopsided: '修复了：A，以及 B 的问题'. The list items are not parallel.
   fix: 另外还修复了两个问题：设置 `training.loraplus_lr_ratio` 会导致每次运行崩溃；`packing: true` 在 TRL 0.29 上会抛出异常。

16. [minor] line 246
   quote: 没有任何模型声明过的键
   problem: '模型' is ambiguous here and reads as an ML model. It means the Pydantic config model.
   fix: 没有任何配置模型声明过的键

17. [minor] line 264
   quote: 批量推理、基准测试、合并/导出
   problem: '基准测试' translates both 'benchmarking' (here) and 'benchmarks' (line 263), so the term is used inconsistently.
   fix: 批量推理、性能压测、合并/导出（line 263 keeps 基准测试 for 'benchmarks'）

18. [minor] line 318
   quote: 每次发布都会把镜像发布到 GHCR
   problem: Repeated '发布' in the same clause is clumsy.
   fix: 每个版本发布时都会同步推送镜像到 GHCR

19. [minor] line 113
   quote: 使用短期有效、一次性的 ticket，
不再把 token 放在查询字符串中
   problem: 'ticket' is left in English while related concepts are translated, so it is inconsistent. The sentence is also run-on.
   fix: 改用短期有效、仅可使用一次的票据（ticket），不再把 token 放在查询字符串中

20. [nit] line 106
   quote: tracker
   problem: 'Tracker' is left in English, while 'experiment tracking' is translated 实验追踪 on line 267.
   fix: 实验追踪器

21. [nit] line 377
   quote: 捐款将用于购买 GPU 算力，投入那些受硬件限制的工作
   problem: '捐款' is used here but 捐赠 is used elsewhere. '投入' is slightly awkward after '购买'.
   fix: 捐赠将用于购买 GPU 算力，推进那些受硬件限制的工作

22. [nit] line 414
   quote: 已在一篇预印本中详细阐述
   problem: '详细' is added. The source says only 'is described'.
   fix: 已在一篇预印本中加以阐述

23. [nit] line 66
   quote: （这两个数字均在 v0.72.2 上测得，早于 v0.73.0 的正确性修复（该修复在 32B 上带来 −4.8% 的开销）；
   problem: Nested full-width parentheses plus a sentence-final period inside the outer pair make the aside heavy to read. The English is similarly dense but easier to parse.
   fix: （这两个数字均在 v0.72.2 上测得，早于 v0.73.0 的正确性修复，而该修复在 32B 上带来了 −4.8% 的开销；

24. [nit] line 204
   quote: 涵盖实验管理、
训练设置
   problem: 'experiments' became 实验管理, which adds 'management' not in the source.
   fix: 涵盖实验、训练设置、实时指标、数据集浏览和模型对话。
